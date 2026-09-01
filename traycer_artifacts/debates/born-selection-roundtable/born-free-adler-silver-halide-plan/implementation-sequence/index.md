---
title: "Passive-model implementation and verification sequence"
kind: spec
---

# Package shape

Create a standalone **feasibility** package with one-way data flow. Physical raw
and verdict modules remain disabled until a scope-specific closure capability
validates:

```text
passive_silver_halide/
  manifests.py          strict schemas, evidence classes and digests
  authority.py          read-only trust/store, scope-capability and run-commitment validation
  fields.py             real carrier-resolved component waveforms
  keys.py               solver-independent disorder and bath identities
  polarization.py       passive dye/exciton coordinate network
  reaction.py           donor/acceptor charge-transfer coordinates
  carriers.py           electron/hole transport, traps and recombination
  clusters.py           Ag-ion transport, neutralization and Ag_n clusters
  development.py        dark survival and independently calibrated readout
  direct_solver.py      optical-cycle multirate reference
  multiscale.py         frozen derived approximation, initially diagnostic
  equivalence.py        trajectory/energy/event/error-certificate gates
  calibration.py        evidence and identifiability authority
  raw_runner.py          streaming raw generation and closed ledgers
  compare.py             post-close classical comparator
  analysis.py            final statistics and falsification
  verify.py              mutation, isolation and numerical checks

adler_counterfactual/
  model.py               explicitly pumped active oscillator
  analysis.py            diagnostic comparison only

authority_issuer/        separate isolated executable; never imported by raw/analysis
  bootstrap.py           fixed v1 encoding/algorithm/root/recovery/log genesis
  trust.py               owner/reviewer/issuer/checkpoint/witness/claim roles
  store.py               witnessed append-only objects/log/consistency proofs
  freshness.py           nonce-bound two-of-three latest-head lease service
  boundary.py            canonical subjects, lease-use receipts and crash recovery
  registry.py            compiled exhaustive schema/revocation/parent map
  recover.py             root transition, retirement and cumulative per-revocation repair
  issue.py               signed scope capability and exact run commitment
  claim.py               atomic commitment CAS, receipt-log append and one-use claim
  revoke.py              signed key/object revocation and precedence records
  release.py             release signer participating inside final-analysis completion
```

The counterfactual package may read frozen field fixtures but cannot import the
passive raw runner, construct grain ledgers or emit physical outcomes. The
existing `hologram_phase_test` remains a classical consistency control and is
not converted into microscopic authority.

Exploratory/conformance types live below `authority.py` and cannot import
physical raw, capability or verdict types. Stages 1–10 use those types only.

# Phase boundaries

| Phase | Work allowed | Physical output allowed? |
| --- | --- | --- |
| I. Authority specification | Evidence inventory, exact equations, observation operators, decision rules and missing-authority records | No |
| II. Nonphysical conformance verification | Stages 1–10: analytic, numerical, recovery and mechanism fixtures typed diagnostic/exploratory | No |
| III. Scope and run authorization | Independent review, trusted signed scope capability, then signed single-use exact-run commitment | Authorization objects only |
| IV. Frozen physical run | Stage 11 onward, using the exact validated capability plus an unused signed run commitment | Only within capability scope and committed inputs |

# Ordered implementation stages

## 0. Specify or fail the preimplementation authority records

- Freeze the exact linear material functional and map every coefficient or
identified composite to an independent observable.
- Select either an explicitly exploratory kinetic surrogate or a specialist-
reviewed electronic-transfer formalism with reverse dynamics, detailed
balance, and exact charge/energy handoff.
- Inventory actual retained-batch datasets, access, samples and uncertainty.
- Write forward observation operators and freeze the structural/practical
identifiability and synthetic-recovery protocols.
- Specify the direct/certified-horizon and resource/rare-event feasibility
protocol.
- Specify thermodynamic/noise, separate F1/F2, capability and quantitative
decision-rule contracts.

**Exit:** every candidate record is either `specified_for_verification` or has
its exact missing-authority/no-result status. Stages 1–10 may run only as
nonphysical conformance fixtures. No physical record or verdict constructor is
reachable yet.

## 1. Freeze feasibility schemas and semantic firewall

- Define versioned field, material, solver, calibration, event, cluster, grain
and run records.
- Encode the four evidence classes and fail-closed physical status.
- Freeze permitted outcomes and forbid target/intensity/event-rate inputs at all
raw public boundaries.
- Establish raw-module import allowlists and a semantic data-dependency audit.
- Add deliberate mutants: renamed intensity input, `K**2`, clipped work,
Poisson photon arrivals, negative damping and comparator-fed exposure.

**Exit:** no feasibility run can receive or derive a target response, and every
mutant is caught for its data dependency rather than spelling alone.

## 2. Real fields and physical identity

- Implement object/reference beams as real carrier-resolved electric fields.
- Freeze dark, single-beam, coherent-phase and phase-scrambled identities.
- Implement static grain/site disorder drawn once per physical master identity.
- Define potential site/carrier/ion identities and absolute fine-time bath keys;
do not instantiate bath increments until Gate E supplies each subsystem's
spectral density, invariant measure and stochastic convention.
- Verify subdivision, streaming, ordering and parallel invariance.

**Exit:** paired counterfactuals share the same disorder/noise realization, and
invalid inputs consume no keys or write no records.

## 3. Passive polarization feasibility reference

- Implement only the frozen linear `H_pol` feasibility fixture.
- Require positive `M`, positive `K`, field-independent `d`, and the sole optical
coupling `-E d^T q`.
- Derive its exact causal susceptibility/Green function.
- Integrate the real optical carrier and record stored energy, signed field work,
bath work, heat, channel energy and residual.
- Test the zero-damping Hamiltonian limit, analytic susceptibility, sign/phase/
waveform/frequency controls, timestep convergence and long-time passivity.
- Add a bath only after its optical-frequency authority closes; otherwise run
deterministic fixtures.
- Mutation-test negative damping, hidden amplitude restoration and per-cycle
work clipping.

**Exit:** the analytic/direct subsystem has a closed energy ledger, cannot
oscillate indefinitely without field/bath energy, and detects an energy-envelope
surrogate. This does not authorize PFG-01 transfer or grain predictions.

## 4. Electronic-transfer authority

- Do not implement a physical carrier from a generic basin crossing.
- A kinetic surrogate uses measured forward/back rates under an
`exploratory_only` type that cannot construct a physical verdict.
- A microscopic candidate implements only the reviewed donor/acceptor
electronic-state formalism, electronic/nuclear coupling, reverse transfer,
committor/reactive-flux rule, local detailed balance and exact charge/energy map.
- Test forward/reverse flux, recrossing, dark equilibrium, sub-barrier and
transfer-disabled controls, and charge/energy conservation.

**Exit:** Gate-B conformance is independently verified and becomes eligible for
the later scope-closure step, or status is `transfer_authority_missing`. A
kinetic surrogate remains exploratory regardless of numerical success.

## 5. Carrier, trap and recombination dynamics

- Implement electron/hole transport in a declared grain energy landscape.
- Implement the full Itô mobility/noise-induced-drift and electrochemical
potential contract from Gate E.
- Verify invariant distribution, detailed balance, temperature scaling and
physical-time keys across divergent event graphs.
- Implement capture-basin trapping, thermal escape and encounter-based
recombination.
- Replay exact boundary cases under timestep refinement and shared noise.
- Keep all injected/mobile/trapped/recombined states in the ledger.

**Exit:** charge fate is traceable from the transfer event and no Bernoulli
timestep decision is used.

## 6. Ag-ion motion and silver-cluster nucleation

- Implement coarse-grained Ag-ion/interstitial transport and charged-center
interactions.
- Implement forward/reverse ion capture/neutralization with chemical reservoirs,
charge/atom conservation and explicit `Ag_n` membership.
- Add independently parameterized binding, dissolution and dark-survival
dynamics.
- Test charge/atom conservation, reversible controls and temperature/dark-delay
dependence.

**Exit:** every latent cluster has a conserved carrier/ion history; cluster size
is not a proxy photon count.

## 7. Separate latent-cluster and development-readout verification

- Verify Gate F1 against a pre-development latent-cluster assay and its forward
operator.
- Verify Gate F2 separately against a conditional development-response dataset
and process-only controls.
- Freeze a low-dimensional readout and its uncertainty; show upstream cluster
predictions are invariant across every admissible readout.
- Keep development amplification/readout separate from latent-image formation.
- Test process-only fog, threshold boundaries and developer/time/temperature
holdouts.

**Exit:** F1 and F2 receive separate conformance records. Missing F1 yields
`latent_cluster_authority_missing`; missing F2 yields
`development_authority_missing`. During Phase II all outputs remain nonphysical
regardless of either result.

## 8. Formal multiscale derivation

- Measure a `FeasibilityEnvelope` first: approximately `4.7e14` carrier cycles/s
at 640 nm, direct/certified horizons, grains/sites/ions, rare-event targets,
replicates/effective sample size, operations, wall time, RSS and storage.
- Use exact linear Green-function elimination before proposing a numerical
carrier envelope.
- Write and freeze the multiple-scale derivation before implementing the fast
solver.
- State reconstructed coordinates, approximation order, discarded terms,
bilinear per-cycle field work and every averaged channel flux.
- Derive bath quadratures from the same fine noise leaves.
- Derive strong error for pathwise claims, weak/rare-event error for distribution
claims, and a full-exposure family-wise event/readout misclassification bound
`<= 0.01` with at least 99% confidence.
- Independently audit the derivation for a hidden norm, clipped power or
target-shaped transfer law.

**Exit:** Gate-D conformance becomes eligible for scope closure only if the
derivation review closes and the maximum certified horizon reaches the shortest
predeclared measurable exposure; otherwise result is `no_resolved_test`. Code
is not used to settle missing mathematics.

## 9. Accelerated solver and equivalence

- Implement only the frozen derivation.
- Compare direct and accelerated fast trajectories, signed work, channel flux,
admitted electronic states/transitions and slow event states.
- Test joint noise quadratures, fine/coarse conservation and pathwise paired
fixtures.
- Accumulate the strong/weak/rare-event certificate over the longest intended
exposure and enforce the preallocated global 1% event-error budget.
- Refuse cases whose intervals straddle any conclusion-bearing boundary.

**Exit:** the solver is `admitted_within_certified_domain` or structurally
unable to generate physical raw records. Final image agreement is not examined.

## 10. PFG-01 evidence and identifiability gate

- Build the evidence-availability manifest from data actually in hand or secured,
including access, sample consumption and raw digests.
- Define the forward observation operator and likelihood for every datum.
- Build the parameter-to-evidence manifest from batch-matched spectroscopy,
kinetics, transport, pre-development latent-image and conditional development
measurements.
- Store identified composites rather than arbitrary factor decompositions.
- Freeze training and holdout conditions.
- Prove structural identifiability, then apply the frozen whitened-Jacobian,
500-dataset synthetic-recovery, 99% holdout and prediction-invariance rules.
- Label proxy-material and assumed parameters exploratory.

**Exit:** Gate-C conformance becomes eligible for scope closure, or the system
emits `evidence_unavailable`/`insufficient_material_calibration` with exact
missing data or combinations.

## 10.5. Mint the requested scope capability

- Load only the compiled `GateGBootstrapProfile/v1` deterministic-CBOR/SHA-256/
Ed25519 profile, root fingerprint, two-of-three recovery fingerprints and
pinned authority-log ID/genesis;
reject algorithm/encoding/version negotiation.
- Load the compiled `AUTHORITY_OBJECT_REGISTRY/v1`; refuse any stored/signed
schema absent from it or any object whose direct tag/sole parent differs.
- Verify the root-signed trust manifest; owner/reviewer/issuer/checkpoint/
witness/revocation/claim roles; trust/recovery transitions and validity
sequences.
- Reopen every immutable authority and conformance record required by the
requested scope.
- Freeze `CapabilityPreimage/v1` and wrap it in `ScopeMintSubject/v1` before any
lease request. Generate a fresh 256-bit nonce and obtain a one-use `scope_mint`
latest-head lease with an identical payload signed by at least two of three
freshness witnesses. Require the exact requester/subject/boundary, a maximum
60-second expiry, the current checkpoint/head, a consistency proof from
persisted state, one active trust/recovery manifest and the complete effective
revocation-set digest.
- Refuse within-age ancestor replay, wrong nonce/requester/subject/boundary,
expired or reused leases, rollback, fork, witness disagreement, equivocation or
unavailable quorum; checkpoint age alone never proves currentness.
- Follow the shared expected-head progression. Append the lease and persist its
exact inclusion head; freeze the next-sequence receipt, capability-result
template payload ID, authorized issuer key and completion-grant template; then
atomically require that head and unchanged leased authority digests, verify the
templates/key, append the receipt envelope, derive its payload ID/object digest,
store the unique receipt-bound capability payload bytes/ID and derive the
payload-specific completion grant.
Any intervening append produces no receipt and requires a fresh lease for the
same subject. Only the grant fixed at the receipt sequence may later sign the
stored payload; append/complete only that signed envelope and record both its
payload ID and object digest.
- Implement the exhaustive subject state machine: `unleased -> leased(attempt) -> abandoned(attempt) -> leased(new attempt)` before consumption, and
`leased -> consumed -> completed | consumed_failed` afterward. Abandonment and
consumption CAS the same active attempt. Query and ambiguous-crash behavior must
return the durable state; no consumed state receives another lease.
- Recompute each complete `GateClosureRecord`: gate/scope/decision, source,
evidence, conformance, decision-rule, review, schema, trust epoch and validity
sequence.
- Require the separately authorized owner and distinct gate/scope reviewer to
have signed those exact bytes; require an exhaustive gate-to-record map and
descriptor-based same-byte store inclusion proofs.
- The fixed exact-type `AuthorityClosureCapability` may name only
`latent_cluster_physical` or `developed_film_physical` and binds the consumed
`scope_mint` subject, lease and append-logged lease-use receipt.
- Apply the closed revocation-target matrix to every authority object; reject an
unknown object class or implementation-defined inheritance rule.
- Compute exceptional repairs independently per exact retroactive-revocation
digest and subtract all valid repaired digests cumulatively. Refuse a later
unrelated repair that changes an earlier disposition, a nonretroactive/self/
circular target, a conflicting precedence tuple or an incomplete re-closure.
- Mutation-test forged, stale, replaced, subclassed, partial, mismatched and
wrong-scope packets, unauthorized/self-consistent gate records, wrong or revoked
owner/reviewer/issuer/checkpoint/witness keys, downgrade, rotation/recovery,
rollback/fork, within-age supersession, stale/tampered store, lease replay and
every direct/parent revocation row before the capability can exist.

**Exit:** one scope capability is minted, or its exact missing/no-result status
is final. There is no generic physical capability.

## 10.75. Commit the exact physical run

- Canonically freeze `FieldManifest/v1`: coordinate frame/units, positions,
propagation vectors/geometry, carrier frequency/wavelength, polarization,
real amplitudes, waveform/envelope/coherence, phases/timing, exposures,
temperatures, dark delays, controls and processing schedules.
- Bind source/executable, material, calibration, solver/certificate,
decision-rule, stochastic namespace, replicate and resource-limit digests.
- Produce a `DomainValidationRecord` binding verifier/version, every checked
bound and value, field-manifest digest and certified-domain digest.
- Freeze `RunCommitmentPreimage/v1` and `RunCommitSubject/v1` before requesting
the lease. Append the lease and persist its exact inclusion head; freeze the
next-sequence receipt, commitment-result template and authorized issuer key;
then in one expected-head transaction require the unchanged leased
head/manifest/revocation view, verify that result/grant templates and key,
append the receipt envelope, derive its payload ID/object digest, store the
unique receipt-bound commitment payload bytes/payload ID and derive its payload-
specific completion grant.
Any intervening append leaves no receipt or commitment and requires a fresh
lease. Only the fixed completion grant may later sign; append and complete only
that stored signed envelope, recording payload ID and object digest, binding the
capability, exact schedule and `run_commit` subject/lease/use-receipt chain.
- Mutation-test changed calibration, field/exposure/control/processing schedule,
carrier/wavelength, geometry, polarization, waveform/coherence, out-of-domain
well-formed values, wrong run/namespace/replicate identity, revoked issuer, stale
checkpoint and commitment replay.

**Exit:** one exact run commitment exists or status is
`run_commitment_invalid`. A capability alone cannot start Stage 11.

## 11. Frozen raw experiment

- Load the exact signed `FieldManifest/v1` and schedule bytes committed at Stage
10.75; Stage 11 cannot regenerate, edit or reselect them.
- Require and freshly revalidate the trust chain, exact scope capability and
exact run commitment. Freeze `RawStartPreimage/v1` over commitment/run/attempt
and wrap it in `RawStartSubject/v1`; then obtain/append its nonce-bound lease,
persist the exact inclusion head, and freeze the next-sequence receipt,
claim-result template payload ID, authorized claim-service key and completion-
grant template. The authorized claim service is the
`raw_start` boundary coordinator: in one commitment-keyed linearizable
compare-and-append it requires the exact lease-inclusion head and unchanged
leased authority digests, verifies the frozen result/grant templates and key,
assigns the unclaimed commitment to that exact subject, append-logs its
`LeaseUseReceipt/v1` envelope, derives its payload ID/object digest and stores
the unique receipt-bound `ClaimReceipt` payload bytes/payload ID and derives its
payload-specific completion grant. Only the
winning subject may append a receipt;
distinct-subject losers receive `claimed_by_other_subject` before any key or
directory is touched. After the atomic transition, recovery may complete only
the fixed grant's deterministic signature over the stored claim payload, while an ambiguous response is queried and treated as
consumed if the transaction may have committed.
- Stream field-to-cluster-to-grain records without opening a comparator.
- Do not create physical cluster records without F1 scope; do not create
`developable`/film records without F2 scope.
- Bind each accelerated block to its derivation/equivalence certificate.
- Hash source, manifests, calibration and every append-only table. Freeze one
canonical `RawManifest/v1` that lists every schema-tagged raw block exactly once
with row counts; no raw block exists outside it.
- Freeze `RawClosePreimage/v1` over capability, commitment, claim and raw-
manifest digests and wrap it in `RawCloseSubject/v1`. Immediately before
closure, append its lease, persist that inclusion head, freeze the receipt and
close-marker template, and consume them only through the expected-head
transaction. That transaction derives the receipt digest and stores the unique
receipt-bound close-marker payload bytes/payload ID plus its payload-specific
completion grant derived in that transaction. Completion appends only its signed envelope and records its object
digest. Any intervening append, transition or revocation
yields no receipt and requires a fresh lease; the stored raw bytes and immutable
subject remain unchanged.
- Write one `CloseMarker/v1` last, binding the raw manifest and both raw-start
and raw-close subject/lease/use-receipt chains.
- Close and validate the raw dataset before final analysis can open it.

A crash after the atomic claim transition consumes the commitment and leaves a
failed nonresumable attempt; a crash before it leaves no receipt and no claim.
The same winning subject may recover only its fixed receipt. No other subject
may take over, and a new attempt requires a newly signed commitment and run ID.
A crash after the raw-close use receipt may only deterministically finish the
same close marker; it may not close changed raw bytes or acquire another lease
for that subject.

**Exit:** byte-stable latent-image predictions exist and no classical intensity
array has been computed by the raw process.

## 12. Final analysis

- Freeze `FinalReportPreimage/v1` and `FinalAnalysisSubject/v1` before any lease
request. Generate a new nonce and obtain/append a one-use `final_analysis`
latest-head lease; require the unique active manifest, complete revocation set
and consistency from persisted state before opening a physical ledger, and
persist the lease's exact inclusion head. Freeze the next-sequence receipt,
exact `FinalReport/v1` payload bytes/ID, release-result template payload ID,
authorized release key, completion-grant template and logical issuance sequence.
Then atomically require the current head to equal
the lease-inclusion head and the manifest/epochs/effective-revocation digest to
remain identical; verify the template, key and grant; and in one authority-
store/WAL commit append the receipt envelope and store the coordinator consumed
row, receipt payload ID/object digest, **exact report bytes**, report payload ID,
release template, unique receipt-bound `AnalysisReleaseRecord/v1` payload
bytes/ID, payload-specific fixed-key grant derived from that ID, `H2` and every
recovery locator.
An intervening append yields no receipt or issuance and requires a fresh lease
and recomputed template. An uncommitted WAL makes none of the bundle
authoritative; a committed WAL is sufficient after process loss. Only the
fixed completion grant may later sign the exact stored release payload.
- Record `completed` only with the release payload ID and signed-envelope object
digest. Recovery after a
crash may have only the key fixed at the receipt sequence deterministically sign
and append the stored report-and-release pair; it cannot change the payload,
key or lease. If that fixed signer cannot complete, the boundary is terminal
`consumed_failed` and repeat queries return that terminal state; no substitute
key may sign. Normal retirement preserves only this payload-specific completion
grant. Retroactive invalidation reaching H2 disables it, while direct revocation
of the release payload ID also disables it; either transition atomically records
`consumed_failed` with the exact revocation reason. An orphaned report is
noncurrent and cannot be presented. A
correction requires a new subject/report/release and leaves raw bytes unchanged.
- Validate every schema ID against `AUTHORITY_OBJECT_REGISTRY/v1`, follow exactly
one immediate parent for every nonrevocable child, and apply signed
`post_close_effect`. Retroactive revocation always withholds; nonretroactive
post-close preservation requires `preserve_completed_run` explicitly.
- Apply exact precedence: authority/lease/gate/capability failures are
`authority_capability_invalid`; only after they pass can run/field/domain/claim/
close failures be `run_commitment_invalid`.
- Separately compute the classical field-intensity comparator.
- Join it to frozen cluster ledgers only with `latent_cluster_physical` scope;
join developed output only with `developed_film_physical` scope.
- Run the full falsification matrix and calibration-ensemble sensitivity.
- Reject conclusions that vary materially across admissible parameter sets.
- Report classical recording consistency separately from material calibration,
numerical status and any optional quantum interpretation.

**Exit:** only the permitted parent-plan vocabulary is used.

## 13. Adler counterfactual, if still useful

- Implement it only after the passive result is frozen.
- Name an explicit sustaining reservoir and close its energy ledger.
- Mark every output `adler_counterfactual_only`.
- Demonstrate that no import/API path can turn it into PFG-01 evidence.

**Exit:** it may illustrate a hypothetical active mechanism but cannot change a
passive physical verdict.

## 14. Independent review

Freeze hashes and ask a cold reviewer to trace the entire data-generating path.
The review must attack:

- intensity, envelope norm, `K**2` or photon flux entering raw generation;
- a quadratic law hidden in averaging rather than derived from bilinear work;
- negative damping, sustaining work or unledgered pump energy;
- clipping/rectification of signed work;
- intensity-, locked-fraction-, Poisson- or Bernoulli-based transfer events;
- solver/arm-dependent noise keys;
- reaction, trap or development boundaries without accumulated error bounds;
- unrestricted composite calibration or final-fringe fitting;
- exposure selection after comparator access;
- raw/final/counterfactual import and data leaks;
- physical outcomes emitted with exploratory evidence.
- unauthorized/self-consistent authority records or wrong reviewer/issuer keys;
- bootstrap downgrade; wrong owner/checkpoint/witness/claim keys; rotation or
recovery errors; rollback, split views and unavailable checkpoints;
- within-age ancestor replay after an unseen transition/revocation; wrong nonce,
requester, boundary, active manifest or revocation-set digest; expired/replayed/
already-used latest-head leases; unavailable or disagreeing witness quorum;
- at each of the five boundaries, any append between lease inclusion and
receipt consumption; changed head with unchanged authority digests; changed
manifest/revocation digests; wrong planned `H2`; and reuse of a result template
whose expected-head CAS failed;
- revoked/stale trust roots, store objects, capabilities or run commitments;
- every direct revocation target and every parent-invalidation row, including
field/domain/raw children that cannot be independently revoked;
- every canonical schema registry row and unknown/alias schema refusal;
- missing/wrong boundary subjects or use receipts; crash before receipt, after
receipt/before result and after result/before caller response at all five
boundaries; expiry racing abandonment and consumption; late abandoned-attempt
receipt; ambiguous consume queries; repeated `consumed_failed` queries;
forbidden fresh-lease retry after receipt; two different
`raw_start` subjects racing one commitment, a late losing receipt, and a crash
between atomic claim/receipt consumption and deterministic signing/append of
the stored claim result;
- a raw block omitted, duplicated, added outside or mismatched with
`RawManifest/v1`, and a close marker bound to any other manifest;
- missing/incompatible `post_close_effect`; preserve/withhold timing;
exceptional recovery repair with wrong target, epoch, activation/log sequence,
affected scopes or re-closure set; two unrelated repairs in successive epochs,
multiple repairs of one digest, circular/self targets and implicit global-set
replacement;
- release-signer failure after consumption; release-key transition before
lease, between lease inclusion and consumption, and after receipt; wrong
logical issuance sequence; changed release on recovery; orphaned pre-CAS result
template; substitute-key signing after receipt; and any report exposed without
the boundary's completed release payload ID/signed-envelope object digest;
- payload bytes containing a self ID; payload-ID/envelope-digest substitution;
signature or object digest fed back into its own payload; direct revocation of a
payload between H2 and signing; an envelope whose payload ID does not recompute;
and descendants binding only one of a signed parent's two identifiers;
- final-analysis crash after H2 with the originating process and its memory
destroyed; incomplete WAL bundle; report bytes differing from the stored report
payload ID; missing recovery locator; and any uncommitted WAL fragment treated
as authoritative;
- each per-principal compromise case, asserting guarantee loss rather than
automatic detection where the contract makes no such promise;
- changed/out-of-domain schedules and replayed/partially consumed commitments;
- omitted/swapped conformance records; changed wavelength, geometry,
polarization, waveform or coherence; concurrent/durability claim faults;
- a generic classical crossing presented as electronic injection;
- missing forward/reverse or thermodynamic contracts;
- a certified horizon shorter than the experimental exposure;
- latent-cluster formation and development readout fitted from the same
undifferentiated data;
- qualitative acceptance language with no machine-readable decision rule.

**Exit:** strict review closes every authority-path attack. Green numerical tests
alone are insufficient.

# Numerical and scientific stop rules

Stop rather than interpret in this precedence order:

- any gate required by the requested scope is not closed;
- its trust chain, authority store, latest-head lease, capability or revocation
state fails
(`authority_capability_invalid`);
- any stored schema is absent from `AUTHORITY_OBJECT_REGISTRY/v1`, has an alias,
or lacks its exact direct tag/sole parent route (`authority_capability_invalid`);
- a physical boundary lacks an exact, freshly revalidated scope capability
(`authority_capability_invalid`);
- only after authority passes, a physical run lacks a valid unused exact signed
commitment or claim receipt (`run_commitment_invalid`);
- a passive subsystem gains energy without field/bath provenance;
- energy residuals fail refinement;
- a material term lacks an exact evidence map or hidden-square-law controls;
- electronic transfer is only a kinetic surrogate or lacks reverse/charge/energy
authority;
- direct/accelerated trajectory, energy or event equivalence fails;
- full-exposure error intervals straddle an event/development boundary;
- the intended exposure is outside the certified numerical domain;
- the global event/readout error budget exceeds 1% or lacks 99% confidence;
- PFG-01 conclusion-bearing parameters or composites are not identifiable;
- uniform holdouts fail without a frozen explanatory rule;
- developed fraction is indistinguishable from fog or saturated;
- F1 pre-development cluster evidence is missing for a cluster claim;
- F2 conditional readout evidence is missing for a developed-film claim;
- any thermodynamic/noise contract is missing (`thermodynamic_authority_missing`);
- exposure choice requires comparator agreement;
- admissible parameter sets imply incompatible fringe predictions;
- any result depends on the Adler counterfactual.

# Cost strategy

The first cost decision precedes physical implementation: freeze the maximum
certified horizon and resource envelope. If it cannot reach a measurable
exposure, do not proceed to grains or a plate patch.

Build and benchmark in ascending expense. Items 1–6 are nonphysical Phase-II
conformance fixtures; they cannot serialize a physical ledger or verdict:

1. one passive polarization coordinate in the analytic linear limit;
2. the retained-batch evidence inventory and candidate transfer-formalism audit;
3. an exploratory transfer surrogate or reviewed microscopic fixture;
4. one grain with Ag-ion capture and cluster growth;
5. direct versus multiscale short-horizon fixtures;
6. a calibrated one-grain exposure/dark/development sequence;
7. only after capability minting, a one-dimensional physical strip across
several fringes and exposure durations;
8. only then, within the same scope, a two-dimensional plate patch.

No full hologram or production exposure is budgeted until the complete
field-to-development chain and numerical certificate exist.
