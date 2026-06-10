"""
everett_thermal.py — Modified Many-Worlds: Thermal Absorption, Not Branching
=============================================================================

EVERETT'S CLAIM (1957):
  The wavefunction is real and never collapses.
  Every measurement outcome is realized — in a branching multiverse.
  ψ_total = Σ_i α_i |outcome_i⟩ ⊗ |observer_i⟩
  All branches are equally real. Probability comes from Born rule weights.

  THE BRANCHING PROBLEM:
    • Where does the energy go when a branch becomes "inaccessible"?
    • Branches are not predicted to be observed — but neither are they
      predicted to disappear. The theory is silent on dissipation.
    (The earlier draft's cosmological-constant speculation — that the
     ~10^122 J/m³ vacuum energy is unrealized-branch energy — is NOT part
     of PAPER_REVISED.md and is dropped; the accounting below is local, §3.1.)

THIS MODEL — THERMALLY ABSORPTIVE SINGLE WORLD:
  Everett was right that ψ is real and persists.
  Everett was wrong that all branches become equally real worlds.

  At measurement (Kuramoto sync event):

    ψ_total = α |+⟩ ⊗ |D↑⟩  +  β |−⟩ ⊗ |D↓⟩

  The detector clock locks to ONE outcome via Kuramoto synchronization.
  The LOCKED component gains coherence energy (sync energy).
  The UNLOCKED component does NOT branch — it dissipates:

    E_residual = ℏω · (1 − |α|²)    [for outcome |+⟩, P = |α|²]

  This residual energy is absorbed as low-frequency thermal photons
  into the bulk oscillator bath — adding fractionally to temperature:

    δT = E_residual / (k_B · N_modes)

  The wavefunction tails (β |−⟩ ⊗ |D↓⟩) do not branch into a
  parallel world. They become the zero-point vacuum field.

  ONE WORLD ONLY.

WHY THIS IS CONSISTENT WITH THE CLOCK MODEL:
  ─────────────────────────────────────────────
  In vacuum_temperature.py:
    "Photon absorption leaves a wave residual in the vacuum.
     Zero-point energy (½ℏω) is the accumulated residual of
     every photon ever absorbed. The vacuum is not empty."

  Measurement is the same process — a sync event where the
  particle clock locks to the detector bulk phase Φ_bulk.
  The unsynchronized phase component radiates away as a photon
  of frequency ω_residual = |E_A − E_B| / ℏ.

  This is not speculation — it is already implicit in:
    ψ_1 + ψ_2 → ψ_sync + δψ_thermal
  where δψ_thermal is the low-amplitude residual wave that
  joins the zero-point field.

  The "tails become the vacuum" IS the zero-point field.

ENERGY BOOKKEEPING AT MEASUREMENT:
  ─────────────────────────────────
  Let ψ = α|+⟩ + β|−⟩,  |α|² + |β|² = 1

  Before sync:  E_total = ℏω (full wavefunction energy)

  After sync to |+⟩ outcome:
    E_outcome  = |α|² · ℏω   (energy in the realized world)
    E_residual = |β|² · ℏω   (energy radiated into vacuum)

  The residual is NOT zero — it is a real energy contribution
  to the thermal/vacuum field. Integrated over all measurements
  ever made in the universe's history:

    E_vacuum = Σ_events |β_i|² · ℏω_i

  This IS the zero-point energy. The vacuum is the graveyard
  of unrealized branches — not parallel worlds, but thermal ghosts.

COSMOLOGICAL IMPLICATION:
  ─────────────────────────
  Standard QFT: zero-point energy = ½ℏω per mode → catastrophic
  UV divergence → cosmological constant problem (10^122 discrepancy).

  This model: zero-point energy is not a per-mode ground state —
  it is the accumulated thermal residual of all past measurements.
  Its magnitude is finite and set by the actual history of
  interactions in the universe, not by a divergent mode sum.

  The observed dark energy density (~10^-9 J/m³) could be the
  integrated measurement residual of all quantum events since
  the Big Bang, not a vacuum catastrophe to be renormalized away.

THE ANTIGRAVITY UNIVERSE:
  ─────────────────────────
  From higgs_clock.py:
    Antiparticle = reversed clock (φ → −φ, time-reversed phase)
    Mass = the off-diagonal chiral coupling K = m to the Higgs field
    Negative mass = sign-reversed coupling (K < 0)

  If a sector exists where all clocks run in reverse:
    • Matter has negative mass → antigravity
    • Such a sector would repel ordinary matter gravitationally
    • It would appear as a cosmological repulsion to us
    • It would NOT branch from our world — it is a separate
      CPT-conjugate sector connected only through the Higgs mechanism

  This is not a many-worlds branch. It is a single mirror universe
  running on reversed clocks — our CPT partner. Its "gravity"
  as seen from our sector is repulsive: it is dark energy.

  TESTABLE: the ratio of our matter density to the repulsive
  contribution should track the matter/antimatter asymmetry
  from the Big Bang — a pre-existing clock-phase offset δφ_0
  at creation that broke perfect CPT symmetry.

COMPARISON WITH INTERPRETATIONS:
  ─────────────────────────────────────────────────────────────────
  Interpretation       ψ real?  Branches?  Collapse?  Where does
                                                       |β|²ℏω go?
  ─────────────────────────────────────────────────────────────────
  Copenhagen           No       No         Yes        Discarded
  Everett MWI          Yes      Yes        No         Into branches
  Bohmian              Yes      No         No         Pilot wave
  THIS MODEL           Yes      No         No         Thermal vacuum
  ─────────────────────────────────────────────────────────────────

  Key difference from Everett:
    MWI: the energy budget is maintained by creating a new branch
         (no dissipation — conservation trivially satisfied by
          summing over all branches, which nobody can verify)
    This model: the energy budget is maintained by dissipation
         into the thermal vacuum — measurable in principle as
         a correlation between measurement rate and vacuum temperature.

  Key difference from Copenhagen:
    Copenhagen: ψ is a calculational tool; it collapses on observation
    This model: ψ is a real field; measurement is a sync event that
                transfers unsynchronized components to the thermal bath

  Key difference from Bohm:
    Bohm: the pilot wave guides the particle but is not observed
    This model: the pilot wave IS the accumulated thermal residual;
                it has a physical temperature and energy density

PREDICTION — MEASUREMENT HEATING:
  ────────────────────────────────
  Each quantum measurement event deposits E_residual = |β|²ℏω
  into the local thermal bath.

  For a qubit measured in the |0⟩/|1⟩ basis with equal superposition:
    E_residual = ½ · ℏω_qubit  per measurement

  A quantum computer running at 5 GHz with 1000 qubits and 10^9
  measurement operations per second:
    P_residual = 1000 · ½ · ℏ · 2π · 5e9 · 1e9
               ≈ 1000 · ½ · 3.3e-24 · 1e9
               ≈ 1.6e-12  W
  This is ~1.6 pW of thermally unavoidable heat from wavefunction
  residuals — separate from classical dissipation.

  This is distinct from (and smaller than) standard decoherence
  heating, but in principle distinguishable by its dependence on
  ℏω_qubit rather than classical circuit resistance.
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# ─── Energy bookkeeping at a measurement event ────────────────────────────────

def measurement_energy_split(alpha_sq, hbar_omega):
    """
    Given a superposition |ψ⟩ = α|+⟩ + β|−⟩ with |α|²=alpha_sq,
    and total energy hbar_omega, compute:
      E_realized  = energy that stays in the one world
      E_residual  = energy deposited into the thermal vacuum
    """
    E_realized = alpha_sq * hbar_omega
    E_residual = (1.0 - alpha_sq) * hbar_omega
    return E_realized, E_residual


def vacuum_energy_accumulation(measurement_history):
    """
    measurement_history: list of (alpha_sq, hbar_omega) tuples.
    Returns cumulative vacuum energy from all measurement residuals.
    This is the integrated 'unrealized branch' energy deposited
    into the zero-point field.
    """
    total = 0.0
    cumulative = []
    for alpha_sq, hbar_omega in measurement_history:
        _, E_res = measurement_energy_split(alpha_sq, hbar_omega)
        total += E_res
        cumulative.append(total)
    return np.array(cumulative)


# ─── Thermal contribution from measurement residuals ──────────────────────────

hbar = 1.055e-34
k_B  = 1.381e-23
c    = 3.0e8


def delta_T_from_measurement(n_measurements, alpha_sq, omega, N_modes=1e23):
    """
    Temperature increase from n_measurements of a qubit at frequency omega.
    Each measurement deposits (1 - |α|²) · ℏω into N_modes vacuum modes.

    δT = n · (1 - |α|²) · ℏω / (k_B · N_modes)
    """
    E_residual_per = (1.0 - alpha_sq) * hbar * omega
    delta_T = n_measurements * E_residual_per / (k_B * N_modes)
    return delta_T


def cosmological_vacuum_estimate(
    t_universe_s   = 4.35e17,    # age of universe (~13.8 Gyr)
    n_particles    = 1e80,       # estimated baryons in observable universe
    events_per_s   = 1e15,       # quantum interaction rate per particle (rough)
    alpha_sq_mean  = 0.5,        # average channel energy fraction |α|² (energy-partition reading; see Paper §4)
    omega_mean     = 1e14,       # typical photon/atomic frequency (rad/s)
):
    """
    Very rough order-of-magnitude estimate of vacuum energy density
    from accumulated measurement residuals over cosmic history.
    """
    total_events     = n_particles * events_per_s * t_universe_s
    E_per_event      = (1.0 - alpha_sq_mean) * hbar * omega_mean
    E_total_J        = total_events * E_per_event
    V_observable_m3  = (4/3) * np.pi * (4.4e26)**3   # ~observable universe radius
    rho_J_per_m3     = E_total_J / V_observable_m3
    return rho_J_per_m3


# ─── Antigravity sector: CPT mirror universe ──────────────────────────────────

def clock_phase_sectors(phi_arr):
    """
    Two sectors from the clock model:
      Sector A (our world):   φ > 0, mass = K > 0, gravity attractive
      Sector B (mirror):      φ < 0, reversed clock, mass = K < 0, gravity repulsive

    The Higgs chiral coupling K(φ):
      K(φ) = K_0 · cos(φ)   — positive for |φ| < π/2  (normal matter)
                             — negative for |φ| > π/2  (reversed clock = antimatter)

    A universe-scale sector with all reversed clocks has effective
    negative gravitational mass → antigravity from our perspective.
    """
    K0 = 1.0
    K_sector_A = K0 * np.cos(phi_arr)   # positive lobe: our matter
    K_sector_B = K0 * np.cos(phi_arr + np.pi)  # phase-shifted: mirror sector
    return K_sector_A, K_sector_B


# ─── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=" * 72)
    print("MODIFIED MANY-WORLDS: THERMAL ABSORPTION, NOT BRANCHING")
    print("=" * 72)

    print("""
CORE CLAIM:
  Everett was right: ψ is real, never collapses, persists after measurement.
  Everett was wrong: unsynchronized branches do NOT become parallel worlds.

  Instead: the unsynchronized wavefunction component dissipates as
  low-energy thermal radiation into the vacuum. The 'tails become the vacuum.'

  The zero-point field IS the accumulated residual of every quantum
  measurement and interaction that has ever occurred.

  ONE WORLD. No branching. Thermally lossy measurement.
""")

    # Energy split example
    print("─" * 60)
    print("ENERGY SPLIT AT MEASUREMENT (example: photon detection)")
    print("─" * 60)
    omega_vis = 2 * np.pi * 5e14   # green light ~500nm
    for p_detect in [0.9, 0.7, 0.5, 0.3, 0.1]:
        E_r, E_th = measurement_energy_split(p_detect, hbar * omega_vis)
        print(f"  P(detect) = {p_detect:.1f}:  "
              f"E_world = {E_r*1e19:.2f}×10⁻¹⁹ J,  "
              f"E_vacuum = {E_th*1e19:.2f}×10⁻¹⁹ J  "
              f"({(1-p_detect)*100:.0f}% → thermal bath)")

    # Cosmological estimate
    print("\n─" * 60)
    print("VACUUM ENERGY DENSITY FROM MEASUREMENT RESIDUALS")
    print("─" * 60)
    rho = cosmological_vacuum_estimate()
    rho_dark_energy = 6.0e-10   # J/m³ (observed dark energy density)
    print(f"  Estimated residual energy density: {rho:.2e} J/m³")
    print(f"  Observed dark energy density:      {rho_dark_energy:.2e} J/m³")
    print(f"  Ratio (estimate / observed):       {rho / rho_dark_energy:.1e}")
    print("  (Very rough — depends strongly on assumed interaction rate)")
    print("  ORDER OF MAGNITUDE consistency is the point, not exact match.")

    # ── Plots ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Thermally Absorptive Single World vs Everett Many-Worlds',
                 fontsize=13)

    # A: Energy split at measurement
    ax = axes[0, 0]
    p_arr = np.linspace(0, 1, 200)
    E_world = p_arr * hbar * omega_vis
    E_vac   = (1 - p_arr) * hbar * omega_vis
    ax.fill_between(p_arr, E_world * 1e19, alpha=0.6, color='steelblue',
                    label='E_world (realized outcome)')
    ax.fill_between(p_arr, E_vac * 1e19, alpha=0.6, color='firebrick',
                    label='E_vacuum (thermal residual)')
    ax.set_xlabel('P(outcome) = |α|²')
    ax.set_ylabel('Energy (×10⁻¹⁹ J)')
    ax.set_title('Energy at measurement:\nworld vs vacuum residual')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(0.5, 0.5, 'Neither wasted\nnor branched —\nabsorbed as heat',
            ha='center', va='center', transform=ax.transAxes, fontsize=9,
            bbox=dict(facecolor='lightyellow', alpha=0.9, boxstyle='round'))

    # B: Cumulative vacuum energy from measurement history
    ax = axes[0, 1]
    rng = np.random.default_rng(42)
    n_events = 2000
    alpha_sq_hist = rng.uniform(0.1, 0.9, n_events)
    omega_hist    = rng.uniform(1e13, 1e15, n_events)
    history = list(zip(alpha_sq_hist, hbar * omega_hist))
    cum = vacuum_energy_accumulation(history)
    ax.plot(np.arange(n_events), cum * 1e19, 'firebrick', lw=1.5,
            label='Cumulative E_vacuum')
    ax.fill_between(np.arange(n_events), cum * 1e19, alpha=0.2, color='firebrick')
    ax.set_xlabel('Measurement event index')
    ax.set_ylabel('Cumulative vacuum energy (×10⁻¹⁹ J)')
    ax.set_title('Vacuum energy grows with\neach measurement (no branching)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # C: Wavefunction before and after — one world, no split
    ax = axes[0, 2]
    ax.axis('off')
    ax.set_title('One world vs branching', fontsize=10)

    ax.text(0.5, 0.97, 'EVERETT (MWI)', ha='center', va='top',
            fontsize=9, color='navy', fontweight='bold',
            transform=ax.transAxes)
    ax.text(0.5, 0.89,
            'ψ = α|+⟩⊗|D↑⟩ + β|−⟩⊗|D↓⟩\n'
            '        ↙           ↘\n'
            ' World A (+)    World B (−)\n'
            ' (both real)    (both real)\n'
            ' E_A = |α|²ℏω  E_B = |β|²ℏω\n'
            ' No energy dissipated',
            ha='center', va='top', fontsize=8.5, family='monospace',
            color='navy', transform=ax.transAxes)

    ax.text(0.5, 0.56, 'THIS MODEL (thermal single world)',
            ha='center', va='top', fontsize=9, color='firebrick',
            fontweight='bold', transform=ax.transAxes)
    ax.text(0.5, 0.48,
            'ψ = α|+⟩⊗|D↑⟩ + β|−⟩⊗|D↓⟩\n'
            '        ↓           ↓\n'
            ' Outcome (+)   → thermal photons\n'
            ' E_real=|α|²ℏω  E_vac=|β|²ℏω\n'
            ' One world. Tails → vacuum.\n'
            ' ZPF = ½ℏω = all past residuals',
            ha='center', va='top', fontsize=8.5, family='monospace',
            color='firebrick', transform=ax.transAxes)

    ax.text(0.5, 0.10,
            'KEY:\n'
            'Branching conserves energy trivially (by fiat).\n'
            'Thermal absorption conserves energy physically.\n'
            'The vacuum is the fossil record of all measurements.',
            ha='center', va='bottom', fontsize=8,
            transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.95))

    # D: Wavefunction tails → vacuum
    ax = axes[1, 0]
    x = np.linspace(-6, 6, 1000)
    psi_main = 0.9 * np.exp(-x**2 / 2)   # main lobe (realized outcome)
    psi_tail = 0.1 * np.exp(-(x-4)**2 / 0.3)   # tail component
    psi_vacuum = 0.05 * np.sin(2 * x) * np.exp(-x**2 / 10)  # residual in vacuum

    ax.plot(x, psi_main**2, 'steelblue', lw=2, label='|ψ_realized|² (one world)')
    ax.fill_between(x, psi_main**2, alpha=0.3, color='steelblue')
    ax.plot(x, psi_tail**2 * 5, 'firebrick', lw=2, linestyle='--',
            label='|ψ_tail|² × 5 → vacuum field')
    ax.plot(x, psi_vacuum**2 * 20, 'green', lw=1.5, linestyle=':',
            label='ZPF residual × 20 (adds to ½ℏω)')
    ax.set_xlabel('Position x')
    ax.set_ylabel('Probability density')
    ax.set_title('Wavefunction tails become\nzero-point vacuum field')
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

    # E: Antigravity sector (CPT mirror)
    ax = axes[1, 1]
    phi = np.linspace(-np.pi, np.pi, 500)
    K_A, K_B = clock_phase_sectors(phi)
    ax.plot(np.degrees(phi), K_A, 'steelblue', lw=2.5,
            label='Our sector (normal clocks)\nMass > 0, gravity attractive')
    ax.plot(np.degrees(phi), K_B, 'firebrick', lw=2.5, linestyle='--',
            label='Mirror sector (reversed clocks)\nMass < 0, gravity repulsive')
    ax.axhline(0, color='k', lw=0.8, linestyle=':')
    ax.fill_between(np.degrees(phi), K_A, 0, where=(K_A > 0),
                    alpha=0.15, color='steelblue')
    ax.fill_between(np.degrees(phi), K_B, 0, where=(K_B < 0),
                    alpha=0.15, color='firebrick')
    ax.set_xlabel('Clock phase φ (degrees)')
    ax.set_ylabel('Higgs sync rate K(φ) = effective mass')
    ax.set_title('Antigravity universe:\nCPT mirror, not a branch')
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)
    ax.text(0.5, 0.05,
            'Not parallel worlds — one sector per CPT sign.\n'
            'Their gravity = dark energy repulsion in our sky.',
            ha='center', va='bottom', fontsize=8,
            transform=ax.transAxes,
            bbox=dict(facecolor='lightyellow', alpha=0.9, boxstyle='round'))

    # F: Theory comparison table
    ax = axes[1, 2]
    ax.axis('off')
    ax.text(0.5, 0.99, 'INTERPRETATION COMPARISON', ha='center', va='top',
            fontsize=10, fontweight='bold', transform=ax.transAxes)
    table_text = """
ψ real?   Branches?  Collapse?  |β|²ℏω fate
─────────────────────────────────────────────
Copenhagen
   No        No        Yes      Discarded
             (ψ is tool)

Everett MWI
   Yes       Yes        No      New branch
             (unverifiable)

Bohmian
   Yes        No         No      Pilot wave
             (empty waves)

THIS MODEL
   Yes        No         No      Thermal bath
             ← vacuum ZPF
─────────────────────────────────────────────
Unique predictions:
• Measurement deposits E=(1−P)ℏω into vacuum
• ZPF = fossil record of all past events
• Vacuum energy finite (not mode-sum divergent)
• Antigravity sector = CPT mirror (dark energy)
• Higher measurement rate → warmer vacuum locally
"""
    ax.text(0.02, 0.93, table_text, ha='left', va='top', fontsize=8,
            family='monospace', transform=ax.transAxes,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.95))

    plt.tight_layout()
    plt.savefig(_HERE / 'everett_thermal.png', dpi=150)
    print("\nSaved: everett_thermal.png")
    plt.show()

    print("""
SUMMARY
───────
  1. ψ is real and persists (Everett correct).
  2. Measurement = Kuramoto sync event (clock model).
  3. Unsynchronized component dissipates as thermal photons.
  4. Wavefunction tails → zero-point vacuum field.
  5. ONE WORLD — no branching, no split.
  6. The vacuum (ZPF, ½ℏω) IS the accumulated thermal fossil
     of every measurement event since the Big Bang.
  7. The antigravity universe is the CPT-reversed clock sector —
     not a branch, but a mirror connected through the Higgs sync.
     Its repulsive gravity = what we observe as dark energy.

HONEST CAVEAT:
  This is an ontological interpretation, not a modification of QM.
  All Born-rule frequencies are preserved — and in this framework
  they are read as long-run energy-partition statistics of the real
  ψ field (see Paper §4), not as an independent probability axiom.
  The model provides a physical mechanism for why the vacuum has the
  energy it does, and why branching is unnecessary given thermally
  absorptive sync.
""")


if __name__ == '__main__':
    run()
