---
title: "06 — Implement survival statistics and isolated comparators"
kind: ticket
status: 2
---

# 06 — Implement survival statistics and isolated comparators

## Objective

Build the separate read-only analysis process that can accept, reject, or decline a coupling-scaling claim without influencing raw event generation.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Primary scaling estimand**, **Isolated comparison curves**, and the ledger/statistics contract
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [05 — One-channel race and immutable ledger](../05-one-channel-race-ledger)

## In scope

- `observables.py`: risk sets, survival, discrete conditional failure, time-rate hazard, cumulative hazard, intervals, censoring, and winner mismatch.
- `analysis.py`: direct binomial complementary-log-log likelihood, unconstrained exponent, uncertainty, deviance, curvature/lack-of-fit, paired master-trial resampling, and explicit `no valid exponent`.
- `compare.py`: closed-ledger verification and comparison with exact-grid eligible count, exact-grid bare relaxation-rate sum, continuum flux, and constant-hazard alternatives.
- Central-clock and fixed-contraction width-only causal defeat rules.
- Frozen out-of-sample rising/falling survival and winner-mismatch comparisons.
- Synthetic estimator and failure-mode tests.

## Out of scope

- Changing raw configurations, selecting a favorable coupling window, dropping zero/all-event cells, executing the production sweep, or presenting continuum flux as the finite-population predictor.

## Requirements

1. Analysis opens only a closed ledger whose content hash matches its manifest.
2. Every binned display includes risk count, events, censoring, and width; events-per-risk is not mislabeled as a continuous rate.
3. The primary fit uses committed/unresolved binomial counts in every frozen coupling cell, including zero- and all-event cells.
4. Exponent is unconstrained. Curvature or lack-of-fit failure returns `no valid exponent`, not a new window.
5. Common-random-number uncertainty resamples master trial IDs or uses independent namespaces; cells are not treated as independent by convenience.
6. The bare sum uses the exact physical production clocks and remains distinct from spacing-weighted continuum flux.
7. The width-only control uses the same fit and out-of-sample diagnostics. A compatible quadratic control or insufficient powered contrast blocks the width-times-rate attribution.
8. The comparison process cannot write or modify the raw ledger.

## Acceptance criteria

- Synthetic binomial datasets recover declared exponents and uncertainty over ordinary, zero-event, all-event, and saturated cells.
- Deliberately curved and non-power datasets return lack of fit or `no valid exponent` without point deletion.
- Known censored-event data reproduce survival and hazard quantities with correct risk sets and bin widths.
- Paired resampling differs appropriately from an intentionally wrong independent-cell calculation.
- Exact-grid bare sum, eligible count, continuum flux, and constant hazard remain separately named in schemas, files, tables, and plots.
- Synthetic central-clock and width-only cases demonstrably defeat a false quadratic causal claim.
- Analysis refuses an open, changed, or hash-mismatched ledger.
- Runtime/import checks prove raw execution still cannot reach analysis or analytic comparators.
- The canonical verifier and all earlier checks pass.

## Handoff

Provide estimator definitions in plain English, synthetic recovery/failure results, causal-control decision table, ledger read-only evidence, comparison labels, and all commands. State that a statistically adequate exponent is not itself a Born-rule result.
