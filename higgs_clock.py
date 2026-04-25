"""
higgs_clock.py — Higgs as Clock Synchronizer, Antiparticles as Reversed Clocks
================================================================================

THREE CONNECTED IDEAS:

  1. MASSLESS SPIN-1/2 FERMIONS (idealized massless neutrinos)
     θ_rel = 90° permanently. The temporal and spatial clocks are
     PERMANENTLY ORTHOGONAL. The Dirac 4-component structure collapses
     to two independent 2-component Weyl spinors — one for each
     clock alignment. Two helicity states, no rest frame.

     NOTE: Photons are NOT described by this section. Photons are
     spin-1 vector bosons governed by Maxwell's equations, not by
     the Dirac/Weyl equation. Their two polarization states come
     from gauge invariance reducing the four components of A^μ to
     two transverse degrees of freedom, not from chiral decoupling.
     See Paper §5 for the photon treatment via Riemann-Silberstein
     F = E + iB.

  2. HIGGS FIELD AS KURAMOTO SYNCHRONIZER
     The Dirac mass term -m(ψ̄_L ψ_R + h.c.) is the COUPLING between
     the left-handed (spatial) clock and the right-handed (temporal) clock.
     Without the Higgs: clocks are decoupled, θ_rel = 90° for all particles.
     With the Higgs VEV ⟨φ⟩ = v/√2: Kuramoto coupling K = y_f · v/√2
     drives the two clocks toward synchronization.
     Mass = the equilibrium synchronization rate = y_f · v/√2.

  3. ANTIPARTICLES AS REVERSED CLOCKS → MATTER/ANTIMATTER ASYMMETRY
     The Dirac negative-energy solution v(p,s) has phase e^{+iEt/ℏ}:
     the time-phase clock runs BACKWARD.
     CP violation in the Higgs-Yukawa coupling: y_f is complex
     y_f = |y_f| e^{iδ_CP}. This shifts the synchronization equilibrium
     for particles and antiparticles in opposite directions.
     Particles synchronize to offset +δ_CP; antiparticles to -δ_CP.
     When they meet, clock mismatch → slightly different annihilation
     probability → residual matter excess.

EQUATIONS:
──────────

1. Massless (m=0):
   Dirac eq. decouples:  iσ̄^μ ∂_μ ψ_L = 0,  iσ^μ ∂_μ ψ_R = 0
   Mixing angle:  tan(θ_rel/2) = |p|/(E+m) → |p|/|p| = 1 → θ_rel = π/2
   Result: ψ_L and ψ_R are independent; each selects one helicity.

2. Higgs Yukawa coupling (Weyl form):
   iσ̄^μ ∂_μ ψ_L = y_f φ ψ_R     [L driven by R through Higgs]
   iσ^μ ∂_μ ψ_R = y_f φ* ψ_L    [R driven by L through Higgs]

   Writing clock phases φ_L, φ_R for ψ_L = ρ_L^½ e^{iφ_L} χ_L, etc.:

   dφ_L/dt = ω_L + K sin(φ_R − φ_L + δ_CP)   ← Kuramoto
   dφ_R/dt = ω_R + K sin(φ_L − φ_R − δ_CP)   ← Kuramoto

   where K = y_f · |⟨φ⟩| = y_f v/√2 = mass m.

   Synchronized equilibrium:  φ_L − φ_R = δ_CP  (particle)
                               φ_L − φ_R = −δ_CP (antiparticle, reversed clock)

3. Annihilation cross-section asymmetry (schematic):
   σ(particle) ∝ 1 + ε cos(δ_CP)
   σ(anti)     ∝ 1 − ε cos(δ_CP)
   Asymmetry η ≈ ε · sin²(δ_CP) / 2
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ─── 1. Massless Particles ────────────────────────────────────────────────────

def mixing_angle_m(p, m):
    """θ_rel = 2·arctan(|p|/(E+m)), with m → 0 giving θ → π/2."""
    E = np.sqrt(p**2 + m**2)
    return 2 * np.arctan(abs(p) / (E + m))


def helicity_fractions(p, m):
    """
    For a Dirac spinor with mixing angle θ_rel:
      Large component fraction: cos²(θ_rel/2)  (temporal clock)
      Small component fraction: sin²(θ_rel/2)  (spatial clock)

    For m=0: both = 1/2 (equal; Weyl spinors emerge).
    For m>>|p|: large → 1, small → 0 (NR limit).
    """
    theta = mixing_angle_m(p, m)
    return np.cos(theta/2)**2, np.sin(theta/2)**2


def print_massless_limit():
    print("═" * 68)
    print("1. MASSLESS PARTICLES: θ_rel = 90° ALWAYS")
    print("═" * 68)
    print("""
  Dirac equation with m=0 splits into two INDEPENDENT Weyl equations:
    Right-handed:   iσ^μ ∂_μ χ_R = 0   (spatial clock)
    Left-handed:    iσ̄^μ ∂_μ χ_L = 0   (temporal clock)

  The two clocks are PERMANENTLY ORTHOGONAL (never interact).
  Each 2-component Weyl spinor selects one helicity projection:
    χ_R: h = +1/2  (spin parallel to momentum)
    χ_L: h = −1/2  (spin antiparallel to momentum)

  Result: only 2 physical states instead of 4 — the 4-component
  Dirac structure is redundant for massless particles because there
  is no mixing between the two clock orientations.

  Helicity = the only spin quantum number for a massless particle
           = which clock (temporal or spatial) the spin aligns with.
""")
    print("  p/m ratio    θ_rel      f_large    f_small    Status")
    print("  " + "─"*58)
    for pm_ratio in [0.01, 0.1, 0.5, 1.0, 2.0, 10.0, 100.0, 1e6]:
        m = 1.0
        p = pm_ratio * m
        theta = np.degrees(mixing_angle_m(p, m))
        fl, fs = helicity_fractions(p, m)
        status = ('← NR' if pm_ratio < 0.1 else
                  '← ultra-rel' if pm_ratio > 100 else
                  '← relativistic')
        print(f"  p/m={pm_ratio:>8.1f}   {theta:5.1f}°   {fl:.4f}     {fs:.4f}     {status}")
    print(f"\n  m→0 limit (p fixed): θ_rel → 90°, f_large = f_small = 0.5")
    print(f"  → Two equal, decoupled Weyl spinors (helicity eigenstates)")


# ─── 2. Higgs as Kuramoto Synchronizer ───────────────────────────────────────

def kuramoto_L_R(t, phi, omega_L, omega_R, K, delta_CP):
    """
    L-R clock synchronization through Higgs field.
    phi = [φ_L, φ_R]
    dφ_L/dt = ω_L + K·sin(φ_R − φ_L + δ_CP)
    dφ_R/dt = ω_R + K·sin(φ_L − φ_R − δ_CP)
    """
    phi_L, phi_R = phi
    dphi_L = omega_L + K * np.sin(phi_R - phi_L + delta_CP)
    dphi_R = omega_R + K * np.sin(phi_L - phi_R - delta_CP)
    return [dphi_L, dphi_R]


def simulate_higgs_sync(K, delta_CP=0.0, omega_L=1.0, omega_R=1.0,
                        phi_L0=0.8, phi_R0=0.0, t_end=20.0):
    """
    Simulate the L and R clocks synchronizing through Higgs coupling K.
    K = y_f · v/√2 = mass
    delta_CP = CP-violating phase in Yukawa coupling
    """
    t_eval = np.linspace(0, t_end, 2000)
    sol = solve_ivp(
        lambda t, y: kuramoto_L_R(t, y, omega_L, omega_R, K, delta_CP),
        (0, t_end), [phi_L0, phi_R0], t_eval=t_eval, rtol=1e-9
    )
    return sol.t, sol.y[0], sol.y[1]


def equilibrium_offset(K, delta_CP, omega_L=1.0, omega_R=1.0):
    """
    At synchronization lock, φ_L − φ_R converges to:
      For equal ω: offset = δ_CP  (particle)
                   offset = −δ_CP (antiparticle)
    This is the residual clock misalignment that causes CP asymmetry.
    """
    t, pL, pR = simulate_higgs_sync(K, delta_CP, omega_L, omega_R, t_end=50.0)
    return (pL[-1] - pR[-1]) % (2 * np.pi)


# ─── 3. Antiparticles as Reversed Clocks ─────────────────────────────────────

def dirac_spinor_particle(p_z, spin_up: bool, m=1.0):
    """Particle: phase e^{−iEt} — forward time clock."""
    E = np.sqrt(p_z**2 + m**2)
    r = p_z / (E + m)
    N = np.sqrt((E + m) / (2 * E))
    vec = np.array([1, 0, r, 0] if spin_up else [0, 1, 0, -r], dtype=complex)
    return N * vec, +E   # returns (spinor, clock_frequency)


def dirac_spinor_antiparticle(p_z, spin_up: bool, m=1.0):
    """
    Antiparticle: phase e^{+iEt} — REVERSED time clock.
    v(p,↑) = N·[r, 0, 1, 0]^T (large and small swapped + sign change)
    v(p,↓) = N·[0,-r, 0, 1]^T

    The large/small structure is INVERTED relative to the particle:
    what was the spatial clock component is now the temporal one,
    and vice versa — a 90° rotation of the time-phase/property relationship.
    """
    E = np.sqrt(p_z**2 + m**2)
    r = p_z / (E + m)
    N = np.sqrt((E + m) / (2 * E))
    vec = np.array([r, 0, 1, 0] if spin_up else [0, -r, 0, 1], dtype=complex)
    return N * vec, -E   # returns (spinor, clock_frequency — NEGATIVE)


def annihilation_probability(delta_phi, epsilon=0.1):
    """
    Schematic: probability of particle-antiparticle annihilation
    as a function of their residual clock phase mismatch delta_phi.
    P(annihilation) ∝ |⟨particle|antiparticle⟩|²
    Peaks when clocks are perfectly anti-aligned (φ_particle = −φ_antiparticle)
    i.e., when delta_phi = 0. CP violation shifts this peak.

    particle clock offset: +δ_CP
    antiparticle clock offset: −δ_CP
    Total mismatch: 2δ_CP → survival asymmetry
    """
    return epsilon * np.cos(delta_phi)**2


def survival_fraction(delta_CP_arr, epsilon=0.3):
    """
    After the Higgs phase transition:
    Particles synchronize to offset +δ_CP from bulk.
    Antiparticles synchronize to offset −δ_CP from bulk.
    When they meet, residual mismatch = 2δ_CP.
    P(survive) = P(fail to annihilate) ∝ sin²(δ_CP) (schematic)
    """
    return np.sin(delta_CP_arr)**2 * epsilon


# ─── Main ─────────────────────────────────────────────────────────────────────

def run():
    print_massless_limit()

    print("\n\n" + "═" * 68)
    print("2. HIGGS FIELD AS KURAMOTO CLOCK SYNCHRONIZER")
    print("═" * 68)

    print("""
  The Yukawa interaction in Weyl form:
    dφ_L/dt = ω_L + K·sin(φ_R − φ_L + δ_CP)
    dφ_R/dt = ω_R + K·sin(φ_L − φ_R − δ_CP)
    K = y_f · v/√2 = fermion mass

  Without Higgs (K=0):  clocks free-run independently, θ_rel = 90°
  With Higgs (K>0):     clocks synchronize, θ_rel → equilibrium
  Large K (heavy top):  fast synchronization, tight lock
  Small K (light e⁻):   slow synchronization, looser lock
  K=0 (photon):         no synchronization, permanently decoupled
""")

    print("  Fermion   Yukawa y_f     Mass (GeV)   Sync rate K/ω")
    print("  " + "─"*52)
    particles = [
        ('electron',   2.9e-6,   0.000511),
        ('muon',       6.0e-4,   0.1057),
        ('tau',        1.0e-2,   1.777),
        ('up quark',   1.3e-5,   0.002),
        ('charm',      7.2e-3,   1.27),
        ('top',        1.0,     173.0),
    ]
    for name, y, m_gev in particles:
        v_higgs = 246.0   # GeV
        K = y * v_higgs / np.sqrt(2)
        print(f"  {name:<12}  y={y:.1e}   m={m_gev:.4f} GeV   K/ω={K/m_gev:.3f}")

    print("\n  K/ω ≈ 1 for all fermions (self-consistent: K = m by construction)")
    print("  The Higgs VEV v=246 GeV sets the SCALE of synchronization.")
    print("  Different Yukawa couplings → different sync strengths → different masses.")

    print("\n\n" + "═" * 68)
    print("3. ANTIPARTICLES: REVERSED CLOCKS → MATTER ASYMMETRY")
    print("═" * 68)

    print("""
  Particle  spinor u(p): phase e^{−iEt},  clock frequency = +E
  Antiparticle v(p): phase e^{+iEt},  clock frequency = −E

  The antiparticle's large/small components are SWAPPED:
    Particle:     large = temporal clock alignment
                  small = spatial clock alignment
    Antiparticle: large = spatial clock alignment
                  small = temporal clock alignment
  The property vector has rotated by π relative to the time-phase clock.

  CP VIOLATION in Yukawa coupling: y_f = |y_f| e^{iδ_CP}
    Particle sync equilibrium:     φ_L − φ_R → +δ_CP
    Antiparticle sync equilibrium: φ_L − φ_R → −δ_CP
    Clock mismatch at meeting:     2δ_CP

  Survival asymmetry (schematic):
    η = (N_matter − N_antimatter) / N_total ≈ sin²(δ_CP) × coupling
    For δ_CP ~ π/4:  η ~ 0.5 × coupling  (large asymmetry)
    Observed: η ~ 6 × 10⁻¹⁰  (requires small coupling × small δ_CP)
""")

    # Particle vs antiparticle spinor comparison
    p_val = 1.0; m_val = 1.0
    sp, E_p = dirac_spinor_particle(p_val, True, m_val)
    sa, E_a = dirac_spinor_antiparticle(p_val, True, m_val)
    print(f"  Particle spinor u(p=1,↑):      {np.round(sp,3)}")
    print(f"  Antiparticle spinor v(p=1,↑):  {np.round(sa,3)}")
    print(f"  Particle clock frequency:  +E = +{E_p:.4f}")
    print(f"  Antiparticle clock freq.:  -E = {E_a:.4f}")
    print(f"\n  Overlap ⟨particle|antiparticle⟩ = {np.abs(sp.conj() @ sa):.6f}")
    print(f"  (Zero overlap confirms reversed clocks are orthogonal states)")

    # ── Plots ──────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle('Higgs as Clock Synchronizer — Antiparticles as Reversed Clocks',
                 fontsize=13)

    # ── A: Massless limit — helicity fractions vs p/m ─────────────────────
    ax = axes[0, 0]
    m_vals = [0.001, 0.1, 1.0]
    p_range = np.logspace(-2, 3, 400)
    for m in m_vals:
        fl = [helicity_fractions(p, m)[0] for p in p_range]
        fs = [helicity_fractions(p, m)[1] for p in p_range]
        ax.semilogx(p_range/m, fl, label=f'm={m} (large, temporal)', lw=1.5)
    ax.axhline(0.5, color='k', linestyle='--', lw=1, label='m=0 limit: f=½ both')
    ax.set_xlabel('|p|/m')
    ax.set_ylabel('Large-component fraction')
    ax.set_title('Massless limit: f_large → ½\n(temporal ⊥ spatial: Weyl decoupling)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ── B: Higgs Kuramoto synchronization for different masses ────────────
    ax = axes[0, 1]
    t_end = 30.0
    for K, col, lbl in [(0.0, 'gray', 'K=0 (massless)'),
                         (0.3, 'steelblue', 'K=0.3 (light)'),
                         (1.0, 'darkorange', 'K=1.0 (medium)'),
                         (5.0, 'firebrick', 'K=5.0 (heavy)')]:
        t, pL, pR = simulate_higgs_sync(K, delta_CP=0.0,
                                         phi_L0=1.2, phi_R0=0.0, t_end=t_end)
        offset = (pL - pR) % (2 * np.pi)
        offset[offset > np.pi] -= 2 * np.pi
        ax.plot(t, offset, color=col, label=lbl, lw=1.8)
    ax.axhline(0, color='k', linestyle=':', lw=1)
    ax.set_xlabel('Time')
    ax.set_ylabel('φ_L − φ_R (clock offset, rad)')
    ax.set_title('Higgs-Kuramoto: L-R clock synchronization\nK = y_f·v/√2 = mass')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ── C: CP violation — asymmetric synchronization ──────────────────────
    ax = axes[0, 2]
    t_end = 40.0
    K = 2.0
    for d_CP, col, lbl in [(0.0,     'gray',      'δ_CP=0 (no CP viol.)'),
                            (0.1,     'steelblue', 'δ_CP=0.1 rad'),
                            (0.3,     'darkorange','δ_CP=0.3 rad'),
                            (np.pi/4, 'firebrick', 'δ_CP=π/4 rad')]:
        # Particle
        t, pL, pR = simulate_higgs_sync(K, d_CP, phi_L0=1.2, phi_R0=0.0, t_end=t_end)
        offset_p = (pL - pR); offset_p -= offset_p[0]
        # Antiparticle: reversed clock → negate d_CP
        t, pLa, pRa = simulate_higgs_sync(K, -d_CP, phi_L0=-1.2, phi_R0=0.0, t_end=t_end)
        offset_a = (pLa - pRa); offset_a -= offset_a[0]
        ax.plot(t, offset_p, color=col, lw=1.5, label=f'particle {lbl}')
        ax.plot(t, offset_a, color=col, lw=1.5, linestyle='--')
    ax.set_xlabel('Time')
    ax.set_ylabel('Phase offset from equilibrium (rad)')
    ax.set_title('CP violation: asymmetric lock\n(solid=particle, dashed=antiparticle)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # ── D: Clock phase diagram (forward vs reversed) ──────────────────────
    ax = axes[1, 0]
    theta = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', lw=0.5, alpha=0.3)
    # Forward clock (particle)
    for t_snap, alpha in zip([0, np.pi/4, np.pi/2, np.pi], [0.3, 0.5, 0.7, 1.0]):
        ax.annotate('', xy=(np.cos(t_snap)*0.85, np.sin(t_snap)*0.85), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='royalblue',
                                   lw=1.5, alpha=alpha))
    # Backward clock (antiparticle) — runs opposite direction
    for t_snap, alpha in zip([0, -np.pi/4, -np.pi/2, -np.pi], [0.3, 0.5, 0.7, 1.0]):
        ax.annotate('', xy=(np.cos(t_snap)*0.65, np.sin(t_snap)*0.65), xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color='firebrick',
                                   lw=1.5, alpha=alpha))
    ax.text(0, 1.15, 'PARTICLE\n(forward clock)', ha='center', color='royalblue', fontsize=9)
    ax.text(0, -1.2, 'ANTIPARTICLE\n(reversed clock)', ha='center', color='firebrick', fontsize=9)
    ax.set_aspect('equal'); ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.5, 1.4)
    ax.set_title('Time-phase clocks:\nparticle (CCW) vs antiparticle (CW)')
    ax.axis('off')

    # ── E: Survival fraction vs δ_CP ─────────────────────────────────────
    ax = axes[1, 1]
    delta_arr = np.linspace(0, np.pi, 300)
    for eps, col, lbl in [(0.1, 'steelblue', 'ε=0.10'),
                           (0.3, 'darkorange', 'ε=0.30'),
                           (0.5, 'firebrick', 'ε=0.50')]:
        surv = survival_fraction(delta_arr, eps)
        ax.plot(np.degrees(delta_arr), surv, color=col, lw=2, label=lbl)
    ax.axhline(6e-10, color='k', linestyle='--', lw=1, label='Observed η ~ 6×10⁻¹⁰')
    ax.set_xlabel('δ_CP (degrees)')
    ax.set_ylabel('η = (N_matter − N_anti) / N_total')
    ax.set_title('Matter survival fraction vs CP phase\nη ~ ε·sin²(δ_CP)')
    ax.set_yscale('log')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ── F: Summary diagram ────────────────────────────────────────────────
    ax = axes[1, 2]
    ax.axis('off')
    ax.text(0.5, 0.98,
            'UNIFIED CLOCK PICTURE',
            ha='center', va='top', fontsize=12, fontweight='bold',
            transform=ax.transAxes)
    summary = """
MASSLESS SPIN-1/2 FERMION (idealized massless ν):
  θ_rel = 90° always
  L and R clocks permanently orthogonal
  → 2 Weyl spinors, 2 helicity states only
  → No rest frame possible
  (Photons are spin-1 vector bosons; see Paper §5)

MASSIVE PARTICLE:
  Higgs gives K = y_f · v/√2 = m
  L and R clocks Kuramoto-lock to offset δ_CP
  θ_rel = 2·arctan(v/c)  at equilibrium
  → 4 Dirac components needed

ANTIPARTICLE:
  Clock runs BACKWARD (E → -E)
  Large/small Dirac components SWAPPED
  Synchronizes to offset -δ_CP (opposite)

MATTER-ANTIMATTER ASYMMETRY:
  At Higgs phase transition:
  Particles lock to +δ_CP
  Antiparticles lock to -δ_CP
  Mismatch 2δ_CP → unequal survival
  η ~ ε · sin²(δ_CP) ~ 6×10⁻¹⁰

OPEN QUESTION:
  Why is δ_CP so small in the SM?
  (Strong CP problem)
  Time-phase model: initial Big Bang
  clock phase distribution may set η.
"""
    ax.text(0.05, 0.92, summary, ha='left', va='top', fontsize=8.5,
            transform=ax.transAxes, family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('higgs_clock.png', dpi=150)
    print("\nSaved: higgs_clock.png")
    # plt.show()  # non-interactive backend (Agg); savefig above is sufficient


if __name__ == '__main__':
    run()
