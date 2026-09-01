---
title: "Complete Adler public-domain validation"
kind: ticket
status: 2
---

# Complete Adler public-domain validation

## Source

[Independent review, final closure section](../independent-review)

## Scope

Close the remaining API-contract finding without changing the already validated stationary or pulsed physics.

- Require nonnegative coupling in every public model and analytic API that accepts physical coupling.
- Reject nonpositive or invalid log-fit inputs rather than silently dropping them.
- Require actual boolean eligibility arrays; reject numeric and string coercion.
- Validate public methods of exported classes, including trajectory queries.
- Require public steppers to reject non-finite callback outputs.
- In measured relaxation, permit NaN only as the documented missing-target sentinel; reject infinities, strings, booleans, and other wrong-kind arrays.
- Extend the completeness check from exported names to public numerical methods and each meaningful argument domain.

Do not weaken existing checks, modify other directories, or change the physical model.

## Completion

All previous and new checks pass, every independent probe in the final closure finding rejects clearly, and the reviewer reports no remaining actionable issue.
