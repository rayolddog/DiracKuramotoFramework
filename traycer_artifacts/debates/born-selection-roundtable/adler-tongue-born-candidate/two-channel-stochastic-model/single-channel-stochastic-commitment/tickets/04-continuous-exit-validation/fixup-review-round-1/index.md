---
title: "Ticket 04 fix-up — convergence, probability domain, audit identity, and memory"
kind: ticket
status: 2
---

# Objective

Close every actionable finding in the first independent review without weakening prior checks, changing the physical event law, or promoting the diagnostic audit into a physical mechanism.

## Governing review

- [Independent Ticket 04 review](../independent-review)
- [Execution decisions](../execution-notes)

## Required corrections

### 1. Freeze the scientific refinement contract

- Put the minimum level count and exact refinement schedule inside the immutable, hashed comparison contract.
- Remove or reject caller overrides that can admit two levels or non-halving schedules.
- Do not allow repeated sub-floor worsening. A single reversal may be treated as statistically unresolved only when the frozen dependence-aware uncertainty calculation supports that conclusion; otherwise return `numerical_no_result`.
- Include the sampling unit, master-trial clustering, auxiliary-replication structure, and uncertainty method in the frozen contract and exported report.
- Add mutations for two-level override, non-halving steps, repeated sub-floor growth, altered clustering, and changed uncertainty rules.

### 2. Keep the stationary oracle inside the probability domain

- Add a defensible time-grid positivity/maximum-principle guard and validate all returned survival and edge-exit fields.
- The accepted coarse-grid reproduction from the review must refuse before returning a solution, or refine internally under a frozen rule.
- Reject any non-finite or out-of-range probability beyond a small numerical roundoff policy that is itself declared and tested; do not repair a materially invalid solution by clipping.
- Preserve the independently confirmed drift sign and edge orientation.

### 3. Make moving-band validation scientifically meaningful

- Retain the reset-only/pathwise-subset audit, but label its current budget run a mechanism smoke test until the new gates pass.
- Add survival differences at declared comparison times and a commitment-time distribution observable such as frozen quantiles.
- Preserve the shared-prefix history required to compute those observables.
- Export dependence-aware uncertainties based on master-trial clusters and auxiliary audit replications, and make the verdict consume them.
- Report the reduced matrix per regime, including central/interior/near-edge, mismatch sign, noise strength, and both pulse sides. Reachability alone is insufficient.
- Keep audit-added reset count as a nonconvergent diagnostic with `require_decrease=false`; it must not rescue failure of any convergent gate.

### 4. Bound verifier memory

- Stream or batch the S3 walkers and direct bridge simulations. Do not materialize sample-by-substep bridge cubes.
- Retain online hit counts and small live state only.
- Measure peak RSS or an equivalent bounded allocation metric and add a regression assertion/record. The 4.65 GB reproduction must be eliminated.

### 5. Give audit uniforms canonical interval identity

- Equal audit keys must imply equal physical bridge intervals across stride, window partition, pulse ordering, and refinement.
- Either key the canonical interval geometry/refinement identity or implement an explicit hierarchical parent/child audit-uniform construction.
- Preserve disjointness from physical Brownian keys and preserve physical histories when audit replication changes.
- Add the review's shared-key/different-geometry reproduction as a failing mutation.

### 6. Refuse unresolved short-time series values

- Give the constant-drift series an explicit truncation/convergence test, preferably using nested term counts under a declared budget.
- Refuse unresolved evaluations rather than returning negative or greater-than-one probabilities.
- Pin boundary values to zero and test zero and both nonzero drift signs, near-edge starts, short times, and resolved moderate/late controls.

### 7. Correct zero-diffusion bridge precedence

- Boundary equality or outside clearance must produce certain reset, or be rejected, before the interior zero-diffusion branch can return zero crossing probability.
- Add combined zero-diffusion/equality and zero-diffusion/outside tests to the public API contract.

### 8. Preserve units and per-position ladders

- Replace the mixed-unit scalar envelope with per-observable, per-position results carrying explicit units.
- Every initial position must have its own frozen ladder and pass independently before any display maximum is computed.
- Export the identity of the observable and position producing every reported maximum.
- Ticket 07 must receive dimensionally meaningful data; it may not compare one scalar mixing probabilities and time.

## Verification contract

- All prior 84 checks remain, with no weakened tolerance unless a documented correction makes the old quantity invalid; any such replacement must be independently discriminating.
- Add direct checks and mutations for all eight corrections.
- Re-run canonical, verbose, direct-script, warning-as-error, deliberate-failure, and compile paths.
- Verify raw-process isolation, no result-file writes, audit/physical namespace separation, and absence of exponent, detector-outcome, measurement, or Born claims.
- Report before/after peak memory and full numerical results.

## Completion gate

The fix-up is complete only after the same independent reviewer returns `CLOSED`. A passing reference budget may be described as a numerical validation pass only if every new frozen convergent gate passes; otherwise it must be labeled a mechanism smoke test or `numerical_no_result`.

## Implementation report — 2026-08-28

All eight findings were reproduced against the pre-fix code, then closed. The
canonical suite is **85/85**; the 79 rows shared with the pre-fix 84-row suite
carry **byte-identical residuals**, and the five rows that changed name are the
Ticket 04 checks whose scope this fix-up widened. No check outside Ticket 04 was
touched, and no tolerance was weakened.

| # | Finding | Reproduced before | State after |
| --- | --- | --- | --- |
| 1 | Frozen contract admits two-level / non-halving / systematic growth | all three returned `pass` | schedule, ratio, level count and sampling design hashed into the digest; `minimum_levels` override removed; non-halving and two-level contracts cannot be constructed; end-to-end + single-reversal + bootstrap-standard-error rules |
| 2 | Oracle returns non-probabilities | survival `−0.0043`, `upper_exit 1.0043`, closure `1.1e−16` | advective Courant guard refuses that grid; every returned field validated against `PROBABILITY_SLACK` and refused, never clipped |
| 3 | Moving-band pass is a smoke test | no survival gate, no distribution gate, no uncertainty | 5 gated observables (commitment probability, survival at 3 declared times, p20 commit-time quantile), cluster-bootstrap standard errors over master trials, 3 independently keyed clocks, 40 × 3 × 3 × 4, per-regime matrix results |
| 4 | 4.65 GB peak RSS | measured 4,653,875,200 B | **565,805,056 B**; both paths streamed; largest allocation 19.2 MB; asserted by `check_bounded_memory` |
| 5 | One audit key, several intervals | 265 shared keys with different geometry | canonical `float.hex` span in the key; 0 collisions; the v1 form is kept as a live reproduction |
| 6 | Series returns non-probabilities at short time | `−2.11`, `−15.75` | nested-truncation convergence test refuses unresolved evaluations; edges pinned to exact zero |
| 7 | Zero diffusion overrides certain absorption | returned `0.0` on and outside the edge | clearance clause moved ahead of the zero-diffusion branch; crossed cases in the API contract |
| 8 | Mixed-unit envelope, collapsed positions | one scalar over a time and three probabilities | per-observable, per-position, unit-bearing ladders (12 for S3); per-unit envelopes naming their observable and position; no scalar across units |

### Command matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 66 s |
| `... --verbose` | 85/85 |
| `python3 adler_born_two_channel/verify.py` | 85/85 |
| `python3 -W error -m ...verify` | 85/85 |
| `... --prove-failure-exit` | exit 1 |
| `python3 -m compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical; the memory row differs because its residual is a measurement of the machine |
| `/usr/bin/time -l` | max RSS 0.57 GB (was 4.65 GB) |

### Scope

Only `adler_born_two_channel/` and this artifact were modified. Nothing was
staged, committed or reverted; no result files were written. The edge-resolved
first-absorption clarification is preserved, the added-reset count remains a
non-convergent diagnostic that cannot rescue any gate, and no exponent,
detector-outcome, measurement or Born claim exists anywhere in the package.
