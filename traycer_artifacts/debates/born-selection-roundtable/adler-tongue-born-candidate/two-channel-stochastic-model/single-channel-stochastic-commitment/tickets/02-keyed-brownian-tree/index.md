---
title: "02 — Implement streamed keyed white noise and the Brownian tree"
kind: ticket
status: 2
---

# 02 — Implement streamed keyed white noise and the Brownian tree

## Objective

Implement the amplitude-neutral effective bath as reproducible independent white phase noise, including distribution-correct nested splits when an exact tongue crossing lies inside a uniform timestep.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Stochastic integration and paired refinement** and **Exact off-grid crossings**
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [01 — Raw-process isolation](../01-raw-process-isolation)

## In scope

- `stochastic.py` counter-keyed Gaussian phase kicks.
- Immutable physical keys based on dataset, trial, clock, finest parent step, and Brownian-tree node/crossing identity.
- Bounded time-block streaming without materializing the trial-by-clock-by-time cube.
- Fine-to-coarse increments formed by summation from one finest physical tree.
- Conditional Brownian child construction at arbitrary deterministic crossing fractions; the right child is the parent residual.
- Recursive chronological splitting for multiple crossings.
- Exact-zero handling for zero duration and zero diffusion.
- S0 noise calibration and mutation checks.

## Out of scope

- Adler drift, phase evolution, eligibility, dwell, commitment, bridge-audit uniforms, outcome statistics, or claims about a microscopic bath.

## Requirements

1. Each unsplit kick has mean zero and variance equal to twice the declared diffusion strength times its duration.
2. Split children have the correct duration-scaled variances, unconditional covariance consistent with zero, and deterministic machine-precision parent conservation.
3. Use a scale-aware few-unit-in-last-place bound for nonzero floating-point parent re-sums; require bit-exact zeros for zero-duration and zero-diffusion children.
4. The split normal belongs to the physical noise namespace. Model labels and audit namespaces cannot affect it.
5. Full/control and fine/coarse consumers receive the same physical leaves.
6. `alpha` endpoints consume no split normal; invalid fractions, identities, or crossing geometry fail loudly.
7. Batch size, early stopping, execution order, and thread scheduling cannot change assigned values.
8. The implementation never introduces coupling, mismatch, amplitude, or analytic-rate dependence into noise strength.

## Acceptance criteria

- Independent statistical checks validate mean, variance, temporal independence, cross-clock independence, and sibling covariance over predeclared samples.
- Parent/child conservation passes across ordinary, near-zero, and near-one fractions and repeated nested splits.
- Coarse increments equal sums of the same elementary leaves used by fine paths.
- Reordering batches, stopping other trials early, and switching full/control labels leaves selected keyed values unchanged.
- Zero diffusion yields byte-identical zero kick arrays and consumes no split key.
- Mutations for proportional splitting, independent right-child sampling, model-specific keys, shared clock noise, or nonzero zero-diffusion descendants fail.
- The canonical verifier passes with every prior check unchanged.
- No generated noise cube or persistent result file is written.

## Handoff

Report the key schema, split construction, statistical sample sizes and intervals, conservation tolerance, memory behavior, mutation evidence, and canonical verification output. State explicitly that white noise is only a minimal effective bath.
