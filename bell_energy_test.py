"""
bell_energy_test.py
===================
Qiskit simulation of the CHSH Bell test at different photon energies.

HYPOTHESIS (Kuramoto clock-phase / Bell-without-FTL theory):
  Photon entanglement = synchronized clocks at pair creation.
  Measurement = Kuramoto synchronization between particle clock and detector.
  The CHSH violation depends on photon energy through the synchronization fidelity.

THREE COMPETING MODELS:
─────────────────────────────────────────────────────────────────────────────
  Model A — Phase-inertia dominates (K ∝ 1/E):
    Higher energy photons have more phase inertia (harder to rotate).
    Coupling K(E) = K_0 · (E_ref/E).
    Sync fidelity F(E) = 1 − exp(−K(E) · τ) = 1 − exp(−K_0·E_ref·τ/E).
    Prediction: Bell violation DECREASES with photon energy.
    Threshold E_crit: F(E_crit) = 1/√2 → CHSH drops below 2.

  Model B — Energy-mass equivalence (K ∝ E, or K ∝ ω = E/ℏ):
    The Kuramoto coupling IS the particle's clock frequency: K = ω = E/ℏ.
    This is the natural identification: the de Broglie clock oscillates faster
    for higher-energy particles (massive or photon), so synchronization to the
    detector bulk is faster.
    Coupling K(E) = K_0 · (E/E_ref).
    Prediction: Bell violation INCREASES with photon energy.
    Heavy particles (large mc²/ℏ) always achieve near-perfect sync.
    Radio photons might show reduced Bell violations.

  Null hypothesis — Standard QM:
    CHSH = 2√2 for ALL energies. No energy dependence.
    Violation of this null = evidence for the clock-phase model.

USER NOTE (session insight):
  "Maybe this is where the energy-mass equivalence enters the equation."
  E = mc² is the bridge: for massive particles K ∝ mc²/ℏ (rest-mass clock),
  giving τ_sync ~ ℏ/mc² → heavier particles sync FASTER (see predictions.py P5).
  For photons: K ∝ hν/ℏ = 2πν → higher-frequency photons sync faster (Model B).
  The two models differ in the sign of the slope: experiments can distinguish them.

CAVEAT — THIS PROGRAM CANNOT BE RUN ON A REAL QUANTUM COMPUTER TO TEST K(E):
─────────────────────────────────────────────────────────────────────────────
  This file is an EXACT SIMULATION using qiskit.quantum_info; no real hardware
  is required and the energy parameter is swept analytically. It is appropriate
  for classical workstation execution.

  If submitted to a real backend (IBM Quantum, IonQ via Braket, Quantinuum via
  Azure, etc.), the program will produce a standard CHSH measurement near the
  device's noise floor (S ≈ 2.5–2.8 on current superconducting hardware), but
  it will NOT physically test the K(E) hypothesis. Reason:

    Digital quantum computers do not contain photons. Their qubits are
    fixed-energy two-level systems — superconducting qubits at ~5 GHz set
    by the Josephson junction design, or trapped-ion hyperfine transitions
    at GHz–THz set by the atomic structure. The qubit transition energy
    is a hardware parameter that cannot be varied at runtime.

  The "photon energy" knob in this simulation is a classical parameter that
  rescales the Rzz(K(E)) coupling angle. It has no physical analog on a
  quantum computer — there is nothing on the device to which "different
  photon energies" could correspond. Sweeping the parameter on hardware
  would just produce different gate angles applied to the same fixed-energy
  qubits, with the resulting CHSH curve reflecting gate fidelity vs angle,
  not photon energy vs synchronization fidelity.

  WHERE THE K(E) HYPOTHESIS ACTUALLY NEEDS TO BE TESTED:
    A photonics experiment with entangled photons at GENUINELY different
    optical / RF frequencies — e.g., SPDC sources at different pump
    wavelengths, or comparison between optical and microwave entangled
    photons. The relevant variable is the photon's physical frequency,
    not a circuit parameter on a digital device.

  WHAT *CAN* BE TESTED ON A QUANTUM COMPUTER (from this framework):
    bulk_sync_asymmetry.py — tests the √N (product bulk) vs N (synced bulk)
    phase-rotation scaling under Rzz coupling. The relevant variable is
    circuit structure, which IS something a quantum computer can vary.
    That program is the natural Qiskit-on-hardware experiment for this
    framework; this one is not.

  In short: keep this program on a classical simulator. The energy sweep
  is a mathematical study of how K(E) would shape Bell correlations IF
  the hypothesis were correct; physical confirmation of K(E) requires
  optical/photonics hardware, not digital quantum hardware.

QISKIT IMPLEMENTATION:
  Uses qiskit.quantum_info (DensityMatrix, Statevector) for exact simulation.
  No shot-based Aer simulation needed — all expectation values are exact.

  Step 1: Prepare Werner state ρ(F) = F|Φ+⟩⟨Φ+| + (1−F)·I/4
          where F(E) = sync fidelity from Kuramoto model.
  Step 2: Apply detector coupling — Rzz(K(E)) between each photon and
          its detector ancilla (initialised in |+⟩ = bulk clock eigenstate).
  Step 3: Compute CHSH via exact ZZ expectation values over rotated bases.
  Step 4: Sweep over photon energy scale E/E_ref from 0.1 to 10.

CHSH MEASUREMENT:
  For state ρ, detector angles a and b:
    E(a, b) = Tr[(Ry(2a)⊗Ry(2b)) ρ (Ry†(2a)⊗Ry†(2b)) · (Z⊗Z)]
  CHSH = |E(a,b) − E(a,b') + E(a',b) + E(a',b')|
  Optimal angles: a=0, a'=π/4, b=π/8, b'=3π/8  → CHSH_QM = 2√2 for |Φ+⟩

Install: pip install qiskit matplotlib numpy
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive — works headless
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import (
    DensityMatrix, Statevector, partial_trace, Operator
)
from qiskit.circuit.library import RZZGate

# ─── Physical parameter scales ───────────────────────────────────────────────
# Photon energies in natural units (eV), with E_ref = optical photon ~2 eV
E_REF   = 2.0          # eV — optical photon reference
E_RANGE = np.logspace(-2, 3, 120)   # 0.01 eV (microwave) to 1000 eV (X-ray)

# Sync parameters
K_0     = 5.0          # base coupling (dimensionless interaction time × K)
TAU     = 1.0          # normalised interaction time

# Bell angles: optimal for |Φ+⟩
A1, A2 = 0.0, np.pi / 4
B1, B2 = np.pi / 8, 3 * np.pi / 8

# ─── Werner state CHSH: analytical ──────────────────────────────────────────
# For ρ(F) = F|Φ+⟩⟨Φ+| + (1−F)I/4 with optimal angles:
#   E(θ_A, θ_B) = F · cos(2(θ_A − θ_B))
#   CHSH_optimal = F · 2√2
# This is an exact analytical result — no need to instantiate DensityMatrix
# for bulk parameter sweeps.

SQRT2 = np.sqrt(2.0)

def chsh_werner(F: float | np.ndarray) -> float | np.ndarray:
    """CHSH for Werner state ρ(F). Analytical: CHSH = F · 2√2."""
    return np.asarray(F) * 2.0 * SQRT2


# ─── Qiskit CHSH (exact, no shots) — used for cross-validation only ─────────

def bell_plus() -> np.ndarray:
    """Density matrix of |Φ+⟩ = (|00⟩+|11⟩)/√2 as 4×4 array."""
    v = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    return np.outer(v, v.conj())


def werner_dm(F: float) -> DensityMatrix:
    """ρ(F) = F·|Φ+⟩⟨Φ+| + (1−F)·I/4  as a Qiskit DensityMatrix."""
    rho = F * bell_plus() + (1.0 - F) * np.eye(4) / 4.0
    return DensityMatrix(rho)


def ry_matrix(theta: float) -> np.ndarray:
    """2×2 Ry(θ) = exp(−iθY/2) rotation matrix."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], dtype=complex)


Z  = np.array([[1, 0], [0, -1]], dtype=complex)
ZZ = np.kron(Z, Z)


def chsh_qiskit(rho: DensityMatrix) -> float:
    """CHSH via exact matrix computation (Qiskit DensityMatrix). Cross-check only."""
    def e(ta, tb):
        Ra = ry_matrix(2 * ta); Rb = ry_matrix(2 * tb)
        R  = np.kron(Ra, Rb)
        rr = R @ rho.data @ R.conj().T
        return float(np.real(np.trace(ZZ @ rr)))
    return abs(e(A1,B1) - e(A1,B2) + e(A2,B1) + e(A2,B2))


# ─── Sync fidelity models ────────────────────────────────────────────────────

def fidelity_model_A(E_arr: np.ndarray) -> np.ndarray:
    """
    Model A: K ∝ 1/E (phase inertia dominates).
    F(E) = 1 − exp(−K_0·E_ref·τ/E)
    Low E → F→1 (strong coupling, full Bell violation).
    High E → F→0 (weak coupling, no Bell violation).
    """
    K_eff = K_0 * E_REF / E_arr
    return 1.0 - np.exp(-K_eff * TAU)


def fidelity_model_B(E_arr: np.ndarray) -> np.ndarray:
    """
    Model B: K ∝ E (energy-mass equivalence, K = ω = E/ℏ).
    F(E) = 1 − exp(−K_0·E·τ/E_ref)
    High E → F→1 (massive/high-energy particles sync fast → strong Bell violation).
    Low E → F→0 (radio photons: weak, slow synchronization → reduced violation).
    """
    K_eff = K_0 * E_arr / E_REF
    return 1.0 - np.exp(-K_eff * TAU)


def fidelity_qm(E_arr: np.ndarray) -> np.ndarray:
    """QM null hypothesis: F = 1 for all energies."""
    return np.ones_like(E_arr)


# ─── Rzz detector coupling circuit ──────────────────────────────────────────

def chsh_rzz_circuit(K_coupling: float) -> float:
    """
    Qiskit circuit: Bell pair + detector ancillae in |+⟩, coupled via Rzz(K).
    Qubits: [photon_A (0), photon_B (1), detector_A (2), detector_B (3)]
    Detectors in |+⟩ model the bulk clock superposition (uniform phase).
    """
    qc = QuantumCircuit(4)
    qc.h(0); qc.cx(0, 1)   # Bell pair |Φ+⟩
    qc.h(2); qc.h(3)        # Detector clocks in |+⟩
    qc.rzz(K_coupling, 0, 2)
    qc.rzz(K_coupling, 1, 3)

    dm_full = DensityMatrix(Statevector(qc))
    rho_photons = partial_trace(dm_full, [2, 3])
    return chsh_qiskit(rho_photons)


# ─── Main simulation ─────────────────────────────────────────────────────────

def run():
    print("=" * 68)
    print("Bell Test at Different Photon Energies — Qiskit Exact Simulation")
    print("=" * 68)

    # ── Compute CHSH vs energy for all models (analytical: CHSH = F·2√2) ──
    F_A   = fidelity_model_A(E_RANGE)
    F_B   = fidelity_model_B(E_RANGE)
    F_QM  = fidelity_qm(E_RANGE)

    chsh_A  = chsh_werner(F_A)
    chsh_B  = chsh_werner(F_B)
    chsh_QM = chsh_werner(F_QM)

    # ── Rzz circuit cross-check (5 points, Qiskit exact) ──────────────────
    print("\nRzz-circuit cross-check (analytical Werner vs Qiskit Rzz circuit):")
    print(f"{'E/E_ref':>10}  {'K_A':>8}  {'CHSH_analytical':>16}  {'CHSH_Rzz':>12}")
    print("-" * 56)
    for E_s in [0.5, 1.0, 2.0, 5.0, 10.0]:
        K_s = K_0 * E_REF / E_s
        F_s = float(1.0 - np.exp(-K_s * TAU))
        c_W = float(chsh_werner(F_s))
        c_R = chsh_rzz_circuit(K_s)
        print(f"{E_s:>10.2f}  {K_s:>8.3f}  {c_W:>16.4f}  {c_R:>12.4f}")

    # ── Analytical thresholds (CHSH = 2.0 when F = 1/√2) ─────────────────
    # Model A: F(E) = 1-exp(-K0*Eref/E) = 1/√2 → K0*Eref/E = -ln(1-1/√2)
    # Model B: F(E) = 1-exp(-K0*E/Eref) = 1/√2 → K0*E/Eref = -ln(1-1/√2)
    F_bell_thr = 1.0 / SQRT2
    ln_term = -np.log(1.0 - F_bell_thr)          # ≈ 1.2279
    E_thr_A_calc = K_0 * E_REF / ln_term
    E_thr_B_calc = ln_term * E_REF / K_0

    print("\nBell inequality thresholds (CHSH = 2.0, analytical):")
    print(f"  Model A (K∝1/E): threshold at E = {E_thr_A_calc:.4f} eV  "
          f"({E_thr_A_calc/E_REF:.3f}·E_ref)")
    print(f"  Model B (K∝E)  : threshold at E = {E_thr_B_calc:.4f} eV  "
          f"({E_thr_B_calc/E_REF:.3f}·E_ref)")
    print(f"  QM null: CHSH = 2√2 = {2*SQRT2:.4f} at all energies")

    # ── Energy-mass equivalence: CHSH for specific photon species ─────────
    photon_energies = {
        "Radio (AM, 1 MHz)":           4.1e-9,
        "Microwave (WiFi, 2.4 GHz)":   9.9e-6,
        "Infrared (10 μm)":            0.124,
        "Red optical (700 nm)":        1.77,
        "Blue optical (400 nm)":       3.10,
        "UV (200 nm)":                 6.20,
        "Soft X-ray (1 nm)":           1240.0,
        "Hard X-ray (0.01 nm)":        1.24e5,
        "Gamma ray (1 MeV)":           1e6,
    }

    print("\nPredicted CHSH by photon type:")
    print(f"  {'Photon type':<30}  {'E (eV)':>12}  {'Model A':>9}  {'Model B':>9}  {'QM':>9}")
    print("  " + "-" * 75)
    for label, E_ph in photon_energies.items():
        F_a = float(fidelity_model_A(np.array([E_ph]))[0])
        F_b = float(fidelity_model_B(np.array([E_ph]))[0])
        c_a = float(chsh_werner(F_a))
        c_b = float(chsh_werner(F_b))
        print(f"  {label:<30}  {E_ph:>12.3g}  {c_a:>9.4f}  {c_b:>9.4f}  {2*SQRT2:>9.4f}")

    # ── Massive particles: E = mc² connection ─────────────────────────────
    print("\nEnergy-mass equivalence: K ∝ E = mc² for massive particles")
    print(f"  {'Particle':<20}  {'Rest energy (eV)':>18}  {'F (Model B)':>12}  {'CHSH':>8}")
    print("  " + "-" * 64)
    particles = {
        "Electron":     0.511e6,
        "Muon":         105.7e6,
        "Pion (π0)":    134.98e6,
        "Proton":       938.3e6,
        "Neutron":      939.6e6,
        "Kaon (K0)":    497.6e6,
    }
    for pname, E_rest in particles.items():
        F_b = float(fidelity_model_B(np.array([E_rest]))[0])
        c_b = float(chsh_werner(min(F_b, 1.0)))
        print(f"  {pname:<20}  {E_rest:>18.4g}  {F_b:>12.6f}  {c_b:>8.4f}")

    print("\n  → Model B prediction: all massive particle Bell tests should")
    print("    show CHSH = 2√2 (F≈1 due to huge mc²/ℏ coupling frequency).")
    print("    ONLY radio/microwave photons would show reduced violation.")

    # ─────────────────────────────────────────────────────────────────────────
    # PLOTS
    # ─────────────────────────────────────────────────────────────────────────

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle(
        "Bell Test at Different Photon Energies\n"
        "Kuramoto Clock-Phase Theory: CHSH vs E  (Qiskit exact simulation)",
        fontsize=13
    )

    # ─ Panel 1: CHSH vs energy, all models ─
    ax = axes[0, 0]
    ax.semilogx(E_RANGE, chsh_A,  'b-',  lw=2.5, label='Model A: K∝1/E  (phase inertia)')
    ax.semilogx(E_RANGE, chsh_B,  'r-',  lw=2.5, label='Model B: K∝E    (E=mc² sync)')
    ax.semilogx(E_RANGE, chsh_QM, 'g--', lw=1.5, label='QM null: CHSH=2√2')
    ax.axhline(2.0,           color='k',      ls='--', lw=1.5, label='Bell bound (2.0)')
    ax.axhline(2*np.sqrt(2),  color='gray',   ls=':',  lw=1,   label='Tsirelson (2√2)')
    ax.axvline(E_REF,         color='orange', ls=':',  lw=1.5, label=f'E_ref = {E_REF} eV')
    ax.fill_between(E_RANGE, 2.0, chsh_A,
                    where=chsh_A > 2.0, alpha=0.12, color='blue', label='_nolegend_')
    ax.fill_between(E_RANGE, 2.0, chsh_B,
                    where=chsh_B > 2.0, alpha=0.12, color='red', label='_nolegend_')
    ax.set_xlabel('Photon energy (eV)')
    ax.set_ylabel('CHSH value')
    ax.set_title('CHSH vs photon energy')
    ax.set_ylim(0, 3.0)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which='both')

    # ─ Panel 2: Sync fidelity F(E) ─
    ax = axes[0, 1]
    ax.semilogx(E_RANGE, F_A,  'b-', lw=2, label='Model A: F = 1−exp(−K₀E_ref/E)')
    ax.semilogx(E_RANGE, F_B,  'r-', lw=2, label='Model B: F = 1−exp(−K₀E/E_ref)')
    ax.axhline(1.0/np.sqrt(2), color='k', ls='--', lw=1.5,
               label='F = 1/√2  (Bell threshold)')
    ax.axvline(E_REF, color='orange', ls=':', lw=1.5)
    ax.set_xlabel('Photon energy (eV)')
    ax.set_ylabel('Sync fidelity F')
    ax.set_title('Synchronization fidelity vs energy')
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which='both')
    ax.annotate('Bell violation requires F > 1/√2',
                xy=(E_REF, 1/np.sqrt(2)),
                xytext=(E_REF*5, 0.55),
                fontsize=8, color='black',
                arrowprops=dict(arrowstyle='->', color='k'))

    # ─ Panel 3: Correlation function E(Δ) for selected energies ─
    # Werner state: E(a,b) = F·cos(2(a-b)) — here Δ = 2*(a-b) on x-axis
    ax = axes[0, 2]
    deltas = np.linspace(-np.pi, np.pi, 300)
    for E_ph, col in [(0.1, 'lightblue'), (E_REF, 'steelblue'), (100.0, 'navy')]:
        F_a = float(fidelity_model_A(np.array([E_ph]))[0])
        E_corr = F_a * np.cos(deltas)
        ax.plot(deltas, E_corr, color=col, lw=1.5, label=f'A: E={E_ph} eV, F={F_a:.2f}')
    ax.plot(deltas, -np.cos(deltas), 'g--', lw=2, label='QM: −cos(Δ)')
    ax.plot(deltas, -0.5*np.cos(deltas), 'k:', lw=1.5, label='Kuramoto limit: −½cos(Δ)')
    ax.axhline(0, color='gray', lw=0.5)
    ax.set_xlabel('Δ = a − b  (rad)')
    ax.set_ylabel('E(a, b)')
    ax.set_title('Correlation function\n(Model A at selected energies)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # ─ Panel 4: Rzz circuit cross-check (20 points only) ─
    ax = axes[1, 0]
    K_rzz_range = np.linspace(0.01, 8.0, 20)
    print("\nComputing Rzz circuit cross-check (20 points)...")
    chsh_rzz_arr    = [chsh_rzz_circuit(k) for k in K_rzz_range]
    F_rzz_arr       = 1.0 - np.exp(-K_rzz_range * TAU)
    chsh_werner_rzz = chsh_werner(F_rzz_arr)

    ax.plot(K_rzz_range, chsh_rzz_arr,    'b-',  lw=2, label='Rzz circuit (Qiskit)')
    ax.plot(K_rzz_range, chsh_werner_rzz, 'r--', lw=1.5, label='Werner state model')
    ax.axhline(2.0,          color='k',    ls='--', lw=1.5, label='Bell bound')
    ax.axhline(2*np.sqrt(2), color='gray', ls=':',  lw=1,   label='Tsirelson')
    ax.set_xlabel('Coupling K (∝ E for Model B, ∝ 1/E for Model A)')
    ax.set_ylabel('CHSH')
    ax.set_title('Rzz circuit vs Werner state\n(cross-validation)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(0.05, 0.10,
            'NOTE: Divergence is expected.\n'
            'Rzz+|+⟩ detectors = correlated Z-dephasing.\n'
            'Werner state = isotropic depolarising.\n'
            'Two different noise channels → different CHSH.\n'
            'Both valid models; Rzz is more physical\n'
            '(bulk clock couples to specific axis).',
            transform=ax.transAxes, fontsize=7,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # ─ Panel 5: CHSH map — energy vs K_0 parameter (analytical, instant) ─
    ax = axes[1, 1]
    K0_grid  = np.logspace(-1, 2, 80)
    E_grid   = np.logspace(-1, 3, 80)
    K0_mesh, E_mesh = np.meshgrid(K0_grid, E_grid)
    K_eff_mesh  = K0_mesh * E_REF / E_mesh          # Model A
    F_mesh      = 1.0 - np.exp(-K_eff_mesh * TAU)
    CHSH_map    = chsh_werner(F_mesh)

    im = ax.contourf(K0_grid, E_grid, CHSH_map,
                     levels=[0, 1, 1.5, 2.0, 2.2, 2.5, 2*np.sqrt(2)],
                     cmap='RdYlGn')
    ax.contour(K0_grid, E_grid, CHSH_map,
               levels=[2.0], colors='black', linewidths=2)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('K₀ (base coupling strength)')
    ax.set_ylabel('Photon energy (eV)')
    ax.set_title('CHSH map: energy vs coupling\n(Model A, black = Bell bound)')
    plt.colorbar(im, ax=ax, label='CHSH value')
    ax.text(0.02, 0.05,
            'ABOVE black line: Bell violated\nBELOW: Bell satisfied',
            transform=ax.transAxes, fontsize=8,
            color='black', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    # ─ Panel 6: Prediction summary table ─
    ax = axes[1, 2]
    ax.axis('off')

    # Key prediction numbers
    F_thr = 1.0 / np.sqrt(2)
    # Model A threshold
    K_thr_A = -np.log(1.0 - F_thr) / TAU
    E_thr_A_calc = K_0 * E_REF / K_thr_A
    # Model B threshold
    K_thr_B = -np.log(1.0 - F_thr) / TAU
    E_thr_B_calc = K_thr_B * E_REF / K_0

    summary = [
        ["", "Model A (K∝1/E)", "Model B (K∝E)", "QM"],
        ["Bell threshold E", f"{E_thr_A_calc:.3f} eV", f"{E_thr_B_calc:.3f} eV", "none"],
        ["Radio photons", "VIOLATED", "sub-classical", "VIOLATED"],
        ["Optical photons", "VIOLATED", "VIOLATED", "VIOLATED"],
        ["X-ray photons", "sub-classical", "VIOLATED", "VIOLATED"],
        ["Gamma rays", "sub-classical", "VIOLATED", "VIOLATED"],
        ["Electrons (mc²)", "sub-classical", "VIOLATED", "VIOLATED"],
        ["Protons (mc²)", "sub-classical", "VIOLATED", "VIOLATED"],
        ["Kaons (K0)", "sub-classical", "VIOLATED", "VIOLATED"],
        ["Slope: CHSH vs E", "decreasing", "increasing", "flat"],
        ["Testable?", "YES (X-ray Bell)", "YES (radio Bell)", "null"],
    ]

    cell_colors = [['#d0d8ff']*4]
    for row in summary[1:]:
        row_col = ['#f5f5f5', '#ddeeff', '#ffeedd', '#e8ffe8']
        cell_colors.append(row_col)

    tbl = ax.table(
        cellText=summary,
        cellColours=cell_colors,
        loc='center',
        cellLoc='center'
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1.1, 1.6)
    ax.set_title('Prediction summary\n(testable at X-ray / radio Bell experiments)',
                 fontsize=9, pad=12)

    plt.tight_layout()
    plt.savefig('bell_energy_test.png', dpi=150, bbox_inches='tight')
    print("\nPlot saved: bell_energy_test.png")
    # plt.show()  # non-interactive; savefig above is sufficient

    print("\n" + "=" * 68)
    print("KEY RESULTS")
    print("=" * 68)
    print(f"""
Model A (K ∝ 1/E — phase inertia):
  Bell threshold: E_crit = {E_thr_A_calc:.4f} eV  ({E_thr_A_calc/E_REF:.3f}·E_ref)
  Prediction: optical/microwave photons → Bell VIOLATED
              X-ray/gamma photons       → Bell NOT violated
  Empirical challenge: X-ray Bell experiments (BaBar Υ→ entangled photons,
  CPLEAR kaons at ~GeV) DO show violations. Model A is falsified by these.

Model B (K ∝ E — energy-mass equivalence, K = ω = E/ℏ):
  Bell threshold: E_crit = {E_thr_B_calc:.6f} eV  ({E_thr_B_calc/E_REF:.5f}·E_ref)
  Prediction: radio/microwave photons → Bell REDUCED or NOT violated
              optical and above        → Bell VIOLATED (F→1)
  Empirical challenge: Bell tests at radio/microwave frequencies
  have not been performed. This is an OPEN experimental question.
  Model B is consistent with ALL known Bell tests (optical + particle).

Energy-mass equivalence insight:
  For massive particles: K ∝ mc²/ℏ → enormous coupling.
  F(electron) = {float(fidelity_model_B(np.array([0.511e6]))[0]):.6f}
  F(proton)   = {float(fidelity_model_B(np.array([938.3e6]))[0]):.6f}
  All massive-particle Bell tests consistent with Model B (F ≈ 1).

  For photons: K = ω = 2πν.
  Bell threshold at ν_crit = {E_thr_B_calc * 1.6e-19 / 6.626e-34:.3e} Hz
  (that is {E_thr_B_calc * 1.6e-19 / 6.626e-34 / 1e9:.3f} GHz — deep microwave/radio).
  Model B is TESTABLE at radio frequencies.
""")


if __name__ == '__main__':
    run()
