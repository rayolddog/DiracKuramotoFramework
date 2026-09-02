# adler_two_channel_exploratory — the two-channel race, run as a diagnostic

Two scripts that build the two-channel plan's race (Experiments 3 and 4 of
`traycer_artifacts/.../two-channel-stochastic-model/index.md`) on top of the validated
one-channel raw race in `adler_born_two_channel/`, without modifying that package.

- `race_driver.py` — writes one closed one-channel ledger per (polarization angle, channel)
  through `raw_runner.write_raw_run`, with K_A = K cos φ and K_B = K sin φ, the frozen
  ticket-07 physics (support ±3, phase diffusion 0.08, lock tolerance 0.35 rad, dwell 0.5,
  raised-cosine pulse of duration 4.0), and independent keyed noise per cell. Imports no
  prediction.
- `analysis.py` — the separate comparison process: pairs the two ledgers per angle
  (outcome = channel of the earliest commitment; tie if equal; unresolved if neither), fits
  the unconstrained coupling exponent, and scores the predeclared comparators (linear,
  Born, strongest-wins, rate-sum race, width-only race). The only place the analytic
  prediction is imported.

Why the pairing is the race: the plan's channels share the envelope and the grid but not
noise or phases, and do not couple to each other, so "the earliest committing clock across
both populations" is the pairwise minimum of two independent one-channel first-commitment
times on the same clock time.

## What this cannot claim

Everything the package's own README says still holds. Every manifest carries
`numerical_gate = "diagnostic_only"` because the ticket-07 frozen numerical budget is not
met, so this is a reduced-budget diagnostic (fewer clocks, coarser timestep than the frozen
configuration), labelled `pilot`, never a production estimate. The first-winner stop is
imposed bookkeeping, not derived exclusivity. A "commitment" is a dwell rule, not a click.
No Born-rule derivation is claimed at any outcome. The fixed physical dwell is kept fixed.

Raw ledgers live under `adler_born_two_channel/results/` (gitignored there); the paired
summaries (`results_*.csv`) live here.
