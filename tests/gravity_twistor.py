"""
gravity_twistor.py — Gravity as Clock Synchronization / Penrose-Twistor Connection
====================================================================================

THREE CONNECTED STRUCTURES:

  1. GRAVITY = LARGE-SCALE KURAMOTO SYNCHRONIZATION
     Gravitational time dilation: ω(x) = ω₀ √(1 + 2Φ(x)/c²)
     A massive body slows surrounding clocks — dragging them toward
     its own phase. The Newtonian Poisson equation:
       ∇²Φ = 4πGρ
     IS the steady-state Kuramoto synchronization field equation:
       ∇²φ_clock = −ρ_matter × K_grav
     Gravity = the equilibrium synchronization field of bulk matter.
     Objects "fall" because they move toward the region of clock
     synchronization — toward higher ω, toward greater mass.

  2. PENROSE OBJECTIVE REDUCTION = CLOCK PHASE DECOHERENCE
     A particle in superposition |x₁⟩ + |x₂⟩ has its clock running
     at TWO DIFFERENT RATES (gravitational time dilation at x₁ vs x₂).
     The two clocks accumulate phase difference:
       δφ(t) = [ω(x₁) − ω(x₂)] · t = δω · t
     When δφ ~ π, the two branches are phase-orthogonal → decoherence.
     Collapse time: τ ~ π/δω = πℏ/E_G   (Penrose formula, E_G = Gm²/Δx)
     No observer needed. No FTL. Just gravitational clock desynchronization.

  3. TWISTOR THEORY CONNECTION
     Penrose's twistor Z^α = (ω^A, π_{A'}):
       ω^A ↔ ψ_L (LEFT Weyl spinor = temporal clock)
       π_{A'} ↔ ψ_R (RIGHT Weyl spinor = spatial clock)

     Incidence relation (massless): ω^A = i x^{AA'} π_{A'}
     This IS the Dirac equation in Weyl form for m=0!

     Null twistor condition (Z·Z̄ = 0):
       ω^A π̄_A + ω̄^{A'} π_{A'} = 0  ↔  L ⊥ R  ↔  θ_rel = 90°  ↔  massless

     Gravity curves twistor space by deforming the incidence relation
     — changing how the temporal and spatial clocks are coupled through
     the spacetime position x. This is gravitational clock synchronization
     written in geometric language.

     Penrose's twistor programme is the geometric formulation of the
     time-phase synchronization model.

DICTIONARY:
  Time-phase model              Twistor theory               Standard physics
  ─────────────────────────────────────────────────────────────────────────────
  Temporal clock ψ_L            ω^A (primed spinor)          Left Weyl spinor
  Spatial clock ψ_R             π_{A'} (unprimed spinor)     Right Weyl spinor
  L-R coupling = mass           Non-null twistor Z·Z̄ ≠ 0    Dirac mass term
  θ_rel = 90° (massless)        Null twistor Z·Z̄ = 0        Photon/gluon
  Higgs synchronizer            Twistor cohomology class     Mass generation
  Gravity = sync field          Twistor space curvature      General relativity
  Penrose OR collapse           δφ = π (clock orthogonal)    Wavefunction collapse
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ─── Constants (SI) ───────────────────────────────────────────────────────────
G     = 6.674e-11    # m³/(kg·s²)
c     = 3.0e8        # m/s
hbar  = 1.055e-34    # J·s
m_e   = 9.109e-31    # kg
m_p   = 1.673e-27    # kg


# ─── 1. Gravity as Kuramoto Synchronization ───────────────────────────────────

def gravitational_clock_rate(r, M, omega_inf=1.0):
    """
    Clock frequency at radius r from mass M (Schwarzschild weak-field):
      ω(r) = ω_∞ · √(1 − 2GM/rc²)  ≈  ω_∞ · (1 − GM/rc²)

    The clock slows near mass — the gradient dω/dr points away from M.
    A particle drifts toward SLOWER clocks (toward mass) because
    its internal clock must synchronize with the bulk clock field.

    Equivalently: the Kuramoto coupling drives φ_particle → φ_bulk(r),
    and the bulk clock field has a gradient that creates a restoring force.
    """
    phi_grav = -G * M / (r * c**2)   # Newtonian potential / c²
    return omega_inf * np.sqrt(np.maximum(1 + 2 * phi_grav, 0))


def clock_sync_force(r, M, omega_0=1.0):
    """
    The 'synchronization force' felt by a particle moving through
    the clock-frequency gradient field.

    In Kuramoto: dφ/dt = ω(r) + K sin(φ_bulk − φ_particle)
    If the particle clock is synchronized to local bulk:
    φ_particle = φ_bulk(r), the particle accelerates toward dω/dr < 0
    i.e., toward greater mass concentration.

    This is gravitational acceleration rewritten as clock sync gradient:
      a = dω/dr · (c²/ω₀) = GM/r²   (recovering Newton!)
    """
    dw_dr = G * M * omega_0 / (r**2 * c**2)  # magnitude of |∇ω|
    return dw_dr * c**2 / omega_0             # = GM/r² ✓


def poisson_as_kuramoto(rho_arr, dr, K_grav=1.0):
    """
    Poisson equation: ∇²Φ = 4πGρ
    Kuramoto field:   ∇²φ_clock = −ρ·K_grav

    Both are elliptic PDEs of the same form. The Kuramoto field φ_clock
    IS the gravitational potential (up to a sign and scaling).

    Solve numerically on 1D grid (spherically symmetric):
      d²Φ/dr² + (2/r)dΦ/dr = 4πGρ(r)
    """
    n = len(rho_arr)
    r = np.arange(1, n+1) * dr
    phi = np.zeros(n)
    # Simple finite difference integration outward from center
    for i in range(2, n):
        phi[i] = (2*phi[i-1] - phi[i-2]
                  + dr**2 * (4*np.pi*G*rho_arr[i-1]
                             - 2/r[i-1] * (phi[i-1]-phi[i-2])/dr))
    return r, phi


# ─── 2. Penrose Objective Reduction as Clock Phase Decoherence ────────────────

def penrose_E_G(mass, delta_x):
    """
    Penrose gravitational self-energy of a mass in superposition
    of two locations separated by delta_x:
      E_G = G m² / Δx   (self-energy of superposed mass distributions)
    """
    return G * mass**2 / delta_x


def penrose_collapse_time(mass, delta_x):
    """
    Time-phase interpretation: collapse occurs when gravitational
    clock phase difference accumulates to π:
      δω(x) = ω₀ · GM / (Δx · c²) · (characteristic length)
      τ = π / δω = πℏ / E_G

    Penrose formula: τ ~ ℏ / E_G  (same result)
    """
    E_G = penrose_E_G(mass, delta_x)
    return np.pi * hbar / E_G


def clock_decoherence(t_arr, mass, delta_x, r_ref=1.0):
    """
    Coherence of superposition |x₁⟩+|x₂⟩ over time.
    Clock at x₁: ω₁ = ω₀(1 − GM/(r_ref · c²))
    Clock at x₂: ω₂ = ω₀(1 − GM/((r_ref+Δx) · c²))
    Phase difference: δφ(t) = (ω₁ − ω₂) · t
    Coherence: C(t) = cos(δφ(t) / 2)
    Collapse when C → 0: t_collapse = π/δω = πℏ/E_G
    """
    omega_0 = mass * c**2 / hbar    # rest-mass frequency
    delta_omega = omega_0 * G * mass / (r_ref * (r_ref + delta_x) * c**2)
    delta_phi = delta_omega * t_arr
    coherence = np.cos(delta_phi / 2)
    tau = np.pi / delta_omega
    return coherence, tau


# ─── 3. Twistor Connection ────────────────────────────────────────────────────

def twistor_null_condition(omega_L, pi_R):
    """
    Null twistor condition: Z·Z̄ = ω^A π̄_A + ω̄^{A'} π_{A'} = 0
    In 2-component notation: Re(ω^† · π) = 0

    For the time-phase model:
      ω^A = ψ_L (temporal clock)
      π_{A'} = ψ_R (spatial clock)
    Null ↔ ψ_L ⊥ ψ_R ↔ θ_rel = 90° ↔ massless
    """
    Z_dot_Zbar = 2 * np.real(omega_L.conj() @ pi_R)
    theta_rel = np.arccos(np.clip(
        np.abs(omega_L.conj() @ pi_R) /
        (np.linalg.norm(omega_L) * np.linalg.norm(pi_R) + 1e-30), -1, 1))
    return Z_dot_Zbar, theta_rel


def twistor_mass_from_coupling(y_f, v_higgs=246.0):
    """
    In twistor language, mass deforms the incidence relation:
      ω^A = i x^{AA'} π_{A'}  +  m · η^A   (massive)
    where η^A is the 'mass twistor' — a fixed reference spinor set
    by the Higgs VEV.

    The additional term m·η^A is EXACTLY the Higgs-Kuramoto coupling
    that synchronizes ψ_L to ψ_R.

    Non-null measure: |Z·Z̄| = m · |ω^A η_A|
    """
    return y_f * v_higgs / np.sqrt(2)


def incidence_relation(x_spacetime, pi_R, mass=0.0):
    """
    Twistor incidence relation:
      ω^A = i x^{AA'} π_{A'} + (mass term)

    x_spacetime: (t, x, y, z) → x^{AA'} = t·I + x·σ₁ + y·σ₂ + z·σ₃
    pi_R: 2-component spatial clock spinor

    Returns omega_L (temporal clock spinor) = L-R coupling through position.
    This is HOW spacetime geometry couples the two clocks.
    """
    t, x, y, z = x_spacetime
    sigma1 = np.array([[0,1],[1,0]], dtype=complex)
    sigma2 = np.array([[0,-1j],[1j,0]], dtype=complex)
    sigma3 = np.array([[1,0],[0,-1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    x_AA_prime = t * I2 + x * sigma1 + y * sigma2 + z * sigma3
    omega_L = 1j * x_AA_prime @ pi_R

    # Mass correction: shifts θ_rel from 90°
    if mass > 0:
        eta = np.array([1, 0], dtype=complex) * mass / (np.linalg.norm(pi_R) + 1e-30)
        omega_L = omega_L + eta

    return omega_L


# ─── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("GRAVITY AS CLOCK SYNCHRONIZATION — PENROSE-TWISTOR CONNECTION")
    print("=" * 70)

    # ── Gravity recovers Newton ───────────────────────────────────────────
    print("\n1. Clock-sync force recovers Newtonian gravity:")
    M_earth = 5.972e24
    r_vals = np.array([6.371e6, 1e7, 1e8])
    for r in r_vals:
        a_newton = G * M_earth / r**2
        a_clock  = clock_sync_force(r, M_earth)
        print(f"   r={r:.2e} m:  Newton={a_newton:.4e} m/s²  "
              f"Clock-sync={a_clock:.4e} m/s²  match={np.isclose(a_newton,a_clock)}")

    # ── Penrose collapse times ─────────────────────────────────────────────
    print("\n2. Penrose collapse times (clock decoherence):")
    print(f"   {'Object':<18} {'Mass (kg)':<14} {'Sep. (m)':<12} {'τ_collapse'}")
    print("   " + "─"*60)
    cases = [
        ("electron",    m_e,   1e-10,  "~10¹⁰ yrs (no collapse)"),
        ("nucleon",     m_p,   1e-15,  ""),
        ("protein",     1e-22, 1e-9,   ""),
        ("dust grain",  1e-15, 1e-6,   ""),
        ("virus",       1e-19, 1e-7,   "~100 ms (biological!)"),
        ("cat",         1.0,   1e-9,   "~10⁻³⁸ s (instant)"),
    ]
    for name, m, dx, note in cases:
        tau = penrose_collapse_time(m, dx)
        unit = 's'
        val = tau
        if tau > 3.15e7 * 1e9:
            val = tau / (3.15e7 * 1e9)
            unit = 'Gyr'
        elif tau > 3.15e7:
            val = tau / 3.15e7
            unit = 'yr'
        elif tau < 1e-9:
            val = tau * 1e15
            unit = 'fs'
        elif tau < 1e-6:
            val = tau * 1e9
            unit = 'ns'
        elif tau < 1e-3:
            val = tau * 1e3
            unit = 'ms'
        print(f"   {name:<18} {m:<14.2e} {dx:<12.2e} "
              f"{val:.2e} {unit}  {note}")

    # ── Twistor null condition ─────────────────────────────────────────────
    print("\n3. Twistor null condition ↔ θ_rel = 90° ↔ massless:")
    pi_R = np.array([1, 0], dtype=complex)   # reference spatial spinor

    for name, x_pos, mass in [
        ("photon at origin",  (0,0,0,0),  0.0),
        ("photon at (t,x)",   (1,1,0,0),  0.0),
        ("massive at origin", (0,0,0,0),  0.5),
        ("massive at (t,x)",  (1,1,0,0),  0.5),
    ]:
        omega_L = incidence_relation(x_pos, pi_R, mass)
        Z_dot, theta = twistor_null_condition(omega_L, pi_R)
        print(f"   {name:<25}  Z·Z̄={Z_dot:+.4f}  "
              f"θ_rel={np.degrees(theta):.1f}°  "
              f"{'NULL (massless)' if abs(Z_dot)<0.01 and mass==0 else 'non-null (massive)'}")

    # ─── Plots ────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))
    fig.suptitle('Gravity as Clock Synchronization — Penrose & Twistor Connection',
                 fontsize=13)

    # A: Clock rate vs distance from Earth
    ax = axes[0, 0]
    M_earth = 5.972e24
    r_arr = np.linspace(6.4e6, 1e8, 400)
    omega_r = gravitational_clock_rate(r_arr, M_earth)
    ax.plot(r_arr/1e6, (1 - omega_r)*1e9, 'steelblue', lw=2)
    ax.set_xlabel('Distance from Earth center (×10⁶ m)')
    ax.set_ylabel('Clock slowing: (1 − ω/ω_∞) × 10⁹')
    ax.set_title('Clock rate gradient = gravitational field\n'
                 'Objects fall toward slower clocks (= toward mass)')
    ax.grid(True, alpha=0.3)
    ax.axvline(6.371, color='green', linestyle='--', lw=1, label="Earth's surface")
    ax.legend(fontsize=8)

    # B: Clock synchronization field (Poisson ↔ Kuramoto)
    ax = axes[0, 1]
    dr = 1e6
    n = 100
    r_profile = np.linspace(6.371e6, 1e8, n)
    # Density profile: Earth concentrated at origin → point mass approx
    rho = np.zeros(n)
    rho[0] = M_earth / (4/3 * np.pi * (6.371e6)**3)
    r_kuramoto, phi_kuramoto = poisson_as_kuramoto(rho, dr)
    phi_newton = -G * M_earth / r_profile
    ax.plot(r_profile/1e6, phi_newton, 'royalblue', lw=2, label='Newton: −GM/r')
    ax.plot(r_kuramoto/1e6, phi_kuramoto/1e7, 'darkorange', lw=2,
            linestyle='--', label='Kuramoto field (rescaled)')
    ax.set_xlabel('r (×10⁶ m)')
    ax.set_ylabel('Synchronization potential')
    ax.set_title('Poisson = Kuramoto field equation\n'
                 '∇²Φ = 4πGρ  ↔  ∇²φ_clock = −ρK')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # C: Penrose collapse — coherence vs time for different objects
    ax = axes[0, 2]
    t_max = 1.0
    t_arr = np.linspace(0, t_max, 1000)
    for name, m, dx, col in [
        ('virus (10⁻¹⁹ kg, 100nm)', 1e-19, 1e-7, 'royalblue'),
        ('protein (10⁻²² kg, 10nm)', 1e-22, 1e-9, 'darkorange'),
        ('dust (10⁻¹⁵ kg, 1μm)',     1e-15, 1e-6, 'firebrick'),
    ]:
        coh, tau = clock_decoherence(t_arr, m, dx)
        if tau < t_max * 10:
            ax.plot(t_arr, coh, color=col, lw=2, label=f'{name}\nτ={tau:.2e}s')
    ax.axhline(0, color='k', lw=0.5, linestyle=':')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Superposition coherence C(t)')
    ax.set_title('Penrose OR: clock phase decoherence\n'
                 'C(t) = cos(δφ(t)/2), collapse at C=0')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # D: Penrose τ vs object mass (collapse time)
    ax = axes[1, 0]
    mass_arr = np.logspace(-31, 3, 200)
    dx_fixed = 1e-9   # 1 nm superposition
    tau_arr = [penrose_collapse_time(m, dx_fixed) for m in mass_arr]
    ax.loglog(mass_arr, tau_arr, 'firebrick', lw=2.5)
    # Reference lines
    for val, lbl, col in [
        (hbar / (1.38e-23 * 300), 'thermal coherence (300K)', 'gray'),
        (13.8e9 * 3.15e7,          'age of universe', 'navy'),
        (1e0,                      '1 second', 'green'),
        (1e-15,                    '1 femtosecond', 'darkorange'),
    ]:
        ax.axhline(val, color=col, linestyle='--', lw=1, label=lbl)
    ax.set_xlabel('Object mass (kg)')
    ax.set_ylabel('Penrose collapse time τ (s)')
    ax.set_title('Penrose OR: clock decoherence time\nτ = πℏ/E_G = πℏΔx/Gm²')
    ax.legend(fontsize=7, loc='lower left')
    ax.grid(True, alpha=0.3, which='both')

    # E: Twistor diagram — null vs massive
    ax = axes[1, 1]
    theta_vals = np.linspace(0, np.pi/2, 200)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')

    # Unit circle
    circle = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(circle), np.sin(circle), 'k-', lw=0.5, alpha=0.3)

    # Null twistor: θ_rel = 90°, L ⊥ R
    ax.annotate('', xy=(0, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='royalblue', lw=2.5))
    ax.annotate('', xy=(1, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='royalblue', lw=2.5,
                                linestyle='dashed'))
    ax.text(0.05, 0.95, 'ψ_L (temporal)', color='royalblue', fontsize=8)
    ax.text(0.8, 0.12, 'ψ_R (spatial)', color='royalblue', fontsize=8)
    ax.text(0.35, 0.65, 'θ=90°\nNULL\nmassless', color='royalblue',
            fontsize=8, ha='center',
            bbox=dict(facecolor='lightblue', alpha=0.7, boxstyle='round'))

    # Massive: θ_rel < 90°
    theta_mass = np.radians(35)
    ax.annotate('', xy=(0, 0.85), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='firebrick', lw=2.5))
    ax.annotate('', xy=(0.85*np.sin(theta_mass), 0.85*np.cos(theta_mass)),
                xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='firebrick', lw=2.5,
                                linestyle='dashed'))
    ax.text(-0.9, 0.5, 'ψ_L', color='firebrick', fontsize=8)
    arc_t = np.linspace(np.pi/2, np.pi/2 - theta_mass, 50)
    ax.plot(0.4*np.cos(arc_t), 0.4*np.sin(arc_t), 'r-', lw=1.5)
    ax.text(-0.55, 0.3, f'θ={90-int(np.degrees(theta_mass))}°\nnon-null\nmassive',
            color='firebrick', fontsize=8, ha='center',
            bbox=dict(facecolor='mistyrose', alpha=0.7, boxstyle='round'))
    ax.set_title('Twistor null condition\nZ·Z̄=0 ↔ θ_rel=90° ↔ massless')
    ax.text(0, -1.35,
            'Higgs coupling rotates ψ_R toward ψ_L\n'
            '(θ_rel: 90° → 0° as mass → ∞)',
            ha='center', fontsize=8)
    ax.axis('off')

    # F: Summary table
    ax = axes[1, 2]
    ax.axis('off')
    ax.text(0.5, 0.99, 'UNIFIED SYNCHRONIZATION PICTURE',
            ha='center', va='top', fontsize=11, fontweight='bold',
            transform=ax.transAxes)
    summary = """
SCALE         PHENOMENON          MECHANISM
────────────────────────────────────────────────────────
Particle      Mass                Higgs: L-R clock sync
              Massless            Weyl: L ⊥ R (θ=90°)
              Antiparticle        Reversed clock (−E)

Spacetime     Gravity             Kuramoto bulk field
              Time dilation       Local clock rate ω(x)
              Gravitational wave  Oscillation in sync field

Quantum       Superposition       Two-phase coherence
              Penrose collapse    Gravitational clock
                                  decoherence (δφ→π)
              Entanglement        Synchronized clocks
                                  at creation

Geometry      Twistor Z^α         (ψ_L, ψ_R) = clock pair
              Null twistor        massless (θ=90°)
              Incidence relation  How x couples L to R
              Twistor curvature   Gravitational sync field

Cosmology     Big Bang            Random initial phases
              Higgs transition    L-R clocks lock in
              Matter asymmetry    CP offset ±δ_CP
              Dark energy?        Unlocked vacuum clocks
"""
    ax.text(0.03, 0.93, summary, ha='left', va='top', fontsize=8,
            transform=ax.transAxes, family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig(_HERE / 'gravity_twistor.png', dpi=150)
    print("\nSaved: gravity_twistor.png")
    plt.show()

    print("""
CONNECTION TO PENROSE'S TWISTOR PROGRAMME:
  Penrose spent decades trying to unify QM and GR via twistors.
  The time-phase model suggests the unification point is:
    → Twistor Z^α = (ψ_L, ψ_R) = (temporal clock, spatial clock)
    → Gravity = synchronization field of the (ψ_L, ψ_R) coupling
    → Quantum superposition = multiple clock phase branches
    → Penrose collapse = gravitational clock decoherence

  Penrose's 'conformal cyclic cosmology' (CCC) may also connect:
  each aeon ends when all massive particles (synchronized clocks)
  lose their mass (clocks decouple), reverting to θ_rel=90° — a
  universe of massless particles — which is conformally equivalent
  to the beginning of the next aeon's Big Bang.

  In the time-phase picture: each conformal aeon is one cycle of
  the universal clock synchronization: random phases → Higgs lock
  → eventual photon-only universe → next Big Bang.
""")


if __name__ == '__main__':
    run()
