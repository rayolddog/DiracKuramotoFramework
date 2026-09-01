---
title: "Independent critique: Born-free passive silver-halide plan"
kind: review
---

# Strict verdict

**Not implementation-ready for a conclusion-bearing PFG-01 model under a strict**
**Born-free, material-authority standard.** The revision removes the unsupported
self-sustained Adler oscillator and closes several obvious circular routes. Its
real-field passive oscillator can legitimately produce cycle-averaged absorption
proportional to field amplitude squared. But the plan still leaves the decisive
field-to-electron coupling, electronic-state transition, observable-to-parameter
map, long-horizon stochastic certificate, and development identifiability to be
invented during implementation. Those gaps can reproduce the desired quadratic
response without an explicit `|E|^2` token.

Implementation may begin only as **exploratory feasibility work** on analytic
passivity, evidence inventory, and cost bounds. It may not begin as a physical
PFG-01 prediction pipeline.

# Findings in strict priority order

## 1. Blocker — the semantic firewall does not constrain the unspecified material map

The direct equation and signed-work ledger are sound in form: a driven passive
linear coordinate can yield positive mean work proportional to amplitude squared
without circularity (`model-architecture/index.md:32-97`). The legitimate route
is: solve `q` from signed real forcing, derive the phase-lagged susceptibility,
then obtain mean `E*qdot` from that same trajectory while stored energy, bath work,
and heat close. The forbidden route is to choose `V(q,z)`, an averaged channel
flux, a crossing rule, or a fitted damping/coupling so that it is already a
positive function of field amplitude or oscillator energy.

The plan never writes the actual `V(q,z,r)` or its symmetry, units, charge state,
and evidence constraints (`model-architecture/index.md:46-56,99-126`). Therefore
the claimed only-optical-force rule does not prevent a `q^2 z`, energy-envelope,
or amplitude-dependent effective coupling from installing the square law one
layer later. Likewise, the multiple-scale derivation and full-exposure bound are
future stage 8 outputs, not present mathematics (`model-architecture/index.md:211-244`;
`implementation-sequence/index.md:130-156`). A semantic dependency audit plus a
small mutant list cannot prove equivalence-class absence (`implementation-sequence/index.md:41-53`).

**Minimum revision before physical implementation:** freeze the complete
Hamiltonian/free-energy functional, optical coupling, state variables, and
parameter provenance; derive passivity and every field-to-`z` channel flux from
it; specify which transformations count as forbidden intensity surrogates; and
add adversarial invariants that perturb phase, sign, waveform, carrier frequency,
and equal-energy temporal shape. The accelerated path must remain diagnostic
until the actual derivation—not a promised derivation—has independent approval.

## 2. Blocker — a classical basin crossing is not yet electronic injection

The plan turns an underdamped classical coordinate crossing into creation of an
electron/hole transport state, with dwell/hysteresis suppressing recrossings
(`model-architecture/index.md:99-152`). This is a trajectory-shaped threshold,
not yet a physical model of sensitizer-to-AgBr nonadiabatic electronic transfer.
No donor/acceptor electronic states, charge-state switch, reorganization energy,
electronic coupling, transition rule, back-transfer, or post-transition energy
map is given. A dividing surface and dwell time can be moved to tune yield while
the same coarse kinetics pass. Rejecting recrossings by hysteresis can also break
microscopic reversibility; declaring that the potential “pays the barrier” does
not show where the electronic energy and charge enter the carrier subsystem.

The event ledger records energy around a crossing but does not impose total
energy/charge conservation across the discrete change, local detailed balance,
or a committor/transmission-coefficient criterion (`model-architecture/index.md:108-126`).
The implementation exit merely requires a replayable crossing
(`implementation-sequence/index.md:81-91`), which an arbitrary threshold can satisfy.

**Minimum revision:** choose and justify a material-specific transfer formalism.
At minimum it must define donor/acceptor electronic states and populations,
electronic coupling and reorganization/free-energy surfaces, forward and reverse
transfer, recrossing treatment, bath heat/work, and the exact charge/energy map
into carrier states. Basin commitment must be committor/reactive-flux based or
otherwise independently measured, not a fitted dwell/hysteresis constant. If
only measured transfer rates/yields are available, call the result a calibrated
kinetic surrogate, not a microscopic crossing derivation, and keep it exploratory.

## 3. Blocker — the proposed observations do not identify the declared mechanism

The evidence table names broad data types but not a realizable observation model
(`calibration-and-analysis/index.md:24-44`). Absorption and linewidth can constrain
susceptibility composites; ultrafast decay can constrain rates/yields. Neither by
itself identifies a unique multidimensional `V(q,z,r)`, friction, barrier
distribution, site count, morphology, trap landscape, ion capture, cluster
energetics, and development threshold. Uniform exposure/development data observe
their convolution, so compensating latent-cluster production, site density, and
readout threshold can fit training and held-out macroscopic curves.

The Jacobian/rank gate is insufficient without explicit observables, likelihood,
noise, parameterization, rank tolerance, and structural-identifiability analysis
(`calibration-and-analysis/index.md:68-84`). “Materially different” is undefined.
The plan also demands batch-matched spectroscopy, ultrafast injection, transport,
latent-cluster, morphology, and development evidence without an availability,
sample-consumption, or instrumentation audit (`calibration-and-analysis/index.md:46-66`;
`implementation-sequence/index.md:158-169`). The proprietary/unknown exact
sensitizer and grain microstructure may make composition-matched transferability
unprovable.

**Minimum revision:** add a dataset feasibility manifest for the actual retained
batch, with sample counts and direct/proxy status; define the forward observation
operator and uncertainty model for every calibration datum; perform structural
identifiability before numerical rank; freeze rank and prediction-equivalence
tolerances; and demonstrate with synthetic recovery/profile ensembles that no
admissible composite changes the two-beam prediction. If the required
batch-matched data do not exist, stop at `insufficient_material_calibration`.

## 4. Blocker — no feasible full-exposure numerical certificate is specified

At 640 nm one optical cycle is about 2.1 fs, so even one second contains roughly
`4.7e14` carrier cycles before grain, ion, dark-interval, and development
dynamics are considered. The reference is explicitly short-horizon
(`model-architecture/index.md:194-209`), while authority requires conservative
full-exposure pathwise intervals through discontinuous, rare transfer/trap/cluster
events (`model-architecture/index.md:228-244`). Short-horizon agreement does not
bound secular bias, rare-event probabilities, or threshold classification over a
plate exposure. Near a stochastic threshold, arbitrarily small strong-path error
can change the event time; a generic accumulated interval will often straddle the
boundary and resolve nothing.

No operation count, memory/streaming bound, grains/sites/ions per run, exposure
duration, ensemble size, rare-event method, error-probability definition, or
confidence/power target is budgeted. The ascending cost list postpones rather
than answers this (`implementation-sequence/index.md:241-255`). “Same fine noise
leaves” over the full hierarchy is a coupling design, not a convergence proof.

**Minimum revision:** provide a benchmarked scale model from optical cycles to
plate patch, including storage and ensemble cost; define strong/weak error goals
and probabilistic event-error guarantees; prove an averaging horizon valid for
the longest exposure; validate rare-event estimators without target-conditioned
bias; and freeze a maximum certified physical horizon. If that horizon cannot
reach a predeclared measurable exposure, the stop result is `no_resolved_test`,
not a future implementation promise.

## 5. Blocker — FDT and detailed balance are incomplete across the state changes

The polarization covariance is stated for a classical underdamped bath
(`model-architecture/index.md:58-66`), but the transfer coordinate has damping
without a declared covariance (`model-architecture/index.md:99-106`). At optical
electronic frequencies, a classical white thermal bath also requires an explicit
coarse-graining justification; it cannot silently claim microscopic electronic
equilibrium. The carrier SDE is consistent only if `mu` means mechanical mobility
in a homogeneous landscape; electrical-mobility units, position-dependent
mobility, constraints, and boundaries require corresponding Einstein factors and
noise-induced drift (`model-architecture/index.md:128-149`). Ag-ion motion,
neutralization, cluster binding/dissolution, and irreversible charge-state changes
have no equations establishing local detailed balance or chemical reservoirs
(`model-architecture/index.md:154-171`).

Key exclusions are directionally correct, and the existing keyed-noise component
does provide a reusable “value belongs to physical key, coarse increments are
sums of fine leaves” pattern, as the parent claims (`index.md:109-124`). But the
new plan does not yet define time-cell/species/site keys, event-created degrees of
freedom, or how paired paths remain solver-independent after their event graphs
diverge (`implementation-sequence/index.md:55-65,145-153`).

**Minimum revision:** write one thermodynamic contract for every continuous and
discrete subsystem: invariant distribution, covariance/convention, chemical
potential, forward/reverse rule, heat/work attribution, and charge/atom balance.
Define physical-time-addressed noise for dynamically born particles and prove
subdivision, stopping, path-divergence, and equilibrium invariance. Add dark
detailed-balance tests beyond histogram agreement.

## 6. Blocker — development can still absorb the desired response

The plan declares `n_develop`, lifetime, and accessibility independently
calibrated (`model-architecture/index.md:173-192`), but uniform exposures followed
by development generally reveal developed output, not the unobserved
pre-development cluster-size distribution conditional on morphology. Thus
cluster production, dissolution, accessibility, fog, and threshold/amplification
remain confounded. A deterministic Boolean does not solve this; it can be a
high-capacity readout fitted to the same plate curves that constrain upstream
kinetics. `development_site_is_accessible` is especially undefined.

**Minimum revision:** require an independent assay of latent-cluster size/state
before development and a separate response curve of development conditional on
known cluster state, morphology, developer, time, and temperature. Freeze a
low-dimensional readout with uncertainty and show upstream predictions are
invariant across all admissible readouts. Otherwise report the cluster ledger
only and keep `developable` exploratory.

## 7. Bounded hardening — isolation is well designed but not yet enforceable

The raw/final/Adler direction is explicit (`index.md:55-83`;
`model-architecture/index.md:246-278`), and final grain agreement is correctly
excluded from solver admission. Remaining risk is operational: import allowlists
do not prove that final analysis cannot rewrite exposure/manifests, and “after
closure” is not an access-control mechanism. Joining by position is safe only if
the comparator process has read-only access to content-addressed raw artifacts
and cannot trigger regeneration.

**Minimum revision:** specify separate executable identities/capabilities,
one-way content-addressed handoff, immutable preregistration and raw closure, and
negative tests for configuration, filesystem, cache, environment, and IPC leaks.
Give the Adler package no dependency edge to verdict or grain-construction types.

## 8. Blocker — falsification and stop rules are mostly qualitative

The matrix is useful coverage, but phrases such as “within coherence
uncertainty,” “beam-profile-corrected,” “independently predicted,” and “materially”
have no numerical acceptance region, sample size, power, multiplicity rule, or
uncertainty propagation (`calibration-and-analysis/index.md:165-187`). Several
failures identify an entire subsystem rather than a discriminating hypothesis.
The “zero-net cyclic forcing” control is ambiguous: zero-mean forcing can still
do positive dissipative work, while zero net signed work must be defined over the
closed field/material/bath ledger before it can diagnose rectification
(`calibration-and-analysis/index.md:177-180`). The stop rules likewise use
undefined “fail refinement,” “identifiable,” “indistinguishable,” and
“incompatible” (`implementation-sequence/index.md:224-239`).

**Minimum revision:** preregister numerical thresholds, uncertainty coverage,
sample sizes/power, convergence order and tolerance, decision ownership, and a
unique machine-readable outcome for every test combination. Rewrite the
zero-work control in ledger terms and separate model-rejection tests from tests
that merely return insufficient resolution.

# What is already a valid bounded foundation

- The passive real-field equation, signed work, no clipping/dark subtraction,
and closed-ledger intent are a legitimate route to emergent classical
squared-field absorption (`model-architecture/index.md:32-97`).
- Proxy/assumption evidence is barred from physical conclusions, composites are
acknowledged, and final-fringe refitting is forbidden
(`calibration-and-analysis/index.md:6-44,110-120`).
- Direct/accelerated admission compares trajectories, energies, crossings, and
shared noise rather than the desired final image
(`model-architecture/index.md:228-244`).
- The Adler branch is correctly demoted and quarantined
(`model-architecture/index.md:246-257`).

These are necessary controls, not evidence that the missing microscopic and
numerical contracts exist.

# Evidence required before conclusion-bearing implementation

1. Frozen explicit material Hamiltonian/free-energy and a reviewed derivation of
 signed optical work through every averaged channel.
2. A material-justified electronic-transfer/state-transition model with reverse
 dynamics, recrossing, detailed balance, and charge/energy conservation.
3. A batch-specific evidence availability audit plus a structurally identifiable
 observation model and synthetic recovery/holdout demonstration.
4. A benchmarked multiscale/rare-event cost and full-exposure probabilistic error
 certificate reaching a measurable predeclared exposure.
5. Complete FDT/local-detailed-balance contracts and solver-independent physical
 path keys across event-created degrees of freedom.
6. Independent pre-development latent-cluster evidence and conditional readout
 calibration, or removal of the physical `developable` claim.
7. Quantitative preregistered falsification thresholds and stop rules.

Until all seven exist, the only defensible terminal physical status is
`insufficient_material_calibration`, `numerically_unresolved`, or
`no_resolved_test`; a PFG-01-class recording verdict is premature.
