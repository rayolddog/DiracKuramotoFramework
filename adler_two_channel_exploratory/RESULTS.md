# Two-channel Adler race — exploratory results (2026-09-02)

**Read the status line first.** Every raw ledger behind these numbers carries the package's
own `numerical_gate = "diagnostic_only"`, because the ticket-07 frozen numerical budget of
`adler_born_two_channel/` is not met. These are reduced-budget diagnostics (16 or 32 clocks
per channel against the frozen 64; timestep 2⁻⁷ or 2⁻⁸ against the frozen 2⁻⁹; 200–300
trials per cell against the 2 406 the power calculation asked for). They are labelled
`pilot` and can never enter a production estimate. Nothing here is a Born-rule derivation,
the first-winner stop is imposed bookkeeping, and a "commitment" is a dwell rule, not a
click.

## The question and the construction

Does direct noisy Adler phase dynamics, applied to two competing populations of absorber
clocks while a common photon-pulse envelope opens and closes their Arnold tongues, produce
first-commitment frequencies proportional to the **square** of their amplitude-linear
peak couplings? Peak couplings K_A = K cos φ, K_B = K sin φ with K = 2.0 and φ the input
polarization angle. The frozen ticket-07 physics otherwise: support ±3, phase diffusion
0.08, lock tolerance 0.35 rad, fixed dwell 0.5, raised-cosine pulse of duration 4.0.

The race is the pairwise minimum of two independent one-channel raw races
(`race_driver.py`); pairing and comparison happen in a separate process (`analysis.py`)
that opens the closed ledgers through the package's gate and is the only place the
analytic prediction is loaded. Estimand: the unconstrained exponent p in
P_A/(P_A+P_B) = K_A^p/(K_A^p+K_B^p), by maximum binomial likelihood with a
profile-likelihood 95 % interval. Comparators: p = 1 (amplitude-linear), p = 2 (Born,
cos²φ), strongest wins, the Poisson race on the bare relaxation-rate sum over the exact
grid (quadratic on these grids: exponent 1.92 at N = 16, 1.99 at N = 64), and the Poisson
race on the eligible-clock count (linear: 0.94–0.96). Each is scored by binomial deviance
against the resolved counts.

## Main sweep — N = 16, dt = 2⁻⁷, 300 trials per cell, 9 angles (`results_main_N16_dt7.csv`)

| φ | K_A | K_B | A | B | tie | unres. | P_A [Wilson 95 %] | Born | linear | rate-sum | width | commit A/B |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10 | 1.970 | 0.347 | 274 | 25 | 1 | 0 | 0.916 [0.879, 0.943] | 0.970 | 0.850 | 0.965 | 0.833 | 1.00/0.27 |
| 20 | 1.879 | 0.684 | 251 | 49 | 0 | 0 | 0.837 [0.791, 0.874] | 0.883 | 0.733 | 0.877 | 0.714 | 1.00/0.63 |
| 30 | 1.732 | 1.000 | 220 | 79 | 1 | 0 | 0.736 [0.683, 0.782] | 0.750 | 0.634 | 0.746 | 0.625 | 1.00/0.77 |
| 40 | 1.532 | 1.286 | 169 | 130 | 1 | 0 | 0.565 [0.509, 0.620] | 0.587 | 0.544 | 0.599 | 0.571 | 0.98/0.95 |
| 45 | 1.414 | 1.414 | 140 | 158 | 1 | 1 | 0.470 [0.414, 0.526] | 0.500 | 0.500 | 0.500 | 0.500 | 0.97/0.98 |
| 50 | 1.286 | 1.532 | 136 | 160 | 4 | 0 | 0.460 [0.404, 0.516] | 0.413 | 0.456 | 0.401 | 0.429 | 0.93/0.98 |
| 60 | 1.000 | 1.732 | 74 | 223 | 3 | 0 | 0.249 [0.203, 0.301] | 0.250 | 0.366 | 0.254 | 0.375 | 0.78/1.00 |
| 70 | 0.684 | 1.879 | 43 | 256 | 1 | 0 | 0.144 [0.109, 0.188] | 0.117 | 0.267 | 0.123 | 0.286 | 0.56/1.00 |
| 80 | 0.347 | 1.970 | 25 | 274 | 1 | 0 | 0.084 [0.057, 0.120] | 0.030 | 0.150 | 0.035 | 0.167 | 0.27/1.00 |

**Fitted exponent p = 1.56, 95 % [1.44, 1.69].** Symmetric control (45°): 0.470 [0.414,
0.526], consistent with ½. Ties 13/2700 = 0.5 %; unresolved 1/2700.

Deviance against the resolved counts (9 cells; a fixed comparator is χ² with 9 dof):

| comparator | deviance |
|---|---|
| linear (p = 1) | 102.6 |
| **Born (p = 2)** | **51.9** |
| strongest wins | 36 968 |
| rate-sum race | 42.7 |
| width-only race | 133.6 |
| fitted p = 1.56 | 13.1 (8 dof) |

Both predeclared families are rejected: the direct events are neither amplitude-linear nor
amplitude-squared. The curve is flatter than Born at both extremes (10°: 0.916 against
0.970; 80°: 0.084 against 0.030) and near 45°. In the plan's interpretation matrix this is
the row *"Quadratic analytic flux, nonquadratic direct outcomes — locking relaxation is
not the detector commitment hazard under the chosen microscopic rule."*

## Sensitivities — 3 angles (20°, 45°, 70°), 200 trials per cell

| run | change | p [95 %] | Born dev. | rate-sum dev. | linear dev. | unresolved | P_A(45°) |
|---|---|---|---|---|---|---|---|
| main (subset) | — | 1.56 [1.44, 1.69] | — | — | — | 0.0 % | 0.470 |
| dt8 | dt = 2⁻⁸ | 1.42 [1.18, 1.67] | 21.4 | 18.1 | 14.2 | 0.3 % | 0.477 |
| n32 | N = 32 | 1.50 [1.26, 1.76] | 13.7 | 13.0 | 16.6 | 0.0 % | 0.507 |
| dw025 | dwell 0.25 | 1.42 [1.18, 1.67] | 22.6 | 19.2 | 15.3 | 0.0 % | 0.566 |
| **dw100** | **dwell 1.0** | **1.95 [1.66, 2.27]** | **1.5** | **1.4** | 48.7 | **7.3 %** | 0.539 |
| df002 | diffusion 0.02 | 1.38 [1.15, 1.63] | 24.7 | 21.1 | 13.0 | 0.0 % | 0.447 |
| df032 | diffusion 0.32 | 1.66 [1.39, 1.95] | 6.2 | 4.6 | 25.9 | 8.7 % | 0.528 |
| pu2 | pulse 2.0 | 1.68 [1.40, 1.97] | 7.4 | 6.1 | 27.1 | 14.2 % | 0.441 |
| pu8 | pulse 8.0 | 1.38 [1.15, 1.63] | 22.4 | 18.8 | 11.1 | 0.0 % | 0.510 |

(3 cells; deviances of fixed comparators are χ² with 3 dof.)

**Numerics.** Halving the timestep (dt8) and doubling the population (n32) leave the
exponent inside the main sweep's interval; ties stay below 1 %. Within this reduced
budget the exponent is not a discretisation artefact and not a population-count artefact.

**Physics.** The exponent is **criterion-dependent**. It rises monotonically with the
fixed dwell (0.25 → 0.5 → 1.0: 1.42 → 1.56 → 1.95; the 0.25 and 1.0 intervals do not
overlap) and it rises when the pulse is shortened (8.0 → 4.0 → 2.0: 1.38 → 1.56 → 1.68)
and when the noise is strengthened (0.02 → 0.08 → 0.32: 1.38 → 1.56 → 1.66). The three
knobs have one thing in common: each makes commitment *harder*, and the unresolved
fraction climbs from zero to 7–14 % exactly where p rises. At dwell 1.0 the three-angle
cells are fitted by the rate-sum race (deviance 1.4) and by Born (1.5), while linear is
rejected (48.7) — but see the dwell extension below: on the full nine-angle sweep at
dwell 1.0 the exponent is 1.78 [1.60, 1.96] and Born is still rejected. Reading: where
nearly every trial commits, the race is decided by which channel's fastest clock locks
first, and that scales with roughly K^1.4–1.5 — more than tongue width alone (K^1) but
less than width times rate (K^2). Where commitment is unreliable, surviving the dwell
selects for strongly contracting clocks, the rate factor enters more fully, and the
frequencies move toward the rate-weighted flux — but they do not reach it before the
efficiency collapses.

## Dwell extension — full sweep at dwell 1.0, and dwell 2.0

| run | dwell | angles | trials/cell | p [95 %] | Born dev. (dof) | rate-sum dev. | linear dev. | unresolved |
|---|---|---|---|---|---|---|---|---|
| dw025 | 0.25 | 3 | 200 | 1.42 [1.18, 1.67] | 22.6 (3) | 19.2 | 15.3 | 0.0 % |
| main | 0.5 | 9 | 300 | **1.56 [1.44, 1.69]** | 51.9 (9) | 42.7 | 102.6 | 0.0 % |
| dw100f | 1.0 | 9 | 200 | **1.78 [1.60, 1.96]** | 23.5 (9) | 19.0 | 113.0 | 7.4 % |
| dw200 | 2.0 | 3 | 200 | 1.71 [1.12, 2.40] | 6.0 (3) | 5.7 | 10.9 | **82.2 %** |

(`results_dw100f_N16_dt7.csv`; per-angle at dwell 1.0: 10° 0.974, 20° 0.839, 30° 0.785,
40° 0.600, 45° 0.429 [0.360, 0.502], 50° 0.367, 60° 0.265, 70° 0.132, 80° 0.084 against
Born 0.970, 0.883, 0.750, 0.587, 0.500, 0.413, 0.250, 0.117, 0.030.)

The exponent rises with the dwell — 1.42, 1.56, 1.78 — and each step is outside the
previous interval's centre by more than its half-width. It does not reach 2: at dwell 1.0
Born is rejected at nine cells (deviance 23.5, p ≈ 0.005), the residual sitting at the
80° cell (0.084 against 0.030) and at 45° (0.429, two sigma below ½). At dwell 2.0, 82 %
of trials produce no commitment at all and the exponent is undetermined [1.12, 2.40].
So the fixed-dwell race approaches the Born curve as the dwell lengthens, but the
efficiency collapses before it gets there.

Three interpretation-matrix rows are therefore triggered at once:

- *Fitted coupling exponent depends strongly on noise, dwell, or tolerance → the law is
  criterion-dependent, not universal.*
- *Coupling exponent changes with pulse duration → the proposed selection propensity is
  time-window dependent* (the "longer pulses mainly reduce unresolved trials" row is
  **not** what happened; the ratio moved).
- *Quadratic analytic flux, nonquadratic direct outcomes* at the frozen dwell.

## The inverse-coupling dwell — the plan's labelled positive control (run 2026-09-02, at JB's request)

The plan: *"An inverse-coupling dwell would preserve Adler scale similarity and make the
quadratic result easier to obtain. It would also make the selection criterion
amplitude-dependent. … It may be run later as a labeled positive control, never as the
primary result."* Implemented at the caller (`--dwell-mode inverse`): each channel's dwell
is 0.5 × √2 / K_chan, so the 45° symmetric cell keeps the frozen dwell 0.5 and the main
sweep's other inputs are unchanged. Strong-channel dwell at 10° is 0.36; weak-channel dwell
is 2.04. Nine angles, 300 trials per cell, N = 16, dt = 2⁻⁷ (`results_invdw_N16_dt7.csv`).

| φ | K_A | K_B | A | B | tie | unres. | P_A [Wilson 95 %] | Born | commit A/B |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 1.970 | 0.347 | 300 | 0 | 0 | 0 | 1.000 [0.987, 1.000] | 0.970 | 1.00/0.00 |
| 20 | 1.879 | 0.684 | 297 | 3 | 0 | 0 | 0.990 [0.971, 0.997] | 0.883 | 1.00/0.23 |
| 30 | 1.732 | 1.000 | 259 | 41 | 0 | 0 | 0.863 [0.820, 0.898] | 0.750 | 1.00/0.60 |
| 40 | 1.532 | 1.286 | 197 | 101 | 2 | 0 | 0.661 [0.606, 0.713] | 0.587 | 0.99/0.91 |
| 45 | 1.414 | 1.414 | 147 | 153 | 0 | 0 | 0.490 [0.434, 0.546] | 0.500 | 0.97/0.96 |
| 50 | 1.286 | 1.532 | 102 | 195 | 2 | 1 | 0.343 [0.292, 0.399] | 0.413 | 0.92/0.99 |
| 60 | 1.000 | 1.732 | 35 | 264 | 0 | 1 | 0.117 [0.085, 0.158] | 0.250 | 0.63/0.99 |
| 70 | 0.684 | 1.879 | 5 | 295 | 0 | 0 | 0.017 [0.007, 0.038] | 0.117 | 0.22/1.00 |
| 80 | 0.347 | 1.970 | 0 | 300 | 0 | 0 | 0.000 [0.000, 0.013] | 0.030 | 0.00/1.00 |

**Fitted exponent p = 3.81, 95 % [3.50, 4.15].** Deviance: linear 706, **Born 204**,
rate-sum 216, width 757, strongest wins 22 596, fitted 6.4 (8 dof). Ties 0.15 %;
unresolved 2 of 2700. Timestep check at 2⁻⁸ (three angles, 200 trials): p = 4.55 [3.71,
5.71], Born deviance 83 on 3 cells — the overshoot survives refinement. That check's
symmetric 45° cell came out 0.385 [0.320, 0.454] on 200 trials, 3.4σ below ½; a re-run
of the same cell on an independent stream with 300 trials gives 0.525 [0.469, 0.581]
(`results_invdw8b_N16_dt8.csv`), so the first reading was a fluctuation.

**The control does not produce Born. It overshoots it.** Making the dwell inversely
proportional to the coupling does not restore a coupling-squared law; it produces a law
near coupling to the fourth. The fixed dwell gives p ≈ 1.5 (too shallow); the inverse
dwell gives p ≈ 3.8 (too steep); the Born exponent lies between two choices of the
commitment criterion's amplitude dependence, and neither the amplitude-neutral choice nor
the scale-similar one lands on it. That is the plan's own falsification row — *"A
universal Born candidate must not require one finely tuned numerical criterion"* —
reached from both sides. The tuned interpolation (dwell ∝ K^−α with α between 0 and 1)
that would hit p = 2 is run below as a demonstration that such a criterion exists and of
how tuned it is; it is not a candidate mechanism.

## The tuned dwell — a demonstration, not a mechanism

Linear interpolation between α = 0 (p = 1.56) and α = 1 (p = 3.81) suggested α ≈ 0.2 for
p = 2; α = 0.25 was run, nine angles, 300 trials, N = 16, dt = 2⁻⁷ (`--dwell-mode power
--dwell-alpha 0.25`; each channel's dwell is 0.5 × (√2/K)^0.25, from 0.46 at K = 1.97 to
0.71 at K = 0.35; `results_tune25_N16_dt7.csv`).

| φ | P_A [Wilson 95 %] | Born | commit A/B |
|---|---|---|---|
| 10 | 0.973 [0.948, 0.986] | 0.970 | 1.00/0.22 |
| 20 | 0.873 [0.830, 0.906] | 0.883 | 1.00/0.45 |
| 30 | 0.747 [0.694, 0.793] | 0.750 | 0.99/0.77 |
| 40 | 0.593 [0.537, 0.647] | 0.587 | 0.99/0.90 |
| 45 | 0.497 [0.440, 0.553] | 0.500 | 0.96/0.98 |
| 50 | 0.442 [0.386, 0.498] | 0.413 | 0.95/0.99 |
| 60 | 0.281 [0.233, 0.334] | 0.250 | 0.80/1.00 |
| 70 | 0.093 [0.065, 0.132] | 0.117 | 0.53/1.00 |
| 80 | 0.030 [0.016, 0.056] | 0.030 | 0.20/1.00 |

**Fitted exponent p = 2.00, 95 % [1.84, 2.16]; Born deviance 4.7 on 9 cells; rate-sum
race 6.8; linear 220; width 261.** Every cell holds Born inside its Wilson interval.
Ties 0.3 %; unresolved 1 of 2700.

What this is: a one-parameter, amplitude-dependent commitment criterion that reproduces
the Born curve across the whole sweep at this budget. What it is not: a mechanism. The
parameter was chosen from the answer — one interpolation, one run, and it landed — and
the sensitivity dp/dα ≈ 2.3 means the criterion must be specified to α = 0.25 ± 0.07 to
stay inside the fitted interval. No physics in the model fixes a quarter-power dwell.
Under the plan's own rule (*"A universal Born candidate must not require one finely
tuned numerical criterion"*) this is the falsification row, now with the tuning
quantified. What it leaves open, and is worth saying: if some physical commitment rule
carried an effective K^−1/4 dependence for a reason of its own, this race would produce
Born. That is a lead for a different rule, not support for this one.

## Spectral controls — Experiment 7 (`spectral_driver.py`, `spectral_analysis.py`)

The raw boundary admits only a flat grid, so these densities were realised through the
package's public factories (`raw_one_clock_path` at chosen detunings, `PopulationIdentity`,
`ClockPopulation`, `race_one_channel`) with commit times recorded in exploratory CSVs, not
the closed ledger. Sixteen clocks per channel, five angles (10°, 30°, 45°, 60°, 80°), 200
trials per cell, frozen criterion; the flat density re-run through the same path as the
reference (`results_spectral_s1_N16_dt7.csv`). Comparators are computed on the same
detunings the race used.

| spectrum | detunings (positive half) | direct p [95 %] | rate-sum exp. | width exp. | dev. Born | dev. rate | dev. width | dev. linear |
|---|---|---|---|---|---|---|---|---|
| flat | 0.19, 0.56, 0.94, 1.31, 1.69, 2.06, 2.44, 2.81 | 1.51 [1.32, 1.71] | 1.91 | 0.97 | 22.2 | 17.0 | 45.5 | 34.4 |
| Gaussian σ = 1 | 0.08, 0.24, 0.40, 0.58, 0.78, 1.01, 1.32, 1.86 | 1.29 [1.13, 1.47] | 1.82 | 0.81 | 51.8 | 26.9 | 47.9 | 14.4 |
| Lorentzian γ = 0.75 | 0.07, 0.23, 0.40, 0.62, 0.91, 1.40, 2.47, 7.62 | 1.09 [0.95, 1.25] | 1.69 | 0.69 | 101.0 | 40.4 | 51.6 | 4.7 |
| central peak | 0.10, 0.25, 0.30, 0.75, 1.25, 1.75, 2.25, 2.75 | 1.01 [0.86, 1.16] | 1.48 | 0.36 | 131.5 | 39.2 | 85.5 | 4.6 |
| central notch | 0.56, 0.94, 1.31, 1.69, 2.06, 2.44, 2.60, 2.81 | 3.01 [2.62, 3.45] | 2.46 | 1.14 | 36.5 | **2.0** | 47.5 | 196.0 |

Ties ≤ 1 %; unresolved 0 except the notch (≤ 3 %).

**The direct exponent moves with the spectrum**, monotonically and in the same order as
both analytic comparators. The plan's falsification, that the events stay quadratic while
the flux changes, did not happen: the race is driven by the spectrum the tongue sweeps
through. But it is not driven by the rate-weighted flux. On the four spectra without a
threshold the direct exponent sits about one half power above the eligible-count
exponent, not one full power: 0.97 + ½ = 1.47 (measured 1.51), 0.81 + ½ = 1.31 (1.29),
0.69 + ½ = 1.19 (1.09), 0.36 + ½ = 0.86 (1.01). The race scales as **width times the
square root of the rate**. The notch is the exception that explains itself: no clock is
eligible until K exceeds 0.56, so the weak channel at 10° and 80° cannot commit at all and
the direct curve is a threshold, which the rate-sum race carries too (deviance 2.0) and
Born does not (36.5).

That half power is the one the tuned dwell supplied by hand. One candidate for it was
recorded as a prediction before the lock-tolerance numbers were opened: a locked clock's
stationary phase spread is √(D/r), so its probability of sitting inside a fixed band goes
as K^½ while the band is narrower than the spread and saturates once it is wider; the
exponent should then rise at tolerance 0.175 and fall toward the fastest-clock value near
1.4 at 0.70. The tolerance sweep scores that prediction next.

## Lock tolerance — Experiment 5, the last criterion knob (`results_tol*_N16_dt7.csv`)

Nine angles, 200 trials per cell, everything else at the frozen criterion.

| tolerance (rad) | p [95 %] | Born dev. (9) | rate-sum dev. | linear dev. | unresolved | ties | P_A(45°) |
|---|---|---|---|---|---|---|---|
| 0.175 | 1.75 [1.56, 1.96] | 10.9 | 7.5 | 77.1 | **25.4 %** | 0.06 % | 0.513 |
| 0.35 (frozen; main sweep, 300 trials) | 1.56 [1.44, 1.69] | 51.9 | 42.7 | 102.6 | 0.0 % | 0.5 % | 0.470 |
| 0.70 | 1.63 [1.48, 1.80] | 23.5 | 19.5 | 78.5 | 0.0 % | 0.8 % | 0.508 |

**Scoring the prediction.** The narrow band raised the exponent, as predicted — but it
did so while leaving 25 % of trials uncommitted, the same signature as the long dwell and
the short pulse, so the rise cannot be attributed to the band rather than to commitment
becoming harder. The wide band did not lower the exponent: at 0.70 rad, about three
times the noise spread, the in-band probability should be nearly K-independent and the
half power should have gone; instead p stayed at 1.63, inside the frozen band's interval.
**The band-to-spread reading of the half power is not supported.** The half power
survives a band wide enough to remove it, so it lives elsewhere in the race — most likely
in the entry-time order statistics over the eligible clocks (how the fastest of N clocks
with random starting phases reaches the band), with noise-assisted entry a second
candidate, since the exponent also rose with the noise strength (1.38 → 1.56 → 1.66) in a
direction a simple "more spread, flatter curve" picture does not give. Neither has been
computed. Across the whole criterion space now swept — dwell, tolerance, noise, pulse,
population, timestep — the frozen-criterion exponent stays between 1.4 and 1.8, and it
reaches 2 only with an amplitude-dependent dwell put in by hand.

## Fixed-area pulse sweep — Experiment 6, the other duration question (`results_fa*_N32_dt7.csv`)

The plan separates fixed-peak and fixed-area duration sweeps because they answer
different questions. The fixed-peak sweep is above (pulse 2 / 4 / 8 at K = 2: exponent
1.68 / 1.56 / 1.38). The fixed-area sweep holds the pulse area K·T at the main sweep's
value of 8, so a short strong pulse and a long weak one deliver the same integrated
coupling. Since K = 4 exceeds the frozen ±3 support, the whole sweep uses a ±6 support with
32 clocks at the same 0.375 spacing, so the population is identical across durations.
Three angles, 200 trials per cell, frozen criterion.

| pulse T | peak K | p [95 %] | Born dev. (3) | rate-sum dev. | linear dev. | eligible A/B at 20° | unresolved | P_A(45°) |
|---|---|---|---|---|---|---|---|---|
| 2 | 4.0 | **1.16 [0.94, 1.40]** | 45.6 | 44.4 | 3.7 | 20/8 | 0.0 % | 0.480 |
| 4 | 2.0 | 1.55 [1.30, 1.81] | 10.8 | 8.4 | 20.1 | 10/4 | 0.0 % | 0.505 |
| 8 | 1.0 | 1.51 [1.27, 1.78] | 14.2 | 5.7 | 19.1 | 6/2 | 0.7 % | 0.462 |
| 16 | 0.5 | undetermined [5.2, 8] | 93.9 | 0.1 | 234.1 | 2/0 | 4.5 % | 0.490 |

The reference cell (T = 4, K = 2) reproduces the main sweep's 1.56 on this wider grid, so
the support change is inert, as it should be. **At fixed area the channel ratio is not
preserved.** The short strong pulse drops the exponent to 1.16, essentially the
single-slide value: with K = 4 twenty of the thirty-two clocks are eligible and all of
them lock at once, so the order-statistic gain from width saturates and the race reduces
to the fastest slide. The long weak pulse holds 1.5. The longest pulse is a grid artefact,
not physics: a coupling of 0.17 reaches no clock on a 0.375 spacing, so the weak channel at
20° and 70° has nothing that can lock and the outcome is deterministic (the rate-sum race,
which carries the same threshold, fits it at deviance 0.1). In the plan's matrix this is
the row *"normalized A/B ratio changes with pulse duration or shape — the proposed outcome
weights are time-window dependent and are not yet a universal Born law,"* now from the
fixed-area side as well as the fixed-peak side.

## The half power, found: entry-time order statistics (`entry_time_order_statistics.py`)

Strip the race to its deterministic skeleton — the package's own drift and raised-cosine
envelope, the frozen grid, band (0.35 rad, contracting side) and dwell (0.5), uniform
random initial phases, **no noise** — and ask what exponent the clocks' entry times alone
produce. Twenty thousand trials per cell, nine angles.

| skeleton | p [95 %] | note |
|---|---|---|
| one central clock per channel, constant K | 1.13 [1.12, 1.14] | closed form t = h(θ₀)/K, h = ln(tan(\|θ₀\|/2)/tan(ε/2)) for \|θ₀\| > ε, else 0; the closed form alone gives 1.134 |
| one central clock per channel, pulsed | 1.12 [1.11, 1.14] | |
| full 16-clock grid, constant K | 1.46 [1.45, 1.48] | 28 % ties: clocks starting inside the band commit simultaneously at constant K |
| **full grid, raised-cosine pulse — the race's geometry** | **1.52 [1.51, 1.53]** | ties 0.7 %, unresolved 4 of 180 000 |
| the noisy race (main sweep) | 1.56 [1.44, 1.69] | |

**The deterministic skeleton reproduces the race.** Noise moves the exponent by at most a
few hundredths. The decomposition:

- **A single clock's entry-time race gives 1.13, not 1.** One clock per channel, entry
  time proportional to 1/K times a random factor h(θ₀) whose log has standard deviation
  0.84; the two-channel outcome is the probability that h_A/K_A < h_B/K_B, a sigmoid in
  the log of the coupling ratio whose slope, in Born form, is 1.13. This is the "rate"
  contribution.
- **Fifteen more clocks add about 0.4, not 1.** In a Poisson race the eligible clocks'
  rates add, so the width contributes a full power and the total is 2. Here each clock's
  entry is a near-deterministic slide from its starting phase, and the fastest of N such
  slides is set by the *closest* starting phase, an order statistic that improves only
  logarithmically in N: the probability that some eligible clock starts inside the band
  is 1 − (1 − ε/π)^N, which is 0.21 at N = 2 and 0.69 at N = 10 (exactly the "inside"
  fractions the constant-K run records), and the time otherwise goes as
  (1/K) ln(tan(π/2N)/tan(ε/2)). Over the swept range (2 to 10 eligible clocks) that
  saturating gain is worth about K^0.4.

So the race scales as K^1.1 from the slide times K^0.4 from the order statistic, which is
the "width times root rate" of the spectral controls stated mechanically. The half power
is not a half power in the physics; it is a full power of rate that a single slide already
carries, plus a logarithmic gain from width where a Poisson race would have a linear one.

**What this says a Born-producing race would need.** For the tongue's rate-weighted flux
to be the outcome frequency — width times rate, the semicircle, coupling squared — each
eligible clock's commitment would have to be *memoryless*: an exponential waiting time
with hazard proportional to its relaxation rate, so that the hazards add across the
tongue. The Adler slide from a random phase is the opposite of memoryless. That is a
precise statement of what the Dirac–Kuramoto substrate would have to supply and does not,
as specified: a per-site commitment that is a Poisson process with rate proportional to
the local locking rate. It is also, read the other way, the golden rule again — a hazard
linear in the site's coupling squared — which is what reading B of Paper 1 already
imports.

## What this does and does not establish

It establishes, at diagnostic budget, that the noisy Adler race with a fixed physical
dwell does not produce a universal coupling-squared law. The exponent it produces sits
between 1.4 and 1.8 and is set by the dwell, the pulse duration and the noise; it rises
toward 2 as commitment becomes unreliable, and the efficiency collapses before it
arrives. That is the negative branch of the two-channel
plan's completion boundary ("It is not complete merely because one parameter choice
visually resembles the Born curve"), reached from the other side: one parameter choice —
dwell 1.0 — does resemble the Born curve, and the sweep around it shows why that is not
a law.

It does not establish anything about production: the frozen numerical budget is unmet,
the moving-band audit's `numerical_no_result` stands, and a production sweep at 64 clocks
and dt = 2⁻⁹ could in principle move the numbers. The dt and N checks above say the
direction is unlikely to be large, not that it is zero. It does not test the inverse-
coupling dwell (a labelled positive control only, never primary), spectral controls
(Gaussian, Lorentzian, structured), lock-tolerance sensitivity, or fixed-area pulse
sweeps. And per the package's own non-claims it says nothing about exclusivity, energy
routing, or a microscopic bath.

Raw ledgers: `adler_born_two_channel/results/x2-<tag>-<A|B>-phi<deg>-N<N>-dt<k>/`
(gitignored there). Paired summaries: `results_<tag>_N<N>_dt<k>.csv` here.
