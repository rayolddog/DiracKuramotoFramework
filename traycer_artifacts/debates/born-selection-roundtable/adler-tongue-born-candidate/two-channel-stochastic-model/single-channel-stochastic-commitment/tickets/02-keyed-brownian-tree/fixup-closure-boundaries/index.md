---
title: "Closure fix-up — canonical mesh routing and safe tree APIs"
kind: ticket
status: 2
---

# Closure fix-up — canonical mesh routing and safe tree APIs

## Parent and evidence

- [Ticket 02](..)
- [First fix-up](../fixup-review-findings)
- [Independent review](../independent-review)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Close the five current geometry/API/documentation defects without changing the effective white-noise law, v2 key schema, statistical thresholds, or out-of-scope boundaries.

## Required changes

### 1. One canonical mesh-boundary rule

- A crossing at a finest-grid boundary must belong to exactly one step for every accepted finite origin/step combination, including non-dyadic decimal meshes.
- Do not independently recompute an earlier step's end and a later step's start in ways that can overlap or leave a floating gap.
- Define one canonical boundary representation/routing rule based on the frozen mesh and integer step index, and use it in all elementary-leaf, streaming, split-node, and coarse aggregation paths.
- Reproduce `FinestMesh(1.0, 0.1)` at the crossing `1.2`, plus cases with the opposite rounding direction, large indices, negative origins, exact starts/ends, adjacent windows, and multiple boundary crossings. Each identity must route once, create no spurious tiny child, and remain stable under window partition/order.

### 2. Remove the unsafe public uniform coarse choice

- A caller of the public refinement API must not be able to aggregate a crossing-bearing window through an unsplit-root path.
- Make root-only coarse aggregation private/test-only, or require an exact validated no-crossings proof/token that cannot be supplied for a crossing-bearing window.
- Retain one public coarse API that always consumes the frozen crossing schedule and aggregates the exact chronological `TreeLeaf` sequence used by fine paths; an empty schedule covers the uniform case.
- Update all internal callers, exports, documentation, API validation, and mutations accordingly.

### 3. Tree-owned split-node identity

- Do not expose a public function that accepts a freely supplied `node_path` independently from node start/end/kick.
- Use an immutable node/leaf object produced and validated by the tree walk, or keep the arithmetic operation private and expose only the complete tree traversal.
- Two different node geometries must never reuse one canonical split key; forged ancestry/endpoints must fail before RNG consumption.
- Cover nested left/right ancestry, repeated crossings, and the reviewer's two `node_path='R'` geometries.

### 4. Canonical leaf-key parsing

- `leaf_from_key` must accept only the exact canonical spelling emitted by `leaf_key`.
- After parsing, reconstruct the canonical key and require byte-for-byte string equality.
- Reject leading zeros, explicit plus signs, whitespace, alternate integer spellings, truncated/extended paths, and other aliases while preserving every emitted v2 key.

### 5. Documentation/API evidence synchronization

- Update README and any verifier detail strings to the actual public callable/invalid-call/parameter counts produced by the canonical verbose run.
- Add a check that the documented counts match the verifier's computed counts so they cannot silently become stale again.

## Acceptance criteria

- The exact `origin=1.0`, `step=0.1`, `crossing=1.2` reproduction routes the crossing once with no tiny duplicate child; opposite-rounding/gap controls also pass.
- Partitioning or reordering adjacent requested windows cannot change routing, leaves, or coarse values.
- No public root-only coarse path remains usable on a crossing-bearing window.
- No public caller can pair one ancestry path with two different node geometries or reuse a split key through forged node data.
- Noncanonical leaf-key aliases reject; all emitted keys round-trip exactly.
- README/API counts are current and mechanically pinned.
- All 42 existing checks remain present, and new discriminating checks/mutations cover each fix.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, compile, raw-isolation, no-file/no-cube, and statistical paths pass.
- Prior deterministic residuals remain unchanged; v2 statistical law remains within frozen bounds; no tolerance is weakened.
- Nothing outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the canonical mesh routing rule, public API removals/signatures, immutable node ownership design, parsing rule, new probes/mutations, commands/results, compatibility effects, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this fix-up.
