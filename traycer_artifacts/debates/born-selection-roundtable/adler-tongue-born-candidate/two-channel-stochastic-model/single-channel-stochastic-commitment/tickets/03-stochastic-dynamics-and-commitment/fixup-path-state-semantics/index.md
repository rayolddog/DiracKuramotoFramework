---
title: "Ticket 03 fix-up: path-state semantics and directed handoffs"
kind: ticket
status: 2
---

# Objective

Close the two semantic validation gaps found in the final Ticket 03 primitive-boundary review without changing clean trajectories, the v3 noise contract, earlier residuals, or raw-layer isolation.

## Required repairs

1. Validate every supplied `PathState` against its owning `ClockPath`, not merely against the standalone `PathState` constructor:
  - phase reconstruction must satisfy the declared numerical identity bound;
  - full-model states cannot carry the width-control auxiliary target/error pair;
  - width-only target/error presence must agree with eligibility and handoff lifecycle;
  - the lifted target must be congruent to the stable or boundary target appropriate to the current schedule state.
2. Make handoff direction exact:
  - `entry_handoff` accepts only the first endpoint of a finite eligibility window;
  - `exit_handoff` accepts only the second endpoint;
  - wrong-side calls fail before a trusted handoff kernel runs.

## Acceptance evidence

- Reproduce and reject the independently reported forged-state cases, including the congruent-looking `target_lift + 1`, `error - 1` pair, a directly edited reconstruction residual, a full-model live auxiliary pair, and a width-only interior missing pair.
- Reproduce and reject entry at an exit endpoint and exit at an entry endpoint.
- Count that the applicable trusted kernel is not entered on refusal.
- Preserve clean public/trusted/high-level walks bit-for-bit, all prior check residual/tolerance pairs, the v3 keyed-noise values, and all isolation/no-file/no-cube guarantees.
- Add discriminating mutations for every new rule and run the full Ticket 03 command matrix.

## Non-blocking limitation

`TreeLeaf` constructor rebuilding validates canonical address syntax but cannot authenticate a different syntactically valid address without mesh/stream ownership context. The high-level runner retains that ownership guarantee; this limitation is documented rather than expanded in this fix-up.
