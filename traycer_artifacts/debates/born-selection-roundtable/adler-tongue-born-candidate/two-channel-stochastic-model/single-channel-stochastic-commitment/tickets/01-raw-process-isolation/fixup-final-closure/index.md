---
title: "Final fix-up — scanner syntax coverage and manifest-derived row count"
kind: ticket
status: 2
---

# Final fix-up — scanner syntax coverage and manifest-derived row count

## Parent and evidence

- [Ticket 01](..)
- [First fix-up](../fixup-boundary-closure)
- [Independent review](../independent-review)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Close the two bounded defects remaining after closure review, without weakening the 32 checks, changing deterministic physics, or implementing stochastic event generation.

## Required changes

### 1. Complete the stated syntactic scanner contract

- Recognize direct multiplication helper calls with structurally identical operands, including `np.multiply(coupling, coupling)`, as the same forbidden written-square pattern already covered for `coupling * coupling` and `np.square(coupling)`.
- Inspect Python structural-pattern binding fields, including `MatchAs.name`, `MatchStar.name`, and `MatchMapping.rest`, so forbidden vocabulary cannot be introduced through a `match` binding.
- Add the reviewer's exact `np.multiply` and mapping-pattern mutants, plus minimal neighboring pattern cases, to registered mutation evidence.
- Keep the claim explicitly syntactic. Do not add or imply semantic/data-flow analysis.

### 2. Derive row-count provenance from the verified manifest

- Remove the caller's ability to make an arbitrary marker count pass by supplying the same arbitrary `expected_rows` value.
- Parse and validate the authoritative trial count from the manifest bytes whose digest is verified by the exact reconstructed `CloseMarker`, or accept an exact validated manifest object whose canonical bytes are the bytes verified by that marker.
- The gate must bind `marker.row_count` to that manifest-derived count. A manifest declaring two trials with marker count 999 must fail even if a caller tries to supply 999; an empty or count-free manifest must fail.
- Keep manifest parsing narrowly scoped to the frozen Ticket 01 manifest schema. Do not implement ledger rows or event generation.
- Update the public signature, API-validation table, checks, and documentation so none still claim a caller-supplied integer establishes provenance.

## Acceptance criteria

- The reviewer's `np.multiply(coupling, coupling)` mutation fails the registered structural checks.
- Pattern bindings using forbidden names fail for mapping, star, and `as` forms; valid pattern bindings remain accepted.
- Verified manifest bytes declaring two trials accept only a marker with `row_count == 2`.
- Marker/caller count 999 cannot pass against a manifest declaring two trials, and an empty/count-free/invalid manifest cannot establish a count.
- Exact marker reconstruction, schema and digest validation, subclass rejection, and changed-manifest rejection remain intact.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, and compile checks pass.
- All deterministic residuals remain unchanged; no tolerance is weakened.
- No file outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the exact manifest schema and parsing boundary, public signature changes, new mutants and probes, command results, compatibility implications, and limitations. The same independent reviewer must close this ticket before Ticket 01 can complete.
