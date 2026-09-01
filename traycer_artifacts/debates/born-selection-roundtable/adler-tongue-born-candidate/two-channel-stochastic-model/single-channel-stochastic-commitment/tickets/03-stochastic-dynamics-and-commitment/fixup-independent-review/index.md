---
title: "Ticket 03 independent-review fix-up"
kind: ticket
status: 2
---

# Ticket 03 independent-review fix-up

## Objective

Close the seven public-contract defects found by the [independent review](../independent-review) without weakening the accepted one-clock dynamics, Ticket 01 isolation, or Ticket 02 Brownian-tree contracts.

## Required fixes

1. Make timestamp dwell numerically faithful at binary64 equality, track the last processed endpoint, reject duplicate/backward observations, and reject a commitment time before `inside_since`. The equality allowance must be scale-aware and only coalesce roundoff-sized differences; it must not grant a materially early dwell.
2. Implement S4's nonzero stationary-coupling half for central, interior, and near-edge clocks at zero/weak/intermediate/strong noise, for full and width-only dynamics, without building the killed-diffusion oracle or stationary-hazard experiment.
3. Remove caller-selected `fixed_rate` from the primary raw width-control factory. Derive the provisional/manifest-frozen scalar in one place. Make the geometric-midpoint derivation overflow/underflow safe and reject any non-finite or non-positive result. Do not add an unlabeled tuning bypass.
4. Preserve target-lift congruence for every accepted phase. Either retain an exact winding representation or enforce and document an angular-resolution domain before the phase becomes too coarse; add adjacent accepted/refused magnitude and congruence probes.
5. Align the raw configuration and lock factory on strict `0 < lock_tolerance < pi`, including exact-`pi` probes through every raw factory.
6. Enforce state/record cross-field invariants: time ordering, category/commitment agreement, eligibility/entry implications, `resets <= entries <= eligible_endpoints`, endpoint subtotals, and the full/width fixed-rate convention. Keep a valid control beside every invalid relation.
7. Replace `raw_runner.py`'s Ticket-01-era “no stepper/dwell/commitment” prose with the current one-clock boundary and the still-true exclusions.

## Verification

- Reproduce every exact reviewer probe before changing code and retain it as a regression test with discriminating controls.
- Add stationary S4 records without weakening or removing the pulsed matrix.
- Preserve all 65 prior checks and every prior residual/tolerance; no tolerance may be weakened.
- Re-run canonical, verbose, direct-script, warnings-as-errors, deliberate-failure, compile, two hash seeds, raw transitive isolation, no-file/no-cube, public API validation, and mutation paths.
- Keep all changes inside `adler_born_two_channel/`; do not stage, commit, revert, or modify unrelated files.

## Compatibility and non-claims

Document API changes, especially the removal of caller-selected raw fixed rates and any new phase-resolution boundary. Preserve the v3 noise schema and accepted keyed values. Do not add a population race, disk ledger, oracle/audit, stationary hazard, scaling analysis, detector-click language, outcome, or Born claim.
