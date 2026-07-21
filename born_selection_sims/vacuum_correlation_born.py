import numpy as np
rng = np.random.default_rng(3)

def kernel(x, kind):
    """Vacuum noise correlation between sites at positions x (units of lambda)."""
    r = 2*np.pi*np.abs(x[:,None] - x[None,:])   # k*dr
    with np.errstate(divide='ignore', invalid='ignore'):
        if kind == 'scalar':
            C = np.where(r < 1e-9, 1.0, np.sin(r)/r)
        elif kind == 'perp':   # dipoles perpendicular to separation (theta=90)
            C = np.where(r < 1e-9, 1.0,
                         1.5*(np.sin(r)/r + np.cos(r)/r**2 - np.sin(r)/r**3))
        elif kind == 'para':   # dipoles along separation (theta=0)
            C = np.where(r < 1e-9, 1.0, 3.0*(np.sin(r)/r**3 - np.cos(r)/r**2))
    return C

def drift_bright(e, C, bright):
    """Normalized share-drift of the bright region: sum_i in B of [s_i Q - sqrt(e_i)(C sqrt e)_i]/E^2, E=1."""
    e = e/e.sum()
    sq = np.sqrt(e)
    Csq = C @ sq
    Q = sq @ Csq
    d = e*Q - sq*Csq
    return d[bright].sum()

# --- Study 1: drift of bright-half share vs fringe spacing d/lambda, three kernels
N = 80
V = 0.8
print("Study 1: initial drift of bright-region share (units sigma^2/E), pattern 1+V cos(2 pi x/d), V=0.8")
print(f"{'d/lam':>6} | {'scalar':>10} | {'perp pol':>10} | {'para pol':>10}")
for dol in [0.5, 0.75, 1.0, 2.0, 3.0, 5.0, 10.0]:
    x = np.linspace(0, 2*dol, N, endpoint=False)        # two fringe periods, units of lambda
    inten = 1 + V*np.cos(2*np.pi*x/dol)
    e0 = inten/inten.sum()
    bright = np.cos(2*np.pi*x/dol) > 0
    row = []
    for kind in ('scalar','perp','para'):
        C = kernel(x, kind)
        row.append(drift_bright(e0, C, bright))
    print(f"{dol:>6} | {row[0]:>10.5f} | {row[1]:>10.5f} | {row[2]:>10.5f}")
Ccom = np.ones((N,N))
x = np.linspace(0, 1.0, N, endpoint=False)
inten = 1 + V*np.cos(2*np.pi*x/0.5)
print(f"(reference, fully common noise, d/lam=0.5: {drift_bright(inten/inten.sum(), Ccom, np.cos(2*np.pi*x/0.5)>0):.5f})")

# --- Study 2: full correlated game, scalar kernel, win freq of bright region vs Born
def corr_game(dol, kind, ntrials=1500, N=40, V=0.8, sigma=0.3, dt=0.02, win=0.7, maxit=60000):
    x = np.linspace(0, 2*dol, N, endpoint=False)
    inten = 1 + V*np.cos(2*np.pi*x/dol)
    e0 = inten/inten.sum()
    bright = np.cos(2*np.pi*x/dol) > 0
    born_frac = e0[bright].sum()
    if kind == 'indep':
        L = np.eye(N)
    else:
        C = kernel(x, kind)
        lam, U = np.linalg.eigh(C)
        L = U * np.sqrt(np.clip(lam, 0, None))
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool); winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        z = rng.normal(0, 1, (idx.size, N))
        dW = (z @ L.T) * np.sqrt(dt)
        ei = np.maximum(e[idx] + sigma*np.sqrt(e[idx])*dW, 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        s = ei/np.maximum(tot[:,None], 1e-12)
        done = (s.max(axis=1) >= win) & (tot > 1e-6)
        dead = tot <= 1e-6
        if done.any():
            fin = idx[done]; winners[fin] = e[fin].argmax(axis=1); active[fin] = False
        if dead.any(): active[idx[dead]] = False
    won = winners[winners >= 0]
    p_bright = bright[won].mean() if len(won) else float('nan')
    return p_bright, born_frac, ntrials - len(won)

print("\nStudy 2: full game, P(winner in bright half) vs Born fraction")
print(f"{'d/lam':>6} {'kernel':>7} | {'P_bright':>8} | {'Born':>6} | {'dev':>7}")
for dol in [0.5, 1.0, 2.0, 5.0]:
    for kind in ('indep','scalar'):
        p, b, lost = corr_game(dol, kind)
        print(f"{dol:>6} {kind:>7} | {p:>8.4f} | {b:>6.4f} | {p-b:>+7.4f}  (no-result {lost})")

# --- Study 3: mixed kernel C = (1-f) I + f C_scalar at d/lam = 0.5 — does deviation scale with f?
def corr_game_mixed(dol, f, ntrials=2000, N=40, V=0.8, sigma=0.3, dt=0.02, win=0.7, maxit=60000):
    x = np.linspace(0, 2*dol, N, endpoint=False)
    inten = 1 + V*np.cos(2*np.pi*x/dol)
    e0 = inten/inten.sum()
    bright = np.cos(2*np.pi*x/dol) > 0
    born_frac = e0[bright].sum()
    C = (1-f)*np.eye(N) + f*kernel(x, 'scalar')
    lam, U = np.linalg.eigh(C)
    L = U * np.sqrt(np.clip(lam, 0, None))
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool); winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        z = rng.normal(0, 1, (idx.size, N))
        dW = (z @ L.T) * np.sqrt(dt)
        ei = np.maximum(e[idx] + sigma*np.sqrt(e[idx])*dW, 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        s = ei/np.maximum(tot[:,None], 1e-12)
        done = (s.max(axis=1) >= win) & (tot > 1e-6)
        dead = tot <= 1e-6
        if done.any():
            fin = idx[done]; winners[fin] = e[fin].argmax(axis=1); active[fin] = False
        if dead.any(): active[idx[dead]] = False
    won = winners[winners >= 0]
    return (bright[won].mean() if len(won) else float('nan')), born_frac, ntrials - len(won)

print("\nStudy 3: mixed noise, d/lam=0.5 — deviation vs correlated fraction f")
for f in [1.0, 0.3, 0.1, 0.03, 0.0]:
    p, b, lost = corr_game_mixed(0.5, f)
    print(f"  f={f:<5}: P_bright={p:.4f}  Born={b:.4f}  dev={p-b:+.4f}  (no-result {lost})")
