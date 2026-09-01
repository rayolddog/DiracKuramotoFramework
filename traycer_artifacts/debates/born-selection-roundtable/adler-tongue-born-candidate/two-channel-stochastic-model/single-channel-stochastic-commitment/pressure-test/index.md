---
title: "Pressure test: single-channel stochastic commitment plan"
kind: review
---

# Pressure test: single-channel stochastic commitment plan

## Review target

[Single-channel stochastic phase noise and fixed-dwell commitment](..)

## Review purpose

Attack the plan before implementation. Prioritize assumptions or test designs that could:

- manufacture coupling-squared behavior;
- prevent a negative result from being interpretable;
- confuse numerical cutoff behavior with physical white-noise behavior;
- make the fixed-dwell rule arbitrary or non-convergent;
- mishandle finite physical clock population;
- hide censoring, saturation, or post-selection in hazard/exponent fits;
- create analytic leakage into event generation;
- produce unreasonable memory or runtime requirements; or
- contradict the calibrated deterministic package or parent two-channel plan.

Use concrete counterexamples and propose the smallest corrective changes. Distinguish blockers that must be resolved before implementation from controls that can remain later sensitivity work.

## Verdict

**Do not implement the production experiment from this plan yet.** The calibrated deterministic substrate is sound — the current `adler_born_two_channel` suite passes all 26 checks — but the stochastic contract is not yet sharp enough to distinguish a rate-weighted-tongue mechanism from a quadratic-looking threshold crossover or a discretization artifact.

The plan is salvageable without changing its scientific question. Seven load-bearing corrections are needed first: fix the dwell clock semantics; make the white-noise exit functional convergent and independently benchmarked; prevent the lock band from admitting the repelling branch; predeclare the statistical estimand and pilot firewall; settle finite-population and analytic normalization semantics; extend analytic isolation to the new runtime boundary; and design a feasible paired-refinement/RNG/data path.

## Blockers before implementation, in priority order

### 1. The proposed dwell counter is internally inconsistent and does not define a fixed physical dwell

The state machine says to add one full timestep at every eligible inside-band sample and commit when the counter reaches the dwell. Experiment S2 separately requires that an initial inside-band sample start dwell without committing instantly. Those requirements conflict.

Concrete counterexample: let `dwell = dt` and let the first evaluated sample be inside the band. Steps 6 and 8 add `dt` and commit at that same sample, while S2 says it must not. When `dwell / dt` is non-integral, `ceil(dwell / dt) * dt` silently becomes the actual dwell, so every refinement level tests a different commitment rule. Whether membership is evaluated at `t_n` or `t_{n+1}` is also unspecified, and the moving stable target is singularly fast near tongue entry/exit.

**Required correction:** define dwell by timestamps, not accumulated sample counts. An inside sample records `inside_since = t_sample`; it never receives retroactive credit for the preceding interval. Commit at the first later sample with `t_sample - inside_since >= tau_dwell`. Define the event as interval-censored to the last step and use the same end-of-step ordering everywhere: evolve to `t_{n+1}`, evaluate eligibility and the target at `t_{n+1}`, then update the state machine. Split steps at the exact deterministic eligibility crossings already provided by `RaisedCosinePulse.eligibility_window`, or prove that not doing so is within the declared event-time tolerance. S2 must test `tau < dt`, `tau = dt`, non-integral `tau/dt`, first-sample-inside, and falling-edge loss.

### 2. Endpoint-only sampling needs a continuum benchmark; a visual “plateau” is not evidence of white-noise convergence

For a continuous Brownian path, “remain inside for an uninterrupted dwell” is an exit-time functional. Endpoints can both be inside while the path exits and returns between them, which endpoint accounting falsely counts as uninterrupted dwell. This error is concentrated near the band boundary and can produce a convincing false plateau under adjacent timestep halvings.

Concrete counterexample: for `dphi = sqrt(2D) dW`, an upper boundary at `a = 0.1`, endpoints `x = y = 0.09`, `D = 0.01`, and `dt = 0.01`, the conditional probability that the Brownian bridge crossed the upper boundary between those two inside endpoints is

`exp(-(a-x)(a-y)/(D*dt)) = exp(-1) = 0.368`.

Endpoint accounting calls every such segment continuously inside. The moving two-sided band is harder, not easier, and its center moves fastest near tongue entry and exit.

**Required correction:** keep endpoint sampling as the primary generator if desired, but add an independent stationary killed-diffusion benchmark before accepting it. For fixed coupling and a fixed band, compare the sampled uninterrupted-dwell survival/commit law against either a Brownian-bridge audit or a PDE/spectral first-exit calculation. Predeclare absolute and relative tolerances for commitment probability, survival quantiles, reset counts, and winner mismatch across at least three paired refinement levels. A Brownian-bridge audit is a numerical validation control, not a rescue of the primary result. Failure to converge is a numerical no-result, not scientific falsification.

### 3. A fixed angular band can count the repelling fixed point as “locked” near the tongue edge

Inside the Adler tongue the stable and unstable fixed points coalesce at the boundary. Any fixed positive symmetric tolerance eventually encloses both. The state machine then awards dwell to phases that are close in angle to the stable point but locally repelling, exactly where the plan expects critical slowing to suppress commitment.

Concrete counterexample: with `K = 1`, `Delta = 0.999`, the stable phase is `1.5261` rad and the unstable phase is `1.6155` rad; their separation is only `0.08945` rad. A fixed tolerance of `0.1` rad declares the unstable fixed point inside the lock band. Noise is not needed for the mistake, and the slow drift near the saddle-node can let the false lock survive a short dwell.

**Required correction:** settle what “locked” means before coding. The smallest defensible rule is proximity to the stable target **and** instantaneous local contraction (for example, require the phase to lie on the contracting side, not merely within circular distance). The alternative is a predeclared edge exclusion such as stable/unstable separation greater than twice the tolerance. Either choice changes the effective tongue and must be applied identically across couplings and reflected in the isolated predictor. Add deterministic tests at the stable point, unstable point, both sides of the separatrix, and a sequence approaching `|Delta|/K -> 1`.

### 4. The primary scaling estimand and pilot procedure can select a quadratic-looking crossover

“Fit the coupling dependence” does not identify the response variable, likelihood, window, weighting, or lack-of-fit test. Commitment probability `q`, cumulative hazard `H = -log(1-q)`, early-time hazard, and median time do not share an exponent once there is censoring or saturation.

Even if the true endpoint cumulative hazard is exactly `H = a K^2`, the log-log slope of the observed commitment probability is

`d log(1-exp(-aK^2)) / d log K = 2x/(exp(x)-1)`, where `x = aK^2`.

It is about `1.16`, not `2`, at `H = 1` and tends to zero in saturation. Conversely, a one-clock noise-driven threshold curve can have a local log-log slope of two in its crossover even though no tongue-width factor exists. A pilot instructed to choose the nonzero/nonsaturated range can therefore choose precisely the region where a flexible threshold response looks quadratic.

Fixed physical `D`, pulse duration, dwell, and band tolerance do prevent an explicit `K` from entering those rules, but they do not create scale invariance. After nondimensionalizing by `K`, the experiment changes `D/K`, `K*tau_dwell`, and `K*T_pulse` across the sweep. A single fitted exponent is therefore a local summary unless curvature is rejected.

**Required correction:**

- Make the primary estimand the endpoint cumulative-hazard exponent fitted directly to binomial counts with a complementary-log-log likelihood, `log(-log(1-q_K)) = alpha + p log K`; do not transform empirical 0/1 proportions and feed them to the existing unweighted `analytic.fit_log_log_exponent`.
- Retain every coupling, including zero-event and all-event cells, in the likelihood. Report raw counts, `q`, `H`, uncertainty, deviance/lack of fit, and local slopes or a curvature term. If the power or fit fails, report no exponent.
- Freeze the coupling grid, trial count, primary `D`, dwell, tolerance, pulse, `N`, fit model, exclusion rules, and seed namespaces in a signed/hashed manifest before production. The pilot may choose a range using predeclared minimum expected event and survivor counts; it may not tune an exponent-friendly window or any physical/state-machine parameter. Production data and later sensitivities may not revise the primary analysis.
- Promote two mechanism-negative controls: fit the same coupling sweep for one central clock (`Delta = 0`), where tongue widening is absent, and run a width-only synthetic control that preserves eligibility geometry while removing `K`-dependent interior contraction. A quadratic central-clock result or a quadratic width-only result defeats the claimed width-times-rate explanation even if the population result is quadratic.
- Treat the shifted instantaneous analytic sum as a heuristic, not a derived dwell hazard. A commitment at `t` depends on the whole path over `[t-tau, t]`; two pulses with the same predictor at `t-tau` but different intervening closure can have different hazards. Mechanistic support should require an out-of-sample time-resolved match, including rising/falling asymmetry and winner mismatch, not just the endpoint exponent.

### 5. Finite-population semantics are mixed with continuum quadrature semantics

The current analytic package correctly exposes two different objects: `tongue_rate_sum`, the bare finite-clock sum, and `tongue_rate_flux = spacing * sum`, the continuum quadrature. The plan alternates between “sum” and “flux” without declaring which is the comparator. They differ by a population-density factor and answer different questions when `N` changes.

The midpoint grid also has load-bearing parity and offset effects at low coupling. With support `[-10, 10]`, `N = 100` has nearest detunings `+/-0.1` and zero eligible clocks at `K = 0.09`; `N = 101` contains a central zero-detuning clock and has one eligible competitor at the same `K`. That is a discontinuous change in the ledger and fitted onset caused only by parity. As `K` crosses grid nodes, eligible count is a staircase, so an exponent is not meaningful unless the primary tongue contains enough cells.

The existing analytic safe range requires `K_min >= 200h`. With `h = 2W/N`, a decade-wide sweep and `W > K_max` imply roughly `N > 4000` if that same safety criterion is imposed on the physical event grid. That feeds directly into the runtime blocker below.

**Required correction:** declare the bare finite-population sum on the exact production detunings as the primary analytic comparator; use spacing-weighted flux only as a separately labeled continuum control. Freeze `N`, support, parity, grid origin, and every coupling node. Predeclare a minimum eligible-cell count at `K_min` or narrow the scientific claim to a discrete population with visible staircase predictions. Across `N`, compare the observed change to the bare-sum change rather than expecting raw probability invariance.

Also fix the per-clock diagnostics: because the trial stops at the first commitment, entry/reset counts for nonwinners are informatively censored. A central clock committing at `t = 0.2` prevents observing an edge clock that would enter at `t = 0.5`; zero recorded edge entries do not mean edge entry was impossible. Store per-clock exposure until stop and report exposure-normalized pre-event statistics, or run a small no-stop shadow sample for mechanism diagnostics.

### 6. The stated analytic isolation is not enforced by the current package boundary

The calibrated code enforces a useful accidental-leakage check for `model.py` and deterministic `simulate.py`, and those checks currently pass. The new plan, however, adds commitment/stochastic/reporting modules that the verifier does not scan. More importantly, `adler_born_two_channel/__init__.py` eagerly imports `analytic`, so every ordinary submodule import initializes the package with the predictor loaded. That contradicts the stronger child-plan statement that the analytic module is read only by the reporting layer.

**Required correction:** leave the calibrated deterministic modules intact; add a pure `commitment.py` and a separate stochastic event runner with a narrow validated configuration containing only physical/numerical inputs and seeds. Remove the eager analytic import from the package root or move event generation behind a top-level package/process that cannot load it. The raw-run process should write an immutable ledger and exit; a separate comparison process may then import `analytic.py` and read the closed ledger. Extend the AST/import allowlist and runtime namespace checks to every module transitively reachable from the event runner, and reject predictor/hazard callbacks or arbitrary comparison objects at the event API. This is isolation against accidental manufacture, not a security sandbox, and should be described that way.

### 7. Paired refinement, common random numbers, and the production matrix have no feasible execution/data design

The computational work is proportional to `trials * clocks * fine_steps * parameter_cells`. The plan supplies none of those values, no precision target for the exponent, and no throughput or memory gate. If `N = 4000` and a fine pulse needs `50,000` steps, materializing one trial's Gaussian increments is already `1.6 GB` as float64; a batch of 64 is `102.4 GB`. A not-unusual `20,000`-trial cell is four trillion clock-steps before the timestep, noise, dwell, tolerance, duration, population, phase, and spectrum sensitivities multiply it.

“Generate the finest increments once” is therefore not an implementation detail. Naively pre-generating the Brownian cube is infeasible, while drawing only for active clocks or stopping early changes random-number consumption across couplings and refinement levels. Common random numbers across coupling points also make fitted points correlated; ordinary independent-error regression understates uncertainty.

**Required correction:** specify a counter-based or stable seed hierarchy keyed by dataset/trial/clock/fine-step so early stopping and batching cannot alter a stream. Stream fine increments in time blocks and advance all requested refinement levels in lockstep by exact summation; never materialize the trial-by-clock-by-time cube. Batch only the live phase/dwell state, event times, and online diagnostic histograms. Estimate exponent uncertainty by resampling the common master-trial IDs (or use independent coupling streams), not by treating coupling cells as independent.

Before production, benchmark clock-steps/second and peak memory, perform a pilot-based power calculation for a declared confidence width on `p`, and publish a finite run matrix and storage estimate. Make S6 staged, not an accidental full factorial: numerical convergence first, then a small set of predeclared one-factor physical falsifications, with expansion only if the primary run is interpretable.

## Controls that can follow a correct core implementation

These are important, but they need not block coding once the seven contracts above are settled. They must still be frozen before any associated production claim.

1. **Grid-realization controls:** shift the midpoint grid by fractions of a cell, compare even/odd `N`, and jitter detunings once while holding that physical realization fixed across couplings. Large exponent movement means the “finite population” result is grid construction, not a stable detector law.
2. **Endpoint audit on the moving band:** after the stationary continuum benchmark passes, compare primary endpoint accounting with a Brownian-bridge or conservative boundary audit on a reduced pulsed matrix. This quantifies the residual moving-boundary error rather than assuming the stationary result transfers.
3. **Stationary burn-in semantics:** define the stationary control as left-truncated survivors with dwell age carried through burn-in, or explicitly reset states and call it a prepared ensemble. Discarding burn-in commitments and silently resetting dwell conditions on a selected survivor population.
4. **Hazard terminology and censoring:** `events in bin / risk at bin start` is a discrete conditional failure probability, not a rate; dividing by bin width (or using the exact discrete-to-continuous conversion) is required before comparison with a quantity having units of inverse time. Event times are interval-censored at `dt`; pulse end is administrative right-censoring. Report risk counts and bin widths with every curve.
5. **Prepared-phase and no-stop controls:** retain the planned alternative phases, and use a limited no-stop shadow run to separate intrinsic mismatch behavior from truncation by the first winner.
6. **Structured spectra and two-channel progression:** proceed only if the single-channel event law passes the numerical audit, the central-clock and width-only negative controls, and the predeclared fit diagnostics. A quadratic endpoint alone is not a gate to two-channel competition.

## Minimum amended implementation contract

Implementation can begin when the parent/child plans record these settled choices:

| Contract | Minimum decision |
| --- | --- |
| Dwell | Timestamp-based `inside_since`; end-of-step ordering; exact semantics for non-integral `tau/dt` |
| Lock | Stable proximity plus a settled contraction/separatrix rule near the tongue edge |
| White-noise convergence | Stationary continuum benchmark, paired three-level tolerance, moving-band audit |
| Primary statistic | Binomial complementary-log-log exponent with curvature/lack-of-fit and all cells retained |
| Pilot firewall | Frozen manifest; pilot selects information-bearing range only; independent production namespace |
| Mechanism controls | Central one-clock and width-only controls must fail to look quadratic for a width-times-rate claim |
| Finite population | Bare sum on exact grid primary; flux labeled continuum-only; parity/cell-count declared |
| Isolation | Raw event process cannot load analytic; all event-reachable modules scanned |
| RNG/refinement | Stable keyed streams; streamed fine increments; common-random-number-aware uncertainty |
| Feasibility | Measured throughput/memory, power-based trial count, finite staged run matrix |

Until those are explicit, a positive quadratic fit is not causally attributable to the rate-weighted Arnold tongue, and a negative fit is not distinguishable from an ill-defined dwell functional, edge-lock misclassification, censoring, or inadequate numerical resolution.

## Revision disposition — 2026-08-26

The parent plan was revised after the user accepted all minimum contracts and explicitly selected:

- stable proximity plus local contraction for the lock definition; and
- an independent stationary killed-diffusion benchmark for continuous dwell survival.

All seven blocker classes are now addressed in the revised [single-channel plan](..): timestamp dwell and end-of-step ordering; continuous killed-diffusion oracle and moving-band audit; contraction guard; binomial complementary-log-log estimand, curvature/lack-of-fit and pilot firewall; exact-grid finite bare sum with parity/exposure controls; closed-ledger process isolation; and counter-keyed streamed RNG with feasibility/power gates.

This disposition means the plan is ready to be broken into implementation tickets. It does not mean any stochastic contract has yet been implemented or verified.

## Closure review — 2026-08-26

### Overall verdict: NOT READY FOR TICKETS

Five of the seven original blockers are closed at plan level. Two remain open because the revision names required controls without defining the algorithms that generate their evidence. Those choices can materially change whether the mechanism passes, so they are technical-plan decisions rather than ordinary ticket-level implementation judgment.

The current calibrated package remains a sound baseline: its deterministic/analytic suite passes 26/26 checks. It still intentionally contains no stochastic commitment code, and its package root still eagerly imports `analytic`; the revised plan correctly makes removal of that access the first implementation boundary. Those are expected implementation gaps, not additional plan blockers.

| # | Original blocker | Status | Exact revised section / evidence | Concrete remaining deficiency |
| --- | --- | --- | --- | --- |
| 1 | Timestamp dwell semantics | **CLOSED** | **Lock and fixed-dwell state machine**, steps 1–8: evolve to `t_{n+1}`, evaluate there, set `inside_since` on the first qualifying sample with no retroactive credit, and commit only when timestamp difference reaches the physical dwell. It also specifies interval censoring, exact eligibility-crossing handling, non-integral dwell/step behavior, S2 edge cases, and verification checks 10–14. | None at plan level. The implementation ticket should encode these steps literally. |
| 2 | Killed-diffusion convergence and moving-band audit | **OPEN** | **Between-step lock-band crossings** and **Experiment S3** now define an independent stationary absorbing-boundary PDE/spectral oracle, several initial positions, at least three paired refinements, frozen absolute/relative tolerances, and a numerical-no-result gate. Verification checks 21–24 carry the gate forward. The pulsed section additionally requires a reduced “endpoint-versus-conservative-exit audit.” | The stationary oracle is defined well enough, but the moving-band comparator is not. “Conservative-exit audit” has no mathematical rule, reference path, bound direction, or acceptance statistic. Different conservative rules can reject radically different path sets and move the exponent. Before ticketing, select and state the audit algorithm—for example, a diagnostic Brownian-bridge crossing calculation against piecewise-linear moving boundaries, or an explicit safety-envelope rule—and specify which primary observables it bounds/compares and the frozen tolerance relationship. |
| 3 | Contraction-safe lock near the repelling branch | **CLOSED** | **Lock and fixed-dwell state machine**, step 3 computes the instantaneous phase derivative of Adler drift and step 5 requires local contraction in addition to stable-target proximity. **Contraction guard and the repelling branch**, S2, and verification checks 18–19 cover the stable point, repelling point, expanding side, both mismatch signs, and tongue-edge coalescence. The parent plan now uses the same rule. | None blocking. In the ticket, make the implied predicate explicit as strict local contraction (`partial f / partial phi < 0`; equality earns no dwell) so the boundary case cannot be interpreted differently. |
| 4 | Cloglog estimand, pilot firewall, and mechanism-negative controls | **OPEN** | **Primary scaling estimand** defines the binomial complementary-log-log likelihood over every coupling cell, uncertainty, deviance, curvature/lack-of-fit, paired-trial resampling, and `no valid exponent`. **Experiment S5** freezes pilot count rules, separates namespaces, hashes the production manifest, and forbids tuning. **Experiment S4** makes central-clock and width-only controls mandatory; verification checks 32–35 cover estimator failure and control falsification. | The central-clock control is defined, but the width-only data-generating process is not. “Preserve eligibility geometry while removing coupling-dependent interior contraction” leaves the replacement drift, target motion, outside-tongue dynamics, and fixed reference contraction unspecified. Those choices can themselves create or remove a quadratic crossover. Before ticketing, freeze one explicit control equation and all shared parameters—for example, a declared `K`-independent contraction toward the same moving stable target while eligible, with an explicitly declared outside-tongue drift—and state that noise, dwell, initial phases, grid, pulse, and fit pipeline are otherwise identical. |
| 5 | Finite bare-sum, grid, and first-winner censoring semantics | **CLOSED** | **Complete ledger** adds per-clock exposure and a predeclared no-stop shadow sample. **Isolated comparison curves** selects the bare sum on the exact production clocks and labels spacing-weighted flux continuum-only. **Experiment S5** freezes parity, origin, support, nodes, and minimum eligible count or an explicit discrete-staircase claim; verification checks 31 and 42–44 preserve these distinctions. The current `analytic.py` already exposes separate `tongue_rate_sum` and `tongue_rate_flux` functions. | None at plan level. |
| 6 | Raw-process analytic isolation | **CLOSED** | **Isolated comparison curves**, **Codebase fit**, and implementation step 1 require a raw runner whose transitive graph cannot load analytic/oracle/reporting code, removal of the eager package-root analytic import, a closed hashed ledger, and a separate comparison process. Verification checks 36–39 extend structural/runtime checks to all raw-reachable modules and reject predictor callbacks or prescribed hazards. | None at plan level. The current eager import in `__init__.py` confirms this must be an implementation ticket and acceptance gate; it does not contradict the revised plan. |
| 7 | Streamed keyed RNG, paired refinement, runtime/data feasibility | **CLOSED** | **Stochastic integration and paired refinement** keys fine increments by dataset/trial/clock/fine-step, streams bounded time blocks, advances refinement levels in lockstep, forbids materializing the noise cube, and accounts for common-random-number correlation. **Data and reproducibility** records stream derivation and measured resource estimates. **Feasibility and power gate** requires measured throughput/memory, power-based trial count, a finite run matrix, and staged sensitivities before production. Verification checks 1–7, 40–41, and 47 enforce the design. | None at plan level. Actual throughput, memory, and power values are correctly deferred to the implementation benchmark gate rather than assumed in the plan. |

### Load-bearing corrections still required

1. Define the reduced moving-band exit-audit algorithm and its pass/fail comparison to the primary endpoint scheme.
2. Define the width-only control as an explicit stochastic differential equation/state transition, including eligible and ineligible drift, target motion, and the fixed contraction parameter.

The earlier unqualified revision disposition is therefore superseded by this closure review. Once these two definitions are added without weakening the existing gates, the plan is ready for ticket breakdown.

## Plan amendment submitted for final closure — 2026-08-26

The [single-channel plan](..) now supplies both missing definitions. This section records the amendments; it does not mark the review closed on the reviewer's behalf.

### Blocker 2 amendment: piecewise-linear Brownian-bridge moving-band audit

The revised audit now has a fixed algorithm and comparison direction:

- the endpoint Euler–Maruyama history remains the primary result;
- every exact deterministic tongue crossing splits the interval;
- on an eligible fine interval, the proximity-plus-contraction lock boundaries are represented continuously and linearly between endpoints;
- conditional one-sided Brownian-bridge crossing probabilities are computed for each moving boundary;
- the two probabilities are combined by a capped union bound and sampled with a separately keyed audit uniform;
- an audited crossing may only add a dwell reset, so audited commitments are a pathwise subset of endpoint commitments; and
- ambiguous geometry resets conservatively instead of selecting a favorable branch.

The plan explicitly limits the mathematical claim: this is conservative for the frozen-drift discretized bridge, not a rigorous bound on the nonlinear continuous process. The stationary killed-diffusion solver remains the continuum oracle.

The reduced audit matrix, three-level paired refinement, auxiliary audit replications, observables, and pass/fail relationship are now frozen in advance. Audit-induced changes must fit both declared absolute/relative caps and a numerical budget no larger than one quarter of the planned production uncertainty; commit-time quantiles additionally receive one finest-timestep allowance. The bridge record cannot replace the raw ledger, tune the production step, or rescue an exponent. Failure produces timestep refinement or a numerical no-result.

### Blocker 4 amendment: fixed-contraction width-only control

The revised control now has one explicit state transition:

- outside eligibility, absolute phase follows free mismatch drift plus the same white-noise increment;
- at exact entry, phase is converted to signed error from the same Adler moving target;
- while eligible, that error is pulled toward zero by one fixed positive rate times the sine of the error, with the same noise increment;
- absolute phase is reconstructed by adding the moving target, so target motion is preserved;
- at exact exit, the reconstructed phase is carried continuously back to free mismatch drift; and
- its contraction guard is strict and uses the derivative of this fixed-rate restoring flow.

The pre-pilot template freezes the rule that makes the reference rate the central-clock Adler relaxation rate at the geometric midpoint of the later frozen production peak-coupling range. The range-only pilot therefore cannot tune the rate by inspecting stochastic behavior. The resulting rate is written into the production manifest and is common to every clock, coupling, pulse time, and trial. The exact grid, eligibility, target, phases, noise streams, dwell, stop rule, ledger, and fit pipeline are paired with the full model.

The control has a predeclared power-based defeat rule: a statistically adequate quadratic width-only response, failure of the paired full-minus-control exponent contrast to exceed the frozen mechanistic difference, or equal/better out-of-sample time-resolved performance blocks the width-times-rate interpretation. It cannot trigger post-result retuning of the fixed rate.

### Current disposition

The two plan-level deficiencies identified by the closure review have been addressed in the planning artifact. Ticket breakdown remains pending a cold final closure check that the definitions are internally consistent and have not weakened the other five contracts.

## Final cold closure review — 2026-08-26

### Strict verdict: OPEN

The moving-band audit blocker is closed. The width-only control is substantially specified, but one causal-isolation contradiction and its associated circular-coordinate handoff remain plan-level blockers. No new blocker was found in the other five closed contracts.

The current deterministic package again passes 26/26 checks. In particular, its calibrated Adler drift is `Delta - K(t) sin(phi)` whether or not a clock is tongue-eligible; eligibility controls whether a stable target exists, not whether the coupling term acts. That existing behavior is load-bearing for the remaining finding.

### 1. Diagnostic moving-band bridge audit — CLOSED

The revised **Between-step lock-band crossings** section now supplies the missing contract:

- exact deterministic tongue entry/exit splits, with no bridge across eligibility changes;
- strict boundary equality handling: proximity or contraction equality is outside and resets;
- continuous local circular representatives, with conservative reset on ambiguous representation, disappearing interval, or within-step topology change;
- the correct one-sided bridge expression for additive variance `2 D_phase dt` against linearly moving boundaries;
- an explicit zero-diffusion branch returning zero bridge-crossing probability after endpoint/topology checks;
- a capped two-sided union bound whose conservatism is limited honestly to the frozen-drift discretized bridge, not claimed for the nonlinear continuum process;
- a separate immutable audit namespace, so auxiliary uniforms cannot perturb the physical Brownian stream;
- reset-only directionality, making audited commitments a pathwise subset of endpoint commitments;
- a frozen reduced matrix, auxiliary replications, all relevant observables, paired timestep halving, and absolute/relative budgets tied to no more than one quarter of planned production uncertainty; and
- a numerical-no-result outcome if refinement cannot meet those budgets.

This does not weaken the stationary killed-diffusion oracle: the plan still names that solver as the continuous-time authority and the bridge as a diagnostic approximation. It also does not alter the primary raw ledger or permit timestep/exponent selection. The union-bound interpretation, zero-noise limit, exact crossing split, circular topology failure path, stochastic namespace, comparison direction, and refinement gate are now explicit enough for tickets.

### 2. Fixed-contraction width-only control — OPEN

The amendment closes most of the former ambiguity. It now defines the fixed sinusoidal restoring flow in target-relative error, exact entry/exit splitting, strict contraction equality, target reconstruction, a single manifest-frozen rate, paired initial phases/Brownian streams, and a power-based causal defeat rule. The pilot still cannot inspect production stochastic behavior or refit the reference rate.

Two connected deficiencies remain:

#### A. The control changes ineligible dynamics despite claiming that only eligible drift changes

The plan says, “Only its deterministic drift while eligible is changed,” but then specifies free mismatch drift outside the tongue:

```text
phase_next = phase + mismatch * step_duration + noise_increment
```

The calibrated full model instead continues to apply `mismatch - K(t) sin(phase)` outside the tongue. For a marginal clock on the rising edge, the subthreshold Adler pull changes slip speed and the phase delivered to exact tongue entry. The proposed control removes that pull, so a paired full-minus-control difference can arise from a different entry-phase distribution as well as from removal of coupling-dependent interior contraction. The frozen exponent contrast therefore does not isolate the factor it is claimed to test.

**Required correction:** choose one causal contract and make the prose, transition, and defeat rule agree. For the stated “remove only coupling-dependent interior contraction” contrast, preserve the full calibrated Adler transition while ineligible and replace only the eligible transition with the fixed-contraction target-relative flow. If free drift outside is scientifically intended instead, rename and reinterpret the control as a broader eligibility-only null; it cannot support a causal full-minus-control attribution specifically to interior relaxation speed.

#### B. The absolute/relative transform does not preserve an explicit continuous lift

At entry the plan maps an unwrapped absolute phase to the *shortest* signed circular error. Reconstructing `phase = moving_target + error` can then differ from the incoming unwrapped phase by `2 pi m`. The text requires continuity at exit but does not store the winding integer or define a continuous lift of target-relative error. A phase just across the `-pi/pi` cut can therefore jump by one turn at entry or exit even with zero diffusion.

**Required correction:** retain a winding/lift offset when converting coordinates, or keep unwrapped absolute phase as the authoritative state and derive the target-relative error without discarding its continuous branch. Specify that exact entry, exact exit, re-entry, both mismatch signs, zero diffusion, and phases straddling the circular cut preserve absolute continuity modulo only the deliberately retained winding. Add the corresponding synthetic transition checks to the width-control contract.

### Effect on the other five closed contracts

Neither amendment weakens timestamp dwell, contraction-safe boundary equality, cloglog/pilot separation, finite-grid bare-sum and censoring semantics, raw-process analytic isolation, or streamed keyed physical RNG/feasibility. The bridge uses a separate non-primary namespace and reset-only replay; the width-control rate is deterministic and manifest-frozen, not an analytic hazard supplied to the primary event generator. The parent plan is consistent with the new high-level bridge and fixed-rate requirements, but it repeats the free-ineligible-drift choice and therefore does not resolve the causal-isolation contradiction.

### Closure condition

The review becomes **CLOSED** when the plan (1) makes the ineligible width-control drift consistent with its stated causal contrast and (2) defines a continuous absolute/relative phase lift across exact entry, exit, and re-entry. No other plan-level blocker remains in scope.

## Narrow plan amendment submitted for closure — 2026-08-26

The [single-channel plan](..) and its [parent plan](../..) now incorporate both required corrections. This records the new specification without changing the reviewer's OPEN verdict; closure still belongs to a fresh cold check.

### Causal-isolation correction

The width-only control now uses the complete calibrated Adler drift whenever the clock is ineligible:

```text
phase change = (mismatch - instantaneous coupling * sin(unwrapped phase))
               * step duration
               + paired noise increment
```

Eligibility continues to control only whether a stable target exists and dwell may accrue. It no longer switches the coupling term off. The fixed-rate substitution begins at exact tongue entry and ends at exact tongue exit, so the control and full model deliver identical paired phase histories up to entry. Any later paired difference is caused by the eligible-region substitution or its downstream consequences.

### Continuous-lift correction

One unwrapped absolute phase is now authoritative through the entire trajectory. At entry, the principal target is shifted by an integer number of turns to the nearest continuous lift; the half-turn tie uses the fixed half-open interval from minus pi inclusive to plus pi exclusive. Both the lifted target and the unwrapped difference are stored, and their sum must equal the incoming absolute phase exactly.

While eligible, the target follows its continuous lifted branch and the unwrapped difference receives the fixed-rate restoring drift and paired noise. At exit, the already reconstructed unwrapped absolute phase is retained without conversion; only the auxiliary target/error state is discarded. Re-entry constructs a new lift from that unchanged phase. The error itself is never wrapped.

Exact crossing splits preserve the original counter-keyed Brownian increment by deterministic subdivision rather than drawing new noise. The required synthetic checks cover ineligible equality with the full model, both sides of the circular cut, both mismatch signs, zero diffusion, exit, re-entry, repeated cycles, accumulated winding, and mutations that drop the lift or substitute free mismatch drift.

### Current disposition

The two requirements named in the final cold review are now explicit in the planning artifacts. No implementation has begun. Ticket breakdown remains gated on a narrow closure review of these amendments.

## Narrow width-control closure check — 2026-08-26

### Strict verdict: OPEN

The two previously requested conceptual corrections are now present: the control preserves full Adler drift whenever ineligible, and it retains an authoritative unwrapped absolute phase with a continuous target lift and unwrapped error. However, two exact-crossing details remain implementation-blocking. Both sit inside the requested scope; no other closed contract is reopened.

### Scope A — ineligible causal isolation

**CLOSED in substance, OPEN at the exact-crossing noise split.**

The revised transition now matches the calibrated full model while ineligible:

`phase_next = phase + (mismatch - K(t) sin(phase)) dt + paired_noise`.

Because the full and control processes also share initial phase and Brownian stream, their phase histories are identical on the rising edge until the first eligible substitution. After falling-edge exit, later differences may persist through the same nonlinear ineligible Adler drift, but those are correctly downstream consequences of the earlier eligible substitution. Re-entry uses the same deterministic tongue boundary in both processes. The parent plan now states the same causal contract and no longer contradicts it.

The remaining problem is the claim that an off-grid exact crossing subdivides one assigned Brownian increment by the existing counter-keyed rule so that the children sum to the parent “without new noise.” A Brownian increment cannot in general be split deterministically in proportion to substep lengths. If a parent phase kick `xi ~ N(0, 2 D h)` is split at fraction `alpha`, proportional splitting gives the first child variance `alpha^2 2 D h`, not the required `alpha 2 D h`.

**Required correction:** define one of these equivalent valid constructions and key it identically for the full and control processes:

1. Conditional Brownian-tree split:
`xi_1 = alpha * xi + sqrt(2 D h alpha (1-alpha)) * Z_split`
`xi_2 = xi - xi_1`,
where `Z_split` has a stable physics-noise split key tied to the parent interval and crossing, not an audit/control-only namespace; or
2. Generate the two correctly distributed child increments from the keyed finest irregular grid and define the parent increment as their exact sum.

For zero diffusion both children must be exactly zero. The same construction must nest under timestep refinement and be shared by the full and control runs. Calling the split deterministic is acceptable only for deterministic key derivation, not for proportional allocation of a realized Brownian kick.

Until that rule is explicit, exact entry/exit splitting can change the noise law and the alleged paired equality before entry.

### Scope B — continuous phase lift

**CLOSED in substance, OPEN at strict eligibility equality.**

The authoritative-state contract is otherwise implementation-ready:

- absolute phase remains unwrapped and retains accumulated winding;
- entry chooses a target lift so the error lies in `[-pi, pi)`, giving a deterministic exact half-turn tie;
- `absolute phase = target lift + unwrapped error` is preserved before and after every eligible step;
- the target follows a continuous lifted branch while the error may cross any number of turns without wrapping;
- exit discards only auxiliary coordinates, not phase;
- re-entry constructs a new lift from the unchanged authoritative phase; and
- synthetic checks cover both mismatch signs, zero diffusion, both sides of the circular cut, repeated cycles, and mutation of the lift.

The exact entry instruction nevertheless says to compute the “principal stable target” at `K = |mismatch|`. In the calibrated package, eligibility is strict and `stable_phase` deliberately returns `NaN` at equality; `boundary_phase(mismatch)` supplies the limiting value `sign(mismatch) pi/2` (and zero for zero mismatch). The same issue occurs when `target_principal_next` lands exactly on the exit crossing.

**Required correction:** explicitly use the calibrated limiting `boundary_phase` at exact entry and exit, lift that finite boundary value with the declared `[-pi, pi)` tie convention, and only use `stable_phase` at strictly eligible interior times. Add a mutation check that calling strict `stable_phase` at equality fails rather than silently seeding a `NaN` lift.

### Regression check

These findings do not regress timestamp dwell, contraction boundary equality, the pilot firewall, finite-grid/censoring semantics, raw-process analytic isolation, or the previously closed bridge audit. The parent plan accurately propagates full ineligible Adler drift and continuous-lift intent; the child plan remains authoritative for the two missing exact-crossing mechanics.

### Closure condition

The width-only contract becomes **CLOSED** once the plan defines a distribution-correct, nested, paired Brownian split at arbitrary exact crossings and names `boundary_phase` as the finite target at strict entry/exit equality. No other blocker remains in this narrow scope.

## Exact-crossing amendment submitted for closure — 2026-08-26

The [single-channel plan](..) and [parent plan](../..) now define both requested mechanics. This section records the amendment without changing the reviewer's OPEN verdict.

### Nested keyed Brownian-tree split

Every off-grid exact entry or exit now splits its assigned parent phase kick conditionally. For parent duration `h`, crossing fraction `alpha`, diffusion `D_phase`, parent kick `xi`, and a separately keyed physical split normal `Z_split`, the left child is:

```text
left = alpha * xi
       + sqrt(2 * D_phase * h * alpha * (1 - alpha)) * Z_split
```

The right child is defined as `xi - left`. This gives the children their correct duration-scaled variances and preserves the parent sum by construction. The split normal belongs to the physical Brownian tree, not the bridge audit or either model. Its key includes the physical namespace, dataset, trial, clock, finest parent step, node path, and canonical crossing identity; model label is excluded.

Multiple crossings recurse chronologically through left/right node paths. The elementary mesh is the union of the finest uniform grid and deterministic exact crossings, and every coarser increment is a sum of those leaves. Full/control and fine/coarse runs therefore share one tree. Endpoint fractions create an exact zero-duration child without a random draw; zero diffusion creates exact-zero parent and descendants. Invalid crossing geometry is a hard error.

The verification contract now covers child moments, zero unconditional sibling covariance, parent conservation to machine precision, extreme fractions, repeated splits, both pulse edges, different clock crossing times, full/control pairing, refinement pairing, batching/early-stop invariance, and mutations using proportional division, an independently sampled right child, model-specific keys, or nonzero zero-diffusion descendants.

### Explicit boundary target

Exact tongue entry and exit are now a named equality state. At `coupling = absolute mismatch`, the width control calls the calibrated finite `boundary_phase(mismatch)`, including zero for zero mismatch. It never calls `stable_phase` at equality because that function deliberately returns not-a-number there.

At entry, the finite boundary value is lifted nearest the authoritative unwrapped phase. At strictly eligible interior times only, the ordinary stable phase is evaluated and continued along the stored lift. If an eligible segment ends at exact exit, the endpoint target is the lifted boundary phase. The zero-duration entry/exit coordinate handoffs change no phase and consume no noise.

Synthetic and mutation checks now require finite boundary targets for both mismatch signs and zero mismatch, reject any equality call to strict stable phase, preserve the phase-lift identity, and fail rather than allowing a not-a-number target to enter state.

### Current disposition

The two mechanics named by the narrow review are explicit in both plans. No stochastic code has been implemented. Ticket breakdown remains gated on the reviewer's final closure confirmation.

## Exact-crossing final closure — 2026-08-26

### Strict verdict: CLOSED

Both exact-crossing contracts are now implementation-ready. The parent plan propagates them without contradiction, and neither amendment reopens another contract.

### Scope A — nested keyed Brownian tree: CLOSED

Let `sigma^2 = 2 D_phase`, let the parent kick be `X ~ N(0, sigma^2 h)`, and let `Z ~ N(0, 1)` be independent. The plan defines

`L = alpha X + sigma sqrt(h alpha (1-alpha)) Z`

and `R = X - L`. Therefore:

- `Var(L) = alpha^2 sigma^2 h + alpha(1-alpha) sigma^2 h = alpha sigma^2 h`;
- `Var(R) = (1-alpha)^2 sigma^2 h + alpha(1-alpha) sigma^2 h = (1-alpha) sigma^2 h`;
- `Cov(L,R) = alpha(1-alpha) sigma^2 h - alpha(1-alpha) sigma^2 h = 0`; and
- `L + R = X` in real arithmetic.

Because `(L,R)` is jointly Gaussian, zero covariance also gives unconditional sibling independence. The second child being the residual is essential; the mutation contract rejects independent right-child sampling.

The tree construction is coherent beyond one split:

- crossings are sorted chronologically and recurse into the affected left/right child;
- each split normal is uniquely keyed by the physical namespace, trial, clock, finest parent step, ancestry path, and canonical crossing identity;
- model label is excluded, so full and width-control runs share the same physical path;
- audit randomness remains in a disjoint namespace;
- the elementary mesh is the frozen finest uniform grid union all deterministic crossings; and
- every coarse increment is a sum of the same leaves rather than a separately generated value.

This makes root/leaf ownership unambiguous within the frozen refinement manifest and supports different crossing times for different clocks without key collisions.

The boundary cases are sufficient: `alpha` equal to zero or one creates an exact-zero duration child without consuming a split normal; near-endpoint fractions remain subject to moment and conservation tests; non-finite/out-of-parent/inconsistently identified crossings fail hard; repeated splits and both pulse edges are tested; and zero diffusion produces exact-zero roots and descendants without consuming split keys.

Floating-point qualification is correct. Residual construction makes the parent identity exact algebraically, but `fl(L + fl(X-L))` is not guaranteed bit-for-bit equal to `X` for every magnitude/cancellation pattern. The plan claims conservation **to machine precision with no statistical tolerance**, not universal bit equality. That is the right contract: verification should use a deterministic few-ulp/scale-aware bound, while retaining bit-exact assertions only for zero-duration and zero-diffusion children. There is no mismatch requiring a plan revision.

### Scope B — calibrated boundary phase: CLOSED

The equality state now matches the calibrated package exactly:

- strict eligibility remains `K > |mismatch|`;
- at `K = |mismatch|`, entry and exit call `boundary_phase(mismatch)` rather than `stable_phase`;
- `boundary_phase` supplies `sign(mismatch) pi/2`, including zero for zero mismatch;
- `stable_phase` is reachable only inside the explicit strictly eligible branch;
- a segment ending at exact exit selects the finite boundary target before reconstruction;
- zero-duration entry/exit handoffs consume no noise and do not change phase; and
- mutation checks reject an equality call to `stable_phase` before a not-a-number can seed the lift.

The lifted-coordinate lifecycle is coherent with that finite target. Entry chooses the declared nearest lift under the `[-pi, pi)` half-turn convention while leaving authoritative unwrapped phase unchanged. Eligible evolution preserves `phase = target_lift + error`; the error may accumulate arbitrary winding. Exit retains the reconstructed phase and discards only auxiliary coordinates. Re-entry repeats the finite boundary lift from that unchanged phase. This covers both mismatch signs, the usual circular cut, exact half-turn ties, repeated cycles, and excursions beyond one turn.

The transition pseudocode has no path that needs `stable_phase` at equality: exact handoffs are separate zero-duration states, eligible endpoint selection explicitly branches to `boundary_phase` at exit, and interior calls are guarded by strict eligibility.

### Final disposition

The two former exact-crossing blockers are closed. All seven original pressure-test blockers are now closed at plan level. The stochastic implementation may proceed to ticket breakdown; implementation and scientific verification remain outstanding.
