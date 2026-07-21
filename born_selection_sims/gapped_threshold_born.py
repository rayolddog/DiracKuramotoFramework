import numpy as np
rng = np.random.default_rng(23)

def biased_exchange(e0, w, profile, ntrials=3000, step=0.1, thresh=0.995, maxit=600000):
    """Gambler's ruin; bias beta(e): 'tail' = min(1, w/(1-e)) [old worst case, Adler tail],
    'gapped' = 1 if (1-e)<=w else 0 [slaved below layer, per derivation]."""
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    def beta(x):
        if profile == 'tail':
            return np.minimum(1.0, w / np.maximum(1 - x, 1e-12))
        return (1 - x <= w).astype(float)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        ei, ej = e[idx, i], e[idx, j]
        stake = step * np.minimum(ei, ej)
        p_toward_i = 0.5 + (beta(ei) - beta(ej)) / 4.0 if w > 0 else 0.5
        d = stake * np.where(rng.random(idx.size) < p_toward_i, -1.0, 1.0)
        e[idx, i] -= d
        e[idx, j] += d
        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    won = winners[winners >= 0]
    freq = np.bincount(won, minlength=n) / max(len(won), 1)
    return freq, int((winners < 0).sum())

A = np.array([1.]*9 + [3.]); born = A**2/np.sum(A**2)
print(f"Born: dim {born[0]:.4f} each, bright {born[-1]:.4f}\n")
print(f"{'w':>7} | {'tail: max|dev|':>15} | {'gapped: max|dev|':>17}")
for w in [0.003, 0.01, 0.03, 0.1]:
    ft, _ = biased_exchange(born.copy(), w, 'tail')
    fg, _ = biased_exchange(born.copy(), w, 'gapped')
    dt_ = np.max(np.abs(ft - born)); dg = np.max(np.abs(fg - born))
    print(f"{w:>7} | {dt_:>15.4f} | {dg:>17.4f}   (gapped bright={fg[-1]:.3f})")
