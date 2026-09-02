"""threshold_gated_commit.py — ledger open item 2a (2026-09-02).

QUESTION. Paper 1 v0.8 section 6.1: in a continuum absorber a site can commit only while
its share exceeds theta = E_gap / E_photon (below theta there is no real final state).
The v0.8 top rung compares the leader's exposed climb t_exp (from theta to 1) with the
commit clock, and estimates t_exp with a one-step continuum formula that E-15 says is
least trustworthy at exactly that leg length. This script replaces the estimate with a
discrete-exchange measurement, and then asks what a theta-GATED commit channel does to
the outcome frequencies as a function of the dimensionless hazard

    r  =  lambda * t_exp0(theta)   ~  expected number of commit opportunities during
                                       the leader's exposed leg  (t_exp/tau_commit in
                                       section 6.1's notation),

for two commit laws: LINEAR in the holding (Theorem 5's golden-rule law, rate ~ e_i)
and ARRHENIUS (a barrier lowered by the deposit, rate ~ exp[beta (e_i - 1)]).

WHY THE GATE MATTERS EVEN FOR A LINEAR LAW. Theorem 4 needs the conditional pick at the
moment of firing to equal the share s_i for EVERY site. A gate sets the pick to zero for
every unexposed site, so a gated law is not Theorem 4's law unless nothing is gated
(theta -> 0, every site exposed) or nothing can fire (r -> 0, first passage). Reading A
of the share ontology therefore needs r << 1 in silicon; reading B (no gate) needs only
linearity. theta = 0 rows below are the ungated Theorem 4 control.

ENGINE. Same fair stakes-scaled exchange as theorem5_check.py: pick a pair (i, j), move
delta = +/- step * min(e_i, e_j) with fair sign. Per step, every EXPOSED site fires with
probability min(1, lambda * f(e_i)); the first to fire takes the whole quantum (P4(a));
if none fires and some site holds >= 0.995 the game absorbs there (first passage).
Exposure is measured at lambda = 0 as the number of steps the eventual winner spends above
theta before absorption: t_exp0(theta). lambda is then set to r / t_exp0.

Nothing here samples an outcome from |A_i|^2: the winner is whoever fires or absorbs.
"""

import sys
import time

import numpy as np


def run(weights, theta, law, lam, beta=10.0, step=0.25, n_trials=6000,
        max_steps=2_000_000, seed=0):
    """Return (born, p_win, mean_exposed_steps_of_winner, mean_game_steps)."""
    rng = np.random.default_rng(seed)
    w = np.asarray(weights, float)
    born = w / w.sum()
    N = len(w)
    e = np.tile(born, (n_trials, 1))
    idx = np.arange(n_trials)
    winner = np.full(n_trials, -1, int)
    exp_count = np.zeros((n_trials, N))          # steps each site spent above theta
    t_end = np.zeros(n_trials, int)
    for k in range(max_steps):
        T = e.shape[0]
        if T == 0:
            break
        i = rng.integers(0, N, size=T)
        j = (i + rng.integers(1, N, size=T)) % N
        rr = np.arange(T)
        ei, ej = e[rr, i], e[rr, j]
        d = step * np.minimum(ei, ej) * np.where(rng.random(T) < 0.5, 1.0, -1.0)
        e[rr, i] = ei + d
        e[rr, j] = ej - d

        exposed = e > theta
        exp_count[idx] += exposed

        anyfire = np.zeros(T, bool)
        if lam > 0 and exposed.any():
            f = e if law == "linear" else np.exp(beta * (e - 1.0))
            p = np.minimum(1.0, lam * f) * exposed
            fire = rng.random((T, N)) < p
            anyfire = fire.any(axis=1)
            if anyfire.any():
                ff = fire[anyfire].astype(float)
                ff /= ff.sum(axis=1, keepdims=True)
                cum = np.cumsum(ff, axis=1)
                u = rng.random((ff.shape[0], 1))
                winner[idx[anyfire]] = (u > cum).sum(axis=1)

        done = (~anyfire) & (e.max(axis=1) >= 0.995)
        if done.any():
            winner[idx[done]] = e[done].argmax(axis=1)

        gone = anyfire | done
        if gone.any():
            t_end[idx[gone]] = k + 1
            keep = ~gone
            e, idx = e[keep], idx[keep]
    if e.shape[0]:
        # unfinished trials: absorb at argmax (should not happen at these settings)
        winner[idx] = e.argmax(axis=1)
        t_end[idx] = max_steps
    p = np.bincount(winner, minlength=N) / n_trials
    win_exposed = exp_count[np.arange(n_trials), winner]
    return born, p, win_exposed.mean(), t_end.mean()


def mc_err(p, n):
    return np.sqrt(max(p * (1 - p), 1e-12) / n)


CONFIGS = {
    "2-site 0.80/0.20":            ([0.8, 0.2], -1),
    "10-site, bright 0.500 (paper)": ([1.0] * 9 + [9.0], -1),
    "100-site Gaussian fringe":     (list(np.exp(-((np.arange(100) - 50.0) ** 2) / (2 * 15.0 ** 2))), 50),
}
THETAS = [0.0, 0.02, 0.37, 0.45, 0.59, 0.72, 0.90, 0.94]   # 0 = ungated control; 0.02 ~ SNSPD proxy
RS = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0]
LAWS = ["linear", "arr"]

# Budget: the 100-site config is ~50x slower per run, so it gets a reduced grid.
GRID = {
    "2-site 0.80/0.20":            dict(thetas=THETAS, rs=RS, n=6000),
    "10-site, bright 0.500 (paper)": dict(thetas=THETAS, rs=RS, n=6000),
    "100-site Gaussian fringe":     dict(thetas=[0.0, 0.02, 0.45, 0.72, 0.90], rs=[0.03, 0.3, 3.0], n=1500),
}

out = open("results_threshold_gated_commit.txt", "w")


def emit(s=""):
    print(s)
    out.write(s + "\n")
    out.flush()


emit(__doc__)
t0 = time.time()
seed = 100
for name, (weights, bright) in CONFIGS.items():
    g = GRID[name]
    w = np.asarray(weights, float)
    born = w / w.sum()
    b_idx = int(np.argmax(born)) if bright < 0 else bright
    n = g["n"]
    emit("=" * 96)
    emit(f"{name}   N = {len(w)}   Born(bright site) = {born[b_idx]:.4f}   trials/run = {n}")
    emit("=" * 96)

    # 1. exposure at lambda = 0, per theta
    texp = {}
    emit(f"\n  Exposure at lambda = 0 (first passage only):")
    emit(f"  {'theta':>6}  {'t_exp0 (steps winner above theta)':>34}  {'game length (steps)':>20}  {'P(bright)':>10}")
    for th in g["thetas"]:
        seed += 1
        bn, p, tx, tg = run(w, th, "linear", 0.0, n_trials=n, seed=seed)
        texp[th] = max(tx, 1e-9)
        emit(f"  {th:6.2f}  {tx:34.1f}  {tg:20.1f}  {p[b_idx]:10.4f}")
    sys.stderr.write(f"[{time.time()-t0:6.0f}s] {name}: exposure done\n")

    # 2. gated commit sweep
    for law in LAWS:
        emit(f"\n  Deviation P(bright) - Born, commit law = {law.upper()}"
             f"{' (beta = 10)' if law == 'arr' else ''}; columns r = lambda * t_exp0; "
             f"MC 1-sigma ~ {mc_err(born[b_idx], n):.3f}")
        header = f"  {'theta':>6}" + "".join(f"{r:>9.2f}" for r in g["rs"])
        emit(header)
        for th in g["thetas"]:
            row = f"  {th:6.2f}"
            for r in g["rs"]:
                seed += 1
                lam = r / texp[th]
                bn, p, tx, tg = run(w, th, law, lam, n_trials=n, seed=seed)
                row += f"{p[b_idx] - born[b_idx]:+9.3f}"
            emit(row)
            sys.stderr.write(f"[{time.time()-t0:6.0f}s] {name} {law} theta={th}\n")

emit("\nRun time: %.0f s" % (time.time() - t0))
out.close()
