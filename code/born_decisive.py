#!/usr/bin/env python3
r"""
born_decisive.py
================

THE DECISIVE STEP.  born_noise_structures.py showed Born requires the Stage-2 noise
to be QND backaction of sigma_x:  D[sigma_x], whose phase noise is D(phi) ~ sin^2 phi
(vanishing at the pointer states).  Question: does the framework's OWN coupling --
the Dirac chiral structure plus the QED gauge vertex -- actually PRODUCE D[sigma_x],
or something else?

OPERATOR CONTENT (1+1D chiral reduction; psi=(psi_L,psi_R), the framework's basis):
    gamma^0=sigma_x, gamma^1=-i sigma_y, gamma^5=sigma_z
      charge density   j^0 = psi^dag psi          = I        (commutes -> no dissipation)
      spatial current  j^1 = psi-bar gamma^1 psi  = sigma_z  (chirality / current)
      scalar density   psi-bar psi                = sigma_x  (THE MASS CHANNEL)
      pseudoscalar     psi-bar i gamma^5 psi       = sigma_y
    System Hamiltonian:  H_S = -p sigma_z + m sigma_x   (kinetic + chiral mass)

COUPLINGS:
    * GAUGE (photon/vacuum) vertex  e j^mu A_mu  ->  bath couples via  I and sigma_z.
      The mass sigma_x is a c-number in H_S, NOT a fluctuating bath coupling.
    * To get D[sigma_x] you must couple the bath to the SCALAR DENSITY psi-bar psi
      = sigma_x -- i.e. a Yukawa/scalar field or a FLUCTUATING MASS (dynamical chiral
      condensate).  That is not the gauge vertex and is not in the present framework.

This script builds the Born-Markov (secular Bloch-Redfield) Lindblad dissipator that
each coupling actually produces, evolves an equatorial input state |psi(phi0)>, and
plots P(outcome +x | phi0) against the Born target cos^2(phi0/2).

PREDICTION (to be confirmed): the gauge sigma_z coupling gives, depending on regime,
  - p=0 (pure mass): sigma_z is TRANSVERSE to H_S=m sigma_x -> RELAXATION (amplitude
    damping) toward the sigma_x ground state.  T=0 -> monostable (one pointer); T>0 ->
    Boltzmann mixture.  Either way it ERASES phi0 -> flat, NOT Born.
  - large p: sigma_z is LONGITUDINAL -> pure DEPHASING in the chirality basis ->
    destroys the equatorial phase -> <sigma_x> -> 0 -> flat 0.5, NOT Born.
Only the scalar-density coupling A=sigma_x (commutes with the mass term) is QND ->
preserves the sigma_x populations -> reproduces Born.
"""

import numpy as np
from scipy.linalg import eigh, expm

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def secular_lindblad_ops(H, A, T, kappa, deph_rate):
    """Born-Markov secular (Bloch-Redfield) Lindblad operators for system-bath
    coupling H_int = A (x) B, bath temperature T (energy units).  Returns list of
    collapse operators in the computational basis.
    - relaxation/excitation at the Bohr gap Delta=E1-E0 with detailed balance,
    - pure dephasing from the diagonal (longitudinal) part of A (rate deph_rate, ~T)."""
    evals, V = eigh(H)                       # E0<=E1 ; columns of V are eigvecs
    Ae = V.conj().T @ A @ V                  # A in the energy eigenbasis
    Delta = evals[1] - evals[0]
    ops = []
    if Delta > 1e-9:
        nbar = 0.0 if T <= 0 else 1.0 / np.expm1(Delta / T)
        g_down = kappa * (1.0 + nbar)        # emission |0><1|
        g_up = kappa * nbar                  # absorption |1><0|
        # |0><1| and |1><0| in energy basis, weighted by the coupling matrix element
        Ldown_e = np.zeros((2, 2), dtype=complex); Ldown_e[0, 1] = Ae[0, 1]
        Lup_e = np.zeros((2, 2), dtype=complex);   Lup_e[1, 0] = Ae[1, 0]
        if abs(Ae[0, 1]) > 1e-12 and g_down > 0:
            ops.append(np.sqrt(g_down) * V @ Ldown_e @ V.conj().T)
        if abs(Ae[1, 0]) > 1e-12 and g_up > 0:
            ops.append(np.sqrt(g_up) * V @ Lup_e @ V.conj().T)
    # pure dephasing from the diagonal (commuting) part of A
    Ldiag_e = np.diag(np.diag(Ae))
    if np.linalg.norm(Ldiag_e) > 1e-12 and deph_rate > 0:
        ops.append(np.sqrt(deph_rate) * V @ Ldiag_e @ V.conj().T)
    return ops, evals


def liouvillian(H, cops):
    """Vectorized Lindblad superoperator (column-stacking convention)."""
    d = H.shape[0]
    Id = np.eye(d, dtype=complex)
    L = -1j * (np.kron(Id, H) - np.kron(H.T, Id))
    for C in cops:
        Cd = C.conj().T
        CdC = Cd @ C
        L += (np.kron(C.conj(), C)
              - 0.5 * np.kron(Id, CdC) - 0.5 * np.kron(CdC.T, Id))
    return L


def evolve_pop(phi0, H, A, T, kappa, deph_rate, t=40.0):
    """Evolve |psi(phi0)> under the dissipator from coupling A; return P(+x)=1/2(1+<sx>)."""
    cops, _ = secular_lindblad_ops(H, A, T, kappa, deph_rate)
    L = liouvillian(H, cops)
    psi0 = np.array([1.0, np.exp(1j * phi0)], dtype=complex) / np.sqrt(2)
    rho0 = np.outer(psi0, psi0.conj())
    rho_t = (expm(L * t) @ rho0.reshape(-1, order="F")).reshape(2, 2, order="F")
    sx_exp = np.real(np.trace(sx @ rho_t))
    return 0.5 * (1.0 + sx_exp)


def main():
    phis = np.radians(np.linspace(0, 180, 19))
    born = np.cos(phis / 2)**2

    print("=" * 80)
    print("OPERATOR CONTENT (1+1D chiral reduction):")
    print("  gauge vertex j^mu A_mu  ->  bath couples via  j^0=I  and  j^1=sigma_z")
    print("  mass term  m*psi-bar*psi = m*sigma_x  is a c-number in H_S (no bath coupling)")
    print("  D[sigma_x] (needed for Born) requires coupling to scalar density psi-bar psi")
    print("  = a Yukawa/scalar field or FLUCTUATING MASS -- NOT the gauge vertex.")
    print("=" * 80)

    cases = [
        # (label, coupling A, p, m, T, kappa, deph_rate)
        ("GAUGE sigma_z, p=0  (pure mass), T=0   : relaxation -> ground",  sz, 0.0, 1.0, 0.0, 1.0, 0.0),
        ("GAUGE sigma_z, p=0  (pure mass), T=2m  : relaxation -> Boltzmann", sz, 0.0, 1.0, 2.0, 1.0, 0.0),
        ("GAUGE sigma_z, p=3m (kinetic-dominated): dephasing in chirality",  sz, 3.0, 1.0, 1.0, 1.0, 1.0),
        ("SCALAR sigma_x (fluctuating mass): QND  -> D[sigma_x]",            sx, 0.0, 1.0, 1.0, 1.0, 1.0),
    ]

    results = {}
    print(f"\n  phi0(deg):  " + "  ".join(f"{int(np.degrees(p)):4d}" for p in phis[::3]))
    print(f"  Born     :  " + "  ".join(f"{b:4.2f}" for b in born[::3]))
    print("  " + "-" * 70)
    for label, A, p, m, T, kappa, deph in cases:
        H = -p * sz + m * sx
        P = np.array([evolve_pop(ph, H, A, T, kappa, deph) for ph in phis])
        results[label] = P
        rms = np.sqrt(np.mean((P - born)**2))
        flat = P.max() - P.min()   # range; ~0 means phi0 erased
        print(f"  {label}")
        print(f"     P(+x):  " + "  ".join(f"{x:4.2f}" for x in P[::3])
              + f"   RMS vs Born={rms:.3f}  range(phi0)={flat:.2f}")

    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)
    print("  GAUGE coupling (sigma_z) does NOT reproduce Born in ANY regime:")
    print("   - p=0, T=0 : relaxes to the sigma_x ground state -> MONOSTABLE, phi0 erased.")
    print("   - p=0, T>0 : relaxes to a Boltzmann mixture       -> flat-ish, phi0 erased.")
    print("   - large p  : dephases in the chirality basis      -> <sx>->0, flat at 0.5.")
    print("  Only the SCALAR-DENSITY coupling A=sigma_x is QND (commutes with m sigma_x),")
    print("  preserves the sigma_x populations, and reproduces Born cos^2(phi0/2).")
    print("  But A=sigma_x = psi-bar psi is a coupling to a FLUCTUATING MASS / scalar")
    print("  condensate -- NOT the QED gauge vertex, and NOT present in the framework as")
    print("  written (mass is a fixed c-number).  => The chiral+gauge structure CANNOT")
    print("  close the Born gap; it gives the WRONG dissipator (relaxation/dephasing).")
    print("  The only escape hatch is to make the MASS itself a dynamical sync field")
    print("  coupling via psi-bar psi -- which the current framework explicitly disavows.")

    make_figure(phis, born, results)


def make_figure(phis, born, results):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print(f"\n[figure skipped: {e}]"); return
    fig, ax = plt.subplots(figsize=(9, 6))
    pd = np.degrees(phis)
    fine = np.linspace(0, 180, 200)
    ax.plot(fine, np.cos(np.radians(fine) / 2)**2, "k-", lw=3, label=r"Born $\cos^2(\phi_0/2)$ (target)")
    styles = {
        "GAUGE sigma_z, p=0  (pure mass), T=0   : relaxation -> ground":   ("C3", "s", "--", "gauge $\\sigma_z$, $p{=}0$, $T{=}0$ (relax$\\to$ground)"),
        "GAUGE sigma_z, p=0  (pure mass), T=2m  : relaxation -> Boltzmann": ("C1", "^", "--", "gauge $\\sigma_z$, $p{=}0$, $T{>}0$ (Boltzmann)"),
        "GAUGE sigma_z, p=3m (kinetic-dominated): dephasing in chirality":  ("C4", "v", "--", "gauge $\\sigma_z$, $p{\\gg}m$ (dephase$\\to$0.5)"),
        "SCALAR sigma_x (fluctuating mass): QND  -> D[sigma_x]":            ("C2", "o", "-",  "scalar $\\sigma_x$ = fluct. mass (QND $\\to$ Born)"),
    }
    for label, P in results.items():
        c, m, ls, leg = styles[label]
        ax.plot(pd, P, color=c, marker=m, ls=ls, lw=1.8, ms=6, label=leg)
    ax.axhline(0.5, color="0.7", lw=0.8, ls=":")
    ax.set_xlabel(r"phase mismatch $\phi_0$ (deg)")
    ax.set_ylabel(r"$P(+x\,|\,\phi_0)$  (outcome probability)")
    ax.set_title("Decisive test: does the chiral GAUGE coupling give Born?\n"
                 "Gauge $\\sigma_z$ erases $\\phi_0$ (no); only scalar $\\sigma_x$ (fluct. mass) gives Born")
    ax.set_xticks([0, 45, 90, 135, 180]); ax.set_ylim(-0.02, 1.02)
    ax.legend(fontsize=9); ax.grid(alpha=0.25)
    fig.tight_layout()
    out = __file__.rsplit("/", 1)[0] + "/born_decisive.png"
    fig.savefig(out, dpi=130)
    print(f"\n[figure written: {out}]")


if __name__ == "__main__":
    main()
