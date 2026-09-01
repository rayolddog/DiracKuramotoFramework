---
title: "Ticket 03 stale-path snapshot fix-up"
kind: ticket
status: 2
---

# Ticket 03 stale-path snapshot fix-up

## Objective

Close the final stale-object defect found by the [independent review](../independent-review): a post-construction mutation may not combine new public path fields with old cached tongue geometry.

## Required fix

At the `run_one_clock` execution boundary, rebuild and validate the complete `ClockPath` snapshot before any key or Brownian leaf is requested. Reconstruct nested drive values rather than trusting a previously validated frozen container. Require the freshly derived schedule to equal the cached schedule exactly, then execute only the rebuilt snapshot or reject the stale object.

The validation must cover at least:

- mutated detuning;
- mutated pulse/train or stationary drive values;
- mutated model and fixed rate;
- mutated cached schedule;
- malformed nested drive members.

Every refusal must happen before any physical key or leaf derivation. Clean pulsed/stationary, full/width-only controls must remain bit-identical.

## Verification

Reproduce the reviewer's `0.9 -> 0.1` stale-detuning record before the fix and retain it as a regression test. Add discriminating mutations for each stale field and nested drive seam. Preserve all 73 prior checks and residuals/tolerances, all earlier closure findings, the v3 noise schema, raw isolation, no-file/no-cube behavior, and explicit non-claims. Run the complete canonical/verbose/direct/warnings/failure/compile/hash-seed/validation/mutation matrix.
