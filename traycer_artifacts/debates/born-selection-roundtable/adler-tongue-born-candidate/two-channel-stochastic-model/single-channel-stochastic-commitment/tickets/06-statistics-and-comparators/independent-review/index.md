---
title: "Independent review: Ticket 06 statistics and comparators"
kind: review
---

# Independent review: Ticket 06

## Strict verdict: OPEN

The read-only ledger boundary, raw import isolation, survival arithmetic, direct
count likelihood, exact-grid comparator arithmetic, and scientific non-claims
survive the cold review. Ticket 06 remains open because the public decision path
does not bind fits, numerical gates, master-trial identities, negative-control
roles, or holdout evidence to the closed manifests that are supposed to be
authoritative. Two additional numerical defects let invalid diagnostics enter a
valid result.

These are actionable scientific-boundary defects. In particular, the current
API can return `physical_verdict_permitted` without opening a ledger, and can
return `not_blocked` when both negative controls explicitly report
`no_valid_exponent`.

## Findings

### P1 — The Ticket-04 numerical gate is caller-asserted rather than manifest-bound

`compare.scaling_verdict` accepts an arbitrary tuple of strings
(`compare.py:924-970`). It does not accept `ReadOnlyRun` objects, fingerprints,
or a manifest-bound sweep. The verifier even treats a caller-supplied
`("production_cleared",)` as a positive control (`verify.py:23020-23032`). This
contradicts the module and README claim that no argument can bypass the
`diagnostic_only` manifests.

Independent reproduction, from the repository root:

```python
from adler_born_two_channel import analysis as a, compare as c

ks = (.2, .3, .45, .7, 1., 1.5)
ids = tuple(range(4000))
cells = []
for k in ks:
    q = 1.0 - __import__("math").exp(-(k * k))
    y = round(4000 * q)
    cells.append(a.CouplingCell(k, ids, (True,) * y + (False,) * (4000-y)))
report = a.fit_exponent(a.ScalingDesign(tuple(cells), "master_trial"))
print(report.verdict, report.exponent)
print(c.scaling_verdict(report, ("production_cleared",)).verdict)
```

Observed:

```text
valid_exponent 2.000...
physical_verdict_permitted
```

No ledger is opened in this reproduction. A good synthetic fit therefore gains
the permission that every real schema-v3 run must be denied.

**Minimal bounded fix:** introduce one manifest-bound sweep/evidence object made
only from `ReadOnlyRun` instances opened through `open_for_comparison`. Derive
all numerical gates inside `scaling_verdict` from those hashed manifests; remove
the public string input. Validate that all non-coupling frozen fields agree and
that every contributing run is represented exactly once. Add the reproduction
above as a must-block mutation and retain the positive control only through an
independently constructed, hash-valid future manifest when that schema value is
actually authorized.

### P1 — Common-random-number inference is computed but not used, and refused resamples are called valid

The direct likelihood is a sound marginal count estimator, but its expected-
information Wald interval, deviance p-value, and curvature likelihood-ratio
p-value assume independent coupling-cell counts (`analysis.py:767-800`). A
`master_trial` sweep deliberately violates that assumption. The paired
bootstrap exists, but neither `ExponentReport.is_valid`, `causal_decision`, nor
`scaling_verdict` consumes it. The causal rules therefore use the same
independence-like Wald interval that the implementation's own wrong-procedure
control is meant to reject.

Independent 600-trial common-random-number sweep:

```text
expected-information Wald stderr       0.06112
paired master-trial bootstrap stderr    0.07932
wrong independent-cell stderr           0.06219
```

The Wald result tracks the intentionally wrong independent-cell procedure, not
the paired uncertainty. Thus uncertainty, lack-of-fit, and curvature are not
mathematically calibrated for the supported `master_trial` design.

There is a second defect in the same path. `resample_exponent` appends any
finite exponent, regardless of `report.is_valid` (`analysis.py:983-985`), and
`paired_exponent_contrast` does the same for both fits
(`compare.py:791-794`). A four-trial-per-cell paired fixture produced:

```text
original fit: no_valid_exponent ('uninformative',)
ResamplingReport.valid_replicates: 50 / 50
independent replay: 50 finite exponents, 0 genuinely valid reports
```

Every replicate was refused, yet the public report labels every one valid and
returns a percentile interval. The paired contrast can likewise look powered
using two refused fits.

**Minimal bounded fix:** for `master_trial` designs, make paired cluster
resampling (or a validated cluster-robust equivalent) authoritative for exponent
uncertainty and calibrate the goodness/curvature decisions under the same
pairing. Count a replicate only when its `ExponentReport.is_valid` is true,
carry refusal counts by reason, and freeze a minimum adequate valid-replicate
fraction. `scaling_verdict` and every control decision must require this
authoritative uncertainty record; an inadequate resampling record blocks.

### P1 — Refused controls and missing holdout evidence can pass causal attribution

The execution notes and README say that an inadequate control has an unbounded
interval and therefore blocks. That premise is false for `lack_of_fit` and
`curvature`: `fit_exponent` retains a finite, often narrow Wald interval for
those refusal reasons. `causal_decision` ignores the control verdicts and only
asks whether those intervals contain two (`compare.py:860-892`).

An independently generated logistic-in-coupling negative control gave:

```text
full:     valid_exponent  2.00058  interval (1.95325, 2.04790)
control:  no_valid_exponent ('lack_of_fit',)
          exponent 2.99103 interval (2.92304, 3.05903)
decision with both controls refused: not_blocked ()
```

The exact call used a finite strong `ContrastReport` and
`control_not_worse=False`. That last argument is itself another bypass:
`causal_decision` accepts a bare boolean, not the frozen holdout scores. Missing
holdout evidence is indistinguishable from evidence that the control was worse.
Neither the central report nor the width-only report carries a manifest,
fingerprint, model role, clock population, or proof that it used the same
pipeline.

The time-resolved helper is also weaker than its documentation. It compares
survival sequences only by length (`compare.py:627-635`), not by matching
`left`, `right`, and `width`; and `rising_falling_split` assigns a bin that
straddles the pulse centre wholly to the falling side
(`compare.py:591-595`). Arbitrary whole-window bin edges can therefore change
the frozen score after the fact.

**Minimal bounded fix:** any non-valid central or width-only fit must block,
whatever finite provisional interval it carries. Replace the boolean with a
manifest/fingerprint-bound holdout evidence object computed inside the decision
path from frozen edges and the declared reference. Missing or inadequate
holdout becomes a named blocker. Require identical time grids and widths and
require the pulse centre to be an edge (or split the straddling interval by a
predeclared rule). Bind control roles: central must be the one zero-detuning
clock; width-only must be the paired fixed-contraction model on the same frozen
sweep.

### P1 — Master-trial identity omits the dataset namespace

`CouplingCell` identifies a trial by a non-negative integer only
(`analysis.py:350-396`). `ScalingDesign` proves pairing by comparing those
integer tuples (`analysis.py:472-480`). It cannot represent, serialize, or
compare the manifest's `stream_namespace`, mesh identity, or run fingerprint.
Consequently two physically different datasets whose local rows are both
numbered `0..n-1` are accepted as paired.

Public signatures and reproduction:

```text
CouplingCell(coupling, trial_ids, outcomes)
ScalingDesign(cells, resampling_unit)
paired_exponent_contrast(two designs with ids 0..99): accepted
```

There is no argument in which the two distinct namespaces could have been
supplied. Reordered, duplicated, missing, and numerically substituted local IDs
are refused, but a substituted namespace is invisible. That is not an
injective master-trial identity across runs.

**Minimal bounded fix:** use an immutable canonical identity containing at
least the hashed stream namespace and master trial number, or bind the entire
design to a verified common namespace/fingerprint set while retaining the
trial number. Construct designs from `ReadOnlyRun` objects rather than caller-
assembled integer IDs. Require exact identity/order equality for paired cells
and full/control designs; require pairwise disjoint canonical identities for
independent namespaces. Add namespace substitution beside the existing
reorder/duplicate/missing mutations.

### P2 — An unidentifiable curvature extension can still certify a valid exponent

`fit_exponent` computes the curvature fit's information condition and sets
`curvature_stderr=inf` when it is singular (`analysis.py:788-795`), but the
verdict logic never checks that condition, the curvature fit's convergence, or
its runaway flag (`analysis.py:821-837`). A p-value of one from a zero
likelihood-ratio is then enough to pass an extension whose coefficient is not
estimable.

Exact deterministic reproduction used six couplings
`1.000, 1.002, ..., 1.010`, 200,000 trials per cell, and exactly half events in
every cell:

```text
verdict                 valid_exponent
exponent interval       (-0.75949, 0.75949)
curvature rcond         9.759e-11  (below the frozen 1e-10 cutoff)
curvature stderr        inf
curvature p             1.0
```

The power-model exponent is adequately informed, but the required curvature
diagnostic is not. The ticket says curvature failure returns no valid exponent;
this currently returns one.

**Minimal bounded fix:** require the curvature fit to converge without runaway
and its information matrix to exceed the frozen reciprocal-condition threshold
before a power exponent can be valid. Otherwise return `no_valid_exponent`
under a named closed-vocabulary reason. Add the narrow-grid/high-information
fixture above and a nearby identifiable positive control.

### P3 — README contains a live Ticket-04 contradiction

`README.md:103-106` correctly states that the stationary killed-diffusion gate
passed and the moving-band audit returned `numerical_no_result`. Nine lines
later, `README.md:112-115` says the stationary oracle “is a later ticket” and
has not passed. The execution notes acknowledge this as stale, but Ticket 06
modified the same README and the requested regression matrix includes its
nonclaims. A reader encounters mutually exclusive numerical status statements
before reaching the analysis section.

**Minimal bounded fix:** update the stale paragraph to say that the stationary
oracle passed its reference budget while the moving-band diagnostic and the
production budget remain uncleared. Add this exact contradiction to the README
semantic check rather than checking only required phrases.

## Judgment calls reviewed

| Judgment | Independent disposition |
| --- | --- |
| Adequately informed constant response | A valid exponent near zero is correct. The declared model includes `p = 0`; refusing it would erase a real negative scaling result. The existing `flat` reason is better read as singular information, not a constant response. |
| Wald interval and frozen ±1 cap | A regular Wald interval is a defensible display quantity for independent namespaces, and ±1 is a conservative frozen informativeness cap. It is not valid as the authoritative CRN interval and must not rescue refused controls. |
| Risk table spans the whole window | Correct and load-bearing. Independent nonuniform tied/censored arithmetic conserved all ten trials and exactly reproduced product-limit survival and Nelson–Aalen cumulative hazard. |
| New paired exponent contrast | Needed, but it is not yet trustworthy because namespace identity is absent and finite exponents from refused replicates are retained. |

## Regression evidence

Environment: CPython 3.12.6, NumPy 2.3.5, macOS arm64.

| Command/probe | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 111/111 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 111/111; peak RSS 653 MB under 944 MB; largest declared array 19.2 MB |
| `python3 adler_born_two_channel/verify.py` | exit 0, 111/111 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 111/111 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 111/112; only the deliberate probe failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| Fresh-interpreter raw import | only the ten expected raw modules; no analysis, comparator, analytic, oracle, or audit module |
| Independent SciPy likelihood cross-check | exponents -2, 0, and 2 agreed within `2.5e-8`; `K=0` refused |
| Adversarial nonuniform risk table | widths, risk, event and censor counts retained; survival/hazard conserved exactly |
| Exact-grid comparator arithmetic | independently recomputed values agree; flux remains spacing-weighted and non-finite-population |
| Results cleanup | `adler_born_two_channel/results/` absent after completed paths |

Pre/post SHA-256 digests were identical for all seven Ticket-06 implementation
and documentation files reviewed:

| File | SHA-256 |
| --- | --- |
| `observables.py` | `762d6a8f4c2db7bafeae0378886ae196af74ac36d4a3380f5945433c7f29b40a` |
| `analysis.py` | `37b276db3adeac13c02947e5bad1132aec4f5eaf23c253ecd5eb622dece81e69` |
| `compare.py` | `1f501de12782cbc00a02c58af96845f80d7ebea1d230a387d9a93a2e3eff1148` |
| `verify.py` | `ee4e63865b4fe15c1da773e2455981dc4967c25a3ae566f3cded7eab1feb109a` |
| `README.md` | `e019ca4c681ba6077b496814a58df617bf069827aff3cbe9fec2c7ee0f74e98c` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

## Scope and scientific boundary

No implementation, check, README, ticket status, Git index, or unrelated file
was edited by this review. All targeted probes were external synthetic inputs;
no source mutation required restoration. The identical pre/post digests above
and the absent results directory are the final cleanup check.

Nothing in this review asserts Born's rule, a detector outcome, absorption,
unique actuality, a microscopic origin of the noise, a two-channel result, or a
production-cleared exponent. The strict verdict is OPEN because the software
can currently manufacture permission and causal non-defeat that the closed
manifests and failed diagnostics do not support.

## Fix-up closure re-review — 2026-08-28

### Verdict: OPEN

Four of the original six findings are closed outright, and the two broad
statistical/control fixes are materially better. The re-review nevertheless
found three actionable defects in the new authority objects. Two permit a
caller to manufacture a physical permission or a causal `not_blocked` result
without the exact evidence those results claim to summarize. The third leaves
general power-law lack-of-fit uncalibrated for the supported common-random-
number design.

The evidence below is a cold replay against the current bytes. The verifier's
fixture helpers were used only to write genuine closed schema-v3 runs; every
assertion and mutation was made independently of the verifier's checks. One
ledger byte was changed and restored inside `finally`, all generated runs were
removed, and the reviewed source hashes remained unchanged.

### P1 — Physical permission is still caller-constructible and ignores contradictory validation status

`CalibratedExponent.__post_init__` validates vocabulary and the superficial
relationship between `verdict` and `reasons`, but it does not require any of
its published values to equal its `ExponentReport` or `ResamplingReport`
(`analysis.py:1398-1426`). `ScalingVerdict` is likewise publicly constructible
as a physical permission from a claimed `closed_runs` source, without checking
that its fingerprints are even `LedgerFingerprint` objects
(`compare.py:1559-1588`). These are the same kind of caller assertion the old
gate-string signature was meant to remove.

The manifest-bound path also checks only `numerical_gate`; it does not inspect
`endpoint_status`, `moving_band_status`, or the validation note
(`compare.py:1638-1648`). The verifier's positive control rewrites only the gate
to `production_cleared` and re-hashes the manifest. It leaves this contradictory
status in the same hashed manifest:

```text
endpoint_status     passed at the declared reference tolerances
moving_band_status  numerical_no_result pooled and in fourteen of fifteen cells
numerical_gate      production_cleared
validation_note     This run is therefore diagnostic ... No ... exponent and
                    no scaling claim may be drawn from these tables.
```

An exact replay over that sweep produced:

```python
actual = calibrate_exponent(design_from_sweep(cleared), 50, 12)
# actual.reasons == ('curvature_unidentified', 'uninformative',
#                    'inadequate_resampling')
forged = CalibratedExponent(
    actual.design_unit, actual.report, actual.resampling,
    "valid_exponent", (), 1.0, 0.05, (0.8, 1.2), (-0.1, 0.1))
scaling_verdict(forged, cleared).verdict
# 'physical_verdict_permitted'
```

The forged interval and verdict disagree with both records it carries. The
permission nevertheless has no reasons, even though its hashed manifest still
says `numerical_no_result` and explicitly forbids an exponent. The output type
has an even shorter bypass:

```python
ScalingVerdict("physical_verdict_permitted", "closed_runs", (),
               ("production_cleared",), ("not-a-fingerprint",))
# accepted
```

There are two additional gaps in the same binding:

- `scaling_verdict` compares aggregate `(committed, trials)` counts only. A
different master-trial outcome matrix with the same cell totals can have a
different paired bootstrap but is indistinguishable here; no design digest
or identity/outcome binding exists.
- `RunSweep` accepts an alternating mixture of full and width-only runs, and
`design_from_sweep` fits it. The `model` property raises only if somebody
happens to read it; `scaling_verdict` does not. The same structure permits
fixed contraction rate to vary between cells despite the plan's one-rate
control (`compare.py:458-495`, `513-573`).

**Minimal bounded fix:** make schema v3 fail closed on its only coherent
status tuple: `diagnostic_only` plus the current moving-band
`numerical_no_result`. A future permission needs a schema revision carrying a
closed-vocabulary production-budget status; changing one free-text gate field
must not create it. Check every load-bearing status in `scaling_verdict` as a
second fail-closed boundary. Make `CalibratedExponent` and `ScalingVerdict`
factory-only (or validate every derived field exactly), and bind the calibration
to a digest of ordered couplings, canonical master-trial identities, outcomes,
and run fingerprints. Prefer computing calibration from the re-opened
`RunSweep` inside the verdict path. Require one model per `RunSweep` in
`__post_init__`, and require one common positive fixed rate across a width-only
sweep. Replace the verifier's gate-only positive control with a negative
contradictory-status mutation until a real production schema exists.

### P1 — Causal evidence remains forgeable and is not joined by provenance

The direct refused-control fixes work: the real four-trial full, central, and
width-only calibrations all caused `causal_decision` to return `blocked` with
the three named no-valid-exponent reasons. Frozen holdout construction also
checks roles, grids, edges, and scores correctly.

The new evidence objects do not, however, prove that those are the objects the
decision consumed:

- `control_evidence` checks couplings and role but not ledger counts or the
master-trial outcome matrix (`compare.py:1274-1292`). It accepted an honest
synthetic calibration with counts `[(54,120), (66,120), (76,120), (87,120)]` as evidence for a closed sweep holding `[(2,6), (4,6), (5,6), (6,6)]`.
- `ContrastReport` carries no coupling grid, CRN identity, design digest, or
fingerprints (`compare.py:1068-1079`). A caller-authored adequate interval is
indistinguishable from the output of `paired_exponent_contrast`.
- `HoldoutEvidence.complete` and both scores are caller-settable
(`compare.py:1311-1334`). `causal_decision` only prevents its full and control
fingerprints from being equal; it never requires either fingerprint to
belong to the full and width-only evidence (`compare.py:1484-1527`).
- `ControlEvidence` carries no numerical gates or validation statuses, so a
causal decision cannot block a diagnostic-only experiment.

Combining those public paths reproduced the forbidden result:

```text
underlying full calibration reasons:
  curvature_unidentified, uninformative, inadequate_resampling
underlying central calibration reasons:
  curvature_unidentified, uninformative, inadequate_resampling
underlying width calibration reasons:
  saturated, curvature_unidentified, uninformative, inadequate_resampling

caller-built ContrastReport: 100/100, interval (0.5, 1.5)
caller-built HoldoutEvidence: complete=True, control deliberately worse
holdout full/control fingerprints present in the control evidence: False, False
causal_decision: not_blocked ()
```

`CausalDecision("not_blocked", (), 1.0, 0.25)` is also directly constructible.
This is not a cryptographic threat model; it is an ordinary supported-API
correctness failure, exactly like the earlier caller-supplied gate string and
boolean holdout.

**Minimal bounded fix:** make `ControlEvidence`, `ContrastReport`,
`HoldoutEvidence`, and `CausalDecision` factory-only derived records. Bind each
calibration to the exact sweep design digest described above. Have
`paired_exponent_contrast` carry the full/control design digests, coupling grid,
CRN identity, and fingerprints; require exact matches in `causal_decision`.
Require the holdout full fingerprint to belong to the full sweep and its control
fingerprint to the width-only sweep, with the declared reference fingerprint
bound as well. Represent missing holdout as `None` or a private missing factory,
not a caller-writable `complete` bit. Carry the hashed gate/status tuple into
each control and add a numerical-not-cleared blocker. Add count substitution,
unrelated contrast, unrelated holdout, and direct-constructor mutations.

### P2 — Replicate estimability is now right, but general CRN lack-of-fit is still uncalibrated

The documented choice not to apply `report.is_valid` to every bootstrap
replicate is sound. A replicate with separation, singular information,
nonconvergence, or unidentified curvature has no usable estimate and must be
dropped. A replicate whose finite estimate merely triggers a marginal
`lack_of_fit` or `curvature` test still contributes to the paired distribution,
because those marginal tests assume independent cells. Strict validity would
destroy calibrated designs: in an independently generated exact power-law CRN
fixture, one seed had 58 marginal goodness flags among 100 bootstrap draws
while the original fit and paired exponent/curvature intervals were valid.

The public names and documentation should say **estimable replicates**, not
valid replicates, but that is not the substantive defect. The substantive gap
is that only curvature gets a paired replacement. `calibrate_exponent` carries
every marginal reason into the final verdict (`analysis.py:1472`) and then adds
a paired percentile interval for the quadratic coefficient
(`analysis.py:1482-1488`). It has no paired or cluster-robust general
lack-of-fit statistic. Yet the module itself correctly states that the marginal
deviance null is invalid under master-trial pairing
(`analysis.py:1348-1354`). Applying it once does not make it calibrated.

Independent null simulation over 500 exact power-law datasets, 400 trials and
six frozen cells, showed the distortion:

| Design | marginal lack-of-fit rejection | marginal curvature rejection |
| --- | --- | --- |
| shared master trials | 0.6% | 3.4% |
| genuinely independent namespaces | 4.4% | 5.6% |

The nominal level is 5%. Under this representative positive CRN dependence the
deviance test is strongly conservative statistically—meaning it under-rejects
non-power responses, not that it is a safe extra refusal. The design type does
not require a covariance sign, so the direction is not guaranteed in general.
A moderate log-curvature fixture (`bend=0.5`, 200 trials) passed because its
paired curvature interval crossed zero while 20/100 resamples carried marginal
goodness flags. That example is underpowered rather than proof that those flags
should be gates; conversely, an obvious stronger curved fixture was refused.
The right conclusion is not to restore strict `is_valid`, but to finish the
paired model-adequacy calculation.

**Minimal bounded fix:** retain the current estimability rule. For
`master_trial` designs, add a cluster-calibrated general lack-of-fit test—for
example a master-trial multiplier/bootstrap test of the saturated-cell versus
power-model residual contrasts centered under the fitted null, or an
equivalent cluster-sandwich score/Wald test over the `cells - 2` contrasts.
Use that and the paired curvature interval as the authoritative goodness gates;
keep marginal p-values descriptive only. For independent namespaces, the
existing binomial chi-square/LR tests may remain authoritative. Rename
`valid_replicates`/its prose to `estimable_replicates` or state the distinction
without contradiction.

## Disposition of the original six findings

| Original finding | Re-review disposition |
| --- | --- |
| Caller-forged gate strings | The exact tuple-string call is now a `TypeError`; changed, partial, duplicated, and reordered sweeps refuse. **Not fully closed** because contradictory hashed statuses and public verdict/calibration constructors still manufacture permission (P1). |
| Paired uncertainty unused / refused resamples called valid | Paired uncertainty is now published, four-trial resampling reports `0/50`, and wrong independent-cell spread is smaller in all replayed seeds. **Mechanically closed**, with the remaining cluster lack-of-fit gap in P2. |
| Refused controls and missing holdout pass | Honest refused controls, inadequate contrast, and incomplete holdout each block. **Not fully closed** because provenance-free public evidence recreates `not_blocked` (P1). |
| Master identity omits namespace | **Closed.** Namespace-plus-trial identity is injective, frozen, and substitution/duplicate/reorder safe; equal integers from different namespaces refuse pairing. |
| Singular curvature can certify | **Closed.** The exact narrow grid now refuses under `curvature_unidentified` with infinite stderr; a nearby wide identifiable design is valid at `p=1.99994`. |
| Stale Ticket-04 README sentence | **Closed.** Live wording is correct; 32 mechanical fixtures catch the stale forms while leaving historical prose legal. |

## Independent positive evidence

- A constant adequately informed response returned a valid exponent
`-3.66e-17` with stderr `0.00719`. This is the correct negative scaling
result; `flat` remains reserved for singular likelihood information.
- An adversarial nonuniform risk table with widths `(0.5, 1.0, 0.5)`, risk
`(10, 8, 4)`, events `(2, 3, 1)`, and censoring `(0, 1, 3)` reproduced
survival `(1, .8, .5, .375)` and Nelson-Aalen cumulative hazard
`(0, .2, .575, .825)` exactly. Every display row retained width, risk,
events, censoring, dimensionless conditional failure, and width-divided rate.
- Direct cloglog likelihood retained every cell and has no window argument.
Zero/all-event, separation, negative/unconstrained exponent, saturation,
singular information, strong curvature, and strong non-power probes behaved
as declared. A random audit of 20,000 count/design configurations found no
optimizer result marked converged with a materially nonzero final Newton
decrement.
- Four independent CRN fixtures gave wrong-independent/paired stderr ratios
`0.890, 0.931, 0.736, 0.810`; the intentionally wrong procedure understated
uncertainty every time.
- Exact-grid comparator arithmetic remained distinct. The canonical check's
independent recomputation residual was `8.88e-16` against `1e-12`; continuum
flux remains spacing-weighted and non-finite-population.
- Changed-ledger reverify failed on the recomputed digest, and the exact restored
bytes reopened normally. Fresh raw import remained isolated from analysis,
comparators, prediction, oracle, and audit.

## Regression matrix and cleanup

Environment: CPython 3.12.6, NumPy 2.3.5, macOS arm64.

| Command | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 113/113 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 113/113; reported peak RSS 614 MB below 944 MB, largest allocation 19.2 MB |
| `python3 adler_born_two_channel/verify.py` | exit 0, 113/113 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 113/113 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 113/114; only deliberate probe failed |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| Results cleanup | zero entries under `adler_born_two_channel/results/` |

Key residuals remain within their prior tolerances: cloglog recovery
`2.623e-10 <= 1e-6`, survival truth `1.144e-3 <= 1e-2`, paired-control ratio
`0.861 <= 0.95`, and comparator arithmetic `8.882e-16 <= 1e-12`.

Pre/post SHA-256 digests were identical:

| File | SHA-256 |
| --- | --- |
| `observables.py` | `762d6a8f4c2db7bafeae0378886ae196af74ac36d4a3380f5945433c7f29b40a` |
| `analysis.py` | `01d294674f42d35050764d0b0538859ab95b1133e8f070f5ca2d8830d254a5a0` |
| `compare.py` | `14a8d1bb04aa0e44b0c6109c5652e3066c15356474259c1ed475ca298deddf16` |
| `verify.py` | `1ba4325de541112b2b2d208ea997b3b581802c90b949d30e62d061ddf8233398` |
| `README.md` | `03db0afd9e3a611a0e6e32cfa5abc55cf1c043859097430cbe1b22c08c247ce2` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

No implementation, verifier, README, ticket status, Git index, or unrelated
file was edited. Only this existing review artifact was appended.

Nothing here is a Born-rule, detector-outcome, absorption, unique-actuality,
microscopic-noise, two-channel, or production-cleared exponent claim. The
strict disposition remains **OPEN** until the three bounded authority and
calibration fixes above are closed.

## Round-three closure re-review — 2026-08-28

### Verdict: OPEN

Round three closes the direct-constructor and schema-v3 permission attacks, and
the ordinary synthetic ensembles show that the new lack-of-fit test can be
discriminating. It does not close the ticket. A cold read and independent
replays found three current defects: the supposed authoritative-ledger reopen
does not use the reopened ledger, two causal provenance joins are absent, and
the cluster score/bootstrap is neither nuisance-adjusted nor calibrated in an
allowed saturated-cell regime.

### P1 — The verdict re-hashes the disk but fits a caller-constructed in-memory ledger

`ClosedLedger` and `ReadOnlyRun` are both exported public constructors.
`ClosedLedger.__post_init__` checks the *types* of its marker, manifest and row
containers, but does not establish that the rows or manifest are the bytes the
marker names (`raw_ledger.py:1107-1135`). `ReadOnlyRun.__post_init__` derives its
fingerprint from that marker alone (`compare.py:386-417`). Most importantly,
`ReadOnlyRun.reverify()` reopens the named disk run and compares fingerprints,
but returns only the new fingerprint (`compare.py:424-438`); it neither compares
nor replaces `self.ledger`. `design_from_sweep` subsequently reads
`run.ledger.rows("ledger")` from the old in-memory object
(`compare.py:661-688`), and `scaling_verdict` follows exactly that sequence
(`compare.py:1888-1890`).

The independent replay used one genuine closed four-cell sweep and no private
seal. For each run it constructed a public `ClosedLedger` with the genuine
marker and fingerprint but with every trial category changed to `committed` and
all four free-text status fields changed to `production_cleared`. The disk was
not changed:

```text
forged_sweep.reverify()                         True
genuine disk gates                              diagnostic_only x 4
in-memory gates                                 production_cleared x 4
genuine counts                                  (2/6, 4/6, 5/6, 6/6)
in-memory counts                                (6/6, 6/6, 6/6, 6/6)
scaling_verdict accepted                        machinery_only
verdict gates                                   production_cleared x 4
verdict digest == forged in-memory design       True
remaining status blocker                        schema v3 only
```

Schema v3 still prevents a physical permission, so the present failure does
not create a production exponent. It does prove that the claimed authoritative
boundary is not the source of the fitted rows, gates, model/configuration or
status. The same forged `RunSweep` can be handed to `control_evidence` and the
other sealed factories, so factory sealing does not repair this lower boundary.
It also makes the live README statements that `ReadOnlyRun` objects “can only
come from `open_for_comparison`” and that the fit uses “the re-opened sweep's own
ledgers” false (`README.md:3270-3276`).

**Minimal bounded fix:** make the fresh read the value that is consumed. Have a
reverification operation return a fresh `ReadOnlyRun`/`RunSweep`, and have every
analysis/control/contrast/holdout factory build exclusively from that fresh
object. Seal `ClosedLedger` so only `require_closed_ledger` can construct it, or
repeat the complete authoritative validation in its constructor; make parsed
rows immutable so a genuine returned object cannot be shallow-mutated. Add the
exact public-constructor replay above and assert that changing only the
in-memory manifest or rows refuses before any design is built.

### P1 — `causal_decision` still accepts foreign contrast fingerprints and an unrelated central experiment

The new evidence records carry substantially better roots, but the decision
does not join all the roots it carries. It compares the contrast's two design
digests, coupling grid and CRN identity (`compare.py:1702-1713`), but never
compares `ContrastReport.full_fingerprints` or `control_fingerprints` against
the corresponding evidence fingerprint tuples. It checks the full and
width-only CRN identities (`compare.py:1690-1694`), but there is no experiment-
family check for the central control. A central sweep necessarily has a
different full CRN token because population and detunings differ, so equality
is not the right check; some separate digest over the fields that should remain
common is required.

Two all-public, factory-produced replays were accepted structurally:

```text
contrast full digest == full evidence digest    True
contrast full fingerprints != evidence prints  True
causal_decision                                 accepted, returned blocked

foreign central stream identity != declared    True
causal_decision                                 accepted, returned blocked
```

The first contrast came from the gate-rewritten full sweep and the genuine
width-only sweep; deterministic rows gave the same exact design digest, while
the full manifest fingerprints differed. The second central control was a
genuine one-clock sweep whose manifest-frozen stream namespace was replaced by
an unrelated hierarchy and rehashed before `control_evidence` computed it.
Current schema-v3 status blockers make both final decisions `blocked`, but the
documented contract is that evidence is fully joined *before* it is decided;
this becomes a live substitution the moment a production schema exists.

`ScalingDesign.digest` correctly distinguishes same totals/different outcome
matrices, but it covers design observations, not run fingerprints, model/status
provenance or the entire experiment. Round three carries those separately and
then fails to join them. That is why equal design digests do not cure the first
reproduction.

**Minimal bounded fix:** require exact equality of both contrast fingerprint
tuples with the full and width-only evidence tuples. Add an
`experiment_family_digest` computed by `control_evidence` from the manifest
fields that must agree across the full and central experiments while excluding
only their declared control differences; require it across all three roles.
Add the two genuine-factory replays above. Keep the holdout fingerprint
membership checks already present.

### P1 — `cluster_lack_of_fit` omits nuisance-score adjustment and falsely rejects an allowed saturated null

The implementation calls the Euclidean complement of `[1, log K]` the
lack-of-fit space, projects each raw saturated-cell score into it, and forms the
meat and multiplier draws directly from those projections
(`analysis.py:1068-1088`). The total score is orthogonal to the nuisance design
at the restricted MLE, but each *cluster contribution* is not. The robust score
contribution for a contrast basis `C` must remove the fitted intercept/slope
directions, for example

```text
e_t = C' s_t - C' W X (X' W X)^-1 X' s_t
```

under the implementation's expected-information notation. The second term
sums to zero in the observed total at the MLE; it does not vanish from the
cluster meat or from a multiplier draw. Re-signing raw `C' s_t` therefore does
not reproduce the score's distribution after fitting the two nuisance
parameters. The prose claim that the multiplier score is “centred under the
fitted null by construction” also does not address sparse cells whose raw
per-cluster score is nearly deterministic.

An independently coded nuisance-adjusted calculation on a six-cell CRN
non-power fixture gave package bootstrap `p = 0.118` versus adjusted-score
`p = 0.027` from 1,999 external multipliers. The paired curvature interval
still refused that particular fixture, so it is evidence about the statistic,
not a claim of an overall false pass.

The overall false decision appears at the ticket's required boundary cells. I
generated exact power-law marginals

```text
log H(K) = 0.7 + 1.6 log K
K = (0.4, 0.7, 1.2, 2.0, 3.5, 6.0),  n = 500
```

with within-master dependence from a Gaussian copula of correlation `0.8`.
Every marginal is exactly the fitted null; the master-trial contract imposes no
monotonicity assumption. Across 120 external seeds, all 120 tests called
themselves adequate and **43/120 = 35.8%** rejected at the nominal 5% level.
Seed `103002` is the smallest exact reproduction retained:

```text
counts                    (187, 337, 466, 500, 500, 500) of 500
marginal fit reasons      ()
cluster bootstrap p       0.002
paired curvature interval (-0.0148, 0.4653)
calibrated reasons        ('lack_of_fit',) only
```

Thus an estimable, exactly specified power response is refused solely by the
new authority. The ordinary regime is not broken: independent external seeds
gave null rejection `10/200 = 5%` for shared master trials and `4/200 = 2%` for
independent namespaces, with power `83/100 = 83%` at bend 0.5 and `60/60 = 100%` at bend 1.2. The defect is specifically the supported sparse/saturated
regime and the score construction, which the current frozen ensembles do not
cover.

**Minimal bounded fix:** form nuisance-adjusted cluster contributions before
the sandwich and multiplier bootstrap, and validate size over predeclared
interior, sparse, zero-event and all-event null ensembles with more than one
dependence structure. If a boundary design lacks enough stochastic variation
for the bootstrap calibration, return `adequate=False`/`uncalibrated_fit`
rather than a `lack_of_fit` rejection. Retain every cell in the likelihood and
report; a calibration refusal is not cell deletion.

### Replayed closures and judgment calls

| Contract | Independent disposition |
| --- | --- |
| Caller gate strings, fabricated `CalibratedExponent`, direct permission | Closed at the public derived-record boundary. Caller strings, direct construction, and `dataclasses.replace` refuse; `MachineryReport` is a separate non-physical type. The lower public-ledger construction above remains open. |
| Schema-v3 status | Closed fail-safe. Gate-only and all-four free-text rewrites both return `machinery_only`; schema 4 cannot be emitted by the v3 manifest parser. |
| Mixed/changed/partial sweeps | Reordered, duplicate, mixed-model, changed-disk and fewer-than-four-cell sweeps refuse. Same totals/different trial matrices produce different digests. |
| Four-trial resampling | Closed. The exact replay reports `0/50` estimable, an inadequate resampling record, and no valid exponent. |
| Replicate admission | The estimability-only choice remains sound. Separation, singularity, nonconvergence and unidentified curvature disqualify; marginal goodness flags are counted and reported, not treated as calibrated cluster decisions. Paired curvature remains authoritative. |
| Master identity | Closed within a design/contrast: namespace-plus-trial is injective, immutable under normal API use, and duplicate/substitution/reorder safe. The missing central experiment-family join is separate. |
| Singular curvature | Closed. The exact `1.000..1.010`, 200,000-trial fixture refuses for `curvature_unidentified` with infinite stderr; a nearby wide design is valid at exponent `1.99998`. |
| Flat response | An adequately informed constant response should remain a valid exponent near zero. `flat` correctly means singular information. |
| Ticket-04 README sentence | Closed. The live oracle wording is correct and the mechanical stale-prose guard passes without rejecting historical discussion. |
| Risk/survival/hazard | Closed. Independent nonuniform rows retained widths `(0.5,1.0,0.5)`, risk `(10,8,4)`, events `(2,3,1)`, censoring `(0,1,3)`, dimensionless failures `(0.2,.375,.25)`, rates `(.4,.375,.5)`, survival `(1,.8,.5,.375)` and cumulative hazard `(0,.2,.575,.825)`. |
| Comparators | Closed. Independent manifest arithmetic matched all four curves exactly (`max abs = 0`); continuum flux remains spacing-weighted and `finite_population=False`. |
| Holdout freezing | Rising/falling segmentation, common bin edges and winner mismatch are enforced. Reference-run and bin-count choice remain caller inputs explicitly deferred by the execution notes to tickets 07–08; schema v3 prevents that open scientific choice from supporting a physical/causal permission. They must be frozen before schema 4 is enabled. |

### Full regression matrix, isolation and cleanup

Environment: CPython 3.12.6, NumPy 2.3.5, macOS arm64.

| Command | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 114/114 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 114/114; peak RSS 654 MB under 944 MB; largest allocation 19.2 MB |
| `python3 adler_born_two_channel/verify.py` | exit 0, 114/114 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 114/114 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 114/115; only the deliberate probe failed |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| Fresh raw import | 11 expected raw/package modules; no observables, analysis, compare, prediction, oracle or audit module |
| Results cleanup | `adler_born_two_channel/results/` absent |

The API/readme census is current: 114 checks, 364 public callables, 997 invalid
calls and 827 parameters. Key prior residuals remain unchanged:
cloglog recovery `2.623e-10 <= 1e-6`, survival truth `1.144e-3 <= 1e-2`, and
comparator arithmetic `8.882e-16 <= 1e-12`.

Pre/post source hashes were identical:

| File | SHA-256 |
| --- | --- |
| `observables.py` | `762d6a8f4c2db7bafeae0378886ae196af74ac36d4a3380f5945433c7f29b40a` |
| `analysis.py` | `6cfbb565080244778bc4e80ca7c68f73dc01a1c657b2941b4f83c816aa6f68fa` |
| `compare.py` | `790b1f8c99ec123381f1b190597d349d82ff080f7ab2390304260c4971f28e6b` |
| `verify.py` | `b1aa61ac819813d040932ecee7f7b315dcab6eedec3301998ca3d7d0b6af6379` |
| `README.md` | `6152f02d106ea0e64441e708ffaac70a3475431106b4e5917e7858e72ac9920f` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

No implementation, verifier, README, ticket status, Git index or unrelated
file was edited. Every generated run was removed; only this existing review
artifact was appended.

Nothing here asserts Born's rule, a detector outcome, absorption, unique
actuality, a microscopic origin of the noise, a two-channel result or a
production-cleared exponent. The scientific boundary remains intact because
schema v3 fails closed. The strict software disposition remains **OPEN** until
the authoritative-read, causal-join and cluster-calibration defects above are
closed.

## Round-four closure re-review — 2026-08-28

### Verdict: OPEN

The three round-three fixes are substantive. All four physical decision
factories now discard a supplied handle's rows, reopen the named run through
the descriptor-scoped reader, compare its fingerprint and compute from the
fresh disk object. The causal decision joins the contrast's ordered
fingerprints and rejects the prior gate-twin, foreign-stream and foreign-
holdout substitutions. The nuisance-adjusted cluster score is algebraically
correct and its larger null ensembles are nominal.

Ticket 06 nevertheless remains open. A cold replay found three actionable
gaps around those fixes: one public analysis route still consumes a mutable
stale ledger, the new experiment-family digest omits the physical drive, and
the still-authoritative paired-curvature interval can be rerolled and can make
a positive curvature assertion in a regime the implementation itself says is
uncalibratable.

### P1 — a verified ledger snapshot is shallow-mutable, and the public design factory consumes it without reopening

The fix is correct on the four named decision paths. I rebuilt the exact
round-three split-brain state using the internal factory token so the result did
not depend on constructor sealing:

```text
disk counts                 ((2,6), (4,6), (5,6), (6,6))
in-memory forged counts     ((6,6), (6,6), (6,6), (6,6))
disk gates                  diagnostic_only x 4
in-memory forged gates      production_cleared x 4
scaling_verdict             disk digest, gates, status and fingerprints
control_evidence            disk digest and status
paired_exponent_contrast    disk digest and fingerprints
holdout_evidence            disk fingerprint
```

Changing one ledger byte after opening caused all four factories to raise on
the digest mismatch; restoring the exact byte restored the read. A public
`ReadOnlyRun(...)` construction also refuses. Those are genuine closures of the
split-brain decision bypass.

The lower snapshot is not immutable, however. `ClosedLedger` is a frozen
dataclass whose rows are tuples of ordinary dictionaries
(`raw_ledger.py:1108-1135`), and `rows()` returns those same dictionaries
(`raw_ledger.py:1175-1183`). `ReadOnlyRun` therefore freezes the reference, not
the parsed data. `design_from_sweep` is public and reads the supplied ledger
directly without reopening (`compare.py:761-783`). Exact all-public replay:

```python
sweep = RunSweep(tuple(open_for_comparison(name) for name in names))
disk_digest = design_from_sweep(sweep).digest
row = sweep.runs[0].ledger.rows("ledger")[0]
row["category"] = "committed"
stale = design_from_sweep(sweep)

stale.digest != disk_digest                    # True
design_from_sweep(sweep.reopen()).digest == disk_digest  # True
calibrate_exponent(stale, 20, 1).design_digest == stale.digest  # True
```

No file changed and no private name was used. The resulting calibration was a
no-result on the six-trial fixture, so this does not cross the physical gate;
schema v3 and the four decision-factory reopens still preserve the scientific
non-claim. It does violate the ticket's stronger contract that ledger-derived
analysis accepts only exact, hash-matching closed rows. The same mutable
`ClosedLedger` is accepted by the public observable functions.

**Minimal bounded fix:** make the parsed closed-ledger snapshot deeply
immutable (including row mappings and their sequence-valued cells) and make a
`ClosedLedger` constructible only by the authoritative byte gate, or move every
public ledger-derived analysis entry to a `ReadOnlyRun` locator that reopens.
At minimum, make public `design_from_sweep` reopen and use a private
already-fresh helper inside the four factories. Add the exact post-open row
mutation above and require both the public design and observable routes either
to refuse or to return the disk result.

### P1 — `experiment_family` omits `drive`, so a stationary central run joins a pulsed causal experiment

The new joins close the two exact round-three substitutions:

- a contrast over a gate-rewritten full-model twin has the same design digest
and different ordered fingerprints, and now raises;
- a central control under an unrelated stream hierarchy has a different
family and now raises;
- the genuine central control shares the full model's family while retaining
its intentionally different population-level CRN token;
- role swaps and a complete holdout computed from foreign fingerprints raise
before any schema-status decision.

The family itself is derived from `CRN_IDENTITY_FIELDS` minus population fields
(`compare.py:335-336`), rather than from the whole experiment manifest minus
the few declared control differences. `drive` is not a CRN field. I wrote a
genuine one-clock full-model sweep, changed only its manifest `drive` from
`pulsed` to `stationary`, re-emitted the manifest canonically, rebuilt each
close marker, and reopened every run through the real gate. The result was:

```text
full drive                         pulsed
central drive                      stationary
"drive" in EXPERIMENT_FAMILY_FIELDS   False
central family == full family      True
causal_decision                    accepted structurally; returned blocked
```

The final result was blocked only by the small-fixture invalid fits and
schema-v3 numerical statuses. There was no provenance refusal. A stationary
control is not the central pulsed control of this causal experiment, and this
becomes live as soon as cleared, adequately powered evidence exists.

**Minimal bounded fix:** derive the family from all manifest fields and remove
only explicit, reviewed legitimate differences: coupling/pulse digest, model,
fixed contraction rate and the central population fields. At an absolute
minimum include `drive`; the safer schema-level construction also includes the
schema/layout and all other physical/numerical fields instead of relying on a
CRN-purpose allowlist. Mutation-test every otherwise shared physical field,
with the genuine central population retained as the positive control.

### P1 — paired curvature is a rerollable percentile interval and makes a positive claim when calibration is known to be invalid

The round-four efficient-score correction is mathematically right. My
independent construction used

```text
W = diag(n_i H_i g(H_i))
B = C - X (X' W X)^-1 X' W C
e_t = s_t' B
```

and obtained:

```text
max |X' W B|                    2.84e-14
max |X' W C|                    67.11
independent statistic           0.31123647938363364
package statistic               0.31123647938363236
independent digest-seed p       0.986
package p                       0.986
independent-namespace statistic 3.8100093716477446
package statistic               3.810009371647738
```

Thus the weight, orientation, nuisance projection, cluster construction, meat
and digest-derived Rademacher signs are all correct. The exact saturated null
now has `adequate=False`, retains all six likelihood cells, and reports
`uncalibrated_fit`; a nondegenerate near-boundary null was adequate in 768/1000
datasets and rejected 39/768 = 5.08%, while all 232 exact-degenerate draws and
no others declined. The degeneracy guard is therefore not overbroad around its
boundary.

The curvature decision does not use that calibrated score machinery. It still
takes the percentile interval of bootstrap curvature estimates
(`analysis.py:1654-1656`) and emits `curvature` whenever that interval excludes
zero (`analysis.py:1902-1905`), even when the same design's calibrated test has
just said no inference is possible. On the review's exact null, seed 103002:

```text
counts                  (187, 337, 466, 500, 500, 500)
cluster lack of fit      inadequate; no rejection
calibrated reasons       ('curvature', 'uncalibrated_fit')
curvature interval       (0.01352, 0.40313)       # analysis seed 17
```

Holding that dataset fixed and changing only the public bootstrap `seed`
produced a curvature interval excluding zero for **58/100** seeds. Across the
120 exact-null saturated datasets, 20 carried the same extra `curvature`
reason. This cannot certify an exponent because `uncalibrated_fit` also blocks,
but it does misstate the evidence: the closed reason says the response is
curved when the implementation knows the boundary bootstrap is not calibrated.
It is also selectable post hoc because every authoritative factory accepts the
seed as an argument rather than deriving or reading it from frozen provenance.

The problem is milder but measurable away from the boundary. On 1,000 fresh
interior exact-power datasets with no degenerate cells, the frozen minimum of
100 bootstrap replicates excluded zero **67/1000 = 6.7%** (95% Wilson interval
5.31–8.42%) at a nominal 5%. On the same 300 datasets, 100 replicates rejected
22/300 = 7.33%, while 499 replicates rejected 13/300 = 4.33%. Thus the existing
minimum can call a curvature record adequate before its Monte Carlo resolution
is adequate for the authority assigned to it; the larger frozen count restores
ordinary null size.

**Minimal bounded fix:** do not emit `curvature` from a design whose curvature
calibration is inadequate; use a named `uncalibrated_curvature` no-result (or
fold it into `uncalibrated_fit`) and leave the percentile interval descriptive.
For authoritative curvature, either freeze at least the empirically adequate
499 draws and derive the seed from the design digest, or use the same bounded
one-dimensional efficient-score multiplier test with the quadratic column
residualized against `[1, log K]`. Physical/control decision factories must not
take a rerollable analysis seed or replicate count; those values must be frozen
by the design/manifest. Add seed-103002 across many analysis seeds, an interior
null-size ensemble, and a curved-power ensemble as discriminating checks.

The lack-of-fit verifier's current null acceptance band of **0.5% to 13% over**
**150 datasets** is also too wide to protect nominal size: 19/150 = 12.67% would
pass even though its one-sided probability under a 5% null is about
`1.9e-4`. The current method survives a much stronger check, so tighten the
guard rather than weakening the implementation: the fresh 2,000-dataset rates
below support a substantially narrower, binomially justified band.

### Independent calibration disposition

Fresh seeds, 2,000 null datasets per dependence setting, 400 trials per cell:

| Design | Rejections | Rate | 95% Wilson interval |
| --- | --- | --- | --- |
| independent namespaces | 107/2000 | 5.35% | 4.45–6.42% |
| master trials, Gaussian copula rho 0.0 | 101/2000 | 5.05% | 4.17–6.10% |
| master trials, Gaussian copula rho 0.4 | 107/2000 | 5.35% | 4.45–6.42% |
| master trials, Gaussian copula rho 0.8 | 103/2000 | 5.15% | 4.26–6.21% |

The earlier 8.7% independent-cell result was sampling variation, not a current
lack-of-fit defect. Fresh power was 391/400 = 97.75% for bend 0.5 and 200/200 =
100% for bend 1.2. The cluster test is both calibrated and discriminating after
the nuisance adjustment.

### Full regression, isolation and cleanup

| Command/probe | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 115/115; bounded-memory check passed |
| `python3 adler_born_two_channel/verify.py` | exit 0, 115/115 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 115/116; only the deliberate probe failed |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |
| `python3 -m py_compile` on the four Ticket-06 Python files | exit 0 |
| Fresh raw import | 11 raw/package modules; no observables, analysis, compare, analytic, oracle or audit |
| Independent no-write bracket | all 40 files of eight full/control runs retained identical SHA-256 digests |
| Results cleanup | zero entries under `adler_born_two_channel/results/` |

The API/readme census passes: 115 checks, 368 public callables, 1001 invalid
calls, 831 parameters and all 43 required README statements. Prior numerical
residuals remain within the same tolerances: survival truth
`1.143809e-3 <= 1e-2`, cloglog recovery `2.623121e-10 <= 1e-6`, comparator
arithmetic `8.881784e-16 <= 1e-12`. The stale Ticket-04 sentence remains fixed.

Final reviewed source hashes, unchanged across all probes:

| File | SHA-256 |
| --- | --- |
| `observables.py` | `762d6a8f4c2db7bafeae0378886ae196af74ac36d4a3380f5945433c7f29b40a` |
| `analysis.py` | `8c384e13d03f9b2910da72e9746b4096771ac8dcd642d5bd94a19cca3f105d8f` |
| `compare.py` | `e98834961c0473bb8fd01b00826d0a4e392328601970fdb3b9f1ab46333d8d93` |
| `verify.py` | `676b4a95f4222f2b8fb0b1744514dbd9ec59c5436dc12b00d881590da3058a56` |
| `README.md` | `32c89bbaa4b58c05e267df8ae5da379a096fac9ce287e1f7883882a6fac4e984` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

No implementation, verifier, README, ticket status, Git index or unrelated
file was edited. Only this existing review artifact was appended.

Nothing here is a Born-rule, detector-outcome, absorption, unique-actuality,
microscopic-noise, two-channel or production-cleared exponent claim. Schema v3
still makes a physical verdict unreachable and every real fixture remains
diagnostic-only. The strict software disposition is **OPEN** until the stale-
snapshot, experiment-family and paired-curvature fixes above are closed.

## Round-five closure re-review — 2026-08-28

### Verdict: OPEN

The three round-four implementation defects are closed on the paths their fixes
address. Public sweep design and all four decision factories reopen the run and
use fresh disk rows; all 45 manifest fields are covered by a subtractive
experiment family with only the intended role/sweep/population differences;
and lack of fit and curvature now share the correctly nuisance-adjusted cluster
score machinery with frozen, digest-derived calibration.

One actionable P1 remains. The new local ledger guard proves only that a
snapshot agrees with the marker carried by that same caller-constructible
snapshot. It does not run the authoritative gate's row-count, identity or
cross-table semantic reconciliation. A caller can therefore edit a parsed
ledger, recompute the public marker and construct a new `ClosedLedger`; all
three observables accept numbers which the authoritative gate rejects as
impossible. This is not a physical-verdict bypass—the decision paths reopen
disk and schema v3 remains closed—but it violates Ticket 06's rule that ledger-
derived analysis consumes only objects that passed the authoritative boundary.

### P1 — a caller-rehashed `ClosedLedger` certifies its own inconsistent rows

`ClosedLedger` is public and checks only outer types (`raw_ledger.py:1109-1137`).
Its tuples contain ordinary row dictionaries and `rows()` returns them directly
(`raw_ledger.py:1177-1185`). `require_unmutated_ledger` re-encodes the manifest
and tables and compares their digests with `ledger.marker`, but returns without
calling `require_closed_ledger` (`raw_ledger.py:1204-1255`). The latter is where
marker counts, row identities, ordering and cross-table semantics are actually
checked (`raw_ledger.py:1258-1386`).

I started from one genuine run, copied its ledger rows, changed trial 0 from
`dwell_failed` to `committed`, re-encoded all three tables with public
`encode_table`, rebuilt a public `CloseMarker` with those new digests, and
constructed a public `ClosedLedger`. No disk byte changed and no private seal
or comparison helper was used.

```text
require_unmutated_ledger(forged)          ACCEPT
commitment_counts(forged).committed      3       (disk: 2)
risk_table(forged).events                 3
winner_mismatch(forged).committed_trials 2
require_closed_ledger(same exact bytes)  REFUSE
  ledger trial 0 is recorded as 'committed'; its own 8 clock rows say
  'dwell_failed'
```

The three observable answers contradict one another: the tally and risk table
invent a third commitment while the winner table still has the two winners
supported by the clock rows. Three independent variants locate the missing
checks rather than merely repeating one category edge:

| Caller-built object | Local guard | Full authoritative gate |
| --- | --- | --- |
| marker declares 7 ledger rows beside the genuine 6 | accepts | refuses declared/present/manifest count mismatch |
| manifest detunings shifted by `+0.125`, rehashed beside unchanged clock rows | accepts; winner table reports the shifted grid | refuses manifest/clock detuning mismatch |
| ledger rows reversed and rehashed | accepts | refuses noncanonical identity order |

Direct mutations which leave the old marker are refused, as intended.
`encode_table(parse_table(writer_bytes))` reproduced all three writer files
byte-for-byte. Dictionary insertion order and list/tuple spellings with the
same values are intentionally canonical-equivalent; boolean-as-integer,
nonfinite float, separator-bearing string, and missing-key probes all refuse.
The serialization is therefore not the problem. The problem is that canonical
equivalence to a caller-supplied marker is weaker than the authoritative
gate's semantic consistency.

The existing verifier misses this exact distinction. Its post-open mutation
keeps the genuine marker, so a digest mismatch is sufficient to make the check
pass. Its exported-surface row gives `require_unmutated_ledger` only a wrong-
type negative. The README consequently overstates the live oracle when it says
the guard protects every ledger door: it protects against edits made without
reclosing, not against a publicly constructed and reclosed inconsistent
snapshot. The round-five execution note's claim that a hand-built ledger must
be self-consistent is disproved by the four variants above.

**Minimal bounded fix:** after constructing the canonical manifest/table bytes,
run those bytes through `require_closed_ledger`, and return the newly parsed
object from that full gate. Every observable and `_design_from_fresh_sweep`
must bind and consume that returned snapshot rather than continue with the
caller's original dictionaries. This both restores all semantic checks and
removes the check/use alias. Add the rehashed category, marker-count,
manifest-detuning and reordered-row probes to the verifier. Sealing
`ClosedLedger` is a useful anti-accident improvement, but is not a substitute
for consuming a freshly reconciled snapshot after an already-open object may
have been mutated.

### Round-four fix disposition

The ordinary public physical/causal route remains closed despite the local
observable defect:

- `design_from_sweep`, `scaling_verdict`, `control_evidence`,
`paired_exponent_contrast` and `holdout_evidence` reopen through the
descriptor-scoped reader, compare ordered fingerprints and compute from the
fresh object. A caller ledger cannot be placed into a public `ReadOnlyRun`,
and a changed disk file is refused. No self-consistent synthetic ledger or
exploratory `resample_exponent` record reaches a physical or causal door.
- The 45-field family audit is complete by construction: 34 included fields
and 11 reviewed exclusions. Thirty-nine legal one-field manifest changes
behaved as declared; the two schema versions, three table layouts and the
relationally coupled clock count cannot be independently changed in a valid
manifest. Genuine controls cover that coupled population change. A
stationary central sweep no longer joins the pulsed full sweep, while the
intended pulsed full/central/width-only trio does join.
- An independent score calculation reproduced both package statistics and
both digest-derived multiplier p-values to floating-point noise. For one
paired design, `max |X'WB| = 2.84e-14`; lack-of-fit statistic/p were
`11.819700439611026 / 0.020` independently and
`11.819700439611030 / 0.020` in-package. Curvature was
`6.128651366533369 / 0.014` independently and
`6.128651366533366 / 0.014` in-package. The kind-specific seed, fixed 499
signs, cluster meat and nuisance orientation all match.
- Seed 103002 retains all six likelihood cells with counts
`(187,337,466,500,500,500)` and reports exactly
`('uncalibrated_fit', 'uncalibrated_curvature')`. All 120 saturated nulls
declined both score tests; none made a positive curvature or lack-of-fit
claim. Near-boundary exact-null designs remained adequate whenever every
cell had variation, and an actual zero/all-event cell caused a refusal rather
than a certification.

Fresh seeds, 600 null datasets per design and 400 master trials per cell:

| Null design | Lack-of-fit | Curvature |
| --- | --- | --- |
| independent cells | 29/600 = 4.83% | 27/600 = 4.50% |
| paired copula rho 0.0 | 31/600 = 5.17% | 24/600 = 4.00% |
| paired copula rho 0.4 | 30/600 = 5.00% | 30/600 = 5.00% |
| paired copula rho 0.8 | 39/600 = 6.50% | 40/600 = 6.67% |

All counts lie inside the independently computed exact 0.001 two-sided
binomial region `[14,49]`. Fresh power was 191/200 = 95.5% for bend 0.5 and
200/200 for bend 1.2, for both tests. Across fresh 800-dataset paired null
ensembles, the union of the two predeclared refusal gates was 6.6–8.9%; that is
the expected conservative cost of two correlated diagnostics and cannot
certify evidence. The verifier's exact region for 150 is correctly `[1,18]`,
so 19 fails and 8 passes. Eight null guard comparisons give at most 0.8%
familywise flake risk at the declared 0.001 per-comparison level; the ensemble,
seed and method surfaces are fixed rather than caller-tunable.

### Full regression, isolation and cleanup

| Command/probe | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 115/115; bounded-memory criterion passed |
| `python3 adler_born_two_channel/verify.py` | exit 0, 115/115 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 115/116; only deliberate probe failed |
| `compileall -q` and `py_compile` on Ticket-06 modules | exit 0 |
| Fresh raw import | 11 package/raw modules; no observables, analysis, compare, analytic, oracle or audit |
| Independent no-write bracket | all 140 files of 28 full/control runs retained identical SHA-256 digests |
| Results cleanup | zero entries under `adler_born_two_channel/results/` |

README/API census is exact: 115 checks, 372 public callables, 1001 invalid
calls and 831 parameters. Prior residuals remain unchanged and inside their
tolerances: survival truth `1.14380941066561e-3 <= 1e-2`, cloglog recovery
`2.62312098768205e-10 <= 1e-6`, comparator arithmetic
`8.88178419700125e-16 <= 1e-12`. The Ticket-04 live wording correctly says the
moving-band audit is `numerical_no_result`/diagnostic-only and no production
budget exists.

Final reviewed source hashes, unchanged across all probes:

| File | SHA-256 |
| --- | --- |
| `raw_ledger.py` | `0ecab1b358861209f48594adf934e1125a53cadf4b35b0799cf485bd9b826be4` |
| `observables.py` | `ec03165c35c14716ec179b45854cc6b8a1e4f81a2ff4d7d4360fea222ab45dfc` |
| `analysis.py` | `0b3b57ff75f07510b1d0d29d611d0841ed3dc54613ece513e0b56fb1e6e1015b` |
| `compare.py` | `f974d837da3e0a91980d2936130414a410f2f30c359f8cf9d2e57576bdfc8423` |
| `verify.py` | `f5ed69c4bced0daa28c87ccf9c1f4aa1c11ef30f0d6f2cf04e115342c8c5dec8` |
| `README.md` | `9df0482edd5461368df5026c8ae3996ce27541eb6ea3daa421156b46db0ee2ef` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

No implementation, verifier, README, ticket status, Git index or unrelated
file was edited. Only this existing review artifact was appended.

Nothing here is a Born-rule, detector-outcome, absorption, unique-actuality,
microscopic-noise, two-channel or production-cleared exponent claim. Schema v3
still makes `physical_verdict_permitted` unreachable and every real fixture is
diagnostic-only. The strict Ticket-06 disposition remains **OPEN** until the
local guard passes its reconstructed bytes through the full semantic gate and
all ledger consumers use that fresh result.

## Round-six closure re-review — 2026-08-28

### Verdict: OPEN

The round-five ledger defect is closed at the authoritative gate. All four
requested rehashed forgeries now refuse, the gate returns a newly parsed
`ClosedLedger`, and the three public observables consume that returned object.
Adjacent identity, count, ordering, winner/co-completion, shadow-exposure and
manifest/row contradictions also refuse, while an independently rebuilt,
self-consistent snapshot round-trips and retains the genuine result.

Three actionable defects remain. Most importantly, the public sweep factories
accept subclasses of `RunSweep` and then dispatch to the caller's polymorphic
`reopen`. A seven-line public subclass therefore turns the authoritative disk
read back into an assertion. Two internal consumers also fail the round-six
contract that *every value* come from the reconciled object. Finally, an early
README section still documents the superseded Ticket-01 ledger interface as if
it were live.

### Closed — full semantic reconciliation of already-open ledgers

`require_unmutated_ledger` now requires an exact `ClosedLedger`, emits canonical
manifest and table bytes, and calls `require_closed_ledger` once
(`raw_ledger.py:1204-1261`). An independent syntax-tree walk found exactly one
call in the function and no route from `require_closed_ledger` or any of its
helpers back to `require_unmutated_ledger`. Runtime interception likewise
counted one call. The returned object is a distinct `ClosedLedger` with distinct
row dictionaries.

The four exact all-public, rehashed reproductions now refuse at the guard and
at `commitment_counts`, `risk_table` and `winner_mismatch`:

| Forgery | Current result |
| --- | --- |
| contradictory trial category beside unchanged clock rows | refuses on the trial/clock semantic contradiction |
| marker declaring seven ledger rows beside six rows and six manifest trials | refuses on the three-way count mismatch |
| manifest detunings shifted by `+0.125` beside unchanged clock detunings | refuses on manifest/clock disagreement |
| ledger identities in reverse order | refuses on noncanonical identity order |

Independent adjacent probes duplicated an identity, swapped the first two
clock rows, increased `co_completion` without another winner, and shortened a
shadow exposure. Each refused at the corresponding identity/order,
winner/co-completion or full-window rule. A self-consistent copy rebuilt from
the genuine rows was accepted; the returned snapshot was not the caller's
object and reproduced the same observables. Re-encoding each parsed table
reproduced the writer's bytes exactly. Schema versions remain 3, the manifest
still has 45 keys and the table layouts remain 17/19/17 columns.

Manifest-only reclosures of otherwise coherent data can still change a local
snapshot's free status or physical configuration fields. That is expected:
the digest is an integrity check, not authentication. Those snapshots cannot
enter `ReadOnlyRun`, and the safe exact-type holdout door reopens disk and
refuses a file changed after its handle was created.

### P1 — a public `RunSweep` subclass bypasses every sweep reopen

`design_from_sweep` (`compare.py:813`), `paired_exponent_contrast`
(`compare.py:1418-1422`), `control_evidence` (`compare.py:1594-1598`) and
`scaling_verdict` (`compare.py:2049` onward) use `require_instance`, then call
the argument's virtual `reopen()` method. `RunSweep` is public and unsealed.
The following uses only the public type and ordinary subclassing:

```python
class StaleSweep(compare.RunSweep):
    def reopen(self):
        return self

stale = StaleSweep(genuine_sweep.runs)
```

After constructing `stale`, I appended one byte to one contributing
`manifest.json` without changing its close marker. The genuine sweep refused
immediately with `manifest digest mismatch`. The same changed disk state gave:

```text
design_from_sweep(stale)                         ACCEPT ScalingDesign
scaling_verdict(stale)                           ACCEPT machinery_only
control_evidence("full", stale)                 ACCEPT ControlEvidence
paired_exponent_contrast(stale, stale_control)   ACCEPT ContrastReport
holdout_evidence(exact ReadOnlyRun arguments)    REFUSE manifest digest mismatch
```

The accepted local rows are internally valid, so the new
`require_unmutated_ledger` cannot detect that the named files changed; only the
skipped reopen could. This does not open the physical verdict under schema v3,
but it is an ordinary public route around the ticket's exact, fresh,
hash-matching-ledger boundary and can mint causal evidence records over stale
runs. The exploit required no underscore, forged seal or replacement of a
`ReadOnlyRun`.

**Minimal bounded fix:** require `type(sweep) is RunSweep` (or the package's
exact-type validator) at every public sweep boundary before dispatch:
`design_from_sweep`, `scaling_verdict`, `control_evidence`, both arguments of
`paired_exponent_contrast`, and public `sweep_master_trials`. Add the reproduction
above with a changed on-disk manifest and require all four factories to refuse.
`holdout_evidence` already demonstrates the appropriate exact-type pattern at
`compare.py:1711-1715`.

### P2 — two consumers still mix reconciled and caller-owned state

The round-six execution note says `_sweep_counts` already consumed the returned
ledger. It consumes only the numerator. At `compare.py:847-848`, the committed
rows come from `require_unmutated_ledger(run.ledger)` but the denominator is
`run.manifest.trials` from the original alias. With a runtime guard wrapper that
first obtained the genuine fresh ledger, then changed the caller manifest from
six to seven trials before returning the fresh object, the helper changed from

```text
((2, 6), (4, 6), (5, 6), (6, 6))
```

to

```text
((2, 7), (4, 7), (5, 7), (6, 7))
```

The numerator remained fresh; only the caller-owned denominator changed. This
helper is currently verifier-facing rather than a physical-decision route, but
it directly falsifies the claimed all-caller audit.

`_design_from_fresh_sweep` has the complementary gap. It calls
`sweep_master_trials(sweep)` before reconciling any run (`compare.py:825-832`),
so the identities and trial count come from the caller's original first
manifest while couplings and outcomes come from returned ledgers. Runtime
interception that replaced the caller manifest's stream hierarchy immediately
before the real guard returned a reconciled ledger produced a design carrying
the old master namespace beside cells from the new reconciled snapshot. Normal
public calls are protected by a genuine reopen once P1 is fixed, but this
private helper's own stated belt-and-braces guarantee is false and leaves a
check/use interval between identity construction and reconciliation.

**Minimal bounded fix:** reconcile all run ledgers first, then derive trial
count, CRN namespace, coupling and outcomes exclusively from that tuple of
returned objects; recheck the cross-run invariants over those objects. Rewrite
`_sweep_counts` as a loop that binds `reconciled` and takes both numerator and
denominator from it. Add returned-object substitution probes for the manifest,
not only for row dictionaries.

### P3 — the README's live ledger API remains stale

The README's present-tense section at `README.md:460-527` still says:

```python
require_closed_ledger(payload, marker, manifest) -> CloseMarker
```

It then describes one payload, four checks, a three-field manifest, and the row
parser as future work. The live function is
`require_closed_ledger(marker, manifest, ledger, clocks, shadow) -> ClosedLedger`;
it reconciles three tables under eight checks and a 45-field schema. Later
README material is current, so a reader encounters two incompatible live
oracles. The existing stale-prose check scans old schema-version and Ticket-04
sentences but does not recognize this stale API block, which is why the
115/115 README check still passes.

**Minimal bounded fix:** update the early block to the current signature,
three-table reconciliation and current manifest, or mark the entire passage
explicitly historical. Add a narrow mechanical guard for the retired signature
and the claims that there is only one payload, three manifest fields, or no row
parser.

### Regression, isolation, preservation and cleanup

| Command/probe | Outcome |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 115/115; bounded-memory criterion passed |
| `python3 adler_born_two_channel/verify.py` | exit 0, 115/115 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 115/116; only deliberate probe failed |
| `compileall -q` and `py_compile` on the Ticket-06 modules | exit 0 |
| Fresh raw import | 11 package/raw modules; none of observables, analysis, compare, analytic, oracle or audit |
| Independent no-write/restore bracket | all 40 files of the full and width sweeps returned to identical SHA-256 digests after every decision path and the deliberate changed-file probe |
| Results cleanup | zero entries under `adler_born_two_channel/results/` |

The README/API census agrees with the verifier: 115 checks, 372 public
callables, 1002 invalid calls and 831 parameters. The earlier live-oracle
sentence remains corrected. Prior numerical residuals are preserved:
survival truth `1.1438094106656083e-3 <= 1e-2`, cloglog recovery
`2.6231209876820486e-10 <= 1e-6`, comparator arithmetic
`8.881784197001252e-16 <= 1e-12`.

Final reviewed source hashes, identical before and after the probes:

| File | SHA-256 |
| --- | --- |
| `raw_ledger.py` | `91af4540abea7eccd4ab52b25d3e1d3dc7b4f805e283a89f24630d1596c26504` |
| `observables.py` | `38223e39a726b747680d6f16610bb90dae60fa75fd5e1e29f3dbf57ed087fe92` |
| `analysis.py` | `0b3b57ff75f07510b1d0d29d611d0841ed3dc54613ece513e0b56fb1e6e1015b` |
| `compare.py` | `1ebc3f81722f86cd892539f51cea42ecded29d0ed93036419a1ed78f240f06b2` |
| `verify.py` | `932368e9160201315685d3e6acaddb06825923850ed11efcc80e58725db36ae8` |
| `README.md` | `690d0fec7d3b234501f63cdb6bbda1e01a195998b5447eba8fdfd8df4f80ac7e` |
| `raw_runner.py` | `298dbad55551a6db80a3a0bec7d8b02a520351e86d8d8108047a55d072ddb9a5` |
| `__init__.py` | `b10c6baaa1a7479e101e6e8a178c54724fec3ec574e77f80fb2528798d9b420f` |

No implementation, verifier, README, ticket status, Git index or unrelated
file was edited. Only this existing review artifact was appended.

Nothing here is a Born-rule, detector-outcome, absorption, unique-actuality,
microscopic-noise, two-channel or production-cleared exponent claim. Schema v3
still makes `physical_verdict_permitted` unreachable and every genuine fixture
remains diagnostic-only. The strict Ticket-06 disposition remains **OPEN**
until the public sweep boundary is exact, all data are derived from returned
reconciled objects, and the live ledger documentation is corrected.

## Round-seven closure re-review — 2026-08-28

### Verdict: CLOSED

No actionable correctness issue remains in Ticket 06. The round-six P1, P2 and
P3 reproductions are closed on the current source, the previously closed
findings remain closed, and the complete verification matrix passes. Ticket 06
is ready to close.

### Exact public types and fresh authoritative reads

The sweep-facing public functions now enforce the documented exact types before
they consume data:

| Public door | Current boundary |
| --- | --- |
| `sweep_master_trials` | exact `RunSweep`, then package `RunSweep.reopen` |
| `design_from_sweep` | exact `RunSweep`, then package `RunSweep.reopen` |
| `scaling_verdict` | exact `RunSweep`, then package `RunSweep.reopen` |
| `control_evidence` | exact `RunSweep`, then package `RunSweep.reopen` |
| `paired_exponent_contrast` | exact `RunSweep` independently for both arguments, then package reads |
| `holdout_evidence` | exact `ReadOnlyRun` independently for all three arguments, then package `ReadOnlyRun.reopen` |

`_fresh_sweep` calls `require_exact_type` and dispatches the unbound
`RunSweep.reopen(sweep)`. `RunSweep.reopen` likewise dispatches the unbound
`ReadOnlyRun.reopen(run)` for each exact run. The review's public
`StaleSweep.reopen() -> self` subclass now raises `TypeError` at all five sweep
factories and at both positions of the paired contrast, with unchanged bytes and
with a contributing manifest changed after opening. The genuine sweep beside it
still detects the changed manifest digest. Exact `ClosedLedger` and
`LedgerFingerprint` boundaries at `ReadOnlyRun` also refuse the adjacent
subclass variants.

Thus a public handle is only a locator. Every analysis-producing door obtains
fresh ledger bytes through `open_for_comparison` / `open_raw_run`, compares the
fresh fingerprint to the locator's fingerprint and computes from the returned
package object. None dispatches an authoritative read through a method supplied
by the caller.

### One reconciled collection, including cross-run consistency

`_reconciled_ledgers` reconciles every run first through
`require_unmutated_ledger` and returns one ordered tuple of newly parsed
`ClosedLedger` objects. `_fresh_master_trials`, `_design_from_fresh_sweep` and
`_sweep_counts` derive every load-bearing value from that tuple:

- trial count and CRN namespace from the first reconciled manifest, after all
other manifests have been required to agree outside the two sweep-varying
fields;
- each coupling and each per-trial outcome from its reconciled ledger; and
- both the committed numerator and trial denominator from the same reconciled
object.

The prior returned-object interception was replayed: while the caller aliases
were changed from six to seven trials and assigned a foreign stream namespace,
counts stayed `((3,6),(5,6),(6,6),(6,6))`, the identities stayed under the
disk namespace, and the design digest stayed the disk's. No earlier/later or
reconciled/caller snapshot is mixed.

The constructor and returned-ledger consistency rules were compared directly.
Both require strictly increasing couplings, a single model, a single fixed
contraction rate, and equality of every manifest field outside
`SWEEP_VARYING_FIELDS = (peak_coupling, pulse_digest)`. Independent current-byte
probes confirmed the intended full, one-clock central and width-only sweeps are
accepted. Mixed sweeps differing in the clock population, drive, status fields
or model are rejected. The verifier additionally accepts only the diagonal of
the three declared roles, rejects all six role swaps, rejects mixed-population
holdouts, rejects a stationary central control in the pulsed experiment, and
audits all 45 manifest fields against the reviewed experiment-family exclusion
list.

### Live schema-v3 documentation

The README now presents the live interface first and unambiguously:

```python
require_closed_ledger(marker, manifest, ledger, clocks, shadow) -> ClosedLedger
```

It documents the five files, all three tables, the eight ordered checks, the
exact 45-key manifest and the separate
`require_unmutated_ledger(ledger) -> ClosedLedger` door. The retired one-payload,
four-check, three-field, future-parser account is explicitly identified as the
package's earliest historical revision rather than a live API.

The stale-prose guard recognizes the retired signature and present-tense claims
while admitting explicitly historical descriptions. Its positive and negative
fixtures both pass; the full README check reports 45 required statements and 45
pattern fixtures with no stale live-schema prose.

### Regression, preservation and cleanup

| Command or probe | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 115/115 |
| `python3 adler_born_two_channel/verify.py` | exit 0, 115/115 |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 115/115 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | expected exit 1, 115/116; only the deliberate probe failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |
| fresh `raw_runner` import | 11 package modules; none of analysis, observables, compare, analytic, oracle or audit |
| independent sweep/type probe | valid full, central and width accepted; population, drive, status and model inconsistencies rejected; all six subclass doors refused |
| fixture cleanup | zero entries under `adler_born_two_channel/results/` after every complete command and after the independent probe |

The verbose verifier reconfirms that the analysis layer is read-only and absent
from the raw import graph, that decision paths leave all five contributing run
files byte-identical, and that all long-lived fixtures are drained. The README
census agrees with the verifier: 115 checks, 372 public callables, 1008 invalid
calls and 831 parameters. Prior residuals remain unchanged: survival truth
`1.1438094106656083e-3`, cloglog recovery `2.6231209876820486e-10`, comparator
arithmetic `8.881784197001252e-16`, and cluster-test calibration `5.0e-2`
against `1e-1`. Peak resident set remained below the unchanged 900 MB bound.

The current source hashes are exactly the round-seven execution-note hashes:
`compare.py` `6bb4be40548b21bb5da9995f09c642c2c3b02dbaa49374f6165532c17ae7f544`,
`verify.py` `c942fb70a6b7ba79e96f9895288de9a337b3195a7c22976b1551836c8563fb3c`,
and `README.md` `82abbc4d4077b3280a0246daace9a35290673eba0beb84467cc8c5d5722067de`;
the six package files declared byte-identical to round six also match their
recorded hashes. No code, ticket status, Git index or unrelated file was
changed by this review.

All scientific boundaries remain intact. Schema v3 still makes
`physical_verdict_permitted` unreachable; every real fixture remains
diagnostic-only; and nothing in Ticket 06 claims Born's rule, detector outcome,
absorption, unique actuality, microscopic noise origin, a two-channel outcome
or a production-cleared exponent.
