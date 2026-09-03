#!/usr/bin/env python3
"""energy_hazard_race.py — an energy-tracking race in which commitment is MEMORYLESS and its
hazard grows with the energy a clock has absorbed from the drive.

Why: the fixed-dwell race scales as tongue width times the square root of the rate, and
the entry-time computation showed why — each clock's commitment is a near-deterministic
slide, so the fastest of N gains only logarithmically in N. A Born-producing race needs
per-site hazards that ADD across the tongue, i.e. memoryless commitment. This variant
replaces the dwell criterion with exactly that, and lets the hazard be set by energy
rather than by a phase-band test, which is where Paper 1 puts the weights (P1).

Model, per clock i in a channel with peak coupling K:
    phase        d theta_i/dt = Delta_i - K(t) sin theta_i  (+ sqrt(2D) dW; D = 0.08 as frozen)
    absorbed     d E_i/dt     = K(t)^n cos theta_i,  clipped at E_i >= 0
                 n = 1: the Adler clock's own energetics — a drive of amplitude K delivers
                        power K cos theta to a fixed-amplitude phase oscillator; over a slip
                        cycle the average is zero, and for a locked clock it is
                        K cos theta* = sqrt(K^2 - Delta^2), the relaxation rate. Nothing
                        squared is inserted.
                 n = 2: Paper 1's P1 deposit law (energy ~ amplitude squared), inserted.
    commitment   hazard lambda_i(t) = c * E_i(t): a Poisson event, no dwell, no band.
    trial        first commitment in either channel wins; none by pulse end = unresolved.
Same frozen grid (16 midpoints on +-3), raised-cosine pulse (duration 4), K_A = K cos(phi),
K_B = K sin(phi), K = 2. The hazard scale c sets the efficiency; if the two channels' energy
profiles have the same time shape the outcome frequencies are independent of c, so c is
swept over a decade as a check.

Prediction, stated before running: with n = 1 the summed absorbed power of a channel's
locked clocks is the tongue's rate sum — the semicircle, K^2 — so a linear memoryless
hazard should give p near 2 (Born) up to entry transients; with n = 2 it should overshoot
toward 3 (width times K^2). The fixed-dwell race gave 1.56.

Not the package's closed ledger; diagnostic only; every non-claim of RESULTS.md applies.
"""

import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from adler_born_two_channel import model  # noqa: E402   (deterministic layer only)
from analysis import fit_exponent, wilson, deviance  # noqa: E402

DURATION, CENTRE, D_FROZEN = 4.0, 0.0, 0.08
GRID = np.array([-3.0 + (k + 0.5) * 0.375 for k in range(16)])
ANGLES = [10, 20, 30, 40, 45, 50, 60, 70, 80]
K_TOTAL = 2.0
DT = 2.0 ** -6
rng = np.random.default_rng(2027)


def channel_commit(K_peak, n_power, c, D, trials, detunings=GRID, dt=DT, mode="gated",
                   m_hazard=1.0, stationary=False):
    """Return (first_commit_time per trial or nan, total absorbed energy per trial at pulse end).

    mode = "clip"   : the first run. dE = K^n cos(theta) dt for every clock, E clipped at 0
                      each step. WRONG for this purpose: clipping rectifies the slip cycles
                      of ineligible clocks (whose power averages to zero), leaving a spurious
                      positive residue linear in K from all sixteen clocks. Kept for the record.
    mode = "signed" : dE accumulated with its sign for every clock; the hazard acts on
                      max(E, 0). A slipping clock's E oscillates about zero.
    mode = "gated"  : dE accumulated with its sign only while the clock is inside the tongue
                      (K(t) > |Delta|); ineligible clocks have no stable point and absorb
                      nothing on average, so they are given nothing. Hazard on max(E, 0).
    """
    Dd = np.asarray(detunings, float)
    nclk = len(Dd)
    theta = rng.uniform(-np.pi, np.pi, size=(trials, nclk))
    E = np.zeros((trials, nclk))
    fired = np.full((trials, nclk), np.nan)
    steps = int(round(DURATION / dt))
    t0 = CENTRE - DURATION / 2
    kick = math.sqrt(2.0 * D * dt) if D > 0 else 0.0

    def K_at(t):
        return K_peak if stationary else K_peak * model.raised_cosine_envelope(t, CENTRE, DURATION)

    for j in range(steps):
        t = t0 + j * dt
        K = K_at(t)
        # energy absorbed over this step (current phase, current coupling)
        dE = (K ** n_power) * np.cos(theta) * dt
        if mode == "clip":
            E = np.maximum(E + dE, 0.0)
        elif mode == "signed":
            E = E + dE
        else:  # gated
            E = E + np.where((K > np.abs(Dd))[None, :], dE, 0.0)
        # memoryless commitment with hazard c * max(E, 0) ** m_hazard
        p_fire = -np.expm1(-c * np.maximum(E, 0.0) ** m_hazard * dt)
        fire = (rng.random((trials, nclk)) < p_fire) & np.isnan(fired)
        fired = np.where(fire, t + dt, fired)
        # phase step: RK4 drift + Euler-Maruyama kick
        K1, K2 = K_at(t + dt / 2), K_at(t + dt)
        k1 = model.adler_drift(theta, K, Dd[None, :])
        k2 = model.adler_drift(theta + 0.5 * dt * k1, K1, Dd[None, :])
        k3 = model.adler_drift(theta + 0.5 * dt * k2, K1, Dd[None, :])
        k4 = model.adler_drift(theta + dt * k3, K2, Dd[None, :])
        theta = theta + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if kick:
            theta = theta + kick * rng.standard_normal((trials, nclk))
    return np.nanmin(fired, axis=1), np.maximum(E, 0.0).sum(axis=1)


def race(n_power, c, D, trials, label, mode="gated", m_hazard=1.0, stationary=False):
    cells, rows = [], []
    print(f"\n===== {label}")
    print(f" {'phi':>4} {'K_A':>6} {'K_B':>6} {'A':>6} {'B':>6} {'tie':>4} {'unr':>6} {'P_A':>7} {'[Wilson]':>16} "
          f"{'Born':>6} {'E_A':>7} {'E_B':>7}")
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        cA, EA = channel_commit(KA, n_power, c, D, trials, mode=mode, m_hazard=m_hazard, stationary=stationary)
        cB, EB = channel_commit(KB, n_power, c, D, trials, mode=mode, m_hazard=m_hazard, stationary=stationary)
        a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
        A = int(np.sum(a_ok & (~b_ok | (cA < cB))))
        B = int(np.sum(b_ok & (~a_ok | (cB < cA))))
        tie = int(np.sum(a_ok & b_ok & (cA == cB)))
        unr = int(np.sum(~a_ok & ~b_ok))
        p = A / (A + B) if A + B else float("nan")
        lo, hi = wilson(A, A + B)
        rows.append(dict(deg=deg, KA=KA, KB=KB, A=A, B=B, tie=tie, unr=unr, p=p,
                         born=KA ** 2 / (KA ** 2 + KB ** 2), lin=KA / (KA + KB),
                         EA=EA.mean(), EB=EB.mean()))
        cells.append((KA, KB, A, B))
        print(f" {deg:>4} {KA:6.3f} {KB:6.3f} {A:6d} {B:6d} {tie:4d} {unr:6d} {p:7.3f} [{lo:.3f}, {hi:.3f}] "
              f"{KA**2/(KA**2+KB**2):6.3f} {EA.mean():7.3f} {EB.mean():7.3f}")
    p_hat, (p_lo, p_hi), _ = fit_exponent(cells)
    dev_b = deviance([r["born"] for r in rows], cells)
    dev_l = deviance([r["lin"] for r in rows], cells)
    # scaling of the channel's total absorbed energy with K (should be ~K^(n+1): width x power)
    Ks = np.array([r["KA"] for r in rows] + [r["KB"] for r in rows])
    Es = np.array([r["EA"] for r in rows] + [r["EB"] for r in rows])
    slope = np.polyfit(np.log(Ks), np.log(Es), 1)[0]
    unres = sum(r["unr"] for r in rows) / (trials * len(ANGLES))
    print(f"   fitted exponent p = {p_hat:.3f} [{p_lo:.2f}, {p_hi:.2f}]   deviance Born {dev_b:.1f}, linear {dev_l:.1f} (9 cells)   "
          f"unresolved {unres:.3f}   ties {sum(r['tie'] for r in rows)}   E_total ~ K^{slope:.2f}")
    return p_hat, (p_lo, p_hi), dev_b, unres, slope


if __name__ == "__main__":
    print(__doc__)
    t0 = time.time()
    trials = 10000
    mode = sys.argv[1] if len(sys.argv) > 1 else "gated"
    out = []
    if mode == "clip":
        variants = [(1, 0.3, D_FROZEN, 1.0, False), (1, 1.0, D_FROZEN, 1.0, False), (1, 3.0, D_FROZEN, 1.0, False),
                    (2, 0.15, D_FROZEN, 1.0, False), (2, 0.5, D_FROZEN, 1.0, False), (2, 1.5, D_FROZEN, 1.0, False),
                    (1, 1.0, 0.0, 1.0, False)]
    elif mode == "checks":
        mode = "gated"
        # (a) the hazard's own exponent: p should scale as m times the energy exponent;
        # (b) a stationary drive: the energy should track the grid's stationary rate-sum exponent (1.91)
        variants = [(1, 1.0, D_FROZEN, 0.5, False), (1, 0.1, D_FROZEN, 2.0, False), (1, 0.5, D_FROZEN, 1.0, True)]
    else:
        variants = [(1, 0.3, D_FROZEN, 1.0, False), (1, 1.0, D_FROZEN, 1.0, False), (1, 3.0, D_FROZEN, 1.0, False),
                    (2, 0.5, D_FROZEN, 1.0, False), (1, 1.0, 0.0, 1.0, False)]
    for n_power, c, D, m, stat in variants:
        out.append((f"n={n_power} c={c} m={m} {'stationary' if stat else 'pulsed'} {'noise' if D else 'no noise'}",
                    race(n_power, c, D, trials,
                         f"[{mode}] power K^{n_power} cos(theta), hazard c*E^{m} with c = {c}, noise D = {D}, "
                         f"{'stationary K' if stat else 'raised-cosine pulse'}",
                         mode=mode, m_hazard=m, stationary=stat)))
    print(f"\nSUMMARY (mode = {mode}; memoryless hazard linear in absorbed energy; frozen grid and pulse):")
    print(f"  {'variant':<40} {'p [95%]':>18} {'dev Born':>9} {'unresolved':>11} {'E_total~K^':>11}")
    for name, (p, (lo, hi), dev_b, unres, slope) in out:
        print(f"  {name:<40} {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {unres:11.3f} {slope:11.2f}")
    print("  fixed-dwell race (main sweep): p = 1.56 [1.44, 1.69]")
    print(f"run time {time.time() - t0:.0f} s")
