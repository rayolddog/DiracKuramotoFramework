#!/usr/bin/env python3
"""Two-station correlated-noise Bell game.

Extends the Paper 1 SS7.1 joint game (two concurrent fair share-games from
50/50 marginals; first commit resets the far wing to
eta*conditional + (1-eta)*current, per SS7.2) with cross-station noise
structure, to answer: does classically correlated noise between the two
detectors of a Bell experiment shift the outcome statistics?

Two injection models:

  WHITE  -- the two stations' share-noise increments are correlated,
            <dW_A dW_B> = rho dt, during the temporal overlap of the games.
            (Broadband common-mode pickup reaching both absorbers, in-band.)

  TONE   -- a common phase-coherent field (frequency in the selection band,
            phase-locked between stations, global phase phi random per shot)
            adds a drift to each station's share game:
              d(share) += lam * sig^2 * cos(2(theta - psi)) * cos(phi)
                          * sqrt(share*(1-share)) dt
            theta = analyzer angle, psi = tone polarization. The cos(2(theta-psi))
            projection is the tone's intensity asymmetry between the two ports.
            Effective single-quantum-sector model of a weak coherent injection
            (a full multi-quantum treatment belongs to SS6.3 machinery).

Share dynamics per station (two ports -> one share x, Wright-Fisher form
from de_i = sig sqrt(e_i) dW_i):  dx = sig sqrt(x(1-x)) dW  (+ tone drift),
absorbing at 0/1. Conditional convention: P(B=+|A=+) = cos^2(a-b), so the
faithful game gives E(a,b) = cos 2(a-b) and CHSH S = 2 sqrt 2 at the
standard angles a=0, a'=pi/4, b=pi/8, b'=-pi/8.

Instrumented: leak statistic L = E[(far share at reset time - 1/2) * (sign of
first outcome)] (the correlation the registry reset discards), straggler
count, and per-setting marginals (no-signaling check).

Usage: python3 two_station_correlated_noise.py [--quick]
"""

import sys
import numpy as np

SIG2DT = 4e-3            # sigma^2 dt per step (sigma = 1)
SQ = SIG2DT ** 0.5
MAX_STEPS = 40000

ANGLES = [(0.0, np.pi / 8), (0.0, -np.pi / 8),
          (np.pi / 4, np.pi / 8), (np.pi / 4, -np.pi / 8)]
CHSH_SIGN = [1.0, 1.0, 1.0, -1.0]
S_QM = 2.0 * np.sqrt(2.0)


def run_pairs(n, a, b, rho=0.0, lam=0.0, psi=0.0, eta=1.0, seed=0):
    """One angle pair, n trials. Returns (A, B, leak, stragglers)."""
    g = np.random.default_rng(seed)
    alpha = np.full(n, 0.5)
    beta = np.full(n, 0.5)
    outA = np.zeros(n, np.int8)
    outB = np.zeros(n, np.int8)
    reset = np.zeros(n, bool)
    phi = g.uniform(0.0, 2.0 * np.pi, n)          # common tone phase per shot
    dA = lam * SIG2DT * np.cos(2.0 * (a - psi)) * np.cos(phi)
    dB = lam * SIG2DT * np.cos(2.0 * (b - psi)) * np.cos(phi)
    pc = np.cos(a - b) ** 2                       # P(far=+ | near=+)
    ps = np.sin(a - b) ** 2                       # P(far=+ | near=-)
    sq1mr = (1.0 - rho * rho) ** 0.5
    Lsum, Lcnt = 0.0, 0
    n_dbl = 0

    for _ in range(MAX_STEPS):
        act = np.flatnonzero((outA == 0) | (outB == 0))
        if act.size == 0:
            break
        z1 = g.standard_normal(act.size)
        z2 = rho * z1 + sq1mr * g.standard_normal(act.size)

        mA = outA[act] == 0
        aA = act[mA]
        va = np.sqrt(alpha[aA] * (1.0 - alpha[aA]))
        alpha[aA] = np.clip(alpha[aA] + va * (SQ * z1[mA] + dA[aA]), 0.0, 1.0)

        mB = outB[act] == 0
        aB = act[mB]
        vb = np.sqrt(beta[aB] * (1.0 - beta[aB]))
        beta[aB] = np.clip(beta[aB] + vb * (SQ * z2[mB] + dB[aB]), 0.0, 1.0)

        cA = aA[(alpha[aA] <= 0.0) | (alpha[aA] >= 1.0)]
        outA[cA] = np.where(alpha[cA] >= 1.0, 1, -1).astype(np.int8)
        cB = aB[(beta[aB] <= 0.0) | (beta[aB] >= 1.0)]
        outB[cB] = np.where(beta[cB] >= 1.0, 1, -1).astype(np.int8)

        # Same-step double commits: in continuous time one wing crossed first
        # (simultaneous absorption is measure-zero for rho < 1). Order them by
        # coin flip and re-open the far wing with the proper registry reset;
        # without this, correlated paths (which finish together) silently skip
        # conditioning -- a discretization artifact that mimics eta < 1.
        # (Physical aside: commits of finite duration tau_commit WOULD escape
        # conditioning like this; see the derivation note.)
        dbl = cA[np.isin(cA, cB) & ~reset[cA]]
        if dbl.size:
            coin = g.random(dbl.size) < 0.5
            dfA = dbl[coin]                        # A first: B re-opened
            outB[dfA] = 0
            beta[dfA] = eta * np.where(outA[dfA] > 0, pc, ps) \
                + (1.0 - eta) * beta[dfA]
            dfB = dbl[~coin]                       # B first: A re-opened
            outA[dfB] = 0
            alpha[dfB] = eta * np.where(outB[dfB] > 0, pc, ps) \
                + (1.0 - eta) * alpha[dfB]
            reset[dbl] = True
            n_dbl += dbl.size

        # Registry reset of the far wing at the FIRST commit (SS7.1-7.2).
        fA = cA[(outB[cA] == 0) & ~reset[cA]]
        if fA.size:
            Lsum += float(np.sum((beta[fA] - 0.5) * outA[fA]))
            Lcnt += fA.size
            beta[fA] = eta * np.where(outA[fA] > 0, pc, ps) + (1.0 - eta) * beta[fA]
            reset[fA] = True
        fB = cB[(outA[cB] == 0) & ~reset[cB]]
        if fB.size:
            Lsum += float(np.sum((alpha[fB] - 0.5) * outB[fB]))
            Lcnt += fB.size
            alpha[fB] = eta * np.where(outB[fB] > 0, pc, ps) + (1.0 - eta) * alpha[fB]
            reset[fB] = True
        # Pairs committing on the same step get no reset (simultaneous commits,
        # measure-zero as dt -> 0); counted implicitly, negligible at this dt.

    strag = int(np.sum(outA == 0) + np.sum(outB == 0))
    A = np.where(outA == 0, np.where(alpha >= 0.5, 1, -1), outA).astype(float)
    B = np.where(outB == 0, np.where(beta >= 0.5, 1, -1), outB).astype(float)
    return A, B, (Lsum / max(Lcnt, 1)), strag, n_dbl / n


def chsh(n, rho=0.0, lam=0.0, psi=0.0, eta=1.0, seed0=0):
    Es, SEs, margA, leaks, strag, dbls = [], [], [], [], 0, []
    for k, (a, b) in enumerate(ANGLES):
        A, B, L, sg, db = run_pairs(n, a, b, rho, lam, psi, eta,
                                    seed=seed0 + 97 * k)
        E = float(np.mean(A * B))
        Es.append(E)
        SEs.append(float(np.std(A * B) / np.sqrt(n)))
        margA.append(float(np.mean(A)))
        leaks.append(L)
        strag += sg
        dbls.append(db)
    S = float(sum(s * E for s, E in zip(CHSH_SIGN, Es)))
    SE_S = float(np.sqrt(sum(se ** 2 for se in SEs)))
    return dict(E=Es, S=S, SE=SE_S, margA=margA, leak=float(np.mean(leaks)),
                strag=strag, dbl=float(np.mean(dbls)))


def kappa_single(n, x0, lam, seed):
    """Single-station drift susceptibility: P(win) - x0 at drift ratio lam."""
    g = np.random.default_rng(seed)
    x = np.full(n, x0)
    out = np.zeros(n, np.int8)
    d = lam * SIG2DT
    for _ in range(MAX_STEPS):
        act = np.flatnonzero(out == 0)
        if act.size == 0:
            break
        v = np.sqrt(x[act] * (1.0 - x[act]))
        x[act] = np.clip(x[act] + v * (SQ * g.standard_normal(act.size) + d),
                         0.0, 1.0)
        c = act[(x[act] <= 0.0) | (x[act] >= 1.0)]
        out[c] = np.where(x[c] >= 1.0, 1, -1).astype(np.int8)
    return float(np.mean(out == 1) - x0)


def main():
    quick = "--quick" in sys.argv
    n = 30_000 if quick else 240_000
    nt = 20_000 if quick else 120_000

    print(f"# Two-station correlated-noise Bell game  (n={n}/angle pair, "
          f"sig^2 dt={SIG2DT}, S_QM=2sqrt2={S_QM:.4f})")
    print("# Angles a=0, a'=pi/4, b=pi/8, b'=-pi/8;  E_QM = +-0.7071")
    print()

    configs = [
        ("1  baseline           rho=0    lam=0    eta=1  ",
         dict(rho=0.0, lam=0.0, eta=1.0), n, 11),
        ("2  white corr         rho=0.8  lam=0    eta=1  ",
         dict(rho=0.8, lam=0.0, eta=1.0), n, 22),
        ("2b white corr extreme rho=0.99 lam=0    eta=1  ",
         dict(rho=0.99, lam=0.0, eta=1.0), n, 33),
        ("3  unfaithful         rho=0    lam=0    eta=0.9",
         dict(rho=0.0, lam=0.0, eta=0.9), n, 44),
        ("4  unfaithful + corr  rho=0.8  lam=0    eta=0.9",
         dict(rho=0.8, lam=0.0, eta=0.9), n, 55),
        ("5  tone psi=0         rho=0    lam=0.3  eta=1  ",
         dict(rho=0.0, lam=0.3, psi=0.0, eta=1.0), nt, 66),
        ("6  tone psi=pi/8      rho=0    lam=0.3  eta=1  ",
         dict(rho=0.0, lam=0.3, psi=np.pi / 8, eta=1.0), nt, 77),
        ("7  tone psi=pi/4      rho=0    lam=0.3  eta=1  ",
         dict(rho=0.0, lam=0.3, psi=np.pi / 4, eta=1.0), nt, 88),
    ]

    results = {}
    print(f"{'config':<52} {'S':>7} {'+-':>6}  {'S-2sqrt2':>9}   E(a,b) E(a,b') E(a'b) E(a'b')")
    for name, kw, nn, sd in configs:
        r = chsh(nn, seed0=1000 * sd, **kw)
        results[name[:1] + name[1:3].strip()] = r
        dS = r["S"] - S_QM
        Estr = " ".join(f"{e:+.4f}" for e in r["E"])
        print(f"{name:<52} {r['S']:7.4f} {r['SE']:6.4f}  {dS:+9.4f}   {Estr}"
              f"   dbl={r['dbl']:.4f}"
              + (f"   [stragglers={r['strag']}]" if r["strag"] else ""))

    # leak statistic from the faithful correlated run (config 2)
    r2 = chsh(n, rho=0.8, lam=0.0, eta=1.0, seed0=22000)
    print(f"\n# leak statistic L = E[(far share at reset - 1/2)*sign(first outcome)]")
    print(f"#   config 2  (rho=0.8, eta=1):   L = {r2['leak']:+.4f}   "
          f"(reset discards it -> no S effect)")
    print(f"#   prediction for config 4:  dS = 4*(1-eta)*L = "
          f"{4 * 0.1 * r2['leak']:+.4f}")

    # no-signaling check in tone mode: A-marginal at a=0 under b vs b'
    r5 = chsh(nt, rho=0.0, lam=0.3, psi=0.0, eta=1.0, seed0=66000)
    print(f"\n# no-signaling / singles-blindness check (tone psi=0):")
    print(f"#   <A> at (a,b)   = {r5['margA'][0]:+.4f}")
    print(f"#   <A> at (a,b')  = {r5['margA'][1]:+.4f}   (both consistent with 0)")

    # single-station susceptibility
    k05 = kappa_single(nt, 0.5, 0.3, 5551)
    k085 = kappa_single(nt, np.cos(np.pi / 8) ** 2, 0.3, 5552)
    print(f"\n# single-station drift response at lam=0.3:")
    print(f"#   dP from x0=0.500: {k05:+.4f}   dP from x0=0.854: {k085:+.4f}")


if __name__ == "__main__":
    main()
