# Stage 2 — results, scored against `PREDICTIONS_STAGE2.md`

*2026-09-04. Both scripts exact or deterministic; no statistical error. Part A: quantum Rabi
absorber (no rotating-wave approximation) with a 128-mode record channel, 53 s. Part B:
Paper 2's own injected Stuart–Landau oscillator with a record channel and an optional
counter-rotating drive, 16 s. Raw output in `stage2_rabi_output.txt` and
`stage2_stuart_landau_output.txt`; data in the two `stage2_*_results.json` files.*

## Scorecard

| # | Prediction | Outcome | Score |
|---|---|---|---|
| A1 | No channel: echo returns 1; ω/K = 64 matches the rotating-wave reference to 3 % | R = 1.000000000000 at every Δ for ω/K = 8 and 64; at ω/K = 64 the half-width matches the reference to 0.04 % and the centre to 0.02 K | confirmed |
| A2 | Bloch–Siegert: centre c = −s K²/ω, s in [0.5, 2], negative | s = 1.10, 1.11, 1.21, 1.51 at ω/K = 64, 32, 16, 8 (Γ = 0.2); 1.27–1.72 at Γ = 0.5; all negative | confirmed |
| A3 | No sharpening: half-width within 10 % down to ω/K = 16, 25 % at 8 | h = 1.598 (RWA), 1.599, 1.604, 1.632, 1.580 at ω/K = 64, 32, 16, 8: within 2 % everywhere | confirmed |
| A4 | Truncation n ≤ 3 vs 4 differ by < 10⁻³ | differences 1.3 × 10⁻⁴, 4.9 × 10⁻⁵, 7.3 × 10⁻⁵ | confirmed |
| B1 | Noiseless winding onset between g = 0.243 and 0.35, noise moves it < 0.02; Appendix A's noise attribution wrong | 50 % onset g = 0.355 (D = 0) and 0.352 (D = 10⁻⁴); Hopf of the forced fixed point at 0.241 (analytic) | confirmed |
| B2 | Stored energy continuous, at most a kink; < 30 % change per 0.1 in g | continuous, kinked: slope 0.004 below the onset, 1.1 above; but up to 70 % change per 0.1 in g at the onset | confirmed in substance; **bound wrong** |
| B3 | Counter-rotating drive changes nothing beyond 10⁻² (ω_d = 40) or 5 × 10⁻² (10) | identical to three decimals at both; onset identical (0.355) | confirmed |
| B4 | Record channel Γ_rec = 0.1 shifts the onset by ≈ 0.05, no change in sharpness | onset 0.355 → 0.397; slopes 0.016 and 1.12; energy smooth | confirmed |

Seven of eight confirmed; one numerical bound was wrong and is recorded.

## Findings

### S1. The carrier frequency is a shift, not a width

Removing the rotating-wave approximation from the stage-1 absorber lets ω into the
dynamics, and it enters exactly as the Bloch–Siegert displacement of the resonance: the
centre of the leak-rate curve moves to negative detuning by s K²/ω with s → 1.1 as
ω/K → ∞, while the half-width of the crossover stays at 1.6 K to within 2 % from
ω/K = 64 down to 8. Paper 2's ω therefore belongs where §3.2 (v0.4) now puts it, in the
conversion of the layer from the deficit-rate variable to share, and nowhere else. The
counter-rotating drive on the classical oscillator (Part B, ω_d = 40 and 10) confirms the
same thing from the other side: no number changes to three decimals.

### S2. In Paper 2's own model the recoverability-relevant observable is continuous across the threshold, with a kink at the running onset and no signature at the Hopf

The stored energy of the injected Stuart–Landau oscillator, which is what a record
channel leaks (stage 1: leak rate = Γ × occupation), sits at the field-set value
F²/Δ² = 0.1225 from g = −1 through the free oscillator's Hopf point g = 0 and through the
Hopf bifurcation of the forced fixed point at g = 0.241, with slope 0.004 per unit gain;
it departs from that value only at the winding onset near g = 0.355, and thereafter
rises with slope 1.1, tracking the oscillator's own limit-cycle energy g. The transition is
continuous with a corner: no jump. The winding rate, by contrast, is exactly zero below
the onset and 0.96 by g = 0.40. So Paper 2's three regimes appear in one model with one
energy observable: *slaved* (g < 0: linear response), *engaged* (0 < g < 0.355: a free phase
exists but is entrained, and the stored energy is still the field's), *running* (the
site's own gain sets the energy). The energy bookkeeping changes hands from field to site
at the running onset, not at the Hopf, and does so smoothly. This is the stage-2 answer to
what stage 1 left open: a self-sustaining absorber does not make the recoverability
crossover sharp; it makes it kinked. Only the phase-winding observable switches.

### S3. Paper 2's Figure 1 caption and Appendix A misattribute the onset to noise

With the noise switched off entirely, the 50 % winding onset is at g = 0.355; with the
paper's noise D = 10⁻⁴ it is at 0.352. The onset near 0.35 is deterministic. The Adler
estimate g = (F/Δ)² = 0.1225 assumes weak injection, F ≪ √g, which is false at that point
(F/√g = 1). The locked state is the forced fixed point F² = u[(g − u)² + Δ²]; a saddle-node
would need (g − u)(g − 3u) = −Δ², impossible for g < √3; the fixed point instead loses
stability by a Hopf bifurcation at u = g/2, i.e. g_H = 0.241, and the winding turns on when
the newborn cycle has grown to encircle the origin, near 0.35. Corrected in Paper 2 v0.4
(Figure 1 caption, Appendix A) at the sponsor's word to apply the test's edits; this
correction is beyond the four listed and is flagged as such.

### S4. A record channel shifts the onset and changes nothing else

Γ_rec = 0.1 moves the 50 % onset from 0.355 to 0.397 and the below-onset energy slope
from 0.004 to 0.016; the kinked shape and the winding switch are unchanged. The record
channel is a damping on the site, and its leak Γ_rec⟨|a|²⟩ is as smooth in g as the
stored energy.

## Non-claims

- Part B is Paper 2's classical analogy with gain and saturation put in by hand; its
  κ_ret for g < 0 is a damping, which Paper 2 itself says the physical κ_ret is not. It
  tests the sharpness structure of the paper's own model, not a detector.
- Part A's absorber is still linear (a two-level system); it tests whether ω enters, not
  whether a self-sustaining absorber sharpens. Part B answers the latter in the classical
  model only. A quantum self-sustaining absorber with a record channel remains the open
  problem Paper 2 §9 names.
- The location κ_ret/K = 1 is not tested in Part B, because in the forced sub-threshold
  oscillator K is set by the response itself (κ_ret/K = −g/√(g² + Δ²) < 1 always); this
  is the circularity Paper 2 §3.1 flags, and Part B does not resolve it.
- Part A's photon truncation at n ≤ 3 and the record channel's single-excitation
  truncation are checked at ω/K = 8 (A4) and not below it.

## What this changes in Paper 2

Applied (v0.4, beyond the four edits, flagged): the Figure 1 caption and Appendix A
correction of S3.

Proposed, not applied: a §4.1 refinement from S2. The table's "lock engagement" row
(free phase exists, entrained) leaves the stored energy, and hence recoverability,
exactly where the field set it; the handover of energy bookkeeping from field to site
happens at the *running* onset, continuously, with a kink. If the cut is where
in-principle recoverability ends, the engaged regime is on the recoverable side by the
energy criterion, and the row's "recoverable in principle — the engaged lock can still
dissolve" is now supported by a number (slope 0.004) rather than an argument.
