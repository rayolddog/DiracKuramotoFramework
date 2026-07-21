import numpy as np
rng = np.random.default_rng(42)

def sde_game(shares0, law, sigma=0.3, dt=0.02, thresh=0.9, ntrials=4000, maxit=300000):
    """de_i = sigma * amp(e_i) * dW_i, independent per site (vacuum noise).
    law: 'sqrt' (amplitude-linear coupling), 'add' (additive), 'lin' (multiplicative).
    Win when a site's SHARE exceeds thresh. Zero is absorbing (clip)."""
    n = len(shares0)
    e = np.tile(np.asarray(shares0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        ei = e[idx]
        if law == 'sqrt':  amp = np.sqrt(ei)
        elif law == 'add': amp = 0.3*np.ones_like(ei)
        elif law == 'lin': amp = ei
        ei = np.maximum(ei + sigma*amp*rng.normal(0, np.sqrt(dt), ei.shape), 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        dead = tot < 1e-6
        s = ei / np.maximum(tot[:,None], 1e-12)
        done = (s.max(axis=1) >= thresh) & ~dead
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
        if dead.any():
            active[idx[dead]] = False   # no-click outcome
    won = winners[winners >= 0]
    freq = np.bincount(won, minlength=n) / max(len(won), 1)
    return freq, (winners[~active[:0].repeat(0)] < 0).sum() if False else int((winners < 0).sum())

born10 = np.array([1.]*9 + [9.]); born10 /= born10.sum()   # bright site 3x amplitude
born3  = np.array([0.5, 0.3, 0.2])

for name, b in (("10-site [1x9, 3x amp]", born10), ("3-site [.5 .3 .2]", born3)):
    print(f"=== {name}:  Born = {np.round(b,3)} ===")
    for law in ('sqrt', 'add', 'lin'):
        freq, noclick = sde_game(b.copy(), law)
        dev = np.max(np.abs(freq - b))
        if len(b) > 3:
            summ = f"dim~{freq[:-1].mean():.3f}  bright {freq[-1]:.3f}"
        else:
            summ = np.round(freq, 3)
        print(f"  law={law:<5}: {summ}   max|dev|={dev:.4f}  (no-click {noclick})")
