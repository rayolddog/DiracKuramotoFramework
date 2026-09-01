---
title: "Enforce the no-bath return-helper contract"
kind: ticket
status: 2
---

# Enforce the no-bath return-helper contract

## Finding

The first [closure review](../fixup-independent-review/closure-review) closed the original findings but found that `capture_and_return_schedule` checks nonzero mark coupling only when callers voluntarily supply `params`. A caller can omit it, build a schedule described as coherent return, and then evolve it with nonzero `G`, producing incomplete return without a warning.

## Required correction

- Make the relevant `Params` or `Model` context mandatory when constructing the resonant no-bath capture-and-return schedule, or move construction to an object that already owns that context.
- Reject nonzero `G_A` or `G_B` unconditionally through the public helper API.
- Update every internal caller and the README.
- Extend verification so omission cannot bypass the contract and the nonzero-`G` misuse is protected.

## Acceptance criteria

1. No public call path can construct the advertised no-bath return schedule without supplying the physical context needed to validate `G`.
2. Nonzero `G_A` or `G_B` raises the documented error before evolution.
3. The complete suite passes without weakened tolerances.
4. Only `first_mark_two_absorber/` is modified.
