---
title: "Implement and verify the 576-state no-bath generator"
kind: ticket
status: 2
---

# Implement and verify the 576-state no-bath generator

## Outcome

Add an isolated `first_mark_two_absorber/` Python package to the Dirac–Kuramoto repository. Construct the full 576-dimensional tensor space and implement the field, absorber, bath-free, capture, and route operators needed for the first calibration. Implement continuous unitary propagation for piecewise-constant Hamiltonians, the analytic no-bath capture-and-return control, and the exact global inverse.

## Scope

- Keep the fixed subsystem order: field, absorber A, absorber B, phase A, record A, phase B, record B.
- Construct explicit 576 by 576 operators without outcome sampling or conditioned jumps.
- Implement the no-bath setting by disabling phase-history and mark/record couplings.
- Begin from one photon coherently divided between paths A and B.
- Verify capture transfers amplitude into the corresponding absorber excitations and returns it coherently.
- Implement exact global inversion as the sign-reversed, reverse-ordered Hamiltonian schedule.
- Provide a command-line verification script and plain-English README.

## Acceptance criteria

1. Every constructed Hamiltonian is Hermitian to numerical precision.
2. State norm remains one to numerical precision.
3. The no-bath capture population agrees with the analytic Rabi-exchange result.
4. Equal A/B inputs and parameters give equal A/B populations.
5. Forward evolution followed by the exact global inverse restores the complete initial 576-component state up to a global phase and numerical tolerance.
6. Tests run locally with the repository's available NumPy/SciPy environment.
7. No pre-existing manuscript, PDF, simulation, or user change is modified.

## Explicit non-goals

- No phase-bath, record-bath, echo, random-reference, Born-selection, or registry claims.
- No manuscript edits.
- No interpretation of the single-excitation truncation as one-world exclusivity.

This ticket implements the first verified slice of the [continuous generator](..).
