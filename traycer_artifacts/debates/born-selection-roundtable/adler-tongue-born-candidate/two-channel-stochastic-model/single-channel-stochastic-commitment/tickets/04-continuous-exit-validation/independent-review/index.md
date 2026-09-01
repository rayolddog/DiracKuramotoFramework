---
title: "Independent review — Ticket 04 continuous exit validation"
kind: review
---

# Strict verdict: OPEN

The stationary operator, absorbing data, edge orientation, moderate-time constant-drift series, straight-boundary bridge formula, reset-only replay direction, physical-noise pairing, raw-process isolation, and non-claims are substantially correct. The canonical verifier passes **84/84**.

The ticket is nevertheless open. Accepted public inputs can make the alleged continuum oracle return negative survival and exit probabilities above one; the frozen-budget gate accepts two-level, non-halving, and systematically worsening ladders; the moving-band pass omits the required survival gate and has no dependence-aware uncertainty calculation; the audit key is not a unique address across refinement levels; and the canonical verifier peaks at **4.65 GB resident memory**. These are present code and evidence defects, not later-production limitations.

## Blocker — the frozen comparison accepts ladders that violate the frozen scientific contract

`killed_diffusion.compare_refinement` checks only distinct timesteps, a caller-controlled minimum level count, finest-level caps, and adjacent absolute-error growth larger than `noise_floor` (`killed_diffusion.py:926-1031`). Neither the required level count nor the timestep schedule is part of `FrozenBudgets.canonical` or its digest (`killed_diffusion.py:709-778`). The noise-floor rule also contradicts the execution note's requirement that an allowed upward fluctuation must then fall or be statistically unresolved.

Independent reproductions, all accepted as `pass`:

```text
two-level override: pass
    compare_refinement(..., minimum_levels=2)

non-halving: pass
    timesteps = 0.040, 0.039, 0.038
    errors    = 0.300, 0.200, 0.100

systematic growth: pass
    timesteps = 0.040, 0.020, 0.010
    errors    = 0.010, 0.020, 0.030
    noise_floor = 0.011, absolute cap = 0.05
```

The last ladder grows at both refinements and receives no reason. Thus `noise_floor` is currently permission for systematic growth in increments just under the floor, not only a predeclared adjacent-level Monte Carlo allowance. There is no sample size, standard error, covariance, master-trial identifier, or confidence interval in `RefinementLevel`, so `compare_refinement` cannot decide that a change is statistically unresolved.

Changing `absolute`, `relative`, `noise_floor`, `require_decrease`, or `observable` does change the budget digest; that part is correct. It is not enough because two other load-bearing thresholds — the minimum number of levels and the actual refinement schedule — remain mutable outside the digest.

Required correction:

- Freeze and hash the minimum level count and exact timestep/refinement schedule, or remove the caller override and enforce the ticket's three-level halving contract in a higher frozen manifest that the verdict validates.
- Reject systematic growth even when each adjacent increment is below the floor. A floor can excuse one statistically unresolved reversal, not a monotonically worsening ladder.
- Carry the predeclared sampling/dependence design and an uncertainty estimate sufficient to justify “statistically unresolved”; a bare scalar called `noise_floor` is not that evidence.
- Add direct mutations for two-level override, non-halving schedules, and repeated sub-floor growth.

## Blocker — the killed-diffusion oracle accepts a time grid that returns non-probabilities

The backward generator signs are correct: for `f d/dx + D d2/dx2`, the lower, diagonal, and upper bands are `D/dx^2 - f/(2dx)`, `-2D/dx^2`, and `D/dx^2 + f/(2dx)` (`killed_diffusion.py:560-567`). The survival boundaries are homogeneous; the upper-exit CDF uses lower datum zero and upper datum one with the correct upper source (`killed_diffusion.py:578-624`). Rannacher startup is implemented as two implicit half-steps for the first four output steps, followed by Crank–Nicolson (`killed_diffusion.py:585-622`).

Only the spatial cell-Peclet restriction is enforced (`killed_diffusion.py:569-577`). There is no time-step positivity/maximum-principle restriction and `SurvivalSolution` does not reject probabilities outside `[0,1]`. A direct accepted case is:

```text
BandGeometry(lower=-1, upper=1, diffusion=0.001,
             coupling=0, detuning=0.05)
solve_survival(..., horizon=100, space_steps=80, time_steps=5)

cell Peclet = 0.625  (< 1, so accepted)
min survival = -0.006268159488942198
max upper_exit = 1.0062073263634468
closure residual = 1.11e-16
```

Closure does not protect against this: `lower_exit` is defined as the complement, so the three fields can sum to one while individual fields are non-probabilities. A sufficient Crank–Nicolson positivity condition for this central generator is visible from the right matrix's diagonal, `1 - dt*D/dx^2 >= 0`; alternatively the API can validate the computed fields and refuse a grid whose propagation violates the maximum principle.

The upper/lower sign itself passed an independent infinite-horizon calculation. For constant drift `mu = +/-0.35`, `D=0.1`, band `(0,1)`, and starts `0.2,0.5,0.8`, the numerical upper-exit probability at `t=10` agreed within `3.14e-5` with

```text
(1 - exp(-mu*x/D)) / (1 - exp(-mu/D)).
```

So the required correction is a time-grid/domain guard and probability validation, not a sign reversal.

## Blocker — the claimed moving-band convergence pass is only a reference-budget mechanism smoke test

The audit ladder budgets only:

- final commitment-probability shift;
- mean commit-time shift conditional on the audited path still committing; and
- mean added resets (`verify.py:14625-14630`).

There is **no survival observable at any comparison time**, although the ticket execution decision says survival remains gated when added-reset monotonicity is waived. There is also no commitment-time quantile, shared-prefix survival path, or per-cell/mismatch gate. The 15-cell matrix is structurally crossed over position/sign/noise and both pulse sides have positive interval counts, but its verifier contribution is one deterministic initial phase, one physical trial, and one audit replication per cell and level (`verify.py:14876-14895`); it establishes reachability of the axes, not accuracy across those regimes.

The headline ladder contains 24 master trial IDs, three detunings, and three auxiliary replications. The three detunings all use `clock=0`, so physical kicks and audit uniforms are correlated across them; the replicates share each physical path. No uncertainty calculation accounts for either dependence. The observed values are:

| Timestep | Commit-probability shift | Conditional mean commit-time shift | Mean added resets |
| --- | --- | --- | --- |
| 0.032 | 0.0000 | 0.03398 | 0.4352 |
| 0.016 | 0.01389 | 0.03674 | 0.6713 |
| 0.008 | 0.0000 | 0.02568 | 0.9028 |

A cluster bootstrap over the 24 shared master trial IDs gave standard deviations for the conditional mean time shift of approximately `0.0075`, `0.0204`, and `0.0161`, with finest-level 95% interval about `[0.0061, 0.0639]`. Those uncertainties are not produced, frozen, or read by the implementation. The frozen time-shift floor is simply `0.005`.

The README is honest that these are reference budgets rather than production budgets (`README.md:2076-2084`), and `require_decrease=false` for added resets does not skip the two convergent gates that are actually present. But the verifier check is titled “its dwell effects shrink under refinement,” the README says the moving-band audit “costs the dwell a shrinking amount,” and the Ticket 04 acceptance gate requires survival plus statistically resolved refinement. The current evidence supports only: reset-only replay works on this small reference sample and the budget mechanism can emit `pass`. It does not support scientific convergence of the moving-band audit.

Required correction:

- Add frozen survival differences at declared times and a commitment-time distribution/quantile observable; retain pathwise prefix information needed to compute them.
- Define the master-trial clustering and the auxiliary-replication contribution, export their uncertainty, and make the pass rule consume it.
- Increase or justify the physical and auxiliary sample sizes before calling an increase “statistically unresolved.”
- Report the matrix per regime (including near-edge sign asymmetry and both pulse sides), not merely interval reachability.
- Keep the added-reset count as a nonconvergent diagnostic. That waiver is scientifically sound only after the independent convergent gates above exist and pass.

## High — the verifier materializes multi-gigabyte Monte Carlo cubes

The S3 endpoint check materializes `6000 x 2048` float64 fine kicks (`verify.py:13723-13733`), about **98.3 MB**, then allocates coarse arrays beside it. More seriously, `_bridge_samples` materializes `samples x substeps` arrays for 40,000 bridges at 2,400 substeps: increments, cumulative walk, bridge, path, and comparisons (`verify.py:14246-14264`).

Measured with the canonical suite:

```text
/usr/bin/time -l python3 -m adler_born_two_channel.verify >/dev/null
53.31 s real
4,653,875,200 bytes maximum resident set size
3,890,761,688 bytes peak memory footprint
```

This is a cube-scale verifier even though the plan requires bounded streaming and the handoff asks for memory implications. It can fail on an otherwise valid development machine for RAM rather than science. No package-scoped result files were written; the defect is memory, not disk output.

Required correction: batch both the endpoint walkers and direct bridge simulations, retaining online hit counts and small live state only. Add a measured peak-memory assertion or benchmark result to the handoff.

## Medium — one audit key addresses different physical intervals at different refinement levels

`AuditUniformStream.key` claims to identify one finest-step/piece (`moving_band_audit.py:282-300`). In `replay_pulse`, however, `piece` is recomputed from the current segmentation order and the key contains no stride, duration, or interval endpoints (`moving_band_audit.py:1015-1018`). Coarse levels are built on the same finest mesh, so the same `(step, piece)` key is reused for a longer bridge.

Instrumentation of the declared pulsed path found:

```text
stride 1 vs 2: 73 shared audit keys; all 73 described different geometries
stride 1 vs 4: 36 shared audit keys; all 36 described different geometries

example key: step=260/piece=0/bridge
stride 1 duration = 0.008, phases = (0.7053318, 0.6758530)
stride 2 duration = 0.016, phases = (0.7067146, 0.6504672)
stride 4 duration = 0.032, phases = (0.7095118, 0.6419516)
```

The physical Brownian leaves are correct: every coarse kick is a deterministic sum of the same finest leaves, with no model/refinement key in the physical history. The collision is in the auxiliary audit address. Reusing a uniform can be a deliberate common-random-number coupling, but then the key does not uniquely or canonically name an elementary piece as documented, and the ordinal has not met the execution note's partition/refinement requirement.

Required correction: either key the actual audit interval canonically (including a stable refinement/endpoint identity), or define a hierarchical audit-uniform construction whose parent/child relationship is explicit. Add a test that equal keys imply equal physical intervals across stride, window, pulse order, and partition variants.

## Medium — the independent series can silently be an invalid short-time oracle

The constant-drift eigenfunction derivation and normalization are correct at resolved times, including nonzero drift: transforming the backward equation gives the documented tilt `k=mu/(2D)`, coefficients reduce to `4/(n*pi)` on odd modes at zero drift, and the moderate-time comparison at `mu=0.35` is genuinely separate from the Crank–Nicolson path.

The public `series_survival` API nevertheless accepts any positive term count and any nonnegative time, with no truncation/convergence estimate and no probability validation (`killed_diffusion.py:314-397`). At `band=(0,1)`, `D=0.1`, `mu=2`, `t=1e-10`, 400 terms return:

```text
x=0.0001 -> -2.1135172024876283
x=0.001  -> -15.75436848247864
x=0.01   -> 0.7055808161676396
x=0.5    -> 0.8819012804717042
```

The true survival tends to one for every fixed interior start as `t -> 0`. Even at zero drift, 400 terms give `1.1790` at `x=0.01`. Exact `t=0` is special-cased, but the short-time regime immediately beside it is not. Thus a caller can use a numerically unconverged “independent reference” and receive a plausible or impossible number without warning.

Required correction: expose and enforce a truncation-error/convergence test (for example, compare nested term counts under a declared series budget), refuse unresolved short-time evaluations, and pin boundary values to zero. Add nonzero drift, both drift signs, near-edge starts, and short-time cases.

## Medium — zero diffusion overrides certain endpoint absorption in the public bridge function

`bridge_crossing_probability` returns zero for zero diffusion before checking endpoint clearances (`moving_band_audit.py:546-551`). Therefore an endpoint exactly on or beyond an edge with `diffusion=0` returns crossing probability zero, although the plan says endpoint equality is an immediate reset and only strictly interior endpoints reach the zero-diffusion branch.

`audit_outcome` currently checks `strictly_inside` first, so the replay itself returns `primary_reset`; the defect is the exported arithmetic API and an omitted cross-case in the verifier, which tests interior/zero-diffusion and boundary/positive-diffusion separately.

Required correction: make nonpositive clearance return one before the zero-diffusion branch, or reject non-interior steps at this API. Add the combined zero-diffusion/zero-clearance and outside-clearance cases.

## Medium — the reported 0.1113 / 0.1393 “envelope” collapses units and can hide per-position reversals

`ValidationVerdict.envelope` takes one maximum absolute error across every observable (`killed_diffusion.py:879-897`). Here `0.111278` is an **exit-time quantile error in time units**, while survival and edge-exit errors are probabilities. A single absolute maximum across those units is not a numerical budget a later production uncertainty can compare meaningfully. The relative maximum `0.139293` is dimensionless, but the exported headline drops the observable and initial position that produced it.

The S3 helper also says observable names carry position indices, but `_s3_levels` uses only four shared names (`verify.py:13794-13819`). `_s3_worst_by_observable` then chooses the worst position independently at each timestep (`verify.py:13822-13843`). If the identity of the worst position changes, `compare_refinement` compares different paths as though they were one ladder and can conceal a position-specific reversal. It does not happen to change the present four ladders, but the gate is mutation-fragile.

Required correction: export per-observable, per-position envelopes with units; make each position a separate frozen observable or require every position-specific ladder to pass before taking a display maximum.

## Decisions and contracts that survived review

| Review burden | Result |
| --- | --- |
| Literal Brownian reset count | **Sound clarification.** Brownian recrossing makes a literal continuous reset count divergent. First absorption, resolved by edge, is a finite well-posed replacement. The docs consistently narrow it to the killed problem and disclose that the total is `1-S`; the edge split supplies the extra information. |
| PDE signs and absorbing data | **Correct**, subject to the missing time-grid positivity guard above. Independent eventual upper/lower hitting probabilities confirm the drift orientation. |
| Crank–Nicolson/Rannacher mechanism | **Implemented as described**, but accepted-domain stability is incomplete. |
| Constant-drift series algebra | **Correct at resolved moderate/late times and genuinely separate in code path**; unsafe short-time truncation remains open. |
| Straight moving-boundary bridge formula | **Correct.** With variance `2Dh`, the one-sided probability is `exp(-clearance_start*clearance_end/(Dh))`; the reflection-principle derivation and direct bridge simulation support the factor and signs. The capped lower-plus-upper quantity is honestly labeled a conservative union bound for the discretized bridge only. |
| Circular/contraction geometry | **Substantially correct.** Strict proximity is intersected with `-K cos(phi)<0`; the repelling branch is excluded, exact eligibility equality is unbridgeable, and ambiguous/disappearing/branch-changing geometries reset conservatively. |
| Reset ordering and pathwise subset | **Correct in the replay.** Hidden resets are applied before the endpoint observation; the shared-stopping snapshot prevents post-primary exposure from masquerading as added resets; no audited commitment is created or advanced. |
| Physical refinement pairing | **Correct.** Coarse kicks are sums of the same finest physical leaves and model/refinement labels do not rekey the physical history. The auxiliary interval identity remains open separately. |
| Audit/physical namespace separation | **Correct.** Prefixes are disjoint, and changing the audit replicate leaves the primary history unchanged. |
| Raw-process isolation | **Correct.** An independent subprocess import of `adler_born_two_channel.raw_runner` left `analytic`, `killed_diffusion`, and `moving_band_audit` absent from `sys.modules`; no oracle/predictor is reachable from the raw graph. |
| No files | **Correct for Ticket 04 execution.** The verifier uses temporary mutation fixtures but writes no result ledger/cube. Peak RAM is open as above. |
| README counts and non-claims | **Correct.** The current suite prints 84 rows and `84/84`; README states one clock, no race/population/hazard/exponent/outcome/measurement/Born claim, and labels the budgets reference-only. |
| Prior 75 rows | **Current reproducibility passes, historical byte identity is not independently provable.** The first 75 current `[PASS]` rows were byte-identical under `PYTHONHASHSEED=0` and `987654321`. No frozen prior-row byte snapshot/digest exists in the repository to compare current bytes with the Ticket 03 version; the previous review records only that its own two runs matched. |
| Born/scaling claims | **None smuggled in.** No exponent, population result, channel outcome, detector measurement, or Born-rule conclusion is computed or claimed. |

## Commands and independent evidence

| Probe | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | `84/84`, exit 0, about 59 s on Python 3.12.6 / NumPy 2.3.5 |
| Current first 75 `[PASS]` rows, `PYTHONHASHSEED=0` vs `987654321` | byte-identical |
| Raw-run import isolation subprocess | `analytic=False`, `killed_diffusion=False`, `moving_band_audit=False` |
| Constant-drift eventual edge-hit calculation | upper/lower orientation correct; max upper error `3.14e-5` |
| Accepted coarse-time PDE sweep | multiple negative-survival / `upper_exit>1` cases; exact reproduction above |
| Short-time series term sweep | out-of-range and grossly unconverged accepted outputs; exact reproduction above |
| Frozen-budget mutations | two levels, non-halving, and systematic sub-floor growth each passed |
| Audit ladder replay and 24-cluster bootstrap | values and uncertainty above; no survival gate present |
| Audit-key instrumentation | every shared key across stride 1/2 and 1/4 mapped to different interval geometry |
| `/usr/bin/time -l` canonical verifier | max RSS `4,653,875,200` bytes |

No implementation file was edited, staged, committed, or reverted. The only write made by this review is this artifact.

# Fix-up round 1 closure review — 2026-08-28

## Strict verdict: OPEN

The fix-up genuinely closes the coarse-grid probability-domain defect, the
multi-gigabyte verifier, the v1 audit-key collision, zero-diffusion boundary
precedence, and the mixed-unit/per-position aggregation bug. The canonical
suite passes **85/85**, and my independent run peaked at **629,932,032 bytes**
rather than the former 4.65 GB.

Closure is still blocked. The series convergence check has a concrete
parity-aliasing false pass; the reduced moving-band matrix is reported but is
not accuracy-gated; and the uncertainty gate can be changed by caller-supplied
standard errors that are neither paired-difference estimates nor tied to the
frozen sampling design. The changed machine-readable report also remains under
the old `v1` schema despite its own rule that changed key meaning requires a
schema version change.

## Blocker — the nested series test can agree exactly while both truncations are wrong

`series_survival` accepts `terms >= 2` and compares the `terms` partial sum with
`terms // 2` (`killed_diffusion.py:451, 478-506`). At zero drift every even
Fourier coefficient vanishes. Consequently, `terms=2` and `terms//2=1` are the
same one-mode approximation, so the declared convergence test sees an exact
zero gap even when the omitted third and higher odd modes are material.

Independent reproduction:

```text
series_survival(0, 1, 0.1, 0,
    [0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95], [0.3],
    terms=2, tolerance=1e-12)

accepted terms=2:
[0.1481334433, 0.2926193497, 0.6695849427, 0.9469361072,
 0.6695849427, 0.2926193497, 0.1481334433]

resolved terms=4000:
[0.1616564923, 0.3166771361, 0.6903665211, 0.9175463352,
 0.6903665211, 0.3166771361, 0.1616564923]

maximum error = 0.029389771996621517
nested terms=2 versus terms=1 gap = 0 exactly
```

All values happen to lie in `[0,1]`, so the probability-domain check does not
catch the false convergence. The original short-time reproduction at 400 terms
now correctly refuses, but that proves only that one example, not that the
nested criterion is sound. This leaves original finding 6 open.

Required correction: use truncations that cannot alias the series' parity
structure and add a discriminating low-term mutation. Prefer a justified tail
bound or at least two independent nested gaps whose cutoffs differ in the last
nonzero mode; do not repair only `terms=2` while retaining cancellation-based
false agreement elsewhere.

## Blocker — the moving-band `pass` does not gate the reduced regimes and does not bound its noisiest observable

The pooled ladder is materially better than the first version: it now has 40
master clusters, three independently keyed clocks, four auxiliary replications,
three paired timesteps, three frozen survival times, and a censored p20
commit-time quantile. The physical paths remain paired and the auxiliary
replications remain inside the master-trial bootstrap cluster.

My direct recomputation of the current ladder is:

| Observable | `dt=0.032` | `dt=0.016` | `dt=0.008` |
| --- | --- | --- | --- |
| commitment-probability shift | 0.00625 | 0.00417 | 0.00833 |
| survival shift at 0.45 | 0.01042 | 0.00833 | 0.00000 |
| survival shift at 0.60 | 0.01042 | 0.01042 | 0.00000 |
| survival shift at 0.80 | 0.02292 | 0.01250 | 0.01458 |
| censored p20 commit-time shift | 0.13440 | 0.11520 | 0.01120 |
| mean added resets | 0.47708 | 0.61042 | 0.98125 |

The p20 bootstrap standard errors are `0.13909, 0.12679, 0.08290`. Thus the
finest point estimate is below the frozen `0.10` reference cap, but its
two-standard-error upper uncertainty is about `0.177`, not below the cap.
`compare_refinement` applies the cap to the point estimate only
(`killed_diffusion.py:1469-1480`); uncertainty is used only to excuse an upward
refinement step (`1485-1523`). This is adequate to exercise a reference-budget
mechanism. It is not evidence that the moving-band discrepancy has been bounded
below 0.10.

The reduced matrix is a more concrete failure. `_matrix_results` computes only
commitment probability and added-reset means from **six** master trials per
cell (`verify.py:15343-15397`). `check_audit_namespace_and_matrix` then gates
only pathwise subset, presence of rising/falling intervals, and structural
coverage (`15578-15597`). It never applies a frozen cap, convergence rule, or
uncertainty estimate to any cell. My per-cell replay found:

```text
S3b/interior/strong/detuning=-0.450
commitment-probability shift, dt 0.032 -> 0.016 -> 0.008:
0.1666666667 -> 0.1666666667 -> 0.1250000000
```

The finest cell is above the pooled ladder's `0.10` reference cap, yet the
matrix check passes with residual zero. The current matrix therefore proves
axis and pulse-edge reachability and records a few point estimates; it does not
establish numerical adequacy across the 15 regimes. Its results are also kept
in a private verifier cache and only the single worst finest cell is mentioned
in the check detail, so the claimed per-regime report is not part of the
machine-readable export Ticket 07 receives.

The documentation overstates this evidence. The check calls the outcome a
`numerical validation pass` (`verify.py:15320-15335`) and the README says the
moving-band amounts “shrink under paired refinement” (`README.md:2242-2246`),
although two gated series have a finest-level reversal. The nearby statement
that these are reference rather than production budgets is honest and must be
retained; the stronger pass language is not.

The original `0.0340 -> 0.0367 -> 0.0257` time shifts and
`0.44 -> 0.67 -> 0.90` resets have been superseded by a larger experiment and
better observables. That old pass was only a mechanism smoke test. The present
run is still a **reference-budget mechanism test with useful diagnostics**, not
a production validation claim and not yet a per-regime numerical bound.

Required correction:

- freeze and gate each matrix regime, with an uncertainty calculation at a
sample size capable of resolving its cap, or explicitly narrow the matrix to
geometry/reachability and stop presenting it as accuracy evidence;
- require the uncertainty-aware finest-level bound, not only the point
estimate, when claiming an error is bounded by a cap; and
- label this result as a reference-budget mechanism test until Ticket 07's
production budget exists and passes.

## High — the frozen sampling contract does not control the uncertainty actually consumed

The schedule, ratio, level count, cluster count, replications, method text,
resample count, coverage, units, positions, caps, floors, and
`require_decrease` flags now do move the digest. Two-level and non-halving
contracts refuse, repeated sub-floor growth returns `numerical_no_result`, and
a waived reset count cannot rescue a failed convergent observable. Those parts
of original finding 1 are closed.

The remaining substitution path is the `standard_error` carried by each
caller-created `RefinementLevel`. It is accepted as any nonnegative number
(`killed_diffusion.py:1159-1201`), is not tied to the frozen method or resamples,
and only the caller's integer `clusters` field is checked against the contract
(`1462-1467`). Under the exact same frozen contract and digest:

```text
errors = 0.010, 0.040, 0.009
standard_error = 0.0 at every level  -> numerical_no_result
standard_error = 0.1 at every level  -> pass
```

No sampling record changed; only the caller-supplied uncertainty did. This is
the caller-substitution attack the frozen `SamplingDesign` was meant to close.

There is also a mismatch between the declared method and the calculation. The
contract defines coverage in standard errors of the **paired difference**
(`killed_diffusion.py:830-834`), but `compare_refinement` uses
`hypot(se_coarse, se_fine)` (`1487-1489, 1510-1513`), the independent-level
formula. `_audit_levels` bootstraps one marginal statistic at a time
(`verify.py:15192-15209`), even though the levels share physical clusters. A
direct common-resample calculation gave, for the survival-at-0.60 ladder,
marginal SEs `0.007681, 0.007681, 0`, while the paired coarse-minus-middle SE
is effectively zero because the two bootstrap statistics move identically.
The current formula therefore does not consume the paired uncertainty its own
contract names. Positive cross-level dependence generally inflates the
allowance and can turn a resolved reversal into an “unresolved” one.

The frozen probability floor is also stale: its comment still says one event
out of 72 is 0.014 (`verify.py:15167-15170`), while the implemented ladder is
40 x 3 physical histories and four auxiliary replications. The probability
lattice is no longer 1/72, yet the floor is 0.030. The bootstrap seed
`20260901` and the actual clock/observable construction also remain outside the
sampling digest.

Required correction: compute and export paired-difference bootstrap
uncertainties from the same cluster resamples, make the comparison consume
those uncertainties, and bind the estimator inputs needed to reproduce them
(including seed and observable/cell identity) to the frozen validation
manifest. At minimum, remove the unsupported 72-run floor rationale and add a
mutation where marginal standard errors are substituted under an otherwise
unchanged contract.

## Medium — the breaking report change still advertises schema v1

Original finding 8's numerical representation is fixed: S3 now has twelve
separate observable/position ladders and per-unit envelopes name the observable
and position producing each maximum (`killed_diffusion.py:1290-1348`). Ticket
07 no longer receives a scalar that mixes probabilities and times.

However, the exported report changed from the old scalar envelope to plural
unit-bearing envelopes and added position, standard-error, and cluster
semantics while `VALIDATION_SCHEMA` remains
`dk-numerical-validation/v1` (`killed_diffusion.py:167-171`). The serializer's
own contract says a change to what keys mean requires a schema version change
(`1322-1327`). A mechanical Ticket 07 reader cannot distinguish the old v1
shape from the new incompatible v1 shape by the schema tag.

Required correction: bump the validation schema and add a fixture/mutation that
an old-shape consumer refuses the new version rather than silently interpreting
new semantics under v1.

## Disposition of all eight original findings

| Original finding | Closure state | Exact closure evidence |
| --- | --- | --- |
| 1. Frozen comparison bypasses | **OPEN (partially fixed)** | Two levels, non-halving schedules, repeated growth, altered declared design, wrong units and missing positions now refuse. Caller-supplied SE substitution and marginal-versus-paired uncertainty remain open. |
| 2. Oracle returns non-probabilities | **CLOSED** | The old grid refuses at Courant 40; every returned field is range-validated. A 2,500-case randomized diffusion/advection/time-grid scan found no accepted material time oscillation; the largest accepted monotonicity defect was `1.70e-9`, confined to `~7e-10` roundoff near zero. The stricter `D dt/dx^2 <= 1` condition would reject the validated S3 grid at about 94 and is not warranted by this evidence. |
| 3. Moving-band pass is a smoke test | **OPEN (improved, not closed)** | Survival, p20 quantile, distinct clocks, cluster bootstrap, and pathwise gates exist. The finest p20 SE is 0.0829, the matrix is ungated, and one finest matrix cell is 0.125 against the pooled 0.10 cap. |
| 4. Multi-GB verifier | **CLOSED** | Independent `/usr/bin/time -l` measurement: 629,932,032 B max RSS, 181,093,480 B peak footprint, 65.20 s. Endpoint blocks and bridge batches are streamed; no hidden bridge cube was found. |
| 5. Audit-key interval collision | **CLOSED for the current replay** | v2 carries exact `float.hex` endpoints; the canonical reproduction reports zero unequal-interval collisions where v1 reproduces 265. Physical fine leaves remain common across every timestep; independent auxiliary uniforms do not rekey or redraw the physical tree. |
| 6. Unsafe series truncation | **OPEN** | The old 400-term short-time case refuses, but the zero-drift `terms=2` parity alias falsely passes with 0.02939 error. |
| 7. Zero-diffusion precedence | **CLOSED** | Public boundary and outside probes both return crossing probability exactly 1.0 before the zero-diffusion interior branch. |
| 8. Mixed units/collapsed positions | **OPEN only at the export boundary** | Per-unit, per-position gates and maxima are correct. The incompatible report still uses schema v1. |

## Other review burdens that passed

- The killed-diffusion generator signs, absorbing data, upper/lower edge
orientation, Rannacher startup, conservation identity, moderate-time
constant-drift normalization, and grid refinement remain correct.
- The moving straight-boundary bridge formula independently matches the
reflection-principle form to `6.66e-16`; its denominator is `D * duration`
under variance `2 D duration`, its signs and zero-clearance handling are
correct, and the two-edge cap is honestly limited to a conservative union
for the discretized bridge.
- Circular representatives, contraction-side exclusion, exact ties,
eligibility splits, disappearing/topology-changing bands, entry/re-entry,
and conservative-reset-before-observation ordering remain covered and
consistent with the implementation.
- Audit replay can only add shared-prefix resets; record construction refuses
created or advanced commitments, and the shared-stopping snapshot excludes
ordinary resets accumulated only after the primary run stopped.
- Audit keys are disjoint from physical noise. Distinct clock identifiers make
the three physical clocks independent, auxiliary replicate changes leave the
physical history unchanged, and all coarser physical increments are exact
left-to-right sums of the same fine leaves.
- The edge-resolved first-absorption replacement remains mathematically sound.
A literal Brownian recrossing count diverges; first absorption is finite, and
the documentation continues to narrow the claim honestly.
- A fresh subprocess importing `raw_runner` loaded none of `analytic`,
`killed_diffusion`, or `moving_band_audit`. `compileall` was clean. No result
files or sample cubes were written, and no exponent, population outcome,
measurement, detector, hazard, or Born-rule claim was found.

## Commands and exact evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, exit 0; 65.20 s; 629,932,032 B max RSS |
| Original contract reproductions | two-level and non-halving constructors refuse; `0.010,0.020,0.030` returns `numerical_no_result` |
| Caller-SE substitution | the same `0.010,0.040,0.009` ladder changes from no-result to pass when only SE changes `0 -> 0.1` |
| Original PDE reproduction | refuses before solving: advective Courant `40.0` |
| Random accepted-CN scan | no material in-range oscillation found; only roundoff-scale `<= 1.70e-9` time reversals |
| Original 400-term short-time series | refuses with nested gap `4.235641969737117` |
| New two-term series attack | accepts; max error against resolved 4000-term value `0.029389771996621517` |
| Current audit ladder and common-cluster bootstrap | values in the table above; p20 SEs `0.13909,0.12679,0.08290` |
| Reduced matrix replay | finest `interior/strong/detuning=-0.450` shift `0.125`, ungated |
| Zero-diffusion equality/outside | both return `1.0` |
| Raw import subprocess | `analytic=False`, `killed_diffusion=False`, `moving_band_audit=False` |
| `python3 -m compileall -q adler_born_two_channel` | clean |

The fix-up artifact's claim that 79 shared historical rows are byte-identical
cannot be independently reconstructed from the present untracked package: no
frozen pre-fix row snapshot or digest exists in the repository. The current
suite's 85/85 result is confirmed; historical byte identity remains an
unverifiable handoff assertion rather than closure evidence.

No implementation file was edited, staged, committed, or reverted. This
closure section is the only write made by the re-review.

# Fix-up round 2 final closure review — 2026-08-28

## Verdict: OPEN

Fix-up round 2 correctly turns the reference moving-band audit into an explicit
blocking `numerical_no_result`, and the green verifier row honestly checks that
the validation machinery emits that outcome. A numerical pass is not required
to close this implementation: Ticket 04's contract expressly permits either a
refinement result or a machine-readable no-result. The canonical check therefore
does **not** need to fail merely because the reference sample is scientifically
unresolved.

Closure nevertheless remains blocked. The constant-drift oracle accepts a
floating-point-cancelled value whose error exceeds its requested tolerance, the
paired uncertainty is not the uncertainty of the absolute-error contrast that
the comparison actually gates, the frozen dataset still has no cluster
identifiers, and the purportedly strict v2 parser can convert a no-result into
an apparent pass. The last defect is a concrete route by which a downstream
ticket can bypass the correct scientific block.

## Blocker — the series tail bound does not bound floating-point cancellation

The original `terms=2`, zero-drift parity-alias reproduction is closed in the
narrow sense: the nested gap is still exactly zero, but the new tail bound is
`0.10963522314633094`, the resolved error is
`0.029389771996621517`, and `series_survival(..., terms=2, tolerance=1e-12)` refuses.

The replacement is not a reliable tolerance contract. The derivation in
`killed_diffusion.py:427-508` bounds the exact mathematical tail only. It does
not bound roundoff in the retained partial sum, whose exponentially tilted
coefficients can be large and mutually cancelling. Reflection gives an exact,
independent invariant for this same killed diffusion,
`S_mu(x,t) = S_-mu(1-x,t)`. The public oracle violates it beyond its declared
tolerance while reporting a negligible tail:

```python
p = np.array([1e-6])
t = np.array([0.0031622776601683794])
a = series_survival(0, 1, .1,  5, p,   t, terms=400, tolerance=1e-6)[0, 0]
b = series_survival(0, 1, .1, -5, 1-p, t, terms=400, tolerance=1e-6)[0, 0]
```

This returns `a = 6.279704393818974e-05` and
`b = 7.910298882052302e-05`, a symmetry gap of
`1.630594488233328e-05`. At least one accepted answer is therefore wrong by at
least `8.15297244116664e-06`, over eight times the requested `1e-6` tolerance.
Both calls report a truncation bound of only
`5.041795014211675e-210`. The nondimensional tilt is only 25, far below the
declared maximum of 300, so this is not an irrelevant overflow-edge case.

The newly exported bound function also does not enforce its own documented
domain. Despite `killed_diffusion.py:477-478` saying that zero times return
zero, a direct call returns `inf`; it accepts an outside start and returns a
finite bound, accepts a negative time as `inf`, and accepts a two-dimensional
position array with a three-dimensional result. The higher-level
`series_survival` validates those inputs, but `series_truncation_bound` is a
public exported API and its validation coverage is incomplete.

Required correction: evaluate the tilted series in a numerically stable form,
or add a defensible roundoff/conditioning bound to the acceptance test so that
the requested tolerance covers both truncation and floating evaluation. Add
reflection probes for both drift signs, near-edge starts, and short times. Make
the public tail-bound API either enforce the survival API's position/time/shape
domain or make it private, and make its zero-time behavior agree with its
contract.

## High — signed bootstrap error is not the gated absolute-error uncertainty

`PairedSample.measured` intentionally bootstraps the signed level estimates,
while `compare_refinement` gates changes in their absolute errors. The argument
at `killed_diffusion.py:1434-1443` is invalid: the pointwise inequality
`||a|-|b|| <= |a-b|` does not establish an ordering of the two random
variables' variances or standard errors.

A two-cluster exact counterexample defeats the claimed conservatism:

```python
values = np.array([[[-2., -1., -1.]],
                   [[ 1.,  2.,  2.]]])
sample = PairedSample("probe", "", values, reference=0.0)
```

With 10,000 shared cluster resamples and seed 7, the whole-sample signed
estimates are `[-0.5, 0.5, 0.5]`, so all three reported absolute errors are
`0.5` and the implementation's signed adjacent contrast has standard error
zero. But the bootstrap distribution of the contrast the gate actually uses,
`abs(mid) - abs(coarse)`, is `{-1, 0, 1}` and has standard error
`0.699390609546963`. The field described as the paired error of the error change
can therefore be zero while that change has substantial sampling uncertainty.

Shared cluster resamples, signed estimates, seeds, resampling count, estimator,
quantile and folding order are now deterministic and digest-bound. The old
caller-supplied-SE substitution and the `0.010 -> 0.040 -> 0.009` bypass refuse.
Those are real improvements, but they do not repair this estimand mismatch.

Required correction: on each shared bootstrap resample, compute the same folded
absolute-error contrast the acceptance rule uses, and use its uncertainty; or
define and document a scientifically justified signed-estimate convergence
rule consistently from statistic through gate. Add a sign-crossing regression
like the two-cluster case above.

## High — the frozen observations still lack cluster identities

`PairedSample` has only `observable`, `position`, `values`, `baseline`, and
`reference` (`killed_diffusion.py:1317-1350`). Its digest binds array shape,
bytes, and row order, but no master-trial IDs exist to establish which physical
cluster each row represents. Consequently it cannot reject duplicated,
missing, or substituted cluster identities, nor prove that two observables or
arms use the same ordered physical clusters. For example, 24 identical cluster
rows are accepted as 24 clusters even though they can encode only one unique
trial copied 24 times. Identical numerical rows can legitimately occur for
binary observables, so the observation bytes cannot serve as identity.

Reordering values changes the digest, missing rows violate the declared count,
and baseline/value shapes must agree. Those checks close only structural
mutations, not identity substitution.

Required correction: carry explicit, nonempty, unique cluster identifiers in
each paired sample; hash them; require values and baseline to share the same
ordered IDs; and require all samples governed by one dataset/sampling contract
to use the intended ordered physical cluster set. Add duplicate, missing,
reordered, and cross-observable substitution tests.

## Blocker — schema v2 is tagged but not strictly parsed

The version bump is present, v1/missing tags and the old scalar `envelope` are
refused, and level rows must contain the new position/unit/paired-error fields.
However, `parse_validation_report` at `killed_diffusion.py:1750-1802` validates
only the top-level key presence, tag, verdict membership, and presence of level
keys. It accepts each of these mutations of an otherwise valid v2 payload:

- `verdict="numerical_no_result"` together with `passed=True`;
- `verdict="pass"`, `passed=True`, and nonempty blocking `reasons`;
- an empty `dataset_digest`;
- a level with numeric `position`, `unit="furlongs"`, negative timestep,
`measured=NaN`, negative errors, and one cluster.

The first mutation is the direct downstream bypass: Ticket 07 can call the
advertised parser and then trust `passed`, advancing a scientifically blocked
report. `ValidationVerdict` construction rejects inconsistent verdicts, but the
parser is specifically the trust boundary for serialized/external payloads and
does not reconstruct that invariant.

Required correction: strictly validate the entire v2 schema, including
`passed == (verdict == "pass")`, reason/verdict consistency, nonempty
well-formed digests, label and collection types, allowed units, string
positions, finite/nonnegative numerical fields, positive cluster counts, and
per-unit envelope structure/identity. Prefer parsing into a validated type over
returning an unchecked mapping. Add explicit no-result-to-pass mutation tests.

## Finding-by-finding round-2 disposition

| Round-2 target | State | Evidence |
| --- | --- | --- |
| 1. Series parity/truncation | **OPEN (narrow parity case fixed)** | `terms=2` now refuses, but the accepted reflection pair differs by `1.63059e-05` at tolerance `1e-6` while both tail bounds are `5.04e-210`. |
| 2. Per-regime audit | **CLOSED** | All 15 cells carry all five separately gated convergent ladders plus the reset diagnostic, against the same caps. The matrix yields `numerical_no_result` with 270 level rows and 33 independent reasons; the formerly hidden `interior/strong/detuning=-0.450` cell has five convergent-gate reasons. Added resets cannot rescue any gate. |
| 3. Paired uncertainty/dataset | **OPEN** | Caller SEs are eliminated and resampling inputs are digest-bound, but signed-contrast uncertainty does not estimate the folded contrast and no cluster IDs exist. |
| 4. Schema v2 | **OPEN** | The tag and fields changed, but the parser accepts inconsistent `passed`/`verdict` and malformed level data, allowing a no-result bypass. |

## Scientific audit and acceptance semantics

The pooled audit is explicitly `numerical_no_result`. Its p20 commitment-time
absolute errors/SEs/uncertainty-aware bounds at timesteps `0.032`, `0.016`, and
`0.008` are respectively:

| dt | absolute error | SE | bound |
| --- | --- | --- | --- |
| 0.032 | 0.1344 | 0.139088 | 0.412576 |
| 0.016 | 0.1152 | 0.126790 | 0.368780 |
| 0.008 | 0.0112 | 0.082900 | 0.177001 |

The finest bound exceeds the frozen `0.10` cap. The per-regime audit is also
`numerical_no_result`; 14 of 15 cells are blocked. The
`interior/strong/detuning=-0.450` cell is no longer pooled away: its commitment
shift is `0.0625 -> 0.020833 -> 0.083333` with finest uncertainty-aware bound
`0.235885`, and its p20 ladder is unresolved with bound `1.46259`. Its added
resets (`0.479 -> 0.479 -> 1.0625`) are only the nonconvergent diagnostic and do
not change those failures.

This is honest reference-budget machinery evidence, not a production
validation result. `verify.py:15572-15579` and the README now say exactly that.
Pulse-end censoring is applied identically to both arms; master trials are the
bootstrap units; auxiliary replications remain inside their cluster; and the
three physical clocks have independent physical keys. A waived reset ladder
cannot make any convergent ladder pass. The no-result outcome itself therefore
closes the earlier overclaim. The open schema parser defect is the place where
that block can currently be lost downstream.

## Reconfirmed closed areas

- The canonical verifier reports **85/85**. Independent `/usr/bin/time -l`
measurement was 75.92 seconds, 617,365,504 B maximum RSS and 183,141,432 B
peak footprint. Endpoint walkers and bridge auxiliaries remain batched; no
bridge or endpoint cube and no result files were found.
- The killed-diffusion PDE signs, absorbing boundaries, upper/lower exit
orientation, Rannacher startup, conservation check, domain/Courant guard and
accepted-grid output-domain validation remain closed. The available evidence
still does not justify imposing the rejected stricter positivity condition:
the prior randomized accepted-grid scan found only roundoff-scale time
reversals, while the material old oscillatory case is rejected.
- Public zero-diffusion crossing checks retain boundary/outside precedence.
- Audit v2 exact interval endpoints make equal keys imply equal intervals across
stride/window/order/partition probes. Auxiliary audit uniforms are independent
across refinement, but the physical fine-leaf tree remains exactly paired and
coarser increments are sums of the same physical leaves.
- Circular representatives, contraction-side exclusion, entry/exit/re-entry,
wrap straddling, disappearing/topology-changing bands, ties, pulse edges, and
conservative-reset ordering remain covered. Replay and record construction
enforce reset-only/shared-prefix behavior and refuse created or advanced
commitments.
- Unit- and position-specific ladders and maxima remain separate. A fresh raw
import still loads none of `analytic`, `killed_diffusion`, or
`moving_band_audit`; `compileall` is clean. README counts and nonclaims remain
honest, with no exponent, Born-rule, measurement, detector, population, or
outcome claim.

## Commands and exact evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, exit 0; 75.92 s; 617,365,504 B max RSS |
| `python3 -m compileall -q adler_born_two_channel` | clean |
| zero-drift `terms=2` reproduction | refuses; bound `0.10963522314633094`, true error `0.029389771996621517` |
| drift-reflection reproduction above | both calls accept; gap `1.630594488233328e-05` at `1e-6` tolerance; bounds `5.041795014211675e-210` |
| two-cluster folded-bootstrap reproduction | implementation signed-contrast SE `0`; actual folded-contrast bootstrap SE `0.699390609546963` |
| parser mutations | accepts inconsistent no-result/`passed=True`, empty dataset digest, and invalid unit/position/nonfinite/negative level fields |
| pooled/per-regime datasets | 18/270 level rows; both `numerical_no_result`; per-regime has 33 reasons |
| fresh `raw_runner` import | `analytic=False`, `killed_diffusion=False`, `moving_band_audit=False` |

The claimed byte identity of the prior 75 check rows remains impossible to
independently reconstruct without a frozen pre-change row snapshot or digest.
The current 85/85 result is independently confirmed; historical identity is
still a handoff assertion.

No implementation file was edited, staged, committed, or reverted. This
round-2 closure section is the only write made by this review.

# Fix-up round 3 closure review — 2026-08-28

## Verdict: OPEN

Round 3 closes the original reflection reproduction, the parity alias, the
signed-versus-folded bootstrap error, the caller-supplied uncertainty path, and
the previously contradictory v2 payloads. It does not close the contracts those
fixes are meant to establish. A public series evaluation is still certified and
returned when its true error exceeds both its tolerance and certificate; two
different physical identity manifests can produce the same sample and dataset
digests; and the report parser accepts both forged envelopes and a coherently
rewritten `numerical_no_result` as a pass.

These are not requests for canonical ordering or an extensible schema. Order is
significant in the implementation and a closed schema is acceptable. The
failures below violate the implementation's own stated policies under those
choices.

## Blocker — `series_error_certificate` is not an error certificate

The exact earlier attacks now behave correctly:

- the positive/negative-drift reflection pair returns
`6.279704305603412e-05` and `6.279695574454315e-05`, a gap of
`8.731149097e-11`, below the requested `1e-6`; its reported roundoff allowance
is approximately `8.349e-08`;
- the zero-drift `terms=2` parity alias refuses, with tail bound
`0.10963522314633094` despite its zero nested gap;
- zero-time and absorbing-edge truncation bounds are exactly zero, while an
outside start, negative time, two-dimensional start array and zero term count
are refused by both public certificate helpers.

The new total remains an unproved error model, and a 150-decimal-digit
calculation breaks it. This public call is **accepted**:

```python
series_survival(
    -0.4, 0.7,
    0.025026019953529995,
    0.4550185446096362,
    [0.6999989000000001],
    [0.0016266446286139454],
    terms=400,
    tolerance=2e-15,
)
```

It returns `8.759717660387155e-05`. Directly summing the same eigenfunction
formula with 150-digit `mpmath` arithmetic gives

```text
0.0000875971765906097686915750852899144450525846675323208984557...
```

at 800 terms. The 400-to-800 high-precision tail is only
`5.479885701614182e-29`, so this is a resolved reference, not another
truncation comparison. The returned value's true error is
`1.3261781198262515e-14`, **6.63 times the requested tolerance** and **7.43**
**times the total certificate**:

| quantity | value |
| --- | --- |
| analytic tail certificate | `5.035691563481804e-26` |
| floating roundoff certificate | `1.784292635432645e-15` |
| claimed total certificate | `1.7842926354830018e-15` |
| nested 392/400-term gap | `1.3552527156068805e-20` |
| actual error against 150-digit reference | `1.3261781198262515e-14` |

The cancellation factor is reported as exactly `1.0`, so no ill-conditioned
sum refusal protects this case. It is a near-edge, nonzero-drift case at an
ordinary tilt, and the returned value is inside `[0,1]`. An adversarial sweep of
184 finite sums over both drift signs, tilts through 299, several translated and
scaled bands, near-edge starts, normalized time scales and 2–400 terms found
this after comparing each retained sum with 90-digit arithmetic.

The reason is visible in the model at `killed_diffusion.py:550-598`:
`(terms + 8) * eps * sum(abs(term)) + 8 * eps` bounds an idealized floating
accumulation, but does not establish the error of all term construction,
coordinate normalization, exponential evaluation and transcendental
evaluation. Exact reduction of `n*u` after `u` has already been formed does not
make the full formula exact. The README's statement that this is what the
floating evaluation “can be out by” is therefore overclaimed.

Required correction: derive a complete, auditable floating-error bound for the
actual operation graph, or compute the reference in precision high enough that
a rigorously bounded conversion plus analytic tail fits the requested
tolerance. Add the exact case above as a regression. A certificate must refuse
whenever the true numerical error can exceed it, even at tolerances smaller than
the package's usual calibration tolerance.

## High — embedded delimiters collide in the physical-identity digest

The structural identity work is otherwise effective. Missing, repeated and
wrong-count identities refuse; all samples in a dataset must share one ordered
cluster set; values/baseline shapes align; identities, members,
baseline-members, observations and their order affect the digest; cluster
reordering and ordinary relabelling move the digest; and the fixed array page
order is interpreted against the frozen schedule consistently. The
two-cluster bootstrap now reports the exact transformed result:

```text
signed adjacent-contrast SE = 0.0
folded adjacent-contrast SE = 0.699390609546963
reported paired_error       = 0.699390609546963
```

No caller-supplied standard-error path remains in
`compare_refinement(dataset, budgets, declared_digest)`.

However, `PairedSample.digest` joins each identity sequence with the NUL
character (`killed_diffusion.py:1657-1663`), while `_require_names` permits NUL
inside an individual label. The encoding is therefore not injective. With
identical observations, these distinct manifests:

```python
identities_a = ("a\x00b", "c")
identities_b = ("a", "b\x00c")
members_a    = ("m\x00n", "q")
members_b    = ("m", "n\x00q")
```

produce the identical sample digest
`0ad6bddc539691eabea09d0db930660e645c1c1916f0d1edb41bf0f51c6d8775`
and identical dataset digest
`9d217899f22e67417686a6819285a1fab6000b547730de6bbc7ebb5c3a58297f`.
The SHA-256 has not collided; two different physical manifests were serialized
to the same bytes before hashing. NUL is representable in Python and escaped
JSON strings, and no public validation excludes it.

Required correction: length-prefix every individual label in the hash input,
or reject every reserved separator in `_require_names`. Apply the same
unambiguous encoding to identities, members and baseline members, and retain a
regression using the exact pair above. The stale `PairedSample.measured`
docstring at `killed_diffusion.py:1683-1692` should also stop claiming that the
signed bootstrap is the conservative statistic; the comparison now correctly
bootstraps `errors()` instead.

## Blocker — v2 still permits forged envelopes and a coherent no-result bypass

The former malformed cases are closed. The parser now refuses:

- contradictory `verdict`, `passed` and `reasons` fields;
- empty, equal, uppercase, nonhex and wrong-length digests;
- v1, missing and unknown top-level or row keys;
- NaN/inf, negative error/SE fields, invalid cluster counts and invalid units;
- false per-level absolute/relative arithmetic;
- duplicate observable/position/timestep rows and unequal timestep sets across
ladders.

It does not validate several semantics it exports as trusted. Starting from an
ordinary valid two-unit report, each of the following mutation classes is
accepted independently:

1. change one level of a ladder from `probability` to `time`, producing a
mixed-unit ladder;
2. replace a probability envelope's absolute error, relative error, standard
error and timestep by `0.0, 0.0, 0.0, 0.123` even though no referenced level
has those values;
3. make the probability envelope name the identity of a `time` row;
4. remove the envelope for a unit that is still present in the levels;
5. set the coarsest level's `paired_error` to `999.0`, although the producer's
own contract defines it as zero.

`parse_validation_report` only checks that an envelope's named
observable/position exists somewhere (`killed_diffusion.py:2239-2271`). It does
not require that row to have the envelope's unit, be the finest row, carry the
envelope numbers, or actually attain the maximum; nor does it require exactly
one envelope for every unit present. A downstream Ticket 07 reader can therefore
receive a parser-approved zero envelope for visibly nonzero levels.

More seriously, a genuine report with `verdict="numerical_no_result"` and two
blocking reasons is accepted after changing the three mutually redundant fields
coherently to:

```python
payload["verdict"] = "pass"
payload["passed"] = True
payload["reasons"] = []
```

All level rows and both digests can remain byte-for-byte unchanged. This is not
the old contradictory-field attack; it shows that the advertised serialized
trust boundary cannot establish the verdict. The report contains no frozen caps,
noise floors, `require_decrease` settings, or complete decision evidence from
which the parser could recompute the result, and neither digest authenticates
the serialized report itself. Consequently a coordinated no-result-to-pass
mutation is internally consistent under the present parser and passes.

Required correction: rebuild every envelope from the validated levels and
compare it field-for-field, enforce one consistent unit per ladder and exactly
the set of envelopes implied by the levels, and enforce coarsest/adjacent paired
error semantics that are representable in the report. To make the verdict a
self-validating trust boundary, the parser must also receive or carry the frozen
budget/decision manifest and enough evidence to recompute the verdict, or verify
an authentication value rooted outside the mutable payload. Otherwise narrow
the contract explicitly: it is a shape-and-local-consistency parser, not a
mechanism that prevents a serialized no-result from becoming a pass.

## Round-3 target disposition

| Target | State | Exact evidence |
| --- | --- | --- |
| 1. Series certification | **OPEN** | Former reflection and parity attacks close, but the accepted 400-term call above has true error `1.32618e-14` against certificate `1.78429e-15` and tolerance `2e-15`. |
| 2. Folded bootstrap and identities | **OPEN only on identity binding** | The transformed bootstrap exactly reproduces `0.699390609546963` and caller SEs are gone. Embedded-NUL manifests produce identical sample and dataset digests. |
| 3. Strict report v2 | **OPEN** | Local malformed rows refuse, but mixed-unit ladders, forged envelope values/references, missing envelopes and a coherent no-result-to-pass rewrite are accepted. |

## Reconfirmed scientific result and closed areas

- The stationary S3 killed-diffusion/endpoint gate still passes. The canonical
S3 row has residual `7.810e-02` against tolerance `5e-01`; the known-limit PDE
row remains `4.537e-04` against `1e-03`.
- The pooled moving-band audit remains `numerical_no_result`: its p20
uncertainty-aware bound is 0.177 against the unchanged 0.10 cap. The
per-regime result remains `numerical_no_result` with 33 reasons and fourteen
of fifteen cells blocked against the same caps. `require_decrease=false` for
added resets cannot rescue commitment, survival, time, or pathwise-subset
gates. The canonical row's residual remains `1.458e-02` against `1e-01`.
- The correct acceptance interpretation is unchanged. A green audit-mechanism
check confirms that an unresolved reference sample emits a frozen,
machine-readable no-result; it does not say the moving audit passed. Ticket
04 permits that blocking outcome, so the canonical command need not exit
nonzero merely because the scientific reference audit is unresolved.
- PDE signs, absorbing data, exit orientation, Rannacher/CN implementation,
conservation, Courant/domain guards, grid convergence, zero-diffusion
precedence, bridge formula, circular/topology/tie cases, reset ordering,
reset-only shared-prefix replay, audit-v2 interval identity and exact physical
fine-leaf pairing remain covered by passing checks.
- Raw-process isolation remains exact in a fresh subprocess:
`analytic=False`, `killed_diffusion=False`, `moving_band_audit=False`.
`compileall` is clean. No `.npy`, `.npz`, `.csv`, `.parquet`, `.h5` or `.hdf5`
result file exists under the package.
- README counts and the scientific nonclaims remain explicit. No population,
race, detector measurement, outcome, production validation, fitted exponent,
scaling or Born-rule result is introduced. The series-certificate statement
is a numerical overclaim, not a smuggled physical claim.

## Commands and exact evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, exit 0; 78.12 s; 595,640,320 B max RSS; 183,026,768 B peak footprint |
| 150-digit series reproduction above | accepted; actual error `1.3261781198262515e-14`, certificate `1.7842926354830018e-15`, tolerance `2e-15` |
| former reflection pair | accepted correctly; gap `8.731149097e-11` at tolerance `1e-6` |
| former `terms=2` parity alias | refuses; tail `0.10963522314633094` |
| former two-cluster bootstrap attack | reported folded SE `0.699390609546963`; independently resampled signed SE `0.0` |
| embedded-NUL identity/member mutation | two different manifests have identical sample and dataset SHA-256 digests |
| parser mutation matrix | contradictions and malformed rows refuse; five envelope/unit/paired-error forgeries and coherent no-result-to-pass rewrite accept |
| `python3 -m compileall -q adler_born_two_channel` | clean |
| fresh raw import and result-file search | prediction/audit modules absent; no result files |

The canonical/RSS log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/dcbd3f95-8859-4d3d-8f8c-bf3412ac7fb0/output.log`.
As in the earlier rounds, byte identity of historical rows cannot be independently
reconstructed without a frozen prior snapshot or digest; the current 85 rows and
their current residuals are independently confirmed.

No implementation file was edited, staged, committed, or reverted. This
round-3 closure section is the only write made by this review.

# Fix-up round 4 closure review — 2026-08-28

## Verdict: OPEN

Round 4 repairs the exact finite-band false certificate and the NUL-delimited
manifest collision. The new length-prefixed physical-manifest encoding is
injective on the accepted labels tested, and the folded bootstrap remains
correct. Closure is still blocked by two public trust failures:

1. finite scalar inputs can overflow the series' derived band arithmetic and
return `nan` through a `nan` certificate; and
2. schema v3 recomputes its verdict from mutable reported uncertainty summaries,
not from evidence bound to `dataset_digest`, so the same frozen no-result can
still be rewritten to a parser-approved pass with both digests unchanged.

The manifest's advertised control-character policy is also incomplete, and
schema v3 cannot round-trip several legitimate machinery no-results emitted by
`compare_refinement`.

## Blocker — finite series inputs can return a NaN as “certified”

The exact round-3 reproduction is closed correctly. At band `(-0.4, 0.7)`,
`D=0.025026019953529995`, drift `0.4550185446096362`, start
`0.6999989000000001`, time `0.0016266446286139454`, and 400 terms, the repaired
value is `8.759717659060986e-05`. Its error from the prior 150-digit reference
is approximately `9.5e-20`, inside the reported total certificate
`1.784478463488835e-15`. Certification at tolerance `2e-15` is therefore valid;
arbitrary refusal is neither needed nor requested. The same call refuses just
below its certificate and accepts just above it. The parity alias still refuses,
and the original reflected drift pair remains within tolerance.

An independent 286-cell finite-sum sweep went beyond the frozen 121 cells over
six translated/scaled bands, both drift signs, tilts through 299, edge fractions
down to adjacent representable values, normalized short/moderate times, and
2–400 terms. No finite retained-sum error exceeded the new floating certificate;
the worst observed error/roundoff ratio was `0.09791`. This is good empirical
evidence for ordinary representable bands.

The public domain is not closed under its own derived arithmetic. With ordinary
warning settings:

```python
series_survival(
    0.0, 1e308,
    1e308, 0.0,
    [5e307], [1e-308],
    terms=400, tolerance=1e-6,
)
```

returns `[[nan]]`. `series_error_certificate` returns tail `inf`, roundoff
`nan`, total `nan`, and cancellation `inf`. The comparison at
`killed_diffusion.py:950-970` does not reject a NaN bound because
`nan > tolerance` is false, and the probability-domain comparison likewise
does not reject a NaN output. A second finite-input case with lower/upper
`-1e308, +1e308` overflows the band width and behaves the same way. Under
`-W error` these cases happen to raise `RuntimeWarning`; without that global
warning policy, the public API returns the NaN.

The failure arises before the claimed operation-graph certificate can apply:
`upper-lower`, Dekker's `_SPLIT * value`, wave construction, or a related derived
quantity overflows despite every scalar input being finite. `_series_domain`
checks the inputs but never requires the width or subsequent scale quantities to
be finite and representable.

Required correction: validate the representability of the derived width,
double-double split operands, tilt/wave/exponential arguments, term array and
every certificate component before evaluation. Any nonfinite intermediate,
output, or certificate must raise a declared `ValueError`; explicitly reject
NaN in the tolerance and probability-domain gates. Add both exact wide-band
cases under normal warnings and `-W error`. Update the stale
`series_error_certificate` docstring, which still describes the removed
`(terms + ROUNDOFF_GROWTH) * eps * SUM|term| + 8 eps` model.

## Blocker — schema v3 still trusts uncertainty summaries not bound to the data

Schema v3 now does useful local work: it embeds and reconstructs the contract and
budgets, validates their budget digest, enforces schedules and units, recomputes
blocking codes with the shared `_ladder_codes`, and rebuilds envelopes
field-for-field. The old coherent rewrite that changes only verdict/passed/reasons
now refuses.

It does **not** recompute the bootstrap evidence. The report embeds only
`measured`, `standard_error`, `paired_error`, `span_error`, and `clusters`; it
does not embed the cluster observations or a proof that connects those summaries
to `dataset_digest`. The parser merely checks that the dataset digest looks like
64 lowercase hex characters.

This exact reproduction starts with a genuine `numerical_no_result` whose point
error is zero but whose frozen two-cluster bootstrap standard error is
`0.49990617181433633`, making its two-sigma bound exceed a `0.1` cap. Keeping
the budget digest, dataset digest, contract, caps, measured values and references
unchanged, mutate only:

```python
for row in payload["levels"]:
    row["standard_error"] = 0.0
    row["paired_error"] = 0.0
    row["span_error"] = 0.0
payload["verdict"] = "pass"
payload["passed"] = True
payload["reasons"] = []
payload["blocking"] = []
payload["envelopes"]["probability"]["standard_error"] = 0.0
```

`parse_validation_report` accepts the forged pass. Both digests remain
byte-for-byte unchanged, including dataset digest
`cfc4336149790a3232e3f3613b1ec5d33b55a0ec9601956b51ccc7e32c34e049`.
The parser faithfully recomputes a pass from invented summaries; it does not
recompute those summaries from the frozen data.

The same missing link appears in simpler mutations:

- every level's `clusters` can be changed from the contract's 2 to 999 and the
parser accepts it with the dataset digest unchanged;
- the human `reasons` can be replaced by arbitrary nonempty sentences while
leaving the machine codes unchanged; only their count is checked;
- a valid `cluster_mismatch` no-result produced by `compare_refinement` has no
level rows and crashes the parser with `UnboundLocalError` because
`schedule_seen` was never assigned;
- a valid `unbudgeted` no-result produced by `compare_refinement` cannot
round-trip because the report contains no sample evidence from which the
parser could reconstruct the unbudgeted identity.

Thus several codes in `REASON_CODES` are not actually recomputable from the v3
payload, while load-bearing uncertainty codes are recomputed from unverified
claims.

Required correction: make the parser consume a trusted `ValidationDataset` (or
embed canonical raw cluster observations/member identities) and recompute
measured values and all three bootstrap uncertainties using the embedded frozen
sampling design. It must recompute and compare `dataset_digest` from that same
evidence. Alternatively, supply an externally rooted authenticated proof binding
every summary to the known dataset digest; a self-declared hex string is not such
a proof. Bind level cluster counts to the sampling design, define how machinery
no-results serialize without levels, and require every report emitted by
`compare_refinement(...).as_dict()` to round-trip. Either derive the human reason
text from codes during parsing or explicitly document it as non-authoritative.

## Medium — manifest encoding is injective, but control rejection is incomplete

The round-3 collision is closed. Both NUL-containing tuple partitions refuse;
the control-free repartitions `("ab","c")` versus `("a","bc")` produce
different sample and dataset digests. Field names, sequence counts, UTF-8 byte
lengths, values/baseline shapes, baseline presence, arm roles and observation
bytes are bound. Reordering, ordinary relabelling, member/baseline substitution,
field swaps and Unicode normalization variants move the digest. The declared
no-normalization/order-significant policy is internally consistent.

The implementation report says control characters are refused outright, but
`_require_names` rejects only C0 characters below U+0020 and DEL. It accepts the
C1 control U+0085, the bidi formatting control U+202E, and the format control
U+200D inside physical identities. Separately, `PairedSample` accepts a newline
in `observable` and NUL in `position`, because `_require_label` and the position
check do not share the manifest-name control policy. Length-prefixing prevents
the old digest collision, but this is not the consistent pre-hash rejection the
round-4 contract and implementation report claim.

Required correction: define “control character” precisely and apply one helper
to every hashed label field. If the policy is to reject them, use Unicode
categories such as `Cc`/the intended `Cf` subset or a declared printable-label
grammar, including observable and position. If some formatting characters are
intentionally valid, narrow the documentation and add positive controls.

## Round-4 target disposition

| Target | State | Exact evidence |
| --- | --- | --- |
| 1. Series certification | **OPEN on overflow domain; repaired finite certificate passes review** | The prior false case is accurate to about `9.5e-20` inside a `1.78448e-15` certificate. But finite wide-band inputs return a NaN value through a NaN certificate. |
| 2. Manifest encoding | **OPEN only on declared control policy** | Count-and-length encoding is injective in every structural mutation tested; NUL refuses and control-free repartitions differ. C1/Cf physical IDs and control-bearing observable/position fields still accept. |
| 3. Schema v3 | **OPEN** | Zeroing unbound SE/paired/span summaries changes a real no-result to a parser-approved pass with both digests unchanged; wrong cluster counts accept and legitimate machinery no-results do not round-trip. |

## Reconfirmed preserved areas

- Canonical verification remains **85/85**. The stationary S3 row remains
`7.810e-02 / 5e-01`, and the known-limit killed-diffusion row remains
`4.537e-04 / 1e-03`.
- Pooled and per-regime moving audits remain honest
`numerical_no_result` under unchanged caps: pooled p20 bound 0.177 against
0.10; per-regime 33 reasons with fourteen of fifteen cells blocked. The reset
waiver cannot rescue any convergent observable or pathwise-subset gate.
- The folded two-cluster bootstrap still reports
`0.699390609546963` versus signed-contrast zero, and no caller-supplied SE path
has returned.
- PDE signs/data/orientation, CN/Rannacher behavior, conservation, grid/domain
guards, zero-diffusion precedence, bridge formula, topology/tie/order cases,
reset-only shared-prefix replay, audit interval identity and physical fine-leaf
pairing remain covered by passing checks.
- The independent RSS run used 655,343,616 bytes maximum resident set and
185,435,216 bytes peak footprint, below the 900 MB gate. No cube or result file
appeared.
- Fresh raw import remains isolated:
`analytic=False`, `killed_diffusion=False`, `moving_band_audit=False`.
`compileall` is clean. README check counts and physical nonclaims remain
explicit: no exponent, population, race, detector measurement, outcome,
production validation, scaling, or Born-rule result is asserted. The README's
v3 trust-boundary claim and one sentence still calling the version v2 are
documentation defects, not smuggled physical claims.

## Commands and evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, exit 0; 79.29 s; 655,343,616 B max RSS; 185,435,216 B peak footprint |
| prior 150-digit false-certificate call | accurately accepted at `2e-15`; error about `9.5e-20`, total certificate `1.784478463488835e-15` |
| independent 286-cell high-precision finite-sum sweep | no finite error exceeded roundoff certificate; worst ratio `0.09791` |
| wide-band overflow probes under normal warnings | `series_survival -> [[nan]]`; certificate total `nan` |
| NUL/control-free/Unicode/role manifest mutations | NUL refuses; accepted structural variants have distinct digests; C1/Cf controls still accept |
| frozen-uncertainty report mutation | real no-result becomes parser-approved pass with both digests unchanged |
| parser cluster/machinery mutations | clusters 999 accepts against design 2; legitimate cluster-mismatch crashes; unbudgeted report refuses round-trip |
| `python3 -m compileall -q adler_born_two_channel` | clean |
| fresh raw import and post-verifier result-file search | prediction/audit modules absent; no result files |

The canonical/RSS log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/64bff71f-0de7-4484-82c3-01e1f5f082a3/output.log`.
The implementer's verbose/direct/warning/failure/hash-seed matrix was not
independently repeated after the public blockers above were reproduced; the
canonical, compile, raw-isolation, no-file, high-precision and memory paths were.

No implementation file was edited, staged, committed, or reverted. This
round-4 closure section is the only write made by this review.

# Independent closure re-review — fix-up round 5

## Verdict: OPEN

Round 5 closes the two literal round-4 wide-band reproductions, and schema v4
correctly rejects the prior plain-dictionary zero-SE and cluster-count
forgeries when it is given an unchanged dataset. The common Unicode policy is
also enforced correctly by every constructor tested.

Closure is nevertheless blocked by two public trust failures:

1. derived series arithmetic can still collapse a nonzero drift to zero and
return a falsely certified probability; several other derived paths emit a
warning, `OverflowError`, or public infinity instead of a named refusal; and
2. the external schema-v4 trust root is only a frozen dataclass around writable,
aliased NumPy arrays. A mutation between its digest check and recomputation
changes a genuine `numerical_no_result` into a parser-approved `pass`.

The shape-only inspector also accepts forbidden Unicode categories in the
observable and position of machinery-only blocking rows. The rooted parser
still refuses those mutations, so that last defect is policy/shape validation,
not another verdict bypass.

## Blocker — derived tilt collapse produces a falsely certified probability

The two exact round-4 cases now refuse cleanly under `python3 -W error` in all
three entry points:

- `(0, 1e308, 1e308, 0, 5e307, 1e-308)` refuses on Dekker's split of the width;
- `(-1e308, +1e308, 0.1, 0, 0, 1)` refuses on the infinite width.

That guard does not make its intermediate operations representation-safe.
This accepted case is decisive:

```python
series_survival(
    0.0, 1e100,
    1e308, 1e308,
    [5e99], [1e-108],
    terms=20, tolerance=1e-6,
)
```

It returns `[[6.585600605439407e-05]]`. The certificate reports tail `0.0`,
roundoff/total `1.7770422122589846e-15`, and cancellation `1.0`.
`series_truncation_bound` independently returns `0.0`.

The mathematical tilt is `drift / (2 diffusion) = 0.5`; the implementation
forms `2.0 * diffusion` first, which overflows to infinity, so the computed tilt
at `killed_diffusion.py:690` is silently `0.0`. The Péclet guard therefore also
sees zero instead of `5e99`. This is not merely a conservative refusal-domain
choice: it certifies the zero-drift series for an overwhelmingly drifted
process.

An independent endpoint bound shows the true survival is negligible. Survival
to time `t` implies that the unconstrained endpoint is below the upper edge. In
standard-normal units that event has

```text
z = (upper - start - drift*t) / sqrt(2*diffusion*t)
  = -7.071067811865475244e99,
log P(endpoint < upper) < -2.5e199.
```

Thus the true error is essentially `6.5856e-05`, over ten orders above the
reported total and above the requested `1e-6` tolerance. This is an accepted,
falsely certified public value.

Required correction: compute ratios and products with scale-safe formulations
(`drift / diffusion / 2`, or a common exponent/mantissa scaling), and validate
the mathematical Péclet number independently of a denominator that may
overflow. A guard is not valid when the arithmetic used to construct the value
being guarded has already collapsed it.

## Blocker — warning and infinity hygiene is still incomplete

The following were run under `python3 -W error` through
`series_survival`, `series_error_certificate`, and
`series_truncation_bound`:

| Attack | Observed result |
| --- | --- |
| `lower=-1e308, upper=1e308, start=1e308` | all three raise `RuntimeWarning: overflow encountered in subtract` while eagerly constructing `max(abs(starts-lower))`, before the already-known infinite width is named |
| `L=1e-200, D=1e-200, drift=2, start=L/2, t=1e-200, terms=20` | survival/certificate raise `RuntimeWarning` from `wave*wave`; truncation bound raises bare `OverflowError: (34, 'Result too large')` from `(pi/L)**2` |
| `L=1, D=.1, drift=60, start=.5, t=nextafter(0,1), terms=400` | survival/certificate refuse a nonfinite tail, but the public `series_truncation_bound` returns `[[inf]]` |
| absorbing start `x=lower` at positive time | `series_error_certificate` returns `cancellation=[[inf]]` even though the round-5 report says every certificate component is finite |

The small-band attack is particularly instructive. The aggregate mathematical
decay product is representable, but `_series_domain` evaluates it in the order
`D * highest * highest * t`, while `_series_terms` squares `wave` first. The
guard proves a different operation graph safe from the one that subsequently
runs.

Required correction: perform every guard with warning-free, scale-safe
arithmetic and in the same grouping as the evaluation, or change the evaluation
to the grouping the guard certifies. Short-circuit after a decisive nonfinite
width before evaluating later derived fields. The public truncation-bound helper
must either return a finite bound or raise the named convergence/domain error;
it cannot export infinity under the round-5 contract. Define a finite
cancellation diagnostic for exactly pinned values, or explicitly narrow the
no-nonfinite-certificate claim and its public type.

## Repaired ordinary series domain remains supported

The prior false-certificate case remains correctly repaired. At
`(-0.4, 0.7)`, `D=0.025026019953529995`, drift
`0.4550185446096362`, start `0.6999989000000001`, time
`0.0016266446286139454`, 400 terms:

- value: `8.759717659060986e-05`;
- tail: `5.035691563481804e-26`;
- roundoff: `1.784478463438478e-15`;
- total: `1.784478463488835e-15`;
- requests at `1.7e-15` and `1.784e-15` refuse, while `1.8e-15` and `2e-15`
accept.

The `terms=2` parity alias still refuses. A fresh independent 286-cell
high-precision partial-sum sweep covered six translated/scaled bands, starts
from adjacent-to-edge through the centre, both drift signs with dimensionless
tilts through 50, short/moderate times, and 2--400 terms. No retained-sum error
exceeded the floating certificate; the worst error/roundoff ratio was
`0.19854`. Of those cells, 179 were publicly certified at `1e-6`; the remainder
refused. These controls support the repaired ordinary-scale implementation but
cannot rescue the derived-overflow counterexample above.

## Blocker — the externally supplied dataset is mutable across the trust check

The intended schema-v4 design is otherwise correctly wired:

- `parse_validation_report(payload, dataset)` has no dataset default; calling it
payload-only raises `TypeError`;
- it requires the exact `ValidationDataset` type, verifies its digest and
contract, re-runs `compare_refinement`, and compares the entire dictionary;
- the prior zero-SE/pass rewrite is accepted only by the explicitly shape-only
inspector and is refused by the rooted parser;
- changing every cluster count from 2 to 999 is likewise refused by the rooted
parser;
- altered observations, substituted datasets/labels, reordered identities and
stale digests refuse;
- repeated comparisons with the same ordinary dataset are byte-identical; and
- legitimate `cluster_mismatch` and `unbudgeted` reports now round-trip as
`numerical_no_result` rather than crashing.

The external root itself is not frozen. `PairedSample.__post_init__` uses
`np.asarray` at `killed_diffusion.py:1807` and `:1823`, retaining a caller's
array when it already has the requested dtype. The arrays remain writable.
`ValidationDataset` and the rebuilt dataset at `:2932` merely retain those
same `PairedSample` objects. The digest is a dynamic property over their current
bytes.

The basic reproduction is direct: mutate the array passed to `PairedSample`
after construction, and `sample.values` changes with it; mutate
`sample.values`, and the caller's array changes. `values.flags.writeable` is
`True`, and the dataset digest changes after each mutation. The class being a
`frozen=True` dataclass freezes only field assignment, not its evidence.

That becomes a verdict bypass because `parse_validation_report` checks the
digest once and then recomputes from the same mutable object. A deterministic
time-of-check/time-of-use probe used two clusters:

- old values `[-1,-1,-1]` and `[+1,+1,+1]` produce a real
`numerical_no_result`, bootstrap SE `0.5002461856388788`, dataset digest
`adab3a9a1d666ffb362d0343996dade04ca0a48f76cb5dda1c47d248dca4b324`;
- new all-zero values produce `pass`, SE `0.0`, digest
`25334bba3138d16fe58b0a49bae77f63bf5cda73629dc77c8a5a11f82f0cd2a9`.

A `dict` subclass (accepted because the inspector checks `isinstance(dict)`)
mutated the aliased observations when `dataset_digest` was read after the left
side of the digest comparison had been computed. It returned the old digest for
that comparison and retained the new digest/new pass report thereafter.
`parse_validation_report` returned the forged **pass**. The same race requires
no exotic arithmetic and can be realized by an ordinary concurrent alias; the
dict subclass merely makes the interleaving deterministic.

Required correction: make `PairedSample` own defensive C-contiguous copies of
both arms and mark them read-only before storing them. Rebuilding a dataset must
not reintroduce caller aliases. In addition, capture the trusted digest once and
verify it again after recomputation (or compare against a truly immutable
snapshot) so any concurrent mutation refuses. A frozen external-root design is
acceptable; a writable external root checked at one instant is not.

## Medium — shape-only machinery rows bypass the common Unicode policy

The constructor-level policy works. U+0085 (`Cc`), U+202E and U+200D (`Cf`), a
lone U+D800 surrogate (`Cs`), U+E000 private use (`Co`), and unassigned U+0378
(`Cn`) were each refused in identities, members, baseline members, observables,
positions, dataset labels and budget/report labels. Greek, Han and emoji labels
pass. Composed `"é"` and decomposed `"e\u0301"` both pass and produce distinct
digests, consistent with the documented no-normalization policy.

There is one uncovered report surface. A legitimate machinery-only
`cluster_mismatch` report has no levels and a blocking row. Replacing that row's
observable or position with each of the five forbidden categories is accepted
by `inspect_validation_report`. At `killed_diffusion.py:2663-2677` the row's
code is validated, but its two labels never pass through `_require_printable`;
machinery codes are then excluded from local recomputation. The rooted parser
refuses because its full recomputation differs, so no scientific pass follows,
but the promised one-policy shape checker does accept a report label the public
constructors refuse.

Required correction: call `_require_label` / `_require_printable` on every
blocking row's observable and position before classifying its code. Apply the
same explicit check to all report label fields instead of relying on a later
ladder reconstruction to validate them incidentally.

## Reconfirmed preserved areas

- Canonical verification is **85/85**, exit 0, in 79.68 s. Maximum RSS was
635,289,600 bytes and peak footprint 181,535,848 bytes, below the 900 MB gate.
- Against the round-4 canonical log, 84 of 85 check rows are byte-identical;
only the measured memory row moved, from 625.0 to 605.9 MB.
- The stationary S3 residual remains `7.810e-02 / 5e-01`; the killed-diffusion
limiting residual remains `4.537e-04 / 1e-03`; the audit row remains
`1.458e-02 / 1e-01`.
- A separate direct recomputation reconfirmed the pooled audit as
`numerical_no_result` with one reason. Its finest time envelope remains
`0.011200000000000876` with SE `0.08290027807264948`, hence the two-sigma
bound near `0.177` against the unchanged `0.10` cap. The per-regime audit is
also `numerical_no_result` with 33 reasons. The five convergent observables
retain absolute caps `0.10`; only `added_resets_mean` has
`require_decrease=False`, with its separate count cap `3.0`.
- Folded bootstrap remains `0.699390609546963` on the two-cluster crossing
fixture. The length-prefixed physical-manifest encoding remains injective in
the prior NUL/repartition/role/order attacks.
- PDE guards, bridge formula, zero-diffusion precedence, reset-only shared
prefixes, audit interval identity, physical fine-leaf pairing, per-unit and
per-position ladders, raw isolation and bounded allocations remain covered by
passing canonical rows.
- `compileall` is clean. A fresh raw-run import has
`analytic=False`, `killed_diffusion=False`, `moving_band_audit=False`. No
`.npy`, `.npz`, `.csv`, `.parquet`, `.h5` or `.hdf5` result appeared under the
package.
- README still states the pooled/per-regime moving audit is a blocking
`numerical_no_result`, not a production validation pass, and explicitly makes
no exponent, population, race, detector-measurement, outcome, scaling or
Born-rule claim. Two stale sentences still call the report version `v2` and
describe the superseded `terms // 2` convergence comparison; those should be
corrected with the blockers.

## Commands and evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, 79.68 s, 635,289,600 B max RSS, 181,535,848 B peak footprint |
| exact round-4 extreme bands, all three helpers under `-W error` | six named `ValueError` refusals |
| drift/diffusion denominator-overflow attack | falsely certified `6.585600605439407e-05` versus endpoint upper bound below `exp(-2.5e199)` |
| edge/square/short-time derived attacks under `-W error` | leaked `RuntimeWarning`, bare `OverflowError`, public `inf` truncation bound, and `inf` cancellation diagnostic |
| independent 286-cell 100-digit retained-sum sweep | zero certificate breaches; worst error/roundoff ratio `0.19854` in the ordinary finite domain |
| ordinary schema-v4 mutation matrix | prior summary, cluster-count, observation, identity, dataset, digest, reason, contract, budget and envelope mutations refuse at rooted parse; mismatch/unbudgeted round-trip |
| writable-dataset TOCTOU reproduction | genuine no-result becomes parser-approved pass after mutation between digest check and recomputation |
| Unicode category/normalization matrix | constructors refuse Cc/Cf/Cs/Co/Cn across all named fields; Greek/Han/emoji pass; normalization forms stay distinct; shape inspector accepts forbidden machinery blocking labels |
| direct pooled/per-regime recomputation | pooled `numerical_no_result` (1 reason), per-regime `numerical_no_result` (33 reasons), unchanged caps and waiver |
| compile, fresh raw import, result-file search | clean; prediction/audit modules absent; no result files |

The canonical/RSS log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/85977449-5e9e-4b6e-ad5b-fcb4d600926b/output.log`.

No implementation file was edited, staged, committed, or reverted. This
round-5 closure section is the only durable write made by this review.

# Independent closure re-review — fix-up round 6

## Strict verdict: OPEN

The scale-safe finite-parameter series repair is effective, and the canonical
suite remains **85/85**. The ticket is still open because the new read-only
NumPy view exposes its writable owner through the public `.base` attribute. An
untrusted report mapping can use that route while `parse_validation_report` is
snapshotting the payload and turn a real `numerical_no_result` dataset into the
dataset for a parser-approved pass. This is the same trust-boundary property
round 6 was required to close, not a defensive-programming preference.

Two smaller public-contract gaps also remain: an arbitrarily large positive
`terms` value leaks a bare `OverflowError`, and the shape inspector applies the
Unicode policy to identity-bearing report labels but still accepts forbidden
Unicode categories in a reason, despite the round-6 contract naming reasons.

## Blocker — the alleged immutable evidence exposes a writable owner

`PairedSample` now makes a genuine defensive copy at
`killed_diffusion.py:1891` and `:1907`, and `ValidationDataset` rebuilds its
samples at `:2052-2061`. Those changes correctly sever source-array and
sample-object aliases. The last step does not make the stored evidence
immutable, however. `_sealed` at `:1735-1750` returns a view whose `.base` is
the owned ndarray. The view and owner initially have `writeable=False`, but the
owner is publicly reachable and owns its memory, so NumPy permits:

```python
sample.values.base.setflags(write=True)
sample.values.base[...] = replacement
```

The exact probe found:

```text
source shares sample/dataset        False False False
sample.values.flags.writeable       False
sample.values.base.flags.owndata    True
sample.values.base.flags.writeable  False
direct write                         ValueError
sample.values.setflags(write=True)   ValueError
memoryview(sample.values).readonly   True
base.setflags + base write           SUCCEEDED
sample.values.flags.writeable        False
sample.values.base.flags.writeable   True
dataset digest changed               True
```

Source-array mutation, post-construction metadata mutation, direct writes,
view-level `setflags` and a direct `memoryview` are harmless or refused. The
base traversal is sufficient to invalidate the snapshot claim.

It also remains a verdict bypass. A two-cluster sample with level vectors
`[-1,-1,-1]` and `[+1,+1,+1]` produced:

```text
before verdict  numerical_no_result
before SE       0.5002461856388788
before digest   8f24bceac72fc4f6f379980cfe33f7c3da3de9cbf5b0a4085b34d68a56650d79
```

Writing zeros through the stored owner's `.base` produced:

```text
after verdict   pass
after SE        0.0
after digest    ee67d09e9645c81a91f96222576c5d9279402b0225eaffd2ca82c9656aaffef4
```

A `dict` subclass whose `items()` callback performs that base write was then
wrapped around the legitimate all-zero pass report. At
`killed_diffusion.py:2953`, `json.dumps(payload)` invoked the callback before
the parser rebuilt the dataset at `:2958`. The rooted parser **accepted the**
**pass**; the callback ran once and the caller's dataset retained the new digest.
The second digest check at `:2995` only establishes that the parser's *new*
snapshot stayed stable during recomputation. It cannot detect that untrusted
payload code changed the externally trusted evidence before that snapshot was
taken.

The canonical test at `verify.py:16752-16834` misses both routes. It tests the
original source alias, direct stored-array writes, view-level flag restoration,
and a mapping callback that mutates the now-disconnected original source. It
never traverses `sealed.values.base`, nor does its callback mutate the owner
that the dataset actually hashes.

Required correction: store numeric evidence over an actually immutable root,
for example a bytes-backed ndarray constructed from an owned immutable byte
snapshot, or keep the ndarray private and return copies such that no public
`.base` chain reaches a writable owner. Add an exact `.base` traversal test and
a payload-protocol callback that mutates every publicly reachable route. Taking
the trusted dataset snapshot before invoking untrusted payload methods is also
the safer order; with a truly immutable root, either order becomes harmless.

## Scale-safe series blocker closed for finite scalar parameters

The prior drift-collapse call
`(0, 1e100, D=1e308, mu=1e308, x=5e99, t=1e-108, N=20)` now refuses cleanly in
all three public helpers because its correctly computed Péclet value is
`5e99 > 300`. The previous false zero-drift certificate cannot be reproduced.
The round-4 width/Dekker cases, `(-1e308,+1e308)`, the `1e-200` band/mode-square
case, the shortest tilted time, and absorbing starts all either return their
exact documented result or raise a named `ValueError` under `python3 -W error`;
none emits a warning, bare arithmetic exception, NaN or infinity.

The Péclet boundary behaves as a real series-domain gate rather than a mask:

- values at `nextafter(300, 0)` and exactly `+/-300` enter the certificate path
and produce finite certificates (the survival helper may still refuse a
value whose total error exceeds its requested tolerance);
- values immediately above 300 refuse consistently in all three helpers; and
- a scale sweep of 2,500 finite parameter tuples produced 4,249 finite helper
returns and 1,523 named `ValueError` refusals, with zero other exceptions or
non-finite public results.

A fresh 286-cell, 100-digit retained-partial-sum comparison accepted 179 cells
at tolerance `1e-6` and refused 107. No accepted cell exceeded its reported
certificate; the worst true-error/roundoff-bound ratio was
`0.198538742619822`. The repaired finite-band case remains
`8.759717659060986e-05` with total certificate
`1.784478463488835e-15`. These results support the declared Péclet limit and
the finite-domain certification.

## Medium — unbounded `terms` still leaks a bare arithmetic exception

`_series_domain` accepts every positive Python integer at
`killed_diffusion.py:698`, then forms `terms * pi / width` at `:740-741`.
With ordinary finite band/diffusion/drift/time inputs and `terms=10**400`, each
public helper (`series_survival`, `series_error_certificate`, and
`series_truncation_bound`) raises:

```text
OverflowError: int too large to convert to float
```

With `terms=10**100`, survival/certificate can instead leak NumPy's generic
`ValueError: Maximum allowed size exceeded`. This violates the round-6 public
rule that an unrepresentable finite-input case gets a named domain/convergence
refusal rather than a bare overflow. Freeze a documented maximum term count
before float conversion or allocation, and refuse larger counts with the same
explicit domain/resource exception across all three entry points.

## Medium — reason strings bypass the stated Unicode policy

The requested identity-bearing label gap is closed: machinery-only and
ordinary rows refuse U+0085 (`Cc`), U+202E/U+200D (`Cf`), a lone U+D800
surrogate (`Cs`), U+E000 (`Co`) and U+0378 (`Cn`) in observable and position
fields; Greek, Han and emoji pass; NFC `"é"` and NFD `"e\u0301"` remain valid
and distinct. The inspector docstring at `killed_diffusion.py:2452-2470` is
also unambiguous that inspection does not establish verdict truth.

The round-6 correction explicitly extends the shared Unicode policy to
`reason`. At `:2552-2555`, however, reasons are checked only for type and
non-emptiness. Replacing a legitimate ordinary no-result reason with
`"blocked " + ch` was accepted by `inspect_validation_report` for each of the
same six Cc/Cf/Cs/Co/Cn characters. Rooted parsing later refuses because the
reason no longer matches recomputation, so this is not a pass-forging route;
it is a remaining public shape-policy defect. Apply the printable/category
validation to every reason and add the ordinary-report matrix to the canonical
tests.

## Reconfirmed preserved areas

- Canonical verification is **85/85**, exit 0, in 83.92 s. Maximum RSS was
636,764,160 bytes and peak footprint 182,633,480 bytes, below the 900 MB
gate. Against round 5, 84 of 85 check rows are byte-identical; only the
measured memory row changed (`605.9` to `607.3` MB).
- Direct recomputation preserves the pooled `numerical_no_result` with one
reason and the per-regime `numerical_no_result` with 33 reasons across 14
blocking cells. The pooled time envelope is still
`0.011200000000000876` with SE `0.08290027807264948`. Budget and dataset
digests remain respectively
`aeb97e3c0c7e5f757fa3f6fed5872bc3b1573570c9d673ca24415290aabd9257`
and `6840ff143b07b7a6deb221d0933728f7a11648075aecdab928d1431b3b45b844`.
Only `added_resets_mean` retains `require_decrease=False`, under its separate
`(absolute=3.0, relative=30.0, noise_floor=0.0)` cap; it cannot rescue a
failed convergent gate.
- The rooted schema-v4 parser still has no payload-only default, recomputes the
full report, refuses zero-SE/pass, cluster-count, digest, reason and dataset
substitutions in ordinary non-racing use, and deterministically round-trips
legitimate reports. The shape-only inspector still says it is not a trust
boundary.
- The folded bootstrap, injective physical-manifest encoding, PDE domain
guard, bridge formula, zero-diffusion precedence, reset-only shared-prefix
behavior, audit-v2 interval identity, physical fine-leaf pairing, per-unit
and per-position ladders, and S3 gate remain covered by unchanged passing
rows.
- `compileall` is clean. A fresh `raw_runner` import leaves
`killed_diffusion` and `moving_band_audit` absent. No `.npy`, `.npz`, `.csv`,
`.parquet`, `.h5` or `.hdf5` result exists under the package.
- README still reports the scientific audit as a blocking no-result and makes
no exponent, population, race, detector-measurement, outcome, scaling or
Born-rule claim. Its obsolete sentence at line 2041 still says the current
v4 report “is v2”; that documentation contradiction should be corrected.

## Commands and evidence

| Probe | Result |
| --- | --- |
| `/usr/bin/time -l python3 -m adler_born_two_channel.verify` | **85/85**, 83.92 s, 636,764,160 B max RSS |
| all round-5 finite-input series reproductions under `python3 -W error` | exact boundary results or named `ValueError`; no warnings/non-finite return |
| Péclet-neighbor and 2,500-tuple scale sweep | finite inside the declared domain or named refusal; zero stray exceptions/non-finite results |
| independent 286-cell 100-digit retained-sum sweep | zero accepted certificate breaches; worst ratio `0.198538742619822` |
| `terms=10**400` in all three public helpers | bare `OverflowError: int too large to convert to float` |
| `.base` traversal | restores owner write flag, changes values and dataset digest |
| mapping `items()` mutation during rooted parsing | real no-result evidence changed; parser accepted the corresponding pass |
| Unicode constructor/row/normalization matrix | identity-bearing labels fixed; forbidden categories still accepted in ordinary reason strings |
| direct pooled/per-regime recomputation | unchanged blocking no-results, digests, caps and added-reset waiver |
| `compileall`, fresh raw import, result-file search | clean; oracle/audit absent; no result files |

The round-6 canonical/RSS log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/74b7eb28-dda8-4bbe-a4b8-fcd61a9e0980/output.log`.

No implementation file was edited, staged, committed, or reverted. This
round-6 closure section is the only durable write made by this review.

# Independent closure re-review — fix-up round 7

## Strict verdict: OPEN

The three functional corrections requested for round 7 are effective.  The
observation arrays now terminate in immutable `bytes`; neither the caller's
arrays nor any public NumPy view/base path can change the evidence.  The rooted
parser fixes its trusted dataset snapshot before invoking payload conversion.
All three public series helpers reject invalid and arbitrarily large term
counts before float conversion or allocation and accept the documented maximum
of 1,000,000.  The common Unicode policy now covers ordinary report reason
text.  The canonical verifier remains **85/85**.

Closure is still blocked by the third correction's documentation clause.  The
package README and two live API comments still describe the current report as
v2 even though the exported schema is v4.  The README mutation check passes
despite the contradiction, because its forbidden list recognizes only the
fully qualified old schema tags, not the stale sentence that is actually
present.

## Blocker — current-schema documentation still says v2

The implementation and the first sentence of the README correctly name
`dk-numerical-validation/v4` (`killed_diffusion.py:212`, `README.md:2034-2039`).
They are contradicted by three descriptions of the live report:

- `README.md:2041` says **“The version is `v2`”**;
- `ValidationVerdict.as_dict` says the live tag “reads `v2`” at
`killed_diffusion.py:2386-2395`; and
- the closed-field declaration says it is the key set of “a v2 report” at
`killed_diffusion.py:2453-2458`.

These are not historical headings: each sentence identifies the version/tag
of the report the adjacent live code exports.  The surrounding history of v1,
v2 and v3 is useful and can remain, but the current object has to be identified
as v4 consistently.

The canonical prose guard misses this exact defect.  `check_readme` forbids
only `dk-numerical-validation/v1`, `/v2`, `/v3`, and `terms // 2`
(`verify.py:17696-17705`).  None of those exact strings is present, so a direct
call reports:

```text
True README.md carries all 17 required statements, including the explicit
non-claim sentence and both verification commands
```

while `"The version is `v2`" in README.md` is also true.  This explains why
the canonical **85/85** is compatible with the remaining documentation error.

Required correction: rewrite the three current-schema descriptions above to
name v4, preserving older versions only as explicitly historical material.
Extend the prose/source guard to cover these live descriptions (or positively
assert that each current-schema description names
`dk-numerical-validation/v4`) so this exact regression fails the verifier.

## The immutable dataset/rooted-parser correction is closed

Both `values` and `baseline` have the public base chain
`readonly ndarray -> readonly ndarray -> bytes`.  They share memory with
neither the caller's arrays nor the `PairedSample` from which a
`ValidationDataset` is rebuilt.  Direct assignment, restoring the view flag,
restoring the immediate base flag, and writing through a `memoryview` all
refuse; the memoryviews are read-only.

The decisive former bypass was repeated on a genuine two-cluster
`numerical_no_result` (bootstrap SE `0.5018174252567522`, digest
`29af583321c376bca6860100a162020f677d8aa212bbab06bbc61e4dc6b1d49b`).
A payload mapping's `items()` callback walked every public base link and tried
to unseal and zero it.  Both ndarray links raised `ValueError`, the root was a
`bytes`, rooted parsing returned the original no-result, and the digest and a
freshly recomputed report were byte-for-byte stable.

The ordering is also literal in the trust-boundary implementation:
`parse_validation_report` reconstructs `ValidationDataset` at
`killed_diffusion.py:3024-3025`, captures its digest at `:3026`, and only then
invokes `json.dumps(payload)` at `:3027`.  No untrusted payload protocol runs
before the independently supplied evidence is fixed as a new immutable
snapshot.

## The term-bound and Unicode corrections are closed

For each of `series_survival`, `series_error_certificate`, and
`series_truncation_bound`, the matrix `True`, `0`, `-1`, `1.5`, `10**400`, and
`MAX_SERIES_TERMS + 1` produced only the module's named `TypeError` or
`ValueError`; none reached float conversion or NumPy allocation.  Each helper
accepted `MAX_SERIES_TERMS == 1_000_000` and returned finite output.  The shared
guard occurs before derived arithmetic at `killed_diffusion.py:727-735`.

A legitimate ordinary no-result report was mutated one forbidden category at
a time in its reason: U+0085 (Cc), U+202E and U+200D (Cf), U+D800 (Cs), U+E000
(Co), and U+0378 (Cn).  `inspect_validation_report` rejected all six through
`_require_reason`; ordinary Greek/Han reason text remains accepted by the
canonical positive control.

## Reconfirmed preserved results

- The canonical verifier is **85/85**, exit 0, in 84.33 s on Python 3.13.11 /
NumPy 2.4.3.  The killed-diffusion limiting residual remains
`4.537e-04 / 1e-03`; the stationary endpoint-refinement gate remains
`7.810e-02 / 5e-01`; the audit row remains `1.458e-02 / 1e-01`.
- The pooled audit is `numerical_no_result` with one reason.  Its finest time
envelope is still `0.011200000000000876` with SE
`0.08290027807264948`, so its two-sigma bound remains about `0.177` against
the unchanged `0.10` cap.
- The per-regime audit is `numerical_no_result` with 33 reasons across 14 of 15
cells.  The five convergent observables retain absolute cap `0.10`; only
`added_resets_mean` has `require_decrease=False`, under its independent
`(absolute=3.0, relative=30.0, noise_floor=0.0)` budget.  That count waiver
cannot rescue a convergent gate.
- The public finite-series/domain checks pass, and the independent maximum-term
probe above returned finite results for every helper.
- Maximum resident set was 644,104,192 bytes (614.3 MiB), with peak footprint
185,468,008 bytes, below the 900 MiB canonical gate.  No Monte Carlo cube was
materialized.
- A fresh `python3 -B` raw-run import reported
`analytic=False`, `killed_diffusion=False`, and
`moving_band_audit=False`.  No `.npy`, `.npz`, `.csv`, `.parquet`, `.h5`, or
`.hdf5` result file exists under the package after the canonical and direct
audit runs.
- The canonical conclusion and README remain explicit that Ticket 04 makes no
coupling-exponent, detector-measurement, outcome, scaling, or Born-rule
claim.  It has one clock, no population, and no race.

## Exact commands and evidence

```sh
/usr/bin/time -l python3 -m adler_born_two_channel.verify

python3 -B - <<'PY'
import numpy as np
from adler_born_two_channel import killed_diffusion as k
a=(0.,1.,.1,0.,np.array([.5]),np.array([1.]))
for f in (k.series_survival,k.series_error_certificate,k.series_truncation_bound):
 for n in (True,0,-1,1.5,10**400,k.MAX_SERIES_TERMS+1):
  try: f(*a,n) if f is not k.series_survival else f(*a,terms=n)
  except (TypeError,ValueError): pass
  else: raise AssertionError((f.__name__,n))
 y=f(*a,k.MAX_SERIES_TERMS) if f is not k.series_survival else f(*a,terms=k.MAX_SERIES_TERMS)
 print(f.__name__,'all_refusals_named','maximum_accepted')
PY

python3 -B - <<'PY'
import json, sys
import adler_born_two_channel.raw_runner
print(json.dumps({name: name in sys.modules for name in (
'adler_born_two_channel.analytic',
'adler_born_two_channel.killed_diffusion',
'adler_born_two_channel.moving_band_audit')}, sort_keys=True))
PY

find adler_born_two_channel -type f \( -name '*.npy' -o -name '*.npz' \
  -o -name '*.csv' -o -name '*.parquet' -o -name '*.h5' \
  -o -name '*.hdf5' \) -print

grep -RInE 'dk-numerical-validation/v[1234]|which is why the tag reads|top-level keys a v[1234] report' \
  adler_born_two_channel --include='*.py' --include='*.md'
```

The direct audit extraction command was:

```sh
/usr/bin/time -l python3 -B - <<'PY'
from adler_born_two_channel import verify as v
from adler_born_two_channel import killed_diffusion as k
from adler_born_two_channel import moving_band_audit as m
p=v._audit_dataset(); pb=v._audit_budgets('S3b moving-band audit, pooled reference budgets',v._AUDIT_TRIALS,('pooled',)); pv=k.compare_refinement(p,pb,pb.digest)
r=v._matrix_dataset(); rb=v._audit_budgets('S3b moving-band audit, per-regime reference budgets',v._MATRIX_TRIALS,tuple(c.label for c in m.REDUCED_MATRIX)); rv=k.compare_refinement(r,rb,rb.digest)
print('pooled',pv.verdict,len(pv.reasons),p.digest,pb.digest)
print('per_regime',rv.verdict,len(rv.reasons),len({x.split(':')[0] for x in rv.reasons}),r.digest,rb.digest)
print('caps',v._audit_caps())
print('pooled_probability_envelope',pv.envelope_for('probability'))
print('pooled_time_envelope',pv.envelope_for('time'))
PY
```

The count of blocked matrix cells was independently extracted with:

```sh
python3 -B - <<'PY'
from adler_born_two_channel import verify as v, killed_diffusion as k, moving_band_audit as m
d=v._matrix_dataset(); b=v._audit_budgets('S3b moving-band audit, per-regime reference budgets',v._MATRIX_TRIALS,tuple(c.label for c in m.REDUCED_MATRIX)); z=k.compare_refinement(d,b,b.digest)
print('verdict',z.verdict,'reasons',len(z.reasons),'blocking_cells',len({position for _,position,_ in z.blocking}),'total_cells',len(m.REDUCED_MATRIX))
PY
```

It printed `verdict numerical_no_result reasons 33 blocking_cells 14 total_cells 15`.

The immutable-root/reason probe was:

```sh
python3 -B - <<'PY'
import copy, numpy as np
from adler_born_two_channel import killed_diffusion as k
from adler_born_two_channel.verify import _probe_contract
c=_probe_contract(clusters=2); x=np.zeros((2,1,3)); x[0]=-1; x[1]=1
s=k.PairedSample('s','',x,None,0.,('t0','t1'),('m',)); d=k.ValidationDataset('m',c,(s,))
b=k.FrozenBudgets('m',c,(k.ValidationBudget('s','probability',.1,9.,0.),))
r=k.compare_refinement(d,b,b.digest).as_dict(); h=d.digest
print('root',type(d.samples[0].values.base.base).__name__,'readonly',memoryview(d.samples[0].values).readonly,'shares',np.shares_memory(x,d.samples[0].values),'verdict',r['verdict'])
for node in (d.samples[0].values,d.samples[0].values.base):
 try: node.setflags(write=True); print('UNSEALED')
 except Exception as e: print('sealed',type(e).__name__)
x[:]=0
print('source_stable',d.digest==h,k.compare_refinement(d,b,b.digest).as_dict()==r)
class M(dict):
 def items(self):
  for node in (d.samples[0].values,d.samples[0].values.base):
   try: node.setflags(write=True); node[:]=0
   except Exception: pass
  return super().items()
print('parse_stable',k.parse_validation_report(M(copy.deepcopy(r)),d)==r,d.digest==h)
for p in (0x85,0x202e,0x200d,0xd800,0xe000,0x378):
 q=copy.deepcopy(r); q['reasons']=[z+chr(p) for z in q['reasons']]
 try: k.inspect_validation_report(q); out='ACCEPTED'
 except Exception as e: out=type(e).__name__
 print(f'U+{p:04X}',out)
PY
```

The larger first pass exercised both `values` and `baseline`, every public
`.base` link, `memoryview`, and the original input arrays; both arms had the
same immutable `bytes` root and stable digest/report behavior.

The round-7 canonical/RSS log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/1c299fa8-e37a-4cf5-b870-45593b1d60b7/output.log`.
The direct audit log is
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/9e109dd8-00f8-4a7c-824a-2466ebac43f0/output.log`.

No implementation file was edited, staged, committed, or reverted.  This
round-7 closure section is the only durable write made by this review.

# Independent closure re-review — documentation fix-up round 8

## Strict verdict: OPEN

The three stale live-schema statements are corrected, the package sources now
contain no present-tense claim that the live numerical-validation report is v1,
v2 or v3, and the full numerical execution matrix is unchanged.  Closure is
nevertheless blocked by the strengthened documentation check itself: it misses
direct abbreviated forms of the same stale claim and rejects an unambiguously
historical sentence.  That fails the round-8 review contract to detect
comparable abbreviated variants while accepting clearly historical prose.

## Blocker — the stale-schema patterns miss abbreviations and overmatch history

The new guard is a material improvement.  `_stale_schema_prose` scans
`README.md`, `killed_diffusion.py` and `moving_band_audit.py`; its fixture table
replays all three original stale sentences, and `check_readme` fails if either
the live scan or fixture table reports a problem (`verify.py:17617-17717`,
`:17798-17809`).  Direct calls returned:

```text
fixture_problems []
source_problems []
check_readme True ... no stale schema prose in any of 3 sources, with all 10
pattern fixtures held
```

An independent mutation matrix against the exported pattern tuple found:

| Present-tense stale sentence | Result |
| --- | --- |
| `The version is v2.` | caught |
| `Tag reads v2.` | caught |
| `The exact top-level keys a v2 report carries.` | caught |
| `The numerical-validation schema is v3.` | caught |
| `The live numerical-validation schema is v1.` | caught |
| `The current schema version is v2.` | caught |
| `Current report: v3.` | **missed** |
| `Live schema: v1.` | **missed** |
| `The report version is v2.` | **missed** |
| `Current version: v3.` | **missed** |
| `Validation schema: v2.` | **missed** |
| `This report uses v2.` | **missed** |

The first two misses are the colon-abbreviated forms of fixtures the code
already declares stale (`the current report is v3`, `the live schema is v1`).
They are not exotic circumventions.  `_STALE_SCHEMA_PATTERNS` requires either
the leading word `the` or the verb `is` in those constructions
(`verify.py:17633-17640`), so a heading or compact label using a colon passes.

The same matrix kept the built-in historical examples legal, but caught the
clearly historical sentence:

```text
Before v4, the live schema was v3.
```

The `current|live` pattern matches any v1-v3 token within the following sixty
characters; it does not require a present-tense assertion, so `was v3` is
mistaken for `is v3`.  That contradicts the check's own stated distinction at
`verify.py:17627-17632`.

Required correction: add fixtures for at least `Live schema: v1`,
`Current report: v3`, and `The report version is v2`, plus an explicitly
historical `Before v4, the live schema was v3`.  Make the patterns recognize
compact present-tense separators/verbs without treating past-tense migration
sentences as live claims.  The fixture table, not a reviewer's interpretation,
should hold both sides of that boundary.

## The three original documentation defects are closed

- `README.md:2060` names `dk-numerical-validation/v4`, and `:2066-2071`
explicitly says the live schema is v4 before recounting the v1-v4 migration.
- `ValidationVerdict.as_dict` says its stable keys are under
`VALIDATION_SCHEMA`, “which is v4,” at `killed_diffusion.py:2386-2395`.
- `REPORT_FIELDS` is now described as the exact top-level keys under the live
`VALIDATION_SCHEMA`, without assigning them to v2
(`killed_diffusion.py:2453-2459`).

A complete `v1|v2|v3|v4` source search found no other stale live numerical-
validation claim.  The remaining older-version text is correctly classified:

- `README.md:2066-2096` and `killed_diffusion.py:192-210` are the validation
schema's historical migration record;
- `killed_diffusion.py:2576-2589` explains why old report shapes are refused;
- README noise/audit passages and `moving_band_audit.py:133-146` name the
separate physical-noise and audit-key schemas or their own history; and
- verifier mentions at `:15229`, `:17142-17213`, and `:17620-17671` are
deliberate old-version rejection mutations and stale-pattern fixtures, not
labels applied to the live report.

## Reconfirmed numerical and scientific results

- Canonical, verbose, direct-script, and warnings-as-errors invocations each
returned **85/85**, exit 0.  The deliberate failure probe printed **85/86**
and exited 1.
- Canonical stationary results remain byte-identical: limiting-solution
residual `4.537e-04 / 1e-03`, endpoint-refinement residual
`7.810e-02 / 5e-01`, and audit residual `1.458e-02 / 1e-01`.
- The 84 deterministic PASS rows (all except the machine-dependent peak-RSS
row) are byte-identical between round 7 and round 8.
- Under `PYTHONHASHSEED=0` and `987654321`, both runs returned 85 PASS rows;
their 84 deterministic rows were identical with SHA-256
`09ec837206b45278effe5babdc0585246e5f47f973f846e3b4ea09c32ef3662a`.
- Direct recomputation preserves pooled `numerical_no_result` with one reason,
dataset digest
`a1b71abec7557997554a0682b40cdef9e97be72e59b63cdbce9cb3ad5b503d14`
and budget digest
`aeb97e3c0c7e5f757fa3f6fed5872bc3b1573570c9d673ca24415290aabd9257`.
Per-regime remains `numerical_no_result` with 33 reasons across 14 of 15
cells, dataset digest
`beffd0afd886ba752846dd66b660ca150c4017a5f38b8de717c9ba4c21e959a7`
and budget digest
`6840ff143b07b7a6deb221d0933728f7a11648075aecdab928d1431b3b45b844`.
- The five convergent audit observables retain absolute cap `0.10` and their
prior floors; `added_resets_mean` alone retains its separate
`(3.0, 30.0, 0.0)` cap and non-decrease waiver.  Pooled finest envelopes are
unchanged: probability `0.014583333333333282` (SE
`0.009136733524487156`), time `0.011200000000000876` (SE
`0.08290027807264948`), and added resets `0.98125` (SE
`0.23208023748307305`).
- Canonical maximum RSS was 625,508,352 bytes (596.5 MiB), peak footprint
178,750,520 bytes, below the 900 MiB gate.  The in-memory compile check
compiled all 15 package Python sources.
- A fresh raw-run import again reported `analytic=false`,
`killed_diffusion=false`, and `moving_band_audit=false`.  The post-matrix
search found no `.npy`, `.npz`, `.csv`, `.parquet`, `.h5`, or `.hdf5`
result file under the package.
- The README and canonical conclusion still make no population, race,
coupling-exponent, detector-measurement, outcome, scaling, or Born-rule
claim for Ticket 04.

## Exact command matrix

```sh
/usr/bin/time -l python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --verbose
python3 adler_born_two_channel/verify.py
python3 -W error -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --prove-failure-exit
```

The compile check was deliberately in-memory so this documentation-only review
did not create bytecode beside the implementation:

```sh
python3 -B - <<'PY'
from pathlib import Path
files=sorted(Path('adler_born_two_channel').glob('*.py'))
for p in files: compile(p.read_text(encoding='utf-8'),str(p),'exec')
print('compiled',len(files),'Python sources in memory')
PY
```

The hash-seed command ran `python3 -m adler_born_two_channel.verify` in two
captured subprocesses with `PYTHONHASHSEED=0` and `987654321`, selected the
`[PASS]` rows, excluded only the bounded-RSS row, and SHA-256 hashed the
remaining byte lines.  The direct-result command rebuilt `_audit_dataset()` and
`_matrix_dataset()`, passed each through `compare_refinement` under the frozen
budgets, and printed verdicts, reason/cell counts, digests, `_audit_caps()`, and
all three pooled envelopes.  The exact scripts and their outputs are retained
in the logs below.

The raw/no-file checks were:

```sh
python3 -B - <<'PY'
import json,sys
import adler_born_two_channel.raw_runner
print(json.dumps({x:x in sys.modules for x in ('adler_born_two_channel.analytic','adler_born_two_channel.killed_diffusion','adler_born_two_channel.moving_band_audit')},sort_keys=True))
PY
find adler_born_two_channel -type f \( -name '*.npy' -o -name '*.npz' \
  -o -name '*.csv' -o -name '*.parquet' -o -name '*.h5' \
  -o -name '*.hdf5' \) -print
```

Round-8 logs:

- canonical/RSS:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/dab5cacd-1603-45be-af34-b2ced6a18aaa/output.log`
- verbose:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/b63696a5-a62e-4ce1-8aef-c19a48f4d5b2/output.log`
- warnings-as-errors:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/643bb6c2-1681-4e3b-bcaf-7190d51aa0b2/output.log`
- direct script:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/48a42ad1-7352-470f-b3a7-2510204b5ae0/output.log`
- deliberate failure:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/ab2fa35f-05e2-43e5-830e-2085d852d26d/output.log`
- hash-seed:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/bfa3c1dc-3a44-446d-87e8-1c73a781faec/output.log`
- direct scientific extraction:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/419b23df-b8dc-437d-a07a-cf2a826737c5/output.log`

No implementation file was edited, staged, committed, or reverted.  This
round-8 closure section is the only durable write made by this review.

# Independent closure re-review — grammar fix-up round 9

## Strict verdict: OPEN

The six exact stale present-tense sentences now reject, the exact historical
sentence accepts, all 17 built-in fixtures are individually discriminating,
and the real three-file prose scan is clean.  The subject-first grammar also
handles the requested colon, equals, `is`, `uses`, `reads`, quoting and
historical-tense cases correctly.

Closure is still blocked by the version-first fallback
`r"\ba v[123] report\b"`.  It has no tense at all, so it rejects ordinary
historical migration prose using exactly the `was`, `carried`, `had` and
`replaced` wording round 9 asked this review to cover.  The full numerical and
operational matrix remains unchanged.

## Blocker — version-first history is rejected without reading its verb

The new primary pattern is principled: a two-word live-artifact subject, a
present-tense link (or `:` / `=`), and a quoted or unquoted old version in that
order (`verify.py:17633-17663`).  The fallback at `:17665-17672` exists for the
third original sentence, whose order is instead “a v2 report carries.”  It
matches only `a vN report`, however, and never checks the following verb.

The requested exact cases all behave correctly:

```text
Current report: v3                    caught
Live schema: v1                       caught
The report version is v2              caught
Current version: v3                   caught
Validation schema: v2                 caught
This report uses v2                   caught
Before v4, the live schema was v3     accepted
```

All 17 rows of `_STALE_FIXTURES` likewise produced `caught == expected`,
`_stale_pattern_fixtures()` returned `[]`, and `_stale_schema_prose()` returned
`[]`.

The nearby grammar matrix passed every subject-first case:

- `The live schema: v1`, `The current report = v2`, and
`Validation schema is v3` reject;
- `This report uses `v2``, `The tag reads "v1"`,
`Schema version carries **v3**`, and `Report version remains 'v2'` reject;
and
- `The live schema was v3 before v4`, `The current report were v2 in the old implementation`, `Validation schema carried v1 before migration`,
`This report had v2 semantics before v4`, `The live schema replaced v3 with v4`, and `The live schema is v4, which replaced v3` all accept.

The same historical tenses fail as soon as the old version precedes the report
subject:

| Clearly historical prose | Observed |
| --- | --- |
| `Before v4, a v3 report was accepted` | **rejected** |
| `Historically, a v2 report carried one envelope` | **rejected** |
| `A v1 report had no dataset digest` | **rejected** |
| `A v3 report was replaced by v4` | **rejected** |

These are not remote paraphrases: `carried`, `had`, and `replaced` are the
historical verbs named in the grammar's own contract at
`verify.py:17653-17657`, and the README's live migration discussion uses this
same version-first style (`README.md:2066-2071`).  The current fixtures cover
only `v1 carried ...`, not the equally natural `a v1 report carried ...`, so
all 17 can pass while this half of the tense boundary remains untested.

Required correction: make the version-first fallback tense-aware.  It must
still catch the original `a v2 report carries` sentence, but must inspect the
post-subject link so `was`, `were`, `carried`, `had`, and `was replaced` remain
historical.  Add the four reproductions above (or an equivalent cross-product)
to the fixture table so both word orders are held by tests.

## `verify.py` exclusion is acceptable and manually clean

The exclusion is explicit and accurate at `verify.py:17674-17683`:
`_PROSE_SOURCES` scans only `README.md`, `killed_diffusion.py`, and
`moving_band_audit.py` because `verify.py` necessarily constructs old schema
tags in parser mutations and quotes stale sentences in its fixture table.
Scanning itself would make the test fail on its own inputs.  The comment also
states the real cost: explanatory prose in `verify.py` is not automatically
covered.

A manual review of every v1-v3 occurrence in `verify.py` found no stale live-
schema assertion outside the quoted examples:

- `:4750-4769` is physical-noise key history, unrelated to the validation
report;
- `:15229`, `:17142-17213` construct or inspect deliberate old-tag/parser
mutations;
- `:15417` and `:17265-17266` say those old tags/shapes are refused; and
- `:17620-17723` explains the stale-prose mechanism and contains its quoted
fixtures.

The exclusion is therefore a sound, documented test boundary; the open finding
is the grammar exercised on the scanned files, not the exclusion.

## Reconfirmed unchanged schema, numerics and nonclaims

- Canonical, verbose, direct-script, and warnings-as-errors runs each returned
**85/85**, exit 0.  The deliberate failure probe printed **85/86** and exited
- Direct schema probing returned `dk-numerical-validation/v4`, round-tripped a
valid report, and refused substituted v1, v2 and v3 tags.
- Stationary results remain `4.537e-04 / 1e-03` for the limiting solution,
`7.810e-02 / 5e-01` for endpoint refinement, and
`1.458e-02 / 1e-01` for the audit row.
- The 84 deterministic PASS rows are byte-identical between round 8 and round
  9. Under `PYTHONHASHSEED=0` and `987654321`, both full runs produced 85 PASS
rows; the 84 deterministic rows were identical with SHA-256
`09ec837206b45278effe5babdc0585246e5f47f973f846e3b4ea09c32ef3662a`.
- Direct recomputation preserves pooled `numerical_no_result` with one reason,
dataset digest
`a1b71abec7557997554a0682b40cdef9e97be72e59b63cdbce9cb3ad5b503d14`
and budget digest
`aeb97e3c0c7e5f757fa3f6fed5872bc3b1573570c9d673ca24415290aabd9257`.
Per-regime remains `numerical_no_result` with 33 reasons across 14 of 15
cells, dataset digest
`beffd0afd886ba752846dd66b660ca150c4017a5f38b8de717c9ba4c21e959a7`
and budget digest
`6840ff143b07b7a6deb221d0933728f7a11648075aecdab928d1431b3b45b844`.
- Audit caps and finest envelopes are unchanged: every convergent observable
has absolute cap `0.10`; `added_resets_mean` alone has `(3.0, 30.0, 0.0)` and
`require_decrease=False`; pooled probability/time/count envelopes remain
`0.014583333333333282`, `0.011200000000000876`, and `0.98125` with the same
standard errors.
- Canonical maximum RSS was 626,016,256 bytes (597.0 MiB) and peak footprint
189,629,472 bytes, below the 900 MiB gate.  All 15 Python sources compiled in
memory.
- Fresh raw import again left `analytic`, `killed_diffusion`, and
`moving_band_audit` absent.  No `.npy`, `.npz`, `.csv`, `.parquet`, `.h5`, or
`.hdf5` result file exists under the package after the full matrix.
- The README and canonical conclusion remain explicit that Ticket 04 makes no
population, race, coupling-exponent, detector-measurement, outcome, scaling,
or Born-rule claim.

## Exact command and log matrix

```sh
/usr/bin/time -l python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --verbose
python3 adler_born_two_channel/verify.py
python3 -W error -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --prove-failure-exit
```

The fixture/nearby-grammar probe imported `_STALE_SCHEMA_PATTERNS`,
`_STALE_README_PATTERNS`, and `_STALE_FIXTURES`, evaluated all 17 exact fixtures
with `re.search(..., re.IGNORECASE)`, called `_stale_pattern_fixtures()` and
`_stale_schema_prose()`, and then evaluated the 17-row subject-first/version-
first matrix reported above.  The direct scientific command rebuilt the pooled
and matrix datasets, compared each under its frozen budgets, and printed the
schema, verdicts, reason/cell counts, digests, caps and envelopes.

The compile/raw/no-file commands were:

```sh
python3 -B - <<'PY'
from pathlib import Path
files=sorted(Path('adler_born_two_channel').glob('*.py'))
for p in files: compile(p.read_text(encoding='utf-8'),str(p),'exec')
print('compiled',len(files),'Python sources in memory')
PY

python3 -B - <<'PY'
import json,sys
import adler_born_two_channel.raw_runner
print(json.dumps({x:x in sys.modules for x in ('adler_born_two_channel.analytic','adler_born_two_channel.killed_diffusion','adler_born_two_channel.moving_band_audit')},sort_keys=True))
PY

find adler_born_two_channel -type f \( -name '*.npy' -o -name '*.npz' \
  -o -name '*.csv' -o -name '*.parquet' -o -name '*.h5' \
  -o -name '*.hdf5' \) -print
```

Round-9 logs:

- canonical/RSS:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/b9716ceb-0299-4c67-9be2-5770079cf9a1/output.log`
- verbose:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/83972242-d758-4483-981e-ab62d07e3383/output.log`
- warnings-as-errors:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/5c1d01ca-bac8-4571-bb45-86a49ccc1c7e/output.log`
- direct script:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/4c41d733-8229-466f-9f45-782c28a75eff/output.log`
- deliberate failure:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/f6249fe9-fc2a-49dd-938c-51eed8c6086d/output.log`
- hash seed:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/ac77e609-b74d-4280-aa6c-cf07e079d516/output.log`
- direct scientific extraction:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/01c9afb6-6af5-4cf8-b02f-e5688e12d5a8/output.log`

No implementation file was edited, staged, committed, or reverted.  This
round-9 closure section is the only durable write made by this review.

# Final independent closure review — scoped grammar round 10

## Strict verdict: CLOSED

No actionable finding survived review.  The version-first rule is now
tense-aware within its documented scope, all 28 fixtures discriminate in the
declared direction, the real three-source scan is clean, and the full numerical
and operational matrix is unchanged.  Ticket 04 is closed.

## The exact grammar boundary passes

The four historical version-first sentences now remain legal:

```text
Before v4, a v3 report was accepted
Historically, a v2 report carried one envelope
A v1 report had no dataset digest
A v3 report was replaced by v4
```

The three parallel current claims still reject:

```text
A v2 report is the current format
A v3 report defines the live schema
A v1 report remains active
```

The added boundary fixtures also behave exactly as declared:

- `a v2 report always carries one envelope` rejects;
- `a v2 report has been superseded` accepts;
- `a v3 report is no longer accepted` accepts;
- `a v1 report used to carry a single envelope` accepts; and
- the original `The exact top-level keys a v2 report carries` still rejects.

An independent loop evaluated every row of `_STALE_FIXTURES` against
`_STALE_SCHEMA_PATTERNS + _STALE_README_PATTERNS`: fixture count **28**, zero
`caught != expected` rows.  `_stale_pattern_fixtures()` returned `[]`,
`_stale_schema_prose()` returned `[]`, and `check_readme()` returned pass with
all 17 required statements, three scanned prose sources, and all 28 fixtures
held.

The implementation and documentation agree on the scope
(`verify.py:17617-17717`): the checker recognizes explicit current/live schema
assertions and fully qualified old numerical-validation identifiers; it uses
tense to distinguish the historical forms its fixture table promises.  It also
states the cost of that boundary—natural-language history beyond the pinned
grammar remains a human-review concern.  Round 10 explicitly asked this review
not to turn that declared contract into an open-ended language challenge, and
the exact contract is now correct.

The exclusion of `verify.py` remains accurately documented and acceptable.
That source intentionally contains old-tag parser mutations and the stale-text
fixture table, so scanning it would report its own test data.  The round-9
manual review of every non-fixture v1-v3 occurrence found only physical-key
history, old-shape rejection tests/results, and explanatory prose about the
checker; round 10 introduces no contrary live-schema assertion.

## Unchanged schema, numerical results and nonclaims

- Canonical, verbose, direct-script, and warnings-as-errors runs each returned
**85/85**, exit 0.  The deliberate failure probe returned **85/86** and exit
- A valid report declares `dk-numerical-validation/v4` and round-trips through
the rooted parser.  Substituted v1, v2 and v3 schema tags each refuse.
- Stationary residuals remain `4.537e-04 / 1e-03` for the limiting solution,
`7.810e-02 / 5e-01` for endpoint refinement, and
`1.458e-02 / 1e-01` for the audit row.
- The 84 deterministic PASS rows are byte-identical between rounds 9 and 10.
Under `PYTHONHASHSEED=0` and `987654321`, both full runs produced 85 PASS
rows; their 84 deterministic rows were identical with SHA-256
`09ec837206b45278effe5babdc0585246e5f47f973f846e3b4ea09c32ef3662a`.
- Direct recomputation preserves pooled `numerical_no_result` with one reason,
dataset digest
`a1b71abec7557997554a0682b40cdef9e97be72e59b63cdbce9cb3ad5b503d14`
and budget digest
`aeb97e3c0c7e5f757fa3f6fed5872bc3b1573570c9d673ca24415290aabd9257`.
Per-regime remains `numerical_no_result` with 33 reasons across 14 of 15
cells, dataset digest
`beffd0afd886ba752846dd66b660ca150c4017a5f38b8de717c9ba4c21e959a7`
and budget digest
`6840ff143b07b7a6deb221d0933728f7a11648075aecdab928d1431b3b45b844`.
- Every convergent audit observable retains absolute cap `0.10` and its prior
floor.  `added_resets_mean` alone retains `(3.0, 30.0, 0.0)` with
`require_decrease=False`.  Pooled probability/time/count envelopes remain
`0.014583333333333282`, `0.011200000000000876`, and `0.98125` with unchanged
standard errors.
- Canonical maximum RSS was 603,652,096 bytes (575.7 MiB), peak footprint
188,187,632 bytes, below the 900 MiB gate.  All 15 package Python sources
compiled in memory.
- A fresh raw import left `analytic`, `killed_diffusion`, and
`moving_band_audit` absent.  No `.npy`, `.npz`, `.csv`, `.parquet`, `.h5`, or
`.hdf5` result file exists under the package after the complete matrix.
- The README and canonical conclusion remain explicit that Ticket 04 makes no
population, race, coupling-exponent, detector-measurement, outcome, scaling,
or Born-rule claim.

## Exact command and log matrix

```sh
/usr/bin/time -l python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --verbose
python3 adler_born_two_channel/verify.py
python3 -W error -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --prove-failure-exit
```

Fixture verification used a direct Python loop over all 28
`_STALE_FIXTURES`, with `re.search(..., re.IGNORECASE)` over
`_STALE_SCHEMA_PATTERNS + _STALE_README_PATTERNS`, followed by direct calls to
`_stale_pattern_fixtures()`, `_stale_schema_prose()`, and `check_readme()`.
The direct scientific command rebuilt `_audit_dataset()` and
`_matrix_dataset()`, compared each under its frozen budgets, and printed the
live schema, verdicts, reason/cell counts, digests, caps and envelopes.

The compile/raw/no-file commands were:

```sh
python3 -B - <<'PY'
from pathlib import Path
files=sorted(Path('adler_born_two_channel').glob('*.py'))
for p in files: compile(p.read_text(encoding='utf-8'),str(p),'exec')
print('compiled',len(files),'Python sources in memory')
PY

python3 -B - <<'PY'
import json,sys
import adler_born_two_channel.raw_runner
print(json.dumps({x:x in sys.modules for x in ('adler_born_two_channel.analytic','adler_born_two_channel.killed_diffusion','adler_born_two_channel.moving_band_audit')},sort_keys=True))
PY

find adler_born_two_channel -type f \( -name '*.npy' -o -name '*.npz' \
  -o -name '*.csv' -o -name '*.parquet' -o -name '*.h5' \
  -o -name '*.hdf5' \) -print
```

Round-10 logs:

- canonical/RSS:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/ec9ac496-c9f7-4a7d-82d0-aad2b668a06c/output.log`
- verbose:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/a98413b8-9e06-4abf-b90b-e51992fc6520/output.log`
- warnings-as-errors:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/d62ab19c-9561-4f81-96d7-8398e16e9175/output.log`
- direct script:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/dad2c8fd-d465-4f99-b3f5-dbecbe847669/output.log`
- deliberate failure:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/b8d3ac2d-4dbe-44ed-b935-0fd817658de8/output.log`
- hash seed:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/3675ce84-b3ee-4f2a-bf34-24ac501a1473/output.log`
- direct scientific extraction:
`/Users/john-bramble/.traycer/commands/c443d91e-b0d5-43ff-a31b-805574ab7771/7586cecd-2bbb-42c0-b837-cf82dd0632b8/output.log`

No implementation file was edited, staged, committed, or reverted.  This
round-10 closure section is the only durable write made by this review.
