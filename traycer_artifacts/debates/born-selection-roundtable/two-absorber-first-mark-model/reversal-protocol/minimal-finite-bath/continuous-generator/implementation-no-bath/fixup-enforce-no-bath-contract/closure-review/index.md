---
title: "Final closure review of the no-bath return contract"
kind: review
---

# Final closure review

## Verdict

The prior opt-in `G`-guard finding is **closed**. No remaining actionable finding survived review.

## Contract verification

| Requirement | Result | Evidence |
| --- | --- | --- |
| Physical context is mandatory | Pass | The public signature is `capture_and_return_schedule(context, K, ...)`, with no default for either leading argument (`controls.py:141-142`). Calling the old context-free form raises `TypeError` before a schedule is constructed. |
| `Params` and `Model` are accepted | Pass | `_resolve_params` resolves either the supplied parameters or `Model.params` and rejects objects missing the physical coupling fields (`controls.py:119-138`). Independent probes succeeded with both supported forms. |
| Nonzero `G` cannot bypass the public helper | Pass | `G_A` and `G_B` are checked unconditionally immediately after context resolution and before any segment is built (`controls.py:191-212`). Symmetric and one-sided nonzero couplings raise `ResonantReturnError` through both `Params` and `Model`. |
| Resonant/no-bath controls remain enforced | Pass | Nonzero `delta` and `u` still raise, while every emitted valid segment has `delta=u=0` (`controls.py:199-219`). Nonzero `chi` with `u=0` is correctly allowed because the phase term then vanishes. |
| Call sites and public documentation match | Pass | Every production, verification, and demo call supplies a `Params` or the exact `Model` (`verify.py:454-569,629,748`). README documents the mandatory first argument and the reason for it (`README.md:77-104`). `ResonantReturnError` remains publicly exported (`__init__.py:14-25`). |
| Omission and misuse are regression-tested | Pass | `check_return_contract` covers omission, `Params`, `Model`, one-sided `G`, invalid contexts, a quantitative failing-`G` sweep, and the valid nonzero-`chi` boundary (`verify.py:492-582`). |

## Verification performed

- `python3 -m first_mark_two_absorber.verify --verbose`: **18/18 passed** under NumPy 2.3.5; no tolerance was weakened.
- Independent signature: `(context, K, t_dark=0.0, capture_time=None, delta=0.0, u=0.0)`.
- Independent probes confirmed:
  - omitted context: `TypeError`;
  - legacy optional `params=` shape: `TypeError`;
  - nonzero `G_A` via `Params`: `ResonantReturnError`;
  - nonzero `G_B` via `Model`: `ResonantReturnError`;
  - invalid context object: explanatory `TypeError`;
  - valid `Params` and valid `Model`: three-segment schedules with `K,0,-K` and zero detuning/reference controls.

The helper necessarily validates the context the caller supplies; as documented, callers must pass the context actually used for evolution. Re-pairing the returned schedule with a different model would be an explicit contract violation, not an omission bypass in this API.

No code was edited during this review.
