---
title: "07 — Establish feasibility, run the range-only pilot, and freeze production"
kind: ticket
status: 2
---

# 07 — Establish feasibility, run the range-only pilot, and freeze production

## Objective

Turn the verified machinery into a finite, affordable, statistically powered production proposal; use a strictly limited pilot to choose only an information-bearing coupling range; then freeze a reproducible production manifest.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Feasibility and power gate**, **Data and reproducibility**, and the S5 pilot firewall
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [05 — One-channel race and immutable ledger](../05-one-channel-race-ledger)
- [06 — Statistics and isolated comparators](../06-statistics-and-comparators)
- [04 — Continuous-exit validation](../04-continuous-exit-validation)

## Required user checkpoints

1. After measured throughput, memory, storage, and power estimates are available, John approves the bounded pilot before it runs.
2. After the pilot selects a range under the frozen count-only rule, John reviews the resulting production manifest and resource estimate before ticket 08 runs.

## In scope

- `experiments.py` versioned experiment manifests and orchestration.
- Measured clock-steps per second, peak memory, storage, and wall-time estimates using intended blocks and finest timestep.
- Power calculation for a predeclared exponent confidence width and causal-control contrast.
- Production-specific absolute/relative timestep, stationary-oracle, and moving-band-audit budgets tied to no more than the allowed fraction of planned statistical uncertainty.
- Finite primary matrix with stop/failure rules and no automatic full factorial.
- Pre-pilot frozen template defining minimum expected event/survivor counts and the deterministic fixed-rate rule.
- Separately keyed, labeled pilot that may choose only the coupling range.
- Post-pilot production manifest freezing physical/numerical/statistical inputs, source hashes, versions, grid, parity, namespaces, and comparison rules.

## Out of scope

- Looking at or optimizing the pilot exponent, curvature, time-resolved fit, noise, dwell, band, pulse, population, state machine, likelihood, or exclusions.
- Using pilot trials in production estimates.
- Launching the production run before John's second checkpoint.

## Requirements

1. Benchmark the real streamed implementation; do not extrapolate from a different kernel.
2. The proposed trial count follows the frozen precision/power target and includes central-clock and width-only controls.
3. Ticket 04's measured refinement-error envelope must fit the production-specific numerical budget at the intended timestep; otherwise revise the timestep/resource proposal before pilot or report no feasible matrix.
4. The pilot and production namespaces, folders, manifests, and outputs are physically distinct.
5. Pilot automation exposes only permitted count summaries until the production manifest is signed; exponent-related output remains unopened.
6. The fixed-contraction reference-rate rule is frozen before pilot and calculated mechanically from the selected production range afterward.
7. Grid support, parity, origin, nodes, physical `N`, minimum eligible-cell count, and discrete-staircase fallback are explicit.
8. If cost or minimum-cell requirements are infeasible, narrow the claim or report no feasible production matrix rather than silently invoke a continuum.

## Acceptance criteria

- Benchmark results are reproducible and include measured peak memory and proof that no full noise cube is materialized.
- Power code recovers predeclared synthetic cases and reports the effect of common-random-number pairing.
- Production timestep and audit/oracle tolerances are frozen before pilot output is opened and satisfy the plan's numerical-to-statistical uncertainty relationship.
- A dry-run manifest enumerates every required frozen field and fails if one is omitted.
- A mutation exposing pilot exponent/curvature or sharing pilot/production namespaces fails.
- After checkpoint 1, the approved pilot selects only cells meeting frozen event/survivor criteria; its trials are marked permanently ineligible for production analysis.
- A signed/hash-verifiable production manifest and finite resource estimate are produced for checkpoint 2.
- The canonical verifier and all earlier gates pass; numerical no-result states remain blocking.

## Handoff

Present the benchmark, power assumptions, pilot-only information viewed, selected range, frozen matrix, total estimated cost/time/storage, and production manifest hash in plain English. Do not begin ticket 08 without explicit approval.

## Settled follow-on direction

John selected a conservative bounded price for the intended-configuration validation campaign before considering any run. The measurement contract is recorded in the [validation-campaign pricing plan](validation-campaign-pricing-plan). It does not authorize benchmarks, validation stages, a pilot, production, or Ticket 08.
