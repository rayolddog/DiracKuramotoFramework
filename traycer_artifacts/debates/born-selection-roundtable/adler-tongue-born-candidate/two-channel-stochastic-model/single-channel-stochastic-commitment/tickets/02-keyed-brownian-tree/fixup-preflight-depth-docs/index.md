---
title: "Closure patch — eager depth validation and exact domain wording"
kind: ticket
status: 2
---

# Closure patch — eager depth validation and exact domain wording

## Parent and evidence

- [Ticket 02](..)
- [Scale-boundary fix-up](../fixup-scale-boundaries)
- [Independent review](../independent-review)

Code scope remains `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Make the complete schedule preflight enforce every existing tree-validity rule before randomness, including maximum depth, and make all domain documentation consistently state the exact half-open upper bound.

## Required changes

### 1. Eager maximum-depth validation

- At each public schedule boundary, route and bucket crossings by requested finest step before any parent or split key can be derived.
- Enforce the existing `_MAX_NODE_DEPTH` rule from those buckets during the same eager preflight used for root and bridge scales.
- Reuse the validated per-step buckets during materialized, streamed, and coarse generation rather than repeatedly rescanning the full crossing schedule.
- A schedule with too many unique crossings in the first or a later step must fail at API call time with zero keys consumed. Generator-returning APIs must fail before returning a generator.
- Add discriminating probes for invalid first-step and later-step schedules across `elementary_leaves`, `stream_elementary_leaves`, and `coarse_kicks`; include a valid schedule exactly at the declared maximum depth.
- Preserve all duplicate-identity, routing, geometry, scale, and chronological-order checks.

### 2. Exact domain wording and guards

- State the exact mathematical target interval consistently as `[MIN_NORMAL, sqrt(DBL_MAX))`, with an open upper end.
- Separately describe the conservative requirement that the computed binary64 scale must also lie inside the representable policy.
- Remove the obsolete DBL_MAX upper literal and all claims that both ends are closed or that exact targets on both bounds are admitted.
- Extend semantic guards to require the current half-open statement and forbid each stale phrase/bracket form.

## Acceptance criteria

- First-step and later-step depth-invalid schedules fail at API call time with zero key/RNG consumption for materialized, generator, and coarse paths.
- A valid schedule at exactly `_MAX_NODE_DEPTH` succeeds and retains chronological leaves/conservation.
- Preflight/generation uses the same routed buckets; arbitrary windows and partitions remain invariant.
- Source and README consistently state the lower-closed/upper-open mathematical target interval and computed-scale conjunction.
- All 54 existing checks remain; new direct/mutation controls cover both fixes.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, compile, raw-isolation, no-file/no-cube, and statistical paths pass.
- v3 keys and all still-accepted values remain unchanged; prior deterministic residuals and numerical boundaries remain unchanged; no tolerance is weakened.
- Nothing outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the bucket/preflight algorithm and complexity, depth probes/key counters, documentation guards, commands/results, compatibility effects, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this patch.
