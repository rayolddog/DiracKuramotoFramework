"""
bell_phase.py — Task 2: Bell Inequality with Time-Phase Synchronization
=======================================================================

Three models compared:
  1. Classical LHV (deterministic, uniform hidden phase)       → triangular, CHSH ≤ 2.00
  2. Phase-clock model (Malus-law probabilistic outcomes)      → -(1/2)cos(Δ), CHSH ≤ √2
  3. Standard quantum mechanics (singlet state)                → -cos(Δ),  CHSH ≤ 2√2

IMPORTANT MATHEMATICAL NOTE:
─────────────────────────────
Bell proved that ANY local hidden variable theory satisfies CHSH ≤ 2.
The time-phase model (as formulated below) IS a local hidden variable theory:
  - hidden variable λ = φ_0 (shared initial particle clock phase)
  - outcomes A(a, φ_0) and B(b, φ_0) are locally determined

So by Bell's theorem it cannot exceed CHSH = 2.  In fact model 2 achieves
only CHSH ≈ √2 ≈ 1.41 — LESS than the classical bound.

WHERE THE USER'S INSIGHT APPLIES:
──────────────────────────────────
Bell's factorization assumption is:
    P(A,B | a,b,λ) = P_A(a | λ) · P_B(b | λ)

The user proposes that the DETECTOR PHASES Φ_D1, Φ_D2 are also hidden
variables (entangled with the bulk), so the full hidden state is:
    Λ = (φ_0, Φ_bulk)     with Φ_D1 = Φ_D2 = Φ_bulk (detector entanglement)

If the synchronization process produces NON-LOCAL correlations between
the particle's outcome and the detector's phase state, the factorization
can fail. This is related to the "measurement-independence loophole":
Bell requires P(λ | a,b) = P(λ) — that the hidden variable is independent
of the measurement choice. In this model the clock synchronization couples
λ to the measurement context.

The correlation function below formally shows exactly where the factorization
assumption enters and what extra term the time-phase model introduces.

FORMAL DERIVATION:
──────────────────
Bell writes:
    E(a,b) = ∫ A(a,λ) · B(b,λ) · ρ(λ) dλ

Time-phase extension with detector entanglement:
    E(a,b) = ∫∫ A(a,φ_0,Φ) · B(b,φ_0,Φ) · ρ(φ_0) · ρ_D(Φ) dφ_0 dΦ

If Φ is SHARED (D1 and D2 both see same Φ_bulk), the integral does NOT
factorize as P_A(a|φ_0) · P_B(b|φ_0) because the synchronization couples
outcome probabilities to the SAME Φ, introducing a non-trivial cross-term:

    E(a,b) = ∫∫ cos(a − φ_0 + Φ) · (−cos(b − φ_0 + Φ)) ρ dφ_0 dΦ
           = −(1/2) cos(a−b)          [still -(1/2)cos with uniform Φ]

To obtain the FULL quantum result −cos(a−b), the effective marginals must
be super-classical — requiring |⟨A⟩| > 1/√2 for some measurement contexts.
This can only occur if the synchronization introduces genuine contextuality
(i.e., the outcome of A depends on what is being measured at B through the
shared Φ). That would require the detector phases to be quantum-entangled
resources, not just classical shared variables.

CONCLUSION: The model correctly identifies WHERE Bell's proof breaks down
(the detector-phase entanglement), but to reproduce full QM correlations the
synchronization mechanism must be quantum (not classical Kuramoto) in nature.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# ─── Model 1: Classical LHV (deterministic) ──────────────────────────────────

def correlation_classical_lhv(delta, n_samples=200_000):
    """
    Hidden variable: φ_0 ~ Uniform[0, 2π]
    A(a, φ_0) = sign(cos(a − φ_0))
    B(b, φ_0) = −sign(cos(b − φ_0))   [singlet anti-correlation]
    E(a,b) = -(1 − 2|Δ|/π)   for |Δ| ≤ π   [triangular wave, analytical]
    """
    phi0 = np.random.uniform(0, 2 * np.pi, n_samples)
    A = np.sign(np.cos(-phi0))           # a=0 reference
    B = -np.sign(np.cos(delta - phi0))
    return np.mean(A * B)


def e_classical_analytical(delta):
    """Analytical triangular result: -(1 - 2|Δ|/π) for |Δ| ∈ [0,π]."""
    d = np.abs(delta) % (2 * np.pi)
    d = np.where(d > np.pi, 2 * np.pi - d, d)
    return -(1.0 - 2.0 * d / np.pi)


# ─── Model 2: Phase-clock with Malus-law outcomes ────────────────────────────

def e_phase_clock(delta):
    """
    Probabilistic outcome rule (Malus law on phase):
      P(A=+1 | a, φ_0) = cos²((a − φ_0)/2)
      P(B=+1 | b, φ_0) = sin²((b − φ_0)/2)   [singlet: opposite Bloch point]

    Analytical result after integrating over φ_0 ~ Uniform[0, 2π]:
      ⟨A⟩ = ∫ cos(a−φ) dφ/2π = 0                (marginals unbiased ✓)
      E(a,b) = ∫ cos(a−φ)·(−cos(b−φ)) dφ/2π = −(1/2)cos(a−b)

    Factor of 1/2 shortfall vs QM: the model under-correlates because
    the hidden phase must serve BOTH the A and B measurement contexts with
    values bounded in [−1, 1], limiting the achievable Cauchy-Schwarz bound.
    """
    return -0.5 * np.cos(delta)


# ─── Model 3: Standard QM ────────────────────────────────────────────────────

def e_quantum(delta):
    """
    Standard QM singlet correlation:  E(a,b) = −cos(a−b)
    Violates Bell/CHSH up to Tsirelson bound 2√2 ≈ 2.83.
    """
    return -np.cos(delta)


# ─── CHSH Calculator ─────────────────────────────────────────────────────────

def chsh(e_func, angles=None):
    """
    CHSH = |E(a,b) − E(a,b') + E(a',b) + E(a',b')|
    Default angles: optimal for QM (a=0, a'=π/2, b=π/4, b'=3π/4)
    """
    if angles is None:
        a, a2, b, b2 = 0, np.pi / 2, np.pi / 4, 3 * np.pi / 4
    else:
        a, a2, b, b2 = angles
    return abs(e_func(a - b) - e_func(a - b2) + e_func(a2 - b) + e_func(a2 - b2))


def chsh_optimal(e_func, n_grid=360):
    """Numerically find the maximum CHSH over all angle combinations."""
    best = 0.0
    angles_range = np.linspace(0, np.pi, n_grid)
    for a2 in angles_range:
        for b in angles_range:
            for b2 in angles_range:
                val = abs(e_func(0) - e_func(-b2) + e_func(a2 - b) + e_func(a2 - b2))
                if val > best:
                    best = val
    return best


# ─── Where Bell's factorization breaks ───────────────────────────────────────

def print_bell_derivation():
    """
    Print the formal step where the factorization assumption enters and
    what the time-phase model adds.
    """
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║       BELL'S DERIVATION: WHERE THE TIME-PHASE TERM ENTERS               ║
╚══════════════════════════════════════════════════════════════════════════╝

Standard Bell (1964):
─────────────────────
  E(a,b) = ∫ A(a,λ) B(b,λ) ρ(λ) dλ          ...(1)

  Key assumption: P(λ | settings a,b) = ρ(λ)  [measurement independence]
  Key assumption: A depends only on (a, λ), B only on (b, λ)  [locality]

  From (1) with |A| ≤ 1, |B| ≤ 1:
    |E(a,b) − E(a,b') + E(a',b) + E(a',b')| ≤ 2    [CHSH inequality]

Time-Phase Extension:
─────────────────────
  Hidden state Λ = (φ_0, Φ_bulk) where:
    φ_0    = shared particle clock phase at creation
    Φ_bulk = shared detector clock phase (D1 and D2 entangled)

  E(a,b) = ∫∫ A(a, φ_0, Φ) · B(b, φ_0, Φ) · ρ(φ_0) · ρ_D(Φ) dφ_0 dΦ

  Factorization P_A · P_B FAILS if:
    A(a, φ_0, Φ) ≠ f(a, φ_0) alone   [A depends on Φ = detector context]

  This is the CONTEXTUALITY TERM:
    ΔE_context(a,b) = E_full(a,b) − E_factorized(a,b)

  For classical Kuramoto synchronization:
    φ_0 → Φ after detection, so A effectively measures (a − Φ + φ_0)
    Averaging over Φ: ΔE_context cancels → still -(1/2)cos(a−b)

  For QUANTUM synchronization (Φ treated as quantum resource):
    A and B outcomes are correlated through shared quantum Φ in a way
    that cannot be expressed as f(a,φ_0)·g(b,φ_0)
    → This IS quantum entanglement, described differently

  The gap between −(1/2)cos and −cos is:
    ΔE_missing(a,b) = −(1/2)cos(a−b)
    Requires: ∫ [A_quant(a,Λ) − A_class(a,Λ)] · B(b,Λ) ρ dΛ = −(1/2)cos(a−b)

  This is exactly what quantum entanglement provides and classical
  phase synchronization cannot.
""")


# ─── Main ────────────────────────────────────────────────────────────────────

def run():
    print_bell_derivation()

    deltas = np.linspace(-np.pi, np.pi, 500)

    e_cl  = e_classical_analytical(deltas)
    e_pc  = e_phase_clock(deltas)
    e_qm  = e_quantum(deltas)

    # ── Compute CHSH values ───────────────────────────────────────────────
    print("\n── CHSH VALUES (optimal angles: a=0, a'=π/2, b=π/4, b'=3π/4) ──")
    print(f"  Classical LHV (triangular):          {chsh(e_classical_analytical):.4f}   (bound = 2.000)")
    print(f"  Phase-clock model (-(1/2)cos):        {chsh(e_phase_clock):.4f}   (bound = √2 ≈ 1.414)")
    print(f"  Quantum mechanics (-cos):             {chsh(e_quantum):.4f}   (Tsirelson = 2√2 ≈ 2.828)")
    print(f"  Bell classical bound:                 2.0000")
    print(f"  Tsirelson quantum bound:              {2*np.sqrt(2):.4f}")

    print("\n  Note: Phase-clock model gives CHSH < classical bound.")
    print("  The model is sub-classical in this formulation.")
    print("  To reach full QM correlations, synchronization must be")
    print("  quantum-mechanical (entangled Φ_bulk), not classical Kuramoto.")

    # ── Plot ──────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Bell Inequality: Time-Phase Model vs QM vs Classical LHV", fontsize=13)

    ax = axes[0]
    ax.plot(deltas, e_qm,  label='QM:  −cos(Δ)',             color='royalblue',   linewidth=2.5)
    ax.plot(deltas, e_pc,  label='Phase-clock: −½cos(Δ)',    color='darkorange',  linewidth=2, linestyle='--')
    ax.plot(deltas, e_cl,  label='Classical LHV: triangular', color='green',       linewidth=1.5, linestyle=':')
    ax.axhline(0, color='k', linewidth=0.5)
    ax.fill_between(deltas, e_pc, e_qm, alpha=0.12, color='royalblue',
                    label='Gap: missing quantum correlations')
    ax.set_xlabel('Δ = a − b  (rad)')
    ax.set_ylabel('E(a, b)')
    ax.set_title('Correlation functions')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # CHSH bar chart
    ax = axes[1]
    models = ['Classical LHV\n(triangular)', 'Phase-clock\n−½cos(Δ)', 'Quantum\n−cos(Δ)']
    chsh_vals = [chsh(e_classical_analytical), chsh(e_phase_clock), chsh(e_quantum)]
    colors = ['green', 'darkorange', 'royalblue']
    bars = ax.bar(models, chsh_vals, color=colors, alpha=0.8, edgecolor='k')
    ax.axhline(2.0,        color='red',    linestyle='--', linewidth=1.5, label='Bell bound (CHSH=2)')
    ax.axhline(2*np.sqrt(2), color='navy', linestyle=':', linewidth=1.5, label='Tsirelson bound (2√2)')
    ax.set_ylabel('CHSH value')
    ax.set_title('CHSH comparison (optimal angles)')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 3.2)
    for bar, val in zip(bars, chsh_vals):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.05, f'{val:.3f}',
                ha='center', fontsize=10, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('bell_phase.png', dpi=150)
    print("\nSaved: bell_phase.png")
    plt.show()


if __name__ == '__main__':
    run()
