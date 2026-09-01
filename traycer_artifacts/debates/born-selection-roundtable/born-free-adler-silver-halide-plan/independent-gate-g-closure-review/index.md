---
title: "Independent Gate G closure re-review"
kind: review
---

# Strict verdict

| Question | Verdict |
| --- | --- |
| Gate G plan-contract closure | **PARTIALLY CLOSED** — five of the six prior findings are fully or substantially repaired, but an accepted witnessed head can still be stale while younger than 24 hours, and the revocation target/effect table is not exhaustive. |
| Bounded Phases I–II feasibility work | **YES** — Stages 0–10 and cost items 1–6 may proceed only through diagnostic/exploratory/conformance types that cannot serialize physical ledgers or verdicts. |
| Stage 10.5 scope closure now | **NO** — the plan contract still has the current-head/revocation defects below, and the reviewed corpus supplies no actual closed scientific records, keys, services, store, witnessed head or scope capability. |
| Stage 11+ conclusion-bearing work now | **NO** — no valid capability or run commitment exists, and the authority contract is not yet fully closed. |

This is a plan-contract review, not an assertion that any authority, data, key,
store, witness, claim service, capability or commitment actually exists. The
revision is close, but “checkpoint younger than 24 hours” is not equivalent to
“latest checkpoint” or “contains every revocation already effective in wall
clock time.” That remaining distinction is sufficient to keep Gate G partially
closed.

# Six-finding closure adjudication

## 1. CLOSED — bootstrap, roles, lifecycle and root recovery

G0 now fixes deterministic CBOR, SHA-256, Ed25519, signed-object domain
separators, the root fingerprint and a two-of-three recovery threshold in the
compiled verifier. Unknown or negotiated suites refuse. The trust manifest
authorizes scientific-owner, gate/scope reviewer, issuer, checkpoint, witness,
revocation and claim-service roles; raw and analysis hold no private signing
keys. `TrustTransition` binds old and new manifests, epochs, activation and
retirements. `RecoveryTransition` binds a monotonic recovery epoch, successor
root and earliest invalid sequence; compromise of recovery/verifier/OS has an
explicit out-of-band boundary. These are implementable plan rules and close the
first prior finding.

The unresolved ability to replay an ancestor view shortly after a transition is
adjudicated under Findings 2 and 5; it is not a missing G0 anchor or lifecycle.

## 2. PARTIALLY CLOSED — witnessed consistency is strong, but freshness does not prove currentness

G2 now supplies the log identity, genesis bootstrap, signed checkpoint shape,
previous digest, consistency proof, persisted last-seen state, two independent
witness signatures, fork/equivocation rules, a 24-hour age ceiling, fail-closed
availability and descriptor-pinned same-byte consumption. It closes the prior
TOCTOU, unwitnessed-log, same-size-fork, nonextension and unbounded-age gaps.

One blocker remains. Consider this valid sequence:

1. At 10:00, witnesses sign checkpoint `C100`; a fresh verifier has persisted
 only `C090`.
2. At 10:05, a revocation or recovery transition is appended and a newer valid
 checkpoint `C101` exists.
3. At 10:10, an attacker supplies `C100`, its valid consistency proof from
 `C090`, the old active manifest, and all objects needed for a run.
4. `C100` is monotonic relative to the verifier's local state, witnessed and
 less than 24 hours old. Nothing in G2 requires an authenticated query proving
 that no later head exists. The verifier can accept it and miss the revocation
 in `C101`.

This is an ancestor replay, not a fork, broken proof, lower sequence or over-age
view. Local last-seen persistence prevents backward movement after a verifier
has observed `C101`; it cannot reveal a newer head the verifier has never seen.
The same gap applies to selecting the active trust/recovery manifest: the
bootstrap order begins with a root-signed manifest, but the accepted head must
also prove which manifest/transition is active at that head.

Therefore a stale, self-consistent, correctly signed packet can still reach the
Stage-11 claim boundary during the permitted age window. Forged, partial,
mismatched and stale-below-last-seen packets cannot.

**Required correction:** choose and state one coherent semantic:

- For immediate revocation, require at raw start, raw close and analysis an
authenticated latest-head lease/status response, bound to the log ID, a
verifier nonce, trusted time and a short expiry, from a defined witness
quorum that tracks the current head. Require the accepted tree size/root to
equal or consistently extend each quorum response, and resolve the unique
active trust/recovery epoch and manifest from that head.
- Alternatively, explicitly accept a bounded revocation-propagation interval.
Then define activation/effect no earlier than a checkpoint-visibility
deadline, replace every “current” and “revocation before claim blocks” claim
with the bounded rule, and state that starts during the interval remain valid.

A 24-hour age check alone cannot support the present immediate-effect language.

## 3. CLOSED — complete signed gate and capability coverage

G1 defines one canonical record signed in full by an authorized scientific
owner and a distinct gate/scope reviewer. It covers schema/version, gate,
scope/profile, decision, sources, material/calibration/solver domain, evidence,
conformance, decision rules, independent review, trust/recovery epoch, validity
sequences and signer IDs. G3 binds an exhaustive gate-to-record map plus the
scope, source/executable, schema, material, calibration, solver and decision-rule
digests. Stage 10.5 recomputes the same fields and same bytes. Omitted,
duplicated, extra, swapped, unauthorized or wrong-scope records refuse.

The contract also says precisely what the signatures do not establish:
authenticated owner/reviewer approval is not scientific truth. This closes the
third prior finding.

## 4. CLOSED — exhaustive Stage-11 commitment and durable one-use claim

`FieldManifest/v1` now binds coordinate frame/units, beam positions and
geometry, propagation vectors, carrier/wavelength, polarization, real
amplitudes, waveform/envelope/coherence, phase/timing, exposures, temperature,
dark delays, controls and processing. The run commitment binds that exact
manifest plus capability, epochs/checkpoint, run/output/master identities,
source, material, calibration, solver/certificate, decision rules, stochastic
and replicate identities, resources and a field-by-field domain-validation
record. Stage 11 consumes the committed bytes without regeneration or
selection.

The claim service has an explicit durable linearizable
`unclaimed -> claimed` transition. Success follows recoverable persistence and
an append-logged signed receipt; exactly one concurrent starter wins; losers
touch neither keys nor directories; ambiguous crash state is consumed; claims
are never released. The close marker and final analysis reopen and bind the
entire chain. This closes the fourth prior finding at plan-contract level.

## 5. PARTIALLY CLOSED — precedence is exact; revocation effect is not yet exhaustive

G5 now gives deterministic precedence:

1. bootstrap/trust/role/checkpoint/store/gate/capability/revocation-state failure
 is `authority_capability_invalid`;
2. only after that layer passes, commitment/field/domain/claim failure is
 `run_commitment_invalid`;
3. only then may scientific outcomes be evaluated.

It also distinguishes normal retirement, pre/post-claim timing, completed runs,
retroactive invalidation and unavailable/rolled-back/equivocated state. That
closes the prior status-routing conflict.

Two contract gaps remain:

- “Nonretroactive object revocation before claim blocks start” is not enforced
during the within-age ancestor replay in Finding 2. The matrix must adopt the
chosen immediate or bounded-propagation semantic and define issuance, claim,
close and analysis against that same authority time/head.
- The revocation signer is expressly allowed to revoke scientific records,
capabilities, run commitments and claim-service objects, while G6 requires
attacks for “every object-class revocation” and the run chain also contains a
field manifest, domain-validation record and close marker. State exhaustively
which signed/stored object types are independently revocable. For each type
that is not, state which parent revocation invalidates it. Bind every target
row to its exact terminal status under the precedence above.

Until those rows are explicit, an implementer must invent revocation scope and
effect for some Stage-11 objects.

## 6. PARTIALLY CLOSED — the scientific-truth and DoS distinctions are correct, but one claim overstates stale-view detection

G1 and G6 correctly distinguish authenticated approval from true evidence and
say that colluding or mistaken owners/reviewers can approve false science. G6
also limits tamper detection to bound bytes and authenticated views, states that
availability loss fails closed rather than being prevented, and identifies
root/recovery, issuer, checkpoint, claim-service and OS compromise as outside
the guarantee. Those are the essential distinctions requested by the prior
finding.

The statement that the contract “rejects stale” or “detects stale” witnessed
views is still too broad: it rejects views older than the local last-seen state
or the 24-hour ceiling, but not the valid within-age ancestor in Finding 2.
Narrow the threat claim to exactly the implemented freshness guarantee, and add
witness and revocation-signer compromise explicitly to the named principal
boundary rather than relying only on the phrase “authorized services.” With
those edits, this finding closes.

# End-to-end pressure tests

| Flow or mutation | Result under the revised plan |
| --- | --- |
| Honest exact-scope flow | Bootstrap → active trust view → complete gate records → capability → exact field/domain/run objects → durable claim → Stage 11 → close → independent analysis is traceable and implementable once real authorities exist. |
| Self-consistent packet signed by attacker-controlled untrusted keys | Refuses at the pinned root/role chain before key use or directory creation. |
| Gate record with omitted/swapped conformance, decision, evidence or review | Refuses because both complete-record signatures and the exhaustive capability map bind these fields. |
| Valid capability with changed scope, executable, calibration, field schedule, wavelength, geometry, polarization, coherence, process or domain value | Refuses through capability/commitment digest and domain-record mismatch. |
| Reopened pathname swaps verified object after hashing | Refuses by descriptor-relative no-follow resolution and consumption of the same opened bytes. |
| Checkpoint below persisted last-seen state, same-size different root, broken consistency proof, unwitnessed or older than 24 hours | Refuses as `authority_capability_invalid`. |
| Correctly witnessed ancestor checkpoint younger than 24 hours but superseded by an unseen revocation/transition | **Can pass the written contract**; this is the remaining Stage-11 authorization route. |
| Two concurrent claims | Exactly one succeeds; every loser refuses without keys or output directory. |
| Crash or ambiguous response during claim | Commitment remains or is treated as consumed; retry requires a new commitment/run ID. |
| Valid authority chain but missing, mismatched, revoked or consumed run object | `run_commitment_invalid`. |
| Invalid trust/gate/capability layer plus invalid run object | `authority_capability_invalid` wins deterministically. |
| Authorized owners/reviewer approve malicious or mistaken evidence | Cryptographic validation can pass; this is authenticated approval, not proof of scientific truth, and is correctly outside the promised guarantee. |

Except for the within-age ancestor case, no self-consistent forged, partial,
replaced or mismatched authorization packet has a written route to physical
Stage 11. This statement is about the design contract; today there is no actual
physical path because no capability or commitment is supplied.

# Exact remaining actions

1. Choose immediate revocation or explicitly bounded propagation, then specify
 the latest-view/lease or activation-deadline protocol consistently in G2,
 G3, G5, Stage 10.5, Stage 11 and final analysis.
2. Require the accepted head to resolve the unique active trust/recovery epoch
 and manifest, preventing selection of an older root-signed manifest that is
 merely still cryptographically valid.
3. Add an exhaustive revocation-target matrix for every authority/run object,
 including an explicit parent-invalidation rule for intentionally
 non-revocable child objects and exact status precedence for every row.
4. Narrow the threat-model freshness claim and explicitly name witness and
 revocation-signer compromise in the principal-compromise boundary.
5. Re-run the required mutations for unseen within-age supersession, active-
 manifest selection and each object-class revocation. Then obtain a new cold
 plan-contract review.
6. Even after contract closure, separately create and independently validate
 the actual gate evidence, owner/reviewer records, keys, trust/recovery state,
 witnessed log, capability, field/domain record, run commitment and durable
 claim service before Stage 10.5 or Stage 11 can be declared operational.

# Preserved scientific and authority nonclaims

- No derivation of the Born rule or single-photon selection.
- No claim that PFG-01 contains a self-sustained or injection-lockable Adler
oscillator; Adler remains a separately pumped counterfactual with no physical
authority edge.
- No physical latent-cluster conclusion without F1 and no developed-film,
developability, density or visibility conclusion without F2 and the exact
developed-film scope.
- No claim that a kinetic surrogate is a microscopic transfer derivation.
- No claim that signatures make evidence true or defeat compromised authorized
principals, OS, recovery threshold, witnesses or services.
- No claim that current material evidence, authority records, keys, services,
store, checkpoints, capabilities or commitments exist.

# Input integrity and comments

Before any reviewed input was read, all seven inputs were SHA-256-frozen. Every
digest matched the supplied observed value. After adjudication, all seven were
rechecked and were unchanged. Artifact comment threads were listed before
adjudication; none were present.

| Reviewed input | Pre-read SHA-256 | Post-review SHA-256 |
| --- | --- | --- |
| parent `index.md` | `92e23d09450c1914cd9075397dc021f7c2b99ea63c4a4b63626a390321d03603` | `92e23d09450c1914cd9075397dc021f7c2b99ea63c4a4b63626a390321d03603` |
| `preimplementation-authority-gates/index.md` | `94c7c3e80ff415c618bfa186cc68f2d4d4c28935d568bcd7a707bff49c94c733` | `94c7c3e80ff415c618bfa186cc68f2d4d4c28935d568bcd7a707bff49c94c733` |
| `model-architecture/index.md` | `7319d14c511ffadb4e2b3a3f16ad2dfbc2ff213387d785c3e30cbfb4ac69f160` | `7319d14c511ffadb4e2b3a3f16ad2dfbc2ff213387d785c3e30cbfb4ac69f160` |
| `calibration-and-analysis/index.md` | `dc7b0e972d401f53114103300881e90c18689433852156459533930068e30cdd` | `dc7b0e972d401f53114103300881e90c18689433852156459533930068e30cdd` |
| `implementation-sequence/index.md` | `ae442c117e8a51a236155820abbf31b8e44616c81af054a2a574aa6390c21e30` | `ae442c117e8a51a236155820abbf31b8e44616c81af054a2a574aa6390c21e30` |
| `material-oscillator-evidence/index.md` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` | `f64ef52478c519ad5f6e6ac7ca49ed0c03e0dd6c45bfd14aef192cb5d539d00a` |
| prior `independent-gate-g-review/index.md` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` | `d5938027e890280fa8c9b6351b33dce2bccbdf376836765910d8b962d17071f4` |

Only this new review artifact was created. No reviewed artifact, code, ticket,
Git state or unrelated file was edited.
