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

## The energy-tracking race: memoryless commitment with hazard proportional to absorbed energy (`energy_hazard_race.py`)

Run at JB's request after the order-statistics result said what a Born-producing race
would need. The dwell criterion is replaced by a memoryless one: each clock accumulates
the energy it absorbs from the drive, and commits as a Poisson event with hazard c·E.
The energy law is the Adler clock's own — a drive of amplitude K delivers power K cos θ to
a fixed-amplitude phase oscillator, which averages to zero over a slip cycle and equals
the relaxation rate √(K² − Δ²) for a locked clock — so **no square is inserted**; Paper 1's
quadratic deposit (P1) is run as the contrast. Same grid, pulse, angles, noise (D = 0.08);
10 000 trials per cell; the first commitment in either channel ends the trial.

**Prediction, stated before running:** with Adler's power the summed absorbed power of a
channel's locked clocks is the tongue's rate sum, the semicircle, so a linear memoryless
hazard should give p near 2 up to entry transients; with P1's square it should overshoot
toward 3.

**A bookkeeping artefact first, on the record.** The first run clipped each clock's
energy at zero every step. That rectifies the slip cycles of the ineligible clocks, whose
power averages to zero, and leaves a spurious positive residue linear in K from all
sixteen clocks: the channel energy scaled as K^1.33 and the exponent came out 1.05–1.15.
Accumulating the signed power without gating fails the same way (1.03–1.15; a slipping
clock's zero-mean oscillation still has positive excursions the hazard sees). The
physical statement — a clock outside its tongue has no stable point and absorbs nothing
on average — has to be enforced: energy is accumulated, with its sign, only while the
clock is inside the tongue, and the hazard acts on its positive part.

**Result (gated), the prediction holding:**

| energy law | hazard scale c | noise | p [95 %] | Born dev. (9 cells, 10⁴ trials each) | channel energy ∝ |
|---|---|---|---|---|---|
| K cos θ (Adler's own) | 0.3 | 0.08 | 2.19 [2.17, 2.22] | 209 | K^2.21 |
| K cos θ | 1.0 | 0.08 | **2.16 [2.14, 2.19]** | 128 | K^2.20 |
| K cos θ | 3.0 | 0.08 | 2.16 [2.13, 2.19] | 147 | K^2.20 |
| K cos θ | 1.0 | 0 | 2.17 [2.15, 2.20] | 142 | K^2.20 |
| K² cos θ (P1 inserted) | 0.5 | 0.08 | 3.20 [3.16, 3.24] | 3795 | K^3.20 |

Per angle at c = 1 with noise: 0.977, 0.897, 0.773, 0.594, 0.496, 0.405, 0.229, 0.104,
0.025 against Born's 0.970, 0.883, 0.750, 0.587, 0.500, 0.413, 0.250, 0.117, 0.030 —
within about 0.02 everywhere, on the Born side of every fixed-dwell result of the day.
Independent of the hazard scale across a decade, independent of noise, no unresolved
trials, ties below 1 %.

**What this is.** The plan's candidate mechanism — the rate-weighted tongue flux, width
times locked absorption rate, as the outcome frequency — realised in the race, once
commitment is memoryless. The square is not inserted: it is tongue width (∝ K) times the
absorbed power of a locked Adler clock (∝ K). The exponent tracks the channel energy's
scaling exactly (2.16 against K^2.20), and that energy is the time-integrated tongue flux
over the pulse, which on this grid and pulse scales as K^2.2 rather than exactly K²: the
central clocks are eligible for more of the pulse than the edge clocks, and the stationary
rate sum on this 16-clock grid already scales as K^1.91. So the race gives the flux, and
the flux is Born to about a tenth of a power on this configuration. Born's deviance of 128
on nine cells at 10 000 trials per cell means 2.16 is statistically distinct from 2.00 at
this precision; it is not distinct from the flux.

**Two checks.** (i) The hazard's own exponent, hazard c·E^m: m = ½ gives p = 1.70
[1.68, 1.73] and m = 2 gives 3.25 [3.21, 3.29], against 2.16 at m = 1, with the channel
energy unchanged (K^2.2) — the outcome exponent is set jointly by the energy's scaling
and the hazard's, and only a hazard linear in the energy lands near 2. (ii) A stationary
drive, K constant over the window instead of the raised-cosine pulse: p = 2.09 [2.06,
2.11], energy ∝ K^2.17, closer to 2 than the pulsed case; the residual above the grid's
stationary rate-sum exponent of 1.91 is the locking transient, which costs the weak
channel proportionally more of its window.

**What it needed, said plainly.** Two things were put in by hand, and neither is the
square: that commitment is a Poisson process with no memory, and that its hazard is
linear in the absorbed energy (check (i) shows the second is load-bearing). Those are the two structural properties of the golden rule,
and they are what Paper 1's Theorem 5 and reading B assume. What the race then supplies
on its own is the amplitude dependence — the tongue geometry and the Adler power law
combine to the square without a squared quantity anywhere in the dynamics. Read against
the fixed-dwell race (1.56, entry-time order statistics) and the tuned dwell (2.00 by a
fitted quarter power), this is the version of the Dirac–Kuramoto candidate that works at
diagnostic budget, and it works by being the golden rule's structure with the substrate's
own coupling law inside it.

## The E-16 first-irreversibility check for a memoryless hazard (`e16_memoryless_hazard_check.py`)

The energy race needs commitment to be a Poisson event with hazard linear in absorbed
energy. Fermi's golden rule supplies exactly that, but only in its regime of validity:
the transition rate λ must be small compared with the bandwidth of the continuum it
decays into, i.e. the bath correlation time τ_c = 1/Γ must be short compared with the
commitment time 1/λ. Otherwise the coherent early-time growth is not over before the
transition completes, the hazard carries memory, and commitment is a cascade rather than
a Poisson event. E-16 already has both numbers for each detector.

**Part 1 — the detectors' Markov ratio λτ_c** (all inputs literature-typical, from the
E-16 ledger; a memoryless hazard needs ≪ 1):

| detector | τ_c = 1/Γ | first-irreversibility clock | λτ_c | verdict |
|---|---|---|---|---|
| Si SPAD 500 nm, 300 K | 10–67 fs | 10 fs – 1 ps (vertex + thermalisation) | **0.01 – 6.7** | marginal, straddles unity |
| InGaAs SPAD 1550 nm (silicon inputs, flagged) | 10–67 fs | 10 fs – 1 ps | 0.01 – 6.7 | marginal |
| NbN SNSPD 2 K, commit = hotspot | 10–20 ps | 10–50 ps | 0.2 – 2.0 | marginal |
| NbN SNSPD 2 K, commit = cascade onset | 10–20 ps | 0.1–1 ps | **10 – 200** | not memoryless: commits inside the bath correlation time |

This is the morning's ladder read for a third time, with a third meaning. This morning
the same ratio decided whether the exchange game finished before commitment could act;
now it decides whether commitment is Poissonian at all. Silicon sits in the same marginal
band it sat in twice already, one order each side of unity, so whether its first
irreversibility has the golden rule's structure cannot be settled from these inputs. The
SNSPD's cascade reading is not memoryless on any input in its range: a quasiparticle
cascade that completes in a fraction of the electron–phonon time is a deterministic
avalanche, not a rate process, and on that reading the SNSPD is exactly the detector for
which the energy race's mechanism should fail — which is the same detector family the
domain question of E-16 excluded on different grounds, and the same standing caution
applies: SNSPDs are in wide use and consistent with quantum mechanics.

**Part 2 — how much memory the Born result tolerates.** The race with a lagged hazard:
each clock's absorbed energy becomes hazard-bearing only after a first-order lag τ_mem
(τ_mem = 0 is the memoryless race). At c = 1 the race's own commitment rate is about 10 per
time unit, so λτ_mem = 1 at τ_mem = 0.1; the pulse lasts 4. Prediction fixed before running:
near 2.16 while λτ_mem is small, rising as the lag pushes commitment toward the pulse end.

| τ_mem | λτ_mem | p [95 %] | Born dev. | unresolved | P_A(45°) |
|---|---|---|---|---|---|
| 0 | 0 | 2.21 [2.19, 2.24] | 210 | 0 | — |
| 0.01 | 0.1 | 2.16 [2.14, 2.19] | 130 | 0 | — |
| 0.03 | 0.3 | 2.21 [2.18, 2.23] | 208 | 0 | — |
| 0.1 | 1 | 2.18 [2.15, 2.21] | 155 | 0 | — |
| 0.3 | 3 | 2.18 [2.15, 2.21] | 152 | 0 | 0.501 |
| 1.0 | 10 | 2.18 [2.16, 2.21] | 158 | 0 | 0.501 |

**The prediction's second half failed: nothing moves.** Across two orders of magnitude of
hazard memory, up to lags of a quarter of the pulse, the exponent stays inside the
memoryless race's scatter, no trial is left unresolved, and the per-angle frequencies at
10° and 80° (0.975 / 0.023 at λτ_mem = 3; 0.978 / 0.022 at 10) are the memoryless ones.
The reason is the one the Poisson race's algebra gives: a lag that is the same for every
clock reparametrizes time identically for both channels, the ratio of their hazards is
unchanged at every instant, and the probability that A fires first is unchanged. Memory
in the hazard's *timing* is harmless; what the sweeps before this one showed is that the
hazard's *form* is not — a square-root or squared hazard moves the exponent (1.70, 3.25),
and a deterministic slide instead of a hazard moves it to 1.5.

**Part 3 — what this does to the E-16 question.** The Markov ratio λτ_c, which put silicon
in a marginal band and the SNSPD's cascade reading outside it, is therefore not the
quantity that decides whether a detector can carry the energy race's mechanism. A finite
bath correlation time that merely delays or reshapes the turn-on of the rate leaves the
Born ratio where it was. What the detector has to supply is narrower than a constant
rate: a *stochastic* commitment whose probability per unit time is linear in the site's
absorbed energy, with a time profile that does not depend on the site. That is the
structure of the absorption vertex itself, in both detector families — a golden-rule
transition into a continuum, linear in the local intensity — and it is the deterministic
physics downstream of the vertex (the avalanche, the hotspot growth, the quench) that is
a cascade, which the device review had already found to be photon-agnostic and unable to
carry which-site weight. On this reading the SNSPD's non-Markov cascade is downstream of
the selection and irrelevant to it, the SPAD/SNSPD asymmetry that reading A predicted
does not arise from this mechanism either, and the picture is reading B's: the weights
are fixed at the vertex, stochastically and linearly, and everything slower writes the
record. What is still not answered by any simulation is whether the vertex's stochastic
selection is one-world actualization or a rate over an ensemble — which is the
measurement problem, and where the day began.

## Ensemble versus one-world at the vertex: the exclusivity discriminator (`vertex_exclusivity_discriminator.py`)

The energy race fixes the weights at the vertex as a stochastic, energy-linear
commitment. Two readings of that remain. In the *ensemble* reading the golden rule gives
independent rates at every site and nothing forbids two separated sites from both
committing in one trial. In the *one-world* reading exactly one site commits per quantum,
which the race enforces by the first-commit stop — imposed bookkeeping, in the plan's
words. The observable that separates them is the coincidence rate between the two ports
of a balanced split fed with single photons: item 2b's heralded 505 nm source gives
g²(0) = 0.0023 with silicon SPADs. Run at JB's request; same race as the energy variant
(gated, Adler power, c = 1, noise), 20 000 trials, step 2⁻⁸; the two channels' commit
times are generated independently, which *is* the ensemble model, and the rules differ
only in how the pair is read.

| reading | rule | P(both commit), 45° | coincidence ratio | against 0.0023 |
|---|---|---|---|---|
| ensemble | independent hazards, no exclusivity | 1.000 | 1.00 | excluded, ×400 |
| one-world | first-commit stop | 0 by rule | 0 | consistent |
| one-world, finite speed | the other channel keeps its hazard for τ_x after the first commit | linear in τ_x, density 1.5 per race unit | — | needs τ_x ≤ 1.5 × 10⁻³ race units |

(At 20°: density 0.5, critical τ_x = 4.5 × 10⁻³. Same-step ties, 0.27 % at this step, are
a discretisation floor — exact simultaneity has zero probability in continuous time — and
are excluded from the doubles.)

**Translation.** The critical delay is 9 × 10⁻⁴ of the mean commit latency at 45° and
3 × 10⁻³ at 20°. Taking E-16's first-irreversibility clock as that latency: for silicon,
10 fs to 1 ps, exclusivity must act within **0.01 to 0.9 fs**, in which light travels 3 nm
to 0.3 µm; for the SNSPD's hotspot reading, within 9 to 45 fs, 3 to 13 µm. The output
ports of a laboratory beamsplitter are 1 mm to 1 m apart, a light-crossing time of 3 ps to
3 ns. The mapping of race time to physical time is a choice (any other mapping still puts
the critical delay at 10⁻³ to 10⁻⁴ of the interaction time, and interaction times at a
vertex are femtoseconds to picoseconds), so the margin is robust: exclusivity must act
10³ to 10⁸ times faster than a signal could cross the separation.

**What it decides.** The ensemble reading is excluded by a factor of four hundred: the
vertex selection is one-world. And the one-world stop is not bookkeeping that could be
dropped or made local: to reproduce the coincidence data it has to act across the
separation faster than light by orders of magnitude, i.e. it is the nonlocal closed-pot
constraint — Paper 1's P5, the premise v0.7 already conceded the single-detector sector
consumes whenever the candidate sites are spacelike separated. This is the Grangier
anticorrelation argument stated inside the race, with the race's own numbers. What
remains is what was always going to remain: the golden rule supplies the rates and the
substrate must supply a one-quantum constraint that is nonlocal in exactly this sense.
Nothing here derives it; the day's simulations have now said precisely what it must do
and how fast.

## Production pricing (`pricing/PRICING_REPORT.md`)

Not a physics result. The package's ticket-07 settled next step was to price the
intended-configuration validation campaign under a frozen protocol before deciding
whether to run it. That benchmark was run (41.6 of the 60-minute ceiling, twelve cases,
all clean, package untouched): six of seven stages are priced, summing to about 58
minutes of compute at 1.6 GiB; the seventh, the 1 024×-trial moving-band time quantile,
is `pricing_unresolved` on the plan's 16× rule and because the comparison kernel is
quadratic in cluster count at that size. A price is not an approval.

The campaign was then authorized and run (`validation/VALIDATION_REPORT.md`; 60.5 min,
serial, peak 635 MiB, package untouched, reference ladders reproduced first). Both
launched stages, S1 and M5, returned `numerical_no_result` under their predeclared rules
and the stop rule halted the rest; the ticket-07 disposition does not change. The
endpoint dwell scheme's discretisation error at dt = 2⁻⁹ is two to five times the frozen
production allowance, measured now at the intended configuration; at 6 000 walkers the
statistical floor alone exceeds the probability allowance, and the moving-band time row
sits at 3.8× the time allowance. So the package's production path is closed as designed,
and everything in this file stays diagnostic. A redesigned campaign (more walkers, finer
timestep, the dt/16 replay, a re-frozen reset cap) is cheap in compute but is a plan
change for the sponsor to decide.

The sponsor decided, and the redesign ran the next morning (`validation/REDESIGN_REPORT.md`;
45 min, peak 509 MiB). Sixteen times the walkers moved the stationary rows from 2–5.5× to
1.1–1.7× the allowance with the refinement gate now passing, so what remains there is a
bias of about 1.4× that one more timestep refinement would test. The dt/16 replay
settled the moving-band probability rows but showed the commit-time quantile *diverging*
under refinement, past the whole-ladder allowance, and the frozen reset-count cap fired
at 14 against 3. The gate stays red; the diagnostic label on this file stays.

A second override ran S2 at dt/64 with 96 000 walkers (`validation/S2_REPORT.md`; 37 min,
oracle peak 1.9 GiB): gate pass, eight of nine probability rows and all three time rows
fit, the ninth misses by 5 %, and every row projects under the allowance at dt/256 with
the package's projection rule now checked against measurement. A third override ran S3
at dt/256 (`validation/S3_REPORT.md`; 67 min, peak 1.5 GiB): the survival field
converges and every time row fits, but the exit-count fields stop converging — the
upper-exit count drifts upward under refinement on resolved increments, and a
systematic offset of about 0.002–0.003 in the attribution of exits to the two edges
remains between the endpoint scheme and the oracle, no longer falling with the
timestep. The √dt projection under-predicted exactly those rows. Refinement has done
what it can on the stationary path; what remains there is a numerics question inside
the package (the oracle-margin check differences only the survival field, so an oracle
error in the exit fields would be invisible to it). The moving-band audit, with its
diverging time quantile and a reset cap frozen for a coarser cell, still blocks by
larger factors. The gate stays red; the diagnostic label on this file stays.

The sponsor then re-froze the production design on the observables that converge —
survival and the time rows, dropping the exit-count fields and the commit-time quantile
(`validation/REFROZEN_DESIGN.json`, `REFREEZE_REPORT.md`; a hashed manifest, no run, no
package change). On that set the stationary path at dt/256 fits every allowance and
would buy an exponent half-width of 0.16 against the target of 0.25. The frozen verdict
nevertheless stays at no-result because the package carries each ladder's gate verdict
through and every gate on record failed on a dropped observable or on the reset cap,
which was not re-frozen. With the gates re-decided on the retained identities the
stationary set is satisfied and the moving-band set is unresolved on M5's probability
shifts at the intended step, which a 25-hour ladder at dt/16 is projected to clear.
Those are decisions for the sponsor; nothing here is a physics result.

The sponsor re-decided the gate verdicts on the retained identities
(`validation/REDECIDED_GATES.json`, `REDECIDE_REPORT.md`; the package's own clause
function applied to the recorded ladders, the reset-count cap set aside as a diagnostic
count, no clause softened). Every retained identity in every ladder passes, so all five
ladders re-decide to pass: the stationary set is now *satisfied* (5 704 admissible trials,
half-width 0.16 against the 0.25 target) and the full set is *unresolved* on M5's
probability shifts at the intended step alone, which the priced 25-hour ladder at dt/16
would address. No evidence set is a numerical no-result any more; the diagnostic label on
this file's physics results stays until a production sweep runs under the re-frozen
design.

## What this does and does not establish

It establishes, at diagnostic budget, that the noisy Adler race with a fixed physical
dwell does not produce a universal coupling-squared law. The exponent it produces sits
between 1.4 and 1.8 and is set by the dwell, the pulse duration and the noise; it rises
toward 2 as commitment becomes unreliable, and the efficiency collapses before it
arrives. The reason is computed: each clock's commitment is a near-deterministic slide,
and the fastest of N slides gains only logarithmically in N where a rate-weighted race
would gain a full power.

It also establishes, at the same budget, that the same clocks, grid and pulse **do**
produce the rate-weighted tongue flux as their outcome frequency — exponent 2.16, within
about 0.02 of Born at every angle — when commitment is made memoryless with a hazard
linear in the energy a clock has absorbed inside its tongue, using the Adler clock's own
power law and no inserted square. What that version puts in by hand is the golden rule's
structure, memorylessness and hazard linearity; what the substrate supplies is the
amplitude dependence, tongue width times locked absorption rate. Whether a physical
commitment process in a detector has that structure is exactly the E-16 question, first
irreversibility as dissipation into a continuum, and is not answered here. That is the negative branch of the two-channel
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
