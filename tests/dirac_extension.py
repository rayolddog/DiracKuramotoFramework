"""
dirac_extension.py — Dirac Spinors as Time-Phase / Property Rotation
======================================================================

CENTRAL CLAIM (user's insight):
────────────────────────────────
The 4-component Dirac spinor exists because, for a moving particle,
the temporal-phase vector (energy clock: E/ℏ) and the spatial-phase
vector (momentum clock: p·x/ℏ) are NOT aligned. The spinor needs extra
components to track BOTH orientations simultaneously.

In the non-relativistic (NR) limit:
  - p → 0, spatial phase → 0
  - Time-phase vector and property (spin) vector are aligned
  - 2-component Pauli spinor suffices
  - Phase-clock model gives E(a,b) = -(1/2)cos(a-b)   ← "missing factor"

In the relativistic (Dirac) limit:
  - p ≠ 0, spatial phase present
  - Time-phase and property vectors are at angle θ_rel to each other
  - 4-component Dirac spinor required to track both
  - Full E(a,b) = -cos(a-b) is recovered by including the rotation term

THE MIXING ANGLE θ_rel:
────────────────────────
In the Dirac boost (natural units: m = c = ℏ = 1):

  tan(θ_rel / 2) = |p| / (E + m)   ←→   sin(θ_rel) = |p|/E = v/c = β

  v/c → 0:  θ_rel → 0   (NR: large component only, no rotation)
  v/c → 1:  θ_rel → π/2 (ultra-relativistic: equal large/small mixing)

LARGE vs SMALL COMPONENTS:
────────────────────────────
For a Dirac particle with momentum p along z:

  u(p, ↑) = N · [1,  0,  r,  0]^T       (upper: spin ∥ time-phase)
  u(p, ↓) = N · [0,  1,  0, -r]^T       (lower: spin ⊥ → spatial)

  where r = p/(E+m) = tan(θ_rel/2),   N = √((E+m)/2E)

  Large component (upper 2): encodes spin × temporal phase alignment
  Small component (lower 2): encodes spin × spatial phase alignment = ROTATION

THREE-TERM CORRELATION DECOMPOSITION:
──────────────────────────────────────
E(a, b) = E_LL + E_SS + E_LS

  E_LL: large-component × large-component  [temporal × temporal]
  E_SS: small-component × small-component  [spatial × spatial]
  E_LS: cross term                         [temporal × spatial = ROTATION COUPLING]

The block sum E_LL + E_SS + E_LS = E_full is an identity (additive by
trace linearity), not a derivation. What varies with momentum is the
*redistribution* of weight among the three blocks:
  At p → 0:  E_LL → -cos(a-b),  E_SS, E_LS → 0  (Pauli singlet recovered)
  At p = 1, m = 1:  the large-block restriction happens to give
                    ≈ -(1/2)cos(a-b), numerically coinciding with the
                    separate Malus-law stochastic phase toy in
                    bell_phase.py — the two models are mathematically
                    distinct and should not be conflated.
  At v/c → 1:  the three blocks contribute comparably.

CONNECTION TO ZITTERBEWEGUNG (PAPER_REVISED.md §2.4):
───────────────────────────────
Zitterbewegung is the interference between the positive- and negative-energy
normal modes (+E and −E) — the large and small Dirac components — whose
splitting is 2E, equal to 2mc²/ℏ at rest. This ±E normal-mode splitting IS
the beat; it is NOT the difference of a "temporal clock" ω_t = E/ℏ and a
"spatial clock" ω_s = p·v/ℏ (that difference tends to mc²/ℏ at rest, not
2mc²/ℏ). The de Broglie carrier is their symmetric mode at ω = E/ℏ.
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ─── Spinor utilities (shared; see spinor_utils.py) ──────────────────────────
# Pauli matrices, Dirac spinors, the mixing angle, the singlets, and the 4×4
# spin operators were factored out into spinor_utils.py so that this script and
# spin_statistics.py share a single source of truth.
from spinor_utils import (
    σ1, σ2, σ3, I2, O2,
    spin_op_2, energy, dirac_spinor, mixing_angle,
    singlet_dirac, singlet_pauli,
    spin_op_4, spin_op_large_only, spin_op_small_only,
)


# ─── Correlation computation ──────────────────────────────────────────────────

def correlation_full(a, b, p, m=1.0):
    """Full Dirac correlation: ⟨Ψ|(Σ_a)_A ⊗ (Σ_b)_B|Ψ⟩"""
    psi = singlet_dirac(p, m)
    OA = np.kron(spin_op_4(a), np.eye(4))
    OB = np.kron(np.eye(4), spin_op_4(b))
    return (psi.conj() @ OA @ OB @ psi).real


def correlation_large_large(a, b, p, m=1.0):
    """Large-component only: NR phase-clock model."""
    psi = singlet_dirac(p, m)
    OA = np.kron(spin_op_large_only(a), np.eye(4))
    OB = np.kron(np.eye(4), spin_op_large_only(b))
    return (psi.conj() @ OA @ OB @ psi).real


def correlation_small_small(a, b, p, m=1.0):
    """Small-component only: pure spatial-phase correlation."""
    psi = singlet_dirac(p, m)
    OA = np.kron(spin_op_small_only(a), np.eye(4))
    OB = np.kron(np.eye(4), spin_op_small_only(b))
    return (psi.conj() @ OA @ OB @ psi).real


def correlation_cross(a, b, p, m=1.0):
    """
    Cross term: large_A × small_B + small_A × large_B
    This is the ROTATION COUPLING — the user's insight.
    It encodes the angle between time-phase and property vectors.
    """
    e_full = correlation_full(a, b, p, m)
    e_ll   = correlation_large_large(a, b, p, m)
    e_ss   = correlation_small_small(a, b, p, m)
    return e_full - e_ll - e_ss


def correlation_nr_pauli(a, b):
    """Standard NR 4-component singlet correlation (reference)."""
    psi = singlet_pauli()
    s_a = spin_op_2(a)
    s_b = spin_op_2(b)
    OA = np.kron(s_a, I2)
    OB = np.kron(I2, s_b)
    return (psi.conj() @ OA @ OB @ psi).real


# ─── Main ────────────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("DIRAC EXTENSION: TIME-PHASE / PROPERTY ROTATION")
    print("=" * 70)

    # ── 1. Verify: full Dirac gives -cos(a-b) for several p values ────────
    print("\n1. Full Dirac correlation vs NR for Δ = π/4 (should be -cos(π/4) ≈ -0.707)")
    print(f"   NR Pauli (reference):                   {correlation_nr_pauli(0, np.pi/4):.6f}")
    for p in [0.01, 0.5, 1.0, 2.0, 10.0]:
        theta_rel = np.degrees(mixing_angle(p))
        e = correlation_full(0, np.pi/4, p)
        print(f"   p={p:.2f}  θ_rel={theta_rel:5.1f}°   E_full={e:.6f}  "
              f"(error from -cos: {e - (-np.cos(np.pi/4)):+.2e})")

    # ── 2. Decomposition into LL, SS, Cross ───────────────────────────────
    print("\n2. Three-term decomposition of E(0, π/4) at p = 1.0 (θ_rel ≈ 53°)")
    p = 1.0
    a, b = 0.0, np.pi / 4
    e_ll    = correlation_large_large(a, b, p)
    e_ss    = correlation_small_small(a, b, p)
    e_cross = correlation_cross(a, b, p)
    e_full  = correlation_full(a, b, p)
    e_qm    = -np.cos(a - b)
    print(f"   E_LL  (large×large, temporal×temporal): {e_ll:.6f}   [NR model gives this]")
    print(f"   E_SS  (small×small, spatial×spatial):   {e_ss:.6f}   [rotation contribution]")
    print(f"   E_LS  (cross: time×spatial rotation):   {e_cross:.6f}   [THE ROTATION TERM]")
    print(f"   ─────────────────────────────────────────────────")
    print(f"   E_LL + E_SS + E_LS = {e_ll+e_ss+e_cross:.6f}   (sum)")
    print(f"   E_full (direct):     {e_full:.6f}   (verification)")
    print(f"   −cos(a−b):           {e_qm:.6f}   (QM prediction ✓)")
    print(f"\n   Small-component contribution at this p: E_SS + E_LS = {e_ss+e_cross:.6f}")
    print(f"   (block weights redistribute with p; the sum is fixed by trace linearity)")

    # ── 3. Decomposition as function of θ_rel (momentum) ─────────────────
    print("\n3. Building E_full from components across all momenta:")
    p_arr    = np.logspace(-2, 2, 50)
    theta_arr = np.degrees([mixing_angle(p) for p in p_arr])

    e_ll_arr    = [correlation_large_large(0, np.pi/4, p) for p in p_arr]
    e_ss_arr    = [correlation_small_small(0, np.pi/4, p) for p in p_arr]
    e_cross_arr = [correlation_cross(0, np.pi/4, p) for p in p_arr]
    e_full_arr  = [correlation_full(0, np.pi/4, p) for p in p_arr]

    # ── 4. Verify for full angular sweep at p=1.0 ─────────────────────────
    deltas   = np.linspace(-np.pi, np.pi, 200)
    e_full_d = [correlation_full(0, d, 1.0) for d in deltas]
    e_ll_d   = [correlation_large_large(0, d, 1.0) for d in deltas]

    # ─── Plots ────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    fig.suptitle('Dirac Extension: Time-Phase/Property Rotation and Bell Correlations',
                 fontsize=13)

    # Panel A: correlation functions for p=1.0
    ax = axes[0, 0]
    ax.plot(np.degrees(deltas), -np.cos(deltas),     'royalblue',   lw=2.5, label='QM: −cos(Δ)')
    ax.plot(np.degrees(deltas), e_full_d,            'royalblue',   lw=1,   linestyle=':', label='Dirac full (verif.)')
    ax.plot(np.degrees(deltas), e_ll_d,              'darkorange',  lw=2,   linestyle='--', label='Dirac large-block only at p=1')
    ax.plot(np.degrees(deltas), -0.5*np.cos(deltas), 'darkorange',  lw=1,   linestyle=':', label='Malus toy reference (−½cos, separate model)')
    ax.fill_between(np.degrees(deltas), e_ll_d, -np.cos(deltas),
                    alpha=0.15, color='green', label='Gap filled by Dirac small component')
    ax.set_xlabel('Δ = a − b  (degrees)')
    ax.set_ylabel('E(a, b)')
    ax.set_title('Correlation at p = 1.0 (θ_rel ≈ 53°)\nDirac full vs large-component only')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel B: three-term decomposition vs θ_rel
    ax = axes[0, 1]
    ax.plot(theta_arr, e_ll_arr,    color='darkorange', lw=2,   label='E_LL: large×large (temporal)')
    ax.plot(theta_arr, e_ss_arr,    color='firebrick',  lw=2,   label='E_SS: small×small (spatial)')
    ax.plot(theta_arr, e_cross_arr, color='purple',     lw=2,   label='E_LS: cross (ROTATION term)')
    total = np.array(e_ll_arr) + np.array(e_ss_arr) + np.array(e_cross_arr)
    ax.plot(theta_arr, total,       color='royalblue',  lw=2.5, linestyle='--', label='Total (= QM)')
    ax.axhline(-np.cos(np.pi/4), color='royalblue', linestyle=':', lw=1, label='−cos(π/4) reference')
    ax.axvline(0, color='gray', lw=0.5)
    ax.set_xlabel('θ_rel (degrees)  [mixing angle between time-phase & property vectors]')
    ax.set_ylabel('Contribution to E(0, π/4)')
    ax.set_title('Three-term decomposition vs θ_rel\n'
                 'NR: θ=0, only E_LL.   Ultra-rel: θ=90°, all three contribute.')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel C: mixing angle vs v/c
    ax = axes[1, 0]
    v_c_arr = [p / np.sqrt(p**2 + 1) for p in p_arr]   # v/c = p/E (m=1)
    theta_rad = [mixing_angle(p) for p in p_arr]
    ax.plot(v_c_arr, np.degrees(theta_rad), 'purple', lw=2)
    ax.set_xlabel('v/c')
    ax.set_ylabel('θ_rel (degrees)')
    ax.set_title('Dirac mixing angle θ_rel vs v/c\n'
                 'tan(θ/2) = p/(E+m) = sin(θ) = v/c')
    for vc, label in [(0.1, 'v=0.1c'), (0.5, 'v=0.5c'), (0.866, 'v=0.87c'), (0.995, 'v=0.99c')]:
        theta_deg = np.degrees(np.arcsin(vc)) if vc < 1 else 90
        ax.axhline(theta_deg, color='gray', linestyle=':', lw=0.8)
        ax.text(0.02, theta_deg + 1, label, fontsize=8, color='gray')
    ax.grid(True, alpha=0.3)

    # Panel D: interpretation diagram
    ax = axes[1, 1]
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Draw time-phase vector and property vector at different angles
    theta_vals = [0, np.pi/8, np.pi/4, 3*np.pi/8]
    labels_verts = ['NR limit\nv/c≈0\nθ_rel=0°',
                    'Low rel.\nv/c=0.38\nθ_rel=22°',
                    'Mid rel.\nv/c=0.71\nθ_rel=45°',
                    'High rel.\nv/c=0.92\nθ_rel=67°']
    colors_v = ['navy', 'steelblue', 'darkorange', 'firebrick']

    for i, (theta, lbl, col) in enumerate(zip(theta_vals, labels_verts, colors_v)):
        cx, cy = 2 + i * 2, 6
        # Time-phase vector (fixed, pointing up)
        ax.annotate('', xy=(cx, cy + 1.5), xytext=(cx, cy),
                    arrowprops=dict(arrowstyle='->', color='royalblue', lw=2))
        # Property vector (rotated by theta)
        ax.annotate('', xy=(cx + 1.5*np.sin(theta), cy + 1.5*np.cos(theta)),
                    xytext=(cx, cy),
                    arrowprops=dict(arrowstyle='->', color=col, lw=2))
        # Angle arc
        arc_theta = np.linspace(np.pi/2, np.pi/2 - theta, 30)
        ax.plot(cx + 0.7*np.cos(arc_theta), cy + 0.7*np.sin(arc_theta), color='gray', lw=1)
        ax.text(cx - 0.5, cy - 1.2, lbl, fontsize=7, ha='center', color=col)

    ax.text(5, 9.0, 'Rotation between time-phase (↑) and property vectors (colored)',
            ha='center', fontsize=9, fontweight='bold')
    ax.text(5, 8.5, 'NR: vectors aligned → 2-component Pauli spinor sufficient',
            ha='center', fontsize=8, color='navy')
    ax.text(5, 8.1, 'Relativistic: rotation grows → 4-component Dirac spinor needed',
            ha='center', fontsize=8, color='firebrick')
    ax.text(1.2, 4.5, 'Time-\nphase', fontsize=8, color='royalblue', ha='center')
    ax.text(5.0, 4.0, '← increasing θ_rel →', fontsize=9, ha='center', color='gray')

    # Equation box
    ax.text(5, 2.8,
            'Dirac boost: tan(θ_rel/2) = p/(E+m)\n'
            'NR only (E_LL):     E = −½cos(a−b)\n'
            '+ Spatial (E_SS):  + δE_SS\n'
            '+ Rotation (E_LS): + δE_LS\n'
            '─────────────────────────────\n'
            'Total Dirac:        E = −cos(a−b)  ✓',
            ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig(_HERE / 'dirac_extension.png', dpi=150)
    print("\nSaved: dirac_extension.png")
    # plt.show()  # non-interactive backend (Agg); savefig above is sufficient

    # ── Summary ───────────────────────────────────────────────────────────
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║   DIRAC SPINOR INTERPRETATION IN THE TIME-PHASE MODEL               ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  WHY DIRAC NEEDS 4 COMPONENTS:                                       ║
║  The 4-component spinor encodes TWO alignments simultaneously:       ║
║    • Upper 2 (large): spin × temporal-phase clock  (ω = E/ℏ)        ║
║    • Lower 2 (small): spin × spatial-phase clock   (k = p/ℏ)        ║
║                                                                      ║
║  MIXING ANGLE θ_rel (property-time rotation):                        ║
║    tan(θ_rel/2) = |p|/(E+m)  ≡  sin(θ_rel) = v/c                   ║
║    θ_rel = 0:  NR, time and property vectors aligned                 ║
║    θ_rel = π/2: ultra-relativistic, equal mixing                    ║
║                                                                      ║
║  THREE-TERM BLOCK DECOMPOSITION (additive by trace linearity):       ║
║    E_LL (temporal × temporal)   → carries all weight at p → 0       ║
║    E_SS (spatial × spatial)     → small-component contribution       ║
║    E_LS (temporal × spatial)    → cross / rotation coupling          ║
║    Sum = -cos(a-b) is an identity, not a discovery                   ║
║    Block weights redistribute with v/c (the substantive content)     ║
║                                                                      ║
║  ZITTERBEWEGUNG (PAPER_REVISED.md §2.4):                             ║
║    Zbw beat = ±E normal-mode splitting (+E, −E), 2E = 2mc²/ℏ        ║
║    at rest.  NOT ω_t − ω_s (that gives mc²/ℏ at rest, not 2mc²/ℏ).  ║
║    de Broglie carrier = symmetric mode at ω = E/ℏ.                   ║
╚══════════════════════════════════════════════════════════════════════╝
""")


if __name__ == '__main__':
    run()
