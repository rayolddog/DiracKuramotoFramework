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
