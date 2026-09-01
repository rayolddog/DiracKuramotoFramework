---
title: "Close independent-review gaps in the no-bath generator"
kind: ticket
status: 2
---

# Close independent-review gaps

## Parent

This is a fixup under [Implement and verify the 576-state no-bath generator](..), based on the [independent review](../independent-review).

## Required changes

1. Make `capture_and_return_schedule` explicitly resonant. Remove or reject nonzero detuning rather than advertising coherent return for a schedule that flips `K` but not the detuning Hamiltonian. The separate `capture_schedule` may retain detuning for its generalized-Rabi calibration.
2. Add an automated two-arm recombination test. It must check declared routing phases, constructive and destructive inputs, the bright-mode rate `sqrt(2) J`, and output probability—not merely single-arm routing.
3. Correct the README and any equivalent statement: the full tensor space contains higher-excitation basis states. The prepared state begins in the invariant `N=1` sector, and the implemented Hamiltonian conserves `N`; that is why the calibration run cannot reach double excitation.

## Acceptance criteria

- An attempted detuned use of the resonant return helper cannot silently produce incomplete return.
- A deliberate error in routing phase/sign would fail the new two-arm test.
- The original verification suite and the new check pass locally.
- No files outside `first_mark_two_absorber/` are modified.
