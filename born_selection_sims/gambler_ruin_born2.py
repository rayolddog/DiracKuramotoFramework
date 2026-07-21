import numpy as np
rng = np.random.default_rng(11)

def fair_exchange_batch(e0, ntrials=3000, step=0.02, thresh=0.97, maxit=200000):
    """Vectorized: all trials exchange energy in fair random pairwise steps
    until one site holds >= thresh of total. Returns win frequencies."""
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        # random pair per active trial
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        d = step * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        # clip so no site goes negative
        d = np.clip(d, -e[idx, j], e[idx, i])
        e[idx, i] -= d
        e[idx, j] += d
        m = e[idx].max(axis=1)
        done = m >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    unfinished = (winners < 0).sum()
    w = winners[winners >= 0]
    freq = np.bincount(w, minlength=n) / max(len(w), 1)
    return freq, unfinished

configs = [
    [2.0, 1.0],
    [3.0, 2.0, 1.0],
    [1.0]*9 + [3.0],
]

for amps in configs:
    A = np.array(amps, float)
    e0 = A**2 / np.sum(A**2)
    freq, unf = fair_exchange_batch(e0)
    born = A**2/np.sum(A**2)
    print(f"A={np.round(amps,2)}  (unfinished trials: {unf})")
    print(f"  empirical: {np.round(freq,4)}")
    print(f"  Born:      {np.round(born,4)}   max|diff|={np.max(np.abs(freq-born)):.4f}")
