---
title: "Ticket 05 execution decisions"
kind: spec
---

# Ticket 05 execution decisions

Decisions taken while implementing the finite one-channel race and the immutable ledger, and the limitations they leave behind. Written for the independent reviewer.

## Scalar reuse rather than a vectorised ensemble stepper

The race walks clocks **one at a time** through the existing scalar `dynamics.ClockPath` and `commitment` kernels, rather than introducing a vectorised ensemble stepper.

Ticket 03's checks certify the scalar path — the exact tongue handoffs, the lift identity, the contraction guard, the timestamp dwell rule — over sixty-odd invariants. A vectorised reimplementation would be a second data-generating process that those checks do not cover, and its agreement with the first would have to become a new gate. The clocks are independent, so nothing is lost physically.

The cost is speed: roughly 6–10 μs per clock-step depending on how much of each walk the stop truncates. A 64-trial, 16-clock, 80-step diagnostic run takes 26–33 s. Ticket 07 owns the production throughput budget and may revisit this; if it does, the scalar path is the reference the vectorised one must reproduce, not the thing it replaces.

## Two passes, and why one is not possible

The channel stop is not known until every clock has been asked, and the per-clock diagnostics must be censored *at* the stop. A single pass would have to retain every clock's time-resolved history in order to truncate it afterwards — the trial-by-clock-by-time cube the plan forbids.

So: pass one (`first_completion`) keeps one number per clock and discards everything else; pass two (`censored_exposure`) re-walks stopping at the channel stop and keeps the diagnostics. Because a leaf belongs to its key and not to the walk that reached it, pass two re-derives bit-for-bit what pass one saw. Up to 2× the clock-steps, and the doubling is the price of censoring honestly rather than a defect.

Pass one truncates each clock at the best time found so far. That is an optimisation and is verified to be nothing more: the stop and the whole winner list are compared, trial by trial, against a no-stop walk of every clock reduced by an independently transcribed minimum rule.

## Initial phases are keyed *without* the mesh

`PhaseNoiseStream` gained `ensemble_prefix`, `initial_phase_key` and `initial_phases`. The key is `<schema>/<namespace>/ensemble/trial=<t>/clock=<c>/phase` — dataset, trial and clock, and nothing else.

The mesh is deliberately absent. The plan requires a refinement ladder to "reuse the same initial phases and physical clock grid"; keying the prepared ensemble to the mesh would hand the same clock a different starting phase at a halved timestep, and the paired comparison would then be measuring two ensembles as well as two timesteps. Diffusion strength is absent for the same reason: a noise sweep is paired.

Disjointness from kick addresses is structural rather than asserted — a leaf key contains `mesh=<hex>:<hex>` where an ensemble key contains the literal segment `ensemble`, and no mesh identity begins with that word.

## Execution parameters are not in the manifest

`clock_block` and `step_window` are arguments to `write_raw_run`, not fields of `RawEventConfig` and not keys of the manifest.

They bound the live working set and cannot change a recorded number. Freezing them into the immutable description of a run would imply that they were part of it — and would make "the same configuration writes byte-identical files" untestable, because the manifest digest would differ between two runs whose three tables were identical. They are reported on `RawRunReport`, which is not part of the record. There is no timestamp in the manifest for the same reason.

## `shadow_trials` is a configuration field

The no-stop shadow sample's size is frozen at the input boundary, with `1 <= shadow_trials <= trials`, and written into the manifest before the run starts. "Predeclared" is the entire content of the requirement: choosing the size after seeing which mismatches looked quiet would make it useless for separating a mismatch that never commits from one that never got the chance.

The minimum is one rather than zero. A run with no shadow sample would report per-clock counts with no way to distinguish censoring from absence, and would look exactly like a run that had checked.

The selection is a **rule** — the first `shadow_trials` trial identifiers — recorded in the manifest as `shadow_rule`, for the same reason the clock grid is a rule rather than a vector of detunings: a list could have been chosen from the answer.

## Compatibility decisions

| Ticket 01 shape | Ticket 05 shape | Why |
| --- | --- | --- |
| `LEDGER_SCHEMA_VERSION = 1`, `MANIFEST_SCHEMA_VERSION = 1` | both `2`; version 1 refused, not partially read | The rows exist, so the schemas that anticipated them change |
| `RawManifest(schema_version, run_label, trials)` | `RawManifest(fields)`, a mapping validated against a 44-field declared schema | A manifest that cannot state the grid, pulse, noise, mesh, namespaces or numerical status cannot support the comparison it exists for. One constructor argument rather than forty-four positional ones |
| `CloseMarker(schema_version, row_count, content_digest, manifest_digest)` | `CloseMarker(schema_version, tables, manifest_digest)` with one `(name, rows, digest)` triple per table | A run whose trial ledger closed and whose shadow sample did not is not a closed run |
| `require_closed_ledger(payload, marker, manifest)` | `require_closed_ledger(marker, manifest, ledger, clocks, shadow)` → `ClosedLedger` | Three tables; and the gate returns parsed rows rather than bytes, so a caller cannot reparse with a looser parser than the one that was checked |
| The trial count checked marker-against-manifest | Checked manifest-against-marker-against-**rows present**, plus row **identities** and row **content** | Ticket 01's own docstring asked for exactly this once a parser existed |

Nothing had been recorded under version 1, so no migration exists and none is needed.

The raw-module import allowlist gained `pathlib` and `platform` — the first because a run creates its own directory and writes five files, the second because the manifest records the interpreter version and "identical ledgers" is a claim about a *recorded* environment. `sys` remains excluded: `sys.modules` is a route to any module at all, and the version string is available without it.

## Row-level authority

`require_closed_ledger` establishes eight things, and the eighth was added after a mutation survived the first seven. Changing one word of one cell — `dwell_failed` to `committed` — leaves every digest valid (a forger recomputes them), every column name unchanged, and every count correct, while turning an unresolved trial into a commitment.

`_require_consistent_rows` restates the identities the writer already enforced at the objects that produced the rows, over the parsed table: category and commit time agree, a committed trial stops at its own commitment, the winner list is distinct and in clock order and as long as `co_completion`, every per-winner column has the same length as the winner list, opportunity never exceeds exposure, resets never exceed entries, and the trial ledger's retained co-completers equal the per-clock ledger's wins.

That last one is the only genuinely *cross-table* rule and it is the one that makes the two files two views of one race rather than two files.

## Known limitations

1. **A population truncated from the right end is invisible to `ChannelOutcome` alone.** **Closed in fix-up round 1.** The race takes a `ClockPopulation` carrying a declared size, clock order and mismatch list from the frozen grid rule, and `ChannelOutcome` retains and validates that identity instead of inferring completeness from `range(len(clocks))`. Right-end truncation now refuses at the population door and again at the outcome.
2. **`exposure_time` is per-trial uniform in the censored table.** Every clock is observed until the channel stop, so within one trial every clock's exposure is the same number, and the informative quantity is `eligible_time`. This is correct and it means `exposure_time` alone is a weak denominator; the exposure-normalised statistics ticket 06 builds should use opportunity. It is now also *derivable*, which is what makes the review's 999-unit forgery a mismatch — see fix-up round 1.
3. **Eligible time is endpoint-resolved.** An elementary interval counts as eligible when its own endpoint is, which is the same convention every other observable in this package uses and is stated rather than hidden. It inherits whatever the endpoint scheme's between-sample error is — which is what the killed-diffusion oracle and the moving-band audit exist to measure, and the moving-band audit is currently a `numerical_no_result`.
4. **The stop-time comparison is exact across clocks.** `stop_time` is an endpoint on the *winning* clock's elementary mesh, which includes that clock's crossings. A clock with a different crossing schedule is observed to the last endpoint at or before the stop, which can be up to one elementary interval earlier. Its `exposure` is still recorded as the channel's observation window, so `eligible_time <= exposure` holds; the granularity difference is the same interval censoring the event times carry.
5. **Throughput is not benchmarked.** Ticket 07 owns it.
6. **No production budget has been applied to anything here.** Every manifest records `numerical_gate = diagnostic_only`.

## Reference diagnostic run

64 trials, 16 clocks, 80 finest steps; `K_peak = 0.9`, `D = 0.08`, tolerance 0.35, dwell 0.5, `dt = 0.05`, support 2.0, namespace `t05-reference`, 8 shadow trials. **Schema version 3.**

| Quantity | Value |
| --- | --- |
| Wall time | 33.9 s (≈164 000 clock-steps over both passes) |
| Peak allocation | 1138 kB — 90 kB above the version-2 run, for 16× the durable rows, because rows are written and dropped |
| Trials-by-clocks-by-steps array avoided | 0.66 MB at this size, growing with all three |
| Categories | committed 58, dwell_failed 6, lock_failed 0, never_eligible 0 |
| Survival | 1.0 → 0.09375, non-increasing |
| Shadow commitments | 17, against 6 retained by the race — **11 censored away** |
| Byte-identical across `(clock_block, step_window)` | (1, 1), (16, 4096), (3, 7) — all five files identical |

```
manifest  fa2ac5172029c77a127d780499775f23fc732617d3bd75ab1693db32cd5c3248
ledger    2fcc8daf8ea3f9912312e06d8d478a1ced85eab0f46732cd26a05b61d8bc4f29     64 rows
clocks    1c55d17bd000800266c44b6608c1c5c6b681b313ece09ced0d889767f03ab994   1024 rows
shadow    7a9de2b1a7377d8092a6dc56b2c3049c94013ac12be537683142ed3ef60fad2c    128 rows
```

The authoritative table, and a committed trial row whose winner never reset (`-`):

```
trial,clock,detuning,category,committed_at,first_eligible_at,first_inside_at,last_reset_at,eligibility_entries,band_entries,dwell_resets,endpoints,eligible_endpoints,inside_endpoints,exposure_time,eligible_time,final_phase,won,co_completed
0,0,-1.875,never_eligible,,,,,0,0,0,80,0,0,4.0,0.0,-3.5963955383487507,false,false
```

```
2,committed,-0.09999999999999987,-0.09999999999999987,true,1,5,-0.625,-0.833451607996971,-0.5999999999999999,-0.7,-,8,3,8,5,6.3585573669276245
```

The derived per-clock aggregate for the busiest clock, computed by `clock_totals()` from rows the gate reconciled — nothing on disk asserts any of it:

```
clock 8, detuning 0.125: trials_eligible 64, trials_inside 30, wins 17,
co_completions 0, eligibility_entries 64, band_entries 59, dwell_resets 40,
exposure_time 131.5, eligible_time 97.3805
```

Every manifest carries `endpoint_status = passed at the declared reference tolerances`, `moving_band_status = numerical_no_result pooled and in fourteen of fifteen per-regime cells at the frozen reference sample`, `numerical_gate = diagnostic_only`.

## Fix-up round 1 — what the independent review changed

### The durable schema now keeps histories, not totals (finding P1a)

`clocks.csv` was one aggregate row per clock. It is now **one authoritative row per `(trial, clock)`**, carrying category, commitment, first eligibility, first band entry, last reset, eligibility-entry / band-entry / reset counts, endpoint / eligible-endpoint / inside-endpoint counts, exposure, opportunity, final phase, and the win and co-completion flags. `shadow.csv` carries the same fields minus the two only a race can have. `winner_last_reset` joins the trial view.

Two new quantities had to be measured to fill it: `eligibility_entries` (transitions into the tongue, distinct from eligible *samples*) and `inside_endpoints` (endpoints at which the clock was inside the band, which the entry and reset counts cannot reconstruct because they say how many dwells there were, not how long they lasted).

The aggregate is **derived, never stored**: `ClosedLedger.clock_totals()` computes it from rows the gate has already reconciled. There is no unbound summary anywhere in a closed run. The writer keeps nothing between trials at all now — the running per-clock counters are gone.

Cost: the clocks table grows from `N` rows to `trials × N`. For a 64×16 run that is 1024 rows, written and dropped one trial at a time; peak memory is unchanged.

### The gate derives instead of reading (finding P1b)

`_require_consistent_rows` was shallow inequalities. It now recomputes, per trial, from the authoritative rows: the channel category, the winner list, the co-completion count, each winner's own `co_completed` flag, every per-winner column, the eligible and inside clock counts, the entry and reset totals, and the opportunity sum. Exposure is recomputed from the manifest window and the channel stop through `raw_race.exposure_of` — the *same expression the writer used*, so a fabricated exposure is a binary64 mismatch rather than a plausible number. Every indexed detuning in every table must equal the manifest's detuning for that clock exactly. And the censored table must be a prefix of the shadow table on the same keys.

All three of the review's recomputed-hash forgeries are reproduced verbatim in the suite on the same zero-coupling two-trial shape and all three refuse, together with two more of the same family. Five positive controls sit beside them.

### The population is declared (finding P1c)

New `PopulationIdentity` (model, pulse digest, ordered detunings) and `ClockPopulation` (paths + identity, every path rebuilt and checked against the declaration). The four public race doors take a `ClockPopulation`, and `ChannelOutcome` retains the identity and validates against it rather than against `range(len(clocks))`.

`PopulationIdentity.require_complete` compares length, identifiers, order **and mismatches**, exactly. Right-end truncation, front omission, middle omission, reorder, duplicate identifier, same-length detuning substitution, a different declared drive and a mixed-model population all refuse before an outcome exists.

### Output is scoped and cleaned (finding P2)

`write_raw_run(config, run_name, ...)` — no directory argument exists any more. `open_raw_run(run_name)` likewise. `_require_inside_results` checks the **resolved** path, so a symlink inside the results root pointing outside it is refused rather than followed.

Verifier fixtures live under the package results root inside `_scoped_run` contexts and are removed in `finally`. `main()` drains anything left in its own `finally`, and an `atexit` hook covers a process that imports the module and exits without reaching `main` — which is how the first attempt at this left a fixture behind. A final check asserts the results root is empty or absent after every other check has run.

### Schema version 3

`LEDGER_SCHEMA_VERSION` and `MANIFEST_SCHEMA_VERSION` both move to 3; versions 1 and 2 refuse rather than partially parse. The manifest gains `pulse_digest`, so the declared drive is frozen alongside the grid. A new `times` column kind spells an absent instant inside a list cell as `-`, because an empty field already means the empty list and a winner with no reset is an ordinary case.

### Suite

85 → 95 → **99 checks**. Criteria 90–93 are new; 22, 25, 40 and 44 were extended in place. No check was renamed or removed.

## Fix-up round 2 — temporal authority and reader scope

### Every row carries a derived observation interval (P1)

Round 1 derived categories, winners, detunings and *censored* exposure. A re-review moved **times** instead and got four more records accepted with every digest and marker field recomputed: a no-stop exposure changed `4.0 → 2.0`; a censored loser's `first_eligible_at` moved to the manifest close, after its own trial had stopped; a same-key shadow `first_eligible_at` moved off the value the censored walk had already observed; and a shadow row inside a band it had not yet entered.

The cause was one omission with three faces: event times were bounded against the **whole manifest window** rather than each row's own observation interval, shadow exposure was never derived, and the shadow prefix compared only counts.

Now each row carries a derived **observation end** — its own commitment, else the channel stop (censored) or the window close (no-stop). `exposure_time` must equal `end − window_open` exactly. Every recorded instant must lie in `(window_open, end]`. Events must be causally ordered:

- `first_eligible_at ≤ first_inside_at`, and an inside event requires an eligibility;
- `last_reset_at > first_inside_at`, and a reset requires a prior inside;
- `committed_at > first_inside_at` and `> last_reset_at`;
- absent/present timestamps must agree with zero/nonzero counts, and `inside_endpoints > 0 ⟺ band_entries > 0`.

Verified empirically over 192 real rows before being asserted: zero violations of any strict form.

### The shadow prefix is now a path relation, not a count relation

Two regimes, decided by comparing observation ends:

- **Equal ends** — the clock committed, or the trial ran to the window close. Both walks are then *the same walk*, so every shared field must be **identical**. (6 of 96 rows in the probe run; zero mismatches.)
- **Shorter censored end** — counts may only grow; `first_eligible_at` and `first_inside_at`, once observed, may not move; equal reset counts require equal reset times, and any extra reset or commitment must fall strictly after the censored walk stopped looking.

### The public reader is scoped (P1)

`open_raw_run` now calls `_require_inside_results` on the resolved path *before* any existence check, and reads through the validated path rather than the lexical one. The reviewer's reproduction — a valid closed run moved outside and reached through a `results/<name>` symlink — is refused; the ordinary in-root run still opens.

Reading through the resolved path also closes the swap-after-validation window: a link replaced after the check cannot redirect a read that no longer goes through it.

### Stale live-schema wording (P3)

`raw_ledger.py` called the live 45-field v3 manifest schema "version-2" one line above the constant saying 3. Corrected, and guarded: `_stale_live_schema_prose` extracts the version from five *declaration* patterns across `raw_ledger.py`, `raw_runner.py`, `raw_race.py` and `README.md` and requires it to equal `MANIFEST_SCHEMA_VERSION`. Ten fixtures pin the patterns — five declarations that must be caught (including the exact stale sentence) and five historical sentences that must not be, since `What changed at schema 2` is true and must keep passing.

### Suite

99 → **100 checks**. Criterion 94 is new; 44 and 93 were strengthened in place. No check renamed or removed.

## Fix-up round 3 — joint prefix monotonicity and pinned file handles

### Opportunity and prefix (P1)

Round 2 derived each row's observation end. A re-review then found six nearby records still accepted, all about *opportunity* or the *same-key prefix* rather than a single instant.

Three rules close them, and each is an identity the writer already obeys:

1. **A commitment already observed recurs unchanged.** If the censored row committed, the shadow row must carry the identical `committed_at` — checked **before** the observation ends are compared. That ordering is the whole fix: deriving a moved commitment's exposure also moves its derived end, which stepped the old rule out of the equal-ends branch it lived in.
2. **Opportunity and eligible endpoints are zero together.** Every counted endpoint closes an interval of strictly positive duration — a zero-duration coordinate handoff is not an endpoint — so `(eligible_endpoints == 0) == (eligible_time == 0.0)`, row-locally, in both tables.
3. **Counts and times are jointly monotone across a longer prefix.** A strictly later observation end must add at least one endpoint; an unchanged eligible count requires unchanged opportunity; an increased eligible count requires strictly increased opportunity. Plus: equal band entries cannot lose inside endpoints.

Verified over 288 real rows and 89 longer-prefix pairs before being asserted — zero violations of any form.

Controls added to the census: a longer observation adding only ineligible endpoints; one adding eligible endpoints *and* opportunity; a later first eligibility the censored walk never saw; a later reset; a later commitment. The run contains all thirteen shapes.

### Scope is a capability, not a check (P1)

A re-review defeated resolved-path validation four ways, two of them without any concurrent attacker: `Path.exists()` reports a **broken** symlink as absent, so the writer's overwrite check passed and `write_bytes` then followed the link; and the reader's per-file opens followed the final component every time.

Validation and I/O are now one operation:

- the **package directory**, fixed at import from `__file__`, is the only name resolved by string;
- `results/` and the run directory are opened beneath it as directory descriptors with `O_NOFOLLOW | O_DIRECTORY`;
- every one of the five files is opened relative to the pinned run descriptor — `O_RDONLY | O_NOFOLLOW` plus an `fstat` regular-file check on read, `O_WRONLY | O_CREAT | O_EXCL | O_NOFOLLOW` on write;
- the close marker is still written last, through the same descriptor;
- `_require_scoped_io` **fails closed** if `O_DIRECTORY`, `O_NOFOLLOW`, `O_EXCL` or `dir_fd` support is missing, rather than claiming a property it cannot deliver.

All four reproductions refuse. The broken-link case creates no external target and does not even create the directory the links point into. A run directory opened, then replaced on disk, still reads through the descriptor it opened — never the replacement.

### The `os` widening

The raw import allowlist gained `os`; `pathlib` cannot express `dir_fd` or `O_NOFOLLOW`. Bounded by adding fourteen process-spawning names (`system`, `popen`, `exec*`, `spawn*`, `fork*`, `posix_spawn`) to the banned-name scan, so the widening buys the descriptor primitives and nothing else. The fresh-interpreter import probe still loads exactly the ten intended modules with `forbidden_loaded=[]`.

### Bytes and suite

**The written schema is unchanged**, so the reference run's five files are byte-identical to rounds 1 and 2 — same digests. Round 3 changed how files are opened and what a reader will believe, not what the writer produces.

100 → **101 checks**. Criterion 95 is new; 94 was strengthened in place. No check renamed or removed.

## Verification burden discharged

**Ten** checks were new at the first submission, one per acceptance criterion 80–89 inclusive — that range has ten members, and an earlier draft of this note said nine, which was simply wrong. The suite grew from 85 checks to 95, and criteria 22, 25, 40 and 44 were extended rather than replaced. The first fix-up round adds four more criteria (90–93) and takes the suite to 99. The command paths — module, direct script, `--verbose`, `-W error`, `--prove-failure-exit`, `py_compile` — are exercised and reported in the handoff.
