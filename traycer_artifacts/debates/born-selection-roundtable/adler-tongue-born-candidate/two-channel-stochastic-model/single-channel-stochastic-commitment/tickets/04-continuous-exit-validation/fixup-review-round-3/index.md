---
title: "Ticket 04 fix-up round 3 — stable series, transformed bootstrap, and strict report semantics"
kind: ticket
status: 2
---

# Objective

Close the three remaining defects without reopening the confirmed per-regime `numerical_no_result`, bounded-memory, PDE-domain, audit-identity, raw-isolation, or non-claim contracts.

## Governing review

- [Independent Ticket 04 review](../independent-review)
- [Round-2 fix-up](../fixup-review-round-2)

## Required corrections

### 1. Bound both truncation and floating-point evaluation error

- The series authority must account for truncation and numerical cancellation separately. A tiny analytic tail bound cannot certify a floating evaluation whose cancellation error is materially larger.
- Reproduce the accepted reflection-symmetry discrepancy: the positive- and negative-drift reflected evaluations differ by about `1.6306e-05` under a requested tolerance of `1e-6`, while the reported tail bounds are approximately `5.04e-210`.
- Use a numerically stable formulation, compensated/high-precision evaluation, a condition/error estimate, or a cross-representation check that can bound rounding/cancellation. Refuse when the total certified error exceeds tolerance.
- The public bound helper must obey its zero-time and domain contract, including boundaries, invalid starts, invalid term counts, and both drift signs.
- Add independent reflection-symmetry, high-precision-reference, cancellation-stress, near-edge, short-time, resolved-time, and mutation tests. Do not describe an analytic tail as a total error bound unless floating evaluation is included.

### 2. Bootstrap the exact statistic being gated and bind physical identities

- The gate compares folded absolute-error contrasts, so the bootstrap must resample and evaluate that same transformed statistic, or use a rigorously justified conservative bound that dominates it in every tested case.
- Reproduce the reviewer’s two-cluster counterexample where the current signed-contrast bootstrap reports zero standard error but the folded-contrast bootstrap is about `0.69939`.
- `PairedSample` must carry explicit immutable cluster/master-trial identities. The dataset digest must bind those identities, level membership, order/canonicalization policy, clock identities, audit-replication identities, and observations.
- Reject duplicate identities, missing/substituted identities, inconsistent identity sets across levels, and relabeling that changes physical provenance. If order is declared irrelevant, canonicalize before hashing and prove order invariance; otherwise reject reordering.
- Keep resampling keys, estimator, transformation, coverage factor, and resample count frozen. Add mutations for signed-vs-folded resampling, duplicate/relabelled clusters, substituted physical identities, and identity-set mismatch.

### 3. Make v2 reports semantically self-validating

- `parse_validation_report` must enforce cross-field invariants, not merely field presence.
- A report with `verdict = numerical_no_result` and `passed = true` must refuse. Define and enforce every allowed verdict/passed relationship.
- Digests must be nonempty, canonical, correctly sized hexadecimal strings; dataset and budget digests must be distinct fields with exact validation.
- Validate all level fields for finite values, allowed units, nonnegative standard errors, positive cluster counts, declared positions, schedule consistency, and coherent paired-error/error/reference relationships.
- Refuse empty/malformed levels, duplicate observable-position-level identities, missing required ladders, mixed schema versions, unknown fields if the schema claims a closed shape, and any payload that could let a downstream consumer bypass `numerical_no_result`.
- Round-trip canonical valid reports and add targeted parser mutations for each invariant.

## Verification contract

- Preserve the round-2 result: pooled and per-regime moving audits remain honest `numerical_no_result`; no cap may be widened.
- Preserve all closed findings and the measured bounded-memory behavior.
- Add direct reproductions and discriminating negative/positive controls for all three corrections.
- Run canonical, verbose, direct-script, warning-as-error, deliberate-failure, compile, hash-seed, raw-isolation, no-file, and memory paths.
- Make no exponent, population-outcome, detector-measurement, or Born-rule claim.

## Completion gate

Round 3 is complete only after the same independent reviewer returns `CLOSED`. A downstream consumer must be unable to turn the frozen `numerical_no_result` into a pass through parser ambiguity, forged identities, or underestimated transformed uncertainty.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 78 s, peak RSS 653 MB. Of the 85 rows shared
with round 2, **84 carry byte-identical residuals**; the only mover is the
memory row, whose residual is a measured RSS. No row was renamed. The pooled and
per-regime moving audits remain `numerical_no_result` with **unchanged caps**,
and the S3 stationary gate still passes.

### 1 — Series: truncation *and* floating cancellation

Two changes, because the defect had two halves.

**Stable evaluation.** `sin(n pi u)` is now computed by exact argument
reduction: `n*u` is formed as a double-double by Dekker splitting (both partial
products exact, since `n` is a small integer), then split into an integer `m`
and a remainder `f` in `[-1/2, 1/2]`, and `sin(n pi u) = (-1)^m sin(pi f)`.
Computing it as `np.sin(u*n*pi)` loses relative precision near the sine's zeros
— exactly where `u` approaches an edge — and an exponentially tilted amplitude
turns a 1e-10 relative slip into a 1e-5 absolute one.

**Certified evaluation error.** New public `series_error_certificate` returns
`tail`, `roundoff`, `total` and `cancellation`. The roundoff term is
`(terms + 8) * eps * SUM|term| + 8 * eps`. `series_survival` refuses when
`total` exceeds the requested tolerance.

On the review's exact pair: symmetry gap **1.6306e-05 -> 8.731e-11** at
tolerance 1e-6; the certificate reads tail `5.042e-210`, roundoff `8.349e-08`,
cancellation `1.467e+10`. A four-tilt reflection sweep certifies 190 cells
agreeing to `9.31e-10` and **refuses 26 ill-conditioned cells**.

**Public bound contract repaired.** `series_truncation_bound` now shares the
survival API's domain helper: zero time returns exactly `0.0` (it returned
`inf`), absorbing edges return exactly `0.0`, and an outside start, a negative
time, a two-dimensional position array and a zero term count are each refused.

### 2 — Folded bootstrap and physical identities

`compare_refinement` now resamples **the folded absolute error** — the statistic
the gate consumes — not the signed estimate. The review's two-cluster
counterexample reproduces exactly: the folded adjacent contrast reports
**0.699390609547** where the signed one reported `0.0`. It is carried as a
regression fixture.

`PairedSample` gained `identities` (master trial per cluster), `members` and
`baseline_members` (clock and auxiliary-replication per column), all hashed into
the sample digest, and `ValidationDataset` requires every sample to be measured
over the **same ordered physical cluster set**. Refused: absent identities,
duplicates, wrong counts, empty labels, baseline members without a baseline arm,
and cross-observable identity mismatch. Relabelling and reordering each change
the digest; order is declared significant and is not canonicalized.

### 3 — Strict v2 report semantics

`parse_validation_report` validates meaning, not shape. It enforces
`passed == (verdict == "pass")`, reason/verdict consistency, two *distinct*
64-lowercase-hex digests, a closed top-level key set, closed level and envelope
key sets, declared units, string positions, strictly positive timesteps, finite
measurements, non-negative standard and paired errors, at least two clusters,
`absolute_error == |measured - reference|` and the matching relative error, no
duplicated observable/position/timestep, one shared schedule across every
ladder, and envelopes naming rows the report contains.

The review's bypass — `numerical_no_result` beside `passed = true` — is refused,
as are twenty other malformed payloads. A valid report round-trips.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 78 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 652,886,016 B max RSS |
| raw-run subprocess | `analytic`, `killed_diffusion`, `moving_band_audit` all absent |
| result files written | none |

### Preserved

Pooled audit `numerical_no_result` (p20 bound 0.177 against the 0.10 cap);
per-regime `numerical_no_result` with 33 reasons; S3 stationary gate passes with
round-1 caps; bounded memory; PDE Courant guard and probability-domain
validation; audit v2 interval identity; physical Brownian pairing; per-unit and
per-position ladders; zero-diffusion precedence; raw isolation; every non-claim.
No exponent, population, detector-measurement or Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
