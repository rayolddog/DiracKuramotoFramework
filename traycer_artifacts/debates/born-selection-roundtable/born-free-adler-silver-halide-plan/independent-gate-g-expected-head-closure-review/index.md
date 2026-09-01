---
title: "Independent Gate G expected-head closure review"
kind: review
---

# Strict verdicts

| Question | Verdict |
| --- | --- |
| Full Gate G plan-contract closure | **NOT CLOSED.** The expected-head repair closes the lease-to-consumption race at all five boundaries, but the signed-result identity, delayed-signature retirement rule, durable final-analysis bundle and coordinator terminal states remain under-specified or contradictory. |
| Diagnostic/exploratory Stages 0–10 | **YES, diagnostic only.** They may use only diagnostic, exploratory and conformance types that cannot mint or serialize physical authority, raw-ledger or physical-verdict objects. |
| Stage 10.5 | **NO.** The plan-contract blockers below must close before scope minting, and no real trust service, signed closures or capability exists here. |
| Stage 11+ | **NO.** Neither this review nor these plans create a scope capability, run commitment, claim, material authority, numerical certificate, closed raw dataset or analysis release. Stage 10.75 is likewise unauthorized. |

This is a specification review, not an authorization act. It authorizes **no**
**actual authority object and no conclusion-bearing physical modeling**.

# Findings in priority order

## 1. Blocker — the receipt/result hash graph does not define one stable result identity

Gate G intends the acyclic direction
`subject -> lease -> receipt(template digest, signer key) -> result`, and
correctly omits the result digest from the receipt
([authority gates](../preimplementation-authority-gates):435–459). But the
remaining identity rules do not determine the bytes or digest used at each
step:

- every admitted object is said to be content-addressed by SHA-256, while
`LeaseUseReceipt/v1` is also said to bind “its own digest”;
- the result template excludes receipt, signature and self digest, yet the
consume transaction claims to construct a “full result preimage/digest”
before the deterministic signature exists;
- later state is `completed(result_digest)`, direct revocation targets the
result digest, and recovery returns that digest, without distinguishing an
unsigned payload ID from the digest of the final signed stored envelope.

A content digest cannot be a field in the exact bytes it hashes, and the digest
of a signed envelope cannot normally be known before its signature. Ed25519
being deterministic does not make the signature bytes available without the
private key. This affects all five results and is especially consequential for
`AnalysisReleaseRecord/v1`: a direct release revocation between receipt and
signature needs a stable target, while completion must later identify the same
release unambiguously.

**Required correction:** define, for every receipt and result, canonical
unsigned payload bytes and `payload_id`, the signature envelope bytes and
`object_digest`, which identifier is stored in the Merkle log/coordinator and
which identifier revocation targets. A self identifier must be excluded from
its own hash preimage by an explicit schema rule. The receipt must bind the
result-template payload digest and fixed signer key; the completed signed
envelope must bind the receipt and payload ID without back-reference. Then
prove the graph acyclic and unique for each boundary.

## 2. Blocker — post-`H2` signing and normal retirement still have contradictory semantics

The dominant rule is now clear: the receipt sequence `H2` is logical issuance,
normal nonretroactive rotation after `H2` preserves it, only the fixed key may
later complete the signature, retroactive invalidation reaching `H2` withholds
it, and direct result revocation applies normally
([authority gates](../preimplementation-authority-gates):427–433,
508–522; [analysis firewall](../calibration-and-analysis):188–211).

Two live sentences contradict that rule. Gate G says delayed append is “never
permission to sign under a retired key” even though the only allowed key may
retire before delayed signing; the timing table says a “preverified signature
fixed at” the receipt sequence remains historical, although the revised design
fixes only the key and preimage there and may obtain the signature later
([authority gates](../preimplementation-authority-gates):427–433, 781–799).
G0's general rule that retired keys cannot issue at or after activation does
not distinguish logical issuance from later cryptographic completion.

**Required correction:** state one exact verifier/signer rule everywhere. If
later completion is retained, an authorized completion request for the stored
`H2` payload is permitted after normal retirement because issuance precedes
retirement; it is forbidden after retroactive invalidation reaching `H2` or a
direct revocation of the stable result ID. Replace all “preverified signature”
and “cannot sign under a retired key” wording, and specify operational retention
or escrow of retired private keys for outstanding completion. Otherwise move
the signature into the `H2` transaction.

## 3. Blocker — crash/retry/concurrency states are not total in the declared machines

The generic coordinator claims its **only** progression is
`unleased -> leased -> consumed -> completed`, but prose later requires
`leased -> abandoned -> fresh leased` and `consumed -> terminal failed`
([authority gates](../preimplementation-authority-gates):461–523). The
commitment machine likewise declares only
`unclaimed -> consumed -> completed`, then introduces terminal
`consumed-failed` when signing cannot finish
([authority gates](../preimplementation-authority-gates):578–613).

That leaves no formal answer for an expiry racing explicit abandonment and
consume, a late response from an abandoned lease, an ambiguous transaction
followed by a retry, or repeated queries of a terminal signing failure. The
prose states the intended outcomes, but they are not transitions in the
machines that are said to be exhaustive. G3 also requires a
“boundary-specific unconsumed `LatestHeadLease`” while reopening a capability,
although a completed capability necessarily binds a consumed `scope_mint`
lease/use receipt ([authority gates](../preimplementation-authority-gates):532–550).

**Required correction:** publish the complete durable state tables, including
lease-attempt identity, `abandoned`, `consumed_failed`, allowed retry loops,
atomic guards and query results. Abandonment must CAS the active lease ID so it
cannot win concurrently with consumption. Clarify that a constructor verifies
the already consumed ancestor receipts and separately obtains the current
boundary's as-yet-unconsumed lease.

## 4. Blocker for `final_analysis` — the consume transaction does not explicitly durably freeze the report bytes

The final-analysis text freezes report bytes/digest, template and key before
the expected-head transaction, but the transaction is explicitly said to store
only the receipt-derived full release preimage/digest
([authority gates](../preimplementation-authority-gates):508–517;
[analysis firewall](../calibration-and-analysis):182–198;
[implementation sequence](../implementation-sequence):383–404). A release
preimage can bind a report digest without containing the report bytes. If the
process crashes after `H2` and before report append, recovery cannot reproduce
the exact report from a digest unless those bytes were durably captured in the
same issuance bundle. “Freeze” outside the transaction does not itself specify
durability.

The shared rule does require one atomic compare/receipt-append/result-store
operation, and `raw_start` additionally forbids a claim/log dual write. That is
adequate as an architectural assertion for the other fixed result preimages,
but the final-analysis bundle has this extra report object and must name it
explicitly.

**Required correction:** the one linearizable authority-store/WAL transaction
must atomically commit the coordinator's `consumed` row, receipt append, `H2`,
release key ID, exact report bytes/digest, release template, receipt-bound full
release payload/ID and every recovery locator. A committed transaction must be
self-sufficient for deterministic report/signature/release append; an
uncommitted transaction must leave none of those items authoritative.

# Exact boundary dispositions

| Boundary | Expected-head/currentness | Atomic result binding | Crash/retry and rotation | Disposition |
| --- | --- | --- | --- | --- |
| `scope_mint` | **Closed.** Consumption requires exact lease-inclusion head `H1` plus manifest, epochs and effective-revocation digest; any append yields no receipt/result and a fresh lease. | Structurally unique template/key binding, but blocked by Finding 1's undefined payload/object digest. | Blocked by Findings 2–3; G3's “unconsumed” ancestor wording must be corrected. | **NOT CLOSED.** |
| `run_commit` | **Closed.** Same exact-head rule is carried into Stage 10.75. | Exact field/domain/run preimage is bound, subject to Finding 1. | Blocked by Findings 2–3. | **NOT CLOSED.** |
| `raw_start` | **Closed at the claim boundary.** One commitment-keyed CAS plus receipt append/result-store is required; a losing subject leaves no use receipt or claim and an ambiguous commit is queried as consumed. | Exact winning subject/template/key is fixed, subject to Finding 1. | One-use failure policy is sound in prose, but `consumed_failed` and abandonment are absent from the declared machine. | **NOT CLOSED overall; claim race itself is closed.** |
| `raw_close` | **Closed.** Exact `RawManifest/v1` subject and unchanged `H1` view are required; intervening append yields no close receipt/result. | Close marker uniquely binds the manifest and start/close chain, subject to Finding 1. | Blocked by Findings 2–3. | **NOT CLOSED.** |
| `final_analysis` | **Closed.** The same transaction checks exact `H1` plus leased manifest/epochs/revocations and assigns logical issuance `H2`. | Report, release template and fixed key are logically bound; stable digest identity and durable report-byte capture remain open. | Signer failure, substitution, correction and report-only append are fail-closed in intent; rotation/revocation wording and terminal states are contradictory. | **NOT CLOSED.** |

# Final-analysis attack disposition

| Attack | Contract result |
| --- | --- |
| Any append between lease inclusion and consumption | Closed: CAS fails with zero receipt/result; same immutable subject needs a fresh lease and recomputed bundle. |
| Signer unavailable/fails after `H2` | Intended terminal consumed-failed with no report presentation or substitute key, but the terminal state is not in the formal machine. |
| Key substitution | Closed in intent: only the key fixed at `H2` may complete. |
| Normal rotation after `H2` | Intended to preserve logical issuance, but contradicted by the retired-key/preverified-signature wording in Finding 2. |
| Retroactive key invalidation reaching `H2` | Closed in intent: withhold under G5. |
| Direct release revocation | Semantics are correct in intent, but the revocable stable digest is undefined before delayed signing under Finding 1. |
| Report-only append | Closed in intent: immutable audit child only, never a current/completed presentation. Durable recovery of its exact bytes remains open under Finding 4. |
| Delayed report/release append | Idempotent completion only, not new authorization, conditional on Findings 1, 2 and 4. |
| Corrected analysis | Closed: new subject/report/release; raw dataset remains immutable. |

# Cross-document consistency and prior-review baseline

The revision successfully repairs the prior review's central lease-to-receipt
ambiguity. The parent plan, Gate G, architecture, analysis firewall and
implementation sequence now agree on `H0 -> H1 -> H2`, exact-head consumption,
zero receipt/result on any intervening append, and logical issuance at `H2`.
They also agree that `AnalysisReleaseRecord/v1`, not the report alone, is the
sole completed final-analysis result.

The remaining stale pre-signature language is localized but normative:
“preverified signature fixed at” `H2` and “never permission to sign under a
retired key.” The state-machine omissions and the G3 “unconsumed” wording are
also live cross-document implementation contradictions, not editorial polish.

# Integrity and review conditions

All six requested inputs were SHA-256-frozen before reading. Artifact comment
threads were checked; none were present. The inputs were rehashed before this
artifact was created and again afterward; every digest matched.

| Reviewed input | Pre-read and post-write SHA-256 |
| --- | --- |
| parent `index.md` | `27da56dbe5a7ea442b94e80efd6adcaca27ac3749e7e983f5b1c15efb4e33926` |
| `preimplementation-authority-gates/index.md` | `29033972178c8faa78c001e8868556ff0bf8ae825f31944c9e9af7479df1edc2` |
| `model-architecture/index.md` | `e5818d48c6e9fa5ade11ba73d4a7c9124f8b1828c3c7584eca19cc65e83f7938` |
| `calibration-and-analysis/index.md` | `ec534993054ce1f43e48808c4a20ab2fbd27fc4d2ecad2fe6447f113d6ef04e4` |
| `implementation-sequence/index.md` | `0be1e95434e876224ca3431afe387cd74824b1c5c1ea65e8736dc4ef687cabf4` |
| prior independent review | `079a0b8f92b5b12a8c85ef56c770fb2ec1370dfdf5d3cc0267116ac985bbebcb` |

Only this review artifact was created. No reviewed artifact, code, ticket or Git
state was modified.
