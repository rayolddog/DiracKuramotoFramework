# Recoverability test of the Heisenberg-cut threshold — results, scored against the predictions

*2026-09-04. Predictions in `PREDICTIONS.md` (fixed before running; the addendum records a
definition error caught by the calibration and corrected before the corrected run). Code:
`fano_recoverability.py`; raw output: `run_output.txt`; data: `results.json`. Run time 5 s.
Uncertainty stated first: this is an exact calculation, so the numbers carry no statistical
error; what they carry is model scope, stated under each prediction.*

## The model in one paragraph

One photon mode, one absorber excitation detuned by Δ, N record modes over a bandwidth
B = 40 with golden-rule leak rate Γ, single-excitation sector, exact propagation. K = 1 is
the capture matrix element; the resonant Rabi frequency is 2K. Recoverability R is the
partial Loschmidt echo: capture for t, then reverse the system's own Hamiltonian (Δ and K)
for t with the record channel untouched, and read off the photon's return probability.

## Scorecard

| # | Prediction | Outcome | Score |
|---|---|---|---|
| 1 | No bath: R = 1 at every Δ | Under the operational K-flip as first defined: R fell to 0.044 off resonance. Under the corrected echo: R = 1 ± 2×10⁻¹⁵ at all 41 detunings | **wrong as written** (definition error), corrected, then passes |
| 2 | One record mode: R oscillates in g·t, never settles | R vs g: 1.00, 0.85, 0.50, 0.16, 0.00, 0.06, 0.21, 0.29, 0.23, 0.09, 0.00, …, 0.89 | confirmed |
| 3 | Dense bath: R = exp(−Γ_eff t), Γ_eff = Γ × absorber occupation | Monotone decay; per-leg rate/Γ = 0.52, 0.48, 0.52 at t = 1, 3, 10 on resonance (occupation 0.5); but the total exponent is 2Γ_eff t, because the echo leg leaks too | confirmed in form; **constant wrong by 2** (bookkeeping) |
| 4 | Location: crossover in Δ/K centred near 1 (factor 2), drifting outward with Γt | Rate-based midpoint Δ/K = 1.3–2.0 (mean 1.6); analytic occupation half-point 2.0; fixed-t midpoint drifts 1.7 → 2.6 → 5.1 as Γt goes 0.15 → 2 → 10 | confirmed, with the convention stated below |
| 5 | Width: order one in Δ/K, not K/ω | Relative width 0.8–1.5 (fixed t), 1.1–1.6 (rate-based); ω cannot appear | confirmed |
| 6 | No share threshold; recoverability degrades continuously | Continuous in Γ_eff t at every Δ; no switch anywhere | confirmed |
| 7 | No bandwidth dependence at fixed Γ | B = 20, 40, 80: R differs by ≤ 0.001 | confirmed |

Two of seven predictions were wrong in a stated detail; both errors were mine and both
are recorded. Neither changes the physics conclusions, but the first changed the
observable, and that is the more important lesson of the run (below).

## Findings

### F1. The operational reversal and in-principle recoverability are different quantities

Flipping the capture coupling alone, which is the reversal an experimenter has, does not
reverse an off-resonant capture even with no record channel at all: the detuning keeps
running forward, the {photon, absorber} rotation is about a tilted axis, and the flipped
coupling tilts it the other way instead of undoing it. The 576-state model's README said
this ("a detuning left running through the pulse is never undone"), and its return helper
refuses detuned returns for the reason. I wrote prediction 1 as if the operational flip
were the in-principle reversal. It is not. Paper 2's cut is about in-principle
recoverability (§4.1), which is the echo with an untouched environment; the K-flip is a
weaker laboratory quantity that mixes in the detuning's non-reversal. Paper 2 should say
which it means, and any experiment that claims to locate the cut by a reversal protocol
must separate the two. Both are on record in `results.json` (`R_echo`, `R_op`).

### F2. One record mode is not a bath; sixteen are not either on these times

N = 1 gives coherent exchange, oscillatory and never settling (prediction 2), which is the
576-state model's non-monotone return (0.83 → 0.09 → 0.25). N = 4 leaks nothing at all: its
modes sit at ±6.7 and ±20, individually off resonance. N = 16 has recurrence time
2πN/B = 2.5 and shows recurrences at t ≥ 3. N = 64 (recurrence 10) agrees with N = 256 to
0.005 at t ≤ 3 and not at t = 10. N = 256 (recurrence 40) is the continuum for every
time used. *Consequence for the program:* the existing 576-state model, with one record
qubit per absorber, cannot exhibit an irreversible step of any kind, only coherent
exchange with the record; a many-mode record channel is a requirement for testing Paper 2,
not a refinement.

### F3. The location claim survives in the smallest exact model

With a dense record channel, recoverability leaks at a rate equal to Γ times the fraction
of the time the excitation spends on the absorber, per leg. That fraction is the two-level
occupation 2K²/(Δ² + 4K²), whose half-point is Δ = 2K, the resonant Rabi frequency. The
measured rate-based midpoint is Δ/K = 1.3–2.0 across Γ = 0.05–1.0 and t = 3–10, pulled
inward at the largest Γ because the record channel broadens the absorber. In Paper 2's
terms: κ_ret = Δ, and the crossover sits where κ_ret equals the coupling's
population-transfer rate. If Paper 2's K is that rate (as the Adler K is a rate of phase
pull), κ_ret/K = 1 holds to within a factor 1.6; if it is the matrix element, the
location is 2 to within the same factor. Either way the claim's content, that the cut
sits where the deficit-induced return rate balances the coupling, is what the model
shows. The midpoint read from R at a fixed observation time drifts outward with Γt, from
1.7 to 5, exactly because R = exp(−2Γ_eff t) reaches a given value at smaller occupation
when Γt is large; the location is a statement about rates, and Paper 2 should say so.

### F4. The width claim is out of scope for a linear absorber, and this fixes what stage 2 must be

The crossover's relative width is of order one in every run (0.8–1.6), because the linear
absorber's occupation is a Lorentzian in Δ of width 2K. Nothing in a rotating-wave model
contains the carrier frequency, so w = K/ω cannot appear, and did not. This is not a
falsification of Paper 2's width claim; it is a scope statement: the sharp layer
(10⁻⁶ for atomic lines, 10⁻² for solids, Paper 2 §3.3) is not a property of capture plus
an irreversible record channel. If it exists it belongs to a nonlinear, self-sustaining
absorber with counter-rotating terms, where the Adler tongue has a sharp edge. The
stage-2 model is therefore fixed: a limit-cycle absorber (not a two-level system) with a
many-mode record channel and no rotating-wave approximation, and the test is whether the
crossover width scales as K/ω as ω/K is varied at fixed K, Δ, Γ. *Prediction on record
now, for that stage:* counter-rotating terms alone (the quantum Rabi model) will shift the
location by the Bloch–Siegert amount ∝ K²/ω and not sharpen the width; sharpening, if it
occurs, requires the limit cycle.

### F5. Completion's ordering holds; its sharpness is not shown

Capture is reversible in principle (F1's corrected calibration) and the record channel is
where irreversibility enters (F2, F3), which is Paper 2's ordering. Recoverability
degrades continuously with Γ_eff t at every detuning; there is no switch at any
occupation, hence no analogue of "lock completion" in a linear absorber. Same scope
statement as F4.

### F6. The bath is memoryless on this grid

R is independent of the record bandwidth at fixed Γ to 0.001 (prediction 7), so the
golden-rule regime holds and the E-16 Markov ratio does not enter here. It would at
B ≲ Γ, K, which is outside the physical regime for any detector in Paper 2's table.

## Non-claims

- Nothing here tests Paper 2's numerical table of layer widths; the model cannot see ω.
- Nothing here tests selection among several absorbers; there is one absorber and no
  competition, no Born weight, no exclusivity.
- The record channel is a linear bath of modes at the absorber's own energy scale; a real
  record (phonons, an avalanche) has structure this model omits.
- "In-principle recoverability" is defined as the echo with the environment untouched; a
  definition that lets the environment be reversed gives R = 1 always (the exact global
  inverse of the 576-state model), and a definition that reverses only the coupling gives
  the K-flip numbers. The physics claim depends on which is meant, and F1 says Paper 2
  must choose.

## What this changes in Paper 2 (proposed, not applied)

1. State recoverability as the echo with an untouched environment, and note that the
   operational coupling-flip is a different, weaker quantity (F1).
2. State the location claim as a rate balance, κ_ret against the coupling's
   population-transfer rate, and note that a fixed-observation-time reading drifts (F3).
3. Restrict the width claim w = K/ω to nonlinear, self-sustaining absorbers, and say that a
   linear absorber with a record channel has a crossover of relative width order one (F4).
4. Say that a single record degree of freedom gives coherent exchange, not a cut; the cut
   needs a dense record channel, and this is a physical requirement on detectors (F2).

## Correction, 2026-09-04, logged before the Paper 2 edits were applied

**F4 and proposed edit 3 misread Paper 2's width.** Paper 2 §3.1 defines w = K/ω as the
layer's extent in *share*: the deficits ΔE ≲ ħK, that is 1 − s ≲ K/ω. It is not a
relative width in κ_ret/K. A layer of share width K/ω, converted to the deficit-rate
variable by ΔE = ħκ_ret, is a crossover of relative width of order one in κ_ret/K, which
is precisely what this test measured (1.1–1.6 rate-based; 25–75% points at κ_ret/K ≈
1.2–3). So the width claim is *not* out of scope for the linear absorber: the test is
consistent with it and supplies the prefactor. The fact "ω cannot appear in a
rotating-wave model" stands; the inference drawn from it was wrong.

What remains open is a different question, and Paper 2 itself poses it (§3.1: no single
continuous model yet spans both sides and exhibits the bifurcation at κ_ret/K = 1):
whether the recoverability crossover is smooth, as here for a linear absorber, or sharp,
as Figure 1(a)'s winding observable is for a self-sustaining oscillator. Stage 2 is
redefined around that question in `PREDICTIONS_STAGE2.md`; the prediction already on
record for counter-rotating terms (a Bloch–Siegert shift ∝ K²/ω, no sharpening) is kept
and tested there. Edit 3 is applied to Paper 2 in corrected form: state what the width is
a width of, and that the on/off of Figure 1(a) is a different observable from the
recoverability crossover.
