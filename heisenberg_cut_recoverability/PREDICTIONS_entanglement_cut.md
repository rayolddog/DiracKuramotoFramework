# The entanglement cut: two absorbers, three regimes — predictions, fixed before running

*2026-09-05, at the sponsor's instruction, after his question whether the Heisenberg cut, a
gradual loss of reversibility, extends to a model of losing entanglement and whether that
loss is a gradual loss of phase coherence. The comparison is to NMR, which names two-spin
coherences by the number of quanta they carry: single-quantum (one spin's coherence, the
Larmor signal, lost at T₂), double-quantum (|ee⟩⟨gg|), zero-quantum (|eg⟩⟨ge|, the
singlet-like combination). Written before `entanglement_cut.py` was run.*

## Model

Two two-level absorbers A and B, each coupled to its own record channel or to a common
one, in the dense-record (Markov) limit stage 1 established: an exact Lindblad master
equation on the 4 × 4 two-qubit state, propagated by the matrix exponential of the
Liouvillian. Entanglement is Wootters' concurrence C(t); the local single-quantum
coherence is c_A(t) = 2|ρ_A,eg|; the double- and zero-quantum coherences are 2|ρ_ee,gg|
and 2|ρ_eg,ge|. Four initial states: |Ψ⁺⟩ = (|eg⟩ + |ge⟩)/√2 (one excitation, zero-quantum
entangled); |Φ⁺⟩ = (|ee⟩ + |gg⟩)/√2 (double-quantum entangled); the tilted state
|Φ_θ⟩ = √0.2|gg⟩ + √0.8|ee⟩ (more weight on the doubly excited component); and a product
state as the null. Three noises: independent pure dephasing on each absorber at rate γ
(jump operators √(γ/2) σ_z^A, √(γ/2) σ_z^B); correlated pure dephasing, both absorbers
seeing one fluctuating field (a single jump operator √(γ/2)(σ_z^A + σ_z^B)); independent
amplitude damping into separate record channels at rate Γ (√Γ σ_−^A, √Γ σ_−^B). A
finite-bath cross-check propagates |Ψ⁺⟩ exactly with N record modes per absorber (single-
excitation sector), as in stage 1.

## Predictions

1. **Independent dephasing: gradual, and exactly the product of the local losses.** For
   both |Ψ⁺⟩ and |Φ⁺⟩ the concurrence decays as e^{−2γt}, equal to the product of the two
   single-quantum coherences c_A c_B (each e^{−γt}) to better than 10⁻⁶ at every time. The
   entanglement cut here is the single-site cut twice over: no threshold, no death.
2. **Correlated dephasing: the zero-quantum state is protected, the double-quantum state
   dies twice as fast.** |Ψ⁺⟩ lives in the decoherence-free subspace of σ_z^A + σ_z^B and
   its concurrence stays at 1 to 10⁻¹² for all t — Levitt's long-lived singlet order, in
   the paper's model. |Φ⁺⟩'s concurrence decays as e^{−4γt}, twice the independent rate,
   because the two phase kicks add coherently on the double-quantum coherence. A common
   reference protects; independent references destroy — the trichotomy's rows, for a pair.
3. **Amplitude damping: gradual for one excitation, asymptotic for the balanced pair, and
   a sharp death for the tilted pair.** |Ψ⁺⟩: C = e^{−Γt}, the survival amplitude, gradual.
   |Φ⁺⟩: with p = 1 − e^{−Γt}, C = (1 − p)², reaching zero only as t → ∞. |Φ_θ⟩ with weights
   0.2 and 0.8: C = 2(1 − p)·max(0, 0.4 − 0.8p), which hits zero **exactly at p = 0.5,
   Γt = ln 2 ≈ 0.693**, and stays there — entanglement sudden death (Yu & Eberly), a sharp
   cut in the pair while every local quantity (the populations; the local coherences,
   which are zero throughout for this state) decays smoothly. The sharpness is in the
   entanglement measure, not in any single-site observable.
4. **Finite record channels: the entanglement cut needs a dense record, as the single-site
   cut did.** |Ψ⁺⟩ under independent damping with N modes per absorber over bandwidth 40:
   N = 64 reproduces e^{−Γt} to 0.01 for Γt ≤ 2; N = 4 shows revival of concurrence within
   the run; N = 1 oscillates and never settles.

## What would count as what

- All four confirmed: the answer to the sponsor's question is "it depends on the state and
  the noise, and the model shows all three cases": gradual and equal to the product of
  local losses under independent dephasing; protected or accelerated under a common
  reference; and, for damping of a state with a doubly excited component, a sharp death
  at a finite time with nothing sharp anywhere locally — an entanglement cut that is
  genuinely a cut, which the single-site crossover never was.
- Prediction 3's death time wrong by more than 5 %: the Yu–Eberly X-state formula has
  been misapplied and the run's number stands.
- Prediction 2's protection failing: the correlated jump operator is mis-specified.
