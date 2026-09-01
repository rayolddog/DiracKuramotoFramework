---
title: "Fix independent-review findings in deterministic Adler controls"
kind: ticket
status: 2
---

# Fix independent-review findings in deterministic Adler controls

## Parent and review

- [Implementation ticket](..)
- [Independent review](../independent-review)

## Scope

Resolve all four actionable findings without weakening existing checks or changing the intended physics.

### 1. Independent pulse oracle

- Add off-grid interior comparisons against a raised-cosine formula written independently in the verifier.
- Verify entry/exit crossings against an independently written crossing identity or bisection, not another `RaisedCosinePulse` method.
- Demonstrate that a materially different symmetric pulse with matching endpoints, area, bounds, and peak fails the new check.

### 2. Independent analytic normalization oracle

- Make the verifier own a literal half-pi normalization oracle.
- Assert the exported constant has that value.
- Compare the numerical flux directly with the independent normalization at predeclared couplings and refinement levels.
- Demonstrate that a common factor-of-two mutation fails while exponent/shape controls remain distinct.

### 3. Paired-duration near-edge recovery and honest categories

- Reuse identical release phases across short and longer pulses.
- Show recovery of near-edge trajectories as duration increases, with time-step refinement.
- Separate already-in-band at first eligibility, entered-band later, and never-entered categories.
- Correct README language: finite exposure changes probabilities; it does not make convergence impossible for every initial phase.
- Reserve `lock-failed` for never-in-band trajectories; do not preassign future dwell outcomes.

### 4. Numeric input validation

- Reject non-finite or invalid peaks, centers, detunings, phases, durations, time steps, and storage cadence at public boundaries.
- Require positive finite duration and time step, nonnegative finite peak, and integer `store_every >= 1`.
- Add explicit tests for NaN, infinities, zero, negative, non-integer, and boolean edge cases as appropriate.

## Constraints

- Do not modify anything outside `adler_born_two_channel/`.
- Do not weaken or delete the existing 19 checks.
- Keep analytic normalization structurally isolated from model/simulation.
- Do not add stochastic, commitment, or competition behavior.
- Do not add the optional mutation-sanity CLI unless it directly and minimally demonstrates the two required oracle regressions.

## Acceptance

The expanded suite passes all old and new checks; each review mutation is caught; public invalid inputs fail clearly at the boundary; the README uses probabilistic finite-time language; and an independent closure review finds no remaining actionable issue.
