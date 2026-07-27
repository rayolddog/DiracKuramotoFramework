#!/usr/bin/env python3
"""
gambler_ruin_born_corrected.py  — corrected after the 2026-07-27 review panel.

ORIGINAL: born_selection_sims/gambler_ruin_born3.py
DEFECT (flagged by GPT-5 Codex, confirmed by re-run): the original stops when a
site's SHARE first reaches thresh=0.95 and declares the argmax the winner. Optional
stopping gives E[s_i(T)] = s_i(0) only for absorbing barriers at 0 and 1; stopping
at 0.95 biases the winner probability upward by an analytically predictable amount.
Verified: [2,1] returned 0.8263 (Born 0.8000), a systematic +2.6% (~3.6 sigma) bias;
a threshold sweep (0.90->0.869, 0.95->0.833, 0.99->0.808, 0.999->0.7975) lands on
Born only in the threshold->1 limit.

FIX: use the TRUE absorbing boundary. A site whose energy hits ~0 is permanently
out (0 is absorbing for the sqrt-e / min-stake dynamics); run until one survivor
holds the whole quantum (share 1). No threshold parameter, so the estimator is
unbiased. The conserving pairwise exchange (energy is exactly conserved: what one
site loses the other gains) is retained.

RESULT: reproduces Born to the Monte-Carlo floor for all three configs.
"""
import numpy as np

rng = np.random.default_rng(11)


def fair_exchange_absorbing(e0, ntrials=20000, step=0.1, eps=1e-9, maxit=4_000_000):
    """Fair pairwise exchange (d = +/- step*min(ei,ej); energy conserved), run to
    TRUE absorption: a site at energy <= eps is dead; the last survivor wins.
    Returns (win_frequencies, unfinished_count)."""
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        e[idx, i] -= d
        e[idx, j] += d
        e[idx] = np.where(e[idx] < eps, 0.0, e[idx])   # 0 is absorbing
        alive = (e[idx] > 0).sum(axis=1)
        done = alive <= 1
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    w = winners[winners >= 0]
    freq = np.bincount(w, minlength=n) / max(len(w), 1)
    return freq, int((winners < 0).sum())


def fair_exchange_threshold(e0, thresh, ntrials=20000, step=0.1, maxit=4_000_000):
    """The ORIGINAL (biased) rule kept for the convergence demonstration: stop at
    max share >= thresh, winner = argmax."""
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        e[idx, i] -= d
        e[idx, j] += d
        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    w = winners[winners >= 0]
    return np.bincount(w, minlength=n) / max(len(w), 1)


configs = [[2.0, 1.0], [3.0, 2.0, 1.0], [1.0] * 9 + [3.0]]

print("CORRECTED: true absorbing boundary (unbiased optional stopping)")
for amps in configs:
    A = np.array(amps, float)
    born = A ** 2 / np.sum(A ** 2)
    freq, unf = fair_exchange_absorbing(born)
    print(f"A={np.round(amps,2)}  (unfinished: {unf})")
    print(f"  corrected: {np.round(freq,4)}")
    print(f"  Born:      {np.round(born,4)}   max|dev|={np.max(np.abs(freq-born)):.4f}")

print("\nWhy the original was biased — threshold sweep on [2,1] (Born bright = 0.8000):")
e0 = np.array([0.8, 0.2])
print(f"  {'thresh':>8} | {'P(bright)':>9} | {'bias':>7}")
for th in (0.90, 0.95, 0.99):
    p = fair_exchange_threshold(e0, th).max()
    print(f"  {th:>8} | {p:>9.4f} | {p-0.8:>+7.4f}")
print(f"  {'absorb':>8} | {fair_exchange_absorbing(e0)[0].max():>9.4f} | (true boundary)")
