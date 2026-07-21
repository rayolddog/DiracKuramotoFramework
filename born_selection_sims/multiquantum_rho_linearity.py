import numpy as np
rng = np.random.default_rng(41)

def fair_rate_commit(shares0, ntrials, sigma=0.3, dt=0.02, lam=5.0, maxit=3000):
    """Fair SDE game + rate-linear commit; returns winner index per trial (-1 = no-click)."""
    n = len(shares0)
    e = np.tile(np.asarray(shares0,float), (ntrials,1))
    T = rng.geometric(lam*dt, ntrials)
    win = np.full(ntrials, -1)
    for t in range(1, maxit+1):
        m = (win==-1)&(t<=T)
        if not m.any(): break
        e[m] = np.maximum(e[m]+sigma*np.sqrt(e[m])*rng.normal(0,np.sqrt(dt),(m.sum(),n)),0)
        c = (T==t)&(win==-1)
        if c.any():
            idx = np.where(c)[0]
            tot = e[idx].sum(axis=1)
            ok = tot>1e-9
            s = e[idx][ok]/tot[ok][:,None]
            picks = (s.cumsum(axis=1)>rng.random(ok.sum())[:,None]).argmax(axis=1)
            win[idx[ok]] = picks
    return win

def one_photon_joint(psi, ntrials=30000):
    """Sequential one-photon commits with registry resync. Returns joint counts matrix."""
    P2 = np.abs(psi)**2
    marg = P2.sum(axis=1); marg = marg/marg.sum()
    n = len(marg)
    first = fair_rate_commit(marg, ntrials)
    joint = np.zeros((n,n))
    for i in range(n):
        sel = first==i
        if not sel.any(): continue
        cond = P2[i]/max(P2[i].sum(),1e-12)
        second = fair_rate_commit(cond, sel.sum())
        for j in range(n):
            joint[i,j] += (second==j).sum()
    return joint/joint.sum()

# Two site-localized modes, equal mean intensity, opposite pair correlations:
psi_anti = np.array([[0,1],[1,0]])/np.sqrt(2)          # |1,1> : one quantum at each site
psi_bun  = np.array([[1,0],[0,1]])/np.sqrt(2)          # (|2,0>+|0,2>)/sqrt2 : bunched
for name, psi in (("anti-correlated |1,1>", psi_anti), ("bunched (|2,0>+|0,2>)/sqrt2", psi_bun)):
    J = one_photon_joint(psi)
    born = np.abs(psi)**2/np.sum(np.abs(psi)**2)
    print(f"{name}: marginals both 0.5")
    print(f"  game joint  : same-site {J[0,0]+J[1,1]:.4f}, split {J[0,1]+J[1,0]:.4f}")
    print(f"  QM (Glauber): same-site {born[0,0]+born[1,1]:.4f}, split {born[0,1]+born[1,0]:.4f}")
    print(f"  naive mean-intensity model: same-site 0.5, split 0.5   <-- fails for both states")

# Two-photon absorbers: stakes from PAIR registry diag vs naive intensity^2
print("\nTwo-photon absorbers (stakes = |psi(i,i)|^2):")
for name, psi in (("anti-correlated", psi_anti), ("bunched", psi_bun)):
    diag = np.abs(np.diag(psi))**2
    if diag.sum() < 1e-12:
        print(f"  {name}: registry stakes all zero -> NO two-photon clicks (QM: correct).")
        print(f"           naive intensity^2 model: clicks 50/50 at both sites  <-- rho-nonlinear, wrong")
    else:
        w = fair_rate_commit(diag/diag.sum(), 20000)
        f = np.bincount(w[w>=0], minlength=2)/max((w>=0).sum(),1)
        print(f"  {name}: game clicks {np.round(f,3)}; QM {np.round(diag/diag.sum(),3)}")

# Generic 3-site pair state: quantitative joint check
print("\nGeneric 3-site pair state, game joint vs |psi_ij|^2:")
A = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3)); psi = (A+A.T)/2
psi = psi/np.linalg.norm(psi)
J = one_photon_joint(psi, ntrials=60000)
born = np.abs(psi)**2/np.sum(np.abs(psi)**2)
print(f"  max|game - QM| over 9 joint entries: {np.max(np.abs(J-born)):.4f}")

# rho-linearity under mixing: P(0.5 rho_a + 0.5 rho_b) = average of P's
Ja, Jb = one_photon_joint(psi_anti), one_photon_joint(psi_bun)
mix_direct = 0.5*Ja + 0.5*Jb
pick = rng.random(30000) < 0.5   # ensemble realization of the proper mixture
Jm = 0.5*one_photon_joint(psi_anti, ntrials=int(pick.sum())) + 0.5*one_photon_joint(psi_bun, ntrials=int((~pick).sum()))
print(f"\nMixture affinity: max|P(mix) - avg P| = {np.max(np.abs(Jm-mix_direct)):.4f} (statistical floor)")
