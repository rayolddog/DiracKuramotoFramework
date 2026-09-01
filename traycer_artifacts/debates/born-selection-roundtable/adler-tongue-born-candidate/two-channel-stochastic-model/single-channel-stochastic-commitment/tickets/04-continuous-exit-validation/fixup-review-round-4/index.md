---
title: "Ticket 04 fix-up round 4 — certified series, injective manifests, and recomputable verdicts"
kind: ticket
status: 2
---

# Objective

Close three exact adversarial failures while preserving the honest pooled/per-regime `numerical_no_result`, unchanged caps, bounded memory, and every previously confirmed contract.

## Required corrections

### 1. Replace the falsified floating-error certificate

- Reproduce the reviewer’s accepted call at tolerance `2e-15`: band `(-0.4, 0.7)`, diffusion `0.025026019953529995`, drift `0.4550185446096362`, start `0.6999989000000001`, time `0.0016266446286139454`, and 400 terms.
- The binary64 result differs from the 150-digit reference by about `1.32618e-14`, while the present certificate reports only about `1.78429e-15`; it must no longer certify this value.
- Do not substitute another heuristic constant. Use a defensible certified computation: directed/high-precision evaluation with an explicit rounding enclosure, interval arithmetic, a validated cross-precision enclosure, or a conservative domain/tolerance refusal rule whose guarantee is testable.
- The total certificate must bound truncation plus evaluation error and must never claim more precision than the evaluation method supports.
- Add high-precision adversarial sweeps across drift, edge distance, time, term count, requested tolerance, and cancellation/tilt regimes. Every accepted value must lie inside its certificate relative to the independent reference; unresolved values refuse.

### 2. Make physical-manifest serialization injective

- Replace NUL-delimited identity/member serialization with a canonical injective encoding such as length-prefixed byte strings or canonical structured JSON.
- Explicitly support or reject embedded NUL and other control characters; do not allow ambiguous concatenation.
- The identity tuples `('a\0b','c')` and `('a','b\0c')`, and analogous member/baseline-member tuples, must not share sample or dataset digests.
- Bind field names, tuple boundaries, element lengths, Unicode encoding, normalization policy, dimensions, and arm role so distinct physical manifests cannot collide structurally.
- Add round-trip and mutation tests for empty labels, control characters, Unicode, swapped fields, tuple repartitioning, reordering, duplicates, and identity substitution.

### 3. Make a report’s verdict recomputable from bound evidence

- A v2 report must carry the frozen budget/contract and sufficient decision evidence for the parser to recompute every ladder verdict, reasons, aggregate verdict, and `passed` value. Digests alone are not enough.
- The parser must reject a genuine no-result whose tag is coherently rewritten to `pass`/`passed=true`/empty reasons while levels and evidence remain unchanged.
- Enforce one unit per observable-position ladder, coherent positions and schedules, coarsest paired-error semantics, exact envelope maxima/identity/timestep/unit, and exactly one required envelope per represented unit.
- Validate all budgets, caps, sampling design, transformation, bootstrap metadata, cluster evidence/digests, and reason codes needed to reproduce the decision. Unknown or omitted decision inputs must refuse.
- If this requires a breaking shape, bump the schema again rather than overloading v2.
- Add mutations for mixed ladder units, forged envelope values/timesteps/units, missing/extra envelopes, nonzero coarsest paired error, forged pass/no-result tags, altered caps, changed reasons, and digest-preserving-looking but inconsistent evidence.

## Verification contract

- Preserve folded-statistic bootstrap correctness and strengthen identity binding; no caller-supplied SE path may reappear.
- Preserve pooled and all per-regime `numerical_no_result` outcomes under unchanged caps.
- Preserve all closed findings, memory behavior, raw isolation, no-file behavior, and scientific non-claims.
- Run canonical, verbose, direct-script, warnings-as-errors, deliberate-failure, compile, hash-seed, memory, and independent high-precision/reference paths.

## Completion gate

Round 4 is complete only after the same reviewer returns `CLOSED`. No accepted series result may exceed its certified error, no two distinct manifests may share a structural encoding, and no downstream parser may convert the frozen no-result into a pass without changing evidence that the parser detects.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 80 s, peak RSS 589 MB. Of the 85 rows shared
with round 3, **84 carry byte-identical residuals**; the only mover is the
memory row, whose residual is a measured RSS. No row renamed. Pooled
`numerical_no_result` (1 reason), per-regime `numerical_no_result` (33 reasons)
and the passing S3 gate are all preserved under **unchanged caps**.

### 1 — The falsified floating-error certificate

**Root cause.** Not the summation the old model bounded: the band coordinate.
`u = (x - lower)/(upper - lower)` was formed in binary64, and everything
upstream of `1 - u` is magnified by `1/(1 - u)`. At the review's start,
1.1e-6 from the upper edge, one rounding of `x - lower` is 2e-10 *relative* and
rounding `upper - lower` costs the same again. The review's remark that exact
reduction of `n*u` after `u` has been formed does not make the formula exact
was precisely right.

**Fix.** Both the edge distance and the band width are now carried as
double-doubles (`_band_fraction`), and `n*u` is reduced exactly. The review's
own call now returns a value **9.49e-20** from their 150-digit reference, down
from **1.33e-14**.

**Certificate.** The `(terms + 8) * eps * SUM|term|` model is gone. The bound
walks the operation graph: the weight's arithmetic, each exponential charged
for its own argument magnitude, the amplitude's *absolute* error (which does
not shrink when its exponentials cancel), the shape's reduction and sine, the
classical summation bound, and a result floor.

**Validation, not assertion.** A frozen adversarial sweep of **121 cells** —
three bands, five edge fractions including 1e-6 from each edge, four drifts
including zero and both signs, two times, and both the 120- and 400-term
regimes — compares every accepted value with an independently written 90-digit
reference (its own sine, its own reduction, living in `verify.py`, sharing no
code with the module). The worst ratio of true error to certified error is
**5.107e-03**; the certificate dominates by at least 200x everywhere.

**Declared refusal domain.** The result floor makes no tolerance below about
1.78e-15 certifiable for any evaluation. That is stated as a conservative
refusal domain and is testable.

*One point for the reviewer to rule on:* the review's exact call at tolerance
2e-15 is now **certified**, and I believe correctly so — its value is accurate
to 9.49e-20, five orders inside its 1.784e-15 certificate. It is no longer
*falsely* certified because it is no longer wrong. Forcing a refusal would have
required raising a constant, which the ticket forbids. If the reviewer wants a
refusal regardless, `RESULT_ULPS` is the single knob.

### 2 — Injective manifest encoding

`_encode_labels` writes `field name | count | (length, utf-8 bytes) per label`,
every integer fixed-width big-endian, for identities, members and baseline
members alike, plus array shapes and the arm role. Control characters
(including NUL) are refused outright in `_require_names`, so both halves of the
review's requirement are met: the encoding is injective *and* the ambiguous
characters are excluded.

Both of the review's tuples are now refused at construction; the analogous
control-free repartition `("ab","c")` vs `("a","bc")` — the same defect without
NUL — produces different sample **and** dataset digests. Regressions cover
empty labels, control characters, swapped fields, repartitioning, reordering,
duplicates and identity substitution.

The stale `PairedSample.measured` docstring no longer claims the signed
bootstrap is conservative; the invalid `||a|-|b|| <= |a-b|` argument is gone
with the practice.

### 3 — Recomputable verdicts, schema v3

`VALIDATION_SCHEMA` is **`dk-numerical-validation/v3`**. The report gained the
frozen contract (timesteps, ratio, full sampling design including seed), the
frozen budgets (caps, floors, `require_decrease`, estimator, quantile), a
machine-readable `blocking` list of reason codes from `REASON_CODES`, and a
per-level `span_error`.

The decision now lives in one function, `_ladder_codes`, called by
`compare_refinement` to reach a verdict and by `parse_validation_report` to
**recompute** one. The parser rebuilds the contract and budgets, checks they
hash to the declared budget digest, re-runs the decision over the levels, and
refuses any disagreement.

Refused: the coherent no-result-to-pass rewrite; mixed-unit ladders; forged
envelope values, timesteps, units and identities; missing and extra envelopes;
a nonzero coarsest paired error; altered caps; changed reason lists; a v2 tag on
a v3 shape; and every round-3 mutation. Envelopes are rebuilt field-for-field
from the levels, exactly one per unit present.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 80 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 588,890,112 B max RSS |
| high-precision sweep | 121 cells, worst error/certificate ratio 5.107e-03 |
| raw-run subprocess | `analytic`, `killed_diffusion`, `moving_band_audit` absent |
| result files | none |

### Preserved

Folded-statistic bootstrap (two-cluster fixture still reports
0.699390609546963); explicit physical identities, now injectively encoded; no
caller-supplied SE path; unchanged caps; pooled and per-regime
`numerical_no_result`; bounded memory; PDE guards; audit v2 interval identity;
physical Brownian pairing; per-unit and per-position ladders; zero-diffusion
precedence; raw isolation; every non-claim. No exponent, population,
detector-measurement or Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
