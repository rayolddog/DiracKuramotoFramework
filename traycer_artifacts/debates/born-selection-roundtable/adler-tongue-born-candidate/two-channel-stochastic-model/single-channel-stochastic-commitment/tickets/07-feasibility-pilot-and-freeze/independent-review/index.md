---
title: "Independent review: Ticket 07 feasibility, pilot, and freeze"
kind: review
---

# Independent review: Ticket 07

## Strict verdict: OPEN

The implementation preserves Ticket 04's `numerical_no_result`, leaves the
proposal `checkpoint_blocked`, keeps Ticket 06 schema-v3 physical permission
unreachable, defines the intended six-node finite matrix, and passes its own
124-check suite. Those are necessary properties, but they are not sufficient
for checkpoint 1.

The benchmark is not measured at the proposed 64-clock/fine-timestep workload;
the power calculation sizes only an assumed marginal binomial curve and does
not validate the paired full/central/width Brownian controls; the pilot
firewall can read a pilot-labelled run outside its declared directory family
and leaves a public unrestricted raw-data reader alongside the count-only
door; and the public proposed-manifest type accepts scientifically false values
for almost all 59 fields. The resource ledger omits or misprices refinement,
shadow, pilot, validation, and arm-specific row costs. Finally, the evidence
supports only “no feasible matrix under the current evidence and provisional
design,” not the unqualified claim that no feasible timestep/sample/config
exists.

Checkpoint 1 therefore must not close on this package. No pilot should run and
no production state should be signed until the findings below are fixed and
independently re-reviewed.

## Findings

### P1 — The benchmark is the real writer, but not the intended workload

`experiments.run_benchmark` correctly calls Ticket 05's
`raw_runner.write_raw_run`, including its two passes, shadow replay, five-file
writer, and cleanup (`experiments.py:723-780`). The Ticket 07 fixture, however,
uses 16 clocks and timesteps `0.05` and `0.0125`, while the proposed matrix uses
64 clocks and timestep `0.001953125` (`verify.py:26330-26360` and
`26390-26406`). Only the six-trial base has one warmup; the two scaling
fixtures have none, and every fixture has one timed repeat. Thus the reported
roughly 2,000–2,300 nominal clock-steps/s is not a sound throughput measurement
at the proposed finest step/blocking, and a single repeat cannot establish
machine variation or a conservative slow-repeat rate.

The existing controlled 4x-trial and 4x-step fixtures do give useful
directional evidence against a materialized trial-by-clock-by-time cube: the
nominal cube grows fourfold while traced peak memory stays roughly flat. That
does not repair the throughput extrapolation, especially because the Python
branching and dwell/reset workload can vary with timestep and population.

As an independent spot check, I ran the real writer at exactly 64 clocks,
`timestep=0.001953125`, `clock_block=16`, and `step_window=64`, with one
discarded warmup and two timed repeats. This was a benchmark-only raw fixture,
not a range pilot, and its output was removed without analysis. The timed runs
were 58.344 s and 58.410 s for 131,072 nominal clock-steps, giving a
slow-repeat rate of **2,243.99 nominal clock-steps/s**. That corroborates the
reported throughput on this machine. Its one physical trial necessarily had
one shadow rewalk (100% rather than the proposed 5%), so it is a conservative
spot check rather than a production-shaped cost sample. Peak traced memory was
193,084 bytes against a 1,048,576-byte one-trial cube; combined with the
implementation's controlled flatness fixtures, this supports streaming/no-cube
behavior but not the missing complete cost ledger.

**Minimal bounded fix:** benchmark the real writer at 64 clocks,
`timestep=0.001953125`, and the proposed `clock_block=16` and
`step_window=64`, with at least one discarded warmup and multiple timed
repeats. Retain controlled trial/step scaling at representative fine settings,
record all repeats, use the slowest, and state exactly which execution costs
are and are not included. Do not call the result a total feasibility estimate
until the resource finding below is fixed.

### P1 — 145 independent and 290 paired trials are not justified for all three arms

For the assumed direct model

```text
q(K) = 1 - exp[-a K^2],  K in logspace(0.5, 2.0, 6),  q(midpoint)=0.5
```

an independent derivation reproduces the implementation's unit-sample Fisher
variance for the cloglog slope, `2.3531137397`. Therefore

```text
ceil(1.96^2 * 2.3531137397 / 0.25^2) = 145
```

is correct for six *independent binomial cells under that assumed curve*. The
declared 2x pairing inflation then mechanically gives 290, marginal half-width
`0.249681`, and equal-precision independent-arm contrast half-width `0.353102`.
Those calculations are internally consistent; they do not validate the design
that Ticket 07 proposes.

The recovery simulation generates nested uniform Bernoulli outcomes, not the
Ticket 05 Brownian race or either control. In 2,000 independent reproductions I
obtained:

```text
trials/cell   design           slope SD   95% half-width
150           independent      0.12710    0.24912
150           nested shared U  0.15281    0.29951
290           independent      0.09087    0.17810
290           nested shared U  0.10569    0.20714
```

The exact asymptotic nested-uniform variance inflation is about `1.455`, so 2x
is conservative for that synthetic generator. But actual Brownian outcomes
need not be monotone across coupling, and full-versus-control covariance need
not be positive. The statement that pairing “can only reduce” contrast
variance is false. No arm-specific expected probabilities or variances are
declared for the central and width-only controls; those arms can be less
informative than the full arm. Even the package recovery silently includes
invalid fits in its mean/SD summaries (197/200 paired and 182/200 independent
were valid in the reproduced run).

The 0.5–2.0 range and exponent 2 are pre-pilot assumptions, yet there is no
post-selection join that recomputes power from the count-only selected range.
Consequently 145/290 is a useful provisional planning calculation, not a
validated all-arm sample size. The value is not shown to be “tuned,” but it is
not justified for the claimed causal contrasts either.

**Minimal bounded fix:** size from a predeclared conservative probability
envelope for every arm and from the covariance range that the keyed Brownian
design can actually generate. Make pilot range selection feed a new blocked
power proposal without exposing forbidden outcomes. Simulate the real
full/central/width configurations through the frozen estimator, count only
valid fits, price failure probability, and show full-minus-control coverage
under adverse covariance. Until then label 290 provisional and do not assert
causal-contrast power.

### P1 — The pilot firewall is a narrow return, not an enforced data boundary

`PilotCellCounts` and `select_range` expose only coupling, trials, committed,
and the derived survivor count; the longest-consecutive-cell rule and its
tie-break are deterministic. The declared namespace and directory prefixes
are distinct, and `pilot_trials_eligible=False` is immutable. Those type-level
properties pass.

The physical firewall does not. `PilotFirewall.require_pilot_run` checks only
the manifest's `run_label` and `stream_namespace` (`experiments.py:2005-2037`).
It never checks the requested `run_name` against `pilot_prefix`. I wrote a
four-trial synthetic diagnostic fixture named `prod-t07-review-bypass`, with a
pilot label and pilot namespace. `pilot_counts` accepted it even though its
directory name was in the production family. The fixture was removed
immediately and was not a Ticket 07 pilot.

More fundamentally, public `raw_runner.open_raw_run` remains an unrestricted
alternate path. On the same fixture it exposed the full ledger, clock rows,
and shadow rows, including forbidden pilot information such as
`commit_time`, `dwell_resets`, `band_entries`, `eligible_time`,
`exposure_time`, `final_phase`, and co-completion data. A typed narrow return
does not prevent another supported import path from opening the same files.

The frozen contraction is also not provenance-bound. A caller can construct a
`RangeSelection` and can separately supply any positive
`fixed_contraction_rate`; the proposed manifest does not prove that the rate
equals `reference_rate(selection)` or that selection was derived from the
specific reconciled pilot ledgers. The manifest does not bind all pilot ledger
fingerprints, count digests, the range selection digest, or the selection-rule
digest.

**Minimal bounded fix:** require and validate the run name/prefix at the
count-only door; put pilot files behind a capability/API that does not export
the unrestricted ledger to pilot consumers; and add must-refuse tests for
directory-family substitution, output aliases, and direct reader access.
Construct the selection only from reconciled pilot fingerprints and bind its
rule/counts/ledger digests into the proposal. Derive the contraction rate
inside the manifest builder and verify equality. Pilot outputs must remain
permanently production-ineligible regardless of copied or renamed files.

### P1 — The 59-field manifest schema is closed by name but open by meaning

`PROPOSED_MANIFEST_KEYS` does contain exactly 59 keys, and the public type
refuses omissions, extras, duplicate keys, the Ticket 06 cleared numerical
gate, the wrong production-status schema, and `pilot_trials_eligible=True`.
The package factory currently emits `checkpoint_blocked`; the present object
is not signed and does not make schema-v3 physical permission reachable.

Almost all field values are otherwise unvalidated. I constructed all
non-special fields as the JSON-valid string `"wrong-but-json-valid"`; the
public `ProposedProductionManifest` accepted and hashed it. I also constructed
a manifest with status `checkpoint_one_approved`; it was accepted and hashed.
Thus the type does not enforce the documented environment, source, version,
grid, arms, controls, budgets, benchmark, matrix, evidence, or blocker joins.
A complete wrong record is more dangerous than an omitted field because it
looks frozen.

The proposal digest is also measurement-unstable because benchmark wall time
is in the frozen component. Re-running the exact source changes the putative
freeze digest. Public component constructors can be caller-forged too, so
exact Python type checks do not establish factory provenance.

**Minimal bounded fix:** follow Ticket 06's fail-closed pattern: reconstruct
and semantically validate every field from authoritative component records and
their digests, reject unknown status strings, bind the current source and
environment fingerprint, and verify every matrix/control/grid/budget join.
Separate a stable design digest from measured benchmark evidence. Keep the
only current status `checkpoint_blocked`; do not add approved, signed, or
`production_cleared` states in Ticket 07.

### P1 — `numerical_no_result` is real, but “no feasible matrix” is overbroad

The planned probability half-width at 290 trials is `0.0575465`; one quarter is
`0.0143866`. Ticket 04's authoritative stationary and moving-band evidence
reproduces these current worst probability bounds:

| Evidence | Unit | uncertainty-aware bound | allowance |
| --- | --- | --- | --- |
| stationary survival | probability | 0.0412454 | 0.0143866 |
| stationary exit quantile | time | 0.1528955 | 0.0219531 |
| moving survival at 0.80 | probability | 0.0328568 | 0.0143866 |
| moving commit-time p20 | time | 0.1770006 | 0.0219531 |

All are at non-intended configurations. The moving audit remains
`numerical_no_result`. Preserving it as blocking is correct and mandatory. On
the probability rows alone, the current worst bound gives at most 35 trials
under the one-quarter rule, while the provisional power model asks for 290.
That reproduces the advertised empty probability window.

It is not the whole feasibility problem. Both time bounds already exceed the
time allowance independently of trial count, so 35 is not an overall
admissible maximum; under the current evidence there is no admissible `n` at
all. `numerical_disposition` computes `admissible_trials` from non-time rows
only (`experiments.py:1544-1609`), making the scalar easy to misread. The
execution notes also describe six evidence rows, but `_t07_evidence` takes only
one envelope per unit from each report and therefore supplies four. The
omitted stationary exit-count and moving commit-probability rows do not change
the present worst bounds, but the authoritative evidence ledger and digest do
not match the claimed six-row ledger. Count/probability/time units must be
explicit and cannot be silently collapsed.

The claimed “8x finer timestep” escape is not established. Scaling the entire
stationary bound by `sqrt(dt)` incorrectly scales its sampling standard error.
Using the frozen stationary decomposition, at dt/8 the projected bias is about
`0.01009`, while the unchanged two-SE term is about `0.01272`; the sum remains
about `0.0228`, above `0.01439`. It would additionally require about 8.8x the
stationary sample under those optimistic assumptions. At dt/16 the analogous
sample factor is about 3.1x. For the moving time row, even if its point term
held fixed, the SE would have to fall from about `0.0829` to `0.00538`, roughly
238x the 40-cluster sample. These are lower-level planning estimates, not
evidence that refinement will work.

**Minimal bounded fix:** preserve the literal `numerical_no_result` and report
the present conclusion as “no feasible matrix under Ticket 04's current
non-intended evidence and this provisional power/configuration.” Separate bias
scaling from sampling error, carry every authoritative evidence row with its
unit, and make time-unit failure part of admissibility. Then present a costed
choice: (a) a narrowed claim that remains blocked but accurately delimits what
is known, or (b) new stationary/moving validation at intended configuration
with predeclared timestep and sample ladders. The implementation has not ruled
out all feasible `n`/timestep/configurations and should not claim it has.

### P2 — Matrix topology is finite, but execution identities and resource arithmetic are incomplete

The primary couplings are exactly six log-spaced nodes from 0.5 through 2.0.
The full/width grid has 64 midpoint clocks on `[-3,3]`, spacing `0.09375`, even
parity, no origin node, and 10 eligible clocks at the weakest coupling. The
declared timestep ladder is `0.001953125`, half, and quarter; stop/failure rules
and the finite-staircase fallback correctly refuse a hidden continuum. The
three arms are full, central, and width-only rather than a full factorial.

However, “2 of 6 cells, 1 of 3 arms” does not identify which cells or which
arm are refined. That choice can be made after data are opened. The central
control has a distinct one-clock grid containing zero, while the manifest has
only the 64-clock global grid fields. The matrix therefore does not fully
specify the exact execution graph or arm-specific grid.

The proposed `961,615,872` nominal clock-steps and roughly 173–197 hours price
the full 64-clock population for the anonymous refinement arm and multiply a
rate already measured with shadow replay by another `1.05`. That is neither an
exact physical-run count nor a clean work-equivalent model. With 290 trials,
the 18 primary cell/arm runs contain 5,220 physical trials. A separately
written 5% shadow sample is `ceil(0.05*290)=15` per run, hence 270 shadow
rewalks, not the aggregate `ceil(0.05*5220)=261` reported as “total trials.”
Two cells × one arm × two finer levels add 1,160 physical trial executions and,
if each run carries 15 shadows, another 60 shadow rewalks. Primary plus
refinement is therefore 6,380 physical executions and 330 shadow rewalks under
that interpretation. Shadow rewalks are validation work over existing master
trials, not new independent trials.

Assuming the refinement arm is a 64-clock arm, the exact durable-row count from
the Ticket 05 tables is about 320,530, not 313,635; fixed file overhead and the
slowest small-fixture bytes/row put storage nearer 49–53 MB. If the anonymous
refinement arm is central, both work and rows change substantially. None of
these totals includes the range pilot, intended-configuration Ticket 04
validation, additional sample ladders, or failed/refused repeats. The quoted
clock-step, wall-time, and storage totals are consequently not total costs.

**Minimal bounded fix:** freeze exact refinement coupling IDs and arm ID before
results; encode arm-specific grids; count physical trials, shadow rewalks,
passes, clock-steps, rows, fixed file overhead, and safety factors separately;
and include pilot plus required numerical validation as separate line items.
Avoid applying a shadow multiplier to a throughput whose benchmark already
contains that shadow fraction unless the units are normalized explicitly.

### P2 — Two frozen numerical/provenance fields are not authoritative

`NumericalBudget.coverage_sigma` is stored and hashed, but
`NumericalEvidence.bound` uses the module constant `COVERAGE_SIGMA` rather than
the budget value. Budgets with sigma 2 and sigma 9 produced different digests
but identical evidence rows and dispositions. The current value is 2, so the
numbers above happen to be correct; the promised freeze is ineffective.

The current proposal's evidence summary is derived by selecting a maximum
absolute observable per unit, not by preserving all authoritative Ticket 04
rows. It happens to retain the current worst bound, but a future row with
smaller absolute error and larger uncertainty bound could be dropped. This is
not a safe evidence-composition rule.

**Minimal bounded fix:** compute bounds from the budget object's frozen sigma,
carry all authoritative rows, and choose limiting evidence by the full
uncertainty-aware bound within an explicit unit—never by absolute point error
alone. Bind the exact Ticket 04 report/evidence digest into the proposal.

### P3 — Correct the stale validation strings now

`raw_runner.VALIDATION_NOTE` says the production numerical budget “does not
exist yet” (`raw_runner.py:236-251`), while Ticket 07 now implements a proposed
budget and concludes it is blocked. The canonical verifier banner likewise
says the pilot firewall, coupling sweep, and production numerical budget are
“NOT implemented” (`verify.py:28371-28375`). README passages repeat parts of
that stale stage description even though later passages describe Ticket 07.

**Judgment:** correct these strings now, despite changing future ledger hashes.
No durable pilot or production run exists to preserve, and pre-checkpoint is
the least disruptive moment to remove false provenance. The content change
should be explicit: record/bump the relevant source/content revision and update
any pinned diagnostic fixture hashes. Hash stability is not a reason to keep a
manifest statement known to be false.

## Checkpoint discipline and preserved properties

- No Ticket 07 pilot was run during this review. The only added raw fixture was
a four-trial synthetic firewall mutation; it was not analyzed and was
removed. A separate intended-resolution writer benchmark was run solely for
timing/memory and removed by its cleanup path. No exponent, curvature,
survival, dwell, noise, band, pulse, population, likelihood, or exclusion
pilot output was opened.
- No pilot or production result directory was present before review, and the
package-scoped result root was empty/absent after every probe and verifier
cleanup. No approved, signed, or `production_cleared` Ticket 07 artifact was
found.
- Ticket 08 remains status 0 and was not edited. Ticket 04's authoritative
`numerical_no_result` and Ticket 06's schema-v3 fail-closed status remain
unchanged.
- The raw source isolation, diagnostic-only gates, prior residual tolerances,
and explicit scientific non-claims continue to pass the package's tests.
- Before this review artifact was created, the Ticket 07 source fingerprints
were unchanged from the execution record. This review did not edit the
implementation, stage, commit, revert, or create production state.

## Independent verification matrix

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 124/124, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 124/124, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 124/124, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 124/124, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 124/125, exit 1; only the injected check failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite's fresh-interpreter raw-import isolation and no-write cleanup checks
passed in every full mode; `results/` was empty or absent after cleanup. Its
API census remained 442 public callables, 1,206 invalid calls, and 1,025
parameters, and all 118 Ticket criteria were represented. Earlier closed
residual/tolerance anchors remained within their frozen bounds, including the
survival truth error `1.1438094106656083e-3`, cloglog recovery error
`2.6231209876820486e-10`, comparator arithmetic `8.881784197001252e-16`, and
cluster calibration `0.05 <= 0.1`. The 45 README/API scientific nonclaims
passed mechanically, although the stage-status strings called out above are
semantically stale.

Final source hashes remained:

```text
raw_runner.py  0cf49763cb86478ccc7eb3e58d05a0ea79b770bd5d36c615a5f673352c5f7543
experiments.py 4338c1528f252b0e8729184fca51f2e223dd1ac0ce584ff97aaf3a329f1a22c2
verify.py      86061e1f4c7ba2db171cbfe1cf872657ab5ebdc2c1fd1d5e9ab38e81a4b6ebfc
README.md      27aa82c8075d66e25e95cdd9252e0a63498f3c1c5c7709be1e45f5e251126b56
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

Ticket 08's artifact hash remained
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

## Required closure conditions

Ticket 07 can return for strict closure only after all of the following are
demonstrated in a fresh independent review:

1. Intended-resolution, repeated real-writer benchmark evidence and a complete
execution/resource ledger.
2. Arm-aware paired power/coverage for the actual frozen Brownian designs,
including invalid-fit and adverse-covariance behavior.
3. A physical pilot capability boundary with no supported forbidden-data path,
exact prefix/provenance binding, and immutable count-only selection-to-rate
joins.
4. Semantic reconstruction/validation of all 59 manifest fields, with only a
blocked unsigned proposal state.
5. An evidence-complete, unit-correct numerical disposition that preserves
`numerical_no_result` and narrows the feasibility claim to what has actually
been ruled out.
6. Exact refinement identities, arm-specific grids, discrete costs, and stale
provenance strings corrected under a recorded content revision.

## Judgment for presentation to John

Do **not** present the current unqualified no-feasible conclusion as settled.
The robust statement is narrower and already decision-useful: the provisional
290-trial design is incompatible with Ticket 04's present non-intended
numerical evidence, and the moving-band `numerical_no_result` independently
blocks scientific interpretation. Present that statement together with the
costed alternatives above before asking for checkpoint approval. A claim that
no feasible timestep/sample/configuration exists requires a search or bound
that this implementation has not performed.

## Fix-up round 1 re-review — 2026-08-29

### Strict verdict: OPEN

Round 1 closes most of the arithmetic and topology findings. The current
package benchmarks the real Ticket 05 writer at the intended 64-clock finest
step, sizes the three arms separately, carries all 17 authoritative Ticket 04
rows without mixing their units, reports only
`no_feasible_matrix_among_searched`, fixes the exact refinement identities,
and keeps the proposal `checkpoint_blocked`. The 22-run matrix arithmetic and
the required failure discipline reproduce.

It is not ready for checkpoint presentation. The proposed manifest does not
actually freeze source or post-pilot design provenance and serializes a false
zero design digest; the public quarantine/count types permit an ordinary
unquarantined raw directory and caller-invented count provenance to reach the
post-range power join; Option A is neither a sufficient design under its own
projection nor a benchmark of the validation kernels it purports to cost; and
the durable storage estimate uses a non-conservative row coefficient. Several
stage statements also remain stale despite the new check claiming they were
corrected.

No pilot may run and no approval/signature/production-cleared state may be
created on this revision.

### Replay of every original finding

| Original finding | Round-1 adjudication |
| --- | --- |
| Intended-resolution writer benchmark missing | **Closed for protocol and throughput direction.** Five real-writer fixtures now use one warmup and two repeats, including 64 clocks at `dt=0.001953125`, block 16/window 64. Costing uses walked steps and does not double-charge shadow. |
| 145/290 was not arm-aware | **Arithmetic closed; scientific qualification remains open.** The new counts are 2,406 full, 6,346 central, and 2,406 width-only, but their envelopes and covariance factors remain declared assumptions checked only with a copula count generator. |
| Pilot firewall had a production-family/direct-reader bypass | **Partly fixed, still open.** Normal quarantine is outside `open_raw_run`, but public handles/counts are forgeable and `_read_quarantined` does not validate its directory under the quarantine root. |
| 59-field manifest was semantically open | **Replaced, still open.** The v2 object has 78 fields and useful type/cross-field checks, but same-kind false values and source/provenance edits still pass its design-freeze guard. |
| Numerical evidence ledger was incomplete and units were collapsed | **Closed for current disposition.** All 17 rows, the budget's own sigma, separate probability/time results, and bias-versus-SE projections reproduce. `numerical_no_result` remains literal and blocking. |
| “No feasible matrix” was overbroad | **Closed in the verdict vocabulary.** The claim is now only about 12 named options. The alternatives do not yet justify the checkpoint decision that accompanies that claim. |
| Refinement identities and resource arithmetic were incomplete | **Topology/arithmetic closed; cost conservatism and omitted visible costs remain open.** Exact arm grids, arm counts, two refinement cells, two levels, and five line items reproduce. |
| Frozen `coverage_sigma` and evidence selection were ineffective | **Closed.** The budget sigma propagates and limiting rows are selected by full uncertainty-aware bound within unit. |
| Stale provenance wording | **Correct for `VALIDATION_NOTE`, incomplete elsewhere.** Revision 2 is the right judgment, but the verifier banner, README, and an adjacent raw-runner comment still state the pre-Ticket-07 stage. |

## Findings

### P1 — The 78-field proposal does not freeze what it says it freezes

The key count is exactly 78, the proposal status vocabulary contains only
`checkpoint_blocked`, and omission, extra-key, wrong-kind, approved-status,
and several cross-field mutations are refused. Ticket 06's live manifest
schema remains 3 while physical permission remains at schema 4. Those are good
fail-closed properties.

Three independent reproductions fail the claimed freeze:

1. The factory writes `design_digest = "0" * 64`. The same object's computed
`design_digest` is
`f1aff5389599f7d136b922a5a0b4ffc4af7a05362e151ee19e25c517875f6aeb`.
Therefore the proposed serialized record contains a design digest that is
false on construction.
2. `DESIGN_DIGEST_KEYS` excludes `source_digest`, Python/NumPy/platform
provenance, `firewall_digest`, the count-rule thresholds behind it,
`fixed_contraction_rate`, `selection_digest`, and
`pilot_ledger_fingerprints`. Replacing the source digest with `ff...ff`
left the computed design digest unchanged, and
`require_unchanged_proposal(mutated, original_design_digest)` accepted it.
A different source or post-pilot selection can therefore pass the guard
intended to prove that the frozen design did not change.
3. The supposedly unexported seal is reachable as `experiments._SEAL` and is
used by the verifier itself. With it, same-kind false values were accepted:
a fake source digest, a fake serialized design digest,
`numerical_blockers=["looks_good"]`, and
`numerical_verdict="satisfied"` while blockers remained. The self-test
substitutes values of the wrong *kind* and checks seven selected
relationships; it does not establish semantic reconstruction of every
field.

The persisted statistics are incomplete too: `trials_per_cell=2406` is the
only explicit trial field although the central control runs 6,346. The opaque
`matrix_digest` changes, but a human-readable closed manifest does not
enumerate the arm-specific allocation it claims to freeze.

**Minimal bounded fix:** remove the serialized digest field from the proposal
body or populate and validate it as a computed adjacent value; include
source and every design-determining firewall/selection/rate field in the
design freeze; enumerate arm trial counts; validate blocker members and all
status/digest joins by value rather than only shape. A public Python sentinel
is not provenance. Reconstruct a persisted proposal from authoritative
components and independently revalidate it without access to a module-private
escape hatch.

### P1 — Quarantine blocks the normal reader, but the public provenance chain is forgeable

The normal path is improved. A genuinely quarantined run at
`results/pilot_quarantine/<name>` cannot be addressed by any accepted
`open_raw_run` spelling, the closure gate is rerun before counts are projected,
and the range rule itself is the frozen longest consecutive run with the
declared weak-side tie break. The pilot and production prefixes and streams
are distinct, and pilot trials remain production-ineligible.

The public boundary does not require that path. `QuarantinedPilotRun` is an
exported, caller-constructible dataclass, and `_read_quarantined` trusts its
`directory` verbatim. In a one-trial synthetic diagnostic reproduction—not a
pilot—I wrote an ordinary unquarantined run named
`pilot-t07-review-r1-handle`, constructed a `QuarantinedPilotRun` pointing to
that ordinary directory, and passed it to `pilot_counts`. It was accepted and
returned `(coupling=1.0, trials=1, committed=0, survivors=1)` while
`raw_runner.open_raw_run` simultaneously exposed its full 1 ledger, 2 clock,
and 2 shadow rows. The run was removed immediately.

`PilotCellCounts` and `RangeSelection` are also public constructors. Six
invented count records with invented 64-character digests selected `[0.5, 2.0]`, and `post_range_power` returned `post_range_join`, `powered`, with
2,401/6,334/2,401 arm trials. No quarantined ledger existed. All three
provenance types accept arbitrary 64-character non-hex strings. The public
count object also exposes `ledger_digest` and `digest` in addition to the
strictly permitted coupling/trials/committed/survivors surface.

Finally, the carried `ledger_digest` is `marker.digest("ledger")`: it binds
the ledger table, not the close marker or the complete five-file closure. The
clock and shadow tables that the closure gate checked are not durably bound to
the later selection.

**Minimal bounded fix:** make the count door resolve and require exactly
`_quarantine_root() / run_name`; do not accept a caller-supplied directory;
bind the complete close marker or all five role digests; and make
`post_range_power` consume an authenticated projection produced by that door,
not publicly constructible count records. Keep provenance opaque/internal so
the public result exposes exactly the four permitted values. Add the exact
unquarantined-handle, non-hex, caller-fabricated-count, changed-clock/shadow,
and simultaneous-reader reproductions as must-refuse tests.

### P1 — Option A is a planning proxy, not a sufficient blocker-resolution design

The full-arm probability allowance at 2,406 trials is
`0.0049947101724`. The limiting stationary survival row has measured bias
`0.0285290281266` and SE `0.0063581774351`. Under the package's own
`sqrt(dt)` projection, `dt/8` leaves bias `0.010086`—more than twice the
allowance before any SE term. No sample enlargement can make that row fit at
`dt/8` under this projection. The moving audit in Option A is enlarged 256x
at unchanged timestep; its nonzero probability point shifts `0.0083333` and
`0.0145833` each exceed the full-arm allowance before SE. Thus the offered
configuration is not shown capable of resolving the numerical block.

The cost is not a measurement of the proposed validation either.
`_t07_alternatives` charges generic Ticket 05 two-pass raw-writer work for a
“stationary killed-diffusion oracle ladder” and a “moving-band audit.” Those
algorithms have different work and storage shapes. The reported approximately
3,766 h / 163 MB (3,620 h / 162.8 MB in my fresh benchmark process) is a
raw-writer-equivalent proxy, not a cost of running either Ticket 04 authority.

The finite search itself is honest: all 12 named rows fail and the closest is
1.326466x over its allowance. It does not prove there is no planning point
outside that set. For example, under the same optimistic transferred-evidence
projection, `dt/64` plus at least 79.24x the validation sample makes every row
fit the *full-arm* scalar allowances. That is not evidence and does not lift
`numerical_no_result`; it merely demonstrates an unsearched planning region.
Accounting for the central arm's 6,346 trials makes the probability allowance
stricter (`0.00307545`): among power-of-two projections, `dt/256` with about
97x the sample is the first reasonably balanced point, still transferred,
unmeasured, and not a physical validation design.

The present disposition remains correctly blocking regardless: every row is
non-intended, the moving report is literally `numerical_no_result`, and the
time bounds fail for every `n`.

**Minimal bounded fix:** label Option A as an exploratory planning proxy, or
replace it with a predeclared ladder that is sufficient under the stated
projection and benchmark the actual stationary/moving validation kernels.
State which arm's statistical width sets each numerical allowance and include
control-specific numerical validation or justify why it is not required.
Failure must remain `numerical_no_result`.

### P2 — The power arithmetic is correct only conditional on unvalidated envelopes

The six-node lever arm is `1.34526843897`. Independent recomputation gives:

| Arm | Worst declared weight | Independent count before inflations | After 2.0 pairing, invalid-fit, and 1.25 factor | Final allocation |
| --- | --- | --- | --- | --- |
| full | 0.0999075443 | 457.31 → 458 | 1,203.44 → 1,204 | 2,406, tied to width |
| central | 0.0199993198 | 2,284.50 → 2,285 | 6,345.85 → 6,346 | 6,346 |
| width | 0.0499890389 | 913.97 → 914 | 2,405.19 → 2,406 | 2,406 |

This reproduces analytic 458, achieved exponent half-width 0.217908,
contrast half-width 0.344543 at covariance floor -0.25, and the primary totals
66,948 physical plus 3,360 shadow. Zero/all-event cells are retained by the
fit and post-range join.

The recovery replay also reproduces 149/150 paired, 142/150 independent, and
149/150 contrast-valid fits; exponent variance inflation 1.29123 against the
declared 2.0; and contrast inflation 0.69862 against 1.25. It is not a
simulation of any of the three race arms. It is a Gaussian-copula binomial
generator. With per-cell correlation 0.85, the requested between-arm latent
correlation -0.25 becomes `0.85^2 * -0.25 = -0.180625` in the generated
variables, so the ensemble does not exercise the declared adverse floor.

The probability envelopes, 5%/10% invalid-fit prices, 2.0 pairing inflation,
and 1.25 factor are frozen source constants and are not silently estimated
from pilot exponent output. They are also not empirically supported by the
real full/central/width configurations. The pilot checks only the full arm's
event/survivor counts; it cannot validate the two control envelopes. An actual
cell outside an envelope, including zero/all expectation, voids the power
bound.

**Minimal bounded fix:** retain the frozen assumptions but call the result
“provisionally sized under declared envelopes and covariance bounds,” not an
unqualified `powered` result. Either provide a conservative argument for the
envelopes/factors or cost a pre-checkpoint real-arm calibration that does not
inspect forbidden exponent output.

### P2 — Matrix arithmetic is exact, but storage and visible checkpoint costs are not conservative

The matrix itself reproduces exactly:

- couplings `(0.5, 0.6597539554, 0.8705505633, 1.1486983550, 1.5157165665, 2.0)`;
- 64-clock midpoint grid on `[-3,3]`, spacing `0.09375`, even parity, no
origin clock, and 10 eligible clocks at `Kmin` against minimum 8;
- full/central/width grids 64/1/64 and trials 2,406/6,346/2,406;
- timestep ladder `dt`, `dt/2`, `dt/4`, refining only couplings 0.659754 and
1.148698 on the full arm at 200 trials;
- five cost lines, 22 run identities, 67,748 physical executions, 3,400
shadow rewalks, 2,102,228 rows, and 8,563,679,232 walked clock-steps.

There is no shadow double pricing, hidden continuum, or full factorial. Stop,
failure, and finite-staircase fallback rules are frozen. The recorded 844 h is
reproducible from that run's slow rate and 1.5 safety factor; fresh independent
processes produced 811–911 h from the same work count, showing the intended
machine-dependent variation rather than an arithmetic disagreement. A
full-duration one-trial spot check at the intended 64-clock/fine-step shape
ran 58.344 and 58.410 s, with 2,243.99 nominal or 6,731.98 walked steps/s,
peak 193,084 bytes, and 5.43x margin to its one-trial cube. The shorter five-row
suite remains the conservative timing fixture and each full invocation took
about 4.5 minutes.

Storage is not conservative. `matrix_resource_estimate` uses the slowest
*timing* fixture's 91.1628 bytes/row rather than the suite maximum 106.2203.
Applying only that measured maximum to the same rows and fixed overhead raises
192 MB to at least **223.47 MB**, before allowing for wider production trial
IDs than the small serialization fixtures. The handoff summary reports the
maximum coefficient while the resource object uses the smaller one.

The range pilot is calculated but not exposed in the handoff total or either
alternative: on the fresh slow rate it is about 45.7 h, 109,120 rows, and 10
MB. Keeping it outside the 22 production runs is correct; omitting its number
from the checkpoint decision is not. Option B says “the same matrix” but costs
only the 18 primary runs at 35 trials and excludes all four refinement runs,
the pilot, and numerical validation. Its fresh 10.8 h / 2.81 MB arithmetic is
correct for that smaller primary-only diagnostic.

**Minimal bounded fix:** use the maximum measured row coefficient or a
production-shaped serialization bound, carry the maximum measured peak, and
show the pilot as a separate visible line. Rename Option B “18-run primary
diagnostic sweep” and enumerate the excluded refinements, pilot, and validation.

### P2 — Revision 2 was the right provenance judgment, but the stale-string check is incomplete

`raw_runner.VALIDATION_NOTE` itself is now correct at revision 2: it says the
budget exists, is not met, and remains `numerical_no_result`; the Ticket 06
gate phrases survive; ledger/manifest schema v3 and 45 keys are unchanged.
Changing future ledger hashes was the right choice. A known-false durable note
must not be retained for hash continuity, especially before any pilot or
production run exists.

The implementation did not finish the stated cleanup:

- `README.md:60`, `README.md:106-107`, and `README.md:2980-2981` still say a
production numerical budget does not exist;
- `verify.py:29218-29220` still prints that the pilot firewall and production
numerical budget are “NOT implemented”;
- `raw_runner.py:234-237` still comments that no production budget exists yet.

`check_stale_stage_strings` searches one exact combined banner phrase that is
not the banner actually printed and checks only one README stage-table row, so
all of these pass unnoticed. Correct the remaining statements now and make the
test assert the current affirmative/blocking language rather than a few exact
obsolete spellings.

## Numerical disposition and checkpoint judgment

The evidence recomputation is correct: 17 rows, probability allowance
`0.00499471017`, time allowance `0.021953125`, worst probability bound
`0.0412453830`, worst time bound `0.1770005561`, probability `nmax=35`, time
inadmissible, overall admissible trials 0, and all six named blockers. No row or
unit was silently combined. The current 2,406/6,346 statistical allocation is
even more incompatible than the superseded 290-trial design. Positive
`feasible_matrix` and `unresolved` controls pass, and the production verdict
remains only `no_feasible_matrix_among_searched`.

That narrow conclusion is robust enough to tell John. The current package is
not robust enough to ask John for a checkpoint choice because the offered
costs do not mean what their prose claims.

Use these descriptions after the bounded fixes:

- **Option A:** “Exploratory intended-configuration validation planning proxy.
The quoted cost is raw-writer-equivalent and the present dt/8 + 256x design
is not shown sufficient under the projection; actual validation-kernel
benchmarks and a sufficient frozen ladder are prerequisites. Either outcome
remains non-physical, and failure remains `numerical_no_result`.”
- **Option B:** “Approximately 11 h / 3 MB for an 18-run, 35-trial primary-only
machinery diagnostic. It excludes four refinements, the range pilot, and
numerical validation; it cannot lift the time-unit or moving-band block and
cannot support a scaling or causal claim.”

## Independent verification and discipline

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 126/126, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 126/126, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 126/127, exit 1; only injected failure |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite preserved 496 public callables, 1,297 invalid calls, 1,117
parameters, 120 acceptance criteria, raw-import isolation, warning cleanliness,
the 900 MB RSS cap, prior residual/tolerance anchors, and 45 scientific
nonclaims. `results/` was empty after the full matrix and after the synthetic
firewall reproduction.

No Ticket 07 pilot ran. No pilot physical fit or exponent/curvature/survival/
dwell/noise/band/pulse/population/likelihood/exclusion output was opened. No
approval, signature, production-cleared state, stage, commit, or revert was
created. Ticket 08 remains status 0 with unchanged hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

Final package hashes remained exactly the round-1 execution hashes:

```text
experiments.py 994896aa1f44c093cdc2a2d44e3ac02d9e438492f4a7781cf8cf134d8aba637c
verify.py      efa40b56c575d78fcd3dc8ff4df71f96649df25f9280bc8a4afc3a11a6859f42
raw_runner.py  cbb6085c610600afd4875fed2ef8531bdc3e8758b307190feca2147ec98a739b
README.md      1594e4abfccc47edc19b61f4fea8a748aa8a3aaf305afcb100bae9fe7b349515
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

## Fix-up round 2 independent re-review — 2026-08-29

### Strict verdict: OPEN

The factory-produced proposal still says `checkpoint_blocked`, the live
schema still cannot express production clearance, and the narrow conclusion
`no_feasible_matrix_among_searched` is correct. The package is nevertheless
not ready to present as a checkpoint choice. Four independent defects remain:

1. the proposed-manifest record can be rehashed into a same-typed,
semantically false record through the module's own reachable seal;
2. the count projection can be forged or edited through that same seal, and
its public record has a fifth visible provenance field;
3. Option A times only the moving audit's comparison of already-generated
observations, not the replay that generates them, and also omits the
stationary sampling/comparison work; and
4. the claimed schema-derived storage bound is not a bound.

The implementation's 126/126 verifier passes because it does not exercise
these exact same-type/private-token, pre-timing dataset-generation, or widest
finite-value reproductions.

### Round-1 replay: what is now closed

| Area | Independent round-2 result |
| --- | --- |
| Ticket 05 benchmark | Closed. Five real `raw_runner.write_raw_run` fixtures, one discarded warmup and two timed repeats each. The current intended 64-clock, `dt=0.001953125`, 256-step fixture ran at 4,014 walked clock-steps/s over 12.245/12.229 s repeats; family rate span 1.30, shadow incremental rate 3,760/s versus base 4,533/s, peak growth 1.07x/1.13x under the two 4x work probes, and projected cube margin 201,291x. The previous full-duration independent spot check remains 58.344/58.410 s at the unchanged writer mechanism. |
| Power | Closed conditionally on the declared envelopes. Lever arm 1.34526843897; analytic full-arm count 458; final full/central/width counts 2,406/6,346/2,406; achieved exponent half-width 0.217908 and adverse-floor contrast half-width 0.344543. The current recovery replay again gives paired inflation 1.291 and contrast inflation 0.699. The measured copula correlation -0.180625 remains explicitly distinct from the frozen floor -0.25. This is provisional sizing under frozen assumptions, not empirical validation of the three race arms. |
| Numerical disposition | Closed. All 17 authoritative rows are propagated with `coverage_sigma`; probability allowance 0.00499471, limiting bound 0.0412454 and `nmax=35`; limiting time bound 0.177001 against allowance 0.0219531 and inadmissible at every trial count. All six blockers remain, including the literal moving-band `numerical_no_result`. Bias and SE respond to different projection levers. |
| Finite search | Closed. All 12 declared options fail; the closest is the dt/16, 1024x-sample, 35-trial option at 1.326x its allowance. Positive feasible and unresolved controls discriminate. The verdict is only among the searched options. |
| Matrix | Closed apart from storage pricing. Exactly six nodes, 64-clock midpoint support `[-3,3]`, spacing 0.09375, even parity and no origin clock; 10 eligible clocks at `Kmin`; three finite arm grids; two refinement couplings on the full arm only; five cost lines and 22 identities; 67,748 physical executions, 3,400 shadow rewalks, 2,102,228 durable rows and 8,563,679,232 walked clock-steps. No shadow double price, continuum substitution, or full factorial. |
| Revision 2 and Ticket 06 | Closed. Correcting `VALIDATION_NOTE` despite changing future ledger hashes remains the right judgment. The false statement should not survive merely to preserve hashes before a pilot or production ledger exists. Schema v3, 45 manifest fields, required Ticket 06 gate phrases and fail-closed permission remain intact. |
| Discipline | Closed. No authorized pilot or campaign ran, no exponent-related pilot output was opened, no approval/signature/production-cleared state exists, results clean up, and Ticket 08 remains status 0 at hash `6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`. |

### P1 — The serialized proposal is self-consistent, not authoritative

The 75/80 design-key split is now exact. Source and environment, firewall,
selection, rate rule, numerical budget/evidence/search, power, matrix,
arm-specific trials and measured correlation are in the design digest;
`design_digest`, the two free-text fields, and wall-time-bearing benchmark and
resource digests are the five exclusions. The factory-produced record carries
the real serialized design digest
`83530512b0a863756321cc7237deb268464f300e412c956d51aa88b68715b5dc`,
uses lowercase hex, and remains structurally unable to say approved, signed or
production-cleared.

That establishes the factory path, not a persisted record's authority. The
seal is a reachable module value at `experiments.py:4201`; the constructor
accepts it at `experiments.py:4407-4414`; and `__post_init__` checks a record's
digest against the same record's fields at `experiments.py:4517-4564`. It does
not rejoin those fields to the authoritative power, disposition, search,
matrix or recovery objects. `require_unchanged_proposal` detects a change only
when a separately trusted old digest is already supplied.

Using a valid factory record as the control, I changed same-typed fields,
recomputed the declared design digest exactly as the class does, and supplied
the module's own `_SEAL`. All three false records were accepted:

| Reproduction | Accepted value |
| --- | --- |
| `numerical_verdict="satisfied"`, `numerical_blockers=[]`, `search_verdict="feasible_matrix"` while the evidence/search digests stayed blocked | digest `b9755653...` |
| arm trials changed from 2,406/6,346/2,406 to 7/8/7 while the matrix and power digests stayed unchanged | digest `15ba13a8...` |
| measured arm correlation changed from -0.180625 to 0.9 while the recovery-derived source stayed unchanged | digest `740c1101...` |

Wrong-type, omission, extra-field, ordinary `dataclasses.replace`, and
seal-less probes do refuse. They do not cover a semantically false same-type
record rehashed with the reachable token. A self-digest proves internal byte
consistency, not provenance.

**Minimal bounded fix:** add an authoritative load/checkpoint validator that
takes the component records, reconstructs the factory proposal, and requires
exact field-for-field equality before accepting a serialized record. Move the
seal into closure state rather than a module attribute, and add the three
same-type/rehashed/private-token reproductions above. A reviewer may freeze a
design digest only after this component join, not from the record's own digest
alone.

### P1 — The count-only quarantine path is sound, but its provenance is forgeable

The filesystem door itself is repaired. Resolution is name-only beneath the
quarantine root; directory and file descriptors use `O_NOFOLLOW`; every file
must be regular; the full five-file gate is rerun; the closure digest binds the
marker schema, all three `(table, rows, digest)` triples and manifest; and no
accepted `open_raw_run` spelling reaches a quarantined run. Ordinary direct
filesystem access is accurately described as outside this anti-accident
boundary.

The object boundary does not deliver the claimed unforgeability. `_Projection`
stores its readable `_closure` and accepts the shared module `_SEAL`
(`experiments.py:3749-3789`). `PilotCellCounts` visibly declares
`projection` as its fourth dataclass storage field in addition to coupling,
trials and committed, with survivors as a property
(`experiments.py:3950-3989`). Its visible scientific/provenance surface is
therefore five values, not exactly coupling/trials/committed/survivors.

Exact reproductions:

- six `_Projection(fake_hex, experiments._SEAL)` tokens and six invented
`PilotCellCounts` selected `[0.5, 1.7]` over all six cells;
- `post_range_power` accepted that forged selection/count join and returned
`post_range_join`, `powered`, with 3,188/8,411/3,188 arm trials; and
- `dataclasses.replace` changed coupling/trials/committed while retaining the
old projection token, and `select_range` accepted the edited counts and
produced a new internally consistent counts digest.

`select_range` and `post_range_power` recompute hashes, but the hashes are over
the forged values and forged tokens (`experiments.py:4098-4132` and
`experiments.py:1728-1762`). They are consistency joins, not authoritative
joins to quarantine bytes.

**Minimal bounded fix:** make the authoritative selection and post-range power
paths take quarantined run handles/names and re-open/project them internally at
the point of use. Return a separate public four-value count view that carries
no token field. If an opaque internal bundle is retained, its minting secret
must be closure-scoped and the bundle must authenticate its count values so
`replace` cannot reuse provenance. Add private-token, copy/replace, six-cell
selection and full post-range-power forgeries as must-refuse tests.

### P1 — Option A measures comparison work after the observations already exist

The stationary oracle timing independently reproduces the implementation:
one warmup, repeats 0.035796/0.035172 s for 360,000 oracle cells, conservative
rate 10,057,060 cells/s, peak 17,278,812 bytes. This is genuinely
`killed_diffusion.solve_survival`.

The moving timing is not a moving replay timing. `_t07_kernel_benchmarks`
calls `_audit_dataset()` before it enters `benchmark_kernel`
(`verify.py:27024-27033`). `_audit_dataset()` obtains `_audit_ladder()`, whose
actual observation generation walks every trial/clock/stride through
`moving_band_audit.replay_pulse` and its paired leaves
(`verify.py:17804-17868`, especially 17845-17851). The timed callable then
does only `killed_diffusion.compare_refinement` over that already-built frozen
dataset. Brownian-tree leaves, primary/audited dwell evolution, bridge draws,
and construction of cluster observations are outside both timed repeats.

The seven stage operation counts consequently do not describe executable
campaign work. They are computed as `base * spatial * sample / timestep`
(`verify.py:27083-27094`). For moving stages this produces 589,824,000,
36,864,000 and 150,994,944,000 *bootstrap resample-observations*. The 64x and
1024x sampling stages put the same factor into both `sample` and the field
labelled spatial, squaring trial enlargement, while the dt/16 stage multiplies
bootstrap comparisons by 16 although the actual missing work is replaying 16
times as many intervals. Overpricing one comparison term does not bound an
unmeasured replay term.

The stationary stages similarly price only PDE space-time cells. They do not
price generation of endpoint Monte Carlo observations or the comparison that
separates measured bias from sampling SE. Their claimed 2x/4x/8x spatial
refinements are entered as factors 4/16/64 even though the declared operation
unit is one space-time cell. The success/no-result vocabulary, dependencies,
unit-specific allowances and caps are frozen, and no stage promises
sufficiency; the operation ledger underneath them is not coherent.

Therefore neither approximately 42 h nor the 3,120 h cap sum is a bound on the
proposed campaign. The cap sum caps only the two recorded kernels and has no
allowance for the omitted sampling/replay kernels. Option A remains a planning
sketch, not a costed blocker-resolution alternative.

**Minimal bounded fix:** benchmark and cost separate real kernels for (a)
stationary oracle solves, (b) stationary endpoint observation generation,
(c) moving `replay_pulse`/paired-leaf observation generation, and (d) the
paired bootstrap comparison. Give each stage an explicit bundle of those
operations, with master-trial, clock, replicate, interval and refinement
counts derived once from its intended configuration. Then rerun the warmed
size sweep, sum the components, and rebuild the range/caps. Preserve
`numerical_no_result` and `sufficiency="not_promised"`.

### P2 — The 329.34 B/row value is not a schema-derived worst-case bound

`row_width_bound` calls the real encoder, but its chosen values are not widest:
`_WIDTH_TIME=1234.5678901234567` serializes in 18 characters and
`_WIDTH_FLOAT=-1.2345678901234567e-16` in 23
(`experiments.py:3217-3220`, 3516-3571). The same schema and encoder accept the
finite values `1.7976931348623157e+308` (23 characters for non-negative times)
and `-1.7976931348623157e+308` (24 characters for signed floats).

Re-encoding the same trial 6,345 / clock 63 / 64-list shapes with those valid
finite values gives:

| Table | Package claim | Direct valid-schema encoding |
| --- | --- | --- |
| ledger | 7,007 B | 8,110 B |
| clocks | 225 B | 257 B |
| shadow | 215 B | 247 B |
| 64-clock blend | 329.338 B/row | 377.815 B/row |

This is still only a lower correction to the claimed bound: schema integer
normalization has a lower bound but no upper bound
(`raw_ledger.py:397-409`), so a true *schema-wide* worst row does not exist.
An intended-configuration bound must instead derive upper limits for every
counter and list from trials, clocks, pulse steps and state-machine invariants,
then combine those with the maximum canonical finite-float spellings.

Using only the corrected float widths on the package's exact 2,102,228 rows
raises row storage from 692.345 MB to **794.254 MB before fixed overhead**.
The current full verifier's same work arithmetic produces 889 h rather than
the execution note's 856 h because the slow measured rate moved; that
machine-dependent change is expected. The storage difference is not.

Option B separately bypasses even its own schema coefficient and uses the
small timing fixture's `benchmark.bytes_per_row`
(`verify.py:27203-27234`). Its 29,268 rows cost at least 10.652 MB under the
corrected 35-trial/64-clock finite-float encoding, plus 18 fixed run overheads,
not the quoted 3 MB conservative total.

**Minimal bounded fix:** rename the helper to an intended-configuration bound,
derive every integer/list maximum, encode maximal finite floats, compute a
separate one-clock central blend, and apply the relevant conservative
coefficient to matrix, pilot and Option B. Add the 8,110/257/247 reproduction
as a test and independently recalculate all displayed storage totals.

### Checkpoint judgment and exact option language

The narrow scientific conclusion is robust enough to tell John now:

<user_quoted_section>Under the 17 current, non-intended Ticket 04 evidence rows, none of the 12declared Ticket 07 options satisfies the frozen numerical budget; themoving-band result remains numerical_no_result, and time-unit bounds failat every trial count.</user_quoted_section>

The package is **not** ready to present as a choice between costed Options A
and B. Use these labels until the bounded fixes are reviewed:

- **Option A — unpriced intended-configuration validation outline.** The
current 42–3,120 h range times the PDE oracle and the post-generation
bootstrap only; it omits the moving replay and stationary observation work,
so it is neither an estimate nor an upper bound. No stage is shown
sufficient; every miss remains `numerical_no_result`; no physical claim is
licensed.
- **Option B — approximately 11.8 h, primary-only machinery diagnostic.** It
runs 18 primary identities at 35 trials/cell, excludes all four refinements,
the range pilot and numerical validation, and cannot lift either the
time-unit or moving-band blocker. Replace the 3 MB claim with a conservative
intended-schema estimate; the present direct correction is about 10.8 MB
including fixed overhead. It supports pipeline behavior only, not scaling,
causality or a physical law.

### Verification and package discipline

| Invocation | Current round-2 result |
| --- | --- |
| `python -m adler_born_two_channel.verify --verbose` | 126/126, exit 0 |
| `python -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python adler_born_two_channel/verify.py` | 126/126, exit 0 |
| `python -W error -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python -m adler_born_two_channel.verify --prove-failure-exit` | 126/127, exit 1; only injected failure |
| `python -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python -m compileall -q adler_born_two_channel` | exit 0 |

The current census remains 496 public callables, 1,305 invalid calls, 1,125
parameters, 120 acceptance criteria and 45 required nonclaims. Raw import
isolation, warnings, prior numerical residual/tolerance gates and no-write
cleanup all pass. `results/` is empty after the matrix.

No implementation file was edited, no pilot/campaign was run, no pilot
physical fit or forbidden output was opened, and no stage, commit or revert
was made. Current package hashes at adjudication:

```text
experiments.py 14e9a1daab28a3908fa42dbf4d1f6bcb49b3af56e16fd0fda6b6e57e05dfbcce
verify.py      0d27a17b0a4dcbc52479c3faf0e025ab68c0cde9c968d2c9b46f2eb0feb2557e
raw_runner.py  7b07bdf84ac88cc382b8ed3ee8dcb9831b8bf52a4724082ae293c4b4581a475d
README.md      1db104a792cf71137d0b7b25242a6678ddd2c90467693e9dffcc6469ee50990b
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

## Fix-up round 3 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 3 closes the production-width row bound and removes provenance from the
public count record, but the package is still not ready to present as a closed
checkpoint. Four authority defects and one presentation defect remain:

1. the proposal/checkpoint rebuild does not derive the recovery correlation
from the `RecoveryReport`, and it accepts a benchmark measured against a
different source fingerprint;
2. the pilot is readable by the supported unrestricted reader before the
post-write quarantine move, and a display-only range can still enter the
reference-rate/manifest path;
3. `post_range_power` reads the quarantine twice and can join a selection from
one closure snapshot to cells from another;
4. Option A still computes and materializes the old 41–3,120 h range internally
even though its returned alternative says `cost=None`; and
5. the README, verifier detail text and execution note still publish several
superseded facts.

The narrow blocker is unchanged and correct. The current proposal remains
`checkpoint_blocked`; this review did not create an approval, signature or
production-cleared state.

### What is now closed

| Area | Independent result |
| --- | --- |
| Public count view | Closed. `dataclasses.fields(PilotCellCounts)` is exactly `coupling, trials, committed`; `survivors` is the fourth public value, `__dict__` has no provenance, and `_Projection` no longer exists. |
| Name-only quarantine door | Closed after the move. Directory and file descriptors use `O_NOFOLLOW`, every payload is regular, the five-file closure gate runs, foreign/unquarantined/linked/changed runs refuse, and every supported `open_raw_run` spelling of a quarantined name refuses. Ordinary filesystem access remains accurately outside the anti-accident scope. |
| Proposal shape | Structurally closed. The map and serialized key set each contain exactly 80 fields; the design digest contains 75 and excludes exactly `design_digest`, the two free-text fields, `benchmark_digest` and `resource_digest`; the whole digest contains all 80. Only `status_reason` and `proposal_label` are classified free text. The current factory design digest is `d33c6818579d4b38a31bb0ecaebf64a876a07a8869f2b31f3ac3941f66bd144b`. |
| Power | Closed under the declared provisional assumptions: analytic 458; arm counts 2,406/6,346/2,406; exponent half-width 0.217908; adverse-floor contrast half-width 0.344543; 66,948 primary physical executions plus 3,360 shadow rewalks. The measured copula correlation remains distinct from the frozen floor. |
| Numerical blocker | Closed. Seventeen rows, probability allowance 0.00499471017, limiting bound 0.041245383 and `nmax=35`; time allowance 0.021953125, limiting bound 0.177000556 and no admissible `n`; all six blockers preserved. All 12 declared options fail, closest by 1.326466x, with positive feasible and unresolved controls. |
| Matrix | Closed. Six nodes; exact 64-clock midpoint grid on `[-3,3]`, spacing 0.09375, even parity and no origin clock; 10 eligible at `Kmin`; three arm grids; four finite refinements. Exact totals remain 22 identities, 67,748 physical executions, 3,400 shadows, 2,102,228 rows and 8,563,679,232 walked clock-steps. |
| Revision 2 / Ticket 06 | Closed. The corrected validation note remains the right choice; schema v3, 45 manifest keys, required gate phrases and fail-closed production status remain intact. |

### P1 — Recovery and benchmark measurements are not authoritative at checkpoint

`PROPOSAL_FIELD_SOURCES` says
`measured_arm_latent_correlation` comes from `RecoveryReport`
(`experiments.py:426`). It does not. `require_authoritative_proposal` accepts a
bare scalar `measured_arm_correlation` (`experiments.py:4941-4974`), and
`checkpoint_one_handoff` supplies that scalar from the proposal being checked,
not from the `recovery` component it already carries
(`experiments.py:5254-5264`). The field therefore rebuilds itself.

Exact end-to-end reproduction: I rehashed a valid proposal with correlation
`0.9` and passed it beside a `RecoveryReport` whose own declared generator
implies `0.85^2 * -0.25 = -0.180625`. `checkpoint_one_handoff` accepted it and
returned `no_feasible_matrix_among_searched` rather than refusing the mismatch.

The source/benchmark join is also missing. A valid `BenchmarkResult` carrying
`source_digest = "f" * 64`, a current `SourceFingerprint`, and a resource record
correctly citing that benchmark were accepted together by
`proposed_production_manifest`. The probe printed
`benchmark_source_mismatch_accepted True`. The factory checks
resource→matrix and resource→benchmark digests (`experiments.py:4812-4817`),
but never benchmark→source. A stale measurement from different source bytes can
therefore be presented inside a current-source proposal.

The round-2 mutations to numerical verdict/blockers/search and arm trials do
refuse when the original components are supplied. Source/environment,
firewall, numerical, power, matrix and resource field mismatches are otherwise
covered by the field-for-field rebuild. The two measurement joins above are
the surviving gaps, so the 80-entry source table is structurally complete but
semantically false for at least the recovery row.

**Bounded fix:** replace the scalar correlation argument with an exact
`RecoveryReport`, derive `correlation ** 2 * arm_correlation` inside the factory
and authoritative checker, and pass the handoff's recovery object. Require
`benchmark.source_digest == fingerprint.digest` both at factory and checkpoint.
Add the exact `0.9`/`-0.180625` and stale-source benchmark probes as
must-refuse tests. If the proposal is meant to provenance the whole recovery
measurement rather than only its derived correlation, add and bind a
`recovery_digest` field.

### P1 — The pilot authority chain still has three supported-path gaps

**Pre-quarantine exposure.** `quarantine_pilot_run` takes a completed run from
the ordinary results root and only then moves it
(`experiments.py:4035-4058`). `raw_runner.open_raw_run` has no pilot-label
refusal (`raw_runner.py:1132-1210`). A four-trial synthetic firewall fixture
reproduced the window exactly:

```text
pre_quarantine_open_succeeded pilot 4
already_returned_ledger_still_readable 4
post_quarantine_new_open_refused ValueError
```

The post-move directory is safe, but a simultaneous supported reader can obtain
the full `ClosedLedger` before the move and retain it afterward. This is not the
ordinary-filesystem exception; it is the package's supported unrestricted
reader.

**Display selection reaches the manifest.** `preview_range` honestly labels
its result display-only and uses synthetic closure digests
(`experiments.py:4285-4307`). But it returns the same `RangeSelection` type as
the authoritative door; `reference_rate` accepts any exact `RangeSelection`
(`experiments.py:4335-4351`), and the manifest factory accepts that same object
(`experiments.py:4780-4833`). Six invented count cells selected `[0.5, 2.0]`;
the first closure digest was all zeros; `reference_rate` returned
`1.0000000000000002`; and a post-range proposal accepted both that rate and the
preview selection digest. Thus display counts no longer enter `select_range`
or `post_range_power`, but they still enter the downstream frozen rate and
manifest.

**Two-snapshot post-range join.** `post_range_power` calls `select_range`, which
reads `_authoritative_cells`, then calls `_authoritative_cells` a second time
(`experiments.py:1871-1872`). An alternating-snapshot probe returned six
eligible cells on the first read and five cells on the second. The function
reported:

```text
authoritative_reads 2
first_selection_cells 6
returned_power_cells 5
returned_stage post_range_join verdict powered
```

No selection/closure digest is carried into `PowerEstimate`, so this mismatch
is not detectable afterward.

**Bounded fix:** make pilot-labeled runs unreachable through `open_raw_run`
even before quarantine, or write them directly into a separate root the
production reader never resolves. Give preview results a distinct display type
that `reference_rate` and the manifest refuse. For the authoritative path, read
one ordered `(counts, closure_digest)` snapshot, derive both selection and
post-range power from it, and bind the resulting selection digest into the
power/proposal join. Prefer making the post-range manifest take
`firewall + run_names` and recompute internally rather than accepting a caller's
selection.

### P1 — Option A remains numerically priced behind an unpriced wrapper

The returned `CheckpointAlternative` is correctly `cost=None`, explicitly says
the moving replay/paired-leaf and stationary endpoint generators are omitted,
promises no sufficiency and preserves `numerical_no_result`. That public record
is honest.

The normal builder still constructs `_t07_campaign`, whose
`ValidationCampaign.cost_range` explicitly returns lower and upper seconds
(`experiments.py:3620-3633`). `_t07_alternatives` evaluates the range and builds
two unused `CostLine` records (`verify.py:27205-27223`) before returning the
unpriced alternative. Independent execution reproduced:

```text
surviving_campaign_cost_range_hours 41.109231549802544 3120.0
stage_caps_hours [240.0, 240.0, 240.0, 240.0, 720.0, 720.0, 720.0]
```

The verifier and source comments still call these “two costed alternatives”.
Thus the old range survives, is computed on the supported checkpoint-builder
path, and can still be mistaken for an approval estimate even though the final
alternative discards it.

**Bounded fix:** remove `cost_range`, kernel-rate/cap aggregation, the seven
numeric `maximum_seconds` values and the two dead `CostLine` constructions from
the unpriced outline. Keep the stage ordering, units, levers and qualitative
stop/no-result rules. Reintroduce numeric costs only after all four end-to-end
kernels are benchmarked and joined.

### P2 — Storage code is repaired; the presentation is not

The intended production bound independently reproduces at 6,346 trials,
64 clocks and 2,048 steps:

| Table / mix | Bytes |
| --- | --- |
| `ledger.csv` | 8,110 |
| `clocks.csv` | 257 |
| `shadow.csv` | 247 |
| 64-clock blend | 377.8153846 per row |
| deliberately conservative one-clock blend | 4,183.5 per row |

At 2,102,228 rows and the measured 7,810-byte fixed maximum, the matrix is
794,425,900 bytes, about 794.4 MB. The central-arm direction is conservative:
its true one-clock shape is smaller, not larger. Derived plots, fits and other
analysis products remain excluded because the run does not write them.

Option B is also arithmetically closed. Its own 35-trial bound is 375.8153846
for the 64-clock mix and 4,181.5 for the deliberately over-priced central mix.
Twelve 64-clock runs plus six central runs give exactly 18 runs, 29,268 rows
and about 12.784 MB. The round-3 execution note labels those two coefficients
as 377.815 and 4,183.5 even though its storage totals are the 35-trial totals;
the labels are off by 2 bytes/row.

Wall hours are measurements, not design constants. This review's verbose run
measured the slow writer at 3,947 walked clock-steps/s and therefore printed
about 904 h for the matrix, 45.4 h for the separate pilot and 12.0 h for Option
B. The execution note's 854/42.9/11.4 h came from a faster measurement. Both
can be honest measurements, but John must see the hours, benchmark digest and
proposal digest from the same run.

Reader-facing prose remains materially stale:

- README lines 3629-3683 still say 844 h / 192 MB, provenance inside
`PilotCellCounts`, 78 proposal fields, 55 design fields and the superseded
`f1aff538...` digest;
- its heading says “two costed alternatives” while Option A says unpriced;
- the verbose verifier detail likewise says the public count has a provenance
digest and calls the pair “two costed alternatives”; and
- `post_range_power`, `select_range` and `_t07_synthetic_counts` docstrings
still describe deleted count/token interfaces.

These are precisely the statements a checkpoint reader sees, so the package is
not presentation-ready even apart from the P1 defects. Update and pin the
current structural counts/storage and describe machine-time figures as one
identified measurement rather than immutable source prose.

### Verification and discipline

| Invocation | Round-3 result |
| --- | --- |
| `python -m adler_born_two_channel.verify --verbose` | 126/126, exit 0 |
| `python -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python adler_born_two_channel/verify.py` | 126/126, exit 0 |
| `python -W error -m adler_born_two_channel.verify` | 126/126, exit 0 |
| `python -m adler_born_two_channel.verify --prove-failure-exit` | 126/127, exit 1; only the injected failure |
| `python -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python -m compileall -q adler_born_two_channel` | exit 0 |

The first matrix wrapper's explicit `py_compile` list accidentally named the
removed files `noise.py` and `raw_schema.py`, so that wrapper row exited 1; the
canonical wildcard command above was rerun and passed. This is a review-command
typo, not a package failure.

The suite still reports 499 public callables, 1,308 invalid calls, 1,142
parameters, 120 criteria and 45 nonclaims. Raw isolation, warnings, prior
residual/tolerance gates and cleanup pass. The results root is empty after all
verification and focused synthetic firewall probes. No authorized pilot or
validation campaign ran, no pilot exponent/curvature/physical fit was opened,
and nothing was staged, committed or reverted. The working tree remains at its
29 pre-existing entries. Ticket 08 remains status 0 at unchanged hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

Current package hashes:

```text
experiments.py 3e209e11c25e6cc07f1d4c15bf869cb44af805ddc09b532aac759c897d8c800a
verify.py      1073ee7df6215bff85b4a9ab27b635d160fd3e3338143dc7ee568efcd4988f2b
raw_runner.py  7b07bdf84ac88cc382b8ed3ee8dcb9831b8bf52a4724082ae293c4b4581a475d
README.md      10278f89c3ac19e5278260d5289c4557e09d6bac78a962e3f0496ed80dab2128
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

### Recommended checkpoint wording

John can be shown the narrow conclusion now, but not a closure or pilot
approval request:

<user_quoted_section>Ticket 07 remains checkpoint-blocked. Under the 17 current, non-intendedTicket 04 evidence rows, none of the 12 declared Ticket 07 optionssatisfies the frozen numerical budget. The moving-band result remainsnumerical_no_result; the probability evidence admits at most 35 trials percell against 2,406 required for the paired arm, and the time-unit bounds failat every trial count. This is no feasible matrix among the searched options,not a claim about every possible design.</user_quoted_section>

Until the authority fixes above are reviewed, phrase the options only as:

- **Option A — unpriced intended-configuration validation outline.** It omits
two observation-generation kernels, carries no defensible estimate or upper
bound, promises no sufficiency, and every miss remains
`numerical_no_result`.
- **Option B — machine-dependent approximately 12 h / 12.784 MB primary-only**
**diagnostic on this review host.** It is 18 runs and 29,268 rows, excludes the
pilot, all four refinements and all numerical validation, and supports
machinery behavior only — no scaling, causal or physical claim.

Do not authorize the pilot or present a production freeze from this package yet.

## Fix-up round 5 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 5 closes the direct-write race, the recovery/source measurement joins and
the numeric Option-A price path. It does **not** close the whole checkpoint
authority boundary. The package is still not ready to present to John as an
authoritative pilot-approval decision, for three reasons:

1. a caller-constructed `RangeSelection` can still authorize its own
contraction rate and post-range proposal, and the pilot door authenticates
the location but not the approved pilot model or configuration;
2. `checkpoint_one_handoff` rebuilds the proposal but accepts caller-built
alternatives and a caller-built pilot line, including a costed Option A and
a fictitiously cheap pilot; and
3. the new current-fact guard mutates only seven of its ten entries and scans
only the README, while the README, API docstrings and verbose verifier output
still state the superseded move lifecycle, provenance field and costed-
alternative story.

The narrow scientific blocker remains correct. The proposal status is still
`checkpoint_blocked`; this review created no approval, signature or
production-cleared state.

### Replay: what is now closed

| Area | Independent result |
| --- | --- |
| Proposal field model | Closed except for the selection source described below. There are exactly 81 fields, 76 design fields, five declared exclusions and 81 source-map entries. The map and key set are identical; only `proposal_label` and `status_reason` are free text. |
| Recovery authority | Closed. The proposal carries `recovery_digest` and derives the measured latent correlation as `r^2 * rho = -0.180625`. Fully rehashed records changing the correlation or recovery digest refuse at the authoritative rebuild. |
| Benchmark/source authority | Closed. A benchmark whose `source_digest` differs from the current fingerprint refuses at the factory. Rehashed source, environment, firewall, budget and resource mutations all refuse when the genuine components are supplied. |
| Direct pilot location | Closed. `write_pilot_run` opens the pinned quarantine descriptor and calls the same `_write_run_beneath` body used by the production writer: `O_EXCL \| O_NOFOLLOW`, regular files and marker last. It returns `QuarantinedPilotRun`, never `ClosedLedger`; the bare production path never exists. |
| Production raw compatibility | Closed. `write_raw_run` refuses the reserved `xpilot-` stream before opening a run directory, `open_raw_run` refuses a reserved manifest, and an ordinary historical `run_label="pilot"` on a non-reserved namespace still writes and opens. |
| One-snapshot count/power path | Closed inside `post_range_power`. It reopens the quarantined names once and derives the selection and power cells from that one ordered snapshot. Preview results are a different type. |
| Numeric Option-A path | Closed in the implementation. `cost_range`, `seconds_at`, `maximum_seconds`, numeric caps and the Option-A cost lines are absent. The actual helper returns `cost=None` and no stage promises sufficiency. |
| Scientific core | Closed and unchanged: 17 numerical rows, six blockers, 12 searched options, exact six-node matrix, arm-aware power, schema-v3 gates and all required nonclaims. |

### P1 — The post-range selection still authorizes itself

The original round-1 provenance finding is only partially closed.
`post_range_power` no longer accepts caller-built count records, but
`RangeSelection` itself remains a public unsealed dataclass
(`experiments.py:4213-4283`). `reference_rate` requires only the exact type,
and `proposed_production_manifest` takes that same caller-supplied object and
writes its rate, digest and purported closure digests
(`experiments.py:4854-5030`). `PowerEstimate` has no `selection_digest`, so the
power record cannot be joined back to the range that sized it.

The pure reproduction constructed a six-cell selection whose rule, count and
closure digests were invented strings. No run existed:

```text
public_range_constructed True 0.5 2.0
forged_reference_rate 1.0000000000000002
seal_field False
power_has_selection_digest False
```

Using the same public selection and an exact-typed power record labelled
`post_range_join`, the proposal factory and the supposedly authoritative
rebuild both accepted it:

```text
forged_selection_rebuild ACCEPTED 1.0000000000000002 True post_range_join False
```

The last `False` is the absence of `selection_digest` from `PowerEstimate`.
The proposal source table says these fields come from `RangeSelection`, but the
component is self-authenticating; the rebuild merely receives the same forged
component again.

**Minimal bounded fix:** make authoritative selections factory-only and
construct them only from one `_authoritative_cells` snapshot. Put that
selection digest in the post-range `PowerEstimate`, require it to equal the
manifest selection, and make the post-range proposal/checkpoint take
`firewall + run_names` and recompute rather than take a `RangeSelection` from
the caller. Add the exact six invented digests and a
`dataclasses.replace(selection, low=..., high=...)` reproduction as
must-refuse tests.

### P1 — The pilot is quarantined, but its approved design is not frozen

The new writer authenticates *where* a run is written, not *which pilot John*
*approved*. `write_pilot_run` accepts an arbitrary raw configuration and either
raw model (`experiments.py:4027-4067`). `_write_scoped_run` checks only that the
stream starts with `xpilot-`; `PilotFirewall.require_pilot_run` checks name,
label and exact namespace, but not model, coupling support, clock grid,
timestep, trials, shadow count or blocking parameters
(`experiments.py:3724-3862`).

The proposal's complete pilot field set is only:

```text
pilot_stream_namespace
pilot_run_directory_prefix
pilot_quarantine_directory
pilot_trials_eligible
pilot_ledger_fingerprints
```

`PilotFirewall` likewise carries only namespaces, prefixes and count
thresholds. There is no pilot-plan digest. The checkpoint's pilot `CostLine`
prices 200 trials over eight full-arm cells, but no record binds those numbers
or the candidate couplings to what `write_pilot_run` will accept.

The supported-path reproduction wrote a width-only, two-clock, `dt=1`,
two-trial run and immediately projected its counts:

```text
wrong_model_supported_write_ACCEPTED width_only 2 1.0 2 2 False True QuarantinedPilotRun
production_reader_reserved_refused ValueError
```

`False` is the absence of the bare production path; `True` is the quarantined
directory. Thus the physical isolation is correct, but a diagnostic control
run of an arbitrary size can become authoritative range-pilot evidence.

There is a smaller refusal-cleanup defect at the same boundary. A config on the
right namespace but with `run_label="production"` is written and closed before
`require_pilot_run` rejects it, leaving a quarantined directory that blocks a
correct retry:

```text
invalid_label_refused ValueError residue True
```

**Minimal bounded fix:** introduce a frozen `PilotPlan` that names the exact
candidate couplings, `model="full"`, 64-clock grid, intended timestep, trials,
shadow, block/window choices and run family; bind its digest in the proposal
and checkpoint. Make `write_pilot_run` take that plan and validate the manifest
before opening the run directory. The count door must recheck the same plan
against every closure. At minimum, wrong model/label/namespace/config must
refuse before leaving any directory.

### P1 — The checkpoint rebuild stops at the proposal, before the decision

`checkpoint_one_handoff` correctly rebuilds the 81-field proposal from the
components it carries. It then passes `alternatives` and `pilot_line` straight
through. `CheckpointAlternative` permits a cost on either label and arbitrary
scientific text; `Checkpoint1Handoff` checks only exact type and the two label
names (`experiments.py:5100-5264`). The pilot line is checked only for being a
`CostLine`, not for being the full-arm 200-by-eight line derived from the same
matrix and benchmark.

The exact adversarial handoff used genuine proposal, recovery, numerical,
power, matrix, resource and firewall components, but substituted a costed
Option A whose `supports` string was `"a physical scaling claim"`, plus a
one-second pilot line. It passed:

```text
false_decision_handoff ACCEPTED True a physical scaling claim 0.0002777777777777778
```

The boolean is `Option A.is_priced`; the last number is the pilot wall hours.
This is the same self-consistency/provenance error the proposal rebuild was
added to prevent, one layer later. The normal `_t07_alternatives` helper is
honest, but the checkpoint boundary does not require its output.

**Minimal bounded fix:** move the two alternative builders and the pilot-plan
cost builder into the authoritative module. Have `checkpoint_one_handoff`
derive or field-for-field rebuild them from the matrix, benchmark, numerical
disposition and frozen pilot plan. Enforce `cost is None` for
`intended_configuration_validation`, the exact 18-run resource record for
`narrowed_claim`, and the machinery-only/nonclaim vocabulary structurally.
Add the costed-A, physical-claim and one-second-pilot reproductions.

### Legacy mover adjudication

`quarantine_pilot_run` remains public, exported and move-based. Under the
supported graph it does **not** recreate the transient exposure:

- there are no call sites other than invalid API-shape probes;
- `write_raw_run` cannot create its reserved source;
- `write_pilot_run` creates the run directly at the target, so calling the
legacy mover on that current run refuses because the bare source does not
exist; and
- the mover only removes an already-existing source from the production root;
it does not write one there.

The runtime reproduction was `legacy_on_direct_current_refused ValueError`.
Therefore its existence is not a supported bypass and is not a closure blocker
by itself. It is not version-restricted, however: a manually placed current-
format reserved run can be moved by it. That is ordinary filesystem access,
accurately outside the anti-accident scope, but the public export should be
deprecated or made private once any real migration need has passed. Validate
the closure before the move if it remains, so an invalid input does not get
parked in quarantine on refusal.

### P2 — The current-fact guard does not guard the current package

Criterion 121 says all ten current facts are computed, mutated back to their
superseded spellings and checked with history left alone. The implementation at
`verify.py:28810-28915` has only seven entries with both a current and a stale
spelling. The old design digest, numerical verdict and searched-option count
are skipped by the mutation loop:

```text
mutation_controls_exercised 7 of 10
superseded design digest NOT_MUTATED
numerical verdict NOT_MUTATED
searched options NOT_MUTATED
```

The two history controls only assert that a marker occurs in a constructed
sentence and not in the README; they are not passed through the same detector.
Excluding the historical execution-note rounds is the right scope, but these
controls do not prove the advertised mutation behavior.

More importantly, the scan reads only `README.md`, and even that file still
says the normal pilot lifecycle is write-then-move
(`README.md:3644-3656`). Current API/help and verbose output also remain stale:

- `experiments.py:331` calls five exclusions “four keys”;
- `experiments.py:513-524` and `3738-3743` say pilots are moved;
- `experiments.py:3570-3578` says the unpriced campaign's cost is a range;
- `experiments.py:5100-5112` calls both alternatives costed;
- `verify.py:27205-27217` says stages are priced and describes lower/upper
range bounds and caps that no longer exist;
- `verify.py:28153`, `28286` and the verbose result say the run is moved;
- `verify.py:28295` says the four-value count record exposes a provenance
digest; and
- `verify.py:28679-28805` prints “two costed alternatives” while calling one
of them unpriced in the same sentence.

The live review measurement also differs from the unlabeled README snapshot:
the standard verbose run measured 3,929 walked clock-steps/s and printed about
908 h for the blocked matrix, 45.6 h for the separate pilot and 12.1 h for
Option B, while the README table says 844 h, 43 h and 11.5 h. Storage remains
the stable 794 MB / 12.78 MB. Variable machine time is not itself a defect;
presenting an old snapshot as the current cost without its benchmark and
proposal digest is.

**Minimal bounded fix:** correct all live README, API-docstring and verifier-
result claims; centralize the lifecycle and alternative wording rather than
restating it. Make the current-fact validator accept text as input and actually
run every one of ten current-to-stale mutations. Add a stale spelling for the
three skipped entries, include the direct-write lifecycle and current field
count, and scan every current user-facing source while explicitly excluding
the historical execution-note rounds. Label wall-time tables by environment,
benchmark digest and proposal digest.

### Scientific and resource reproduction

The independent standard run reproduced the intended benchmark and all frozen
scientific arithmetic:

| Item | Current result |
| --- | --- |
| Writer | five fixtures; one warmup + two repeats; intended 64 clocks, `dt=0.001953125`, 256 steps; intended repeats 12.509/12.491 s; conservative rate 3,929 walked clock-steps/s; rate span 1.29; base 4,383 vs shadow 4,019 incremental steps/s; peak 95 kB; trial/step growth 1.06/1.11; projected cube margin 162,787x |
| Power | analytic 458; arm trials full 2,406, central 6,346, width-only 2,406; recovery inflation 1.291 against 2.0; contrast inflation 0.699 against 1.25; measured latent correlation -0.180625 distinct from the -0.25 floor |
| Numerical | 17 rows; probability allowance 0.00499, limiting bound 0.04125, `nmax=35`; time allowance 0.02195, limiting bound 0.17700, no admissible `n`; `numerical_no_result` with all six blockers |
| Search | 12 declared options, none feasible; closest option misses by 1.326x; positive intended-configuration feasible and transferred-evidence unresolved controls still work |
| Matrix | six nodes, exact 64-clock even midpoint grid, spacing 0.09375, no origin, 10 eligible at the weakest coupling; 22 identities, 67,748 physical trials, 3,400 shadows, 2,102,228 rows and 8.564e9 walked clock-steps |
| Resources | about 908 h / 794 MB for the blocked matrix; separate pilot about 45.6 h; Option B exactly 18 runs / 29,268 rows / about 12.1 h / 12.78 MB on this invocation |

Option A's actual returned record remains honestly unpriced and promises no
sufficiency. Option B remains machinery-only and excludes the pilot, all four
refinements and every numerical-validation run. Neither resolves the time or
moving-band blocker.

### Verification and discipline

| Invocation | Round-5 independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127; normal completion |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected check |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite reports 502 public callables, 1,318 invalid calls, 1,152 parameters,
121 criteria and the prior nonclaims intact. Raw import isolation, Ticket-05
writer/reader regression, prior residual/tolerance gates and cleanup pass.
`results/` is absent after the full matrix and the focused synthetic firewall
fixtures. Nothing is staged; all 29 pre-existing worktree entries were
preserved. Ticket 08 remains status 0 at hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

No authorized range pilot or validation campaign ran. The only pilot-labelled
files were tiny synthetic firewall reproductions, immediately removed. No
pilot exponent, curvature, survival shape, dwell distribution or physical fit
was opened; no production state, stage, commit or revert was made.

Current source hashes reviewed:

```text
experiments.py 2d3c807fc2bf554fc72c2f1968314e0da542e740f08385db031cc358a345f5d0
verify.py      205ae341882d3c40e54b7831ed09dbbe29a5b30592de5a000d855571b5d6a5da
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
README.md      fddb8dbc3525ed2d52c676b0c273f5e1f9199844dd0e48b7baf8b206a1aceb70
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

### Recommended checkpoint wording

John can be shown the narrow scientific conclusion as a blocked status update,
but this package should not yet be presented as an authoritative pilot-approval
request:

<user_quoted_section>Ticket 07 remains checkpoint-blocked. Under the 17 current, non-intended Ticket 04 evidence rows, none of the 12 declared Ticket 07 options satisfies the frozen numerical budget. The moving-band result remains numerical_no_result; the probability evidence admits at most 35 trials per cell against 2,406 required for the paired arm, and the time-unit bounds fail at every trial count. This is no feasible matrix among the searched options, not a claim about every possible design. The pilot has not been authorized, and its exact model/configuration and count-derived selection still need to be bound at the checkpoint boundary before it can run.</user_quoted_section>

Phrase the options only as:

- **Option A — unpriced intended-configuration validation outline.** It has no
estimate or upper bound, promises no sufficiency, and every miss remains
`numerical_no_result`.
- **Option B — machine-dependent approximately 12.1 h / 12.78 MB on this**
**review invocation, primary-only machinery diagnostic.** It is exactly 18
runs and 29,268 rows, excludes the pilot, all refinements and numerical
validation, and supports no scaling, causal or physical claim.

Do not authorize the pilot or present a production freeze until the selection,
pilot-plan and checkpoint-decision authority fixes above are reviewed.

## Fix-up round 8 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 8 closes the previous costed-Option-A / one-second-pilot checkpoint
injection, adds the frozen pilot record and the one-snapshot post-range record,
and repairs the live prose it actually scans. It does **not** close the whole
pilot-to-production authority chain. Four independently reproduced defects
remain:

1. post-range power can report `powered` while one required arm is over the
declared per-cell ceiling;
2. the proposal recomputes an authoritative post-range power record and then
discards it, serializing a different caller-supplied `PowerEstimate` instead;
3. the ordered pilot identity set is not exact — reordered and incomplete
plans are accepted as scientific post-range outcomes; and
4. `PilotPlan` construction is gated only by a reachable token, and neither
the proposal nor checkpoint rebuild establishes that it is the approved
production pilot rather than the verifier-only eight-clock fixture or a
record carrying false environment/schema/config claims.

The package therefore remains unsuitable for pilot approval or a post-pilot
production freeze. The narrow scientific blocker remains correct and nothing
in this review licenses a pilot, campaign, production run or physical claim.

### Frozen scope and what is now closed

All six requested implementation hashes match before and after review:

```text
experiments.py f763243d9712482553e24c8f016db7d5d0834b3dadd716c549cfd55bae914613
verify.py      dfe964eec66c6a8fd34773d39a0917e87931fbcffc8dea23e52d712178468369
README.md      c06943c5aebfcd803bb4c23a65d61c8443912ebf385d05a4d973b1da6308f45a
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py  eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

The requested design digest reproduces exactly as
`064998ab04d8ab8708074f8e0260ab6fb63fb3006b9aac68d812c020b176be8a`
under the recorded Miniconda Python 3.13 / NumPy 2.4.3 environment. The system
Python 3.12 / NumPy 2.3.5 build produces a different design digest because the
environment tuple is deliberately inside the freeze; the source bytes are not
moving.

| Area | Independent result |
| --- | --- |
| Deterministic fixture | Closed as a fixture. Its final tables pass the full closure gate, identities and exposure are rebuilt, the shadow is the declared prefix, it honestly declares eight clocks and `dt=0.05`, the production plan refuses its manifests, and cleanup removes it. It is not production evidence. |
| Non-zero pulse centre | Closed in the factory path. A plan at `pulse_centre=0.75` round-tripped `0.75` through `PilotPlan`, `config_for`, the 45-field manifest and `require_manifest`. |
| Pilot write isolation | Closed on the supported writer: direct-to-quarantine, reserved production write/read refusal, no ordinary-results exposure, five-file closure, `O_NOFOLLOW` and pinned descriptors. Invalid caller-controlled name/config inputs are resolved before the run directory is opened. |
| Naked selection/rate | Closed at the public signatures. `reference_rate`, `post_range_power`, the proposal and checkpoint take plan/firewall/run names rather than a caller's `RangeSelection`; preview selections remain a different display-only type. |
| Proposal shape | Structurally closed: 86 fields, 81 design fields, five declared exclusions and 86 source-map rows. The design digest and whole digest cover the declared sets, and direct proposal field forgeries are refused when genuine authoritative components rebuild them. |
| Checkpoint alternatives | Closed for the prior exact attack. `checkpoint_one_handoff` has no `alternatives` or `pilot_line` parameter; Option A is exactly unpriced and `unpriced_no_claim`, Option B is rebuilt as 18 runs / 29,268 rows and machinery-only, and the pilot line is derived from the plan and slowest live benchmark. The prior costed-A, physical-claim and one-second line cannot enter. |
| Option A numeric path | Closed. No numeric price, cap, range, `cost_range`, `maximum_seconds` or hidden Option-A cost line survives. The validation campaign carries shapes only and promises no sufficiency. |
| Resource arithmetic | Closed for the current records: 22 matrix identities, 67,748 physical executions, 3,400 shadows, 2,102,228 rows, 8,563,679,232 walked clock-steps and about 794 MB. Option B is exactly 18 runs, 29,268 rows and about 12.78 MB. Hours remain correctly machine-dependent snapshots. |
| Scientific boundary | Closed and unchanged: 17 non-intended Ticket-04 rows, 12 searched options, probability `nmax=35` versus 2,406 paired trials, time failure at every count, moving `numerical_no_result`, six blockers and no physical/Born/detector/two-channel/production claim. Manifest schema 3 remains below production-status schema 4. |

### P1 — The post-range affordability verdict ignores the largest arm

`_finish_power` sizes every arm separately, but the affordability condition at
`experiments.py:1853-1859` compares only `trials`, the common count of the
*paired* full and width-only arms, to `maximum_trials_per_cell`. The error
message itself reports `max(sized.values())`, but that maximum is not what the
condition tests. The unpaired central control can therefore exceed the ceiling
while the record says `powered`.

The honest four-cell deterministic fixture reproduced exactly:

```text
post_range_status post_range_powered
paired/full trials 8419
central_control trials 22211
width_only_control trials 8419
declared maximum_trials_per_cell 20000
power_verdict powered
```

The central arm is 2,211 trials per cell over the declared ceiling, yet the
`PostRangePlan` derives `post_range_powered` from that false verdict at
`experiments.py:5055-5059`. This is not a display defect: it is the status the
proposal and checkpoint are intended to consume after the pilot.

**Minimal bounded fix:** compare `max(sized.values())` to the ceiling and name
the driving arm in the reason. Add a post-range fixture where the unpaired arm
alone crosses the ceiling and require `no_powered_matrix` /
`post_range_no_powered_matrix`.

### P1 — The proposal discards the authoritative post-range power it computes

The proposal factory does take one authoritative snapshot. At
`experiments.py:5607-5609` it receives `(selection, power, post_range)` but
binds the middle value to `_` and discards it. At
`experiments.py:5690-5693` it serializes the separate caller-supplied
`power.digest`, `power.stage` and `power.verdict`. There is no equality check
between that record and `post_range.power_digest`, no equality between their
selection digests, and no requirement that the matrix couplings/trials match
the selected range and its re-sized arm counts.

Exact public/reachable reproduction, with genuine fixture closures and a
`dataclasses.replace`-built exact `PowerEstimate`:

```text
forged_power_proposal_ACCEPTED True
proposal power stage post_range_join
proposal power selection ffffffffffffffff...
authoritative selection      c58ff676cd941ad8...
selection_mismatch True
power_digest_mismatch_postrange True
forged cells/arm trials 6 {'full': 2406, 'central_control': 6346,
                           'width_only_control': 2406}
actual cells/arm trials 4 {'full': 8419, 'central_control': 22211,
                           'width_only_control': 8419}
```

`require_authoritative_proposal` accepted the result because it rebuilt the
same mismatch from the same supplied forged power. `checkpoint_one_handoff`
passes that same power and run-name list into the same rebuild at
`experiments.py:6261-6269`, so the checkpoint adds no missing join.

This also lets the proposal's six-node `PrimaryMatrix` survive beside a
four-cell selected range. The post-range digest is genuinely derived, but it
is an adjacent truthful record rather than the authority for the power and
matrix fields that will be frozen.

**Minimal bounded fix:** on a non-empty pilot run list, use the authoritative
power returned by `_post_range_snapshot` and either remove the `power` argument
or require exact digest equality. Rebuild or require the post-range matrix and
resource estimate from the selected couplings and authoritative arm counts.
Require `power.selection_digest == selection.digest == post_range.selection_digest` and `power.digest == post_range.power_digest` at
the proposal and checkpoint boundaries. Add the exact `f...f` replacement and
six-versus-four matrix reproduction as must-refuse tests.

### P1 — Missing and reordered pilot identities are accepted as outcomes

`_authoritative_cells` validates each named manifest and rejects duplicate
names/couplings, but it never requires the set of couplings to equal the
plan's candidate set or the caller's order to follow that set
(`experiments.py:4643-4672`). It sorts the pairs by coupling before selection.
Consequently a missing run is interpreted as count-rule evidence rather than
an incomplete pilot, and a reordered run list is accepted.

Exact reproduction over the four-cell fixture:

```text
normal post_range_powered
reordered_ACCEPTED post_range_powered
reordered run_names (...cell-3, ...cell-2, ...cell-1, ...cell-0)
missing_ACCEPTED post_range_refused run_too_short
missing run_names (...cell-0, ...cell-1, ...cell-2)
```

The missing case is especially dangerous: `run_too_short` reads as a
scientific selection refusal even though the approved pilot was never
completed. The reorder also exposes a binding defect at
`experiments.py:5048-5050`: original-order names are zipped to coupling-sorted
closure digests, so the aggregate closure record associates names with the
wrong closures whenever input order changes.

**Minimal bounded fix:** derive one canonical `(coupling, run_name)` identity
for every declared candidate and require exact set and order before reading an
outcome. Missing, extra, reordered, duplicate and foreign runs must be input
errors, not selection refusals. Build the aggregate closure digest from the
same canonical `(name, counts, closure)` records rather than zipping two
differently ordered sequences.

### P1 — `PilotPlan` is self-authenticating, and the verifier-only plan can reach the checkpoint boundary

The record says it is factory-only, but `PilotPlan.__post_init__` checks only
identity with reachable `experiments._PLAN_SEAL` and validates no field
relationship (`experiments.py:4067-4075`). `require_plan_firewall` checks only
the firewall digest and stream. The proposal checks the plan's source digest,
but does not rebuild the plan or validate its environment versions, schema
versions or `config_digest`.

Two independent reproductions survive the supposedly authoritative proposal
rebuild:

1. The genuine verifier-only plan — eight clocks, `dt=0.05`, four candidate
couplings and explicitly labelled “not the approved pilot” — was accepted by
`proposed_production_manifest` and `require_authoritative_proposal`, including
with its fixture closures. Thus the test fixture can reach the production
proposal boundary even though the production plan correctly refuses its
manifests when used directly.
2. Starting from the real production plan, direct exact-type construction with
the reachable seal changed `python_version`, `numpy_version`, `platform`,
ledger schema, manifest schema and `config_digest` while retaining the current
source digest. The proposal and authoritative rebuild accepted it:

```text
forged_plan_proposal_ACCEPTED True
plan claims forged-python forged-numpy forged-platform 999 998 eeeeeeeeeeeeeeee...
proposal claims live environment 3.12.6 2.3.5 schema 3/3
```

The plan digest freezes both stories without joining them. Manifest revalidation
does not help because those provenance fields are not used by `config_for` or
`require_manifest`.

**Minimal bounded fix:** add an authoritative production-pilot builder/rebuild
in `experiments.py`, not only the generic verifier-accessible `pilot_plan`
factory. Recompute every derived plan field — grid, window, shadow, block,
selection rule, environment, schemas and config digest — from canonical inputs
at proposal/checkpoint consumption, and compare field for field. Require the
approved production plan identity/digest, so the honest fixture plan remains
valid for verifier doors but cannot enter a production proposal. Add the exact
fixture-plan and forged environment/schema/config reproductions.

### P2 — The current-fact validator still does not scan every live module

The twelve declared README mutations and all three historical controls now do
traverse `_validate_current_facts`; that round-5 defect is closed. Source
discovery is still narrower than the advertised “every live user-facing
source.” `_live_prose_sources` hard-codes only `README.md`, `experiments.py`,
`raw_runner.py`, `__init__.py` and extracted verifier strings
(`verify.py:29421-29469`). It omits sixteen live Python modules, including
`analysis.py`, `compare.py`, `raw_config.py`, `raw_ledger.py` and
`raw_race.py`. The check at `verify.py:29605-29609` actively fails if the live
source set grows, so this is an enforced exclusion rather than an accidental
gap.

The current grep over all package Python/README sources found no unambiguous
surviving stale Ticket-07 claim outside the guard's own mutation strings. The
finding is nevertheless actionable because inserting one of the twelve stale
spellings into any omitted public module cannot reach the detector the
criterion says is unified.

**Minimal bounded fix:** discover all live package `.py` sources and extract
their user-facing literals/docstrings, with an explicit narrow exclusion only
for the mutation table and validator body. Add one mutation in an otherwise
unmentioned module such as `compare.py` and require the same validator to
catch it. Keep historical Traycer notes excluded by path as they are now.

### Scientific, resource and checkpoint reproduction

The standard verbose run independently reproduced:

| Item | Result on this invocation |
| --- | --- |
| Writer benchmark | Five real-writer fixtures; intended 64 clocks at `dt=0.001953125`; slowest about 4,129 walked clock-steps/s; traced peak about 102 kB; no cube materialized. |
| Power before pilot | Analytic 458; arm trials 2,406 / 6,346 / 2,406; recovery inflation 1.291; adverse contrast floor retained. |
| Numerical | 17 rows; probability allowance 0.00499; limiting bound 0.04125; `nmax=35`; time allowance 0.02195 against 0.17700 and failure at every count; all six blockers. |
| Search | 12 declared options; none feasible; closest misses by 1.326x; feasible and unresolved controls remain live. |
| Matrix | Six nodes, 64-clock even midpoint grid, no origin clock, 10 eligible at the weakest node; 22 identities and exact resource arithmetic above. |
| Machine-dependent timing | About 864 h for the blocked matrix, 43.4 h for the separate pilot and 11.5 h for Option B on this Python 3.12 invocation. Stable storage: about 794 MB and 12.78 MB. |

Ticket 06 remains fail-closed at manifest schema 3 versus production-status
schema 4. Ticket 08 remains status 0 with unchanged hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.
No pilot, validation campaign or production run was performed, and no pilot
exponent, curvature, survival shape, commit-time distribution or physical fit
was opened.

### Verification and discipline

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the deliberate probe fails |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The verifier reports 518 public callables, 1,363 invalid calls, 1,257
parameters, 121 acceptance criteria and the 45 required nonclaims. Raw import
isolation, the Ticket-05 writer/reader regression, API census, documentation,
warnings, no-write analysis and results cleanup all pass. `results/` is absent
after the full matrix and the focused adversarial fixtures. No implementation
file, ticket status, Git index entry or unrelated file was edited; only this
review round was appended.

### Recommended checkpoint wording

The narrow result remains suitable only as a blocked status update:

<user_quoted_section>Under the 17 current, non-intended Ticket 04 evidence rows, none of the 12 declared Ticket 07 options satisfies the frozen numerical budget. The moving-band result remains numerical_no_result; probability evidence admits at most 35 trials per cell against 2,406 required for the paired arm, and the time-unit bounds fail at every trial count. This is no feasible matrix among the searched options, not a claim about every possible design. The pilot has not been authorized.</user_quoted_section>

Do not present the post-range plan, proposal or checkpoint as authoritative
until the affordability, power/matrix join, exact run-identity and pilot-plan
authority defects above are fixed and independently re-reviewed.

## Fix-up round 9 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 9 closes the exact affordability, forged-power, ordered-identity and
false-provenance attacks from round 8. It does not close Ticket 07. Two
disclosed limitations are reachable production authority paths, not harmless
test-only qualifications:

1. the public post-range proposal path accepts a power record sized for four
selected cells beside the old six-cell matrix and serializes both stories;
the authoritative proposal rebuild and checkpoint accept that contradiction;
2. the verifier's eight-clock `_t07_probe_production_plan` is accepted as an
authoritative production plan even though it is not the frozen 64-clock
pilot, and its real quarantined fixture rows can drive the first defect.

The live-prose detector also misses current stale budget-provenance statements
in `compare.py` and a line-wrapped equivalent in `__init__.py`. The scientific
result remains the same narrow blocked no-result. Nothing in this review
licenses a pilot, validation campaign, production run, Ticket 08 activity or a
physical/Born/detector/two-channel claim.

### Frozen scope and closed replays

The six requested hashes matched before and after review:

```text
experiments.py 21c95b717da80f94ba19418ac660b6a5818852be38a44fc415fae18990f7d1d6
verify.py      11b52e029032a794bc845023bc60279e7398223677f1ec68275cd42263f76afd
README.md      228761ee13d5e00c53a064fff6cfb9f182b808ae6aea2996a3b09b570e558d2a
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py  eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
__init__.py    aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b
```

Under Miniconda Python 3.13.11 / NumPy 2.4.3 the frozen proposal design digest
reproduced as `08b5dc14ab5a0a36...`. The following prior attacks are now
closed on public/reachable behavior:

- the deterministic four-cell fixture carries real full-gate tables, exact
200-trial identities and exposure, the declared shadow prefix, its honest
eight-clock plan, five-file closure and cleanup; it is refused as a declared
`verifier_fixture` at production doors;
- all three post-range arm sizes are 8,419 / 22,211 / 8,419 against a ceiling
of 20,000 and the verdict is `no_powered_matrix`; a ceiling of 22,211 admits
and 22,210 refuses;
- reversed, omitted, duplicated, extra, foreign, swapped and renamed run lists
are authority refusals before a selection or power decision; the name,
coupling and closure remain one record and are not cross-zipped;
- `dataclasses.replace` cannot construct a `PilotPlan`; direct sealed plans
with false Python, NumPy, platform, source, schema or configuration claims
are refused by authoritative rebuild; a fixture-purpose plan cannot reach a
production proposal;
- provisional/relabelled/replaced `PowerEstimate` records are refused beside
real runs unless their exact digest equals the one-snapshot recount;
- the public writer remains direct-to-quarantine, reserved production
identities refuse write and read, no ordinary-results exposure occurs, and
the five-file `O_NOFOLLOW` closure remains intact;
- the prior costed/physical Option A and one-second pilot line have no caller
route; Option A is unpriced and non-sufficient, while Option B is exactly 18
runs / 29,268 rows and machinery-only; and
- the non-zero pulse centre, 86-field / 81-design-field proposal, source map,
direct proposal forgery refusals, row/storage/resource arithmetic, schema-v3
fail-closed behavior and narrow scientific boundary all remain green.

### P1 — The post-range proposal and checkpoint accept mutually incompatible matrix and power authority

`proposed_production_manifest` applies the target-power and matrix-power joins
only when `pilot_run_names` is empty (`experiments.py:5809-5816` and
`5829-5840`). With names present it correctly rebuilds the one-snapshot power
and requires the caller's digest to equal it (`5853-5864`), but then emits
`trials_per_cell` and `arm_trials` from the old `PrimaryMatrix`
(`5921-5923`) beside `power_digest`, stage and verdict from the post-range
estimate (`5950-5953`). The source comment says nothing here produces a
post-range proposal. The public factory does.

Exact frozen-environment reproduction using genuine five-file quarantined
runs from the verifier's production-purpose probe plan:

```text
joined power: cells=4, verdict=no_powered_matrix
joined arm trials: {'full': 8419, 'central_control': 22211,
                    'width_only_control': 8419}
joined target digest: 3555436d2a3b6217...

matrix: cells=6
matrix arm trials: {'full': 2406, 'central_control': 6346,
                    'width_only_control': 2406}
matrix digest: 50f3feffd624e87c...

proposal_ACCEPTED
proposal sampling_target_digest: 36f6c78e2c85fb64...
proposal power_digest: 6d0668cafacc72b0...
proposal arm_trials: [['full', 2406], ['central_control', 6346],
                      ['width_only_control', 2406]]
authoritative_rebuild_ACCEPTED
checkpoint_ACCEPTED post_range_join 50f3feffd624e87c...
```

`require_authoritative_proposal` reproduces the same stage-aware skipped joins,
so it accepts the record. `checkpoint_one_handoff` calls that rebuild and then
stores the caller's post-range `power` beside the old `matrix` and proposal
(`experiments.py:6521-6545`), so the checkpoint accepts three inconsistent
surfaces: post-range power, pre-pilot matrix and proposal arm counts. The
`post_range_no_powered_matrix` status blocks approval, but blocking status does
not make a contradictory frozen record authoritative.

**Closure condition:** until Ticket 08 re-derives a matrix, a non-empty
post-range run list must fail closed at proposal and checkpoint. Alternatively,
derive and join the post-range matrix/resources before either record exists,
and require exact equality among selected couplings, target, every arm count,
matrix digest, power digest and post-range digest. Add the reproduction above
as must-refuse rather than as a successful positive-control proposal.

### P1 — Any self-rebuilding production-purpose plan is accepted; the eight-clock probe authorizes the defect above

`require_authoritative_plan` rebuilds a plan from *that plan's own declared*
*inputs*. This closes false derived/provenance fields, but it establishes only
self-consistency. It never requires the canonical frozen production plan or
its digest. The only production/fixture distinction is the caller-chosen
`purpose` plus the `-fixture-` naming convention.

The verifier openly constructs `_t07_probe_production_plan` as
`approved_production_pilot` with eight clocks, `dt=0.05`, four couplings and a
non-fixture prefix (`verify.py:27396-27415`), while `_t07_plan` is the actual
64-clock, `dt=0.001953125`, six-coupling frozen pilot. Exact reproduction:

```text
probe digest:  ebcf610bf959fc10...
frozen digest: 6a19687f03e5e8c5...
equal: False
probe:  approved_production_pilot, 8 clocks, dt=0.05, 4 cells
frozen: approved_production_pilot, 64 clocks, dt=0.001953125, 6 cells
require_authoritative_plan(probe, ...): ACCEPTED
```

This is not confined to the intended negative test. The first reproduction
used that plan's real quarantine fixture, then reached
`proposed_production_manifest`, `require_authoritative_proposal` and
`checkpoint_one_handoff`. The probe therefore supplies a supported route from
probe-only physics into production authority despite its docstring saying
"nothing is decided from it."

**Closure condition:** production consumption must require one canonical plan
identity/digest rebuilt from the exact Ticket-07 frozen inputs, not arbitrary
inputs labeled with a production purpose. A cheap production-purpose probe
must be structurally unable to reach proposal/checkpoint; test the power-digest
refusal below the scientific boundary without minting an alternative approved
pilot.

### P2 — The unified live-prose claim is false and current stale provenance survives

`_live_prose_sources` now discovers all package modules, which closes the
round-8 enumeration gap. The stale-stage validator remains a second,
non-unified path: `check_stale_stage_strings` hard-codes only `README.md`,
`raw_runner.py`, `experiments.py`, `__init__.py` and printed banner lines
(`verify.py:30074-30097`). Its regexes also spell literal spaces, so a
source-wrapped sentence can evade them.

Current live sources contain:

```text
compare.py:83   "no production numerical budget exists yet."
compare.py:232  "production numerical budget and it does not exist yet."
__init__.py:135-136  "production numerical\nbudget belongs to a later ticket
                     and does not exist yet"
```

Exact result:

```text
len(_live_prose_sources()) = 22
'compare.py' in sources = True
'no production numerical budget exists yet' in sources['compare.py'] = True
check_stale_stage_strings().passed = True
```

The twelve-entry `_t07_current_facts` table has no budget-existence/provenance
fact, so the broader discovery does not help this spelling; the dedicated
stale-stage check excludes `compare.py` and misses the wrapped `__init__.py`
form. This contradicts the live package's correct current statement: Ticket 07
has frozen a production numerical budget and it is **not met**.

**Closure condition:** use the same discovered live-source set and one
whitespace-tolerant semantic detector for budget provenance, including module
docstrings, comments/help, banner/output strings and f-string literal pieces.
Add the exact `compare.py` sentences and a line-wrapped/dynamic-string control
as must-fail tests.

### Scientific, resource and verification reproduction

The frozen-environment verbose run independently reproduced 17 non-intended
Ticket-04 evidence rows, 12 searched options, probability `nmax=35` against
2,406 paired trials, time failure at every trial count, the moving-band
`numerical_no_result`, all six blockers, 86 proposal fields / 81 design fields,
67,748 physical executions, 3,400 shadows, 2,102,228 durable rows, about
794 MB, unpriced Option A and Option B at 18 runs / 29,268 rows / 12.78 MB.
The machine-dependent snapshot on this run was about 900 h for the blocked
matrix and about 12.0 h for Option B; it is correctly labeled and does not
become a portable claim. Manifest schema 3 remains below production-status
schema 4. Ticket 08 remains status 0 with hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the deliberate probe fails |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite reports 523 public callables, 1,373 invalid calls and 1,266
parameters. Raw isolation, Ticket-05 regression, no-write analysis, API census,
documentation, warnings and cleanup all pass. `results/` is absent; all review
fixtures were removed. No implementation file, ticket status, Git index entry
or unrelated file was edited; only this independent-review round was appended.

Do not present the post-range proposal/checkpoint as an authoritative freeze,
and do not authorize the pilot, until both production-plan identity and the
post-range matrix/power join fail closed and are independently re-reviewed.

## Fix-up round 10 independent closure re-review — 2026-08-30

### Strict verdict: OPEN

Round 10 closes the exact round-9 four-cell-power/six-cell-matrix record and
the arbitrary self-consistent production-plan path. It does not close Ticket
07. The verifier-only fixture writer accepts the canonical production plan
and a polymorphic plan, writes canonical reserved identities, and can put
fixture-cloned physics through the genuine production recount, proposal,
authoritative rebuild and checkpoint. In addition, direct verifier execution
fails reproducibly and the requested warnings run failed in the frozen matrix,
so the full command/cleanup matrix is not green.

The current scientific conclusion remains the narrow blocked one. Nothing in
this review licenses a pilot, validation campaign, production run, Ticket 08
activity, physical interpretation, Born claim, detector claim or two-channel
claim.

### Frozen scope

The requested bytes matched before and after review:

```text
experiments.py 1baf7013c3d10d4a2f3050ef3b9b0d948fa4ff9e8b5e90a9bda9a05fcd12f672
verify.py      494aae89c4fee77e89cc4564a9668eeaaa1ddd3d9d2442265e8a9ed83e5dcbb3
README.md      3a99c991b1c430789c6899a186e1b5daa7046351a513dedce4cf36ca27507868
compare.py     abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py    9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py  eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
```

Miniconda Python 3.13.11 / NumPy 2.4.3 reproduced canonical plan digest
`5b55647ef587b065...` and provisional proposal design digest
`a84750ce21edb5c2...`. No implementation file, ticket status or Git index
entry was changed by this review.

### Closed replays

The following requested round-9 attacks are closed on the frozen bytes:

- the genuine four-cell post-range estimate is
`no_powered_matrix`, with 8,419 / 22,211 / 8,419 arm counts against the
20,000 ceiling; `_require_post_range_design` refuses it beside the
six-cell 2,406 / 6,346 / 2,406 matrix with the named
`post_range_matrix_not_derived` reason, while the coherent provisional
design survives;
- the production doors require the exact canonical 64-clock, six-cell,
`dt=0.001953125` plan from `PRODUCTION_PILOT_SPEC`, the live fingerprint,
schemas and firewall. The former eight-clock plan, direct exact-type
mutations, `dataclasses.replace`, subclasses and one-field changes are
refused at those doors; `_t07_probe_production_plan` is gone;
- replaced or forged power records disagreeing with the one-snapshot recount
are refused; ordered run names, couplings and closures remain aligned, and
reversed, missing, duplicated, extra and foreign identities refuse before a
scientific decision;
- direct-to-quarantine writing, reserved production read/write refusal,
five-file closure, `O_NOFOLLOW`, no ordinary-results exposure and nonzero
pulse-centre threading remain intact;
- Option A remains exactly unpriced and non-sufficient; Option B remains the
machinery-only 18-run / 29,268-row diagnostic. The matrix arithmetic remains
67,748 physical executions, 3,400 shadows, 2,102,228 durable rows and about
794 MB, with timing explicitly machine-dependent;
- all 22 discovered current sources now say that Ticket 07's production
numerical budget exists and is not met. The distinct statement that
production-status schema v4 does not exist yet remains truthful because the
live manifest schema is still v3; and
- the scientific boundary remains 17 non-intended Ticket-04 evidence rows,
12 searched options, probability `nmax=35` versus 2,406, time failure at
every trial count, moving-band `numerical_no_result`, and no intended-
configuration evidence. No pilot, campaign or Ticket-08 run occurred.

### P1 — The verifier fixture writer can mint canonical production evidence

`verify._t07_pilot_fixture(plan)` and `_t07_write_fixture_cell` at
`verify.py:27494-27569` impose no exact-type, fixture-purpose or fixture-prefix
guard. The writer calls `plan.config_for(coupling)` once to generate a tiny
source run and a second time to create the manifest. It then clones the tiny
source histories to the declared trial count and writes whatever
`plan.run_name_for` returns. Passing the canonical plan therefore writes the
reserved `xpilot-t07-cell-*` family; passing a same-field `PilotPlan` subclass
also lets the source and manifest calls return different configurations.

Exact reachable reproduction used an `AlternatingPlan` whose fields and
digest equal the canonical plan, whose odd `config_for` calls return a cheap
`dt=0.05`, coupling-0.2 source configuration, and whose even calls return the
canonical manifest configuration. The fixture writer created all six
canonical reserved names and removed its source directories. The genuine
exact-typed canonical base plan then consumed those closures:

```text
written names: xpilot-t07-cell-0 ... xpilot-t07-cell-5
select_range(base plan): selected=True, cells=6
post_range_power: verdict=powered, stage=post_range_join, cells=6
arm trials: {'full': 2406, 'central_control': 6346,
             'width_only_control': 2406}
proposal: ACCEPTED, power_status=post_range_powered
require_authoritative_proposal: ACCEPTED
checkpoint_one_handoff: ACCEPTED
checkpoint stage/status: post_range_join / post_range_powered
cleanup: results absent
```

This is not the closed four-cell/two-design attack: it is a counterfeit
six-cell authoritative snapshot whose counts happen to match the provisional
matrix. Consequently `_require_post_range_design` passes. It disproves both
"the fixture cannot masquerade as production evidence" and "Ticket 07
produces no post-range production proposal." The checkpoint remains globally
blocked by the numerical disposition, but blocked status does not turn cloned
four-trial fixture histories into production evidence.

**Closure condition:** the fixture writer must require an exact fixture-plan
type/identity, fixture purpose and fixture-only name prefix before creating a
directory; it must refuse the canonical production plan and subclasses. Use
one immutable configuration snapshot for both source generation and manifest
construction. Add the alternating-`config_for` reproduction and the simpler
canonical-plan call as must-refuse tests. Production authority must also bind
an origin that a verifier cloning helper cannot mint merely by reproducing the
same manifest and five-file closure.

### P1 — The required direct/warnings verifier matrix is not green

The frozen matrix produced:

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | uncaught lifecycle error, exit 1 |
| `python3 -W error -m adler_born_two_channel.verify` | uncaught lifecycle error, exit 1 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the deliberate check fails |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The first direct failure observed `verify-t6full-0002` change between its open
and authoritative reopen. An isolated direct retry failed again, independently,
while `run_benchmark` wrote its close marker:

```text
verify.py:5936 check_documented_counts
verify.py:15802 _ticket07_api_rows
verify.py:27139 _t07_benchmarks
experiments.py:1224 run_benchmark
raw_runner.py:1166 _write_run_beneath
ValueError: the close marker could not be created (No such file or directory)
ROUND10_DIRECT_RETRY_EXIT=1
```

The warnings run in the full sequential matrix then found
`verify-t6full-0002` missing and exited 1. Two later retry processes were
terminated externally before completion and do not replace that observed
matrix result. The verifier's final cleanup removed the interrupted fixtures;
`results/` was absent at handoff.

**Closure condition:** make direct execution use the same single module/cache
and cleanup ownership as package execution, and make generated fixture
lifetimes unable to remove a directory another live check is writing or
reopening. Re-run the complete matrix from a clean absent `results/` root and
require every non-deliberate invocation to exit 0.

### P2 — The live-prose detector is still spelling- and construction-sensitive

The actual round-10 live prose is correct, but the claimed detector is not the
whitespace-tolerant semantic guard requested in round 9. Its regexes use
literal spaces and `_validate_current_facts` uses exact substring equality.
Exact controls show all of these stale user-facing forms evade detection:

```text
the production numerical\nbudget belongs to a later ticket and does not exist yet
no production numerical\nbudget exists yet
tickets 07 and 08 own the\nproduction numerical budget and it does not exist yet
```

An f-string such as `f"no production numerical {stage} exists yet"` is split
by the AST scan into literal pieces and is not recognized as the stale runtime
sentence. The current suite's 15 exact mutations pass because they mutate the
same literal spellings the validator stores; they do not exercise line wraps
or dynamic construction.

**Closure condition:** normalize whitespace and evaluate/join safe literal
segments for the user-facing surfaces, or use a token/semantic predicate that
does not depend on exact source formatting. Add line-wrapped, f-string/help,
docstring/banner and newly discovered module controls through the same live
validator.

Round 10 should not be marked closed until the fixture-origin escape and the
direct command lifecycle failure are fixed and independently replayed. The
prose-detector hardening should accompany that closure because it is part of
the declared Ticket-07 current-fact contract.

## Fix-up round 10 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 10 closes all three round-9 findings on their exact reproductions.  The
production proposal and checkpoint now require the one canonical 64-clock,
six-cell, `dt=0.001953125` pilot plan; the eight-clock production-purpose
replay is refused.  The real deterministic four-cell post-range snapshot
reproduces arm counts 8,419 / 22,211 / 8,419, reports
`no_powered_matrix`, and is refused beside the pre-pilot target and matrix
with the named `post_range_matrix_not_derived` reason.  Live package prose now
states that Ticket 07's production numerical budget exists and is not met.

Ticket 07 is nevertheless not closed.  A separate pre-pilot authority join is
missing: the proposal verifies the target/power digest and matrix/power arm
counts but never verifies that the matrix's coupling nodes are the target's
nodes or the canonical pilot plan's nodes.  An honestly resource-priced matrix
over a different six-node grid therefore reaches the proposal, authoritative
rebuild and checkpoint while the same record carries the old target and
canonical pilot candidate grid.  The checkpoint presentation also omits the
explicit statement requested for this boundary: Ticket 08 derivation has not
begun.

No pilot, numerical-validation campaign, production run, Ticket 08 work,
physical fit, exponent result or production-status state is authorized by this
review.

### P1 — The pre-pilot proposal can freeze a matrix over a different coupling grid than its target and canonical pilot

`proposed_production_manifest` checks that `power.target_digest` equals the
supplied target digest, that resources name the supplied matrix digest, and
that matrix arm counts equal the power counts (`experiments.py:5978-6001`).
It never joins `matrix.couplings` to `target.couplings` or `plan.couplings`.
The body then serializes the matrix nodes as `peak_couplings`
(`experiments.py:6017`) and the canonical plan's nodes separately as
`pilot_candidate_couplings` (`experiments.py:6090-6092`).

Exact frozen-environment reproduction:

```text
target / canonical pilot first coupling: 0.5
altered matrix first coupling:            0.55
matrix nodes:                              every target node multiplied by 1.1
resource record:                           built by matrix_resource_estimate
proposal factory:                          ACCEPTED
proposal peak_couplings[0]:                0.55
proposal pilot_candidate_couplings[0]:     0.5
proposal sampling_target_digest:           the unchanged 0.5...2.0 target
authoritative proposal rebuild:            ACCEPTED
checkpoint_one_handoff:                    ACCEPTED
```

The altered matrix remained a valid finite six-node matrix, kept the same
three arm counts, and used its own honestly constructed resource estimate; no
resource digest was forged in the stronger reproduction.  The earlier
reproduction additionally showed the authoritative rebuild and checkpoint
accepting the same split story.  This is the same class of defect round 9
closed after a post-range selection, reachable before a pilot: one proposal
contains two different answers to which coupling grid it freezes.

`require_authoritative_proposal` cannot repair the omission because it rebuilds
from the same mutually inconsistent components (`experiments.py:6144-6159`).
The checkpoint passes those components straight back through that rebuild
(`experiments.py:6643-6658`).

**Closure condition:** at proposal construction and authoritative rebuild,
require exact equality among the provisional target nodes, matrix nodes and
canonical pilot candidate nodes, including order and binary64 values.  Join
the remaining shared physical fields that the proposal presents as one design
(`clocks`, timestep, pulse duration/centre, diffusion, lock tolerance and
dwell) or derive the matrix from one authoritative frozen design record.
Add the exact honestly resource-priced 1.1x-grid reproduction as a must-refuse
test at the proposal, rebuild and checkpoint.  Keep the current valid
0.5...2.0 pre-pilot proposal as the positive control.

### P2 — The checkpoint presentation does not explicitly say Ticket 08 derivation has not begun

The implementation comments correctly say that coherent post-range target,
matrix and resource derivation belongs to Ticket 08 and is not performed here
(`experiments.py:5963-5967`).  That fact does not reach the checkpoint
presentation.

The actual `requested_decision` says only that no pilot has run, no forbidden
pilot output has been opened and no production manifest has been signed
(`verify.py:27839-27843`).  `Checkpoint1Handoff.summary()` has no Ticket-08 or
post-range-derivation field (`experiments.py:6556-6604`), and the README
checkpoint section likewise omits the statement.  Independent inspection of
the built handoff reproduced:

```text
"ticket 08" in requested_decision: false
Ticket-08/post-range derivation key in summary: false
```

This is a bounded presentation finding, not evidence that Ticket 08 ran:
Ticket 08 remains status 0 with its prior artifact hash, and no Ticket-08
output exists.

**Closure condition:** make the checkpoint's presented text explicitly say
that Ticket 08 derivation has not begun.  Prefer also a derived closed-valued
summary field such as `post_range_matrix_status="not_derived_ticket_08_not_started"`
so the statement is carried structurally rather than only as free prose.  Pin
the exact phrase/field in the current-fact guard and README checkpoint section.

### Closed round-9 replays and preserved boundary

- `PRODUCTION_PILOT_SPEC` and `canonical_pilot_plan` reproduce exactly 64
clocks, six cells, `dt=0.001953125`, 200 pilot trials per cell and the frozen
source/environment/schema/firewall inputs.  An eight-clock, `dt=0.05`,
four-cell plan declaring `approved_production_pilot` is refused by
`require_canonical_pilot_plan` and cannot drive a proposal.
- The real four-cell fixture snapshot reports `post_range_join`, 4 cells,
arm trials `{'full': 8419, 'central_control': 22211, 'width_only_control': 8419}` and `no_powered_matrix`; 22,211 exceeds the
frozen 20,000 ceiling.  `_require_post_range_design` refuses it beside the
pre-pilot target/matrix and names `post_range_matrix_not_derived`.
- The valid pre-pilot six-cell proposal remains constructible and blocked.  No
post-range production proposal was found or constructed during review.
- Exact run/coupling identity and order, ordered closure alignment, direct
quarantine lifecycle, five-file closure, full-manifest plan reconstruction,
production-reader exclusion, count-only projection and pulse-centre
propagation remain green.
- Option A remains unpriced and non-sufficient.  Option B remains exactly 18
runs / 29,268 rows / about 12.78 MB and supports machinery/diagnostics only.
- The numerical record remains 17 non-intended evidence rows and 12 declared
search options: probability `nmax=35` against 2,406 paired full-arm trials,
time bounds fail at every count, the moving-band verdict remains literal
`numerical_no_result`, and the conclusion is only
`no_feasible_matrix_among_searched`.
- Live prose across the discovered 22-source set states that Ticket 07 froze a
production numerical budget and that it is **not met**.  The truthful claim
that production-status schema v4 does not exist remains distinct.
- Manifest schema 3 remains below production-status schema 4, so Ticket 06's
physical permission remains unreachable.  Ticket 08 is status 0 and its
artifact hash remains
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

### Independent verification and cleanup

All final command results below are from strictly serial Miniconda Python
3.13.11 / NumPy 2.4.3 runs.  Earlier attempts overlapped a separate retry
harness in the shared results directory and failed with disappearing-fixture
digest/close-marker errors; those interference results were discarded, the
retry processes were stopped, the fixture root was cleared, and the full
matrix was rerun alone.

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected check failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite reports 525 public callables, 1,378 invalid calls, 1,271 parameters
and all 121 acceptance criteria.  Raw isolation, Ticket-05 regression,
analysis read-only behavior, API census, documentation, warning discipline and
cleanup passed.  `results/` is absent after the final matrix and both focused
reproductions.  No implementation file, ticket status, Git entry or unrelated
file was edited; only this review section was appended.

Final frozen hashes remain:

```text
experiments.py 1baf7013c3d10d4a2f3050ef3b9b0d948fa4ff9e8b5e90a9bda9a05fcd12f672
verify.py      494aae89c4fee77e89cc4564a9668eeaaa1ddd3d9d2442265e8a9ed83e5dcbb3
README.md      3a99c991b1c430789c6899a186e1b5daa7046351a513dedce4cf36ca27507868
compare.py     abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py    9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
```

Do not present the current proposal/checkpoint as an authoritative production
freeze and do not authorize the pilot.  Round 10's post-range and canonical
plan fixes are correct, but the pre-pilot matrix/target/plan grid join and the
explicit Ticket-08-not-started checkpoint wording require a bounded fix and a
fresh independent review.

## Fix-up round 11 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 11 closes the shared-physics defect.  The sampling target, primary
matrix and canonical pilot plan now pass through one 16-field identity table,
and the exact honestly resource-priced 1.1x coupling-grid reproduction is
refused at proposal construction, authoritative rebuild and checkpoint.  Each
refusal names `peak_couplings`; the coherent pre-pilot record still passes.

The canonical checkpoint now also presents the requested Ticket-08 boundary:
its derived `ticket_08_derivation_status` is `not_started`, its summary carries
`post_range_production_proposal: None`, and both its requested decision and the
README explicitly say that derivation has not begun and is not authorized.

One bounded presentation authority gap remains.  `checkpoint_one_handoff`
still accepts `requested_decision` from its caller and neither the factory nor
`Checkpoint1Handoff.__post_init__` requires the two Ticket-08 statements.  A
fully coherent authoritative checkpoint therefore still constructs with
`requested_decision='approve the presented choice'`.  Its structural status is
truthful and its post-range proposal field is `None`, but the checkpoint text
the caller presents omits exactly the facts this round was required to make
explicit.  The current-fact table requires the README's not-started sentence,
but does not pin the non-authorization sentence and does not make the public
checkpoint boundary refuse an omission.

No pilot, campaign, production run, Ticket 08 work, physical fit, exponent
result or production-status state is authorized by this review.

### P2 — A coherent public checkpoint can omit the required Ticket-08 presentation

The canonical handoff is correct at `verify.py:27865-27882`.  The production
factory, however, exposes `requested_decision` as a parameter
(`experiments.py:6768-6770`) and passes it unchanged into the record
(`experiments.py:6831-6844`).  The record validates only that it is non-empty
bounded text (`experiments.py:6671-6673`).

Exact frozen-environment reproduction using the canonical target, matrix,
power, recovery, disposition, search, resources, firewall, proposal, pilot
plan, campaign and measured benchmarks:

```text
checkpoint_one_handoff(requested_decision="approve the presented choice")
result:                                  ACCEPTED
returned requested_decision:             "approve the presented choice"
ticket_08_derivation_status:              "not_started"
summary.post_range_production_proposal:   None
required Ticket-08 wording in text:       absent
```

The verifier inspects the one `_t07_handoff()` instance for the not-started
phrase (`verify.py:29963-29967`), but this does not constrain another valid
public handoff.  Its authorization check is conditional: if the word
`authorized` is absent, the omission passes (`verify.py:29968-29970`).  The
unified fact table pins the not-started and no-proposal sentences only at
`README.md` (`verify.py:30132-30137`) and has no current non-authorization
fact.  Thus the current frozen presentation is truthful, but the boundary that
creates checkpoint presentations does not make that truth invariant.

**Closure condition:** derive the requested-decision text at
`checkpoint_one_handoff`, or validate at construction that it explicitly says
there is no post-range production proposal, Ticket 08 derivation has not
begun, and Ticket 08 is not authorized.  Add the exact omission reproduction
above as a must-refuse test.  Pin the non-authorization phrase in the unified
current-fact table and mutate it away as a negative control.  Keep the current
canonical handoff as the positive control.

### Closed shared-physics finding

`SHARED_PHYSICAL_FIELDS` and `shared_physical_identity`
(`experiments.py:5401-5482`) cover the 16 meaningful overlaps: exact ordered
couplings and cells; clock grid and support; timestep; pulse duration and
centre; diffusion, lock band and dwell; shadow fraction; arm names and clock
counts; pilot arm; and reference-rate control arms.  The factory invokes the
guard before deriving proposal fields (`experiments.py:6062-6066`).

Independent probes changed each of the 16 declared identities.  Every variant
was refused with its expected field named, including reordered arms, a changed
arm clock, a changed reference-rate arm, a changed pilot arm and the exact
1.1x coupling grid.  Raw dataclass-field inspection found two same-named
non-overlaps that correctly are not equated: record labels are metadata, and
the 200-trial range pilot is intentionally distinct from the 2,406-trial full
production arm.  Grid spacing, parity, origin and window fields are derived
from already-compared inputs and the canonical-plan rebuild.  The coherent
record returned the original target and produced design digest
`4da165f3c294c07b...`; the canonical plan digest is
`296fff87710da4a6...`.

The exact 1.1x matrix used its own honest `matrix_resource_estimate`.  All
three doors raised `ValueError` naming `peak_couplings`; none reached a second
serialized coupling grid.

### Preserved fail-closed and scientific boundary

- The canonical production pilot remains exactly 64 clocks, six cells,
`dt=0.001953125`, 200 trials per cell and purpose
`approved_production_pilot`.  Smaller deterministic plans remain fixtures.
- The real four-cell count-only replay returned post-range arm counts
8,419 / 22,211 / 8,419, verdict `no_powered_matrix` and status
`post_range_no_powered_matrix`.  The central arm exceeds the 20,000 ceiling.
`_require_post_range_design` refused it beside the pre-pilot six-cell design
and named `post_range_matrix_not_derived`; no post-range proposal exists.
- The numerical evidence remains 17 rows, all `non_intended`, over 12 declared
options.  The probability window admits at most 35 trials against 2,406
paired full-arm trials; time is inadmissible at every count, the moving-band
result is `numerical_no_result`, and the search conclusion remains only
`no_feasible_matrix_among_searched`.
- The Ticket-07 budget exists and is not met, with all six blockers preserved.
Production-status schema v4 remains separately absent and schema v3 remains
fail closed.
- Option A remains unpriced (`cost=None`).  Option B remains exactly 18 runs,
29,268 rows and 12,784,450.43 bytes, with support class
`machinery_and_diagnostic_only`.
- Exact run/coupling order, closure alignment, direct quarantine, five-file
closure, count-only projection, pulse-centre propagation and the prior
authority/firewall checks remain green.  No pilot, validation campaign or
Ticket-08 activity occurred.
- Ticket 08 remains status 0 at independent artifact hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

### Independent serial verification and cleanup

All verifier paths ran strictly one at a time under Miniconda Python 3.13.11
and NumPy 2.4.3.  No other verifier was active.

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected check failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

An initial reviewer `py_compile` command mistakenly named a nonexistent
`fixed_point.py`; that invocation was discarded and the actual package glob
above passed.  Python bytecode was redirected to a temporary cache and
removed.  `results/` is absent after every final verifier path and after the
focused fixture replays.  No implementation file, ticket status, Git entry or
unrelated file was edited; only this review section was appended.

Final frozen hashes remain:

```text
experiments.py fd688b5c23b6f28c9f66d99dcd972f1c66d017527544459e5a47dc0001689b92
verify.py      0e8c9ddc4a6f411fc0d68b735171576779b69158b0ec512e679be29576e3eeed
README.md      b8fe328eb12cfdfa716d254368618dd467ace6589d4fe0a18fa6d42cd64da16d
compare.py     abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py    9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
```

Do not authorize the pilot or present an arbitrary public handoff as the
Ticket-07 checkpoint.  The scientific and production-design boundaries are
closed; the required Ticket-08 status is truthful in the canonical record but
must still be made unavoidable at the checkpoint presentation boundary.

## Fix-up round 12 independent closure re-review — 2026-08-29

### Strict verdict: OPEN

Round 12 closes the round-11 caller-text defect on every exact reproduction.
`checkpoint_one_handoff` has no `requested_decision` parameter, derives the
one canonical text, and returns a handoff whose text contains all three
required clauses.  Direct `Checkpoint1Handoff` construction refuses the
review's `"approve the presented choice"`, removal of each clause separately,
removal of the non-authorization tail, and even an otherwise canonical string
with extra text.  README and the unified current-fact guard now carry and pin
the three prose facts.

One bounded presentation finding remains against the explicit round-12
requirement that the **summary** carry those same three facts.
`Checkpoint1Handoff.summary()` carries
`ticket_08_derivation_status="not_started"` and
`post_range_production_proposal=None`, but it has no authorization field.  The
source comment says this is not authorization; a consumer of the returned
summary cannot observe that comment.  The verifier likewise checks only the
two present summary values.  The canonical requested-decision text and README
are truthful, but the summary surface is two facts out of three.

No pilot, validation campaign, production run, Ticket 08 work, physical fit,
exponent result or production-status state is authorized by this review.

### P2 — The checkpoint summary omits the Ticket-08 non-authorization fact

The returned summary mapping at `experiments.py:6798-6808` contains exactly
these Ticket-08/post-range keys:

```text
ticket_08_derivation_status          "not_started"
post_range_production_proposal       None
```

Independent AST inspection of the actual `summary()` dictionary reproduced:

```text
summary_ticket_keys ['ticket_08_derivation_status',
                     'post_range_production_proposal']
summary_has_authorization_fact False
```

There is no `ticket_08_authorized=False`,
`ticket_08_authorization_status="not_authorized"`, or equivalent closed field.
The adjacent comment at `experiments.py:6799-6803` does not enter the returned
mapping.  Correspondingly, the checkpoint verifier asserts the not-started
status and absent post-range proposal at `verify.py:29936-29945` but makes no
summary assertion for non-authorization.

README is correct and the current-fact table now includes all three text facts,
including `("ticket 08 non-authorization", "Ticket 08 is not authorized", ...)`
at `verify.py:30154-30162`.  Independent in-memory mutations of the README's
not-started, no-proposal and non-authorization spellings were all caught.  That
does not add the missing fact to `Checkpoint1Handoff.summary()`.

**Closure condition:** add a derived, closed-valued summary field such as
`ticket_08_authorized=False` or
`ticket_08_authorization_status="not_authorized"`.  Assert that exact value in
the checkpoint check, and add a negative control proving a summary with an
authorized/omitted state cannot be presented.  Keep the canonical decision
text and the three current-fact mutations as positive coverage.

### Closed round-11 presentation finding

- `inspect.signature(checkpoint_one_handoff)` has no
`requested_decision` parameter.
- The factory assigns `CHECKPOINT_REQUESTED_DECISION` directly
(`experiments.py:6875-6889`).
- The canonical handoff's text equals that constant exactly and contains:
`There is no post-range production proposal.`,
`Ticket 08 matrix derivation has not begun.`, and
`Ticket 08 is not authorized.`
- The original replacement text and each one-clause omission raised
`ValueError` naming the non-canonical presentation.  A removed
non-authorization tail and an added suffix were also refused.
- The structural handoff status and summary status are both `not_started`, and
`post_range_production_proposal` is `None`.
- The frozen proposal design digest is `aa321492bdef87d7...`; the canonical
pilot plan digest on this run is `f862353844fefc71...`.

### Preserved shared-physics, post-range and scientific boundary

- The coherent target/matrix/plan identity passes.  All 16 declared shared
physical fields were changed independently and every change was refused with
its field named.
- The exact honestly resource-priced 1.1x coupling matrix is refused at
proposal construction, authoritative rebuild and checkpoint, each naming
`peak_couplings`.
- The canonical production pilot remains 64 clocks, six cells,
`dt=0.001953125`, 200 trials per cell and
`approved_production_pilot`.  Smaller deterministic plans remain fixtures.
- The actual four-cell count-only replay remains 8,419 / 22,211 / 8,419,
`no_powered_matrix` and `post_range_no_powered_matrix`; 22,211 exceeds the
frozen 20,000 ceiling.  `_require_post_range_design` refuses it beside the
pre-pilot design and names `post_range_matrix_not_derived`.  No post-range
production proposal exists.
- The numerical evidence remains 17 `non_intended` rows and 12 declared
options, probability `nmax=35` against 2,406 paired full-arm trials, time
inadmissible at every count, moving-band `numerical_no_result`, and only
`no_feasible_matrix_among_searched`.
- The Ticket-07 budget exists and is not met, with the same six blockers.
Production-status schema v4 remains separately absent and schema v3 remains
fail closed.
- Option A remains unpriced.  Option B remains exactly 18 runs, 29,268 rows,
12,784,450.43 bytes and `machinery_and_diagnostic_only`.
- Exact run/coupling order, closure alignment, direct quarantine, five-file
closure, count-only projection, pulse-centre propagation and the established
firewall/authority checks remain green.  No pilot, campaign or Ticket-08
activity occurred.
- Ticket 08 remains independently status 0 at artifact hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

### Independent serial verification and cleanup

All paths ran strictly one at a time under Miniconda Python 3.13.11 and NumPy
2.4.3; no other verifier was active.

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected check failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent after every invocation and after all focused probes.
Bytecode was redirected to a temporary cache and removed.  No implementation
file, ticket status, Git entry or unrelated file was edited; only this review
section was appended.

Final frozen hashes remain:

```text
experiments.py 61d85c0d56c0ae72ce3aa61bbd464ff2b4ba5d28def02b076840be3ee923ad88
verify.py      e4b3a300fd0b2b3f30b11dc81bf83c2eca16686ca2815bdef24182969983fe6b
README.md      022149ddef1b4ac620f181d9f68a32f3a9931e6da460ce83104e74ccce1854c9
compare.py     abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py    9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py  eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
```

Do not authorize the pilot.  Round 12 closes the caller-controlled checkpoint
text, and every production/scientific boundary remains fail closed, but the
summary must expose the third Ticket-08 fact before this exact review contract
is closed.

## Fix-up round 13 final independent closure review — 2026-08-29

### Strict verdict: CLOSED

No actionable finding survives round 13.  The sole round-12 gap is closed:
`Checkpoint1Handoff` now carries the derived authorization status
`not_authorized` under a one-member vocabulary, the production factory has no
parameter for it, the digest binds it, and `summary()` exposes it beside the
derived `not_started` status and `post_range_production_proposal=None`.
Alternate authorization strings and non-string values refuse, the exact valid
value survives, and the README/current-fact machinery pins both the prose and
structured spellings.

This is closure of Ticket 07's review contract at its accepted boundary.  It
does **not** authorize the pilot, a validation campaign, production, Ticket 08,
a physical fit, an exponent result or a production-status state.  No
post-range production proposal exists; Ticket 08 matrix derivation has not
begun; Ticket 08 is not authorized.

### Closed round-12 summary finding

The authorization vocabulary is exactly:

```text
TICKET_08_AUTHORIZATION_STATUSES = ("not_authorized",)
```

The canonical factory signature contains neither
`ticket_08_authorization_status` nor `requested_decision`.  It derives both
from their closed constants.  The independently built handoff and its summary
reported:

```text
handoff.ticket_08_derivation_status          not_started
handoff.ticket_08_authorization_status       not_authorized
summary.ticket_08_derivation_status          not_started
summary.ticket_08_authorization_status       not_authorized
summary.post_range_production_proposal       None
```

The canonical decision text equals `CHECKPOINT_REQUESTED_DECISION` exactly and
contains all three clauses:

1. `There is no post-range production proposal.`
2. `Ticket 08 matrix derivation has not begun.`
3. `Ticket 08 is not authorized.`

Direct frozen-record variants with `authorized`, `AUTHORIZED`, `not_started`,
`conditionally_authorized`, the empty string, `None`, booleans, integers and
an arbitrary object all refused with the expected `ValueError` or `TypeError`.
Replacing the value with the sole valid `not_authorized` member reproduced the
same summary and digest.

The unified current-fact guard now pins four distinct facts: derivation not
started, post-range proposal absent, prose non-authorization, and the
structured `ticket_08_authorization_status = not_authorized` spelling.
Independent in-memory mutations of all four were caught; the unmodified live
source set returned no current-fact problem.  README presents both one-member
statuses and the null post-range proposal explicitly.

Ticket 08 remains independent evidence rather than a field asserting its own
truth: its ticket artifact is still status 0 at hash
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

### Preserved shared-physics, post-range and scientific boundary

- The proposal design digest is `ee530c06191e9792...`; the canonical pilot
plan digest independently observed here is `555fbd417a8418dd...`.
- The coherent target/matrix/plan identity passes.  All 16 declared shared
physical fields were changed independently and every mismatch refused with
its field named.
- The exact honestly resource-priced 1.1x coupling matrix refuses at proposal
construction, authoritative rebuild and checkpoint, each naming
`peak_couplings`.
- The canonical production pilot remains 64 clocks, six cells,
`dt=0.001953125`, 200 trials per cell and purpose
`approved_production_pilot`.  Smaller deterministic plans remain fixtures.
- The actual four-cell count-only replay remains 8,419 / 22,211 / 8,419,
`no_powered_matrix` and `post_range_no_powered_matrix`; the central count
22,211 exceeds the frozen 20,000 ceiling.  `_require_post_range_design`
refuses it beside the pre-pilot design and names
`post_range_matrix_not_derived`.  No post-range production proposal exists.
- Numerical evidence remains 17 `non_intended` rows and 12 declared options,
probability `nmax=35` against 2,406 paired full-arm trials, time inadmissible
at every count, moving-band `numerical_no_result`, and only
`no_feasible_matrix_among_searched`.
- The Ticket-07 numerical budget exists and is not met, with the same six
blockers.  Production-status schema v4 remains separately absent and schema
v3 remains fail closed.
- Option A remains unpriced.  Option B remains exactly 18 runs, 29,268 rows,
12,784,450.43 bytes and `machinery_and_diagnostic_only`.
- Exact run/coupling order, ordered closure alignment, direct quarantine,
five-file closure, count-only projection, pulse-centre propagation and the
established authority/firewall checks remain green.  No pilot, campaign or
Ticket-08 activity occurred.

### Independent quiet serial matrix and cleanup

Every path ran strictly one at a time under Miniconda Python 3.13.11 and NumPy
2.4.3.  No other verifier was active.

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected check failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent after every invocation and after all focused probes.
Bytecode was redirected to a temporary cache and removed.  No implementation
file, ticket status, Git entry or unrelated file was edited; only this review
section was appended.  No artifact comment is open.

Final frozen hashes remain:

```text
experiments.py c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e
verify.py      bb2b8dd07cea6b3a8c82644d189e2d468604fc758863af2540af0f3e218554ff
README.md      4f48a3140574e1014301536cb6e8e8e56647f2f2b2858613037e69595c22c521
compare.py     abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py    9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py  b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py  eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
```

Ticket 07 is strictly closed at the fail-closed pre-pilot boundary.  A later
decision to authorize anything remains outside this review and requires the
separate authority already documented by the ticket sequence.

## Reconstruction baseline R1 independent review — 2026-08-29

### Strict verdict: OPEN

The executable Ticket-01–07 baseline is substantially intact, but the
reconstruction is not review-clean.  Three actionable findings survive.  The
first is itself enough to keep the baseline open: the live README presents
subtracted, unauthorized Ticket-08 work as implemented, and every prose guard
passes over that false claim.

### Findings

#### [P1] Live README still presents the subtracted Ticket-08 gate as implemented

`README.md:1683-1691` says that the “final seven” checks are the Ticket-08
production gate, then enumerates those seven checks.  `README.md:3792` says the
Ticket-08 production gate and its closed no-result are implemented in
`production.py` and gives that absent gate the verdict `numerical_no_result`.
Both statements are false in this reconstruction:

- only 127 checks are registered, acceptance criteria stop at 121, and no
Ticket-08 check or API row remains;
- `production.py` is absent and
`find_spec("adler_born_two_channel.production")` returns `None`;
- the Ticket-08 artifact is still status 0 at its original hash and has no
execution/review child artifact in the active tree.

This is not merely stale prose that the guards catch.  `_live_prose_sources()`
does include `README.md`, but `_t07_current_facts()` has no fact for the absence
of an implemented Ticket-08 gate or its seven checks.  On the exact candidate
bytes, `_validate_current_facts(...)`, `check_readme()` and
`check_stale_stage_strings()` all return clean.  The two false statements must
be removed or corrected, and the no-Ticket-08-implementation boundary must be
pinned so the same residue cannot pass again.

The subtraction also left a bounded source residue at `verify.py:94-99`: a
comment says the verifier takes an unsupported route into Ticket-08
`production` records under a named seal, but the import and seal are gone.  It
does not execute and is excluded from the verifier's live-output scan, but it
should be removed with the false README presentation.

#### [P1] Criteria 110 and 118 can be certified without satisfying their text

The criterion registry and its covering checks no longer agree semantically:

- criterion 118 (`verify.py:452-455`) still requires “both costed
alternatives,” while the accepted Ticket-07 boundary, `experiments.py`, the
covering check at `verify.py:29774-30089`, and the README all require Option A
to be explicitly **unpriced** and Option B to be the one priced,
machinery-only diagnostic;
- criterion 110 (`verify.py:415-417`) says every closed status/verdict/blocker
vocabulary is enforced, including the production gate by name.  In a fresh
process, appending `review_rogue_verdict` to
`FEASIBILITY_VERDICTS` still leaves `check_experiments_isolation()` passing.

`check_coverage()` also passes, because it checks only that the integer IDs
1–121 appear in `covers` and that check names are unique.  It cannot detect
either semantic contradiction.  Correct criterion 118 to the one-unpriced,
one-priced contract and strengthen criterion 110's covering check to pin every
closed vocabulary it claims, rather than selected bad spellings.

#### [P2] The live budget-ownership guard misses a Ticket-08 co-ownership paraphrase

`raw_runner.py:192-193`, which `_live_prose_sources()` scans, still says “the
production numerical budget, which tickets 07 and 08 own.”  The accepted fact
is that Ticket 07 froze the budget and it is not met; Ticket 08 is status 0,
has not begun matrix derivation and is not authorized.

The guard misses this because its stale pattern at `verify.py:30462` recognizes
only “production numerical budget ... belongs to tickets 07 and 08,” while the
current-fact stale literal at `verify.py:30222-30223` recognizes another exact
line-wrapped spelling.  Both `check_current_facts()` and
`check_stale_stage_strings()` pass on the live co-ownership sentence.  Pin the
ownership fact semantically or include this actual wording; a closed guard must
not depend on one paraphrase of the false claim.

### Preserved executable and scientific boundary

No executable regression was found in the reconstructed Ticket-01–07 surface:

- exact candidate hashes were present before and after review:
`verify.py` `d3249e37bef73257a91005e20969155c0235d3303efed7aa1a39f8ab61feace3`,
`README.md` `bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55`,
and unchanged `experiments.py`
`c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e`;
- criteria are exactly 1–121, each criterion 110–121 has one registered
covering check, and the API table has 527 rows against 526 exported-surface
entries with no missing entry or duplicate; its sole extra row is the
explicitly tested `experiments.quarantine_pilot_run`;
- README's computed census remains 127 checks, 527 table rows, 1,383 invalid
calls and 1,278 parameters; the full suite independently accepts those
computed joins;
- the raw graph still forbids `production` and all comparison/oracle layers,
retains its authorized allowlist and required modules, and no active source
imports Ticket-08 machinery;
- the Ticket-07 numerical no-result, finite search, post-range fail-closed
boundary, Option A/B contract, scientific residual checks, schema-v3 gate and
explicit non-claims all execute and pass.  No pilot, campaign, production,
sensitivity or Ticket-08 activity occurred.

### Quiet serial matrix, cleanup and frozen boundary

No other verifier was active.  Every command ran strictly after the preceding
one completed:

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only the injected probe failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent after every path and at final inspection.  Bytecode for
this review was redirected to a temporary cache and removed.  Ticket 08 remains
status 0 at SHA-256
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`;
`production.py` and active Ticket-08 execution/review artifacts remain absent.
`hologram_phase_test/` was not read, edited or otherwise touched.  No
implementation file, ticket status or Git state was modified; only this review
section was appended.

R1 is therefore **OPEN**.  The green 127-check matrix is evidence that the
Ticket-01–07 executable baseline survived subtraction, but it is also exact
evidence that the current prose and coverage guards do not detect the three
findings above.

## Addendum to the 2026-08-30 round-10 re-review — concurrency qualification

The `P1 — required direct/warnings verifier matrix is not green` subsection in
the 2026-08-30 round-10 review is **withdrawn as an intrinsic round-10**
**finding**. A final scope check showed that another review/implementation stream
was active after that frozen-byte review and that the shared verifier fixture
names were being used across processes. The observed missing/changed
`verify-t6full-0002` directory and close-marker disappearance therefore prove
a cross-process fixed-name collision, but do not prove that a quiet serial run
of the requested frozen bytes fails. The interrupted retry processes cannot
resolve that ambiguity. Do not use those failures as a Ticket-07 closure
blocker without a truly exclusive serial replay.

This qualification does **not** change the strict round-10 verdict. The
fixture-origin authority escape was reproduced end to end without relying on
the command-matrix collision: a polymorphic fixture plan wrote canonical
reserved closures, the genuine canonical base plan recounted them, and
proposal, authoritative rebuild and checkpoint accepted the resulting
`post_range_powered` snapshot. The live-prose detector weakness is likewise a
separate static reproduction.

The requested round-10 hashes matched before and after those adversarial
reproductions. After the round-10 section was appended, the current workspace
advanced to later implementation hashes (`experiments.py`
`c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e`,
`verify.py` `d3249e37bef73257a91005e20969155c0235d3303efed7aa1a39f8ab61feace3`,
`README.md` `bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55`).
Those later bytes are outside this round-10 verdict.

## Fixture-origin closure independent review — 2026-08-30

### Strict scoped verdict: OPEN

The normal deterministic fixture remains internally valid, the eleven existing
must-refuse cases are meaningful, the one-snapshot change is present, and every
documented serial verifier/compile path is green and cleans up.  Production
scientific modules are byte-identical to the frozen reconstruction baseline.

One actionable authority defect survives, however.  The new door validates the
declared fields and digest of an exact-type `PilotPlan`, but it does not validate
the instance behavior the writer invokes after that check.  A shadowed
exact-type fixture plan can therefore pass the door and write an eight-clock,
`dt = 0.05` fixture closure under the approved production pilot's reserved
`xpilot-t07-cell-0` identity.  That violates both requested guarantees that
fixture and production identities remain separate and that an invalid plan is
refused before output is created.  This narrow fixture-origin change remains
OPEN.

The separate reconstruction-baseline R1 verdict also remains **OPEN**.  Its
three pre-existing documentation/criteria findings are untouched and still
independently present; none is reclassified by this fixture review.

### P1 — An exact-type plan can shadow the methods used after validation

`PilotPlan` is a frozen dataclass, but it is not slotted
(`experiments.py:4119-4120`).  It therefore has an instance dictionary, and
`object.__setattr__` can attach instance attributes named like its non-data
descriptor methods.  This is within the codebase's own mutation model: the
regression itself uses `object.__setattr__`, and the raw configuration boundary
explicitly treats frozen records as mutable through that mechanism.

`_t07_require_fixture_plan` checks exact type, purpose, marker, authoritative
rebuild, every declared dataclass field, digest, and the ordinary `run_names`
property (`verify.py:27515-27550`).  None of those checks rejects extra instance
state.  After the door returns, `_t07_write_fixture_cell` dynamically dispatches
`plan.require_run_name`, `plan.coupling_for`, and `plan.config_for`
(`verify.py:27677-27691`), while `_t07_pilot_fixture` dynamically dispatches
`plan.run_name_for` (`verify.py:27754-27759`).  Those are precisely the names an
exact-type instance can shadow.

The no-write focused probe reproduced the gap without changing a declared field
or the fixture digest:

```text
identity_door_accepted_shadowed_exact_type  True
accepted_reserved_cell_name                xpilot-t07-cell-0
reserved_mapping_matches                   True
snapshot_matches_production                True
fixture_digest_unchanged                    True
results before/after                        absent / absent
```

A bounded write-level probe then shadowed only `require_run_name` and
`coupling_for`, kept the honest fixture `config_for`, and called the real
per-cell helper.  It produced:

```text
identity_door_accepted_shadowed_exact_type  True
written_reserved_production_name            xpilot-t07-cell-0
reserved_directory_exists                   True
written manifest clocks                     8
written manifest timestep                   0.05
results after finally                       absent
```

This is not a claim that the canonical production recount accepts that fixture
manifest: its physics still differ, and the authoritative manifest check should
refuse it.  The scoped closure is conjunctive, though.  It explicitly promises
that a fixture cannot occupy a production identity and that a refused plan
creates no output; this exact-type plan defeats both promises before the later
recount is relevant.

The existing eleven attacks remain useful: they cover the canonical plan, two
stateful subclasses, a sealed relabel, `dataclasses.replace`, a second honest
fixture plan, direct per-cell misuse, reserved/unmarked names, and a coupling
swap.  They miss this case because exact type is treated as equivalent to class
behavior even though the object can carry method-shadowing instance state.

**Bounded fix:** after comparing the supplied record, continue exclusively with
the freshly built expected fixture plan and never invoke the caller object
again.  Concretely, have `_t07_require_fixture_plan` return that fresh expected
record and assign its return value in both writers.  Alternatively reject every
unexpected instance-dictionary key and invoke the `PilotPlan` implementations
through the class.  Add a regression that shadows each dynamically used method,
requires refusal before `results/` exists, and retains the present positive
fixture control.

### Preserved behavior and verification

- The cold read confirms one call to `config_for` per cell, with that single
`config` object supplying both the twelve-trial source replacement and the
cloned cell manifest.  The former two-call split-brain is gone.
- Direct invocation of `check_range_selection()` passed with residual `0.0`.
Its positive fixture remained authoritative under its own plan, selected all
four declared cells, stayed non-authoritative under the production plan, and
the process removed its generated output.
- No package module imports `verify.py`.  `experiments.py`, `README.md`,
`compare.py`, `__init__.py`, `raw_runner.py`, and `raw_config.py` remain at
their frozen R1 hashes, so the scientific production surface is unchanged by
this verifier-only edit.
- Ticket 08 remains status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`,
and `production.py` remains absent.

Quiet serial matrix under Python 3.13.11 / NumPy 2.4.3:

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly the deliberate probe failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent after every matrix path and after both focused probes.
Bytecode and captured verifier output lived only under a temporary `/tmp`
directory removed by the matrix's exit trap.  No source, ticket status, Git
entry, or unrelated file was edited; only this review section was appended.

Post-review frozen hashes:

```text
verify.py               8bde04e60f358db63905cf5cb305d71ab276b3a8806f2ba43f03e5f8ec2670c7
experiments.py          c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e
README.md               bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55
compare.py              abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py             9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py           b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py           eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
execution-notes/index.md 35a65a231a62f852f02d1d6d5bfb8b000a6581eaec842c1ab96fc76e650005d9
```

## Fixture-plan instance-behaviour closure review — 2026-08-30

### Strict scoped verdict: CLOSED

No actionable finding survives the cold read or the independent data replay.
The exact-type instance-method-shadowing escape is closed: injected instance
state is rejected before any output exists, the validation door returns a new
factory-built fixture plan, and both writer entry points continue exclusively
with that returned record.  The earlier fixture-origin finding and its
instance-behaviour follow-up are therefore **CLOSED** in this narrow scope.

The separate reconstruction-baseline R1 verdict remains **OPEN**.  Its three
documentation/criteria findings are outside this fix and are neither resolved
nor reclassified here.

### Cold correctness result

- `_t07_require_fixture_plan` first requires the exact `PilotPlan` type and
rejects every instance-dictionary name outside
`PilotPlan.__dataclass_fields__` before reading a plan field.  It then performs
the existing purpose, prefix, authoritative-rebuild, field/digest and
production-reserved-name checks, and returns the local `expected` record
freshly constructed by `_t07_fixture_plan()` rather than the supplied object.
- `_t07_write_fixture_cell` and `_t07_pilot_fixture` both assign that return
value over their `plan` argument before any subsequent name, coupling or
configuration lookup.  No other fixture-writer call site exists.
- The per-cell writer takes exactly one `config_for(coupling)` snapshot.  The
twelve-trial source is a `dataclasses.replace` of that snapshot and the final
manifest is built from the same snapshot.  The finished directory contains
exactly the manifest, three tables and last-written close marker.
- The writer opens the package `results/` directory and the quarantine by file
descriptor and writes its source and cell directly beneath the quarantine.
The normal fixture's names are fixture-marked and disjoint from the canonical
production plan's reserved names.
- No package module imports `verify.py`.  The six production-adjacent files are
byte-identical to the frozen R1 baseline, so this verifier-only change does
not alter production physics or the scientific decision boundary.

### Independent focused replay

The ten frozen inputs matched before any probe.  All data below were temporary
and `adler_born_two_channel/results/` was absent again after each phase.

1. Seven exact-type, fixture-digest-equal inputs were constructed: the previous
three-method case plus individual shadows of `require_run_name`,
`coupling_for`, `config_for`, `run_name_for`, `require_run_names` and
`require_manifest`.  Each was sent through both the whole-fixture and
per-cell entry point: **14/14 refused** from an absent quarantine without
creating `results/`.
2. The same **14/14 refused** beside a pre-existing quarantine.  Its sole
bystander entry and sentinel bytes were unchanged after every call, and
`xpilot-t07-cell-0` was never created.
3. Successful validation returned a distinct exact `PilotPlan` object with the
expected digest
`76c8955f79c2f6b4a8fe393df129268a42debd0135498a109f59dee0b2bdbdcd`,
field-for-field equality and no undeclared instance state.
4. A runtime wiring probe substituted a poison caller and a one-cell returned
record at the validation seam.  The whole-fixture path completed without
consulting the caller; its nested per-cell path used the returned record and
called that record's `config_for` exactly **once**.
5. The real normal fixture wrote its four ordered
`xpilot-t07-fixture-cell-*` cells directly under the quarantine, with exactly
five files in each closure and no cell beside the quarantine.  Its own plan
read and selected all four cells; the canonical production plan refused the
same runs.  Cleanup removed the entire result tree.
6. The frozen scientific boundary rebuilt as
`numerical_no_result`, `no_feasible_matrix_among_searched` and
`checkpoint_blocked`, with contraction rate, selection digest, post-range
digest and post-range status all `None`.  A first reviewer-harness assertion
had expected a synthetic `"not_run"` spelling for that last `None`; the
corrected boundary probe passed and cleaned up.  This was a probe-expectation
correction, not a product failure.

The canonical in-suite regression is broader still: 30 must-refuse attacks are
replayed from both absent and populated quarantine states, for 60 refusal
assertions, followed by the honest fixture positive control.

### Quiet strictly serial matrix and cleanup

One verifier process at a time ran under an exclusive lock on Python 3.13.11 /
NumPy 2.4.3.  The wrapper required `results/` absent before the matrix, after
every invocation and after the matrix.

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0 |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0 |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; the only failure was `deliberate failure probe` |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The registered census remains 127 checks and criteria 1–121.  Ticket 08 remains
status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`;
`production.py` remains absent.  No source, execution note, ticket status, Git
state or unrelated file was edited; this section is the only review mutation.

Post-review frozen hashes (the review artifact itself is necessarily excluded
from its own self-referential table):

```text
verify.py               dc43d946b2f50bcbdbaa9bda03a3a1a50693c8e1f6d247e43c396216e3ec7697
experiments.py          c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e
README.md               bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55
compare.py              abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py             9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py           b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74
raw_config.py           eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
execution-notes/index.md b3e06b8b0775a10b3e8cf542f1ad562d184fb84d6db3d0a02f85a711b33ae1d4
fix-up ticket index.md   8f56c259bc7b8d92e59478774d8729e1ef4d31828eff2625a6218a01fcab2e91
```

## R1 documentation/criteria follow-up closure review - 2026-08-31

### Strict verdict: OPEN

The frozen source and artifact inputs matched before review:

```text
verify.py       0732ca7643f26c047f45848472f92ba8cb1da06d640c06a9c7f9551dffd8b20f
experiments.py  6f8e79a869c9b49ea29c6193a170900c555294b33bb42a8156f50464a4481b25
README.md       76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9
raw_runner.py   ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b
compare.py      abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py     9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_config.py   eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
execution-notes/index.md f9cb110fad3b0e368254b728985f498cf0e0b1598fbf8dcd67ca58d592d5bf14
r1-documentation-criteria-closure/index.md a6fd85503c5ee6c7679541275430cb2a93c7d913be02f46ac766b61d1c1ba2f9
prior independent-review/index.md 94f6baf43381dbb81e9b693e99a9aa98d065a302d7efddca3ddf357a553c8ca6
ticket 08 index.md 6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975
```

The original R1 prose and criteria findings are mostly closed on the current
bytes: live README/source no longer presents seven Ticket-08 checks,
`production.py`, or an implemented production gate; criteria are exactly
1-121; Ticket 08 remains status 0; criterion 110 now pins the claimed
vocabularies member-for-member; criterion 118 now states one unpriced
intended-configuration outline beside one priced machinery-only diagnostic;
budget-ownership paraphrases are caught over the discovered live-source set;
campaign-derived checkpoint wording is caught; Option A takes no input and is
unpriced; Option B remains exactly 18 runs / 29,268 rows; and the full serial
verification matrix is green.

One P1 authority/presentation escape survives. `Checkpoint1Handoff` is a
non-slotted frozen dataclass (`experiments.py:6660-6661`). The repair correctly
made `feasibility`, `alternatives`, `pilot_line` and `digest` data-descriptor
properties, so direct `object.__setattr__` of those names refuses and a direct
constructor call with `pilot_line=...` is now unexpressible. But ordinary method
names are still instance-shadowable, and the authoritative checkpoint door
compares only dataclass fields plus `handoff.digest` (`experiments.py:7109-7119`).
It does not reject unexpected instance state and it returns the supplied object.

Exact reproduction:

```text
h = verify._t07_handoff()
object.__setattr__(
    h,
    "summary",
    lambda: {
        "pilot_wall_hours": 0.0002777777777777778,
        "ticket_08_authorization_status": "authorized",
    },
)
xpr._require_authoritative_checkpoint(h, **verify._t07_handoff_components())

result: ACCEPTED
extra instance state: ["summary"]
returned summary: {"pilot_wall_hours": 0.0002777777777777778,
                   "ticket_08_authorization_status": "authorized"}
```

This is the same class of exact-type instance-behaviour problem the fixture-plan
follow-up closed. A subclass that overrides `summary()` is refused, but an
exact-type instance shadow is not. A consumer that does use the private
authoritative door still receives and can present the forged `summary()`. A
consumer that follows the prior alignment-review attack literally - reach the
seal, build the exact type, call public `summary()` without voluntarily calling
a private door - can do the same.

The separate field-mutation probe distinguishes raw self-consistency from
authoritative provenance: forcing `resources` to Option B's exact
`ResourceEstimate` changes raw public summary values to 630 physical executions,
29,268 rows and 12,784,432.430769231 bytes, but
`_require_authoritative_checkpoint` refuses that object on `resources`. The
method-shadow case is worse because it passes the authority door unchanged.

**Closure condition:** make checkpoint presentation immune to exact-type
instance state. The simplest bounded repair is to give `Checkpoint1Handoff` no
instance dictionary, or have `_require_authoritative_checkpoint` reject every
unexpected instance key and return the freshly rebuilt handoff rather than the
supplied one. Add exact-type shadows for `summary`, `alternative` and any other
presentation method as must-refuse tests before a checkpoint is presented.

### Closed replays and preserved boundary

- Ticket-08 residue: `production.py` is absent, `find_spec` returns `None`, no
package source imports a production module, README and the stage table state
that the Ticket-08 production gate is not implemented, the check count is
127, and criteria stop at 121.
- Current-fact and stale-stage controls catch the old "final seven" wording,
line-wrapped Ticket-08 production-gate wording, `production.py` implementation
claims, "production numerical budget does not exist yet", and Ticket-08
budget-ownership claims. Truthful `not implemented`, `production.py` absence,
Ticket-07 budget-not-met, and schema-v4 absence controls pass.
- Criterion 110 replay: `check_experiments_isolation()` passes with 16 closed
vocabularies pinned, including `FEASIBILITY_VERDICTS`,
`SUPPORT_CLASSES`, and the single-member Ticket-08 state vocabularies.
- Criterion 118 replay: `checkpoint_one_handoff` has no `alternatives`,
`pilot_line`, `requested_decision`, `ticket_08_derivation_status` or
`ticket_08_authorization_status` parameter; Option A is
`intended_configuration_validation / unpriced_no_claim / cost=None`; Option B
is `narrowed_claim / machinery_and_diagnostic_only / 18 runs / 29268 rows`.
- Benchmark joins: slower benchmark variants are refused as authority-changing;
faster extra measurements leave the pilot line, alternatives, feasibility,
rate and authoritative benchmark digest unchanged, and appear only in supplied
provenance / conservative maxima.
- Campaign removal: `campaign` is absent from `Checkpoint1Handoff` fields and
from `checkpoint_one_handoff`, `checkpoint_alternatives` and
`intended_configuration_option` signatures. The stale campaign relation
controls, including line-wrapped forms, are caught; truthful separate
`ValidationCampaign` planning prose passes.
- Fixture-plan closure remains preserved: the in-suite regression still covers
exact-type instance shadowing and reserved/canonical-name attacks before
output, and the honest fixture works and cleans.
- Scientific boundary remains `numerical_no_result`,
`no_feasible_matrix_among_searched`, `checkpoint_blocked`; no pilot,
campaign, production, sensitivity or Ticket-08 activity occurred; schema v3
remains fail-closed below production-status schema v4.
- The separate round-10 P2 runtime dynamic-f-string limitation remains
explicitly **OPEN and out of this R1 closure**. Line-wrapped stale prose is
now exercised, but a runtime construction such as
`f"no production numerical {stage} exists yet"` is not reclassified here.

### Independent quiet serial matrix and cleanup

The full matrix ran strictly one invocation at a time from absent
`adler_born_two_channel/results/`, with `PYTHONPYCACHEPREFIX` redirected to a
temporary directory removed by the wrapper:

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 287 s |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 290 s |
| `python3 adler_born_two_channel/verify.py` | exit 0, 287 s |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 289 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | exit 1, 290 s, exactly one `[FAIL]`, `deliberate failure probe` |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

The suite-reported census is 127 checks, criteria 1-121, 530 public callables,
1,380 invalid calls and 1,274 parameters. Final checks found
`adler_born_two_channel/results/` absent and no matching verifier/review process.
No implementation file, execution note, ticket status, Git index entry or
unrelated file was edited; only this review section was appended.

## Reconstruction baseline R1 closure review — 2026-08-31

### Strict verdict: OPEN

The frozen implementation hashes matched before review:

```text
verify.py       cd706adf77799242083dcc183367c348d70b754eb8083e42184ee612e4d51275
README.md       aebefcbc4f901c894f0765f9e8c5f3baba846f8a91d09f8861e08fc602a43fc9
raw_runner.py   ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b
experiments.py  c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e
compare.py      abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py     9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_config.py   eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
```

The Ticket-08 presentation finding is closed on the tested surface:
`production.py` is absent, `find_spec("adler_born_two_channel.production")`
returns `None`, no package Python source imports a `production` module, 127
checks are registered, criteria are exactly 1-121, the README and stage table
state that the ticket-08 production gate is not implemented, and Ticket 08 is
still status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.
Replaying the old claims through the live discovered-source mechanisms refused
both current-fact and stale-stage forms for:

```text
The final seven are the ticket-08 production gate.
The final seven are the
ticket-08 production gate.
The ticket-08 production gate is implemented in production.py.
the ticket-08 production gate is
implemented in production.py
The ticket-08 production gate and its closed no-result are implemented **outside** the raw graph (`production.py`).
```

Truthful controls passed, including:

```text
| The ticket-08 production gate | **not implemented**: `production.py` does not exist |
`production.py` does not exist
the production-status schema-v4 absence is truthful because schema v4 does not exist
```

The old stale verifier comment is gone as an executable/live-source problem;
the remaining round-record mentions are historical context.

Two R1 findings remain open.

#### [P1] Budget-ownership prose can still pass with a Ticket-08 ownership paraphrase

The exact old wording and line-wrapped variants are now caught:

```text
the production numerical budget, which tickets 07 and 08 own
the production numerical budget, which tickets 07
and 08 own
tickets 07 and 08 own the production numerical budget
tickets 07 and 08 own the
production numerical budget
the production numerical budget that ticket 08 co-owns
```

But a semantically equivalent ownership sentence planted in another discovered
live source still passes both validators:

```text
source: __init__.py
planted sentence: ticket 08 jointly owns the production numerical budget
check_current_facts passed: True
check_stale_stage_strings passed: True
```

The stale-stage regex only catches `ticket 08` before an ownership verb when
`production numerical budget` appears earlier in the sentence, or `tickets 07 and 08 ... own ... production numerical budget`. It misses singular/reversed
wording where Ticket 08 is the subject. The requested ownership closure was by
meaning across every discovered live source; this paraphrase is actionable and
keeps the budget-ownership R1 finding open.

#### [P1] A public checkpoint record can still carry caller-supplied pilot cost

The factory route is improved: `checkpoint_one_handoff(...)` has no
`alternatives`, `pilot_line`, `requested_decision`,
`ticket_08_derivation_status` or `ticket_08_authorization_status` parameter,
and the built handoff remains:

```text
feasibility: no_feasible_matrix_among_searched
proposal status: checkpoint_blocked
ticket_08_derivation_status: not_started
ticket_08_authorization_status: not_authorized
post_range_production_proposal: None
Option A: intended_configuration_validation / unpriced_no_claim / unpriced
Option B: narrowed_claim / machinery_and_diagnostic_only / 18 runs / 29268 rows
```

The Option A/B record-level attacks refused as expected: priced Option A,
unpriced Option B, Option A relabelled to diagnostic support, missing Option B,
duplicate-only Option A, and an extra alternative label all raised `ValueError`.
The prior rogue `FEASIBILITY_VERDICTS` and rogue `SUPPORT_CLASSES` examples now
make `check_experiments_isolation()` fail, and added/removed/reordered members
were detected for every claimed vocabulary, including the single-member
vocabularies where add/remove are the meaningful mutations.

However, exported `Checkpoint1Handoff` still has a public optional
`pilot_line` field, and direct construction accepts an arbitrary exact
`CostLine` without checking it against `pilot_cost_from_plan(plan, benchmark, safety_factor)`. Exact reproduction:

```text
constructed:
  xpr.Checkpoint1Handoff(
      label="l",
      feasibility="no_feasible_matrix_among_searched",
      ticket_08_derivation_status="not_started",
      ticket_08_authorization_status="not_authorized",
      benchmarks=(verify._t07_slowest(),),
      target=verify._t07_target(),
      power=verify._t07_power(),
      recovery=verify._t07_recovery(),
      disposition=verify._t07_disposition(),
      search=verify._t07_search(),
      matrix=verify._t07_matrix(),
      resources=verify._t07_resources(),
      firewall=verify._t07_firewall(),
      proposal=verify._t07_proposal(),
      alternatives=verify._t07_alternatives(),
      requested_decision=xpr.CHECKPOINT_REQUESTED_DECISION,
      pilot_line=verify._t07_alternatives()[1].cost.lines[0])

result: ACCEPTED
```

That supplied line is a narrowed-diagnostic cost component, not the derived
range-pilot line. Because `summary()` reports `pilot_wall_hours`,
`pilot_storage_bytes` and `pilot_durable_rows` directly from `self.pilot_line`,
the public checkpoint record still has a caller-supplied cost route. This keeps
the criterion-118 R1 finding open despite the factory-level fix.

### Preserved non-regressions

The fixture-plan authority finding remains closed as a non-regression. The
in-suite fixture regression still covers the exact-type instance-shadowing and
reserved-name attacks before output, and the honest deterministic fixture still
works and cleans up. The focused replay observed no persistent `results/`
directory after process exit.

The scientific boundary remains:

```text
numerical verdict: numerical_no_result
search verdict: no_feasible_matrix_among_searched
proposal status: checkpoint_blocked
selection_digest: None
post_range_digest: None
post_range_status: None
Option A: unpriced
Option B: 18 runs / 29268 rows
```

Schema v3 remains fail-closed and no pilot, campaign, production run,
sensitivity run or Ticket-08 derivation was performed. The separate round-10 P2
dynamic-construction limitation remains open and outside this R1 closure:
line-wrapped stale prose was tested and caught, while a runtime f-string such
as `f"no production numerical {stage} exists yet"` still appears to the AST
literal scan only as `["no production numerical ", " exists yet"]`, not as the
whole runtime sentence.

### Quiet strictly serial matrix and cleanup

The full matrix ran from absent `adler_born_two_channel/results/`, one command
at a time, with bytecode redirected to a temporary cache removed by the wrapper:

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 288 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 288 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 287 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 289 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1, 289 s; exactly one `[FAIL]`, `deliberate failure probe` |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

Final checks: `adler_born_two_channel/results/` absent; no verifier or
review-matrix process matched `pgrep -fl "adler_born_two_channel.verify|t07-r1-review|t07-review"`.
The registered census remains 127 checks / 121 criteria / 527 public callables
/ 1383 invalid calls / 1278 parameters. Execution notes, R1 fix-up ticket and
Ticket 08 remained at hashes
`978982be05fbd9a0afc67d7958b255ff2e05274a6955816d9c2e73ab1ae6377a`,
`cb4cadc2c14efe449794ab0bad2d0bb562a12208335ecdedbf71b91846ec3fe4` and
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

Only this review artifact was edited in this review turn; implementation files,
execution notes, ticket statuses and Git index were not edited.

## R1 slotted-checkpoint closure re-review - 2026-08-31

### Strict verdict: CLOSED

No actionable R1 finding remains open in the newly frozen candidate. The exact
P1 from the prior OPEN review is closed: `Checkpoint1Handoff` is now an
exact-type, frozen, slotted record with no instance dictionary, caller shadowing
is refused, subclass dictionary/shadow records are refused at all authority
doors, and the reachable authority door returns a freshly factory-rebuilt exact
record instead of trusting the supplied object. The separate round-10 runtime
dynamic-f-string P2 limitation remains explicitly **OPEN and out of scope** for
this R1 closure.

Frozen source and artifact hashes matched before review:

```text
verify.py             259f2f864070989cc524c0499e1a7b8ef03f6a7973a8b579d775244774fa11c5
experiments.py        b2672e0ff226ef48f073cb31176b656d301ec37f24fa13d28f027586bb68afeb
README.md             76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9
compare.py            abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817
__init__.py           9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a
raw_runner.py         ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b
raw_config.py         eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430
execution notes       0ebb58b832d5faeae7647afe65b291bf9541a6d37ae1fcfc63a21a259552cb44
R1 fix-up ticket      c5aafa6d26a521334c2ebe149341571811eaeab8fb92519c9683e4a69e722dc8
prior review artifact edfb60345bf54f1b83d673aff8dcb63b6474a7f2a1fe4773529c69e0d1a599e7
Ticket08              6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975
```

Artifact path reviewed and appended:

```text
~/.traycer/epics/c443d91e-b0d5-43ff-a31b-805574ab7771/artifacts/debates/born-selection-roundtable/adler-tongue-born-candidate/two-channel-stochastic-model/single-channel-stochastic-commitment/tickets/07-feasibility-pilot-and-freeze/independent-review/index.md
```

Post-append artifact SHA-256 is reported in the reviewer reply; it is not
embedded here because doing so would make the file hash self-referential.

### Exact P1 replay evidence

Focused replay produced:

```text
type exact True
frozen dataclass True
has __dict__ False
slots ('label', 'ticket_08_derivation_status', 'ticket_08_authorization_status', 'benchmarks', 'target', 'power', 'recovery', 'disposition', 'search', 'matrix', 'resources', 'firewall', 'proposal', 'plan', 'requested_decision', 'seal')
declared ('label', 'ticket_08_derivation_status', 'ticket_08_authorization_status', 'benchmarks', 'target', 'power', 'recovery', 'disposition', 'search', 'matrix', 'resources', 'firewall', 'proposal', 'plan', 'requested_decision', 'seal')
slots_match_declared True
summary baseline {'pilot_wall_hours': 29.611087649993713, 'pilot_durable_rows': 81840.0, 'ticket_08_authorization_status': 'not_authorized'}
digest baseline 4732d50af9640851
```

Exact-type instance shadowing refused and left the genuine record unchanged:

```text
summary -> AttributeError: object attribute 'summary' is read-only
digest -> AttributeError: property 'digest' has no setter
alternative -> AttributeError: object attribute 'alternative' is read-only
feasibility -> AttributeError: property 'feasibility' has no setter
alternatives -> AttributeError: property 'alternatives' has no setter
pilot_line -> AttributeError: property 'pilot_line' has no setter
_slowest -> AttributeError: property '_slowest' has no setter
__dict__ -> AttributeError: no attribute '__dict__'
anything_else -> AttributeError: no attribute 'anything_else'
```

Factory/authority replay:

```text
direct pilot_line injection refused TypeError: unexpected keyword argument 'pilot_line'
dataclasses.replace refused TypeError: Checkpoint1Handoff is factory-only
subclass with __dict__ and forged summary: shadow effective on raw subclass
_require_authoritative_checkpoint refused subclass TypeError
_require_unchanged_checkpoint refused subclass TypeError
_require_no_undeclared_state refused subclass TypeError
authority_return_is_supplied False
authority_return_exact True
authority_return_has_dict False
authority_return_digest_equal True
authority_return_summary_equal True
```

Slot mutation through `object.__setattr__` can alter a raw exact instance, but
the authoritative provenance door refuses the changed record:

```text
slot_mutated_raw_summary 630 29268.0 12784432.430769231
slot_mutated authority refused ValueError: checkpoint handoff disagrees with the one its own components build
```

An exact `object.__new__` record populated with the canonical field values is
self-consistent and has no dictionary/shadow state; the authority door still
returns a rebuilt record. This is raw self-consistency, not an independent
authority route.

Reachable seal, direct constructor/cost injection, `dataclasses.replace`,
forged/reordered alternatives, friendlier verdicts, foreign
plan/matrix/resources/proposal, foreign benchmark, mismatched digests, changed
cost lines, public `summary()`/`digest()`, campaign route and previous record
attacks are refused or unexpressible unless the private authority door is
voluntarily invoked.

### Reconfirmed R1 closure scope

- Ticket08/production docs: no `production.py`, no import route, README and
stage table state not implemented, checks are 127, criteria are exactly
1-121, and Ticket08 remains status 0. Old live-source wording, paraphrases
and line-wrapped stale claims are refused; truthful `not implemented` and
schema-v4 absence controls pass.
- Criterion 110: rogue `FEASIBILITY_VERDICTS` and `SUPPORT_CLASSES`, plus
add/remove/reorder attacks for every claimed vocabulary including singletons,
fail the check. No text claims an implemented production gate.
- Criterion 118: Option A is exactly
`intended_configuration_validation / unpriced_no_claim / cost=None`; Option B
is exactly `narrowed_claim / machinery_and_diagnostic_only / 18 runs / 29268 rows`. `feasibility`, `alternatives` and `pilot_line` are not dataclass
fields or constructor/factory parameters and derive from bound components.
- Benchmark binding: slower, foreign, equal-rate and order variants do not
redirect authority. Extra faster supplied measurements affect only explicitly
labelled supplied provenance/conservative maxima and do not change pilot,
alternatives, verdict, rate or margins.
- Campaign removal/live docs: `campaign` is absent from `Checkpoint1Handoff`,
`checkpoint_one_handoff`, `checkpoint_alternatives` and
`intended_configuration_option`; Option A takes no input. Stale campaign
claims, semantic paraphrases and line wraps are refused by the live-source
guard; truthful separate `ValidationCampaign` planning docs pass.
- Budget ownership: exact old `tickets 07 and 08 own`, singular/reversed
Ticket08 ownership, owns/co-owns/shares/holds/responsible/belongs/passive
forms, hyphenation, whitespace and contradictory negation examples are
refused by both prose checks. True denials and schema-v4 absence pass.
- Fixture-plan behavior: exact-type instance shadow, reserved-name and
canonical/fixture relabel attacks refuse before output; an honest fixture
works and cleans.
- Scientific boundary: `numerical_no_result`,
`no_feasible_matrix_among_searched`, `checkpoint_blocked`; no pilot,
campaign, production, sensitivity or Ticket08 activity; schema v3 remains
fail-closed.

Focused helper evidence included:

```text
CHECK check_experiments_isolation True
CHECK check_checkpoint_handoff True
CHECK check_current_facts True
CHECK check_stale_stage_strings True
CHECK check_range_selection True
production_spec None
production_py_exists False
checks_criteria 127 1 121 121
documented_counts {'checks': (127, 127), 'public callables': (530, 530), 'invalid calls': (1380, 1380), 'parameters': (1274, 1274)}
boundary no_feasible_matrix_among_searched numerical_no_result no_feasible_matrix_among_searched checkpoint_blocked None
ticket08 statuses not_started not_authorized not_authorized
optionA intended_configuration_validation unpriced_no_claim None False
optionB narrowed_claim machinery_and_diagnostic_only 18 29268 True
```

Representative ownership and campaign probes:

```text
ownership refused: ticket 08 jointly owns the production numerical budget
ownership refused: ticket 08 owns the production numerical budget
ownership refused: ticket 08 co-owns the production numerical budget
ownership refused: ticket-08 co owns the production numerical budget
ownership refused: tickets 7 and 8 own the production numerical budget
ownership refused: the production numerical budget is jointly owned by ticket 08
ownership refused: ticket 08 is not implemented but jointly owns the production numerical budget
ownership allowed: ticket 08 does not own the production numerical budget
ownership allowed: ticket 08 neither owns nor co-owns the production numerical budget
ownership allowed: production-status schema v4 does not exist yet
campaign refused: the checkpoint builds this record from the campaign it carries
campaign refused: the handoff builds this record from the campaign it carries
campaign allowed: there is no campaign parameter and Option A takes nothing
campaign allowed: a validation campaign is a finite staged plan for gathering the evidence the budget lacks
```

### Independent serial matrix and cleanup

The full exclusive matrix ran strictly one command at a time from absent
`adler_born_two_channel/results/`, with `PYTHONPYCACHEPREFIX` redirected to a
temporary directory removed by the wrapper:

| Invocation | Independent result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | exit 0, 289 s |
| `python3 -m adler_born_two_channel.verify --verbose` | exit 0, 289 s |
| `python3 adler_born_two_channel/verify.py` | exit 0, 312 s |
| `python3 -W error -m adler_born_two_channel.verify` | exit 0, 289 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | exit 1, 825 s, exactly one `[FAIL]`, `deliberate failure probe`, `127/128 checks passed` |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0, 1 s |
| `python3 -m compileall -q adler_born_two_channel` | exit 0, 0 s |

I did not reproduce the implementation-run `-W error` 3,833 s anomaly; the
`-W error` row was normal at 289 s in this run. The long row in this machine
sample was the deliberate failure probe at 825 s, with the expected failing
exit.

The wrapper ended `MATRIX_OK results_absent`. Final checks found
`adler_born_two_channel/results/` absent, no matching verifier/review process,
and the source hashes still at the frozen values. Only this review section was
edited; no implementation file, execution note, ticket status, Git index entry
or unrelated file was changed.
