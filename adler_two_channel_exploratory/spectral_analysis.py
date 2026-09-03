#!/usr/bin/env python3
"""spectral_analysis.py — comparison process for spectral_driver.py (Experiment 7).

Per spectrum and angle: pair the two channel CSVs into A / B / tie / unresolved, fit the
unconstrained exponent across angles, and score the comparators computed on the SAME
detunings the race used: the Poisson race on the bare relaxation-rate sum
(sum over eligible clocks of sqrt(K^2 - Delta^2), via analytic.local_relaxation_rate) and the
Poisson race on the eligible-clock count, plus the spectrum-blind curves (linear, Born,
strongest). The plan's question: do the direct events move with the spectrum the way the
rate-weighted flux does? "If outcome frequencies remain exactly quadratic while the
analytic flux changes strongly, the proposed mechanism is not what drives the simulated
result." The only place the prediction is loaded.
"""

import argparse
import csv
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from adler_born_two_channel import analytic  # noqa: E402
from analysis import wilson, pair, fit_exponent, deviance  # noqa: E402
from spectral_driver import run_name, SPECTRA  # noqa: E402
from race_driver import channel_coupling  # noqa: E402


def read_run(path):
    with open(path) as f:
        header = json.loads(f.readline()[2:])
        times = {}
        for row in csv.DictReader(f):
            times[int(row["trial"])] = None if row["commit_time"] == "" else float(row["commit_time"])
    return header, times


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--N", type=int, default=16)
    ap.add_argument("--dtexp", type=int, default=7)
    ap.add_argument("--K", type=float, default=2.0)
    ap.add_argument("--angles", default="10,30,45,60,80")
    ap.add_argument("--spectra", default=",".join(SPECTRA))
    ap.add_argument("--rundir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "spectral_runs"))
    a = ap.parse_args()
    angles = [int(x) for x in a.angles.split(",")]
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, f"results_spectral_{a.tag}_N{a.N}_dt{a.dtexp}.csv")
    allrows = []
    summary = []
    for s in a.spectra.split(","):
        cells, rows = [], []
        dets = None
        for deg in angles:
            hA, tA = read_run(os.path.join(a.rundir, run_name(a.tag, s, "A", deg, a.N, a.dtexp) + ".csv"))
            hB, tB = read_run(os.path.join(a.rundir, run_name(a.tag, s, "B", deg, a.N, a.dtexp) + ".csv"))
            dets = np.array(hA["detunings"])
            nA, nB, tie, unres = pair(tA, tB)
            KA, KB = channel_coupling(a.K, deg, "A"), channel_coupling(a.K, deg, "B")
            n_res = nA + nB
            pA = nA / n_res if n_res else float("nan")
            lo, hi = wilson(nA, n_res)
            def rate_sum(K):
                m = analytic.eligible_mask(K, dets)
                return float(np.sum(analytic.local_relaxation_rate(K, dets[m]))) if np.any(m) else 0.0
            SA, SB = rate_sum(KA), rate_sum(KB)
            wA, wB = int(np.sum(np.abs(dets) < KA)), int(np.sum(np.abs(dets) < KB))
            row = dict(spectrum=s, deg=deg, K_A=round(KA, 4), K_B=round(KB, 4), trials=len(tA),
                       A=nA, B=nB, tie=tie, unresolved=unres, P_A=round(pA, 4),
                       wilson_lo=round(lo, 4), wilson_hi=round(hi, 4),
                       born=round(KA ** 2 / (KA ** 2 + KB ** 2), 4), linear=round(KA / (KA + KB), 4),
                       rate_sum=round(SA / (SA + SB), 4) if SA + SB > 0 else float("nan"),
                       width=round(wA / (wA + wB), 4) if wA + wB > 0 else float("nan"),
                       eligible_A=wA, eligible_B=wB,
                       commit_A=round(sum(v is not None for v in tA.values()) / len(tA), 3),
                       commit_B=round(sum(v is not None for v in tB.values()) / len(tB), 3))
            rows.append(row)
            cells.append((KA, KB, nA, nB))
        p_hat, (p_lo, p_hi), _ = fit_exponent(cells)
        comps = {"linear": [r["linear"] for r in rows], "Born": [r["born"] for r in rows],
                 "rate-sum": [r["rate_sum"] for r in rows], "width": [r["width"] for r in rows]}
        devs = {k: deviance(v, cells) for k, v in comps.items()}
        # analytic exponents of the comparators on this spectrum over the swept couplings
        Ks = np.array(sorted({c[0] for c in cells} | {c[1] for c in cells}))
        S = np.array([sum(analytic.local_relaxation_rate(K, dets[analytic.eligible_mask(K, dets)])) if np.any(analytic.eligible_mask(K, dets)) else 0.0 for K in Ks])
        W = np.array([np.sum(np.abs(dets) < K) for K in Ks])
        ok = (S > 0) & (W > 0)
        pS = analytic.fit_log_log_exponent(Ks[ok], S[ok]) if ok.sum() >= 2 else float("nan")
        pW = analytic.fit_log_log_exponent(Ks[ok], W[ok]) if ok.sum() >= 2 else float("nan")
        print(f"\n===== spectrum {s:8s}  detunings {np.round(dets, 3).tolist()}")
        print(f"      analytic exponents over the swept couplings: rate-sum {pS:.2f}, eligible-count {pW:.2f}")
        print(f" {'phi':>4} {'A':>4} {'B':>4} {'tie':>3} {'unr':>3} {'P_A':>6} {'[Wilson]':>15} {'Born':>6} {'lin':>6} {'rate':>6} {'width':>6} elig  commit")
        for r in rows:
            print(f" {r['deg']:>4} {r['A']:4d} {r['B']:4d} {r['tie']:3d} {r['unresolved']:3d} {r['P_A']:6.3f} [{r['wilson_lo']:.3f},{r['wilson_hi']:.3f}] "
                  f"{r['born']:6.3f} {r['linear']:6.3f} {r['rate_sum']:6.3f} {r['width']:6.3f} {r['eligible_A']:2d}/{r['eligible_B']:<2d} {r['commit_A']:.2f}/{r['commit_B']:.2f}")
        print(f"      fitted exponent p = {p_hat:.2f} [{p_lo:.2f}, {p_hi:.2f}];  deviance: " +
              ", ".join(f"{k} {v:.1f}" for k, v in devs.items()))
        summary.append(dict(spectrum=s, p=p_hat, lo=p_lo, hi=p_hi, pS=pS, pW=pW, **{f"dev_{k}": v for k, v in devs.items()}))
        allrows += rows
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(allrows[0].keys()))
        w.writeheader()
        w.writerows(allrows)
    print(f"\n{'spectrum':<9} {'direct p [95%]':>22} {'rate-sum exp':>13} {'width exp':>10} {'dev Born':>9} {'dev rate':>9} {'dev width':>10} {'dev lin':>8}")
    for r in summary:
        print(f"{r['spectrum']:<9} {r['p']:6.2f} [{r['lo']:.2f}, {r['hi']:.2f}] {r['pS']:13.2f} {r['pW']:10.2f} {r['dev_Born']:9.1f} {r['dev_rate-sum']:9.1f} {r['dev_width']:10.1f} {r['dev_linear']:8.1f}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
