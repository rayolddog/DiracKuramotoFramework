import numpy as np
rng = np.random.default_rng(53)

def port_game(Splus, c_plus, c_minus=0.0, m=4, ntrials=20000, sigma=0.3, dt=0.02, win=0.7, maxit=60000):
    """Two ports x m sites. Port+ sites share noise at correlation c_plus (block),
    port- at c_minus. Fair sqrt(e) exchange otherwise. Returns P(winning site in port+)."""
    n = 2*m
    e0 = np.concatenate([np.full(m, Splus/m), np.full(m, (1-Splus)/m)])
    C = np.eye(n)
    C[:m,:m] = c_plus + (1-c_plus)*np.eye(m)
    C[m:,m:] = c_minus + (1-c_minus)*np.eye(m)
    lam, U = np.linalg.eigh(C)
    L = U*np.sqrt(np.clip(lam,0,None))
    e = np.tile(e0,(ntrials,1))
    active = np.ones(ntrials,bool); winners = np.full(ntrials,-1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        dW = (rng.normal(0,1,(idx.size,n)) @ L.T)*np.sqrt(dt)
        ei = np.maximum(e[idx]+sigma*np.sqrt(e[idx])*dW, 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        s = ei/np.maximum(tot[:,None],1e-12)
        done = (s.max(axis=1)>=win)&(tot>1e-6)
        dead = tot<=1e-6
        if done.any():
            fin = idx[done]; winners[fin] = e[fin].argmax(axis=1); active[fin]=False
        if dead.any(): active[idx[dead]] = False
    w = winners[winners>=0]
    return (w < m).mean(), ntrials-len(w)

print("P(port+) vs input share S+, port+ internally correlated at c, port- independent (m=4/port)")
print(f"{'S+':>5} | {'c=0 (sym)':>10} | {'c=0.5':>8} | {'c=1.0':>8} |  deviation(c=1)")
for S in (0.2, 0.35, 0.5, 0.65, 0.8):
    r0,_ = port_game(S, 0.0)
    r5,_ = port_game(S, 0.5)
    r1,nl = port_game(S, 1.0)
    print(f"{S:>5} | {r0:>10.4f} | {r5:>8.4f} | {r1:>8.4f} |  {r1-S:+.4f}  (no-click {nl})")

print("\nControl: BOTH ports correlated c=1 (matched collective structure):")
for S in (0.5, 0.8):
    r,_ = port_game(S, 1.0, 1.0)
    print(f"  S+={S}: P(port+)={r:.4f}  dev={r-S:+.4f}  (matched ports -> fair)")

print("\nMatched-ports control at c=0.5 both (non-degenerate):")
for S in (0.2, 0.5, 0.8):
    r,nl = port_game(S, 0.5, 0.5)
    print(f"  S+={S}: P(port+)={r:.4f}  dev={r-S:+.4f}  (no-click {nl})")
print("\nWeak-mismatch scaling (port+ c, port- 0), S+=0.5:")
for c in (0.1, 0.25, 0.5):
    r,nl = port_game(0.5, c)
    print(f"  c={c}: P(port+)={r:.4f}  dev={r-0.5:+.4f}")
