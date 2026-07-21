import numpy as np
rng = np.random.default_rng(9)

def rate_commit_game(e0, alpha, lam, sigma=0.3, dt=0.02, ntrials=4000, maxit=200000):
    """Fair share game (sqrt-e vacuum noise) + commitment as a rate process:
    per step, commit prob = lam*dt*sum(s_i^alpha); if commit, pick i w.p. s_i^alpha/sum.
    alpha=1 is the golden-rule (linear-in-occupation) law. Backstop absorb at s>=0.995."""
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        ei = np.maximum(e[idx] + sigma*np.sqrt(e[idx])*rng.normal(0, np.sqrt(dt), (idx.size, n)), 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        dead = tot <= 1e-6
        s = ei/np.maximum(tot[:,None], 1e-12)
        sa = s**alpha
        sa_sum = sa.sum(axis=1)
        commit = (rng.random(idx.size) < lam*dt*sa_sum) | (s.max(axis=1) >= 0.995)
        commit &= ~dead
        if commit.any():
            sub = np.where(commit)[0]
            p = sa[sub]/sa_sum[sub][:,None]
            picks = (p.cumsum(axis=1) > rng.random(sub.size)[:,None]).argmax(axis=1)
            winners[idx[sub]] = picks
            active[idx[sub]] = False
        if dead.any(): active[idx[dead]] = False
    won = winners[winners >= 0]
    return np.bincount(won, minlength=n)/max(len(won),1), int((winners<0).sum())

born = np.array([0.8, 0.2])
print("2-site, Born=[0.8, 0.2].  lam=50: commits ~instantly; lam=0.5: game concentrates first.")
print(f"{'alpha':>6} {'lam':>5} | {'P_1':>7} | {'dev':>7}")
for alpha in (1.0, 2.0, 0.5):
    for lam in (50.0, 5.0, 0.5):
        f, lost = rate_commit_game(born.copy(), alpha, lam)
        print(f"{alpha:>6} {lam:>5} | {f[0]:>7.4f} | {f[0]-born[0]:>+7.4f}  (no-result {lost})")

A = np.array([1.]*9+[3.]); b10 = A**2/A.dot(A)
print("\n10-site stress config, bright Born=0.500, alpha=1 (golden rule):")
for lam in (50.0, 5.0, 0.5):
    f, lost = rate_commit_game(b10.copy(), 1.0, lam, ntrials=3000)
    print(f"  lam={lam:<5}: bright={f[-1]:.4f}  max|dev|={np.max(np.abs(f-b10)):.4f}  (no-result {lost})")
