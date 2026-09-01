---
title: "08 — Execute frozen production, falsifications, and final review"
kind: ticket
status: 0
---

# 08 — Execute frozen production, falsifications, and final review

## Objective

Execute the user-approved frozen single-channel experiment, run only the predeclared causal controls and staged sensitivities, and produce a reproducible positive, negative, or numerical-no-result scientific verdict.

## Governing artifacts

- [Closed single-channel plan](../..), especially **Experiments S5–S7**, **Predeclared interpretations**, and **Completion boundary**
- [Pressure-test and closure record](../../pressure-test)
- [Ticket sequence](..)

## Dependencies

- [07 — Feasibility, pilot, and production freeze](../07-feasibility-pilot-and-freeze)
- Explicit user approval of the frozen production manifest and resource estimate.

## In scope

- Fresh production namespace using the frozen manifest without revision.
- Primary finite-population full-Adler sweep, central-clock control, fixed-contraction width-only control, and their paired uncertainty.
- Required stationary-hazard control with declared burn-in/reset semantics.
- Numerical audit replay and refusal to interpret a failed convergence/oracle gate.
- Frozen complementary-log-log, curvature, time-resolved rising/falling, survival, and winner-mismatch analyses.
- Staged one-factor sensitivities for timestep, noise, dwell, band, pulse duration conventions, physical population, initial phase, and one structured spectrum—only in the order authorized by the plan.
- README/results walkthrough and independent adversarial code/scientific review.

## Out of scope

- Retuning after production, changing the coupling window, substituting sensitivity runs for the primary result, full factorial expansion, two-channel polarization competition, manuscript edits, or claiming a Born derivation.

## Requirements

1. Verify source and manifest hashes before execution; any mismatch stops the run.
2. Production never reads pilot trials into its estimates.
3. Every coupling cell, zero/all-event cell, unresolved trial, co-completion, and exclusion remains visible.
4. A failed timestep, killed-diffusion, moving-band, power-model, or curvature gate produces the plan's declared no-result rather than a revised analysis.
5. Width-only or central-control success at the target scaling blocks the width-times-rate causal interpretation.
6. Endpoint scaling alone is insufficient; out-of-sample time behavior and winner mismatch must agree.
7. Sensitivities run one factor at a time after the primary verdict and retain their own namespaces.
8. Independent review receives frozen manifests, raw-ledger hashes, code, checks, and analysis—not only plots.

## Acceptance criteria

- Approved production finishes within the frozen or explicitly stopped resource envelope and writes closed, hash-verifiable ledgers.
- The canonical verifier and every numerical/scientific gate pass, or a machine-readable no-result names the failed gate.
- The primary report includes raw counts, risk sets, survival, hazards, cumulative hazards, exponent and uncertainty if valid, lack-of-fit, all comparator curves, controls, and unresolved categories.
- The conclusion follows the predeclared interpretation table and is one of: candidate supported over the tested regime; candidate falsified/incomplete; no valid exponent; or numerical no-result.
- Sensitivity results are labeled secondary and never alter the frozen primary analysis.
- Independent adversarial review has no unresolved correctness finding; scientific disagreements remain recorded rather than silently resolved.
- README clearly states that even a positive single-channel result does not establish polarization Born frequencies, energy routing, exclusivity, a microscopic bath, or the Born rule.
- No manuscript file is modified.

## Handoff

Give John a plain-English learning report before detailed tables: what was tested, what happened, which controls mattered, what failed or survived, what remains unknown, and whether the two-channel experiment is justified. Include exact paths to manifests, raw ledgers, analysis files, and the independent review.
