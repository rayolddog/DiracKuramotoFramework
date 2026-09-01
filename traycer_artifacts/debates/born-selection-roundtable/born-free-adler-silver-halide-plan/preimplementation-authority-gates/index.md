---
title: "Preimplementation authority gates for the passive silver-halide model"
kind: spec
---

# Current readiness

**Feasibility-only.** No conclusion-bearing PFG-01 simulation may be built or
presented until the exact closure profile for that output has a closed,
independently reviewed record and a valid scope capability. A physical latent-
cluster result and a developed-film result have different profiles; neither is
enabled by a generic “packet closed” flag.
The allowed work is limited to evidence inventory, analytic passive-response
fixtures, candidate electronic-transfer formalisms, structural-identifiability
analysis and scale/cost benchmarks.

Missing authority is a result, not a parameter choice:

| Missing gate | Required terminal status |
| --- | --- |
| Exact material functional or field coupling | `material_authority_missing` |
| Justified electronic-transfer formalism | `transfer_authority_missing` |
| Required retained-batch data unavailable | `evidence_unavailable` |
| Structural/practical identifiability fails | `insufficient_material_calibration` |
| Certified horizon shorter than measurable exposure | `no_resolved_test` |
| Numerical uncertainty crosses an event/readout boundary | `numerically_unresolved` |
| Bath/FDT, detailed-balance, conservation or noise-key authority | `thermodynamic_authority_missing` |
| Independent latent-cluster evidence unavailable | `latent_cluster_authority_missing` |
| Conditional development readout unavailable | `development_authority_missing` |
| Capability signature, trust chain, store object or revocation check invalid | `authority_capability_invalid` |
| Exact Stage-11 run commitment absent, changed, out of domain or already consumed | `run_commitment_invalid` |

# Scope-specific closure profiles

| Output scope | Gates that must be closed | Permitted output |
| --- | --- | --- |
| `diagnostic_only` | No physical capability | Schemas, real-field/key fixtures, analytic linear-polarization diagnostics and explicitly exploratory transfer/transport fixtures only |
| `latent_cluster_physical` | A, B, C, D, E, F1, G and H | Physical latent-cluster ledger and `latent_image_prediction_frozen`; no `developable`, density, visibility or film claim |
| `developed_film_physical` | A, B, C, D, E, F1, F2, G and H | Conditional developed-grain/film output and classical-recording comparison within the certified domain |

An open required gate yields its exact status; the system may not silently fall
back to a narrower physical scope. A caller must request the narrower scope
explicitly and satisfy its complete profile.

# Independent-review closure map

The review findings are converted into gates rather than answered with new
fitted constants:

| Review blocker | Required closure | Fail-closed consequence |
| --- | --- | --- |
| A flexible material potential or averaged channel can install a hidden squared-field law | Gate A fixes the exact field coupling and Gate D audits every analytic or averaged reduction against real-field work | `material_authority_missing` or `no_resolved_test` |
| Classical coordinate crossing does not justify electronic injection | Gate B requires a reviewed electronic-state formalism, reverse dynamics, recrossing and exact charge/energy handoff | `transfer_authority_missing` |
| Available measurements do not identify the microscopic groups or separate latent image from development | Gate C requires an evidence inventory, forward operators and structural/practical identifiability; Gates F1/F2 require separate cluster and readout streams | `evidence_unavailable`, `insufficient_material_calibration`, `latent_cluster_authority_missing` or `development_authority_missing` |
| Optical-cycle-to-exposure separation and rare events may be computationally infeasible | Gate D requires a measured resource and probabilistic error envelope before production work | `no_resolved_test` or `numerically_unresolved` |
| Bath, carrier, ion and event-created-state noise lacks a complete thermodynamic/key contract | Gate E requires FDT or named reservoirs, local detailed balance, conservation and physical-time keys | `thermodynamic_authority_missing` |
| Development thresholds can absorb the desired spatial response and qualitative tests can pass by interpretation | Gates F1/F2 separate latent-state evidence from readout and Gate H freezes numerical decision rules | `latent_cluster_authority_missing`, `development_authority_missing` or the relevant inconsistency status |

The capability concern that spans all six findings is handled by Gate G:
conclusion-bearing raw code cannot see a comparator, and exploratory modules
cannot construct physical outcome records.

# Gate A — exact material functional and field coupling

The first admitted subsystem is the independently testable passive linear
polarization network:

```text
H_pol(q,p;E) = 1/2 p^T M^-1 p + 1/2 q^T K q - E(t) d^T q
```

with `M` and `K` positive definite and damping/bath authority specified in Gate
E. `M`, `K` and `d` are field-independent. Nonlinear, excitonic or
reaction-coordinate terms cannot enter merely because they improve the final
response. Each additional term requires:

1. exact algebra, dimensions, symmetries and boundedness/passivity proof;
2. a one-to-one source map from coefficient or identified composite to an
independent observable;
3. a declared validity domain;
4. sign, carrier-phase, waveform-shape and carrier-frequency controls that
distinguish trajectory-derived work from an energy-envelope surrogate;
5. independent review before any physical raw module imports it.

The sole optical interaction in the first authority is `-E d^T q`. Higher-order
field couplings are prohibited unless independently measured and separately
reviewed. A field-independent material term such as `q^2 z` is not automatically
forbidden, but it cannot become authoritative without its own evidence map and
the controls above.

# Gate B — electronic-transfer authority

A classical dividing-surface crossing is no longer presumed to create an
electron. Two explicitly different products are allowed:

## B1. Empirical kinetic surrogate

Measured forward/back transfer and recombination kinetics may drive a
coarse-grained state model. It must be labelled `kinetic_surrogate`, may test
engineering consistency, and cannot claim a microscopic Born-free derivation.
Its rates may depend only on independently measured state variables and frozen
material conditions, never on the final comparator.

## B2. Microscopic-transfer candidate

A conclusion-bearing candidate must freeze:

- donor and acceptor electronic states and charge assignments;
- electronic coupling and nuclear/reorganization coordinates;
- the evolution law for electronic state/population and nuclei;
- forward transfer, back transfer and recrossing/commitment;
- local detailed balance or the precisely named nonequilibrium reservoirs;
- charge, atom and total energy mapping across every state change;
- the observation that identifies each term and the approximation domain.

If commitment is represented by a dividing surface, it requires an independently
validated committor/reactive-flux or transmission-coefficient rule. A fitted
dwell/hysteresis interval is insufficient. Any quantum or semiclassical
formalism must state exactly where probabilities enter and may not be described
as a derivation of Born selection.

Gate B closes only after a specialist material-physics review. Until then, the
reaction-coordinate implementation is exploratory.

# Gate C — evidence availability and identifiability

Before fitting, an `EvidenceAvailabilityManifest` inventories the actual retained
plate batch and witness samples:

| Field | Required content |
| --- | --- |
| Material identity | manufacturer, batch, emulsion/sensitizer information actually known |
| Dataset | observable, instrument, units, raw-file digest, sample count, temperature/process |
| Evidence class | batch-matched, composition-matched, proxy or assumption |
| Access | data in hand, instrument/time secured, or unavailable |
| Destructive use | witness samples consumed and samples remaining |
| Uncertainty | calibration, repeatability and batch components |
| Training/holdout role | frozen before model fitting |

Every parameter group has an explicit forward observation operator and
likelihood/noise model. Structural identifiability is required before numerical
fitting: the operator must be injective modulo declared symmetries or the model
must store the identifiable composite. Practical identifiability uses the
whitened sensitivity

```text
J_w = Sigma_y^-1/2 J diag(s_theta)
```

where `s_theta` is a frozen scientifically meaningful parameter scale. The
default admission rules are:

- `rank(J_w)` equals the number of claimed identifiable groups;
- smallest retained singular value `>= 1` and condition number `<= 100`;
- 500 preregistered synthetic-recovery datasets have simultaneous 95% interval
coverage inside the exact binomial acceptance region at level `0.01`;
- no admissible parameter set changes any scope-authorized reported quantity by
more than one preregistered experimental standard error; for developed
fraction the additional absolute limit is `0.02`;
- all frozen holdouts pass their model-specific 99% predictive checks without
refitting.

If these defaults are scientifically inappropriate, replacements must be
justified and frozen before any two-beam result exists. They cannot be loosened
after failure.

# Gate D — timescale, rare-event and resource feasibility

The plan acknowledges that a 640 nm carrier has a period near 2.1 fs, or about
`4.7e14` cycles per second. A direct full-exposure path is not presumed feasible.

A `FeasibilityEnvelope` must be measured before production implementation:

- carrier cycles, polarization sites, grains, carriers and ions represented;
- direct-reference horizon and why it covers the fastest transfer physics;
- candidate maximum certified physical horizon;
- operations, wall time, peak RSS, storage and number of stochastic replicates;
- rare-event estimator, target event probabilities and effective sample size;
- strong trajectory error where pathwise claims are made;
- weak distributional error for event/count claims;
- family-wise probability that any reported grain is misclassified.

The default global error budget is `0.01`: with at least 99% confidence, the
probability that numerical approximation changes any conclusion-bearing event or
grain classification in the declared patch must be at most 1%. The budget is
allocated across solver, rare-event and threshold errors before the run.

The passive linear polarization network should be eliminated analytically by its
causal susceptibility/Green function when possible. A numerical envelope is not
needed merely to rediscover that exact response. Nonlinear or transfer-coupled
averaging remains diagnostic until direct comparisons and a conservative
long-horizon weak-error proof close.

If the maximum certified horizon is shorter than the shortest predeclared
measurable exposure, the result is `no_resolved_test`. An uncosted direct
fallback is forbidden.

# Gate E — thermodynamic, FDT and noise contract

Each continuous and discrete subsystem declares its invariant measure,
stochastic convention and energy/particle ledger.

For an underdamped classical coordinate:

```text
dq = M^-1 p dt
dp = -grad U dt - Gamma M^-1 p dt + sqrt(2 k_B T Gamma) dW
```

For an overdamped coordinate with position-dependent mobility `Mu(r)`, the Itô
form includes noise-induced drift:

```text
dr = [-Mu grad U + k_B T div Mu] dt + sqrt(2 k_B T Mu) dW
```

Electrical mobility is converted to mechanical mobility with explicit units.
At optical electronic frequencies the classical white-bath formula is not
automatically valid; a measured spectral density or a reviewed quantum/colored
bath is required. Its use does not authorize a quantum measurement claim.

Every discrete transition satisfies

```text
k(i->j) / k(j->i) = exp[-beta (Delta F - W_reservoir)]
```

or names and ledgers the nonequilibrium chemical reservoir that invalidates
equilibrium detailed balance. Ion neutralization, cluster binding/dissolution and
developer chemistry each conserve charge and atoms and record heat/chemical
work.

Noise keys are addressed by physical master identity, potential particle/site,
bath channel and absolute fine-time interval. Potential carrier/ion identities
exist before the event that activates them, so divergent paths address the same
counterfactual leaves. Solver, arm, outcome and model label never enter a
physical key. Coarse increments are derived from the same fine leaves.

Admission tests include invariant-distribution, forward/reverse flux,
Crooks/local-detailed-balance where applicable, subdivision, stopping-time,
path-divergence and charge/atom/energy conservation—not histogram agreement
alone.

If any required subsystem lacks this contract, Gate E is open, no physical
record may be constructed for either scope, and the exact terminal status is
`thermodynamic_authority_missing`.

# Gate F1 — latent-cluster authority

A physical cluster ledger requires independent pre-development evidence of
latent cluster size/state, morphology, assay detection limits and dark survival,
plus an explicit forward operator from the modeled cluster state to that assay.
Gate C must show that the cluster-producing parameters are identifiable from
this evidence without using developed density or the final interference fringe.

If this evidence or identifiability is absent, cluster simulation remains an
exploratory diagnostic and the only physical status is
`latent_cluster_authority_missing`. It cannot emit
`latent_image_prediction_frozen`.

# Gate F2 — conditional development readout

After F1 closes, `developable` remains exploratory until a second, independent
evidence stream exists:

1. a conditional development response measured for known cluster state,
morphology, developer, time and temperature;
2. process-only fog and developer/time/temperature controls on separate samples.

The readout is a frozen low-dimensional model with uncertainty. Upstream latent
cluster predictions must remain invariant across all admissible readouts. If the
conditional readout evidence cannot be obtained, an F1-authorized run may stop
at the latent-cluster ledger and report `latent_image_prediction_frozen` plus
`development_authority_missing`; it may not infer developability, film density
or interference visibility.

# Gate G — capability-enforced closure

Authority activation is a constructor boundary, not a declarative manifest
field.

## G0. Fixed bootstrap profile and recovery anchors

The verifier and physical raw executable compile in
`GateGBootstrapProfile/v1`. The profile fixes, rather than negotiates:

- deterministic CBOR under RFC 8949;
- SHA-256 object and key identifiers;
- Ed25519 signatures;
- a distinct ASCII domain separator for every signed object type;
- one offline root public-key fingerprint;
- three offline recovery public-key fingerprints with a two-of-three threshold;
- one authority-log ID and genesis root from which every accepted trust,
revocation and witness transition must consistently extend;
- rejection of every unknown version, algorithm, encoding or domain separator.

An unverified manifest cannot select the rules used to verify itself. The
root-signed `AuthorityTrustManifest` may name only keys, roles, service
endpoints, epochs and validity sequences permitted by this bootstrap profile;
it cannot replace the pinned log ID or genesis. `key_id` is
the SHA-256 digest of the fixed algorithm identifier plus public-key bytes and
must be unique across roles.

The manifest authorizes separate keys for scientific owners by gate, reviewers
by gate/scope, capability/run issuers, transparency-checkpoint signers,
revocation signers, claim-service signers and checkpoint witnesses. A principal
may not hold both scientific-owner and reviewer roles for the same gate record.
It also authorizes a separate analysis-release signer. Raw, analysis and
exploratory processes possess no signing private key.

A normal trust transition is a root-signed `TrustTransition` binding old/new
manifest digests, old/new epochs, activation log sequence and exact key
retirements. Old signatures remain verifiable for objects issued before
activation. Retirement forbids new logical issuance at or after activation,
but an HSM completion grant durably fixed by an earlier receipt sequence may
sign only its named stored payload after retirement. The retirement transition
retains that restricted key operation until every listed grant reaches
`completed` or `consumed_failed`; it cannot authorize any other payload. A
retroactive invalidation reaching the receipt sequence disables the grant.
After root compromise,
a `RecoveryTransition` requires two of the three pre-pinned recovery signatures,
increments a monotonic recovery epoch, installs a new root and declares the
earliest invalid sequence. Every affected scope is independently re-closed. If
the recovery threshold or verifier/OS trust boundary is compromised, there is no
in-band recovery; a reviewed verifier update is required.

## G1. Complete signed gate closure

Each gate uses one canonical `GateClosureRecord` binding:

- schema/version, gate ID, exact requested scope/profile digest and decision;
- source/executable, material, calibration and solver-domain digests;
- evidence, conformance-result, decision-rule and independent-review digests;
- trust/recovery epoch, validity sequences and owner/reviewer key IDs.

The authorized scientific owner and a distinct gate/scope-authorized reviewer
each sign the complete record bytes under separate domain separators. The
isolated issuer verifies both signatures, roles, validity sequences and every
referenced object before accepting the record. A capability binds an exhaustive
`gate_id -> GateClosureRecord digest` map; an omitted, duplicated or extra gate
refuses. Signatures establish authenticated approval, not the truth of mistaken,
malicious or collusive scientific evidence.

## G2. Immutable store, witnessed latest-head leases and file authority

Every stored schema admitted by `AUTHORITY_OBJECT_REGISTRY/v1` is content-
addressed at `objects/sha256/<digest>` in one append-only Merkle log. Latest-head
leases and lease-use receipts enter that same log before their boundary
succeeds. The bootstrap order is:

1. verify the trust manifest directly with the pinned bootstrap root/profile;
2. obtain its fixed log ID, genesis root and authorized checkpoint/witness keys;
3. verify a checkpoint and consistency proof from genesis or the last persisted
trusted checkpoint;
4. verify object inclusion only under that accepted checkpoint.

A canonical `StoreCheckpoint` binds log ID, tree size, root hash, previous-
checkpoint digest, trust/recovery epoch, active trust-manifest digest, complete
revocation-set digest, issuance time and sequence. It requires the authorized
checkpoint-signer signature and signatures from at least two of three
independent authorized freshness witnesses. A verifier durably persists its
last accepted log ID, tree size, root and checkpoint digest before accepting a
newer view. Every later view must be a strictly monotonic consistent extension.
Equal tree size with a different root, a broken consistency proof, conflicting
witnessed views or a lower sequence is `authority_capability_invalid` and
requires manual resolution.

A checkpoint age bound is only an availability diagnostic; it is **not** proof
that the checkpoint is current. At each authority boundary the verifier creates
a cryptographically random 256-bit nonce and requests a canonical
`LatestHeadLease/v1` from the freshness-witness quorum. The lease binds:

- log ID, requester/verifier identity, exact subject digest and the exact boundary
(`scope_mint`, `run_commit`, `raw_start`, `raw_close` or `final_analysis`);
- nonce, issue time, expiry no more than 60 seconds later and a one-use lease ID;
- current tree size/root/checkpoint digest and a consistency proof from the
verifier's durably persisted head;
- the uniquely active trust-manifest digest, trust epoch and recovery epoch at
that head;
- the complete effective revocation-set digest and latest effective sequence;
- the identities and signatures of at least two of the three authorized
freshness witnesses.

Each witness must query the same configured append-log service for its current
head after receiving the nonce, durably remember its highest signed tree size
per log ID and never sign a lower or inconsistent head. It refuses if it cannot
obtain a current view, sees witness disagreement, cannot prove consistency, or
cannot resolve one unique active trust/recovery manifest and revocation set. The
verifier accepts only quorum responses with identical lease payloads, begins
the expected-head consumption workflow immediately at its named boundary, and
append-logs a durable `LeaseUseReceipt` before the boundary succeeds. A lease is not transferable
across boundary, requester, subject, nonce or run and cannot be cached. Replayed,
expired, already-used, wrong-boundary, split-view or ancestor-head responses
fail as `authority_capability_invalid`.

Lease consumption is one expected-head compare-and-append operation. The lease
first witnesses authority head `H0`; its own append produces and durably records
the exact lease-inclusion head `H1`. Before consumption, the coordinator freezes
the planned receipt payload bytes, sole-result template (every field except the
receipt identifiers, signatures, payload ID and envelope digest), authorized
result-signer key and completion-grant template for the next log
sequence `H2`. The atomic `leased -> consumed` transaction must:

1. require the log's current head to equal `H1` exactly, with no intervening
append;
2. require the active trust/recovery manifest, epochs and complete effective-
revocation-set digest at `H1` to equal the values witnessed in the lease at
`H0` (the lease append itself changes none of them);
3. verify that the fixed result signer is authorized at that view;
4. atomically envelope and append `LeaseUseReceipt/v1` at `H2`, derive its
payload ID and object digest, construct the unique full result payload bytes and
payload ID from the stored template plus that receipt, and construct/store the
fixed completion grant binding that result payload ID, key, `H2`, permitted
signature operation and terminal-state record.

If the head, manifest, epoch or revocation digest differs, the transaction
appends no receipt and fixes no result. The lease becomes stale/abandoned; after
expiry or explicit abandonment the same immutable subject must obtain a fresh
nonce/lease and recompute its receipt/result bundle. This includes benign
unrelated appends: availability yields to a single unambiguous authorization
view. A prepared template for a failed transaction is unusable because its
lease never received a receipt. The log/store must expose
this expected-head CAS-plus-append primitive; otherwise every boundary fails
closed.

This is immediate-boundary rather than time-window authorization. A revocation
or transition appended after `raw_start` is detected by the mandatory fresh
lease at `raw_close`; nothing becomes a physical conclusion until a third fresh
lease passes at `final_analysis`. A revocation may explicitly preserve a
completed run under G5, but no earlier lease can conceal its existence. If the
log, quorum or trusted clock is unavailable, the boundary fails closed. The
contract does not claim to prevent denial of service or to provide continuous
authorization between boundaries.

The receipt sequence is the logical issuance sequence of its already fixed sole
result. A normal nonretroactive key rotation or retirement appended after
that sequence does not rewrite the fixed result. The key service may execute
only the payload-specific completion grant stored at `H2`; this is completion
of earlier issuance, not new issuance under a retired key. The transition must
retain or escrow that restricted operation until it resolves. A retroactive
transition whose earliest invalid sequence reaches the receipt disables the
grant and withholds the result. Direct revocation targets the stable result
`payload_id`; inherited parent revocation applies G5. The next boundary
evaluates the completed envelope under that signed timing policy.

### G2.1 Canonical boundary subjects and receipt state machine

The abstract boundary-subject envelope is deterministic CBOR with the bootstrap
domain separator, log ID, boundary enum, requester identity, exact run/scope
identity and one immutable preimage digest. It is not itself a stored schema.
The stored schemas are the five exact subject types below. No subject contains
the result, lease, use receipt or its own identifier.

Every authority object uses two noninterchangeable identifiers:

1. `payload_bytes` are canonical unsigned bytes. They exclude `payload_id`, all
signatures, `object_digest` and enclosing-store metadata.
`payload_id = SHA256(payload_domain || payload_bytes)` is the stable scientific
and revocation identity.
2. `SignedEnvelope/v1` contains the exact payload bytes, payload ID, schema and
domain, signer-key ID and signature over the domain-separated payload ID and
bytes. It excludes `object_digest`.
`object_digest = SHA256(envelope_domain || envelope_bytes)` identifies the
completed stored envelope and Merkle-log object.

The canonical decoder recomputes both identifiers and refuses a self-identifier
inside either hash preimage. A coordinator `consumed` row stores the result
`payload_id`; `completed` additionally stores its signed-envelope
`object_digest`. Descendants bind both identifiers whenever they depend on a
signed parent. Direct result revocations target `payload_id`, so a result can be
withdrawn after `H2` even before signature completion. Merkle inclusion,
same-byte retrieval and API return identify the final `object_digest` together
with its payload ID. No signature or envelope digest is an input to its own
payload, receipt or signature.

`LeaseUseReceipt/v1` unsigned payload binds the boundary/subject/lease; witnessed authority head
`H0`; exact lease-inclusion head `H1`; receipt/logical-issuance sequence `H2`;
active manifest, trust/recovery epoch and effective-revocation digests; fixed
sole-result **template payload ID** and authorized result-signer key ID. It
contains neither its payload ID nor envelope digest. The authority-log service
envelopes and appends it at `H2`; the result payload binds the receipt payload ID
and receipt object digest. The final result payload or envelope digest is absent
from the receipt, so the graph is acyclic. These fields are planned before
consumption and become authoritative only if the expected-head transaction
appends those exact bytes at `H2`.

| Boundary | Immutable subject preimage | Sole permitted result and required binding |
| --- | --- | --- |
| `scope_mint` | `ScopeMintSubject/v1` over `CapabilityPreimage/v1`: scope/profile, exhaustive gate map and every capability payload field except issuer signature, lease/use-receipt identifiers, payload ID and envelope digest | `AuthorityClosureCapability` binds subject, lease and use-receipt payload IDs/object digests |
| `run_commit` | `RunCommitSubject/v1` over `RunCommitmentPreimage/v1`: capability, field/domain, run/namespace/master, source/material/calibration/solver/rules, stochastic/replicate/resource fields except issuer signature, lease/use-receipt identifiers, payload ID and envelope digest | `RunCommitment` binds subject, lease and use-receipt payload IDs/object digests |
| `raw_start` | `RawStartSubject/v1` over `RawStartPreimage/v1`: exact run-commitment digest, run ID and attempt ID | `ClaimReceipt` is the sole result; the commitment claim service atomically assigns the commitment to this subject, consumes the lease, appends the use receipt and fixes the receipt result |
| `raw_close` | `RawCloseSubject/v1` over `RawClosePreimage/v1`: exact capability, run commitment, claim receipt and canonical `RawManifest/v1` digest | `CloseMarker` binds subject, lease and use-receipt digests |
| `final_analysis` | `FinalAnalysisSubject/v1` over `FinalReportPreimage/v1`: exact close marker, analysis executable/configuration, frozen comparator specification and complete report payload except lease/use-receipt, payload ID, signature and envelope digest | `AnalysisReleaseRecord/v1` is the sole completed result and binds the exact `FinalReport/v1`, subject, lease and use-receipt chain |

Except for the commitment-keyed `raw_start` transaction specified in G4, one
durable linearizable boundary coordinator owns `(boundary, subject_digest)`.
Its exhaustive progression is:

```text
unleased
  -> leased(attempt_id, lease_digest, expiry, H1)
  -> abandoned(attempt_id, lease_digest, reason)
  -> leased(new_attempt_id, new_lease_digest, expiry, H1)

leased(attempt_id, ...)
  -> consumed(attempt_id, lease_payload_id, lease_object_digest,
              receipt_payload_id, receipt_object_digest,
              result_payload_id, signer_key_id, completion_grant_id, H2)
  -> completed(result_payload_id, result_object_digest)
  -> consumed_failed(result_payload_id, completion_grant_id, reason)
```

`abandoned` is an immutable attempt record, not a terminal subject state. A
single active-attempt pointer permits the retry edge shown above. Expiry alone
does not mutate state. Expiry-triggered or explicit abandonment CASes the exact
active `attempt_id` from `leased`; consumption CASes that same ID. Exactly one
wins, so a late response from an abandoned attempt appends nothing. Queries
return the durable attempt and subject state; an ambiguous consume is treated
as `consumed` whenever it may have committed. `consumed_failed` is terminal and
repeat queries return its fixed reason and payload ID; it cannot be retried with
a new lease, subject, payload or key. A semantically corrected operation needs a
new subject preimage.

For `scope_mint`, `run_commit` and `raw_close`, the exact order is: freeze the
subject; obtain and append the nonce-bound quorum lease; persist its exact
inclusion head; precompute the next-sequence receipt; construct and, where
required, freeze the sole-result template and authorized signer; atomically
compare the current head and authority digests, append the receipt, and store
the unique receipt-derived result payload bytes/payload ID; use only the stored
payload-specific completion grant to sign and append its envelope; durably
record `completed(result_payload_id, result_object_digest)`; only then return
success.
Post-receipt signing is explicitly cryptographic completion of the issuance
fixed at `H2`, not a new authorization event. The `raw_start` claim service combines this expected-head
operation with the commitment CAS specified in G4. The `final_analysis`
coordinator uses the same operation for its report-and-release bundle specified
below and in the analysis firewall. A receipt is valid only for its subject,
one active lease, one authority head and one fixed result. No old receipt can
authorize a new preimage or result.

Crash and retry behavior is exact:

- before receipt append, the boundary has not succeeded; after the active lease
expires the coordinator may mark it abandoned and issue a fresh nonce/lease
for the **same immutable subject**. A late receipt for an abandoned lease
loses the coordinator compare-and-append and refuses;
- after receipt append but before result completion, the subject is locked.
Recovery may only invoke the payload-specific completion grant fixed at `H2`
to sign and append/complete the exact result payload stored by the consume
transaction. Normal retirement does not disable that restricted grant;
retroactive invalidation reaching `H2` or direct revocation of the result
payload ID disables it and CASes `consumed -> consumed_failed` with the exact
revocation reason. A fresh lease, substitute key,
changed result or changed subject is forbidden;
- after result append or completed-state persistence but before caller receipt,
a query returns the same result payload ID/object digest and never repeats the
boundary;
- `raw_start` is not a generic subject-only transaction. Under G4, one atomic
commitment-keyed transition assigns the commitment to the immutable subject,
consumes that subject's lease, append-logs its use receipt and fixes the sole
`ClaimReceipt`. No losing subject can append a receipt. After that transition,
the commitment remains consumed even if the raw attempt crashes; recovery may
finish only the winning receipt, and only a new commitment/run ID may start
another attempt;
- `final_analysis` is completed only by the exact
`AnalysisReleaseRecord/v1`. After receipt consumption, recovery may append only
the frozen `FinalReport/v1` and release bundle accepted by
the expected-head consume transaction. Before that transaction, the coordinator
fixes the report bytes/digest, release key ID, canonical release-record template
and logical issuance sequence `H2`. The transaction verifies the release key is
active at the unchanged leased authority view, appends the receipt, derives its
identifiers, and in the **same linearizable authority-store/WAL commit** stores
the coordinator `consumed` row, exact report bytes and report payload ID,
receipt payload ID/object digest, release template, unique receipt-bound release
payload bytes/payload ID, fixed key/completion grant, `H2` and every descriptor-
pinned recovery locator. An uncommitted transaction makes none of those items
authoritative. The committed WAL is sufficient without the originating process
to reproduce every later byte. Obtaining the deterministic signature through
that fixed completion grant and appending the report/release envelopes are
idempotent completion of an issuance already fixed at `H2`, not a new
authorization event. The sole
`completed` transition accepts only that release payload ID and signed-envelope
object digest.
A report without that release may remain as an immutable noncurrent child but
is never a completed or current physical presentation;
- if deterministic completion of `scope_mint`, `run_commit`, `raw_close` or
`final_analysis` is impossible, the subject terminates failed and cannot be
reused. A failed `final_analysis` may not expose its report; a new or corrected
analysis requires a new preimage and boundary. A new semantically changed
operation always requires a new preimage digest.

All store access begins from a pinned directory descriptor. Each path component
is opened relative to that descriptor with beneath/no-symlink semantics; the
final object uses no-follow, is `fstat`-verified as a regular file, is digested
from that descriptor and those exact verified bytes are consumed without
reopening a pathname. A handle is only a locator for this fresh read.

## G3. Scope capability

The isolated issuer signs a canonical `AuthorityClosureCapability` containing:

- exact scope and exhaustive required-gate/profile digest;
- the exhaustive signed gate-record map from G1;
- source/executable, schema, material, calibration, solver-domain and decision-
rule digests;
- trust/recovery epoch, issuer key ID, accepted store-checkpoint digest and the
consumed `scope_mint` boundary-subject/latest-head-lease/lease-use-receipt
digests;
- validity sequence interval and the canonical payload digest.

Every physical constructor reopens and verifies the root/recovery chain, owner,
reviewer, issuer, checkpoint and witness signatures; log consistency/inclusion;
every already-consumed ancestor boundary receipt and completed signed envelope;
then separately obtains the current boundary's new, as-yet-unconsumed
`LatestHeadLease` and verifies its uniquely active trust manifest and complete
effective revocation set; the complete gate map; and exact scope/source/domain
agreement. Missing, self-consistent-but-unauthorized,
forged, subclassed, replaced, partial, stale, wrong-scope or mismatched inputs
refuse before any key or directory is touched. A capability can authorize a
domain but is never a run authorization and cannot silently downgrade scope.

## G4. Exact run commitment and linearizable claim

`FieldManifest/v1` is canonical and exhaustive. It binds coordinate frame and
units; beam/source positions; propagation/wave vectors; carrier frequency and
wavelength; polarization vectors; real amplitudes; real waveform/envelope and
coherence model; phases and timing; exposure durations; temperatures; dark
delays; controls; developer/process schedule; and its schema digest.

An issuer-signed, content-addressed `RunCommitment` binds:

- capability, trust/recovery epoch, accepted checkpoint and `run_commit`
boundary-subject/latest-head-lease/lease-use-receipt digests;
- exact `FieldManifest/v1` digest;
- run ID, output namespace and physical master identity;
- source/executable, material, calibration, solver/certificate and decision-rule
digests;
- stochastic namespaces, replicate identities and resource limits;
- a `DomainValidationRecord` naming the verifier/version, every checked bound,
exact value and certified-domain digest.

Stage 11 loads and consumes the exact committed field-manifest bytes; it does
not regenerate, edit or reselect a schedule.

The trust manifest authorizes one `CommitmentClaimService`, and that service is
the `raw_start` boundary coordinator. It owns a single linearizable transaction
indexed by the commitment payload ID and carrying the immutable subject digest.
Its exhaustive commitment-level progression is:

```text
unclaimed
  -> claimed_consumed(subject_digest, attempt_id, lease_payload_id,
                      receipt_payload_id, receipt_object_digest,
                      claim_payload_id, claim_signer_key_id,
                      completion_grant_id, issuance_sequence)
  -> completed(claim_payload_id, claim_object_digest)
  -> consumed_failed(claim_payload_id, completion_grant_id, reason)
```

Before the commitment leaves `unclaimed`, its subject lease may traverse the
generic `leased -> abandoned -> leased` attempt loop. Abandonment CASes the
active lease attempt while leaving the commitment `unclaimed`; the atomic claim
CAS checks both that exact active attempt and `unclaimed`. Once
`claimed_consumed`, neither abandonment nor reassignment is legal. Queries of
`consumed_failed` return the same terminal record forever.

Before `unclaimed -> claimed_consumed`, the claim service precomputes the next-
sequence receipt payload and freezes the claim-result template payload ID,
authorized signer key and completion grant.
The compare-and-append is one durable operation: it checks the exact lease-
inclusion head and leased authority digests under the shared rule above;
verifies the claim-service key at that view; assigns the commitment to that
exact subject; marks the lease used; append-logs the matching
`LeaseUseReceipt` envelope; derives its payload ID/object digest; and stores the
unique full `ClaimReceipt` payload bytes/payload ID, the payload-specific
completion grant derived from the grant template and logical issuance sequence. No
use receipt or authoritative claim exists before this transition commits. This
is one transactional CAS-plus-log-append primitive in the configured authority
store, not two best-effort writes across the claim and log services; if that
primitive is unavailable, `raw_start` fails closed. Two distinct subjects for one commitment race on the same
record: exactly one commits and every loser receives `claimed_by_other_subject`
without consuming its lease, appending a receipt, consuming a key or creating a
directory. A late receipt from an abandoned or losing subject cannot pass the
same compare-and-append.

After `claimed_consumed`, recovery may only invoke the fixed claim-service
completion grant to deterministically sign the stored payload, append that
exact `ClaimReceipt` envelope and
advance to `completed`; the same subject then receives the same result. This is
completion of issuance at the stored receipt sequence. If signing cannot be
completed, the commitment enters terminal `consumed_failed` and is never
reassigned. A crash or ambiguous response is queried by commitment digest and
is treated as consumed whenever this transaction may have committed. Claims are never released. A raw attempt that crashes is
nonresumable, and every new attempt requires a new issuer-signed commitment and
run ID. These commitment-keyed rules override the generic subject-only retry
rule for `raw_start` and make post-receipt deterministic completion compatible
with exactly one winning subject.

`RawManifest/v1` is canonical and exhaustive. It binds the run/capability/claim
identities; material and solver manifests; ordered, schema-tagged digests for
every trajectory block, transfer/carrier ledger, cluster ledger and grain
ledger; table row counts and schemas; and no unlisted raw object. Every raw
block occurs exactly once. The close marker binds capability, commitment,
field-manifest, domain-validation, claim-receipt, accepted-checkpoint,
`RawManifest/v1`, `raw_start` subject/lease/use receipt and `raw_close`
subject/lease/use-receipt digests. Final analysis reopens the same objects and
obtains a new `final_analysis` lease before it may expose a `FinalReport/v1`.

## G5. Exhaustive revocation-target matrix and status precedence

Root or two-of-three recovery authority signs trust-role revocations. A root-
authorized revocation signer may sign only the direct targets in the closed
table below; it cannot revoke the root, recovery threshold or its own role.
Every `RevocationRecord/v1` binds target digest and exact object type, effective
log sequence, reason, retroactive flag, earliest invalid sequence when
retroactive, signer role, `post_close_effect` and record digest. The closed
`POST_CLOSE_EFFECTS/v1` enumeration is `not_applicable`,
`preserve_completed_run` or `withhold_completed_run`. Unknown targets, object
types or effects refuse rather than inheriting an implementation-defined
meaning.

The ordinary revocation signer's closed `REVOCABLE_OBJECT_TYPES/v1` enumeration
is exactly:

```text
evidence_object
material_authority_record
calibration_authority_record
solver_authority_record
conformance_result
decision_rule
independent_review
gate_closure_record
authority_closure_capability
run_commitment
claim_receipt
close_marker
analysis_release_record
```

Trust-role/key changes are a separate root/recovery mechanism, not members of
that enumeration. A signed revocation is immutable and cannot itself be revoked
or deleted. A mistaken nonretroactive revocation is repaired only by creating
new authority objects with new digests; a mistaken retroactive revocation needs
a `RecoveryTransition/v1` under the exact repair rule below. Silent
“un-revocation” is forbidden.

The compiled `AUTHORITY_OBJECT_REGISTRY/v1` is the exhaustive schema-to-
revocation map. The physical store refuses a schema ID absent from this table;
adding a schema requires a reviewed bootstrap/registry revision.

| Canonical stored or signed schema IDs | Lifecycle class / direct tag or sole immediate invalidation parent | Inherited terminal status |
| --- | --- | --- |
| `GateGBootstrapProfile/v1`, `AUTHORITY_OBJECT_REGISTRY/v1` | Compiled verifier lifecycle only | `authority_capability_invalid` |
| `AuthorityTrustManifest/v1`, `TrustTransition/v1`, `RecoveryTransition/v1` | Root/recovery lifecycle only | `authority_capability_invalid` |
| `StoreCheckpoint/v1`, `LatestHeadLease/v1`, `LeaseUseReceipt/v1` | Currentness/consistency/one-use lifecycle; signer-role invalidation by sequence | `authority_capability_invalid` |
| `ScopeMintSubject/v1`, `CapabilityPreimage/v1` | Nonrevocable child; sole parent `AuthorityClosureCapability/v1` | Parent authority status |
| `RunCommitSubject/v1`, `RunCommitmentPreimage/v1` | Nonrevocable child; sole parent `RunCommitment/v1` | Parent run status after authority passes |
| `RawStartSubject/v1`, `RawStartPreimage/v1` | Nonrevocable child; sole parent `ClaimReceipt/v1` | Parent run status after authority passes |
| `RawCloseSubject/v1`, `RawClosePreimage/v1` | Nonrevocable child; sole parent `CloseMarker/v1` | Parent run status after authority passes |
| `FinalAnalysisSubject/v1`, `FinalReportPreimage/v1`, `FinalReport/v1` | Nonrevocable child; sole parent `AnalysisReleaseRecord/v1` | Parent release authority status |
| `EvidenceObject/v1`, `EvidenceAvailabilityManifest/v1` | Direct tag `evidence_object` | `authority_capability_invalid` |
| `MaterialManifest/v1` | Direct tag `material_authority_record` | `authority_capability_invalid` |
| `CalibrationAuthorityRecord/v1` | Direct tag `calibration_authority_record` | `authority_capability_invalid` |
| `SolverManifest/v1`, `FeasibilityEnvelope/v1` | Direct tag `solver_authority_record` | `authority_capability_invalid` |
| `ConformanceResult/v1` | Direct tag `conformance_result` | `authority_capability_invalid` |
| `DecisionRule/v1` | Direct tag `decision_rule` | `authority_capability_invalid` |
| `IndependentReview/v1` | Direct tag `independent_review` | `authority_capability_invalid` |
| `GateClosureRecord/v1` | Direct tag `gate_closure_record` | `authority_capability_invalid` |
| `AuthorityClosureCapability/v1` | Direct tag `authority_closure_capability` | `authority_capability_invalid` |
| `FieldManifest/v1`, `DomainValidationRecord/v1`, `StochasticManifest/v1`, `ReplicateManifest/v1`, `ResourceManifest/v1` | Nonrevocable child; sole parent `RunCommitment/v1` | `run_commitment_invalid` after authority passes |
| `RunCommitment/v1` | Direct tag `run_commitment` | `run_commitment_invalid` after authority passes |
| `ClaimReceipt/v1` | Direct tag `claim_receipt` | `run_commitment_invalid` after authority passes |
| `RawManifest/v1` | Nonrevocable child; sole parent `CloseMarker/v1` | `run_commitment_invalid` after authority passes |
| `TrajectoryBlock/v1`, `TransferCarrierLedger/v1`, `ClusterLedger/v1`, `GrainLedger/v1` | Nonrevocable child; sole parent `RawManifest/v1` | Raw-manifest then close-marker run status |
| `CloseMarker/v1` | Direct tag `close_marker` | `run_commitment_invalid` after authority passes |
| `AnalysisReleaseRecord/v1` | Direct tag `analysis_release_record`; signed by the authorized analysis-release service and binds close marker, final report and final-analysis subject/lease/use receipt | `authority_capability_invalid` for that release; raw status remains separately inspectable |
| `RevocationRecord/v1` | Immutable revocation lifecycle; repair only through the recovery rule below | Existing target status until repair activates |

Aliases are forbidden: the architecture terms “material manifest,” “solver
manifest,” “trajectory block,” “transfer/carrier ledger,” “cluster ledger,”
“grain ledger” and “run manifest” mean exactly the versioned IDs above; “run
manifest” is renamed `RawManifest/v1`. A conformance or evidence subtype remains
inside its exact registered envelope and cannot invent a new top-level schema.

For a nonretroactive object revocation, `post_close_effect` is mandatory:

- `preserve_completed_run` is legal only when the close marker was completed
before the revocation's effective sequence. It blocks every future start or
close depending on the target but permits analysis of that already closed run
while displaying the revocation and preservation decision;
- `withhold_completed_run` blocks every later analysis/release of the affected
completed run while retaining immutable bytes for audit;
- `not_applicable` is legal only for trust lifecycle/currentness objects that
cannot directly preserve a physical run;
- every retroactive revocation requires `withhold_completed_run`; a missing or
incompatible value is `authority_capability_invalid`.

For nonretroactive direct targets, the evidence/material/calibration/solver/
conformance/rule/review/gate/capability/run/claim/close tags may spell either
preserve or withhold. `analysis_release_record` may spell only
`withhold_completed_run`, because revoking the release cannot leave that same
report current. Trust/recovery/currentness lifecycle objects use only
`not_applicable`. Nonrevocable children inherit the compatible value from their
sole parent and never carry an independent policy.

An exceptional repair of a mistaken retroactive revocation is possible only in
`RecoveryTransition/v1`. Each repair decision targets exactly one immutable
retroactive `RevocationRecord/v1` digest and binds the reason, superseding
recovery epoch, activation sequence, exhaustive affected-scope digests and new
independently signed gate/capability re-closure digests. It may not target a
nonretroactive revocation, another repair or recovery/trust transition, itself,
or a circular dependency.

Repair evaluation is cumulative and independent per revoked digest. Let
`R(H)` be every valid revocation at or before head `H`. For each `r` in `R(H)`,
select only repair transitions that target exactly `r`, activate at or before
`H`, are valid under the recovery chain at `H`, and have complete validating
affected-scope re-closures. The controlling repair for `r` is the maximum
ordered tuple `(recovery_epoch, activation_sequence, log_sequence)` among those
candidates. A conflict at the same tuple is `authority_capability_invalid`.
Then:

```text
effective_revocations(H) =
  {r in R(H) | no valid controlling repair exists for r}
```

A later transition repairing unrelated `r2` neither removes nor reactivates the
repair disposition of `r1`; no transition implicitly replaces a global repair
set. A later repair of the same `r` may supersede its earlier repair record only
with a strictly greater tuple and a complete replacement re-closure bundle. It
cannot reverse the repair back into a revocation; a newly discovered defect
requires a new `RevocationRecord/v1` against the repaired/reclosed authority
objects. `TrustTransition/v1` cannot repair a revocation. Every original
revocation and repair byte remains in the log forever.

| Stored or signed object class | Directly revocable? / authorized mechanism | Child or parent effect | Exact terminal routing |
| --- | --- | --- | --- |
| Compiled bootstrap profile, pinned root and recovery fingerprints | No in-band revocation; reviewed verifier replacement or G0 recovery only | Invalidates every descendant authority object | `authority_capability_invalid` |
| `AuthorityTrustManifest`, `TrustTransition`, `RecoveryTransition` | Root transition or two-of-three recovery only; ordinary revocation signer forbidden | Determines all active roles/epochs; recovery may invalidate from its earliest sequence | `authority_capability_invalid` |
| Role/key grant for owner, reviewer, issuer, checkpoint signer, witness, revocation signer or claim service | Root or recovery authority | New signatures at/after effective sequence refuse; prior signatures follow retirement/retroactivity row below | `authority_capability_invalid` |
| `StoreCheckpoint`, `LatestHeadLease` and `LeaseUseReceipt` | Not independently revocable | Currentness, consistency, subject, nonce, expiry, one-use and active-manifest checks govern; signer-role revocation invalidates them by sequence | `authority_capability_invalid` |
| `evidence_object`, `material_authority_record`, `calibration_authority_record`, `solver_authority_record`, `conformance_result`, `decision_rule`, `independent_review`, `gate_closure_record` | Yes, ordinary revocation signer under the exact enum above | Invalidates every gate record/capability/run depending on the target | `authority_capability_invalid` |
| `authority_closure_capability` payload ID | Yes, ordinary revocation signer | Invalidates every descendant run commitment, claim, close and physical conclusion | `authority_capability_invalid` |
| `FieldManifest/v1`, `DomainValidationRecord/v1`, `StochasticManifest/v1`, `ReplicateManifest/v1`, `ResourceManifest/v1` | No separate revocation | Content-addressed children of one `RunCommitment/v1`; revoke that parent | `run_commitment_invalid` after authority passes |
| `run_commitment` payload ID | Yes, ordinary revocation signer | Invalidates its claim receipt, close marker, raw ledger and conclusion | `run_commitment_invalid` after authority passes |
| Claim-service role/key | Root or recovery authority | Invalidates claim receipts signed at/after effect; retroactivity may invalidate earlier receipts by sequence | `authority_capability_invalid` because the trusted service role failed |
| `claim_receipt` payload ID | Yes, ordinary revocation signer | Invalidates its close marker, raw ledger and conclusion | `run_commitment_invalid` after authority passes |
| `close_marker` payload ID / physical dataset identity | Yes, ordinary revocation signer | Withholds that dataset and every derived physical conclusion | `run_commitment_invalid` after authority passes |
| `RawManifest/v1` | No separate revocation | Sole immediate parent is `CloseMarker/v1` | `run_commitment_invalid` after authority passes |
| `TrajectoryBlock/v1`, `TransferCarrierLedger/v1`, `ClusterLedger/v1`, `GrainLedger/v1` | No separate revocation | Sole immediate parent is `RawManifest/v1` | Raw-manifest then close-marker run status |
| `analysis_release_record` payload ID | Yes, ordinary revocation signer, including after `H2` but before envelope completion | Withdraws the report it authorizes without altering immutable raw bytes | `authority_capability_invalid` for that release; upstream raw status remains separately inspectable |
| `FinalReport/v1` and final-analysis subject/preimage | No separate revocation | Sole immediate parent is `AnalysisReleaseRecord/v1`; corrected analysis requires a new subject, report and release record | Same as the parent release record |
| `RevocationRecord/v1` | No; immutable and irreversible inside its epoch | New objects or exact `RecoveryTransition/v1` repair above | Existing target status remains until the permitted repair activates |

Timing is evaluated against the exact current head in the boundary's nonce-bound
lease, never against a cached age window:

| Case | Required behavior |
| --- | --- |
| Normal key retirement | Reject new logical issuance at/after activation. Preserve only H2-issued, payload-specific completion grants and their restricted HSM/escrow operation until each reaches `completed` or `consumed_failed`; no arbitrary retired-key signing is allowed |
| Commitment issued before retirement and claimed afterward | Allowed only if commitment/issuer validity has not expired and the `raw_start` lease proves no applicable revocation |
| Claim before retirement, close afterward | May finish only if the `raw_close` lease proves the applicable object chain remains valid |
| Nonretroactive direct or inherited revocation effective before a boundary | That boundary refuses according to the object-class routing table |
| Nonretroactive revocation after completed close | Raw bytes remain immutable; `final_analysis` applies the record's explicit preserve/withhold policy and may not infer one |
| Retroactive compromise/scientific invalidation | Withhold every affected present and later conclusion from the declared earliest invalid sequence, even if raw start and close previously passed |
| Any append after lease inclusion but before receipt consumption | Expected-head CAS fails, appends no receipt/result and requires a fresh lease for the same immutable subject, even when the append is otherwise unrelated |
| Normal signer retirement after a completed receipt sequence | The payload ID, key and completion grant fixed at that sequence remain an issued historical result. That grant may complete only that payload after retirement; retroactive invalidation reaching H2 disables it, and direct revocation of the payload ID still applies |
| Latest-head lease, revocation view or quorum unavailable, expired, replayed, rolled back or equivocated | Fail closed; do not mint, start, close or analyze |

Status precedence is deterministic:

1. bootstrap, trust/recovery chain, signer role, checkpoint/witness, latest-head
lease/use receipt, store, gate-record, scope-capability or analysis-release
revocation-state failure yields
`authority_capability_invalid`;
2. only after step 1 passes, a missing/mismatched/out-of-domain/revoked/consumed
run commitment, field manifest, domain record, claim receipt or close marker yields
`run_commitment_invalid`;
3. only after both pass may material, numerical or scientific outcomes be
evaluated.

Scope mint, run commitment, raw start, raw close and every final analysis each
perform the current check with a new nonce-bound lease. Later normal retirement
does not erase a valid completed run; a matching retroactive record does.

## G6. Isolation, threat boundary and required attacks

Exploratory records live below the authority layer and cannot import or
serialize physical record, capability or verdict types. Preregistration/raw,
claim service, issuer/store, analysis-release service and final comparison run
under separate executable identities. Raw writes only a new directory and has no comparator/final config;
analysis has only read-only closed descriptors and cannot regenerate; Adler has
no grain/verdict dependency.

Within an honest pinned bootstrap/recovery threshold, append-log service,
freshness quorum, authorized services and OS boundary, the contract
authenticates approvals, detects changed bound bytes, rejects views below
persisted state, requires a nonce-bound quorum attestation of the current head
at each named boundary, prevents scope/input substitution and makes a commitment
single-use. It does **not** provide continuous authorization between boundaries,
make evidence scientifically true, prevent colluding/mistaken approval, provide
confidentiality, or prevent denial of service.

Compromise is not automatic fail-closure. The per-principal boundary is:

| Compromised principal | What may pass before external detection | Detection and permitted response |
| --- | --- | --- |
| Offline root alone, recovery threshold/verifier/OS honest | Malicious trust manifests or transitions may authenticate | No automatic detection claim. After external detection, two-of-three `RecoveryTransition/v1` installs a new root, declares earliest invalid sequence and re-closes every affected scope |
| Two-of-three recovery threshold | Malicious recovery/root replacement may authenticate | No in-band detection, recovery or security guarantee; reviewed verifier/bootstrap replacement is required |
| Verifier or OS boundary | Arbitrary acceptance, key/byte substitution or false result | No in-band guarantee; rebuild on an independently reviewed trusted platform |
| Append-log service | A consistently suppressed current head or availability denial may be presented to otherwise honest witnesses | Suppression is not guaranteed detectable; inconsistent, unavailable or externally gossiped conflicting views fail closed. Restore a trusted log view and re-close affected scopes after external detection |
| Checkpoint signer alone | Cannot create an accepted head without an honest witness quorum, but can deny service | Honest quorum rejects a noncurrent/inconsistent head; retire the signer after detection |
| One freshness witness | Cannot form the two-of-three invalid quorum under an honest log and two honest witnesses | Other witnesses preserve the guarantee; retire the key after detection |
| Two freshness witnesses | Stale, suppressed or split latest-head leases may authenticate | No currentness/anti-equivocation guarantee until external detection; rotate witnesses, restore trusted log state and re-close affected scopes |
| Capability/run issuer | Malicious in-scope capabilities or commitments may authenticate | May remain undetected until audit; revoke/retire issuer, invalidate affected objects and re-close |
| Analysis-release signer | A malicious final report may be authentically released | May remain undetected until audit; revoke the release record/key, preserve raw bytes and issue a newly reviewed report/release |
| Revocation signer | Malicious revocations may authenticate and cause denial/withdrawal | Audit/log monitoring may detect but is not guaranteed; root/recovery retires signer and applies the exact repair rules where justified |
| Claim service | Duplicate or false claim receipts may authenticate | One-use guarantee is lost until external detection; retire service and invalidate affected claims/runs |
| Scientific owner or reviewer; both colluding | False evidence or conclusions may receive authentic approval | Cryptography proves provenance only. Independent scientific audit may detect; revoke affected authority records and re-close |

Availability loss, an observed inconsistency or an invalid signature fails
closed. Undetected malicious acts by an authorized compromised principal may
pass; recovery is an explicit action after detection, not an automatic property
of compromise.

Required attacks include algorithm/encoding downgrade; unauthorized owner,
reviewer, issuer, checkpoint, witness, revocation or claim key; omitted/swapped
conformance or gate records; old-but-valid checkpoints after a newer one;
within-age ancestor replay after an unseen transition/revocation; wrong nonce,
boundary, requester, active manifest or revocation-set digest; replayed/expired/
already-used leases; same-size split views; broken consistency proofs;
unavailable witness quorum or revocation state; every boundary crash window and
retry transition; missing/wrong lease-use receipt; cross-process/cross-subject
replay; any head append or authority-digest change between lease inclusion and
receipt consumption at each of the five boundaries; wrong planned receipt
sequence; orphaned result template after failed CAS; two distinct
`raw_start` subjects racing one commitment, late losing receipt append, and
crash after atomic claim/receipt consumption but before signed-result append;
release-key transition before lease, between lease inclusion and consumption,
and after receipt; release-key/signature substitution, wrong logical issuance
sequence and any completion keyed by a report rather than its release;
descriptor/path swaps; changed wavelength, geometry, polarization, waveform,
coherence, exposure/control/process or calibration; out-of-domain values; two
concurrent claims; crash during durable claim; each retirement/revocation timing
row; every registry schema, direct-revocation target and parent-invalidation
row; missing/incompatible post-close effect; exceptional repair precedence per
revoked digest, successive unrelated repairs, repeated same-target repairs,
self/circular targets and omitted re-closures;
each compromised-principal row; and exact status-precedence assertions.

# Gate H — quantitative decision rules

Every falsification test has a `DecisionRule` fixed before data with:

- estimand and unit;
- null/alternative and direction;
- sample size and minimum relevant effect;
- uncertainty interval and simultaneous coverage;
- family-wise multiplicity procedure;
- numerical tolerance/convergence order;
- missing/invalid-data rule;
- one machine-readable outcome and its owner.

Default statistical policy is two-sided family-wise `alpha = 0.01` using Holm
correction and power `>= 0.90` at the preregistered minimum effect. Numerical
refinement must demonstrate its declared order with a 99% confidence bound and
keep its total error below one quarter of the experimental acceptance half-width.

The former “zero-net cyclic forcing” control is replaced by two distinct tests:

- zero **field work** over the complete closed ledger may not create a persistent
chemical state unless a named bath/chemical reservoir supplied the energy;
- zero-mean AC forcing may dissipate positive energy and is compared with the
analytically derived passive-work prediction, not expected to give zero.

# Authority-packet closure

Closure is scope-specific. The closure process mints no capability until every
gate in the requested profile is individually `closed`, its source/data/review
hashes are frozen, no conclusion-bearing field is an assumption/proxy, and an
independent reviewer finds no route from comparator or desired response back
into raw authority. Until then, that scope's physical conclusions remain fail-
closed. F2 may be open for a latent-cluster capability; F1 may never be open for
one.
