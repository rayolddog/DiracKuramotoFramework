---
title: "Independent review: Ticket 05 finite one-channel race and immutable ledger"
kind: review
---

# Independent review: Ticket 05

## Strict verdict: OPEN

The race kernel itself survives the independent stop, tie, replay, keying, reproducibility, memory, isolation, shadow-sample, survival, numerical-status, and non-claim probes. The ticket does not close because the on-disk ledger omits required per-clock diagnostics, the version-2 consumer gate accepts recomputed-but-contradictory records, the public race boundary cannot detect a population truncated from the right, and the writer/verifier do not enforce the package-scoped output contract.

These are correctness defects at the declared public and durable boundaries, not requests for extra polish. The first two can make a closed run irreversibly unable to support the later censoring analysis or let a consumer accept rows that do not describe the manifest-bound race.

## Findings, in priority order

### P1 — The immutable schema discards required per-trial/per-clock entry and reset diagnostics

The governing plan's **Complete ledger** requires winner tongue-entry, band-entry, and last-reset times, plus per-clock entry/reset/exposure/commit diagnostics under first-winner censoring. Ticket 05 likewise puts per-clock entry/reset/exposure/commit diagnostics in scope.

The in-memory `ClockExposure` has the needed timestamps (`first_eligible_at`, `first_inside_at`, `last_reset_at`, `committed_at`) in `raw_race.py:229-242`, but the durable schema drops them:

- `CLOCK_COLUMNS` is one row per clock aggregated across all trials and contains only counts and total times (`raw_ledger.py:267-285`). It cannot say which trial contributed an entry, reset, exposure, or win.
- `SHADOW_COLUMNS` retains `(trial, clock)` identity but omits first eligibility, first band entry, last reset, endpoint counts, and final phase (`raw_ledger.py:287-303`).
- `_trial_values` writes winner first eligibility and first band entry but not the winner's required last-reset time (`raw_runner.py:675-701`).
- `_shadow_values` writes only category, commitment, counts, exposure, and opportunity (`raw_runner.py:704-716`).

Consequently a later consumer cannot replay or reconcile the stated per-clock censoring diagnostics from a closed ledger, and a winner's last-reset time is gone permanently. Aggregates are not a substitute: different trial-level histories can produce the same totals and different censoring conclusions.

**Required fix:** retain one censored row per `(trial, clock)` with, at minimum, category, commit time, first eligible time, first inside time, last reset time, entry/reset counts, endpoint counts, exposure, eligible time, and final phase; retain the corresponding declared shadow fields; and add winner last-reset values to the trial view. Either replace the aggregate clock table with this authoritative table and derive aggregates later, or add a fourth authoritative table and close/hash/reconcile it. Update the schema, manifest column declarations, counts, marker, strict parser, README, and mutation checks together.

### P1 — `require_closed_ledger` accepts row content that contradicts the manifest and its own category semantics

The byte, schema, count, identity, and canonical-spelling checks are strict. The semantic gate is not. `_require_consistent_rows` checks only shallow inequalities and the total number of winners across the trial and clock tables (`raw_ledger.py:1208-1318`). It does not:

- derive each unresolved category from `clocks_ever_eligible`, `clocks_ever_inside`, entries, and resets;
- require clock/shadow/winner detunings to equal the manifest's clock-indexed detunings;
- reconcile winner identities with each clock row's `wins` and `co_completions`, rather than only comparing total wins;
- derive per-clock entry/reset/exposure/opportunity aggregates from authoritative per-trial rows; or
- bound aggregate exposure by the manifest's trial count and observation window.

Independent zero-coupling fixture, with every digest and marker recomputed after each edit:

```text
baseline_categories ['never_eligible', 'never_eligible']
forged_unresolved_category_ACCEPTED lock_failed 0 0
forged_detunings_ACCEPTED (0.0,) 0.75 -0.75
forged_clock_aggregates_ACCEPTED 1 999.0
```

The first accepted row says `lock_failed` while zero clocks were ever eligible or inside. The second binds manifest detuning `0.0` to clock and shadow detunings `0.75` and `-0.75`. The third reports one eligible trial and 999 units of exposure in a two-trial, 0.4-unit-window run. All returned a `ClosedLedger`.

This is within the module's own threat model: its documentation explicitly recomputes a marker around a forged row to test row-level authority. Hashes are not authentication, so the semantic gate must establish the relationships it claims after recomputation.

**Required fix:** after adding an authoritative `(trial, clock)` table, derive and compare all category, winner, co-completer, detuning, entry/reset, exposure, eligible-time, inside-at-least-once, and aggregate values. At minimum, reject impossible unresolved categories; require every indexed detuning in every table to match the manifest; reconcile wins by clock, not only in total; enforce window-derived exposure bounds; and add the three successful forgeries above as mutations that must refuse.

### P1 — The public race boundary accepts a population truncated from the right

`ChannelOutcome.__post_init__` checks clock identifiers against `range(len(clocks))` (`raw_race.py:388-400`). That catches a missing clock at the front or middle but makes a trailing omission indistinguishable from a smaller declared population. `_validated_race` similarly accepts any non-empty tuple of same-model paths and has no declared population or grid identity (`raw_race.py:612-643`).

Independent probe:

```text
declared_grid_n 2
full_outcome_clocks 2 [0, 1]
right_truncated_public_race_ACCEPTED 1 [0] never_eligible
```

The serialized writer later catches this because the manifest says how many clock rows must exist, but that is not sufficient for the exported in-memory API: `race_one_channel`, `ChannelOutcome`, and their derived category claim completeness before any ledger exists. Omitting the trailing clock can change the winner, channel category, opportunity, and censoring record.

**Required fix:** bind the public race/outcome to an explicit declared population and immutable grid identity. Validate exact population length, clock identifiers, clock order, and detunings at the race boundary and in `ChannelOutcome`; do not rely on a later writer to repair an already-valid but incomplete public object. Add mutations for right-end truncation and a same-length detuning substitution.

### P2 — The output path and verification cleanup contradict the package-scoped result contract

`raw_results_directory` correctly returns `<package>/results/<run>` and rejects path escape, but its own documentation says `write_raw_run` deliberately accepts an arbitrary directory (`raw_runner.py:390-430`). The writer then calls `Path(directory)` and creates it without a descendant check (`raw_runner.py:803-829`). The canonical verifier also creates `_RUN_ROOT` with unconstrained `tempfile.mkdtemp(...)` and never cleans it (`verify.py:11406-11419`).

That contradicts the governing requirement that generated output be written only beneath the package-scoped ignored results directory, and it leaves complete run fixtures outside the package after every verification invocation. Before this review there were already multiple `adler-raw-verify-*` directories under the platform temporary directory. The six created by this review were identified exactly and removed; no review-created run files remain.

**Required fix:** make the supported writer accept a validated run name or require the resolved target to be a descendant of the package results root. If a scratch/testing writer is necessary, make it a separately named internal/testing surface rather than weakening the production entry point. Put verifier fixtures under a `TemporaryDirectory` context and remove them on success and failure. Add path-escape, arbitrary-absolute-path, symlink-escape, interrupted-run cleanup, and no-leftover checks.

### P3 — The handoff miscounts the new acceptance criteria

The execution notes say “Nine checks are new (acceptance criteria 80–89).” The inclusive range 80–89 has ten criteria, and the suite grew from the prior 85 checks to 95. The live suite reports 95 checks covering 89 acceptance criteria.

**Required fix:** change “Nine” to “Ten,” or name the exact nine if one criterion was not intended to be new.

## What passed independently

### Race and two-pass replay

- The channel stop agrees trial-by-trial with a no-stop walk reduced by an independently transcribed minimum rule.
- Completion times are shared uniform-mesh endpoints; arbitrary deterministic tongue-crossing schedules do not move those endpoints. Pass two therefore reaches the shared stop for every clock.
- Same-endpoint co-completers remain in clock order with their separate mismatches and phases. No random winner source exists in `raw_race.py`.
- Empty populations refuse. One-clock populations run. The canonical synthetic battery covers no commitment, first/final-window behavior, multiple co-completers, unequal crossing schedules, and all four category names.
- Initial phases and Brownian leaves are rederived from the same trial/clock keys in both passes; there is no history cube.

### Keying, execution invariance, shadow sample, and opportunity

- Initial phase addresses are `<schema>/<dataset>/ensemble/trial=<t>/clock=<c>/phase`; timestep and diffusion are absent, while dataset namespace, trial, and clock are present. Fine/coarse, batch, subset, order, and diffusion changes reuse the intended ensemble without cross-trial/clock key collisions.
- A separate small run written with `(clock_block, step_window) = (1, 1)` and `(8, 4096)` produced byte-identical manifest, ledger, clocks, shadow, and close marker.
- The manifest carries no timestamp or live-block size. Row iteration order is explicit and stable.
- `shadow_trials` is validated in `1..trials`, the selection rule is the first identifiers, and the manifest freezes both size and rule before outcomes. The shadow uses the same initial phases and Brownian keys and never enters channel category counts.
- Censored counts are prefix-consistent with no-stop rows; eligible time does not exceed exposure. The missing per-trial durable diagnostics remain the blocker described above.

### Ledger mechanics that are sound

- Version 2 fixes exact manifest fields, table names, field order, and kinds. CSV parsing requires canonical UTF-8, one final newline, exact header/order/width, canonical number/bool spellings, and valid categories.
- Missing, truncated, extended, reordered, duplicated, malformed, edited, wrong-version, and digest/manifest/count mismatches refuse in the canonical mutation battery.
- The close marker is written last. A missing/partial marker or missing table refuses, and a fresh writer refuses to overwrite any of the five run filenames.
- The remaining defect is semantic authority after valid reparsing and recomputation, not the byte-level protocol.

### Isolation, memory, numerical status, survival, and claims

- A fresh-interpreter runtime probe loaded only `commitment`, `dynamics`, `model`, `raw_config`, `raw_experiments`, `raw_ledger`, `raw_race`, `raw_runner`, `stochastic`, and `validation`; it loaded none of `analytic`, `killed_diffusion`, `moving_band_audit`, statistics/comparator/reporting modules, or general dynamic-import paths. `raw_race`, `pathlib`, and `platform` did not create a forbidden transitive reachability path.
- Independent warmed `tracemalloc` race probes measured peak deltas of 48,329 bytes for 1 trial × 8 clocks × 20 steps, 46,312 bytes after quadrupling steps to 80, and 49,816 bytes after quadrupling trials. The working set did not scale with total trials or steps. The two-pass cost is real but streamed; no trials × clocks × steps cube was found.
- The verbose canonical suite measured 618 MB whole-process peak RSS after all Monte Carlo/oracle/audit paths, below its 944 MB regression bound; its largest declared array was 19.2 MB. That whole-suite number is not the race-specific evidence, so the independent race deltas above are the discriminating measurement.
- Ticket 04 is represented accurately: stationary endpoint validation passed at declared reference tolerances; the moving-band audit is `numerical_no_result` pooled and in fourteen of fifteen regime cells; every raw run says `numerical_gate = diagnostic_only`. Ticket 05 is not production-cleared.
- Survival reconstructed directly from raw commit times was non-increasing and ended at the unresolved fraction. The independent three-trial fixture produced `1.0 -> 0.6666666666666667` from raw times `[None, None, 0.0]`.
- README, package/module docstrings, manifest non-claims, and CLI output consistently call the first clock a model stopping event and explicitly deny detector click, absorption, measurement outcome, unique actuality, microscopic-bath derivation, two-channel outcome, and Born-rule meaning. The killed-diffusion text uses “absorption” only for its mathematical absorbing boundary, not for the first clock.

## Environment and commands

Environment recorded on 2026-08-28 in `America/Denver`:

| Item | Value |
| --- | --- |
| Repository | `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework` |
| Python | CPython 3.12.6, `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3` |
| NumPy | 2.3.5 |
| Platform | macOS 26.5.2, arm64 |
| Worktree | Dirty with pre-existing unrelated tracked and untracked user files; package currently untracked. No implementation file was edited, staged, reverted, or committed. |

Core reviewed source digests:

| File | SHA-256 |
| --- | --- |
| `raw_race.py` | `1f03be378cef6fcb0e678aac01232bb7ff1b1a5dbf498b50841d7b0e44189c63` |
| `raw_ledger.py` | `ce50cfc51ad41515f9a317c9f29af27656e6ad0f4f293512d78ca84595a39b82` |
| `raw_runner.py` | `c394c74fae04ee92834167d3b7a756b5eb10991050c77394bdcc313c20e2034e` |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` |
| `stochastic.py` | `fdf5420ebe38b1c85f27a121efe626f690b30bd00bfd09f511feef01563cbac2` |
| `verify.py` | `8cc3aa8ebef3e567886b26f762c09bb6b4f047b7213bbdce8c26b964feb111f2` |
| `README.md` | `ecdb2bcfe9e7215e77a239bfa45c5b42319c606b62dbb2f8c1e7f53588eecbfa` |
| `__init__.py` | `b5ef6809a649780918a3f1cf8a63bf8d1026f2840dc9f38ead30d706b0e47399` |

Commands and outcomes:

```text
python3 -m adler_born_two_channel.verify
  exit 0; 95/95 passed; whole-suite peak 634.4 MiB

python3 -m adler_born_two_channel.verify --verbose
  exit 0; 95/95 passed; whole-suite peak 618 MB; largest declared array 19.2 MB

python3 adler_born_two_channel/verify.py
  exit 0; 95/95 passed

python3 -W error -m adler_born_two_channel.verify
  exit 0; 95/95 passed with warnings promoted to errors

python3 -m adler_born_two_channel.verify --prove-failure-exit
  exit 1; deliberate probe failed; 95/96 passed

python3 -m py_compile adler_born_two_channel/*.py
  exit 0

fresh-interpreter raw import probe
  exit 0; ten expected raw package modules loaded; forbidden_loaded=[]

independent recomputed-marker ledger mutations
  three contradictory edits accepted (category, detunings, aggregates)

independent right-truncation probe
  one path accepted from a declared two-clock grid

independent byte/reconstruction probe
  all five files byte-identical across live-block extremes; survival non-increasing

independent warmed tracemalloc probe
  48,329 B short; 46,312 B at 4x steps; 49,816 B at 4x trials
```

Every run fixture created by this review was removed. Six verifier-created temporary directories were removed by exact path after the command-path runs. Older pre-existing verifier directories were not touched.

## Closure conditions

Ticket 05 becomes **CLOSED** only when:

1. the durable schema retains the specified per-trial/per-clock diagnostics, including winner last-reset time;
2. the closed-ledger gate rejects the three independently demonstrated semantic forgeries and reconciles identities/aggregates by clock and trial;
3. the public race/outcome binds and validates the complete declared population and exact grid, including right-end truncation;
4. the supported writer and verifier obey the package-scoped output and cleanup contract; and
5. the canonical and focused regression probes pass after the schema/API/count/documentation updates.

Ticket 04's `numerical_no_result` and `diagnostic_only` status remain unchanged. Closing these software boundaries would not production-clear the experiment.

## Fix-up round 1 closure re-review — 2026-08-28

## Strict verdict: OPEN

Fix-up round 1 closes the durable-row omission, the three original forgeries, and the declared-population defect. It does **not** close semantic authority or result-directory scoping. With every table digest and every close-marker field recomputed, the v3 reader still accepts event times outside a clock's exposure, fabricated no-stop exposure, and a no-stop row that contradicts the same observed prefix. Separately, the public reader follows a result-directory symbolic link out of the package and accepts the external run.

These are public-boundary correctness defects. Both are direct closure requirements in the governing ticket and this re-review request.

## Findings, in priority order

### P1 — The v3 semantic gate still accepts impossible authoritative clock and shadow histories

The three original review forgeries now refuse. The nearby variants below do not. Each mutation was made against a valid 12-trial, 16-clock v3 run; the changed table was canonically re-encoded; its row count and digest, all other table digests, and the close marker were recomputed; and `require_closed_ledger` returned a `ClosedLedger`.

| Recomputed-marker mutation | Exact baseline and edit | Result |
| --- | --- | --- |
| Fabricated no-stop exposure | shadow trial 0, clock 0 was uncommitted with `exposure_time=4.0`, `eligible_time=0.0`; exposure changed to `2.0` | **ACCEPTED** |
| Event after censoring | censored trial 0 stopped at `-0.5`; loser clock 4 had exposure `1.5` and first eligibility `-0.5999999999999999`; `first_eligible_at` changed to the manifest close `2.0` | **ACCEPTED** |
| Broken same-key shadow prefix | trial 0, clock 8 had observed and no-stop `first_eligible_at=-1.5`; shadow value changed to `-1.0` | **ACCEPTED** |
| Impossible event order | shadow trial 0, clock 4 had first eligibility and first band entry both at `-0.5999999999999999`; `first_inside_at` changed to `-0.6999999999999998`, before eligibility | **ACCEPTED** |

The implementation explains all four acceptances:

- `_require_possible_clock_row` bounds event times only against the whole manifest window and exposure only against the whole window (`raw_ledger.py:1560-1576`). It does not bound an event by that row's own observation end or enforce `first_eligible_at <= first_inside_at <= committed_at` and reset-time ordering.
- Censored exposure is derived per row (`raw_ledger.py:1469-1481`), but shadow exposure is never derived from `committed_at` or `window_close`.
- The declared shadow-prefix gate compares six counts, opportunity, a commitment already seen under the stop, and detuning (`raw_ledger.py:1483-1510`). It does not compare first eligibility, first band entry, reset-time ordering, exposure, or any other time-prefix invariant.

This defeats the stated purpose of the v3 authoritative rows: a consumer can accept a closed run whose durable opportunity history could not have occurred in the observation interval and whose no-stop row is not the same physical path. It also means the assertion in the fix-up notes that there is “no unbound summary anywhere” is too broad. The aggregate returned by `ClosedLedger.clock_totals()` is correctly derived, but shadow exposure and several event-time relationships remain unbound.

**Required fix:** derive every censored row's observation end from its own commitment or the channel stop, and every shadow row's end from its own commitment or the manifest close; require exact exposure from that end; bound every event timestamp by that end; enforce causal time ordering; and enforce the time-bearing shadow-prefix relationships that the retained schema can establish. At minimum, first eligibility and first band entry already present in the censored prefix must be identical in the same-key shadow row; reset times must be ordered consistently with reset counts. Add all four recomputed-marker mutations above as must-refuse regressions, with positive controls.

### P1 — `open_raw_run` follows a symbolic link outside the package results root

Independent public-boundary reproduction:

```text
reader_symlink_escape ACCEPTED 12 12 /private/var/folders/.../T/t05-reader-link-8u9u4s2k/closed-run
inside_removed True outside_removed True
```

I wrote a valid named run under the package results root, moved that exact closed directory to a temporary external directory, placed a symbolic link at the original `results/<run-name>`, and called `open_raw_run(<run-name>)`. The reader accepted all 12 rows from the external target.

The writer calls `_require_inside_results(root)` before writing (`raw_runner.py:883-896`). The reader obtains the lexical path from `raw_results_directory`, then checks and reads files through it without ever calling `_require_inside_results` (`raw_runner.py:957-970`). Criterion 93 exercises the resolved-link helper directly, but not the public reader through such a link, so the 99-check suite misses this path.

**Required fix:** have `open_raw_run` resolve and validate its target with `_require_inside_results` before any existence check or read, use that validated target for the read, and add a public-reader symlink-escape regression containing an otherwise valid closed run. Keep the existing run-name, traversal, absolute-name, and writer-link refusals.

### P3 — One live schema declaration still labels v3 as version 2

`raw_ledger.py:214` says `The complete version-2 manifest schema` immediately above the live 45-field v3 `MANIFEST_FIELDS`. Runtime constants, marker parsing, README counts, and the fix-up notes correctly say v3, so this is documentation drift rather than a format defect. The stale-schema prose check does not inspect this source.

**Required fix:** change that live declaration to version 3 and extend the stale-schema prose check to the schema module or otherwise cover this exact declaration.

## Original finding closure matrix

| Original item | Re-review result | Evidence |
| --- | --- | --- |
| Durable per-`(trial, clock)` diagnostics and winner last reset | **CLOSED** | 192 rows for 12×16, exactly 19 clock fields; shadow has the corresponding 17 fields; all rows matched their in-memory `ClockExposure`; winner reset was present in 2 cases and `-` represented missing reset in 10. `ClosedLedger.clock_totals()` derives aggregates. |
| Original category, detuning, exposure/eligibility forgeries | **CLOSED as written; broader semantic authority OPEN** | Direct `check_ledger_semantic_forgeries()` passed: all three original recomputed-marker edits plus false eligible-count and outside-window stop variants refused. The four nearby accepted mutations above remain. |
| Declared population boundary | **CLOSED** | Independent three-clock probes refused right, front, and middle omission; reorder; duplicate; detuning substitution; drive digest mismatch; declared-model mismatch; mixed-model paths; bare tuple race; and right-truncated `ChannelOutcome`. Full three-clock and one-clock controls ran. |
| Package-scoped writer/verifier cleanup | **PARTIAL** | Writer name, traversal, absolute/path-object, overwrite, and resolved-link rules pass; verifier cleanup passes all command paths and the results root is empty afterwards. Public reader link escape remains open. |
| “Nine” versus “Ten” note | **CLOSED** | The notes now correctly state ten criteria for inclusive range 80–89, 85→95 checks, then four more criteria and 99 checks. |

## Reconfirmed passing behavior

### Race, replay, categories, shadow, and opportunity

- The canonical race checks passed for the independently reduced earliest per-clock completion, exact same-endpoint co-completers, retained mismatch/phase diagnostics, and absence of any internal random winner. Source inspection confirms pass one retains only the earliest time and pass two replays each `(dataset, trial, clock)` stream, stopping before the first clock-specific endpoint past the shared stop; no history cube is retained.
- The suite's hand-built category populations accept exactly one of `committed`, `never_eligible`, `lock_failed`, and `dwell_failed` and refuse the other three. Trial rows, clock wins, ties, unresolved rows, no-clock refusal, one-clock success, first/final endpoint cases, unequal crossing schedules, and co-completers all passed. The zero-coupling two-trial control remained two `never_eligible` trials.
- Empty `winner_last_reset` lists serialize as an empty CSV cell and parse as `()`; a winner with no reset serializes as `-` and parses as `(None,)`. v1 and v2 close markers both refused with `schema_version must be 3`.
- The no-stop sample remains predeclared as the first `shadow_trials` identifiers, uses the same physical keys, and is absent from channel tallies. In an independent 12-trial run, the first four shadow trials retained 4 race commitments but contained 21 no-stop clock commitments, exposing censoring. The on-disk reader's incomplete prefix enforcement is the P1 finding above.
- Survival reconstructed directly from commit times was non-increasing. The independent run produced nine descending levels from `0.8333333333333334` to `0.0`, equal to its unresolved fraction at the terminal event.

### Keying, reproducibility, isolation, and memory

- Initial-phase keys were exactly `dk-phase-noise/v3/physical/<dataset>/ensemble/trial=<t>/clock=<c>/phase`. Phases were byte-identical across simultaneous timestep and diffusion changes and under subset/reordered requests, while dataset and trial changes separated them; four clock keys gave four distinct samples.
- Three writes at `(clock_block, step_window)=(1,1),(16,4096),(3,7)` were byte-identical for all five files: manifest 5,533 bytes, trial ledger 1,662, clocks 19,153, shadow 6,530, marker 548. All three fixtures were removed.
- Fresh isolated import loaded only `commitment`, `dynamics`, `model`, `raw_config`, `raw_experiments`, `raw_ledger`, `raw_race`, `raw_runner`, `stochastic`, and `validation`; `forbidden_loaded=[]`. Adding `raw_race`, `pathlib`, and `platform` did not load analytic, killed-diffusion, moving-band audit, statistics/comparator/reporting code, or a package dynamic-import route.
- Warmed race-only `tracemalloc` peaks were 45,514 bytes for 1×8×20, 42,461 bytes after quadrupling steps to 80, and 45,555 bytes after quadrupling trials. Live-block extremes `(1,1)` and `(8,80)` measured 38,779 and 43,267 bytes. This discriminates against a trials×clocks×steps cube and confirms the two-pass implementation scales with live work rather than run totals.

### Schema, numerical status, claims, and cleanup

- Runtime schema is v3/v3 with 45 manifest fields, 17 trial columns, 19 authoritative clock columns, and 17 shadow columns. Exact CSV header/order/type/canonical-spelling, unique identities, three-way counts, hashes, manifest/table relationships, close-marker-last protocol, malformed/edit/truncate/extend/reorder/duplicate/wrong-version refusal, overwrite refusal, incomplete-run refusal, and derived aggregate checks all passed the canonical mutation suite.
- Every manifest inspected recorded `endpoint_status = passed at the declared reference tolerances`, `moving_band_status = numerical_no_result pooled and in fourteen of fifteen per-regime cells at the frozen reference sample`, and `numerical_gate = diagnostic_only`. Ticket 05 remains non-production regardless of software closure.
- README, CLI, package docstring, and manifest non-claims continue to call the first clock a model stopping event and expressly deny detector click, absorption, measurement outcome, unique actuality, microscopic bath, two-channel outcome, and Born-rule meaning.
- The package results root was empty after canonical, verbose, direct, warnings-as-errors, compile, and deliberate-failure paths. Sixteen legacy `adler-raw-verify-*` directories already existed in the platform temporary directory with modification times 08:24–08:56, before this re-review's 09:52 command start; the current verifier created no new external fixture. All independent package and temporary fixtures from this re-review were removed, including exception paths.

## Environment, source scope, and commands

Environment on 2026-08-28 in `America/Denver`: CPython 3.12.6 at `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3`, NumPy 2.3.5, macOS 26.5.2 arm64. The worktree was already dirty with unrelated tracked and untracked user files; the package is untracked. I edited no implementation, staged nothing, reverted nothing, and committed nothing. The only write made by this review is this appended artifact section.

| Reviewed source | SHA-256 |
| --- | --- |
| `raw_race.py` | `44e83995c12b6d08d766efcc39ed6a1ee2b64c3fdc7dbb43c665808bcd7f6432` |
| `raw_ledger.py` | `c86fe2e016f073eb1d997f8119ce9626ae23de195a19e49b227d848f6d197827` |
| `raw_runner.py` | `334e1173528ca8de2602baa265bf28dfebc3e0450d7c366bbe3f6874462667a3` |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` |
| `stochastic.py` | `fdf5420ebe38b1c85f27a121efe626f690b30bd00bfd09f511feef01563cbac2` |
| `verify.py` | `6c4b18b880f1152094dfe5b7f0327596ea9d415f4a1bbf2ea69bce64d2cd03ef` |
| `README.md` | `4b9e1960c1d424c1e8e281f65d3eb525b4a32c1951e9f12d4b7a9faf5ed66406` |
| `__init__.py` | `03d8c72dd8072830a4ee5b483a07cd3db9a294d7075bcd456b92aceba15f646e` |

Command paths:

```text
python3 -m adler_born_two_channel.verify
  exit 0; 99/99 passed

python3 -m adler_born_two_channel.verify --verbose
  exit 0; 99/99 passed; peak resident set 633 MB; largest declared array 19.2 MB

python3 adler_born_two_channel/verify.py
  exit 0; 99/99 passed

python3 -W error -m adler_born_two_channel.verify
  exit 0; 99/99 passed with warnings promoted to errors

python3 -m py_compile adler_born_two_channel/*.py
  exit 0

python3 -m adler_born_two_channel.verify --prove-failure-exit
  exit 1 as required; deliberate probe failed; 99/100 passed

direct focused closure checks
  authoritative rows PASS; the three original semantic forgeries PASS;
  population binding PASS

independent recomputed-marker variants
  four impossible clock/shadow histories ACCEPTED

independent public-reader resolved-link escape
  external valid closed run ACCEPTED

independent key, byte, survival, isolation, and warmed-memory probes
  PASS, with exact measurements recorded above
```

## Closure conditions after round 1

Ticket 05 remains **OPEN** until:

1. v3 derives shadow exposure, bounds all event times by each row's actual observation end, enforces event ordering, and verifies the retained time-bearing shadow-prefix relationships;
2. the four accepted recomputed-marker variants above become must-refuse regressions with valid controls;
3. `open_raw_run` refuses a valid externally located run reached through a package-results symbolic link; and
4. the canonical command paths pass again after those changes, with the package results root clean.

The durable schema, declared population, original three forgeries, writer scoping, cleanup, Ten-note correction, race kernel, replay, keying, reproducibility, isolation, memory, survival, numerical status, and non-claims do not need redesign. They need to remain passing while these two public-boundary defects are closed.

## Fix-up round 2 closure re-review — 2026-08-28

## Strict verdict: OPEN

Round 2 closes the four exact temporal forgeries from round 1, the pre-existing external-directory-link reader path, and the stale live schema prose. It does **not** close semantic authority for opportunity/prefix relationships, and it does not make filesystem scoping stable across validation and use. Recomputed-marker ledgers with impossible same-key histories still open. The public reader and writer can both be redirected to external files, including without a timing race.

These are governing-ticket closure requirements, so the otherwise clean 100-check suite cannot close Ticket 05.

## Findings, in priority order

### P1 — v3 still accepts impossible opportunity and same-key shadow-prefix histories

The four exact round-1 mutations now refuse after every row count, digest, aggregate and marker field is recomputed:

| Exact reproduction | Result |
| --- | --- |
| shadow trial 0 clock 0 exposure changed from its derived `4.0` to `2.0` | **REFUSED** |
| censored trial 0 clock 4 first eligibility moved to `2.0`, after its `-0.5` channel stop | **REFUSED** |
| shadow trial 0 clock 0 first eligibility moved from the already observed `-0.5999999999999999` to `-1.0` | **REFUSED** |
| shadow first band entry moved to `-1.999999999`, before its `-0.5999999999999999` first eligibility | **REFUSED** |

The untouched 12-trial, 192-clock, 64-shadow-row fixture opened, and the built-in positive census contained 104 never-eligible rows, 55 eligible-but-never-inside rows, 21 inside-with-no-reset rows, 10 reset-without-commitment rows, 12 committed rows, 3 tied trials, 8 shadow first events hidden by censoring, 20 shadow-only later-event rows, and 4 equal-observation-end shadow rows identical field for field. Thus the refusals discriminate valid categories, ties, unresolved paths, winner/no-reset spelling, shorter prefixes, and exact endpoint equality.

Nearby recomputed-marker variants still opened:

| Accepted contradiction | Exact evidence |
| --- | --- |
| An already observed winner moves in its same-key continuation | trial 0 clock 5 committed at `-0.5` in both tables; changing only the shadow commitment to `-0.4` and deriving its exposure accordingly was **ACCEPTED** |
| Positive opportunity with no eligible endpoint | trial 4 clock 0 had `eligible_endpoints=0`, `eligible_time=0.0`; changing time to `0.1` and the authoritative trial total to `1.352574462907429` was **ACCEPTED** |
| Eligible endpoints with zero opportunity | trial 4 clock 6 had 2 eligible endpoints and `eligible_time=0.14471458707824625`; changing the time to `0.0` and recomputing the trial total was **ACCEPTED** |
| A genuinely longer prefix gains no endpoint | trial 0 clock 0 ended at `-0.5` with 15 endpoints; its shadow ended at `2.0` with 40. Changing the shadow count to 15 was **ACCEPTED** |
| Equal eligible count but changed opportunity | trial 0 clock 0 had zero eligible endpoints and zero eligible time in both rows; changing only shadow eligible time to `0.01` was **ACCEPTED** |
| Extra eligible endpoints add no opportunity | trial 0 clock 3 had 0 eligible endpoints/time in the censored row and 7 endpoints/`0.6217224930206653` in shadow; changing shadow time to `0.0` was **ACCEPTED** |

The source matches the reproductions. `_require_shadow_prefix` treats unequal derived ends as the shorter-prefix branch, but its commitment rule only constrains a free commitment when the censored row has none (`raw_ledger.py:1596-1602`). It therefore loses the previously enforced invariant that a commitment already observed under the stop must recur at the identical time without the stop. Prefix counts and times are only independently monotone (`raw_ledger.py:1552-1563`), so the gate does not bind added endpoints to added positive-duration observation/opportunity. Row-local validation only checks `eligible_time <= exposure_time` (`raw_ledger.py:1680-1683`), not the reachable equivalence between zero eligible endpoints and zero eligible time.

**Required fix:**

1. If the censored row has `committed_at`, require the same shadow commitment regardless of whether the forged shadow value changes the derived end.
2. Enforce row-local `(eligible_endpoints == 0) == (eligible_time == 0.0)` for this strictly positive-duration mesh.
3. For a shorter censored prefix, require a strictly later shadow end to add at least one endpoint. Equal eligible endpoint counts require equal eligible time; additional eligible endpoints require additional positive eligible time.
4. Add all six accepted variants above as recomputed-marker must-refuse regressions, alongside valid controls for all four categories, ties, winner-without-reset, first/final endpoints, empty time lists, and binary64-equal observation ends.

### P1 — path validation is not an I/O capability; reader and writer still escape the results root

The ordinary controls and the round-1 reproduction now behave correctly: an ordinary in-root run opens; traversal, absolute, nested, missing and incomplete names refuse; and a symlink already present at `results/<run>` and pointing to a valid external run refuses.

Validation is still separated from use, however. Four independent reproductions succeeded:

| Scope reproduction | Result |
| --- | --- |
| Reader run directory replaced after `_require_inside_results` returned | **ACCEPTED** the replacement external run: 3 trial rows rather than the validated in-root control's 2 |
| Writer run directory replaced after `_require_inside_results` returned | **ACCEPTED** and created all five files externally: `CLOSED.json`, `clocks.csv`, `ledger.csv`, `manifest.json`, `shadow.csv` |
| Ordinary in-root directory whose five filenames are symlinks to external valid files | `open_raw_run` **ACCEPTED** all 12 external trial rows; every resolved file path was outside the package |
| Fresh in-root writer directory containing five broken symlinks to nonexistent external targets | `write_raw_run` **ACCEPTED** and created all five external targets |

The last two need no concurrent attacker. In the writer, `Path.exists()` ignores a broken final symlink, validation returns no pinned object, and later `write_bytes`/table opens follow the links (`raw_runner.py:883-901`). In the reader, resolving a directory to another `Path` does not pin its inode, and every existence check/read follows the final filename (`raw_runner.py:963-977` and following). The comment that a later replacement “cannot redirect” those reads is therefore false.

**Required fix:** treat validation and I/O as one operation. Open the results root and run directory once as no-follow directory descriptors, verify the opened identity is inside the package root, and perform every file operation relative to that pinned descriptor. Require regular non-link files; on write, create each file exclusively with no-follow semantics, retain marker-last ordering, and refuse pre-existing links including broken ones. Add directory-replacement and individual-file-link regressions for both public boundaries.

All scope fixtures were removed in `finally` paths. The direct file-link probe ended with an empty package results root and a nonexistent temporary external directory. The final isolated canonical run removed its own results directory completely.

## Round-2 closure matrix

| Requested item | Result | Evidence |
| --- | --- | --- |
| Four exact temporal forgeries | **CLOSED** | All refuse after fully recomputed table hashes, row counts, aggregates and marker. |
| Derived row ends/exposure and basic event ordering | **CLOSED as implemented** | Built-in criterion 94 and the exact probes pass; positive controls cover all required row shapes and equality branch. |
| Opportunity/count and full shadow-prefix authority | **OPEN** | Six nearby recomputed-marker contradictions above are accepted. |
| Pre-existing external run-directory link | **CLOSED** | Public reader refuses; ordinary in-root control opens. |
| Stable scoped I/O after validation | **OPEN** | Directory replacement and final-component file-link reproductions redirect both reader and writer externally. |
| Live schema prose and guard | **CLOSED** | `raw_ledger.py:214` now says version 3; `_stale_live_schema_prose()` and `_live_schema_pattern_fixtures()` both return `[]` over ten fixtures while legitimate schema history remains allowed. |
| Durable v3 rows and population identity | **RECONFIRMED** | v1/v2 refuse; exact field sets/counts and all right/front/middle/reorder/duplicate/substitution/drive/model/bare-tuple probes pass. |
| Race/replay/keying/invariance/shadow/survival/memory/isolation/status/docs/nonclaims | **RECONFIRMED** | Focused probes and the full matrix pass as detailed below. |

## Reconfirmed passing behavior

- Earliest endpoint-resolved dwell completion agrees with the independent all-clock walk for arbitrary clock order and crossing schedules. Same-step co-completers and mismatches remain explicit; no random internal winner exists. The four trial categories reconcile exhaustively and exclusively, including no-clock refusal, one-clock success, zero coupling, no commitment, first/final endpoint, unequal schedules and ties.
- Pass two regenerates the same prepared phases and Brownian leaves from `(dataset, trial, clock)` keys and stops at the shared endpoint. Initial-phase keys are `dk-phase-noise/v3/physical/<dataset>/ensemble/trial=<t>/clock=<c>/phase`: timestep and diffusion do not enter, while dataset/trial/clock do. No history cube is stored.
- Writes at `(clock_block, step_window)=(1,1),(16,4096),(3,7)` were byte-identical for all five files: manifest 5,533 bytes, trial ledger 1,662, clocks 19,153, shadow 6,530, marker 548. No timestamp, block size or incidental ordering leaked into bytes.
- The first `shadow_trials=4` trial identifiers are frozen before outcomes and recorded in the manifest. The same physical streams are used; the 64 shadow rows expose first-winner censoring and never enter channel category counts.
- Survival reconstructed from raw commit times is non-increasing: `[0.8333333333333334, 0.75, 0.5833333333333334, 0.5, 0.33333333333333337, 0.25, 0.16666666666666663, 0.08333333333333337, 0.0]`, with terminal survival equal to the unresolved fraction.
- Warmed race-only `tracemalloc` peaks were 44,573 bytes for 1 trial × 8 clocks × 20 steps, 41,703 after quadrupling steps, and 45,553 after quadrupling trials; live-block extremes were 38,609 and 43,173 bytes. This discriminates against trials × clocks × steps storage while acknowledging the two-pass compute cost.
- A fresh raw import loaded only the ten intended package modules and `forbidden_loaded=[]`; adding `raw_race`, `pathlib`, and `platform` did not load analytic, killed-diffusion, moving-band audit, statistics/comparator/reporting modules, or general dynamic-import routes.
- Schema v3/v3 has 45 manifest fields, 17 trial columns, 19 authoritative clock columns and 17 shadow columns. Exact parsing, identities, row/table/manifest counts, hashes, marker-last protocol, malformed/edit/truncate/extend/reorder/duplicate/wrong-version refusal and derived aggregates remain passing.
- Ticket 04 is still reported honestly: stationary endpoint validation passed, moving-band is `numerical_no_result` pooled and in fourteen of fifteen cells, and `numerical_gate=diagnostic_only`. Nothing production-clears Ticket 05.
- README and all live output retain 100 checks over acceptance criteria 1–94, include the prior 85 checks, and explicitly deny detector click, absorption, measurement outcome, unique actuality, microscopic bath, two-channel winner/outcome and Born-rule meaning.

## Environment, source scope, and commands

The interactive review environment was CPython 3.12.6 at `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3`, NumPy 2.3.5, macOS 26.5.2 arm64. Traycer's persistent `/bin/sh` command matrix resolved CPython 3.13.11 and NumPy 2.4.3; both environments are recorded because the PATHs differ. The worktree was already dirty with unrelated user changes and the package is untracked. No implementation file was edited, staged, reverted or committed. This appended section is the review's only durable edit.

| Reviewed source | SHA-256 |
| --- | --- |
| `raw_race.py` | `44e83995c12b6d08d766efcc39ed6a1ee2b64c3fdc7dbb43c665808bcd7f6432` |
| `raw_ledger.py` | `68968f4e3fd350b00680ea14d3dc5bf0e26fb421a952f47f6090578454eb75e0` |
| `raw_runner.py` | `039ce73642f05c372162183b31d2948ced48f627059a413586ab7dd28a7e10ec` |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` |
| `stochastic.py` | `fdf5420ebe38b1c85f27a121efe626f690b30bd00bfd09f511feef01563cbac2` |
| `verify.py` | `4e4d757c00f114c59354cb6933901318b99392340bfe99d6cf049c55f1d78469` |
| `README.md` | `b067561eab052742046e80ebc96ce7aa75e2fa583592f60471fbf0105bed7f2b` |
| `__init__.py` | `03d8c72dd8072830a4ee5b483a07cd3db9a294d7075bcd456b92aceba15f646e` |

Command matrix:

```text
python3 -m adler_born_two_channel.verify
  isolated final run: exit 0; 100/100 passed; 627.2 MB peak RSS; results directory absent afterward

python3 -m adler_born_two_channel.verify --verbose
  exit 0; 100/100 passed; 595.8 MB peak RSS; largest declared array 19.2 MB

python3 adler_born_two_channel/verify.py
  exit 0; 100/100 passed

python3 -W error -m adler_born_two_channel.verify
  exit 0; 100/100 passed with warnings promoted to errors

python3 -m py_compile adler_born_two_channel/*.py
  exit 0

python3 -m adler_born_two_channel.verify --prove-failure-exit
  exit 1 as required; deliberate probe failed; 100/101 passed

independent recomputed-marker temporal probes
  four exact round-1 variants REFUSED; six nearby contradictions ACCEPTED

independent scope probes
  ordinary/traversal/absolute/missing/incomplete/pre-existing-directory-link cases behaved as required;
  reader/writer directory replacement and individual-file-link escapes ACCEPTED

independent key, byte, survival, population, isolation and warmed-memory probes
  PASS with exact measurements above
```

One earlier canonical invocation overlapped a reviewer byte fixture and another overlapped a separate verifier fixture; each failed only the final empty-results-root check. After both processes ended and exact review fixtures were removed, the isolated canonical run above passed 100/100 and left no result. The interference is recorded rather than counted as a product defect.

## Closure conditions after round 2

Ticket 05 remains **OPEN** until:

1. the v3 gate rejects all six opportunity and same-key shadow-prefix contradictions above after full digest/marker recomputation;
2. the reader and writer pin validated directories and refuse both directory replacement and final-component file links, including broken links on write;
3. regressions exercise those exact public boundaries and retain the existing exact-forgery, schema, population, race, key, byte, memory, status and nonclaim coverage; and
4. the full command matrix passes again with no package or external fixture left behind.

The round-2 changes materially improve the ledger, but the remaining accepted records and external I/O paths prevent strict closure.

## Independent round-2 corroboration — 2026-08-28

## Strict verdict: OPEN

I independently reran the requested command matrix and the four exact round-2 temporal attacks. The exact attacks now refuse, ordinary in-root reading works, and the original run-directory link escape refuses. The round-2 snapshot still does not close because final-component file links redirect both supported public boundaries outside the results root.

### Blocking finding — validated directory names do not bind the files used by I/O

Against the round-2 snapshot (`raw_ledger.py` `68968f4e3fd350b00680ea14d3dc5bf0e26fb421a952f47f6090578454eb75e0`, `raw_runner.py` `039ce73642f05c372162183b31d2948ced48f627059a413586ab7dd28a7e10ec`, `verify.py` `4e4d757c00f114c59354cb6933901318b99392340bfe99d6cf049c55f1d78469`), I built an ordinary directory beneath `adler_born_two_channel/results` whose five named files were links to an otherwise valid external closed run. `open_raw_run` returned all 12 trial rows. In a fresh ordinary run directory, I placed five broken final-component links to external nonexistent targets; `write_raw_run` accepted them and created all five targets externally: `CLOSED.json`, `clocks.csv`, `ledger.csv`, `manifest.json`, and `shadow.csv`.

This independently confirms the public-scope blocker already recorded above. Validating the run directory and then using ordinary path-based final-file reads/writes does not establish that the actual files are regular files beneath that validated directory. The reader and writer must refuse linked final components and bind validation to the I/O operation itself.

Every focused fixture was removed in `finally`; the package results root and both external fixture directories were absent afterward.

### Exact round-2 requirements that passed

An independent 12-trial fixture opened with 12 trial rows, 192 authoritative clock rows, and 64 shadow rows. Re-derivation found zero exposure, event-bound, or causal-order violations. Six equal-observation histories were identical across every shared field, and 58 genuinely shorter censored histories satisfied the documented prefix relationships with zero prefix violations.

With every affected table re-encoded and every row count, digest, and close-marker field recomputed, all four exact prior attacks refused:

1. fabricated no-stop shadow exposure;
2. a censored loser's first eligibility moved after its own stop;
3. a same-key shadow first eligibility moved away from the already observed value; and
4. a shadow first-inside time moved before first eligibility.

The public reader also refused a valid closed run reached through a pre-existing run-directory link outside the results root, while the ordinary in-root control opened. Live schema declarations identify v3, and the historical version-1/version-2 migration text remains correctly historical.

### Command evidence

```text
python3 -m adler_born_two_channel.verify
  exit 0; 100/100 passed

python3 -m adler_born_two_channel.verify --verbose
  exit 0; 100/100 passed; peak resident set 608 MB; largest declared array 19.2 MB

python3 adler_born_two_channel/verify.py
  exit 0; 100/100 passed

python3 -W error -m adler_born_two_channel.verify
  exit 0; 100/100 passed with warnings promoted to errors

python3 -m py_compile adler_born_two_channel/*.py
  exit 0

python3 -m adler_born_two_channel.verify --prove-failure-exit
  isolated rerun: exit 1 as required; deliberate probe was the only failure; 100/101 passed
```

One earlier deliberate-failure invocation overlapped another process's verifier fixtures and transiently reported 98/101; the isolated rerun produced the required 100/101 and left no fixture. This is recorded as review-environment interference, not a product defect.

The full suite and source inspection reconfirmed authoritative rows and semantic reconciliation, complete population binding, earliest-completion and tie behavior, deterministic replay and byte invariance, predeclared shadow selection, non-increasing survival, bounded memory, raw-module isolation, Ticket 04's stationary-passed / moving-band-`numerical_no_result` / `diagnostic_only` status, and all scientific nonclaims.

### Snapshot note

The implementation began changing to round 3 while this corroboration was running: `raw_ledger.py` and `raw_runner.py` digests changed after the round-2 tests. This section is therefore a verdict on the requested round-2 snapshot and its independently reproduced public-file boundary, not a review of the in-progress round-3 implementation. No implementation file was edited, staged, reverted, or committed by this reviewer; this appended section is the only durable edit.

## Fix-up round 3 closure re-review — 2026-08-28

## Strict verdict: CLOSED

No blocking or non-blocking correctness finding remains. I independently reproduced both round-3 blocker classes against the public closed-ledger and run-I/O boundaries, inspected the current implementation, reran the complete command matrix, and reconfirmed the previously closed Ticket 05 requirements. The six recomputed-marker semantic attacks now refuse, all thirteen declared valid history shapes occur and accept, and neither a directory-entry replacement nor any linked final component can redirect one of the five package-scoped file operations.

### Same-key history and opportunity gate

I generated a fresh 16-clock, 16-shadow-trial run and independently derived each observation interval from the writer's actual endpoint convention: an endpoint is recorded only for a positive-width elementary interval; a zero-duration coordinate handoff is not an endpoint. Across 256 authoritative clock rows there were zero derived-end, exposure, event-presence, event-order, or count-bound errors. Four equal-observation censored/shadow pairs were field-identical, and all 60 genuinely shorter observations were valid prefixes of their no-stop histories, with zero prefix errors.

The positive census contained every declared shape:

```text
never_eligible                              104
eligible_never_inside                        55
inside_no_reset                              21
reset_no_commitment                          10
committed                                    12
tied                                          3
shadow_first_event_after_stop                 8
shadow_only_later_events                     20
longer_only_ineligible_endpoints             24
longer_eligible_endpoints_and_opportunity    36
later_first_eligibility                       8
later_reset                                   7
later_commitment                             17
```

For each negative probe I decoded the rows, changed the durable history, canonically re-encoded every affected table, recomputed all table row counts and SHA-256 digests, rebuilt the close metadata, and invoked `require_closed_ledger`. All six refused:

```text
moved_observed_commitment                         REFUSED
zero_eligible_endpoints_positive_opportunity      REFUSED
positive_eligible_endpoints_zero_opportunity      REFUSED
longer_observation_without_endpoint_growth        REFUSED
unchanged_eligible_count_changed_opportunity      REFUSED
increased_eligible_count_no_added_opportunity     REFUSED
```

Source inspection agrees with the behavior. `_require_shadow_prefix` compares an already observed commitment before observation-end branching, enforces the row-local zero-endpoint/zero-opportunity equivalence, requires endpoint growth for a longer observation, and makes eligible endpoint count and eligible time jointly monotone. This closes the exact route by which a derived moved commitment previously changed the derived observation end and escaped the equal-end check.

### Pinned package-scoped file operations

The public ordinary control wrote and reopened a completed three-trial run with exactly `manifest.json`, `ledger.csv`, `clocks.csv`, `shadow.csv`, and `CLOSED.json`. Focused adversarial results were:

```text
linked run entry: reader REFUSED; writer REFUSED
linked final component: reader REFUSED for all five files
broken linked final component: writer REFUSED for all five files;
  no external target or target directory created
pre-existing regular component: writer REFUSED for all five files;
  every sentinel remained unchanged
incomplete run without close marker: reader REFUSED
run entry renamed and replaced after its handle opened:
  all five reads returned the original run bytes
```

Inspection confirms that `results/` and the run directory are opened as directory descriptors with `O_NOFOLLOW | O_DIRECTORY`. Every read is relative to the pinned run descriptor with `O_RDONLY | O_NOFOLLOW` and a regular-file `fstat`; every write uses `O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW`; the marker remains last and uses the same pinned handle. `_require_scoped_io` fails closed if the platform lacks the required flags or `dir_fd` support. Thus the designated package results folder is a capability boundary used by the operation itself, not a path checked before a later reopen.

Only `raw_runner.py` imports `os`. Its observed `os` attributes are the local primitives `O_CREAT`, `O_EXCL`, `O_RDONLY`, `O_WRONLY`, `close`, `fdopen`, `fstat`, `mkdir`, `open`, and `supports_dir_fd`; the raw-graph scan additionally bans the process-spawning family. The verbose fresh-runtime isolation check passed: 11 reachable raw-graph modules, none of 51 banned names, and no forbidden prediction/audit module loaded through the raw boundary.

Every focused history, results, and external fixture was removed in `finally`. A final filesystem scan found no package result entry and no external review fixture.

### Regression and byte evidence

The documented reference configuration was independently replayed under CPython 3.13.11 / NumPy 2.4.3, matching the runtime recorded in its manifest. It reproduced 64 ledger rows, 1,024 clock rows, 128 shadow rows, and categories `committed=58`, `dwell_failed=6`, `lock_failed=0`, `never_eligible=0`. The payload bytes retained their documented SHA-256 values:

```text
manifest  fa2ac5172029c77a127d780499775f23fc732617d3bd75ab1693db32cd5c3248
ledger    2fcc8daf8ea3f9912312e06d8d478a1ced85eab0f46732cd26a05b61d8bc4f29
clocks    1c55d17bd000800266c44b6608c1c5c6b681b313ece09ced0d889767f03ab994
shadow    7a9de2b1a7377d8092a6dc56b2c3049c94013ac12be537683142ed3ef60fad2c
```

The five-file invariance check, including `CLOSED.json`, passed across `(clock_block, step_window)` variations. Deterministic keyed replay, authoritative `(trial, clock)` population, trial/table semantic reconciliation, earliest completion, retained same-endpoint ties, predeclared shadow selection, non-increasing survival, and byte invariance all remain covered and passing.

The live schema declarations consistently identify v3. The stale-prose guard passes all 28 fixtures across three sources while preserving the valid historical schema-1/schema-2 migration discussion. The README check finds all 24 required statements and both verification commands. The exported API contract check covers 259 public callables and all 606 parameters with 816 correctly refused invalid calls. Ledger declarations remain 45 manifest fields plus 53 table columns (`17 + 19 + 17`).

Ticket 04 remains unchanged: the stationary endpoint gate is `passed`, the moving-band audit is `numerical_no_result`, and written runs are `diagnostic_only`, not production-cleared. The package, CLI, README, and manifest retain the scientific nonclaims: a first clock is a model stopping event, not a detector click, absorption, measurement outcome, unique actuality, microscopic-bath derivation, two-channel outcome, or Born-rule result; no survival law, hazard, exponent, or scaling claim is made.

### Exact command evidence

```text
python3 -m adler_born_two_channel.verify
  exit 0; 101/101 passed; bounded-memory residual 652.8 MiB (limit 900 MiB)

python3 -m adler_born_two_channel.verify --verbose
  exit 0; 101/101 passed; peak resident set 649 MB;
  largest declared array 19.2 MB; declared bound 944 MB

python3 adler_born_two_channel/verify.py
  exit 0; 101/101 passed; bounded-memory residual 660 MiB

python3 -W error -m adler_born_two_channel.verify
  exit 0; 101/101 passed; bounded-memory residual 603.5 MiB

python3 -m adler_born_two_channel.verify --prove-failure-exit
  exit 1 as required; deliberate probe was the only failure; 101/102 passed

python3 -m py_compile adler_born_two_channel/*.py
  exit 0
```

Final reviewed-source SHA-256 values were stable before and after the review:

| File | SHA-256 |
| --- | --- |
| `raw_race.py` | `44e83995c12b6d08d766efcc39ed6a1ee2b64c3fdc7dbb43c665808bcd7f6432` |
| `raw_ledger.py` | `9cacde49672d9307bbbb436e1b5235364a154dd37f7f993e1974061d183a5221` |
| `raw_runner.py` | `b9ad310b4cb827e341ec2bfcd913b6e9cf4732216e731077964c527e94eaa6e0` |
| `raw_config.py` | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` |
| `stochastic.py` | `fdf5420ebe38b1c85f27a121efe626f690b30bd00bfd09f511feef01563cbac2` |
| `verify.py` | `379bc73cb29d686f1e351351130c27f9b1d23dbf4862d797933696be44aeeabc` |
| `README.md` | `a2506b32cc62c43c7a1defae725be31eabae1b677b52a5999d7638a56f945956` |
| `__init__.py` | `03d8c72dd8072830a4ee5b483a07cd3db9a294d7075bcd456b92aceba15f646e` |

No implementation file was edited, staged, reverted, or committed by this reviewer. The package remains a pre-existing untracked directory in this worktree; this appended review section is the only durable change.
