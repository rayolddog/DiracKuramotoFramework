---
title: "Edge-case closure — multiply keywords and duplicate manifest keys"
kind: ticket
status: 2
---

# Edge-case closure — multiply keywords and duplicate manifest keys

## Parent and evidence

- [Ticket 01](..)
- [Final fix-up](../fixup-final-closure)
- [Independent review](../independent-review)

Code scope remains `~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`. Do not touch, stage, commit, or revert anything outside this package.

## Objective

Close the two remaining parser edge cases without changing physics, weakening the stated syntactic scanner contract, or adding stochastic/event behavior.

## Required changes

### 1. Keyword-bearing direct multiplication

- Catch direct named multiplication of structurally identical first and second operands when unrelated ufunc options are present, including `np.multiply(x, x, where=mask)`.
- Catch equivalent keyword operands, including `np.multiply(x1=x, x2=x)` and mixed positional/keyword forms where the two multiplicands can be identified unambiguously.
- Preserve valid unequal multiplication such as `np.multiply(x, y)` and `np.multiply(x1=x, x2=y, where=mask)`.
- Do not broaden the claim beyond direct syntactic self-products; the documented alias/data-flow limitation remains.

### 2. Duplicate manifest member rejection

- Parse JSON in a way that detects and rejects duplicate object member names before construction of the manifest mapping.
- Reject duplicate `trials`, `schema_version`, or `run_label` regardless of order or whether the duplicate values agree.
- Continue accepting unique-key manifests with different ordering and whitespace when their exact bytes match the marker digest.
- Keep the exact three-field schema, exception conventions, marker reconstruction, digest verification, and manifest-derived trial-count binding intact.

## Acceptance criteria

- `np.multiply(x, x, where=mask)` and `np.multiply(x1=x, x2=x)` fail the registered scanner checks.
- Unequal positional, keyword, and option-bearing multiply controls pass.
- Duplicate manifest names fail for first-wins, last-wins, and equal-value cases; unique reordered/whitespace manifests still pass with their own digests.
- All prior configuration, marker, digest, schema, count, and pattern-binding probes remain closed.
- Canonical, verbose, direct-script, warning-clean, deliberate-failure, and compile checks pass.
- All deterministic residuals remain unchanged; no tolerance is weakened.
- No file outside `adler_born_two_channel/` changes, and nothing is staged or committed.

## Completion

Report the exact AST operand-selection rule, duplicate-key parsing mechanism, new distinguishing probes, command results, and remaining limitations. The same independent reviewer must close this edge-case ticket before Ticket 01 completes.
