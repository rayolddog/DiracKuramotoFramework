---
title: "Ticket 05 fix-up — authoritative clock histories, semantic ledger, population binding, and scoped output"
kind: ticket
status: 2
---

# Objective

Close every actionable finding from the first independent Ticket 05 review while preserving the race, replay, keying, shadow-sample, memory, isolation, and non-claim behavior that already passed.

## Governing review

- [Independent Ticket 05 review](../independent-review)
- [Ticket 05](..)

## Required corrections

### 1. Preserve authoritative per-trial/per-clock diagnostics

- Persist one censored row for every `(trial, clock)` in the physical race.
- At minimum retain: trial, clock, detuning, per-clock category at the shared stop, commitment time, first eligible time, first inside time, last reset time, eligibility-entry count, band-entry count, reset count, eligible endpoint count, inside endpoint count, exposure time, eligible time, final phase, completion/co-completion status, and any identity fields needed to bind the path.
- Preserve corresponding no-stop fields for every declared shadow `(trial, clock)` row.
- Add winner last-reset time to the channel/trial view.
- Keep a per-clock aggregate table only if it is mechanically derived from the authoritative rows. Otherwise derive aggregates after reading; do not let an unbound summary be the only durable record.
- Bump/version the manifest, table schemas, close marker, hashes, strict parser, and documentation together. Old schemas must refuse rather than partially parse.

### 2. Make closed-ledger semantics derivable and strict

- From authoritative rows, derive and compare every channel category, per-clock category, winner, co-completer, mismatch, count, entry/reset total, exposure, eligible time, inside-at-least-once, and aggregate value.
- Require each table’s detuning for clock `i` to equal the manifest/grid detuning for `i` exactly under the declared serialization.
- Reconcile wins and co-completions by `(trial, clock)` and by clock, not merely as one total.
- Enforce exact trial and clock identity sets, one authoritative row per declared pair, and the declared shadow subset/rule.
- Enforce time and opportunity bounds from the manifest window and channel stop; disallow impossible entry/reset/endpoint/category combinations.
- The three independently accepted forgeries must now refuse even after all hashes and marker fields are recomputed:
  1. `never_eligible` changed to `lock_failed` with zero eligible/inside clocks;
  2. manifest detuning `0.0` paired with clock/shadow detunings `0.75/-0.75`;
  3. fabricated eligibility and exposure `999` in a two-trial, `0.4`-window run.
- Add nearby positive controls so strict reconciliation does not reject valid zero-coupling, unresolved, committed, tied, and shadow cases.

### 3. Bind the public race to the complete declared population

- The public race call must receive or own an immutable declared population/grid identity including exact population size, ordered clock identifiers, and detunings.
- Validate exact length, identifiers, order, detunings, dataset/model identity, and any mesh/control fields needed to establish that the supplied paths are the declared population.
- `ChannelOutcome` must retain and validate the declared population/grid identity; it may not infer completeness from `range(len(clocks))`.
- Right-end truncation of a declared two-clock population and same-length detuning substitution must refuse at the public boundary before a valid outcome exists.
- Test empty, one-clock, full multi-clock, middle omission, trailing omission, reorder, duplicate identifier, and detuning substitution.

### 4. Enforce package-scoped output and cleanup

- The supported public writer must accept a validated run name or otherwise prove the resolved target is a descendant of the package’s ignored `results` root.
- Reject arbitrary absolute paths, parent traversal, and resolved-link escape. Refuse overwriting existing run files.
- If a directory-oriented writer is useful internally, keep it private/testing-only and do not expose it as the production contract.
- Verifier fixtures must live beneath the package results root inside cleanup contexts and be removed on success, assertion failure, and exceptions.
- Add checks that no run directories remain after canonical, direct, deliberate-failure, and warning-as-error paths.
- Interrupted/incomplete writes must remain unreadable and must either be cleaned or be left clearly incomplete without a valid close marker.

### 5. Correct the execution-note count

- Change “Nine checks are new (acceptance criteria 80–89)” to “Ten checks…” or otherwise state the exact intended count accurately.

## Verification contract

- Preserve all 95 prior checks unless a schema/API check is strengthened in place; document any renamed or replaced check.
- Add exact reproductions and discriminating controls for every correction above.
- Re-run canonical, verbose, direct-script, warning-as-error, deliberate-failure, compile, hash-seed, memory, raw-isolation, byte-reproducibility, interrupted-write, and cleanup paths.
- Keep Ticket 04 status exactly `stationary passed / moving-band numerical_no_result / diagnostic_only`.
- Keep every non-claim: first clock is a model stopping event, not detector click, absorption, measurement, unique actuality, microscopic bath, two-channel outcome, or Born-rule result.

## Completion gate

The fix-up closes only after the same independent reviewer returns `CLOSED`. Durable rows must support later censoring analysis without rerunning the model, and neither a truncated population nor a recomputed-hash semantic contradiction may become a valid public result.
