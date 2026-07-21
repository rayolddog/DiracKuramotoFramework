import numpy as np
rng = np.random.default_rng(31)

def closed_form(p, alpha, eps):
    c2, s2 = np.cos(alpha)**2, np.sin(alpha)**2
    sp = p*c2 + (1-p)*s2; sm = 1-sp
    return p*(c2*sp**eps + s2*sm**eps)/(sp**(1+eps) + sm**(1+eps))

def full_game(p, alpha, eps, ntrials=60000, sigma=0.3, dt=0.02, lam=5.0, maxit=4000):
    """Alice: nonlinear commit f(s)=s^(1+eps); Bob: linear, basis beta=0.
    Partially entangled sqrt(p)|00>+sqrt(1-p)|11>. Returns Bob's P(B=0)."""
    c2, s2 = np.cos(alpha)**2, np.sin(alpha)**2
    sA0 = p*c2 + (1-p)*s2
    # Bob conditionals given Alice outcome +/- at angle alpha
    pB0_given = {1: p*c2/max(sA0,1e-12), -1: p*s2/max(1-sA0,1e-12)}
    eA = np.column_stack([np.full(ntrials,sA0), np.full(ntrials,1-sA0)])
    eB = np.column_stack([np.full(ntrials,p), np.full(ntrials,1-p)])
    TA = rng.geometric(lam*dt, ntrials); TB = rng.geometric(lam*dt, ntrials)
    outA = np.zeros(ntrials,int); outB = np.zeros(ntrials,int)
    for t in range(1, maxit+1):
        mA = (outA==0)&(t<=TA); mB = (outB==0)&(t<=TB)
        if not (mA.any() or mB.any()): break
        for e,m in ((eA,mA),(eB,mB)):
            if m.any():
                e[m] = np.maximum(e[m]+sigma*np.sqrt(e[m])*rng.normal(0,np.sqrt(dt),(m.sum(),2)),0)
        # Alice commits (nonlinear pick)
        cA = (TA==t)&(outA==0)
        if cA.any():
            idx = np.where(cA)[0]
            tot = eA[idx].sum(axis=1); s = eA[idx,0]/np.maximum(tot,1e-12)
            fa = s**(1+eps); fb = (1-s)**(1+eps)
            outA[idx] = np.where(rng.random(idx.size) < fa/(fa+fb), 1, -1)
            need = idx[outB[idx]==0]   # resync Bob (linear conditional)
            for v in (1,-1):
                sel = need[outA[need]==v]
                if sel.size:
                    tB = eB[sel].sum(axis=1)
                    eB[sel,0] = tB*pB0_given[v]; eB[sel,1] = tB*(1-pB0_given[v])
        # Bob commits (linear pick); if Bob first, resync Alice (conditional, still committed nonlinearly later)
        cB = (TB==t)&(outB==0)
        if cB.any():
            idx = np.where(cB)[0]
            tot = eB[idx].sum(axis=1); s = eB[idx,0]/np.maximum(tot,1e-12)
            outB[idx] = np.where(rng.random(idx.size) < s, 1, -1)
            need = idx[outA[idx]==0]
            # conditional Alice shares given Bob=0/1 at beta=0: P(A=+|B=0)=c2 etc.
            for v,pa in ((1, c2), (-1, s2)):
                sel = need[outB[need]==v]
                if sel.size:
                    tA = eA[sel].sum(axis=1)
                    eA[sel,0] = tA*pa; eA[sel,1] = tA*(1-pa)
    good = (outA!=0)&(outB!=0)
    return (outB[good]==1).mean()

print("Partially entangled p=0.8; Alice nonlinear commit; Bob marginal P(B=0) vs Alice setting")
print(f"{'eps':>5} | {'M(a=0) form':>11} {'M(a=45) form':>12} {'dM form':>8} | {'M(a=0) game':>11} {'M(a=45) game':>12} {'dM game':>8}")
for eps in (0.0, 0.2, 0.5):
    f0, f45 = closed_form(0.8,0,eps), closed_form(0.8,np.pi/4,eps)
    g0, g45 = full_game(0.8,0,eps), full_game(0.8,np.pi/4,eps)
    print(f"{eps:>5} | {f0:>11.4f} {f45:>12.4f} {f0-f45:>+8.4f} | {g0:>11.4f} {g45:>12.4f} {g0-g45:>+8.4f}")
print("\nSymmetry protection at p=0.5, eps=0.5:")
f0, f45 = closed_form(0.5,0,0.5), closed_form(0.5,np.pi/4,0.5)
g0, g45 = full_game(0.5,0,0.5), full_game(0.5,np.pi/4,0.5)
print(f"  form: dM = {f0-f45:+.4f}   game: dM = {g0-g45:+.4f}   (both ~0)")
