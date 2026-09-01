---
title: "Reject negative coupling histories in Trajectory"
kind: ticket
status: 2
---

# Reject negative coupling histories in Trajectory

## Defect

An exported `simulate.Trajectory` accepts a same-shape negative coupling history and then returns plausible ineligible/undefined-lock diagnostics.

## Required fix

- Validate `Trajectory.coupling` with the nonnegative-array validator at construction.
- Add a direct same-shape negative-coupling constructor regression probe.
- Ensure the valid zero/nonnegative trajectory cases remain accepted.
- Correct any README or verification claim that overstates generic domain completeness; the present mechanism covers declared probes per parameter, not every possible value class automatically.
- Do not change physics kernels, weaken tests, or modify files outside `adler_born_two_channel/`.

## Completion

The reviewer's exact negative-history probe rejects clearly, all prior checks pass unchanged, and the independent reviewer reports no concrete current defect.
