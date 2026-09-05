#!/usr/bin/env python3
"""energy_race_adiabatic.py — the gated energy race in its broadband, adiabatic, continuum limit.
Predictions fixed first in PREDICTIONS_energy_race_adiabatic.md. Flat +-3 grids of 16 and 64
clocks; stationary drive with windows 4, 8, 16, 32; raised-cosine pulses of duration 1..16;
hazard scale scaled as 4/T. Diagnostic only; every non-claim of RESULTS.md applies."""
import math, sys, time
import numpy as np
import energy_hazard_race as ehr
from energy_hazard_race import channel_commit, fit_exponent, deviance, ANGLES, K_TOTAL, D_FROZEN

def flat(n, half=3.0):
    return np.array([-half + (k + 0.5) * (2 * half / n) for k in range(n)])

def rate_sum_exponent(det):
    Ks = np.linspace(0.4, 2.0, 9); S = [np.sum(np.sqrt(np.clip(K*K - det**2, 0, None))) for K in Ks]
    return np.polyfit(np.log(Ks), np.log(S), 1)[0]

def race_on(det, T, stationary, c, D, trials):
    ehr.DURATION = T
    cells, rows = [], []
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        cA, EA = channel_commit(KA, 1, c, D, trials, detunings=det, mode="gated", stationary=stationary)
        cB, EB = channel_commit(KB, 1, c, D, trials, detunings=det, mode="gated", stationary=stationary)
        a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
        A = int(np.sum(a_ok & (~b_ok | (cA < cB)))); B = int(np.sum(b_ok & (~a_ok | (cB < cA))))
        rows.append(dict(KA=KA, KB=KB, A=A, B=B, unr=int(np.sum(~a_ok & ~b_ok)), EA=EA.mean(), EB=EB.mean(), born=KA**2/(KA**2+KB**2)))
        cells.append((KA, KB, A, B))
    p, (lo, hi), _ = fit_exponent(cells)
    dev_b = deviance([r["born"] for r in rows], cells)
    Ks = np.array([r["KA"] for r in rows] + [r["KB"] for r in rows]); Es = np.array([r["EA"] for r in rows] + [r["EB"] for r in rows])
    slope = np.polyfit(np.log(Ks), np.log(Es), 1)[0]
    unres = sum(r["unr"] for r in rows) / (trials * len(ANGLES))
    pa30 = rows[2]["A"] / (rows[2]["A"] + rows[2]["B"])
    return p, lo, hi, dev_b, slope, unres, pa30

if __name__ == "__main__":
    print(__doc__); t0 = time.time()
    g16, g64 = flat(16), flat(64)
    print(f"rate-sum exponent of the grid (stationary, analytic): 16 clocks {rate_sum_exponent(g16):.3f}, 64 clocks {rate_sum_exponent(g64):.3f}, continuum 2.000")
    configs = [  # (label, grid, T, stationary, c, D, trials)
        ("P1  stationary T=4,  16 clk", g16, 4.0, True, 0.5, D_FROZEN, 10000),
        ("P1  stationary T=4,  64 clk", g64, 4.0, True, 0.5, D_FROZEN, 10000),
        ("P5  stationary T=4,  64 clk, D=0", g64, 4.0, True, 0.5, 0.0, 10000),
        ("P2  stationary T=8,  64 clk", g64, 8.0, True, 0.25, D_FROZEN, 10000),
        ("P2  stationary T=16, 64 clk", g64, 16.0, True, 0.125, D_FROZEN, 8000),
        ("P2  stationary T=32, 64 clk", g64, 32.0, True, 0.0625, D_FROZEN, 5000),
        ("P4  pulse T=1,  64 clk", g64, 1.0, False, 4.0, D_FROZEN, 10000),
        ("P3  pulse T=2,  64 clk", g64, 2.0, False, 2.0, D_FROZEN, 10000),
        ("P3  pulse T=4,  64 clk", g64, 4.0, False, 1.0, D_FROZEN, 10000),
        ("P3  pulse T=8,  64 clk", g64, 8.0, False, 0.5, D_FROZEN, 8000),
        ("P3  pulse T=16, 64 clk", g64, 16.0, False, 0.25, D_FROZEN, 5000),
    ]
    print(f"\n{'config':<34} {'p':>6} {'[95%]':>14} {'dev Born':>9} {'E~K^':>6} {'unres':>6} {'P_A(30)':>8}  (Born 0.750)   elapsed")
    for label, det, T, stat, c, D, trials in configs:
        p, lo, hi, dev_b, slope, unres, pa30 = race_on(det, T, stat, c, D, trials)
        print(f"{label:<34} {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {slope:6.2f} {unres:6.3f} {pa30:8.3f}   {time.time()-t0:7.0f} s"); sys.stdout.flush()
    print(f"\nrun time {time.time()-t0:.0f} s")
