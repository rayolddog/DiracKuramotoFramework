"""G3 probe: does a 'drain' preserve Born statistics, and does its TIMING decide?

JB's drain analogy (2026-07-04 discussion, recorded as a candidate exclusivity
mechanism): a drain opens at the interaction site and the packet goes down it.
The open question raised on 2026-08-31: is the drain an ATTRACTOR that pulls
during competition, or a SINK that opens only on commitment?

Three variants of one closed-pot fair game (sum_i e_i = 1, one quantum):
  A  fair        - pairwise stakes-scaled exchange only (paper Appendix D law)
  B  attractor   - aperture grows super-linearly with energy already held,
                   g_i ~ gamma * e_i^alpha, applied DURING competition
  C  commit-sink - identical to A until a site reaches the absorbing boundary;
                   the sink then opens and takes the quantum

No outcome is ever drawn from |A_i|^2. The winner is whoever reaches the
boundary first. Vectorized across trials.
"""
import numpy as np


def run(weights, variant, alpha=2.0, gamma=0.0, step=0.25, thresh=0.995,
        n_trials=20000, max_steps=200_000, seed=0):
    rng = np.random.default_rng(seed)
    w = np.asarray(weights, float)
    born = w / w.sum()
    N = len(w)

    e = np.tile(born, (n_trials, 1))
    winner = np.full(n_trials, -1, int)
    steps = np.zeros(n_trials, int)
    idx = np.arange(n_trials)          # original index of each active row

    for k in range(max_steps):
        T = e.shape[0]
        if T == 0:
            break
        # --- fair pairwise stakes-scaled exchange (zero drift on shares) ---
        i = rng.integers(0, N, size=T)
        off = rng.integers(1, N, size=T)
        j = (i + off) % N              # j != i
        r = np.arange(T)
        ei, ej = e[r, i], e[r, j]
        d = step * np.minimum(ei, ej) * np.where(rng.random(T) < 0.5, 1.0, -1.0)
        e[r, i] = ei + d
        e[r, j] = ej - d

        # --- the drain, if it pulls during competition ---
        if variant == "attractor" and gamma > 0.0:
            e += gamma * e**alpha
            e /= e.sum(axis=1, keepdims=True)     # closed pot

        # --- absorbing boundary: the sink opens here for variants A and C ---
        mx = e.max(axis=1)
        done = mx >= thresh
        if done.any():
            winner[idx[done]] = e[done].argmax(axis=1)
            steps[idx[done]] = k
            keep = ~done
            e, idx = e[keep], idx[keep]

    p = np.bincount(winner[winner >= 0], minlength=N) / max((winner >= 0).sum(), 1)
    return born, p, steps[winner >= 0].mean(), (winner < 0).sum()


def report(name, weights, variant, **kw):
    born, p, mean_k, unfin = run(weights, variant, **kw)
    dev = np.abs(p - born).max()
    flag = "" if unfin == 0 else f"  [{unfin} unfinished]"
    print(f"{name:<36} Born={np.round(born,3)}  got={np.round(p,3)}  "
          f"max|dev|={dev:.4f}  <steps>={mean_k:6.0f}{flag}")
    return dev


if __name__ == "__main__":
    ten = [1.0]*9 + [9.0]      # nine unit sites + one triple-amplitude: Born 0.5
    two = [2.0, 1.0]

    print("=== 2-site, energy ratio 2:1 (Born 0.667 / 0.333) ===")
    report("A  fair exchange", two, "fair", seed=1)
    report("C  commit-sink (= A pre-boundary)", two, "commit", seed=2)
    for g in (0.001, 0.01, 0.05):
        report(f"B  attractor gamma={g}", two, "attractor", gamma=g, seed=3)

    print("\n=== 10-site, bright-site Born 0.500 ===")
    report("A  fair exchange", ten, "fair", seed=11)
    report("C  commit-sink (= A pre-boundary)", ten, "commit", seed=12)
    for g in (0.001, 0.01, 0.05):
        report(f"B  attractor gamma={g}", ten, "attractor", gamma=g, seed=13)

    print("\n=== control: linear aperture alpha=1 must be share-neutral ===")
    report("B' alpha=1, gamma=0.05", ten, "attractor", gamma=0.05, alpha=1.0, seed=21)
