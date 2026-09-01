---
title: "Ticket 04 execution decisions"
kind: spec
---

# Ticket 04 execution decisions

## Continuum reset observable

The plan's literal request for a convergent Brownian reset count is not mathematically well posed: a continuous Brownian path can touch and recross a boundary infinitely often. Ticket 04 therefore uses edge-resolved first-absorption probabilities for the stationary killed problem. Their sum is the probability of at least one killing exit. This is the continuum authority for the reset/exit comparison.

For the moving-band replay, the discrete number of audit-added resets is retained as a transparent diagnostic but is not required to decrease under refinement. Its `require_decrease = false` status is frozen in the budget digest and exported in the report. It cannot by itself establish convergence or rescue a pass. Survival/commitment differences, time shifts, pathwise-subset behavior, and every other declared convergent observable remain gated.

This is accepted technical clarification, not permission to weaken the later production budget. Ticket 07 must decide whether the diagnostic magnitude is small enough for the intended experiment and must still return a numerical no-result when the convergent observables miss their frozen bounds.

## Audit key piece ordinal

The audit uniform key retains the plan's immutable dataset/trial/clock/finest-step address and adds a deterministic elementary-piece ordinal. One finest step can contain two separate eligible pieces after exact exit/entry splitting; without the ordinal those pieces would reuse one uniform. The ordinal is accepted as a uniqueness-preserving refinement. It remains inside the disjoint audit namespace and cannot perturb the physical Brownian tree.

## Noise-floor semantics

The frozen `noise_floor` is an adjacent-refinement Monte Carlo allowance: a finer discrepancy may exceed the preceding discrepancy by no more than the predeclared floor and must then fall or remain statistically unresolved. It is not an after-the-fact tolerance and not permission for systematic growth. Its value, interpretation, and any observable-specific `require_decrease` flag are included in the immutable budget digest.

## Review burden

Independent review must challenge all three decisions. In particular, it must verify that disabling reset-count monotonicity cannot bypass the survival/commitment gates, that the piece ordinal is canonical under paired refinement, and that `noise_floor` cannot be changed after results are opened without invalidating the digest.
