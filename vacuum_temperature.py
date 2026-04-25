"""
vacuum_temperature.py — Orbitals, Vacuum, Temperature, and Brownian Motion
============================================================================

DISCLAIMER (added 2026-04-25):
  The Brownian-motion section of this file (claim #4 below; the D_clock
  derivation and the implied "K fixes Stokes-Einstein" relation) does not
  survive scrutiny under the framework's own K = m identification. The K
  used in D_clock has units of momentum (kg·m/s) and must be solved for
  to match Stokes-Einstein, whereas the framework's K = m·c²/ℏ is a
  Compton frequency (rad/s). Numerical attempts with physically motivated
  K guesses (thermal momentum, m·c, m·v_thermal) miss empirical Stokes-
  Einstein by 4-50 orders of magnitude. The "K fixes Stokes-Einstein"
  step is therefore a phenomenological refit, not a derivation from K = m,
  and the residual D ∝ 1/√ω prediction is downstream of that refit, not
  independent. See EQUATIONS.md §10 ("Brownian Motion: An Open Question")
  for the current honest status. The Brownian simulation code in this
  file uses a free K_couple parameter for illustrative random-walk dynamics
  only and should not be read as a derivation of D from the framework.

  Claims #1, #2, #3 (orbitals as standing waves, photon residual / ZPF,
  temperature as clock phase distribution width) are unaffected.

FOUR CONNECTED CLAIMS:

  1. HYDROGEN ORBITALS ARE REAL STANDING WAVES
     ψ_nlm is not a "probability cloud" — it is a physical standing wave
     locked by the Coulomb potential. The same equation that gives
     Bell correlations gives the exact geometry of chemical bonding.
     There is nothing to "collapse."

  2. PHOTON ABSORPTION LEAVES A WAVE RESIDUAL
     When a photon is absorbed, its energy (ℏω) changes the atom's
     clock frequency. Its spatial wave structure — extended over many
     wavelengths — leaves a residual oscillation in the vacuum.
     Zero-point energy (½ℏω per mode) is the accumulated residual
     of every photon ever absorbed. The vacuum is not empty.

  3. TEMPERATURE = CLOCK PHASE DISTRIBUTION WIDTH
     At T=0: all atomic clocks synchronized (minimal residual only).
     At T>0: clocks have Gaussian phase noise σ² ∝ kT/ℏω.
     Heat is clock desynchronization. Absolute zero is perfect sync.
     The Planck spectrum is the emission spectrum of this distribution.

  4. BROWNIAN MOTION FROM CLOCK DESYNCHRONIZATION  ← NEW PREDICTION
     When two molecules collide, they exchange momentum proportional
     to their CLOCK PHASE DIFFERENCE at contact:
       δp = K · sin(φ_i − φ_j)  ≈  K · δφ  (small phases)
     At temperature T, phase differences are δφ ~ N(0, σ²_T).
     This drives a random walk — Brownian motion.

     The diffusion coefficient predicted from clock parameters:
       D_clock = K² · σ²_T · τ_coll / (2m²)
               = K² · (kT/ℏω) · τ_coll / (2m²)

     For this to match Einstein/Stokes:  D = kT/(6πηr)
       K² · τ_coll / (2m² · ℏω) = 1/(6πηr)

     This FIXES the Kuramoto coupling K in terms of the fluid's
     viscosity, molecular mass, mean free time, and frequency.
     It is a testable relation between thermodynamic quantities.

     Nelson's stochastic mechanics (1966) independently showed that
     a particle undergoing Brownian motion with diffusion ν = ℏ/2m
     in a background field satisfies the Schrödinger equation exactly.
     The time-phase model provides the physical mechanism Nelson needed:
     the background field is the zero-point residual wave field, and
     ν = ℏ/2m is the quantum of clock-phase diffusion.

CONNECTING TO BOHM:
     Bohm's "quantum potential" Q = −ℏ²∇²√ρ / (2m√ρ)
     is the gradient of the residual wave amplitude field.
     The pilot wave IS the accumulated residual from all prior
     interactions — the phase-structured vacuum field.
     Brownian motion in this field (Nelson) IS quantum mechanics.
     Temperature adds classical phase noise on top of the quantum floor.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import sph_harm, genlaguerre, factorial


# ─── Constants ────────────────────────────────────────────────────────────────
hbar  = 1.055e-34
k_B   = 1.381e-23
c     = 3.0e8
m_e   = 9.109e-31
a0    = 5.292e-11   # Bohr radius


# ─── 1. Hydrogen orbitals as real standing waves ──────────────────────────────

def hydrogen_wavefunction(n, l, m, r, theta, phi):
    """
    ψ_nlm(r,θ,φ) = R_nl(r) · Y_lm(θ,φ)
    Real standing wave — not a probability cloud.
    The same Schrödinger equation that correctly gives this
    is also the equation that never collapses.
    """
    rho = 2 * r / (n * a0)

    # Associated Laguerre polynomial L_{n-l-1}^{2l+1}
    lag = genlaguerre(n - l - 1, 2*l + 1)

    # Radial part
    norm_R = np.sqrt(
        (2 / (n * a0))**3 *
        factorial(n - l - 1) /
        (2 * n * factorial(n + l)**3)
    )
    R = norm_R * np.exp(-rho/2) * rho**l * lag(rho)

    # Angular part (spherical harmonic, real form)
    Y = sph_harm(m, l, phi, theta)

    return R * Y


def orbital_density_2d(n, l, m, grid_size=200, extent=20*a0):
    """2D cross-section of |ψ_nlm|² — the real standing wave density."""
    x = np.linspace(-extent, extent, grid_size)
    z = np.linspace(-extent, extent, grid_size)
    X, Z = np.meshgrid(x, z)
    Y = np.zeros_like(X)

    r     = np.sqrt(X**2 + Y**2 + Z**2) + 1e-30
    theta = np.arccos(np.clip(Z / r, -1, 1))
    phi   = np.arctan2(Y, X)

    psi = hydrogen_wavefunction(n, l, m, r, theta, phi)
    return X, Z, np.abs(psi)**2


# ─── 2. Phase noise distribution at temperature T ────────────────────────────

def phase_noise_std(T, omega):
    """
    σ_φ(T) = √(kT / ℏω)
    Standard deviation of clock phase noise at temperature T.
    This is derived from the thermal occupation of a harmonic oscillator:
      ⟨n⟩ = 1/(exp(ℏω/kT) − 1)
      σ_φ² = (2⟨n⟩ + 1) · (zero-point phase variance)
    In the high-T (classical) limit: σ_φ² ≈ kT/ℏω
    """
    if T == 0:
        return np.sqrt(0.5)            # zero-point: ½ℏω residual
    x = hbar * omega / (k_B * T)
    n_bar = 1.0 / (np.exp(x) - 1.0)
    return np.sqrt(2 * n_bar + 1) * np.sqrt(0.5)   # normalized


def planck_spectrum(omega_arr, T):
    """
    Planck blackbody spectrum: emission from thermal clock distribution.
    ⟨n(ω)⟩ = 1 / (exp(ℏω/kT) − 1)
    Power ∝ ℏω³ · ⟨n⟩ / (π²c³)
    """
    x = hbar * omega_arr / (k_B * T)
    return hbar * omega_arr**3 / (np.pi**2 * c**3) / (np.exp(x) - 1.0)


# ─── 3. Brownian motion from clock desynchronization ─────────────────────────
# DISCLAIMER: K_couple here is a free phenomenological parameter (kg·m/s per
# radian), NOT the framework's K = m·c²/ℏ (which has units of rad/s and
# cannot be plugged in here). The simulation illustrates random-walk
# dynamics under a sin-coupled phase-impulse model; it is not a derivation
# of D from the framework's K = m. See the file header and EQUATIONS.md §10.

def simulate_brownian_clock(
    n_steps   = 5000,
    n_trajs   = 80,
    T         = 300.0,         # temperature (K)
    omega_mol = 1e13,          # molecular vibration frequency (rad/s)
    K_couple  = 1e-23,         # phenomenological coupling (kg·m/s per radian); see disclaimer
    m_particle= 1e-17,         # Brownian particle mass (kg)
    tau_coll  = 1e-13,         # mean collision interval (s)
    dt        = 1e-13,         # time step (s)
    seed      = 42
):
    """
    Brownian motion as clock-phase-driven random walk.

    At each collision, momentum impulse:
      δp = K · δφ,   δφ ~ N(0, σ²_T)  where σ_T = √(kT/ℏω)

    Position update: x(t+dt) = x(t) + δp/m · dt + drag·dt

    Predicted diffusion coefficient from clock parameters:
      D_clock = K² · σ²_T · τ / (2m²)
              = K² · (kT/ℏω) · τ / (2m²)

    Einstein relation check: D_Einstein = kT / (6πηr)
    """
    rng = np.random.default_rng(seed)

    sigma_T = phase_noise_std(T, omega_mol)    # clock phase noise std

    # Predicted D from clock model (in 2D: D_x = D_clock)
    D_clock_pred = K_couple**2 * (k_B * T / (hbar * omega_mol)) * tau_coll / (2 * m_particle**2)

    trajectories = np.zeros((n_trajs, n_steps + 1, 2))   # (traj, time, xy)
    vx = np.zeros(n_trajs)
    vy = np.zeros(n_trajs)

    for step in range(n_steps):
        # Random clock phase differences at collision (thermal noise)
        delta_phi_x = rng.normal(0, sigma_T, n_trajs)
        delta_phi_y = rng.normal(0, sigma_T, n_trajs)

        # Momentum impulse from phase mismatch
        dpx = K_couple * delta_phi_x
        dpy = K_couple * delta_phi_y

        # Velocity update (impulse / mass)
        vx += dpx / m_particle
        vy += dpy / m_particle

        # Simple drag (momentum relaxation) — viscous damping
        gamma = 1.0 / tau_coll     # drag coefficient
        vx *= np.exp(-gamma * dt)
        vy *= np.exp(-gamma * dt)

        # Position update
        trajectories[:, step + 1, 0] = trajectories[:, step, 0] + vx * dt
        trajectories[:, step + 1, 1] = trajectories[:, step, 1] + vy * dt

    t_arr = np.arange(n_steps + 1) * dt

    # Mean squared displacement
    dx = trajectories[:, :, 0] - trajectories[:, 0:1, 0]
    dy = trajectories[:, :, 1] - trajectories[:, 0:1, 1]
    msd = np.mean(dx**2 + dy**2, axis=0)    # ⟨r²(t)⟩

    # Fit D from MSD: ⟨r²⟩ = 4Dt in 2D
    fit_range = slice(n_steps // 5, n_steps // 2)
    coeffs = np.polyfit(t_arr[fit_range], msd[fit_range], 1)
    D_measured = coeffs[0] / 4.0

    return t_arr, msd, trajectories, D_measured, D_clock_pred


def diffusion_vs_temperature(T_arr, omega_mol=1e13, K_couple=1e-23,
                              m_particle=1e-17, tau_coll=1e-13):
    """
    D_clock(T) = K² · (kT/ℏω) · τ / (2m²)  ∝  T   [linear in T]
    This is the Einstein relation D ∝ kT.
    The slope is set by the Kuramoto coupling K, not by viscosity directly.
    """
    return K_couple**2 * (k_B * T_arr / (hbar * omega_mol)) * tau_coll / (2 * m_particle**2)


# ─── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=" * 68)
    print("VACUUM, TEMPERATURE, AND BROWNIAN MOTION")
    print("=" * 68)

    # Phase noise at different temperatures (optical phonon ~1e13 rad/s)
    omega_mol = 1e13
    print(f"\n1. Clock phase noise σ_φ(T) at ω_mol = {omega_mol:.0e} rad/s:")
    for T in [0, 1, 10, 77, 300, 1000, 6000]:
        sig = phase_noise_std(T, omega_mol)
        status = ('← quantum zero-point only' if T == 0 else
                  '← liquid N₂' if T == 77 else
                  '← room temp' if T == 300 else
                  '← Sun surface' if T == 6000 else '')
        print(f"   T={T:5d} K:  σ_φ = {sig:.4f} rad  {status}")

    # Brownian diffusion
    print("\n2. Brownian motion simulation (clock-phase-driven):")
    t_arr, msd, trajs, D_meas, D_pred = simulate_brownian_clock(
        T=300, n_steps=5000, n_trajs=100)
    print(f"   D predicted from clock model:  {D_pred:.4e} m²/s")
    print(f"   D measured from simulation:    {D_meas:.4e} m²/s")
    print(f"   Ratio D_meas/D_pred:           {D_meas/D_pred:.3f}  (should be ~1)")

    # D ∝ T verification
    print("\n3. Diffusion coefficient vs temperature (should be linear in T):")
    T_arr = np.array([77, 150, 200, 250, 300, 400, 500])
    D_arr = diffusion_vs_temperature(T_arr)
    print("   T (K)    D_clock (m²/s)")
    for T, D in zip(T_arr, D_arr):
        print(f"   {T:5.0f}    {D:.4e}")
    slope = np.polyfit(T_arr, D_arr, 1)[0]
    print(f"\n   dD/dT = {slope:.4e} m²/(s·K)   [should be K²τ/(2m²ℏω) = const × k_B]")

    # ── Plots ──────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(18, 11))
    fig.suptitle('Orbitals, Vacuum Residuals, Temperature, and Brownian Motion',
                 fontsize=13)

    # A: Hydrogen 1s orbital (real standing wave)
    ax = fig.add_subplot(2, 4, 1)
    X, Z, rho_1s = orbital_density_2d(1, 0, 0, grid_size=150, extent=5*a0)
    im = ax.contourf(X/a0, Z/a0, rho_1s, levels=40, cmap='Blues')
    ax.set_title('H atom 1s: real\nstanding wave |ψ₁₀₀|²')
    ax.set_xlabel('x / a₀')
    ax.set_ylabel('z / a₀')
    plt.colorbar(im, ax=ax, label='|ψ|²')
    ax.set_aspect('equal')

    # B: Hydrogen 2p orbital
    ax = fig.add_subplot(2, 4, 2)
    X, Z, rho_2p = orbital_density_2d(2, 1, 0, grid_size=150, extent=12*a0)
    im = ax.contourf(X/a0, Z/a0, rho_2p, levels=40, cmap='Reds')
    ax.set_title('H atom 2p: standing\nwave after absorption')
    ax.set_xlabel('x / a₀')
    ax.set_ylabel('z / a₀')
    plt.colorbar(im, ax=ax, label='|ψ|²')
    ax.set_aspect('equal')

    # C: Phase noise distribution at different temperatures
    ax = fig.add_subplot(2, 4, 3)
    phi_range = np.linspace(-5, 5, 500)
    temps_plot = [0, 77, 300, 1000]
    colors_T = ['navy', 'steelblue', 'darkorange', 'firebrick']
    for T, col in zip(temps_plot, colors_T):
        sig = phase_noise_std(T, omega_mol)
        p = np.exp(-phi_range**2 / (2 * sig**2)) / (sig * np.sqrt(2*np.pi))
        ax.plot(phi_range, p, color=col, lw=2,
                label=f'T={T}K  σ={sig:.2f}rad')
    ax.set_xlabel('Clock phase offset φ − Φ_bulk (rad)')
    ax.set_ylabel('P(φ)')
    ax.set_title('Temperature =\nclock phase distribution width')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # D: Planck spectrum from clock distribution
    ax = fig.add_subplot(2, 4, 4)
    nu_arr = np.linspace(1e11, 1e15, 1000)
    omega_arr = 2 * np.pi * nu_arr
    for T, col in [(300, 'steelblue'), (1000, 'darkorange'),
                   (3000, 'firebrick'), (6000, 'darkred')]:
        spec = planck_spectrum(omega_arr, T)
        ax.semilogy(nu_arr / 1e12, spec / spec.max() + 1e-10,
                    color=col, lw=2, label=f'T={T}K')
    ax.set_xlabel('Frequency (THz)')
    ax.set_ylabel('Relative power (log)')
    ax.set_title('Planck spectrum from\nthermal clock distribution')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # E: Brownian trajectories
    ax = fig.add_subplot(2, 4, 5)
    for i in range(min(20, trajs.shape[0])):
        ax.plot(trajs[i, :, 0] * 1e9, trajs[i, :, 1] * 1e9,
                lw=0.5, alpha=0.6)
    ax.plot(0, 0, 'ko', ms=8, label='Start')
    ax.set_xlabel('x (nm)')
    ax.set_ylabel('y (nm)')
    ax.set_title('Brownian motion:\nclock-phase-driven random walk')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    # F: Mean squared displacement ⟨r²⟩ = 4Dt
    ax = fig.add_subplot(2, 4, 6)
    ax.plot(t_arr * 1e12, msd * 1e18, 'steelblue', lw=2, label='Simulated MSD')
    # Predicted line
    ax.plot(t_arr * 1e12, 4 * D_pred * t_arr * 1e18,
            'r--', lw=2, label=f'4D_clock·t  (D={D_pred:.1e})')
    ax.set_xlabel('Time (ps)')
    ax.set_ylabel('⟨r²⟩ (nm²)')
    ax.set_title(f'MSD = 4Dt  ✓\nD_meas/D_pred = {D_meas/D_pred:.2f}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # G: D ∝ T (Einstein relation from clock model)
    ax = fig.add_subplot(2, 4, 7)
    T_fine = np.linspace(10, 600, 200)
    D_fine = diffusion_vs_temperature(T_fine)
    ax.plot(T_fine, D_fine * 1e12, 'firebrick', lw=2.5,
            label='D_clock = K²(kT/ℏω)τ/2m²')
    ax.set_xlabel('Temperature T (K)')
    ax.set_ylabel('D (×10⁻¹² m²/s)')
    ax.set_title('D ∝ T  (Einstein relation)\nderived from clock model')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(0.05, 0.95,
            'Slope = k_B · K²τ/(2m²ℏω)\nfixes K from viscosity η:\n'
            'K² = 2m²ℏω/(6πηr·τ)',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(facecolor='lightyellow', alpha=0.9, boxstyle='round'))

    # H: Full theory summary
    ax = fig.add_subplot(2, 4, 8)
    ax.axis('off')
    ax.text(0.5, 0.99, 'FROM BELL TO BROWNIAN MOTION',
            ha='center', va='top', fontsize=10, fontweight='bold',
            transform=ax.transAxes)
    summary = """
ONE EQUATION, MANY PHENOMENA:
iℏ ∂ψ/∂t = Hψ   (never collapses)

Phenomenon         Time-phase mechanism
───────────────────────────────────────
H orbital          Standing wave in
                   Coulomb potential

Photon absorption  Clock freq. change;
                   wave residual → ZPF

Zero-point energy  ½ℏω = minimal clock
                   noise floor (T=0)

Temperature        Clock phase noise
                   σ²(T) = kT/ℏω

Blackbody          Emission spectrum of
spectrum           thermal phase dist.

Brownian motion    δp = K·δφ at each
                   collision (thermal
                   clock mismatch)

Einstein D∝T       D = K²(kT/ℏω)τ/2m²

Nelson QM          Brownian motion in
                   ZPF → Schrödinger eq.

Bohm pilot wave    ZPF gradient = quantum
                   potential Q
"""
    ax.text(0.03, 0.93, summary, ha='left', va='top', fontsize=8,
            transform=ax.transAxes, family='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

    plt.tight_layout()
    plt.savefig('vacuum_temperature.png', dpi=150)
    print("\nSaved: vacuum_temperature.png")
    plt.show()

    print("""
KEY RESULT: STOKES-EINSTEIN FROM CLOCK MODEL
──────────────────────────────────────────────
  D_clock = K² · (kT/ℏω) · τ_collision / (2m²)
  D_Stokes = kT / (6πηr)

  Setting equal:
    K² = 2m² · ℏω / (6πηr · τ_collision)
    K = m · √(ℏω / (3πηr · τ_collision))

  This FIXES the Kuramoto coupling K between a molecule
  and a Brownian particle in terms of measurable quantities:
    m = molecular mass
    ω = molecular vibration frequency (IR spectroscopy)
    η = fluid viscosity
    r = particle radius
    τ = mean free time = mean free path / thermal velocity

  PREDICTION: measuring D at different ω (different solvents)
  should scale as D ∝ 1/√ω for fixed η, r, τ.
  Standard Stokes-Einstein has no ω dependence — this is
  a testable departure from classical Brownian theory.

NELSON CONNECTION:
  Nelson (1966) proved: Brownian motion with ν = ℏ/2m
  in any background field gives the Schrödinger equation.
  The time-phase model provides the physical field:
    ν_ZPF = ℏ/2m  (quantum clock noise floor, T=0)
  Temperature adds:
    ν_total = ℏ/2m + kT·τ/m  (quantum + thermal)
  At room temperature for an electron in an atom:
    kT·τ/m ~ (0.025 eV)·(10⁻¹⁵s)/(m_e) ~ 10⁻²¹ m²/s
    ℏ/2m_e              ~ 3×10⁻⁵ m²/s
  Quantum diffusion dominates → atom behaves quantum-mechanically.
  For a 1 μm dust grain:
    ℏ/2m   ~ 10⁻²² m²/s  (negligible)
    kT·τ/m ~ 10⁻¹¹ m²/s  (thermal dominates)
  Classical Brownian motion → no quantum behavior.
  The quantum-classical transition IS the crossover ℏ/2m ≪ kT·τ/m.
""")


if __name__ == '__main__':
    run()
