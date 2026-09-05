# Gated energy race on peaked spectra — predictions, fixed before running

*2026-09-04. Written before `energy_race_spectra.py` was run, at the sponsor's instruction
("Run the gated energy race on peaked spectra"). Context: with deriving the Born rule no
longer required, the sponsor asked whether Adler synchronization is compatible with Born
selection when commitment is put in as a memoryless hazard linear in absorbed energy. The
gated energy race showed it is, on the flat spectrum (exponent 2.16 [2.14, 2.19]; the
un-gated control gave 1.05). The compatibility rests on the tongue factor — the fraction of
clocks inside |Δ| < K, linear in K for a flat spectrum wider than the coupling — supplying
the second power of K on top of the locked absorption rate, which is linear in K. This run
tests what happens when the spectrum is narrower than the coupling.*

## The claim under test

On a spectrum of detunings ρ(Δ), the eligible fraction is f(K) = ∫_{|Δ|<K} ρ(Δ) dΔ. The
race's probability of channel A scales as K_A^p with p the fitted exponent of
P_A/(P_A+P_B) = K_A^p/(K_A^p + K_B^p). If the hazard is linear in absorbed energy and the
absorbed power of a locked clock is K cos θ* (θ* the locked phase), then
P_A ∝ f(K_A) × K_A × ⟨cos θ*⟩, and:

- flat spectrum, half-width 3 ≫ K: f ∝ K, so p ≈ 2 (measured 2.16);
- Gaussian spectrum of width σ: f(K) = erf(K/σ√2), linear for K ≪ σ and saturating for
  K ≫ σ; the fitted p falls from ≈ 2 toward 1 as σ falls below the couplings in play
  (K_A = 2 cos φ, K_B = 2 sin φ, so K ranges 0–2 across the angle grid);
- delta spectrum (every clock at Δ = 0): f = 1 and cos θ* = 1 for every K, so p = 1.

## Predictions

1. **Flat, half-width 3 (the control): p = 2.16 ± 0.05**, reproducing the record.
2. **Gaussian σ = 2: p between 1.9 and 2.2.** The couplings 0–2 sit mostly inside the
   linear part of erf.
3. **Gaussian σ = 1: p between 1.6 and 1.9.** Partial saturation for the larger couplings.
4. **Gaussian σ = 0.5: p between 1.3 and 1.6.**
5. **Gaussian σ = 0.25: p between 1.05 and 1.3.**
6. **Delta at Δ = 0: p = 1.00 ± 0.05.** All clocks lock at cos θ* = 1; the hazard is
   linear in K; the second power is gone.
7. **Monotone.** p decreases monotonically with decreasing σ across the sequence.
8. **Deviance.** At σ ≤ 0.5 the Born comparator (p = 2) is rejected by the same binomial
   deviance test that accepted it on the flat spectrum, and the linear comparator (p = 1)
   is accepted at the delta spectrum.

## What would count as what

- Predictions 1, 6, 7 confirmed: the synchronization-plus-golden-rule mechanism is
  Born-compatible only for a substrate whose detuning spread exceeds the coupling. Since
  atomic-line absorbers (spread ≪ coupling in the relevant sense) obey Born, the mechanism
  cannot be the universal substrate; its compatible domain is broadband absorbers. This
  is the risk stated to the sponsor before the run.
- Prediction 6 refuted (p stays near 2 at the delta spectrum): the second power of K has a
  source other than the tongue factor, and the analysis of where the square comes from is
  wrong; the run's own numbers would say where.
- Predictions 2–5 wrong in their brackets but 7 confirmed: the trend is right and the
  saturation scale is not erf(K/σ√2); recorded as such.

## Grid

The energy race's frozen grid and pulse (16 clocks per channel, raised-cosine pulse of
duration 4, K = 2, noise D = 0.08, hazard scale c as in the record's gated run), mode
"gated", hazard exponent m = 1, no hazard memory; detuning sets: flat midpoints of ±3;
Gaussian quantile sets (16 midpoint-probability quantiles) with σ = 2, 1, 0.5, 0.25; the
delta set (16 clocks at Δ = 0). Trials per angle and channel as in the record's gated run;
exponent by profile likelihood; deviance against the p = 1 and p = 2 comparators.
