#!/usr/bin/env python3
"""energy_race_spectra.py — the gated energy race (memoryless hazard linear in absorbed energy,
power K cos(theta) accumulated only inside the tongue) on detuning spectra of decreasing width.
Predictions fixed first in PREDICTIONS_energy_race_spectra.md. Everything else — grid size,
pulse, K = 2, noise D = 0.08, hazard scale c = 1.0, m = 1, trials — is the record's gated run.
Diagnostic only; every non-claim of RESULTS.md applies."""
import math, sys, time
import numpy as np
from scipy.stats import norm
from energy_hazard_race import channel_commit, fit_exponent, wilson, deviance, ANGLES, K_TOTAL, GRID, D_FROZEN

N = 16
def gauss_set(sigma):
    return np.array([norm.ppf((k + 0.5) / N) * sigma for k in range(N)])
SPECTRA = [("flat +-3", GRID), ("gauss s=2", gauss_set(2.0)), ("gauss s=1", gauss_set(1.0)),
           ("gauss s=0.5", gauss_set(0.5)), ("gauss s=0.25", gauss_set(0.25)), ("delta", np.zeros(N))]

def race_on(detunings, trials, c=1.0, D=D_FROZEN):
    cells, rows = [], []
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        cA, EA = channel_commit(KA, 1, c, D, trials, detunings=detunings, mode="gated")
        cB, EB = channel_commit(KB, 1, c, D, trials, detunings=detunings, mode="gated")
        a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
        A = int(np.sum(a_ok & (~b_ok | (cA < cB)))); B = int(np.sum(b_ok & (~a_ok | (cB < cA))))
        unr = int(np.sum(~a_ok & ~b_ok))
        rows.append(dict(deg=deg, KA=KA, KB=KB, A=A, B=B, unr=unr, EA=EA.mean(), EB=EB.mean(),
                         born=KA**2/(KA**2+KB**2), lin=KA/(KA+KB)))
        cells.append((KA, KB, A, B))
    p, (lo, hi), _ = fit_exponent(cells)
    dev_b = deviance([r["born"] for r in rows], cells); dev_l = deviance([r["lin"] for r in rows], cells)
    Ks = np.array([r["KA"] for r in rows] + [r["KB"] for r in rows]); Es = np.array([r["EA"] for r in rows] + [r["EB"] for r in rows])
    slope = np.polyfit(np.log(Ks), np.log(Es), 1)[0]
    unres = sum(r["unr"] for r in rows) / (trials * len(ANGLES))
    return p, lo, hi, dev_b, dev_l, slope, unres, rows

if __name__ == "__main__":
    print(__doc__); t0 = time.time(); trials = 10000
    print(f"\n{'spectrum':<14} {'p':>6} {'[95%]':>14} {'dev Born':>9} {'dev lin':>8} {'E~K^':>6} {'unres':>6}   P_A at phi = 10, 30, 45, 60, 80 (Born: .970 .750 .500 .250 .030)")
    for name, det in SPECTRA:
        p, lo, hi, dev_b, dev_l, slope, unres, rows = race_on(det, trials)
        pa = {r["deg"]: r["A"] / (r["A"] + r["B"]) for r in rows}
        print(f"{name:<14} {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {dev_l:8.1f} {slope:6.2f} {unres:6.3f}   "
              + " ".join(f"{pa[d]:.3f}" for d in (10, 30, 45, 60, 80))); sys.stdout.flush()
    print(f"\n(9 cells per fit; deviance ~ chi^2 with 9 dof under the comparator: 16.9 is the 5% point)\nrun time {time.time()-t0:.0f} s")
