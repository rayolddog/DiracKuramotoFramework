---
title: "Ticket 06 execution notes — the separate read-only analysis layer"
kind: spec
---

# Ticket 06 execution notes

Implementation record for [06 — Statistics and comparators](..). Ticket status
is left at **1 (in progress)** for re-review; nothing here closes it.

Round 2 (this revision) closes the six findings of the
[independent review](../independent-review). Every one of its reproductions was
replayed against the current bytes before any edit, and again afterwards.

## What was built

Three modules in `adler_born_two_channel/`, all **outside** the raw import
graph:

| File | Lines | Responsibility |
| --- | --- | --- |
| `observables.py` | 727 | Risk sets, survival, discrete conditional failure, width-divided hazard, cumulative hazard, unresolved causes, winner mismatch |
| `analysis.py` | 1497 | Provenance-bound master-trial identity, the binomial cloglog exponent on raw counts, curvature identifiability, the closed refusal vocabulary, and the paired resampling that is the authoritative uncertainty |
| `compare.py` | 1704 | Manifest-bound `RunSweep`, read-only access with fingerprints, four separately typed comparators, role-bound control evidence, computed holdout evidence, the causal defeat rule, and the numerical gate |

Modified: `verify.py` (12 ticket-06 checks, criteria 96–107, ~120 validation
rows), `raw_runner.py` (`UNIMPLEMENTED_RAW_STAGES` wording), `__init__.py`
(docstring), `README.md`.

Nothing outside `adler_born_two_channel/` was touched. Nothing staged,
committed or reverted; the working tree still shows exactly the 29 pre-existing
entries it showed at session start, with `adler_born_two_channel/` untracked as
before.

## Commands

```bash
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework

python3 -m py_compile adler_born_two_channel/*.py           # compile   -> 0
python3 -m adler_born_two_channel.verify                    # canonical -> 0
python3 -m adler_born_two_channel.verify --verbose          # verbose   -> 0
python3 adler_born_two_channel/verify.py                    # direct    -> 0
python3 -W error -m adler_born_two_channel.verify           # -W error  -> 0
python3 -m adler_born_two_channel.verify --prove-failure-exit   #        -> 1
```

**113/113 checks pass** on every path; `--prove-failure-exit` gives 113/114 and
exit 1, with only the deliberate probe failing. `results/` is absent afterwards
on every path (17 long-lived fixture runs are drained by the cleanup check).
Wall time ≈ 112 s; peak resident set 628 MB against the suite's unchanged
900 MB bound.

## Review findings — before and after

Every probe below was run verbatim against the pre-fix bytes and reproduced the
review's result, then re-run against the current bytes.

### P1 — the numerical gate was caller-asserted

|  |  |
| --- | --- |
| **Before** | `scaling_verdict(good_fit, ("production_cleared",))` → `physical_verdict_permitted`, no ledger opened |
| **After** | `TypeError: calibrated must be a CalibratedExponent, got ExponentReport`; and the second argument is now a `RunSweep`, not strings |

`RunSweep` can only be built from `ReadOnlyRun` objects. Construction requires
distinct fingerprints, strictly increasing distinct couplings, and **every**
frozen manifest field outside `SWEEP_VARYING_FIELDS`
(`peak_coupling`, `pulse_digest`, `model`, `fixed_contraction_rate`) identical
across the runs. `scaling_verdict` re-opens and re-hashes the whole sweep
before deciding, and additionally recomputes the committed/trial counts from
the ledgers — so a synthetic design carrying the sweep's couplings but not its
data is refused.

The positive control is an **independently constructed, hash-valid** run: the
verifier re-emits a real closed run's manifest with
`numerical_gate = "production_cleared"` through
`canonical_manifest_bytes`, rebuilds the close marker with the new manifest
digest, and reopens it through the gate. The same calibrated ledger fit carries
the gate reason over the `diagnostic_only` sweep and does not over the cleared
one. A mixed-gate sweep is now refused *at construction* rather than blocked.

Synthetic machinery has a separate door, `synthetic_machinery_verdict`, whose
`ScalingVerdict` source is `synthetic_machinery`; `ScalingVerdict` refuses to
hold `physical_verdict_permitted` from that source at all.

### P1 — CRN inference computed but not used; refused replicates called valid

|  | Before | After |
| --- | --- | --- |
| Wald stderr (600-trial CRN sweep) | 0.06196 | 0.06196 — display only |
| paired bootstrap | 0.07872 (unused) | 0.07872 — **authoritative** |
| wrong independent-cell | 0.06245 | 0.06245 |
| `CalibratedExponent.stderr` | — | 0.07872, identically the paired one |
| four-trial design, `valid_replicates` | 50/50 | **0/50**, `adequate=False` |
| its calibrated verdict | — | `no_valid_exponent` incl. `inadequate_resampling` |

`calibrate_exponent` is now the only object `compare.py` accepts. Its interval,
standard error and curvature diagnostic come from the paired record; the
marginal Wald interval is reported but decides nothing. Adequacy has frozen
floors: `MIN_RESAMPLE_REPLICATES = 100` and
`MIN_VALID_RESAMPLE_FRACTION = 0.9`.

**One deliberate departure from the literal wording of the review's fix**, and
it is the main judgment call of this round. The review asked to "count a
replicate only when its `ExponentReport.is_valid` is true". Implemented
literally that criterion refuses every genuine CRN design, because the two
model-adequacy tests are exactly the statistics pairing invalidates — a paired
bootstrap resamples whole master trials, so its replicates are clustered.
Measured on a perfectly specified power law:

| trials/cell | replicates refused for `lack_of_fit` | for `curvature` |
| --- | --- | --- |
| 200 | 14 % | 10 % |
| 400 | 11 % | 9 % |
| 2000 | **60 %** | 13 % |

So `valid_replicates` counts **estimable** replicates — refused for none of
`ESTIMABILITY_REASONS` (`saturated`, `separation`, `flat`, `ill_conditioned`,
`non_convergence`, `curvature_unidentified`). `GOODNESS_REASONS`
(`lack_of_fit`, `curvature`) are counted and reported in `refusals` but do not
disqualify. Model adequacy under pairing is instead decided by the **bootstrap**
**distribution of the curvature coefficient** (`curvature_interval`), which is
cluster-robust by construction, plus the marginal tests applied once to the
original fit as a conservative refusal. The review's four-trial reproduction
still gives 0/50, because those replicates fail on *estimability*.

### P1 — refused controls and missing holdout could pass causal attribution

|  |  |
| --- | --- |
| **Before** | full valid at 2.00058; both controls `no_valid_exponent ('lack_of_fit',)` at 2.99103, interval (2.92304, 3.05903) → `not_blocked ()` |
| **After** | same evidence → `blocked ['central_control_no_valid_exponent', 'width_control_no_valid_exponent']` |

The premise that an inadequate control has an unbounded interval was false. The
interval **excludes** two in that counterexample, so only a verdict-based
blocker can fire — and the verifier uses exactly that shape (a hand-built
`CalibratedExponent`, refused with a finite narrow interval) to prove the new
blocker does work the interval test cannot.

`causal_decision` now takes three `ControlEvidence` objects and a computed
`HoldoutEvidence`. Roles are checked against the sweeps they were fitted from:
each of the three real sweeps is offered in each of the three roles and only the
diagonal is accepted (six off-diagonal refusals). The holdout is computed inside
the decision path from `frozen_edges` — a binning with the pulse centre exactly
on a boundary — and records the fingerprints of all three runs. New blockers:
`central_control_no_valid_exponent`, `width_control_no_valid_exponent`,
`contrast_inadequate`, `holdout_evidence_missing`.

The two weaker helpers the review named are fixed: `discrepancy_score` requires
identical `(left, right, width)` per interval rather than equal lengths, and
`rising_falling_split` refuses a table whose bin straddles the pulse centre
rather than assigning it to the falling side.

### P1 — master-trial identity omitted the namespace

|  |  |
| --- | --- |
| **Before** | `paired_exponent_contrast` on two unrelated designs, both numbered 0..99 → accepted, contrast −0.6387 |
| **After** | `ValueError: the two designs hold different master trial identities…` |

`MasterTrial(namespace, trial)` with a length-prefixed injective `key`. The
namespace of a real design is `compare.crn_identity` — the digest of 28 frozen
manifest fields that decide which Brownian path trial *i* is. It excludes
`peak_coupling` (a sweep varies it) and `model`/`fixed_contraction_rate` (full
and width-only share one tree by construction, and the plan excludes the model
label from the physical noise key), so a sweep pairs across its couplings and
the full/control pair pairs with each other — both asserted. A cell may hold
only one namespace; an `independent_namespace` design must use a *distinct*
namespace per cell, not merely disjoint numbering. Mixed, reordered, duplicated,
bare-integer and substituted identities are each refused with a valid control
beside them. `design_from_sweep` builds designs from the ledgers themselves.

### P2 — an unidentifiable curvature extension certified a valid exponent

|  |  |
| --- | --- |
| **Before** | 1.000–1.010, 200 000 trials/cell, half events → `valid_exponent`, curvature stderr `inf`, curvature p 1.0 |
| **After** | `no_valid_exponent ('curvature_unidentified',)` |

The curvature fit must converge without runaway, its information must exceed
the frozen reciprocal-condition threshold, and its interval must be bounded,
before the power model it tests can be valid. A nearby *identifiable* design of
the same size still returns 2.000, so the gate is not a blanket refusal.

### P3 — README Ticket-04 contradiction

The stale paragraph now reads: *"The stationary killed-diffusion oracle that*
*bounds it has passed its reference budget; the moving-band diagnostic beside it*
*has not, and no production budget exists for either."* The contradiction is
mechanically guarded: `_STALE_ORACLE_CLAIM` matches the claim rather than the
words, with four fixtures pinning both directions so legitimate past-tense
history still passes.

## API and schema changes

**No schema change.** Ledger and manifest remain v3; the five run files are
untouched; nothing in the layer writes.

Signature changes (all inside ticket 06's own new surface):

- `CouplingCell.trial_ids` now holds `MasterTrial`, not `int`.
- `scaling_verdict(report, gate_strings)` → `scaling_verdict(calibrated, sweep)`.
- `causal_decision(..., control_not_worse: bool)` →
`causal_decision(full, central, width_only, contrast, minimum_difference, holdout)`
over `ControlEvidence` and `HoldoutEvidence`.
- `ResamplingReport` gains `refusals` and `curvature_interval`;
`valid_replicates` changes meaning (estimable, not finite).
- `ContrastReport` gains `valid_fraction` and `is_adequate`.
- `ScalingVerdict` gains `source` and `fingerprints`.

New public names: `MasterTrial`, `master_trials`, `CalibratedExponent`,
`calibrate_exponent`, `ESTIMABILITY_REASONS`, `GOODNESS_REASONS`,
`MIN_RESAMPLE_REPLICATES`, `MIN_VALID_RESAMPLE_FRACTION`; `RunSweep`,
`crn_identity`, `sweep_master_trials`, `design_from_sweep`, `frozen_edges`,
`ControlEvidence`, `control_evidence`, `HoldoutEvidence`, `holdout_evidence`,
`synthetic_machinery_verdict`, `CRN_IDENTITY_FIELDS`, `SWEEP_VARYING_FIELDS`,
`CONTROL_ROLES`, `VERDICT_SOURCES`.

Documented counts: 111 → **113** checks, 321 → **353** public callables,
910 → **960** invalid calls, 730 → **783** parameters. All pinned and passing.

## Decision semantics, stated plainly

- **`scaling_verdict`** → `physical_verdict_permitted` only when every run in a
re-hashed sweep records `production_cleared`, the fit's couplings *and counts*
are the sweep's, and the calibrated exponent is valid. Otherwise
`machinery_only` with reasons. Currently unreachable, by design.
- **`causal_decision`** → `not_blocked` only when the full model and *both*
controls are valid, neither control's paired interval contains two, the
contrast is adequate and clears the frozen minimum, and complete holdout
evidence shows the control worse. There is no verdict spelled `supported`.
- **`calibrate_exponent`** → `valid_exponent` only when the marginal fit is
clean, the resampling record is adequate, the paired interval is inside the
frozen cap, and the paired curvature interval contains zero.

## Flat-response semantics — rechecked, unchanged

The review's disposition agrees with the implementation: *"A valid exponent near*
*zero is correct. The declared model includes `p = 0`; refusing it would erase a*
*real negative scaling result. The existing `flat` reason is better read as*
*singular information, not a constant response."* `flat` remains a singular
expected-information matrix; a constant response with adequate information
returns a valid exponent near zero; a constant response with *inadequate*
information is caught by `uninformative`. Now stated explicitly in
`analysis.py`'s docstring and in the README.

## Preservation

- All 95 pre-ticket-06 acceptance criteria and every prior residual/tolerance
unchanged; the 18 ticket-06 checks are additive.
- Raw isolation unchanged and re-asserted: a fresh interpreter importing
`raw_runner` loads 11 package modules and none of `observables`, `analysis`,
`compare`, `analytic`, `killed_diffusion`, `moving_band_audit`.
- No-write behaviour unchanged: none of the 27 write-capable names appears in
any of the three modules at any binding or call position, and a full
comparison leaves all five files' digests identical.
- Ticket 04's `diagnostic_only` state preserved and pinned by check.
- Every scientific non-claim preserved and extended.

## Limitations and residual risks

- **The estimability/goodness split is a judgment call.** It departs from the
literal wording of the review's fix for the measured reason above. If the
reviewer prefers strict `is_valid` counting, the constant is one line — but
the consequence is that no CRN design with more than a few hundred trials per
cell will ever be adequate.
- Lack of fit under pairing has **no fully calibrated test**. The marginal
deviance is used one-sidedly as a refusal on the original fit and documented
as conservative-in-direction-unknown; a properly calibrated version needs a
parametric bootstrap under the null, which is a larger piece of work.
- The paired curvature interval is a percentile bootstrap interval; it is
cluster-robust but not exact at small replicate counts.
- The real run sweeps in the verifier are six trials per coupling, so no
*real* sweep produces a valid calibrated exponent. Consequently
`physical_verdict_permitted` is never reached positively; what is demonstrated
is that the **gate term** appears and disappears with the manifest value, and
that permission is unconstructible from the synthetic source. A ticket-07
pilot with production trial counts would close that last gap.
- `holdout_evidence` requires the caller to name a reference run. Which run
*should* be the declared reference is a scientific choice belonging to
tickets 07–08; the machinery only enforces that it is named, agrees with the
experiment, and is used identically for both candidates.
- The bootstrap rebuilds cell objects per replicate. One calibration at the
frozen floor over six cells and a few hundred trials is ~0.11 s; a production
sweep will want a faster path.

## Scientific boundary

Nothing here claims Born's rule, a detector click, an absorption, a measurement
outcome, unique actuality, a microscopic origin for the noise, a two-channel
outcome, or a production-cleared exponent. What is demonstrated is that the
analysis machinery behaves as specified on synthetic data with known answers,
and that every route from it to a physical statement is bound to re-hashed
manifests that all say `diagnostic_only`.

## Round 3 — the closure re-review's three findings

The [re-review](../independent-review) verdict was OPEN with three bounded
findings. Every one of its probes was replayed against the pre-fix bytes and
reproduced exactly, then fixed, then replayed again.

### R3-P1 — physical permission was still caller-constructible

|  |  |
| --- | --- |
| **Before** | a forged `CalibratedExponent` (verdict and interval agreeing with neither record it carried) over a gate-rewritten sweep → `physical_verdict_permitted`; `ScalingVerdict("physical_verdict_permitted", "closed_runs", (), ("production_cleared",), ("not-a-fingerprint",))` → accepted; a `RunSweep` alternating full and width-only runs → accepted and fitted |
| **After** | every derived record is factory-only and refuses direct construction; `scaling_verdict(sweep, replicates, seed)` **recomputes** the calibration from the re-opened sweep; a mixed-model sweep is refused at construction; and `physical_verdict_permitted` is **unconstructible under manifest schema v3** |

The decisive change is the schema boundary the reviewer asked for. Rewriting the
free-text `numerical_gate` left the same hashed manifest saying
`moving_band_status: numerical_no_result` and `validation_note: … no scaling claim may be drawn from these tables`. So all four status fields are now read
jointly, and above them sits `PRODUCTION_STATUS_SCHEMA = 4` — a manifest schema
that does not exist. Schema v3 fails closed.

The gate is still shown to *read its input*: rewriting one run's
`numerical_gate` removes **exactly** that blocker from the sweep's status list
and leaves five standing, including the schema and the moving-band
`numerical_no_result`. The suite asserts that set difference rather than a
verdict flip.

Binding was tightened as asked: `ScalingDesign.digest` covers ordered couplings,
canonical master-trial identities **and every outcome** (not the aggregate
counts, which two different outcome matrices can share); the fit, resampling
record and lack-of-fit test all carry it and `CalibratedExponent` refuses three
records about three designs. `SWEEP_VARYING_FIELDS` narrowed to
`(peak_coupling, pulse_digest)`, so one sweep is one model at one contraction
rate; `EXPERIMENT_VARYING_FIELDS` covers the cross-sweep comparisons.

Synthetic work now returns a **different type**: `MachineryReport`, with no
verdict field, `is_physical == False`, and its disclaimer in `summary`.

### R3-P2 — causal evidence remained forgeable

|  |  |
| --- | --- |
| **Before** | three unrelated controls + a caller-authored `ContrastReport` + a holdout whose fingerprints belonged to neither → `not_blocked ()`, over calibrations that all said `no_valid_exponent`; `CausalDecision("not_blocked", (), 1.0, 0.25)` directly constructible |
| **After** | all four records sealed; `control_evidence(role, sweep, replicates, seed)` and `paired_exponent_contrast(full_sweep, control_sweep, …)` take **sweeps** and compute their own calibrations; the same combination now returns `blocked` with eight reasons |

`causal_decision` joins before it decides: the contrast's `full_digest` /
`control_digest` must be the two evidences' own design digests, its coupling
grid and CRN identity must be theirs, and the holdout's full and control
fingerprints must **belong to** the respective evidence's fingerprint tuples.
Each control carries its sweep's status blockers, adding
`numerical_status_not_cleared`. `HoldoutEvidence.complete` is derived from a
`source` field with `missing_holdout(reason)` as the only producer of an
absence.

### R3-P2 (statistics) — general CRN lack-of-fit was uncalibrated

Confirmed the reviewer's measurement independently (500 exact power-law
datasets, 400 trials, six cells): the marginal deviance rejected **0.6 %** under
shared master trials against a nominal 5 %, and 3.6 % under independent
namespaces.

Implemented the cluster-sandwich option the reviewer offered:
`analysis.cluster_lack_of_fit` is a **cluster-robust generalized score test** on
the `cells − 2` lack-of-fit contrasts with a **Rademacher multiplier bootstrap**
p-value that re-signs whole master trials. Because the MLE conditions make the
saturated-model score exactly orthogonal to the power model's columns, the whole
score lies in the lack-of-fit space; the meat `V = Σ s_t s_t'` is summed over
clusters, so master-trial dependence is carried rather than assumed away. An
independent-namespace design has one observation per cluster, so the same
formula reduces to the ordinary independent score test — one test covers both
units.

Measured over ensembles frozen before any result was seen:

| ensemble | cluster test | marginal deviance |
| --- | --- | --- |
| null, shared master trials | **4.0 %** | 0.0 % |
| null, independent namespaces | 3.0 % | 4.5 % |
| curved, `bend = 0.5` | 85 % | 91 % |
| curved, `bend = 1.2` | 100 % | 100 % |

Correcting the size did not cost the power. Nothing is tunable: no seed and no
replicate count are arguments — the count is frozen at
`LACK_OF_FIT_REPLICATES = 499` and the seed is derived from the design digest,
so the same data always give the same p-value. Fewer than
`MIN_LACK_OF_FIT_CLUSTERS = 30` clusters is `uncalibrated_fit`, not a silent
pass. For `master_trial` designs the paired curvature interval and this test are
authoritative and the marginal `lack_of_fit` / `curvature` reasons are dropped;
for `independent_namespace` designs the marginal tests are kept, as the reviewer
directed. `valid_replicates` was renamed **`estimable_replicates`** throughout.

### Authority chain, end to end

```text
ReadOnlyRun        open_for_comparison -> require_closed_ledger (5 files, digests)
RunSweep           one model, one rate, one experiment; every field but 2 identical
design_from_sweep  cells built from the ledgers' own category column
ScalingDesign      .digest = couplings + identities + every outcome
fit_exponent       marginal; carries the digest
resample_exponent  paired; carries the digest, seed, refusals by reason
cluster_lack_of_fit  cluster score + multiplier bootstrap; seed from the digest
calibrate_exponent -> CalibratedExponent (sealed, every field recomputed)
scaling_verdict(sweep, ...)  re-hashes, recomputes all of the above,
                             reads 4 statuses + schema -> machinery_only
control_evidence(role, sweep, ...)   recomputes; role checked against the sweep
paired_exponent_contrast(sweeps)     recomputes; carries both digests + prints
holdout_evidence(3 runs, bins)       computes both scores on frozen_edges
causal_decision                      joins digests/grids/identities/fingerprints
```

### Regression

**114/114** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` gives 114/115 and exit 1; `py_compile` and `compileall`
clean; `results/` absent on every path. ≈ 118 s, peak RSS 608 MB against the
unchanged 900 MB bound. Counts updated to 364 callables / 997 invalid calls /
827 parameters. Criterion 108 added for the calibrated lack-of-fit test.

### Round-3 limitations

- **The seal is not a cryptographic boundary and is not described as one.** It
is the same line this package already draws at the prediction import: the
unsupported route requires writing a leading underscore, which makes it
impossible by accident and visible when taken. `verify.py` takes it openly in
one place, because the decision *rule* and the decision's *binding to runs*
are different subjects.
- The cluster test is **mildly conservative** under the strongest CRN dependence
tested (4.0 % against 5 %). Direction is safe-ish but not guaranteed for every
dependence structure; the measured band is declared rather than assumed.
- `physical_verdict_permitted` is now unreachable **by construction**, not merely
unmet. That is the right state for schema v3, and it means the permission
branch has no positive test — only the schema refusal and the status set
difference. A future production schema will need its own positive control.
- The verifier's real sweeps are six trials per coupling, so their calibrations
are legitimately `no_valid_exponent`. The decision *rule* is therefore
exercised on sealed synthetic evidence and the *binding* on real sweeps.

## Round 4 — the round-three re-review's three P1 findings

All three probes were replayed against the pre-fix bytes and reproduced
exactly — including the reviewer's `43/120` copula rejection rate and seed
`103002` at `p = 0.002` with counts `(187, 337, 466, 500, 500, 500)`.

### R4-P1 — the verdict re-hashed the disk but fitted an in-memory ledger

|  |  |
| --- | --- |
| **Before** | a public `ClosedLedger` with the genuine marker beside forged rows and a forged manifest → `reverify() == True`, fitted counts `(6/6,6/6,6/6,6/6)` over a disk holding `(2/6,4/6,5/6,6/6)`, verdict gates `production_cleared × 4` |
| **After** | the public constructor refuses (`ReadOnlyRun` is sealed); and built *with* the token, `scaling_verdict` still returns the **disk's** gates, counts, design digest and status blockers |

The substantive fix is that the fresh read is now the value consumed.
`ReadOnlyRun.reopen()` and `RunSweep.reopen()` return a **fresh object** parsed
from disk; `reverify()` is a thin reading of it kept for the byte-equality
proof. `scaling_verdict`, `control_evidence`, `paired_exponent_contrast` and
`holdout_evidence` each call `reopen()` immediately before building a design and
compute only from what it returns. The supplied handle is a locator: its name
selects the run, its fingerprint is compared, its data are discarded.

TOCTOU is unchanged in kind and re-checked: `open_raw_run` resolves the package
directory once and opens the results root, the run directory and all five files
under pinned `O_NOFOLLOW` descriptors, so there is no name left to replace after
the reopen. A handle whose bytes changed between opening and reopening is
refused by `reopen` and by the verdict, and reads normally once restored.

### R4-P2 — two causal provenance joins were absent

|  |  |
| --- | --- |
| **Before** | a contrast built from a gate-rewritten twin of the full sweep — *identical* design digest, different fingerprints — accepted; a central control on an unrelated stream hierarchy accepted |
| **After** | both `ValueError` before anything is decided |

`causal_decision` now requires the contrast's two **ordered fingerprint tuples**
to equal the full and width-only evidence's own, not merely the digests.

For the central control, equality of the CRN token is the wrong test — a
one-clock sweep necessarily has a different one — so `EXPERIMENT_FAMILY_FIELDS`
(`CRN_IDENTITY_FIELDS` minus `POPULATION_FIELDS`) gives an
`experiment_family` digest that all three roles must share. The verifier asserts
both directions: the genuine central control shares the family and does *not*
share the CRN token, and the foreign one shares neither. The holdout's
reference fingerprint must also belong to one of the two sweeps.

### R4-P3 — the cluster score omitted the nuisance adjustment

**The derivation.** With `X = [1, log K]`, `W = diag(n_i H_i g(H_i))` and `C` an
orthonormal basis of the Euclidean complement of `X`, the efficient score for
the contrasts *after* estimating the two nuisance parameters is

```text
e_t = C' s_t − C' W X (X'WX)⁻¹ X' s_t
    = B' s_t          with   B = C − X (X'WX)⁻¹ X' W C
```

because the cross-information between the saturated `eta` and `beta` is `W X`
and the nuisance information is `X'WX`. `B` satisfies `X'WB = 0` **exactly**
(checked to `1.4e-14`; the unadjusted `C` is off by `67.0`). The numerator is
unchanged — `Σ e_t = C'S` since `X'S = 0` at the maximum — so only the meat and
the multiplier draws move (meat changes by `29.1`).

**The boundary.** A cell in which every trial did the same thing contributes a
*constant* cluster score: a systematic offset with no sampling variation, which
the sandwich divides by a variance the bootstrap invents, and the ratio grows
with the cluster count. Such a design is now `adequate=False` with the reason
recorded, and `calibrate_exponent` returns `uncalibrated_fit`. **Every cell stays**
**in the likelihood and the report**; a calibration refusal is not cell deletion,
and the verifier asserts `cells_fitted == len(cells)` on the refused fixture.

**Empirical calibration**, method frozen before the table, four dependence
structures from a Gaussian copula rather than the monotone shared-uniform case:

| ensemble | before | after | marginal deviance |
| --- | --- | --- | --- |
| null interior, independent cells | — | 8.7 % | 8.0 % |
| null interior, copula ρ = 0.0 | — | **4.0 %** | 4.7 % |
| null interior, copula ρ = 0.4 | — | **4.7 %** | 2.0 % |
| null interior, copula ρ = 0.8 | — | **4.7 %** | 0.7 % |
| curved bend 0.5, ρ = 0.8 | 85 % | **97 %** | 97 % |
| curved bend 1.2, ρ = 0.8 | 100 % | **100 %** | 100 % |
| **null saturated, ρ = 0.8** (the review's fixture) | **35.8 % rejected** | **0 rejected, 120/120 decline to calibrate** | — |

Seed `103002` now reports `uncalibrated_fit`, not `lack_of_fit`. Correcting the
size raised the power. The marginal deviance grows monotonically more
conservative as dependence strengthens (0.7 % at ρ = 0.8), which is what it was
replaced for.

**Mutation.** `verify` computes the unadjusted basis alongside the adjusted one
and asserts `|X'WC| > 1e-6` while `|X'WB| < 1e-8`, that the numerator is
unmoved and that the meat is not — so restoring the omission is detected
deterministically rather than through a noisy ensemble.

### Round-4 regression

**115/115** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` gives 115/116 and exit 1; `py_compile` and `compileall`
clean; `results/` absent on every path. ≈120 s, peak RSS 580 MB against the
unchanged 900 MB bound. Counts: 368 callables, 1001 invalid calls, 831
parameters. Criterion 109 added; 107 and 108 restated.

### Round-4 limitations

- The seal is still not a cryptographic boundary, and the authoritative-read
fix does not depend on it: the split-brain replay is built *with* the token in
`verify.py` precisely so that the reopen contract, not the seal, is what is
under test.
- `ClosedLedger` itself remains publicly constructible. Sealing it belongs to
ticket 05's module and would touch the raw import graph; the bounded fix here
makes such an object unusable by the decision path instead.
- On the saturated copula fixture the **paired curvature** interval fires in
about 20 % of seeds (`('curvature', 'uncalibrated_fit')` rather than
`('uncalibrated_fit',)`). That is an extra *refusal* on a design that is
already refused, so it can only block and never certify — but the curvature
bootstrap is presumably anti-conservative in the same regime, and a future
round may want the same degeneracy guard applied to it.
- The independent-cell null sits at 8.7 % against a nominal 5 % on 150
datasets (binomial SE ≈ 1.8 %). Inside the declared band, ~2σ high, worth
watching.
- `physical_verdict_permitted` remains unreachable by construction under schema
v3, so the permission branch still has no positive test.

## Round 5 — the round-four re-review's three P1 findings

All three probes were replayed against the pre-fix bytes and reproduced
exactly: the stale-row digest divergence, `drive` absent from the family, and
"curvature excludes zero" for 58 of 100 analysis seeds on seed 103002.

### R5-P1 — a verified snapshot was shallow-mutable

|  | Before | After |
| --- | --- | --- |
| edit one parsed row, then `design_from_sweep(sweep)` | different digest, and it calibrated | **the disk's digest** (the public door reopens) |
| `observables.commitment_counts` on the edited ledger | returned 3 where disk says 2 | `ValueError` |
| `observables.risk_table` / `winner_mismatch` | consumed it | `ValueError` |
| `compare._sweep_counts` | consumed it | `ValueError` |
| `scaling_verdict` with an edited handle | — | returns the disk's design |

Two independent mechanisms, because they catch different things.

`raw_ledger.require_unmutated_ledger` re-encodes the parsed rows through
`encode_table` — the same `header_row` / `encode_row` the writer used — re-emits
the manifest canonically, and requires all four digests to equal the ones the
run's own close marker declares. It needs no disk access, so it protects the
*display* doors, which have a ledger and no run name. Deep immutability was
considered first and rejected: it needs `types.MappingProxyType` or a custom
mapping in `raw_ledger.py`, which is inside the raw import graph and whose
import allowlist is a ticket-01 contract. The re-encode guard is additive,
changes no bytes and no existing signature.

`design_from_sweep` now reopens and delegates to a private
`_design_from_fresh_sweep`, which the four decision factories call after their
own single reopen — so a verdict still costs one read, not two.

### R5-P2 — `experiment_family` omitted the drive

Rebuilt by **subtraction**: `EXPERIMENT_FAMILY_FIELDS` is now all 45 manifest
keys minus 11 reviewed `EXPERIMENT_FAMILY_EXCLUSIONS` — the four sweep-level
differences (`peak_coupling`, `pulse_digest`, `model`,
`fixed_contraction_rate`) and the seven population fields. A field nobody
thought about is now *included* by default, which is the property the old
CRN-derived allowlist lacked.

The verifier mutates **every one of the 45 fields** in turn and requires each
either to change the family or to appear on the exclusion list; five are
structurally pinned by the schema (the two versions and the three column lists)
and are reported as pinned rather than counted as covered. The review's exact
reproduction — a genuine one-clock full-model sweep whose manifest says
`stationary` — is now refused, while the pulsed central control beside it is
accepted.

### R5-P3 — curvature was a rerollable percentile interval

Replaced by the **same one-dimensional cluster score test**, with the quadratic
column W-residualized against `[1, log K]`: `_multiplier_score_test` is now
shared, so lack of fit and curvature cannot drift apart. The percentile interval
survives on `ResamplingReport` as a descriptive figure.

**No authoritative door takes a seed or a replicate count.**
`calibrate_exponent(design)`, `scaling_verdict(sweep)`,
`control_evidence(role, sweep)` and
`paired_exponent_contrast(full, control)` derive everything: the count is
`RESAMPLE_REPLICATES = 499` and the seed comes from the design digest.
`resample_exponent(design, replicates, seed, unit)` keeps both arguments and is
the clearly-exploratory door — it is what the wrong-procedure control is
measured with and it feeds no decision.

**An inadequate calibration makes no positive claim.** A new
`uncalibrated_curvature` reason mirrors `uncalibrated_fit`; seed 103002 now
reports `('uncalibrated_fit', 'uncalibrated_curvature')` with neither
`lack_of_fit` nor `curvature`, and all 120 saturated nulls decline both tests
with every cell still in the likelihood.

Size and power over ensembles frozen after the method, 300 nulls each, every
dataset scored by both tests:

| ensemble | lack of fit | curvature | marginal deviance |
| --- | --- | --- | --- |
| null interior, independent cells | 7.0 % | 4.0 % | 6.7 % |
| null interior, copula ρ = 0.0 | 5.7 % | 7.0 % | 6.0 % |
| null interior, copula ρ = 0.4 | 4.0 % | 4.3 % | 1.3 % |
| null interior, copula ρ = 0.8 | 5.0 % | 3.7 % | 0.7 % |
| curved `bend = 0.5`, ρ = 0.8 | 97 % | 99 % | 97 % |
| curved `bend = 1.2`, ρ = 0.8 | 100 % | 100 % | 100 % |
| null saturated, ρ = 0.8 | *both decline, 120/120* |  | — |

**The guard was tightened.** Null ensembles are judged by the exact two-sided
binomial acceptance region at a level of 1e−3 rather than a hand-picked band.
For 150 datasets that region is `[1, 18]`, so the review's `19/150` mutant fails
and an ordinary `8/150` passes; the suite asserts both directions explicitly.

### API changes

- `calibrate_exponent(design)`; `scaling_verdict(sweep)`;
`control_evidence(role, sweep)`; `paired_exponent_contrast(full, control)` —
all lose `replicates` and `seed`.
- `LackOfFitReport` → `ClusterScoreTest`, with a `kind` field and an
`inadequate_reason`.
- New: `cluster_curvature`, `curvature_column`, `RESAMPLE_REPLICATES`,
`CLUSTER_TEST_KINDS`, `uncalibrated_curvature`,
`EXPERIMENT_FAMILY_EXCLUSIONS`, `raw_ledger.encode_table`,
`raw_ledger.require_unmutated_ledger`.
- `CalibratedExponent` gains `curvature_test`.
- `design_from_sweep` reopens; `_design_from_fresh_sweep` is the private
already-fresh helper.

### Round-5 regression

**115/115** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` gives 115/116 and exit 1; `py_compile` and `compileall`
clean; `results/` absent on every path. ≈150 s (the frozen 499-replicate
authoritative bootstrap costs about 30 s), peak RSS 563 MB against the unchanged
900 MB bound. Counts: 372 callables, 1001 invalid calls, 831 parameters.

### Round-5 limitations

- The re-encode guard is **O(rows) per call**. On the six-trial fixtures it is
invisible; a production ledger will pay for it at every observable door. If
that matters, the right answer is deep-immutable rows at `raw_ledger`, which
needs the raw import allowlist widened by one name.
- `ClosedLedger` is still publicly constructible. A hand-built one now has to
be *self-consistent* to survive the guard, which is a much higher bar, but
sealing it at source remains ticket 05's call.
- The curvature test's null size ranges 3.7–7.0 % over 300-dataset ensembles
(binomial SE ≈ 1.3 %); all four sit inside the exact acceptance region, and
the ρ = 0.0 cell at 7.0 % is the highest.
- `physical_verdict_permitted` remains unreachable by construction under schema
v3, so the permission branch still has no positive test.

## Round 6 — the round-five re-review's single P1

All four all-public rehashed forgeries were replayed against the pre-fix bytes
and reproduced exactly.

### The defect

The round-five guard re-encoded the parsed rows and compared their digests with
the marker the snapshot carried. That catches an edit made *without* reclosing.
It cannot catch an edit made *with* reclosing: a caller may copy the rows, edit
them, re-encode all three tables with the public `encode_table`, rebuild a
public `CloseMarker` over the new digests and construct a new `ClosedLedger` —
which then agrees with its own marker perfectly.

| all-public rehashed forgery | guard, before | authoritative gate |
| --- | --- | --- |
| trial 0 `lock_failed` → `committed` | accept — **5** commitments vs 4 winners | refuse |
| marker declares 7 ledger rows beside the genuine 6 | accept | refuse |
| manifest detunings +0.125, clock rows unchanged | accept — winner grid reads `-1.625` | refuse |
| ledger rows reversed | accept | refuse |

The three observables disagreed with each other on the first variant, which is
the clearest statement of the problem: a tally reporting five commitments beside
a winner table holding four.

### The fix

`require_unmutated_ledger` now reconstructs the canonical manifest and table
bytes from the snapshot and puts those bytes, with the snapshot's own marker,
through the whole of `require_closed_ledger` — the same eight checks a run read
from disk passes, including marker row counts, row identities, ordering and
cross-table reconciliation. **It returns the object that gate parsed.**

| after | result |
| --- | --- |
| all four forgeries at the guard | refused, with the gate's own message |
| all four at `commitment_counts`, `risk_table`, `winner_mismatch` | refused |
| untouched snapshot rebuilt the same way | accepted, same counts |
| `encode_table(parse_table(writer bytes))` | byte-identical to the writer's files |

### API return change, and the callers audited

The function's return value went from "the object you passed" to "a freshly
reconciled object you must use". Every caller now **binds** it:

| caller | before | after |
| --- | --- | --- |
| `observables.commitment_counts` | called, discarded | `ledger = require_unmutated_ledger(...)` |
| `observables.risk_table` | called, discarded | bound |
| `observables.winner_mismatch` | called, discarded | bound |
| `compare._design_from_fresh_sweep` | called, discarded | `reconciled = ...`, outcomes **and** the coupling read from it |
| `compare._sweep_counts` | already consumed the return | unchanged |

That was the second half of the defect: validating one object and continuing
with another is a check-then-use alias, and it is gone.

### No recursion, no schema change

`require_closed_ledger` does not call `require_unmutated_ledger` — asserted by
walking `raw_ledger.py`'s syntax tree over the gate and its seven helpers. The
new function builds bytes and calls the gate once; the gate reads bytes and
knows nothing about it.

`LEDGER_SCHEMA_VERSION` and `MANIFEST_SCHEMA_VERSION` remain 3, the 45 manifest
keys and the 17/19/17 column layouts are untouched, the header rows are
unchanged, and `require_closed_ledger` itself was not edited. Ticket 05's
semantics are strengthened by reuse, not altered.

### Verifier additions

`check_authoritative_read` now builds all four forgeries from public names via a
`_reclosed_ledger` helper and requires each to be refused at the guard **and**
at all three observables — with two controls beside them, an untouched
re-encoded snapshot that passes and gives the same numbers, and a byte-level
check that re-encoding a parsed table reproduces the writer's file exactly. The
exported-surface row for `require_unmutated_ledger` gained a semantic negative
where it previously had only a wrong-type one.

### Round-6 regression

**115/115** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` gives 115/116 and exit 1; `py_compile` and `compileall`
clean; `results/` absent on every path. Peak RSS 576 MB against the unchanged
900 MB bound. Counts: 372 callables, 1002 invalid calls, 831 parameters. Prior
residuals unchanged.

### Round-6 limitations

- The guard now costs a **full authoritative reconciliation** per call —
O(trials × clocks) — where it previously cost a re-encode. On six-trial
fixtures that is invisible; on a production ledger every observable door pays
  254. It is the correct cost for the guarantee, but it is a real one.
- `ClosedLedger` is still publicly constructible. It no longer matters for
correctness — any snapshot must now survive the full gate — but sealing it
would turn a caught error into an impossible one, and that remains ticket
05's call.
- `physical_verdict_permitted` remains unreachable by construction under schema
v3, so that branch still has no positive test.

## Round 7 — the round-six re-review's P1, P2 and P3

All three defects were reproduced against the unmodified bytes before any edit.

### P1 reproduced — a public subclass turns the disk read into an assertion

Seven public lines, no underscore and no seal:

```python
class StaleSweep(compare.RunSweep):
    def reopen(self):
        return self
```

One byte appended to a contributing `manifest.json`, close marker untouched:

| door, over the changed disk state | before |
| --- | --- |
| `design_from_sweep(genuine)` | **refuse** — `manifest digest mismatch` |
| `design_from_sweep(stale)` | accept `ScalingDesign` |
| `scaling_verdict(stale)` | accept `ScalingVerdict` |
| `control_evidence("full", stale)` | accept `ControlEvidence` |
| `paired_exponent_contrast(stale, stale_control)` | accept `ContrastReport` |
| `sweep_master_trials(stale)` | accept |

The rows the stale handle carried were internally valid, so the round-six
re-encode guard could not see that the named files had changed. Only the
skipped reopen could.

### P2 reproduced — two consumers still mixed reconciled and caller state

`_sweep_counts`, with the guard intercepted so it returned the genuine fresh
ledger while the caller's alias changed from six trials to seven:

```text
((3, 6), (5, 6), (6, 6), (6, 6))   ->   ((3, 7), (5, 7), (6, 7), (6, 7))
```

Numerators fresh; the denominator was `run.manifest.trials` from the alias.

`_design_from_fresh_sweep` had the complementary gap. `sweep_master_trials(sweep)`
ran **before** any run was reconciled, so with the guard returning a
namespace-rewritten snapshot the design came back carrying identities under
`crn_identity` = `6ed80e8d…` — the caller's — beside cells built from a snapshot
whose own identity was `48a21125…`.

### The fixes

| what | change |
| --- | --- |
| `_fresh_sweep(sweep, name)` | new: `require_exact_type(sweep, RunSweep, name)` then `RunSweep.reopen(sweep)` — the **unbound** implementation, so the read is never the caller's method |
| `_reconciled_ledgers(sweep, name)` | new: exact type, reconciles **all** runs first, and re-establishes the sweep invariants (increasing couplings, one model, one contraction rate, every frozen field outside `SWEEP_VARYING_FIELDS`) over the *returned* manifests |
| `_fresh_master_trials(ledgers)` | new: trial count **and** namespace from `ledgers[0].manifest` |
| `sweep_master_trials` | now exact-typed, reopens, and derives from the reconciled manifests |
| `design_from_sweep`, `scaling_verdict`, `control_evidence`, both arguments of `paired_exponent_contrast` | `require_instance` + `sweep.reopen()` → `_fresh_sweep(...)` |
| `_design_from_fresh_sweep` | reconciles first; identities, couplings and outcomes all read from that tuple; the caller's sweep supplies only a run *name* for an error message |
| `_sweep_counts` | numerator **and** denominator from the same reconciled ledger |
| `RunSweep.reopen`, `RunSweep.reverify`, `ReadOnlyRun.reverify`, `holdout_evidence` | `run.reopen()` → `ReadOnlyRun.reopen(run)` / `RunSweep.reopen(self)` |
| `ReadOnlyRun.__post_init__` | `require_instance` → `require_exact_type` for `ledger` and `fingerprint` |

The `LedgerFingerprint` tightening is the audit the review asked for rather than
a finding it made: a subclass overriding `__eq__` to return `True` would answer
every reopen comparison in the module with the object being compared.

After the fix, over the same changed disk state, all six doors refuse on type
before consuming anything — and refuse with the bytes intact too, which is what
distinguishes a type boundary from a read that happened to disagree.

### P3 — the README's live ledger API

`README.md:460-527` still documented ticket 01's gate as current:
`require_closed_ledger(payload, marker, manifest) -> CloseMarker`, four checks, a
three-field manifest, and the row parser as future work. Replaced with the live
schema-v3 contract: the five-input signature returning `ClosedLedger`, the three
tables and what each holds, all eight checks in order including cross-table
reconciliation, the 45-key manifest with the field groups that matter, and
`require_unmutated_ledger` as the second door. The anti-accident and
not-authentication caveats that followed were already current and are kept
verbatim.

`_RETIRED_LEDGER_API` is the mechanical guard, added to `_STALE_README_PATTERNS`.
It matches the retired signature, the "checks four things" and "three fields"
claims in the present tense, and the forward-looking row-parser scope note. Six
new positive fixtures quote the retired block verbatim and six negatives cover
the live statements and the same retired facts told as history — so a pattern
that rotted into matching nothing would fail rather than pass louder.

### Verifier additions

`check_authoritative_read` gained the subclass replay (changed byte, restore,
and the type refusal with bytes intact), the `LedgerFingerprint` and
`ClosedLedger` subclass refusals at `ReadOnlyRun`, and the returned-object
interception — the guard hands back the genuine reconciled ledger while the
caller's alias gains a trial and a foreign stream namespace, and the counts,
the identities and the design digest must all stay the disk's. Six
exported-surface negatives were added, one per public sweep door, so the API
census requires the exact-type refusal independently of any single check.

### No schema, semantics or claim change

`observables.py`, `analysis.py`, `raw_ledger.py`, `raw_runner.py`,
`__init__.py` and `validation.py` are byte-identical to round 6. Schema
versions remain 3, the manifest keeps 45 keys and the tables 17/19/17 columns,
`require_closed_ledger` was not edited, and `PRODUCTION_STATUS_SCHEMA = 4` still
makes `physical_verdict_permitted` unreachable. Nothing here claims Born's rule,
a detector click, unique actuality, a microscopic noise origin, a two-channel
outcome or a production-cleared exponent.

### Round-7 closure evidence

Both P1 and P2 replayed against the fixed bytes, same probes:

| probe | before | after |
| --- | --- | --- |
| `design_from_sweep(stale)` | accept `ScalingDesign` | `TypeError: sweep must be exactly RunSweep, got the subclass StaleSweep` |
| `scaling_verdict(stale)` | accept | same refusal |
| `control_evidence("full", stale)` | accept | same refusal |
| `paired_exponent_contrast(stale, stale_control)` | accept | `full_sweep must be exactly RunSweep` |
| `sweep_master_trials(stale)` | accept | same refusal |
| `design_from_sweep(genuine)`, changed byte | refuse | refuse (unchanged) |
| `_sweep_counts`, caller alias 6 -> 7 trials | `((3,7),(5,7),(6,7),(6,7))` | `((3,6),(5,6),(6,6),(6,6))` |
| `_design_from_fresh_sweep` identity namespace | `6ed80e8d…` (caller) | `48a21125…` (reconciled) |

### Round-7 regression

**115/115** on canonical, `--verbose`, direct-script and `-W error`, exit 0 on
all four; `--prove-failure-exit` gives 115/116 and exit 1 with only the
deliberate probe failing; `py_compile` and `compileall` clean; `results/` absent
on every path. Peak RSS 627 MB against the unchanged 900 MB bound. Counts:
115 checks, 372 public callables, **1008** invalid calls (1002 + the six new
subclass negatives, README updated to match), 831 parameters. Prior residuals
identical: survival truth `1.1438094106656083e-3`, cloglog recovery
`2.6231209876820486e-10`, comparator arithmetic `8.881784197001252e-16`,
cluster-test calibration `5.0e-2` against `1e-1`.

Files changed this round: `compare.py`, `verify.py`, `README.md`. Everything
else in the package is byte-identical to round 6. Nothing outside
`adler_born_two_channel/` and this note was touched; the Git working tree still
shows exactly its 29 pre-existing entries, with nothing staged and nothing
committed.

| file | SHA-256 |
| --- | --- |
| `raw_ledger.py` | `91af4540abea7eccd4ab52b25d3e1d3dc7b4f805e283a89f24630d1596c26504` |
| `observables.py` | `38223e39a726b747680d6f16610bb90dae60fa75fd5e1e29f3dbf57ed087fe92` |
| `analysis.py` | `0b3b57ff75f07510b1d0d29d611d0841ed3dc54613ece513e0b56fb1e6e1015b` |
| `validation.py` | `ede647938253fefec4b366dbaa5117356638d070db3a794a6de1252a88bf693d` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |
| `compare.py` | `6bb4be40548b21bb5da9995f09c642c2c3b02dbaa49374f6165532c17ae7f544` |
| `verify.py` | `c942fb70a6b7ba79e96f9895288de9a337b3195a7c22976b1551836c8563fb3c` |
| `README.md` | `82abbc4d4077b3280a0246daace9a35290673eba0beb84467cc8c5d5722067de` |

### Round-7 limitations

- `sweep_master_trials` now costs a full sweep reopen and reconciliation where
it previously read one in-memory manifest. It is a public bridge function and
correctness is the right trade, but it is no longer cheap.
- `_reconciled_ledgers` restates `RunSweep.__post_init__`'s cross-run rules
rather than sharing one implementation with it. That is deliberate — the two
run over different objects — but it is duplicated logic that must stay in
step, and only the verifier enforces that today.
- `RunSweep` and `ReadOnlyRun` remain publicly subclassable. Every boundary now
refuses a subclass, so this is a caught error rather than an impossible one.
