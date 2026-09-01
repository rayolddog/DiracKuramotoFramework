---
title: "Ticket 04 fix-up round 6 — scale-safe series and immutable evidence roots"
kind: ticket
status: 2
---

# Objective

Close the remaining arithmetic and trust-root failures without changing any numerical caps or the existing pooled/per-regime `numerical_no_result` conclusions.

## Required corrections

### 1. Make every series ratio and product scale-safe

- Reproduce the accepted wrong-result probe:
`lower=0`, `upper=1e100`, `diffusion=1e308`, `drift=1e308`, `start=5e99`, `time=1e-108`, `terms=20`, `tolerance=1e-6`.
- Never form `2*diffusion` or another overflowing/underflowing intermediate when the final ratio is finite. Compute tilt, Péclet-like guards, decay exponents, and all other ratios/products with scale-safe ordering, exponent decomposition, or exact classification.
- The probe must refuse or return a certified value consistent with an independent tail/probability bound; it may not collapse drift to zero.
- Under warnings-as-errors, all three public series helpers must cleanly handle:
  - `lower=-1e308`, `upper=1e308`, `start=1e308`;
  - `width=1e-200`, `diffusion=1e-200`, `drift=2`, `time=1e-200`;
  - short tilted interior cases whose truncation bound is unrepresentable;
  - absorbing starts whose certificate currently reports infinite cancellation.
- A mathematically unresolved or unrepresentable finite-input case must raise a named domain/convergence exception, never emit a warning, bare overflow, NaN, or infinity.
- Absorbing-boundary helpers must return their exact documented boundary result with a finite certificate.
- Add independent probability-tail controls and mutations that restore unsafe evaluation order or remove warning/finite guards.

### 2. Make the trusted dataset an immutable snapshot

- `PairedSample` and `ValidationDataset` must defensively copy all numeric arrays into owned C-contiguous storage before hashing or validation.
- Mark stored arrays read-only and prevent writable aliases from affecting the snapshot. Copy nested metadata/containers as needed so later caller mutation cannot change evidence.
- `parse_validation_report` must recompute only from the immutable snapshot and recheck the dataset digest after recomputation before accepting.
- Reproduce the reviewer’s TOCTOU attack using writable aliases and a mapping subclass that mutates during parsing; it must fail or be harmless.
- Add tests for source-array mutation, view/base mutation, write-flag restoration attempts, dict-subclass side effects, concurrent-looking callback/order effects, and post-construction metadata mutation.
- Preserve deterministic digest and verdict behavior for valid immutable datasets.

### 3. Apply label policy in shape-only inspection

- `inspect_validation_report` remains explicitly non-authoritative, but it must still enforce schema shape and the shared Unicode policy on observable, position, reason, blocking, and other identity-bearing labels.
- Machinery-only blocking rows containing Cc/Cf/Cs/Co/Cn characters must refuse at inspection as well as rooted parsing.
- Do not imply that passing inspection validates numerical truth or verdict.

## Verification contract

- Preserve repaired ordinary series certificates and independent high-precision sweeps.
- Preserve schema v4 rooted recomputation, injective encoding, folded bootstrap, unchanged caps, pooled/per-regime no-results, bounded memory, raw isolation, no-file behavior, and every non-claim.
- Run canonical, verbose, direct-script, warnings-as-errors, deliberate-failure, compile, hash-seed, memory, TOCTOU, and independent-reference paths.

## Completion gate

Round 6 is complete only after the same reviewer returns `CLOSED`. No evaluation order may silently change the modeled drift, and no mutation through an external alias may change the dataset after its digest establishes trust.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 85 s, peak RSS 635 MB. Of the 85 rows shared
with round 5, **84 carry byte-identical residuals**; only the memory row moved.
No row renamed. Pooled `numerical_no_result` (1 reason), per-regime
`numerical_no_result` (33 reasons) and the passing S3 gate preserved under
**unchanged caps**.

### 1 — Scale-safe derived arithmetic

**The tilt.** New `_tilt_of(drift, diffusion)` computes `drift / diffusion / 2`
and never `drift / (2 * diffusion)`; every site calls it. The review's probe
now refuses on `|k| L = 5e+99` above the declared 300 limit, rather than
collapsing the tilt to zero and certifying the zero-drift series.
`_tilt_of(1e308, 1e308) = 0.5` where the unsafe ordering gives `0.0`, and the
suite asserts both halves.

**Same grouping as the evaluation.** `_series_domain` now validates the width
first and short-circuits on it, then the Dekker splits, the widest edge
distance (inside `np.errstate`), the longest time, the tilt, the Peclet
argument, the highest mode, `highest * highest` (never `** 2`, which raises a
bare `OverflowError`), `diffusion * squared * longest`, `diffusion * k^2 * t`
and the weight denominator `k^2 + (n pi/L)^2` — each in the grouping
`_series_terms` actually uses. All twelve of the review's warnings-as-errors
cases now refuse with named `ValueError`s: no `RuntimeWarning`, no bare
`OverflowError`, no public infinity.

**Boundary helpers.** `series_truncation_bound` raises a named convergence
error rather than returning `[[inf]]`. The cancellation diagnostic is `1.0`
where nothing is summed — an absorbing start is pinned to exactly zero by
definition — so every certificate component is finite, and the check asserts it
at exactly that start.

Preserved: the repaired ordinary case still returns `8.759717659060986e-05`;
the 121-cell high-precision sweep is unchanged at worst ratio `5.107e-03`; the
4000-term limiting case and the reflection sweep still pass.

### 2 — Immutable evidence root

`PairedSample` copies both arms with `np.array(..., order="C", copy=True)` and
seals them via `_sealed`: a read-only *view* of a read-only base, so the write
flag cannot be restored (the owner could otherwise just set it back).
`ValidationDataset` **rebuilds** each sample rather than retaining it, so a
dataset never holds an array anybody else can write to.

`parse_validation_report` snapshots the payload into an owned plain `dict`
(closing the mapping-subclass second-read race), rebuilds the dataset, captures
the digest **once**, and re-checks it after recomputation.

The review's TOCTOU attack — writable alias plus a `dict` subclass mutating on
the second `dataset_digest` read — is refused. Mutating the source array no
longer changes the digest; writing through the stored array and restoring its
write flag both raise; valid reports still round-trip.

### 3 — Label policy in shape-only inspection

`inspect_validation_report` now applies `_require_label` / `_require_printable`
to the report label, every level's observable and position, every budget's
observable and position, every envelope's named observable and position, and —
the uncovered surface — **every blocking row's observable and position, before**
**the code is classified**. All six forbidden categories in both fields of a
machinery-only `cluster_mismatch` row are refused, twelve cases in the suite.
The inspector remains explicitly non-authoritative for verdict truth.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 85 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 635,305,984 B max RSS |
| high-precision sweep | 121 cells, worst error/certificate ratio 5.107e-03 |
| TOCTOU / write-flag / subclass probes | all refused |
| raw-run subprocess | `analytic`, `killed_diffusion`, `moving_band_audit` absent |
| result files / unexpected git changes | none / none |

### Documentation

The two stale README sentences the review flagged are corrected: the
`terms // 2` convergence description is replaced by the total-certificate rule,
and the schema references read v4. New passages cover the scale-safe tilt and
the immutable snapshot.

### Preserved

Schema-v4 rooted recomputation; folded bootstrap (two-cluster fixture still
0.699390609546963); injective length-prefixed encoding; unchanged caps; pooled
and per-regime `numerical_no_result`; bounded memory; PDE guards; audit v2
interval identity; physical pairing; per-unit and per-position ladders;
zero-diffusion precedence; raw isolation; every non-claim. No exponent,
population, detector-measurement or Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
