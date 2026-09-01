---
title: "Ticket 04 fix-up round 2 — independent series, regime gates, paired uncertainty, and schema"
kind: ticket
status: 2
---

# Objective

Close the four remaining findings from the round-1 closure review while preserving every confirmed closure: probability-domain protection, bounded memory, canonical audit interval identity, zero-diffusion boundary precedence, raw isolation, reset-only replay, unit-separated position ladders, and all non-claims.

## Governing review

- [Independent Ticket 04 review](../independent-review)
- [Round-1 fix-up](../fixup-review-round-1)

## Required corrections

### 1. Make series convergence discriminating

- Replace the `terms` versus `terms/2` comparison with a convergence test that cannot alias through the zero-drift odd/even parity structure.
- The exact reproduction `drift=0`, `terms=2`, `tolerance=1e-12` must refuse; its approximately 0.02939 error against a resolved high-term result must be exposed.
- Use at least two genuinely nested, non-aliased truncations or a defensible tail bound. Include the chosen term counts and residual/error estimate in the returned evidence.
- Test zero drift, both drift signs, near-boundary starts, short times, low and high term counts, and resolved controls. Add mutations for parity aliasing and false convergence.

### 2. Gate every reduced-matrix regime

- Treat the pooled moving-audit ladder only as an aggregate display, never as a substitute for per-regime accuracy.
- Give every frozen matrix cell its own convergent-observable ladders, uncertainties, and declared caps, including commitment probability, survival at declared times, and commitment-time distribution/quantile behavior.
- A cell whose finest commitment-probability shift is 0.125 against a 0.10 cap must produce `numerical_no_result`; it cannot be hidden by pooled results.
- Reassess the p20 quantile because its standard errors are larger than the measured shifts. If the reference sample cannot resolve it, the correct result is `numerical_no_result`, not pass. Do not widen a cap after seeing the data.
- Keep added-reset counts diagnostic and ungated; they cannot rescue any failed regime.

### 3. Derive paired uncertainty from frozen raw cluster data

- Do not accept caller-supplied marginal standard errors as authoritative inputs to `compare_refinement`.
- Freeze or bind the paired cluster-level differences, master-trial identities, audit-replication structure, resampling keys, and estimator algorithm to the comparison digest/report, then compute the paired uncertainty internally.
- Use the standard error of the paired difference or a cluster bootstrap of the paired contrast, not `hypot` of marginal errors.
- The review reproduction `0.010 -> 0.040 -> 0.009` must have one verdict under one frozen dataset/contract and cannot switch from no-result to pass when a caller changes a scalar SE.
- Remove or recompute the stale probability floor that cites 1/72; all granularity and uncertainty statements must match the actual 40 master trials × 3 clocks × 4 replications design.
- Add mutations for forged SEs, altered cluster membership/order, changed resampling key, changed estimator, and stale sample-size floors.

### 4. Version the report schema honestly

- The breaking report additions—unit-separated envelopes, positions, standard errors, and clusters—must use a new schema version.
- Update serializer/parser expectations, README, frozen fixtures, and mutation tests. A v1 consumer must not silently accept the new shape, and a current parser must refuse ambiguous or mismatched schema declarations.

## Verification contract

- Preserve all currently passing checks unless a check is strengthened in place; report any renamed/replaced row explicitly.
- Add direct reproductions and discriminating controls for all four findings.
- Run canonical, verbose, direct-script, warning-as-error, deliberate-failure, compile, hash-seed reproducibility, raw-isolation, no-file, and measured-memory paths.
- Do not alter the physical Brownian tree, Ticket 03 event law, or audit v2 interval identity.
- Make no exponent, population-outcome, detector-measurement, or Born-rule claim.

## Completion gate

Round 2 is complete only after the same independent reviewer returns `CLOSED`. If the present sample cannot resolve a per-regime or quantile gate under predeclared rules, report `numerical_no_result`; do not tune the reference budget to manufacture a pass.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 77 s, peak RSS 616 MB. Of the 84 rows shared
with the round-1 suite, **83 carry byte-identical residuals**; the only mover is
the memory row, whose residual is a measured RSS and which grew because the
per-regime matrix runs more work. One row was renamed in place (the audit gate,
whose scope widened to per-regime). **No cap was widened anywhere** — the S3
caps are the round-1 numbers, now applied to a stricter uncertainty-aware bound.

### 1 — Series parity alias

Replaced the `terms` vs `terms // 2` comparison with a **rigorous tail bound**,
derived in `series_truncation_bound`'s docstring from `weight_n <= 2/(n pi)`,
`|sin| <= 1` and `SUM_{n>N} exp(-a n^2) <= exp(-a N^2)/(2 a N)`. The nested gap
is retained at a step of **two** — which always drops an odd mode, so it cannot
alias the zero-drift parity structure — and is reported as corroborating
evidence. Both must fit inside the declared budget.

On the review's exact reproduction: nested gap **exactly 0.0**, tail bound
**0.109635**, true error **0.029390**. The evaluation is refused, and the raise
names which test refused it. The check asserts the gap is exactly zero (the
alias is reproduced) and that the bound exceeds the true error (it is a bound).
Resolved controls pass at both drift signs, zero drift, near-edge starts and
moderate/late times; both absorbing edges are pinned to exact zero.

### 2 — Per-regime gating

Every one of the fifteen frozen cells now has its own ladders for all five
convergent observables, its own cluster bootstrap, and **the same frozen caps as**
**the pooled ladder**. Matrix trials raised from 6 to 12.

**Both the pooled ladder and the per-regime ladders return**
**`numerical_no_result`.** The pooled blocker is exactly the one the review
predicted: the p20 commit-time shift is 0.0112 with a bootstrap standard error
of 0.0829, so its 2-sigma bound is 0.177 against the 0.10 cap. Fourteen of
fifteen regimes are blocked, 33 reasons in total. No cap was widened to avoid
this.

`check_audit_subset` passes, and what it asserts is the machinery plus honest
reporting: a no-result is a scientific outcome, but a no-result whose reasons
are about the machinery (missing sample, wrong unit, schedule or cluster
mismatch) is refused. The verdict label is computed from the verdict, so the
check now prints `REFERENCE-BUDGET MECHANISM TEST -- numerical no-result`.
Added-reset counts remain ungated with `require_decrease=false`.

### 3 — Paired uncertainty from frozen data

`compare_refinement(dataset, budgets, declared_digest)` now takes a
`ValidationDataset` of hashed cluster-level observations and computes the
statistic, the bootstrap and the verdict internally. **There is no**
**standard-error argument**; the old level-sequence signature raises with a
message naming the substitution it used to permit.

- The estimator (`mean` / `quantile`) and its level moved into the frozen
budget; the resampling **seed** and resample count into the frozen sampling
design. All are in the digest.
- One resample of clusters is evaluated at *every* level, so the paired contrast
is genuinely paired. `hypot` of marginal errors is gone. On a
cluster-common-scatter fixture: marginal SE **0.052**, paired SE **6.2e-17**.
- The bootstrap resamples the **signed** estimate and the comparison folds
afterwards, because folding first destroys the pairing wherever the signed
error can cross zero.
- The finest-level absolute cap is applied to `|error| + coverage * SE`.
- The review's `0.010 -> 0.040 -> 0.009` is `numerical_no_result` and stays
there under added dispersion.
- The stale floor is gone: the commitment-probability floor is **0.010** against
the actual 40x3 granularity of 0.0083, and the check asserts the relationship
and that the old 0.030 is not still present.
- New mutations: reordered clusters (digest moves), changed resampling key (SEs
move), swapped estimator (digest and measured values move), undeclared cluster
count (refused), caller-built levels (refused).

### 4 — Schema

`VALIDATION_SCHEMA` is **`dk-numerical-validation/v2`**, with
`parse_validation_report` refusing a v1 tag, a missing tag, a v1 scalar
`envelope` beside the v2 plural ones, a missing `dataset_digest`, a level
missing its `paired_error`, and a non-mapping payload. The report gained
`dataset_digest` and per-level `paired_error`. README, API table and mutations
updated.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 77 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical (memory row is a measurement) |
| `/usr/bin/time -l` | 616,284,160 B max RSS |
| raw-run subprocess | `analytic`, `killed_diffusion`, `moving_band_audit` all absent |
| result files written | none |

### Preserved

Memory bound, PDE Courant guard and probability-domain validation, audit v2
interval identity, physical Brownian pairing, per-unit/per-position ladders,
zero-diffusion precedence, raw isolation, reset-only replay, edge-resolved
first-absorption clarification, and every non-claim. No exponent, population,
detector-measurement or Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
