#!/usr/bin/env python3
"""analysis.py — pair the one-channel ledgers written by race_driver.py into two-channel
outcomes, and compare the measured channel frequencies with the predeclared alternatives.

This is the COMPARISON process of the two-channel plan: it runs after the raw ledgers are
closed, opens them only through the package's own gate (``raw_runner.open_raw_run``), and
is the only place the analytic prediction (``adler_born_two_channel.analytic``) is loaded.

Per angle phi, for trial t with commit times tA(t), tB(t) (None if unresolved):
    A wins if tA < tB or (tA set, tB None); B symmetric; tie if both set and equal;
    unresolved if both None.
Reported: counts A/B/tie/unresolved; P_A among resolved with a Wilson 95% interval; the
single-channel commit fractions; and the fitted exponent p in
    P_A/(P_A+P_B) = K_A^p / (K_A^p + K_B^p),
by maximum binomial likelihood over all angles with a profile-likelihood 95% interval.
Predeclared comparators (two-channel plan, Experiment 4), each scored by its binomial
deviance against the resolved counts:
    p = 1  amplitude-linear weighting
    p = 2  amplitude-squared weighting (Born; cos^2 phi at fixed total K)
    strongest channel always wins
    Poisson race on the bare relaxation-rate sum over the exact grid (analytic.tongue_rate_sum)
    Poisson race on the eligible-clock count (tongue width only)
The tie fraction is a convergence diagnostic and is printed with the results; a
non-negligible tie fraction blocks interpretation per the plan.

Every manifest carries numerical_gate = "diagnostic_only"; nothing here upgrades it.
"""

import argparse
import csv
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from adler_born_two_channel import raw_runner  # noqa: E402
from adler_born_two_channel import analytic  # noqa: E402  (comparison process only)

from race_driver import run_name, channel_coupling, PHYSICS  # noqa: E402


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return (c - h, c + h)


def commit_times(name):
    closed = raw_runner.open_raw_run(name)
    gate = closed.manifest.value("numerical_gate")
    times = {}
    for row in closed.ledger:
        times[int(row["trial"])] = row["commit_time"]  # float or None
    return times, gate


def pair(tA, tB):
    nA = nB = tie = unres = 0
    for t in sorted(tA):
        a, b = tA[t], tB[t]
        if a is None and b is None:
            unres += 1
        elif b is None or (a is not None and a < b):
            nA += 1
        elif a is None or b < a:
            nB += 1
        else:
            tie += 1
    return nA, nB, tie, unres


def loglik(p, cells):
    """Binomial log-likelihood of the resolved counts under P_A = K_A^p/(K_A^p+K_B^p)."""
    ll = 0.0
    for KA, KB, nA, nB in cells:
        q = KA ** p / (KA ** p + KB ** p)
        q = min(max(q, 1e-12), 1 - 1e-12)
        ll += nA * math.log(q) + nB * math.log(1 - q)
    return ll


def deviance(qs, cells):
    """Binomial deviance of a comparator giving P_A = q per cell (saturated minus model)."""
    d = 0.0
    for (KA, KB, nA, nB), q in zip(cells, qs):
        n = nA + nB
        if n == 0:
            continue
        q = min(max(q, 1e-12), 1 - 1e-12)
        ph = nA / n
        sat = (nA * math.log(ph) if nA else 0.0) + (nB * math.log(1 - ph) if nB else 0.0)
        d += 2 * (sat - (nA * math.log(q) + nB * math.log(1 - q)))
    return d


def fit_exponent(cells):
    grid = np.linspace(0.0, 8.0, 1601)
    ll = np.array([loglik(p, cells) for p in grid])
    j = int(np.argmax(ll))
    # refine
    lo, hi = grid[max(j - 1, 0)], grid[min(j + 1, len(grid) - 1)]
    fine = np.linspace(lo, hi, 2001)
    llf = np.array([loglik(p, cells) for p in fine])
    k = int(np.argmax(llf))
    p_hat, ll_max = float(fine[k]), float(llf[k])
    inside = grid[ll >= ll_max - 1.92]
    return p_hat, (float(inside.min()), float(inside.max())), ll_max


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--dtexp", type=int, required=True)
    ap.add_argument("--K", type=float, default=2.0)
    ap.add_argument("--angles", default="10,20,30,40,45,50,60,70,80")
    ap.add_argument("--out", default=None, help="CSV path; default results_<tag>_N<N>_dt<dtexp>.csv")
    a = ap.parse_args()
    angles = [int(x) for x in a.angles.split(",")]
    here = os.path.dirname(os.path.abspath(__file__))
    out = a.out or os.path.join(here, f"results_{a.tag}_N{a.N}_dt{a.dtexp}.csv")

    grid = analytic.FlatGrid(PHYSICS["half_width"], a.N)
    rows, cells = [], []
    gates = set()
    for deg in angles:
        nameA = run_name(a.tag, "A", deg, a.N, a.dtexp)
        nameB = run_name(a.tag, "B", deg, a.N, a.dtexp)
        tA, gA = commit_times(nameA)
        tB, gB = commit_times(nameB)
        gates |= {gA, gB}
        if set(tA) != set(tB):
            raise SystemExit(f"trial sets differ at phi={deg}")
        nA, nB, tie, unres = pair(tA, tB)
        KA, KB = channel_coupling(a.K, deg, "A"), channel_coupling(a.K, deg, "B")
        n_res = nA + nB
        pA = nA / n_res if n_res else float("nan")
        lo, hi = wilson(nA, n_res)
        SA, SB = analytic.tongue_rate_sum(KA, grid), analytic.tongue_rate_sum(KB, grid)
        wA = int(np.sum(np.abs(grid.detunings) < KA))
        wB = int(np.sum(np.abs(grid.detunings) < KB))
        cA = sum(v is not None for v in tA.values()) / len(tA)
        cB = sum(v is not None for v in tB.values()) / len(tB)
        row = dict(deg=deg, K_A=round(KA, 5), K_B=round(KB, 5), trials=len(tA),
                   A=nA, B=nB, tie=tie, unresolved=unres,
                   P_A=round(pA, 4), wilson_lo=round(lo, 4), wilson_hi=round(hi, 4),
                   born=round(KA ** 2 / (KA ** 2 + KB ** 2), 4),
                   linear=round(KA / (KA + KB), 4),
                   strongest=1.0 if KA > KB else (0.5 if KA == KB else 0.0),
                   rate_sum=round(SA / (SA + SB) if SA + SB > 0 else float("nan"), 4),
                   width=round(wA / (wA + wB) if wA + wB > 0 else float("nan"), 4),
                   eligible_A=wA, eligible_B=wB,
                   commit_frac_A=round(cA, 4), commit_frac_B=round(cB, 4))
        rows.append(row)
        cells.append((KA, KB, nA, nB))

    p_hat, (p_lo, p_hi), _ = fit_exponent(cells)
    comps = {
        "linear (p=1)": [r["linear"] for r in rows],
        "Born (p=2)": [r["born"] for r in rows],
        "strongest wins": [r["strongest"] for r in rows],
        "rate-sum race": [r["rate_sum"] for r in rows],
        "width-only race": [r["width"] for r in rows],
        f"fitted p={p_hat:.2f}": [r["K_A"] ** p_hat / (r["K_A"] ** p_hat + r["K_B"] ** p_hat) for r in rows],
    }
    devs = {k: deviance(v, cells) for k, v in comps.items()}

    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    total = sum(r["trials"] for r in rows)
    ties = sum(r["tie"] for r in rows)
    unres = sum(r["unresolved"] for r in rows)
    print(f"tag={a.tag} N={a.N} dt=2^-{a.dtexp} K={a.K}  numerical_gate(s)={sorted(gates)}")
    print(f"{'phi':>4} {'K_A':>6} {'K_B':>6} {'A':>5} {'B':>5} {'tie':>4} {'unres':>5} "
          f"{'P_A':>7} {'[Wilson 95%]':>16} {'Born':>6} {'lin':>6} {'rate':>6} {'width':>6}  elig A/B  commit A/B")
    for r in rows:
        print(f"{r['deg']:>4} {r['K_A']:6.3f} {r['K_B']:6.3f} {r['A']:5d} {r['B']:5d} {r['tie']:4d} {r['unresolved']:5d} "
              f"{r['P_A']:7.3f} [{r['wilson_lo']:.3f}, {r['wilson_hi']:.3f}] {r['born']:6.3f} {r['linear']:6.3f} "
              f"{r['rate_sum']:6.3f} {r['width']:6.3f}   {r['eligible_A']:2d}/{r['eligible_B']:<2d}   "
              f"{r['commit_frac_A']:.2f}/{r['commit_frac_B']:.2f}")
    print(f"\nfitted exponent p = {p_hat:.3f}   profile-likelihood 95% [{p_lo:.2f}, {p_hi:.2f}]   "
          f"(p=1 linear, p=2 Born)")
    print("binomial deviance of each comparator against the resolved counts "
          f"({len(rows)} cells; lower is better; ~chi^2 with {len(rows)} dof for a fixed comparator):")
    for k, d in devs.items():
        print(f"   {k:<18} {d:8.2f}")
    print(f"\ntie fraction {ties}/{total} = {ties/total:.4f}   unresolved {unres}/{total} = {unres/total:.3f}")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
