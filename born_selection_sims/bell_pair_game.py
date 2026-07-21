import numpy as np
rng = np.random.default_rng(17)

def bell_game(a, b, eta, ntrials=40000, sigma=0.3, dt=0.02, lam=1.0, maxit=2000):
    """Two simultaneous local fair games (sqrt-e noise, 2 ports each), rate-linear
    commitment (constant total rate since shares sum to 1). First commit (preferred-
    foliation order) resyncs the other wing's shares to eta*conditional + (1-eta)*current.
    Returns outcomes (+-1) per wing, commit-order flags, no-click count."""
    delta = a - b
    # conditional P(B=+ | A=+/-) and P(A=+ | B=+/-) for |Phi+>, ports along analyzer axes
    condB = {1: np.array([np.cos(delta)**2, np.sin(delta)**2]),
            -1: np.array([np.sin(delta)**2, np.cos(delta)**2])}
    condA = condB  # symmetric for Phi+
    eA = np.full((ntrials,2), 0.5); eB = np.full((ntrials,2), 0.5)
    TA = rng.geometric(lam*dt, ntrials); TB = rng.geometric(lam*dt, ntrials)
    same = TA == TB
    TA[same] += (rng.random(same.sum() if same.any() else 0) < 0.5).astype(int) if same.any() else 0
    outA = np.zeros(ntrials, int); outB = np.zeros(ntrials, int)
    resynced = np.zeros(ntrials, bool)
    dead = np.zeros(ntrials, bool)
    def evolve(e, m):
        if not m.any(): return
        e[m] = np.maximum(e[m] + sigma*np.sqrt(e[m])*rng.normal(0, np.sqrt(dt), (m.sum(),2)), 0.0)
    def commit(e, m):
        tot = e[m].sum(axis=1)
        ok = tot > 1e-9
        s = e[m][:,0]/np.maximum(tot,1e-12)
        pick = np.where(rng.random(m.sum()) < s, 1, -1)
        return pick, ok
    for t in range(1, maxit+1):
        actA = (outA == 0) & ~dead & (t <= TA.clip(max=maxit))
        actB = (outB == 0) & ~dead & (t <= TB.clip(max=maxit))
        if not (actA.any() or actB.any()): break
        evolve(eA, actA); evolve(eB, actB)
        for wing in ('A','B'):
            T, out, e_self, e_oth, out_oth, cond = ((TA,outA,eA,eB,outB,condB) if wing=='A'
                                                    else (TB,outB,eB,eA,outA,condA))
            m = (T == t) & (out == 0) & ~dead
            if not m.any(): continue
            pick, ok = commit(e_self, m)
            idx = np.where(m)[0]
            dead[idx[~ok]] = True
            idx = idx[ok]; pick = pick[ok]
            out[idx] = pick
            # resync the other wing if it hasn't committed yet
            need = idx[(out_oth[idx] == 0) & ~resynced[idx]]
            pk = out[need]
            totO = e_oth[need].sum(axis=1)
            sO = e_oth[need]/np.maximum(totO[:,None],1e-12)
            for val in (1,-1):
                sel = pk == val
                if sel.any():
                    newS = eta*cond[val][None,:] + (1-eta)*sO[sel]
                    e_oth[need[sel]] = totO[sel][:,None]*newS
            resynced[need] = True
    good = (outA != 0) & (outB != 0)
    return outA[good], outB[good], (TA < TB)[good], (~good).sum()

# CHSH: S = E(a1,b1) - E(a1,b2) + E(a2,b1) + E(a2,b2)
a1, a2 = 0.0, np.pi/4
b1, b2 = np.pi/8, 3*np.pi/8
print("CHSH at standard angles; QM: S = 2*sqrt(2) = 2.828, local-realism bound 2")
for eta in (1.0, 0.9, 0.707, 0.5):
    Es, margA = {}, []
    for (aa,bb,key) in ((a1,b1,'11'),(a1,b2,'12'),(a2,b1,'21'),(a2,b2,'22')):
        oA,oB,firstA,nc = bell_game(aa,bb,eta)
        Es[key] = (oA*oB).mean()
        margA.append((bb, oA.mean()))
    S = Es['11'] - Es['12'] + Es['21'] + Es['22']
    print(f"  eta={eta:<5}: S = {S:+.3f}   (pred {2*np.sqrt(2)*eta:.3f})   "
          f"E11={Es['11']:+.3f} (pred {np.cos(2*(a1-b1)):+.3f})")
# no-signaling: A's marginal at a1 under b1 vs b2 (eta=1)
oA1,_,f1,_ = bell_game(a1,b1,1.0); oA2,_,f2,_ = bell_game(a1,b2,1.0)
print(f"\nNo-signaling: A marginal at a1: b=b1 -> {oA1.mean():+.4f}, b=b2 -> {oA2.mean():+.4f} (both ~0)")
print(f"Commit order: A first in {f1.mean()*100:.1f}% of trials (order-independence built into stats above)")
# order-resolved correlation check (eta=1): E when A first vs B first
oA,oB,firstA,_ = bell_game(a1,b1,1.0,ntrials=80000)
EA_first = (oA[firstA]*oB[firstA]).mean(); EB_first = (oA[~firstA]*oB[~firstA]).mean()
print(f"Order independence: E(a1,b1) = {EA_first:+.3f} (A first) vs {EB_first:+.3f} (B first), pred {np.cos(2*(a1-b1)):+.3f}")
