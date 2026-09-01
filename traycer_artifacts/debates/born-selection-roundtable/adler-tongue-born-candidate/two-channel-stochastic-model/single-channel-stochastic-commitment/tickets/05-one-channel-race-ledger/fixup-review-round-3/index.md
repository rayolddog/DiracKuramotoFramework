---
title: "Ticket 05 fix-up round 3 — complete prefix opportunity and stable file handles"
kind: ticket
status: 2
---

# Objective

Close the remaining shadow-prefix and scoped-file-operation classes without changing the race, written schema bytes, or scientific status.

## Required corrections

### 1. Complete censored/no-stop prefix reconciliation

- A commitment already observed in the censored path must have the identical commitment time in the same-key no-stop shadow path. It cannot move later or earlier.
- Enforce the endpoint-resolved opportunity identities used by the writer:
  - zero eligible endpoints implies zero eligible time;
  - positive eligible endpoints implies positive eligible time;
  - inside endpoints cannot exceed eligible endpoints;
  - each row’s endpoint counts and times remain within its derived observation interval.
- For a longer same-key shadow observation:
  - total endpoints must strictly increase;
  - eligible endpoints and eligible time must be jointly monotone;
  - equal eligible-endpoint counts require equal eligible time;
  - growth in eligible endpoints requires positive added eligible time, and added eligible time requires endpoint growth;
  - counts/timestamps already observed remain identical; only genuinely later events may be added.
- Apply analogous monotone prefix rules to inside endpoints, entries, resets, and commitment status wherever the durable fields permit a determination.
- The six reviewer variants must refuse after recomputed hashes/marker:
  1. observed winner shadow commitment moved from `-0.5` to `-0.4`;
  2. zero eligible endpoints with positive eligible time;
  3. positive eligible endpoints with zero eligible time;
  4. longer shadow observation with no endpoint growth;
  5. equal eligible count with changed opportunity;
  6. extra eligible endpoints with no added opportunity.
- Add valid controls where a longer shadow interval adds only ineligible endpoints, later eligibility, later inside endpoints, later resets, and a later commitment.

### 2. Anchor reader and writer operations to stable directory handles

- Do not validate a path and then reopen it through an ordinary path string.
- Anchor operations beneath the package results root using stable directory descriptors/handles and relative opens. On supported POSIX systems, use no-follow semantics for the run directory and each of the five files; fail closed if the required primitives are unavailable.
- Reader: open the declared run directory beneath an already opened results-root handle, open every required regular file relative to that directory without following links, read through those handles, and verify file type/identity as needed before accepting.
- Writer: create/open the run directory beneath the results-root handle, create every file exclusively relative to the stable directory handle without following pre-existing file links, and write the close marker last.
- Directory-name replacement after lexical validation must not redirect either reader or writer. A linked run directory and linked individual table files must refuse or remain unable to redirect I/O.
- The two reviewer reproductions must close:
  1. an in-root directory whose five file names refer to an external valid run must not open;
  2. five pre-existing broken file links must not cause the writer to create external files.
- Add ordinary in-root read/write controls, interrupted/incomplete controls, overwrite refusal, cleanup, and platform-capability checks.

## Verification contract

- Preserve the byte-identical legitimate reference run if the durable schema itself need not change.
- Preserve all 100 checks unless strengthened; add exact reproductions and controls.
- Preserve schema v3, population identity, memory, raw isolation, Ticket 04 diagnostic-only status, results cleanup, and all non-claims.
- Run canonical, verbose, direct, warnings-as-errors, deliberate-failure, compile, file-handle scope, semantic mutation, and cleanup paths.

## Completion gate

Round 3 closes only after independent review returns `CLOSED`. Same-key shadow opportunity may grow only through actual later eligible intervals, and public I/O may not be redirected after scope validation.
