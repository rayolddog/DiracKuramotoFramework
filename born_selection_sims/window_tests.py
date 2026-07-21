import numpy as np
rng = np.random.default_rng(5)

# --- Test A: commit-at-layer-entry. Pure fair game, absorbing boundary at 1-w.
# Measures boundary-placement error alone (no biased play inside the layer).
def fair_game_early_commit(e0, w, ntrials=4000, step=0.1, maxit=600000):
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    thresh = 1.0 - w
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, -1.0, 1.0)
        e[idx, i] -= d; e[idx, j] += d
        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    won = winners[winners >= 0]
    return np.bincount(won, minlength=n) / max(len(won), 1)

A = np.array([1.]*9 + [3.]); born = A**2/A.dot(A)
print("Test A: fair game, commit at layer entry (absorb at 1-w). 10-site, bright Born=0.500")
for w in [0.003, 0.01, 0.03, 0.1]:
    f = fair_game_early_commit(born.copy(), w)
    print(f"  w={w:<6}: bright={f[-1]:.4f}  max|dev|={np.max(np.abs(f-born)):.4f}")

# --- Test B: common-mode vs independent sqrt(e) noise (SDE), win at share>=0.9
def sde_game(shares0, mode, sigma=0.3, dt=0.02, ntrials=4000, maxit=300000):
    n = len(shares0)
    e = np.tile(np.asarray(shares0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        ei = e[idx]
        if mode == 'indep':
            dW = rng.normal(0, np.sqrt(dt), ei.shape)
        else:  # common: one shared Wiener increment per trial
            dW = np.repeat(rng.normal(0, np.sqrt(dt), (ei.shape[0], 1)), n, axis=1)
        ei = np.maximum(ei + sigma*np.sqrt(ei)*dW, 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        s = ei/np.maximum(tot[:, None], 1e-12)
        done = (s.max(axis=1) >= 0.9) & (tot > 1e-6)
        dead = tot <= 1e-6
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
        if dead.any(): active[idx[dead]] = False
    won = winners[winners >= 0]
    return np.bincount(won, minlength=n) / max(len(won), 1)

print("\nTest B: independent vs common-mode vacuum noise. 2-site, Born=[0.8, 0.2]")
b2 = np.array([0.8, 0.2])
for mode in ('indep', 'common'):
    f = sde_game(b2.copy(), mode)
    print(f"  {mode:>6}: emp={np.round(f,4)}  max|dev|={np.max(np.abs(f-b2)):.4f}")
