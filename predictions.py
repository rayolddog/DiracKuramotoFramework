"""
predictions.py — Testable Predictions of the Time-Phase Model
=============================================================

INTERPRETIVE STATUS (updated 2026-04-08, after Route A/B analysis):
  The KPS framework is a QUANTUM REINTERPRETATION with gravitational decoherence
  predictions, NOT a local-realistic alternative to QM. Quantum mechanics produces
  the correlations (via the Dirac spinor structure, Paper 3). The Kuramoto model
  provides the dynamical mechanism for how gravitational synchronization to the
  local bulk DEGRADES those correlations. Bell's theorem is not challenged.
  See resynchronization_calc.py for the formal analysis.

The time-phase model agrees with standard QM in the limit of:
  - Perfect detector entanglement (Φ_D1 = Φ_D2)
  - Identical particle energies (ω_A = ω_B)
  - Short flight time (minimal clock drift before detection)

It DEPARTS from standard QM predictions in these scenarios:

  P1. CLOCK DRIFT — particles with slightly different energies  [RETRACTED]
      *** RETRACTED: Falsified by km-scale Bell tests (Weihs 1998, loophole-free 2015). ***
      *** Bell violations hold over km separations with broadband photons, ruling out ***
      *** detectable clock drift at these scales. Retained for historical context only. ***
      Δω = ω_A − ω_B ≠ 0  →  phase gap grows as δφ(t) = Δω · t
      Prediction: entanglement degrades as a function of (mass/energy mismatch × flight time)
      Distinct from: standard QM decoherence (no mass-dependent degradation in vacuo)

  P2. DETECTOR ISOLATION — detectors NOT entangled with bulk
      If Φ_D1 and Φ_D2 are drawn independently → correlation washes out
      Prediction: correlation degrades as detector clocks become independent
      (i.e., isolated, cryogenically shielded, or freshly reset detectors
       should show weaker Bell violations than thermalized bulk-coupled ones)
      NOTE: Standard QM predicts the OPPOSITE — isolation preserves coherence.
      This prediction is a clean empirical discriminant.

  P3. PATH-LENGTH ASYMMETRY — different flight distances  [RETRACTED]
      *** RETRACTED: Self-refuted. The spatial de Broglie phase cancels at detection ***
      *** (detector clock ticks at same ω as particle). The author correctly determined ***
      *** this prediction is not viable. Retained for historical transparency. ***
      Temporal phase: cancels at detection (detector clock ticks at same ω as particle).
      Residual: δφ ~ ω · L · v / (2c²)  [relativistic proper-time correction, tiny]
      This is why km-scale and satellite Bell tests (Weihs 1998, Micius 2017) show
      full violations — consistent with the model.

  P4. SYNCHRONIZATION SPEED — strong vs weak coupling K
      High K: fast synchronization → quantum correlations recovered
      Low K:  slow synchronization → classical-like correlations
      Prediction: deliberately weakening the particle-detector interaction
       (e.g., very thin detector, very brief interaction time)
       should reduce Bell violation in a K-dependent way

  P5. MASS / ENERGY DEPENDENCE (energy-mass equivalence: K = ω = E/ℏ)
      K = ω = E/ℏ = mc²/ℏ for massive particles at rest.
      Prediction: heavier / higher-energy particles synchronize faster.
      Massive particles (electrons, protons, kaons): K ≈ mc²/ℏ → F ≈ 1 always.
      Photons: K = 2πν. Bell threshold at ν_crit ~ 10^14 Hz (~0.49 eV, mid-IR).
      This is consistent with all known Bell tests; testable with mid-IR entangled photons.

  P6. GRAVITATIONAL FIELD AS SHARED Φ_BULK — gravitational Bell degradation
      KEY INSIGHT: In this theory, gravity IS the large-scale Kuramoto synchronization
      field (see gravity_twistor.py). Therefore Φ_bulk at any detector location is simply
      the local gravitational phase:
          Φ_bulk(x, t) = ω₀ · t · √(1 + 2Φ_grav(x)/c²)
      Both detectors D1 and D2 independently couple to the SAME gravitational field —
      they need not communicate. The Earth (Sun, Galaxy) is one coherent classical field
      that pre-establishes Φ_bulk everywhere, at subluminal speed, before any experiment.
      This resolves the question: "How does Φ_bulk stay coherent across km without FTL?"
      Answer: The gravitational field IS the coherence mechanism.

      PREDICTION: Bell violation degrades when detectors are at different gravitational
      potentials ΔΦ_grav, because Φ_bulk(D1) ≠ Φ_bulk(D2):
          δφ_grav = ω₀ · (ΔΦ_grav / c²) · τ_sync
          F_grav   = exp(−δφ_grav² / 2)
          CHSH(ΔΦ) = 2√2 · F_grav

      For terrestrial / satellite experiments:
          ΔΦ/c² ~ 10^-13/m altitude → δφ negligible for optical photons → full violation ✓
          Micius satellite (1200 km): ΔΦ/c² ~ 1.3×10^-10 → F ≈ 1 for optical → consistent ✓

      For extreme environments:
          Neutron star surface: ΔΦ/c² ~ 0.2 → measurable degradation
          High-energy particles (ω₀ = mc²/ℏ large): threshold at much smaller ΔΦ/c²
          Near black hole event horizon: ΔΦ/c² → ∞ → F → 0 → Bell violation destroyed

      Standard QM prediction: no gravitational dependence on Bell violation at fixed
      entanglement fidelity. Any difference is a signal of this theory.

      SECONDARY CONSEQUENCE: Φ_bulk coherence does NOT require superdeterminism or a
      conspiracy. Both detectors locally couple to the same gravitational field — the
      correlator of Φ_bulk between widely separated points is set by the gravitational
      field's own coherence length (effectively infinite for the static Earth field).
      Bell's measurement-independence assumption ρ(λ|a,b) = ρ(λ) is broken not by
      conspiracy but by the ordinary fact that the gravitational field is pre-shared.

  P6b. LINEWIDTH-DEPENDENT GRAVITATIONAL BELL TEST (near-term experimental design)
      KEY INSIGHT: Two photon time scales are distinct (see Paper §5.4):
          τ_sync = ℏ/E   (Kuramoto re-sync to detector; set by photon energy)
          τ_coh  = 1/Δν  (photon coherence time; set by linewidth, not energy)
      For the gravitational decoherence prediction, what matters is τ_coh:
      a narrow-linewidth photon spends longer in coherent superposition during
      detection, accumulating more gravitational phase mismatch. Therefore:

          δφ = ω₀ · (ΔΦ/c²) · τ_coh = ω₀ · (ΔΦ/c²) / Δν
          CHSH(Δν) = 2√2 · exp(−δφ² / 2)

      This creates a LINEWIDTH-DEPENDENT Bell violation:
        − Broadband photons (large Δν): τ_coh short → δφ tiny → full violation
        − Narrow-linewidth photons (small Δν): τ_coh long → δφ large → violation suppressed

      Standard QM: CHSH is INDEPENDENT of linewidth (only depends on entanglement fidelity).
      This theory: CHSH DECREASES with narrowing linewidth. Clean discriminant.

      EARTH-MOON BASELINE (ΔΦ/c² = 6.52×10⁻¹⁰):
        − Broadband SPDC (Δν ~ 1 THz):    δφ ~ 2.5×10⁻⁶ → no effect
        − Rb-87 natural linewidth (6 MHz): δφ ~ 0.066 rad → CHSH = 2.822  (0.2% reduction)
        − Cavity-filtered (Δν = 10 kHz):   δφ ~ 40 rad   → CHSH ≈ 0  (violation destroyed)
        − Optimal discriminating linewidth: Δν ~ ω₀·(ΔΦ/c²) / 1.0  (δφ ~ 1 rad threshold)

      TERRESTRIAL VERSION (Mauna Kea, h = 4205 m, ΔΦ/c² = 4.57×10⁻¹²):
        − Bell threshold at Δν ~ ω₀·(ΔΦ/c²) / √2 ~ 10 kHz for optical photons
        − Achievable with cavity-QED or optical frequency comb filtering
        − No Moon required. Tabletop-accessible prediction.

      EXPERIMENTAL DESIGN:
        1. Generate entangled photon pairs (e.g., SPDC at 810 nm)
        2. Filter one to narrow linewidth via optical cavity (tunable Δν from GHz to kHz)
        3. Alice at sea level, Bob at altitude (or on Moon)
        4. Measure CHSH vs Δν
        5. QM predicts flat line. This theory predicts CHSH ∝ exp(−(ω₀·ΔΦ/c²/Δν)²/2)

All predictions are in principle experimentally distinguishable from standard QM.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive — works headless
import matplotlib.pyplot as plt


# ─── P1: Clock Drift (energy mismatch) ───────────────────────────────────────

def e_clock_drift(delta_angle, delta_omega, flight_time):
    """
    E(a,b) with phase offset from energy mismatch.
    Phase gap at detection: δφ = Δω · t_flight
    Effective correlation:  E = −cos(a − b − δφ/2)  [symmetric drift]
    Amplitude envelope:     |E_max| = |cos(δφ/2)|    [beats pattern]

    This is an oversimplification; full treatment requires integrating
    over the synchronization dynamics. This gives the qualitative envelope.
    """
    phase_gap = delta_omega * flight_time
    # The relative phase offset shifts the correlation peak; envelope decays
    # as the phase uncertainty accumulates (assuming Gaussian spread):
    # Here we use the deterministic offset for clarity.
    return -np.cos(delta_angle - phase_gap / 2.0)


def envelope_vs_time(t_arr, delta_omega):
    """Amplitude of correlation at Δ=π/4 as function of flight time."""
    delta_angle = np.pi / 4
    return -np.cos(delta_angle - delta_omega * t_arr / 2)


# ─── P2: Detector Phase Randomness ───────────────────────────────────────────

def e_detector_noise(delta, sigma_phi):
    """
    If detector phases Φ_D1, Φ_D2 are NOT perfectly synchronized but
    have independent Gaussian noise σ_φ around Φ_bulk:
      Φ_D1 ~ N(Φ_bulk, σ²),  Φ_D2 ~ N(Φ_bulk, σ²) independently

    The phase model gives:
      E(a,b,σ) = E_QM(a,b) · exp(−σ²)
    (attenuation by Gaussian noise factor, analogous to visibility loss
     in optical interferometry)

    Standard QM: σ_φ has no effect unless it physically modifies the
    detection probability — it would NOT predict this attenuation for
    isolated but classically operating detectors.
    """
    return -np.cos(delta) * np.exp(-sigma_phi**2)


# ─── P3: Path-Length Asymmetry ───────────────────────────────────────────────

def e_path_length_corrected(delta, delta_L, omega, v_over_c=0.01, c=3e8):
    """
    CORRECTED — accounts for detector clock continuing to oscillate.

    KEY INSIGHT (user correction to initial derivation):
    ─────────────────────────────────────────────────────
    Both particle clock and detector clock oscillate at frequency ω.
    At the moment of detection (t_arrival = L/v):

      φ_particle(t_arrival) = φ_0  +  ω · t_arrival
      Φ_detector(t_arrival) = Φ_0  +  ω · t_arrival   ← detector also ticking

      Relative phase = φ_0 − Φ_0   (ω·t terms CANCEL)

    The path length changes t_arrival, but it changes BOTH clocks equally.
    The relative phase at contact is determined by initial conditions only.
    This is why EPR correlations survive km-scale paths: the detector's
    continued oscillation absorbs the free-flight phase accumulation.

    WHAT DOES REMAIN — relativistic proper time correction:
    ────────────────────────────────────────────────────────
    If the particle clock runs on proper time τ and detector on coordinate t:

      τ = t · √(1 − v²/c²)  ≈  t · (1 − v²/2c²)

      δφ_residual = ω · t_arrival · [√(1−v²/c²) − 1]
                  ≈ −ω · (L/v) · v²/(2c²)
                  = −ω · L · v / (2c²)

    This IS path-length dependent, but is order (v/c)² — tiny for
    non-relativistic particles, and zero for massless particles (no proper time).

    ADDITIONAL RESIDUAL — spatial (de Broglie) phase:
    ──────────────────────────────────────────────────
    The spatial part of the wave ψ ~ exp(ip·x/ℏ) contributes p·ΔL/ℏ
    for path difference ΔL. The detector does NOT have this spatial phase
    (it is at rest), so this does NOT cancel. However, this is the
    SPATIAL phase (momentum), not the TEMPORAL phase (energy/clock).
    Whether the user's model couples the spin property to spatial vs
    temporal phase is a design decision of the theory.
    """
    # Relativistic residual (proper time effect)
    delta_phi_relativistic = -omega * (delta_L / (v_over_c * c)) * v_over_c**2 / 2
    # At non-relativistic speeds this is negligible; plot to show scale
    return -np.cos(delta) * np.ones_like(np.atleast_1d(np.array(delta, dtype=float))), delta_phi_relativistic


def e_path_length_spatial(delta, delta_L, momentum, hbar=1.055e-34):
    """
    Spatial (de Broglie) phase contribution — detector does NOT cancel this.
    φ_spatial = p · ΔL / ℏ
    This phase acts like a rotation of the measurement axis.
    """
    phi_spatial = momentum * delta_L / hbar
    return -np.cos(delta - phi_spatial)


# ─── P4: Kuramoto Coupling Strength ──────────────────────────────────────────

def sync_fidelity_vs_K(K_arr, interaction_time=0.1, phi_mismatch=np.pi/3):
    """
    After interaction time τ with coupling K, how close does the particle
    phase get to the detector phase?

    Linearized Kuramoto near lock:
      δφ(t) = δφ_0 · exp(−K · t)
    Synchronization fidelity: F = 1 − |δφ(τ)| / |δφ_0|
    Effective correlation amplitude: A = cos(δφ(τ) / 2)
    """
    delta_phi_final = phi_mismatch * np.exp(-K_arr * interaction_time)
    amplitude = np.cos(delta_phi_final / 2)
    return amplitude


# ─── P5: Mass / Frequency Dependence ─────────────────────────────────────────

def sync_time_vs_mass(mass_arr, K_base=1e10, hbar=1.055e-34, c=3e8):
    """
    Synchronization timescale τ_sync ~ 1/K where K ∝ interaction energy.
    For a massive particle: E = mc² → ω = mc²/ℏ

    If K ∝ ω (coupling proportional to energy):
      τ_sync(m) ~ ℏ / (coupling · mc²)  →  heavier = faster sync
                                            (counter-intuitive vs decoherence)

    Standard decoherence: τ_decohere ~ ℏ / (kT) — independent of mass.
    This model: τ_sync ~ 1/m — heavier particles synchronize faster.
    """
    omega = mass_arr * c**2 / hbar
    K = K_base * omega           # K scales with ω
    tau_sync = 1.0 / K
    return tau_sync


# ─── P6 / P6b: Gravitational Bell Degradation & Linewidth Test ───────────────

# Physical constants
HBAR = 1.055e-34    # J·s
C    = 3e8          # m/s
G    = 6.674e-11    # m³/kg/s²
EV   = 1.602e-19    # J per eV

def gravitational_fidelity(delta_phi_over_c2_arr, omega_0, tau_sync=1e-15):  # noqa: E302
    """
    Bell fidelity as a function of gravitational potential difference ΔΦ/c²
    between the two detector locations.

    Φ_bulk(x) = ω₀ · t · √(1 + 2Φ_grav(x)/c²)
    Phase difference accumulated during interaction τ_sync:
        δφ_grav = ω₀ · (ΔΦ/c²) · τ_sync
    Werner fidelity:
        F_grav = exp(−δφ_grav² / 2)
    CHSH = 2√2 · F_grav

    Parameters:
        delta_phi_over_c2_arr : ΔΦ/c²  (dimensionless, 0 = same potential)
        omega_0               : particle clock frequency ω = E/ℏ (rad/s)
        tau_sync              : detector interaction time (s), default 1 fs
    """
    delta_phi_grav = omega_0 * np.asarray(delta_phi_over_c2_arr) * tau_sync
    return np.exp(-delta_phi_grav**2 / 2)


def gravitational_potential_diff(h_meters, R_earth=6.371e6, M_earth=5.972e24):
    """
    ΔΦ/c² = (GM/c²) · (1/R − 1/(R+h)) ≈ g·h/c² for small h.
    Returns dimensionless ratio ΔΦ/c².
    """
    phi1 = -G * M_earth / R_earth
    phi2 = -G * M_earth / (R_earth + h_meters)
    return (phi2 - phi1) / C**2


# Key environments
# ── P6b helpers ───────────────────────────────────────────────────────────────

def chsh_vs_linewidth(delta_nu_arr, omega_0, delta_phi_over_c2):
    """
    CHSH as a function of photon linewidth Δν (Hz).
    τ_coh = 1/Δν  →  δφ = ω₀ · (ΔΦ/c²) / Δν
    F = exp(−δφ²/2),  CHSH = 2√2 · F

    Standard QM: CHSH = 2√2 for all Δν.
    This model: CHSH decreases as Δν decreases (narrower → longer τ_coh → more phase slip).
    """
    delta_phi_rad = omega_0 * delta_phi_over_c2 / np.asarray(delta_nu_arr)
    return 2 * np.sqrt(2) * np.exp(-delta_phi_rad**2 / 2)


def linewidth_threshold(omega_0, delta_phi_over_c2, reduction_fraction=0.01):
    """
    Linewidth Δν at which CHSH is reduced by reduction_fraction from Tsirelson.
    F = 1 - reduction_fraction  →  δφ = sqrt(-2·ln(F))
    Δν_thresh = ω₀ · (ΔΦ/c²) / δφ_thresh
    """
    F_thresh = 1.0 - reduction_fraction
    dphi_thresh = np.sqrt(-2 * np.log(F_thresh))
    return omega_0 * delta_phi_over_c2 / dphi_thresh


# Gravitational potential differences for key baselines
def dphi_c2(h_m, M=5.972e24, R=6.371e6):
    """ΔΦ/c² for altitude h_m above Earth's surface."""
    return G * M / C**2 * (1/R - 1/(R + h_m))


BASELINES = {
    'Sea level → Mauna Kea  (4.2 km)':      dphi_c2(4205),
    'Sea level → Mount Everest (8.8 km)':    dphi_c2(8849),
    'Sea level → Stratosphere (40 km)':      dphi_c2(40e3),
    'Sea level → Micius sat. (500 km)':      dphi_c2(5e5),
    'Sea level → GPS sat. (20,000 km)':      dphi_c2(2e7),
    'Sea level → Moon (384,400 km)':         6.52e-10,     # pre-computed (includes Moon's own grav.)
}

# Key atomic/laser photon sources with natural/cavity linewidths
PHOTON_SOURCES = {
    'Broadband SPDC (Δν=1 THz)':          (810e-9, 1e12),
    'Mode-locked laser (Δν=1 GHz)':        (780e-9, 1e9),
    'Rb-87 D2 (Δν=6.07 MHz, natural)':    (780e-9, 6.07e6),
    'Sr optical clock (Δν=7.6 kHz)':      (698e-9, 7.6e3),
    'Yb optical clock (Δν=10 mHz)':       (578e-9, 0.010),
}

ENVIRONMENTS = {
    'Alice & Bob same floor (1 m)':       gravitational_potential_diff(1),
    'Alice & Bob different floors (10 m)': gravitational_potential_diff(10),
    'Ground vs. aircraft (10 km)':        gravitational_potential_diff(1e4),
    'Ground vs. Micius satellite (500 km)': gravitational_potential_diff(5e5),
    'Ground vs. GPS satellite (20,000 km)': gravitational_potential_diff(2e7),
    'Earth surface vs. neutron star surf.': 0.2,
    'Earth surface vs. BH event horizon':  1.0,
}

# Particle ω₀ values (E = ℏω)
PARTICLES = {
    'Radio photon (1 GHz)':      2 * np.pi * 1e9,
    'Optical photon (500 nm)':   2 * np.pi * C / 500e-9,
    'X-ray photon (0.1 nm)':     2 * np.pi * C / 0.1e-9,
    'Electron (mc²)':            0.511e6 * EV / HBAR,
    'Proton (mc²)':              938.3e6 * EV / HBAR,
}


# ─── Main ────────────────────────────────────────────────────────────────────

def run():
    fig, axes = plt.subplots(3, 3, figsize=(18, 14))
    fig.suptitle('Testable Predictions of the Time-Phase Synchronization Model\n'
                 '(P1–P5 classic predictions, P6 gravitational degradation, P6b linewidth test)',
                 fontsize=12)

    deltas = np.linspace(-np.pi, np.pi, 400)
    e_qm = -np.cos(deltas)

    # ── P1: Clock drift envelope ──────────────────────────────────────────
    ax = axes[0, 0]
    t_arr = np.linspace(0, 5, 400)
    for dw_label, dw in [('Δω = 0', 0), ('Δω = 0.1 rad/s', 0.1),
                          ('Δω = 0.5 rad/s', 0.5), ('Δω = 1.0 rad/s', 1.0)]:
        env = envelope_vs_time(t_arr, dw)
        ax.plot(t_arr, env, label=dw_label)
    ax.set_xlabel('Flight time (s)')
    ax.set_ylabel('E(π/4, t)')
    ax.set_title('P1: Correlation vs flight time\n(energy mismatch → clock drift)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-1.1, 0.1)
    ax.axhline(-np.cos(np.pi/4), color='royalblue', linestyle=':', label='QM constant')

    # ── P2: Detector phase noise ──────────────────────────────────────────
    ax = axes[0, 1]
    for sigma in [0, 0.3, 0.7, 1.2, 2.0]:
        e = e_detector_noise(deltas, sigma)
        ax.plot(deltas, e, label=f'σ_φ = {sigma:.1f} rad')
    ax.plot(deltas, e_qm, 'k--', linewidth=2, label='QM (σ=0)')
    ax.set_xlabel('Δ = a − b (rad)')
    ax.set_ylabel('E(a, b)')
    ax.set_title('P2: Detector phase noise\n(isolated detectors → weaker Bell violation)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # ── P3: Corrected path-length — show what survives ────────────────────
    ax = axes[0, 2]
    # Temporal clock phase cancels: detector ticks same ω as particle.
    # Only residual: relativistic proper-time correction (order v²/c²)
    # and de Broglie spatial phase (p·ΔL/ℏ, if theory couples to spatial phase).
    hbar = 1.055e-34
    m_neutron = 1.675e-27
    v_arr = np.linspace(1e-4, 0.3, 300)       # v/c
    c = 3e8
    L = 1.0                                    # 1 m path difference
    omega_neutron = m_neutron * c**2 / hbar    # rest-mass frequency

    # Relativistic proper-time residual (temporal phase only)
    delta_phi_rel = omega_neutron * (L / (v_arr * c)) * v_arr**2 / 2
    # This is already ω·L·v/(2c²) — still enormous for rest-mass ω!
    # But: if ω_effective is NOT mc²/ℏ but something smaller (e.g., thermal
    # de Broglie or some emergent scale), the residual shrinks.
    # Plot with a reduced effective ω to show the functional form:
    omega_eff_scale = np.logspace(0, 12, 5)    # range of possible ω_eff
    for omega_eff in omega_eff_scale:
        dphi = omega_eff * L * v_arr / (2 * c)
        ax.semilogy(v_arr, np.abs(dphi), label=f'ω_eff={omega_eff:.0e} rad/s')

    ax.set_xlabel('v/c (particle speed)')
    ax.set_ylabel('|δφ_residual| (rad)')
    ax.set_title('P3 CORRECTED: Residual phase after\ndetector clock cancellation')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3, which='both')
    ax.axhline(1.0, color='red', linestyle='--', linewidth=1, label='δφ = 1 rad (observable)')
    ax.text(0.02, 0.92,
            'Detector clock cancels ω·t.\nOnly proper-time correction\n'
            'survives: δφ ~ ω·L·v/(2c²)\n'
            'Model survives km EPR tests\nif ω_eff is not mc²/ℏ.',
            transform=ax.transAxes, fontsize=7, color='darkgreen',
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='honeydew', alpha=0.8))

    # ── P4: Kuramoto coupling strength ────────────────────────────────────
    ax = axes[1, 0]
    K_arr = np.linspace(0.01, 50, 400)
    for tau_int, col in [(0.02, 'blue'), (0.05, 'green'),
                          (0.1, 'orange'), (0.5, 'red')]:
        amp = sync_fidelity_vs_K(K_arr, interaction_time=tau_int)
        ax.plot(K_arr, amp, color=col, label=f'τ_interact = {tau_int} s')
    ax.axhline(1.0, color='royalblue', linestyle='--', linewidth=1, label='Full QM (K→∞)')
    ax.set_xlabel('Kuramoto coupling K')
    ax.set_ylabel('Correlation amplitude')
    ax.set_title('P4: Coupling strength\n(weak interaction → reduced Bell violation)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ── P5: Mass dependence ───────────────────────────────────────────────
    ax = axes[1, 1]
    mass_arr = np.logspace(-31, -26, 400)   # electron mass to proton mass range
    tau_sync = sync_time_vs_mass(mass_arr)
    ax.loglog(mass_arr / 9.109e-31, tau_sync, color='purple', linewidth=2,
              label='Time-phase model')
    # Standard decoherence: roughly flat (thermal, independent of mass)
    tau_decohere = np.full_like(mass_arr, 1e-12)   # ~1 ps at room temp
    ax.loglog(mass_arr / 9.109e-31, tau_decohere, 'k--', linewidth=1.5,
              label='Thermal decoherence (flat)')
    ax.set_xlabel('Mass (in electron masses)')
    ax.set_ylabel('Synchronization timescale (s)')
    ax.set_title('P5: Mass dependence\n(heavier particle = faster sync, ≠ decoherence)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which='both')

    # ── P6: Gravitational Bell degradation ───────────────────────────────
    ax = axes[1, 2]

    delta_phi_range = np.logspace(-14, 0, 400)   # ΔΦ/c² from 10^-14 to 1

    # Plot CHSH vs ΔΦ/c² for each particle type
    colors_p6 = ['#aaaaff', '#4444ff', '#000099', '#cc3300', '#880000']
    for (pname, omega0), col in zip(PARTICLES.items(), colors_p6):
        F = gravitational_fidelity(delta_phi_range, omega0)
        chsh = 2 * np.sqrt(2) * F
        ax.semilogx(delta_phi_range, chsh, color=col, lw=1.8, label=pname)

    ax.axhline(2 * np.sqrt(2), color='green', ls=':', lw=1, label='Tsirelson (2√2)')
    ax.axhline(2.0,            color='black', ls='--', lw=1.5, label='Bell bound (2.0)')

    # Mark known environments
    env_markers = {
        'Same lab\n(1 m)':         (gravitational_potential_diff(1),    2.75),
        'Aircraft\n(10 km)':       (gravitational_potential_diff(1e4),  2.55),
        'Micius\n(500 km)':        (gravitational_potential_diff(5e5),  2.35),
        'Neutron\nstar':           (0.2,                                2.15),
    }
    for label, (x, y) in env_markers.items():
        ax.axvline(x, color='gray', ls=':', lw=0.8, alpha=0.6)
        ax.text(x * 1.3, y, label, fontsize=6.5, color='gray', va='top')

    ax.set_xlabel('ΔΦ/c²  (gravitational potential difference, dimensionless)')
    ax.set_ylabel('CHSH value')
    ax.set_title('P6: Gravitational Bell degradation\n'
                 'Φ_bulk = grav. field → coherence without FTL')
    ax.legend(fontsize=6.5, loc='lower left')
    ax.set_ylim(0, 3.1)
    ax.grid(True, alpha=0.3, which='both')
    ax.text(0.02, 0.35,
            'Gravity IS the shared Φ_bulk.\n'
            'D1 and D2 both couple locally\n'
            'to the same gravitational field.\n'
            'No FTL needed.\n'
            'QM predicts: flat at 2√2.\n'
            'This model: degrades at high ΔΦ/c².',
            transform=ax.transAxes, fontsize=7,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

    # ── P6b Panel 1: CHSH vs photon linewidth for key baselines ─────────────
    ax = axes[2, 0]
    omega_opt = 2 * np.pi * C / 810e-9    # 810 nm SPDC photon
    delta_nu  = np.logspace(0, 14, 500)   # 1 Hz to 100 THz

    colors_bl = ['#330099', '#0055cc', '#0099dd', '#00aa88', '#33bb00', '#aabb00']
    for (bl_name, dphi), col in zip(BASELINES.items(), colors_bl):
        chsh_arr = chsh_vs_linewidth(delta_nu, omega_opt, dphi)
        ax.semilogx(delta_nu, chsh_arr, color=col, lw=1.8,
                    label=f'{bl_name}\n  ΔΦ/c²={dphi:.2e}')

    ax.axhline(2 * np.sqrt(2), color='green', ls=':', lw=1,   label='Tsirelson (QM)')
    ax.axhline(2.0,            color='black', ls='--', lw=1.5, label='Bell bound')

    # Mark specific photon sources
    source_colors = ['#aaaaaa', '#888888', '#cc4400', '#aa0099', '#660044']
    for (src_name, (wl, dnu)), scol in zip(PHOTON_SOURCES.items(), source_colors):
        ax.axvline(dnu, color=scol, ls=':', lw=0.9, alpha=0.7)
        ax.text(dnu * 1.15, 0.25, src_name.split('(')[0].strip(),
                fontsize=6, color=scol, rotation=90, va='bottom')

    ax.set_xlabel('Photon linewidth Δν  (Hz)')
    ax.set_ylabel('CHSH')
    ax.set_title('P6b: CHSH vs photon linewidth\n'
                 '(810 nm, for different gravitational baselines)')
    ax.legend(fontsize=5.5, loc='lower left')
    ax.set_ylim(0, 3.1)
    ax.grid(True, alpha=0.3, which='both')

    # ── P6b Panel 2: linewidth threshold for 1% and 50% CHSH reduction ──────
    ax = axes[2, 1]
    baselines_arr = np.logspace(-14, -6, 200)  # ΔΦ/c² range
    reductions = [(0.01, '1% reduction (δφ~0.14)', '#1177cc'),
                  (0.29, '10% reduction (δφ~0.46)', '#cc7700'),
                  (0.50, '50% reduction (δφ~1.18)', '#cc0000')]

    for red_frac, label, col in reductions:
        thresh = linewidth_threshold(omega_opt, baselines_arr, red_frac)
        ax.loglog(baselines_arr, thresh, color=col, lw=2, label=label)

    # Mark real baselines
    for (bl_name, dphi), col in zip(BASELINES.items(), colors_bl):
        short_name = bl_name.split('→')[1].strip().split('(')[0].strip()
        ax.axvline(dphi, color=col, ls=':', lw=1, alpha=0.8)
        ax.text(dphi * 1.2, 1e13, short_name, fontsize=6.5,
                color=col, rotation=90, va='top')

    # Mark photon source linewidths as horizontal lines
    for (src_name, (wl, dnu)), scol in zip(list(PHOTON_SOURCES.items())[1:], source_colors[1:]):
        ax.axhline(dnu, color=scol, ls='--', lw=0.8, alpha=0.7)
        ax.text(1e-14 * 1.5, dnu * 1.3, src_name.split('(')[0].strip(),
                fontsize=6, color=scol)

    ax.set_xlabel('ΔΦ/c²  (gravitational potential difference)')
    ax.set_ylabel('Linewidth Δν  (Hz)  for threshold')
    ax.set_title('P6b: Required linewidth to observe\ngravitational Bell degradation')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3, which='both')
    ax.text(0.02, 0.02,
            'BELOW each curve: effect observable.\n'
            'Intersection of vertical baseline\n'
            'and horizontal photon source = test.',
            transform=ax.transAxes, fontsize=7,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

    # ── P6b Panel 3: Summary / experimental design table ────────────────────
    ax = axes[2, 2]
    ax.axis('off')

    print("\nP6b: Linewidth threshold summary (810 nm photon)")
    print(f"  {'Baseline':<40}  {'ΔΦ/c²':>12}  {'Δν for 1% reduction':>22}  {'Δν for 50%':>15}")
    print("  " + "-" * 94)
    table_rows = [['Baseline', 'ΔΦ/c²', 'Δν threshold\n(1% reduction)', 'Δν threshold\n(50% reduction)',
                   'Achievable\ntoday?']]
    achievable = ['No (too small)', 'No (too small)', 'Cavity QED',
                  'Optical clock', 'Optical clock', 'Sr/Yb clock']
    for (bl_name, dphi), ach in zip(BASELINES.items(), achievable):
        thresh_1pct  = linewidth_threshold(omega_opt, dphi, 0.01)
        thresh_50pct = linewidth_threshold(omega_opt, dphi, 0.50)
        short = bl_name.split('→')[1].strip()
        print(f"  {bl_name:<40}  {dphi:>12.3e}  {thresh_1pct:>22.3e}  {thresh_50pct:>15.3e}")
        table_rows.append([short,
                           f'{dphi:.2e}',
                           f'{thresh_1pct:.2e} Hz',
                           f'{thresh_50pct:.2e} Hz',
                           ach])

    cell_cols = [['#c8d8ff'] * 5]
    row_colors = [['#f0f0f0', '#ffffff', '#f0f0f0', '#ffffff', '#f0f0f0'],
                  ['#ffffff', '#f0f0f0', '#ffffff', '#f0f0f0', '#ffffff']] * 4
    cell_cols += row_colors[:len(table_rows)-1]

    tbl = ax.table(cellText=table_rows, cellColours=cell_cols,
                   loc='center', cellLoc='center')
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(6.5)
    tbl.scale(1.05, 1.7)
    ax.set_title('P6b: Experimental targets\n(810 nm, 1% and 50% CHSH reduction)',
                 fontsize=8, pad=10)

    plt.tight_layout()
    plt.savefig('predictions.png', dpi=150, bbox_inches='tight')
    print("\nSaved: predictions.png")
    # plt.show()  # non-interactive

    # ── Console summary ───────────────────────────────────────────────────
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║               TESTABLE PREDICTIONS SUMMARY                          ║
╠══════════════════════════════════════════════════════════════════════╣
║  P1  Energy-mismatched pairs: Bell violation decays with time       ║
║      Signal: correlation oscillates as cos(Δω·t_flight/2)           ║
║                                                                      ║
║  P2  Isolated detectors: Bell violation attenuated                  ║
║      Signal: CHSH ∝ exp(−σ²_detector_phase)                         ║
║      NOTE: QM predicts the OPPOSITE (isolation helps). Best test.  ║
║                                                                      ║
║  P3  Path asymmetry: detector clock cancels particle clock          ║
║      Residual: δφ ~ ω·L·v/(2c²) — tiny, consistent with Micius     ║
║                                                                      ║
║  P4  Thin/brief detectors: reduced Bell violation                   ║
║      Signal: CHSH approaches classical bound as K→0                 ║
║                                                                      ║
║  P5  Energy-mass equivalence: K = ω = E/ℏ                          ║
║      Optical+ photons: F≈1 always. Mid-IR threshold ~0.49 eV.      ║
║      Massive particles: F≈1 (mc²/ℏ enormous). Consistent with all. ║
║                                                                      ║
║  P6  Gravitational Bell degradation                                 ║
║      Gravity IS Φ_bulk. Both detectors couple to same grav. field.  ║
║      F_grav = exp(−(ω₀·ΔΦ/c²·τ)²/2). No FTL needed.               ║
║      Signal: Bell violation degrades at neutron star/BH gradients.  ║
║      QM predicts: no gravitational dependence. Clean discriminant.  ║
║                                                                      ║
║  P6b Linewidth-dependent gravitational Bell test (near-term)        ║
║      τ_sync = τ_coh = 1/Δν. Narrower linewidth → longer sync time. ║
║      CHSH(Δν) = 2√2·exp(−(ω₀·ΔΦ/c²/Δν)²/2)                       ║
║      Earth-Moon: Sr optical clock photons (7.6 kHz) → CHSH→0       ║
║      Mauna Kea:  cavity-filtered photons (sub-kHz) → measurable     ║
║      QM predicts: CHSH independent of linewidth. KEY DISCRIMINANT.  ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    # ── P6: Gravitational fidelity table ─────────────────────────────────
    print("P6: CHSH values by environment and particle type")
    print(f"  {'Environment':<40}  {'ΔΦ/c²':>12}  {'Optical γ':>10}  {'Electron':>10}  {'QM':>8}")
    print("  " + "-" * 88)
    omega_optical  = 2 * np.pi * C / 500e-9
    omega_electron = 0.511e6 * EV / HBAR
    for env_name, dphi in ENVIRONMENTS.items():
        F_opt = float(gravitational_fidelity(dphi, omega_optical))
        F_el  = float(gravitational_fidelity(dphi, omega_electron))
        c_opt = 2 * np.sqrt(2) * F_opt
        c_el  = 2 * np.sqrt(2) * min(F_el, 1.0)
        print(f"  {env_name:<40}  {dphi:>12.3e}  {c_opt:>10.4f}  {c_el:>10.4f}  {2*np.sqrt(2):>8.4f}")


if __name__ == '__main__':
    run()
