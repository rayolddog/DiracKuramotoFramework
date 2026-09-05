# Gated energy race: the broadband, adiabatic limit — predictions, fixed before running

*2026-09-04, evening. Prompted by the sponsor's question whether removing the absorbing
atom's wave function (its discrete resonance) and the vacuum's contribution makes the
result "more broadband". Answering it required re-reading the record, which changed a
claim: the record's own stationary-drive variant gives p = 2.09 [2.06, 2.11] on the
16-clock grid whose stationary rate sum scales as K^1.91, and the pulsed flat grid gives
2.16–2.21. For a continuous flat density the tongue's rate sum is the semicircle,
∫_{−K}^{K} √(K² − Δ²) dΔ = πK²/2, exactly K². So the flat grid's excess above 2 is not a
property of the broadband limit; it is grid discreteness (−0.09), the locking transient
(+0.2), and the pulse. My statement of the same day that "Born is exact at one width
only, a tuned coincidence" (RESULTS.md finding 2; single paper §4.2) conflated the two and
is corrected after this run, whichever way it goes. This run measures the limit directly.*

## The claim under test

In the broadband (spread ≫ K), adiabatic (drive slow against locking, K·T ≫ 1), continuum
(clock spacing ≪ K) limit, the gated energy race's channel absorption is the semicircle
rate sum, ∝ K² exactly, so the exponent is 2.00. The deviations seen on the record are
finite-grid, finite-window and finite-pulse effects, each with a sign: discreteness lowers
the exponent (1.91 on 16 clocks), the locking transient raises it (the weak channel loses
proportionally more of a short window), and a fast pulse raises it further.

## Predictions

1. **Grid density at stationary drive.** Stationary K, window as the record's, flat ±3:
   16 clocks gives p = 2.09 ± 0.03 (reproducing the record); 64 clocks gives p between
   2.00 and 2.08 (discreteness removed, transient remains); the rate-sum exponent of the
   64-clock grid is within 0.03 of 2.
2. **Window length at stationary drive, 64 clocks.** Lengthening the window from the
   record's 4 to 8, 16 and 32 (hazard scale reduced in proportion so the efficiency stays
   comparable) brings p down monotonically toward 2.00, within 0.03 of 2 by window 32.
   The locking transient is a fixed cost that a longer window amortizes.
3. **Pulse duration, 64 clocks, raised-cosine pulse.** Durations 2, 4, 8, 16 (peak K fixed
   at 2): p falls monotonically toward 2 as the pulse lengthens, from above 2.2 at
   duration 2 to within 0.05 of 2 at duration 16.
4. **Fast pulses do not go linear.** At duration 1 (K·T = 2 at peak) the exponent stays
   above 2, not below: the impulsive regime raises the exponent, because locking favours
   the stronger channel disproportionately when there is little time to lock. If instead
   the exponent falls below 2 at short pulses, the impulsive limit has its own law and
   this prediction is wrong.
5. **Noise.** D = 0 versus 0.08 at 64 clocks, stationary: within 0.03 of each other
   (the record: 2.17 vs 2.16 pulsed).

## What would count as what

- Predictions 1–3 confirmed: the broadband adiabatic limit is Born-exact by the
  semicircle identity, and the earlier "tuned coincidence" statement is corrected to: the
  mechanism is Born-exact in the broadband, adiabatic, continuum limit and deviates on
  either side for a stated reason — narrow spectra (deficit, previous run), fast or short
  drives and coarse grids (excess). The sponsor's question is then answered: removing the
  atom's discrete resonance in favour of a band makes the substrate broadband and moves
  the mechanism into its Born-exact domain, provided the drive is slow against locking.
- Prediction 2 or 3 refuted (p stays ≥ 2.05 at long windows and pulses on the dense
  grid): the excess is not a transient and the semicircle argument misses something in
  the race; the "tuned" statement stands.
- Prediction 4 refuted: the impulsive limit is a separate regime to be characterized;
  single-photon absorption on atoms (K·T ≪ 1) would then be outside the mechanism's
  Born domain from the other side.

## Grid

Gated mode, hazard linear in absorbed energy (m = 1), K = 2, angles as the record, flat
±3 detunings with 16 and 64 clocks, D = 0.08 (and 0 once), 10,000 trials per angle and
channel; stationary drive with windows 4, 8, 16, 32 (hazard scale c = 0.5, 0.25, 0.125,
0.0625); raised-cosine pulses of duration 1, 2, 4, 8, 16 (c scaled as 4/T from the
record's c = 1 at T = 4). Exponent by profile likelihood; deviance against Born.

## Addendum, written after the eleven-configuration run and before the check below

The run refuted predictions 2 and 3: the stationary exponent rose with window length
(2.08, 2.12, 2.17, 2.15 at windows 4, 8, 16, 32 on 64 clocks) and the pulsed series sat
flat (2.10, 2.13, 2.12, 2.14, 2.16 at durations 1–16). The excess above 2 is intrinsic to
the race, not a transient. Two candidate causes remain: noise-driven escape of weakly
locked clocks across the tongue edge (a steady-state effect that grows with time and
falls on the weak channel, whose relaxation rates are smaller), or a deterministic
feature of how energy accumulates (the locking delay, the signed accumulation before
lock). The record's noise-off run at window 4 (2.07 against 2.08) says noise is not the
cause at short windows, where the transient dominates.

**Prediction for the check (stationary, window 16, 64 clocks, D = 0, 8,000 trials):**
the rise with window length is noise-driven, so with the noise off the exponent falls
back to within 0.03 of the window-4 noise-off value, 2.07 — i.e. 2.04–2.10 — and not to
2.00; the residual is the deterministic locking structure. If instead the exponent stays
at 2.15 or above with the noise off, the excess is deterministic throughout and the
noise plays no role at any window.

## Second addendum, after the noise-off check and before the small-hazard run

The check gave 2.16 [2.12, 2.19] with the noise off at window 16, refuting the addendum's
prediction: the excess is deterministic throughout. It also showed why the window series
never reached the steady state. With the hazard c·E and a channel energy growing as
R·t, the survival is exp(−cRt²/2) and the typical commitment time is t* = √(2/(cR)).
Scaling c as 4/T gives t* ≈ √(T/R), and with R of order 40 for the strong channel on 64
clocks that is about 0.6 time units at every window used — inside the locking transient
(lock times of order 1/√(K² − Δ²), from 0.5 upward), and independent of the window, which
is why the exponent plateaued. The windows were long; the races were not. The channel
energy exponent, measured at the window's end, did fall toward 2 (2.20 → 2.11 stationary;
2.06 with the noise off), which is the semicircle asserting itself in the steady state
while the outcome was still being decided in the transient.

**Prediction for the small-hazard run (stationary, window 32, 64 clocks, D = 0.08,
5,000 trials): pushing commitment past the transient brings the exponent down toward the
steady-state energy exponent.** At c = 10⁻³ (t* ≈ 7): p between 2.02 and 2.10. At
c = 2.5 × 10⁻⁴ (t* ≈ 14): p between 2.00 and 2.06, with some unresolved trials. If p stays
at 2.15 with commitment at t* ≈ 14, the excess is not the transient either and this
analysis has no explanation for it.

## Third addendum, before the noise-off check at the longest commitment time

At the sponsor's word, the separating run named in RESULTS.md: stationary, window 32,
64 clocks, D = 0, c = 2.5 × 10⁻⁴ (commitment near 14 time units), 5,000 trials. It
separates the noise-reduced absorbed power of weakly locked clocks (a steady-state,
noise-dependent effect) from the deterministic candidates (pre-lock signed accumulation,
the closest-phase leak into the Poisson race). The evidence so far: with the noise off
at commitment time 0.6 the exponent was unchanged (2.16 vs 2.17), and with the noise on
the exponent moved only from 2.15 to 2.13 as the commitment time went from 7 to 14.

**Prediction: the residual is deterministic.** With the noise off at commitment time 14,
p stays between 2.09 and 2.16 (within the noise-on value's interval, 2.13 [2.09, 2.17]),
while the channel-energy exponent at the window's end falls to 2.02–2.06 (the
noise-off value at window 16 was 2.06). If instead p falls to 2.06 or below, the residual
is the noise's doing in the steady state and the deterministic candidates are cleared.
