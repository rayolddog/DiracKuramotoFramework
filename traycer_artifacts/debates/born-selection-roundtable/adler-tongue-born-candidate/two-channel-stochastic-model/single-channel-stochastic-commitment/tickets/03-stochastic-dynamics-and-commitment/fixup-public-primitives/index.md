---
title: "Ticket 03 validated public primitives fix-up"
kind: ticket
status: 2
---

# Ticket 03 validated public primitives fix-up

## Objective

Close the remaining stale-object bypasses in exported primitive transitions. A public state-machine or dynamics method may not accept an object that the high-level snapshot validators refuse.

## Required design

Refactor public transition methods into validated wrappers over private trusted kernels:

- `LockCriterion.inside_now` and `LockCriterion.advance` rebuild/validate the criterion and delegate to private kernels. High-level helpers validate once and use the trusted kernels internally.
- Every exported `ClockPath` operation needed for a direct walk—including crossings, initial-state construction, handoffs, advance, observation, and public schedule access—must operate on a rebuilt/validated snapshot or be made private. `run_one_clock` validates once and uses private trusted kernels so it does not rebuild per leaf.
- Trusted kernels must not be exported and must only receive already rebuilt objects.

## Verification

Reproduce the reviewer's direct stale criterion commitment and direct stale width-only walk before the fix. Add exact direct-method probes for stale detuning, nested drive, cached schedule, model/rate and criterion fields, with zero keys and zero state mutation before refusal. Add mutations reducing each wrapper to the old unchecked body. Clean direct public walks and high-level runs must remain bit-identical.

Preserve all 74 checks and their residuals/tolerances, every prior closure, v3 keys, raw isolation, no-file/no-cube behavior and non-claims. Run the full command matrix and update public API evidence/documentation as needed.
