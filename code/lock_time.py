#!/usr/bin/env python3
r"""
lock_time.py
============

User's idea (2026-06-13): the time for Stage-2 to reach equilibrium (lock) depends
on BOTH (i) the depth of the basin and (ii) the initial phase difference between the
arriving particle and the detector's reference phase.

Test it against the second-harmonic Adler dynamics that makes the two basins
(phi_dissipative_check.py):

        dphi/dt = -gamma sin(2 phi)         (detector reference at phi=0; basins at 0, pi)

phi0 = phase mismatch between particle and detector at arrival.

PART 1 confirms the intuition analytically + numerically:
    integrating to a basin gives   t_lock = (1/2gamma) * ln[ tan(phi0) / tan(phi_f) ],
    so  t_lock ~ 1/gamma            (deeper basin -> faster: dependence (i)), and
        t_lock -> infinity as phi0 -> pi/2  (the separatrix): the bigger the mismatch
        FROM THE NEAREST BASIN, the longer the lock -- diverging at maximal AMBIGUITY
        (equidistant from both pointers), which refines (ii).

PART 2 follows the idea to its consequence.  The SAME flow that sets the lock time
sets which basin you land in -- i.e. the OUTCOME PROBABILITY (the Born weight).  For
the equatorial state |psi> = (|L> + e^{i phi0}|R>)/sqrt2, Born says
        P(basin 0) = |<+x|psi>|^2 = cos^2(phi0/2).
We compute P(basin 0 | phi0) two ways:
    (a) classical Adler + THERMAL (additive) noise  -> a STEP/Boltzmann split about the
        separatrix pi/2  -- NOT cos^2(phi0/2).
    (b) quantum measurement backaction (QSD unraveling of D[sigma_x]) -> cos^2(phi0/2)
        EXACTLY (Born), because that noise is the state-dependent backaction.
=> The lock-time picture is correct and computable, but recovering Born REQUIRES the
   quantum (multiplicative) backaction; plain thermal locking gives the wrong measure.
   This is the open Born-measure problem, made concrete via the user's own idea.
"""

import numpy as np

# ----------------------------------------------------------------------------
# PART 1 -- deterministic lock time
# ----------------------------------------------------------------------------
def lock_time_deterministic(phi0, gamma, phi_f=1e-3, T=200.0, dt=1e-3):
    """Integrate dphi/dt=-gamma sin2phi from phi0; return time to come within phi_f
    of the nearest basin (0 or pi)."""
    phi = float(phi0)
    n = int(T / dt)
    for k in range(n):
        phi = phi + (-gamma * np.sin(2 * phi)) * dt
        d0 = abs(((phi) % (2*np.pi) + np.pi) % (2*np.pi) - np.pi)        # dist to 0
        dpi = abs(((phi - np.pi) % (2*np.pi) + np.pi) % (2*np.pi) - np.pi)  # dist to pi
        if min(d0, dpi) < phi_f:
            return k * dt
    return np.nan


def lock_time_analytic(phi0, gamma, phi_f=1e-3):
    """t = (1/2g) ln[tan(phi0)/tan(phi_f)] toward 0 (phi0<pi/2), mirrored toward pi."""
    p = phi0 if phi0 <= np.pi/2 else np.pi - phi0
    if p <= phi_f:
        return 0.0
    return (1.0 / (2 * gamma)) * np.log(np.tan(p) / np.tan(phi_f))


# ----------------------------------------------------------------------------
# PART 2a -- classical Adler + thermal (additive) noise: basin split
# ----------------------------------------------------------------------------
def basin_split_classical(phi0, gamma, D, n=4000, T=6.0, dt=2e-3, seed=0):
    rng = np.random.default_rng(seed)
    nsteps = int(T / dt)
    sq = np.sqrt(2 * D * dt)
    phi = np.full(n, float(phi0))
    for _ in range(nsteps):
        phi = phi - gamma * np.sin(2 * phi) * dt + sq * rng.standard_normal(n)
    # basin 0 if cos(phi) > 0  (closer to phi=0 than pi)
    return np.mean(np.cos(phi) > 0)


# ----------------------------------------------------------------------------
# PART 2b -- quantum backaction (QSD of continuous sigma_x measurement): basin split
# ----------------------------------------------------------------------------
def basin_split_qsd(phi0, gamma, n=4000, T=6.0, dt=2e-3, seed=0):
    """Vectorized stochastic-Schrodinger (QSD) for L=sqrt(gamma) sigma_x, H=0.
    Start |psi>=(|L>+e^{i phi0}|R>)/sqrt2 ; return fraction ending in basin 0 (<sx> >0)."""
    rng = np.random.default_rng(seed)
    nsteps = int(T / dt)
    psi0 = np.full(n, 1.0 / np.sqrt(2), dtype=complex)             # |L> amplitude
    psi1 = np.full(n, np.exp(1j * phi0) / np.sqrt(2), dtype=complex)  # |R> amplitude
    for _ in range(nsteps):
        ex = 2 * np.real(np.conj(psi0) * psi1)        # <sigma_x>
        a0 = psi1 - ex * psi0                          # (sx - ex) psi
        a1 = psi0 - ex * psi1
        b0 = a1 - ex * a0                              # (sx - ex)^2 psi
        b1 = a0 - ex * a1
        dW = rng.normal(0.0, np.sqrt(dt), n)
        psi0 = psi0 - 0.5 * gamma * b0 * dt + np.sqrt(gamma) * a0 * dW
        psi1 = psi1 - 0.5 * gamma * b1 * dt + np.sqrt(gamma) * a1 * dW
        nrm = np.sqrt(np.abs(psi0)**2 + np.abs(psi1)**2)
        psi0 /= nrm; psi1 /= nrm
    ex_final = 2 * np.real(np.conj(psi0) * psi1)
    return np.mean(ex_final > 0)


def main():
    print("=" * 74)
    print("PART 1 -- lock time vs (basin depth gamma, phase mismatch phi0)")
    print("  dphi/dt = -gamma sin(2 phi);  detector reference at phi=0")
    print("=" * 74)
    print("  (a) deeper basin = faster:  t_lock ~ 1/gamma")
    phi0 = np.radians(60.0)
    for g in [0.5, 1.0, 2.0, 4.0]:
        t = lock_time_deterministic(phi0, g)
        print(f"      gamma={g:4.1f}:  t_lock(phi0=60deg) = {t:6.2f}   (1/gamma={1/g:.2f}: "
              f"t*gamma={t*g:.2f})")
    print("\n  (b) bigger mismatch from nearest basin = longer; diverges at separatrix pi/2:")
    gamma = 1.0
    for deg in [10, 30, 60, 80, 89, 89.9]:
        p = np.radians(deg)
        t_num = lock_time_deterministic(p, gamma)
        t_ana = lock_time_analytic(p, gamma)
        print(f"      phi0={deg:5.1f}deg:  t_lock(num)={t_num:6.2f}  t_lock(analytic)={t_ana:6.2f}")
    print("  => t = (1/2gamma) ln[tan(phi0)/tan(phi_f)] : logarithmic divergence at pi/2.")
    print("     'maximal phase difference' that slows the lock = maximal AMBIGUITY")
    print("     (equidistant from both pointers), not distance to the far pointer.")

    print("\n" + "=" * 74)
    print("PART 2 -- the SAME flow sets the OUTCOME (Born weight).  P(basin 0 | phi0):")
    print("  Born target:  P = cos^2(phi0/2)   for |psi>=(|L>+e^{i phi0}|R>)/sqrt2")
    print("=" * 74)
    phis = np.radians(np.array([0, 15, 30, 45, 60, 75, 90, 120, 150, 180.0]))
    print("   phi0(deg)   Born cos^2      classical Adler+thermal    quantum backaction(QSD)")
    Pc, Pq, Pb = [], [], []
    for i, p in enumerate(phis):
        born = np.cos(p / 2)**2
        pc = basin_split_classical(p, gamma=2.0, D=0.15, seed=10 + i)
        pq = basin_split_qsd(p, gamma=4.0, seed=20 + i)
        Pc.append(pc); Pq.append(pq); Pb.append(born)
        print(f"     {np.degrees(p):5.0f}      {born:5.2f}            {pc:5.2f}                      {pq:5.2f}")
    Pc, Pq, Pb = map(np.array, (Pc, Pq, Pb))
    print(f"\n  RMS deviation from Born:  classical+thermal = {np.sqrt(np.mean((Pc-Pb)**2)):.3f}"
          f"   QSD backaction = {np.sqrt(np.mean((Pq-Pb)**2)):.3f}")
    print("  => classical thermal locking gives a STEP-like split about pi/2 (overcounts the")
    print("     nearer basin) -- NOT Born.  Only the quantum measurement BACKACTION reproduces")
    print("     cos^2(phi0/2).  So the user's lock-time picture is right and computable, but the")
    print("     Born WEIGHTS need the multiplicative backaction, not thermal sync (open problem).")

    make_figure(gamma, phis, Pc, Pq, Pb)


def make_figure(gamma, phis, Pc, Pq, Pb):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print(f"\n[figure skipped: {e}]")
        return
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))

    # (0,0) lock time vs phi0 for several gamma
    a = ax[0, 0]
    pp = np.radians(np.linspace(2, 178, 200))
    for g, c in zip([0.5, 1.0, 2.0], ["C0", "C1", "C2"]):
        t = [lock_time_deterministic(p, g) for p in pp]
        a.plot(np.degrees(pp), t, c, lw=2, label=f"$\\gamma={g}$")
    a.axvline(90, color="r", ls="--", lw=1, label="separatrix $\\pi/2$ (max ambiguity)")
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)")
    a.set_ylabel(r"lock time $t_{\rm lock}$")
    a.set_title("Lock time: diverges at the separatrix; $\\propto 1/\\gamma$")
    a.set_ylim(0, 8); a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    # (0,1) t * gamma collapse (shows 1/gamma scaling)
    a = ax[0, 1]
    for g, c in zip([0.5, 1.0, 2.0, 4.0], ["C0", "C1", "C2", "C3"]):
        t = np.array([lock_time_deterministic(p, g) for p in pp])
        a.plot(np.degrees(pp), t * g, c, lw=1.5, label=f"$\\gamma={g}$")
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)")
    a.set_ylabel(r"$\gamma\cdot t_{\rm lock}$ (rescaled)")
    a.set_title("Curves collapse $\\Rightarrow$ depth enters only as $1/\\gamma$")
    a.set_ylim(0, 6); a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    # (1,0) THE BORN PANEL: basin split vs phi0
    a = ax[1, 0]
    pd = np.degrees(phis)
    pp2 = np.linspace(0, 180, 200)
    a.plot(pp2, np.cos(np.radians(pp2)/2)**2, "k-", lw=2.5, label=r"Born $\cos^2(\phi_0/2)$")
    a.plot(pd, Pq, "C2o-", lw=1.5, ms=5, label="quantum backaction (QSD) = Born")
    a.plot(pd, Pc, "C3s--", lw=1.5, ms=5, label="classical Adler+thermal (STEP $\\neq$ Born)")
    a.axvline(90, color="0.6", ls=":", lw=1)
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)")
    a.set_ylabel(r"$P(\rm basin\ 0\ |\ \phi_0)$")
    a.set_title("Same flow sets the OUTCOME: only backaction gives Born")
    a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    # (1,1) deviation from Born
    a = ax[1, 1]
    a.bar(pd - 3, np.abs(Pc - Pb), width=6, color="C3", alpha=0.7, label="classical+thermal")
    a.bar(pd + 3, np.abs(Pq - Pb), width=6, color="C2", alpha=0.7, label="quantum backaction")
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)")
    a.set_ylabel(r"$|P - P_{\rm Born}|$")
    a.set_title("Deviation from Born: thermal sync fails, backaction succeeds")
    a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    fig.tight_layout()
    out = __file__.rsplit("/", 1)[0] + "/lock_time.png"
    fig.savefig(out, dpi=130)
    print(f"\n[figure written: {out}]")


if __name__ == "__main__":
    main()
