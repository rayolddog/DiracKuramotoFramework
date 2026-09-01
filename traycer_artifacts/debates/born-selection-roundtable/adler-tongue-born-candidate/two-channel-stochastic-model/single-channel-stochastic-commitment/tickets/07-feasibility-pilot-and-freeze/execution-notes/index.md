---
title: "Ticket 07 execution notes — measured feasibility, and why checkpoint 1 is blocked"
kind: spec
---

# Ticket 07 execution notes

Implementation record for [07 — Establish feasibility, run the range-only pilot,](..)
[and freeze production](..). Ticket status is left at **1 (in progress)** for
independent review and for John's decision; nothing here closes it.

<user_quoted_section>Superseded in part by fix-up round 1 at the end of this note.The submission below was reviewed and returned OPEN. Its conclusionsurvives — the numerical evidence blocks — but three of its numbers do not:the throughput was not measured at the intended resolution, the 290-trialdesign was sized from one arm rather than three, and the feasibility claim wasbroader than the evidence supported. Read the closure round for the currentfigures.</user_quoted_section>

**No pilot was run.** No pilot exponent-related output was opened. No
production-cleared manifest exists. Ticket 08 has not been started. This note
covers everything the ticket asks for *up to* its first named checkpoint, and
the answer it arrives at is that the checkpoint should be refused as posed —
the numerical evidence ticket 04 produced does not fit the statistical
precision this ticket would have to plan for, and no trial count satisfies both
constraints.

## What was built

One new module in `adler_born_two_channel/`, outside the raw import graph:

| File | Lines | Responsibility |
| --- | --- | --- |
| `experiments.py` | 2670 | Frozen provenance, the measured benchmark, the design-based power calculation and its simulation check, the production numerical budget and its disposition, the finite matrix proposal and its cost, the pilot firewall and count-only range rule, and the dry-run production proposal |

Modified: `verify.py` (nine ticket-07 checks, criteria 110–118, 70 new
exported-surface rows), `raw_runner.py` (`UNIMPLEMENTED_RAW_STAGES` wording
only), `__init__.py` (docstring), `README.md`.

Nothing outside `adler_born_two_channel/` and this note was touched. Nothing
staged, committed or reverted; the working tree still shows exactly the 29
pre-existing entries it showed at session start, with `adler_born_two_channel/`
untracked as before.

## Commands

```bash
cd ~/Projects/Physics/DiracKuramotoFramework

python3 -m py_compile adler_born_two_channel/*.py          # compile   -> 0
python3 -m compileall -q adler_born_two_channel            # compileall-> 0
python3 -m adler_born_two_channel.verify                   # canonical -> 0
python3 -m adler_born_two_channel.verify --verbose         # verbose   -> 0
python3 adler_born_two_channel/verify.py                   # direct    -> 0
python3 -W error -m adler_born_two_channel.verify          # -W error  -> 0
python3 -m adler_born_two_channel.verify --prove-failure-exit  #        -> 1
```

**124/124 checks pass** on every path; `--prove-failure-exit` gives 124/125 and
exit 1, with only the deliberate probe failing. `results/` is absent afterwards
on every path. Wall time ≈ 190 s (was ≈ 150 s; ticket 07 adds ≈ 40 s, of which
≈ 29 s is the real streamed benchmark and ≈ 9 s the recovery ensemble). Peak
resident set **634 MB** against the suite's unchanged 900 MB bound.

Documented counts updated: 115 → **124** checks, 372 → **442** public
callables, 1008 → **1206** invalid calls, 831 → **1025** parameters. All pinned
and passing.

## 1. Measured feasibility

The benchmark calls `raw_runner.write_raw_run` — the scalar race ticket 05
chose, both censoring passes, the shadow walk, the five written files — at
`clock_block = 16`, `step_window = 64`. A `BenchmarkFixture` holds an exact
`RawEventConfig`; there is no surrogate kernel and no argument through which one
could be supplied.

| Fixture | Nominal clock-steps | Wall | Rate | Traced peak | Bytes/row |
| --- | --- | --- | --- | --- | --- |
| base (6 trials, 16 clocks, 80 steps) | 7 680 | 3.54 s | 2 169 /s | 90.5 kB | 154 |
| trials ×4 (24 trials) | 30 720 | 12.73 s | 2 413 /s | 115.4 kB | 117 |
| steps ×4 (320 steps) | 30 720 | 12.42 s | 2 473 /s | 102.2 kB | 164 |

**Throughput ≈ 2 200 nominal clock-steps/s**, taken as the slowest fixture.
"Nominal" is `trials × clocks × steps` — the planning unit a matrix multiplies.
It is deliberately *not* the number of steps the race walks: the race walks each
clock twice and truncates the first pass at the best time found so far, so a
per-walked-step rate could not be multiplied by anything. Every timed repeat
runs under `tracemalloc`, which slows it, so the rate is conservative by
construction and the record says so (`traced = True`).

**No noise cube, proved by flatness.** Quadrupling the trials and quadrupling
the steps each quadruple the `trials × clocks × steps` float64 array the plan
forbids. The measured peak grows by **1.28×** and **1.13×** respectively. The
instrument is right for the claim: NumPy's data allocator is traced under
`numpy.lib.tracemalloc_domain`, so a materialized array appears in the number
rather than hiding behind it (verified directly: a 160 MB `np.zeros` shows as
160 MB of traced memory). At the proposed matrix's 9.6 × 10⁸ clock-steps the
unstreamed cube would be **7.7 GB, ≈ 67 000× the largest peak measured**.

Every benchmark run directory is removed on every exit path, including on an
exception; the suite's own "results root is empty" check covers the rest.

## 2. Power and precision

The per-trial Fisher information for the cloglog linear predictor is
`H² / (e^H − 1)`. It vanishes at both ends of a sweep, so zero-event and
all-event cells buy almost no precision however many trials go into them — they
stay in the likelihood (nothing here drops a cell) but the sizing has to know
they are not paying.

`cloglog_slope_variance` is the exact design variance that follows, and it is
**checked against a simulation of itself** rather than trusted. 200 replicates,
150 trials in each of six cells, exponent 2.0 declared before the table, fitted
with `analysis.fit_exponent` — the production estimator, not a private
re-derivation:

| Ensemble | Mean | SD | Closed form |
| --- | --- | --- | --- |
| Independent namespaces | 1.9998 | **0.12485** | **0.12525** |
| Shared master trials (CRN) | 2.0056 | **0.16023** | — |

Agreement to 0.3 %. The paired-versus-independent variance ratio — the resource
price of common random numbers — is **1.647**. The frozen target is sized with a
declared **2.0**, and the suite requires the measurement not to exceed it; an
earlier seed gave 1.55 and another 1.74, so the declared value carries real
margin over the seed-to-seed spread of a variance ratio at 200 replicates.

Pairing *costs* here. It is still right — it is what makes the full-minus-control
contrast cheap and it is what the plan requires for the exponent's uncertainty —
but the trial count has to pay for it, and this is the first place in the project
where that price is a measured number.

**Trial counts, with every control and the shadow sample inside them.** Six
cells over `K ∈ [0.5, 2.0]`, 0.25 exponent half-width:

|  |  |
| --- | --- |
| Independent | 145 trials/cell |
| Paired (×2.0 declared inflation) | **290 trials/cell** |
| Arms | full, central-clock control (1 clock), fixed-contraction width-only control |
| Shadow | 5 % |
| **Total** | **5 481 trials** |
| Achieved exponent half-width | 0.2497 |
| Paired contrast half-width | 0.3531, inside the frozen 0.5 minimum |

The contrast half-width assumes the two arms' estimates are **independent**,
which is conservative: pairing them on one Brownian tree can only reduce it.
That assumption is labelled in the code rather than fitted, because the actual
between-arm correlation is a property of the experiment that has not been run.

## 3. The numerical budget — the blocker

The rule is the closed plan's: a measured discrepancy, inflated by two of its
own bootstrap standard errors, must sit under **one quarter** of the planned
production 95 % half-width, with one intended timestep added for a commit-time
quantile because an event interval-censored to a step did not move if it moved
by less than one.

At 290 trials/cell the planned per-cell probability half-width is 0.0575, so the
allowance is **0.01439**. Ticket 04's own ladders were put back through
`compare_refinement` — not quoted from a note — and their envelopes compared:

| Source | Observable | Bound | Allowance | Fits |
| --- | --- | --- | --- | --- |
| Stationary oracle | survival | 0.04125 | 0.01439 | **no** |
| Stationary oracle | edge-resolved exit count | 0.03670 | 0.01439 | **no** |
| Stationary oracle | exit-time quantile p35 | 0.15290 | 0.02195 | **no** |
| Moving-band audit | commitment probability | 0.01905 | 0.01439 | **no** |
| Moving-band audit | survival at 0.80 | 0.03286 | 0.01439 | **no** |
| Moving-band audit | commit-time quantile p20 | 0.17700 | 0.02195 | **no** |

Disposition: **`numerical_no_result`**, with five blockers.

1. **`moving_band_numerical_no_result`.** The pooled moving-band ladder's own
ticket-04 verdict, carried through unchanged. Re-deciding it from its point
estimate is the relabelling the plan forbids — and the point estimate is not
the issue anyway: the pooled commit-time shift is 0.0112 with a standard
error of 0.0829, so the reference sample cannot resolve the cap in *either*
direction. Enlarging the audit sample is what would move it, and no
refinement of the timestep alone will.
2. **`endpoint_envelope_exceeds_allowance`** and
**`audit_envelope_exceeds_allowance`.** Recorded as separate facts from (1),
deliberately: collapsing them would let the magnitude problem vanish the
moment somebody enlarged the sample enough to turn the no-result into a pass.
3. **`no_evidence_at_intended_configuration`.** Ticket 04's S3 ladder is a
*stationary* reference cell and its S3b matrix is a reduced pulsed one.
Neither was run at the population, pulse, noise or grid the matrix proposes.
Transferring their envelopes is an assumption, so `matches_intended` is false
on every row. This is a finding in its own right and it is the one most
likely to be overlooked, because the arithmetic works either way.
4. **`trial_window_empty`.** The quantitative form of the contradiction.
Numerical error is allowed a quarter of a half-width that shrinks like
`1/√n`, so tolerating the measured envelope **caps** the trial count at
**35 per cell**, while the frozen precision target **floors** it at
**290**. There is no `n` that satisfies both. That is what makes
`no_feasible_matrix` a measurement rather than an opinion, and it is why the
right response is not a wider budget.

The gate is shown not to be a constant function: an empty evidence set returns
`unresolved / evidence_missing` rather than `satisfied`, and evidence inside the
allowance at the intended configuration does satisfy the same rule.

**What would unblock it**, stated so it can be costed rather than argued:

- an enlarged moving-band audit sample — the blocker there is resolution, not
magnitude, and the standard error must fall by roughly an order of magnitude
for the pooled commit-time cap to be decidable;
- a stationary-oracle ladder at a **finer** timestep: the endpoint bias falls
like `√dt`, so meeting a 0.0144 allowance from 0.0412 needs about **8×** the
resolution, which multiplies the ladder's cost by the same factor; and
- both re-run at, or credibly transferred to, the **proposed production**
**configuration** rather than the stationary reference cell.

Only after all three would a numerical budget be met at 290 trials/cell. None of
this is a scientific failure; it is a numerical no-result, which is exactly the
outcome the plan reserves for it.

## 4. The proposed finite matrix, and what it would cost

| Field | Value |
| --- | --- |
| Coupling nodes | 6, log-spaced, 0.5 … 2.0, frozen (no factorial, no continuum) |
| Clocks | 64, midpoint grid, support [−3, 3], spacing 0.09375, **even** parity, origin 0.0 |
| Eligible at the weakest coupling | **10**, counted on the exact grid, minimum 8 |
| Staircase fallback | if the minimum is not met the claim narrows to the exact discrete grid and its visible staircase; the spacing-weighted continuum flux is never substituted |
| Timestep | 1.953125e−3 — the finest level at which *any* continuum evidence exists |
| Refinement ladder | that step halved twice, over **2 of 6 cells and 1 of 3 arms** |
| Arms | full, central-clock control, width-only control |
| Trials/cell | 290 |
| Shadow | 5 % |
| Event/survivor minima | 20 commitments and 20 survivors per pilot cell (pilot rule); production cells are sized by the power target, not by a minimum |
| Stop rule | earliest endpoint on which any clock completes its uninterrupted dwell; every same-endpoint co-completer retained, no winner randomized |
| Failure rule | a ladder that misses the frozen budget, or a moving-band audit that returns `numerical_no_result`, blocks interpretation of the whole sweep; no window reselected, no budget widened after results are opened |

**Cost, scaled from the measurement at a 1.5 safety factor: 9.6 × 10⁸ nominal**
**clock-steps, ≈ 185 hours, ≈ 48 MB over 3.1 × 10⁵ durable rows.**

Cost is therefore **not** what blocks this experiment. About eight days of one
core is affordable. The numerical budget is what blocks it, and that is a more
interesting result than "too expensive" would have been.

## 5. The pilot firewall — implemented, not run

Four separations, all structural:

1. **Streams.** `pilot-…` and `prod-…` namespaces, distinct and prefix-disjoint.
A firewall that shares one refuses to exist.
2. **Folders.** The run-directory families carry the same two prefixes. Nesting
is *unreachable* rather than merely refused, because neither prefix is a
prefix of the other — asserted as an invariant, since a probe for it would be
a probe for something that cannot happen.
3. **Eligibility.** `pilot_trials_eligible` is `False` and cannot be set
otherwise. It exists to be recorded in a manifest, not chosen.
4. **Information.** The count-only door returns a `PilotCellCounts`: coupling,
trials, committed, survivors. Not "the rest is hidden" — the type **does not**
** have** the rest. All 28 names in `FORBIDDEN_PILOT_FIELDS` are asserted absent
and `permits` refuses each by allowlist, so a field nobody thought of is
forbidden by default.

The door was exercised on a **four-trial synthetic run created and removed by**
**the suite**, whose ledger really did carry 16 per-clock rows and a shadow table —
so what the door declines to expose was present to expose. A
production-labelled run and a run on an undeclared namespace are both refused at
it.

The count-only selection rule is frozen before any pilot exists: a cell is
eligible with ≥ 20 commitments **and** ≥ 20 survivors, the selection is the
longest run of consecutive eligible cells (ties to the weakest run, so it is
deterministic), and it must hold ≥ 4 cells or the pilot refuses with a named
reason. `select_range` accepts nothing but `PilotCellCounts`, so it could not
read an exponent if somebody wanted it to. Exercised on five frozen count
patterns whose answers were written down first, including a saturated top that
must be excluded and a gap that must refuse rather than be bridged.

The width-only reference rate is frozen as a **rule**, not a number:
`dynamics.fixed_contraction_rate(low, high)` at the geometric midpoint of
whatever range the count rule selects. Before a pilot there is no range, so the
proposal records the rate as **null** rather than writing a provisional number
nobody would re-derive.

## 6. The proposal is not an approval

`proposed_production_manifest` builds a dry run over **59 required fields**. The
suite omits every one of them in turn and requires each omission to fail; adding
an undeclared field fails; naming one twice fails; editing one after the digest
was quoted fails `require_unchanged_proposal`.

Three things it structurally cannot be:

- it cannot say `production_cleared` — the gate string is refused by name;
- it cannot claim ticket 06's production status schema. It records
`compare.PRODUCTION_STATUS_SCHEMA` as the number it does **not** meet, and the
suite asserts that number still sits above the live manifest schema, so
`physical_verdict_permitted` remains unreachable under schema v3. **No new**
**production status schema was invented, and ticket 06's fail-closed permission**
**is untouched**; and
- it cannot be signed. There is no signature field, and the only two statuses
are `checkpoint_blocked` and `checkpoint_one_approved` — neither of which means
approved-for-production. With the disposition blocking, the second is refused
outright.

**Current proposal digest** `82c184f7f4e2d8cf2d23f41c3cf4a5996eb3a1098f60c126ccb97860c73ff507`,
status `checkpoint_blocked`. **Checkpoint-1 handoff digest**
`b1ea8e2d9b5dc9e944d7edeefa83e02fba338984a2663c52e87f6398eb21567b`,
feasibility `no_feasible_matrix`.

## Preservation

- Ledger and manifest remain **schema v3**; the 45 manifest keys, the 17/19/17
column layouts and `require_closed_ledger` are untouched, and no run file
changed.
- `PRODUCTION_STATUS_SCHEMA = 4` unchanged, so ticket 06's fail-closed
permission is unchanged and asserted.
- Raw isolation unchanged and extended: `experiments` was already on
`_RAW_FORBIDDEN_MODULES`; the file now exists, no `raw_*.py` names it, and the
fresh-interpreter probe still loads none of the forbidden six.
- The analysis layer remains read-only; `experiments.py` writes only benchmark
runs, under the package results root, and removes them on every exit path.
- All prior residuals, tolerances and non-claims unchanged. Ticket 04's
`diagnostic_only` state and its `numerical_no_result` moving-band status are
preserved and are now *load-bearing* rather than merely recorded.

## Decisions taken, and why

**Nominal clock-steps as the planning unit.** The alternative — instrumenting
`raw_race._walk_clock` to count walked steps — would have meant either editing a
raw module for a measurement or monkey-patching one, and would have produced a
kernel rate nothing multiplies. Nominal steps are what a matrix is expressed in,
the measured rate absorbs both passes and the shadow walk, and the record says
so.

**A declared pairing inflation of 2.0 against a measured ~1.65.** A variance
ratio at 200 replicates moves by ±0.1 between seeds, and a target sized from a
number measured *after* the fact is not frozen. So the conservative value is
declared and the measurement is required not to exceed it — which is the same
discipline the numerical budgets use.

**The contrast half-width assumes independent arms.** Conservative, and stated.
The real between-arm correlation is a property of an experiment that has not run.

**The time half-width is declared, not derived.** A commit-time quantile's
sampling distribution depends on the density at the quantile, which is what the
experiment is trying to measure. Two per cent of the pulse duration is declared
and hashed rather than computed from an assumption about the answer.

**Blockers are recorded independently, not collapsed.** A ladder that returned a
no-result *and* whose bound exceeds the allowance has two things wrong with it.

## Limitations and residual risks

1. **The proposal digest embeds a measurement, so it is not machine-stable.**
`benchmark_digest` and `resource_digest` carry wall times, so the same
scientific proposal on a different machine hashes differently. The
scientifically frozen part *is* stable and is separately hashed:
`matrix_digest`, `sampling_target_digest`, `numerical_budget_digest`,
`firewall_digest` and `source_digest` contain no measurement. If a reviewer
wants one stable identifier for "the same experiment", it is those five, not
the proposal digest.
2. **`raw_runner.VALIDATION_NOTE` still says the production numerical budget**
** "does not exist yet".** A budget now exists, is frozen, and has been
evaluated and not met. The note is inside the hashed manifest, so correcting
it changes every ledger digest and touches ticket 05's and ticket 06's
fixtures — which this ticket was told not to disturb. It was left alone and
`UNIMPLEMENTED_RAW_STAGES`, which is *not* in the manifest, was made precise
instead. **This is a live wording inconsistency inside one file and a**
** reviewer should decide it**, not me.
3. **Transferring ticket 04's envelopes is an assumption, and it is the**
** assumption doing the most work.** The disposition blocks on it explicitly
(`no_evidence_at_intended_configuration`), but if a reviewer disagrees that
the stationary cell is a fair stand-in, the *magnitudes* in section 3 are the
part to attack. The verdict does not depend on them — the moving-band
no-result blocks on its own — but the "8× finer timestep" costing does.
4. **The recovery ensemble is 200 replicates.** Enough for a 0.3 % check of the
closed form; the inflation ratio it produces has a standard error of roughly
±0.08, which is why the declared value carries margin.
5. **The suite is now ≈ 190 s.** Ticket 07 adds ≈ 40 s, of which ≈ 29 s is real
race time that cannot be faked without defeating the purpose of the check.
6. **`admissible_trials` is computed at `q = 0.5`.** That is the least
favourable cell for a binomial half-width and therefore the conservative
choice, but a matrix whose cells sat away from a half would have a slightly
different cap.
7. **The count-only door was tested on a synthetic run, not a pilot.** That is
deliberate and required — the pilot needs checkpoint 1 — but it means the
firewall has never been exercised at production trial counts.

## Scientific boundary

Nothing here claims Born's rule, a detector click, an absorption, a measurement
outcome, unique actuality, a microscopic origin for the noise, a two-channel
outcome, or a production-cleared exponent. No exponent of any kind was fitted to
any physical run. What is demonstrated is that the machinery costs what it
costs, that the sizing arithmetic recovers a synthetic answer it was given, and
that the numerical evidence in hand is not small enough against the precision
this experiment would need — which is a statement about resolution, not about
the physics.

## The decision requested at checkpoint 1

Not "approve the pilot". The honest question is narrower:

<user_quoted_section>Given that no trial count satisfies both the frozen precision target and thefrozen numerical budget on the evidence in hand, does John want the additionalticket-04 evidence gathered first (an enlarged moving-band sample and a finer,production-configured oracle ladder), or the scientific claim narrowed untilthe existing envelope fits it?</user_quoted_section>

Running the range-only pilot before either would produce a coupling range for a
production sweep that could not be interpreted whichever range it chose.

# Fix-up round 1 — the independent review's closure

Every probe in the [independent review](../independent-review) was reproduced
against the unmodified bytes before any edit, and replayed afterwards. Ticket
status stays **1**. **No pilot was run, no pilot exponent-related output was**
**opened, no production state was signed, ticket 08 was not touched.**

## Reproduced before fixing

| Probe | Before |
| --- | --- |
| `pilot_counts` on a pilot-labelled, pilot-keyed run in a directory named `prod-t07-review-bypass` | **accepted**, returning counts |
| `raw_runner.open_raw_run` on the same fixture | **exposed** `committed_at`, `dwell_resets`, `band_entries`, `eligible_time`, `exposure_time`, `final_phase`, `co_completed` |
| every non-special manifest field set to `"wrong-but-json-valid"` | **accepted and hashed** |
| a manifest with `status="checkpoint_one_approved"` | **accepted and hashed** |
| budgets with `coverage_sigma` 2 and 9 | different digests, **identical** rows and dispositions |
| authoritative evidence rows supplied | **4**, not the six the note described |
| `admissible_trials` | **35**, computed from probability rows only, while both time rows fail at every `n` |

All seven now refuse or report correctly.

## What changed

`experiments.py` rewritten (2 670 → **4 455 lines**), schema
`dk-experiments/v2`, `CONTENT_REVISION = 2`. `verify.py`: section 11 rewritten,
eleven ticket-07 checks, criteria **110–120**, API census rows rebuilt.
`raw_runner.py`: `VALIDATION_NOTE` corrected under `VALIDATION_NOTE_REVISION`.
`README.md` rewritten for this round.

**126/126** checks pass on canonical, `--verbose`, direct-script and
`-W error`; `--prove-failure-exit` gives 126/127 and exit 1. `py_compile` and
`compileall` clean. `results/` absent on every path. Peak RSS **628 MB** against
the unchanged 900 MB bound. Counts: 442 → **496** callables, 1 206 → **1 297**
invalid calls, 1 025 → **1 117** parameters.

### 1. Benchmark protocol (review P1)

Five fixtures, each with a discarded warmup and **two** timed repeats, every
repeat recorded. The `intended` fixture runs at the matrix's own **64 clocks**
**and `1.953125e-3` timestep** with the proposed blocking; its pulse is shortened
to bound the workload, it commits nothing, so its first pass does not truncate
and its rate is the honest one.

The work unit changed from nominal to **walked** clock-steps —
`2 × trials × clocks × steps + shadow_trials × clocks × steps` — which is what
removes the double-counted shadow the review found. Measured:

| Fixture | Walked | Repeats (s) | Rate | Peak | Truncating |
| --- | --- | --- | --- | --- | --- |
| intended (64 clocks, dt 1.95e-3) | 49 152 | 11.63, 11.62 | **4 228/s** | 173 kB | no |
| base (16, 0.05) | 16 640 | 3.51, 3.51 | 4 742/s | 104 kB | yes |
| trials ×4 | 62 720 | 12.69, 12.88 | 4 870/s | 114 kB | yes |
| steps ×4 | 66 560 | 12.19, 12.17 | 5 460/s | 99 kB | yes |
| shadow ×6 | 23 040 | 4.97, 4.98 | 4 624/s | 86 kB | yes |

Rates span **1.29×** across a 4× clock change and a 25× timestep change — the
independent spot-check agreement, asserted in the suite against a declared 1.5
band. The shadow rewalk's incremental rate is measured separately and matches
the base rate. Storage is now **91–106 bytes/row with the fixed per-run**
**overhead (7.1–7.8 kB) separated**. Costing takes the slowest, which is the
intended fixture. Peak flatness: ×1.10 (trials) and ×0.96 (steps) against a
cube that quadruples.

### 2. Power plan (review P1)

Every arm now declares a conservative probability envelope and its own
invalid-fit price, and is sized from the least informative point in it:

| Arm | Clocks | Envelope | Weight | Trials/cell |
| --- | --- | --- | --- | --- |
| full | 64 | 0.10–0.95 | 0.0999 | **2 406** |
| width_only_control | 64 | 0.05–0.95 | 0.0500 | **2 406** |
| central_control | 1 | 0.02–0.95 | 0.0200 | **6 346** |

Paired arms share a count; the central control does not pair and keeps its own.
The three contributions are reported apart: analytic independent-cell **458**,
declared pairing inflation **2.0**, declared conservative factor **1.25**, plus
per-arm failure inflation. The provisional label is carried on the record
(`stage = provisional_pre_pilot`) and in every consumer.

The recovery ensemble now draws its shared master-trial latent from the
package's **own counter-keyed physical stream** and mixes it with a per-cell
component at correlation **0.85**, so realizations are not monotone across
coupling. Only **valid** fits contribute (142/150 independent). Measured
pairing inflation **1.29** against the declared 2.0. A control arm is generated
at a declared **negative** between-arm correlation and the contrast's measured
variance inflation is **0.70** against the declared 1.25 — the "pairing can only
reduce" claim is gone and `CONTRAST_COVARIANCE_FLOOR = -0.25` replaces it.

`post_range_power` is the frozen mechanical join: its only inputs are a
`RangeSelection` and the `PilotCellCounts` it came from; a mismatched pair is
refused; zero- and all-event cells inside the range are retained.

### 3. Numerical budget (review P1, P2)

- `bound_at(coverage_sigma)` takes the sigma; `numerical_disposition` passes
**the budget's own frozen value**. Two budgets with different sigmas now move
every row — asserted.
- **17** authoritative rows are carried (every observable at every position at
each ladder's finest level, excluding the `added_resets_mean` diagnostic
ticket 04 froze as non-convergent). Nothing is selected by point error;
`limiting(unit)` picks by full bound inside a unit.
- `probability_admissible_trials` (**35**) and `time_admissible` (**false**) are
separate; `admissible_trials` derives to **0** because a time failure is
`n`-independent. `time_bounds_fail_at_every_trial_count` is a named blocker.
- `projected_bound` scales **bias by √dt and standard error by 1/√n**
**separately**.

### 4. The finite search (review P1)

`search_feasible_options` enumerates **12 declared options** — refinements to
dt/16, enlargements to 1024×, reduced trial counts, combinations, and one at the
intended configuration. None fits; the closest misses by **1.33×**. Verdict
`no_feasible_matrix_among_searched`, and `no_feasible_matrix` is no longer in
the vocabulary. Positive controls: a generous option at the intended
configuration returns `feasible_matrix`, the same option on transferred
evidence returns `unresolved`.

### 5. Pilot firewall (review P1)

- `require_pilot_name` refuses a run in the production family, in neither
family, or spelled with a separator. The review's own
`prod-t07-review-bypass` reproduction is refused.
- A closed pilot run is **moved** to `results/pilot_quarantine/<name>`.
`open_raw_run` refuses it by every spelling — bare name, two-segment path, and
the quarantine directory itself — all three asserted. `pilot_counts` is the
only supported path, and it re-runs the full eight-check closure gate: a
duplicated row in the quarantined ledger is refused and restoring the bytes
restores the counts.
- `PilotCellCounts` carries the close-marker digest; `RangeSelection` carries
every one; the manifest **derives** the contraction rate through
`reference_rate` and has no parameter for one.

### 6. Manifest semantics (review P1)

Factory-only via a seal, **78** declared fields, each validated by type, enum,
range and cross-field relationship. Every field is separately refused when given
a wrong value **with the seal present**; the review's complete
`"wrong-but-json-valid"` record is refused twice over. `PROPOSAL_STATUSES` has
one member. Seven cross-field relationships checked (spacing, parity, ladder
start, refinement subset, arm agreement, status-schema ordering, blockers).

The freeze split: **`design_digest`** over 55 measurement-free fields
(reproducible), whole-proposal digest over everything (moves with the machine).
`require_unchanged_proposal` compares the design digest.

### 7. Matrix and resource accounting (review P2)

Exact identities: `refinement_couplings = (0.6598, 1.1487)`,
`refinement_arm = "full"`, `arm_clocks` with the central control pinned at one
clock, `arm_trials` per arm, `refinement_trials_per_cell = 200`.

| Line | Runs | Physical | Shadow | Rows | Hours |
| --- | --- | --- | --- | --- | --- |
| primary/full | 6 | 14 436 | 726 | 984 804 | 382 |
| primary/central_control | 6 | 38 076 | 1 908 | 78 060 | 16 |
| primary/width_only_control | 6 | 14 436 | 726 | 984 804 | 382 |
| refinement/level1/full | 2 | 400 | 20 | 27 280 | 21 |
| refinement/level2/full | 2 | 400 | 20 | 27 280 | 42 |
| **total** | **22** | **67 748** | **3 400** | **2 102 228** | **844** |

≈ 192 MB. Every one of those is recomputed independently inside
`check_primary_matrix`. Shadow is rounded up **per run**. The pilot is a
separate `CostLine` outside the total.

**These are not the review's 6 380 / 330 / 320 530 figures**, and the difference
is not an arithmetic disagreement: the review computed them for the earlier
290-trial provisional design, and arm-aware sizing replaced that with 2 406 for
the paired arms and 6 346 for the central control. The *rules* the review asked
for — per-run shadow rounding, per-arm grids and counts, a named refinement arm,
rows as `trials + trials×clocks + shadow×clocks` — are exactly the ones used
here; only the inputs moved.

### 8. Stale strings (review P3)

`VALIDATION_NOTE` no longer says the production budget "does not exist yet"; it
records that ticket 07 froze one, that the disposition is `numerical_no_result`,
and that no matrix was feasible among the options searched, at **validation-note**
**revision 2**. The durable phrases ticket 06's gate reads are asserted to
survive. **The schema is unchanged**: 45 keys, version 3, same layout — only a
field *value* moved, so every manifest written from here has a new digest, which
is the cost the review judged worth paying. `raw_runner`'s docstring, its stage
list, the verifier banner and the README stage table were corrected with it, and
`check_stale_stage_strings` pins all of it.

## The two costed alternatives

| Option | What it buys | Cost |
| --- | --- | --- |
| **A — intended-configuration validation** | stationary oracle ladder on the production grid and pulse at dt/8, plus a 256× enlarged moving-band audit | **≈ 3 766 h**, 163 MB |
| **B — narrowed claim** | the same matrix at 35 trials/cell, the largest count the present probability bound admits | **≈ 11 h**, 3 MB |

Option B supports a **machinery and diagnostic statement only**: at 35
trials/cell the exponent interval is far wider than the frozen target, both time
bounds still fail at every trial count, and the moving-band
`numerical_no_result` still blocks. No physical scaling claim is invented under
either option.

## Digests

|  |  |
| --- | --- |
| proposal **design** digest (measurement-free, reproducible) | `f1aff5389599f7d136b922a5a0b4ffc4af7a05362e151ee19e25c517875f6aeb` |
| proposal digest (binds the measurement, machine-dependent) | `3a4aaca2626fac37ea0a63c5d5efb4794945c874b37e0f0d2661de666ad67c0a` |
| checkpoint-1 handoff | `f5…` — recomputed per run, see the suite |

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `994896aa1f44c093cdc2a2d44e3ac02d9e438492f4a7781cf8cf134d8aba637c` |
| `verify.py` | `efa40b56c575d78fcd3dc8ff4df71f96649df25f9280bc8a4afc3a11a6859f42` |
| `raw_runner.py` | `cbb6085c610600afd4875fed2ef8531bdc3e8758b307190feca2147ec98a739b` |
| `README.md` | `1594e4abfccc47edc19b61f4fea8a748aa8a3aaf305afcb100bae9fe7b349515` |
| `__init__.py` | `aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b` |

## Round-1 limitations

1. **The arm envelopes are declared judgement, and they now drive the design.**
The central control's 0.02 floor sets 6 346 trials/cell and therefore much of
the 844-hour total. Nothing measures where these arms actually sit, because
no run has been made; a narrower envelope would be cheaper and less
conservative, and the trade is visible rather than buried.
2. **The recovery ensemble is a copula, not a race.** The shared latent comes
from the package's real keyed stream, and the dependence is non-monotone as
the review asked, but the outcomes are still generated from the frozen model
rather than by running the full/central/width arms through `raw_race`. Doing
that at ensemble scale is a many-hour job and would itself need a budget.
3. **`√dt` bias scaling is the ticket-04 ladder's asserted rate**, applied to a
different cell. It is a planning projection and the search says so.
4. **The measured contrast inflation (0.70) is below the declared floor (1.25)**
under *this* synthetic dependence. That is the direction the declaration
wants, but it is one dependence structure, not a bound.
5. **Every manifest digest changed.** No durable pilot or production run
existed, so nothing was invalidated, but any external note quoting an older
manifest digest is now stale.
6. **The suite is ≈ 4.5 minutes**, of which ≈ 90 s is real race time.
7. **`ClosedLedger` and the quarantine directory are still ordinary files.**
Quarantine removes the *supported* reader, not filesystem access; it is
protection against accidental exposure, described as that and not as a
sandbox.

# Fix-up round 2 — the re-review's closure

Ticket status stays **1**. **No pilot was run, no pilot exponent-related output**
**was opened, no approval or production-cleared state exists, ticket 08 untouched.**
Delivered over two working turns; this note covers both.

## Every round-2 probe reproduced before any edit

| Probe | Before | After |
| --- | --- | --- |
| serialized `design_digest` | `"0"*64` beside a computed `f1aff538…` | computed in the factory, **recomputed and compared in `__post_init__`** |
| `source_digest` → `ff…ff`, guard accepts | accepted | refused — source is inside the freeze |
| sealed `numerical_blockers=["looks_good"]` | hashed | refused — `list_blockers` checks membership |
| sealed `numerical_verdict="satisfied"` with blockers | hashed | refused by the recomputed digest **and** the derived relation |
| non-hex 64-char digests | accepted everywhere | `_require_hex_digest` on every digest field |
| unquarantined handle → `pilot_counts` returns counts while `open_raw_run` exposes rows | accepted | refused: `'…' is not a run inside the quarantine` |
| six invented `PilotCellCounts` → `post_range_power` powered | accepted | `TypeError`: projections are seal-minted only |
| dt/8 bias 0.010086 > allowance 0.00499471 | confirmed | Option A relabelled; campaign refines to **dt/256** |
| 91.1628 B/row used vs 106.2203 max → 223.47 MB | confirmed | now **max(empirical, schema bound)** |
| stale prose at README 60/106/2980, banner 29218, raw_runner 234 | all five | all corrected; guard rewritten as a scan |

## Item 1 — proposal authority

`design_digest` is computed by the factory over `DESIGN_DIGEST_KEYS` and
**recomputed in `__post_init__`**; a record whose serialized freeze is not its
own design is refused. `DESIGN_DIGEST_KEYS` is derived by subtraction: **75 of**
**80** keys, everything except the five in `DESIGN_DIGEST_EXCLUSIONS`
(`design_digest` self-referential, `status_reason`/`proposal_label` free text,
`benchmark_digest`/`resource_digest` wall-time bearing).

Per the coordinator's ruling the two levels are documented at
`DESIGN_DIGEST_EXCLUSIONS`: **`design_digest` is the reproducible scientific**
**freeze** — source, environment, firewall, selection, reference rate, numerical
budget and evidence, search, power, matrix and every measurement-free resource
assumption — and **`digest` is the measured proposal envelope**, binding the
benchmark and resource records too. Semantic authority is not traded for
stability: a substituted measurement cannot enter a proposal because the factory
recomputes the construction-time joins.

New declared fields: **`arm_trials`** (`full` 2 406, `central_control` 6 346,
`width_only_control` 2 406), validated against `arms` and `trials_per_cell`; and
**`measured_arm_latent_correlation` = −0.180625** carried beside
**`contrast_covariance_floor` = −0.25**, with a relation check refusing a
measurement past the floor and a suite assertion that they are not the same
number. Every digest field is lowercase-hex validated.

Probes added: six post-freeze edits (trial count, **source**, environment,
firewall, reference rate, numerical budget), each rehashed so the guard has a
well-formed record to reject; public-constructor, `dataclasses.replace`,
manual-`type()`, deep-copy and seal-less-token refusals.

## Item 2 — quarantine authority

`QuarantinedPilotRun` **has no directory field**. Resolution is name-only:
`results/` → quarantine → run directory, each opened `O_DIRECTORY|O_NOFOLLOW`,
every file relative to the pinned run descriptor with `O_NOFOLLOW` and an
`S_ISREG` check; the only string-resolved name is the package directory. OS
failures become refusals with messages.

`closure_digest` binds the **whole closure** — marker schema version, all three
`(table, rows, digest)` triples, and the manifest digest — not one table.

`PilotCellCounts` public surface is exactly **coupling, trials, committed,**
**survivors**, plus an opaque `_Projection` with `__slots__`, no readable
attribute and a seal-gated constructor. `select_range` and `post_range_power`
derive their counts digest from those tokens, so an invented cell reaches
neither. `RangeSelection.closure_digests` replaces `ledger_digests`.

## Item 3 — actual kernel benchmarks and a staged campaign

The **real** ticket-04 kernels are timed, each with a discarded warmup and two
repeats, on its own unit:

| Kernel | Unit | Problem | Repeats (s) | Rate | Peak |
| --- | --- | --- | --- | --- | --- |
| `killed_diffusion.solve_survival` | oracle space-time cell | 600×600 implicit grid, 3 starts, horizon 2.0 | 0.0359, 0.0347 | **1.0 × 10⁷ /s** | 17.3 MB |
| `killed_diffusion.compare_refinement` | bootstrap resample-observation | 200 resamples × 40 clusters × 6 samples × 3 levels | 0.1406, 0.1401 | **1.02 × 10⁶ /s** | 124 kB |

The two units are never divided by one another; `ValidationStage.seconds_at`
refuses a benchmark whose unit is not the stage's.

**Seven predeclared stages**, each attacking one budget unit by one lever, with
operation counts *derived* from the declared factors (`base × spatial × sample ÷ timestep`) rather than asserted:

| Stage | Unit | Attacks | Lower-bound cost |
| --- | --- | --- | --- |
| stationary, dt/16 at 2× space | probability | timestep bias | 0.00 h |
| stationary, dt/64 at 4× space | probability | timestep bias | 0.01 h |
| stationary, dt/256 at 8× space | probability | timestep bias | 0.16 h |
| stationary time quantile, dt/256 at 8× space | time | timestep bias | 0.16 h |
| moving-band, 64× master trials | probability | sampling error | 0.16 h |
| moving-band, dt/16 replay | probability | timestep bias | 0.01 h |
| moving-band time quantile, 1024× master trials | time | sampling error | 41.15 h |

Stationary stages go **finer than dt/8** because dt/8 is already insufficient,
and refine space separately from time. Moving stages attack timestep bias and
sampling SE in separate stages with increasing master trials. Every stage
carries a frozen success rule tied to its unit's own allowance, a `no_result_rule`
that must literally name `numerical_no_result`, a stop rule (cap, or the first
predecessor that returned a no-result), a resource cap, and
`sufficiency = "not_promised"` — the only value that field can hold.

**Cost is a range: ≈ 42 h at the measured kernel rates, up to ≈ 3 120 h if every**
**stage runs to its declared cap.** Not an approval estimate, and the record says
so. `ValidationCampaign` refuses to exist unless both units and both levers are
covered and every dependency names a real stage.

## The production-width row bound

Worst-case valid schema-v3 rows are constructed at the proposed maxima (trial
6 345, clock 63, `-1.2345678901234567e-16` floats, 1234.5678901234567 times,
64-entry list cells) and encoded through the writer's own
`raw_ledger.encode_row`:

| Table | Worst row |
| --- | --- |
| `ledger.csv` | **7 007 B** (64 winners, five per-winner list columns) |
| `clocks.csv` | **225 B** |
| `shadow.csv` | **215 B** |
| three header lines | **700 B** |

Quoting the widest row would price every row as a 64-winner ledger line, which
no clocks row is; the **blended** bound for the mix a run actually writes — one
ledger row per trial and `clocks` authoritative rows — is
`(7007 + 64 × 225) / 65 = ` **329.34 B/row**. The cost model takes
`max(empirical 106.2203, 329.34)`.

**Included**: the trial ledger, the authoritative per-`(trial, clock)` table and
the no-stop shadow sample — the three tables a closed run writes.
**Excluded**: the manifest and close marker, costed separately as fixed per-run
overhead; and every derived product (binned survival tables, plots, analysis
output), which no run writes and this ticket does not cost.

**Storage rises from 223.47 MB to 692.5 MB.** The matrix total is now
**856 h / 692.5 MB**, the range pilot **43.0 h** as its own visible line, and
the summary quotes the coefficient the total was actually built on with the
empirical maximum beside it under its own name.

## Item 5/6 — prose and checkpoint wording

README:60, README:106-107, README:2980-2981, the printed verifier banner and the
raw_runner comment are corrected. The guard is a **scan**: six claim patterns
over README / raw_runner / experiments / `__init__` plus the *printed* banner
lines, required affirmative statements in each of the three reader-facing
places, and eight pattern fixtures pinned in both directions.

- **Option A** is an exploratory staged campaign: it states the cost is a range
from measured kernels, that no stage is promised sufficient, and that a miss
is a numerical no-result. It no longer claims dt/8 + 256× is enough.
- **Option B** is an **18-run primary-only diagnostic sweep** at 35 trials/cell,
≈ 11 h, with the four refinement runs, the range pilot and all numerical
validation excluded in both summary and prerequisites, supporting a
machinery/diagnostic statement only.

## Verification

126/126 on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → 126/127, exit 1. `py_compile`/`compileall` clean,
`results/` absent on every path. Counts 496 callables / 1 305 invalid calls /
1 125 parameters, criteria 110–120. Tree at its 29 pre-existing entries.

|  |  |
| --- | --- |
| design digest (reproducible) | `83530512b0a863756321cc7237deb268464f300e412c956d51aa88b68715b5dc` |
| proposal digest (measured envelope) | `659bd2b87e9280f7d1dd64f74c548aae5eaec3ff1082a406baffbbfdf5f5f2f3` |
| `experiments.py` | `14e9a1daab28a3908fa42dbf4d1f6bcb49b3af56e16fd0fda6b6e57e05dfbcce` |
| `verify.py` | `0d27a17b0a4dcbc52479c3faf0e025ab68c0cde9c968d2c9b46f2eb0feb2557e` |
| `raw_runner.py` | `7b07bdf84ac88cc382b8ed3ee8dcb9831b8bf52a4724082ae293c4b4581a475d` |
| `README.md` | `1db104a792cf71137d0b7b25242a6678ddd2c90467693e9dffcc6469ee50990b` |

## Round-2 limitations

1. **`KernelBenchmark`, `benchmark_kernel`, `ValidationStage` and**
** `ValidationCampaign` are not exported.** They are planning records for
unauthorized work, built and exercised by `verify.py`; keeping them off the
public surface says a campaign is a proposal rather than an API. The cost is
that they carry no exported-surface census row.
2. **The campaign's stage costs scale linearly in each kernel's own operation**
** count.** That is a stated assumption about an implicit PDE solve and a
cluster bootstrap, measured at one size each; neither was measured across a
size sweep, so the lower bound is a lower bound.
3. **The 329.34 B/row blend assumes the 64-clock arm's mix.** The one-clock
central arm writes two rows per trial, not sixty-five, so its own blend is
different and higher per row; the total uses the single blended coefficient
across all arms, which over-prices the central arm and under-prices nothing.
4. **The measured arm latent correlation is a property of the copula**
** generator**, not of the race. It is now named and carried as such, and the
frozen floor it is checked against remains an assumption.
5. **Quarantine removes the supported reader, not filesystem access.**
6. **No stage of the campaign has run.** The disposition remains
`numerical_no_result`, the search remains
`no_feasible_matrix_among_searched`, and the proposal remains
`checkpoint_blocked`.

# Fix-up round 3 — the re-review's four blockers

Ticket status stays **1**. **No pilot, no approval, no production-cleared**
**state, Ticket 08 untouched.** Every probe was replayed against the unmodified
bytes before any edit.

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| rehashed `numerical_verdict="satisfied"`, empty blockers, `search_verdict="feasible_matrix"`, module seal | **accepted**, design digest `b9755653…` | refused by the component rebuild, naming the disagreeing fields |
| rehashed arm trials **7/8/7** | **accepted**, `15ba13a8…` | refused |
| rehashed measured correlation **0.9** | **accepted**, `740c1101…` | refused |
| six forged `_Projection` cells → `post_range_power` | **accepted**, `powered`, 3 425/9 035/3 425 | the token no longer exists |
| `dataclasses.replace`-edited counts keeping provenance | **accepted** | provenance is gone; edited counts are display-only |
| `PilotCellCounts` visible fields | `coupling, trials, committed, projection` | `coupling, trials, committed` (+ `survivors`) |
| clocks worst row at maximal finite floats | 225 B claimed | **257 B** |

## 1 — Proposal semantic authority

**`require_authoritative_proposal(proposal, …components…)`** rebuilds the
proposal from the numerical disposition, the feasibility search, the power
plan, the matrix's own arm and cell identities, the recovery measurement, the
firewall, the selection, the benchmark and the resource estimate, and requires
**field-for-field equality**. Nothing about the record is trusted; it is
reconstructed and compared. A self-digest proves byte consistency and says
nothing about provenance, and the docstring says so.

**The seal stays a module-private attribute and nothing depends on its**
**secrecy.** `SEAL_IS_NOT_THE_AUTHORITY` states the property and the suite tests
it: a reachable-token record still fails the rebuild, caller counts are
display-only, and the authoritative pilot doors reopen and recount.

## 2 — Pilot authority

`_Projection` deleted. `select_range(firewall, run_names)` and
`post_range_power(target, firewall, run_names)` take **quarantined run names**
and go through `_authoritative_cells`, which re-opens and re-counts every run
through the five-file closure gate; `post_range_power` recomputes the selection
itself, so neither a caller's counts nor a caller's selection can arrive. A
refused selection is a `no_powered_matrix` result rather than an exception.
Display counts live behind **`preview_range`**, whose selections carry all-zero
closure digests that no real run can produce.

## 3 — Option A: explicitly unpriced

Under the permitted branch. `CheckpointAlternative.cost` accepts `None` and
`is_priced` is `False`. The summary states that the two timed kernels — the
PDE oracle solve and the paired bootstrap over **already-generated**
observations — omit the moving `replay_pulse`/paired-leaf generation and the
stationary endpoint generation entirely, so no range built on them is an
estimate or an upper bound. **The 42–3 120 h figures are gone.** The seven-stage
outline, its per-unit stop rules and `sufficiency="not_promised"` survive as an
outline. Pricing it would need end-to-end benchmarks of four kernels; that is
recorded as the prerequisite and was deliberately not attempted.

## 4 — Intended-configuration row bound

`row_width_bound(trials, clocks, steps)` uses the **widest finite** spellings
(`±1.7976931348623157e+308`) and derives every counter from the configuration —
identifiers from trials and clocks, endpoint/entry/reset counters from pulse
steps, since a clock cannot record more endpoints than the window has.
Changing any of the three forces recomputation. There is no schema-wide bound,
because integers are unbounded, and the docstring says that too.

| Table | Bytes |
| --- | --- |
| `ledger.csv` | **8 110** |
| `clocks.csv` | **257** |
| `shadow.csv` | **247** |
| 64-clock blend | **377.815 B/row** |
| one-clock central blend | **4 183.5 B/row** |

**Matrix: 854 h, 794.4 MB** (was 692.5 MB). **Range pilot: 42.9 h**, its own
visible line.

### Option B, repriced arm by arm

18 primary runs, 630 physical trials, **29 268 rows**, priced at Option B's
*own* trial count rather than the small timing fixture's coefficient:

| Line | Runs | Rows | Coefficient | Storage |
| --- | --- | --- | --- | --- |
| full + width (64 clocks) | 12 | 28 836 | 377.815 B/row | **10.931 MB** |
| central (1 clock) | 6 | 432 | 4 183.5 B/row | **1.853 MB** |
| **total** | **18** | **29 268** |  | **12.784 MB**, **11.4 h** |

The 64-clock line alone is 10.93 MB, which brackets the re-review's
10.65–10.8 MB expectation; the difference is the central arm, which this model
prices with its own blend because a run whose rows are half ledger lines is not
priced by a 64-clock blend. The suite mutation-tests that the coefficient is
not the small-fixture one and that the run and row counts are exactly 18 and
29 268. Exclusions unchanged: four refinement runs, the range pilot, all
numerical validation, and no physical claim.

## Component-source map

`PROPOSAL_FIELD_SOURCES` maps all **80** serialized fields to their
authoritative component and a classification. Exactly two — `status_reason` and
`proposal_label` — are `free_text`; every other field is `derived` and rebuilt.
The suite checks the map covers the exact key set with no duplicate or
omission, that only those two are free text, and that membership of the design
freeze agrees with `DESIGN_DIGEST_EXCLUSIONS` field by field.

## Consumption boundary

`checkpoint_one_handoff` now calls `require_authoritative_proposal` with the
very components it carries **before** the handoff exists, so a bare
self-consistent proposal is refused at the checkpoint rather than presented.

## Verification

126/126 on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → 126/127, exit 1; `py_compile`/`compileall` clean;
`results/` absent. Counts 499 callables / 1 308 invalid calls / 1 142
parameters. Tree at its 29 pre-existing entries.

|  |  |
| --- | --- |
| design digest | `d33c6818579d4b38a31bb0ecaebf64a876a07a8869f2b31f3ac3941f66bd144b` |
| proposal digest | `ac7a1d4b9a4ce8f1618d566a26f7d593a6c25ad01572ad23f65d038aad2b1ac7` |
| `experiments.py` | `3e209e11c25e6cc07f1d4c15bf869cb44af805ddc09b532aac759c897d8c800a` |
| `verify.py` | `1073ee7df6215bff85b4a9ab27b635d160fd3e3338143dc7ee568efcd4988f2b` |
| `raw_runner.py` | `7b07bdf84ac88cc382b8ed3ee8dcb9831b8bf52a4724082ae293c4b4581a475d` |
| `README.md` | `10278f89c3ac19e5278260d5289c4557e09d6bac78a962e3f0496ed80dab2128` |

## Round-3 limitations

1. **Option A is unpriced, not measured.** The four end-to-end kernels were
deliberately not benchmarked; the omission is the closure.
2. **The seal remains a module attribute.** Authority does not rest on it, and
that is asserted rather than assumed — but a determined caller can still
*construct* a self-consistent record; it simply cannot pass the rebuild.
3. **The central-arm blend is coarse.** A one-clock run's two-row mix is priced
as half ledger lines, which over-prices it; the direction is conservative.
4. **The rebuild takes the two free-text fields from the record**, by
classification. A wrong `status_reason` is not detectable and is not a
statement about the experiment.
5. **No campaign stage has run.** `numerical_no_result` blocks,
`no_feasible_matrix_among_searched` stands, the proposal is
`checkpoint_blocked`.

# Fix-up round 4 — the round-3 review's four findings

Status **1**. **No pilot, no approval, no production state, Ticket 08**
**untouched.** Probes replayed against the unmodified bytes first.

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| rehashed measured correlation **0.9** with a matching scalar handed to the rebuild | **accepted** | the scalar is gone; the value is derived from the `RecoveryReport` |
| `require_authoritative_proposal` had no `recovery` parameter | true | it takes the record and binds `recovery_digest` |
| benchmark source digest never joined to the fingerprint | true | a benchmark whose `source_digest` is not the current fingerprint is refused |
| `ValidationCampaign.cost_range` computable | **41.95 h .. 3 120 h** | the property, `seconds_at`, `maximum_seconds` and the Option A cost lines are **deleted** |

## 1 — Proposal measurement authority

`require_authoritative_proposal` and `proposed_production_manifest` now take the
authoritative **`RecoveryReport`** and derive
`measured_arm_latent_correlation = r² · ρ` internally; there is no scalar
parameter to forge. A new `recovery_digest` field binds the record. The
benchmark is joined to the environment: `benchmark.source_digest` must equal
the current `SourceFingerprint.digest`, so a timing of different bytes cannot
enter. The manifest is now **81 fields, 76 in the design freeze, 5 declared**
**exclusions**, and the component-source map covers all of them.

## 2 — Pilot authority (partial)

- **`PreviewRangeSelection`** is a distinct display-only type. `reference_rate`,
the manifest factory, `post_range_power` and the handoff all demand exactly a
`RangeSelection`, so a preview cannot enter any authoritative door — checked
by type, not by a digest convention.
- **One read, one snapshot.** `post_range_power` calls the quarantine reader
**once** and derives both the selection and the cell list from that single
ordered snapshot; the two-read path that could mix a six-cell and a five-cell
state is gone.

**Not done:** writing pilot ledgers directly into the quarantine root. They are
still written under the ordinary results root and moved, so a transient
production-root entry exists. `raw_runner.open_raw_run` is also unchanged and
still does not refuse pilot-labelled manifests at creation.

## 3 — Option A: no numeric price path at all

`cost_range`, `seconds_at`, `maximum_seconds`, the per-kernel rate lookup and
both Option A `CostLine`s are **deleted**. `ValidationCampaign.is_priced`
returns `False` unconditionally. Stages keep their order, dependencies, a
qualitative `candidate` description, per-unit success/no-result/stop rules and
`sufficiency="not_promised"`; `operations` is a **relative shape**, never
multiplied by a rate. The 41.1 h and 3 120 h values are gone from code and
prose.

## 4 — Presentation

README updated: 81 declared fields, 76-of-81 design freeze, four-value
`PilotCellCounts`, matrix ≈ 852 h / 794 MB, pilot ≈ 43 h, Option B 18 runs /
29 268 rows / ≈ 11.4 h / 12.78 MB, Option A unpriced, and the section retitled
**"One blocked option and one machinery-only diagnostic"** rather than two
costed alternatives. The stale `f1aff…` digest, 55-design-field, 192 MB and
3 MB claims are removed.

## Verification

126/126 canonical / `--verbose` / direct / `-W error`; `--prove-failure-exit`
→ 126/127 exit 1; compile paths clean; `results/` absent; tree at 29 entries.
Counts 501 callables / 1 312 invalid calls / 1 146 parameters.

|  |  |
| --- | --- |
| design digest | `bdc747f011ebb8b6b840551ff7ff216032022a61a80c0f7a6598e024087dacf0` |
| proposal digest | `a1365712ed58ed5a08e0f76baf586a8ac1da59d0c902a273e87510acc2dda450` |
| `experiments.py` | `22258a45bbc9065c0db74591c428dae3574cd6ca55c51d35a30c1dfbe724545a` |
| `verify.py` | `14d5aa62f2b0bd7ed03e0e05b8c5c883c90050513782a6824ab79b86bdb31d2b` |
| `README.md` | `2165377cf2e5c7ed8388a1ab7349f6ad3a21be0ca7bde4b124129aa8ef886e56` |

## Round-4 limitations

1. **Pilot runs are still created under the ordinary results root and moved.**
The transient production-root entry the review asked to eliminate remains.
2. **`raw_runner.open_raw_run` does not refuse pilot-labelled runs at**
** creation**; it is defeated by the move, not by a rule.
3. The mechanical current-fact guard is **not** added; the prose was corrected
by hand and only the existing stale-stage scan protects it.
4. Option A remains unpriced by omission, as ruled.
5. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`.

# Fix-up round 5 — the three outstanding items

Status **1**. **No pilot, no campaign, no approval, no production state,**
**Ticket 08 untouched.**

## 1 & 2 — direct-to-quarantine writing and a reserved raw-owned identity

`raw_runner` gained **`EXPERIMENT_PILOT_NAMESPACE_PREFIX = "xpilot-"`**, a
raw-owned constant so the raw side recognizes a pilot **without importing**
**`experiments`** — the import graph stays one-way. `run_label = "pilot"` is
deliberately *not* the authority, so ordinary historical pilot-labelled
fixtures keep working.

The writer was split: `_write_run_beneath(checked, run_name, parent_fd, …)` is
the shared body, and `_write_scoped_run` is the private door that accepts the
reserved identity and takes an already-opened parent descriptor. Marker-last,
`O_EXCL | O_NOFOLLOW`, the regular-file checks, cleanup and byte determinism are
unchanged — it is the same code, reached through a different parent.

`experiments.write_pilot_run(firewall, config, run_name)` opens the quarantine
as a pinned descriptor and writes **directly beneath it**, returning a
`QuarantinedPilotRun` **receipt** and never a `ClosedLedger`. There is no
write-then-move.

| Probe | Result |
| --- | --- |
| production entry exists after `write_pilot_run` | **False** — no transient path |
| `write_raw_run` on a reserved namespace | refused |
| `open_raw_run` on a manifest carrying the reserved namespace | refused |
| ticket-05 writer/reader regression on an ordinary namespace | unchanged |

`quarantine_pilot_run` survives as a documented legacy path for runs written
before the direct writer existed.

## 3 — Mechanical current-fact guard

New check, criterion **121**. Ten current facts are computed and required to
appear — 81 declared fields of which 76 are the design freeze, the four-value
count surface, 794 MB of matrix storage, Option B at 18 runs / 29 268 rows /
12.78 MB, Option A unpriced, `numerical_no_result`, the twelve searched
options, and "one blocked option and one machinery-only diagnostic" — and each
is then **mutated back to the exact superseded spelling** an independent review
found and required to be caught. Two historical controls assert that a round
record naming its own superseded numbers stays legal. The storage, row and run
figures are additionally compared against the live computation, so prose and
arithmetic cannot drift apart.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → 127/128, exit 1; `py_compile` and `compileall` clean;
`results/` absent; raw-import isolation unchanged; tree at its 29 entries.
Counts 502 callables / 1 318 invalid calls / 1 152 parameters.

|  |  |
| --- | --- |
| design digest | `8d1222adb431b4e244b7a3d05e7cbe29c3fe98e6005ea327df5cd3c4f97e7813` |
| proposal digest | `1b3c28da5df88d0574abd137cfb8a5d84c89687cff48d128c122c21a6cef2750` |
| `experiments.py` | `2d3c807fc2bf554fc72c2f1968314e0da542e740f08385db031cc358a345f5d0` |
| `verify.py` | `205ae341882d3c40e54b7831ed09dbbe29a5b30592de5a000d855571b5d6a5da` |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` |
| `README.md` | `fddb8dbc3525ed2d52c676b0c273f5e1f9199844dd0e48b7baf8b206a1aceb70` |

## Round-5 limitations

1. **The reserved prefix is a naming convention enforced at two doors**, not a
filesystem capability. A caller with `importlib` and a descriptor can still
write anywhere; this is anti-accident, described as that.
2. **`quarantine_pilot_run` still exists** and still moves. Nothing calls it in
the supported path, but it is reachable.
3. **The current-fact guard scans the README only.** The execution notes are
deliberately unscanned so historical rounds keep their own numbers.
4. Option A remains unpriced by omission, as ruled.
5. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 7 — the frozen pilot plan and the deterministic pilot fixture

Status stays **1**. **No pilot was run, no pilot exponent-related output was**
**opened, no approval or production-cleared state exists, Ticket 08 is untouched**
**at status 0, hash `6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

This round closes **two** of the round-5 review's four open items — the frozen
pilot design (its second P1) and the selection/rate half of its first P1 — and
the deterministic fixture the remaining two need. It does **not** close the
checkpoint-decision rebuild or the unified current-fact validator; those are
listed as outstanding below rather than described as done.

## Reproduced before any edit

| Probe | Before |
| --- | --- |
| caller-built `RangeSelection` → `reference_rate` | **accepted**, `1.0000000000000002` |
| `PowerEstimate` carries a `selection_digest` | **False** |
| `write_pilot_run(firewall, config, name, model=…)` | accepted an arbitrary config and either model |
| a wrong `run_label` at that door | `ValueError`, **`residue True`** — a quarantined directory blocking a correct retry |
| `PilotPlan` / `PostRangePlan` exist | **False** / **False** |
| proposal pilot vocabulary | two namespaces, two prefixes, an eligibility flag and a fingerprint list — nothing naming *which* pilot |
| proposal fields | 81 declared, 76 in the design freeze |
| `select_range` / `post_range_power` signatures | `(firewall, run_names)` / `(target, firewall, run_names)` |

Baseline before any edit: **127/127, exit 0**, `results/` absent, design digest
`36a8d23b8d46ab90…` — the frozen round-6 snapshot, confirmed.

## 1 — `PilotPlan`: the approved pilot, frozen

A factory-only record (`pilot_plan(...)`, its own construction token) naming the
role, the model, the run label, the ordered candidate couplings, the whole clock
grid with its derived spacing/parity/origin/support, the intended timestep and
the step count and observation window it implies, the pulse, noise, band and
dwell, 200 trials per cell and its derived shadow count, the execution blocking,
the reserved stream and run-name family, the count-only selection rule and its
three thresholds, and the source, environment and schema versions it was frozen
against. `require_plan_firewall` binds it to the firewall it was minted with.

`PilotPlan.require_manifest` rebuilds the **whole 45-key raw manifest** through
`raw_runner.raw_manifest(plan.config_for(coupling), plan.model)` and requires
field-for-field equality. That is a total check rather than a list of fields
somebody remembered.

`write_pilot_run(plan, firewall, coupling, run_name)` has **no configuration**
**parameter and no model parameter**; the review's width-only two-clock `dt=1`
two-trial run is not expressible. Every check — the plan/firewall join, the name
against both records, and the configuration derivation itself — runs **before**
**any directory is created**, so the `residue True` defect is closed structurally
rather than by ordering a cleanup.

The plan is re-checked at the **count door**: `_authoritative_cells` rebuilds
each quarantined run's manifest from the plan, so a directory placed in the
quarantine by any other route is refused at the recount as well as at the writer.

## 2 — The selection and the rate stop authorizing themselves

`reference_rate(plan, firewall, run_names)` has no selection parameter. It takes
one authoritative reopen/recount snapshot and computes the rate from the range
the frozen rule chose. `select_range` and `post_range_power` take the plan too.
`_rate_of` is the single expression every door uses, so a manifest and a
checkpoint cannot quote two rates for one range.

The proposal binds **`pilot_plan_digest`**, `pilot_candidate_couplings` and
`pilot_trials_per_cell` inside the design freeze: **84 declared fields, 79 in the**
**design freeze, five declared exclusions**, source map at 84.

## 3 — The deterministic pilot fixture

Verifier-only. Four cells, one per declared candidate coupling — the proposed
matrix's own first four nodes, bit for bit — each a real quarantined pilot run
whose committed and unresolved histories are **cloned and reindexed** to the
plan's declared 200 trials, 100 commitments and 100 survivors per cell against
the frozen 20-and-20 minimum. Exposure is recomputed through
`raw_race.exposure_of`, tables through `raw_ledger.encode_table`, marker and
manifest digests rebuilt, and every cell passes `require_closed_ledger`. Bytes
are written **directly beneath the quarantine** and the tree is removed in
`finally`. Cost: ≈ 5 s.

**The honest part.** The frozen production plan is 64 clocks at
`dt = 1.953125e-3` — about forty-three hours, which is exactly the work
checkpoint 1 has not authorized. Rather than write that plan's manifest over
cheaper rows, the fixture declares what it is: a **second plan**, minted through
the same public factory, honestly stating eight clocks and `dt = 0.05`, at the
same 200 trials per cell and the same firewall and run-name family. The suite
asserts **both directions** — the fixture's runs are authoritative under the
fixture plan and are **refused under the production plan**, on
`['clocks', 'grid_spacing', 'detunings', 'timestep', …]`. Because the fixture's
couplings are the production plan's own nodes, that refusal is about being a
different experiment and not about an unknown coupling.

## What changed

`experiments.py`: the plan section, the plan-driven writer, plan revalidation at
the recount, the authoritative `reference_rate`, `_rate_of`, three new proposal
fields with rules and source-map entries, and the "moved" prose corrected to
direct-write at `QUARANTINE_DIRNAME` and in `PilotFirewall`. `verify.py`: the
fixture builder and its two plans, the probe plan the exported-surface rows run
under, strengthened `check_pilot_firewall` and `check_range_selection`, and the
census rows. `README.md`: the pilot-plan paragraph, the direct-write lifecycle,
the authoritative-door paragraph, and the counts.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall`
clean; `results/` absent on every path; tree at its 29 pre-existing entries;
nothing staged, committed or reverted. Counts **510 callables / 1 347 invalid**
**calls / 1 223 parameters**, criteria 110–121 unchanged. No test was removed or
renamed; every change is additive or strengthening.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `15709e8685793eee5ee8d44eff0bb26fa3dd3f92c2d860c7bf7ad68ba3d23e57` |
| `verify.py` | `e2bb692534e201aea58832003196178604586353012063a53f7030113b74f629` |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `README.md` | `a9a53349e41ca1d3a99e16987cfa09de67c5a0160ba4b16052c76f4b99f95709` |
| `__init__.py` | `aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b` (unchanged) |

Design digest `4b0589fbe2ae469b…` (was `36a8d23b8d46ab90…`; every manifest
digest moved, and no durable pilot or production run existed to invalidate).

## Round-7 limitations, and what is **not** done

1. **`PostRangePlan` was not built.** The post-range join is authoritative — one
snapshot, plan-checked, no selection or rate parameter — but there is still
no single record binding `pilot_plan_digest`, the ordered closure digests, a
`selection_digest`, the target/power digests and a derived status.
`PowerEstimate` still carries no `selection_digest`.
2. **The checkpoint decision is still a caller's to give.** `checkpoint_one_handoff`
now takes and binds the plan, but it still accepts caller-built
`alternatives` and a caller-built pilot `CostLine`. The review's costed
Option A with a forged physical claim, and its one-second pilot line, are
**not** yet refused. The negative probes for them are not written.
3. **The unified current-fact validator is not built.** The guard still scans
`README.md` only and still mutates seven of its ten entries; the stale
statements the review found in `experiments.py` and `verify.py` docstrings
and in the verbose output — priced campaign stages, "two costed
alternatives", the provenance digest on the count surface — are **not**
corrected. The two direct-write statements and the "five keys" comment are.
Machine timings are still presented without an environment/benchmark digest.
4. **The fixture is a fixture.** Its rows are real races cloned to a declared
trial count under a declared plan; it is not a pilot and no number is read
from it.
5. **`raw_config` accepts a non-finite `pulse_centre`.** Found while writing the
plan factory's invalid-input probes; the parameter is exempted in the census
with a note. It is a pre-existing latent gap in a ticket-05 module and was
deliberately not fixed here.
6. **Round 6 is still undocumented.** Its changes are visible in the code — the
proposal factory's `pilot_run_names` snapshot and `selection_digest`, and a
`_t07_api_reference_rate` helper that was unreachable — but no note records
them, and this round did not invent one.
7. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands, the
proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 6 — reconstructed from the code and the coordinator's record

**This section was not written when round 6 was done, and it is not an**
**independent measurement.** Round 6 left `experiments.py` and `verify.py`
changed with no note; the two items below are the coordinator's record of what
it changed, checked against the bytes that were in the tree at the start of
round 7. Nothing here was re-measured, and no digest is quoted for it.

1. **Proposal-boundary authority.** The caller `selection` argument was removed
from `proposed_production_manifest` and `require_authoritative_proposal` and
replaced by ordered `pilot_run_names`; the selection and the contraction
rate are recomputed inside the factory from one authoritative quarantine
recount. Confirmed in the bytes: the factory took `pilot_run_names=()` and
recomputed both, and `check_range_selection` asserted the factory had no
`selection` parameter.
2. **The legacy mover was made private.** `quarantine_pilot_run` became
`_quarantine_pilot_run`, left `__all__`, and refuses current reserved
`xpilot-` identities before moving. Confirmed in the bytes.

Round 6 also left an unreachable `_t07_api_reference_rate` helper in `verify.py`
calling `reference_rate(firewall, run_names)` — a two-argument signature the
module did not yet have. Round 7 made that signature real and the helper
reachable.

# Fix-up round 8 — the authority boundary closed

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

This round closes the two remaining round-5 review items — the checkpoint
decision and the current-fact validator — and the half of the selection item
round 7 left open.

## 1 — A correction to round 7, found first

Round 7's `pilot_plan` factory **never passed `pulse_centre` into the**
**configuration it derived**, and neither did `PilotPlan.config_for`. A plan
declaring a non-zero pulse centre silently recorded and rebuilt `0.0`.

The coordinator's ruling described this as a `raw_config` gap. It is not:
`raw_config.RawEventConfig` validates `pulse_centre` with `require_finite` and
refuses NaN, `+inf` and `-inf`, which was reproduced before anything was
changed. The gap was **round 7's own**, in `experiments.py`, and it is fixed
there rather than at the ticket-05 boundary — no ticket-05 module was touched.
The census exemption round 7 took for the parameter is removed and a real
NaN probe stands in its place; the plan now round-trips a declared centre of
0.75 through `config_for` into a 45-key manifest that `require_manifest`
accepts.

## 2 — D: the checkpoint decision is no longer a caller's to give

`checkpoint_one_handoff` has **no `alternatives` parameter and no `pilot_line`**
**parameter**. It takes the frozen plan and the campaign and rebuilds all three
records internally through `checkpoint_alternatives` and
`pilot_cost_from_plan`, priced from the slowest measured benchmark and the
resource estimate's own safety factor, so the pilot and the matrix are costed
on one convention.

The forged decisions are now **inexpressible**, not merely rejected.
`CheckpointAlternative` gained `supports_class`, a member of the closed
`SUPPORT_CLASSES`; there is no member licensing a physical, causal or scaling
claim, and `ALTERNATIVE_CONTRACT` ties each label to its required class and to
whether it may be priced. So the review's costed Option A carrying
`supports = "a physical scaling claim"` fails twice — on the class and on the
price — and the one-second pilot line has no parameter to arrive through. Both
are exercised as negative probes, together with an unpriced narrowed claim and
a narrowed claim borrowing the unpriced class.

Option B's numbers are derived rather than declared: the trial count is the
disposition's own `probability_admissible_trials`, the run count is arms times
coupling nodes, and each distinct clock count takes its own row blend.

## 3 — C: `PostRangePlan`, and a power estimate that can be joined back

`PostRangePlan` is factory-only under its own token and binds
`pilot_plan_digest`, `firewall_digest`, the ordered run names, **one closure**
**digest over all of their whole-five-file closures**, `counts_digest`,
`selection_digest`, the range, the reference rate, `target_digest`,
`power_digest`, `power_verdict`, and a **derived** `status` re-derived in
`__post_init__` from the refusal and the power verdict.

`_post_range_snapshot` is the single reopen-and-recount every post-range door
goes through — `post_range_power`, `post_range_plan` and the proposal factory —
so a proposal cannot quote a range from one read of the quarantine and a rate
from another. `PowerEstimate` now carries `selection_digest`: required on a
`post_range_join` estimate and refused on a provisional one, so a post-range
record can be joined back to the range that sized it. The proposal binds
`post_range_digest` and `post_range_status`: **86 declared fields, 81 in the**
**design freeze**, five declared exclusions, source map at 86.

Exercised against the deterministic fixture: status `post_range_powered` over
four cells, the plan/firewall/target digests all bound, and the power record's
selection digest equal to the plan's.

## 4 — E: one validator, every source, every mutation

`_validate_current_facts` is the single function used by the live scan, by
every current-to-stale mutation and by the historical controls.

`_live_prose_sources` scans six live surfaces: `README.md`, `experiments.py`,
`raw_runner.py`, `__init__.py`, the verifier's **printed** banner lines, and
**every string literal in `verify.py`** taken through `ast` — docstrings, check
descriptions and the literal parts of every `Result` detail f-string — with
exactly two functions skipped, the fact table and this guard, which necessarily
spell superseded values out.

The historical execution notes are excluded **by scope**: they live outside the
package and the scanner resolves nothing outside it. That exclusion is asserted
rather than assumed, and three historical round sentences are passed through
the same validator *as if live* and required to be flagged — which is what
proves the detector is real while a round record stays free to name its own
numbers.

**Twelve facts, every one with both spellings, every one mutated back and**
**caught.** The three round-5 found unmutated — the superseded design digest, the
numerical verdict and the searched-option count — now carry mutable spellings,
and two new facts cover the direct-write lifecycle and the frozen plan.

Stale live statements corrected this round: the "two costed alternatives"
framing in the vocabulary comment, the section header, the
`CheckpointAlternative` docstring, the check description, the check detail and
the campaign note; the campaign's "the cost is a **range**" docstring and its
lower/upper-bound note; the printed "moved into" lifecycle; and the printed
claim that the four-value count record exposes a provenance digest.

**Machine timings are labelled.** The README states that every wall-time figure
is a machine-dependent snapshot, names the environment/benchmark-digest/
proposal-design-digest it was taken under, says the live numbers are re-derived
by the verifier on the machine that runs it, and tells a reader to quote the
row, storage and run counts and take the hours from their own run. The bare
`≈ 43 h` pilot figure and the `≈ 11.5 h` Option B figure are gone; the
reproducible parts — 18 runs, 29 268 rows, 12.8 MB — stand.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; raw import isolation and the ticket-05
writer/reader regression pass inside the green run; the working tree is at its
**29 pre-existing entries**; nothing staged, committed or reverted. Counts
**518 callables / 1 363 invalid calls / 1 257 parameters**, criteria 110–121
unchanged. No check was removed, renamed or weakened; the checkpoint check's
*description* changed because its old wording was one of the stale statements
this round had to fix.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `f763243d9712482553e24c8f016db7d5d0834b3dadd716c549cfd55bae914613` |
| `verify.py` | `dfe964eec66c6a8fd34773d39a0917e87931fbcffc8dea23e52d712178468369` |
| `README.md` | `c06943c5aebfcd803bb4c23a65d61c8443912ebf385d05a4d973b1da6308f45a` |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |
| `__init__.py` | `aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b` (unchanged) |

Design digest `064998ab04d8ab87…` (was `4b0589fbe2ae469b…` at round 7 and
`36a8d23b8d46ab90…` at the round-6 freeze). Every manifest digest moved again;
no durable pilot or production run exists, so nothing was invalidated.

## Round-8 limitations

1. **The fixture is verifier-only and is not a pilot.** Its rows are real races
cloned to a declared trial count under an honestly declared second plan at
eight clocks and `dt = 0.05`. It is **not evidence about production**
** performance** and no scientific number is read from it; it exists to prove
that the authoritative doors are driven by bytes on disk.
2. **The `verify.py` literal scan skips two functions by name.** The fact table
and the guard itself must spell superseded values out. Everything else in
the file is in scope, but a stale statement moved into either of those two
functions would not be seen.
3. **`_quarantine_pilot_run` still exists** and still moves. Nothing on the
supported path calls it.
4. **The campaign has still never run**, and Option A is still unpriced by
omission — the four end-to-end kernels were deliberately not benchmarked.
5. **The two free-text proposal fields** are still taken from the record by
classification; a wrong `status_reason` is undetectable and is not a
statement about the experiment.
6. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 9 — the round-8 review's five findings

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

Every finding was reproduced against the frozen round-8 bytes before any edit.

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| four-cell fixture post-range join | **`post_range_powered`** with arms 8 419 / **22 211** / 8 419 against a declared ceiling of 20 000 | `post_range_no_powered_matrix`, reason names `central_control at 22211` |
| `dataclasses.replace` power, `post_range_join`, `selection_digest=f*64`, beside four real runs | **accepted**; proposal `power_digest` ≠ `PostRangePlan.power_digest` | refused at the proposal, and the proposal binds the snapshot's own digests |
| the four runs in **reverse** | **accepted**, returned a selection | `ValueError`: "these are not the approved pilot's runs" |
| one cell **omitted** | scientific `post_range_refused / run_too_short` | authority `ValueError`, not a scientific result |
| sealed plan with false Python/NumPy/platform/config digest | **accepted**; proposal recorded the *live* environment beside it | refused, naming the disagreeing fields |
| the verifier fixture plan at the production proposal | **accepted** | refused by declared purpose |
| live-prose scope | 4 modules + verifier strings; 16 package modules unscanned | **22 sources**, discovered |

## 1 — the affordability ceiling binds every arm

`_finish_power` compared only the paired arms' shared count. It now compares
**every sized arm** and names each one that exceeds the ceiling, so an unpaired
central control at 22 211 against a declared 20 000 is a refusal rather than a
`powered` verdict. The exact boundary is controlled from both sides: a ceiling
at the worst arm's own count admits the join and one trial below it refuses.

## 2 — the proposal consumes the authoritative post-range power

When `pilot_run_names` is given, the factory takes **one** snapshot and binds
*its* estimate: a supplied power record that is not the snapshot's is refused,
and `power_digest`, `power_stage`, `power_verdict`, `selection_digest`,
`post_range_digest` and `post_range_status` all come from that snapshot. A
proposal naming no runs while carrying a `post_range_join` estimate is refused
too.

Two joins were made **stage-aware**, and this is a real change rather than a
loosening: the `target_digest` equality and the matrix/power `arm_trials`
equality are pre-pilot checks. After a pilot the estimate is re-sized against
the *selected* range — a narrower target derived from the supplied one — and a
matrix re-derived with it is ticket-08 work. Post-range records are bound to
their snapshot instead. Nothing in this ticket produces a post-range production
proposal; the frozen one is pre-pilot and both equalities still apply to it.

## 3 — exact pilot identity and order

`PilotPlan.run_names` derives the ordered run name of every declared cell, and
`run_name_for` / `coupling_for` freeze the mapping inside the plan digest.
`require_run_names` demands **set, length, order, uniqueness and the one-to-one**
**coupling mapping** before anything is read, and a miss is an **authority**
refusal with a message that says so. The writer refuses a declared coupling
written under another cell's name. The recount refuses a run whose
`peak_coupling` is not the one the plan writes under that name.

The closure digest is built from **one ordered record per run** — name,
coupling and closure together. The previous construction zipped the caller's
original name order against a coupling-sorted closure list, so a reordered call
paired each name with another run's closure and still produced a well-formed
digest. Nothing is zipped now.

Mutations added for reordered, omitted, duplicated, extra, foreign and swapped
run sets, against both `select_range` and `post_range_plan`.

## 4 — plan authority, and a purpose that cannot be relabelled

`require_authoritative_plan` **rebuilds** the plan: its declared design inputs
go back through `pilot_plan` together with the **trusted live** source
fingerprint and live schema versions, and every field is compared. A plan
carrying a false Python version, NumPy version, platform, source digest,
configuration digest, schema version, derived grid spacing, derived step count
or derived shadow count is refused before any decision. It is called at the
writer, at the recount, at the proposal and at the checkpoint.

`PILOT_PURPOSES` separates the verifier fixture from the approved pilot, and
the production doors take `approved_production_pilot` only. **The purpose is**
**not a label a caller can restate**: `FIXTURE_PREFIX_MARKER` ties it to the
run-name family, so a fixture relabelled `approved_production_pilot` does not
build — the prefix contradicts the purpose — and neither does a production plan
carrying the marker. Fixture plans keep their use for count mechanics; they
reach no decision.

## 5 — live-prose scope by discovery

`_live_prose_sources` now **discovers** its scope: every Python module in the
package directory plus the README, with one documented exclusion — `verify.py`
itself, scanned separately through `ast` because two of its functions must
spell superseded values out. The rule is stated rather than the files listed.
It **fails closed**: fewer than fifteen discovered modules raises, and any
package module missing from the scanned set is a failure, so a module added
later is scanned rather than silently exempt. **22 sources**, 19 modules, and a
stale claim planted in each of three other discovered modules is required to be
caught. The twelve mutation controls and the three historical controls are
unchanged and still run through the same validator; the execution notes remain
outside by scope. No false positives were introduced.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; raw import isolation and the ticket-05
writer/reader regression pass inside the green run; tree at its **29**
**pre-existing entries**; nothing staged, committed or reverted. Counts **523**
**callables / 1 373 invalid calls / 1 266 parameters**, criteria 110–121
unchanged. No check removed, renamed or weakened.

Preserved: direct-to-quarantine writing with `O_NOFOLLOW` and the five-file
closure, the non-zero pulse centre threading, unpriced Option A, Option B at
exactly 18 runs / 29 268 rows, schema-v3 fail-closed, and the narrow scientific
boundary. The proposal grew from 84/79 to **86/81** in round 8 and is unchanged
here.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `21c95b717da80f94ba19418ac660b6a5818852be38a44fc415fae18990f7d1d6` |
| `verify.py` | `11b52e029032a794bc845023bc60279e7398223677f1ec68275cd42263f76afd` |
| `README.md` | `228761ee13d5e00c53a064fff6cfb9f182b808ae6aea2996a3b09b570e558d2a` |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |
| `__init__.py` | `aa8cba800a986cc099301669c3d720ba5b38f74c2e2b170a3a4b6fb5ba495a5b` (unchanged) |

Design digest `08b5dc14ab5a0a36…` (was `064998ab04d8ab87…`).

## Round-9 limitations

1. **A post-range production proposal is not a coherent record yet.** The
matrix would have to be re-derived at the re-sized counts, which is
ticket-08 work; the two joins that would have caught that are now pre-pilot
only. Nothing here produces such a proposal.
2. **`_t07_probe_production_plan` declares `approved_production_pilot` at eight**
** clocks.** It exists for exactly one probe — that a forged post-range power
is refused beside real runs — and the purpose gate separates *declared*

- fixtures*, not "plans with the right physics". The frozen pilot is
 `_t07_plan`; nothing is decided from the probe plan.

3. **`FIXTURE_PREFIX_MARKER` is a naming convention**, enforced at the plan
factory. It makes the purpose and the run-name family contradict each other
when either is restated alone; it is not a capability.
4. **The `verify.py` literal scan still skips two functions by name.**
5. Option A remains unpriced by omission; the campaign has never run.
6. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 10 — the round-9 review's three findings

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

All three findings were reproduced against the frozen round-9 bytes first, with
the review's own digests.

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| probe-plan post-range proposal | **accepted**: power 8 419/22 211/8 419 at target digest `3555436d…` serialized beside matrix 2 406/6 346/2 406 at digest `50f3feff…` — two designs in one record | refused |
| the same estimate beside the pre-pilot target and matrix | accepted | `ValueError` naming **`post_range_matrix_not_derived`** |
| eight-clock, `dt = 0.05`, four-cell plan declaring `approved_production_pilot` | **passed** `require_authoritative_plan` and drove the proposal | refused: "this is not the approved production pilot" |
| `compare.py:83`, `compare.py:232`, `__init__.py:135-136` | said the production numerical budget does not exist / belongs to a later ticket | corrected; zero stale occurrences across all 22 discovered sources |

## 1 — one design per proposal, or a named refusal

The two stage-aware exemptions round 9 introduced are **gone**.
`target_digest` equality and matrix/power `arm_trials` equality apply
unconditionally again. The snapshot is now taken **before** any join, the
authoritative estimate replaces the supplied one, and
`_require_post_range_design` then refuses by name when the target and matrix
beside it are still the pre-pilot ones.

The choice the review offered was "derive the coherent post-range records, or
fail closed with a named reason". This **fails closed**: deriving a post-range
target, matrix and resource estimate is ticket-08 work and this ticket does not
do it. The rule is factored into its own function precisely so it can be
exercised — the outer canonical-plan gate means no fixture plan reaches the
factory, and a rule that cannot be reached cannot be trusted. Both directions
are controlled: the coherent pre-pilot design passes it.

The fixture's post-range state is asserted to be
`post_range_no_powered_matrix`, because it exceeds the declared affordability
ceiling; it cannot produce an approval proposal. Mismatch probes run at all
three doors — the proposal factory, the authoritative rebuild and the
checkpoint handoff — and each is required to refuse **and to name** either the
post-range reason or the canonical-plan one. **No within-ceiling positive**
**control is claimed**, because none exists yet: it would need a genuinely
re-derived coherent matrix, which is exactly what is not built.

## 2 — canonical production pilot identity

`PRODUCTION_PILOT_SPEC` freezes the approved pilot's constants;
`canonical_pilot_plan(firewall, fingerprint)` builds it from them plus the
trusted live fingerprint and live schema versions; and
`require_canonical_pilot_plan` requires **field-for-field and digest** equality
at the production proposal and, through it, at the checkpoint. Purpose and
prefix self-consistency were never identity, and the review's replay proves it:
its eight-clock plan met every self-consistency rule.

`_t07_plan()` is now `canonical_pilot_plan(...)` rather than a restatement, so
there is exactly one place the approved numbers live.
`_t07_probe_production_plan` is **deleted**. The inner power-digest join is
tested through the module's own private helper `_require_snapshot_power`
against a real authoritative snapshot, which is the sanctioned route. Probes
added: the exact eight-clock approved-purpose replay at a production door, at
the proposal, and **thirteen one-field mutations** across every declared
production-plan input, each refused.

Generic, fixture and probe plans keep their use at the lower count and power
doors; none reaches a production decision.

## 3 — budget provenance, and one live-source set

Corrected: `compare.py`'s module docstring and its `PRODUCTION_GATE` comment,
and `__init__.py`'s stage-9 paragraph. All three now say the budget ticket 07
froze **exists and is not met**. The two `compare.py` statements about
`PRODUCTION_STATUS_SCHEMA` not existing are left alone — schema v4 genuinely
does not exist, and that is ticket 06's fail-closed permission.

`check_stale_stage_strings` no longer keeps its own four-module idea of "live":
it uses `_live_prose_sources()`, the same discovered set the current-fact
validator uses, and the affirmative "is **not met**" statement is now required
in `compare.py` and `__init__.py` as well as in the README, the raw runner and
the printed banner. Three budget-provenance facts joined the unified fact
table, each with both spellings and each mutated back and caught.

The literal scan skips **three** functions now, and only three — the fact
table, the current-fact guard and the stale-stage guard — each of which must
spell superseded values out in order to look for them. **22 discovered sources**
under the documented rule: every package Python module plus the README, with
`verify.py` scanned separately through `ast`.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; tree at its **29 pre-existing entries**;
nothing staged, committed or reverted. Counts **525 callables / 1 378 invalid**
**calls / 1 271 parameters**, criteria 110–121 unchanged. No check removed,
renamed or weakened.

Preserved: the all-arm affordability check, exact run order and identity,
ordered closure alignment with no cross-order zip, refusal of false
environment/source/schema/config digests, direct-to-quarantine writing, Option
A unpriced, Option B at exactly 18 runs / 29 268 rows, the 17-row / 12-option
scientific boundary, schema-v3 fail-closed, and no downstream activity.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `1baf7013c3d10d4a2f3050ef3b9b0d948fa4ff9e8b5e90a9bda9a05fcd12f672` |
| `verify.py` | `494aae89c4fee77e89cc4564a9668eeaaa1ddd3d9d2442265e8a9ed83e5dcbb3` |
| `README.md` | `3a99c991b1c430789c6899a186e1b5daa7046351a513dedce4cf36ca27507868` |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |

Design digest `a84750ce21edb5c2…` (was `08b5dc14ab5a0a36…`). Canonical pilot
plan digest `5b55647ef587b065…`.

## Round-10 limitations

1. **There is no post-range production proposal, by construction.** The
post-range target, matrix and resource estimate are not derived; the factory
refuses by name until they are. That derivation is ticket-08 work and is not
attempted here.
2. **No within-ceiling positive control exists.** One would need a genuinely
re-derived coherent matrix, which is the same missing work as (1). The
fixture is deliberately over the ceiling and its state blocks.
3. **`PRODUCTION_PILOT_SPEC` is declared, not derived.** Its couplings are the
matrix's own six nodes written out as literals; the suite asserts the frozen
plan and the canonical plan agree, but a change to the matrix's grid would
have to be made in both places.
4. **`FIXTURE_PREFIX_MARKER` remains a naming convention** enforced at the plan
factory, and the literal scan still skips three functions by name.
5. Option A remains unpriced by omission; the campaign has never run.
6. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 11 — the serial round-10 review's two findings

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

Both findings were reproduced against the frozen round-10 bytes first. All runs
this round were **serial**, with `results/` removed between them.

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| a valid, honestly resource-priced six-node matrix with every target coupling × 1.1 | **accepted** at the proposal, the authoritative rebuild **and** the checkpoint; the record carried `peak_couplings[0] = 0.55` beside `pilot_candidate_couplings[0] = 0.5` | refused at all three, naming `peak_couplings` and printing what each record said |
| `Checkpoint1Handoff` ticket-08 field | absent, in the record and in `summary()` | derived `ticket_08_derivation_status = "not_started"` |
| `requested_decision` mentions ticket 08 | **no** | states no post-range production proposal exists and that ticket-08 derivation has not begun |

## 1 — one experiment, or a named refusal

Every join in the factory compared *counts and digests*; none compared the
physics the records share. A matrix and a pilot plan could each be internally
consistent, each carry an honest digest, and describe two different
experiments.

`SHARED_PHYSICAL_FIELDS` names the overlap once, and
`shared_physical_identity` builds the table so a reader can inspect it: the
coupling grids at **exact ordered binary64 equality**, the cell count, the
clock count, the grid half-width and support, the timestep, the pulse duration
and centre, the phase diffusion, the lock tolerance, the dwell time, the shadow
fraction, the arm names, the per-arm clock counts, the arm the pilot runs, and
the control arm the reference-rate rule is about. Only the records that
actually carry a field appear under it, so the comparison is over genuine
overlaps rather than invented defaults.

`require_shared_physical_identity` is called at proposal construction, and
therefore at the authoritative rebuild and the checkpoint, which both go
through it. The refusal **names the disagreeing field** and shows each record's
value.

Probes: the review's exact 1.1× reproduction at all three doors; a check that
the refusal names `peak_couplings`; **ten one-field variations** — clocks, grid
half-width, timestep, pulse duration, pulse centre, phase diffusion, lock
tolerance, dwell time, shadow fraction and the pilot arm — each required to be
refused *and named*; a table/field-set agreement check; and the coherent
pre-pilot records as the positive control.

## 2 — the checkpoint says what has not begun

`Checkpoint1Handoff` carries a **derived** `ticket_08_derivation_status`, whose
vocabulary `TICKET_08_DERIVATION_STATUSES` has exactly one member,
`not_started`. There is no factory parameter for it. It appears in the record,
in `summary()` beside an explicit `post_range_production_proposal: None`, in
the `requested_decision` text, and in the README.

The wording is deliberately narrow: it states **what exists**, and says in the
same sentence that it is *not* a statement that ticket 08 is authorized. The
suite asserts that, asserts the field is derived rather than supplied, refuses
a handoff claiming `in_progress`, and pins both the field and the prose in the
unified current-fact guard with stale variants that mutate and are caught.
Ticket 08's own status and hash remain checked separately, as independent
evidence.

## Verification

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; tree at its **29 pre-existing**
**entries**; nothing staged, committed or reverted. Counts **527 callables /**
**1 383 invalid calls / 1 278 parameters**, criteria 110–121 unchanged. No check
removed, renamed or weakened.

Preserved: the round-10 fail-closed post-range boundary, canonical plan
identity, live budget provenance, the all-arm affordability check, exact run
order and identity, ordered closure alignment, false environment/source/schema/
config refusal, direct-to-quarantine writing, Option A unpriced, Option B at
exactly 18 runs / 29 268 rows, schema-v3 fail-closed, and the 17-row /
12-option scientific boundary.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `fd688b5c23b6f28c9f66d99dcd972f1c66d017527544459e5a47dc0001689b92` |
| `verify.py` | `0e8c9ddc4a6f411fc0d68b735171576779b69158b0ec512e679be29576e3eeed` |
| `README.md` | `b8fe328eb12cfdfa716d254368618dd467ace6589d4fe0a18fa6d42cd64da16d` |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (unchanged) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (unchanged) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |

Design digest `4da165f3c294c07b…` (was `a84750ce21edb5c2…`). Canonical pilot
plan digest `296fff87710da4a6…`.

## Round-11 limitations

1. **The shared-physical table is a declared overlap.** It covers every field
two of the three records carry today; a field added to one record later is
not compared until it is added here. The suite asserts the table's key set
equals `SHARED_PHYSICAL_FIELDS`, which catches a silent edit but not an
omission at design time.
2. **`ticket_08_derivation_status` has one member**, so it is an assertion this
ticket cannot contradict rather than a measurement. That is deliberate: this
ticket derives no post-range records, and a vocabulary that could say
otherwise would be a field a later caller could set.
3. Everything carried forward from round 10: no post-range production proposal
by construction, no within-ceiling positive control,
`PRODUCTION_PILOT_SPEC` declared rather than derived,
`FIXTURE_PREFIX_MARKER` a naming convention, and three functions skipped by
the literal scan.
4. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 12 — the presented decision is derived, not written

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| `checkpoint_one_handoff(..., requested_decision="approve the presented choice")` with coherent authoritative components | **accepted**; `ticket_08_derivation_status="not_started"` and `post_range_production_proposal=None` were both correct, and the sentence a reader is shown said none of it | `TypeError` — there is no such parameter |
| a handoff constructed with that replacement text | accepted | `ValueError`, naming the omitted clauses |
| the canonical text with any one clause removed | — | `ValueError` for each of the three |

The finding is worth stating plainly: **every derived field was right.** The
defect was that the one sentence a human actually reads was a caller's to
write, so a correct record could be presented with an incorrect summary. A
derived field nobody reads is not a presentation.

## What changed

`CHECKPOINT_DECISION_CLAUSES` names the three invariants separately —

1. *There is no post-range production proposal.*
2. *Ticket 08 matrix derivation has not begun.*
3. *Ticket 08 is not authorized.*

— and `CHECKPOINT_REQUESTED_DECISION` is assembled from them, once, with a
closing sentence that the last two state what exists and what has not been
done and that neither is a request to authorize ticket 08.

`checkpoint_one_handoff` **has no `requested_decision` parameter**; it passes
the constant. `Checkpoint1Handoff.__post_init__` compares the presented text to
that constant **exactly** and, when it differs, names which clauses are
missing. Removing any single clause is therefore refused, and so is the
review's replacement text.

The previous guard — `if "authorized" in lowered and "not a statement that" not in lowered` — is **gone**. It passed vacuously on any text that simply
omitted the word, which is exactly how missing text stayed legal. Exact
equality against the canonical constant replaces it, with a per-clause
containment check beside it so a failure says which invariant went missing.

README carries the same three sentences verbatim, and the unified current-fact
guard pins the non-authorization clause alongside the post-range-absence and
ticket-08-derivation facts — three facts, each with both spellings, each
mutated back and caught.

## Verification (serial)

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; tree at its **29 pre-existing**
**entries**; nothing staged, committed or reverted. Counts **527 callables /**
**1 382 invalid calls / 1 277 parameters**, criteria 110–121 unchanged. No check
removed, renamed or weakened.

Round-11's shared-physical-identity joins and every earlier closure are
preserved: the 1.1× coupling-grid refusal and its per-field probes, canonical
plan identity, the fail-closed post-range boundary, all-arm affordability,
exact run order and identity, ordered closure alignment, false
environment/source/schema/config refusal, direct-to-quarantine writing, live
budget provenance, unpriced Option A, Option B at exactly 18 runs / 29 268
rows, the 17-row / 12-option scientific boundary, and schema-v3 fail-closed.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `61d85c0d56c0ae72ce3aa61bbd464ff2b4ba5d28def02b076840be3ee923ad88` |
| `verify.py` | `e4b3a300fd0b2b3f30b11dc81bf83c2eca16686ca2815bdef24182969983fe6b` |
| `README.md` | `022149ddef1b4ac620f181d9f68a32f3a9931e6da460ce83104e74ccce1854c9` |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (unchanged) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (unchanged) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |

Design digest `aa321492bdef87d7…`.

## Round-12 limitations

1. **The canonical text is one string.** Its clauses are pinned and mutated,
but a future edit that rewrote all of them consistently would still pass;
what is enforced is that the presentation and the constant agree, not that
the constant says the right thing. The three clauses are the checkable part.
2. Everything carried forward from round 10 and 11 stands: no post-range
production proposal by construction, no within-ceiling positive control,
`PRODUCTION_PILOT_SPEC` declared rather than derived, `FIXTURE_PREFIX_MARKER`
a naming convention, and the literal scan skipping three functions by name.
3. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Fix-up round 13 — non-authorization as an observable fact

Status stays **1**. **No pilot was run, no campaign stage was run, no pilot**
**exponent-related output was opened, no approval or production-cleared state**
**exists, Ticket 08 is untouched at status 0, hash**
**`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.**

## Reproduced, then closed

| Probe | Before | After |
| --- | --- | --- |
| `Checkpoint1Handoff.summary()` keys about ticket 08 | only `ticket_08_derivation_status` | that **and** `ticket_08_authorization_status` |
| any observable non-authorization fact | **none** — the statement existed only inside the presented sentence | `ticket_08_authorization_status = "not_authorized"` |
| `ticket_08_authorization_status` as a handoff field | absent | present, derived, closed at one member |

Round 12 made the presented *sentence* canonical, and that closed the wording.
It did not make the fact **observable**: a reader or a downstream consumer had
to parse prose to learn that ticket 08 is not authorized, while
"not started" sat beside it as a structured value. Those are different facts —
work can be unauthorized and also not begun, and neither implies the other — so
the second is now a field rather than a clause.

## What changed

`TICKET_08_AUTHORIZATION_STATUSES = ("not_authorized",)`, and
`Checkpoint1Handoff` carries `ticket_08_authorization_status` beside
`ticket_08_derivation_status`. Both are **derived**: neither has a factory
parameter, both are validated by `_require_member` in `__post_init__`, and both
are inside the handoff digest and in `summary()`. `authorized` is not a value
the vocabulary can spell rather than one a guard happens to reject.

`summary()` now carries all three observable facts together —
`ticket_08_derivation_status = not_started`,
`ticket_08_authorization_status = not_authorized`, and
`post_range_production_proposal = None` — and the suite asserts each key and
each value.

Direct-construction refusals added for `"authorized"`, `"AUTHORIZED"`,
`"not_started"`, `"conditionally_authorized"` and `""` (all `ValueError`), and
for `None`, `True` and `1` (all `TypeError`). The current-fact guard pins the
field and its value as its own fact, alongside the non-authorization clause of
the canonical decision text, which is unchanged.

Nothing else changed: the round-12 canonical decision text and its three
clauses, the round-11 shared-physical joins, the round-10 fail-closed
post-range boundary and canonical plan identity, and every earlier closure are
untouched.

## Verification (serial)

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; tree at its **29 pre-existing**
**entries**; nothing staged, committed or reverted. Counts **527 callables /**
**1 383 invalid calls / 1 278 parameters**, criteria 110–121 unchanged. No check
removed, renamed or weakened.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e` |
| `verify.py` | `bb2b8dd07cea6b3a8c82644d189e2d468604fc758863af2540af0f3e218554ff` |
| `README.md` | `4f48a3140574e1014301536cb6e8e8e56647f2f2b2858613037e69595c22c521` |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (unchanged) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (unchanged) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (unchanged) |

Design digest `ee530c06191e9792…`. Ticket 08 remains status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`, checked as
independent evidence beside the derived fields rather than in place of them.

## Round-13 limitations

1. **`not_authorized` is a statement this package makes about itself.** It is
structurally the only value the type can hold, which is the right property
for a ticket that cannot authorize anything; it is not a cryptographic
assertion and the Ticket-08 status/hash check remains the independent
evidence beside it.
2. Everything carried forward from rounds 10–12 stands: the canonical decision
text is one string whose three clauses are the checkable part, no post-range
production proposal by construction, no within-ceiling positive control,
`PRODUCTION_PILOT_SPEC` declared rather than derived,
`FIXTURE_PREFIX_MARKER` a naming convention, and the literal scan skipping
three functions by name.
3. `numerical_no_result` blocks, `no_feasible_matrix_among_searched` stands,
the proposal is `checkpoint_blocked`, and no pilot has been run.

# Reconstruction baseline R1 — subtraction of unauthorized Ticket 08 additions

**This is not round 13, and it is not a byte restoration of it.** An
unauthorized Ticket 08 run edited `verify.py` and the package `README.md` and
added `production.py`. No copy of the round-13 bytes exists — the package is
untracked, so there is no git object; no backup was written; `__pycache__`
holds only bytecode, which cannot reconstruct source text. The round-13 hashes
`bb2b8dd0…` (verify) and `4f48a314…` (README) are **not recoverable** and the
bytes below **do not** hash to them.

What follows is a reconstruction by subtraction, produced under explicit
instruction, presented for fresh review and claimed as nothing else.

## What was never damaged

`experiments.py` is byte-identical to round 13 at
`c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e`, as are
`compare.py`, `__init__.py`, `raw_runner.py` and `raw_config.py`. **The entire**
**ticket-07 authority layer is the reviewed artefact**: every join, gate,
canonical plan, fail-closed rule and derived field lives in `experiments.py`
and was untouched. The design digest recomputes to `ee530c06191e9792…`, the
round-13 value.

## The exact subtraction

`verify.py`, **1 926 lines removed** in six spans plus one line edited:

| Span | What it was |
| --- | --- |
| line 77 | `from . import production as prod` |
| line 101 | `from .production import _SEAL as _PRODUCTION_SEAL` |
| lines 473–506 | `ACCEPTANCE_CRITERIA` entries 122–128 and their preamble comment |
| line 14757 | `rows += _ticket08_api_rows()` in `_api_table` |
| lines 30262–30279 | four Ticket-08 facts added inside `_t07_current_facts()` |
| lines 30589–32459 | the whole contiguous Ticket-08 block: `_T08_CACHE`, `_T08_ALLOWED_MODULE_ACCESS`, `_ticket08_api_rows` and the seven checks covering criteria 122–128 |
| `_public_surface()` | `("production", prod)` removed from the module list |

`README.md`, **71 lines removed**: the whole `## Ticket 08: the production gate, and the no-result it returns` section, plus four pinned counts restored —
`**134 checks**` → `**127 checks**`, and 555/1 447/1 342 → **527/1 383/1 278**.

Nothing else was touched. `production.py` was **not** recreated; the Ticket 07
and Ticket 08 artefacts were not edited.

## The strongest evidence the subtraction was clean

The exported-surface census, computed independently by the suite from the live
package, returns **527 public callables, 1 383 invalid calls and 1 278**
**parameters** — **exactly the round-13 figures**. Those three numbers are
derived by walking every public callable and its declared probes; recovering
all three simultaneously is not something a lossy subtraction produces.

Beside that: **127 registered checks**, **121 acceptance criteria**, criteria
**110–121 all present**, and the design digest unchanged at `ee530c06…`.

## Verification (serial)

**127/127** on canonical, `--verbose`, direct-script and `-W error`;
`--prove-failure-exit` → **127/128, exit 1**; `py_compile` and `compileall -q`
clean; `results/` absent on every path; 20 package modules; nothing staged,
committed or reverted.

| File | SHA-256 |
| --- | --- |
| `experiments.py` | `c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e` (round-13 exact) |
| `verify.py` | `d3249e37bef73257a91005e20969155c0235d3303efed7aa1a39f8ab61feace3` (**new**) |
| `README.md` | `bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55` (**new**) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (round-13 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (round-13 exact) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (round-13 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (round-13 exact) |

Ticket 08 index restored by the coordinator to status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.

## Limitations of this baseline

1. **Byte equality with round 13 is unprovable and almost certainly false**
for `verify.py` and `README.md`. Comment wording, blank-line placement and
the exact spelling of anything Ticket 08 may have *rephrased* rather than
added cannot be recovered. The census triple and the check/criteria counts
are the strongest available evidence, and they are evidence, not proof.
2. **A rephrasing of an existing ticket-07 check would be invisible to this**
** procedure.** Subtraction removes what was added; it cannot detect a
sentence reworded in place. The suite passing at 127/127 with criteria
110–121 covered does not exclude a check that now tests slightly less.
**This is the reason the result must be reviewed rather than trusted.**
3. The working tree now shows **30** untracked entries rather than 29. The
additional one is `hologram_phase_test/` at the repository root, which is
not mine and which I did not touch.
4. All round 10–13 limitations stand unchanged.

# Fixture-origin closure — the cloning helper cannot mint production evidence

**Scope: one finding, and nothing else.** This closes the 2026-08-30 round-10
`P1 — The verifier fixture writer can mint canonical production evidence`
against the reconstruction-baseline R1 bytes. No other round-10 finding, no R1
finding, no pilot, no validation campaign, no production run and no Ticket-08
work is touched, and no ticket status changed. `experiments.py`, `README.md`,
`compare.py`, `__init__.py`, `raw_runner.py` and `raw_config.py` are
byte-identical to the R1 baseline; `verify.py` is the only file edited.

## The defect, reproduced first

The escape was reproduced end to end on the exact R1 bytes before anything was
changed. An `AlternatingPlan` — a `PilotPlan` **subclass** whose fields and
digest equal the canonical production plan, whose odd `config_for` calls return
a cheap `dt = 0.05`, coupling-0.2 configuration and whose even calls return the
canonical one — was handed to `_t07_pilot_fixture`:

```text
digest equal to canonical: True
written names: xpilot-t07-cell-0 ... xpilot-t07-cell-5
select_range(base plan): selected=True, cells=6
post_range_power: verdict=powered stage=post_range_join cells=6
arm trials: {'full': 2406, 'central_control': 6346, 'width_only_control': 2406}
```

That is the review's record, digit for digit. Twelve-trial histories at a
twenty-five-times coarser step were written under the approved pilot's own
manifest, in the approved pilot's own reserved run-name family, and the genuine
exact-typed canonical plan then recounted them as authoritative range evidence.

## What changed

`verify.py` only, four edits.

1. **`_t07_require_fixture_plan(plan)` — a new identity door.** It runs before
anything is opened or created, and it takes five things at once:
exactly the `PilotPlan` type (a subclass — the whole alternating attack —
is refused by type, not by watching what it returns); the declared
`verifier_fixture` purpose; a run-name family carrying
`FIXTURE_PREFIX_MARKER`; an exact rebuild through
`experiments.require_authoritative_plan` against the live firewall,
fingerprint and schema versions; and field-for-field **and** digest equality
with `_t07_fixture_plan()`. A last check refuses any plan whose names fall
inside the approved pilot's reserved family, so a fixture cannot occupy a
production identity even if the four rules above were ever made to disagree.
2. **`_require_fixture_source_name`** — the throwaway twelve-trial source run
carries the fixture marker too, is one path segment, and is neither a
declared cell name nor anything in the reserved production family.
3. **`_t07_write_fixture_cell` — one configuration, taken once.** The door and
the name checks run *before* `root.mkdir`, and `config_for` is now called a
single time; that one immutable snapshot drives both the source walk and the
manifest written above the clone. The split-brain second call is gone. The
cell name must also map to the coupling being written.
4. **`_t07_pilot_fixture`** takes the same door before its loop, so a refused
plan never reaches the first cell.

Nothing about the writer's physics changed: the source run is still a real
race, the clone is still a pure reindexing with exposures recomputed through
`raw_race.exposure_of`, and the five files still go straight into the
quarantine under `O_NOFOLLOW` with the marker last.

## The regression replay

Eleven must-refuse cases now run inside `check_range_selection`, each asserting
the exception type, that the quarantine root was **not created** if it did not
already exist, and that nothing was left behind:

| Attack | Refusal |
| --- | --- |
| the canonical production plan | `ValueError` |
| the alternating canonical subclass | `TypeError` |
| an alternating subclass carrying the fixture's own digest | `TypeError` |
| a sealed exact-type relabel of the canonical plan | `ValueError` |
| a `dataclasses.replace` of the fixture plan | `TypeError` |
| a second self-consistent fixture plan | `ValueError` |
| the per-cell writer handed the canonical plan | `ValueError` |
| the per-cell writer handed the alternating subclass | `TypeError` |
| the per-cell writer asked for a reserved cell name | `ValueError` |
| the per-cell writer asked for an unmarked source name | `ValueError` |
| one cell's coupling written under another cell's name | `ValueError` |

The replay first asserts that both subclasses really do reproduce the digests
they copy — an attack that failed to would prove nothing — then asserts the
consequence is gone: after the refusals the canonical plan's own recount over
its reserved cells finds nothing to read. The positive control is beside them:
the verifier's own fixture plan survives the door, still writes its four
honestly-named `xpilot-t07-fixture-cell-*` cells, is still authoritative under
its own plan and is still refused under the production plan.

## Verification (quiet, strictly serial, exclusive)

No other verifier was active; the matrix ran under an exclusive lock, one
command strictly after the previous one completed, from an absent `results/`,
with bytecode redirected to a temporary cache that was removed afterwards.
Miniconda Python 3.13.11 / NumPy 2.4.3.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 284 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 282 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 280 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 283 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; only `deliberate failure probe` failed |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent before, between and after every invocation. The check
count stays 127 and the acceptance criteria stay 1–121: the replay was added
inside an existing check rather than as a new one, and only private `_t07_*`
helpers were introduced, so the exported-surface census is untouched.

The direct-script and `-W error` invocations that failed in the 2026-08-30
round-10 matrix both pass here. That is consistent with the review's own
concurrency addendum, which withdrew those failures as a cross-process
fixed-name collision rather than an intrinsic finding.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `8bde04e60f358db63905cf5cb305d71ab276b3a8806f2ba43f03e5f8ec2670c7` (**new**) |
| `experiments.py` | `c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e` (R1 exact) |
| `README.md` | `bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55` (R1 exact) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

Ticket 07 remains status 2; Ticket 08 remains status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.
`production.py` remains absent. Nothing was staged, committed or reverted, and
no unrelated working-tree file was touched.

## Limitations of this closure

1. **One finding.** The round-10 `P2` live-prose detector weakness and all
three R1 findings — the false Ticket-08 README presentation, criteria 110
and 118, and the `raw_runner.py` co-ownership paraphrase — are untouched and
still open.
2. **Identity is against this verifier's own fixture plan**, so the helper is
now single-purpose by construction. A future check wanting a differently
shaped fixture must extend `_t07_fixture_plan` rather than pass its own
plan; that is the intended cost.
3. The door refuses a subclass by **type**, which is what makes a stateful
`config_for` unreachable. It does not attempt to detect a stateful
`config_for` behaviourally; the single-snapshot rule is the second,
independent reason the split-brain cannot recur.
4. The scientific boundary is unchanged and nothing here moves it:
`numerical_no_result` still blocks, `no_feasible_matrix_among_searched`
still stands, the proposal is still `checkpoint_blocked`, and no pilot,
campaign, production run or Ticket-08 derivation has occurred.

# Fixture-plan instance behaviour — fields are not behaviour

**Scope: one finding, again.** This closes the independent review's follow-on
finding recorded in the [fix-up ticket](../fixture-plan-instance-behavior-fix):
an exact-typed `PilotPlan` can keep every declared field and the right digest
while instance attributes shadow the methods the fixture writer calls after
validation. Nothing else is touched — the R1 findings, the round-10 prose
finding, Ticket 08, all ticket statuses and the Git index are untouched, and
the fix-up ticket stays status 1 until independent closure.

## The defect, reproduced first

`PilotPlan` is a frozen dataclass but not slotted, so its instances have a
`__dict__`. Plain methods are non-data descriptors, so an entry in that
dictionary wins the lookup. On the previous bytes:

```text
type is exact: True
digest equal: True
door returns: True
WROTE: xpilot-t07-cell-0
quarantine entries: ['xpilot-t07-cell-0']
```

That instance carried the fixture plan's own fields and digest, with
`require_run_name`, `coupling_for` and `run_name_for` injected through
`object.__setattr__`. The identity door validated the record and returned
**that object**, and the per-cell writer then asked it for the name mapping,
the coupling mapping and the configuration. The closure written underneath was
the honest eight-clock `dt = 0.05` fixture manifest and no canonical recount
was claimed — but a fixture had occupied a production identity, which is the
invariant.

Two properties were never at risk and it is worth saying why: `run_names`,
`digest` and `cells` are `property` objects, which are data descriptors, so an
instance-dictionary entry can never shadow them. The four plain methods were
the whole surface.

## What changed

`verify.py` only, and two independent answers rather than one.

1. **The supplied record is refused if it carries anything outside its declared**
**fields.** A frozen dataclass keeps its fields in the instance dictionary and
nothing else belongs there, so the rule is exact:
`set(vars(plan)) - set(PilotPlan.__dataclass_fields__)` must be empty. This
runs immediately after the exact-type check, before any field is read and
long before any directory is created, and it names the offending attributes
in the refusal.
2. **The caller's record is not returned.** `_t07_require_fixture_plan` now
returns the freshly built `_t07_fixture_plan()` record — constructed at the
boundary from the module's own factory, not from a cache or an alias — and
both `_t07_pilot_fixture` and `_t07_write_fixture_cell` assign that return
over their argument. Every subsequent `plan.` call — name mapping, coupling
mapping, configuration, window, model, blocking — is made on the fresh
record. The door additionally asserts that the record it is about to return
carries nothing outside its own declared fields.

Either answer alone closes the finding. Together, an unforeseen second route to
instance state on the supplied object still cannot influence what is written.

Everything from the previous closure is preserved unchanged: exact-type,
declared purpose, fixture-marked prefix, the `require_authoritative_plan`
rebuild against the live firewall/fingerprint/schema/config, field-for-field and
digest equality with the fixture plan, the reserved-family exclusion, the single
`config_for` snapshot per cell, the coupling/name join, and the rule that all of
it happens before `root.mkdir`.

## The regression replay

Thirty must-refuse cases now run inside `check_range_selection`, each twice —
once from an absent quarantine and once beside an unrelated pre-existing
quarantined run — for sixty refusal assertions. Nineteen are new:

| Shadowed attribute | Entry points |
| --- | --- |
| `require_run_name` | whole-fixture, per-cell |
| `coupling_for` | whole-fixture, per-cell |
| `config_for` | whole-fixture, per-cell |
| `run_name_for` | whole-fixture, per-cell |
| `require_run_names` | whole-fixture, per-cell |
| `require_manifest` | whole-fixture, per-cell |
| `run_names` (property; unshadowable, refused anyway) | whole-fixture, per-cell |
| an unrelated non-method attribute | whole-fixture, per-cell |
| the reviewer's exact three-method instance | whole-fixture, per-cell, and the door itself |

Each shadow case first asserts that it really is exact-typed and really does
carry the fixture's own digest — an attack that failed to would prove nothing.
The reviewer's exact write-level case is driven through
`_t07_write_fixture_cell(..., cell_name="xpilot-t07-cell-0")`, the call that
previously succeeded.

Every case, in both phases, asserts: the declared exception type; that the
quarantine root was not created if it did not already exist; that the
quarantine holds exactly what it held before — nothing, or only the bystander
run; that the reserved production name is not among its entries; and, in the
populated phase, that the unrelated pre-existing run's bytes are neither
mutated nor removed.

The positive control changed shape rather than disappearing. The door now
returns a different object by design, so the control asserts non-identity, then
exact type, digest equality, field-for-field equality, and that the returned
record carries no attribute outside its declared fields. The honest fixture
still writes its four `xpilot-t07-fixture-cell-*` cells, is still authoritative
under its own plan and still refused under the production plan.

## Verification (quiet, strictly serial, exclusive)

No other verifier was active; the matrix ran under an exclusive lock, one
command strictly after the previous one completed, from an absent `results/`,
with bytecode redirected to a temporary cache that was removed afterwards.
Miniconda Python 3.13.11 / NumPy 2.4.3.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 284 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 282 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 280 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 281 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` was absent before, between and after every invocation. The census is
unchanged: 127 checks, criteria 1–121, and only private `_t07_*` helpers and a
nested test closure were added, so the exported surface is untouched.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `dc43d946b2f50bcbdbaa9bda03a3a1a50693c8e1f6d247e43c396216e3ec7697` (**new**) |
| `experiments.py` | `c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e` (R1 exact) |
| `README.md` | `bfe791e7ac54865cdc7f0bc95010a9ff182884cfae4c4795154828ad095e2d55` (R1 exact) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_runner.py` | `b0067b189725cbd3f1c65aaf5499c1436785533b8b40589217358d2005e17e74` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

The prior fixture-origin closure's `verify.py`
`8bde04e60f358db63905cf5cb305d71ab276b3a8806f2ba43f03e5f8ec2670c7` is
superseded by the hash above. Ticket 07 remains status 2; the fix-up ticket
remains status 1; Ticket 08 remains status 0 at
`6657ff71ec46d35507c9cc076a29879bdc97b4acf483d5295261a9e7bd7b8975`.
`production.py` remains absent. Nothing was staged, committed or reverted, and
no unrelated working-tree file was touched.

## Limitations of this closure

1. **One finding.** The round-10 `P2` live-prose detector weakness and all three
R1 findings remain open and untouched.
2. **The attribute rule is structural, not a slot.** `PilotPlan` is still not
`__slots__`-bearing; adding slots would be a change to the reviewed
`experiments.py` authority layer and is outside this fix-up. The door
therefore refuses injected attributes rather than making them impossible,
and the fresh-record return is the second, independent reason they cannot
matter here.
3. The refusal enumerates attributes present in the instance dictionary. It
cannot see state hidden somewhere other than that dictionary; the
fresh-record return is what covers that case, and it covers it without
needing to enumerate anything.
4. The scientific boundary is unchanged and nothing here moves it:
`numerical_no_result` still blocks, `no_feasible_matrix_among_searched`
still stands, the proposal is still `checkpoint_blocked`, and no pilot,
campaign, production run or Ticket-08 derivation has occurred.

# R1 documentation and criteria closure — three findings, three mechanisms

**Scope: the three reconstruction-baseline R1 findings and nothing else.** No
`production.py`, no Ticket-08 check, no criterion 122 or beyond, no
authorization and no run. Ticket 07 stays status 2, Ticket 08 stays status 0,
the R1 fix-up ticket stays status 1 pending independent review, and the Git
index is untouched. The just-closed fixture-plan work is preserved intact —
its thirty two-phase attack replays and its honest positive control still run
and still pass.

## Each finding, reproduced before it was touched

```text
=== finding 1
production spec: None
registered checks: 127   criteria: 121
README contains 'The final seven are the ticket-08 production gat': True
README contains 'implemented **outside** the raw graph (`producti': True
check_readme / check_current_facts / check_stale_stage_strings: all passed

=== finding 2
with a rogue feasibility verdict, isolation passed=True
with a rogue support class,      isolation passed=True

=== finding 3
raw_runner co-ownership entry present: True
check_current_facts passed=True   check_stale_stage_strings passed=True
```

Every guard was clean over all three. That is the finding, not the prose.

## Finding 1 — the subtracted Ticket-08 gate, presented as implemented

**Corrected.** `README.md:1683` no longer enumerates seven Ticket-08 checks; it
now states that **there is no ticket-08 production gate in this package**, that
`production.py` does not exist, that no registered check covers a production
gate, that the criteria stop at 121 and that ticket 08 has not begun. The stage
table row at `README.md:3787` reads `**not implemented**` with the same three
facts. The `verify.py` comment describing an absent import of ticket 08's
`production` seal is gone, replaced by one sentence saying there is no second
such route and why the description was removed.

**Enforced three ways.** Three new current facts — *ticket 08 gate absence*,
*ticket 08 gate implementation*, *production module absence* — carry both
spellings and go through `_validate_current_facts` like every other fact,
including the current-to-stale mutation loop. Four new stale-prose patterns
catch the claim by meaning rather than by spelling: `final seven … ticket-08`,
`ticket-08 production gate … implemented`, an affirmative `implemented … ` + "`production.py`" + `(with a`(?<!not )`lookbehind so the true "not implemented" passes) and`production.py … implemented`. And the absences themselves are asserted rather than assumed: `production.py`does not exist, no package module imports a`production`module,`max(ACCEPTANCE_CRITERIA)` is
121, and the two affirmative README sentences are required to be present.

## Finding 2 — criteria 110 and 118 could be certified without their text

**Criterion 118** said "offers both costed alternatives". It now says one
explicitly unpriced intended-configuration validation outline beside one priced
machinery-only diagnostic. `check_checkpoint_handoff` writes the accepted
`ALTERNATIVE_CONTRACT` out and compares it, then proves that pin by altering
it four ways — Option A priced, Option B unpriced, Option A relabelled as a
diagnostic, and a third alternative added — each of which must be detected. It
also refuses the criterion text if the phrase "both costed alternatives"
returns.

**Criterion 110** claimed an absent production gate by name and its covering
check tested one bad spelling, so an appended `review_rogue_verdict` passed.
The criterion now names exactly what it enforces, and
`check_experiments_isolation` pins **sixteen** closed vocabularies member for
member and in order: proposal statuses, feasibility verdicts, budget verdicts
and blockers, power stages and verdicts, post-range statuses, selection
refusals, pilot roles and purposes, alternative labels and support classes,
configuration labels, permitted count-only fields, and the two Ticket-08 state
vocabularies. Each is exercised against copies — never by mutating the live
module — with an added member, a removed member and a reordered set, all of
which must be detected. Independently confirmed after the change: rebinding
`FEASIBILITY_VERDICTS` or `SUPPORT_CLASSES` with a rogue member now makes the
check fail.

## Finding 3 — budget ownership

`raw_runner.py` said "the production numerical budget, which tickets 07 and 08
own". It now says the budget **ticket 07 froze** and which is **not met**, and
that ticket 08 is not implemented in this package. A new current fact pins that
sentence against the exact co-ownership wording, and three new stale patterns
catch ownership by meaning: `tickets 07 and 08` near the budget, `ticket 08`
followed by an ownership verb near the budget, and the reversed
`tickets 07 and 08 own … production numerical budget`. Eleven new pinned
control sentences run both directions through the real patterns, including the
review's exact wording, three paraphrases, four line-wrapped variants and five
true statements that must pass.

The distinct truthful statement that production-status schema v4 does not exist
is untouched and still passes; the live manifest schema is still v3.

## Whitespace tolerance — what this does and does not close

Finding 3 required whitespace variants, so both validators now fold whitespace:
`_validate_current_facts` compares folded prose against folded spellings, and
`check_stale_stage_strings` scans the folded text as well as the raw text so a
hit can still be reported at its own line when it sits on one. Independently
confirmed: the co-ownership sentence wrapped as `which tickets 07\nand 08 own`
is caught by **both** fact rules, where before it was caught by neither.

**This closes the line-wrap half of the round-10 P2 finding and only that**
**half.** The dynamic-construction half is untouched: an f-string such as
`f"no production numerical {stage} exists yet"` is still split by the AST scan
into literal pieces and is still not recognised as the runtime sentence. Round
10 P2 should stay open on that basis and is not reclassified here.

## Digests that moved, and why

`raw_runner.py` is in `SOURCE_FILES`, so correcting its prose changes the live
source fingerprint and everything derived from it:

| Derived value | New |
| --- | --- |
| source fingerprint digest | `ecb801ba2b4782895cbf0c7b4c5bb39bbacbea35e3d7fc3ee1064202f5afc503` |
| canonical pilot plan digest | `ae6545abe0bdabca1cf4c4cecd9a38fa701ca5c4f824741f689653447a30f140` |
| verifier fixture plan digest | `398c61b41d4dfe8899227cbad5df78dc338343e473a6097574a7d9b9cdc91c51` |
| proposal design digest | `ee4b71ac86df69180825116af1647a457c8b81700a1bc2188d983532fc3261a3` |

No raw run manifest changes: `UNIMPLEMENTED_RAW_STAGES` is not a manifest key,
`VALIDATION_NOTE` is unedited and its revision is still 2, and the ledger and
manifest schemas remain 3 with 45 keys.

## Verification (quiet, strictly serial, exclusive)

No other verifier was active; exclusive lock, one command strictly after the
previous, from an absent `results/`, bytecode redirected to a temporary cache
and removed. Miniconda Python 3.13.11 / NumPy 2.4.3.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 283 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 284 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 283 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 284 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` absent before, between and after every invocation. Census unchanged
and internally consistent: **127 checks**, criteria **1–121**, **527** public
callables, **1 383** invalid calls, **1 278** parameters — the same figures the
README pins, recomputed by the suite from the live package.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `cd706adf77799242083dcc183367c348d70b754eb8083e42184ee612e4d51275` (**new**) |
| `README.md` | `aebefcbc4f901c894f0765f9e8c5f3baba846f8a91d09f8861e08fc602a43fc9` (**new**) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (**new**) |
| `experiments.py` | `c24cb79e753d4fc4d8863a136a99075aa0af40c86063af5ac62d4492df1b4d8e` (R1 exact) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

The fixture-plan closure's `verify.py`
`dc43d946b2f50bcbdbaa9bda03a3a1a50693c8e1f6d247e43c396216e3ec7697` is
superseded by the hash above; its behaviour and its tests are unchanged.

## Limitations of this closure

1. **Round-10 P2 is half closed and said so.** Line wraps are handled; runtime
f-string construction is not, and that finding stays open on that basis.
2. **The vocabulary pins are literal sets written in the verifier.** Adding a
genuinely new member is now a two-file change by design; that is the cost of
the criterion's word "closed", and it is what makes a rogue member visible.
3. **The README's narrative group arithmetic was already approximate** in the
reconstruction and remains so. Only the machine-checked counts — 127, 121,
527, 1 383, 1 278 — are pinned, and those agree with the live package.
4. **Digests derived from the source fingerprint moved**, because a corrected
sentence in a fingerprinted module is still a byte change. Nothing physical,
numerical or statistical moved with them.
5. The scientific boundary is unchanged: `numerical_no_result` still blocks,
`no_feasible_matrix_among_searched` still stands, Option A is still unpriced
and Option B is still exactly 18 runs / 29 268 rows, the proposal is still
`checkpoint_blocked`, and no pilot, campaign, production run or Ticket-08
derivation has occurred.

# R1 re-review closure — checkpoint authority, and ownership by meaning

**Scope: the two P1 escapes the independent R1 re-review returned OPEN on.**
Nothing else. No `production.py`, no Ticket-08 check or criterion, no ticket
status change, no Git index entry, no unrelated file. The R1 fix-up ticket
stays status 1. Both prior closures — the fixture-origin door and the
fixture-plan instance-behaviour door — are preserved with all thirty of their
two-phase attack replays intact.

Reviewed bytes at the start of this round matched the frozen set exactly:
`verify.py cd706adf…`, `README.md aebefcbc…`, `raw_runner.py ee13e099…`,
`experiments.py c24cb79e…`, `compare.py abc89474…`, `__init__.py 9f05ee02…`,
`raw_config.py eb59d197…`.

## Escape 1 — the checkpoint cost authority

### Reproduced first

```text
  pilot_wall_hours       genuine=32.110218391668845 forged=11.277735240000764
  pilot_storage_bytes    genuine=30885581.07692308  forged=10931032.430769231
  pilot_durable_rows     genuine=81840.0            forged=28836.0
  digests differ: True
  dataclasses.replace ACCEPTED, pilot_wall_hours=11.277735240000764
  subclass ACCEPTED: Sub
```

The factory had already removed the `alternatives` and `pilot_line`
*parameters*. What stayed open was the **record type**: `Checkpoint1Handoff`
was a plain frozen dataclass, so a caller could build one directly with every
canonical component and Option B's own comparison `CostLine` where the approved
pilot's belonged. `summary()` then presented the approved pilot at Option B's
eleven hours and 28 836 rows instead of its own thirty-two hours and 81 840.
`dataclasses.replace` and a subclass worked equally well.

### What changed

`experiments.py`:

1. **`_CHECKPOINT_SEAL`, and a `seal` field.** `Checkpoint1Handoff` is now
factory-only, exactly as `PilotPlan` and `ProposedProductionManifest` are.
The seal is checked **last** in `__post_init__`, deliberately: every field
rule above it is a statement about what a checkpoint may say and each has to
stay separately reachable and testable, so the existing field probes are
unchanged and still raise their own `ValueError`s. The seal is the separate
statement that even a record saying only permitted things is not a caller's
to mint.
2. **`_require_authoritative_checkpoint(handoff, …components…)`.** The seal
permits construction and proves nothing, so the handoff is rebuilt through
`checkpoint_one_handoff` from its own components and compared field for
field and digest for digest. This is what a reachable seal runs into. A
subclass is refused by `require_exact_type`, because a subclass could answer
`summary` or `digest` with whatever it liked.
3. **`_require_unchanged_checkpoint(handoff, frozen_digest)`**, the
post-freeze door, matching `require_unchanged_proposal`.

Both doors are **private**, like `_require_post_range_design` and
`_require_snapshot_power`, so the exported surface stays at 527 rows. The
public `checkpoint_one_handoff` factory remains the sole authority and still
derives the pilot line from `pilot_cost_from_plan(plan, slowest, resources.safety_factor)` and both alternatives from
`checkpoint_alternatives(...)`.

`verify.py`: `_t07_handoff_components()` names the exact component set once, so
the record and its authoritative rebuild cannot be asked different questions;
`_t07_handoff()` is now that call.

### The regression replay

Inside `check_checkpoint_handoff`, over **every other cost line in the**
**evidence** — the matrix's own lines and Option B's, not just the reviewer's
one — each of which is a real, correctly built `CostLine` describing something
that is not the approved pilot:

| Attack | Refusal |
| --- | --- |
| the review's exact direct construction | `TypeError` |
| direct construction with nothing altered | `TypeError` |
| `dataclasses.replace` of the handoff | `TypeError` |
| each substituted line through the seal, at the authority door | `ValueError` |
| reordered alternatives through the seal | `ValueError` |
| a friendlier feasibility through the seal | `ValueError` |
| a `Checkpoint1Handoff` subclass at the authority door | `TypeError` |
| the unchanged-digest door given another record's digest | `ValueError` |

Positive controls beside them: the factory's own record survives both doors;
its `pilot_line` digest equals what `pilot_cost_from_plan` builds from the
frozen plan and the slowest measured benchmark; and the three presented pilot
values equal that derived line's own. The signature check now also refuses a
`seal`, `ticket_08_derivation_status` or `ticket_08_authorization_status`
parameter on the factory, so there is no caller route to any of them —
independently confirmed as `no caller route: none`.

Independent replay after the change:

```text
  REFUSED  the review's exact direct construction                  TypeError
  REFUSED  direct construction, nothing altered                    TypeError
  REFUSED  dataclasses.replace                                     TypeError
  REFUSED  the same substitution through the seal, at the door     ValueError
  REFUSED  reordered alternatives through the seal                 ValueError
  REFUSED  a subclass at the authority door                        TypeError
  genuine survives door: True
  presented pilot: 32.027 h, 81840 rows
  no caller route: none
```

### Census

The `seal` field adds one parameter and one probe, so the pinned census moves
**1 383 → 1 384 invalid calls** and **1 278 → 1 279 parameters**. The README's
three pinned numbers are updated to `527 / 1 384 / 1 279` and
`check_documented_counts` accepts the join. Public callables stay 527, checks
stay 127, criteria stay 1–121. This is the one source-visible census change in
this round and it is here because a sealed record is a probed parameter.

## Escape 2 — ownership by meaning

### Reproduced first

Planting `ticket 08 jointly owns the production numerical budget` in the
discovered live `__init__.py` passed **both** guards: the previous patterns
knew `belongs to tickets 07 and 08` and required the budget to come first, so
the singular, reversed, differently-verbed form went straight through.

### What changed

A detector that asks the question instead of listing its spellings.
`_budget_ownership_claims(prose)` folds whitespace, then searches three orders
— subject before the budget, subject after it, and the passive "the budget is
owned by ticket 08" — over a declared subject set (singular and plural, either
order, hyphenated or spaced, with or without the leading zero) and a declared
ownership-verb set (`own/owns/owned/co-own/jointly own/joint owner/ownership/ share/hold/responsible for/responsibility for/belongs to`). A hit is
**discarded** when its window carries a negator, because "ticket 08 does not
own the production numerical budget" is the true statement and a guard that
flagged it would be unusable for saying so.

`_ownership_prose_problems(sources)` runs it over the same discovered live set,
and **both** `check_stale_stage_strings` and `check_current_facts` call it —
the review planted one sentence and both passed, so both now look.

### Controls

Twenty-four pinned control sentences run through the real detector: twelve
affirmative claims that must be caught (the review's exact plant, `owns`,
`co-owns`, `co owns` hyphen-variant, plural `tickets 7 and 8 own`, `shares`,
`holds`, `has responsibility for`, passive `is jointly owned by`, relative
`which ticket 08 co-owns`, `belongs to ticket 08`, `is a joint owner of`);
three of those wrapped across a line; and nine true statements that must pass,
including three negated ownership forms, `only ticket 07 owns…`, the live
`raw_runner.py` sentence, and **two schema-v4 controls** so the distinct
truthful statement about production-status schema v4 is preserved without
false positives. Beyond the sentences, the plant is made in three real
discovered modules — `__init__.py`, `compare.py`, `raw_runner.py` — through the
real source set, so the scope is exercised rather than asserted.

Independent replay after the change:

```text
  the review's plant is caught: True
  __init__.py names ticket 08 as an owner of the frozen numerical budget:
    'ticket 08 jointly owns the production numerical budget'
  live sources clean: True
  check_current_facts passed: True
  check_stale_stage_strings passed: True
```

## Round-10 P2 remains OPEN

Unchanged from the previous round and repeated here so it is not lost: line
wraps are handled, **runtime f-string construction is not**. An
`f"no production numerical {stage} exists yet"` is still split by the AST scan
into literal pieces and still not recognised as the sentence it prints. This
round does not close that and does not reclassify it.

## Verification (quiet, strictly serial, exclusive)

No other verifier was active; exclusive lock, one command strictly after the
previous, from an absent `results/`, bytecode redirected to a temporary cache
and removed. Miniconda Python 3.13.11 / NumPy 2.4.3.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 286 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 284 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 283 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 284 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` absent before, between and after every invocation. The suite's own
computed census reports **527 public callables, 1 384 invalid calls, 1 279**
**parameters**, 127 checks and criteria 1–121.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `e62f69e952301e86e14f75cda077c77fd99dfdd3a6acc01ee0d0c44fcf973c56` (**new**) |
| `experiments.py` | `35de6a27599986a3d2032a3e76a3334c4f127240a9b20e996516ba70c67d01ba` (**new**) |
| `README.md` | `ad710e8031fee05096fdfa445c97ff1e2b4604727380e9cc7c4c26c2fb8c989f` (**new**) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (unchanged this round) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

`experiments.py` is in `SOURCE_FILES`, so the fingerprint-derived digests moved
again:

| Derived value | New |
| --- | --- |
| source fingerprint | `f4bc296e98eba47479e90b5760cc64c78d02b3a42e44867ca800e6d5f02e0cf9` |
| canonical pilot plan | `d72a1ddb39e6cf15b5659ad77a2ea9e9fce1351b6cc28fa826aeda3ca016225f` |
| verifier fixture plan | `5bfc5beab7d7bd4c11071e1c5a7b4e6f10914aa40118fa84714a7ae3259e07d0` |
| proposal design digest | `5bbf0571d0b11f4773fac896f8bca8b9b4b849c7e78c75fc41985adf79069c66` |
| checkpoint handoff digest | `3ab76da560e2ddd431a7aea3e3c803cb8a1b899c85486b5a2c7a877ec64ecc0e` |
| derived pilot cost line | `08582eae46f3eb03f770dc1b4f3d73d5086b1af79559db961592c8f0ec1052a1` |

No raw run manifest changes; `VALIDATION_NOTE` is unedited at revision 2 and
the schemas remain 3 with 45 keys.

Scientific boundary unchanged and re-confirmed on these bytes: Option A
`is_priced=False`, Option B exactly 18 runs / 29 268 rows, proposal
`checkpoint_blocked`, feasibility `no_feasible_matrix_among_searched`, the
presented pilot its own 32.4 h / 81 840 rows. No pilot, campaign, production
run or Ticket-08 derivation occurred.

## Limitations of this closure

1. **Round-10 P2's dynamic-construction half stays open**, stated above.
2. **The seal is checked last**, so a directly built record is fully field-
validated before it is refused. That is a deliberate ordering to keep the
field rules separately testable; it means the refusal a caller sees for a
malformed direct construction is the field's, not the seal's.
3. **The ownership detector is a declared verb and subject set**, not a parser.
A sufficiently oblique paraphrase — ownership asserted without any of the
listed verbs — would still pass. The set is written out where a reviewer can
read it and extend it, and the negation rule is what keeps it usable.
4. **The census moved by one probe and one parameter** and the README was
updated to match. That is the only source-visible count change in this round.

# Alignment re-review closure — the seal was not the answer

The previous round's checkpoint repair was **not sufficient** and the
alignment review was right about why. `_CHECKPOINT_SEAL` is ordinary module
state: a caller reaches it, builds the record with Option B's cost line, and
calls the public `summary()` — never presenting it to
`_require_authoritative_checkpoint`, which is private, external and optional.
Proving a forgery fails *if voluntarily submitted to a door* proves nothing
about a caller who does not submit it. The ownership detector had the same
shape of hole: a negator anywhere in the match window masked an affirmative
relation elsewhere in the sentence.

Both are now closed structurally rather than by a door.

## Escape 1 — nothing left to substitute

`feasibility`, `alternatives` and `pilot_line` **are not fields any more**.
They are derived properties of `Checkpoint1Handoff`:

| Property | Derived from |
| --- | --- |
| `feasibility` | the search verdict, downgraded when the disposition blocks, the power is not `powered`, or the matrix misses its minimum eligible cells |
| `alternatives` | `checkpoint_alternatives(matrix, slowest benchmark, disposition, campaign, resources.safety_factor)` |
| `pilot_line` | `pilot_cost_from_plan(plan, slowest benchmark, resources.safety_factor)` |

The record now carries `plan` and `campaign` as fields so those derivations
have their inputs, and **binds every derivation input to the canonical**
**proposal** at construction: `pilot_plan_digest`, `matrix_digest`,
`resource_digest`, `firewall_digest`, `power_digest`, `recovery_digest`,
`search_digest` and `sampling_target_digest` must each equal the carried
component's own digest, and the numerical verdict and ordered blockers must
equal the proposal's. `require_plan_firewall(plan, firewall)` runs beside them.
A component the proposal did not freeze cannot be bound in, so the derivation
cannot be pointed at a different experiment.

The seal remains, checked last, and `_require_authoritative_checkpoint` /
`_require_unchanged_checkpoint` remain — as defence in depth, explicitly not as
the defence.

### The alignment review's exact route, replayed

```text
=== reach the seal, call summary(), present to no door
  UNEXPRESSIBLE (TypeError): Checkpoint1Handoff.__init__() got an unexpected
    keyword argument 'pilot_line'
  sealed record, no door called: pilot 32.042 h, 81840 rows
  identical to the factory's: True
  fields that are still caller-controlled: none
  they are derived properties: True
  replace REFUSED (TypeError)
```

The substitution is not refused — it is **unexpressible**. A record built
through the reachable token and never shown to anything presents the frozen
plan's own 32 h and 81 840 rows, because that is the only thing it can compute.

### Regressions

`check_checkpoint_handoff` now asserts, for each of `feasibility`,
`alternatives` and `pilot_line`: that it is **not** a dataclass field, that it
**is** a property, and that supplying it to the constructor raises. Over every
other cost line in the evidence — the matrix's own and Option B's — it asserts
both the unsealed and the sealed construction raise `TypeError`. It then builds
the record **through the reachable seal**, calls `summary()` and `digest`
directly, and requires both to equal the factory's. Beside those: `replace`
refused; a subclass refused at the authority door; a plan, matrix or resource
estimate the proposal did not freeze refused at construction; a rebuild from a
different label refused; and the derived verdict asserted not to be
`feasible_matrix` over a blocking disposition.

## Escape 2 — negation scoped to the relation

`_budget_ownership_claims` now cuts the match at the last clause boundary
before the ownership verb and searches only that clause for a negator. Clause
breakers: `,` `;` `:` `and` `but` `yet` `however` `although` `though`
`whereas` `while` `whilst` `nonetheless` `nevertheless`.

```text
  caught  (want caught ) ticket 08 is not implemented but jointly owns the …
  passes  (want passes ) ticket 08 does not own the production numerical budget
  caught  (want caught ) ticket 08 is not implemented and owns the …
  passes  (want passes ) ticket 08 is not implemented and does not own the …
  caught  (want caught ) the production numerical budget is not frozen but is
                         owned by ticket 08
  passes  (want passes ) production-status schema v4 does not exist yet
```

Ten new controls were added to the pinned set in `check_stale_stage_strings`:
six affirmative-after-a-negation forms that must be caught (including one
wrapped across a line) and four true denials that must pass. The existing
schema-v4 controls are unchanged and still pass.

One consequence worth recording: the detector's own docstring had to stop
spelling the affirmative example, because `_budget_ownership_claims` is a
module-level function and its docstring is inside the scanned literal set. The
exact sentences live in `check_stale_stage_strings`, which the literal scan
skips by name. A detector that trips on its own documentation is not a
detector.

## Census

Three derived properties on an exported class are three new public surface
entries, and the record's `__init__` lost three parameters and gained two:

| Figure | Was | Now |
| --- | --- | --- |
| public callables | 527 | **530** |
| invalid calls | 1 384 | **1 383** |
| parameters | 1 279 | **1 278** |

The README's three pinned numbers are updated and `check_documented_counts`
accepts the join. Checks stay 127, criteria stay 1–121.

## Verification (quiet, strictly serial, exclusive)

No other verifier active; exclusive lock, one command strictly after the
previous, from an absent `results/`, bytecode to a temporary cache and removed.
Miniconda Python 3.13.11 / NumPy 2.4.3.

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 283 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 283 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 282 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 285 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` absent before, between and after every invocation. Computed census
**530 / 1 383 / 1 278**. Fixture-plan attacks preserved and green.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `5c4bf7f9d5b28121a3c7e19b3d9eca4f954afeaa82992fa80bc8ec7762455e77` (**new**) |
| `experiments.py` | `f90abbe955793a2711cb68cf7283df168cb1353343adf345ccab9238aac198d1` (**new**) |
| `README.md` | `50f07413cf1a0f56c6f6789db0e632cf9eeafd480923428004c67eef8df5bb31` (**new**) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (unchanged) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

Fingerprint-derived values on these bytes:

| Derived value | New |
| --- | --- |
| source fingerprint | `db9294ea083e6b40574c9887e876f861f792b3fe5661ab591373dc0255313bb7` |
| canonical pilot plan | `16e0004fb18ea7649662c3181847ccef3ef4252f7077d7e0fe2f7941cdf937ad` |
| verifier fixture plan | `dd9dfed7d7b54673650b2a67b3c7e04eaad30d5047fc0f6d6c41878606900c8b` |
| proposal design digest | `03486572518cfa606830b88609ccfda9cc021bba3be604092a34251c64d35c4b` |
| checkpoint handoff digest | `91228fb9d064968c2b590423db0bf7b86726f5416f22ccb6e8937d5b0dda030c` |
| derived pilot cost line | `c4e72fcf6d9c8a5e0270851520b4d154c6016945a11484ae42be2525c526dfa5` |

Scientific boundary re-confirmed: Option A `is_priced=False`, Option B exactly
18 runs / 29 268 rows, proposal `checkpoint_blocked`, feasibility
`no_feasible_matrix_among_searched`, presented pilot its own 32.3 h / 81 840
rows. No pilot, campaign, production run or Ticket-08 derivation occurred.

## Limitations

1. **Round-10 P2's dynamic-f-string half remains OPEN.** Line wraps are
handled; runtime interpolation is not. Not closed, not reclassified.
2. **The clause-breaker list is a declared set**, not a parser. A sentence
whose negation and whose affirmation are separated by a construction not in
that list would still be misread; the list is written out where a reviewer
can read and extend it, and the controls pin both directions.
3. **`_require_authoritative_checkpoint` is now genuinely defence in depth.**
It is still private and still optional, and that is no longer load-bearing:
the record cannot present a caller's value whether or not anyone calls it.
4. **The census moved by three surface entries.** Deriving a value as a public
property is a source-visible change and the README was updated to match.
5. The scientific boundary is unchanged and nothing here moves it.

# Second alignment closure — the derivation *inputs*

The outputs were derived; two of the inputs they read were still a caller's,
and the class docstring claimed otherwise. Both are closed, and one of them is
closed by deletion rather than by a join that does not exist.

## Input 1 — the benchmark that prices everything

`pilot_line`, Option B and the presented clock-step rate all read `_slowest`,
and `__post_init__` never compared it with the proposal's own
`benchmark_digest`. The binding loop listed eight components and omitted the
one the prose said was bound. A caller could swap the benchmark tuple for
another exact `BenchmarkResult`, reach `_CHECKPOINT_SEAL`, and move every
derived number without touching a door.

**Closed:** the slowest supplied benchmark must equal
`proposal.value("benchmark_digest")`, checked at construction. Independently
replayed:

```text
  proposal benchmark_digest == presented authoritative: True
  REFUSED  a foreign slower benchmark alone
  REFUSED  a foreign slower benchmark beside the frozen set
  a faster benchmark: pilot line unchanged: True
  a faster benchmark: alternatives unchanged: True
  a faster benchmark: cube margin not widened: True
```

**And the rest of the tuple.** The proposal freezes exactly one benchmark, so
there is no authoritative join for the others and none is claimed. What is
asserted instead is a property that can be checked: the only two presented
values an extra benchmark can move are `peak_bytes` and
`empirical_bytes_per_row`, both **maxima**. A supplied measurement can
therefore only raise the peak — shrinking `projected_cube_margin` — and only
widen the empirical row bound. It can make this evidence more conservative and
never more favourable. `walked_clock_steps_per_second` is a minimum and is
pinned by the binding above, because a slower measurement would have to be the
frozen one. `summary()` now carries `authoritative_benchmark_digest` and
`supplied_benchmark_digests` so the distinction is visible rather than implied,
and the regression asserts the margin never widens, the pilot numbers never
move, and a reordered tuple is the same checkpoint.

## Input 2 — the campaign, removed rather than joined

`alternatives` derived Option A from a caller-supplied `ValidationCampaign`,
and the 86-field proposal has **no** campaign digest. There was no
authoritative join to make, and inventing a self-consistent caller digest would
have been the same self-authentication defect this ticket has closed four times
already.

**Closed by deletion.** `campaign` is gone from `Checkpoint1Handoff`, from
`checkpoint_one_handoff`, from `checkpoint_alternatives` and from
`intended_configuration_option`, which now takes nothing at all. The only
caller-dependent thing in Option A's text was the stage count; the rest was
already constant, and what Option A says — that four kernels were never
measured end to end, so no number exists — does not depend on how many stages
someone's campaign declares. The frozen 86-field proposal contract is
untouched.

```text
  campaign is a handoff field: False
  checkpoint_one_handoff         campaign parameter: False
  checkpoint_alternatives        campaign parameter: False
  intended_configuration_option  campaign parameter: False
  Option A digest matches the presented one: True | priced: False
```

`_t07_campaign()` and the `ValidationCampaign` record are unchanged and keep
their own checks; they simply no longer reach the checkpoint's presentation.

## Regressions added

In `check_checkpoint_handoff`: the presented authoritative benchmark equals the
proposal's frozen digest; a slower foreign benchmark is refused both alone and
beside the frozen set; a faster foreign benchmark leaves the pilot line,
alternatives, verdict and every pilot summary value identical and cannot widen
the cube margin; its digest appears in the presented provenance; a reordered
tuple reprices nothing; `campaign` is absent from the record and from all three
public builders; and Option A's presented digest equals what
`intended_configuration_option()` builds from nothing and is unpriced.

## Census

| Figure | Was | Now |
| --- | --- | --- |
| public callables | 530 | **530** |
| invalid calls | 1 383 | **1 380** |
| parameters | 1 278 | **1 274** |

Four parameters and three probes went away with the campaign. README updated;
`check_documented_counts` accepts the join. Checks 127, criteria 1–121.

## Verification (quiet, strictly serial, exclusive)

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 284 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 284 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 283 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 283 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` absent throughout; computed census **530 / 1 380 / 1 274**;
fixture-plan attacks preserved and green; the relation-scoped ownership fix
preserved and green.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `95bfe576230ca72af9b970ddce73f64e70ac0461575773c0c04d17c9876e9056` (**new**) |
| `experiments.py` | `460c9a850743282297904990e63451e97f5e167a22a4504350110f0a6c96d77f` (**new**) |
| `README.md` | `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9` (**new**) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (unchanged) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

Derived on these bytes:

| Derived value | New |
| --- | --- |
| source fingerprint | `1427b95e79b68fb342719866f0085d309afcd61eec3d9f0cdfba87b7d12da2aa` |
| canonical pilot plan | `d4dbf380a443473308b2a3eb29f0022c4f878a1f63538d77182c39939f92b158` |
| verifier fixture plan | `8d4b1f0119f028308aa3016128989405cf3abdc7a7d2800d25cc94d606978b70` |
| proposal design digest | `399365e30a052b2bb10566b2bf0ca96baeafc420ef8a13f31f3122f73701bf39` |
| checkpoint handoff digest | `b712a65589f532cebc2ef7f724a85e513e066455256164dea0adf58fe905050d` |
| derived pilot cost line | `a58215c21d8f1f2828b9897308a1c63f20163ac4c0e5ae7f96264957c206c2eb` |

Scientific boundary re-confirmed: Option A `is_priced=False`, Option B exactly
18 runs / 29 268 rows, proposal `checkpoint_blocked`, feasibility
`no_feasible_matrix_among_searched`, presented pilot 32.5 h / 81 840 rows. No
pilot, campaign, production run or Ticket-08 derivation occurred.

## Limitations

1. **Round-10 P2's dynamic-f-string half remains OPEN.**
2. **The non-authoritative benchmarks are argued by monotonicity, not bound.**
The proposal freezes one benchmark and this round does not invent a second
join. The claim made is exactly the one that can be checked: an extra
supplied measurement moves only maxima, so it can only make the presented
evidence more conservative, and its digest is shown either way.
3. **Option A no longer reports a stage count.** That number was the only
caller-dependent thing in its text and there was no authoritative source for
  254. The campaign record and its own checks are unchanged; it simply does not
reach the checkpoint.
4. `_require_authoritative_checkpoint` remains defence in depth. The public
`summary()` and `digest` are safe without it.

# Live-documentation cleanup — four stale campaign claims

Removing the campaign route left `experiments.py` describing it in four
places. These are live API help inside the discovered prose scope, and each
described a parameter and a field that no longer exist:

| Where | What it said |
| --- | --- |
| `intended_configuration_option` docstring | the checkpoint builds this record *from the campaign it carries* |
| `Checkpoint1Handoff.alternatives` docstring | derived from the matrix, the benchmark, the disposition, *the campaign* and the safety factor, *every one of which is bound* |
| `checkpoint_one_handoff` docstring | both alternatives rebuilt from the matrix, the benchmark, the disposition *and the campaign* |
| `_require_authoritative_checkpoint` error | alternatives *derived by* the factory from the benchmark, the matrix, the disposition, *the campaign* and the frozen plan |

The last one was the worst of the four: a refusal message telling a reader that
a record they had just been refused was rebuilt from something the record does
not have.

## Corrected

All four now say what is true: **Option A is the fixed, no-input, unpriced**
**outline**, and **Option B derives from the bound matrix, the authoritative**
**benchmark, the numerical disposition and the resource estimate's safety**
**factor**. The `alternatives` docstring additionally states why there is no
campaign clause to bind — the proposal freezes no such digest — rather than
leaving the omission to be inferred. The `ValidationCampaign` record, its
stages and their own documentation are untouched and still truthful.

## The guard that keeps them corrected

`_campaign_claim_problems(sources)` reports a live sentence that names a
checkpoint subject (`checkpoint`, `handoff`, `alternatives`, `Option A`,
`intended_configuration_option`), names a campaign, relates the two by a
declared relation (`derives from`, `derived by`, `computed from`, `built from`,
`builds`, `rebuilt`, `carries`, `takes`, `holds`, `uses`, `reads`), and carries
no negator. Whitespace is folded first, so a line-wrapped claim is the same
sentence. It runs inside `check_stale_stage_strings` over the same discovered
source set, beside a structural assertion that the field and the three public
signatures are campaign-free.

Each of the four corrected claims was restored into the live sources and
required to be caught:

```text
intended_configuration_option    restored -> caught: True
alternatives property            restored -> caught: True
checkpoint_one_handoff           restored -> caught: True
rebuild error                    restored -> caught: True
live sources clean: True
```

Twelve pinned controls run both directions: six affirmative claims that must be
caught, including one wrapped across a line and the exact `derived by …` shape
of the refusal message, and six that must pass — four truthful negations about
the removed route and **two sentences from the separate planning machinery**,
which name no checkpoint subject and are therefore out of scope by
construction rather than by exception.

One structural consequence: the detector's own patterns now live inside the
function and the function is skipped by the literal scan, for the same reason
the fact table is. The literal scan's skip list is four names rather than
three, and its comment says so. A detector whose own source satisfies it is not
a detector — the first draft flagged itself on exactly that.

## Verification (quiet, strictly serial, exclusive)

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 282 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 283 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 281 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, 282 s |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

`results/` absent before, between and after every invocation and at handoff.
Census unchanged at **530 / 1 380 / 1 274**, 127 checks, criteria 1–121 — this
round changed prose and added a guard, not surface. Fixture-plan attacks, the
relation-scoped ownership fix, the derived checkpoint properties and the
benchmark binding all preserved and green. Lock released, temporary bytecode
cache removed, no verifier processes left.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `0732ca7643f26c047f45848472f92ba8cb1da06d640c06a9c7f9551dffd8b20f` (**new**) |
| `experiments.py` | `6f8e79a869c9b49ea29c6193a170900c555294b33bb42a8156f50464a4481b25` (**new**) |
| `README.md` | `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9` (unchanged) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

`experiments.py` is fingerprinted, so the derived values moved again:

| Derived value | New |
| --- | --- |
| source fingerprint | `3cc9d9d175fb8027afb1fceea450bd9675a6daab48b5c2ea99152e61314f036c` |
| canonical pilot plan | `79d5332963b11b058585296f51c6011c2a80984a72631ab50b1ac3ad563e00c1` |
| verifier fixture plan | `4b8de938ef9021b0a4d29a0f6f81a161a4e7234b6813d242480b0e9103728e77` |
| proposal design digest | `227c5a28ddaa56f702aada7372f73ecf1b0369a90068deaf6306fb6f035c78ac` |
| checkpoint handoff digest | `5268a712a1ac1ebdc5ad899f198b1be2ecb69aae20f9b19821b0d406af3c24ef` |
| derived pilot cost line | `39398c3c204ac6f4fbcb0dbf1b4ee1ad87ec0f4566f4cfa8f52cc65970662453` |

Scientific boundary re-confirmed on these bytes: Option A `is_priced=False`,
Option B exactly 18 runs / 29 268 rows, proposal `checkpoint_blocked`,
feasibility `no_feasible_matrix_among_searched`, presented pilot 32.3 h /
81 840 rows. No pilot, campaign, production run or Ticket-08 derivation
occurred.

## Limitations

1. **Round-10 P2's dynamic-f-string half remains OPEN.**
2. **The campaign detector is a declared subject/relation set**, like the
ownership one. A claim phrased with none of those relations would pass; the
sets are written out where a reviewer can read and extend them, and the
controls pin both directions.
3. **The literal scan now skips four functions rather than three.** The fourth
is this detector, whose patterns would otherwise satisfy it. That is a real
dependence on a skip list and is recorded as one.

# Slotted checkpoint — the record itself could be poisoned

The derived properties closed what a caller could *supply*. They did nothing
about what a caller could *attach*. `Checkpoint1Handoff` was frozen but not
slotted, so it had an instance dictionary, and a plain method is a non-data
descriptor: an instance attribute named `summary` wins the lookup outright.

## Reproduced on the frozen reviewed bytes

```text
extra instance state: ['summary']
ACCEPTED; door returns the supplied object: True
poisoned summary: {'pilot_wall_hours': 0.0002777777777777778,
                   'ticket_08_authorization_status': 'authorized'}
has __dict__: True
```

A genuine factory record, one `object.__setattr__`, and the authority door —
which compared dataclass fields and digests — handed the poisoned object back.
One second of pilot time and an authorized Ticket 08, presented by a record
whose every field was correct.

## What changed

`experiments.py`, two changes and one new private door.

1. **`@dataclass(frozen=True, slots=True)`.** There is no instance dictionary
now, so no attribute outside the declared fields can exist and no method or
property on the record can be shadowed. The review's exact assignment
raises `AttributeError: 'Checkpoint1Handoff' object attribute 'summary' is read-only`. This is the whole of the closure; everything below is so that
removing it is a test failure rather than a silent reopening.
2. **`_require_authoritative_checkpoint` returns the rebuild**, not the object
it was handed. A boundary that authorizes something now never forwards a
caller's record, whatever a future class change might reintroduce.
3. **`_require_no_undeclared_state(handoff)`** — exact type, and no instance
dictionary. Called by both doors and exercised directly.

`_require_unchanged_checkpoint` still returns the record it was given, because
a digest is not a set of components and there is nothing to rebuild from; the
no-undeclared-state rule is what makes that safe, and it runs there too.

## Replayed after the change

```text
=== the review's exact reproduction
  IMPOSSIBLE (AttributeError): 'Checkpoint1Handoff' object attribute
    'summary' is read-only
  has __dict__: False
  __slots__ == declared fields: True

=== every dynamically consumed member, one at a time
  IMPOSSIBLE summary / digest / alternative / feasibility / alternatives
  IMPOSSIBLE pilot_line / _slowest / __dict__ / anything_else

=== subclass with a dictionary is refused by type at every door
  the subclass shadow does take effect: True
  REFUSED at the authoritative / unchanged / no-state doors (TypeError)

=== the authority door returns its own rebuild
  is the supplied object: False
  same digest and summary: True
  returned record has no dictionary: True
  replace REFUSED (TypeError)
```

## Regressions

In `check_checkpoint_handoff`: the record has no `__dict__`; the class is
slotted; `__slots__` is **exactly** the declared field set; nine individual
shadow attempts — `summary`, `digest`, `alternative`, `feasibility`,
`alternatives`, `pilot_line`, `_slowest`, `__dict__` and an unrelated name —
each required to raise; the review's exact poisoned-summary assignment as its
own case; a subclass carrying a dictionary, with its shadow shown to take
effect, refused at all three doors; `dataclasses.replace` refused; the
reachable seal still presenting the factory's own numbers; and the authority
door asserted to return a record that is **not** the one supplied, is
exact-typed, hashes and summarises identically, and carries no dictionary.

## Verification (quiet, strictly serial, exclusive)

| Invocation | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 127/127, exit 0, 283 s |
| `python3 -m adler_born_two_channel.verify --verbose` | 127/127, exit 0, 282 s |
| `python3 adler_born_two_channel/verify.py` | 127/127, exit 0, 281 s |
| `python3 -W error -m adler_born_two_channel.verify` | 127/127, exit 0, **3 833 s** |
| `python3 -m adler_born_two_channel.verify --prove-failure-exit` | 127/128, exit 1; exactly one `[FAIL]`, the deliberate probe |
| `python3 -m py_compile adler_born_two_channel/*.py` | exit 0 |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |

**The `-W error` wall time is an anomaly and is recorded as one.** It ran 3 833 s
against the ~283 s every other invocation took, on the same bytes, in the same
serial sequence, under the same lock. The machine's load average was 14.9 when
it finished and 2.7 minutes later; the verifier process itself was the only
one at full CPU. The result is unaffected — 127/127, exit 0, `results/` absent
— and this package already labels every wall time a machine-dependent
snapshot. It is reported here rather than smoothed away, and it is not a cost
claim about anything.

`results/` absent before, between and after every invocation. Census unchanged
at **530 / 1 380 / 1 274**, 127 checks, criteria 1–121: slots add no public
surface and the new door is private. Every earlier closure preserved and
re-confirmed on these bytes — the fixture-plan attacks, the relation-scoped
ownership guard, the campaign-claim guard, the derived checkpoint properties,
the benchmark join and the campaign removal.

| File | SHA-256 |
| --- | --- |
| `verify.py` | `259f2f864070989cc524c0499e1a7b8ef03f6a7973a8b579d775244774fa11c5` (**new**) |
| `experiments.py` | `b2672e0ff226ef48f073cb31176b656d301ec37f24fa13d28f027586bb68afeb` (**new**) |
| `README.md` | `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9` (unchanged) |
| `compare.py` | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` (R1 exact) |
| `__init__.py` | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` (R1 exact) |
| `raw_runner.py` | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` (unchanged) |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` (R1 exact) |

Derived on these bytes:

| Derived value | New |
| --- | --- |
| source fingerprint | `8bb1a4eddd8b93a3458393bd027536e3b6f7a5f51d49fa561f7161926b945992` |
| canonical pilot plan | `319ee12bd6d3fa07408ac81caa9ac5144fea5a96e05ec097fcae4a902f32e5dc` |
| verifier fixture plan | `f1b3ba4a8def7452c2143d11e83f632c5343c5d579a521b197192350953edf61` |
| proposal design digest | `de9e336654c844e2d1b3b1928656123c8c7f4497927ad49c77c9a34aa6eb7d81` |
| checkpoint handoff digest | `97f3137573182d3e2d17bb0df4ff363ffa0db3568f95c3326a687786b99020ea` |
| derived pilot cost line | `4295deea479a8ab0c2a08299177684fcce7cf856cc22f3ca219f4f4ab64d7390` |

Scientific boundary re-confirmed: Option A `is_priced=False`, Option B exactly
18 runs / 29 268 rows, proposal `checkpoint_blocked`, feasibility
`no_feasible_matrix_among_searched`, presented pilot 31.9 h / 81 840 rows. No
pilot, campaign, production run or Ticket-08 derivation occurred.

## Limitations

1. **Round-10 P2's dynamic-f-string half remains OPEN.**
2. **Only `Checkpoint1Handoff` was slotted.** The review asked not to broaden
into unrelated classes and I did not. `PilotPlan` remains unslotted and is
defended by the explicit undeclared-attribute refusal added earlier; the two
mechanisms differ and both are tested.
3. **The `-W error` timing anomaly above** is unexplained beyond machine load.
It is a wall-time observation on a shared machine, not a property of these
bytes, and the check result was identical.
4. The literal scan's four-name skip list stands as previously recorded.
