---
title: "Fix-up — close raw scanner, configuration, and ledger boundary gaps"
kind: ticket
status: 2
---

# Fix-up — close raw scanner, configuration, and ledger boundary gaps

## Parent and evidence

- [Ticket 01](../..)
- [Independent review](../independent-review)
- [Closed stochastic plan](../../../..)

Code scope remains `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Close the three concrete false-negative/read-boundary defects found by independent review without weakening any of the 32 passing checks or adding event physics.

## Required changes

### 1. Structural scanner

- Check forbidden vocabulary in imported object names and aliases, function/class names, arguments, and assignment/binding targets—not only ordinary `Name` and `Attribute` uses.
- Keep allowed relative-module traversal distinct from validation of an object imported from that module. `from . import validation` may be allowed; `from .raw_config import hazard as event_rule` must fail because the imported object is forbidden.
- Replace the unenforceable “no exponentiation means no square” claim with an enforceable raw-graph rule that also catches at least structurally identical multiplication operands such as `coupling * coupling`, plus equivalent explicitly named square helpers used in raw code.
- Add the reviewer's hidden-object and multiplication mutants to the registered/live mutation evidence without overclaiming sandbox-level semantic detection.

### 2. Exact configuration types

- `validate_raw_config` must require exact `RawEventConfig` type, rebuild an exact base instance from an explicit allowlist of fields, and require/rebuild an exact `RawClockGrid`.
- Reject dataclass and ordinary subclasses, including a frozen subclass carrying an opaque `predictor` or other extra field.
- Preserve mapping construction and all established TypeError/ValueError conventions.

### 3. Closed-ledger evidence

- Require an exact `CloseMarker` and reconstruct/canonicalize it at read time so post-construction mutation cannot bypass schema, row-count, or digest validation.
- Require manifest bytes and verify them against `manifest_digest`.
- Bind `row_count` to a separately supplied expected trial count from the validated frozen manifest, or to independently parsed rows once a row parser exists. Ticket 01 should use the manifest-count form because ledger row generation is still out of scope.
- Reject wrong positive counts, unsupported schema, zero count, invalid manifest digest, marker subclasses, changed manifest bytes, and post-construction mutation.
- Keep the digest explicitly non-cryptographic-authentication/non-signature in documentation.

## Acceptance criteria

- Both reviewer mutants (`def hazard` imported under a safe alias; `coupling * coupling`) fail the registered structural checks.
- Configuration subclass probes fail and returned valid configurations/grids are exact base types.
- The same payload cannot pass with row counts 1, 2, and 999 when the independently supplied manifest expectation is fixed.
- Mutated marker fields and wrong manifest bytes/digests fail at the read gate.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, and compile checks pass.
- All original deterministic residuals remain unchanged and no tolerance is weakened.
- The package remains untracked and no file outside it changes.

## Completion

Report exact fixes, new/strengthened checks, API signature changes, commands/results, compatibility implications, and anything the closure reviewer should probe. Ticket 01 remains open until the same independent reviewer closes this fix-up.
