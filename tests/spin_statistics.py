"""
spin_statistics.py — Spin-Statistics Within the Many Clocks Framework
======================================================================

QUESTION:
─────────
Can the Many Clocks Interpretation (MCI) of the Dirac equation, with its
chiral clock pair (ψ_L, ψ_R) coupled by the off-diagonal chiral coupling
K = m (Eq. 3 of PAPER_UNIFIED.md), reproduce the spin-statistics theorem?
And if so, where does the fermion sign live in its mathematical structure?

CLAIM TESTED:
─────────────
The −1 phase under fermion exchange comes from the SU(2) representation
each chiral spinor carries — NOT from the chiral-pair phase dynamics.
MCI reproduces spin-statistics geometrically (via the 2π = −1 fact for
spinors plus the Feynman/Finkelstein continuous-deformation argument that
exchange ≃ 2π rotation in 3+1D), but it does not derive it from the
phase ODEs alone.

This is a CONSISTENCY CHECK, not a new theorem. MCI is already committed
to the chiral clock pair through the mass coupling K = m. Given that
commitment, fermion antisymmetry is automatic — the framework localizes
the sign in the spinor frames χ_{L,R}, not in the phases φ_{L,R} or the
amplitudes ρ_{L,R} of the Madelung decomposition.

SIX TESTS:
──────────
A. 2π spatial rotation of a Dirac 4-spinor → −1 (chiral pair, std basis)
B. 2π rotation of a Weyl 2-spinor (single chirality) → −1
C. Two identical Dirac fermions in a spin singlet at the SAME momentum →
   full exchange gives −1.
D. Dirac entangled singlet (opposite momenta, Bell scenario from
   dirac_extension.py) → spin exchange gives −1 across all v/c, robust
   against the relativistic large/small mixing.
E. Scalar (single-clock) toy and spin-1 vector: 2π rotation and exchange
   both give +1 (Bose).
F. Kuramoto chiral-pair phase dynamics under classical particle exchange:
   the joint phase tuple is invariant — NO sign.

The contrast between A–D and F localizes the source of the sign: it is
structural (the SU(2) rep), not dynamical (the Kuramoto coupling).
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from dirac_extension import (
    σ1, σ2, σ3, I2, O2,
    dirac_spinor, singlet_dirac, singlet_pauli,
    energy, mixing_angle,
)


# ─── Rotation operators ───────────────────────────────────────────────

def spin_rotation_2(theta, axis='z'):
    """SU(2) rotation: U = exp(−i θ σ·n̂ / 2)."""
    s = {'x': σ1, 'y': σ2, 'z': σ3}[axis]
    return np.cos(theta/2) * I2 - 1j * np.sin(theta/2) * s


def spin_rotation_4(theta, axis='z'):
    """4×4 Dirac spin rotation: block_diag(SU(2), SU(2)).
    Σ = diag(σ, σ); U = exp(−i θ Σ·n̂ / 2)."""
    R = spin_rotation_2(theta, axis)
    return np.block([[R, O2], [O2, R]])


def spin_rotation_3(theta, axis='z'):
    """SO(3) rotation acting on a spin-1 vector."""
    c, s = np.cos(theta), np.sin(theta)
    if axis == 'z':
        M = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    elif axis == 'x':
        M = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    elif axis == 'y':
        M = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    return M.astype(complex)


def exchange_op(d=4):
    """SWAP on H_d ⊗ H_d.   P(|a⟩⊗|b⟩) = |b⟩⊗|a⟩."""
    P = np.zeros((d*d, d*d), dtype=complex)
    for i in range(d):
        for j in range(d):
            P[j*d + i, i*d + j] = 1.0
    return P


# ─── Test A: 2π rotation of Dirac 4-spinor ────────────────────────────

def test_a_dirac_2pi(p=1.0):
    print("\n" + "=" * 70)
    print("TEST A: 2π rotation of a Dirac 4-spinor (the chiral PAIR)")
    print("=" * 70)
    u = dirac_spinor(p, spin_up=True)
    print(f"  u(p={p}, ↑)  = {np.round(u.real, 4)}  (small/large ratio r = p/(E+m))")

    print(f"\n  Rotation around z, varying θ:")
    print(f"    {'θ/(2π)':>8}   {'⟨u|U(θ)|u⟩':>20}")
    for frac in [0.0, 0.5, 1.0, 1.5, 2.0]:
        theta = frac * 2 * np.pi
        U = spin_rotation_4(theta, 'z')
        amp = u.conj() @ U @ u
        print(f"    {frac:6.2f}   {amp.real:+.6f} {amp.imag:+.6f}j")

    U_2pi = spin_rotation_4(2*np.pi, 'z')
    is_minus_I = np.allclose(U_2pi, -np.eye(4))
    print(f"\n  U(2π, z) = −I (4×4)?  {is_minus_I}")
    print(f"  ⟹  2π rotation: u → −u   (sign = −1)")
    print(f"  Both upper and lower 2-blocks pick up −1 jointly:")
    print(f"  upper block at θ=2π:\n{np.round(U_2pi[:2,:2].real, 4)}")
    print(f"  lower block at θ=2π:\n{np.round(U_2pi[2:,2:].real, 4)}")


# ─── Test B: 2π rotation of a Weyl 2-spinor ───────────────────────────

def test_b_weyl_2pi():
    print("\n" + "=" * 70)
    print("TEST B: 2π rotation of a Weyl 2-spinor (single chirality)")
    print("=" * 70)
    chi = np.array([1, 0], dtype=complex)
    R_2pi = spin_rotation_2(2*np.pi, 'z')
    chi_rot = R_2pi @ chi
    print(f"  χ_↑               = {chi}")
    print(f"  R(2π, z) χ_↑      = {np.round(chi_rot, 6)}")
    print(f"  ⟹ Each chirality alone is in the spin-1/2 rep and picks up −1.")
    print(f"  The Dirac 4-spinor is the DIRECT SUM of two such doublets;")
    print(f"  each doublet contributes −1 to its own block.")


# ─── Test C: Two-fermion spin singlet at identical momentum ───────────

def test_c_identical_momentum_exchange(p=1.0):
    print("\n" + "=" * 70)
    print("TEST C: Two identical Dirac fermions, same momentum, spin-singlet")
    print("=" * 70)
    u_up = dirac_spinor(p, spin_up=True)
    u_dn = dirac_spinor(p, spin_up=False)
    psi = (np.kron(u_up, u_dn) - np.kron(u_dn, u_up)) / np.sqrt(2)
    print(f"  |Ψ⟩ = (u(p,↑) ⊗ u(p,↓) − u(p,↓) ⊗ u(p,↑)) / √2     (16-dim)")
    print(f"  ‖Ψ‖² = {(psi.conj() @ psi).real:.6f}")

    P = exchange_op(d=4)
    psi_swap = P @ psi
    overlap = (psi.conj() @ psi_swap).real
    print(f"  ⟨Ψ | P_full | Ψ⟩ = {overlap:+.6f}     (expect −1)")
    print(f"  ⟹  Two identical Dirac fermions in spin singlet are antisymmetric.")


# ─── Test D: Dirac entangled singlet, spin exchange across v/c ────────

def test_d_relativistic_robustness():
    print("\n" + "=" * 70)
    print("TEST D: Dirac entangled singlet (Bell scenario), spin exchange")
    print("=" * 70)
    print("  |Ψ⟩ = (u(+p,↑) ⊗ u(−p,↓) − u(+p,↓) ⊗ u(−p,↑)) / √2")
    print("  Spin exchange swaps the SU(2) spin labels on each side, holding")
    print("  the (+p, −p) momenta fixed. This isolates the spinor sign from")
    print("  any momentum-label permutation, and lets us scan v/c.\n")
    print(f"    {'p':>10}  {'v/c':>8}  {'θ_rel':>8}  {'⟨Ψ|P_spin|Ψ⟩':>18}")
    for p in [1e-4, 0.1, 0.5, 1.0, 5.0, 50.0]:
        psi = singlet_dirac(p)
        psi_swap = (np.kron(dirac_spinor(+p, False), dirac_spinor(-p, True))
                    - np.kron(dirac_spinor(+p, True),  dirac_spinor(-p, False))) / np.sqrt(2)
        sign = (psi.conj() @ psi_swap).real
        v_c = p / np.sqrt(p*p + 1.0)   # m = 1 natural units
        theta_rel = np.degrees(mixing_angle(p))
        print(f"    {p:10.4f}  {v_c:8.4f}  {theta_rel:6.1f}°   {sign:+.10f}")
    print("\n  ⟹  Sign is robust: relativistic mixing (large/small redistribution)")
    print("     does NOT erode the antisymmetry. The spinor sign is invariant.")


# ─── Test E: Scalar / vector — Bose statistics ────────────────────────

def test_e_scalar_and_vector():
    print("\n" + "=" * 70)
    print("TEST E: Scalar (single-clock) and spin-1 vector — Bose statistics")
    print("=" * 70)

    # Scalar: 1-component complex amplitude, no SU(2) structure
    print("  Scalar field ψ(x) = e^{iφ(x)}:")
    print("    Under spatial rotation: ψ → ψ (invariant, trivial rep)")
    print("    Two-scalar exchange: |ψ_A⟩|ψ_B⟩ → |ψ_B⟩|ψ_A⟩ = same product")
    print("    ⟹ scalar pair: sign = +1\n")

    # Vector (spin-1): 3-component object, integer rep
    v = np.array([1, 0, 0], dtype=complex)
    R_v = spin_rotation_3(2*np.pi, 'z')
    overlap = v.conj() @ R_v @ v
    print(f"  Spin-1 vector (e_x):")
    print(f"    R(2π, z) v = {np.round((R_v @ v).real, 6)}")
    print(f"    ⟨v | R(2π) | v⟩ = {overlap.real:+.6f}     (expect +1)")
    print(f"    ⟹  integer spin: sign = +1 (no Pauli sign on 2π)")

    # Two-vector symmetric exchange
    P3 = exchange_op(d=3)
    sym = (np.kron(v, np.array([0,1,0])) + np.kron(np.array([0,1,0]), v)) / np.sqrt(2)
    sym_swapped = P3 @ sym
    sign = (sym.conj() @ sym_swapped).real
    print(f"  Symmetric 2-vector state:  ⟨ψ|P|ψ⟩ = {sign:+.6f}  (expect +1, Bose)")


# ─── Test F: the chiral-pair phase dynamics carry no sign ─────────────

def kuramoto_evolve(phi0, K, omega, t_arr, delta_CP=0.0):
    """Two coupled chiral phases (φ_L, φ_R). This integrates the dissipative
    Adler/sine form for illustration; the point of Test F — that the phase
    dynamics carry no fermion sign — is independent of whether one uses the
    closed (cosine-in-phase, unitary, no attractor) or open (sine,
    dissipative) form. The −1 lives in the spinor frames χ_{L,R}, not φ_{L,R}."""
    phi = np.array(phi0, dtype=float)
    out = np.zeros((len(t_arr), 2))
    out[0] = phi

    def f(p):
        phiL, phiR = p
        return np.array([omega + K * np.sin(phiR - phiL + delta_CP),
                         omega + K * np.sin(phiL - phiR - delta_CP)])

    for i in range(1, len(t_arr)):
        dt = t_arr[i] - t_arr[i-1]
        k1 = f(phi)
        k2 = f(phi + dt*k1/2)
        k3 = f(phi + dt*k2/2)
        k4 = f(phi + dt*k3)
        phi = phi + dt*(k1 + 2*k2 + 2*k3 + k4)/6
        out[i] = phi
    return out


def test_f_kuramoto_no_sign():
    print("\n" + "=" * 70)
    print("TEST F: Kuramoto chiral-pair dynamics under classical exchange")
    print("=" * 70)
    K, omega = 1.0, 1.0
    t_arr = np.linspace(0, 10, 500)
    rng = np.random.default_rng(0)
    A0 = (rng.uniform(0, 2*np.pi), rng.uniform(0, 2*np.pi))
    B0 = (rng.uniform(0, 2*np.pi), rng.uniform(0, 2*np.pi))
    A_traj = kuramoto_evolve(A0, K, omega, t_arr)
    B_traj = kuramoto_evolve(B0, K, omega, t_arr)

    print(f"  Two clock pairs, identical (K, ω). Initial conditions:")
    print(f"    A: (φ_L, φ_R) = ({A0[0]:.4f}, {A0[1]:.4f})")
    print(f"    B: (φ_L, φ_R) = ({B0[0]:.4f}, {B0[1]:.4f})")

    def order(phi_L, phi_R):
        return np.abs((np.exp(1j*phi_L) + np.exp(1j*phi_R)) / 2)

    rA = order(A_traj[:,0], A_traj[:,1])
    rB = order(B_traj[:,0], B_traj[:,1])
    print(f"  Sync order parameter at end: |r_A| = {rA[-1]:.4f}, |r_B| = {rB[-1]:.4f}")
    print(f"  (1.0 = locked at φ_L − φ_R = 0)")

    print(f"\n  CLASSICAL EXCHANGE A↔B is the relabeling")
    print(f"     (φ_L^A, φ_R^A, φ_L^B, φ_R^B) ↦ (φ_L^B, φ_R^B, φ_L^A, φ_R^A)")
    print(f"  The Kuramoto ODE is invariant under this relabeling:")
    print(f"  the phases are real numbers in [0, 2π), the coupling is symmetric")
    print(f"  in (A, B), and there is no algebraic place a sign could appear.\n")
    print(f"  ⟹  Pure clock dynamics carry NO information about Fermi/Bose statistics.")
    print(f"     The fermion sign must come from the spinor structure layered")
    print(f"     over the Madelung decomposition (the χ_{{L,R}} factors), not")
    print(f"     from φ_{{L,R}} or ρ_{{L,R}}.")
    return t_arr, A_traj, B_traj, rA, rB


# ─── Plotting ─────────────────────────────────────────────────────────

def make_plots(t_arr, A_traj, B_traj, rA, rB):
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 10))
    fig.suptitle('Spin-Statistics in the Many Clocks Framework', fontsize=13)

    # Panel A: Rotation-overlap vs angle for different reps
    ax = axes[0, 0]
    theta = np.linspace(0, 4*np.pi, 400)
    u = dirac_spinor(1.0, True)
    chi = np.array([1, 0], dtype=complex)
    v3 = np.array([1, 0, 0], dtype=complex)

    amps_dirac = np.array([(u.conj() @ spin_rotation_4(t, 'z') @ u).real for t in theta])
    amps_weyl  = np.array([(chi.conj() @ spin_rotation_2(t, 'z') @ chi).real for t in theta])
    amps_v1    = np.array([(v3.conj() @ spin_rotation_3(t, 'z') @ v3).real for t in theta])
    amps_scalar = np.ones_like(theta)

    ax.plot(theta/np.pi, amps_scalar, 'green',  lw=2,                label='Scalar (spin 0)')
    ax.plot(theta/np.pi, amps_v1,     'blue',   lw=2,                label='Vector (spin 1)')
    ax.plot(theta/np.pi, amps_weyl,   'orange', lw=2,                label='Weyl 2-spinor (chiral half)')
    ax.plot(theta/np.pi, amps_dirac,  'red',    lw=2, linestyle='--',label='Dirac 4-spinor (chiral pair)')
    ax.axhline(0,  color='gray', lw=0.5)
    ax.axhline(1,  color='gray', lw=0.5, linestyle=':')
    ax.axhline(-1, color='gray', lw=0.5, linestyle=':')
    ax.axvline(2,  color='black', lw=0.8, linestyle='--', alpha=0.6, label='θ = 2π')
    ax.axvline(4,  color='black', lw=0.8, linestyle=':',  alpha=0.6, label='θ = 4π')
    ax.set_xlabel('θ / π')
    ax.set_ylabel('⟨ψ₀ | U(θ) | ψ₀⟩')
    ax.set_title('Rotation overlap vs angle\n'
                 'Spinors return to +1 only at 4π (the spin-statistics fact)')
    ax.legend(fontsize=8, loc='lower left')
    ax.grid(True, alpha=0.3)

    # Panel B: Exchange amplitudes (table)
    ax = axes[0, 1]
    ax.axis('off')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.text(5, 9.5, 'Exchange amplitudes  ⟨Ψ | P | Ψ⟩',
            ha='center', fontsize=11, fontweight='bold')
    ax.text(5, 9.0, '(P swaps the two single-particle factors)',
            ha='center', fontsize=8, color='gray')

    # Compute live values
    rows = []
    psi_pauli = singlet_pauli()
    P2 = exchange_op(d=2)
    rows.append(('Pauli spin-1/2 singlet',
                 (psi_pauli.conj() @ P2 @ psi_pauli).real))
    P4 = exchange_op(d=4)
    for p_val in [0.5, 1.0, 5.0]:
        u_up = dirac_spinor(p_val, True)
        u_dn = dirac_spinor(p_val, False)
        psi_id = (np.kron(u_up, u_dn) - np.kron(u_dn, u_up)) / np.sqrt(2)
        rows.append((f'Dirac id-momentum singlet (p={p_val})',
                     (psi_id.conj() @ P4 @ psi_id).real))
    # Symmetric scalar pair
    sc = np.array([1.0])
    rows.append(('Scalar pair (Bose)', 1.0))
    # Symmetric spin-1 pair
    v_a = np.array([1, 0, 0], dtype=complex)
    v_b = np.array([0, 1, 0], dtype=complex)
    sym = (np.kron(v_a, v_b) + np.kron(v_b, v_a)) / np.sqrt(2)
    rows.append(('Symmetric vector pair (Bose)',
                 (sym.conj() @ exchange_op(d=3) @ sym).real))

    for i, (label, val) in enumerate(rows):
        y = 8 - i*1.05
        col = 'crimson' if val < 0 else 'forestgreen'
        ax.text(0.3, y, label, fontsize=9.5)
        ax.text(8.5, y, f'{val:+.4f}', fontsize=10.5, ha='right',
                color=col, fontweight='bold', family='monospace')

    ax.text(5, 1.3,
            'Antisymmetry survives across all v/c (relativistic mixing).\n'
            'Bose pairs (scalar, symmetric vector): +1 at all momenta.',
            ha='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='mistyrose', alpha=0.85))

    # Panel C: Kuramoto dynamics (no sign)
    ax = axes[1, 0]
    ax.plot(t_arr, np.cos(A_traj[:,0]), label='cos φ_L^A', color='royalblue', lw=1.5)
    ax.plot(t_arr, np.cos(A_traj[:,1]), label='cos φ_R^A', color='royalblue', lw=1.5, linestyle='--')
    ax.plot(t_arr, np.cos(B_traj[:,0]), label='cos φ_L^B', color='darkorange', lw=1.5)
    ax.plot(t_arr, np.cos(B_traj[:,1]), label='cos φ_R^B', color='darkorange', lw=1.5, linestyle='--')
    ax.set_xlabel('t  (units of 1/K)')
    ax.set_ylabel('cos φ')
    ax.set_title('Kuramoto chiral-pair dynamics (Test F)\n'
                 'Classical exchange A↔B is a relabeling — no sign possible')
    ax.legend(fontsize=8, ncol=2, loc='lower left')
    ax.grid(True, alpha=0.3)

    # Panel D: Where the sign lives
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.text(5, 9.7, 'Where the fermion sign lives in MCI',
            ha='center', fontsize=11, fontweight='bold')

    summary = (
        'Madelung decomposition:\n'
        '   ψ_{L,R} = ρ_{L,R}^{1/2} · e^{iφ_{L,R}} · χ_{L,R}\n'
        '\n'
        'Phases φ_{L,R}:    real, mod 2π    — no sign possible.\n'
        'Amplitudes ρ_{L,R}: real, ≥ 0      — no sign possible.\n'
        'Spinor frames χ_{L,R}: SU(2) doublets\n'
        '   • χ → −χ under 2π rotation (the spinor double cover)\n'
        '   • Direct sum of two doublets (Dirac) → −1\n'
        '   • Trivial rep (scalar) → +1\n'
        '   • Tensor product → spin-1 → +1 (integer)\n'
        '\n'
        'CONCLUSION:\n'
        'MCI inherits spin-statistics from the SU(2) representation\n'
        'attached to each chiral clock, not from the Kuramoto ODEs.\n'
        'The coupling K = m gives mass; the SU(2) gives the sign.\n'
        'They are layered, not equivalent.'
    )
    ax.text(0.4, 9.0, summary, fontsize=8.7, va='top', family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.92))

    plt.tight_layout()
    plt.savefig(_HERE / 'spin_statistics.png', dpi=150)
    print("\nSaved: spin_statistics.png")


# ─── Main ─────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("SPIN-STATISTICS IN THE MANY CLOCKS FRAMEWORK")
    print("=" * 70)
    print("Testing: do MCI commitments reproduce Fermi/Bose statistics, and")
    print("where in the formalism does the −1 fermion sign live?")

    test_a_dirac_2pi(p=1.0)
    test_b_weyl_2pi()
    test_c_identical_momentum_exchange(p=1.0)
    test_d_relativistic_robustness()
    test_e_scalar_and_vector()
    t_arr, A_traj, B_traj, rA, rB = test_f_kuramoto_no_sign()

    make_plots(t_arr, A_traj, B_traj, rA, rB)

    print("""
╔══════════════════════════════════════════════════════════════════════╗
║   SPIN-STATISTICS IN THE MANY CLOCKS INTERPRETATION                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   QUESTION:  Does MCI derive spin-statistics?                        ║
║                                                                      ║
║   ANSWER:    It REPRODUCES the theorem; the sign comes from the      ║
║              SU(2) representation each chiral spinor carries, NOT    ║
║              from the Kuramoto sync dynamics.                        ║
║                                                                      ║
║   STRUCTURAL FACTS (Tests A–D):                                      ║
║     • Dirac 4-spinor under 2π rotation:        −1                    ║
║     • Weyl 2-spinor (single chirality):        −1                    ║
║     • Pauli singlet exchange:                  −1                    ║
║     • Dirac id-momentum singlet:               −1                    ║
║     • Dirac entangled singlet, all v/c:        −1                    ║
║     • Scalar / spin-1 vector:                  +1                    ║
║                                                                      ║
║   DYNAMICAL FACT (Test F):                                           ║
║     • Kuramoto evolution of (φ_L, φ_R) pairs is symmetric under      ║
║       classical particle relabeling. Phases are real numbers; no     ║
║       sign can emerge from the ODE alone.                            ║
║                                                                      ║
║   INTERPRETIVE TAKE:                                                 ║
║     MCI commits to the chiral pair (ψ_L, ψ_R) to give mass via       ║
║     K = m (Eq. 3 of PAPER_UNIFIED.md). The same chiral pair carries  ║
║     the spin-1/2 representation, and that representation is what     ║
║     forces 2π rotation to give −1 — which by Feynman/Finkelstein     ║
║     continuous deformation forces fermion antisymmetry under         ║
║     exchange in 3+1D.                                                ║
║                                                                      ║
║     Spin-statistics is reproduced, NOT derived anew. But the         ║
║     framework localizes the sign cleanly: it lives in the spinor     ║
║     frames χ_{L,R}, not in the phases φ_{L,R} or amplitudes          ║
║     ρ_{L,R}. The coupling K = m gives mass; the SU(2) gives the      ║
║     sign. They are layered, not equivalent.                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")


if __name__ == '__main__':
    run()
