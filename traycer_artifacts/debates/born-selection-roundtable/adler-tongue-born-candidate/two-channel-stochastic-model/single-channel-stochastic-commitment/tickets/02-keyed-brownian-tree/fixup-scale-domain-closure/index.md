---
title: "Scale-domain closure — preserve the Gaussian law"
kind: ticket
status: 2
---

# Scale-domain closure — preserve the Gaussian law

## Parent and evidence

- [Ticket 02](..)
- [Numerical-law fix-up](../fixup-duration-law)
- [Independent review](../independent-review)

Code scope remains `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Define and enforce a numerically honest Brownian-scale domain: accepted positive scales must be normal finite floating-point values whose Gaussian law is not destroyed by subnormal quantization. Remove the legacy overflow-prone constructor check and correct v2-era documentation.

## Required changes

### 1. Reject subnormal output scales before randomness

- A mathematically positive Brownian root or conditional split scale that would be subnormal or unrepresentable as a normal finite binary64 value must fail before key/RNG derivation.
- Apply the same policy to roots, irregular children, and bridge/split scales; do not allow a proportional deterministic-looking split to emerge because the stochastic correction rounded away.
- Preserve accepted cases where one input is subnormal but the resulting scale is normal and accurately representable, such as `diffusion = ulp(0), duration = 1`.
- Reproduce and reject `diffusion = ulp(0), duration = ulp(0)` before randomness. Retain exact no-key zeros only for mathematically exact zero diffusion or zero duration.
- Use a genuinely independent high-precision reference (`decimal`, `fractions`, integer exponent analysis, or equivalent) that does not round through the implementation's binary64 result before comparison.
- Add a root-distribution discriminator showing why the formerly accepted both-subnormal case violates the high-precision target law; the rejection test must replace, not conceal, that evidence.

### 2. Overflow-safe constructor/domain validation

- Remove all left-associated `2 * diffusion * duration` acceptance tests that can overflow before multiplication by a small duration.
- Validate the nominal configured scale with the same stable scale-domain helper used at generation, while still validating every realized step/window separately.
- Accept `diffusion = DBL_MAX, nominal duration = 0.25` and `diffusion = 1e308, duration = 0.1` when the stable resulting scale is normal and finite.
- Reject `diffusion = DBL_MAX, duration = DBL_MAX` and all genuinely overflowing/unrepresentable scales before RNG.
- Cover neighboring accepted/refused thresholds and exact exception conventions.

### 3. Correct semantic documentation

- Correct `FinestMesh.step_bounds` documentation so realized widths—not the nominal step—drive variance and splits.
- Correct `PhaseNoiseStream` documentation so it describes the stable normal-scale domain rather than the removed product check.
- Strengthen documentation verification with required current statements or forbidden legacy phrases so semantic regressions are caught, not merely removed method names.

## Acceptance criteria

- The both-subnormal public root and split cases reject before any key/RNG call; the former quantized distribution failure remains recorded as a discriminating control.
- One-subnormal-input and ordinary/tiny-normal-output cases retain correct nonzero randomness and high-precision scale agreement.
- Representable large cases (`DBL_MAX × 0.25`, `1e308 × 0.1`) accept; genuinely unrepresentable cases reject.
- Stable-scale acceptance/refusal is consistent in constructor, root, split, tree, stream, and coarse paths.
- Exact zero diffusion/duration still yields bit-exact zeros with no key consumption.
- v3 key grammar remains unchanged; accepted keyed values remain unchanged in this round.
- Semantic v3 documentation is current and mechanically guarded.
- All 50 existing checks remain present; new independent and mutation probes cover every fix.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, compile, raw-isolation, no-file/no-cube, and statistical paths pass.
- Prior deterministic residuals remain unchanged; no tolerance is weakened.
- Nothing outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the exact accepted scale interval, stable validation algorithm, high-precision reference, rejected quantization evidence, new probes/mutations, documentation guards, commands/results, compatibility effects, and remaining limitations. Ticket 02 remains open until the same independent reviewer closes this fix-up.
