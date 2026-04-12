"""
bulk_sync_asymmetry.py
======================
Tests the clock-phase synchronization asymmetry hypothesis:

HYPOTHESIS: When a single particle (qubit) interacts with a bulk of N particles
via Kuramoto-like ZZ coupling, the single particle undergoes a phase rotation
that is much larger than each bulk particle's rotation. The ratio scales as:
  - sqrt(N) for an unsynchronized (product state) bulk
  - N       for a synchronized (GHZ / Kuramoto cluster) bulk

This maps onto quantum decoherence asymmetry: the system (single qubit) loses
coherence rapidly while the environment (bulk) is barely disturbed per qubit.

QUBIT ↔ CLOCK MAPPING:
  - Qubit in |+⟩ = clock at phase θ=0 (X eigenstate)
  - Rzz(K) gate  = Kuramoto phase coupling, strength K
  - ⟨X_i⟩       = cos(accumulated phase φ_i)
  - K ∝ 1/E      = inverse energy (higher energy → smaller phase rotation per hit)

PREDICTIONS:
  Product bulk  → ⟨X_single⟩ = cos^N(K),  φ_s ≈ sqrt(N)·K
  GHZ bulk      → ⟨X_single⟩ = cos(N·K),  φ_s = N·K  ← coherent sync
  Each bulk (product) → ⟨X_b_i⟩ = cos(K), φ_b = K
  Ratio (GHZ) / Ratio (product) → scales as sqrt(N)

Install: pip install qiskit matplotlib numpy
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive — works headless
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, DensityMatrix, partial_trace


# ---------------------------------------------------------------------------
# Circuit builders
# ---------------------------------------------------------------------------

def circuit_product_bulk(n_bulk: int, K: float) -> QuantumCircuit:
    """
    Single qubit (q0) in |+⟩ coupled to N bulk qubits in |+⟩ via Rzz(K).
    Models an *unsynchronized* bulk — each qubit has its own phase reference.
    """
    qc = QuantumCircuit(n_bulk + 1)
    for i in range(n_bulk + 1):
        qc.h(i)                          # all → |+⟩
    for i in range(1, n_bulk + 1):
        qc.rzz(K, 0, i)                  # ZZ coupling: single ↔ each bulk qubit
    return qc


def circuit_ghz_bulk(n_bulk: int, K: float) -> QuantumCircuit:
    """
    Single qubit (q0) in |+⟩ coupled to N bulk qubits in GHZ state via Rzz(K).
    GHZ = maximally synchronized Kuramoto cluster: collective phase is locked.
    Each individual GHZ qubit has zero definite phase, but the collective does.
    """
    qc = QuantumCircuit(n_bulk + 1)
    qc.h(0)                              # single qubit → |+⟩
    qc.h(1)                              # GHZ seed
    for i in range(1, n_bulk):
        qc.cx(i, i + 1)                  # CNOT chain → (|00..0⟩ + |11..1⟩)/√2
    for i in range(1, n_bulk + 1):
        qc.rzz(K, 0, i)                  # ZZ coupling: single ↔ each bulk qubit
    return qc


# ---------------------------------------------------------------------------
# Measurement helpers
# ---------------------------------------------------------------------------

def reduced_dm(sv: Statevector, qubit: int, n_total: int) -> DensityMatrix:
    """Reduced density matrix of a single qubit (traces out all others)."""
    dm = DensityMatrix(sv)
    trace_out = [i for i in range(n_total) if i != qubit]
    return partial_trace(dm, trace_out)


def x_expectation(dm: DensityMatrix) -> float:
    """⟨X⟩ = Tr[X·ρ]"""
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    return float(np.real(np.trace(X @ dm.data)))


def phase_from_x(dm: DensityMatrix) -> float:
    """Phase angle φ = arccos(⟨X⟩); starts at 0 for |+⟩, grows to π/2 for mixed."""
    return np.arccos(np.clip(x_expectation(dm), -1.0, 1.0))


# ---------------------------------------------------------------------------
# Experiment 1: Phase shift vs bulk size N
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    N_VALUES = list(range(1, 9))
    K = 0.3   # coupling strength

    print("=" * 65)
    print(f"Experiment 1: Phase asymmetry vs N  (K = {K:.2f})")
    print("=" * 65)
    print(f"{'N':>4}  {'φ_s (prod)':>12}  {'φ_b (prod)':>12}  {'ratio':>8}  "
          f"{'φ_s (GHZ)':>12}  {'pred prod':>10}  {'pred GHZ':>10}")
    print("-" * 75)

    prod_phi_s, prod_phi_b, prod_ratio = [], [], []
    ghz_phi_s = []

    for n in N_VALUES:
        n_total = n + 1

        # ---- Product bulk ----
        sv = Statevector(circuit_product_bulk(n, K))
        phi_s = phase_from_x(reduced_dm(sv, 0, n_total))
        phi_bs = [phase_from_x(reduced_dm(sv, i, n_total)) for i in range(1, n_total)]
        phi_b_avg = float(np.mean(phi_bs))
        ratio = phi_s / phi_b_avg if phi_b_avg > 1e-10 else float("nan")
        prod_phi_s.append(phi_s)
        prod_phi_b.append(phi_b_avg)
        prod_ratio.append(ratio)

        # ---- GHZ bulk ----
        sv_ghz = Statevector(circuit_ghz_bulk(n, K))
        phi_s_ghz = phase_from_x(reduced_dm(sv_ghz, 0, n_total))
        ghz_phi_s.append(phi_s_ghz)

        # Analytic predictions
        pred_prod = np.arccos(np.cos(K) ** n)   # cos^N(K) → phase
        pred_ghz  = float(n * K)                 # cos(NK) → phase = NK

        print(f"{n:>4}  {phi_s:>12.4f}  {phi_b_avg:>12.4f}  {ratio:>8.3f}  "
              f"{phi_s_ghz:>12.4f}  {pred_prod:>10.4f}  {pred_ghz:>10.4f}")


    # ---------------------------------------------------------------------------
    # Experiment 2: Energy dependence — sweep K (K ∝ 1/E)
    # ---------------------------------------------------------------------------

    print("\n" + "=" * 65)
    print("Experiment 2: Energy dependence  (N = 4, sweep K)")
    print("=" * 65)

    N_FIXED = 4
    K_VALUES = np.linspace(0.05, 1.2, 40)
    energy_phi_s, energy_phi_b = [], []

    for K_val in K_VALUES:
        sv = Statevector(circuit_product_bulk(N_FIXED, K_val))
        energy_phi_s.append(phase_from_x(reduced_dm(sv, 0, N_FIXED + 1)))
        energy_phi_b.append(phase_from_x(reduced_dm(sv, 1, N_FIXED + 1)))


    # ---------------------------------------------------------------------------
    # Plots
    # ---------------------------------------------------------------------------

    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    fig.suptitle("Clock-Phase Synchronization Asymmetry  (Kuramoto / Bell-without-FTL)",
                 fontsize=13)

    # --- Plot 1: Phase shift of single qubit vs N ---
    ax = axes[0]
    ax.plot(N_VALUES, prod_phi_s, "b-o", label="Product bulk (sim)")
    ax.plot(N_VALUES, ghz_phi_s,  "r-s", label="GHZ bulk (sim)")
    ax.plot(N_VALUES, [np.arccos(np.cos(K)**n) for n in N_VALUES],
            "b--", alpha=0.5, label="cos^N(K) theory")
    ax.plot(N_VALUES, [n * K for n in N_VALUES],
            "r--", alpha=0.5, label="N·K theory")
    ax.set_xlabel("N  (bulk size)")
    ax.set_ylabel("Single qubit phase shift  φ_s  (rad)")
    ax.set_title("Single qubit phase rotation vs bulk size")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.4)

    # --- Plot 2: Ratio φ_s / φ_b vs N (asymmetry test) ---
    ax = axes[1]
    sqrt_N = [np.sqrt(n) for n in N_VALUES]
    lin_N  = list(N_VALUES)

    ax.plot(N_VALUES, prod_ratio, "b-o", lw=2, label="Product bulk ratio (sim)")
    ax.plot(N_VALUES, sqrt_N,     "b--", alpha=0.6, label="√N reference")
    ax.plot(N_VALUES, lin_N,      "r--", alpha=0.6, label="N reference")
    ax.set_xlabel("N  (bulk size)")
    ax.set_ylabel("φ_single / φ_each_bulk")
    ax.set_title("Asymmetry ratio  (hypothesis: scales as √N or N)")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.4)

    # Add annotation
    ax.annotate("Synchronized (GHZ)\nbulk would follow N",
                xy=(5, 5), xytext=(3, 6.5),
                arrowprops=dict(arrowstyle="->", color="red"),
                color="red", fontsize=8)
    ax.annotate("Product bulk\nfollows √N",
                xy=(6, np.sqrt(6)), xytext=(4, 3.5),
                arrowprops=dict(arrowstyle="->", color="blue"),
                color="blue", fontsize=8)

    # --- Plot 3: Energy dependence (K ∝ 1/E) ---
    ax = axes[2]
    ax.plot(K_VALUES, energy_phi_s, "b-",  lw=2, label=f"Single qubit (N={N_FIXED})")
    ax.plot(K_VALUES, energy_phi_b, "g-",  lw=2, label="Each bulk qubit")
    ax.plot(K_VALUES, [np.arccos(np.cos(K_val)**N_FIXED) for K_val in K_VALUES],
            "b--", alpha=0.5, label="cos^N(K) theory")
    ax.plot(K_VALUES, K_VALUES, "g--", alpha=0.5, label="K theory")
    ax2 = ax.twiny()
    ax2.set_xlim(ax.get_xlim())
    ax2.set_xticks(np.linspace(0.05, 1.2, 5))
    ax2.set_xticklabels([f"{1/k:.1f}" for k in np.linspace(0.05, 1.2, 5)], fontsize=8)
    ax2.set_xlabel("Relative energy E  (∝ 1/K)", fontsize=8)
    ax.set_xlabel("Coupling K  (∝ 1/E,  low energy → right)")
    ax.set_ylabel("Phase shift  (rad)")
    ax.set_title(f"Energy dependence  (N = {N_FIXED})")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.4)

    plt.tight_layout()
    plt.savefig("bulk_sync_asymmetry.png", dpi=150, bbox_inches="tight")
    print("\nPlot saved: bulk_sync_asymmetry.png")
    # plt.show()  # non-interactive; savefig above is sufficient


    # ---------------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------------

    print("\n" + "=" * 65)
    print("SUMMARY")
    print("=" * 65)
    print(f"Coupling K = {K:.2f}  (larger K = lower effective energy)")
    print()
    print("Product bulk (unsynchronized):")
    print(f"  φ_single scales as arccos(cos^N(K)) ≈ sqrt(N)·K for small K")
    for n, r in zip(N_VALUES, prod_ratio):
        print(f"  N={n}: ratio = {r:.3f}  (√N = {np.sqrt(n):.3f})")
    print()
    print("GHZ bulk (synchronized Kuramoto cluster):")
    print(f"  φ_single = N·K  (coherent coupling — single qubit feels full bulk)")
    print(f"  Each bulk qubit: individual ⟨X⟩ = 0 (GHZ qubits are maximally mixed)")
    print(f"  → Synchronization amplifies back-reaction by factor N vs product bulk")
    print()
    print("Energy interpretation (K ∝ 1/E):")
    print(f"  High energy photons (small K) → smaller phase rotation per interaction")
    print(f"  Phase inertia ∝ E, consistent with de Broglie clock (ω = E/ℏ)")
    print()
    print("Connection to decoherence:")
    print(f"  Product bulk ratio ≈ √N matches decoherence timescale τ_d ∝ 1/N")
    print(f"  GHZ bulk ratio = N matches coherent (laser/BEC-like) environment")
