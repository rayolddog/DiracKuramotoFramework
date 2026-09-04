#!/usr/bin/env python3
"""fano_recoverability.py — recoverability of a captured quantum in the smallest exact model
with capture, off-resonant return and an irreversible record channel. Predictions are in
PREDICTIONS.md (with its addendum) and were fixed before this was run.

Single-excitation sector: |p> (photon), |e> (absorber excitation, detuned by Delta),
|k> (N record modes over bandwidth B). H = Delta|e><e| + sum eps_k|k><k|
+ K(|p><e| + h.c.) + sum g_k(|e><k| + h.c.), g_k = g/sqrt(N), Gamma = 2 pi g^2 / B.

Two observables, both after capture under H for time t:
  R_echo : partial Loschmidt echo — system block reversed (Delta -> -Delta, K -> -K), record
           channel untouched, for time t; R = |<p|psi>|^2.  No bath => R = 1 exactly.
  R_op   : operational K-flip only (Delta and bath left running). Kept on record; conflates
           the detuning's non-reversal with the record channel's irreversibility.
Exact propagation by eigendecomposition; no integrator.
"""

import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
K = 1.0
B = 40.0
DELTAS = np.logspace(math.log10(0.05), math.log10(20.0), 41)
GAMMAS = (0.05, 0.2, 1.0)
TIMES = (1.0, 3.0, 10.0)
NS = (1, 4, 16, 64, 256)


def hamiltonian(N, delta, gamma, mode, B=B):
    """mode: 'fwd' capture; 'echo' system block reversed, bath untouched; 'op' K flipped only."""
    dim = N + 2
    H = np.zeros((dim, dim))
    s_delta = -1.0 if mode == "echo" else 1.0
    s_K = -1.0 if mode in ("echo", "op") else 1.0
    H[1, 1] = s_delta * delta
    H[0, 1] = H[1, 0] = s_K * K
    if N > 0 and gamma > 0:
        g = math.sqrt(gamma * B / (2 * math.pi))
        eps = np.linspace(-B / 2, B / 2, N) if N > 1 else np.array([0.0])
        gk = g / math.sqrt(N)
        for k in range(N):
            H[2 + k, 2 + k] = delta + eps[k]     # bath energies never reversed
            H[1, 2 + k] = H[2 + k, 1] = gk       # bath couplings never reversed
    return H


def propagator(H, t):
    w, V = np.linalg.eigh(H)
    return (V * np.exp(-1j * w * t)) @ V.conj().T


def run(N, delta, gamma, t, B=B):
    psi = np.zeros(N + 2, complex)
    psi[0] = 1.0
    psi = propagator(hamiltonian(N, delta, gamma, "fwd", B), t) @ psi
    in_record = float(np.sum(np.abs(psi[2:]) ** 2))
    R_echo = abs((propagator(hamiltonian(N, delta, gamma, "echo", B), t) @ psi)[0]) ** 2
    R_op = abs((propagator(hamiltonian(N, delta, gamma, "op", B), t) @ psi)[0]) ** 2
    return R_echo, R_op, in_record


def crossover(deltas, R):
    """Midpoint x50 and relative width (x75 - x25)/x50 of R(Delta/K) between its ends."""
    lo, hi = R[:3].mean(), R[-3:].mean()
    if abs(hi - lo) < 0.05:
        return float("nan"), float("nan"), lo, hi

    def x_at(frac):
        target = lo + frac * (hi - lo)
        for i in range(len(R) - 1):
            a, b = R[i] - target, R[i + 1] - target
            if a == 0 or a * b < 0:
                f = a / (a - b) if a != b else 0.0
                return math.exp(math.log(deltas[i]) + f * (math.log(deltas[i + 1]) - math.log(deltas[i])))
        return float("nan")

    x50, x25, x75 = x_at(0.5), x_at(0.25), x_at(0.75)
    ok = all(v == v for v in (x50, x25, x75))
    return x50, (abs(x75 - x25) / x50 if ok else float("nan")), lo, hi


if __name__ == "__main__":
    print(__doc__)
    t0 = time.time()
    out = {"K": K, "B": B, "deltas": DELTAS.tolist(), "runs": []}

    # 1. calibration: no bath, both observables, every Delta
    R0 = np.array([run(0, d, 0.0, 3.0)[:2] for d in DELTAS])
    print(f"Prediction 1 (no bath, t = 3): echo  min R = {R0[:,0].min():.15f}  max R = {R0[:,0].max():.15f}")
    print(f"                              K-flip min R = {R0[:,1].min():.3f}  (fails off resonance: definition error, addendum)")
    out["no_bath_echo_min_R"] = float(R0[:, 0].min())

    # 2. single record mode: oscillation in g t (echo observable)
    print("\nPrediction 2 (N = 1, one record mode; Delta = 0, t = 3): R_echo vs record coupling g")
    gs = np.linspace(0.0, 1.5, 16)
    R1 = []
    for g in gs:
        H = hamiltonian(1, 0.0, 1.0, "fwd"); H[1, 2] = H[2, 1] = g
        He = hamiltonian(1, 0.0, 1.0, "echo"); He[1, 2] = He[2, 1] = g
        psi = np.zeros(3, complex); psi[0] = 1
        psi = propagator(He, 3.0) @ (propagator(H, 3.0) @ psi)
        R1.append(abs(psi[0]) ** 2)
    print("   g:  " + " ".join(f"{g:5.2f}" for g in gs))
    print("   R:  " + " ".join(f"{r:5.2f}" for r in R1))
    out["N1_g"] = gs.tolist(); out["N1_R"] = R1

    # 3-6. the sweep, echo observable
    occ = 2 * K * K / (DELTAS ** 2 + 4 * K * K)          # time-averaged absorber occupation
    print("\nSweep, R_echo(Delta/K): crossover midpoint x50, relative width; R_op midpoint for comparison")
    print(f" {'N':>4} {'Gamma':>6} {'t':>5} {'Gamma*t':>8} {'R(in)':>7} {'R(out)':>7} {'x50':>7} {'width':>7} {'x50_op':>7}  "
          f"{'R_echo at Delta/K = 0.05 .. 20 (every 5th)':>40}")
    for N in NS:
        for gamma in GAMMAS:
            for t in TIMES:
                res = [run(N, d, gamma, t) for d in DELTAS]
                Re = np.array([r[0] for r in res]); Ro = np.array([r[1] for r in res])
                x50, width, lo, hi = crossover(DELTAS, Re)
                x50o = crossover(DELTAS, Ro)[0]
                out["runs"].append(dict(N=N, gamma=gamma, t=t, R_echo=Re.tolist(), R_op=Ro.tolist(),
                                        in_record=[r[2] for r in res], x50=x50, width=width, R_in=lo, R_out=hi,
                                        x50_op=x50o))
                print(f" {N:4d} {gamma:6.2f} {t:5.1f} {gamma*t:8.2f} {lo:7.3f} {hi:7.3f} {x50:7.3f} {width:7.3f} {x50o:7.3f}  "
                      + " ".join(f"{r:4.2f}" for r in Re[::5]))

    # 3. time dependence at fixed Delta, dense bath: is it exp(-Gamma_eff t) with Gamma_eff = Gamma * occupation?
    print("\nPrediction 3 (N = 256, Gamma = 0.2): -ln(R_echo)/(Gamma t) vs t at Delta/K = 0, 1, 2, 4;  analytic occupation 2K^2/(D^2+4K^2) in the last column")
    for d in (0.0, 1.0, 2.0, 4.0):
        vals = [-math.log(max(run(256, d, 0.2, t)[0], 1e-300)) / (0.2 * t) for t in (1.0, 3.0, 10.0, 30.0)]
        print(f"   Delta/K = {d:3.1f}:  " + "  ".join(f"{v:6.3f}" for v in vals) + f"   occ = {2/(d*d+4):.3f}")

    # 4. location drift with Gamma t, dense bath: x50 across Gamma t at N = 256
    print("\nPrediction 4 (N = 256): x50 and width against Gamma t (all Gamma, t combinations, sorted)")
    rows = sorted([(r["gamma"] * r["t"], r["gamma"], r["t"], r["x50"], r["width"]) for r in out["runs"] if r["N"] == 256])
    for gt, g, t, x, w in rows:
        print(f"   Gamma t = {gt:5.2f} (Gamma {g:4.2f}, t {t:4.1f}):  x50 = {x:6.3f}   width = {w:6.3f}")

    # 7. bandwidth check at fixed Gamma
    print("\nPrediction 7 (N = 256, Gamma = 0.2, t = 3): R_echo at Delta/K = 0.5, 1, 2 for B = 20, 40, 80")
    for Bv in (20.0, 40.0, 80.0):
        vals = [run(256, d, 0.2, 3.0, B=Bv)[0] for d in (0.5, 1.0, 2.0)]
        print(f"   B = {Bv:4.0f}:  " + "  ".join(f"{v:.4f}" for v in vals))
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f)
    print(f"\nrun time {time.time() - t0:.0f} s; wrote results.json")
