# The two calculations the review round owed — results, scored

*2026-09-05. Predictions in `PREDICTIONS_review_runs.md`, fixed before running. Run A:
`gamma_regime_sweep.py` (exact 2 × 2 non-Hermitian propagation, instantaneous). Run B:
`../adler_two_channel_exploratory/staggered_arrival_race.py` (213 s; diagnostic budget).
Outputs beside the scripts.*

## Run A — the crossover location at Γ/K = 10, 100, 1000

| Γ/K | capture time | rate-based midpoint x₅₀ (Δ/K) | √(Γ²/4 + 2K²)/K | Γ/2K |
|---|---|---|---|---|
| 0.2 (calibration) | 3 | 1.54 | 1.42 | 0.10 |
| 1 (calibration) | 3 | 1.28 | 1.50 | 0.50 |
| 10 | 3 | 5.09 | 5.20 | 5.00 |
| 100 | 25 | 50.0 | 50.0 | 50.0 |
| 1000 | 250 | 500.0 | 500.0 | 500.0 |

**A1 confirmed.** The calibration rows reproduce the record's 256-mode results (1.5–2.0 at
Γ/K ≤ 0.2; 1.3 at Γ/K = 1) within the record's scatter, and at Γ/K = 10, 100, 1000 the
midpoint sits at Γ/2K to 2 %; the interpolation √(Γ²/4 + 2K²)/K tracks every row within
15 %. Reviewer R1's adiabatic-elimination formula is right.

**A2 stands.** For Γ ≫ K the crossover in detuning is set by the record channel's rate. For
a room-temperature semiconductor detector (Γ/K of order 10⁵) it is record-set, and since
Γ(T) is the temperature-dependent quantity, temperature-set. "Coupling-set rather than
temperature-set" holds only for Γ ≪ K — rare-earth memories, cavity QED at strong coupling
— and is withdrawn from the paper's list of distinctive claims; the location claim is
restated with its regime of validity and the general half-width.

## Run B — the race with channels reached at different times

Gated energy race, K = 2, 16 clocks, pulse duration 4, channel B delayed by 0, 2, 8;
hazard scale c = 1 (the record's) and 0.05. P(A first) is the conditional ratio the record
fitted; the click probabilities are unconditional.

| hazard scale | delay | P(A first) at 10°, 30°, 45°, 60°, 80° (Born 0.97, 0.75, 0.50, 0.25, 0.03) | P(A clicks) at 45° | note |
|---|---|---|---|---|
| 1 | 0 | 0.978, 0.777, 0.500, 0.232, 0.021 | 1.000 | the record's synchronous result |
| 1 | 2 | 1.000, 1.000, 1.000, 0.982, 0.401 | 1.000 | half a pulse of delay |
| 1 | 8 | 1.000, 1.000, 1.000, 0.994, 0.481 | 1.000 | fully sequential |
| 0.05 | 0 | 0.975, 0.771, 0.498, 0.228, 0.024 | 0.582 | synchronous, half efficiency |
| 0.05 | 2 | 0.992, 0.897, 0.702, 0.392, 0.046 | 0.584 | |
| 0.05 | 8 | 0.993, 0.901, 0.707, 0.400, 0.045 | 0.584 | |

**B1 confirmed in substance, wrong in its bracket at the most asymmetric angle.** Fully
sequential at c = 1, the nearer channel wins in every trial in which it fires: 1.000 at
10°–45°, 0.994 at 60°, 0.912 at 70°; at 80° it wins 0.481 because its own click
probability at that amplitude is 0.481 — the residual is the efficiency, not the race.
**B2 confirmed.** At c = 0.05 the conditional ratio departs from Born toward the nearer
channel at every angle (by +0.02 to +0.21), and the click probability is an exponential of
intensity: a channel at half the full intensity clicks 0.584 of the time where the
full-intensity channel clicks 0.834, against 0.43 for a law linear in intensity — an
excess of 36 %. **B3 confirmed:** delay 0 reproduces the record within its scatter; delay 2
already shows the departure. The "P(both)" column, near 1 for sequential exposure at c = 1,
shows what the nonlocal stop is doing: without it both channels would click.

**B4 stands.** Clause 2 of the v1.0 postulate — a hazard on the whole quantum, linear in the
energy the site has drawn — is falsified by the record's own model as soon as exposure is
staggered, which is every unequal-arm interferometer and every Bell test. The only
stochastic process with these ingredients that reproduces quantum mechanics is the one
in which the hazard acts on the *branch weight of the conditional state* and a null at
one detector renormalizes the branches at the others: the quantum-jump unravelling
(Srinivas & Davies 1981; Dalibard, Castin & Mølmer 1992; Carmichael 1993; Wiseman &
Milburn 2010). That is the Born rule's branch weights put in, and the no-jump
renormalization is nonlocal. The paper's §5 is restated accordingly in v1.1, and §5.2's
"specification" is reduced to what it is: the Born rule and nonlocal exclusivity.
