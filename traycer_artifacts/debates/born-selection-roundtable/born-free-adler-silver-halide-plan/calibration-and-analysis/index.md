---
title: "Passive-material calibration, analysis firewall, and falsification"
kind: spec
---

# Calibration authority

PFG-01 manufacturer data freeze the material name, nominal wavelength region,
bulk exposure scale, processing chemistry and published characteristic/grain
curves. They do **not** identify the microscopic passive model.

Every parameter or identifiable parameter group has one evidence class:

| Class | Meaning | Physical prediction allowed? |
| --- | --- | --- |
| Batch-matched direct measurement | Measured on the actual plate batch or a retained witness sample under the declared processing | Yes, inside its uncertainty/domain |
| Composition-matched literature | Same sensitizer/AgX morphology and compatible temperature/process, with uncertainty inflation | Only after an explicit transferability review |
| Proxy material | Different emulsion, sensitizer, grain morphology or processing | Exploratory simulation only |
| Assumption | No independent measurement | Exploratory simulation only |

The gate fails closed with a missing-evidence table. It never tunes an unknown
parameter against the final interference pattern.

Before model fitting, an `EvidenceAvailabilityManifest` inventories the actual
retained plate batch, sensitizer/emulsion identity that is truly known, every
dataset and raw digest, instrument/access status, sample count and destructive
sample use, uncertainty, evidence class and frozen training/holdout role. A
measurement merely named in this plan but not in hand or contractually available
is `evidence_unavailable`, not future calibration.

# Parameter-to-evidence map

Before implementation, the calibration manifest must name how each group is
constrained:

| Model group | Required independent evidence |
| --- | --- |
| Dye/exciton resonance, damping and coupling | Batch-matched absorption/reflectance, linewidth and temperature dependence; time-resolved fluorescence or transient absorption |
| Exciton-network coupling/disorder | Spectral line shape, polarization dependence and independently justified aggregate morphology |
| Electronic transfer | A selected donor/acceptor formalism plus ultrafast forward/back injection, charge-separation, recrossing/recombination and temperature data; rates alone authorize only a kinetic surrogate |
| Electron/hole mobility, traps and recombination | Conductivity, transient charge decay, thermally stimulated or equivalent trap measurements |
| Ag-ion mobility and capture | Ionic-conductivity/diffusion evidence at plate-relevant temperature plus silver-halide latent-image studies |
| Cluster binding, dissolution and dark survival | Latent-image cluster measurements or validated atomistic/coarse-grained calculations tied to the actual AgX morphology |
| Grain/site morphology | Grain-size distribution, sensitizer coverage, sensitivity-center density and emulsion thickness |
| Latent cluster | Pre-development cluster size/state and dark-survival assay |
| Development readout | Response conditional on independently known cluster state and morphology under the exact developer, time and temperature |
| Fog/background | Dark storage and process-only controls across temperature and batch |

If evidence identifies only a composite (for example `Q^2/m` from absorption),
the manifest stores that composite rather than pretending its factors are known.
Separate values may be sampled only when the final prediction is invariant over
the admissible factorization.

# Calibration experiment design

The calibration set is frozen before any two-beam raw run:

1. dark/process-only controls at several temperatures and dark intervals;
2. uniform single-beam spectroscopy across wavelength and polarization;
3. time-resolved excitation/transfer measurements across at least three field
amplitudes inside the unsaturated range;
4. uniform plate exposures crossing toe, useful-density and shoulder regions,
with irradiance and duration varied independently;
5. dark-delay series to identify trap/cluster survival;
6. development-time and temperature series on separate witness samples.

Training and holdout conditions are named in advance. At least one irradiance,
one duration, one temperature and one development condition remain untouched
until the model and parameters are frozen.

A single uniform exposure may validate a plate-level scale but cannot calibrate
polarization coupling, transfer efficiency, barrier distribution, site count and
development threshold together. The previous one-condition scale permission is
removed.

# Identifiability gate

Identifiability is checked **before** a physical interference prediction:

- write the explicit forward observation operator and likelihood/noise model for
every calibration datum;
- prove structural identifiability modulo declared symmetries before numerical
rank; otherwise store the identifiable composite;
- construct the whitened sensitivity `J_w = Sigma_y^-1/2 J diag(s_theta)` using
frozen scientific parameter scales;
- require full claimed rank, smallest retained singular value `>= 1`, and
condition number `<= 100`;
- profile weak directions or retain an ensemble of all admissible parameter
sets rather than selecting one optimum;
- require 500 preregistered synthetic-recovery datasets to attain simultaneous
95% interval coverage inside the exact binomial acceptance region at level
`0.01`;
- replay 99% predictive holdouts without refitting;
- refuse a physical conclusion when admissible sets change a scope-authorized
reported quantity by more than one preregistered experimental standard error;
for developed fraction the additional absolute limit is `0.02`.

The gate reports `insufficient_material_calibration` with the unresolved
parameter combinations. A good fit to a final fringe cannot cure failed
identifiability. Alternative thresholds must be scientifically justified and
frozen before any two-beam result; they cannot be loosened after failure. The
full contract is in the [authority packet](../preimplementation-authority-gates).

# Numerical-admission gate

A measured `FeasibilityEnvelope` precedes solver admission. It freezes the
carrier-cycle count, sites/grains/carriers/ions, direct and maximum certified
horizons, rare-event method and target probabilities, replicate/effective sample
sizes, operations, wall time, peak RSS and storage. At 640 nm the plan prices
approximately `4.7e14` optical cycles per second rather than hiding them in an
“envelope” label.

The direct optical-cycle solver is the reference. The accelerated
envelope/multiscale solver has only three states:

- `diagnostic_only`;
- `admitted_within_certified_domain`;
- `equivalence_failed`.

The linear passive network is first accelerated by its exact causal
susceptibility/Green function. Admission of any other multiscale approximation
binds the formal averaging derivation, source, noise projection,
parameter domain and full-exposure error certificate. The validation matrix
spans phase, beam ratio, amplitude, wavelength/detuning, linewidth, temperature,
transfer barriers, transport/trap regimes, cluster stability and distances to
every event threshold.

Required metrics include fast trajectories, per-cycle signed field work,
inter-coordinate energy flux, admitted electronic forward/back transitions,
slow-state events, rare-event weak error and conservative accumulated threshold
margins. With at least 99% confidence, the family-wise probability that numerical
approximation changes any conclusion-bearing event or grain classification in
the declared patch must be `<= 0.01`. Final grain or classical intensity
agreement is never an admission metric.

A conclusion-bearing case outside the certified domain returns
`numerically_unresolved`. Direct fallback is permitted only if its complete cost
and run are recorded; it is not promised as a theoretical escape hatch. If the
maximum certified horizon is shorter than the shortest measurable predeclared
exposure, the result is `no_resolved_test`.

# Calibration data that are forbidden

Before the raw prediction is frozen, calibration may not use:

- a two-beam interference fringe or any spatial phase label;
- `|E_object + E_reference|^2` or an equivalent renamed array;
- an intensity exponent, fringe visibility target or image-quality metric;
- an exposure chosen because it improves agreement with the comparator;
- final developed-grain agreement as evidence for solver equivalence;
- an Adler-locking label or locked fraction as evidence for energy transfer;
- unrestricted refitting after a holdout or two-beam result is opened.

# Exposure selection

Exposure windows are selected from material and numerical criteria only:

- the manufacturer/batch useful density range;
- measurable response above fog and below saturation;
- calibrated transfer/trap/cluster timescales;
- dark survival and processing limits;
- full-exposure numerical certification;
- a predeclared maximum plate dose and thermal/vibration budget.

The selected grid includes more than one irradiance and duration so reciprocity
cannot be imposed by a single dose variable. If no window is simultaneously
calibrated, measurable, unsaturated and numerically certified, the outcome is
`no_resolved_test`.

# Final-analysis firewall

Only after raw manifests and all ledgers are closed does a separate process
revalidate the compiled bootstrap/recovery chain; complete signed gate records;
capability, field/domain, run-commitment and claim-receipt signatures; and same-
byte store inclusion. It generates a new 256-bit nonce and obtains a one-use
`final_analysis` latest-head lease carrying identical signatures from at least
two of three authorized freshness witnesses. The lease must bind this process,
nonce, boundary and exact `FinalAnalysisSubject/v1`/
`FinalReportPreimage/v1` digests; consistently extend
the durably persisted head; resolve one active trust/recovery manifest; and bind
the complete effective revocation set. After append-logging the lease, the
coordinator persists its exact inclusion head `H1`. It freezes the exact report
payload bytes/ID, the receipt payload expected at `H2`, the canonical release-
result template payload ID, the analysis-release key authorized by the leased
manifest and its completion-grant template. The template binds every
release field except the not-yet-known receipt identifiers, signatures, release
payload ID and signed-envelope object digest.

One expected-head transaction then requires the current log head to equal `H1`
and the active manifest/epochs/effective-revocation digest to equal the leased
view; verifies the frozen release key, result template and grant template under that
same view; and in one linearizable authority-store/WAL commit appends the
`LeaseUseReceipt/v1` envelope at `H2`, derives its payload ID/object digest, and
stores the coordinator `consumed` row, **exact report bytes**, report payload ID,
release template, unique receipt-bound `AnalysisReleaseRecord/v1` payload
bytes/ID, payload-specific release-key completion grant derived from that ID,
`H2` and every recovery locator. Any intervening append or authority
change makes the CAS fail with no receipt or fixed result; the same immutable
subject requires a fresh lease and recomputed template. An uncommitted WAL makes
none of those records authoritative; a committed WAL is self-sufficient after
process loss. After the transaction, only the payload-specific grant fixed at
`H2` may have that key deterministically sign the exact stored release payload.
The boundary appends the report and signed release envelope idempotently and
records `completed(release_payload_id, release_object_digest)`. Only then may a
physical presentation be returned.

A crash after receipt append may finish only the stored report-and-release
payload with the key/grant fixed at `H2`; it cannot obtain a new lease, alter
the payload or substitute a later release key. Signing is cryptographic completion
of the issuance logically fixed at `H2`, not a later authorization decision.
If the fixed signer cannot complete, the boundary is terminal `consumed_failed`
and repeat queries return the same failure; no substitute key may sign. Normal
retirement after `H2` preserves only this restricted completion grant until it
resolves and does not permit arbitrary retired-key signing. Retroactive key
invalidation reaching `H2` or a direct revocation of the stable release payload
ID disables the grant, atomically records `consumed_failed` with that reason and
withholds it under Gate G. A report appended without
the completed matching release is an immutable noncurrent child and must not be
presented. Correction requires a new subject/report/release while leaving raw
bytes unchanged. An age-bounded checkpoint or a report without this completed
chain is not currentness evidence.

The analysis validates every reopened schema against
`AUTHORITY_OBJECT_REGISTRY/v1`, then applies the exhaustive Gate-G revocation-
target matrix, including the sole parent route for nonrevocable field/domain/raw
children. Its effective set starts from all valid revocations at the accepted
head and subtracts every retroactive-revocation digest having its own valid
controlling recovery repair and exhaustive current re-closure. Repair decisions
are ordered and resolved independently per target; a later repair of another
digest cannot reactivate or erase an earlier disposition. Trust, lease,
checkpoint, gate, capability or authority-object revocation failure takes
precedence as `authority_capability_invalid`; only with that layer valid can a
run commitment, claim, close or child-object failure be
`run_commitment_invalid`. A retroactive revocation always withholds the physical
result. A nonretroactive revocation effective after close preserves a result
only when its signed `post_close_effect` is exactly
`preserve_completed_run`; `withhold_completed_run` withholds it and a missing or
incompatible effect fails authority. The process then computes

```text
I_classical(x) = |A_object(x) + A_reference(x)|^2
```

It joins that classical comparator to frozen latent-cluster results by position
only when a `latent_cluster_physical` capability is present. Developed-grain
and film observables are joined only with a `developed_film_physical`
capability. It reports without feeding anything back:

- phase translation and latent-cluster spatial contrast; film visibility only
with developed-film authority;
- normalized shape error and uncertainty;
- nonparametric cluster response versus field amplitude; and, only with admitted
readout authority, `P(developable | field amplitude)` as an empirical summary;
- exposure-, duration-, temperature- and processing-dependent response;
- latent-cluster size distributions, fog, spatial correlations and
overdispersion;
- sensitivity across the full admissible calibration ensemble;
- solver/error-certificate provenance for every record;
- all preregistered negative and mechanism controls.

`psi_squared` and `Born` may appear only in an optional interpretation report.
The primary result remains a statement about real classical fields and
silver-halide grain recording.

# Falsification matrix

| Test | Frozen passive-model expectation | Failure means |
| --- | --- | --- |
| Dark/process-only | Calibrated fog and thermal events only | Bath, trap, cluster or development model is wrong |
| Single beam | Beam-profile-corrected uniform response | Field calibration or material homogeneity is wrong |
| Relative-phase translation | Grain pattern translates by the geometric phase shift without refitting | Coherent real-field drive is not reaching the modeled material path if absent |
| Phase scrambling | Cross-term contrast vanishes within coherence uncertainty | Nonlocal artifact, key contamination or incorrect field model |
| Equal dose, different duration | Independently predicted reciprocity or reciprocity failure | Transfer/trap/cluster kinetics are wrong |
| Wavelength scan | Response follows independently calibrated dye/AgBr spectrum | Polarization/transfer model is wrong |
| Temperature scan | Predicts linewidth, transport, trap, ion and dark-survival changes | Bath or kinetic model is wrong |
| Dark-delay scan | Predicts latent-cluster survival without refitting | Trap/cluster stability is wrong |
| Sensitizer-removed control | Removes dye-mediated transfer contribution | Claimed sensitizer authority is wrong |
| Transfer coupling disabled | No injected carrier from that channel | Detects hidden rate or energy leakage |
| Zero closed-ledger field work | No persistent chemical state unless a named bath/chemical reservoir supplies the energy | Detects work clipping or unledgered energy |
| Zero-mean AC forcing | Positive dissipation may occur and must match the analytically derived passive-work prediction | Distinguishes legitimate absorption from a false zero-work control |
| Direct versus accelerated | Trajectory, channel-energy and event agreement inside the certified domain | Rejects the accelerated solver |
| Development chemistry variation | Frozen latent image maps to independently calibrated readout changes | Development threshold/amplification is wrong |
| Parameter ensemble | All admissible calibrations preserve the reported conclusion | Exposes non-identifiability |

The decisive question is not merely whether a fringe appears. It is whether
independently constrained passive trajectories predict energy transfer, latent
clusters, exposure/reciprocity behavior, fluctuations and processing response
without fitting the final fringe.

# Acceptance language

Every row above has a machine-readable `DecisionRule` fixed before data: estimand
and unit, null/alternative, sample size, minimum effect, uncertainty/simultaneous
coverage, multiplicity rule, numerical tolerance/order, missing-data rule and one
outcome owner. Default policy is two-sided family-wise `alpha = 0.01` with Holm
correction and power `>= 0.90` at the preregistered minimum effect. Numerical
refinement must demonstrate its declared order with a 99% confidence bound and
keep total numerical error below one quarter of the experimental acceptance
half-width.

Undefined phrases such as “materially different,” “within coherence
uncertainty,” or “indistinguishable” are prohibited in executable criteria; the
manifest must supply their numbers before the run.

Permitted physical outcomes are:

- `material_authority_missing`;
- `transfer_authority_missing`;
- `evidence_unavailable`;
- `insufficient_material_calibration`;
- `thermodynamic_authority_missing`;
- `latent_cluster_authority_missing`;
- `development_authority_missing`;
- `authority_capability_invalid`;
- `run_commitment_invalid`;
- `no_resolved_test`;
- `passive_model_inconsistent`;
- `numerically_unresolved`;
- `envelope_equivalence_failed`;
- `latent_image_prediction_frozen`;
- `classical_recording_consistent`;
- `classical_recording_inconsistent`.

The two `classical_recording_*` outcomes require a validated
`developed_film_physical` capability. A physical
`latent_image_prediction_frozen` outcome requires a validated
`latent_cluster_physical` capability. If F1 is open, only
`latent_cluster_authority_missing` and nonphysical diagnostics are permitted; if
F1 is closed but F2 is open, the cluster result may be frozen but cannot be
translated into film density, visibility or developability.

The isolated active-model report may emit only `adler_counterfactual_only` and
diagnostic locking quantities. No path may emit `Born_rule_derived`,
`single_photon_selection_derived`, or a claim that PFG-01 contains an Adler
oscillator.
