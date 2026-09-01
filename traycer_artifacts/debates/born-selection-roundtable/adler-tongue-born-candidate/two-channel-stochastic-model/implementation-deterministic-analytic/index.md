---
title: "Implement deterministic Adler calibration and analytic flat-spectrum control"
kind: ticket
status: 2
---

# Implement deterministic Adler calibration and analytic flat-spectrum control

## Parent plan

[Two-channel stochastic Adler test](..)

## Scope

Create an isolated Python package at:

`/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`

Implement only the first three construction stages from the parent plan:

1. stationary deterministic one-clock Adler calibration;
2. raised-cosine photon-envelope calibration of tongue entry, exit, moving stable phase, and finite synchronization time; and
3. analytic finite-grid flat-spectrum relaxation-rate sum and its coupling-squared convergence.

Do not implement stochastic noise, commitment dwell, channel competition, polarization winner frequencies, or manuscript edits.

## Required boundaries

- The analytic rate calculation must be structurally isolated from the deterministic time evolution.
- Dynamics receive coupling, not amplitude-squared input or a precomputed hazard.
- Use a common normalized pulse envelope suitable for later use by two channels.
- Preserve unresolved/failed-lock concepts in documentation, but do not simulate commitment yet.
- Do not import or modify `first_mark_two_absorber/`.
- Do not alter, stage, or revert any pre-existing user changes.
- Prefer NumPy and the Python standard library; keep SciPy optional and isolated if used.

## Minimum files

- `__init__.py`
- `model.py` — phase wrapping, stationary/pulsed coupling, eligibility, stable phase, deterministic Adler stepping
- `analytic.py` — local relaxation rate, fixed flat detuning grid, finite-grid sum, exponent fit or ratio convergence
- `simulate.py` — deterministic stationary and pulsed trajectories
- `verify.py` — registered, readable checks and CLI
- `README.md` — plain-English walkthrough, commands, results, and explicit non-claims
- `.gitignore`

Names may change when technically justified, but responsibilities and boundaries must remain.

## Acceptance criteria

1. Phase wrapping and circular distance work across the negative/positive pi boundary.
2. A stationary inside-tongue clock converges to the correct stable phase.
3. Its measured near-lock relaxation agrees with the analytic local rate away from the critical boundary.
4. A stationary outside-tongue clock remains ineligible and phase-slips.
5. Zero coupling has no eligible clock and no stable phase.
6. The raised-cosine envelope has correct endpoints, peak, and symmetry.
7. Deterministic eligibility entry and exit agree with the instantaneous tongue-boundary crossings.
8. A near-boundary clock visibly lags the moving stable phase and can run out of interaction time.
9. Increasing pulse duration at fixed peak never reduces the calculated eligibility window for a fixed detuning.
10. The analytic flat-grid relaxation-rate sum approaches a constant times coupling squared as the detuning grid and support are refined.
11. The fitted analytic scaling exponent approaches two over a declared safe coupling range.
12. The dynamics/simulation modules do not import or call the analytic sum or fitted hazard.
13. Verification runs from the repository root and as a direct script, exits nonzero on failure, and prints every registered check.
14. README explicitly says these controls do not demonstrate Born probabilities, stochastic selection, commitment, exclusivity, or energy routing.

## Verification commands

At minimum:

```text
python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --verbose
python3 adler_born_two_channel/verify.py
```

Report environment versions, check count, numeric residuals, files changed, and any deviations from this ticket.

## Completion condition

This ticket is complete only when all checks pass without fitting or retuning parameters to conceal a failed physical prediction.
