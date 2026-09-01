---
title: "03 — Implement stochastic Adler dynamics and fixed-dwell commitment"
kind: ticket
status: 2
---

# 03 — Implement stochastic Adler dynamics and fixed-dwell commitment

## Objective

Implement one-clock stochastic evolution, exact tongue handoffs, the timestamp-based commitment state machine, and both mechanism-negative controls without yet running a finite-population race.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Lock and fixed-dwell state machine** and **Exact width-only data-generating process**
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [01 — Raw-process isolation](../01-raw-process-isolation)
- [02 — Keyed Brownian tree](../02-keyed-brownian-tree)

## In scope

- Euler–Maruyama full Adler phase dynamics driven by ticket 02 noise.
- One authoritative unwrapped absolute phase; periodic evaluation only for sine, cosine, and angular distance.
- Exact entry/exit splitting with `boundary_phase` at equality and `stable_phase` only in the strict interior.
- Continuous lifted target and unwrapped error through entry, eligible evolution, exit, and re-entry.
- `commitment.py` timestamp dwell with strict proximity and local-contraction predicates.
- Central-clock control and fixed-contraction width-only control with full Adler drift while ineligible.
- S1 deterministic-limit, S2 synthetic state-machine, and S4 one-clock stochastic experiments.

## Out of scope

- Multiple-clock first-winner races, killed-diffusion oracle, moving-band bridge audit, production statistics, or a physical interpretation of commitment beyond this phase-only control.

## Requirements

1. Zero noise reduces exactly to deterministic Euler and reproduces the calibrated pulse behavior within its stated order.
2. Eligibility equality is a zero-duration handoff: finite boundary phase, no dwell, no noise consumption, and no phase change.
3. The identity `absolute phase = lifted target + unwrapped error` holds throughout every eligible segment without discarding winding.
4. Ineligible width-control steps equal full Adler steps for identical state and noise. Only eligible contraction is replaced by the one manifest-frozen rate.
5. The first qualifying endpoint starts `inside_since` with no retroactive credit. Every band exit, contraction loss, or eligibility loss clears it.
6. Strict equality at the proximity or contraction boundary earns no dwell.
7. Dwell shorter than, equal to, or non-integral relative to timestep uses the same timestamp rule.
8. No analytic prediction, amplitude square, or prescribed hazard reaches the dynamics or state machine.

## Acceptance criteria

- Exact-entry/exit/re-entry tests pass for both mismatch signs, zero mismatch, both sides of the circular cut, accumulated winding, error excursions beyond one turn, and zero diffusion.
- Calling strict `stable_phase` at equality fails a mutation test rather than seeding a not-a-number lift.
- Brownian substeps use ticket 02 leaves and preserve full/control pairing.
- Synthetic dwell sequences cover initial-inside state, exit on the prospective commit step, falling-edge loss, wrap crossing, repelling point, expanding side, and tongue-edge coalescence.
- Central-clock and width-only processes produce labeled raw one-clock event records but no scaling claim.
- Mutations that wrap authoritative state, drop the lift, use free mismatch outside the tongue, scale dwell/rate/noise with coupling, or remove contraction fail.
- The canonical verifier passes with every earlier residual unchanged.

## Handoff

Provide a plain-English state-transition walkthrough, exact boundary conventions, the fixed-rate derivation rule, one-clock example ledgers, all new checks, and explicit non-claims. Do not describe a commitment as a detector click or Born outcome.
