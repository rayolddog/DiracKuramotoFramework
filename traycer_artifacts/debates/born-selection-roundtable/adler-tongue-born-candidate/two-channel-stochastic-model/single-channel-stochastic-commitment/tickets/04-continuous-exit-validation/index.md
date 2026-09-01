---
title: "04 — Validate continuous exits and moving-band dwell"
kind: ticket
status: 2
---

# 04 — Validate continuous exits and moving-band dwell

## Objective

Measure and bound the endpoint scheme's missed between-step exits before any finite-population scientific interpretation.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Between-step lock-band crossings**, **Experiment S3**, and the continuous-white-noise verification contract
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [02 — Keyed Brownian tree](../02-keyed-brownian-tree)
- [03 — Stochastic dynamics and commitment](../03-stochastic-dynamics-and-commitment)

## In scope

- `killed_diffusion.py` independent stationary absorbing-boundary PDE or spectral oracle.
- Known limiting-solution calibration and several initial positions inside a fixed lock band.
- Three or more paired timestep refinements against continuous survival, exit quantiles, and reset counts.
- `moving_band_audit.py` diagnostic piecewise-linear Brownian-bridge reset replay.
- Strict boundary and contraction geometry, exact crossing splits, circular local representatives, ambiguous-topology resets, separate audit uniforms, and capped two-boundary union probability.
- Configurable absolute/relative numerical budgets, numerical-no-result output, and measured refinement-error summaries for ticket 07's production-specific power budget.

## Out of scope

- Replacing or correcting the primary raw event ledger, choosing a timestep after seeing a desirable exponent, finite-population racing, or using the audit as a physical law.

## Requirements

1. Oracle and audit modules are unreachable from the raw event import graph.
2. The stationary oracle remains the continuous-time authority; the moving-band bridge is labeled a frozen-drift diagnostic approximation.
3. Audit replay may only add resets. Its commitments must be a pathwise subset of endpoint commitments.
4. Audit randomness uses a namespace disjoint from the physical Brownian tree.
5. Zero diffusion, exact eligibility splits, disappearing intervals, topology changes, and boundary equality follow the closed plan literally.
6. Every validation run receives immutable tolerances before its results open. This ticket verifies that mechanism with synthetic/reference budgets; ticket 07 later freezes the production-specific values at no more than the plan's fraction of intended production uncertainty.
7. Failure produces timestep refinement or a numerical no-result, never a changed event law.

## Acceptance criteria

- The independent oracle reproduces its known limiting case and is cross-checked without importing raw dynamics.
- Endpoint survival and exit quantiles converge toward the oracle across at least three paired levels.
- The reduced moving-band matrix covers central/interior/edge clocks, both mismatch signs, both pulse edges, and weak/intermediate/strong noise.
- Audit commitments are a pathwise subset and differences decrease or become statistically indistinguishable from zero under refinement.
- Mutations for audit-created commitments, removed primary resets, shared physical/audit keys, nonlinear boundary interpolation, or favorable topology selection fail.
- A deliberate overlarge discrepancy yields a machine-readable numerical-no-result and blocks the next scientific gate.
- Measured refinement errors and required observables are exported in a form ticket 07 can compare with its later power-derived numerical budget.
- The canonical verifier and all prior checks pass unchanged.

## Handoff

Report oracle method, independent reference, bridge formula, namespace, reduced matrix, validation tolerances, paired differences, measured refinement-error envelope, and pass/no-result verdict. Make no claim about the final coupling exponent.
