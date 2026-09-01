---
title: "Passive microscopic architecture and equations"
kind: spec
---

# 1. Real field input

Raw generation receives measured real-valued beam parameters: carrier
frequency, propagation vector, polarization, real amplitude/envelope and phase.
It constructs and adds the physical fields without first creating a complex
intensity:

```text
E_object(x,t)    = e_object A_object(x,t) cos(k_object.x - omega t + phi_object)
E_reference(x,t) = e_reference A_reference(x,t) cos(k_reference.x - omega t + phi_reference)
E_total(x,t)     = E_object(x,t) + E_reference(x,t)
```

Converting an independently measured irradiance into each beam's real field
amplitude is legitimate instrument calibration. Its provenance is frozen before
any material outcome exists. Raw field APIs refuse a precomputed intensity,
complex norm, photon flux, target exposure response or comparator array.

Controls preserve the same individual beam amplitudes:

- object only;
- reference only;
- both beams with predeclared relative phases;
- phase-scrambled/incoherent control;
- dark field.

# 2. Passive sensitizer and exciton network

Each grain carries a frozen set of sensitizer coordinates `q_a`, with conjugate
momenta `p_a`. The only currently admitted analytic feasibility model is

```text
H_pol(q,p;E) = 1/2 p^T M^-1 p + 1/2 q^T K q - E_total(t) d^T q
```

where:

- `M` is positive definite;
- `K` is positive definite;
- `M`, `K` and `d` are field-independent identified composites;
- `-E_total d^T q` is the only first-stage optical coupling.

This model is a passivity and hidden-square-law fixture, not yet a microscopic
PFG-01 authority. Its causal susceptibility/Green function is derived
analytically and compared with direct real-carrier integration. Any excitonic,
anharmonic or reaction-coordinate extension first freezes its complete
Hamiltonian/free-energy, units, symmetries, boundedness proof and coefficient-to-
observable map in the authority packet. Generic `V(q,z,r)` is no longer an
implementation placeholder.

The raw implementation may not add negative damping, a van-der-Pol term,
amplitude restoration, hidden pump, phenomenological `locked` switch, or
higher-order field coupling. A field-independent nonlinear term is allowed only
after independent evidence and phase/sign/waveform/frequency controls distinguish
it from an energy-envelope surrogate.

No classical white-bath law is assumed at optical frequency. The bath spectral
density, stochastic convention and validity of any classical or quantum/colored
approximation must close the thermodynamic gate in the
[authority packet](../preimplementation-authority-gates) before physical use.

# 3. Explicit energy and channel ledger

The material Hamiltonian excludes the external field coupling. Its change must
close against the field and bath ledgers:

```text
dW_field = sum_a Q_a E_total(x_a,t) qdot_a dt
dH_material = dW_field + dW_bath - dQ_heat
```

Every coupling between polarization, exciton and reaction coordinates records
equal-and-opposite channel energy. The ledger contains:

- polarization/exciton stored energy;
- reaction-coordinate stored energy;
- signed field work;
- signed bath work;
- dissipated heat;
- inter-coordinate transfer work;
- numerical balance residual.

There is no `max(0, work)`, reflected reservoir, light-minus-dark optical-work
correction, or excess-dissipation proxy. Dark optical work is exactly zero; the
dark run measures thermal activation, fog and model error rather than being
subtracted to create positive chemical energy.

A positive cycle-averaged absorption proportional to field amplitude squared is
not forbidden. In a passive linear oscillator it can legitimately follow from
the bilinear work `E*qdot`. The requirement is that it be derived from the real
trajectory and closed ledger, not inserted as an event-rate law.

# 4. Charge-transfer reaction coordinates

No conclusion-bearing transfer equation is presently selected. A classical
coordinate crossing plus a fitted dwell/hysteresis rule is specifically
insufficient to create an electron/hole state.

Two products are distinguished:

- `kinetic_surrogate`: independently measured forward/back transfer and
recombination kinetics. It may test engineering consistency but cannot claim
a microscopic Born-free derivation.
- `microscopic_transfer_candidate`: a frozen donor/acceptor electronic-state
formalism with electronic coupling, nuclear/reorganization coordinates,
forward/back transfer, recrossing, local detailed balance or named
nonequilibrium reservoirs, and exact charge/energy mapping into the carrier
subsystem.

If the microscopic candidate uses a reaction coordinate, commitment requires an
independently validated committor/reactive-flux or transmission-coefficient rule,
not an adjustable dwell interval. The event record includes electronic/charge
state, complete material energy, bath/chemical work, forward or reverse event,
and conserved charge/atom identities before and after the transition.

The transfer module cannot construct physical carriers until a specialist
review closes Gate B. The current terminal status is
`transfer_authority_missing`.

# 5. Carrier transport, trapping and recombination

After injection, electron and hole coordinates evolve in a frozen grain energy
landscape. A minimal overdamped form is

```text
dr = [-Mu(r) grad U(r) + k_B T div Mu(r)] dt
     + sqrt(2 k_B T Mu(r)) dW            [Ito]
```

with mechanical mobility `Mu`, explicitly converted from any electrical-mobility
measurement. Position-dependent mobility includes the Itô noise-induced drift.
The invariant measure, electrochemical potential, boundaries and bath convention
are part of the authority record.

- An electron is trapped only through an admitted forward/reverse transition
whose rate ratio or reactive flux satisfies local detailed balance.
- A hole is trapped or removed by its separately calibrated pathway.
- Recombination occurs through an admitted reversible encounter/transition
contract; it is not an arbitrary Bernoulli draw per timestep.
- Thermal de-trapping is a trajectory escape from the same energy landscape.
- Static disorder is drawn once from a frozen batch distribution and reused in
all counterfactual arms.

Potential carrier identities are frozen before their creation event so paired
counterfactual paths address the same physical-time noise leaves after their
event graphs diverge. The model reports injected, mobile, trapped, detrapped and
recombined carriers even when no latent image survives.

# 6. Silver-ion motion and latent-image nucleation

Mobile/interstitial `Ag+` ions follow their own passive, temperature-dependent
transport in the grain lattice under the same position-dependent-mobility
contract. A trapped electron can attract and neutralize an ion only through a
forward/reverse reaction with a named free-energy or chemical reservoir:

```text
Ag+ + e_trapped -> Ag0
```

Repeated neutralization grows a surface or sensitivity-center cluster
`Ag_n`. Cluster binding/free energies determine whether an atom remains,
migrates or dissolves during the dark interval. The authoritative state is the
explicit cluster membership and charge ledger, not an accumulated photon count.

Every neutralization, binding and dissolution step conserves charge and atoms,
records heat/chemical work and satisfies local detailed balance unless a named
nonequilibrium reservoir is present. Developer chemistry is a later external
reservoir and cannot supply energy during latent-image formation.

Only after Gates B, C and E close may the plan begin with a coarse-grained
lattice/capture-basin model rather than atomistic electronic structure. Every
effective barrier or binding energy must be tied to PFG-01-class evidence or
the entire subsystem remains exploratory.

# 7. Latent-cluster and development authorities

Physical cluster output requires Gate F1: a pre-development assay of cluster
size/state, morphology, assay detection limits and dark survival, with an
explicit forward operator from the modeled state to that assay. If F1 is open,
cluster simulation is diagnostic-only, reports
`latent_cluster_authority_missing`, and cannot emit
`latent_image_prediction_frozen`.

After F1 closes, Gate F2 separately requires development response conditional
on independently known cluster state, morphology, developer, time and
temperature, plus process-only controls. Only then may a frozen low-dimensional
readout derive `developable` with an uncertainty interval. All admissible
readouts must preserve the upstream latent-cluster prediction. Optical density
and diffraction efficiency remain later plate-level observables.

Uniform developed-density curves alone cannot identify cluster production,
accessibility and development threshold separately. With F1 closed and F2 open,
the model may emit a physical `latent_image_prediction_frozen` result together
with `development_authority_missing`, but cannot emit developability or film
visibility. There is no Poisson photon counter or Bernoulli development draw.

# 8. Direct and accelerated numerical solvers

## Direct optical-cycle multirate reference

The reference resolves the real carrier for the fast polarization coordinates
over a measured short horizon. It does **not** yet integrate an authoritative
electronic transition or second-scale grain history. It is authoritative only
for:

- real-field trajectories and signed work;
- inter-coordinate channel energy;
- timestep and energy-balance convergence.

At 640 nm the optical period is approximately 2.1 fs (`~4.7e14` cycles/s).
Before any slow material process is implemented, the direct solver records its
measured maximum horizon, work, memory and storage in a `FeasibilityEnvelope`.
It is never described as a full-exposure fallback unless that exposure was
costed and completed.

## Exact linear elimination before a generic envelope

For the admitted linear passive network, the causal susceptibility/Green
function is the preferred acceleration. It is derived exactly from `M`, `K`,
the admitted damping/bath contract and `-E d^T q`, and verified against direct
real-carrier fixtures. It may compute a quadratic cycle-averaged work term only
as the algebraic reduction of the bilinear real-field ledger.

## Nonlinear/multiscale candidate

The accelerated solver may use real quadratures or internal complex coordinates
only after a frozen multiple-scale derivation specifies:

1. reconstructed `q` and `qdot`;
2. every retained and discarded term with approximation order;
3. the bilinear expression for per-cycle field work;
4. every averaged channel-energy flux;
5. how bath quadratures are projected from the exact same fine noise leaves;
6. how local weak/strong errors and rare-event bias accumulate through the
admitted transfer, trapping and cluster model over the complete exposure.

An internal `|A|^2` can appear algebraically if derived from the bilinear real
work. It may not be treated as an independent microscopic rate or substituted
before the derivation. Source scanning alone is not an admission proof.

## Admission gate

The direct and candidate solvers must agree within frozen bounds for:

| Quantity | Required comparison |
| --- | --- |
| Fast trajectory | `q`, `qdot`, amplitude and phase at carrier-resolved/stroboscopic times |
| Energy | Signed per-cycle field work, channel fluxes, stored energy, heat and balance residual |
| Transfer | Admitted electronic state/population, forward/back event, recrossing/commitment and exact charge/energy handoff |
| Slow state | Carrier positions/basins, trap and recombination events, cluster membership |
| Shared noise | Fine/coarse conservation and joint quadrature covariance from identical physical leaves |
| Full exposure | Strong error where pathwise claims are made, weak distributional/rare-event error elsewhere, and family-wise event/readout misclassification probability `<= 0.01` with at least 99% confidence |

If the certified interval straddles a transfer, trap, cluster or development
boundary, the case is `numerically_unresolved`. It may use the direct solver only
when that fallback has been explicitly costed and completed. Final fringe or
grain-density agreement is forbidden as solver-admission evidence.

The `FeasibilityEnvelope` freezes the intended exposure, grains/sites/ions,
replicate count, rare-event estimator, effective sample size, wall time, peak
RSS and storage. If its maximum certified horizon is shorter than the shortest
measurable exposure, the result is `no_resolved_test` and production solver work
stops.

# 9. Adler counterfactual quarantine

Any self-sustained Adler model lives outside the passive raw package. It must:

- name and ledger an explicit pump reservoir;
- carry `counterfactual_only` in every record;
- be unable to construct `developable` PFG-01 ledgers or a physical verdict;
- import frozen field fixtures only after passive-run closure;
- expose locking/tongue behavior solely to show how an unsupported active model
differs from the passive material prediction.

No passive-model acceptance criterion depends on this branch.

# 10. Raw records and isolation

Raw output is append-only and manifest-bound:

| Record | Required contents |
| --- | --- |
| Authority object identity | Canonical unsigned `payload_bytes`; stable `payload_id` excluding identifiers/signatures; `SignedEnvelope/v1` containing exact payload, key and signature; `object_digest` over envelope bytes excluding itself. Revocation targets payload ID; completion/Merkle inclusion store both IDs |
| Bootstrap/trust | Compiled v1 encoding/hash/signature/domain separators; pinned root/recovery fingerprints and authority-log ID/genesis; root-signed role/epoch/service manifest; signed transitions |
| Store checkpoint | Log ID, size/root, previous checkpoint, trust/recovery epoch, active-manifest and complete-revocation-set digests, time/sequence, checkpoint signature, two-of-three witness signatures and consistency proof |
| Schema/revocation registry | Compiled exhaustive schema IDs; each maps to one direct revocation tag, one sole immediate parent, trust/recovery lifecycle or immutable correction path; unknown schemas refuse |
| Boundary subject/lease/use receipt | Versioned immutable preimage for one of five boundaries; exact requester/subject/run, fresh 256-bit nonce, witnessed authority head `H0`, exact lease-inclusion head `H1`, unique active manifest/epochs, complete effective revocation set, issue/expiry, one-use attempt ID, two-of-three witness signatures, frozen result-template payload ID/signer key/completion-grant template and an expected-head CAS that appends the receipt envelope and derives the payload-specific grant at `H2` only if nothing intervened |
| Gate closure | Complete gate/scope/decision, source, evidence, conformance, decision-rule, review, schema/epoch/validity payload with distinct owner/reviewer signatures |
| Closure capability | Issuer signature; exact scope/profile; exhaustive signed gate-record map; source/executable, schema, material, calibration, solver, decision-rule, checkpoint and consumed `scope_mint` subject/lease/use-receipt digests |
| Field manifest | Versioned coordinate/units, positions, propagation vectors, carrier/wavelength, polarization, real waveform/envelope/coherence, amplitudes, phases/timing, exposure/control/process schedule and schema digest |
| Domain validation | Verifier/version, every checked value/bound, field-manifest digest and certified-domain digest |
| Run commitment | Issuer signature; capability/field/domain and `run_commit` subject/lease/use-receipt digests; exact run/namespace/master identity; stochastic/replicate/resource identities |
| Claim receipt | Claim-service signature over commitment, run, attempt and the sole winning `raw_start` subject; one commitment-keyed transaction assigns that subject, consumes its lease, appends its use receipt and fixes the receipt result |
| Material manifest | Exact admitted functional/transfer formalism, grain landscape, thermodynamic contracts, traps, ions, clusters and evidence map |
| Solver manifest | Direct or admitted multiscale version, derivation/equivalence digest and certified domain |
| Trajectory blocks | Real field samples or reconstructible quadratures, coordinates, velocities and all energy terms |
| Transfer/carrier ledger | Electronic/charge states, forward/back transitions, carriers, traps, recombination and energy/charge provenance |
| Cluster ledger | Ag-ion capture, neutralization, cluster membership, stability and dark survival |
| Grain ledger | Physical latent-cluster state only with F1 scope authority; `developable` only with F2 scope authority; no comparator |
| Raw manifest | Exact capability/commitment/claim identities; material/solver manifests; ordered schema-tagged trajectory, transfer/carrier, cluster and grain block digests; row counts and no unlisted raw object |
| Close marker | Exact raw manifest plus capability, commitment, field/domain, claim, checkpoint and `raw_start`/`raw_close` subject/lease/use-receipt digests |
| Final report | Exact close marker, analysis executable/configuration, frozen comparator, result payload and consumed `final_analysis` subject/lease/use-receipt digests; immutable but noncurrent without its release parent |
| Analysis release | Sole completed result of the `final_analysis` boundary: stable release payload ID plus signed-envelope object digest over close marker, exact final report and final-analysis chain; payload ID is the direct revocation target and the envelope is the only current physical presentation authority |
| Revocation/repair | Exact target tag, effect sequence, retroactivity and signed post-close policy; recovery-only exceptional repair evaluated cumulatively and independently per retroactive revocation digest, with ordered epoch/sequence precedence and exhaustive re-closure bundle |

Every physical constructor and raw entry point reopens and validates the exact-
type `AuthorityClosureCapability` and `RunCommitment` before consuming keys or
creating a directory. Validation begins with the compiled bootstrap profile,
follows the pinned root/recovery chain through owner/reviewer/issuer/checkpoint/
witness/revocation/claim roles, requests a new nonce-bound latest-head lease for
the exact boundary, resolves one active manifest plus the complete effective
revocation set, and then recomputes every digest and domain check from
descriptor-pinned bytes.
Forged, self-consistent-but-unauthorized, stale, partial, replaced, subclassed,
wrong-scope, changed-schedule, out-of-domain, rolled-back, equivocated or
replayed records refuse.
Exploratory modules are in a lower dependency layer that cannot import physical
record, capability or verdict types.

Raw modules cannot import comparison, plotting, final statistics, exposure
selection or the Adler counterfactual. Raw generation and comparison run under
separate executable identities. Stage 11 consumes the exact committed field-
manifest bytes. At every boundary, the subject is frozen before lease request;
the lease is appended and its exact inclusion head persisted; the next receipt,
result template, authorized signer key and completion-grant template are frozen;
and one expected-head
transaction verifies the unchanged leased authority view before appending the
receipt envelope, deriving its payload ID/object digest and storing the unique
receipt-bound result payload bytes/payload ID plus a payload-specific completion
grant derived in that transaction. Any intervening append has zero effect and forces a fresh
lease for the same subject. For `raw_start`, the trusted claim service itself owns one
commitment-keyed atomic transition that assigns the sole winning subject,
consumes its lease, append-logs its use receipt and fixes the receipt-bound claim
preimage before any write; losing subjects cannot append receipts, and an
ambiguous crash is treated as consumed. The other boundaries use their
subject-keyed coordinator. Closure first freezes one
`RawManifest/v1` binding every raw block, then writes its marker last, binding
that manifest plus the `raw_start` and `raw_close` subject/lease/use-receipt
chains. The comparison process receives read-only descriptors,
obtains a new `final_analysis` lease, applies the exhaustive revocation-target
matrix and status precedence, and cannot invoke regeneration. Before consuming
that boundary's lease it fixes the report, release template and authorized key;
the expected-head authority-store/WAL transaction stores the **exact report**
**bytes**, receipt-bound release payload, stable payload ID, fixed key/grant and
all recovery locators at the receipt sequence. That grant's later deterministic
signature completes the issuance fixed at that sequence, and completion stores
the release payload ID and signed-envelope object digest. Correcting a report creates a
new subject/report/release without changing raw bytes. Exceptional repairs are
resolved per revoked digest, so a later unrelated repair cannot reactivate an
earlier one. Configuration,
cache, environment, filesystem and IPC leak probes are mandatory.

Each subject coordinator has durable `unleased`, `leased(attempt_id)`,
`abandoned(attempt_id)`, `consumed`, `completed` and terminal
`consumed_failed` states. Abandonment and consumption CAS the same active attempt
ID, so only one can win; an abandoned attempt can be followed by a fresh lease
for the same subject, while consumed states cannot. Constructors verify
completed ancestor receipts/envelopes and obtain a separate unconsumed lease
only for their own current boundary. Normal retirement preserves only H2-fixed,
payload-specific completion grants; retroactive invalidation reaching H2
disables them.

Public boundaries refuse `psi`, `Born`, target exponents, comparator arrays and
assumed photon-event rates. A semantic verifier additionally traces data
dependencies so renamed intensity or event-rate insertions do not evade a token
scan.
