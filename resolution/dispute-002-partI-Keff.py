#!/usr/bin/env python3
"""
dispute-002-partI-Keff.py
=========================
Part I of the T6 retirement path (dispute-002-retirement-path.md): DERIVE the
Adler locking strength K_eff from a standard transmon + readout-cavity model,
discharging GPT-5.5 Major Concern #1 / dispute-001 ("the Adler equation is
asserted, not derived").

The chain, each link checked numerically (numpy + scipy only):

  (1a)  transmon dispersively coupled to a driven, decaying readout cavity
        --adiabatic elimination of the cavity-->  measurement-induced dephasing
        Gamma_phi = 8 chi^2 nbar / kappa   [standard; here verified from the full
        qubit+cavity Liouvillian spectrum].

  (1b)  the qubit master equation  rho' = -i[H,rho] + gamma D[sigma_x] rho,
        with H = (Omega/2) sigma_z (detuning/precession), reduces EXACTLY on the
        Bloch equator to the second-harmonic Adler equation
              phi_dot = Omega - K_eff sin(2 phi),   K_eff = gamma = Gamma_phi/2.
        => K_eff = 4 chi^2 nbar / kappa.   [verified: fit returns K_eff/gamma=1,
        spurious 1st-harmonic ~1e-15.]

  (1c)  that derived equation has SNIC (saddle-node-on-invariant-circle)
        universality -- exactly the T6 prediction:
          * sharp threshold at |Omega| = K_eff,
          * critical slowing Gamma_lock = 2 sqrt(K_eff^2 - Omega^2)  (exponent 1/2),
          * sub-threshold slips at <phi_dot> = sqrt(Omega^2 - K_eff^2).

Physical headline: the Heisenberg cut (locking onset) is a readout-power threshold
        nbar_crit = kappa |Omega| / (4 chi^2).
"""
import numpy as np
from numpy import kron
from scipy.linalg import eig, expm
from scipy.integrate import solve_ivp

# ---------------- superoperator helpers (column-stacking vec) ----------------
def liouvillian(H, cops):
    d = H.shape[0]; I = np.eye(d)
    L = -1j*(kron(I, H) - kron(H.T, I))
    for c in cops:
        cdc = c.conj().T @ c
        L += kron(c.conj(), c) - 0.5*(kron(I, cdc) + kron(cdc.T, I))
    return L

def unvec(v, d):
    return v.reshape(d, d, order='F')

def check_construction():
    N = 8; kappa = 1.0
    a = np.diag(np.sqrt(np.arange(1, N)), 1).astype(complex)
    L = liouvillian(np.zeros((N, N), complex), [np.sqrt(kappa)*a])
    rho0 = np.zeros((N, N), complex); rho0[1, 1] = 1.0
    t = 0.3
    nop = a.conj().T @ a
    nt = np.trace(nop @ unvec(expm(L*t) @ rho0.flatten('F'), N)).real
    rate = -np.log(nt)/t
    assert abs(rate - kappa) < 1e-3, "Liouvillian construction bug"
    print(f"[self-check] bare-cavity decay rate = {rate:.4f}  (= kappa = {kappa}) OK")

# ---------------- (1a) cavity -> Gamma_phi ----------------
def part1a(chi=0.05, kappa=1.0, eps=0.9, N=14):
    a = np.diag(np.sqrt(np.arange(1, N)), 1).astype(complex)
    Ic = np.eye(N); Iq = np.eye(2)
    sz = np.array([[1, 0], [0, -1]], complex)
    sp = np.array([[0, 1], [0, 0]], complex)
    A = kron(Iq, a); SZ = kron(sz, Ic); Splus = kron(sp, Ic)
    # dispersive readout in the frame rotating at the drive=cavity frequency
    H = chi*SZ@(A.conj().T@A) + eps*(A + A.conj().T)
    L = liouvillian(H, [np.sqrt(kappa)*A]); dim = 2*N
    w, vr = eig(L)
    iss = np.argmin(np.abs(w))
    rho_ss = unvec(vr[:, iss], dim); rho_ss /= np.trace(rho_ss)
    nbar = np.trace((A.conj().T@A) @ rho_ss).real
    overlaps = np.array([abs(np.trace(Splus.conj().T @ unvec(vr[:, k], dim)))
                         for k in range(len(w))])
    cand = np.where(-w.real > 1e-6, overlaps, -1)
    Gphi = -w[np.argmax(cand)].real
    Gphi_pred = 8*chi**2*nbar/kappa
    print("\n(1a) transmon+readout  ->  measurement-induced dephasing Gamma_phi")
    print(f"     chi={chi}  kappa={kappa}  eps={eps}  =>  nbar={nbar:.3f}")
    print(f"     Gamma_phi  numeric (qubit+cavity Liouvillian) = {Gphi:.5f}")
    print(f"     Gamma_phi  predicted  8 chi^2 nbar / kappa     = {Gphi_pred:.5f}")
    print(f"     agreement = {Gphi/Gphi_pred:.3f}")
    K_eff = Gphi/2
    print(f"     => K_eff = Gamma_phi/2 = {K_eff:.5f}   (4 chi^2 nbar/kappa = {4*chi**2*nbar/kappa:.5f})")
    return dict(chi=chi, kappa=kappa, nbar=nbar, Gphi=Gphi, K_eff=K_eff)

# ---------------- (1b) master eq -> Adler; fit K_eff ----------------
def bloch_rhs(t, r, Omega, gamma):
    x, y, z = r
    return [-Omega*y, Omega*x - 2*gamma*y, -2*gamma*z]

def part1b(gamma):
    Omega = 0.3*gamma
    sol = solve_ivp(bloch_rhs, [0, 40/gamma], [np.cos(0.6), np.sin(0.6), 0.05],
                    args=(Omega, gamma), dense_output=True, rtol=1e-10, atol=1e-12)
    ts = np.linspace(5/gamma, 20/gamma, 4000)        # late time: on the equator
    R = sol.sol(ts); phi = np.arctan2(R[1], R[0])
    phidot = np.gradient(np.unwrap(phi), ts)
    s2 = np.sin(2*phi)
    coef, *_ = np.linalg.lstsq(np.vstack([np.ones_like(s2), -s2]).T, phidot, rcond=None)
    Om_fit, K_fit = coef
    resid = phidot - (Om_fit - K_fit*s2)
    h1 = np.linalg.lstsq(np.vstack([np.sin(phi), np.cos(phi)]).T, resid, rcond=None)[0]
    print("\n(1b) qubit master eq (D[sx] + precession)  ->  phi_dot = Omega - K_eff sin2phi")
    print(f"     fitted K_eff / gamma = {K_fit/gamma:.4f}   (exact reduction => 1.0000)")
    print(f"     fitted Omega        = {Om_fit:.5f}   (input {Omega:.5f})")
    print(f"     spurious 1st-harmonic amplitude = {np.hypot(*h1):.1e}  (should be ~0)")

# ---------------- (1c) SNIC universality of the derived equation ----------------
def phi1d(t, ph, Om, K):
    return [Om - K*np.sin(2*ph[0])]

def relax_rate(Om, K):
    phistar = 0.5*np.arcsin(Om/K); Gpred = 2*np.sqrt(K**2 - Om**2); d0 = 0.01
    sol = solve_ivp(phi1d, [0, 25/Gpred], [phistar+d0], args=(Om, K),
                    dense_output=True, rtol=1e-12, atol=1e-14)
    tt = np.linspace(0, 25/Gpred, 12000); ph = sol.sol(tt)[0]
    dev = np.abs(ph - phistar); m = (dev < 0.6*d0) & (dev > 1e-4*d0)
    return -np.polyfit(tt[m], np.log(dev[m]), 1)[0]

def slip_rate(Om, K):
    Gpred = np.sqrt(Om**2 - K**2)
    sol = solve_ivp(phi1d, [0, 600*np.pi/Gpred], [0.0], args=(Om, K),
                    dense_output=True, rtol=1e-12, atol=1e-14, max_step=np.pi/Gpred/50)
    ph = sol.sol([0, 600*np.pi/Gpred])[0]
    return (ph[1]-ph[0])/(600*np.pi/Gpred)

def part1c(K):
    print("\n(1c) SNIC signatures of the DERIVED equation phi_dot = Omega - K_eff sin2phi")
    eps = np.array([0.10, 0.05, 0.02, 0.01, 0.005, 0.002])*K
    Glock = np.array([relax_rate(K-e, K) for e in eps])
    pred = 2*np.sqrt(K**2 - (K-eps)**2)
    p = np.polyfit(np.log(eps), np.log(Glock), 1)[0]
    print("     critical slowing  Gamma_lock vs 2 sqrt(K^2-Om^2):")
    for e, gn, gp in zip(eps, Glock, pred):
        print(f"        (K-|Om|)/K={e/K:6.3f}   num={gn:.5f}   pred={gp:.5f}   ratio={gn/gp:.3f}")
    print(f"     => critical-slowing exponent = {p:.3f}   (SNIC predicts 0.500)")
    print("     sub-threshold slips  <phi_dot> vs sqrt(Om^2-K^2):")
    sl_r = []
    for r in [1.02, 1.05, 1.1, 1.3, 1.6]:
        fs = slip_rate(r*K, K); pr = np.sqrt((r*K)**2 - K**2); sl_r.append((r, fs, pr))
        print(f"        Omega/K={r:4.2f}   num={fs:.5f}   pred={pr:.5f}   ratio={fs/pr:.3f}")
    return eps, Glock, sl_r

def figure(par, eps, Glock, sl_r):
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    except Exception as e:
        print(f"[figure skipped: {e}]"); return
    chi, kappa, K = par["chi"], par["kappa"], par["K_eff"]
    fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.2))
    # (1) Arnold tongue: K_eff = 4 chi^2 nbar/kappa vs nbar; locked region |Om|<K_eff
    nb = np.linspace(0, 2*par["nbar"], 200); Keff = 4*chi**2*nb/kappa
    ax[0].fill_between(nb, -Keff, Keff, color="C0", alpha=0.25, label="locked (record forms)")
    ax[0].plot(nb, Keff, "C0"); ax[0].plot(nb, -Keff, "C0")
    ax[0].axhline(0, color="k", lw=0.5)
    ax[0].scatter([par["nbar"]], [0.3*K], color="C3", zorder=5, label="example detuning Ω")
    ax[0].set_xlabel("readout photons  n̄"); ax[0].set_ylabel("detuning Ω")
    ax[0].set_title("Arnold tongue\nK_eff = 4χ²n̄/κ  (derived)"); ax[0].legend(fontsize=8)
    # (2) critical slowing log-log
    ax[1].loglog(eps/K, Glock, "o", color="C3", label="from master-eq reduction")
    xs = np.array([eps.min()/K, eps.max()/K])
    ax[1].loglog(xs, Glock[0]*(xs/(eps[0]/K))**0.5, "k--", label="slope ½ (SNIC)")
    ax[1].set_xlabel("(K_eff−|Ω|)/K_eff"); ax[1].set_ylabel("Γ_lock")
    ax[1].set_title("Critical slowing\nexponent ½"); ax[1].legend(fontsize=8)
    # (3) slip freq
    r = np.array([s[0] for s in sl_r]); num = [s[1] for s in sl_r]; pr = [s[2] for s in sl_r]
    ax[2].plot(pr, num, "o", color="C3", label="numeric")
    lim = [0, max(pr)*1.05]; ax[2].plot(lim, lim, "k--", label="√(Ω²−K_eff²)")
    ax[2].set_xlabel("√(Ω²−K_eff²)"); ax[2].set_ylabel("⟨φ̇⟩  (slip rate)")
    ax[2].set_title("Sub-threshold slips"); ax[2].legend(fontsize=8)
    fig.suptitle("Part I — K_eff and the SNIC cut, derived from the transmon+readout model", y=1.02)
    fig.tight_layout(); fig.savefig("dispute-002-partI-Keff.png", dpi=130, bbox_inches="tight")
    print("\n[figure written: dispute-002-partI-Keff.png]")

if __name__ == "__main__":
    print("="*74)
    print("PART I — deriving K_eff from the transmon + readout model")
    print("="*74)
    check_construction()
    par = part1a()
    part1b(par["K_eff"])
    eps, Glock, sl_r = part1c(par["K_eff"])
    print("\n" + "="*74)
    print("RESULT:  K_eff = 4 chi^2 nbar / kappa   (DERIVED, not asserted)")
    print("         Heisenberg cut = readout-power threshold  nbar_crit = kappa|Omega|/(4 chi^2)")
    print(f"         e.g. chi={par['chi']}, kappa={par['kappa']}: nbar_crit = {par['kappa']/(4*par['chi']**2):.0f} x |Omega|")
    print("="*74)
    figure(par, eps, Glock, sl_r)
