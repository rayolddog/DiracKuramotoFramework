---
title: "Independent Gate G latest-head closure review"
kind: review
---

# Strict verdict

| Question | Verdict |
| --- | --- |
| Gate G plan-contract closure | **PARTIALLY CLOSED** — witnessed-head currentness is now closed under the stated honest append-log/witness boundary, but the boundary-object receipt chain, the supposedly exhaustive revocation contract, and the compromise/recovery claims still require exact rules. |
| Diagnostic Phases I–II | **YES** — Stages 0–10 and cost items 1–6 may proceed only as diagnostic/exploratory/conformance work whose types cannot serialize a physical ledger, capability or verdict. |
| Stage 10.5 scope closure now | **NO** — the plan contract is not strictly closed, and the corpus supplies no actual closed gate records, keys, services, log state, lease quorum or capability. |
| Stage 11+ conclusion-bearing work now | **NO** — no valid scope capability, exact run commitment, durable claim service or physical authority evidence exists; Stage 10.5/10.75/11/12 remain fail-closed. |

This is a plan-contract critique, not a code review and not a claim that any
scientific evidence, keys, service, capability or commitment exists. The
currentness repair is real: the previous valid-but-unseen `C101` replay route no
longer exists when the configured append-log service and an honest witness
quorum satisfy the written contract. The remaining blockers are different and
should not be conflated with that repaired route.

# Prior six findings re-adjudicated

| Prior finding | Disposition | Basis / exact remaining change |
| --- | --- | --- |
| 1. Bootstrap, roles, lifecycle and root recovery | **CLOSED** | G0 fixes the bootstrap algorithms, pins log ID/genesis and root/recovery keys, authorizes every named role, defines monotonic trust/recovery transitions and distinguishes in-band recovery from verifier replacement. No bootstrap-selected-by-unverified-manifest route remains. |
| 2. Latest trusted checkpoint/currentness | **CLOSED, within the stated honest-service boundary** | A checkpoint age is expressly nonauthoritative. Every boundary requires a nonce-bound quorum lease; each witness queries the configured append-log after receiving the nonce, signs only an identical current head, persists its highest signed size and refuses lower/inconsistent/ambiguous views. The exact threat-boundary qualification below must remain explicit. |
| 3. Complete signed gate/capability coverage | **CLOSED** | One canonical owner/reviewer-signed gate record covers the complete closure payload, and the capability binds an exhaustive gate map and all load-bearing domain digests. The scientific-truth nonclaim is preserved. |
| 4. Exact run and durable claim | **PARTIALLY CLOSED** | The field/domain/run bytes and one-winner durable claim are closed. However, `RunCommitment` binds only the `run_commit` lease, not its use receipt; the close marker binds the `raw_close` lease, not its use receipt; and no canonical boundary-subject rule avoids circular or cross-object binding. Add one boundary-state table defining subject preimages, ordering, receipt binding and crash/retry behavior for all five boundaries. Also make the close marker bind the exact run/raw-manifest digest containing every raw block. |
| 5. Revocation effect and precedence | **PARTIALLY CLOSED** | Direct authority/run targets and status precedence are substantially repaired, but the closed enum is not demonstrably exhaustive across all named schemas, nonrevocable raw children do not have one exact immediate parent route, post-close nonretroactive `preserve/withhold` has no field in `RevocationRecord/v1`, and the exceptional retroactive-repair transition is not defined by either transition schema. Add the exact object-type registry and transition semantics described below. |
| 6. Threat-model accuracy | **PARTIALLY CLOSED** | Authenticated approval versus scientific truth, tamper detection versus DoS, and continuous versus boundary authorization are correctly distinguished. The statement that every listed compromise “causes fail-closed re-closure under G0” is too strong: a compromised append log can consistently suppress a newer head, compromised authorized signers may act undetected, and root compromise is specifically recoverable only while the recovery threshold remains honest. State loss of guarantee, detection assumptions and recovery separately for each principal. |

# Concrete flow adjudication

## 1. Witnessed C100, unseen C101, fresh nonce

Assume `C100` is valid and previously witnessed, then `C101` is appended with a
revocation or transition. The attacker presents `C100` with a fresh nonce.

- With an honest configured append-log service, each honest witness must query
the service *after* receiving that nonce. Its current head is `C101`; it may
not sign `C100`. An honest two-of-three quorum therefore cannot produce the
identical stale lease required by the verifier. The boundary fails
`authority_capability_invalid`.
- A witness that has already signed `C101` also durably remembers the higher size
and independently refuses `C100`.
- A partial quorum, disagreement, inconsistent proof, retired witness key or
unavailable log cannot satisfy the identical two-of-three payload rule and
fails closed.
- If the append-log service consistently suppresses `C101` to the witnesses, or
a witness quorum is compromised, `C100` can be signed. That is not an
honest-service execution; it is explicitly outside the present guarantee.
The plan must not call this suppressed view detected or automatically
fail-closed.

Thus the old within-age ancestor finding is **closed**, but only with the threat
boundary stated exactly as above.

## 2. Old manifest or redirected log

An old self-consistent manifest cannot redirect verification to a different
log: the compiled profile pins the log ID and genesis, and the manifest cannot
replace them. A lease must resolve exactly one active trust/recovery manifest at
the accepted current head. Old signatures remain historically verifiable only
under the transition/validity rules; they cannot select an older active epoch.

Ambiguous active-manifest resolution, a second genesis, a different log ID, a
broken extension or a lower head refuses as `authority_capability_invalid`.
Again, a consistent view suppressed by a compromised append-log service is a
threat-boundary failure, not a cryptographic detection success.

## 3. Lease misuse, replay and boundary crashes

Wrong nonce, requester, subject, boundary or run; expired/already-used leases;
cross-process transfer; and any payload not identically signed by the quorum all
refuse as `authority_capability_invalid`. The claim contract correctly makes an
ambiguous committed claim consumed and allows exactly one concurrent winner.

The durable chain is nevertheless incomplete:

- `AuthorityClosureCapability` binds both the `scope_mint` lease and use receipt.
- `RunCommitment` binds the `run_commit` lease but not the corresponding use
receipt.
- `ClaimReceipt` binds the `raw_start` lease and use receipt.
- The close marker binds the `raw_close` lease but not the corresponding use
receipt; its `raw_start` receipt is only inherited through `ClaimReceipt`.
- The final report binds the `final_analysis` lease and use receipt.

Because every receipt must be appended before its boundary succeeds, the plan
must define a canonical `BoundarySubject/v1` (or equivalent) for each boundary,
the exact subject digest and run binding, and the order:

1. form immutable boundary-request/preimage bytes;
2. request the nonce-bound lease for that digest;
3. append the lease and durable use receipt;
4. create/sign the boundary result binding both digests;
5. declare success.

It must also state what happens after a crash (a) before receipt append, (b)
after receipt append but before object signature/claim/close/report publication,
and (c) after durable success but before the caller receives it. `raw_start`
keeps the existing query-and-consume rule; a failed raw attempt remains
nonresumable. For `scope_mint`, `run_commit`, `raw_close` and `final_analysis`,
the contract must say whether a fresh lease may retry the same immutable subject
or whether a new subject/object is mandatory. No old receipt may authorize a
new object.

## 4. Witness transitions and availability

An honest witness never signs below its durable high-water mark or an
inconsistent extension. The verifier refuses witness disagreement, a partial
quorum, split payloads, invalid/retired/revoked witness keys, unresolved active
roles, an unavailable append log and an unavailable complete revocation view.
These are fail-closed availability outcomes, not prevention of DoS.

A consistent suppressed view divides cleanly:

- honest append log + honest quorum: not a permitted result of the written
`current head` query;
- compromised append log or compromised witness quorum: may pass and is outside
the guarantee;
- one compromised witness with two honest witnesses: cannot form an invalid
quorum if the honest append-log/current-head premise holds.

## 5. Revocation between raw start, raw close and analysis

The contract is boundary authorization, not continuous authorization. A
revocation appended immediately after `raw_start` may occur while raw
computation continues; the plan does not promise to stop it mid-instruction or
mid-block. The mandatory new `raw_close` lease must see the revocation and refuse
closure under the target matrix. The raw bytes may remain as an unclosed failed
attempt but cannot become a physical dataset or conclusion. A new
`final_analysis` lease independently rechecks the current state.

That semantics is coherent and appropriately modest. It must not be restated as
continuous authorization. A post-close nonretroactive record may preserve or
withhold a completed run only if that choice is canonical and signed; currently
`RevocationRecord/v1` does not list such a field even though the timing table
requires it.

## 6. Exhaustive revocation scope and repair

The matrix covers the principal trust, authority, run, claim, close, raw-ledger
and report families, refuses unknown types and distinguishes authority from run
status. It is not yet genuinely exhaustive across the full corpus. The
[architecture](../model-architecture) separately names `Material manifest`,
`Solver manifest`, `Run manifest`, trajectory blocks, transfer/carrier ledger,
cluster ledger and grain ledger; the gate documents also name
`EvidenceAvailabilityManifest`, `FeasibilityEnvelope`, stochastic/replicate/
resource manifests and multiple conformance/decision records. Some can
reasonably map to the generic enum rows, but that mapping is not canonical, and
unknown exact types must refuse.

Closure requires one versioned registry that, for **every** stored or signed
schema name in all plan documents, fixes exactly one of:

- a direct `REVOCABLE_OBJECT_TYPES/v1` tag and signer authority; or
- one nonrevocable-child tag with exactly one immediate content-addressed parent
invalidation route and inherited terminal status; or
- a trust/recovery-only lifecycle mechanism; or
- immutable/nonrevocable status with its explicit correction path.

In particular:

- map `EvidenceAvailabilityManifest`, material/calibration/solver manifests,
`FeasibilityEnvelope`, conformance records and decision rules to exact enum
tags rather than relying on prose aliases;
- make `RunManifest` the single immediate parent that binds every trajectory,
transfer/carrier, cluster and grain block, and make the close marker bind that
exact run-manifest digest; ancestor commitment/capability invalidation can
still cascade through the chain;
- define the final report's canonical parent bindings and status inheritance;
- add `preserve_completed_run` (or an equivalent closed enum) to the signed
nonretroactive record if post-close preservation is allowed;
- define the exact exceptional-repair field and precedence in
`TrustTransition` or `RecoveryTransition`. Logging an immutable revocation
while later excluding it from the “complete effective revocation set” needs a
deterministic epoch/sequence rule; “names the exceptional record” is not
enough, and repair must still re-close every affected scope.

## 7. Target timing and status precedence

For every direct target and inherited child, the intended timing rule is:

| Timing | Required result |
| --- | --- |
| Before `raw_start` claim | Fresh lease sees the target; authority-layer targets yield `authority_capability_invalid`, otherwise a run-layer target yields `run_commitment_invalid`; no keys or directory are touched. |
| After claim, before `raw_close` | Raw may compute, but the fresh close lease refuses; the attempt is consumed and cannot close physically. |
| After close, before/later analysis | Fresh analysis lease applies the signed post-close preserve/withhold rule; missing policy must refuse rather than infer. |
| Retroactive from an earlier sequence | Every affected current or future physical conclusion is withheld, including one whose start/close previously passed. |

Combined failures follow the written precedence: any bootstrap, trust/role,
checkpoint/witness, lease/use receipt, store, gate, capability or revocation-view
failure wins as `authority_capability_invalid`; only after that layer validates
can commitment, field/domain, claim, close or their children yield
`run_commitment_invalid`. The remaining work is exhaustive object mapping, not
status-order selection.

## 8. Cross-document stage and record bindings

The parent, Gate G, architecture, calibration firewall and implementation
sequence consistently require:

- a fresh lease at `scope_mint`, `run_commit`, `raw_start`, `raw_close` and every
`final_analysis`;
- exact committed Stage-11 field bytes, not regenerated or reselected inputs;
- no physical constructor from a capability alone;
- no physical cluster output without F1, and no developed-film conclusion
without F2;
- no young checkpoint as an authorization route;
- authority failures before run failures, and both before scientific outcomes.

The cross-document mismatch is the missing `run_commit` and `raw_close` receipt
binding noted above. The close marker also needs to bind the canonical run/raw
manifest that closes every table, rather than merely asserting that raw blocks
are its children.

## 9. Threat-model claims

The plan correctly says that signatures authenticate approval rather than
scientific truth, and that immutable hashes detect changed bound bytes rather
than malicious-but-canonically-signed evidence. It also correctly treats log or
quorum unavailability as DoS/fail-closed availability loss.

The compromise sentence must be split by principal and detection:

- root compromised while the two-of-three recovery threshold, verifier and OS
remain honest: recovery is supported only after compromise is detected, via
the specified recovery transition and independent re-closure;
- recovery threshold or verifier/OS compromised: no in-band recovery or
security guarantee; reviewed verifier replacement is required;
- issuer, checkpoint signer, revocation signer or claim service compromised:
authenticated malicious acts may pass until external detection and effective
retirement/revocation/re-closure; compromise does not itself force fail-close;
- append-log service or freshness-witness quorum compromised: a consistent
suppressed view can pass; currentness, anti-equivocation and revocation
completeness are no longer guaranteed;
- one witness compromised: the two honest witnesses preserve the quorum rule
under an honest append log;
- owner/reviewer compromise or collusion: false science can be authentically
approved; cryptography supplies provenance, not truth.

Replace “is outside the stated guarantee and causes fail-closed re-closure” with
the accurate per-principal statements above. Recovery is an action after
detection; it is not an automatic property of compromise.

# Exact closure actions

1. Define a canonical boundary-subject and state machine for all five leases;
 bind both lease and use-receipt digests into the capability, run commitment,
 claim receipt, close marker and final report as applicable; specify all crash
 windows and retry identity rules.
2. Make the close marker bind one canonical run/raw-manifest digest that in turn
 binds every raw block.
3. Publish one exhaustive schema-to-revocation registry covering every object
 name in all documents, with exactly one direct target or immediate parent
 route and exact inherited status.
4. Add a signed post-close preserve/withhold field or prohibit preservation;
 define the exceptional retroactive-repair transition, effective-set
 calculation, epoch/sequence precedence and mandatory re-closure.
5. Rewrite G6 compromise semantics by principal, distinguishing guarantee loss,
 external detection, recoverability and DoS. Explicitly state that a
 consistently suppressed view can pass after append-log or witness-quorum
 compromise.
6. Add mutation oracles for missing/wrong use receipts, cross-process and
 cross-subject lease replay, every crash window, every named object type and
 inherited route, missing post-close policy, exceptional revocation repair,
 and each compromised-principal boundary.
7. Obtain another cold plan-contract review. Separately, even after contract
 closure, create and independently validate the real evidence, keys, roles,
 services, log, leases, gate records, capability and run commitment before any
 Stage 10.5 or Stage 11 operational claim.

# Preserved scientific and authority nonclaims

- No Born-rule or single-photon-selection derivation.
- No claim that PFG-01 contains a self-sustained or injection-lockable Adler
oscillator; the evidence audit supports only a passive material path and a
quarantined, explicitly pumped counterfactual.
- No physical latent-cluster conclusion without F1; no developability, film
density, visibility or classical-recording conclusion without F2 and the
exact developed-film scope.
- No claim that a kinetic surrogate is a microscopic transfer derivation.
- No claim that signatures make evidence true, that tamper detection prevents
DoS, or that boundary leases provide continuous authorization.
- No claim that actual material/calibration/solver authority, keys, services,
capabilities, commitments or physical outputs currently exist.

# Input integrity and comments

All eight inputs were SHA-256-frozen before any input was read. Every digest
matched the supplied freeze and was unchanged after adjudication. Artifact
comment threads were listed before adjudication; none were present.

| Reviewed input | Pre-read and post-review SHA-256 |
| --- | --- |
| parent `index.md` | `1156b4a7d9e64207e408760fac95957ca60f03e2fadb44981a369678a2ff9657` |
| `preimplementation-authority-gates/index.md` | `767c01c438293331efda8b5ad95dcb06afd1f799e6cb65fed87bab477e384662` |
| `model-architecture/index.md` | `f53b09b8a7c32f1089380533515eeba3e834fa8735f6c7da207afac67a35584a` |
| `calibration-and-analysis/index.md` | `119a4b71c825a3c80694a264b48abb52e574fa2b38930257c5d941c9def325d5` |
| `implementation-sequence/index.md` | `3093c29853df71ea0d3d9014e15944ba4c2427ab370ee51a3aba69db1422ea87` |
| `material-oscillator-evidence/index.md` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` |
| prior `independent-gate-g-review/index.md` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` |
| prior `independent-gate-g-closure-review/index.md` | `fc8d2846bcde133a617dc4bdade43d658bdd53002e1e369a6c8a66af8cfb1c06` |

Only this new review artifact was created. No reviewed artifact, code, ticket,
Git state or unrelated file was edited.
