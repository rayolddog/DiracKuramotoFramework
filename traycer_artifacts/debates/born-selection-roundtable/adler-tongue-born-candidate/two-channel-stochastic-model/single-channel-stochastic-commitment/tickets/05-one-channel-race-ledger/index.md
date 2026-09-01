---
title: "05 — Implement the finite one-channel race and immutable ledger"
kind: ticket
status: 2
---

# 05 — Implement the finite one-channel race and immutable ledger

## Objective

Run a fixed finite population of actual competing clocks until the first dwell completion, while retaining every unresolved path, co-completion, and exposure needed to audit first-winner censoring.

## Governing artifacts

- [Closed single-channel plan](../..), especially **First channel commitment**, **Complete ledger**, and **Experiment S5**
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [01 — Raw-process isolation](../01-raw-process-isolation)
- [02 — Keyed Brownian tree](../02-keyed-brownian-tree)
- [03 — Stochastic dynamics and commitment](../03-stochastic-dynamics-and-commitment)
- [04 — Continuous-exit validation](../04-continuous-exit-validation)

## In scope

- `raw_runner.py` finite-population batching and first-commit stopping.
- One exact immutable clock grid with visible support, origin, parity, nodes, and physical population size.
- Earliest completion, all same-step co-completers, and no random internal winner.
- Mutually exclusive channel-level ledgers: committed; never eligible; eligible but never inside; inside at least once but dwell incomplete.
- Per-clock entry/reset/exposure/commit diagnostics and a small predeclared no-stop shadow sample.
- Streamed bounded-memory execution using ticket 02 keys.
- Human-readable manifest, raw CSV ledger, close marker, and content hash in a package-scoped ignored results directory.

## Out of scope

- Survival or exponent fitting, analytic comparisons, continuum replacement of the finite population, production-range selection, two-channel competition, or manuscript claims.

## Requirements

1. Every trial lands in exactly one committed or unresolved category; no trial is conditioned away.
2. The channel stop equals the earliest per-clock completion to endpoint resolution.
3. Same-step co-completers and their mismatches remain explicit and must decrease or become negligible under refinement before winner-mismatch interpretation.
4. Early stopping cannot change any other trial or clock's random stream.
5. Per-clock statistics expose opportunity time rather than treating stopped clocks as fully observed.
6. Physical `N` and grid changes are labeled model sensitivities, never numerical convergence.
7. Raw execution cannot load analytic, oracle, audit, statistical, or reporting modules.
8. A ledger is unreadable by later comparison code until its close marker and hash validate.

## Acceptance criteria

- Synthetic clocks with known completion times produce the correct first completion, co-completers, categories, and stopping time.
- Ledger category counts equal total trials; per-clock winner counts reconcile with committed trials and explicit co-completers.
- Survival reconstructed directly from raw commit times is non-increasing.
- Re-running with different batch sizes and early-stop patterns produces identical ledgers in the recorded environment.
- The no-stop shadow sample exposes expected first-winner censoring in a constructed example.
- Invalid or incomplete ledgers fail hash/close verification and cannot be opened by a consumer probe.
- Peak memory remains bounded by the configured live block rather than total trials times clocks times steps.
- Ticket 04's oracle/audit implementation checks must be recorded as passed; otherwise the runner may produce diagnostic data only. The production-specific numerical budget is frozen and enforced by tickets 07–08.
- The canonical verifier and all earlier checks pass.

## Handoff

Report the raw schema, category/exposure invariants, memory measurements, reproducibility hashes, example ledger, no-stop comparison, and explicit statement that a first clock is a model stopping event—not yet a detector click or one-world mechanism.
