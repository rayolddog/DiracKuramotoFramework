---
title: "Sprint 01 evaluation — round 2"
kind: review
---

# Sprint 01 evaluation — round 2

## Verdicts

| Verdict | Result |
| --- | --- |
| Contract | **FAIL** |
| Sprint 1 addressable rubric slices | **FAIL** |
| Deferred Sprint 2–3 slices | **UNRESOLVED**, unchanged |

No overall 90/100 score is computed at Sprint 1.

The seven mandatory commands all produce the expected exits, and the ordinary round-1 attacks now fail on their original forms. Adversarial variants through the same public module surfaces still forge authority, bypass the preregistered claim gate, inject a comparator after raw-view construction, accept non-faithful typed replays, and produce green runner output while substantive checks are skipped. Those are contract failures and trigger the rubric's automatic-failure rules for claim inflation, comparator leakage, and mutable/forgeable authority.

Clean manifest root captured independently before mutation:

```text
751b8245df8b9c814934bee6d8873f17359628b0696812100635ccd4ed0346d7
```

## Mandatory command evidence

| Command | Independent result |
| --- | --- |
| `python3 -m pytest -q born_selection_equilibrium_fixture/tests` | exit 0; **217 passed in 4.00s** |
| `python3 -m born_selection_equilibrium_fixture.verify` | exit 0; **217/217** |
| `python3 -W error -m born_selection_equilibrium_fixture.verify` | exit 0; zero warnings |
| `python3 born_selection_equilibrium_fixture/verify.py` | exit 0; **217/217** |
| `python3 -m born_selection_equilibrium_fixture.verify --prove-failure-exit` | expected exit 1; planted manifest-root mismatch named |
| `python3 -m py_compile born_selection_equilibrium_fixture/*.py` | exit 0 |
| `python3 -m compileall -q born_selection_equilibrium_fixture` | exit 0 |

Supplemental evidence: unknown flag exits 2; pytest collects 217 IDs; `--json` is byte-identical under `PYTHONHASHSEED=1` and `9999` with SHA-256 `5cce6b1ea51b4e74f0a01ef5931125f1c4e7c94acaa70780bda538a38e0e8a85`.

## Round-1 replay status

Independently replayed outside the registered checks:

- The five original direct constructors now raise exact `AuthorityError` when called without the mint argument.
- Caller prose in the old result-detail position raises `AuthorityError`.
- Plain and nested list/dict alias mutation no longer changes an ordinary `RawStageView`, measure, record, or lifecycle snapshot.
- `FrozenInputSet.close()` no longer accepts another manifest.
- The happy-path typed round-trip returns the exact original type with equality and digest equality.
- NFC-equal row keys raise `MeasureError`; lone surrogates raise `SerializationError`.
- `BSEF_CHILD=1 python3 -m born_selection_equilibrium_fixture.verify` exits 1.

The repairs are therefore real but incomplete, rather than absent.

## Findings

### 1. Critical — the exported mint still forges the entire authority chain

`_internal.py` places `MINT` in `__all__`, binds it as a module-global object, and every authority constructor accepts it through a caller-visible `_mint` parameter. Importing that exported value allowed construction of an arbitrary-root `ManifestAuthoritative`, `DependencyGate`, `ClaimGate`, `FixtureRunPermit`, and `Closed`, followed by a serialized `Supported` result:

```text
from born_selection_equilibrium_fixture._internal import MINT
...construct each token with root = "f" * 64 and _mint = MINT...
Supported(...).serialize() -> 762 bytes
```

This is the round-1 authority-forgery attack with one extra imported argument. An exported shared sentinel is not transition custody. Relevant sites: `_internal.py:33,36-52`; `provenance.py:197-212`; `dependency.py:132-166`; `freeze.py:107-123`; `authority.py:27-45`.

**Repair obligation:** eliminate any importable/exported capability that satisfies authority constructors, remove the mint parameter from caller-visible construction paths, and make exact authority types constructible only inside the successful transition that earns them. Add an attack that imports every runtime module and uses all names exposed through `__all__`; none may mint an authority value or serialize `Supported` without a real manifest verification, dependency reconciliation, claim closure, and lifecycle closure.

### 2. Critical — result claims are not bound to either the claim gate or the result kind

Using only legitimate public transitions, a claim gate fixed to the single claim `equivariance_not_tested` produced a valid permit and lifecycle. That permit then emitted:

```text
Supported(... claim=conditional_outcome_compatibility_supported_for_frozen_domain ...)
```

even though the claim was absent from `permit.claim_gate.claims`. The same permit emitted `equivariance_tested_nonphysical_fixture_same_space_flow_invariant_for_frozen_domain` without any `SameSpaceFlowContract`. Separately, both `Refused` and `Failed` accepted the positive compatibility-supported claim and a matching positive detail code.

`Supported.__init__` checks the permit and lifecycle roots but never checks the emitted claim or attestations against the permit's preregistered claim set, and `Result.__init__` has no result-kind/claim/detail compatibility matrix. Relevant sites: `results.py:211-234,308-346`; `authority.py:55-86`.

This breaks the fixture-scoped claim gate, the separate-flow-contract requirement, and the claimed disjoint four-way result algebra. Exact Python classes are disjoint while their meanings are not.

**Repair obligation:** enforce a literal, reviewed result-kind × claim × detail-code matrix; require every emitted claim and attestation to have been fixed in the permit's `ClaimGate`; restrict `Supported` to the compatibility-supported claim; and make equivariance claims obtainable only from an API whose required input is the exact `SameSpaceFlowContract`. Add negative tests for every cross-kind claim, every mismatched detail code, claims/attestations absent from the gate, and both equivariance claims without a flow contract.

### 3. High — typed replay accepts stale and relabeled schemas, and its decoder registry is mutable

`schema_io` checks field *names* but does not validate or preserve several field relationships:

- an `InputRecord` payload with `schema_version="stale/schema"` reconstructs successfully as the current schema;
- a `Manifest` payload with a stale top-level schema version reconstructs to the clean manifest and root;
- changing the outer manifest record key from `upstream` to `renamed_outer_key` while leaving the inner `record_id` unchanged reconstructs to the original `('consumer', 'upstream')` manifest and clean root;
- `SCHEMA_TYPES` is a public mutable dictionary. Replacing its `Manifest` entry with `lambda payload: clean_manifest` makes `decode_typed(Manifest, canonical_bytes({"bogus":1}))` return the clean exact type and then `ManifestAuthoritative` against the held root.

Relevant sites: `schema_io.py:40,43-54,104-133,167-197`.

The replay path therefore has multiple byte representations for one schema value and can be redirected before the exact-type check. This contradicts PRV-07/10, CAN-20's repaired meaning, and the strict authority-bearing replay rule.

**Repair obligation:** make replay dispatch immutable and internal; validate every serialized schema-version field; require outer manifest keys to equal inner normalized `record_id` values; require auxiliary content keys to match the manifest record-ID set exactly; and after reconstruction require the reconstructed schema payload to re-emit byte-for-byte as the supplied schema payload. Add stale-version, outer/inner relabel, missing/extra auxiliary-content, mutable-dispatch, and reconstructed-byte-mismatch attacks for both records and manifests.

### 4. High — deep freezing trusts attacker-controlled `__module__`, reopening the comparator TOCTOU leak

`freeze_value` and `_freeze_field` treat any object whose type module starts with `born_selection_equilibrium_fixture` as an already-immutable harness value. A caller controls `type(obj).__module__`:

```text
class Box: pass
Box.__module__ = "born_selection_equilibrium_fixture.user_payload"
box.items = []
view = RawStageView(box)
box.items.append(comparator)
reaches_comparator(view) -> True
view.raw_content() is box -> True
```

No private state or `object.__setattr__` is used. The same prefix trust is the common deep-immutability mechanism for public value fields. Relevant sites: `_internal.py:117-145`; `measures.py:61-67`; `isolation.py:147-166`.

**Repair obligation:** remove module-name trust. Use exact known immutable types or recursively snapshot only a closed data vocabulary, and reject unknown objects at the raw-view boundary. Add module-spoofed mutable objects at the top level and inside containers, plus mutation after construction, to every alias/immutability regression family.

### 5. High — externally supplied runner guards still manufacture a green run

Two independent caller-controlled paths skip substantive runner checks while reporting success:

```text
python3 -m born_selection_equilibrium_fixture.verify --internal-recursion-guard
-> exit 0, 217/217 passed, 10 skipped as a spawned child, 0.06s

BSEF_CHILD=1 python3 -m pytest -q born_selection_equilibrium_fixture/tests
-> exit 0, 217 passed in 0.20s
```

The parser marks any caller providing `--internal-recursion-guard` as authorized. The environment-variable failure is enforced only by `verify.main`, which pytest never calls; `ATK-21` also returns immediately in child mode. Relevant sites: `verify.py:93-104,110-148`; `tests/harness.py:56-105`; `tests/checks_runner.py:56-79` and every `in_child_process()` early return.

This is the round-1 runner bypass through the remaining invocation surfaces. RUN-01/03/04/05/06/07/10/12/13/14 can still be green without running.

**Repair obligation:** no flag or environment value supplied by an external caller may authorize skipped checks. The public parser must reject the internal marker, and both the bare runner and pytest entry point must fail if any substantive check is skipped outside a parent-owned child channel. Add exact attacks for the internal flag in module and direct-script modes and for `BSEF_CHILD=1` under both runners; all must be non-zero and must never print/collect a wholly green result.

## Addressable rubric status

| Criterion | Sprint 1 status | Evidence |
| --- | --- | --- |
| Scientific boundary integrity | **FAIL** | Exported mint forges `Supported`; equivariance claim is emitted without its required flow contract; claim gate does not bind output. |
| Circularity detection — declared-label slice | **FAIL** | A legitimately closed claim gate can be bypassed by result emission, and its token can also be forged. |
| Measure-space correctness | **FAIL** | Same-space invariance claims remain reachable without `SameSpaceFlowContract`. Arithmetic checks pass but the authority boundary around their meaning does not. |
| Structural isolation and provenance | **FAIL** | Comparator TOCTOU through module spoof; stale/relabelled/non-faithful typed replay; mutable decoder dispatch; exported authority mint. |
| Discriminating tests | **FAIL** | All 217 checks are green while each independent attack above succeeds. |
| Reproducibility and numerical discipline | **FAIL** | Ordinary commands and hash determinism pass, but two caller-controlled skip paths produce green runs without the claimed checks. |
| Clarity and maintainability | **FAIL** | Serialized result kinds can contradict their claims; typed replay's name and tests materially overstate its fidelity. |

Deferred import firewall, fixture mechanisms, semantic circularity, blinded holdouts, equivalence margins, nonequilibrium response, negative controls, and Sprint 3 tolerance policy remain **UNRESOLVED**.
