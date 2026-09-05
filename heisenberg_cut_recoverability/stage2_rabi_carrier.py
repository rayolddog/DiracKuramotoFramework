#!/usr/bin/env python3
"""Stage 2, Part A: does the carrier frequency enter the recoverability crossover?
Quantum Rabi model (no RWA) + dense record channel, echo recoverability. See PREDICTIONS_STAGE2.md."""
import json, math, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
K, B, N = 1.0, 40.0, 128
DPOS = np.logspace(math.log10(0.05), math.log10(6.0), 21)
DELTAS = np.concatenate([-DPOS[::-1], [0.0], DPOS])
OMEGAS = (8.0, 16.0, 32.0, 64.0)


def build(omega, delta, gamma, nmax, rwa, mode):
    """Basis |n, s, b> : n photons (0..nmax), s in {g,e}, b in {vac, k=1..N}. mode: fwd / echo."""
    np_ = nmax + 1; nb = N + 1
    dim = np_ * 2 * nb
    idx = lambda n, s, b: (n * 2 + s) * nb + b
    H = np.zeros((dim, dim))
    sgn = -1.0 if mode == "echo" else 1.0
    g = math.sqrt(gamma * B / (2 * math.pi)) if gamma > 0 else 0.0
    eps = np.linspace(-B / 2, B / 2, N)
    gk = g / math.sqrt(N)
    for n in range(np_):
        for s in (0, 1):
            for b in range(nb):
                i = idx(n, s, b)
                e_sys = omega * n + (omega + delta) * s
                e_bath = 0.0 if b == 0 else (omega + delta + eps[b - 1])   # bath energies never reversed
                H[i, i] = sgn * e_sys + e_bath
                # capture: rotating part  a sigma+ : |n, g> -> |n-1, e>
                if s == 0 and n >= 1:
                    j = idx(n - 1, 1, b); v = sgn * K * math.sqrt(n); H[i, j] += v; H[j, i] += v
                # counter-rotating part a sigma- : |n, e> -> |n-1, g>  (a^dagger sigma^+ is its h.c.)
                if (not rwa) and s == 1 and n >= 1:
                    j = idx(n - 1, 0, b); v = sgn * K * math.sqrt(n); H[i, j] += v; H[j, i] += v
                # record channel (never reversed): |n, e, vac> <-> |n, g, k>
                if s == 1 and b == 0 and gk > 0:
                    for k in range(1, nb):
                        j = idx(n, 0, k); H[i, j] += gk; H[j, i] += gk
    return H, idx(1, 0, 0)


def echo_R(omega, delta, gamma, t, nmax=3, rwa=False):
    Hf, i0 = build(omega, delta, gamma, nmax, rwa, "fwd")
    He, _ = build(omega, delta, gamma, nmax, rwa, "echo")
    psi = np.zeros(Hf.shape[0], complex); psi[i0] = 1.0
    w, V = np.linalg.eigh(Hf); psi = V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))
    w, V = np.linalg.eigh(He); psi = V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))
    return abs(psi[i0]) ** 2


def centre_halfwidth(deltas, rate):
    m = rate.max(); half = m / 2
    i = int(rate.argmax())
    def cross(lo, hi, step):
        j = i
        while 0 <= j + step < len(rate) and rate[j + step] > half:
            j += step
        if not (0 <= j + step < len(rate)): return float("nan")
        a, b = rate[j] - half, rate[j + step] - half
        return deltas[j] + (deltas[j + step] - deltas[j]) * a / (a - b)
    xl, xr = cross(0, i, -1), cross(i, len(rate) - 1, +1)
    return 0.5 * (xl + xr), 0.5 * (xr - xl), xl, xr


if __name__ == "__main__":
    t0 = time.time(); out = {"deltas": DELTAS.tolist(), "rows": []}
    print("A1 calibration, no channel, echo R at every Delta (nmax 3):")
    for om in (8.0, 64.0):
        Rs = [echo_R(om, d, 0.0, 3.0) for d in DELTAS[::4]]
        print(f"   omega/K = {om:4.0f}: min R = {min(Rs):.12f}  max R = {max(Rs):.12f}")
    print("A4 truncation at omega/K = 8, Gamma 0.2, t 3, Delta = -2, 0, 2: nmax 3 vs 4")
    for d in (-2.0, 0.0, 2.0):
        r3, r4 = echo_R(8.0, d, 0.2, 3.0, 3), echo_R(8.0, d, 0.2, 3.0, 4)
        print(f"   Delta {d:+.0f}: {r3:.6f}  {r4:.6f}  diff {abs(r3-r4):.2e}")
    print("\nRate curves Gamma_eff(Delta) = -ln R/(2t); centre c, half-width h, and c*omega/K^2")
    print(f" {'omega/K':>8} {'Gamma':>6} {'c':>8} {'h':>7} {'c*om/K2':>8} {'x_left':>7} {'x_right':>7}")
    for gamma in (0.2, 0.5):
        rows = []
        for om in list(OMEGAS) + ["RWA"]:
            rwa = om == "RWA"; omv = 64.0 if rwa else om
            R = np.array([echo_R(omv, d, gamma, 3.0, 3, rwa) for d in DELTAS])
            rate = -np.log(np.clip(R, 1e-300, 1)) / (2 * 3.0)
            c, h, xl, xr = centre_halfwidth(DELTAS, rate)
            out["rows"].append(dict(omega=("RWA" if rwa else om), gamma=gamma, R=R.tolist(), c=c, h=h, xl=xl, xr=xr))
            print(f" {str(om):>8} {gamma:6.2f} {c:8.4f} {h:7.4f} {(c*omv/K/K if not rwa else float('nan')):8.3f} {xl:7.3f} {xr:7.3f}")
            sys.stdout.flush()
    json.dump(out, open(os.path.join(HERE, "stage2_rabi_results.json"), "w"))
    print(f"\nrun time {time.time()-t0:.0f} s")
