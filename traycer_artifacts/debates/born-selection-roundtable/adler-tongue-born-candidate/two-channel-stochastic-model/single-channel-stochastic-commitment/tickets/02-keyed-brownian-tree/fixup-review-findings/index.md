---
title: "Fix-up — close keyed Brownian tree review findings"
kind: ticket
status: 2
---

# Fix-up — close keyed Brownian tree review findings

## Parent and evidence

- [Ticket 02](..)
- [Independent review](../independent-review)
- [Ticket 01 isolation boundary](../../01-raw-process-isolation)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Close the five bounded correctness and public-boundary defects found by independent review without changing the effective-white-noise model, weakening the statistical checks, or implementing drift, commitment, outcomes, or analytic prediction.

## Required changes

### 1. Canonical elementary-leaf identity

- Separate the private 1,024-value block seed from the public elementary-leaf address.
- `leaf_key(trial, clock, index)` must uniquely identify each finest-grid step, including all offsets inside a block, while retaining the block generation optimization.
- State clearly whether existing keyed values are preserved or the key schema version changes.
- Verify uniqueness across a complete block and adjacent block boundaries, plus deterministic reconstruction of the value from the public address.

### 2. Irregular elementary-leaf coarse aggregation

- Add a bounded/streamed API that accepts frozen per-step crossings or the exact `TreeLeaf` stream used by the fine consumer.
- Coarse increments must be sums of the same chronological irregular leaves on the finest uniform grid union exact crossings—not separately generated unsplit roots.
- Cover multiple crossings in multiple finest steps, arbitrary request windows, multiple coarse strides, and conservation against the exact same leaf sequence.
- Do not materialize the full trial-by-clock-by-time cube.

### 3. Geometry-safe public split boundary

- Prevent callers from supplying a fraction inconsistent with `Crossing.time` or a crossing outside the parent node.
- Prefer one public geometry-validating operation that derives the fraction from exact node start/end; keep any arithmetic-only helper private.
- Reject the reviewer's out-of-parent and mismatched-fraction examples at the public boundary, including nested node intervals.

### 4. Representable numerical range

- Reject or safely handle finite inputs whose declared variance/scale would overflow or become non-finite.
- `leaf_scale`, split scales, generated kicks, and `conservation_tolerance` must remain finite for every accepted input.
- Replace endpoint-overflow-prone spacing with a finite ULP calculation such as `math.ulp`, with an explicit finite result check.
- Test maximum float, near-maximum representable accepted/rejected boundaries, overflow products, subnormals, large cancellation, and ordinary regimes.

### 5. Clock identifier range

- Prevent unsigned arrays above the supported signed identifier range from wrapping during conversion.
- Make scalar and vector clock-ID domains agree, or explicitly widen both to a shared exact grammar without lossy casts.
- Test `2**63 - 1`, `2**63`, and `2**64 - 1`, plus mixed arrays and ordinary values.

## Acceptance criteria

- All five independent reproductions fail before the fix and pass after it.
- Public leaf addresses are unique per elementary kick and reconstruct the assigned value.
- Coarse irregular increments are derived from the exact `TreeLeaf` sequence consumed by fine paths.
- Invalid split geometry cannot reach key derivation or random-number consumption.
- Every accepted numerical input produces finite scales/tolerances/kicks; rejected overflow cases fail with established exception conventions.
- Unsigned clock arrays cannot wrap to negative serialized identifiers.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, and compile paths pass.
- All 38 existing checks remain present; prior deterministic residuals and raw isolation remain unchanged; no tolerance is weakened.
- No generated cube or persistent result file is written; nothing outside the package changes.

## Completion

Report exact API/signature/schema changes, compatibility effects, new probes and mutation evidence, statistical samples/tolerances, memory behavior, command results, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this fix-up.
