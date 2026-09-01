---
title: "Ticket 05 fix-up round 2 — temporal ledger authority and reader scope"
kind: ticket
status: 2
---

# Objective

Close the remaining temporal-semantic and public-reader scope defects without altering the validated race, population, keying, or scientific status.

## Required corrections

### 1. Derive every row’s observation interval and temporal semantics

- For each censored `(trial,clock)` row, derive its observation end from the channel stop or full manifest window as appropriate; for each no-stop shadow row, derive the full declared observation window.
- Derive and validate exposure time rather than trusting it. A shadow no-stop row spanning the full window must carry exactly the derived full exposure.
- Every recorded time must lie within its row-specific observation interval, not merely the global manifest window.
- Enforce causal ordering and count/time equivalence:
  - first eligibility cannot follow first inside;
  - first inside requires eligibility and an inside/band-entry count;
  - last reset requires a prior inside event and must not precede first inside;
  - commitment requires prior eligibility/inside and cannot precede them or the last reset;
  - absent/present first-event timestamps must agree with zero/nonzero corresponding counts and endpoint counts;
  - eligible time cannot exceed exposure, and inside/eligible endpoint counts must respect total endpoints.
- For the same physical shadow key, enforce prefix equality for all events already observed before the race stop: first eligibility, first inside, and reset history/times. Shadow-only later events are allowed only after the censored observation end.
- The four reviewer variants must refuse after recomputed hashes/marker:
  1. shadow exposure `4.0 -> 2.0` on an uncommitted no-stop row;
  2. censored loser `first_eligible_at` after its trial stop;
  3. same-key shadow first eligibility changed away from the already observed physical value;
  4. shadow first inside before first eligibility.
- Add nearby valid controls for never eligible, eligibility without inside, inside without reset, reset without commitment, committed, tied, censored-before-shadow-event, and shadow-only later events.

### 2. Apply package-scope validation to the public reader

- `open_raw_run` must apply the same resolved-descendant check as the writer before opening any file.
- A run path under `results/<name>` that is a symbolic link to an external directory must refuse.
- Also verify parent traversal, absolute run names, link replacement after name validation, missing/incomplete runs, and ordinary in-root runs.
- Keep fixtures cleaned on every path.

### 3. Correct stale schema wording

- Change `raw_ledger.py` prose that calls the live 45-field v3 manifest “version-2” to accurate v3/live-schema wording.
- Add a focused documentation guard so this exact stale live-schema statement cannot return.

## Verification contract

- Preserve all 99 checks unless strengthened in place; add direct reproductions and controls for the corrections.
- Preserve schema v3, authoritative rows, population binding, byte invariance, memory, raw isolation, Ticket 04 `diagnostic_only`, and every non-claim.
- Run canonical, verbose, direct, warnings-as-errors, deliberate-failure, compile, cleanup, link-scope, and semantic-mutation paths.

## Completion gate

Round 2 closes only after the same independent reviewer returns `CLOSED`. A recomputed-hash ledger may not contain a physically impossible event order or observation time, and the public reader may not escape the package results root.
