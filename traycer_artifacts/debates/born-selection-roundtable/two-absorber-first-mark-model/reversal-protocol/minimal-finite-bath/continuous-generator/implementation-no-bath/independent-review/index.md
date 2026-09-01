---
title: "Independent review of the 576-state no-bath implementation"
kind: review
---

# Independent review

Reviewed `first_mark_two_absorber/` against the implementation ticket and its parent continuous-generator specification. No code was changed.

## Findings

### Medium — `capture_and_return_schedule` silently stops being a return schedule when `delta` is nonzero

`controls.py:108-126` exposes `delta`, applies the same detuning during capture, hold, and return, and documents that the photon returns with its original relative phase. But the pulse duration at `controls.py:118` is the resonant `pi/(2K)` time and only `K` changes sign at `controls.py:121`; the detuning term does not. This is not an inverse of the detuned two-level evolution. With `K=0.85`, `t_dark=1.9`, and `delta=0.5`, an independent run returned only `0.8226530516` arm-photon population and had phase-aligned state error `0.4312719942`. The bundled coherent-return check uses only the default `delta=0`, so it cannot expose this (`verify.py:361-390`).

Either reject/non-expose nonzero detuning on this resonant helper, or define and test the intended detuned return protocol. If it is meant to follow the parent operational-reversal rule, the controlled detuning must be treated according to that rule rather than silently replayed unchanged.

### Medium — the recombiner test does not test recombination phase or two-arm interference

The implementation at `model.py:214-225` contains both route operators and the specified complex phases. However, `verify.py:318-331` starts from photon A only, sets only `J_A`, and compares only output population to `sin^2(Jt)`. That population is independent of `theta_A`, so this check would still pass if theta were ignored or conjugated. It also never exercises the shared-output bright/dark interference that is the physical purpose of the recombiner.

Add a two-arm test that verifies constructive and destructive inputs for declared `theta_A`, `theta_B`, including the `sqrt(2)J` bright-mode rate. As an independent probe of the current code, equal arms with equal route phases reached output population `0.9999999999999998` at `pi/(2 sqrt(2) J)`, while a relative input phase of `pi` produced `4.88e-30`; the source is currently correct, but the advertised verification does not protect that semantics.

### Low — the README misstates why the run stays in the one-excitation sector

`README.md:188-192` says the state space forbids more than one optical excitation by construction. The actual tensor product contains independent field and absorber factors, and `basis_state` accepts all their combinations (`model.py:265-269`). For example, both `|vac,e_A,e_B>` and `|photon-A,e_A,g_B>` exist and have excitation number 2 under `N_excitation` (`model.py:190-191`). The supplied initial state starts in the `N=1` sector and the Hamiltonian conserves `N`; that conservation, not the 576-dimensional state space alone, prevents double excitation in the calibration trajectory.

Reword the claim to distinguish the four-state field truncation from restriction to the dynamically invariant one-excitation sector.

## Verification performed

- `python3 -m first_mark_two_absorber.verify --verbose`: **15/15 checks passed** under NumPy 2.3.5.
- Independently inspected every source and documentation file in `first_mark_two_absorber/`.
- Independently probed detuned return, two-arm constructive/destructive routing, and basis states outside the one-excitation sector.

No correctness issue was found in tensor ordering, transition direction, Hamiltonian Hermiticity, resonance/energy bookkeeping, resonant or generalized Rabi expectations, the current two-arm route operator itself, or construction of the reverse-ordered, sign-flipped global inverse.
