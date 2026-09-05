# The two calculations the review round owes — predictions, fixed before running

*2026-09-05, after the four reviews and before either run. Reviewer R1 (M2) found the exact
model never swept into the regime real detectors occupy, Γ ≫ K; reviewer R3 (M1) found the
selection postulate never tested with detectors reached at different times. Both are cheap.
Predictions here; results scored in `REVIEW_RUNS_RESULTS.md`.*

## Run A — the crossover location at Γ/K = 10, 100, 1000 (`gamma_regime_sweep.py`)

Method: the record channel's effect on the single-excitation amplitude in the Markov limit is
the non-Hermitian term −iΓ/2 on the absorber; the partial echo with the record untouched is
forward evolution under H_eff = Δ|e⟩⟨e| − (iΓ/2)|e⟩⟨e| + K(|p⟩⟨e| + h.c.) followed by the same
with Δ → −Δ, K → −K and the decay term kept. Calibration: at Γ/K = 0.2 and 1 this must
reproduce the record's 256-mode results (rate-based midpoints 1.5–2.0 and 1.3) to within
the record's own scatter. Then Γ/K = 10, 100, 1000 with the capture time scaled so that the
resonant leak over the run is of order one.

- **A1.** The rate-based crossover midpoint follows the interpolation x₅₀ ≈ √(Γ²/4 + 2K²)/K
  within 30 % at every Γ/K: about 1.4 at Γ ≪ K, about 5.4 at Γ/K = 10, about 50 at 100,
  about 500 at 1000. R1's adiabatic-elimination formula is right: for Γ ≫ K the crossover
  is at half the record rate and is record-set.
- **A2.** Consequence, on record: for a room-temperature semiconductor detector (Γ/K ~ 10⁵)
  the crossover in detuning is set by the record channel's rate, which is the
  temperature-dependent quantity; "coupling-set rather than temperature-set" holds only
  for Γ ≪ K and is withdrawn from the paper's list of distinctive claims.

## Run B — the race with channels reached at different times (`staggered_arrival_race.py`)

Method: the record's gated energy race (hazard linear in absorbed energy, K = 2, frozen
16-clock grid, raised-cosine pulse of duration 4), with channel B's pulse delayed by
0, 2 and 8 time units (8 = fully sequential), at the record's hazard scale c = 1 (every
channel fires within its window) and at a reduced scale c = 0.05 (a channel exposed to the
full amplitude fires about half the time). Reported: the unconditional click probability of
each channel, the probability that A fires first, and the conditional ratio, against Born.

- **B1.** At delay 8 and c = 1, A fires first in essentially every trial at every angle,
  including the 80° split where Born gives A 0.03: the nearer detector wins with
  probability above 0.95. R3's arithmetic is right.
- **B2.** At delay 8 and c = 0.05, the conditional ratio departs from Born toward A at every
  angle, by more than the synchronous race's own scatter, and the single-channel click
  probability is not linear in the squared coupling: at the 45° split each channel's
  unconditional click probability exceeds half the full-amplitude value by more than 10 %,
  the exponential-in-intensity nonlinearity.
- **B3.** At delay 0 the synchronous result of the record (exponent ≈ 2.2, conditional
  ratio within 0.03 of Born at 30° and 60°) is reproduced, and at delay 2 (half a pulse)
  the departure is already visible.
- **B4.** Consequence, on record: clause 2 of the postulate as written in v1.0 is
  falsified by the record's own model once exposure is staggered, and the paper must
  restate the hazard as acting on the branch weight of the conditional state with the
  no-jump renormalization — the quantum-jump unravelling — which is the Born rule's
  branch weights put in.

## Run A′ — the intermediate regime Γ/K = 1.5–7 (third round, before running)

Two third-round reviewers re-ran Run A's propagator in the region Run A skipped and report
that the rate-based midpoint is non-monotone in Γ/K, dipping to about 0.6K near Γ = 4K —
the exceptional point of the 2 × 2 non-Hermitian matrix, where at Δ = 0 its eigenvalues
−iΓ/4 ± √(K² − Γ²/16) coalesce — and that it drifts by a factor of about 4 with observation
time at Γ/K = 3, so that the formula √(Γ²/4 + 2K²) is off by factors 1.6–2.2 at Γ/K = 2–5.
Their numbers are not in the record; this run puts the measurement there.

**Prediction:** the reviewers are right. At Γ/K ∈ {1.5, 2, 3, 4, 5, 7}, with the capture
time scaled so the resonant leak over the run is of order one, the rate-based midpoint
falls below the formula by a factor between 1.5 and 3 across the range, with its minimum
near Γ/K = 4; at fixed Γ/K = 3 the midpoint changes by more than a factor of 2 between
capture times differing by a factor of 10. Consequence, on record: the formula is a
two-asymptote interpolation that fails in the intermediate regime, "to 15 % from 0.2 to
1000" is false, and the location statement must be reduced to its two asymptotes with
the intermediate region called non-monotone and convention-dependent.
