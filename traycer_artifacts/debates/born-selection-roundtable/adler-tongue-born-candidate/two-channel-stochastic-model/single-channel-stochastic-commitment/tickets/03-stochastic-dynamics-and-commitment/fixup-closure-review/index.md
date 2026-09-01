---
title: "Ticket 03 closure-review fix-up"
kind: ticket
status: 2
---

# Ticket 03 closure-review fix-up

## Objective

Close the two remaining public bypasses identified in the [closure re-review](../independent-review). Five original findings are already independently closed and must remain closed.

## Required fixes

1. The ordinary production `ClockPath` → `run_one_clock` → `OneClockRecord` path must require the one frozen width-control contraction rate. An alternate rate may not run under an ordinary S4 label or produce an ordinary primary record. If sensitivity support is retained, it must use a distinct structured type/factory and a durable sensitivity identity in the record; otherwise keep arbitrary-rate helpers private.
2. Enforce the state machine's exact entry/reset/live conservation at public constructors:
  - `band_entries == dwell_resets + int(inside_since is not None)`;
  - `ever_inside == (band_entries > 0)`;
  - unreachable historical flags/counts are refused.
3. Enforce corresponding record conservation:
  - `band_entries - dwell_resets` is zero or one;
  - committed records have exactly one live/unreset entry;
  - `never_eligible` and `lock_failed` have zero entries and resets;
  - stationary records have zero boundary endpoints;
  - ordinary width-only records carry the frozen scalar exactly.

## Verification

Reproduce the reviewer's arbitrary-rate trajectories and all listed unreachable states first. Add a valid reachable control beside every refusal and mutations that remove each new relation. Preserve all 71 prior checks and their residuals/tolerances without weakening. Re-run the complete canonical, isolation, no-file/no-cube, validation, warnings, direct, failure, compile, hash-seed and mutation matrix.

Keep changes inside `adler_born_two_channel/`; preserve the v3 noise schema, stationary and pulsed S4 matrices, lift/dwell/tolerance fixes, and all explicit non-claims.
