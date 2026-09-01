---
title: "Independent Gate G final contract review"
kind: review
---

# Strict verdicts

| Question | Verdict |
| --- | --- |
| Full Gate G plan-contract closure | **PARTIALLY CLOSED** — latest-head leases, boundary subjects, the raw-manifest registry, post-close policy, status precedence and per-principal threat claims are substantially closed, but the raw-start claim is not one atomic transaction with its lease-use receipt, the separately signed analysis release is outside the completed final-analysis boundary, and the exceptional-repair effective-set rule is not cumulative. |
| Diagnostic/exploratory Stages 0–10 | **YES** — only through diagnostic, exploratory or conformance types that cannot mint a physical capability or serialize a physical ledger or verdict. |
| Stage 10.5 scope closure now | **NO** — the three contract blockers below remain, and the corpus contains no actual closure keys, signed gate records, append-log state, witnessed lease, re-closure bundle or capability. Prototype/conformance work remains inside Stages 0–10; no minted object may be treated as physical authority. |
| Stage 11+ conclusion-bearing physical work now | **NO** — there is no valid capability, exact run commitment, claim, close marker or analysis release, and the authority contract is not fully closed. |

Contract completeness is separate from operational authority. These documents
specify intended types and controls; they do not instantiate trustworthy keys,
services, evidence, witnesses, commitments or material authority. The negative
Adler evidence audit supplies only authority for the nonclaim: it does not close
any passive-material gate.

# Blocking findings

## 1. Blocker — `raw_start` receipt consumption and the one-use commitment claim are two coordinators in the wrong order

The [Gate contract](../preimplementation-authority-gates), G2.1 lines 415–449,
gives the boundary coordinator ownership only of `(boundary, subject_digest)`
and requires it to append the lease-use receipt before completing the sole
result. G4 lines 502–510 separately gives the claim service the
`unclaimed -> claimed` CAS keyed by commitment. The
[implementation sequence](../implementation-sequence), Stage 11 lines 325–330,
makes the conflict explicit: consume the subject/lease/use-receipt chain first,
then ask the claim service to compare-and-append.

Two concurrent attempts may use distinct attempt IDs and therefore distinct
`RawStartSubject` digests. Both subject coordinators can reach `consumed`; only
later does one commitment-level CAS win. The loser then has a durable receipt
after which G2.1 says its sole `ClaimReceipt` must be deterministically
completable, but the commitment belongs to the other subject. Likewise, a crash
after receipt append but before the claim CAS can be followed by another subject
claiming the commitment, leaving the first subject locked but impossible to
complete. This contradicts both the post-receipt recovery rule and exactly-one-
winner semantics.

**Bounded repair:** make the authorized claim service the `raw_start` boundary
coordinator and key its linearizable transaction by both commitment digest and
subject digest. Only the winning subject may commit the lease-use receipt. One
durable transition must reserve/consume the commitment for that immutable
subject, append the matching receipt, and fix the sole `ClaimReceipt` result;
crash recovery must complete that subject or terminally consume the commitment
without permitting a second subject. State the loser and late-receipt CAS
results explicitly and align G2.1, G4 and Stage 11.

## 2. Blocker — `AnalysisReleaseRecord` is outside the completed `final_analysis` boundary

G2.1 lines 407–449 makes `FinalReport/v1` the sole result and declares the
boundary completed when that report is appended. The
[analysis firewall](../calibration-and-analysis), lines 170–189, and Stage 12
lines 354–365 then ask a separate release service to sign and append
`AnalysisReleaseRecord/v1`. That later act has no subject/CAS state of its own
and is not the sole result protected by the consumed final-analysis receipt.

Consequently, a crash after the report completes but before release signing, a
release signer retry, or an intervening signer transition/revocation has no
contract-defined linearization rule. The old final-analysis chain authenticates
the report preimage but does not by itself establish that the later release
action was current at its authorization boundary. Corrected reports are
well-described, and release revocation preserves raw bytes, but initial release
issuance remains outside the five-boundary state machine.

**Bounded repair:** keep the five boundary types but make the sole completed
`final_analysis` result the release package or `AnalysisReleaseRecord`. After
the receipt fixes the report preimage, the coordinator must append the exact
`FinalReport`, obtain the authorized release signature over that fixed report
and chain, append the release, and record completion by release digest. Recovery
may complete only that pair. If release signing cannot finish, the subject
terminates failed and no report becomes current. Define release-key validity at
that same linearization sequence. A sixth fresh `analysis_release` boundary is
an alternative, but it would require revising the currently closed five-type
enumeration everywhere.

## 3. Blocker — exceptional repairs are not cumulative and can silently reactivate an earlier repaired revocation

G5 lines 620–629 defines the effective set as all revocations minus “a repaired
digest named by the highest valid recovery epoch.” Read literally, recovery
epoch 2 repairing `R1`, followed by recovery epoch 3 repairing unrelated `R2`,
subtracts only `R2`; `R1` re-enters the effective set even though no transition
explicitly reversed its repair. “Higher sequence wins within an epoch” does not
define a per-revocation decision, cumulative repair set, or whether a later
recovery transition must carry forward every earlier repair. The ambiguity can
change which gates/capabilities validate at Stage 10.5.

The rule does correctly restrict repair to `RecoveryTransition/v1`, retains the
original bytes, requires exhaustive affected scopes and re-closure, rejects
same-epoch/sequence conflict, and forbids `TrustTransition` repair. It does not
yet define the result of multiple legitimate repairs across epochs.

**Bounded repair:** compute repair disposition independently for each exact
retroactive `RevocationRecord` digest. At head `H`, subtract every digest whose
latest valid repair decision by ordered `(recovery_epoch, activation_sequence, log_sequence)` is active and whose complete affected-scope re-closure validates.
Forbid repair targets other than retroactive revocation records, self/circular
references, repair of recovery/trust transitions, and implicit reversal. If a
later recovery epoch is intended to supersede the whole repair set instead,
require an exhaustive carried-forward repair-set digest and fail on omission.

# Prior-finding dispositions

| Prior Gate G finding | Final disposition |
| --- | --- |
| 1. Bootstrap, roles, lifecycle and root recovery | **CLOSED at contract level.** Fixed encoding/algorithms/domain separation, pinned root/recovery/log genesis, distinct roles, transition epochs and the out-of-band verifier boundary are explicit. No corresponding real keys or ceremonies are evidenced. |
| 2. Latest-head freshness, rollback and file authority | **CLOSED within the stated honest append-log plus honest witness-quorum boundary.** Every named boundary uses a nonce-bound current-head lease; ancestor, rollback, fork, unavailable and descriptor/path cases have exact refusal rules. A compromised log or two-witness quorum may still authenticate suppression, as G6 now accurately says. |
| 3. Complete scientific signature coverage | **CLOSED at contract level.** The owner/reviewer signatures cover the complete canonical gate record and the capability binds an exhaustive gate map. Authenticated approval remains expressly distinct from scientific truth. |
| 4. Exact run and durable claim | **PARTIALLY CLOSED.** Field/domain/run coverage, run-commit receipt binding, exact bytes and RawManifest closure are closed. The cross-subject raw-start transaction in Finding 1 remains. |
| 5. Revocation targeting, effect and precedence | **PARTIALLY CLOSED.** Exact direct tags, sole parents, aliases/unknown schemas, signed post-close effects and authority-before-run routing are closed. Multi-epoch repair-set computation in Finding 3 remains. |
| 6. Threat-model accuracy | **CLOSED.** The table separately covers root, recovery threshold, verifier/OS, append log, checkpoint signer, one witness, witness quorum, issuer, analysis-release signer, revocation signer, claim service and owner/reviewer. It distinguishes approval from truth, tamper detection from DoS, and observed failures from undetected compromise and external recovery. |
| Latest residual: boundary subjects/use receipts/crashes | **PARTIALLY CLOSED.** All five exact subject/preimage types and result bindings exist; run-commit and raw-close receipt omissions are repaired. Raw-start composition remains non-atomic, and final release remains outside its boundary result. |
| Latest residual: exhaustive RawManifest | **CLOSED at contract level.** The manifest binds all block kinds exactly once, ordered schema-tagged digests, row counts/schemas and the no-unlisted-object rule; the close marker binds that exact manifest. |
| Latest residual: exhaustive registry/parent invalidation | **CLOSED at contract level.** Every named canonical stored/signed v1 schema is assigned a direct tag, trust/currentness lifecycle, immutable correction path or exactly one immediate parent; aliases and unknown schemas refuse. |
| Latest residual: post-close preserve/withhold | **CLOSED at contract level.** Mandatory compatibility, timing, retroactive withholding, release-only withholding and inherited child policy are exact. |
| Latest residual: analysis-release currentness/correction | **PARTIALLY CLOSED.** Direct revocation, corrected report/release creation and raw preservation are exact; release issuance is not inside the completed current-head boundary (Finding 2). |

# Required adversarial pressure tests

## Five subjects and crash/replay behavior

| Boundary | Exact binding adjudication | Crash/replay adjudication |
| --- | --- | --- |
| `scope_mint` | `ScopeMintSubject/v1(CapabilityPreimage/v1)` is bound with lease and receipt by `AuthorityClosureCapability`. | Before-receipt same-subject lease renewal, late-receipt CAS loss, post-receipt deterministic completion and post-result idempotent return are exact. |
| `run_commit` | `RunCommitSubject/v1(RunCommitmentPreimage/v1)` is bound with lease and receipt by `RunCommitment`. | Same-subject recovery is exact; cross-subject, requester, process, nonce and result replay refuse. |
| `raw_start` | `RawStartSubject/v1(RawStartPreimage/v1)` is bound with lease and receipt by `ClaimReceipt`. | **Fails the combined pressure test:** distinct-subject receipts can precede the commitment CAS, so post-receipt deterministic completion and exactly-one winner cannot both hold. Raw-attempt nonresumability itself is explicit. |
| `raw_close` | `RawCloseSubject/v1(RawClosePreimage/v1)` binds capability, commitment, claim and exact `RawManifest`; `CloseMarker` binds subject, lease and receipt plus the reopened run/raw chain. | Changed manifest, fresh-lease retry after receipt, cross-subject replay and post-receipt changed close all refuse. |
| `final_analysis` | `FinalAnalysisSubject/v1(FinalReportPreimage/v1)` and `FinalReport` bindings are exact. | Report recovery is exact, but the later `AnalysisReleaseRecord` is not covered by completed-state idempotence or release-boundary currentness. |

The generic coordinator correctly handles crash before receipt, after receipt
before result, after result before response, late receipt CAS and retry of the
same immutable subject. The two exceptions above arise where another authority
operation occurs after the coordinator's protected result or receipt.

## RawManifest and schema registry

- Omitted block, duplicate block, extra/unlisted object, wrong row count,
mismatched schema or close marker pointing to another manifest violates
`RawManifest/v1`/`CloseMarker/v1` and yields `run_commitment_invalid` after
authority validation.
- Wrong immediate parent, alias and unknown schema refuse under
`AUTHORITY_OBJECT_REGISTRY/v1`. Raw blocks have the sole parent
`RawManifest/v1`; that manifest has the sole parent `CloseMarker/v1`.
- The registry accounts for evidence, material/calibration/solver records,
feasibility/conformance/review/rule objects, all five subject/preimage pairs,
field/domain/stochastic/replicate/resource children, run/claim/raw/close,
report/release and immutable revocation records. No prose alias creates a new
top-level type.

These are closed plan assertions, not evidence that an implementation performs
the required directory inventory and row/schema recomputation. Those checks
must be conformance-tested before any real close marker is accepted.

## Revocation, release and combined failures

- Missing or incompatible `post_close_effect` fails authority. Preservation is
legal only for a run already closed before the effective sequence;
withholding retains raw bytes; retroactivity always withholds; nonrevocable
children inherit their sole parent's compatible policy.
- Direct release revocation makes that release
`authority_capability_invalid`, preserves raw inspectability, and requires a
new subject/report/release for correction. Finding 2 prevents declaring the
issuance boundary itself closed.
- If bootstrap/trust/recovery, signer role, checkpoint/witness, lease/receipt,
store, gate, capability, revocation view or release authority fails,
`authority_capability_invalid` wins. Only after that layer passes may
commitment/field/domain/claim/close failures become
`run_commitment_invalid`; scientific statuses are evaluated last.
- Repair activation, affected-scope exhaustiveness, re-closure validation and
same-epoch conflicts are specified, but multiple repairs across recovery
epochs fail the effective-set pressure test in Finding 3.

## Principal compromise and cross-document consistency

The per-principal G6 table passes the requested distinction tests. Authenticated
malice may remain undetected; observed signature/view/availability failures fail
closed; external detection and recovery are not automatic. One witness cannot
forge a quorum under an honest log and two honest witnesses; two compromised
witnesses or a suppressed log lose currentness. A malicious owner/reviewer can
approve false science, while a malicious issuer, release signer, revocation
signer or claim service can authenticate role-specific damage until audit.

The parent plan, architecture, calibration firewall and implementation sequence
agree on passive real-field input, exact committed Stage-11 bytes, F1/F2 scope,
RawManifest closure, authority-before-run precedence and comparator isolation.
The two cross-document defects are the raw-start ordering at Stage 11 and the
post-report release step at Stage 12. The Gate-G repair-set ambiguity propagates
to every document that calls the effective revocation set “complete.”

# Scientific nonclaims and authority boundary

The strict Born-free nonclaims are preserved. Nothing claims a universal Born
rule, single-photon selection, a unique microscopic mechanism, or an autonomous
PFG-01 Adler oscillator. The material audit supports a passive, transient
silver-halide path and permits Adler only as a separately pumped,
`counterfactual_only` branch with no physical authority edge.

No actual material functional, microscopic transfer authority, retained-batch
identifiability result, thermodynamic contract, F1/F2 evidence, numerical
full-exposure certificate, signed gate closure, key set, log, witness quorum,
capability, commitment, claim, raw close or release is supplied. Contract repair
cannot substitute for any of those objects.

# Integrity and review conditions

All nine inputs were SHA-256-frozen before reading and matched the requested
digests. Artifact comment threads were listed before adjudication; none were
present. After this artifact was written, all nine inputs were rechecked and
remained unchanged.

| Reviewed input | SHA-256 |
| --- | --- |
| parent `index.md` | `2caa1ae9e003cdb6704a8f9a869508a60027ede26ea3021649bc4476a2778909` |
| `preimplementation-authority-gates/index.md` | `c504bb011130d105793f079c701f436a7d20770e8b61cc1e91d76204b090d422` |
| `model-architecture/index.md` | `62570d483d2461cb174a8d68f0031b63ae768293014906bd36ca71df6c41c13e` |
| `calibration-and-analysis/index.md` | `22488e016ccb948da51e22bc14ede23867e0431d6bccf2be38be779f20ae5d21` |
| `implementation-sequence/index.md` | `1c7f9bc780533c3eb1f44c28a1fd427b12f07d7e4f676cc207bbd85ef9577706` |
| `material-oscillator-evidence/index.md` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` |
| `independent-gate-g-review/index.md` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` |
| `independent-gate-g-closure-review/index.md` | `fc8d2846bcde133a617dc4bdade43d658bdd53002e1e369a6c8a66af8cfb1c06` |
| `independent-gate-g-latest-head-review/index.md` | `a60efe3ae628c66c97a8ac8ab9dd2f08cfd312e5f0587cf05361d6166f194c74` |

Only this review artifact was created. No reviewed plan, prior review, code,
ticket, Git state or unrelated artifact was edited.
