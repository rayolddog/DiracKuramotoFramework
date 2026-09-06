# The entanglement cut — results, scored against `PREDICTIONS_entanglement_cut.md`

*2026-09-05. `entanglement_cut.py`, exact Lindblad propagation of the two-absorber state
and an exact finite-bath cross-check; output `entanglement_cut_output.txt`; instantaneous.
No statistical error; the scope is the two-qubit Markov model and the single-excitation
finite-bath model.*

## Scorecard

| # | prediction | outcome | score |
|---|---|---|---|
| 1 | Independent dephasing: C = e^{−2γt} for Ψ⁺ and Φ⁺, "equal to the product of the local single-quantum coherences" | C = e^{−2γt} to 5 decimals for both; but the local coherences c_A, c_B are **zero at every time** for both states — the reduced state of a maximally entangled pair is maximally mixed | rate confirmed; **phrasing wrong**: the concurrence is the two-spin coherence (ZQ for Ψ⁺, DQ for Φ⁺), which decays as the product of the two local *decay factors*, not of the local coherences, which never exist |
| 2 | Correlated dephasing: Ψ⁺ protected at C = 1; Φ⁺ decays as e^{−4γt} | C(Ψ⁺) = 1.00000 at every t; C(Φ⁺) = e^{−4γt} to 5 decimals | confirmed |
| 3 | Independent damping: Ψ⁺ C = e^{−Γt}; Φ⁺ C = (1−p)², asymptotic; tilted state dies exactly at Γt = ln 2 | all three to 5 decimals; tilted C = 0.00006 at t = 0.693 and 0 from t = 0.75 on, while its double-quantum coherence is still 0.40 at death and 0.29 at t = 1 | confirmed |
| 4 | Finite channels: N = 64 reproduces e^{−Γt} to 0.01 for Γt ≤ 2; N = 4 revives; N = 1 oscillates | N = 64: deviations 0.017, 0.013, 0.005, 0.001, 0.000 at t = 0.5–5 (the short-time excess is the non-Markovian onset); N = 4: 0.74 → 0.97 → 0.89, revival; N = 1: 0.09, 0.66, 0.11, 0.08, 1.00 | confirmed in substance; the 0.01 bracket missed at the two shortest times |

## Findings, in the scanner's language

**F1. Under independent dephasing the entanglement cut is gradual, set by the two local T₂
rates, and invisible locally.** The zero-quantum coherence of Ψ⁺ and the double-quantum
coherence of Φ⁺ both decay at the sum of the single-quantum rates, e^{−2γt}, with no
threshold; but neither spin has any single-quantum coherence at any time. A loss of
entanglement "as a gradual loss of phase coherence" is right about the rate and wrong
about where to look: the phase coherence that is lost is the pair's, and it is not the
sum of anything either spin shows on its own.

**F2. Under a common fluctuating field, the zero-quantum state does not decay at all and
the double-quantum state decays twice as fast.** Ψ⁺ sits in the decoherence-free subspace
of the collective dephasing and keeps concurrence 1 for all time — the singlet order that
outlives T₁ in Levitt's long-lived-state experiments, here exact; Φ⁺'s double-quantum
coherence takes the two kicks coherently and decays at 4γ against 2γ for independent
kicks. The trichotomy's rows for a pair: a common reference protects, independent
references destroy, and which state is protected depends on how many quanta its coherence
carries.

**F3. Under damping into separate record channels the cut can be sharp.** The
single-excitation state decays as the survival amplitude, gradually; the balanced Φ⁺
reaches zero only asymptotically; the tilted state, with more weight on the doubly
excited component, loses all entanglement at exactly Γt = ln 2 and stays disentangled,
while every local population decays smoothly and its double-quantum coherence is still
0.40 at the moment of death. This is Yu and Eberly's entanglement sudden death, reproduced
to four decimals. It is a cut in the pair with nothing sharp at either site — which the
single-site recoverability crossover of the paper never was.

**F4. The entanglement cut needs a dense record channel, as the single-site cut did.** With
64 modes per absorber the exact finite-bath model tracks the Markov decay to a percent
after the non-Markovian onset; with 4 it revives; with 1 it oscillates and never settles.

## What this answers

The sponsor's question — does the Heisenberg cut, a gradual crossover in recoverability,
extend to a model of losing entanglement, and is that loss a gradual loss of phase
coherence — has three answers in the same model, selected by the state and the noise: (i)
gradual, at the sum of the local rates, and invisible in any local coherence
(independent dephasing); (ii) protected or accelerated by a factor two, according to the
quantum number of the coherence, under a common reference (correlated dephasing); (iii)
sharp, at a finite time, with nothing sharp locally, when a record channel drains a state
with a doubly excited component (damping). MRI contains all three: T₂ decay of
single-quantum coherence, the long-lived singlet, and the faster death of double-quantum
order under T₁. None of this is new physics; all of it is standard open-systems theory
(Yu & Eberly 2004, 2009; Carravetta, Johannessen & Levitt 2004; Levitt 2012). What it
establishes for the programme is that "cut" can mean a genuine finite-time boundary for a
pair, and that the machinery built for the single-site crossover computes it exactly.
