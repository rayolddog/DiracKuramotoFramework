---
title: "Independent review: deterministic Adler controls"
kind: review
---

# Independent review: deterministic Adler controls

## Review target

Review the implementation produced for [the deterministic and analytic ticket](..):

`~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`

## Required lenses

1. Mathematical correctness of the Adler sign convention, fixed points, stability, local relaxation, and phase-slip calibrations.
2. Correct construction of the raised-cosine pulse, instantaneous eligibility boundary, entry/exit times, and moving stable phase.
3. Whether the near-boundary lag/run-out test genuinely demonstrates admitted-but-unlocked behavior rather than encoding its conclusion.
4. Correct normalization and convergence of the flat-spectrum relaxation-rate sum.
5. Structural isolation of analytic coupling-squared arithmetic from deterministic dynamics.
6. Test strength: identify false implementations that could still pass, brittle tolerances, circular tests, hidden post-selection, NaN vulnerabilities, or untested boundary cases.
7. Scope and documentation honesty: no implied Born outcome, commitment, exclusivity, stochastic bath, or energy-routing claim.
8. Repository hygiene and absence of changes outside the new package.

## Review output

Prioritize actionable findings by severity with file and line references. Re-run the suite and add independent probes where needed. Do not edit code. A clean review must say explicitly that no actionable finding remains and distinguish that from scientific validation of the later Born-selection hypothesis.

## Verdict

**Changes requested.** The implemented Adler sign convention, pulse formula, crossing formula, and present finite-grid values are numerically correct, and all 19 registered checks pass. The verification suite nevertheless has two material circularity holes: it can certify a non-Hann pulse as a raised cosine, and it can certify a factor-of-two analytic normalization error. The near-edge evidence is real but its causal control and documentation need tightening. Public input validation also permits silent invalid runs.

This verdict concerns only the deterministic/analytic control package. It is not scientific validation of stochastic selection, a commitment rule, channel competition, Born frequencies, exclusivity, or energy routing.

## Findings

### High — Pulse tests can certify a different envelope as the required raised cosine

**Where:** `adler_born_two_channel/verify.py:445-502`, `verify.py:505-567`, `verify.py:570-735`; implementation under test at `model.py:165-181` and `model.py:246-263`.

The envelope check pins endpoints, peak, symmetry, bounds, area, and unimodality, but never compares interior samples with an independent Hann formula. The entry/exit check then uses `RaisedCosinePulse.eligibility_window()` as the prediction and `RaisedCosinePulse.coupling()` as the observed source, so a wrong envelope and its matching inverse crossing formula validate each other.

Independent mutation probe: replacing the Hann envelope with

`E(u) = (1-u^2)^p`, `|u| < 1`, with `p = 2.381750264764574` chosen so its area is also exactly one-half, and replacing the crossing inverse consistently, left all five pulse-facing checks passing: envelope, entry/exit, finite-time lag, duration monotonicity, and adiabatic limit. This alternative differs from the Hann by `3.996e-3` at quarter support and therefore violates the declared pulse requirement.

**Action:** add off-grid interior comparisons against a formula written independently in `verify.py`, e.g. `0.5 * (1 + cos(2*pi*(t-center)/duration))`, including both edges and both sides of the peak. For entry/exit, compare the sampled transition against either an independent bisection of that literal formula or the independent identity `half_width = T*acos(sqrt(|Delta|/K_peak))/pi`; do not obtain both sides of the comparison from `RaisedCosinePulse` methods.

### High — The analytic normalization oracle shares the implementation constant, so a common factor error passes

**Where:** `adler_born_two_channel/analytic.py:69-70`, `analytic.py:219-243`, `verify.py:757-810`, `verify.py:813-875`.

`refinement_study()` computes its error relative to the module's own `SEMICIRCLE_CONSTANT`, and `check_flux_convergence()` trusts that reported error. The exponent check cannot catch a constant factor. Consequently the suite establishes quadratic shape and self-consistency, but not the claimed normalization `pi/2` independently.

Independent mutation probe: multiplying `tongue_rate_sum()` by 2 and changing `SEMICIRCLE_CONSTANT` from `pi/2` to `pi` left both “flat-grid rate sum converges to (pi/2) * coupling^2” and “fitted analytic exponent approaches two” passing with their original residuals. The printed detail still said `pi/2`.

The checked implementation itself is correct: a separate quadrature probe against the literal `0.5*pi*K^2` found the expected convergence (worst relative error `8.75e-4` across deliberately mixed coarse/fine grids and couplings), but the suite cannot protect that result against regression.

**Action:** make the verifier own an independent oracle using `math.pi / 2`, assert `SEMICIRCLE_CONSTANT == math.pi / 2`, and compare `tongue_rate_flux(K, grid)` directly with `0.5*pi*K*K` at predeclared `K` and refinement levels. Retain the exponent and support checks as separate shape/convergence checks.

### Medium — The near-edge result is genuine, but the test does not prove finite-time causation and the README overclassifies trajectories

**Where:** `adler_born_two_channel/verify.py:570-640`; `README.md:104-116`, `README.md:230-245`.

The test runs only one pulse duration and labels failure to ever enter a `0.05`-rad band as “run-out.” A broken near-edge response could produce the same observation. It also counts lucky clocks already within the band at the first eligible sample as having reached lock; the current 16-phase probe has a `0.0625` first-sample coincidence fraction at `Delta/K = 0.98` and `0.995`. The README's statement that an order-one-or-smaller e-fold budget means a clock “cannot converge no matter where it started” contradicts both those lucky starts and the test's own warning at `verify.py:575-580`. Likewise, only the clocks that never reach the band are `lock-failed`; clocks that enter it may later be dwell-failed or commit once that stage exists.

An independent paired-duration probe supports the intended mechanism and supplies the missing causal control: with identical 16 release phases, the ever-in-band fraction rose from `0.3125 -> 0.75 -> 1.0` at `Delta/K=0.98` and from `0.1875 -> 0.4375 -> 0.875` at `Delta/K=0.995` as `T=40 -> 160 -> 640`.

**Action:** codify that same-phase duration recovery (plus time-step refinement), distinguish “already in band at first eligible sample,” “entered later,” and “never entered,” and state the finite-budget result probabilistically rather than “no matter where it started.” Reserve `lock-failed` for never-in-band clocks until the dwell state machine can classify the rest.

### Medium — Invalid numeric controls are accepted or fail accidentally instead of being rejected at the boundary

**Where:** `adler_born_two_channel/model.py:194-196`, `model.py:230-234`, `simulate.py:106-124`.

The constructors reject negative peaks but accept `NaN` peaks because `NaN < 0` is false. More seriously, `integrate(..., dt=-0.1)` is silently accepted: `max(1, round(span/dt))` collapses it to one forward step and reports an effective positive `dt=1.0`. `dt=0` and `store_every=0` fail later with incidental `ZeroDivisionError`s rather than clear validation errors. A `NaN` pulse peak then appears merely ineligible everywhere, which can be mistaken for a physical no-admission result.

**Action:** require finite, non-negative peaks; finite centers/detunings/initial phases; finite positive `dt` and duration; and integer `store_every >= 1`. Add explicit rejection checks for `NaN`, infinities, zero, and negative values.

## Checks and independent probes

- `python3 -m adler_born_two_channel.verify`: **19/19 pass** under Python 3.12.6 / NumPy 2.3.5.
- `python3 -m adler_born_two_channel.verify --verbose`: **19/19 pass**.
- `python3 adler_born_two_channel/verify.py`: **19/19 pass**.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: exits **1** as required.
- Independent sign probe over `K={0.4,1.3,3.0}` and signed `Delta/K` through `+-0.99`: fixed-point drift residual `0`; finite-difference Jacobian agrees with `-sqrt(K^2-Delta^2)` to `2.32e-10`.
- Independent Hann interior probe: maximum formula residual `1.11e-16`; independent crossing identity residual `8.88e-15`.
- Independent near-edge duration recovery: longer pulses recover the same release phases as reported above.
- Isolation inspection: `model.py` and `simulate.py` contain no analytic import/call and no coupling-squared arithmetic. The package source contains no reference to `first_mark_two_absorber/` or manuscript paths. The repository was already broadly dirty and both packages are untracked, so repository-wide authorship/absence of unrelated changes cannot be established from the current Git baseline alone.

## Closure review — 2026-08-26

### Closure verdict

**Open: two narrower actionable findings remain.** The pulse oracle, analytic normalization oracle, and causal same-phase duration recovery now close the substantive mathematical/test-circularity findings. The headline near-edge recovery result is robust. The sampled already/later split is honestly caveated in the README, but the code still assigns it a stronger physical meaning than its sampling permits. Numeric validation now rejects the originally demonstrated NaN peaks and invalid integration controls, but it is not yet complete at all public boundaries claimed by the fixup ticket.

This remains a deterministic/analytic software verdict only, not validation of Born selection or any later stochastic claim.

### Closed — Wrong-but-self-consistent pulse mutation is now rejected

**Relevant code:** `adler_born_two_channel/verify.py:513-750`.

An independent runtime mutation replaced the Hann kernel with the same area-matched alternative used in the original review and replaced `eligibility_window()` with that alternative's consistent inverse. The old coarse envelope and entry/exit checks still passed, as expected, while the new independent interior oracle failed with residual `7.21e-3` and the independent crossing oracle failed with residual `1.04e-1`. This closes the pulse circularity finding.

### Closed — Shared factor-two analytic normalization mutation is now rejected

**Relevant code:** `adler_born_two_channel/verify.py:1148-1215`.

An independent runtime mutation doubled `tongue_rate_sum()` and changed `SEMICIRCLE_CONSTANT` from `pi/2` to `pi`. The new normalization oracle failed with residual `1.000027`; the exponent check still passed, confirming shape and normalization remain distinct. The direct convergence check also now fails this mutation. This closes the normalization finding.

### Closed in substance — Same-phase long-pulse recovery establishes finite-time causation

**Relevant code:** `adler_born_two_channel/verify.py:930-1024`; `README.md:309-325`.

The new paired control reuses identical phases and shows ever-in-band recovery as `T=40 -> 160 -> 640`: `0.3125 -> 0.75 -> 1.0` at `Delta/K=0.98` and `0.1875 -> 0.4375 -> 0.875` at `Delta/K=0.995`. The totals are unchanged across `dt=0.008/0.004/0.002`. An independent rerun reproduced those totals. The README now uses probabilistic exposure language and reserves `lock-failed` for never-in-band trajectories. The original causal/documentation finding is closed apart from the category-label precision below.

### Medium — “Already in band” is still a sampled, semantically ambiguous category

**Where:** `adler_born_two_channel/verify.py:903-927`, `verify.py:952-1023`; `README.md:281-307`.

The README candidly says the already/later boundary is not robust at the single-clock level, which adequately scopes the limitation for the **ever-in-band recovery total**. It does not make the stronger statements in `_band_categories()` and the check output correct: a clock found in band at the first *stored eligible sample* need not have been in band at the continuous eligibility boundary. It may have entered during the interval between the exact crossing and that stored sample, especially in the main recovery run where `dt=0.005` and `store_every=4` make stored samples `0.02` apart.

Independent exact-entry probe: integrating to the analytic entry time and comparing with the limiting target `+pi/2` gives `0/16` already-in-band clocks at `Delta/K=0.90, T=40`, while the main sampled recovery output reports `1/16`. The README reports the same one-clock instability across step sizes. Therefore wording such as “did not synchronise” and “a lucky release phase, not a synchronisation” is not established for every member of the sampled category.

**Action:** either classify at the exact analytic entry time (with interpolation/error bracketing) or rename the first category to an explicitly ambiguous observation such as “in band at first stored eligible sample.” In the latter case, remove the definite no-synchronisation interpretation. The causal recovery conclusion may continue to use the robust ever/never total.

### Medium — Numeric validation is incomplete at public pulse/dynamics boundaries

**Where:** `adler_born_two_channel/model.py:85-112`, `model.py:143-176`, `model.py:220-246`, `model.py:259-266`, `model.py:297-310`; coverage at `verify.py:1541-1686`.

The original examples are fixed: NaN/inf/negative peaks, zero/negative/non-finite duration or `dt`, non-finite integration detunings/phases/times, and invalid storage cadence now fail clearly. However public methods bypass the new validators:

- `RaisedCosinePulse(1, 2).envelope(NaN)` returns `0.0`, and `.coupling(+inf)` returns `0.0` (with the former also emitting a runtime warning), turning an invalid time into a plausible off-support physical value.
- `is_eligible(NaN, 0)` returns `False`, and `stable_phase(1, NaN)` returns `NaN`, despite the fixup ticket's public-boundary detuning/coupling requirement.
- `RaisedCosinePulse("1", "2", "3")` passes `__post_init__` because `require_finite()` converts locally, but the frozen dataclass keeps the strings and later fails in `support()` with an incidental `TypeError`. Boolean physical parameters are also accepted.

**Action:** define the intended public validation boundary explicitly and enforce it consistently. At minimum, validate time inputs in public `envelope()`/`coupling()` methods and either reject non-real convertible values (including booleans/strings) or write the normalized floats back with `object.__setattr__` in the frozen dataclasses. If low-level vectorized primitives intentionally propagate NaN, narrow the ticket/README claim and test contract rather than saying all public boundaries reject it.

### Closure checks

- `python3 -m adler_born_two_channel.verify`: **24/24 pass** under Python 3.12.6 / NumPy 2.3.5.
- `python3 -m adler_born_two_channel.verify --verbose`: **24/24 pass**.
- `python3 adler_born_two_channel/verify.py`: **24/24 pass**.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: exits **1**.
- Independent pulse and normalization mutations fail the new oracles as described above.
- Independent exact-entry/category and paired-duration probes reproduce the robust ever/never recovery while exposing the sampled already/later ambiguity.
- No code was edited during closure review; only this review artifact was updated.

## Final closure re-review — fixup 2 — 2026-08-26

### Final verdict

**Open: one validation finding remains.** Continuous-entry classification is now correct, independently step-stable, and stable to dead-margin changes when the physical phase at pulse support is held fixed. The review's exact invalid-input examples are fixed. However, the claimed exhaustive public numerical contract still has untested and behaviorally significant gaps, including invalid coupling signs and diagnostic inputs that are silently coerced or filtered.

The pulse and normalization oracle findings remain closed. This is still only a deterministic/analytic software verdict; it does not validate a stochastic Born-selection mechanism.

### Closed — Classification is evaluated at the continuous analytic entry

**Relevant code:** `adler_born_two_channel/model.py:213-227`, `simulate.py:190-221`, `verify.py:903-1067`; documentation at `README.md:327-355`.

The implementation now propagates directly to the analytic tongue-entry time and compares against the limiting boundary phase `sign(Delta)*pi/2`. It no longer assigns physical meaning to the first stored eligible sample. The check reproduces the review's discriminating case: at `Delta/K=0.90, T=40`, sampled classification reports `1/16` while exact entry correctly reports `0/16`.

Independent verification with SciPy DOP853 and a separately transcribed Hann envelope found the package entry phases within `1.63e-10` rad across the tested near-edge detunings. With the phase at pulse support held fixed and the earlier free drift compensated, margins `0, 0.5, 2, 5` gave identical entry counts at every detuning; phase differences across margins were at most `1.57e-10` rad. This is the correct margin control: changing the margin without compensating the release phase changes the physical initial condition rather than testing numerical stability.

The package's own `dt=0.008/0.004/0.002` classification is stable, agrees with a `dt=0.000125` reference to `1.52e-10` rad, and has a minimum `5.29e-4`-rad margin to the lock-band boundary. The earlier sampled-category finding is closed.

### Closed for the review's exact examples — NaN times, strings, booleans, and low-level predicates now reject

**Relevant code:** `adler_born_two_channel/validation.py:51-140`, `model.py:122-247`, `model.py:294-416`; coverage at `verify.py:1866-2184`.

Independent probes confirm all previously reported cases now fail at the boundary with named errors: pulse `envelope(NaN)`, pulse `coupling(+inf)`, stationary `coupling(NaN)`, string-valued pulse construction, boolean peak construction, `is_eligible(NaN, 0)`, and `stable_phase(1, NaN)`. Frozen dataclasses store normalized values rather than retaining merely convertible input.

### Medium — The “whole exported surface” validation claim is not yet true

**Where:** `adler_born_two_channel/model.py:165-247`, `analytic.py:96-147`, `analytic.py:194-238`, `analytic.py:261-291`, `simulate.py:107-118`, `simulate.py:260-311`, `verify.py:1866-2184`; public claim at `README.md:216-245`.

The 33-row table is exhaustive only at the level “each module-level name in `__all__` appears once.” It is not exhaustive over each callable's argument domains or the public methods of exported dataclasses. Independent probes found several invalid values still accepted silently:

- Negative physical coupling is accepted by `model.is_eligible`, `model.stable_phase`, `model.adler_drift`, `analytic.eligible_mask`, `analytic.local_relaxation_rate`, `tongue_rate_sum`, and `tongue_rate_flux`. Most return a plausible `False`, `NaN`, or `0.0` instead of rejecting the invalid sign. `efolds_available([0,1], [-1,-1], 0.5)` is worse: because it squares the coupling, it returns the positive physical-looking budget `0.8660254`. `refinement_study([-1,1], ...)` accepts the negative sweep value. This contradicts fixup-2's explicit invalid-sign/range requirement and the package's nonnegative coupling convention.
- `fit_log_log_exponent([1,-2,3], [1,4,9])` silently drops the negative coupling and returns approximately `2.0`. Its documented domain filter does not satisfy a strict public-input contract and can hide post-selection.
- `measured_eligibility_window` coerces strings and arbitrary numerics to boolean: `['False','True','False']` becomes all true and reports `(0.0, 2.0)`; `[0,2,0]` is also accepted. A boolean predicate should require a boolean array.
- Public methods omitted from the export-name table still bypass validation: `Trajectory.index_at(NaN)` and `index_at(+inf)` both return index `0`, and public steppers accept a callable that returns `NaN` and return `NaN` themselves.

**Action:** validate physical coupling as nonnegative wherever the public API treats it as a coupling; reject nonpositive log-fit inputs rather than silently dropping them (or explicitly return a structured mask that makes exclusion visible); require boolean dtype for eligibility flags; and extend completeness beyond module-level `__all__` names to the public numerical methods/callback results actually exposed by exported classes and wrappers.

### Assessment — The non-finite deviation carve-out is legitimate only for NaN-as-missing

**Where:** `adler_born_two_channel/simulate.py:260-287`.

Allowing `NaN` in `deviation` is justified: `Trajectory.tracking_error()` deliberately emits NaN where no stable target exists, and a relaxation fit over the finite eligible band must ignore those structurally missing samples. That does not justify accepting every non-finite or coercible value. The current implementation also silently filters `+/-inf`, accepts numeric strings, and accepts boolean arrays. Independent probes showed a single `+inf` is discarded and still returns the same fitted rate, while an array of numeric strings is coerced and fitted. Infinity can indicate numerical blow-up, and strings/booleans are wrong-kind inputs under the stated contract.

**Action:** preserve the NaN carve-out explicitly, but reject infinities and non-real/string/boolean deviation arrays before applying the finite-band mask. A masked array or an explicit allowed-NaN validator would make the distinction durable.

### Final re-review checks

- `python3 -m adler_born_two_channel.verify`: **26/26 pass** under Python 3.12.6 / NumPy 2.3.5.
- `python3 -m adler_born_two_channel.verify --verbose`: **26/26 pass**.
- `python3 adler_born_two_channel/verify.py`: **26/26 pass**.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: exits **1**.
- The suite reports 33 exported callables/dataclasses and 108 invalid calls, but the independent probes above demonstrate why name-level table completeness is not exhaustive domain coverage.
- No code was edited; only this review artifact was appended.

## Final binary closure review — fixup 3 — 2026-08-26

### Verdict

**OPEN: one concrete current validation defect remains.** Fixup 3 closes all 19 independently reported behaviors: negative couplings now reject in the nine model/analytic calls previously identified; the log-log fit rejects rather than filters a negative sweep entry; eligibility flags require boolean dtype; non-finite trajectory queries reject; both public steppers reject non-finite callback output; and measured relaxation accepts NaN alone while rejecting infinity, strings, and booleans. However, the exported `Trajectory` dataclass itself still accepts a negative physical coupling history and converts it into plausible no-admission diagnostics.

This is a software-contract verdict for the deterministic/analytic package only. It is not scientific validation of stochastic selection, commitment, channel competition, or Born frequencies.

### Medium — `Trajectory` accepts negative coupling while the expanded completeness check reports full domain coverage

**Where:** `adler_born_two_channel/simulate.py:61-72`, `simulate.py:88-106`; validation table at `verify.py:2268-2297`; completeness logic and claim at `verify.py:2440-2475`.

`Trajectory.__post_init__()` validates `coupling` with `require_finite_array`, not `require_nonnegative_array`. An independent public-constructor probe with `coupling=np.array([-1.0, -1.0])` succeeds; `trajectory.eligible` then returns `[[False], [False]]` and `trajectory.stable` returns `[[NaN], [NaN]]`. Thus an invalid coupling sign is silently reinterpreted as a physically plausible trajectory in which no stable target exists—the same failure mode that motivated strict coupling validation elsewhere.

The new completeness machinery correctly expands name coverage to 56 module-level callables, dataclasses, methods, and properties, and checks that all 112 signature parameters appear in at least one invalid probe or exemption. It does not establish completeness over each meaningful domain: probes are reduced to a set of parameter names at `verify.py:2452`, so the `Trajectory(coupling=...)` length-mismatch probe marks the whole coupling parameter covered and the negative-sign domain escapes. The check consequently passes and prints that negative couplings and every parameter are covered even while the public constructor above accepts one. This is a demonstrated current behavior, not a hypothetical future taxonomy concern.

**Action:** validate `Trajectory.coupling` with the package's nonnegative-array boundary and add a same-shape negative-coupling constructor probe. Amend the completeness wording or representation so a shape probe alone is not described as covering the sign domain.

### Closed behaviors and rerun evidence

- `python3 -m adler_born_two_channel.verify`: **26/26 pass** under Python 3.12.6 / NumPy 2.3.5.
- `python3 -m adler_born_two_channel.verify --verbose`: **26/26 pass**.
- `python3 adler_born_two_channel/verify.py`: **26/26 pass**.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: exits **1** and prints the deliberate failure.
- All **19/19** independent probes from the prior finding now reject with the intended `ValueError`/`TypeError`: nine negative model/analytic coupling calls, one no-filter log-fit call, two non-boolean eligibility arrays, two non-finite trajectory queries, two non-finite stepper callbacks, and three forbidden deviation arrays.
- Positive controls still succeed: zero coupling retains its defined behavior, a valid quadratic log fit returns exponent 2, boolean eligibility produces `(0.5, 1.5)`, finite trajectory queries and callbacks work, and a relaxation trace containing the documented NaN missing-target sentinel fits rate `0.999999999999999` from 16 finite in-band samples.
- The NaN-only deviation carve-out is legitimate because `Trajectory.tracking_error()` deliberately emits NaN where no stable target exists; rejecting infinity and wrong-kind arrays keeps missing data distinct from numerical blow-up or coercion.
- No code was edited during this re-review; only this review artifact was updated.

## Final closure review — fixup 4 — 2026-08-26

### Verdict

**CLOSED. No actionable finding remains.** The final narrow fix rejects negative coupling histories at the exported `Trajectory` constructor, preserves valid zero and nonnegative histories, and accurately narrows the verification guarantee from generic value-domain completeness to public-surface and declared per-parameter probe coverage.

This closes the deterministic/analytic software review only. It is not scientific validation of stochastic selection, commitment, channel competition, Born frequencies, exclusivity, or energy routing.

### Independent probes

- A same-shape all-negative history `[-1.0, -1.0, -1.0]` now raises `ValueError` naming `coupling`, reporting all three negative entries.
- A mixed history `[1.0, -1e-12, 1.0]` now raises `ValueError` naming the single negative entry, so rejection is not limited to all-negative arrays or a coarse threshold.
- An all-zero history is accepted and retains the defined boundary behavior: eligibility is false and the stable target is NaN at every sample.
- A mixed zero/positive history `[0.0, 0.5, 1.0]` is accepted unchanged; for detuning `0.5`, eligibility is `[False, False, True]` and the final stable phase is `pi/6`, confirming the validator did not become reject-everything and preserves the strict tongue boundary.

### Completeness wording assessment

`simulate.py:73-80` now applies the shared `require_nonnegative_array` validator to the stored coupling history. `verify.py:2313-2336` retains the structural length-mismatch probe and adds direct all-negative and single-negative same-shape probes.

The README and verifier now state the actual mechanical guarantee: all 56 exported callables/dataclasses/methods/properties are represented; all 112 signature parameters have a declared invalid probe or visible exemption; and 159 declared invalid calls reject with their expected exception types. Both explicitly say this is parameter coverage, not automatically derived value-class coverage, and use the escaped `Trajectory.coupling` sign case as the concrete limitation. That wording matches the implementation at `verify.py:2497-2544` and no longer claims that one probe for a parameter exhausts every way its values can be invalid.

### Rerun evidence

- `python3 -m adler_born_two_channel.verify`: **26/26 pass** under Python 3.12.6 / NumPy 2.3.5.
- `python3 -m adler_born_two_channel.verify --verbose`: **26/26 pass**.
- `python3 adler_born_two_channel/verify.py`: **26/26 pass**.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: exits **1** and prints the deliberate failure, as required.
- No code was edited during this closure review; only this review artifact was appended.
