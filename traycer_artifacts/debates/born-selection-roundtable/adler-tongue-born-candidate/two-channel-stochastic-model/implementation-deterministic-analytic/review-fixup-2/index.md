---
title: "Close exact-entry classification and public validation gaps"
kind: ticket
status: 2
---

# Close exact-entry classification and public validation gaps

## Inputs

- [Implementation ticket](..)
- [Independent review with closure findings](../independent-review)

## Finding 1 — classify at the continuous tongue-entry boundary

Replace the first-stored-eligible-sample classification with a classification evaluated at the analytic continuous entry time for the raised-cosine pulse.

Requirements:

- Propagate or interpolate each deterministic trajectory to the exact entry time using a numerically controlled method.
- Compare its phase with the boundary fixed phase at that instant.
- Name the categories according to what is actually measured: inside the lock band at exact entry, entered the band later, or never entered the band.
- Time-step refine the exact-entry classification and demonstrate stability.
- Retain the robust ever-versus-never and same-phase long-pulse recovery results.
- Remove wording that calls a first-stored-sample coincidence definitively lucky or nonsynchronized.

## Finding 2 — enforce the exported public numerical contract

Audit every public numerical callable and exported dataclass in `adler_born_two_channel`.

Requirements:

- Reject non-real values, strings, booleans, NaN, and infinities wherever a finite real physical parameter is required.
- Reject invalid sign/range values at the public boundary.
- Validate evaluation arguments too, including pulse `envelope(t)`, `coupling(t)`, eligibility predicates, stable-phase/rate/drift functions, and exported analytic helpers.
- Preserve scalar and intended NumPy-array use.
- Private validated-fast-path kernels are allowed so inner integration loops do not repeatedly validate immutable inputs.
- Add direct regression tests for the reviewer examples and a systematic exported-API validation table.
- Error types and messages must identify the offending public argument.

## Constraints

- Do not weaken or delete any of the 24 passing checks.
- Do not change the physical model or add stochastic/commitment/competition behavior.
- Modify only `adler_born_two_channel/`.

## Completion

All existing and new checks pass, the continuous-entry categories are step-stable, invalid public inputs cannot silently resemble physical no-admission, and independent closure review finds no actionable issue.
