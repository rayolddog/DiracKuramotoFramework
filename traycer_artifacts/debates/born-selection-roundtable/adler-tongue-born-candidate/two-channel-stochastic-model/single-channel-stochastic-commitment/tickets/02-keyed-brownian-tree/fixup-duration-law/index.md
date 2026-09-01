---
title: "Numerical-law fix-up — realized durations and stable Brownian scales"
kind: ticket
status: 2
---

# Numerical-law fix-up — realized durations and stable Brownian scales

## Parent and evidence

- [Ticket 02](..)
- [Canonical-routing fix-up](../fixup-closure-boundaries)
- [Independent review](../independent-review)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Make one physical duration law govern root kicks, conditional splits, `TreeLeaf` records, and coarse consumers across ordinary, large-origin, subnormal, and cancellation regimes. Refuse unresolvable physical windows before any random key is consumed. Update stale source documentation.

## Required changes

### 1. One duration representation for the whole tree

- For every accepted finest step, obtain its physical start, end, and duration from the same canonical `FinestMesh.step_bounds(index)` representation used for routing.
- Scale the root kick with that realized positive duration, not the separately declared nominal step when they differ in floating-point representation.
- Every child duration and split fraction must be derived from that same parent interval; `TreeLeaf.duration`, root variance, child variances, sibling covariance, and coarse aggregation must agree with it.
- Reproduce `FinestMesh(1e15, 0.2)`, whose first realized width is `0.25`, and independently verify the required parent/child moments and zero sibling covariance through the public tree API.
- Because this changes keyed kick values under existing v2 addresses, make the compatibility break visible with a key-schema/version bump unless an equally explicit, non-silent migration mechanism exists. No production dataset exists to migrate.

### 2. Underflow/overflow-safe Brownian scale

- Compute `sqrt(2 * diffusion * duration)` and conditional split scales without first forming products that can spuriously underflow to zero or overflow to infinity.
- Use a stable factorization/exponent method whose accepted result is finite and positive whenever the mathematically required scale is representable.
- Cover `duration = math.ulp(0), diffusion = 0.2`; `diffusion = math.ulp(0), duration = 1`; midpoint and near-endpoint splits; maximum/near-maximum finite inputs; subnormal results; and ordinary controls.
- If the required scale itself is not representable or the interval is not resolvable, reject before key/RNG derivation. Exact zero diffusion and exact zero duration remain bit-exact zeros with no key consumption.
- Tests must distinguish the corrected conditional split from the proportional-split mutation in these tiny regimes.

### 3. Validate physical windows before randomness

- Every public physical root/stream/tree/coarse path must validate all requested step intervals as finite, ordered, and positive-width before any keyed normal is generated.
- Reproduce `FinestMesh(1e16, 0.1)` and `FinestMesh(1e308, 1)`: requests must fail before key/RNG consumption rather than return plausible kicks from collapsed intervals.
- Include multi-step windows where a later step collapses, block boundaries, arbitrary partitions, empty requests, and valid large-origin controls.
- Make eager-versus-generator validation behavior explicit so errors do not appear only after partial random consumption.

### 4. Source documentation accuracy

- Remove or correct stale docstrings referring to removed `coarse_kicks_over_crossings` or describing the current public `coarse_kicks` as uniform-only.
- Add a source/documentation assertion that public method names and the refinement narrative match the actual exported API.

## Acceptance criteria

- Public moment checks at origin `1e15`, nominal step `0.2`, realized width `0.25` match the realized-duration Brownian law; the old nominal-duration law fails a discriminating control.
- Tiny positive-duration/diffusion cases retain nonzero physical randomness and correct conditional moments when the scale is representable.
- Unresolvable windows fail before key/RNG consumption on every public physical generation path.
- Zero diffusion/duration behavior remains exact and consumes no key.
- Any changed key-to-kick mapping has an explicit schema/version bump and documentation; no silent v2 change.
- Stale source API references are removed and mechanically guarded.
- All 46 existing checks remain present; new independent/mutation controls cover each fix.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, compile, raw-isolation, no-file/no-cube, and statistical paths pass.
- Prior deterministic residuals remain unchanged; no statistical tolerance is weakened.
- Nothing outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the exact realized-duration rule, stable-scale algorithm and accepted domain, schema compatibility change, eager validation design, new statistical samples and mutation evidence, commands/results, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this fix-up.
