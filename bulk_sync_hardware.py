"""
bulk_sync_hardware.py — IBM Quantum demonstration of bulk_sync_asymmetry
[v2: mitigated, 2026-04-29]
============================================================================

Hardware-targeted Qiskit program for execution on IBM Quantum Runtime.
Sweeps N for both product-state and GHZ-state bulks and plots the
√N vs N phase-rotation scaling discriminator.

═════════════════════════════════════════════════════════════════════════════
INTERPRETIVE STATUS — READ THIS BEFORE CLAIMING "VALIDATION":
═════════════════════════════════════════════════════════════════════════════

The √N (product bulk) vs N (GHZ bulk) phase-rotation scaling is a STANDARD
quantum-metrology prediction. It is well-established (Heisenberg scaling for
GHZ states; standard quantum limit for product states) and is NOT specific
to the Many Clocks Interpretation. Both standard QM and MCI predict exactly
the same scaling — MCI does not modify QM's predictions, it reframes them
(see PAPER_UNIFIED.md §1.4).

A successful hardware run therefore confirms:
  ✓ The simulation in bulk_sync_asymmetry.py correctly predicts hardware
  ✓ Digital quantum hardware reproduces standard quantum-metrology scaling
  ✓ MCI's qualitative measurement-asymmetry picture is CONSISTENT with what
    physical quantum systems do

It does NOT confirm:
  ✗ K = m (the chiral mass-as-coupling identification)
  ✗ The measurement-as-resynchronization interpretation per se
  ✗ Any framework-distinctive prediction

This program is a CONSISTENCY CHECK and HARDWARE DEMONSTRATION, not an
experimental validation of MCI's distinctive interpretive content. The
framework's discriminating predictions live in optical/photonics experiments
(linewidth-dependent gravitational Bell, §5.4; K(E) photon energy scaling)
and astrophysical/collider data (kaon vs B-meson decoherence, §6.2 P4),
none of which a digital quantum computer can perform.

═════════════════════════════════════════════════════════════════════════════
WHAT THIS PROGRAM DEMONSTRATES:
═════════════════════════════════════════════════════════════════════════════

  Single qubit (system) coupled to N bulk qubits via Rzz(K).
    Product bulk:  ⟨X_system⟩ = cos^N(K),  φ_sys ≈ √N · K  (slope ½ on log-log)
    GHZ bulk:      ⟨X_system⟩ = cos(N·K),  φ_sys = N · K   (slope 1 on log-log)

  Discriminating observable: log-log slope of φ_sys vs N.
    Slope = ½  → product bulk (each bulk qubit contributes incoherently)
    Slope = 1  → GHZ bulk (coherent N-fold amplification)

═════════════════════════════════════════════════════════════════════════════
HARDWARE FEASIBILITY NOTES (updated 2026-04-29 from real ibm_fez data):
═════════════════════════════════════════════════════════════════════════════

  N = 2, 4, 8:    Reliable on IBM Eagle/Heron (free tier). Confirmed
                  on ibm_fez 2026-04-28 — slope-½ and slope-1 cleanly
                  separated, predicted ⟨X_sys⟩ matched theory.
  N = 16:         Without mitigation: ~20% loss (product), ~46% loss
                  (GHZ). With readout mitigation + DD enabled below:
                  expected to recover to within ~10% of theory.
  N = 32:         Without mitigation: SATURATED (system qubit ⟨X⟩ → 0
                  on ibm_fez 2026-04-29, both circuits). The system
                  qubit's path through SWAP networks accumulates 50-100+
                  CNOTs on heavy-hex topology; that depth exceeds the
                  fidelity budget. Skipped by default in this version.
                  Options to recover N=32:
                    - RESILIENCE_LEVEL = 2 (ZNE; 3-5× shot cost)
                    - K = 0.02 (smaller signal but unambiguous; keeps
                      ⟨X⟩ well clear of zero so saturation is unmistakable)
                    - Trapped-ion backend (IonQ/Quantinuum, paid) with
                      native all-to-all connectivity erases the SWAP
                      problem entirely.

  This version enables, by default (hardware mode only):
    - Readout error mitigation (T-REx, resilience_level = 1)
    - Dynamical decoupling (XpXm sequence) on idle qubits
  These cost effectively no extra shots and ~5-15% additional wall time,
  but recover most of the N=16 fidelity loss observed without them.

═════════════════════════════════════════════════════════════════════════════
SETUP:
═════════════════════════════════════════════════════════════════════════════

  pip install qiskit qiskit-ibm-runtime qiskit-aer matplotlib numpy

  Authenticate with IBM Quantum (free tier at https://quantum.ibm.com).
  If rotating an API key, re-run save_account with the new token (this
  overwrites the stored credentials):

      from qiskit_ibm_runtime import QiskitRuntimeService
      QiskitRuntimeService.save_account(
          channel="ibm_quantum",
          token="YOUR_NEW_TOKEN_HERE",
          overwrite=True,
      )

  Then set USE_HARDWARE = True below.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


# ─── Configuration ──────────────────────────────────────────────────────────

N_VALUES     = [2, 4, 8, 16]          # Default: clean fit through known-good range.
                                       # Add 32 only with mitigation tuned (see notes).
K            = 0.06                    # Rzz coupling (rad). At N=32, GHZ phase = 1.92
                                       # rad rotates past π/2 — for clean N=32, use K=0.02.
SHOTS        = 4096
USE_HARDWARE = True
BACKEND_NAME = None                    # None = least busy; or e.g. "ibm_brisbane"

# ── Mitigation toggles (hardware mode only) ─────────────────────────────────
RESILIENCE_LEVEL = 1                   # 0 = none, 1 = readout (T-REx), 2 = + ZNE
ENABLE_DD        = True                # XpXm dynamical decoupling on idle qubits
DD_SEQUENCE      = "XpXm"              # "XpXm", "XX", or "XY4"


# ─── Circuit builders ───────────────────────────────────────────────────────

def circuit_product_bulk(n_bulk: int, K: float) -> QuantumCircuit:
    """
    System qubit q0 in |+⟩ coupled to n_bulk independent |+⟩ qubits via Rzz(K).
    Bulk qubits are NOT entangled with each other — product state.
    Predicted: ⟨X_system⟩ = cos^N(K), φ_sys ≈ √N · K
    """
    qc = QuantumCircuit(n_bulk + 1)
    for i in range(n_bulk + 1):
        qc.h(i)                       # all qubits → |+⟩
    for i in range(1, n_bulk + 1):
        qc.rzz(K, 0, i)               # system ↔ bulk qubit i
    return qc


def circuit_ghz_bulk(n_bulk: int, K: float) -> QuantumCircuit:
    """
    System qubit q0 in |+⟩ coupled to GHZ-entangled bulk via Rzz(K).
    Bulk: H on q1 + CNOT cascade through q2..q_n → (|0..0⟩+|1..1⟩)/√2.
    Predicted: ⟨X_system⟩ = cos(N·K), φ_sys = N · K
    """
    qc = QuantumCircuit(n_bulk + 1)
    qc.h(0)                           # system → |+⟩
    qc.h(1)                           # seed of GHZ
    for i in range(2, n_bulk + 1):
        qc.cx(1, i)                   # CNOT cascade
    for i in range(1, n_bulk + 1):
        qc.rzz(K, 0, i)               # system ↔ each bulk qubit
    return qc


# ─── Theory predictions ─────────────────────────────────────────────────────

def predicted_X(n_bulk: int, K: float, kind: str) -> float:
    """Noiseless theoretical ⟨X_sys⟩ for product or GHZ bulk."""
    if kind == 'product':
        return np.cos(K) ** n_bulk
    elif kind == 'ghz':
        return np.cos(n_bulk * K)
    raise ValueError(kind)


# ─── Backend selection ──────────────────────────────────────────────────────

def get_backend():
    if USE_HARDWARE:
        from qiskit_ibm_runtime import QiskitRuntimeService
        service = QiskitRuntimeService()
        if BACKEND_NAME is None:
            backend = service.least_busy(simulator=False, operational=True,
                                          min_num_qubits=max(N_VALUES) + 1)
        else:
            backend = service.backend(BACKEND_NAME)
        print(f"Hardware backend: {backend.name}")
        return backend, service
    else:
        from qiskit_aer import AerSimulator
        backend = AerSimulator()
        print("Local Aer simulator (USE_HARDWARE=False)")
        return backend, None


# ─── Observable construction ────────────────────────────────────────────────

def make_observables(n_total: int):
    """⟨X⟩ on system qubit (q0) and on representative bulk qubit (q1)."""
    pauli_sys = "I" * (n_total - 1) + "X"          # X on q0 (rightmost)
    pauli_b0  = "I" * (n_total - 2) + "X" + "I"    # X on q1
    return (
        SparsePauliOp.from_list([(pauli_sys, 1.0)]),
        SparsePauliOp.from_list([(pauli_b0,  1.0)]),
    )


# ─── Estimator construction with mitigations ────────────────────────────────

def build_estimator(backend):
    """
    Build EstimatorV2 with mitigation options enabled per config.
    Hardware: applies readout mitigation + DD as configured.
    Local Aer: noiseless, MPS method (handles 33-qubit circuits cheaply).
    """
    if USE_HARDWARE:
        from qiskit_ibm_runtime import EstimatorV2 as Estimator
        estimator = Estimator(mode=backend)
        estimator.options.default_shots = SHOTS
        estimator.options.resilience_level = RESILIENCE_LEVEL
        if ENABLE_DD:
            estimator.options.dynamical_decoupling.enable = True
            estimator.options.dynamical_decoupling.sequence_type = DD_SEQUENCE
        print(f"  Mitigations: resilience_level={RESILIENCE_LEVEL}, "
              f"DD={'on (' + DD_SEQUENCE + ')' if ENABLE_DD else 'off'}")
        return estimator
    else:
        from qiskit_aer.primitives import EstimatorV2 as Estimator
        return Estimator(options={
            "backend_options": {"method": "matrix_product_state"},
        })


# ─── Main experiment loop ───────────────────────────────────────────────────

def run_experiment():
    backend, _ = get_backend()
    pm = generate_preset_pass_manager(optimization_level=3, backend=backend)
    estimator = build_estimator(backend)

    results = {'product': {}, 'ghz': {}}

    for n_bulk in N_VALUES:
        n_total = n_bulk + 1
        obs_sys, obs_b0 = make_observables(n_total)

        print(f"\nN_bulk = {n_bulk}  (total qubits = {n_total})")

        for label, build_fn in [('product', circuit_product_bulk),
                                 ('ghz',     circuit_ghz_bulk)]:
            qc = build_fn(n_bulk, K)
            qc_t = pm.run(qc)
            obs_sys_t = obs_sys.apply_layout(qc_t.layout)
            obs_b0_t  = obs_b0.apply_layout(qc_t.layout)

            pubs = [(qc_t, [obs_sys_t, obs_b0_t])]
            result = estimator.run(pubs).result()
            evs  = result[0].data.evs
            stds = getattr(result[0].data, 'stds', None)

            ev_sys = float(np.atleast_1d(evs[0])[0])
            ev_b0  = float(np.atleast_1d(evs[1])[0])
            if stds is not None:
                std_sys = float(np.atleast_1d(stds[0])[0])
                std_b0  = float(np.atleast_1d(stds[1])[0])
            else:
                std_sys = std_b0 = 0.0

            x_pred = predicted_X(n_bulk, K, label)

            results[label][n_bulk] = {
                'X_sys':     ev_sys,
                'X_sys_std': std_sys,
                'X_b0':      ev_b0,
                'X_b0_std':  std_b0,
                'X_pred':    x_pred,
                'phi_sys':   float(np.arccos(np.clip(ev_sys, -1.0, 1.0))),
                'phi_b0':    float(np.arccos(np.clip(ev_b0,  -1.0, 1.0))),
                'phi_pred':  float(np.arccos(np.clip(x_pred, -1.0, 1.0))),
            }
            r = results[label][n_bulk]
            loss = (1.0 - abs(ev_sys / x_pred)) * 100 if abs(x_pred) > 0.05 else float('nan')
            print(f"  {label:7s}  ⟨X_sys⟩ = {ev_sys:+.4f} ± {std_sys:.4f}  "
                  f"(pred {x_pred:+.4f}, loss {loss:+.1f}%)   "
                  f"φ_sys = {r['phi_sys']:.4f}  (pred {r['phi_pred']:.4f})")

    return results


# ─── Plotting ───────────────────────────────────────────────────────────────

def _phi_err(x_mean: float, x_std: float) -> float:
    """Propagate σ(X) → σ(arccos(X)) = σ(X)/sqrt(1-X²). Saturates near |X|=1."""
    denom = np.sqrt(max(1.0 - x_mean**2, 1e-6))
    return x_std / denom


def plot_results(results, title_suffix: str = ""):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    fig.suptitle(f'Bulk-sync asymmetry on quantum hardware{title_suffix}',
                 fontsize=12)

    N_arr = np.array(N_VALUES, dtype=float)
    phi_prod      = np.array([results['product'][int(n)]['phi_sys']  for n in N_arr])
    phi_ghz       = np.array([results['ghz']    [int(n)]['phi_sys']  for n in N_arr])

    # Propagated errors on phi from X stds
    phi_prod_err = np.array([
        _phi_err(results['product'][int(n)]['X_sys'],
                 results['product'][int(n)]['X_sys_std'])
        for n in N_arr])
    phi_ghz_err = np.array([
        _phi_err(results['ghz'][int(n)]['X_sys'],
                 results['ghz'][int(n)]['X_sys_std'])
        for n in N_arr])

    # Theory curves on a denser grid for the dashed lines
    N_dense = np.linspace(min(N_arr), max(N_arr), 100)
    phi_prod_theory = np.sqrt(N_dense) * K
    phi_ghz_theory  = N_dense * K

    # Panel A: system phase vs N (the slope discriminator)
    ax = axes[0]
    ax.errorbar(N_arr, phi_prod, yerr=phi_prod_err, fmt='o-', color='steelblue',
                capsize=3, label='Product bulk (measured)')
    ax.errorbar(N_arr, phi_ghz,  yerr=phi_ghz_err,  fmt='s-', color='firebrick',
                capsize=3, label='GHZ bulk (measured)')
    ax.plot(N_dense, phi_prod_theory, '--', color='steelblue', alpha=0.5,
            label='√N · K  (theory, slope ½)')
    ax.plot(N_dense, phi_ghz_theory,  '--', color='firebrick', alpha=0.5,
            label='N · K   (theory, slope 1)')
    ax.set_xscale('log'); ax.set_yscale('log')
    ax.set_xlabel('Bulk size N')
    ax.set_ylabel('System phase φ_sys (rad)')
    ax.set_title('System qubit phase vs bulk size')
    ax.legend(fontsize=9)
    ax.grid(True, which='both', alpha=0.3)

    # Panel B: ⟨X_sys⟩ measured vs predicted (the diagnostic for decoherence)
    ax = axes[1]
    X_prod      = np.array([results['product'][int(n)]['X_sys']     for n in N_arr])
    X_prod_std  = np.array([results['product'][int(n)]['X_sys_std'] for n in N_arr])
    X_prod_pred = np.array([results['product'][int(n)]['X_pred']    for n in N_arr])
    X_ghz       = np.array([results['ghz']    [int(n)]['X_sys']     for n in N_arr])
    X_ghz_std   = np.array([results['ghz']    [int(n)]['X_sys_std'] for n in N_arr])
    X_ghz_pred  = np.array([results['ghz']    [int(n)]['X_pred']    for n in N_arr])

    ax.errorbar(N_arr, X_prod, yerr=X_prod_std, fmt='o-', color='steelblue',
                capsize=3, label='Product ⟨X_sys⟩ (measured)')
    ax.errorbar(N_arr, X_ghz,  yerr=X_ghz_std,  fmt='s-', color='firebrick',
                capsize=3, label='GHZ ⟨X_sys⟩ (measured)')
    ax.plot(N_arr, X_prod_pred, '--', color='steelblue', alpha=0.5,
            label='Product (theory)')
    ax.plot(N_arr, X_ghz_pred,  '--', color='firebrick', alpha=0.5,
            label='GHZ (theory)')
    ax.axhline(0.0, color='gray', linestyle=':', alpha=0.5,
               label='Decoherence floor (⟨X⟩=0)')
    ax.set_xscale('log')
    ax.set_xlabel('Bulk size N')
    ax.set_ylabel('⟨X_system⟩')
    ax.set_title('Decoherence diagnostic: measured vs theory ⟨X_sys⟩')
    ax.legend(fontsize=9)
    ax.grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    fname = 'bulk_sync_hardware.png'
    plt.savefig(fname, dpi=150)
    print(f"\nSaved: {fname}")


# ─── Slope fit and report ───────────────────────────────────────────────────

SATURATION_THRESHOLD = 0.05      # |⟨X⟩| below this is treated as decohered

def report_slopes(results):
    print("\n" + "=" * 70)
    print("LOG-LOG SLOPE FIT (the discriminator)")
    print("=" * 70)

    N_arr = np.array(N_VALUES, dtype=float)
    saturated = []   # (label, N) pairs treated as saturated

    for label, expected in [('product', 0.5), ('ghz', 1.0)]:
        phi  = np.array([results[label][int(n)]['phi_sys'] for n in N_arr])
        Xsys = np.array([results[label][int(n)]['X_sys']   for n in N_arr])
        phi  = np.clip(phi, 1e-6, None)         # guard log of zero

        # Identify saturated points
        keep_mask = np.abs(Xsys) > SATURATION_THRESHOLD
        sat_Ns = N_arr[~keep_mask]
        for n in sat_Ns:
            saturated.append((label, int(n)))

        # Full fit
        slope_full, _ = np.polyfit(np.log(N_arr), np.log(phi), 1)

        # Unsaturated-only fit
        if keep_mask.sum() >= 2:
            slope_clean, _ = np.polyfit(
                np.log(N_arr[keep_mask]), np.log(phi[keep_mask]), 1)
            clean_str = f"{slope_clean:+.3f}  (using {keep_mask.sum()}/{len(N_arr)} pts)"
        else:
            clean_str = "n/a (too few unsaturated points)"

        print(f"  {label:7s}   full slope    = {slope_full:+.3f}    "
              f"(expected {expected:+.2f})    "
              f"deviation = {slope_full - expected:+.3f}")
        print(f"  {label:7s}   clean slope   = {clean_str}")

    if saturated:
        print("\n  ⚠ Saturated points (|⟨X⟩| < {:.2f}, treated as decohered):"
              .format(SATURATION_THRESHOLD))
        for label, n in saturated:
            x = results[label][n]['X_sys']
            print(f"      {label:7s} N={n:<3d}  ⟨X_sys⟩={x:+.4f}  "
                  f"(noise floor — exclude from slope fit)")
        print("\n  Recovery options if saturation appears at smaller N than expected:")
        print("      1. Increase RESILIENCE_LEVEL to 2 (enables ZNE; ~3-5× shot cost)")
        print("      2. Reduce K (e.g., K = 0.02) — smaller phase per qubit")
        print("      3. Switch to all-to-all backend (IonQ/Quantinuum, paid)")
    else:
        print("\n  ✓ All measured points clear of decoherence floor.")

    print("\nInterpretation:")
    print("  • Slopes near 0.5 (product) and 1.0 (GHZ) confirm the simulation's")
    print("    prediction holds on real hardware.")
    print("  • This is a CONSISTENCY CHECK against standard quantum metrology,")
    print("    not an experimental discrimination of MCI from standard QM.")
    print("  • For framework-distinctive tests, see §5.4 (linewidth gravitational")
    print("    Bell), §6.2 P4 (kaon/B-meson decoherence), and sg_angular.py.")


# ─── Main ───────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 70)
    print("BULK SYNC ASYMMETRY — HARDWARE DEMONSTRATION (mitigated v2)")
    print("=" * 70)
    print(f"  N values         : {N_VALUES}")
    print(f"  Coupling K       : {K} rad  (N·K_max = {max(N_VALUES) * K:.3f} rad)")
    print(f"  Shots per circuit: {SHOTS}")
    print(f"  Hardware mode    : {USE_HARDWARE}")
    print(f"  Backend override : {BACKEND_NAME or '(least-busy)'}")
    if USE_HARDWARE:
        print(f"  Resilience level : {RESILIENCE_LEVEL}  (0=none, 1=readout, 2=+ZNE)")
        print(f"  Dynamical decoup : {'on (' + DD_SEQUENCE + ')' if ENABLE_DD else 'off'}")
    print("=" * 70)

    results = run_experiment()

    suffix = " — IBM hardware (mitigated)" if USE_HARDWARE else " — local simulator"
    plot_results(results, title_suffix=suffix)
    report_slopes(results)
