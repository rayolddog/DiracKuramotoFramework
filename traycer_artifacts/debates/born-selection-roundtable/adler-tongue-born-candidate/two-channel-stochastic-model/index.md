---
title: "Technical plan: two-channel stochastic Adler test"
kind: spec
---

# Two-channel stochastic Adler test

## Purpose

Test one sharply bounded hypothesis under a finite interaction time:

<user_quoted_section>Does direct noisy Adler phase dynamics, applied to two competing populations of absorber clocks while a photon-pulse envelope opens and closes their Arnold tongues, produce first-commitment frequencies proportional to the square of their amplitude-linear peak couplings?</user_quoted_section>

The simulation must be capable of answering **no**. The analytic semicircle result is a comparison curve, not a stochastic event rule.

This is the smallest statistical test of the [rate-weighted tongue candidate](..). It is not the 576-state field–absorber model and does not modify it.

## User-settled decisions

| Decision | Selected option | Why it matters |
| --- | --- | --- |
| Test mode | Direct stochastic phase simulation | Does not insert the predicted coupling-squared hazard into the event generator |
| Microscopic commitment | First clock that stays locked for a fixed physical dwell time | Gives a clear detector-seed event without scaling the criterion by coupling |
| Bath noise | Independent amplitude-neutral phase noise | Smallest stochastic bath; prevents amplitude from entering through the noise law |
| Finite interaction | A common photon-pulse envelope makes both channel couplings rise and fall | A marginal clock can enter the tongue but run out of time before locking; pulse duration becomes a falsification variable |

## Non-claims and model boundary

The model tests **weighting only**.

It does not contain a photon field, energy-bearing absorber levels, amplification, a detector bias supply, or a norm-preserving route for losing amplitude. Its global first-winner stop is imposed as a bookkeeping rule and must never be described as derived physical exclusivity.

Consequently, even a perfect quadratic result would show only:

<user_quoted_section>a two-channel noisy synchronization race can reproduce the Born frequency curve under its stated clock, bath, and stopping assumptions.</user_quoted_section>

It would not establish one-world actuality, energy conservation, no-signaling, or a microscopic detector mechanism.

## Physical picture

Use a polarizing beam splitter as the teaching configuration:

```text
one prepared polarization
          |
          v
common photon-pulse envelope times
amplitude-linear coupling to two outputs
       /                         \
horizontal absorber clocks     vertical absorber clocks
       \                         /
        first clock to remain locked
                    |
                    v
          provisional channel winner
```

The input angle is used only to calculate the two coupling magnitudes. No probability is assigned at that step.

## Minimal state

Each channel contains `N` independent phase errors.

For every clock store only:

- its fixed natural-frequency detuning;
- its current wrapped phase error;
- its accumulated uninterrupted dwell time inside the lock band; and
- whether it is currently eligible to possess a stable Adler lock; and
- when it entered and left the transient tongue during the pulse.

Global trial state contains:

- the two peak channel couplings and the common pulse-envelope value;
- the phase arrays for A and B;
- dwell counters;
- simulation time; and
- an outcome flag: A, B, unresolved, or numerical tie.

No channel receives the squared amplitude. The dynamics layer receives only the two linear coupling magnitudes.

## Clock population

### Primary flat-spectrum population

- Both channels use the same fixed midpoint grid of detunings across a support much wider than the largest coupling.
- Equal numbers of clocks and the identical grid guarantee exact A/B material symmetry.
- A clock is tongue-eligible only while the instantaneous pulse-scaled coupling exceeds the magnitude of its detuning.
- The initial phases are sampled independently and uniformly around the circle on every trial.

A fixed grid isolates stochastic phase effects from random spectral-sampling imbalance. Every clock is an actual competitor, so increasing `N` changes the physical number of commitment opportunities. Population size is varied as a physical sensitivity; it is not called numerical convergence.

### Spectral controls

After the flat case, repeat with:

- Gaussian detuning density;
- Lorentzian detuning density; and
- one deliberately structured density containing a narrow spectral notch or peak.

These controls test the predicted loss of exact quadratic scaling when the tongue is not narrow relative to spectral structure.

## Finite photon-pulse envelope

The primary transient mechanism is the passing photon wave packet. A single nonnegative envelope rises from zero, reaches one peak, and returns to zero. Both channels receive exactly the same envelope; polarization changes only their peak coupling magnitudes.

This makes each Arnold tongue open and then close:

```text
before pulse        rising edge          near peak          falling edge       after pulse
no eligible clocks  tongue admits clocks widest tongue      clocks drop out     no eligible clocks
```

A clock near the tongue boundary has a slow local synchronization rate. It may become temporarily eligible yet fail to approach the moving stable phase before the falling edge removes the lock. The outcome therefore depends on the competition among:

- time spent inside the tongue;
- distance from the instantaneous boundary;
- phase-locking time;
- bath noise;
- fixed commitment dwell time; and
- pulse duration.

Use one smooth compact or effectively compact envelope as the primary case. A raised-cosine pulse is the clearest bounded control; a Gaussian pulse is a secondary shape check. Pulse area must not be silently renormalized when duration changes: run separate fixed-peak and fixed-area duration sweeps because they answer different physical questions.

### Important geometric correction

An oscillator does not leave a stationary Arnold tongue merely because its phase rotates. The tongue boundary lies in coupling-versus-frequency-mismatch space, not in phase-angle space. Leaving requires a changing coupling or detuning. Here the falling photon envelope supplies that change. A later frequency-drift experiment may test moving detuning, but it is not part of the smallest primary model.

## Direct stochastic dynamics

For each clock and each time step:

```text
phase change = detuning drift
             - pulse-scaled sinusoidal pull toward the channel reference
             + independent Gaussian phase kick
```

Implementation requirements:

- Euler–Maruyama integration, vectorized over all clocks;
- identical time step and noise strength for both channels;
- independent random numbers for each clock and channel;
- authoritative unwrapped phases, with sine, cosine, and angular lock distances evaluated periodically and continuously across the usual circular cut;
- eligibility is recalculated from the instantaneous coupling at every step; exact entry/exit equality uses the finite calibrated boundary phase, and the stable phase is evaluated only at strictly eligible interior times;
- clocks outside the transient tongue may drift but cannot be declared locked because no stable fixed point exists;
- the same normalized pulse envelope and clock time are used for both channels; and
- no amplitude dependence in detunings, initial phases, noise strength, lock tolerance, or dwell time.

When an exact deterministic entry or exit falls inside a uniform timestep, split the physical Brownian kick with a nested keyed conditional Brownian-tree construction. The children must have the correct duration-scaled variances and sum to the assigned parent kick; proportional division is forbidden. Full/control and fine/coarse runs share the same tree, while zero diffusion produces exact-zero descendants.

## Lock and commitment rule

At exact tongue entry or exit, use the calibrated limiting boundary phase because strict stable phase is undefined at equality. For every strictly eligible interior clock, calculate its moving stable Adler phase from its detuning and instantaneous pulse-scaled coupling.

A clock is locally locking only when it is both strictly inside the fixed angular tolerance and on the locally contracting side of the Adler flow. Equality at either boundary earns no dwell. This prevents the repelling fixed point from counting as locked when stable and unstable phases approach one another near the tongue edge and makes the endpoint rule consistent with the absorbing-boundary audit.

Dwell is timestamp-based. The first qualifying sample records `inside_since` at that sample and receives no retroactive timestep credit. Any band exit, loss of contraction, or loss of eligibility clears the timestamp. The clock commits at the first later sampled time whose elapsed interval reaches the single fixed physical dwell shared by every channel and amplitude. This rule is unchanged when dwell divided by timestep is non-integral.

The trial outcome is the channel of the earliest committing clock. At that instant the simulation stops.

If the pulse ends before either channel commits, the trial is unresolved. That category must be retained rather than conditioned away. Conditioning only on successful commitments could manufacture an apparently clean channel ratio while hiding a strong pulse-duration dependence in the overall detection efficiency.

### Tie handling

Do not break a numerical tie with a coin flip. Record it as a tie and reduce the integration step. The tie fraction is a convergence diagnostic and must be negligible before outcome frequencies are interpreted.

### Why fixed physical dwell is load-bearing

An inverse-coupling dwell would preserve Adler scale similarity and make the quadratic result easier to obtain. It would also make the selection criterion amplitude-dependent. The primary model therefore uses a fixed physical dwell even though this may falsify the candidate.

An inverse-coupling dwell may be run later as a labeled positive control, never as the primary result.

## Analytic control, isolated from event generation

For each coupling, independently calculate the bare sum of deterministic Adler relaxation rates across the exact finite production clocks. This is the primary comparator for a finite competing population. The spacing-weighted continuum flux remains a separately labeled ideal control.

For a flat continuum this must approach the semicircle result: a universal constant times coupling squared.

This module is permitted to use the analytic relaxation rate. The raw stochastic event process must not load it directly or indirectly. It closes and hashes its ledger before a separate comparison process imports the analytic prediction.

The separation should be structural:

```text
analytic.py       predicts the quadratic tongue flux
model.py          evolves phases without seeing that prediction
commitment.py     applies the fixed dwell rule
experiments.py    compares measured outcomes to alternative curves
```

## Experiment sequence

### Experiment 0 — deterministic calibration

- Switch noise off.
- Evolve one clock at several detunings inside the tongue.
- Verify the stable phase and exponential near-lock relaxation rate.
- Verify critical slowing at the tongue edge.
- Verify that an outside-tongue phase keeps slipping.

Run these checks first with constant coupling. Then apply a slow pulse and verify that clocks enter and exit eligibility at the predicted times and that near-boundary clocks lag behind the moving stable phase.

### Experiment 1 — analytic flat-spectrum sum

- Sweep coupling over at least one decade.
- Sum the analytic clock-relaxation rates over the fixed grid.
- Fit the scaling exponent.
- Confirm convergence toward exponent two as the grid is refined.

This checks the proposed mathematics, not the stochastic selection claim.

### Experiment 2 — single-channel transient first-passage law

- Run each coupling alone.
- Measure the full distribution of first commitment times.
- Plot survival probability and instantaneous hazard.
- Test whether the hazard is approximately constant.
- Fit how median time, mean time, and early-time hazard scale with coupling.
- Repeat across pulse durations and record separately: never eligible, eligible but never locked, temporarily locked but dwell-incomplete, and committed.
- Validate endpoint dwell first against an independent stationary killed-diffusion survival oracle; failure is a numerical no-result.
- On a frozen reduced pulsed matrix, apply a diagnostic piecewise-linear Brownian-bridge audit that can only add hidden-exit resets. Its commitments must be a pathwise subset of endpoint commitments, and all paired differences must fit within frozen numerical-error budgets before production interpretation.
- Require every off-grid exact entry/exit to use the shared nested Brownian tree: correctly distributed child kicks, residual parent-sum conservation, refinement nesting, and exact-zero behavior at zero diffusion.
- Fit committed/unresolved binomial counts with a predeclared complementary-log-log cumulative-hazard model, retaining zero/all-event cells and reporting curvature and lack of fit.
- Require a central single-clock control and a fixed-contraction width-only control not to manufacture the same quadratic result. The width-only process keeps the same finite tongue, moving target, noise, dwell, and grid. It exactly preserves full Adler evolution while ineligible and replaces only eligible contraction with one frozen rate. One authoritative unwrapped phase and a continuously lifted target preserve entry, exit, and re-entry without artificial full-turn jumps.
- Treat physical clock count as sensitivity and compare with the exact-grid bare sum; do not call population changes numerical convergence.

This determines whether a Poisson race is justified rather than assumed.

### Experiment 3 — symmetric two-channel control

- Set equal couplings.
- Require A and B to win equally within Monte Carlo uncertainty.
- Swap all labels and random streams; the result must swap exactly in paired tests.

### Experiment 4 — polarization-angle sweep

- Sweep input polarization from near-horizontal to near-vertical.
- Convert the two field projections to linear couplings.
- Measure A wins, B wins, ties, and unresolved trials.
- Compare the outcome curve against three predeclared alternatives:
  - amplitude-linear weighting;
  - amplitude-squared weighting; and
  - deterministic strongest-channel wins.
- Fit an unconstrained exponent rather than reporting only visual agreement with the quadratic curve.

Perform the full angle sweep at several pulse durations. A candidate Born mechanism must preserve the normalized channel ratio once the pulse is long enough for the detector regime being modeled, while any remaining duration dependence must appear honestly in the unresolved fraction.

### Experiment 5 — mechanism sensitivity

Repeat the angle sweep across:

- time-step refinements;
- population sizes;
- noise strengths;
- fixed dwell times;
- lock-band tolerances; and
- initial-phase distributions.
- pulse durations at fixed peak coupling;
- pulse durations at fixed pulse area; and
- raised-cosine versus Gaussian pulse shapes.

A universal Born candidate must not require one finely tuned numerical criterion.

### Experiment 6 — finite-time falsification

- For detunings from the tongue center to its edge, measure time eligible, time locked, and commitment probability.
- Confirm that near-edge clocks suffer critical slowing and are preferentially lost when the pulse closes.
- Test whether increasing the available interaction time raises total commitment probability.
- Test separately whether it changes the normalized A/B winner ratio.
- Compare the result with a stationary-coupling control having the same peak coupling.

If longer pulses merely reduce unresolved trials while leaving the A/B ratio stable, finite synchronization time behaves like detector efficiency. If the A/B ratio changes, pulse duration has entered the proposed selection law and the model does not yet give a universal Born weight.

### Experiment 7 — spectral falsification

Repeat with Gaussian, Lorentzian, and structured detuning densities. Compare observed deviations with the independently calculated rate-weighted tongue flux.

If outcome frequencies remain exactly quadratic while the analytic flux changes strongly, the proposed mechanism is not what drives the simulated result.

## Measurements and saved outputs

Every run should report:

| Output | Purpose |
| --- | --- |
| A/B/tie/unresolved counts | Complete outcome ledger |
| Wilson or exact binomial intervals | Monte Carlo uncertainty without visual guesswork |
| Fitted coupling exponent | Direct test of linear versus quadratic versus other scaling |
| First-commitment survival curves | Checks whether a constant hazard exists |
| Time-dependent hazard estimates | Tests the Poisson-race assumption |
| Eligible-clock counts | Separates tongue width from locking speed |
| Lock-time distributions by detuning | Tests the variable interior of the tongue |
| Eligibility-entry and exit times | Measures the finite window actually available to each clock |
| Never-eligible / lock-failed / dwell-failed counts | Prevents all no-commit events from being conflated |
| Pulse duration, shape, peak, and area | Exposes time-window dependence of both efficiency and channel ratio |
| Time-step convergence | Numerical reliability under the white-noise cutoff |
| Physical population-size sensitivity | Separates clock-count dependence from the coupling exponent |
| Random seed and complete parameters | Reproducibility |

Raw results should be saved as CSV plus a compact JSON manifest. Plots are derived outputs, not the primary record.

## Interpretation matrix

| Result | Interpretation |
| --- | --- |
| Quadratic analytic flux, quadratic direct outcomes, robust across numerical controls | Supports the rate-weighted tongue as a candidate statistical mechanism |
| Quadratic analytic flux, nonquadratic direct outcomes | Locking relaxation is not the detector commitment hazard under the chosen microscopic rule |
| Direct exponent changes with dwell or noise | The outcome law is criterion- or bath-dependent, not universal |
| Longer pulses reduce unresolved trials but preserve the normalized A/B ratio | Finite synchronization time acts like an efficiency factor after a sufficient-duration regime is reached |
| Normalized A/B ratio changes with pulse duration or shape | The proposed outcome weights are time-window dependent and are not yet a universal Born law |
| Near-edge clocks enter but usually fail before closure | Confirms the user's finite-time mechanism and quantifies the failure region |
| Amplitude-linear outcome curve | Tongue eligibility dominates; the interior speed does not supply the needed second factor |
| Strongest channel wins nearly always | Deterministic competition overwhelms stochastic sampling |
| Non-exponential survival curves | A simple first-past-the-post rate formula is invalid even if final frequencies look quadratic |
| Structured spectra cause predicted deviations | Supports the spectral-flux interpretation but creates a strong empirical burden |
| Structured spectra do not affect outcomes | Refutes the claim that the rate-weighted tongue integral controls them |

## Verification contract

Numerical checks should pass independently of whether the scientific hypothesis succeeds:

1. Phase wrapping and angular distances are correct at the negative/positive pi boundary.
2. With noise off, the stable phase matches the Adler fixed point.
3. With noise off, the measured near-lock relaxation matches the analytic rate.
4. Outside-tongue clocks never satisfy the eligibility predicate.
5. The analytic flat-grid sum converges to coupling-squared scaling.
6. Zero coupling produces no eligible clock and no commitment.
7. Equal couplings produce label symmetry under paired random streams.
8. Global phase rotation leaves all results unchanged.
9. Changing only the channel labels swaps the outcome ledger.
10. Noise samples have the declared mean, variance, and independence within statistical tolerance.
11. Dwell counters reset on every lock-band exit.
12. The event generator never receives amplitude squares or analytic hazards.
13. Numerical ties shrink under time-step refinement and are never randomized away.
14. Outcome estimates converge with timestep refinement; population-size dependence is reported separately as a physical sensitivity rather than forced to converge.
15. Fixed seeds reproduce byte-identical raw summaries.
16. Every trial ends in exactly one ledger category: A, B, tie, or unresolved.
17. The scientific fit reports the exponent even when it is far from two.
18. Documentation states that exclusivity, energy routing, and Born's rule remain unproved.
19. The pulse envelope is identical in the two channels and reaches the declared peak and endpoints.
20. Eligibility-entry and exit times agree with the instantaneous tongue boundary in a deterministic test; the finite boundary-phase function is used at equality and strict stable phase only inside.
21. A dwell counter resets when a clock becomes ineligible on the falling edge, even if its phase remains inside the old lock band.
22. Very long, slowly varying pulses approach the stationary-coupling calibration over the central plateau.
23. Shorter pulses never increase a clock's available tongue time at fixed peak and shape convention.
24. Fixed-peak and fixed-area duration sweeps are stored and labeled separately.
25. Every unresolved trial records whether it was never eligible, lock-failed, or dwell-failed.
26. Channel-ratio and total-commitment changes with pulse duration are reported separately; unresolved trials are never silently discarded.
27. Timestamp dwell gives no retroactive credit and preserves one physical dwell for non-integral dwell/timestep ratios.
28. Repelling or locally expanding phases cannot earn dwell inside the proximity band.
29. Endpoint white-noise dwell matches an independent killed-diffusion benchmark, and the diagnostic moving-band bridge audit only adds resets and remains within frozen budgets before production.
30. The primary exponent uses all binomial cells, reports curvature/lack-of-fit, and may return no valid exponent.
31. Central-clock and fixed-contraction width-only controls can defeat a false width-times-rate claim; the width-only reference rate cannot vary with coupling, its ineligible steps match full Adler evolution, and its continuous phase lift survives entry, exit, and re-entry.
32. Raw event generation cannot load analytic code; comparison begins only from a closed hashed ledger.
33. Counter-keyed streamed noise and nested crossing splits are invariant to early stopping, batching, model label, and refinement level; child kicks have correct variances, sum to their parent, and vanish exactly at zero diffusion.
34. Throughput, memory, statistical power, and a finite staged run matrix are frozen before production.

## Proposed codebase fit

Create a new isolated package:

`/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`

| File | Responsibility |
| --- | --- |
| `model.py` | Parameters, pulse envelope, detuning grids, moving stable phases, vectorized stochastic Adler step |
| `commitment.py` | Lock-band and fixed-dwell state machine; tie-safe stopping |
| `analytic.py` | Semicircle/grid prediction only; inaccessible from the event generator |
| `simulate.py` | Single-trial and batched direct simulations |
| `experiments.py` | Calibrations, angle sweeps, sensitivity and spectral controls |
| `observables.py` | Survival, hazard, exponent fits, intervals, complete ledger |
| `verify.py` | The 26 numerical and boundary checks |
| `README.md` | Plain-English mechanism, commands, results, and non-claims |
| `.gitignore` | Cache and generated result directories |

Use NumPy and the Python standard library; SciPy may be used only for clearly isolated statistical fitting or quadrature already available in the environment. Follow the auditable `Result`/registered-check pattern of `first_mark_two_absorber/verify.py`, but do not import or modify that package.

The single-channel prerequisite additionally separates a raw event runner, independent killed-diffusion oracle, binomial analysis, and post-ledger comparison process. The package root must not eagerly import analytic code for a raw run.

## Implementation order

1. Deterministic one-clock stationary Adler calibration.
2. Raised-cosine envelope and deterministic tongue-entry/exit calibration.
3. Analytic finite-grid stationary tongue sum.
4. Vectorized noisy pulsed clock ensemble without competition.
5. Fixed-dwell state machine and single-channel transient first-passage outputs.
6. Symmetric two-channel race and complete outcome ledger.
7. Angle and pulse-duration sweeps with separate efficiency and channel-ratio results.
8. Numerical, physical-population, envelope-shape, and spectral sensitivity sweeps.
9. Independent scientific review before any manuscript use.

Detailed prerequisite plan: [Single-channel stochastic phase noise and fixed-dwell commitment](single-channel-stochastic-commitment).

## Completion boundary

Implementation is complete when the numerical contract passes and the direct simulation produces a reproducible scientific verdict—positive or negative—across the predeclared sensitivity grid.

It is not complete merely because one parameter choice visually resembles the Born curve.
