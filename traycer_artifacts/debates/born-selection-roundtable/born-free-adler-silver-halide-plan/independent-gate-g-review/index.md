---
title: "Independent Gate G authorization-contract review"
kind: review
---

# Strict disposition

| Question | Disposition |
| --- | --- |
| Gate G at plan-contract level | **PARTIALLY CLOSED** |
| Actual scope capability or run commitment valid now | **NO** |
| Conclusion-bearing physical modeling authorized now | **NO** |
| Bounded feasibility implementation safe to begin | **YES — only Phases I–II / Stages 0–10, with diagnostic/exploratory types and no physical ledger or verdict path** |

The revision closes the earlier architectural omission of an authenticity root
and an exact-run object: a pinned offline Ed25519 root authorizes roles, a scope
capability is explicitly not a run authorization, and a distinct signed,
single-use `RunCommitment` binds the run identity, domain and schedule. Gate G is
not fully closed because an implementer must still invent load-bearing bootstrap,
signer, checkpoint-freshness, recovery, signature-coverage and failure-routing
rules. These are contract gaps, not missing runtime keys or evidence.

# Findings in priority order

## 1. Blocker — the root-of-trust contract does not fully define its own bootstrap, authorized signers or recovery

Gate G pins an offline root fingerprint and says canonical trust-manifest bytes
are Ed25519-signed, but the manifest itself selects canonicalization, digest and
signature algorithms
([preimplementation-authority-gates](../preimplementation-authority-gates):284–292).
The verifier therefore needs a pre-manifest bootstrap encoding/version and
algorithm suite, plus explicit rejection of unknown or downgraded suites; those
rules cannot safely come only from the unverified object they are needed to
verify.

The manifest names issuer and reviewer keys, but not the scientific-owner keys
or owner roles whose signatures are mandatory at lines 294–299. It also does not
name the signer role/key for authority-store Merkle checkpoints or revocation-log
checkpoints, even though those signed checkpoints are relied on at lines 308–315
and 340–348. Consequently, a conforming implementer cannot determine which key
may authenticate an owner closure or checkpoint without adding policy.

Finally, “key validity, rotation and retirement rules” is only a field category,
not a lifecycle. The plan does not fix transition authorization, epoch/sequence
monotonicity, overlap, successor binding, retired-key verification, or recovery.
The stated response to offline-root compromise—root revocation and independent
re-closure (lines 301–304)—has no trusted way to install a successor after the
only pinned root is compromised. Closure requires one of: a pre-pinned recovery
root/threshold, an explicit out-of-band verifier-update ceremony, or a similarly
precise recovery anchor. The threat boundary may exclude root compromise, but
the contract must not claim an in-band “root revocation” that it cannot
authenticate.

**Required correction:** freeze the bootstrap wire format and algorithm suite in
the verifier; authorize scientific-owner and checkpoint-signer roles in the
root-signed manifest; define key-ID uniqueness and full rotation/retirement
transitions; and specify the root-recovery ceremony and what remains permanently
invalid after each compromise class.

## 2. Blocker — “latest trusted checkpoint” has no freshness, anti-rollback or anti-equivocation rule

A signed Merkle checkpoint proves membership in one tree view. It does not prove
that the view is current, is an extension of the verifier's last view, or is the
only view. Gate G repeatedly requires the “latest trusted checkpoint”
([preimplementation-authority-gates](../preimplementation-authority-gates):313–315,
340–348), while the trust manifest carries checkpoint values and itself lives in
the logged object store. No rule defines:

- log identity, tree size, previous-checkpoint/consistency proof and checkpoint
signer;
- a monotonic trusted state or external witness by which a raw or analysis
process rejects an older valid manifest/checkpoint;
- fork/split-view detection, reconciliation or terminal failure;
- maximum revocation age, clock/sequence authority, or fail-closed behavior when
the newest checkpoint is unavailable;
- the non-circular order by which a root-signed trust manifest names a checkpoint
while the manifest object is itself logged.

This leaves a realistic rollback: replay an old, correctly signed trust manifest,
store checkpoint and revocation checkpoint from before a key/object revocation.
All listed signatures and inclusion proofs can pass. Mutation-testing a “stale
checkpoint” does not define how the verifier knows it is stale.

The filesystem rule also stops one step short of a TOCTOU contract. Rejecting a
symlink/nonregular final file and recomputing its digest (lines 313–318) does not
say that all path components are resolved from a trusted directory descriptor,
that no-follow/open and `fstat` apply to the same descriptor, or that the exact
verified bytes—not a reopened pathname—are consumed. A rename/swap between check
and use remains implementation-dependent.

**Required correction:** define signed checkpoint authority and consistent-
extension verification; persist or witness a monotonic last-seen state; specify
fork, rollback, unavailable and over-age handling as fail-closed; resolve the
manifest/checkpoint bootstrap order; and require descriptor-based no-follow
resolution, digesting and consumption of the same opened regular file.

## 3. High — scientific closure signatures do not expressly cover every load-bearing gate fact

The revision correctly requires a distinct authorized reviewer for each allowed
gate/scope and rejects self-consistent unsigned packets. However, the capability
payload expressly binds each gate record's source, evidence, decision-rule and
review digests, but not its conformance-result digest
([preimplementation-authority-gates](../preimplementation-authority-gates):322–330).
G1 says the issuer “verifies” conformance digests; Stage 10.5 does not list them
among the digests recomputed at minting
([implementation-sequence](../implementation-sequence):244–260). Neither passage
unequivocally says that the scientific-owner and reviewer signatures cover the
canonical gate ID, exact requested scope/profile, closure decision, evidence
digest, conformance digest, decision-rule digest and review digest together.

Without that coverage, a valid signature over one closure context can be paired
with a different conformance object or scope and still leave room for an
implementer-defined check. The missing scientific-owner authorization in Finding
1 compounds this gap.

**Required correction:** define one canonical `GateClosureRecord` signed in full
by the authorized owner and distinct gate/scope-authorized reviewer. It must bind
gate ID, profile/scope, decision, source, evidence, conformance, decision rule,
review, schema/version, trust epoch and validity sequence. The capability must
bind the digest of each complete signed record and an exhaustive gate-to-record
map. Make clear that signatures establish authorized approval, not the scientific
truth of malicious or mistaken evidence.

## 4. High — the exact-run contract still leaves physical inputs and atomic-claim durability implicit

The new `RunCommitment` is a real improvement: it binds capability, run ID,
output namespace, physical master identity, stochastic/replicate identities,
resource limits, a domain proof and single-use consumption
([preimplementation-authority-gates](../preimplementation-authority-gates):350–369).
But the supposedly complete real-field manifest enumerates positions, amplitudes,
phases, durations, temperatures, dark delays, controls and processing. It does
not expressly bind carrier frequency/wavelength, propagation vectors/beam
geometry, polarization, real waveform/envelope/coherence parameters, or the
canonical field-manifest/schema digest. Those inputs are authoritative elsewhere
([model-architecture](../model-architecture):6–30), and the planned wavelength
and polarization controls can change both physics and certified-domain validity.

Stage 11 also says to “predeclare” inputs after Stage 10.75 has already frozen and
signed them ([implementation-sequence](../implementation-sequence):265–289).
The only safe interpretation is that Stage 11 loads the exact committed bytes
and refuses any regenerated or reselected schedule; the contract should say so.

“Atomic append-only single-use claim” is directionally correct, but durability
and concurrency are load-bearing. The plan does not require a linearizable,
durable compare-and-append keyed by commitment digest, define which one of two
concurrent starters wins, or state that success is returned only after the claim
is durably recoverable. Crash/no-resume behavior is specified after a successful
claim, but the crash boundary during claim persistence is not.

**Required correction:** bind a complete versioned `FieldManifest`/schedule
digest that exhaustively includes every raw public input; require Stage 11 to
consume those exact committed bytes; define the domain-proof verifier and bound
validation record; and make the claim a durable linearizable transition in the
authoritative consumption log. Exactly one concurrent claimant may succeed;
ambiguous persistence must consume the commitment fail-closed, and no loser may
consume a key or create a directory.

## 5. High — revocation effect and terminal-status precedence are incomplete and inconsistent across stages

Root-signed append-only revocations now distinguish normal retirement from
retroactive invalidation, and final analysis rechecks revocation state. The
remaining lifecycle cases are not settled:

- a commitment issued before normal retirement but started after the effective
sequence;
- a run claimed before retirement but closed after it;
- later analysis of a nonretroactively retired key/object;
- revocation of a gate/evidence/review object versus the scope capability versus
the run commitment itself;
- revocation-check unavailability or a checkpoint beyond its allowed freshness.

Status routing conflicts. Gate G says every retroactively invalidated later
analysis emits `authority_capability_invalid`, even when the revoked object is a
run commitment ([preimplementation-authority-gates](../preimplementation-authority-gates):340–369).
Stage 10.75 groups a revoked issuer with commitment failures and exits
`run_commitment_invalid` ([implementation-sequence](../implementation-sequence):265–280),
while the global stop rules route trust-chain/revocation failure to
`authority_capability_invalid` (lines 355–364). A caller cannot deterministically
choose the required result when both layers fail.

**Required correction:** provide a revocation matrix by target, effective
sequence, retroactivity, issuance/claim/close/analysis time and availability;
then define status precedence. A natural split is trust/gate/capability failure
to `authority_capability_invalid` and an otherwise valid authority chain with a
missing, mismatched, consumed or specifically revoked run object to
`run_commitment_invalid`, but the plan must settle it.

## 6. Medium — the threat model overstates tamper resistance and omits signer/evidence compromise and denial of service

The explicit exclusion of offline-root, issuer-host and OS compromise is useful.
Within that boundary, the intended contract can prevent unsigned caller-built
records, wrong roles/scopes, changed bound bytes, broad-capability substitution,
commitment replay, and comparator feedback into raw generation. It cannot by
cryptography alone prevent:

- a compromised or colluding scientific owner/reviewer from approving false
evidence;
- a malicious but internally valid scientific dataset or conformance result;
- compromise of a checkpoint signer unless that role/lifecycle is defined;
- denial of service by withholding a current store/revocation checkpoint;
- rollback or equivocation until Finding 2 is fixed.

Store tampering is therefore detected only for changed bytes under a sufficiently
fresh, non-equivocating checkpoint; the present unconditional claim at
[preimplementation-authority-gates](../preimplementation-authority-gates):301–304
is too broad. Availability should fail closed, not be described as prevented.

# What the revision does close

- A scope capability is exact, exhaustive, issuer-signed and cannot silently
downgrade a developed-film request to latent-cluster scope.
- A broad domain capability is expressly insufficient to start a physical run.
- Each run has a distinct commitment binding capability digest, run ID, output
namespace, physical master, stochastic namespace, replicates and resources.
- Changed/out-of-domain schedules, stale handles, capability/commitment replay,
crash reuse and wrong-scope use are named failure cases.
- The commitment is claimed before key use or directory creation; a successful
claim is single-use; a crash is nonresumable; and the close marker binds both
authority digests and the claim sequence.
- Raw generation and final analysis remain isolated, and later analysis rechecks
the committed authority and current revocation state.

These decisions are strong enough to retain rather than redesign. They are not
enough to close Gate G until the blockers above receive exact rules.

# Cross-document and mutation-case adjudication

The parent plan, Gate G, architecture and phase boundaries consistently say that
an exact commitment—not a capability alone—is required for Stage 11. The main
cross-document defects are the Stage-11 “predeclare” wording and the revoked-
issuer/status conflict in Finding 5.

The mutation list is broad, but tests cannot repair missing oracles. Before Gate
G can close, it must add contract-defined expected results for:

1. an old but correctly signed manifest/checkpoint after a newer one was seen;
2. two valid checkpoints of the same log size with different roots;
3. unavailable/over-age revocation state;
4. trust-manifest algorithm/canonicalization downgrade;
5. unauthorized scientific-owner or checkpoint-signer key;
6. omitted or swapped per-gate conformance digest;
7. changed wavelength, polarization, geometry, waveform or coherence control;
8. two concurrent claims and a crash during durable claim persistence;
9. nonretroactive retirement at issuance, claim, close and later-analysis
 boundaries;
10. revocation of each object class with exact status precedence.

# Permitted implementation boundary

Phases I–II / Stages 0–10 and cost-ladder items 1–6 may begin now only as
diagnostic or exploratory feasibility work. This includes schema design,
test-key trust/store prototypes, mutation fixtures, analytic passive-response
work, candidate transfer fixtures, evidence inventory, identifiability analysis
and feasibility/cost measurement, provided those types cannot serialize a
physical ledger or verdict.

Actual Phase-III authority activation is not permitted: no Stage-10.5 scope
capability or Stage-10.75 run commitment may be accepted as physically valid.
Phase IV / Stages 11–14 and cost-ladder items 7–8 remain unauthorized as a
conclusion-bearing path. No actual material, calibration, solver, scientific
closure, store, revocation, capability or run-commitment evidence is supplied by
these plan documents.

# Preserved nonclaims

- No Born-rule or single-photon-selection derivation.
- No claim that PFG-01 contains a self-sustained or injection-lockable Adler
oscillator.
- No claim that a kinetic transfer surrogate is a microscopic derivation.
- No physical latent-cluster claim without independent F1 authority.
- No developability, density, visibility or classical-recording conclusion
without F2 and the exact developed-film scope.
- No claim that signatures make scientific evidence true or protect against
compromised root, issuer host, OS, owner or reviewer principals.
- No claim that current evidence, keys, trust store, checkpoints, revocations,
capabilities or run commitments exist.
- No inference from one batch, exposure or process to a unique mechanism or an
uncalibrated domain.

# Hash and comment integrity

All six inputs below were SHA-256-frozen before any input was read and rechecked
after the review. Every digest was unchanged. No artifact comment threads were
present on any reviewed input.

| Reviewed input | SHA-256 |
| --- | --- |
| `preimplementation-authority-gates/index.md` | `1179843d8e2fb82aabc3d3b1c18bd777ba6ed1b99e554c4837912f852bcfad57` |
| `implementation-sequence/index.md` | `a0ad8c316ae864bd327896e096aa3c4c8cc6eb9cbb71c941071d536d601b5f81` |
| `model-architecture/index.md` | `e9b111c8b15d42e4819b43afbe254ab09eadbe830e876a1f24f507b445c336c9` |
| `calibration-and-analysis/index.md` | `9167df3f9b5a9744868e3ec9d48c03d9bc87ecfd78bb69eeb256066c51572edc` |
| parent `index.md` | `92287045dde8db5cb473652e09b2f31aa3336a48f05babb65909095dfbad01bd` |
| `independent-passive-closure-review/index.md` | `0e2a99d9502458be03864c2c05ff823f2f89371f7c08f2e526d279c5ee8de2ff` |

Only this review artifact was created. No plan, prior review, code, ticket, Git
state or unrelated file was edited.
