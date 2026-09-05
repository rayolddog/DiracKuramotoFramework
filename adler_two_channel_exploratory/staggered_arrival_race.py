#!/usr/bin/env python3
"""Run B of the review round: the gated energy race with channel B's pulse delayed. Predictions in
heisenberg_cut_recoverability/PREDICTIONS_review_runs.md. Diagnostic only; every non-claim of RESULTS.md applies."""
import math, time, sys
import numpy as np
import energy_hazard_race as ehr
from energy_hazard_race import channel_commit, ANGLES, K_TOTAL, D_FROZEN

def race(delay, c, trials=10000):
    rows = []
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        ehr.CENTRE = 0.0
        cA, _ = channel_commit(KA, 1, c, D_FROZEN, trials, mode="gated")
        ehr.CENTRE = delay
        cB, _ = channel_commit(KB, 1, c, D_FROZEN, trials, mode="gated")
        ehr.CENTRE = 0.0
        a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
        A_first = np.sum(a_ok & (~b_ok | (cA < cB))); B_first = np.sum(b_ok & (~a_ok | (cB < cA)))
        rows.append(dict(deg=deg, pA=a_ok.mean(), pB=b_ok.mean(), both=(a_ok & b_ok).mean(),
                         ratio=A_first / max(A_first + B_first, 1), born=KA**2 / (KA**2 + KB**2)))
    return rows

if __name__ == "__main__":
    t0 = time.time()
    for c in (1.0, 0.05):
        for delay in (0.0, 2.0, 8.0):
            rows = race(delay, c)
            print(f"\n=== hazard scale c = {c}, channel B delayed by {delay} (pulse duration 4)")
            print(f" {'phi':>4} {'Born':>6} {'P(A clicks)':>12} {'P(B clicks)':>12} {'P(both)':>8} {'P(A first)':>11} {'ratio-Born':>11}")
            for r in rows:
                print(f" {r['deg']:>4} {r['born']:6.3f} {r['pA']:12.3f} {r['pB']:12.3f} {r['both']:8.3f} {r['ratio']:11.3f} {r['ratio']-r['born']:+11.3f}")
            sys.stdout.flush()
    print(f"\nrun time {time.time()-t0:.0f} s")
