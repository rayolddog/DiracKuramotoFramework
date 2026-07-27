#!/usr/bin/env python3
"""
rate_commit_born_corrected.py  — corrected after the 2026-07-27 review panel.

ORIGINAL: born_selection_sims/rate_commit_born.py
DEFECT (flagged by GPT-5 Codex, confirmed): the per-step commit probability was
lam*dt*sum(s_i^alpha), used directly in `rng.random() < p`. For alpha < 1,
sum(s_i^alpha) > 1, so at lam=50, dt=0.02 the "probability" reaches
50*0.02*1.342 = 1.342 > 1 and is silently clipped to certainty — an invalid
Bernoulli parameter that corrupts the alpha=0.5 rows.

FIX: use the correct discrete-time hazard from a Poisson (competing-exponential)
rate process, p_commit = 1 - exp(-lam*dt*sum(s_i^alpha)), which lies in [0,1] for
any rate. Given a commit, pick site i with probability s_i^alpha / sum(s_j^alpha).
The absorbing backstop uses true absorption (last survivor) rather than a 0.995
share threshold.

RESULT: alpha=1 (golden-rule / rate-linear) reproduces Born at every commit speed;
alpha=2 and alpha=0.5 deviate as the theorem's converse predicts. No invalid
probabilities at any lam.
"""
import numpy as np

rng = np.random.default_rng(9)


def rate_commit_game(e0, alpha, lam, sigma=0.3, dt=0.02, eps=1e-9,
                     ntrials=4000, maxit=400_000):
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        ei = e[idx] + sigma * np.sqrt(e[idx]) * rng.normal(0, np.sqrt(dt), (idx.size, n))
        ei = np.where(ei < eps, 0.0, ei)
        e[idx] = ei
        tot = ei.sum(axis=1)
        alive = (ei > 0).sum(axis=1)
        s = ei / np.maximum(tot[:, None], 1e-12)
        sa = s ** alpha
        sa_sum = sa.sum(axis=1)
        p_commit = 1.0 - np.exp(-lam * dt * sa_sum)        # valid hazard in [0,1]
        commit = (rng.random(idx.size) < p_commit) | (alive <= 1)
        dead = tot <= eps
        commit &= ~dead
        if commit.any():
            sub = np.where(commit)[0]
            p = sa[sub] / np.maximum(sa_sum[sub][:, None], 1e-12)
            picks = (p.cumsum(axis=1) > rng.random(sub.size)[:, None]).argmax(axis=1)
            winners[idx[sub]] = picks
            active[idx[sub]] = False
        if dead.any():
            active[idx[dead]] = False
    w = winners[winners >= 0]
    return np.bincount(w, minlength=n) / max(len(w), 1), int((winners < 0).sum())


born = np.array([0.8, 0.2])
print("CORRECTED commit hazard p = 1 - exp(-lam*dt*sum s^alpha)  (always valid).")
print("2-site, Born=[0.8, 0.2].  lam=50 ~ fast commit; lam=0.5 ~ game concentrates first.")
print(f"{'alpha':>6} {'lam':>5} | {'P_1':>7} | {'dev':>8}  | max lam*dt*sum s^a (start)")
for alpha in (1.0, 2.0, 0.5):
    sa_sum0 = (born ** alpha).sum()
    for lam in (50.0, 5.0, 0.5):
        f, lost = rate_commit_game(born.copy(), alpha, lam)
        print(f"{alpha:>6} {lam:>5} | {f[0]:>7.4f} | {f[0]-born[0]:>+8.4f}  |"
              f" {lam*0.02*sa_sum0:.3f}  (no-result {lost})")

A = np.array([1.] * 9 + [3.]); b10 = A ** 2 / A.dot(A)
print("\n10-site stress config, bright Born=0.500, alpha=1 (golden rule):")
for lam in (50.0, 5.0, 0.5):
    f, lost = rate_commit_game(b10.copy(), 1.0, lam, ntrials=3000)
    print(f"  lam={lam:<5}: bright={f[-1]:.4f}  max|dev|={np.max(np.abs(f-b10)):.4f}  (no-result {lost})")
