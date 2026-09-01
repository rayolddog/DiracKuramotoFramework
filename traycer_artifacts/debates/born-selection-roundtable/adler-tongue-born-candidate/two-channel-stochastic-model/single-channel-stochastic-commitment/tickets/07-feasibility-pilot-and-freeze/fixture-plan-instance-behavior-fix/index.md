---
title: "Ticket 07 fix-up — bind fixture writer to validated plan behavior"
kind: ticket
status: 2
---

# Ticket 07 fix-up — bind fixture writer to validated plan behavior

## Objective

Close the independent review finding that an exact-type, non-slotted
`PilotPlan` can retain its declared fields and digest while instance attributes
shadow methods the verifier fixture writer calls after validation.

## Required change

- Treat the caller record only as input to validation. After validation,
continue exclusively with a freshly constructed exact fixture plan, or prove
equivalently that no unexpected instance state can influence writer
behavior.
- Ensure both whole-fixture and per-cell paths use that validated behavior for
name mapping, coupling mapping and configuration construction.
- Preserve the single `config_for` snapshot per cell and the existing
pre-directory refusal boundary.
- Add focused coverage for exact-type instances carrying instance attributes
named `require_run_name`, `coupling_for`, `config_for`, `run_name_for`, and
relevant derived properties. Each case must be rejected or rendered
behaviorally irrelevant before a production-reserved output can be written.
- Confirm an invalid call cannot alter unrelated pre-existing quarantine
contents and leaves no generated fixture.
- Preserve the honest deterministic fixture, all scientific boundaries, the
127-check/121-criterion census, and the full quiet serial verifier matrix.

## Acceptance

An independent reviewer must reproduce the previous exact-type method-shadow
case, observe no production-reserved directory or fixture output, and return a
strict scoped `CLOSED` verdict. Broader reconstruction-baseline findings remain
outside this fix-up.

## Implementation record — awaiting independent closure

Implemented in `adler_born_two_channel/verify.py` only. Full evidence is in the
[Ticket 07 execution notes](../execution-notes), section *Fixture-plan instance*
*behaviour — fields are not behaviour*. **Status stays 1**: this records what was
built, not a closure verdict.

The finding was reproduced first on the previous bytes — an exact-typed
instance with `require_run_name`, `coupling_for` and `run_name_for` injected
through `object.__setattr__` passed the identity door and wrote a closure under
the reserved name `xpilot-t07-cell-0`.

Two independent answers, either of which closes it alone:

- the identity door refuses any supplied record carrying an attribute outside
`PilotPlan.__dataclass_fields__`, checked immediately after the exact-type
gate and before anything is read or created;
- the door returns the **freshly built** `_t07_fixture_plan()` record rather
than the caller's, and both `_t07_pilot_fixture` and `_t07_write_fixture_cell`
assign that return over their argument, so every later name, coupling and
configuration lookup happens on the fresh record.

`run_names`, `digest` and `cells` are properties — data descriptors — and were
never shadowable; the four plain methods were, and now are not.

Coverage: thirty must-refuse cases inside `check_range_selection`, each run
twice — from an absent quarantine and beside an unrelated pre-existing
quarantined run — asserting the exception type, no root creation, unchanged
quarantine contents, absence of the reserved name, and that the bystander run's
bytes are neither mutated nor removed. Nineteen are new, covering
`require_run_name`, `coupling_for`, `config_for`, `run_name_for`,
`require_run_names`, `require_manifest`, `run_names`, an unrelated attribute,
and the reviewer's exact three-method write-level case, at both entry points.
The honest fixture positive control is preserved and now asserts non-identity
plus field/digest equality of the returned record.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]` (the deliberate probe), both compile passes clean,
`results/` absent throughout. New `verify.py` SHA-256
`dc43d946b2f50bcbdbaa9bda03a3a1a50693c8e1f6d247e43c396216e3ec7697`; all other
package files byte-identical to the R1 baseline.

## Independent closure

The fresh independent re-review returned strict scoped **CLOSED**. It
reproduced the prior exact-type instance case and the individual method cases
at both writer entry points, observed every case refuse before output from an
absent quarantine, and observed an unrelated pre-existing quarantine record
remain byte-identical. The honest four-cell fixture, single configuration
snapshot, five-file closure, production-plan separation, cleanup and full
quiet serial verifier/compile matrix all passed. See the final fixture-plan
section of the sibling [independent review](../independent-review).

This completes only this bounded fix-up. The separate reconstruction-baseline
R1 documentation and criteria findings remain open.
