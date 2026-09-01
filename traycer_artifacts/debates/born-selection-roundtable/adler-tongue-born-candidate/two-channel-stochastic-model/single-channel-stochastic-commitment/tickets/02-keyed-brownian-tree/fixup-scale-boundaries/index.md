---
title: "Scale-boundary fix-up — finite kicks and keyless schedule refusal"
kind: ticket
status: 2
---

# Scale-boundary fix-up — finite kicks and keyless schedule refusal

## Parent and evidence

- [Ticket 02](..)
- [Normal-scale policy](../fixup-scale-domain-closure)
- [Independent review](../independent-review)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Guarantee that every accepted physical scale produces finite ordinary keyed kicks, that every complete crossing schedule is scale-valid before any parent or split key is consumed, and that lower/upper scale-boundary decisions follow the exact mathematical target rather than a rounded binary64 proxy.

## Required changes

### 1. Conservative finite-kick upper domain

- Replace the erroneous maximum accepted scale of `DBL_MAX` with a conservative upper scale no larger than `sqrt(DBL_MAX)` or an independently justified bound that guarantees ordinary keyed-normal multiplication cannot overflow.
- Preserve acceptance of `diffusion = DBL_MAX, duration = 0.25` and `diffusion = 1e308, duration = 0.1` when their scales fall inside the corrected domain.
- Reject `diffusion = duration = DBL_MAX / 2` and neighboring truly above-boundary cases before any key/RNG call; no public array, stream, tree, or coarse path may emit `inf` or a runtime warning for accepted inputs.
- Correct every source/README claim about the maximum accepted scale and pin it mechanically.

### 2. Eager whole-schedule scale validation

- Before drawing a parent root normal, prewalk every routed crossing/node in the requested schedule and validate all root and conditional bridge scales.
- Apply this eager preflight to materialized leaves, generator-returning streams, and coarse aggregation. A generator function must validate at API call time, not at first `next()`.
- Reproduce `diffusion = ulp(0)`, `duration = 1`, crossing at `ulp(0)`: refusal must occur with zero parent and zero split keys consumed.
- Cover later invalid crossings after valid earlier steps/nodes, multiple crossings, window partitions, and valid controls. No partial output or partial key consumption may precede refusal.

### 3. Exact mathematical boundary classification

- Do not classify a target as normal merely because the factored binary64 result rounded up to `MIN_NORMAL`, nor accept an upper target because it rounded down to the corrected maximum.
- Use exact float-ratio/integer-exponent comparison, high-precision arithmetic, or another production-safe method to classify the mathematical target `sqrt(2 * diffusion * duration)` against both domain boundaries without forming the unstable product.
- Add predecessor/exact/successor cases at the lower boundary, including the reviewer's `diffusion = ulp(0)`, `duration = nextafter(2**-971, 0)`, and analogous upper-boundary neighbors.
- Keep the independent Decimal verifier oracle and demonstrate it distinguishes all three sides.
- Document any deliberately conservative treatment of exact-boundary or rounded-neighbor cases.

## Acceptance criteria

- Every accepted public generation call returns finite kicks without warnings across the tested domain.
- The reviewer's large-scale public reproduction rejects before key/RNG; both previously required large-but-safe cases still accept.
- Invalid subnormal-bridge schedules reject at API-call time with zero root/split key consumption across leaves, stream, and coarse paths.
- Lower and upper predecessor/exact/successor targets receive the documented mathematically correct or explicitly conservative verdict.
- Exact zero diffusion/duration remains bit-exact and keyless.
- v3 key grammar and all still-accepted key-to-kick values remain unchanged.
- All 51 existing checks remain; new discriminating controls/mutations cover each fix.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, compile, raw-isolation, no-file/no-cube, and statistical paths pass.
- Prior deterministic residuals remain unchanged; no tolerance is weakened.
- Nothing outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the exact accepted scale interval and comparison algorithm, preflight traversal design, key-consumption evidence, boundary probes, corrected documentation, commands/results, compatibility effects, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this fix-up.
