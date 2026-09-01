---
title: "Sprint 01 evaluation — round 1"
kind: review
---

# Sprint 01 evaluation — round 1

## Verdicts

| Verdict | Result |
| --- | --- |
| Contract | **FAIL** |
| Sprint 1 addressable rubric slices | **FAIL** |
| Deferred rubric slices | **UNRESOLVED**, unchanged |

The mandatory invocation matrix passes, including 196 pytest checks, the bare and warning-clean runners, direct-script mode, the intentional exit-1 path, exit-2 usage handling, compilation, and hash-seed determinism. Independent public-API attacks nevertheless invalidate multiple green checks and trigger the rubric's automatic-failure rules for claim inflation and mutable authority records.

Clean manifest root captured independently before attacks:

```text
751b8245df8b9c814934bee6d8873f17359628b0696812100635ccd4ed0346d7
```

## Findings

### 1. Critical — authority tokens and a `Supported` result are publicly mintable

`ManifestAuthoritative`, `DependencyGate`, `ClaimGate`, `Closed`, and `FixtureRunPermit` all have caller-accessible constructors. `authorize_fixture_run` verifies exact types and matching root strings, but those exact objects can be constructed directly without a manifest, dependency reconciliation, claim-gate closure, or lifecycle transition. `Supported` is weaker still: it accepts any gate-shaped object whose `is_closed` attribute is truthy.

Evidence from the public API:

```text
verdict = ManifestAuthoritative("forged-root")
dep = DependencyGate("forged-root", ())
claim = ClaimGate("forged-root", (<permitted claim string>,))
authorize_fixture_run(verdict, dep, claim)
→ FixtureRunPermit("forged-root", ...)

Closed({"raw":"never-ran"}, "forged-digest") + those tokens
→ Supported serializes successfully
```

This contradicts DEP-14…16, RES-04, LIF-06, and the fixture-scoped authority boundary. Relevant construction/consumption sites: `provenance.py:196-210`, `dependency.py:131-167`, `freeze.py:73-95` and `98-115`, `authority.py:26-82`, `results.py:159-184`.

Required outcome: authority-bearing values must only be created by successful verification/closure transitions, must be bound to the same manifest root, and consumers must require the exact verified permit/token rather than caller-shaped objects or truthy attributes. Add direct-constructor, dummy-gate, cross-root, and forged-closed attacks.

### 2. Critical — result `detail` is an unrestricted serialized claim channel

`Result.__init__` validates only the enum-valued `claim`; it stores caller text in `detail` unchanged and serializes it. A forged `Supported` was emitted with:

```json
"detail":"the Born rule is derived and physical selection is demonstrated"
```

The fixed `model_class` and `physical_authority` fields remain adjacent, but they do not erase the affirmative claim. RES-15 scans package prose and one planted sentence; it is never enforced on emitted result content. This is claim inflation in a serialized field and therefore an automatic rubric failure. Relevant code: `results.py:71-109`, `results.py:159-196`, `claims.py:62-86`; the weak check is `tests/checks_policy.py:406-420`.

Required outcome: result-emitting paths must not accept arbitrary authority-shaped prose. Use closed reason/detail codes with fixed templates, or enforce a construction-time output policy that cannot be bypassed by caller text or negation-marker tricks. Add attacks against every result type and deserialization.

### 3. High — raw/comparator isolation is vulnerable to post-construction alias mutation

`RawStageView` checks reachability once, stores the caller's raw object by reference, and returns that same object from `raw_content()`. This succeeds:

```text
raw = []
view = RawStageView(raw)       # clean at construction
raw.append(comparator)         # mutate retained alias
reaches_comparator(view, sentinels) → True
view.raw_content()[0] is comparator → True
```

CMP-03 only tests a clean immutable-looking literal and therefore passes while the gate is breakable. Relevant code: `isolation.py:144-159`; check: `tests/checks_provenance.py:299-302`.

Required outcome: snapshot raw content into a recursively immutable representation, return only defensive immutable content, and prove that mutation of every caller-held alias after construction cannot introduce comparator data.

### 4. High — public value types are shallow wrappers around mutable state

`_Immutable` blocks attribute assignment but does not recursively freeze stored values. Measures expose mutable `weights`; kernels/flows expose nested row dictionaries; manifests expose a mutable `records` dictionary; `InputRecord.content` is public and mutable; lifecycle values alias the caller's payload. Demonstrated effects:

```text
measure.weights["x"] = Fraction(1)  # succeeds; now sums to 3/2
frozen = Draft(payload).freeze(); mutate(payload)
→ frozen.digest changes while frozen.frozen_digest stays stale
manifest.records["upstream"].content["payload"] = "changed"  # no use() call
```

This invalidates LIF-12/13 and also disproves DEP-05's claim that content is readable only through `FrozenInputSet`. The defensive accessor is shallow for tuples and other nested structures. Relevant code: `measures.py:60-113` and weight/row constructors, `provenance.py:66-152` and `235+`, `freeze.py:47-77`, `dependency.py:170-216`. Weak checks: `tests/checks_provenance.py:468-493` and `699-704`.

`FrozenInputSet` also accepts a different manifest at `close()`: reads taken from manifest A can produce a gate bound to manifest B when record IDs align. Independent evidence returned `roots_differ=True` and `gate_bound_to_b=True`.

Required outcome: recursively copy/freeze all public value state; remove direct content access outside the mediator; preserve stable digests/hashes; and bind `FrozenInputSet` permanently to the manifest/root it was created from.

### 5. High — CAN-20 is not a schema round-trip

No schema type shown in CAN-20 is reconstructed. The test calls each object's private `_payload()`, encodes it, decodes to a plain `dict`, and only checks that re-encoding the dictionary yields the same bytes. `Manifest` has no `from_canonical`; the observed decoded type is `dict`.

This does not satisfy “every schema type round-trips,” does not exercise constructor invariants during replay, and leaves authority-bearing manifest replay unavailable. Relevant check: `tests/checks_canonical.py:184-202`; generic decoder: `canonical.py:198-234`.

Required outcome: exact-type schema reconstruction with strict field sets and constructor revalidation. The round-trip assertion must be `type(decoded) is type(original)`, equality, and digest equality for every schema type, with an out-of-band root required before an authority-bearing reconstruction becomes authoritative.

### 6. Medium — additional validation and runner false positives

- `_check_rows` NFC-normalizes a row key and overwrites an earlier NFC-equal row instead of rejecting it. A kernel built with `"é"` and `"e\u0301"` silently contains one row (`measures.py:311-331`).
- `from_canonical(b'"\\ud800"')` leaks `UnicodeEncodeError` instead of the exact `SerializationError` required by the error contract.
- Externally setting `BSEF_CHILD=1` makes RUN-01/03/04/05/06/07/10/12/13/14 return successfully without performing their claimed checks. The recursion guard is therefore a caller-controlled self-test bypass, not merely internal recursion state (`tests/harness.py:39-50`, `tests/checks_runner.py`).

## Rubric status

| Criterion | Sprint 1 status | Evidence |
| --- | --- | --- |
| Scientific boundary integrity | **FAIL** | Serialized free-text claim inflation; forged `Supported` |
| Circularity detection — declared-label slice | **FAIL** | Dependency-gate evidence can be minted and cross-manifest-laundered |
| Measure-space correctness | **FAIL** | Normalized measures/rows remain publicly mutable; NFC row duplicates collapse |
| Structural isolation and provenance | **FAIL** | Comparator TOCTOU leak, mutable records/content, forgeable authority tokens, no typed replay |
| Discriminating tests | **FAIL** | 196/196 green while the planted public attacks succeed |
| Reproducibility and numerical discipline | **PASS with open medium finding** | Mandatory commands deterministic; external recursion-guard bypass remains |
| Clarity and maintainability | **FAIL** | CAN-20's title materially overstates what it tests |

No overall 90/100 score is computed. Deferred Sprint 2–3 slices remain UNRESOLVED.
