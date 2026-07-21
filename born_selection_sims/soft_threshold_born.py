import numpy as np
rng = np.random.default_rng(23)

def biased_exchange(e0, w, ntrials=3000, step=0.1, thresh=0.995, maxit=600000):
    """Gambler's ruin with rich-get-richer bias from a soft lock layer of
    fractional width w: beta(e) = min(1, w/(1-e)); pairwise direction prob
    toward i = 0.5 + (beta_i - beta_j)/4.  w=0 recovers the fair game."""
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        ei, ej = e[idx, i], e[idx, j]
        stake = step * np.minimum(ei, ej)
        if w > 0:
            bi = np.minimum(1.0, w / np.maximum(1 - ei, 1e-12))
            bj = np.minimum(1.0, w / np.maximum(1 - ej, 1e-12))
            p_toward_i = 0.5 + (bi - bj) / 4.0
        else:
            p_toward_i = 0.5
        d = stake * np.where(rng.random(idx.size) < p_toward_i, -1.0, 1.0)
        # d>0 means i loses to j; p_toward_i is prob energy flows to i
        e[idx, i] -= d
        e[idx, j] += d
        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    won = winners[winners >= 0]
    freq = np.bincount(won, minlength=n) / max(len(won), 1)
    return freq, (winners < 0).sum()

for amps in ([2.,1.], [1.]*9 + [3.]):
    A = np.array(amps); born = A**2/np.sum(A**2)
    print(f"\n=== A={np.round(amps,1)},  Born={np.round(born,3)} ===")
    for w in [0.0, 0.003, 0.01, 0.03, 0.1, 0.3]:
        freq, unf = biased_exchange(born.copy(), w)
        dev = np.max(np.abs(freq - born))
        tag = np.round(freq,3) if len(A)==2 else f"[dim~{freq[:-1].mean():.3f} bright {freq[-1]:.3f}]"
        print(f"  w={w:<6}: emp={tag}  max|dev|={dev:.4f}  (unfinished {unf})")
