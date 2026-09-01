---
title: "Ticket 03 execution decisions"
kind: spec
---

# Ticket 03 execution decisions

## Dynamics module placement

The governing plan's code-fit table assigned Euler–Maruyama stepping and the width-control phase lift to `stochastic.py`. During implementation, those responsibilities were placed in a new raw-graph module, `dynamics.py`.

This is accepted technical drift, not a product change:

- Ticket 02 established `stochastic.py` as a drift-free physical-noise source and mechanically pins that responsibility.
- `dynamics.py` consumes Ticket 02's `TreeLeaf` sequence without changing its key schema, Gaussian law, or public refinement surface.
- `dynamics.py` is transitively reachable from `raw_runner.py` and is covered by the same analytic-isolation, banned-name, square-rule, runtime-namespace, and public-validation checks.
- The product boundary remains unchanged: one authoritative unwrapped phase, exact tongue handoffs, timestamp dwell, and no analytic predictor or prescribed hazard in the raw process.

Relocating the stepper into `stochastic.py` would weaken the already-closed single-responsibility boundary without changing user-visible behavior, so the separate module is retained.

## Fixed-rate freeze boundary

Ticket 03 freezes the derivation rule, not a production result: the width-only rate is the central-clock Adler relaxation at the geometric midpoint of a declared peak-coupling range. The current `(0.5, 2.0)` range is explicitly provisional. Ticket 07 remains responsible for writing the pilot-selected range and its derived scalar into the production manifest before production event results are opened.

No per-run coupling, mismatch, trial, dwell, tolerance, or noise value may alter that frozen scalar.
