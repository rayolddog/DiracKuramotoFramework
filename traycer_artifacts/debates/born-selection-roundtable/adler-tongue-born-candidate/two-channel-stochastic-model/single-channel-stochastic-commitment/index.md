---
title: "Technical plan: single-channel stochastic phase noise and fixed-dwell commitment"
kind: spec
---

# Single-channel stochastic phase noise and fixed-dwell commitment

## Purpose

Build the smallest direct event experiment that can answer this question:

<user_quoted_section>When independent white phase noise is added to the calibrated pulsed Adler clocks, does the first clock to remain inside a fixed lock band for a fixed physical dwell time behave like an event drawn from the rate-weighted Arnold tongue?</user_quoted_section>

The experiment must be able to answer **no**. It must generate events only from noisy phase paths and the dwell state machine. The event generator never receives amplitude squared, the analytic relaxation-rate sum, or a prescribed commitment hazard.

This is Experiment 2 in the [two-channel stochastic Adler plan](..). It is a one-channel prerequisite, not a Born-rule test.

## User-settled decisions

| Decision | Selected design | Consequence |
| --- | --- | --- |
| Bath | Independent additive white phase noise for every clock | Minimal effective bath; no microscopic or quantum-vacuum origin is claimed |
| Noise dependence | Same noise strength for every mismatch and coupling | Photon amplitude cannot enter through the bath law |
| Interaction | Existing raised-cosine photon-pulse envelope | Tongue opens and closes during a finite interaction |
| Lock criterion | Fixed angular band around the moving stable phase | Same criterion for every clock and coupling |
| Commitment | One uninterrupted fixed physical dwell inside the band while eligible | Coupling is not allowed to shorten the commitment requirement |
| Between-step crossings | Direct stepwise accounting remains primary; a piecewise-linear Brownian-bridge moving-band audit may only add hidden-exit resets | The audited commitments are a pathwise subset of endpoint commitments; the bridge never becomes the event generator |
| Channel event | First clock completing dwell commits the one channel | Supplies a first-passage event without two-channel competition |
| Clock population | Fixed finite population of actual competitors | Clock count is a physical sensitivity, not numerical grid convergence |
| Dwell clock | Timestamp-based `inside_since` with end-of-step evaluation | One fixed physical dwell is preserved for every timestep, including non-integral dwell/step ratios |
| Lock guard | Stable-phase proximity plus instantaneous local contraction | The repelling Adler branch cannot count as locked near the tongue edge |
| Continuum audit | Independent stationary killed-diffusion survival benchmark | Hidden white-noise exits are measured against a continuous-time oracle |
| Width-only control | Full Adler evolution while ineligible; same moving tongue and continuously lifted target with one frozen eligible contraction rate | Removes only coupling-dependent interior relaxation without changing phase delivery to tongue entry |
| Primary scaling statistic | Binomial complementary-log-log cumulative-hazard model | Uses committed/unresolved counts directly and retains zero/all-event cells |
| Finite-population comparator | Bare relaxation-rate sum on the exact production clocks | Matches actual competitors; spacing-weighted flux is continuum control only |
| Analytic isolation | Raw event process cannot load analytic prediction | A separate comparison process reads the closed immutable ledger |
| Reproducibility | Counter-keyed, time-block-streamed increments with nested Brownian-tree splits at exact crossings | Early stopping, batching, refinement, and off-grid crossing splits cannot change a clock's physical noise path |

## Revision outcome after pressure test

The [cold pressure test](pressure-test) changed what constitutes an interpretable result:

- Failure of the endpoint implementation to match the killed-diffusion benchmark or reach a predeclared timestep tolerance is a **numerical no-result**, not scientific falsification.
- Failure of the predeclared statistical model or its curvature test is **no valid exponent**, not permission to choose a friendlier fit window.
- A quadratic population result supports the width-times-rate mechanism only if a central single-clock control and a width-only control do **not** also look quadratic.
- A positive endpoint exponent alone is never enough; time-resolved rising/falling behavior and winner mismatch must agree out of sample.
- Pilot results choose only an information-bearing coupling range under frozen count rules. They cannot tune physical parameters, the state machine, the exponent window, or the analysis model.

## Non-claims

This experiment does not contain:

- a second outcome channel;
- a polarization or spatial Born-frequency comparison;
- photon-energy routing;
- absorber energy levels;
- detector amplification;
- global one-world exclusivity; or
- a microscopic derivation of the noise.

The strongest positive result would be:

<user_quoted_section>A finite population of independently noisy Adler clocks with a fixed dwell rule produces a first-commitment law consistent with the isolated rate-weighted-tongue prediction over the tested regime.</user_quoted_section>

That would justify proceeding to two-channel competition. It would not derive the Born rule.

## System being simulated

### One finite detector channel

The channel contains `N` actual clocks. Each clock has:

- one fixed frequency mismatch;
- one authoritative evolving unwrapped absolute phase;
- when the width-only control is eligible, one auxiliary continuously lifted target and unwrapped target-relative error whose sum equals that absolute phase;
- one independent random-number stream;
- one current eligibility flag;
- one moving stable phase while eligible;
- one inside-lock-band flag;
- one uninterrupted dwell counter;
- counts of band entries and dwell resets; and
- an optional commitment time.

The primary frequency-mismatch population is a symmetric midpoint grid across a declared flat support. The support must be wider than the largest pulse coupling.

Every clock is a real competitor. Refining this grid by adding clocks increases the physical number of commitment opportunities. Therefore:

- `N` is frozen within a production sweep;
- results at different `N` are labeled population-size sensitivity;
- total commitment probability is expected to change with `N`; and
- robustness means the qualitative mechanism and fitted coupling exponent remain stable, not that the raw probability converges to one `N`-independent value.

No fractional clock weight or probabilistic thinning enters the event generator.

### Initial state

At the start of the pulse support:

- clock phases are independently uniform around the circle;
- frequency mismatches use the fixed declared grid;
- all dwell counters are zero;
- no clock is committed; and
- the white-noise process begins.

Uniform phases are the primary ensemble. Alternative prepared phases are sensitivity controls, never silently substituted into production.

## Noise law

At every Euler–Maruyama timestep, every clock receives:

```text
deterministic Adler phase change
plus
an independent zero-mean Gaussian phase kick
```

The kick's standard deviation is the square root of twice the declared phase-diffusion strength times the timestep.

Consequences:

- zero noise exactly recovers the deterministic Euler limit;
- doubling elapsed time doubles unwrapped phase variance when coupling and mismatch are zero;
- different clocks have zero intended noise correlation;
- successive timesteps have zero intended noise correlation;
- noise strength is independent of pulse height, frequency mismatch, lock tolerance, and dwell time; and
- the same noise law operates whether a clock is inside or outside the tongue.

Because the noise is additive, the Ito-versus-Stratonovich distinction does not change this model. This should be stated in documentation rather than presented as an additional physical conclusion.

White noise is an effective infinite-bandwidth idealization. The timestep supplies the numerical cutoff; timestep convergence is therefore a scientific requirement, not merely a software check.

## Stochastic integration and paired refinement

Use vectorized Euler–Maruyama over all clocks.

The production timestep is not accepted until commitment probability, the full survival curve, and the winner-mismatch distribution agree across a refinement ladder.

For strong refinement comparisons, random numbers use a stable counter-keyed hierarchy. Each fine increment is identified by immutable keys:

```text
dataset namespace / trial ID / clock ID / finest-step index
```

Consequently early stopping, batch size, thread scheduling, coupling value, and refinement level cannot alter any clock's assigned stream.

- Generate fine increments in bounded time blocks rather than materializing a trial-by-clock-by-time cube.
- Obtain every coarser increment by exact summation of the corresponding fine increments.
- Advance all requested refinement levels in lockstep from the same blocks.
- Reuse the same initial phases and physical clock grid.
- Store only live phase/dwell state, event records, and online diagnostic histograms.
- Estimate uncertainty across a coupling sweep by resampling common master-trial IDs, or else use explicitly independent coupling namespaces. Never treat common-random-number cells as independent regression observations.

This separates timestep error from Monte Carlo sampling noise.

### Exact off-grid crossings: nested keyed Brownian tree

An exact tongue entry or exit can fall inside an assigned uniform timestep. Never divide that timestep's realized Brownian kick merely in proportion to the two durations: that preserves the sum but gives the children the wrong variances.

Let a parent interval have duration `h`, parent phase kick `parent_kick`, and an exact crossing at fraction `alpha` of the interval, with `0 < alpha < 1`. Use an independent standard-normal value `split_normal` from the physical Brownian-tree namespace and construct:

```text
left_kick = alpha * parent_kick
            + sqrt(2 * D_phase * h * alpha * (1 - alpha))
              * split_normal

right_kick = parent_kick - left_kick
```

This is the conditional Brownian split. The left and right kicks have the correct unconditional variances for durations `alpha * h` and `(1 - alpha) * h`, and their sum is the assigned parent kick by construction. The second child is always formed as the residual rather than sampled independently. Verify parent conservation to machine precision, with no statistical tolerance.

The split normal is additional information needed to reveal the path inside the parent interval. It is physical-noise randomness—not a bridge-audit uniform and not a control-specific correction. Its immutable key is:

```text
physical noise namespace / dataset / trial / clock /
finest parent-step index / Brownian-tree node path /
canonical crossing identity
```

The crossing identity consists of clock ID, rising-versus-falling label, pulse-manifest hash, and the exact crossing time encoded in its canonical floating-point representation. The full Adler process and width-only control use the same key. Batch size, early stopping, thread scheduling, and model label never enter it.

If more than one declared split lies inside a node, split chronologically and recurse on the affected child. The node path records left/right ancestry, so repeated splitting never reuses a normal. The elementary physical mesh is the union of the finest uniform grid and all exact deterministic entry/exit times. Coarser refinement increments are sums of these same elementary leaves; they are never generated independently. Thus full/control pairing and fine/coarse pairing refer to one Brownian tree.

Boundary cases are fixed:

- `alpha = 0` or `alpha = 1` creates no stochastic split and assigns an exact zero kick to the zero-duration side;
- zero diffusion gives parent, children, and every nested descendant exactly zero without drawing or consuming a split normal;
- a non-finite crossing, a crossing outside its parent, or two inconsistent canonical identities is a hard configuration error; and
- the separate moving-band audit retains its own namespace and cannot read or perturb the physical Brownian tree.

Verification must cover zero child means, duration-scaled child variances, unconditional left/right covariance consistent with zero, parent-sum conservation, fractions near zero and one, repeated nested splits, rising and falling crossings, multiple clocks with different crossing times, equality across full/control runs, equality across refinement levels, and invariance to batching and early stopping. Mutations using proportional subdivision, independent right-child sampling, a control-specific split key, or nonzero zero-diffusion descendants must fail.

### Between-step lock-band crossings

The primary implementation evaluates eligibility and lock-band membership at every integration endpoint. A clock can cross out and back between endpoints without being observed, which can overestimate uninterrupted dwell. Adjacent timestep agreement alone is not sufficient because missed crossings can create a false plateau.

Before pulsed production, construct an independent stationary killed-diffusion benchmark:

- hold coupling, stable target, and lock band fixed;
- initialize the phase at declared points inside the band;
- solve the continuous first-exit/survival problem with absorbing band edges using an independently implemented PDE or spectral method;
- compare endpoint simulation with the continuous probability of surviving inside for the dwell duration; and
- predeclare absolute and relative tolerances for survival probability, commitment probability, survival quantiles, and reset/exit counts across at least three paired refinement levels.

The benchmark is the oracle; it is not imported by the event generator. The primary endpoint scheme may proceed only after it matches that oracle in the declared regime.

For the moving pulsed band, use the following **diagnostic-only piecewise-linear Brownian-bridge audit** after the stationary oracle passes.

1. Run the primary endpoint process at the finest declared Euler–Maruyama timestep and retain its endpoint phases, coupling values, eligibility flags, and dwell state.
2. Split an interval at an exact deterministic tongue entry or exit. Never bridge across a change of eligibility.
3. On each wholly eligible fine interval, form the admissible lock interval by intersecting the fixed proximity band with the strictly contracting side of the Adler flow. Equality at the contraction boundary is outside.
4. Give the circular phase and both admissible boundaries continuous local representatives. Approximate the lower and upper boundaries by straight lines between their endpoint values. If that local representation is ambiguous, the admissible interval disappears, or its topology changes within the step, reset dwell conservatively rather than choosing a favorable representation.
5. If either endpoint lies on or outside the admissible interval, use the primary reset. If both endpoints lie strictly inside, calculate the conditional Brownian-bridge crossing probability separately for the linearly moving lower and upper boundaries. With the noise convention `phase kick = sqrt(2 * D_phase) * Brownian increment`, the independently transcribed audit calculation is:

```text
p_upper = exp(-(upper_start - phase_start)
                * (upper_end - phase_end)
                / (D_phase * step_duration))

p_lower = exp(-(phase_start - lower_start)
                * (phase_end - lower_end)
                / (D_phase * step_duration))
```

For zero diffusion both probabilities are zero. A zero or negative endpoint clearance means an immediate reset rather than evaluation of the expression. Subtracting a straight moving boundary from the conditioned path is what makes the same one-sided result apply to a piecewise-linear boundary.
6. Combine the two one-sided probabilities with their sum capped at one. This union bound deliberately overstates the chance of touching either boundary when both crossings overlap. Draw one auxiliary uniform value from a separate immutable key: `audit namespace / dataset / trial / clock / finest-step`. If it falls below the capped probability, insert a hidden-exit reset at that interval's end.
7. The audit may add a reset to the endpoint history. It may never remove a primary reset, create an earlier commitment, or turn an unresolved trial into a committed one. Audited committed trials must therefore be a pathwise subset of endpoint committed trials.

Conditioned on the two endpoints, the one-sided bridge calculation is exact for the frozen-drift Euler–Maruyama interpolation and a straight boundary. It is only an approximation to the continuously varying nonlinear Adler drift and moving lock interval. The capped two-boundary combination is conservative for that discretized bridge, not a rigorous bound on the original continuous nonlinear process. The stationary killed-diffusion calculation remains the continuum oracle.

Run the audit on a frozen reduced matrix containing central, interior, and near-edge clocks; both mismatch signs; rising and falling pulse segments; weak, intermediate, and strong noise; and at least three paired fine timesteps. Repeat the auxiliary audit namespace enough times to resolve its added Monte Carlo variation.

Before looking at the audit, freeze absolute and relative tolerances. At the intended production timestep:

- the audit-induced change in commitment probability and survival at every declared comparison time must be no larger than one quarter of the planned production 95-percent confidence half-width and must also pass the frozen absolute and relative caps;
- changes in mean reset count, co-commit rate, and winner-mismatch bins must remain within one quarter of their planned production uncertainty budgets;
- a commit-time quantile may move by no more than one finest timestep plus one quarter of its planned confidence half-width;
- the fitted endpoint cumulative-hazard exponent may move by no more than one quarter of its planned standard error; and
- every audit difference must decrease toward zero, or remain statistically indistinguishable from zero, under paired timestep halving.

If the pathwise subset rule fails, the audit implementation is wrong. If the comparison budgets fail, reduce the primary timestep and repeat. If the budgets cannot be met within the feasibility gate, report a numerical no-result. The Brownian-bridge record cannot replace or correct the primary production ledger, and it cannot be used to select a favorable timestep or exponent.

## Lock and fixed-dwell state machine

Use one ordering everywhere. For a step from the current time to the next time:

1. Evolve the noisy phase to the next time.
2. Evaluate pulse coupling and eligibility at that next time.
3. If eligible, calculate the moving stable phase and the instantaneous derivative of deterministic Adler drift with respect to phase.
4. Measure the shortest circular phase error to the stable target.
5. Declare `inside_now` only when both conditions hold:
  - phase error is strictly smaller than the fixed angular tolerance; and
  - local deterministic flow is contracting, meaning a small phase error is pulled smaller rather than pushed larger.
6. If `inside_now` is false, clear `inside_since` immediately.
7. If `inside_now` is true and `inside_since` is empty, set `inside_since` to the current timestamp. Give no credit for the preceding interval.
8. If `inside_now` is true and the current time minus `inside_since` is at least the fixed dwell, commit at this sampled time.

The lock tolerance and dwell duration are fixed in one reference time and angle system for the entire coupling sweep. They never scale inversely with coupling. Because dwell is timestamp-based, the same physical rule applies when dwell divided by timestep is non-integral. The event time is interval-censored to the final timestep.

At deterministic pulse eligibility crossings, split a step at the exact crossing time supplied by the calibrated raised-cosine pulse, or demonstrate that not splitting changes every primary observable by less than the declared event-time tolerance. No dwell may begin before exact eligibility.

The following events reset dwell immediately:

- the noisy phase leaves the lock band;
- the falling tongue makes the clock ineligible; or
- the stable phase moves far enough that the clock is no longer within the band.

### Contraction guard and the repelling branch

Near the Arnold-tongue edge, the stable and repelling fixed phases approach one another. A proximity-only band can contain both. The contraction guard prevents this: a phase near the target earns dwell only on the locally attracting side of the Adler flow.

This changes the accepted region near the edge and must remain visible. Verification includes the stable point, repelling point, both sides of the separatrix, both signs of mismatch, and a sequence approaching the tongue boundary. Post-run predictors must use the same declared eligible clock population and must not pretend that proximity alone defines commitment.

The contraction guard is not described as a microscopic detector fact. It is the minimum mathematically consistent definition of “locally locking” in this phase-only model.

### Required dwell edge cases

Synthetic tests must cover dwell shorter than one timestep, equal to one timestep, non-integral relative to timestep, initial inside-band state, exit on the prospective commit step, and falling-edge eligibility loss. An initial inside sample starts the timestamp and never commits immediately for positive dwell.

### First channel commitment

The channel commits at the earliest timestep on which any clock completes dwell. Simulation stops for that trial.

If several clocks complete on the same timestep:

- the channel is still recorded as committed;
- all co-committing clock IDs and mismatches are retained;
- no random winner is chosen inside the channel; and
- co-commit multiplicity must shrink or reach a stable negligible level under timestep refinement before winner-mismatch statistics are interpreted.

The stop is an experimental endpoint for this one-channel first-passage study. It is not claimed to derive global physical exclusivity.

## Complete ledger

Every trial ends in exactly one channel-level category:

| Category | Meaning |
| --- | --- |
| `committed` | At least one clock completed uninterrupted dwell before pulse end |
| `never_eligible` | No clock ever entered its tongue |
| `lock_failed` | At least one clock was eligible, but no clock ever entered the lock band |
| `dwell_failed` | At least one clock entered the band, but none completed dwell |

The last three categories together are the unresolved fraction. They are never discarded or conditioned away.

For a committed trial also store:

- first-commit time;
- all co-committing clock IDs;
- their mismatches and phases;
- their tongue-entry, band-entry, and last-reset times;
- number of clocks ever eligible;
- number ever entering the band;
- total dwell resets; and
- complete run configuration and random seed.

Aggregate per-clock counts by mismatch are stored even though the trial stops at first commitment.

Those per-clock diagnostics are informatively censored: once one clock commits, later opportunities for every other clock are unobserved. Therefore each clock also stores exposure time until channel stop. Report exposure-normalized pre-event statistics, not raw zero counts as evidence of impossibility.

Run a small, predeclared **no-stop shadow sample** through the full pulse after the first hypothetical commitment. It is diagnostic only and never contributes production channel outcomes. It separates intrinsic mismatch behavior from truncation by the first winner.

## What will be measured

### Primary empirical quantities

1. **Commitment probability:** fraction of all trials that commit.
2. **Unresolved fraction:** reported with its three causes.
3. **Survival curve:** fraction not yet committed at each time.
4. **Time-dependent hazard:** new commitments during a time interval divided by trials still unresolved at its start.
5. **Commit-time distribution:** including median and quantiles; mean reported only with its censoring convention.
6. **Winner-mismatch distribution:** which part of the tongue supplies first commitment.
7. **Band-entry and reset statistics:** distinguishes noise-assisted entry from noise-broken dwell.
8. **End-of-pulse cumulative hazard:** inferred directly from committed/unresolved binomial counts through the declared complementary-log-log model, not by taking logarithms of empirical proportions.

The pulsed hazard is expected to vary in time. No constant Poisson rate is fitted by default. Events are interval-censored to one timestep and pulse end is administrative right-censoring.

For binned displays, always report:

- number at risk at bin start;
- event count;
- censoring count;
- bin width; and
- either discrete conditional failure probability or a time rate obtained by an explicitly stated conversion.

Do not label events-per-risk as a continuous hazard rate unless bin width has been accounted for.

### Primary scaling estimand

The primary production parameter is the coupling exponent in a binomial complementary-log-log model fitted directly to committed and unresolved trial counts at every frozen coupling value.

The model says, in words: the logarithm of endpoint cumulative hazard is a constant plus an unconstrained exponent times the logarithm of peak coupling.

Requirements:

- retain every coupling cell in the likelihood, including zero-event and all-event cells;
- never transform empirical zero or one proportions and silently discard them;
- report raw counts, commitment probability, cumulative hazard with uncertainty, exponent uncertainty, deviance, and lack-of-fit;
- predeclare and test a curvature extension or local-slope diagnostic;
- report **no valid exponent** when the power-law model fails;
- account for common random numbers by resampling master-trial IDs or use independent coupling namespaces; and
- do not use the existing unweighted analytic log-log fitter for binomial outcomes.

### Isolated comparison curves

Only after the raw event process closes and writes an immutable ledger may a separate comparison process read that ledger and compare results with:

- the instantaneous eligible-clock count on the exact production grid, representing tongue-width-only behavior;
- the bare independent relaxation-rate sum over the exact finite production clocks, the primary rate-weighted comparator;
- the spacing-weighted continuum flux, labeled as a continuum control rather than a finite-population predictor; and
- a constant-hazard model, retained mainly as a falsifiable control.

The fixed dwell introduces a real delay. Predictor curves may be shifted by the declared dwell duration, but no free time shift is fitted in the primary comparison.

The shifted instantaneous analytic sum is only a heuristic: commitment at one time depends on the whole path over the preceding dwell interval. Mechanistic support requires an out-of-sample time-resolved comparison including rising/falling asymmetry and winner mismatch, not just an endpoint exponent.

The analytic module is read only by the comparison/reporting process. Stochastic evolution and commitment code may not load it directly or indirectly.

## Production experiment sequence

### Experiment S0 — random-kick calibration

- Generate phase kicks without drift or coupling.
- Verify zero mean, declared variance, temporal independence, and cross-clock independence.
- Verify paired fine increments sum exactly to coarse increments.
- Verify that changing coupling while reusing a paired stream does not change the supplied random kicks.

### Experiment S1 — deterministic limit

- Set noise strength to zero.
- Require Euler–Maruyama to become deterministic Euler.
- Reproduce the existing pulsed eligibility and finite-time behavior within Euler timestep error.
- Require zero coupling to produce no commitment for every positive dwell.

### Experiment S2 — synthetic dwell-machine tests

Feed declared eligibility and phase-error sequences directly into the state machine:

- timestamp-based uninterrupted inside-band time commits at the correct later sample;
- one exit resets the full dwell;
- loss of eligibility resets dwell;
- wrap-boundary phases use circular distance;
- an initial inside-band sample starts dwell but does not instantly commit;
- dwell shorter than, equal to, and non-integral relative to the timestep preserves the same timestamp rule;
- the repelling fixed point and locally expanding side never earn dwell even when within the proximity tolerance;
- both mismatch signs and near-boundary stable/unstable coalescence obey the contraction guard;
- zero or negative dwell and band tolerance are rejected; and
- dwell and tolerance remain identical when coupling changes.

### Experiment S3 — stationary killed-diffusion oracle

Before any first-commit production:

- freeze a stationary coupling and fixed lock band;
- solve continuous survival inside the band with absorbing edges using an independently implemented killed-diffusion PDE or spectral calculation;
- begin endpoint simulations at several declared positions inside the band;
- compare survival through the dwell duration, exit-time quantiles, and exit/reset counts across at least three paired timestep levels; and
- enforce predeclared absolute and relative tolerances.

The oracle code cannot be imported by the event generator. Failure blocks pulsed scientific interpretation.

### Experiment S4 — one stochastic clock

Run one clock under stationary and pulsed coupling:

- zero coupling verifies pure phase diffusion;
- central, interior, and near-edge mismatches map noise-assisted band entry and noise-broken dwell;
- noise is swept from zero through weak, intermediate, and strong regimes;
- commit probability, reset count, and time distribution are retained; and
- non-monotonic noise behavior is allowed and reported.

This stage validates the event mechanism before population competition obscures it.

Two negative mechanism controls are mandatory:

1. **Central-clock control:** one zero-mismatch clock, for which tongue widening is absent. A quadratic result here defeats the claimed width-times-rate explanation.
2. **Fixed-contraction width-only control:** preserve the exact finite eligibility geometry and moving stable target while replacing Adler's coupling-dependent interior contraction with one fixed rate. A quadratic result here shows that eligibility width, pulse timing, thresholding, or censoring can manufacture the target without the proposed second factor.

#### Exact width-only data-generating process

The width-only control uses the same finite clock grid, pulse coupling, eligibility rule, moving stable target, initial phases, white-noise strength, Brownian increments, proximity tolerance, contraction guard, dwell, stop rule, ledgers, coupling sweep, and statistical pipeline as the full Adler run. Only its deterministic drift while eligible is changed. Before entry, after exit, and between later eligible windows, its evolution is exactly the calibrated full Adler evolution.

For each clock:

- **Authoritative state at all times:** retain one unwrapped absolute phase on the real line. Never replace it with a wrapped phase or discard its winding count. Circular functions and lock distances may read this phase modulo one turn, but state transitions always update the unwrapped value.
- **Outside the tongue:** evolve that unwrapped phase with the complete calibrated Adler drift—mismatch minus instantaneous coupling times the sine of phase—plus the same additive white-noise increment. Eligibility only determines whether a stable target and dwell are available; it does not turn off the subthreshold Adler pull.
- **At exact tongue entry:** eligibility equality is a separate state. At `coupling = absolute mismatch`, call the calibrated finite `boundary_phase(mismatch)`—never `stable_phase`, which deliberately returns not-a-number at equality. Add an integer number of complete turns to that boundary value to obtain the target lift nearest the incoming unwrapped phase. Use the half-open error interval from minus pi inclusive to plus pi exclusive to resolve the exact half-turn tie deterministically. Store both the lifted boundary target and the unwrapped error equal to absolute phase minus lifted target. This identity leaves the authoritative absolute phase unchanged at entry. For zero mismatch, the calibrated boundary phase is zero.
- **While strictly eligible:** only when `coupling > absolute mismatch`, evaluate `stable_phase(coupling, mismatch)`. Continue that finite principal target onto the unique lifted branch nearest the preceding lifted target. Evolve the unwrapped relative error with a restoring drift equal to minus one fixed positive contraction rate times the sine of the error, plus the same Brownian increment assigned to the corresponding full-model clock. Do not wrap the evolving error. Reconstruct the authoritative absolute phase as lifted target plus unwrapped error. In absolute coordinates this includes the target's motion; in relative coordinates the intended contraction is transparent and does not vary with coupling, mismatch, pulse time, or trial.
- **At exact tongue exit:** at equality, use `boundary_phase(mismatch)` and continue it onto the lifted branch nearest the preceding target lift. Reconstruct and retain the unwrapped absolute phase at that finite boundary target, then discard only the auxiliary target/error representation and resume the complete calibrated Adler drift with the same Brownian tree. There is no coordinate reset and no call to `stable_phase` at equality.
- **At re-entry:** construct a new lifted target from the current authoritative unwrapped phase using the same deterministic half-open convention. Previous eligible evolution may have changed the phase, but the coordinate handoff itself may not.

The control's local contraction derivative is minus the fixed rate times the cosine of the relative error. It is strictly contracting only when that derivative is negative; equality earns no dwell. Thus the control uses the same logical contraction guard without quietly replacing it with proximity alone.

The Euler–Maruyama state transition is fixed in code-like plain text:

```text
if ineligible:
    phase_unwrapped_next = phase_unwrapped
                           + (mismatch
                              - coupling_now * sin(phase_unwrapped))
                             * step_duration
                           + noise_increment

if exact_entry_handoff:
    target_principal = boundary_phase(mismatch)
    target_lift = nearest_lift(target_principal, phase_unwrapped)
    error_unwrapped = phase_unwrapped - target_lift
    # The zero-duration handoff changes no phase and consumes no noise.

if evolving_an_eligible_segment:
    if segment_ends_at_exact_exit:
        target_principal_next = boundary_phase(mismatch)
    else:
        target_principal_next = stable_phase(coupling_next, mismatch)

    target_lift_next = continuous_lift(target_principal_next,
                                       target_lift_now)
    error_unwrapped_next = error_unwrapped
                           - fixed_rate * sin(error_unwrapped)
                             * step_duration
                           + noise_increment
    phase_unwrapped_next = target_lift_next + error_unwrapped_next

if exact_exit_handoff:
    keep phase_unwrapped unchanged
    discard target_lift and error_unwrapped
    # The zero-duration handoff changes no phase and consumes no noise.
```

An entry or exit inside a numerical step is split at its exact calibrated crossing time before applying these transitions. Its physical kick is divided by the nested keyed Brownian-tree rule above. The split normal reveals the conditional path inside the parent interval; it is shared by the full and control processes, and the two child kicks sum to the originally assigned parent kick.

Before population runs, synthetic transition checks must establish all of the following:

- with identical phase and noise, every ineligible control step equals the full Adler step exactly;
- entry changes neither the unwrapped phase nor its sine, including phases immediately on both sides of the usual circular cut;
- exact entry and exit use finite `boundary_phase` values, while any attempted `stable_phase` call at equality returns not-a-number and fails the transition rather than seeding a target lift;
- target-lift plus error equals the authoritative unwrapped phase before and after every eligible step;
- exit and later re-entry preserve the unwrapped phase without a positive or negative full-turn jump;
- both mismatch signs and zero diffusion obey the same continuity rule;
- repeated entry/exit cycles retain the accumulated winding rather than resetting it; and
- deliberately dropping the stored lift, replacing the ineligible drift with free mismatch drift, proportionally splitting a parent kick, or using `stable_phase` at equality fails the checks.

Before the range-only pilot, freeze the rule that sets the fixed rate equal to the full Adler central-clock relaxation rate at a reference coupling given by the geometric midpoint of the eventual frozen production peak-coupling range. After the pilot selects that range under its count-only rule, this deterministic calculation supplies the one reference rate written into the production manifest before any production event result is opened. It is common to every clock and coupling and may not be refitted. Lower and upper fixed-rate choices may be run later as labeled sensitivities, never substituted for the primary width-only control.

First verify this control one clock at a time in S4. Then run it over the complete S5 production clock grid with paired initial phases and paired Brownian streams. The pairing exposes the consequence of removing only coupling-dependent contraction; it does not authorize paired trials to be treated as statistically independent.

The width-times-rate interpretation is blocked if the width-only control passes the same power-law adequacy tests and either:

- its predeclared 95-percent exponent interval contains two; or
- the paired full-model-minus-control exponent contrast fails to exceed the minimum mechanistic difference frozen by the power calculation.

It is also blocked if the width-only control matches or outperforms the full Adler model on the frozen out-of-sample rising/falling survival and winner-mismatch diagnostics. These are causal-identification failures, not reasons to tune the fixed rate or discard the control.

### Experiment S5 — finite-population one-channel race

Freeze one primary clock population and sweep peak coupling over a predeclared range.

Before the pilot, freeze a versioned analysis template containing the count thresholds the pilot may use. Then use two separate Monte Carlo namespaces:

1. A labeled pilot may choose only an information-bearing coupling range using predeclared minimum expected event and survivor counts. It may not examine or optimize the exponent, curvature, physical noise, dwell, tolerance, pulse, grid, population, state machine, likelihood, or exclusion rules. It may not enter the production estimate.
2. Before production, write and hash a manifest freezing the coupling grid, trial count, primary noise, dwell, tolerance, pulse, `N`, support, grid parity and origin, fit model, curvature/lack-of-fit tests, inclusion rules, seed namespaces, software versions, and source hashes.
3. A fresh production run uses only that frozen manifest. Production and later sensitivity results cannot revise the primary analysis.

For every coupling report all ledger categories, survival, time-dependent hazard, cumulative hazard, and winner mismatch.

Fit committed/unresolved counts with the predeclared binomial complementary-log-log likelihood without forcing exponent two. Every coupling cell remains represented. If the power model or its curvature/lack-of-fit tests fail, report no exponent rather than changing the window.

The exact finite production grid is load-bearing:

- use the bare relaxation-rate sum on those exact clocks as the primary analytic comparator;
- freeze even/odd parity, grid origin, support, and coupling nodes;
- predeclare a minimum number of eligible clocks at the weakest coupling, or explicitly narrow the result to a visibly discrete staircase regime;
- report predicted and observed grid staircases rather than smoothing them away; and
- compare changes across `N` with changes in the finite bare sum, not with raw-probability invariance.

### Experiment S6 — stationary-hazard control

Use a long constant-coupling interval with predeclared burn-in semantics. Either carry dwell age and condition honestly on left-truncated survivors, or reset every state at the analysis start and call it a newly prepared ensemble. Never discard burn-in commitments and silently reset selected survivors.

- measure whether first-commit survival is exponential over any interval;
- report the full time-dependent hazard even if it appears flat; and
- compare the stationary result with the pulsed result without assuming they share one rate law.

Only this stationary control is a reasonable place to ask whether a constant Poisson approximation exists.

### Experiment S7 — sensitivity and falsification

Repeat the primary production sweep across:

- timestep refinement with paired noise;
- low, medium, and high noise strength;
- several fixed dwell durations;
- several fixed lock-band tolerances;
- fixed-peak pulse-duration changes;
- separately labeled fixed-area pulse-duration changes;
- several finite physical population sizes;
- alternative initial-phase preparations; and
- one deliberately structured mismatch spectrum after the flat case.

Population size is never called a numerical convergence parameter. A robust candidate may preserve its fitted coupling exponent while total commitment probability changes with the number of competitors.

Run a small no-stop shadow sample for exposure-normalized per-mismatch diagnostics. Stage the sensitivities rather than running a full factorial: numerical convergence first, then a finite predeclared set of one-factor physical falsifications, and expand only if the primary result is interpretable.

## Predeclared interpretations

| Observation | Interpretation |
| --- | --- |
| Hazard tracks rate-weighted flux after the fixed dwell delay | Supports using synchronization speed as a candidate commitment propensity |
| Hazard tracks eligible-clock count better | Tongue width dominates; expected scaling is closer to amplitude-linear |
| Hazard is strongly non-Poisson and neither predictor works | A simple rate race is not justified |
| Endpoint scheme misses the killed-diffusion tolerance or timestep plateau | Numerical no-result; no mechanism verdict permitted |
| Complementary-log-log power model fails curvature or lack-of-fit | No valid exponent; do not choose another window after seeing production data |
| Central single clock appears quadratic | Quadratic crossover does not require tongue widening; width-times-rate explanation fails |
| Width-only control appears quadratic | Threshold/censoring pipeline can manufacture the target exponent |
| Weak noise raises commitment but strong noise lowers it | Noise assists band entry and later disrupts dwell; a physically plausible non-monotonic regime |
| Fitted coupling exponent depends strongly on noise, dwell, or tolerance | The law is criterion-dependent, not universal |
| Longer pulses mainly reduce unresolved trials | Finite time acts principally like detector efficiency |
| Coupling exponent changes with pulse duration | The proposed selection propensity is time-window dependent |
| Exponent is robust while total success rises with population | Population changes opportunity count but not coupling dependence |
| Structured spectrum changes behavior as independently predicted | Supports the spectral-flux mechanism but creates an empirical detector-spectrum burden |
| Direct events remain quadratic when the independent analytic flux is not | Refutes the claim that the rate-weighted tongue causes the event scaling |
| Endpoint exponent is quadratic but time-resolved rising/falling shape or winner mismatch fails out of sample | Endpoint agreement is coincidental or incomplete, not mechanistic support |

## Verification contract

The stochastic implementation is correct only if checks cover at least these invariants:

### Noise

1. Zero diffusion produces exactly zero kicks.
2. Kick mean and variance match the declared white-noise law within statistical intervals.
3. Cross-clock correlations and temporal autocorrelations are statistically consistent with zero.
4. Coarse paired increments equal sums of their fine increments, and every off-grid Brownian-tree parent equals the residual-constructed sum of its correctly distributed children to machine precision.
5. Reusing a paired noise stream at different coupling values supplies identical kicks.
6. Counter-keyed streams and nested split normals are unchanged by batch size, early stopping, model label, or refinement level; zero diffusion consumes no split key and yields exact zeros.
7. Fixed seeds reproduce identical raw event ledgers in the recorded environment.

### Dynamics and dwell

8. Zero-noise stochastic integration matches deterministic Euler.
9. Zero coupling and zero mismatch reproduce free phase diffusion in the unwrapped phase variance.
10. Timestamp dwell gives no retroactive credit to the first inside sample.
11. Dwell shorter than, equal to, and non-integral relative to timestep follows the same timestamp definition.
12. One band exit resets `inside_since` completely.
13. Eligibility loss on the falling edge resets `inside_since`.
14. Exact deterministic tongue crossings cannot earn premature dwell; `boundary_phase` supplies the finite target at equality, while `stable_phase` is called only at strictly eligible interior times.
15. Circular lock-band distance works across the phase wrap.
16. An ineligible clock cannot commit.
17. Dwell time and proximity tolerance are identical across coupling values.
18. Stable points strictly inside the proximity band earn dwell; the proximity boundary, repelling points, and locally expanding phases do not.
19. The contraction guard is symmetric under mismatch sign and remains correct approaching the tongue edge.
20. Multiple same-step clock completions are retained and never randomized away.

### Continuous white-noise audit

21. The independently implemented killed-diffusion oracle reproduces a case with a known limiting solution.
22. Endpoint survival and exit-time quantiles approach the oracle across at least three paired refinements.
23. Absolute and relative oracle tolerances are frozen before the pulsed audit.
24. The moving-band audit splits exact eligibility crossings, uses piecewise-linear boundaries and independently keyed bridge uniforms, only adds resets, and produces a pathwise subset of endpoint commitments; failure of its frozen comparison budgets blocks production interpretation.

### Ledger and statistics

25. Every trial lands in exactly one committed or unresolved category.
26. The three unresolved categories are mutually exclusive and exhaustive.
27. Channel stopping time equals the earliest per-clock completion time to timestep resolution.
28. Survival is non-increasing and agrees with the raw commit-time ledger.
29. Discrete failure probability and time-rate hazard reproduce known synthetic event distributions with bin width and risk counts visible.
30. Winner-mismatch counts sum to committed trials, including explicit co-commit handling.
31. Exposure-normalized per-clock diagnostics and no-stop shadow diagnostics expose first-winner censoring.
32. The complementary-log-log binomial estimator recovers synthetic exponents, retains zero/all-event cells, and reports lack of fit and curvature.
33. A deliberately non-power response produces `no valid exponent` rather than a selected window.
34. Pilot and production namespaces, manifests, and outputs are physically separated and hash-verifiable.
35. Central-clock and fixed-contraction width-only controls are capable of defeating a false width-times-rate claim. The width-only process exactly matches full Adler evolution whenever ineligible, changes only eligible contraction, shares the same nested physical Brownian tree, uses finite boundary targets at equality, keeps one unwrapped authoritative phase with a continuous target lift through entry/exit/re-entry, and uses one reference contraction at every coupling.

### Scientific isolation and convergence

36. Raw event-process modules and their transitive imports cannot load or name the analytic prediction.
37. Package initialization for raw runs does not eagerly import `analytic`.
38. Event-generating APIs reject predictor callbacks, arbitrary comparison objects, amplitude squares, intensity weights, and prescribed hazards.
39. The raw process closes and hashes its ledger before the comparison process opens it.
40. Timestep refinement uses streamed paired Brownian increments and reports changes in all primary observables.
41. Failure to reach a timestep or killed-diffusion tolerance blocks scientific interpretation.
42. Population-size changes are labeled physical sensitivity, not convergence.
43. The exact-grid bare sum is the primary comparator; spacing-weighted flux is separately labeled continuum control.
44. Grid parity, origin, support, coupling nodes, and minimum eligible-cell count are frozen and visible.
45. All fitted exponents are unconstrained and reported even when far from two.
46. Zero-event, all-event, saturated, censored, and excluded cells remain visible in raw outputs and manifests.
47. Common-random-number uncertainty is estimated by resampling master trial IDs or using independent coupling streams.
48. Documentation preserves every non-claim and every numerical-no-result rule in this plan.

Independent review should add mutation tests for at least: shared instead of independent noise, coupling-dependent noise strength, proportional rather than conditional Brownian subdivision, independently sampled right children, split keys that include the model label, nonzero zero-diffusion descendants, `stable_phase` calls at eligibility equality, sample-count rather than timestamp dwell, a dwell counter that fails to reset, removal of the contraction guard, a bridge audit that removes resets or creates commitments, reuse of the physics-noise namespace for audit uniforms, nonlinear or discontinuous audit boundaries, a width-only contraction rate that scales with coupling, replacement of the full ineligible Adler drift by free mismatch drift, omission of target motion, loss of the target-lift winding at entry/exit/re-entry, wrapping of the authoritative phase or eligible error, analytic leakage through package initialization, discarded unresolved trials, silent fit-point filtering, replacement of the bare sum by flux, parity changes, early-stop-dependent RNG streams, and regression uncertainty that ignores paired trials.

## Codebase fit

Extend the existing isolated package:

`~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`

| File | Responsibility |
| --- | --- |
| `model.py` | Keep calibrated deterministic physics; expose validated private drift kernels needed by stochastic stepping |
| `stochastic.py` | Counter-keyed streamed Brownian increments, nested physical Brownian-tree splitting at irregular crossings, Euler–Maruyama ensemble stepping, and the width-control's authoritative unwrapped phase plus continuous target-lift handoff |
| `commitment.py` | Timestamp dwell, contraction-safe lock predicate, and ledger categories only |
| `simulate.py` | Preserve deterministic API; stochastic raw runs live behind a separate event boundary |
| `raw_runner.py` | Validated raw event configuration, batches, early stopping, immutable ledger writing; cannot import analytic/reporting code |
| `killed_diffusion.py` | Independent stationary absorbing-boundary survival oracle; cannot be imported by raw runner |
| `moving_band_audit.py` | Diagnostic piecewise-linear Brownian-bridge reset audit with a separate keyed namespace; never imported by the primary raw runner |
| `observables.py` | Ledger aggregation, survival, hazard, cumulative hazard, intervals |
| `analysis.py` | Complementary-log-log binomial model, curvature/lack-of-fit, paired-trial uncertainty |
| `compare.py` | Separate process reading a closed ledger and comparing bare sum, width-only, continuum, and constant-hazard alternatives |
| `experiments.py` | Frozen pilot/production manifests and staged run matrix orchestration |
| `analytic.py` | Unchanged prediction boundary except validated read-only reporting helpers if required |
| `verify.py` | Existing 26 checks plus the new stochastic contract |
| `README.md` | Plain-English walkthrough, commands, configurations, results, and non-claims |

Remove the eager `analytic` import from the package root for raw-event execution. Either make package exports lazy or provide a raw-event subpackage/process whose transitive import graph cannot reach analytic, comparison, or killed-diffusion code. The comparison process may import analytic only after verifying the raw ledger's close marker and hash.

Extend AST/import and runtime-namespace checks to every module transitively reachable from `raw_runner.py`. This prevents accidental manufacture; it is not described as a security sandbox.

Do not import or modify `first_mark_two_absorber/`. Preserve every existing deterministic residual and check.

## Data and reproducibility

Write generated output only beneath a package-scoped ignored results directory.

For every production configuration store:

- human-readable JSON manifest;
- raw trial ledger as CSV;
- binned survival and hazard CSV;
- complete physical and numerical parameters;
- clock mismatches;
- trial count;
- immutable clock grid, parity, origin, support, and minimum eligible-cell count;
- counter-key namespace and stream derivation scheme;
- event-process ledger hash and close marker;
- frozen statistical model, curvature test, inclusion rules, and resampling unit;
- measured throughput, peak memory, and planned run-matrix estimate;
- Python and NumPy versions;
- Git status summary or source hash; and
- explicit pilot-versus-production label.

Plots are derived results and never the sole record.

## Feasibility and power gate

Before production:

1. Benchmark clock-steps per second and peak memory using the intended block size and fine timestep.
2. Demonstrate that streamed refinement never materializes the full trial-by-clock-by-time noise cube.
3. Use a labeled pilot only to estimate event/survivor counts and perform a power calculation for a predeclared confidence width on the coupling exponent.
4. Publish a finite primary run matrix with total clock-steps, wall-time estimate, storage estimate, and failure/stop criteria.
5. Stage later sensitivity runs one factor at a time. Do not launch a full factorial automatically.

If the minimum eligible-cell requirement implies an infeasible clock population, narrow the claim to the exact finite discrete grid and its visible staircase rather than quietly invoking a continuum approximation.

## Implementation order

Implementation is tracked in the dependency-ordered [ticket set](tickets). Each ticket must leave the deterministic verifier passing and may advance only through its stated gate.

1. Remove eager analytic access from the raw-event import boundary and prove transitive isolation.
2. Counter-keyed streamed noise generator, nested irregular-crossing Brownian tree, and paired refinement utilities.
3. Timestamp dwell and contraction-safe lock state machine driven by synthetic sequences.
4. Independent stationary killed-diffusion oracle and endpoint convergence gate.
5. Diagnostic piecewise-linear Brownian-bridge moving-band audit and its pathwise-subset/tolerance gate.
6. One-clock stochastic controls, including the central-clock and exact fixed-contraction width-only processes.
7. Raw one-channel finite-population race, immutable ledger, exposure accounting, and no-stop shadow sample.
8. Survival, binned failure probability, time-rate hazard, and complementary-log-log analysis in a separate layer.
9. Throughput/memory benchmark, power calculation, and frozen finite run matrix.
10. Pilot firewall, signed production manifest, and production coupling sweep.
11. Finite-population/grid sensitivity plus staged noise, dwell, band, pulse, phase, fixed-rate, and structured-spectrum controls.
12. Independent adversarial code and scientific review.

## Completion boundary

The experiment is complete when:

- all existing deterministic checks still pass;
- the new stochastic verification contract passes;
- timestamp dwell and contraction-safe lock semantics pass their boundary cases;
- the endpoint scheme matches the independent killed-diffusion oracle and the diagnostic moving-band audit within their frozen tolerances;
- production results have a reproducible positive or negative verdict;
- timestep convergence is demonstrated or scientific interpretation is explicitly blocked as a numerical no-result;
- the predeclared binomial power model passes curvature/lack-of-fit or reports no valid exponent;
- central-clock and fixed-contraction width-only controls do not defeat the width-times-rate interpretation under the frozen causal decision rule;
- clock-count dependence is reported honestly as physical population sensitivity;
- measured runtime, memory, and statistical power support the finite production matrix; and
- no manuscript claim is made before independent review closes.

Implementation is not complete merely because one configuration yields a fitted exponent near two.
