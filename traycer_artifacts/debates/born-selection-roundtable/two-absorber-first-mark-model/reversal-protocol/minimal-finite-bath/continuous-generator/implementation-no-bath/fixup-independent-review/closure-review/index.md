---
title: "Closure review of the independent-review fixup"
kind: review
---

# Closure review

The fixup closes all three findings from the original independent review. One new medium-severity gap remains in the broader `ResonantReturnError` guarantee.

## Remaining finding

### Medium — the no-bath `G` guard is optional, so the helper can still silently return a non-returning schedule

`capture_and_return_schedule` describes itself as “resonant and no-bath only” and says it enforces that (`controls.py:119-150`), but `params` defaults to `None` and the `G_A/G_B` check runs only when the caller supplies it (`controls.py:120,161-166`). A caller can therefore build the schedule normally, evolve it with `Model(Params(G_A=..., G_B=...))`, and receive no `ResonantReturnError` even though the photon fails to return. The new verification only exercises the guarded form with an explicit `params=` argument (`verify.py:451-462`), so 17/17 checks can pass while this hole remains.

Independent reproduction with `K=0.85` and `t_dark=1.9`:

| `G_A = G_B` | Returned arm-photon population | Phase-aligned state error |
| --- | --- | --- |
| 0.1 | 0.8298890013 | 0.4219420874 |
| 0.3 | 0.0870779969 | 1.1873585712 |
| 0.5 | 0.2540097674 | 0.9959981759 |

Make the relevant `Params`/`Model` mandatory for this helper (or move the helper onto `Model`) if it is to promise enforcement. Otherwise narrow the contract and README wording to say it validates only its emitted controls and that callers must ensure `G_A = G_B = 0`; the current unqualified README claim at `README.md:77-83` is not true.

## Original-finding closure

| Original finding | Verdict | Evidence |
| --- | --- | --- |
| Detuned return silently fails | Closed | Nonzero `delta` and `u` now raise `ResonantReturnError`; the helper emits zero-detuning/zero-`u` segments. The targeted check also demonstrates the refused detuned schedule really fails (`controls.py:151-170`, `verify.py:438-490`). |
| Recombiner phase and two-arm behavior untested | Closed | The new test scans the full analytic phase law, checks bright and dark inputs, and verifies the `sqrt(2)J` rate (`verify.py:363-435`). Runtime mutation probes confirmed it fails when phases are ignored, conjugated, one arm is sign-flipped, or the bright-mode rate is changed to `J`. |
| README says the tensor space forbids `N=2` | Closed | README and observable documentation now distinguish the full tensor space from the invariant `N=1` trajectory, and the suite explicitly constructs and evolves two `N=2` states (`README.md:225-235`, `observables.py:76-87`, `verify.py:245-291`). |

## Verification

- `python3 -m first_mark_two_absorber.verify --verbose`: **17/17 passed** under NumPy 2.3.5.
- Route mutation probes all failed the new route test as intended:
  - ignored phases: residual `0.288163`;
  - conjugated phases: residual `0.564642`;
  - bright coupling reduced from `sqrt(2)J` to `J`: residual `0.974441`;
  - B-arm sign flip: residual `1.0`.
- Direct guard probes confirm nonzero `delta`, nonzero `u`, and explicitly supplied nonzero `G` raise the documented exception.

No code was edited during this review. No other actionable finding survived validation.
