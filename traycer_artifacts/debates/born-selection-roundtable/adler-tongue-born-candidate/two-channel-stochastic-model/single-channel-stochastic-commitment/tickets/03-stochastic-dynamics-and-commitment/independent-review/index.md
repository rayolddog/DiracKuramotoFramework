---
title: "Independent review — Ticket 03 stochastic dynamics and commitment"
kind: review
---

# Verdict

**OPEN — seven actionable current defects remain.** The core numerical path is substantially correct: the 65-check suite passes in every required invocation, all 56 earlier check residuals and tolerances remain unchanged, independent off-grid walks consume Ticket 02 leaves chronologically and conserve their parents, zero noise is bit-exact Euler, the observed Euler halving ratios are 1.98–2.00, width-only handoffs preserve the authoritative phase in ordinary supported ranges, and a 96-record one-clock matrix is internally consistent.

Closure is blocked by one ordinary-scale dwell error, one omitted S4 mode, and five public-contract gaps. In particular, a dwell that should complete from `t=0.1` through `t=0.3` with `dwell=0.2` is delayed to `t=0.4`; the raw width-control factory permits arbitrary per-run rates; and accepted large phase magnitudes cease to carry a target lift congruent to the declared principal target.

## High — ordinary decimal timestamps can delay an exact dwell by one sample, while duplicate and backwards endpoints are accepted

**Where:** `commitment.py:210-216,342-417`.

The state machine implements the declared comparison literally as `moment - inside_since >= dwell`. Binary64 subtraction can round an exact physical equality down:

```text
criterion = LockCriterion(0.2, 0.2)
inside samples: 0.1, 0.2, 0.3, 0.4

0.3 - 0.1 = 0.19999999999999998
```

The current machine therefore does **not** commit at `0.3`; it commits at `0.4`. The verifier avoids this by choosing binary-exact `dt=0.125`, so its equal-dwell test does not exercise the ordinary decimal mesh used elsewhere. This violates the fixed physical timestamp rule and makes event time depend on arithmetic spelling rather than elapsed time.

The public machine also has no last-observed timestamp. Starting a dwell at `t=1.0`, both a duplicate call at `1.0` and a backwards call at `0.9` return valid states. `synthetic_dwell_history` rejects these sequences, but `LockCriterion.advance`—the actual public state transition—does not. `DwellState` likewise accepts `inside_since=10.0, committed_at=9.0` when the flags/counts are otherwise populated.

**Bounded fix:** define a scale-aware few-ulp equality rule for the elapsed-time threshold, add the last processed endpoint to `DwellState`, require strict time increase in `advance`, and require `committed_at >= inside_since`. Add decimal equality from a nonzero origin, nonuniform samples, duplicates, backwards samples, and large-origin resolution cases. The comparison must not grant a materially early dwell; only numerically equal endpoints should be coalesced.

## High — the stationary half of governing experiment S4 is not implemented

**Where:** `dynamics.py:298-396,650-704`; `raw_runner.py:212-233`; `raw_experiments.py:308-406`; `verify.py:8118-8268`.

The governing plan requires S4 to run one clock under **stationary and pulsed coupling**. The current implementation only accepts a `PulseTrain` containing `RaisedCosinePulse` objects, and `raw_one_clock_path` always constructs exactly one raised-cosine pulse. A direct attempt to construct the existing path with `StationaryCoupling(1.0)` fails:

```text
ClockPath(0.4, StationaryCoupling(1.0), "full", 0.0)
TypeError: train must be exactly PulseTrain, got StationaryCoupling
```

The 24 canonical S4 records and the independent 96-record matrix are all pulsed. The dark `peak=0` diffusion check is a useful control but does not implement the nonzero stationary central/interior/near-edge cells named by S4.

**Bounded fix:** add an isolated stationary one-clock path/coupling schedule, with no fake finite tongue crossings, and run the same central/interior/near-edge × zero/weak/intermediate/strong-noise record checks for full and fixed-contraction processes. This is not the killed-diffusion oracle or stationary-hazard experiment; those remain later tickets.

## High — the raw path API allows silent per-run tuning of the supposedly frozen width-control rate

**Where:** `raw_runner.py:212-233`; `dynamics.py:244-291,650-690`.

The causal control requires one common central-clock rate, invariant to coupling, mismatch, trial, dwell, tolerance, and noise. The primary raw factory instead exposes `fixed_rate` as a caller-supplied scalar:

```text
raw_one_clock_path(config, 0.4, "width_only", 0.1).fixed_rate  -> 0.1
raw_one_clock_path(config, 0.4, "width_only", 1.0).fixed_rate  -> 1.0
raw_one_clock_path(config, 0.4, "width_only", 10.0).fixed_rate -> 10.0
```

All three are accepted under the same raw configuration. The built-in check proves only that the tests themselves reuse `FIXED_CONTRACTION_RATE`; it does not prevent a real caller from varying the rate with the run. This permits exactly the coupling-dependent/per-run tuning the control is meant to exclude.

The public derivation helper also has an unguarded numerical domain: `fixed_contraction_rate(1e-300, 1e-300)` returns `NaN` because `lower*upper` underflows to zero and `stable_phase(0,0)` is undefined; large finite pairs can overflow before the square root.

**Bounded fix:** remove the numeric rate from the primary raw factory and derive the provisional/manifest-frozen value in one place. If later sensitivity rates are needed, expose a separately named sensitivity factory with a required structured label. Compute the geometric mean without materializing `lower*upper`, validate the finite positive result, and add underflow/overflow probes.

## Medium — accepted large unwrapped phases no longer preserve a lift of the declared target

**Where:** `model.py:114-121`; `dynamics.py:183-241,741-815`.

The public phase/lift functions accept every finite binary64 magnitude. At `phase=1e16` and principal target `pi/2`:

```text
nearest_lift(pi/2, 1e16) = 9999999999999998.0
phase - lift             = 2.0
wrap_phase(lift - pi/2)  = -0.5043502211754891
```

The selected value is more than half a radian away from being congruent to the target it claims to lift. At `1e17` and above the stored error can collapse to zero while the congruence error remains order one. The reconstruction identity still adds back to the authoritative phase, so the current lift-residual check passes while the auxiliary target has become the wrong target. The next eligible contraction and lock error can therefore be wrong for an accepted state.

Ordinary accumulated winding is sound: independent two-pulse runs for both mismatch signs and zero mismatch, full/control, a 37-turn initial phase, circular-cut entries, the exact half-turn tie, and errors beyond four turns all passed. This finding is specifically the undocumented large-magnitude domain.

**Bounded fix:** either use a representation that retains an exact winding integer plus a resolvable principal residual, or reject phase/lift magnitudes once their ulp exceeds a declared angular-resolution budget. Add target-congruence checks, not only `lift + error == phase`, at adjacent accepted/refused magnitudes.

## Medium — the raw configuration accepts a lock band its criterion factory rejects

**Where:** `raw_config.py:328-334`; `commitment.py:305-314`; `raw_runner.py:195-209`.

`RawEventConfig` accepts `lock_tolerance == pi` because it rejects only values greater than `pi`. `validate_raw_config` and `raw_noise_stream` accept the resulting configuration. `raw_lock_criterion` then raises because `LockCriterion` correctly requires a tolerance strictly less than `pi`.

This makes the declared single raw input boundary accept a run configuration that cannot instantiate its own state machine.

**Bounded fix:** make the raw configuration use the same strict `< pi` domain and add an exact-`pi` boundary probe through configuration validation and every raw factory.

## Medium — state and record constructors admit mutually contradictory ledgers

**Where:** `commitment.py:218-249`; `raw_experiments.py:203-247`.

The actual 96 independently generated S4 records obeyed all checked relations: category/time agreement, resets no greater than entries, entries no greater than eligible endpoints, endpoint subtotals, and commit times inside the run. The public record constructor does not enforce those relations, despite its statement that every field is checked.

This record was accepted unchanged:

```text
category="never_eligible"
band_entries=3
dwell_resets=9
endpoints=1
eligible_endpoints=5
boundary_endpoints=7
```

The `DwellState` constructor also permits a commitment before its own `inside_since`, as noted above. These objects are the handoff to later ledger work, so contradictory counts should fail where they are created rather than become plausible raw rows.

**Bounded fix:** enforce category/eligibility/entry implications, `resets <= entries <= eligible_endpoints`, endpoint subtotals, `committed_at >= inside_since`, and the full-model/width-control fixed-rate convention. Add one valid control beside each invalid relation.

## Low — `raw_runner.py` still says the newly implemented stages do not exist

**Where:** `raw_runner.py:22-40`.

The module-level documentation says the package contains “no stochastic integration, no lock band, no dwell clock, no commitment” and “there is no stepper.” The same file now imports and advertises all of those in `IMPLEMENTED_RAW_STAGES`. README and the runtime tuples are current, but the raw entry point’s first explanation is not.

**Bounded fix:** replace the Ticket-01-era paragraph with the current one-clock boundary and preserve the still-true exclusions: no population race, disk ledger, oracle/audit, survival/hazard/exponent analysis, or channel outcome.

# Independently confirmed contracts

## Dynamics, crossings, and Brownian ownership

- One off-grid noisy run used two deterministic crossings, 60 chronological `TreeLeaf` objects over 58 finest steps, and an independently reconstructed segment list. Every leaf start/duration matched its exact segment, every full-model update matched the start-frozen Adler Euler expression bit for bit, and each step’s leaf kicks re-summed to its root with maximum conservation-bound ratio `0.0`.
- A 4,000-trial public Brownian split at `alpha=0.25`, `D=0.03`, `h=1` measured parent/left/right variances `0.05873 / 0.01467 / 0.04502` against `0.06 / 0.015 / 0.045`, sibling correlation `-0.0186`, and maximum conservation ratio `0.25`. Proportional subdivision produced only `0.2447` of the required left variance.
- Zero diffusion produced exact-zero leaves and a phase endpoint bit-identical to an independently written deterministic Euler walk.
- Against a SciPy DOP853 continuous reference, pulsed zero-noise Euler errors were `1.4288e-2, 7.2086e-3, 3.5993e-3, 1.8026e-3` at timesteps `0.08, 0.04, 0.02, 0.01`, giving halving ratios `1.982, 2.003, 1.997`.
- Six two-pulse entry/exit/re-entry cases—both mismatch signs and zero mismatch, full and width-only—preserved finite unwrapped phase and the target-lift identity from a 37-turn initial state. Cut-straddling entries, the exact `-pi` half-turn tie, and multi-turn unwrapped errors also passed.
- Shared full/control leaves were identical. In a direct paired walk, 27 ineligible intervals used the same code and produced bit-identical phases, while 33 eligible intervals differed under the fixed contraction.

## Commitment and records

- Initial-inside, dwell shorter/equal/non-integral relative to the sample spacing, proximity equality, contraction equality, repelling/expanding sides, falling eligibility loss, prospective-commit-step band exit, and already-committed refusal passed when timestamps were numerically unambiguous.
- The independent S4 matrix contained 96 pulsed records: three mismatch cells × four noise levels × two models × four initial phases. Categories were 46 `lock_failed`, 41 `committed`, and 9 `dwell_failed`; no generated record violated the count, category, or timing relations above.
- The central control is the full model at zero mismatch, not a third dynamics label. Generated labels are raw `S4/...` mechanism labels, and the record schema contains no probability, predictor, hazard, weight, exponent, click, outcome, or Born field.

## Isolation, files, and compatibility

- An independent AST import walk from package root, `raw_runner.py`, and `raw_ledger.py` reached exactly `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, and `validation`; it reached no analytic, simulation, oracle, comparison, analysis, experiment-orchestration, or verifier module.
- `dynamics.py`, rather than `stochastic.py`, is therefore harmless technical placement drift: it is in the raw graph, consumes Ticket 02 `TreeLeaf` objects, and creates no isolation or ownership gap.
- The raw graph contains no filesystem writer. `raw_ledger.json.dumps` returns canonical bytes in memory; it is not a disk operation. No result file or trial/clock/time cube was created. The one-clock runner materializes one clock’s leaves, segments, and returned phase history, not a population cube; population streaming remains a later ticket.
- Current source SHA-256 values include `dynamics.py 01c9ca84...`, `commitment.py 87335fa9...`, `raw_experiments.py 4c151ce5...`, `raw_runner.py f247bc80...`, `stochastic.py e6a3f649...`, `verify.py c77308bc...`, and `README.md f204fc53...`. No implementation source was edited during review.

# Canonical execution evidence

Environment: macOS 26.5.2 arm64; Python 3.12.6; NumPy 2.3.5; SciPy 1.15.3.

- Canonical module: **65/65**, exit 0.
- Verbose module: **65/65**, exit 0.
- Direct script: **65/65**, exit 0.
- `PYTHONWARNINGS=error`: **65/65**, exit 0.
- Deliberate failure: **65/66**, process exit 1 with only the deliberate probe failing.
- `python3 -m compileall -q adler_born_two_channel`: exit 0.
- `PYTHONHASHSEED=0` and `PYTHONHASHSEED=987654321`: **65/65** with identical printed residuals.

Compared with Ticket 02’s final closure record, all 56 earlier check residuals and tolerances are unchanged. The load-bearing values remain wrapping `8.452e-15`, stationary arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`, and v3 noise/split residuals `3.460 / 1.171`. The nine Ticket 03 checks add no tolerance weakening to those earlier checks.

# Scope, limitations, and non-claims

Reviewed source: `dynamics.py`, `commitment.py`, `raw_experiments.py`, their raw factories/configuration, calibrated model kernels, Ticket 02 leaf API, verifier coverage/mutations, README, and the full transitive raw graph. Governing context included the complete Ticket 03, the closed single-channel plan and pressure-test amendments, Ticket 01’s final raw-isolation closure, and Ticket 02’s complete fix-up/closure history.

This review does not validate a population race, channel-level first winner, disk ledger, killed-diffusion oracle, moving-band audit, survival/hazard estimator, scaling fit, detector click, measurement outcome, microscopic bath, or Born-selection claim. Those remain absent. A CLOSED verdict requires the defects above to be fixed and independently re-probed; the canonical 65/65 result alone is not sufficient.

# Closure re-review after the seven-finding fix-up — 2026-08-27

## Verdict

**OPEN — five of the seven original findings are closed, but two repaired contracts still have public bypasses.** The decimal-dwell, stationary-S4, lift-resolution, exact-`pi`, and stale-documentation findings are closed. The primary raw factory also no longer accepts a rate. However, the public `ClockPath` plus public `run_one_clock` path still runs and labels an ordinary width-only S4 record at any caller-selected positive rate, and the strengthened state/record constructors still accept histories their own state machine cannot produce. These are actionable current defects in the two contracts the fix-up was meant to close.

The numerical implementation remains strong. The canonical suite is **71/71** in every required successful invocation; deliberate module and direct-script failures exit exactly 1; compilation succeeds; both hash seeds reproduce the same output; the 65 pre-fix-up check lines retain their recorded residuals and tolerances; Ticket 02's `stochastic.py` hash, v3 schema and keyed residuals remain unchanged; and 248 independent repair-focused assertions passed before the two omitted constructor/bypass cases below were added.

## High — the frozen-rate primary factory is closed, but the public experiment path still permits unlabelled per-run tuning

**Where:** `dynamics.py:926-977`; `raw_experiments.py:379-484`; `raw_runner.py:229-277`.

`raw_one_clock_path` is repaired: its signature is `(config, detuning, model='full', drive='pulsed')`, it has no rate spelling, and every width path it returns carries the single derived `FIXED_CONTRACTION_RATE == 1.0000000000000002`. The derived value is finite and positive from `(5e-324, 5e-324)` through `(DBL_MAX, DBL_MAX)`, malformed ranges reject, and its one-ulp change from the earlier provisional value is the documented compatibility cost of avoiding `sqrt(lower * upper)` underflow/overflow.

That is not yet the only public way to run the experiment. `ClockPath` is exported, accepts any positive `fixed_rate`, and `run_one_clock` is exported and accepts that exact type without requiring the frozen rate or a structured sensitivity label. The same raw mechanism label therefore produces three distinct trajectories under one keyed stream:

```text
ClockPath(0.35, StationaryDrive(1.0), "width_only", 0.1)
ClockPath(0.35, StationaryDrive(1.0), "width_only", 1.0000000000000002)
ClockPath(0.35, StationaryDrive(1.0), "width_only", 7.0)

run_one_clock(..., label="S4/stationary/interior/zero/width_only")
record.fixed_rate -> 0.1 / 1.0000000000000002 / 7.0
final_phase       -> 0.7957360227017478 / 0.7588964119177131 / 0.5747151036221074
```

`OneClockRecord(model="width_only", fixed_rate=7.0, ...)` is also accepted as an ordinary record. Thus behavioral enforcement at `raw_one_clock_path` is necessary but not sufficient while the generic constructor and runner are both public and no sensitivity identity is required. This is the exact alias/bypass the closure request asked to exclude.

**Bounded fix:** make the production `ClockPath`/`run_one_clock` boundary require the one frozen scalar, or make non-primary rates reachable only through a separately named sensitivity type/factory carrying a mandatory structured label that survives into `OneClockRecord`. Require primary width-only records to carry the frozen scalar exactly. Keep direct mutation helpers private if the verifier needs arbitrary rates internally.

## Medium — state and record cross-field validation still accepts unreachable ledgers

**Where:** `commitment.py:248-365`; `raw_experiments.py:203-326`.

The new checks correctly reject commitments before their dwell, missing live-entry flags/counts, resets greater than entries, endpoint subtotals, category/time disagreement, and the full/non-positive-width rate conventions. They do not enforce the conservation law of the state machine itself. At any reachable endpoint, every past band entry is either the one currently live or has been reset, so:

```text
band_entries == dwell_resets + int(inside_since is not None)
ever_inside  == (band_entries > 0)
```

The current constructor accepts all four impossible states below unchanged:

```text
DwellState(band_entries=1)
# category never_eligible, despite a historical band entry

DwellState(ever_eligible=True, ever_inside=True)
# category dwell_failed, despite zero band entries

DwellState(inside_since=1.0, last_time=1.0,
           band_entries=1, dwell_resets=1,
           ever_eligible=True, ever_inside=True)
# the only entry is simultaneously live and already reset

DwellState(band_entries=2, dwell_resets=0,
           ever_eligible=True, ever_inside=True, last_time=2.0)
# two ended entries with no reset
```

The exported record repeats the gap. With otherwise valid fields, it accepts `category="dwell_failed", band_entries=5, dwell_resets=0`; it also accepts `category="committed", committed_at=0.5, band_entries=5, dwell_resets=0`. A committed record must have exactly one more entry than reset, while an unresolved `dwell_failed` record may have either an active dwell (`entries = resets + 1`) or no active dwell (`entries = resets`). Five independent active dwells are impossible in this one-clock machine. A second cross-field omission accepts `drive="stationary", boundary_endpoints=1`, although `OpenSchedule` has no boundary by construction.

All 48 canonical pulsed/stationary records and all 48 independently generated controls obey the stronger relations; this is a constructor-boundary defect, not a generated-data failure.

**Bounded fix:** enforce the exact entry/reset/live relation and the latch implication in `DwellState`; reject a never-processed state with historical flags/counts. In `OneClockRecord`, require `entries - resets` to be zero or one, require exactly one for `committed`, require zero entries/resets for `never_eligible` and `lock_failed`, and require `boundary_endpoints == 0` for `drive="stationary"`. Add each rejected object beside a reachable control and include mutations that remove each relation.

## Original-finding closure matrix

| Original finding | Independent closure result |
| --- | --- |
| Decimal dwell equality/order/invariants | **Closed for timing/order.** `0.1 -> 0.3` commits at `0.3`; a `1e-12` early endpoint does not; a one-ulp-near equality is accepted only within its computed allowance; nonuniform samples work; duplicate/backward/already-committed calls reject; `1e12` with `dwell=1e-3` refuses as unresolvable. A scale sweep's largest accepted allowance was `4.76837158203125e-7` of dwell, below the `1e-6` hard budget. Constructor reachability remains open under the separate finding above. |
| Missing stationary S4 | **Closed.** Independent central/interior/near-edge x zero/weak/intermediate/strong x full/width produced 24 nonzero-stationary records with empty crossing lists, zero boundary endpoints and valid labels/counts. Equality and outside detunings use an empty schedule; strict interiors use `OpenSchedule`. The preserved pulsed matrix produced 24 separately labelled records and real boundary endpoints. No fake wide pulse was used. |
| Frozen rate | **Primary factory and derivation closed; public bypass open.** The raw factory and extreme-domain arithmetic pass, but exported `ClockPath -> run_one_clock` remains tunable as reproduced above. |
| Large lift resolution | **Closed.** Both signs of `1e16`, `1e17`, `2**21`, and the adjacent outside floats reject through `PathState`, `nearest_lift`, `continuous_lift`, `ClockPath.initial_state`, and the raw runner. One ulp inside the boundary remains accepted. Across cut, exact-half-turn, 100-turn, million-radian and adjacent-boundary controls, independent reconstruction found maximum principal congruence error `4.656612873077393e-10 < 1e-9`. A monkeypatched key counter remained zero on an initial `1e16` refusal. |
| Exact-`pi` lock band | **Closed.** `RawEventConfig`, `raw_event_config`, validation, noise, criterion and path factories reject exact `pi`, including an `object.__setattr__`-mutated frozen config. `nextafter(pi, 0)` works through every factory. |
| Contradictory states/records | **Partially closed; open** for entry/reset/live conservation, stationary-boundary consistency, and the frozen-rate record bypass above. |
| Stale Ticket-01 source/README | **Closed.** The raw runner states current one-clock dynamics and the still-absent population race, disk ledger, oracle/audit and statistics. Mechanical forbidden-phrase checks pass. File-local statements in `stochastic.py` and `raw_config.py` correctly say those individual modules contain no stepper/dwell and are not stale package claims. |

## Independent numerical, mutation, isolation and compatibility evidence

- The independent repair probe made 248 passing assertions. Besides the values above, it enumerated malformed rate ranges, constructor invariants, already-committed refusal, full/width stationary and pulsed matrices, exact threshold schedules, arbitrary configuration changes, ordinary large winding, circular-cut continuation, exact half-turn behavior, raw pre-key lift refusal, exact-`pi` factories, and generated-record reconstruction.
- The full dynamics mutation check catches **22/22** named mutations: wrapped authority, dropped lift, `stable_phase` at equality, free outside-tongue mismatch, end-frozen drift, recomputed endpoint, model-specific split stream, proportional child, coupling-scaled diffusion/rate/dwell, sample-counted and retroactive dwell, missing reset, removed contraction, non-strict boundaries, missing/effectively-unbounded equality allowance, missing last timestamp, missing lift domain, raw rate argument, and fake stationary pulse. The two constructor invariants and direct-rate runner bypass above are additional discriminating mutations the battery does not yet contain.
- An independent AST walk from package root, `raw_runner` and `raw_ledger` reached exactly `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, and `validation`. Runtime clean-process imports reached no `analytic`, `simulate`, `verify`, predictor, comparator or oracle module. No reachable filesystem writer or static three-dimensional allocation was found. Placing stepping in `dynamics.py` remains harmless technical drift: it is reached by the isolated raw graph and consumes Ticket 02 leaves without changing noise ownership.
- Public validation remains **143 callables / 486 invalid calls / 309 parameters**, all passing. The new findings demonstrate the documented limitation of that table: per-parameter invalid probes are not exhaustive cross-field reachability proofs.
- `stochastic.py` remains SHA-256 `e6a3f649...`; `KEY_SCHEMA` remains `dk-phase-noise/v3/physical`; Ticket 02 keyed values therefore have unchanged source and the canonical S0/split residuals remain exactly `3.460 / 1.171`. No model label or coupling reaches the noise law.
- The 65 checks that existed before this fix-up retain the formatted residual/tolerance pairs recorded in the first review. Load-bearing values remain wrapping `8.452e-15`, stationary arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`, Ticket 02 S0/split `3.460 / 1.171`, Ticket 03 zero-noise Euler `3.537e-03`, lift/winding `7.105e-15`, and S4 record residual `1.754e-02`; no tolerance weakened.

## Commands, environment and source snapshot

Environment: macOS 26.5.2 arm64; Python 3.13.11; NumPy 2.4.3; SciPy 1.16.3.

Successful commands included:

```text
python -m adler_born_two_channel.verify
python -m adler_born_two_channel.verify --verbose
python adler_born_two_channel/verify.py
python -W error -m adler_born_two_channel.verify
python -W error adler_born_two_channel/verify.py
PYTHONHASHSEED=0 python -m adler_born_two_channel.verify
PYTHONHASHSEED=987654321 python -m adler_born_two_channel.verify
python -m compileall -q adler_born_two_channel
```

The module and direct-script `--prove-failure-exit` commands each exited exactly 1 with only the deliberate probe failing. Canonical, verbose, direct, both warning-as-error paths and both hash seeds passed 71/71. The initial invalid-CLI check exited 2 as argparse specifies and was not treated as the deliberate harness proof; it was rerun with the intended flag.

Review-time SHA-256 values: `commitment.py 66866bd4...`, `dynamics.py 6ff0b8b5...`, `raw_config.py 19779ed9...`, `raw_experiments.py 95332c44...`, `raw_runner.py e7b5297f...`, `stochastic.py e6a3f649...`, `verify.py 97560677...`, package `README.md e5f3532c...`. No implementation, test, README or Git state was edited by this review; only this artifact was appended. The repository already contains unrelated user changes and an untracked package, so scope evidence is the source snapshot and the assigning implementer's preserved handoff, not a claim that the repository is globally clean.

## Limitations and explicit non-claims

This remains raw one-clock mechanism validation. It does not validate or add a population race, channel competition, first-winner stop, disk ledger, killed-diffusion oracle, moving-band audit, stationary-hazard analysis, burn-in semantics, survival curve, exponent fit, scaling law, detector click, absorption, measurement outcome, microscopic bath, or Born-selection claim. Stationary S4 is a finite-window one-clock trajectory matrix only. Endpoint accounting can still miss a leave-and-return between samples; the later killed-diffusion oracle is still required before physical interpretation.

Ticket 03 must remain status 1/OPEN until the public rate bypass and unreachable ledger states are repaired and independently re-probed.

# Final closure re-review after the two-bypass fix-up — 2026-08-27

## Verdict

**OPEN — both requested bypasses are closed, but one adjacent public stale-path defect remains.** Exact rate identity is now enforced at construction, execution and recording; unreachable dwell/record ledgers are now refused; all requested controls, generated records and four new mutations pass. However, `run_one_clock` adopts the `object.__setattr__` stale-object threat model only for `fixed_rate`. The same mutation can change an exported `ClockPath.detuning` after its schedule was cached, and the runner accepts and records the new detuning with the old tongue crossings. This silently changes eligibility and commitment timing under an ordinary record label.

The expanded verifier passes **73/73** throughout the required command matrix, and its 71 prior formatted residual/tolerance pairs remain unchanged. That is strong regression evidence but cannot close a directly reproduced raw-path inconsistency.

## High — `run_one_clock` revalidates a smuggled rate but accepts a smuggled detuning with a stale tongue schedule

**Where:** `dynamics.py:926-1002`; `raw_experiments.py:438-482`.

`ClockPath.__post_init__` derives and caches `_schedule = train.schedule(detuning)`. The exact schedule is load-bearing: it owns the Brownian crossing split, entry/exit handoffs, eligibility states, endpoint targets and dwell start/reset geometry. The new `run_one_clock` check correctly refuses a post-construction edit of `fixed_rate`, explicitly because a frozen dataclass is not frozen against `object.__setattr__`. It does not revalidate the other fields that define the cached schedule.

Independent reproduction:

```python
train = PulseTrain((RaisedCosinePulse(1.0, 4.0, 2.0),))
path = ClockPath(0.9, train, "full", 0.0)
object.__setattr__(path, "detuning", 0.1)
record, _ = run_one_clock(path, criterion, stream, 0, 0, 0.1, 0, 400,
                          "ordinary")
```

The accepted path and a freshly constructed control disagree:

```text
                         stale accepted path                 fresh path
recorded detuning        0.1                                 0.1
schedule                 (1.590334470601733,                 (0.40966552939826695,
                           2.409665529398267)                   3.590334470601733)
category                 committed                           committed
committed_at             1.9000000000000001                  1.02
endpoints                191                                 103
eligible_endpoints       31                                  62
boundary_endpoints       1                                   1
final_phase              0.1459422334001247                  0.17171640847850062
```

The stale path's schedule is exactly the schedule for the original `0.9` mismatch, while its record says `0.1`. This is not merely a malicious object that later fails validation: it returns an ordinary committed `OneClockRecord`. Between `0.4097` and `1.5903`, and again between `2.4097` and `3.5903`, the actual `0.1` clock is strictly eligible but the accepted path treats it as ineligible and therefore uses the wrong transition/control branch and dwell geometry.

The failure matters under the fix-up's own threat model. `run_one_clock` now states that a frozen dataclass must be rechecked because `object.__setattr__` can smuggle a semantic change past construction. `detuning` and `train` are at least as semantic as the rate because `_schedule` is derived from them once. Rechecking only the rate closes one bypass while leaving the cached causal geometry stale.

**Bounded fix:** at the execution boundary, reconstruct/validate the complete `ClockPath` snapshot before any keys are drawn, and require its freshly derived schedule to equal the cached schedule; use the rebuilt snapshot for the run or reject stale input. Rebuild the exact drive/pulse values as needed rather than trusting a previously validated frozen container. Add the reproduction above, a mutated pulse/train control, a mutated cached schedule control, and a clean path beside each; require every refusal before `elementary_leaves` or any key derivation. A narrower minimum fix is to rederive `path.train.schedule(path.detuning)` and compare it exactly to `path.schedule`, but a full snapshot rebuild better matches `validate_raw_config` and avoids moving the stale seam to a nested drive field.

## The two requested bypasses are independently closed

### Frozen rate

- Both stationary and pulsed `ClockPath` construction refused width-only rates `0.1`, `7.0`, `0.0`, `1.0`, twice the frozen value, and both adjacent floats. Only `FIXED_CONTRACTION_RATE == 1.0000000000000002` was accepted. Full paths accepted exactly zero and refused the frozen value, `0.1`, and the adjacent nonzero floats.
- `run_one_clock` refused `fixed_rate` values smuggled with `object.__setattr__`, including both adjacent floats, before `PhaseNoiseStream.elementary_leaves` was called. Legal full/width stationary paths ran and recorded exact rates `0.0 / 1.0000000000000002`; independently generated pulsed paths did likewise.
- `OneClockRecord` refused ordinary width rows at `0.1`, `7.0`, `0.0`, `1.0` and both adjacent floats, and refused a full row carrying the control rate. Legal full and width records remained constructible.
- Production exports contain no sensitivity entry point. The only callable export whose name contains `rate` is `fixed_contraction_rate(lower_peak, upper_peak)`, which derives from a coupling range and cannot inject a scalar into any path. `raw_one_clock_path` has no rate parameter.

### Reachable ledgers

- All four earlier impossible `DwellState` objects now reject: a historical entry with no inside latch; an inside latch with zero entries; one entry both live and reset; and two ended entries with no reset. Additional history with `last_time=None` also rejects.
- Reachable initial, processed-ineligible, eligible-never-inside, live, reset, second-live and second-dwell committed states construct. Along an independent ten-sample sequence containing two resets, a falling-edge eligibility loss and a commitment, `entries == resets + live` and `ever_inside == (entries > 0)` held at every processed endpoint; the final state committed with `entries=3`, `resets=2`.
- `OneClockRecord` refused `dwell_failed 5/0`, `committed 5/0`, `committed 2/2`, never-eligible/lock-failed rows carrying entry history, resets beyond entries, stationary boundary count 1, endpoint subtotal overflow and all exact-rate contradictions. Six hand-built reachable category/live controls and both legal rate controls succeeded.
- An independently generated 48-record matrix — central/interior/near-edge × zero/weak/intermediate/strong noise × pulsed/stationary × full/width — obeyed rate identity, entry/reset conservation, committed-live implication and stationary zero-boundary geometry in every row.

### Mutation sensitivity

Four independent removed-rule predicates accepted the old failures while current production rejected them: positive-only rate validation accepted `0.1/7.0`; old `resets <= entries` state validation accepted all four impossible states; old record validation accepted `5/0` and committed `2/2`; and a missing stationary-boundary rule accepted boundary count 1. The canonical mutation battery independently reports **26/26** caught, adding the exact frozen-rate, state conservation/latch, record conservation and stationary-boundary mutations to the earlier 22.

## Previously closed findings and compatibility

- Decimal dwell equality remains closed: inside endpoints `0.1, 0.2, 0.3` with dwell `0.2` commit at `0.3`; ordering, allowance budget and large-origin refusal remain unchanged.
- Stationary S4 still uses `OpenSchedule`, empty crossings and zero boundary endpoints; the pulsed matrix remains separately labelled.
- The midpoint derivation remains finite and positive at minimum-subnormal, `1e-300`, and `DBL_MAX` controls. The provisional one-ulp rate compatibility change remains explicit.
- Both signs of `1e16/1e17` remain refused; one ulp inside the lift boundary had independently reconstructed principal congruence error `2.3283064365386963e-10 < 1e-9`.
- Exact `pi` remains refused while the adjacent strict interior remains accepted. Current one-clock/still-absent stage documentation and non-claims remain accurate.
- `stochastic.py` remains SHA-256 `e6a3f649...`, `KEY_SCHEMA` remains `dk-phase-noise/v3/physical`, and canonical S0/split residuals remain exactly `3.460 / 1.171`. No accepted Ticket 02 keyed value changed.
- The 71 checks predating this final fix-up retained their formatted residuals and tolerances. Load-bearing values remain wrapping `8.452e-15`, stationary arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`, zero-noise Euler `3.537e-03`, lift/winding `7.105e-15`, record residual `1.754e-02`, lift congruence `1.850e-10`, and the v3 residuals above; no tolerance weakened.

## Commands, isolation, API and source snapshot

Environment remains macOS 26.5.2 arm64; Python 3.13.11; NumPy 2.4.3; SciPy 1.16.3.

Canonical, verbose, direct-script, module warning-as-error, direct warning-as-error, `PYTHONHASHSEED=0`, and `PYTHONHASHSEED=987654321` each passed **73/73**. Module and direct-script `--prove-failure-exit` each exited exactly 1 with only the deliberate probe failing. `python -m compileall -q adler_born_two_channel` succeeded.

Public evidence is **143 callables / 487 invalid calls / 309 parameters**. Independent AST reachability from the raw roots is unchanged: `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, `validation`; clean runtime import reaches the same raw implementation modules and no analytic, simulation, verifier, predictor, comparator or oracle. The raw graph contains no file writer and no static three-dimensional allocation.

Review-time SHA-256 values: `__init__.py 05abc217...`, `commitment.py 91793eae...`, `dynamics.py a60f2007...`, `raw_config.py 19779ed9...`, `raw_experiments.py 219256a7...`, `raw_runner.py e7b5297f...`, `stochastic.py e6a3f649...`, `verify.py 380f751e...`, package `README.md a09c2a94...`. The final fix-up source scope is consistent with the handoff: version/export, commitment invariants, path/rate validation, record/runner validation, tests and package README; no population, ledger-on-disk, oracle, hazard or analysis module was added. No implementation, test, README or Git state was edited by this review; only this artifact was appended.

## Limitations and non-claims

The same explicit limits remain. This is one raw clock, not a population race or channel outcome. Commitment is timestamp dwell under strict proximity and contraction, not a detector click, absorption, measurement outcome or Born event. There is no disk ledger, killed-diffusion oracle, moving-band audit, stationary-hazard analysis, survival curve, exponent fit or scaling claim. Endpoint accounting can still miss a between-sample leave-and-return, so later oracle/convergence gates remain required before interpreting pulsed records as physics.

Ticket 03 must remain status 1/OPEN until the stale detuning/train/schedule execution boundary is repaired and independently re-probed.

# Definitive closure re-review after path/criterion snapshots — 2026-08-27

## Verdict

**OPEN — the two high-level experiment boundaries are repaired, but the exported primitive state-machine/stepper doors still accept the same stale objects.** `validate_clock_path`, `validate_lock_criterion`, `run_one_clock`, and `synthetic_dwell_history` pass every requested snapshot, nested rebuild, schedule-equality, zero-consumption and clean bit-identity probe. The expanded suite passes **74/74** everywhere. However, `LockCriterion.advance` remains a public state transition and accepts a criterion edited to `tolerance = pi`, producing the formerly forbidden commitment from a 3-radian error. Likewise the exported `ClockPath` stepping/observation methods accept a detuning paired with its old cached schedule and produce the wrong width-only transition and eligibility state. The closure request explicitly required that no other public experiment/state-machine door accept stale criterion or cached path state; that requirement is not yet met.

## High — public primitive transitions bypass the new trusted snapshots

**Where:** `commitment.py:466-580`; `dynamics.py:1004-1285`; snapshot validators at `commitment.py:582-606` and `dynamics.py:1290-1382`.

The new validators are sound at the two helpers that call them. They are not enforced by the public objects whose methods actually perform the transition. Both classes are exported; their public methods are included in the 145-callable API table; and earlier reviews correctly treated `LockCriterion.advance`, rather than `synthetic_dwell_history`, as the actual state machine when requiring time-order validation there.

### Direct stale criterion reproduction

```python
criterion = LockCriterion(0.25, 0.3)
object.__setattr__(criterion, "tolerance", math.pi)

state = DwellState()
state = criterion.advance(state, 0.0, True, 3.0, -1.0)
state = criterion.advance(state, 0.3, True, 3.0, -1.0)
```

Result:

```text
category      committed
committed_at  0.3
lock error    3.0 rad
```

`3.0 < pi`, so the edited object admits an error far outside the largest legal band and commits. Both new high-level doors refuse this exact object, but the exported `advance` door does not call `validate_lock_criterion`. A negative dwell happens to raise through `elapsed_allowance` on an inside sample, but that incidental downstream check does not repair the invalid tolerance or guarantee refusal before a transition on all branches.

### Direct stale width-only stepper reproduction

```python
path = ClockPath(0.9, train, "width_only", FIXED_CONTRACTION_RATE)
object.__setattr__(path, "detuning", 0.1)

# Public crossings / initial_state / advance / observe walk, no run_one_clock.
```

After 51 zero-noise steps of `0.01`, the stale and freshly rebuilt `0.1` paths report:

```text
               stale public primitives        fresh trusted path
time           0.51                           0.51
phase          0.14751832500889214            -0.6151793069386349
has target     False                          True
state          outside                        interior
eligible       False                          True
target         NaN                            0.7177694220123114
```

The stale path takes the full Adler transition because its cached `0.9` schedule says outside; the fresh `0.1` width-only path is already eligible and takes the fixed-contraction transition. Thus this is not merely a stale reporting property: it changes the phase update itself.

**Bounded fix:** make every public transition path use a validated snapshot, or separate public validated wrappers from private unchecked kernels. A practical structure is `advance -> validate/rebuild once -> _advance_validated`, with `run_one_clock` retaining and calling the private validated kernel across its loop so it does not rebuild the pulse train and schedule at every leaf. Apply the same pattern to `LockCriterion.advance`; route `inside_now` through validated state or keep an unchecked private predicate used only after validation. For `ClockPath`, cover the public sequence needed for a direct walk (`crossings`, `initial_state`, `advance`, `observe`, and coordinate handoffs), or make those unchecked methods private and expose stepping only on a distinct trusted snapshot type. Add the exact two reproductions above and mutations that reduce each public wrapper to its current unchecked body.

## Snapshot validators and high-level boundaries independently pass

### Complete path rebuild and preflight refusal

- `validate_clock_path` requires exact `ClockPath`, exact drive kind, exact `RaisedCosinePulse` members, rebuilds every pulse from `peak/duration/center`, rebuilds `PulseTrain` or `StationaryDrive`, rebuilds `ClockPath(detuning, model, rate)`, derives a fresh schedule, and requires exact schedule type and value equality. The returned object, not the input, is used by `run_one_clock`.
- Independent mutations covered **16** path seams: stale `0.9 -> 0.1` detuning, whole train, drive-kind swap, nested peak/duration/center, invalid nested peak, malformed nested member, planted `TongueSchedule`, planted `OpenSchedule`, model, rate, non-drive value, stationary peak, stationary detuning, and missing cache.
- Every refusal was a `TypeError` or `ValueError` with **zero** `elementary_leaves` calls and **zero** `_normals_from_key` calls. The missing cache takes its dedicated refusal path.
- Schedule-preserving edits are safely normalized into the rebuilt snapshot; schedule-changing or malformed edits refuse. The type/value cache comparison is exact.

### Criterion rebuild at both helpers

- `validate_lock_criterion` exact-type rebuilds `LockCriterion(tolerance, dwell)`. Edited tolerances at `pi`, one ulp above, zero and negative, and dwells at zero and negative refused at both `run_one_clock` and `synthetic_dwell_history`.
- `run_one_clock` refusals consumed zero leaves/keys. `synthetic_dwell_history` refusals invoked `LockCriterion.advance` zero times, so they occurred before a state transition.
- The formerly committed `tolerance=pi`, error `3.0` history and the negative-dwell first-inside case are refused by both helpers. A clean five-sample committing history was bit-identical through the original criterion, its rebuilt copy, and a direct clean `advance` walk.

### Clean bit identity and generated records

- Four clean pulsed/stationary × full/width paths rebuilt equal by value with the same schedule and drive digest. `run_one_clock` record and phase tuples were bit-identical to an independently written direct trusted walk that did not use either validator.
- An independent 48-cell S4 regeneration compared every high-level run against the same manual trusted walk. All **48 records and phase histories were exactly equal**. The independent category counts were 39 committed, 2 lock-failed, and 7 dwell-failed for this declared seed/initial-phase set; every record retained the frozen rate, conservation and stationary-boundary laws.
- All previously closed dwell, stationary, rate, lift, exact-`pi`, ledger, documentation and non-claim findings remain closed at the high-level boundaries.

## Regression, mutation, isolation and compatibility evidence

- Canonical, verbose, direct-script, module warning-as-error, direct warning-as-error, `PYTHONHASHSEED=0`, and `PYTHONHASHSEED=987654321` each passed **74/74**. Module and direct `--prove-failure-exit` each exited exactly 1 with only the deliberate failure. `compileall` succeeded.
- All 73 check lines predating the snapshot check retain their recorded residual/tolerance pairs, and the second-door edit leaves all 74 lines unchanged. Load-bearing numerical values and every tolerance remain as recorded in the prior sections.
- The canonical mutation battery catches **32/32**: the earlier 26 plus stale detuning, stale drive, planted schedule, nested pulse field, half-turn criterion and negative-dwell criterion snapshot mutations. The missing mutations are the direct public primitive bypasses above.
- Public evidence is **145 callables / 495 invalid calls / 311 parameters**. The validators are exported and their declared valid/invalid calls pass. The API-table limitation remains the one its own detail states: parameter coverage is not exhaustive state/cross-field coverage.
- Raw AST reachability remains `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, `validation`; clean runtime imports reach no analytic, simulation, verifier, predictor, comparator or oracle. No raw file writer or static three-dimensional allocation was found.
- `stochastic.py` remains SHA-256 `e6a3f649...`; `KEY_SCHEMA` remains `dk-phase-noise/v3/physical`; S0/split residuals remain `3.460 / 1.171`, so Ticket 02 source and accepted keyed values are unchanged.

Review-time SHA-256 values: `__init__.py 787134fb...`, `commitment.py 6e39b26d...`, `dynamics.py b18805d8...`, `raw_config.py 19779ed9...`, `raw_experiments.py abcaf2a7...`, `raw_runner.py e7b5297f...`, `stochastic.py e6a3f649...`, `verify.py 18001b43...`, package `README.md 60fd3936...`. The implementation scope is limited to exports/version, the two validators, their two high-level callers, verification and package documentation. No implementation, test, README or Git state was edited by this review; only this artifact was appended.

## Limitations and non-claims

No product boundary moved: this is still one raw clock, not a population race, channel outcome or disk ledger. Commitment remains a band-and-contraction dwell, not a detector click, absorption, measurement outcome or Born event. No killed-diffusion oracle, moving-band audit, stationary-hazard analysis, survival curve, exponent fit or scaling claim exists. Endpoint accounting still needs the later oracle/convergence gates before physical interpretation.

Ticket 03 is **not** ready for status 2 while its exported primitive state-machine/stepper methods accept stale objects that the two helper boundaries refuse.

# Definitive re-review after validated public primitives and TreeLeaf completion — 2026-08-27

## Verdict

**OPEN — the path, criterion, dwell-state and TreeLeaf constructor-domain bypasses are closed, but the new `PathState` rebuild is not a complete state validation.** A constructor-valid live auxiliary pair can be one radian off the path's actual target while still satisfying `phase = target_lift + error` to rounding. Public `ClockPath.observe` and `ClockPath.advance` accept it; the latter changes the next authoritative phase by about `0.924` rad relative to the clean state. The public handoff methods also accept the opposite crossing orientation. These are actionable defects in the explicit validated-public-primitives contract, so Ticket 03 is **not ready for status 2**.

The requested repairs themselves otherwise work. Across 84 independently generated stale path/door combinations, every public `ClockPath` door refused before any trusted kernel ran. Stale criteria and unreachable `DwellState` inputs likewise refused before the state-machine kernel. All nine malformed/duck-typed `TreeLeaf` probes refused before `_advance_trusted`, including both address fields, while a clean leaf remained bit-identical. Clean pulsed/stationary × full/width public walks, trusted walks and high-level runs remained identical.

## High — rebuilding `PathState` through its constructor does not validate the authoritative lifted state

**Where:** `dynamics.py:787-860`, public wrappers at `1091-1230` and `1340-1352`, `_validated_path_state` at `1431-1446`.

`_validated_path_state` does exactly what the fix-up says mechanically: exact-type checks and reconstructs all four fields through `PathState`. The constructor, however, validates only finiteness/resolution and whether `target_lift` and `error` are both live or both NaN. It does not enforce the documented reconstruction identity, and it cannot by itself establish that a live lift is congruent to this `ClockPath`'s actual principal target.

Independent reproduction on a stationary width-only path:

```python
path = ClockPath(0.35, StationaryDrive(1.0),
                 "width_only", FIXED_CONTRACTION_RATE)
clean = path.initial_state(0.0, 0.2)

# Still constructor-valid, and reconstruction still holds to rounding.
forged = PathState(clean.time, clean.phase,
                   clean.target_lift + 1.0, clean.error - 1.0)
seen = path.observe(forged)
stepped = path.advance(
    forged, TreeLeaf(0.0, 0.1, 0.0, "root", 0), 0.1)
```

Result:

```text
forged lift congruence error from the real target   1.0 rad
(target_lift + error) - phase                       -5.551115123125783e-17
public observed lock error                          -1.1575711036455103
public next phase from forged state                 -0.7084169548957528
public next phase from clean state                   0.21569198662706887
```

Thus merely preserving the reconstruction identity is necessary and not sufficient: the wrong target plus compensating error changes `sin(error)` and therefore the width-only transition. An even simpler post-construction edit, `object.__setattr__(state, "error", state.error + 1.0)`, is also accepted; it carries `lift_residual == 1.0`, reports lock error `0.8424288963544897`, and steps to phase `1.1253737880122676`. Neither reaches a key, but both reach and execute the trusted transition through the public wrapper.

The same missing path-aware invariants open other direct observation states: a full-model path accepts a live auxiliary pair and reports it as its target, and a strictly interior width-only path accepts a state with no auxiliary pair and observes it using the full-model branch. Clean high-level runs never create these objects, which is why all generated-record checks remain green; the defect is at the exported direct primitive boundary the fix-up was specifically meant to close.

**Bounded fix:** after exact-type reconstruction, validate the pair against the rebuilt path before any trusted kernel: enforce the reconstruction identity within a declared rounding bound; require a live pair only for `width_only`; require it at every strictly interior width-only state; reject it outside; and require its lift to be congruent within `LIFT_RESOLUTION` to `stable_phase` in the interior or `boundary_phase` at a crossing. Entry and exit wrappers can then add their narrower preconditions. Add direct mutations for `error += 1`, `lift += 1; error -= 1`, a live pair on `full`, and a missing pair in a width-only interior state, with a trusted-kernel counter required to stay zero on refusal.

## Medium — public entry and exit handoffs do not distinguish crossing direction

**Where:** `dynamics.py:1125-1202`, `_require_crossing` at `1316-1324`.

Both public wrappers rebuild the path and state, but `_require_crossing(time, what)` ignores `what`: it accepts any `boundary`, not the named rising entry or falling exit. With a single window `(0.5, 1.5)`:

```text
path.entry_handoff(PathState(time=1.5, phase=0.2))  -> accepted, target live
path.exit_handoff(live_state_at_time_0.5)           -> accepted, target discarded
```

Both preserve phase, but each performs the opposite coordinate operation at the wrong edge. This contradicts the public methods' exact-entry/exact-exit contract and can also make a direct observation select the wrong auxiliary/full contraction branch at that boundary.

**Bounded fix:** make the handoff precondition edge-specific: entry time must equal a window's first endpoint and exit time its second. Add the symmetric wrong-edge controls and mutations; both must refuse before `_entry_handoff_trusted` / `_exit_handoff_trusted` changes the auxiliary state.

## Independently closed parts of the requested refactor

### Public snapshots and pre-transition refusal

- Twelve stale path seams—detuning `0.9 -> 0.1`, whole train, drive kind, nested peak/duration/center, malformed nested member, planted `TongueSchedule`, planted `OpenSchedule`, model, rate, and missing cache—were crossed with all seven public doors: schedule, crossings, initial state, entry, exit, advance and observe. All **84/84** calls raised `TypeError` or `ValueError`; counters around all six trusted transition kernels remained exactly zero.
- `LockCriterion(tolerance=pi)` refused at both `inside_now` and `advance`. An edited impossible `DwellState` refused at `advance`; the module-level trusted transition counter remained zero for both advancing refusals. A clean `0.0, 0.1, 0.2, 0.3` direct history was bit-identical to `synthetic_dwell_history` and committed at `0.3` for dwell `0.3` from its first `0.0` sample.
- `ClockPath.advance` refused NaN/inf kick, negative duration, NaN start, step indices `-5` and `1.5`, node paths `"XYZ"` and `""`, and a duck-typed leaf. None reached `_advance_trusted`. A clean leaf gave an exactly equal `PathState` through the public wrapper and private trusted kernel.
- Four clean pulsed/stationary × full/width paths were walked independently through public wrappers, rebuilt trusted kernels and `run_one_clock`. Every state and observation matched NaN-aware field-for-field; all positive-duration phase histories were exactly equal. Instrumenting `_validated_tree_leaf` during a high-level run recorded zero calls, confirming that `run_one_clock` remains on stream-produced trusted leaves.
- No `_trusted` or `_validated_*` helper appears in the `__all__` of `commitment`, `dynamics`, `raw_experiments`, `raw_runner` or `stochastic`. The only production trusted-kernel callers are the validated wrappers and the two high-level loops after their one-time snapshots; verifier-only mutant calls remain outside the raw product path.

### Earlier closures, isolation and mutation sensitivity

- The current canonical output retains the **74 pre-existing check names and formatted residual/tolerance pairs**; their normalized line set has SHA-256 `33a4ab250ade71f9b4de0d74b7ec9bd03ecdc7fa6d12f9ccf04384526257eb3b`. All load-bearing values remain unchanged, including zero-noise Euler `3.537e-03`, lift/winding `7.105e-15`, S4 record residual `1.754e-02`, lift congruence `1.850e-10`, and Ticket 02 noise/split residuals `3.460 / 1.171`. The added primitive check is zero-residual.
- `stochastic.py` remains SHA-256 `e6a3f649...`, and `KEY_SCHEMA` remains `dk-phase-noise/v3/physical`; no Ticket 02 source, address grammar or keyed residual moved.
- The canonical **40/40** mutation battery remains sensitive to every listed old mutation, including all public wrapper removals and the invalid TreeLeaf address mutations. It does **not** contain the constructor-valid live-pair/congruence or wrong-edge handoff mutations above; the green mutation count therefore does not close these findings.
- An independent AST walk from package root, `raw_runner` and `raw_ledger` reached exactly `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, and `validation`. A clean runtime import reached the same raw implementation modules and no analytic, simulation, verifier, predictor, comparator or oracle. The raw graph contains no filesystem writer and no static three-axis allocation.
- Public evidence remains **145 callables / 497 invalid calls / 311 parameters**. This result's own documented limitation—parameter coverage is not exhaustive value-class or cross-field coverage—is exactly why the accepted live-pair state was not detected.
- Previously closed dwell equality/order/allowance, stationary S4, frozen rate, lift-resolution magnitude, exact-`pi`, state/record ledger, stale-schedule and source/README findings remain closed for their tested domains. The current four-path direct comparison independently corroborates that the wrapper refactor did not change clean generated dynamics. The outstanding `PathState` defect extends, rather than reopens, the large-lift finding: accepted generated states are still congruent; an exported constructor-valid supplied state need not be.

## Commands, environment, source snapshot and compatibility

Environment: macOS 26.5.2 arm64 (build 25F84); Python 3.12.6; NumPy 2.3.5; SciPy 1.15.3.

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 75/75, exit 0 |
| `python3 -m adler_born_two_channel.verify --verbose` | 75/75, exit 0 |
| `python3 adler_born_two_channel/verify.py` | 75/75, exit 0 |
| module/direct with `PYTHONWARNINGS=error` | 75/75, exit 0 both |
| module/direct with `python3 -W error` | 75/75, exit 0 both |
| `PYTHONHASHSEED=0` / `987654321` | 75/75; all 75 printed lines byte-identical |
| module/direct `--prove-failure-exit` | 75/76, exit 1 both; only deliberate probe failed |
| `python3 -m compileall -q adler_born_two_channel` | exit 0 |
| independent wrapper/state/leaf script | 104 passing assertions plus the exact defects above |

The three canonical/hash-seed `[PASS]` line files are byte-identical, SHA-256 `d6b7c1f03fc76cff6205f67735e0fc1bc0d32a999b439369044c4ae3af13a987`.

Review-time source SHA-256 values: `__init__.py c079dcc7...`, `commitment.py 7f121245...`, `dynamics.py d750ed18...`, `raw_config.py 19779ed9...`, `raw_experiments.py feaf69f9...`, `raw_runner.py e7b5297f...`, `stochastic.py e6a3f649...`, `verify.py 90f49f33...`, package `README.md b0db885e...`. Relative to the previous review snapshot, changes are confined to the expected package version/export, validated primitive kernels/callers, verifier and package documentation; the repository already contains unrelated user changes outside this untracked package. This review edited no implementation, tests, README or Git state; only this review artifact was appended.

For clean callers, compatibility is intact: public, trusted and high-level paths are bit-identical, and the high-level record path still consumes the exact Ticket 02 chronological stream. The intentional compatibility tightening is limited to malformed or stale constructor-domain inputs. A constructor-valid but path-inconsistent `PathState` is currently accepted rather than tightened, which is the blocker above.

One narrower limitation is recorded without treating it as a separate defect under this ticket's declared contract: reconstructing a `TreeLeaf` proves that each field lies in Ticket 02's constructor domain, but a `ClockPath` has no mesh/stream context with which to authenticate a different yet canonical step index or node path. The high-level runner avoids that provenance problem by accepting leaves only from its validated `PhaseNoiseStream`.

## Scope, limitations and non-claims

This remains one raw clock. No population race, first-winner stop, channel outcome, disk ledger, killed-diffusion oracle, moving-band audit, stationary hazard, survival curve, exponent fit, scaling law, detector click, absorption, measurement outcome or Born claim was added or inferred. Commitment remains strict timestamp dwell under proximity plus contraction, and endpoint accounting still needs the later killed-diffusion/convergence gates before pulsed records can be interpreted as physics.

Ticket 03 remains **status 1 / OPEN** until the path-aware live-state invariants and edge-specific handoff preconditions are implemented and independently re-probed.

# Final closure re-review after path-state semantics and directed handoffs — 2026-08-28

## Verdict

**CLOSED — no actionable current Ticket 03 defect remains. Ticket 03 is ready for status 2.**

The last two findings are independently closed. Every named path-inconsistent state now refuses at both public `observe` and public `advance` before either trusted kernel runs. Entry and exit handoffs now accept only their own directed window endpoint, again refusing the opposite edge before a trusted handoff kernel runs. Correct boundary states, large unwrapped errors, clean direct walks and high-level runs remain bit-identical.

This verdict retains the declared `TreeLeaf` provenance limitation as non-blocking: the public primitive rebuild proves constructor-domain/canonical address syntax, while the high-level `PhaseNoiseStream` owns the binding between a canonical address and its kick. The fix introduced no correctness defect beyond that documented boundary.

## Independent closure probes

### Path-aware `PathState` validation

On the exact stationary width-only reproduction (`detuning=0.35`, `peak=1.0`, initial phase `0.2`), I rebuilt and exercised all five inconsistent inputs at both public doors:

| Input | `observe` | `advance` |
| --- | --- | --- |
| `target_lift + 1`, `error - 1` | refused | refused |
| post-construction `error += 1`, residual `1.0` | refused | refused |
| full-model state carrying a live auxiliary pair | refused | refused |
| width-only interior state missing its pair | refused | refused |
| width-only outside state carrying a live pair | refused | refused |

The forged compensating pair was first confirmed to be the original reproduction: reconstruction residual `-5.551115123125783e-17`, but target congruence error exactly `1.0` rad. Counters around `_observe_trusted` and `_advance_trusted` remained **0 / 0** across all ten refusals.

The four rules are all load-bearing and correctly ordered in `_validated_path_state(path, state)`: constructor rebuild, reconstruction within `conservation_tolerance`, full/width pair ownership, schedule-state lifecycle, and congruence to the interior `stable_phase` or equality `boundary_phase` within `LIFT_RESOLUTION`. The rebuilt path is supplied to this validator by every public state-taking wrapper.

Clean controls passed beside the failures: a live interior width-only state, a bare full-model state, and a bare outside width-only state. Unwrapped errors at `-300000, -1000, -37, -5, 0, 5, 37, 1000, 300000` turns remained accepted; the most extreme phases were about `+-1.884955e6`, below the declared lift-resolution boundary. Their observations were the exact circular images of the unwrapped errors, and their next states retained the reconstruction identity within the declared scale-aware bound. The repair therefore validates the target without wrapping or discarding winding.

### Directed handoffs

I used two-window pulsed paths at positive, negative and zero mismatch. For every one of the six finite windows:

- `entry_handoff` at the window's second endpoint refused;
- `exit_handoff` at the window's first endpoint refused;
- counters around `_entry_handoff_trusted` and `_exit_handoff_trusted` remained zero on all **12** wrong-edge calls;
- entry at the first endpoint established the pair;
- exit at the second endpoint discarded it; and
- both correct handoffs preserved the authoritative phase bit for bit.

The edge selector now reads the requested operation rather than merely testing `state_at(time) == "boundary"`. `OpenSchedule` has no finite edges and therefore admits neither handoff, consistent with stationary initialization owning its pair directly.

### Clean public/trusted/high-level identity

Independent zero-noise walks over pulsed/stationary × full/width paths compared every public state and observation with the rebuilt path's trusted kernels, NaN-aware and field-for-field. All four state histories matched, and their positive-duration phase sequences were exactly equal to `run_one_clock`:

```text
pulsed/full             dwell_failed, 43 stored phases
pulsed/width_only       lock_failed,   43 stored phases
stationary/full         dwell_failed, 41 stored phases
stationary/width_only   dwell_failed, 41 stored phases
```

The targeted closure script completed **50 independent assertions**. It did not use verifier helpers as its oracle.

## Regression, mutation, isolation and compatibility evidence

- Canonical, verbose and direct-script executions each passed **75/75**.
- Module and direct-script warning-as-error runs passed under both `PYTHONWARNINGS=error` and `python3 -W error`.
- `PYTHONHASHSEED=0` and `PYTHONHASHSEED=987654321` passed 75/75. Their complete `[PASS]` lines were byte-identical to canonical output.
- Module and direct `--prove-failure-exit` each exited exactly **1**, at 75/76 with only the deliberate probe failing.
- `python3 -m compileall -q adler_born_two_channel` exited 0.
- The current 75 `[PASS]` lines are byte-identical to the complete baseline captured by the preceding independent review, SHA-256 `d6b7c1f03fc76cff6205f67735e0fc1bc0d32a999b439369044c4ae3af13a987`. Thus every prior name, residual and tolerance—including the already-zero primitive check—remains unchanged.
- The mutation battery now catches **46/46**, adding four constructor-only path-state mutations and two undirected-handoff mutations with clean controls beside them.
- Public evidence is **145 callables / 499 invalid calls / 311 parameters**. No signature changed.
- `stochastic.py` remains SHA-256 `e6a3f649...`; `KEY_SCHEMA` remains `dk-phase-noise/v3/physical`; keyed-noise and split residuals remain exactly `3.460 / 1.171`. Ticket 02 source, addresses and accepted keyed values are unchanged.
- The independently recomputed raw AST graph reaches exactly `__init__`, `raw_runner`, `raw_ledger`, `raw_config`, `raw_experiments`, `stochastic`, `dynamics`, `commitment`, `model`, and `validation`. Clean runtime import reaches the same implementation modules and no analytic, simulation, verifier, predictor, comparator or oracle. No filesystem writer or static three-axis allocation exists in the raw graph.
- Private validated/trusted helpers remain absent from every production `__all__`. High-level loops still validate once and use only their own generated states/leaves thereafter.
- Every earlier Ticket 03 closure remains intact: decimal dwell equality/order/allowance, stationary S4, one frozen width rate, lift-resolution magnitude, exact-`pi` lock domain, reachable state/record ledgers, complete path/criterion snapshots, public wrappers, chronological TreeLeaf consumption, authoritative phase/lift behavior for generated states, source accuracy, isolation and explicit non-claims.

Compatibility is the intended tightening only: path-inconsistent supplied states and wrong-edge handoffs that previously ran now raise. Clean public, private and high-level behavior is bit-identical. The version is `0.8.0`; the API signatures and clean record schema are unchanged.

## Environment and source snapshot

Environment: macOS 26.5.2 arm64; Python 3.12.6; NumPy 2.3.5; SciPy 1.15.3.

Review-time SHA-256 values: `__init__.py c03ece8a...`, `commitment.py 7f121245...`, `dynamics.py 9ecfefb4...`, `raw_config.py 19779ed9...`, `raw_experiments.py feaf69f9...`, `raw_runner.py e7b5297f...`, `stochastic.py e6a3f649...`, `verify.py e052caed...`, package `README.md aefd2dd5...`.

Relative to the preceding review snapshot, only the expected version, `dynamics.py`, verifier and package README changed; commitment, raw configuration/experiments/runner and Ticket 02 stochastic source are byte-identical. The repository already contains unrelated user work outside the untracked package. This review edited no implementation, test, README or Git state; only this review artifact was appended.

## Scope, limitations and non-claims

This is still one raw clock, not a population race, first-winner stop, channel outcome or disk ledger. Commitment remains strict timestamp dwell under proximity plus contraction—not a detector click, absorption, measurement outcome or Born event. There is no killed-diffusion oracle, moving-band audit, stationary-hazard analysis, survival curve, exponent fit or scaling claim. Endpoint accounting still needs the later killed-diffusion and convergence gates before pulsed records can be interpreted as physics.

**Final disposition: CLOSED. Ticket 03 is ready for status 2.**
