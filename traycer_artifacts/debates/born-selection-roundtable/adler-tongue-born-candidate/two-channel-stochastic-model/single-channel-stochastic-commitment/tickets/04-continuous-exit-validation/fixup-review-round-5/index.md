---
title: "Ticket 04 fix-up round 5 — finite derived arithmetic, rooted evidence, and Unicode labels"
kind: ticket
status: 2
---

# Objective

Close the three remaining round-4 findings without changing caps or the pooled/per-regime `numerical_no_result` outcomes.

## Required corrections

### 1. Refuse nonfinite derived series arithmetic

- Reproduce extreme finite-input cases including `(lower, upper, diffusion, drift, start, time) = (0, 1e308, 1e308, 0, 5e307, 1e-308)` and the `(-1e308, +1e308)` band.
- Validate every derived quantity used by the series and its certificate: width, normalized coordinate, edge distances, drift tilt, exponential arguments/weights, modes, terms, partial sums, tail, roundoff, total, and final probability.
- Any NaN or infinity must raise before a public result or certificate is returned. NaN comparisons must never serve as a refusal mechanism accidentally.
- Guard arithmetic so warnings-as-errors remains clean. If a finite mathematical value cannot be represented or certified in binary64, refuse with a named domain/convergence error.
- Add extreme-scale positive controls where derived arithmetic remains finite, plus mutations that remove final and intermediate finite guards.

### 2. Root report decisions in recomputable cluster evidence

- A bare `dataset_digest` is not a trust root. The parser must either:
  - receive canonical raw cluster evidence in the report, recompute the dataset digest, estimates, folded bootstrap, standard/span/paired errors, envelopes, reason codes, and verdict; or
  - require an explicit trusted external dataset/proof argument and refuse verdict validation without it.
- For the current self-contained machine-readable report, prefer embedding canonical cluster evidence unless size or layering makes an externally rooted API demonstrably necessary.
- The reviewer’s forgery—zeroing SE/error fields, changing no-result to pass, and leaving digests unchanged—must refuse.
- Changing cluster counts `2 -> 999` without matching evidence must refuse.
- Fix the legitimate `cluster_mismatch` parser crash and ensure both mismatch and unbudgeted no-result reports round-trip as valid no-results with recomputed reasons.
- Bind identities, members, baseline members, observations, level schedule, estimator, transformation, resampling seed/count, budgets, and sampling contract. Recompute rather than trust every derived scalar.
- Add mutations for altered raw observations, dropped/duplicated/reordered identities, altered cluster counts, forged summaries, changed reasons/verdict, missing trust root, and stale digest.
- Bump the schema if required by the evidence shape.

### 3. Define and enforce the Unicode label policy everywhere

- Apply one policy to physical identities, member/baseline-member labels, observable names, positions, and report labels.
- Reject embedded NUL and Unicode control/format/surrogate/private-use/unassigned code points at minimum, including U+0085, U+202E, and U+200D, or narrow the public claim and prove the remaining encoding is injective. Prefer explicit rejection for auditability.
- State whether Unicode normalization is applied. If not, distinct normal forms remain distinct identities; if yes, normalize before validation and hashing.
- Add tests for ASCII controls, the three reviewer code points, bidi controls, zero-width joiners, lone surrogates, private-use characters, composed/decomposed Unicode, empty labels, and valid non-ASCII text.

## Verification contract

- Preserve the repaired finite-band series case and its independent high-precision evidence.
- Preserve folded bootstrap correctness, injective length-prefixed encoding, unchanged caps, pooled/per-regime no-results, and all closed findings.
- Run canonical, verbose, direct-script, warning-as-error, deliberate-failure, compile, hash-seed, memory, raw-isolation, and no-file paths.
- Make no exponent, population-outcome, detector-measurement, or Born-rule claim.

## Completion gate

Round 5 is complete only after the same reviewer returns `CLOSED`. Nonfinite arithmetic must never escape, report verdicts must be rooted in evidence the parser actually recomputes, and label policy must be consistent across all identity-bearing fields.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 81 s, peak RSS 625 MB. Of the 85 rows shared
with round 4, **84 carry byte-identical residuals**; the only mover is the
memory row. No row renamed. Pooled `numerical_no_result` (1 reason), per-regime
`numerical_no_result` (33 reasons) and the passing S3 gate all preserved under
**unchanged caps**.

### 1 — Nonfinite derived arithmetic

`_series_domain` now validates every *derived* quantity — band width, Dekker
splits of the width and both edges, drift tilt, highest mode, widest edge
distance, longest time, highest decay exponent, tilt exponential — and refuses
any that is not finite, with a named domain error. Both reviewer cases refuse:
`(0, 1e308)` on "Dekker's split of the band width is inf" and
`(-1e308, +1e308)` on "the band width (upper - lower) is inf".

`series_survival` was still carrying its own inline validation block rather
than calling `_series_domain` — that is why it reached `_series_terms` and
warned under `-W error` while the two certificate helpers refused cleanly. It
now routes through the shared guard. All six paths (three helpers x two bands)
refuse cleanly under `-W error`.

NaN can no longer pass a gate by losing a comparison: the tolerance gate is
`not (evidence <= tolerance)` and the probability-domain gate is
`not (low >= -slack and high <= 1 + slack)`. Every partial sum and every
certificate component is checked finite before return.

Positive controls: the repaired review case still returns `8.759717659060986e-05`
inside its certificate; the 4000-term limiting case still passes; an extreme but
*representable* band (0, 1e3) with diffusion 1e6 evaluates with a finite
certificate. The stale `series_error_certificate` docstring describing the
removed `(terms + ROUNDOFF_GROWTH)` model is corrected.

### 2 — Rooted report evidence, schema v4

`parse_validation_report(payload, dataset)` takes the `ValidationDataset` as a
**required argument**, verifies `dataset.digest` against the report's declared
digest and the dataset's contract against the embedded one, then **recomputes**
**the entire report** with `compare_refinement` and refuses on any difference.
Recomputing everything rather than checking invariants is deliberate: it is the
only formulation that cannot be incomplete.

`inspect_validation_report(payload)` keeps the shape-and-local-consistency path,
documented as **not** establishing the verdict.

Refused: the zeroed-SE forgery; `clusters` 2 -> 999; arbitrary reason text; an
altered raw observation; and every round-4 mutation. Round-tripping: the
`cluster_mismatch` crash is fixed (`schedule_seen` is initialized, and machinery
codes are no longer recomputed locally where no levels exist), and both
`cluster_mismatch` and `unbudgeted` no-results now round-trip as valid
no-results.

**Why the evidence is an argument, not embedded.** The S3 dataset holds twelve
samples of six thousand clusters at three levels — 216,000 observations, several
megabytes of JSON for a report whose purpose is to be read. The ticket permits
the externally rooted route where size makes embedding impractical; the
guarantee is identical, since the digest is checked and everything else is
recomputed.

### 3 — One Unicode label policy

`FORBIDDEN_LABEL_CATEGORIES = ("Cc", "Cf", "Cs", "Co", "Cn")`, enforced by one
helper `_require_printable` applied to identities, members, baseline members,
observables, positions and report labels alike. U+0085, U+202E, U+200D, lone
surrogates, private-use code points, C0 controls, DEL, the newline in
`observable` and the NUL in `position` are all refused.

**No normalization is applied**, stated in the module and the README: a composed
and a decomposed spelling are distinct identities and hash differently, and the
suite asserts it. Positive controls confirm Greek, Han and emoji labels are
accepted — the policy rejects categories, not scripts.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 81 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 624,607,232 B max RSS |
| high-precision sweep | 121 cells, worst error/certificate ratio 5.107e-03 |
| raw-run subprocess | `analytic`, `killed_diffusion`, `moving_band_audit` absent |
| result files / unexpected git changes | none / none |

### Preserved

Repaired finite-band series case and its high-precision evidence; folded
bootstrap (two-cluster fixture still 0.699390609546963); injective
length-prefixed encoding; unchanged caps; pooled and per-regime
`numerical_no_result`; bounded memory; PDE guards; audit v2 interval identity;
physical pairing; per-unit and per-position ladders; zero-diffusion precedence;
raw isolation; every non-claim. No exponent, population, detector-measurement or
Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
