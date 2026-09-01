---
title: "Independent Gate G three-repair contract review"
kind: review
---

# Strict verdicts

| Question | Verdict |
| --- | --- |
| Full Gate G plan-contract closure | **PARTIALLY CLOSED.** The atomic `raw_start` claim and cumulative per-revocation repair are closed. The final-analysis result is now correctly the release record, but release-key/current-head semantics across lease issuance, lease-use receipt and delayed release signing remain ambiguous. |
| Diagnostic/exploratory Stages 0–10 | **YES.** They may proceed only through diagnostic, exploratory or conformance types that cannot mint a physical authority object or serialize a physical ledger or verdict. |
| Stage 10.5 scope closure now | **NO.** The plan-contract blocker below can affect `scope_mint` and later boundaries. Independently, this corpus supplies no real keys, services, signed closures or capability. |
| Stage 11+ conclusion-bearing physical work now | **NO.** No valid scope capability, exact run commitment, claim receipt, close marker, material authority or numerical certificate exists, and Gate G is not yet fully specified. |

This review separates specification closure from operational existence. Missing
keys, evidence, services, signed closures, capabilities, commitments, material
authority and numerical certificates do **not** by themselves make a closed
specification open. Here, however, one specification ambiguity also remains.

# Finding in priority order

## 1. Blocker — boundary currentness and release-key issuance use two unresolved linearization times

The latest-head lease binds the active trust manifest and complete effective
revocation set at its witnessed head, expires up to 60 seconds later, and is then
append-consumed ([preimplementation authority gates](../preimplementation-authority-gates):362–388).
The same document calls this immediate-boundary authorization and says no earlier
lease can conceal a revocation ([preimplementation authority gates](../preimplementation-authority-gates):390–397).
Final analysis, however, selects the release key valid at the **lease-use receipt**
linearization sequence, fixes that key ID in consumed state and may obtain its
signature later ([preimplementation authority gates](../preimplementation-authority-gates):455–463;
[calibration and analysis](../calibration-and-analysis):170–198;
[implementation sequence](../implementation-sequence):365–381).

Those rules do not settle a real sequence:

1. witnesses lease head `H0`, whose active manifest authorizes release key `K0`;
2. a trust transition or revocation at `H1` retires `K0` and authorizes `K1`;
3. the still-unexpired lease is consumed at receipt sequence `H2`;
4. the report is appended and release signing happens later.

The lease authenticates `K0`'s manifest, while the receipt-time rule appears to
require `K1`. Selecting `K1` contradicts the lease payload; selecting `K0`
contradicts the receipt-time rule. If `K0` is fixed at receipt and retired before
the later signature, G0 says retired keys cannot issue at or after activation
([preimplementation authority gates](../preimplementation-authority-gates):311–319),
yet deterministic completion forbids substituting `K1`. The specified terminal
signing failure is fail-closed, but it does not decide whether the release was
already logically issued at receipt or is issued when its signature/record is
actually created. The same lease-to-receipt gap can let a newly appended
authority revocation miss `scope_mint`, `run_commit`, `raw_start` or `raw_close`,
so this is not only an analysis-availability question.

**Bounded correction:** choose one boundary linearization rule and encode it in
the shared state machine. The least disruptive rule is: the atomic
`leased -> consumed` transition must compare the authority log's then-current
head, active-manifest digest and effective-revocation digest with the lease; if
any advanced, it appends no receipt, abandons the lease and obtains a fresh lease
for the same immutable subject. For `final_analysis`, that same transaction must
fix the report digest, authorized release-key ID, canonical release-record
preimage/digest and logical issuance sequence. Either obtain the deterministic
Ed25519 release signature inside that transaction, or explicitly authorize
post-receipt completion as issuance at the stored receipt sequence. State that
normal post-receipt rotation does not change the fixed result, while retroactive
key invalidation or later release-record revocation withholds presentation.
Apply the same head-equality/advance oracle to all five boundary coordinators and
add the lease→receipt race to Stage 10.5/10.75/11/12 attacks.

# Three final repairs adjudicated independently

## A. Atomic `raw_start` claim — CLOSED at plan-contract level

The claim service is now the `raw_start` coordinator and owns one
commitment-keyed durable CAS-plus-log-append primitive
([preimplementation authority gates](../preimplementation-authority-gates):521–555).
The single transition assigns the commitment to one immutable subject, consumes
only that subject's active lease, appends its use receipt and fixes the receipt
preimage. It is implementable as one authority-store transaction/WAL primitive;
the text expressly forbids a best-effort claim/log dual write and fails closed if
the primitive is unavailable.

| Attack | Contract result |
| --- | --- |
| Two distinct subjects race one commitment | Exactly one CAS commits; the loser gets `claimed_by_other_subject`, appends no receipt and touches no key/directory. |
| Same subject retries before transaction | An uncommitted/expired lease appends no receipt; after expiry the same immutable subject may obtain a fresh lease. If another subject has since won, the retry loses the commitment CAS. |
| Lease expires before transaction | Active-lease verification fails atomically; commitment remains unclaimed and no receipt exists. |
| Late losing or abandoned receipt | Cannot be appended outside the same CAS-plus-log primitive and therefore loses/refuses. |
| Crash before CAS | No state change and no claim/receipt. |
| Crash during CAS-plus-append | The primitive is all-or-nothing; an ambiguous response is queried by commitment digest and treated as consumed whenever commit may have occurred. |
| Crash after `consumed` but before receipt signature/append | The winning subject and receipt preimage are fixed; recovery may sign/append only that receipt. |
| Crash after result but before response | Query returns the same completed receipt digest. |
| Terminal signing failure | Commitment enters terminal consumed-failed and is never reassigned. This may yield no usable winner, but never two winners. |
| Unavailable or compromised claim/log service | Unavailability fails closed; claim-service compromise explicitly loses the one-use guarantee until external detection, retirement and invalidation. A compromised/suppressing log is outside the currentness guarantee as stated. |
| New attempt after any committed claim | Requires a new issuer-signed commitment and new run ID; the old claim is never released. |

Exactly-one assignment is therefore compatible with deterministic recovery. A
post-CAS terminal signing failure consumes the commitment rather than inventing
a second winner, which is the correct fail-closed tradeoff.

## B. Analysis release inside `final_analysis` — PARTIALLY CLOSED

The prior structural defect is repaired: `AnalysisReleaseRecord/v1`, not
`FinalReport/v1`, is now the sole completed result; the consumed state fixes the
report and release key; report append is idempotent; completion accepts only the
matching release-record digest; and caller return occurs only after durable
completion. Changed reports, changed releases, fresh-lease recovery and key
substitution refuse. A corrected analysis uses a new subject/report/release and
leaves raw bytes immutable. An orphaned report may remain discoverable as an
immutable audit child—the contract promises no confidentiality—but it is
noncurrent and may not be returned as a completed physical presentation.

Crash edges after receipt consumption, report append, release signing, release
append and completed-state persistence are deterministic **provided the release**
**key and release-record preimage were validly fixed**. An unavailable signer may
be retried only for the fixed pair and otherwise terminates failed; a malicious
authorized signer may deny service or authentically sign a bad fixed report,
which the per-principal threat model correctly places outside cryptographic truth
guarantees. The unresolved before/between/after key-rotation sequence is Finding
1, so this repair cannot yet be called fully closed.

## C. Cumulative repairs per revoked digest — CLOSED at plan-contract level

G5 now defines candidates and the controlling tuple independently for every
exact retroactive revocation digest, then subtracts every digest with a valid
controlling repair ([preimplementation authority gates](../preimplementation-authority-gates):665–694).

| Case | Deterministic result at head `H` |
| --- | --- |
| `R1` repaired at epoch 2; unrelated `R2` repaired at epoch 3 | Both repairs remain independently controlling; neither `R1` nor `R2` is effective. |
| Two repairs of `R1` | The complete valid repair with the greatest `(recovery_epoch, activation_sequence, log_sequence)` controls. |
| Invalid/incomplete higher repair | It is not a candidate; the earlier valid repair remains controlling. |
| Same-tuple conflict | `authority_capability_invalid`. |
| A required re-closure is later revoked/invalidated | It is no longer a validating current re-closure, so that repair ceases to qualify and `R1` becomes effective again through an explicit authority event, not an unrelated repair. |
| Repair of nonretroactive record, repair/recovery/trust transition, self or circular target | Refused by the closed target rule. |
| New revocation after repair | It is a distinct member of `R(H)` and remains effective unless independently repaired; defects in reclosed objects require a new revocation against those objects. |
| Heads before, at and after activation | Candidate inclusion is exactly `activation <= H`; the result is total at every accepted head. |

The rule is cumulative, noncircular and does not silently reactivate `R1` merely
because an unrelated later transition repairs `R2`.

# Regression and cross-document check

| Earlier closed area | Disposition |
| --- | --- |
| Bootstrap/root/recovery, role separation and recovery boundary | **CLOSED.** Fixed bootstrap/profile, root/recovery/log pins, transition sequences and out-of-band terminal boundary remain exact. |
| Latest-head witness leases | **REOPENED only for the lease→receipt head-advance ambiguity in Finding 1.** Nonce binding, witness quorum, rollback/fork/ancestor refusal and compromised-principal limits remain closed. |
| Five canonical boundary subject types | **CLOSED.** Exact preimages and sole result bindings remain exhaustive. |
| `run_commit` and `raw_close` lease/use-receipt bindings | **CLOSED.** Both results bind subject, lease and receipt. |
| `RawManifest/v1` completeness | **CLOSED.** Ordered schema-tagged block digests, row counts/schemas, exactly-once and no-unlisted-object rules remain exact. |
| Exhaustive schema registry and sole parents | **CLOSED.** Unknown/alias schemas refuse; each child has its one route. |
| Post-close preserve/withhold | **CLOSED.** Signed compatibility, retroactive withholding and release-only withholding remain exact. |
| Authority-vs-run status precedence | **CLOSED.** Authority failures win before run failures, then scientific results. |
| Per-principal threat claims | **CLOSED.** The plan distinguishes authenticated malice, detection, recovery, DoS and guarantee loss for every named principal. |
| F1/F2 routing | **CLOSED.** Cluster authority and conditional development authority remain separate, scope-specific and fail-closed. |
| Final comparator isolation | **CLOSED.** Comparator access remains post-close and cannot regenerate raw data. |
| Adler counterfactual and nonclaims | **CLOSED.** The passive authority path excludes Adler; the counterfactual is separately pumped, quarantined and cannot support Born/PFG-01 claims. |

Across the parent plan, Gate packet, model architecture, calibration/firewall and
implementation sequence, the repaired raw-start, final-release and cumulative-
repair shapes agree. The only live cross-document contract defect is the shared
authority-time ambiguity in Finding 1; repeated references to the receipt's
linearization sequence do not supply the missing head-advance and post-receipt
key-issuance oracle.

# Operational authority remains absent

Even after the bounded contract correction, Stage 10.5 would still require real,
independently validated gate evidence and reviews, current material/calibration/
solver records, actual owner/reviewer/issuer/recovery/release keys, an append-log
and witness quorum, signed closure records and a scope capability. Stage 10.75
would additionally require an exact field/domain/run commitment. Stage 11+
would require the claim service, material and thermodynamic authority, F1/F2 as
applicable, a full-exposure numerical certificate, a consumed claim, a complete
raw close and a nonrevoked analysis release. None of those objects or
capabilities is instantiated by these plan documents.

# Integrity and review conditions

All ten inputs were SHA-256-frozen before reading and matched the requested
digests. Artifact comment threads were listed before adjudication; none were
present. Post-write hash verification is recorded below.

| Reviewed input | Pre-read SHA-256 | Post-write SHA-256 |
| --- | --- | --- |
| parent `index.md` | `89a2664b122301d2d918d94e973c4bed774b7f0b38211bed82ad4c2595135185` | `89a2664b122301d2d918d94e973c4bed774b7f0b38211bed82ad4c2595135185` |
| `preimplementation-authority-gates/index.md` | `7eca494a6ab696156936883cf5d7f25cb80a3c718ed37e34bad36ea2b3607fd0` | `7eca494a6ab696156936883cf5d7f25cb80a3c718ed37e34bad36ea2b3607fd0` |
| `model-architecture/index.md` | `624c340f8b9203606a0807ce3b97a0484aa09018898ea8e7b960cf942a56f580` | `624c340f8b9203606a0807ce3b97a0484aa09018898ea8e7b960cf942a56f580` |
| `calibration-and-analysis/index.md` | `c0edde7428c051372bf5f0410d25a0105b8a3fbb682f7d9f655a9074d83fa4a2` | `c0edde7428c051372bf5f0410d25a0105b8a3fbb682f7d9f655a9074d83fa4a2` |
| `implementation-sequence/index.md` | `ce10499d9bd6eb834ae037a32907f338897ab14e3c340aec65af8ace04b75e65` | `ce10499d9bd6eb834ae037a32907f338897ab14e3c340aec65af8ace04b75e65` |
| `material-oscillator-evidence/index.md` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` |
| `independent-gate-g-review/index.md` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` |
| `independent-gate-g-closure-review/index.md` | `fc8d2846bcde133a617dc4bdade43d658bdd53002e1e369a6c8a66af8cfb1c06` | `fc8d2846bcde133a617dc4bdade43d658bdd53002e1e369a6c8a66af8cfb1c06` |
| `independent-gate-g-latest-head-review/index.md` | `a60efe3ae628c66c97a8ac8ab9dd2f08cfd312e5f0587cf05361d6166f194c74` | `a60efe3ae628c66c97a8ac8ab9dd2f08cfd312e5f0587cf05361d6166f194c74` |
| `independent-gate-g-final-review/index.md` | `32ec67a16bf9a748693c63325ca60c1139dd58730c23b6db604df69ac9c062d5` | `32ec67a16bf9a748693c63325ca60c1139dd58730c23b6db604df69ac9c062d5` |

Only this review artifact was created. No reviewed plan, prior review, code,
ticket, Git state or unrelated artifact was modified.
