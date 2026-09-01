---
title: "Evaluator critique — Sprint 01 contract proposal r1"
kind: review
---

# Evaluator critique — Sprint 01 contract proposal r1

**Verdict:** revise before implementation. The proposal is unusually concrete, but several checks presently prove less than their wording claims, and two sections contradict the actual Evaluator environment or each other.

## Blocking revisions

1. **The environment correction is not portable and is false on the Evaluator host (§0, C-073).** Here, both `python3` and `python3.12` resolve to Python 3.12.6 and both have pytest 9.0.2. The build-index pytest command succeeds. State the Generator-host difference separately, keep the build-index path mandatory on the Evaluator host, and add Generator-host Python 3.13 coverage as supplemental rather than replacing the approved path.
2. **The “stdlib-only across all `.py` files” requirement conflicts with C-083’s required `pytest.raises` usage (C-061, C-083).** Either tests import pytest, violating C-061 and preventing bare-Python verification from importing them, or they do not use `pytest.raises`. Use stdlib-only test code that pytest can collect, including an exact-exception helper based on `type(exc) is Expected`, or narrow C-061 explicitly to runtime modules and keep `verify.py` independent of pytest.
3. **The rehash attack stops one level too early (C-032, C-033, C-051).** Recomputing only a record digest while preserving the old manifest root is not a full rehash attack. Add tests that mutate/delete/relable content, recompute every nested digest and the manifest digest, then verify against a separately held expected root commitment. A deserialized manifest without an expected commitment must not be described as tamper-evident; either require the commitment or return a non-authoritative/unverified state.
4. **The dependency-edge direction contradicts `declared_downstream` (C-046).** If `A → B` means “A declares B as downstream,” contamination originating at a target-dependent C propagates from C to its downstream consumers, not backward from C to A. Define the edge meaning once, add a positive contamination chain and a reverse-direction negative control, and base closure on that definition.
5. **The comparator data gate can pass while the target remains reachable through the view object (C-042).** Blocking named target attributes is insufficient if `vars`, `repr`, `str`, iteration, mapping conversion, dataclass conversion, pickling, or canonical serialization exposes the payload—or if the raw view retains the comparator object internally. Require that the raw-stage view contain no comparator reference or target values, then attack all ordinary introspection/serialization paths.
6. **The Sprint 1 rubric mapping overclaims circularity detection (§6).** Declared provenance can reject a dependency labeled target-dependent; it cannot discover target-shaped preparation, coupling, thresholds, analysis, or model selection when the record is mislabeled state-independent. State this limitation explicitly and remove the claim that metadata checks “cover the routes.” Sprint 1 may pass its addressable rubric slice, but deferred non-negotiable slices remain unresolved rather than passed or scored.

## Required adversarial additions

- **Canonical collision attacks:** a literal mapping equal to the reserved Fraction marker must not serialize identically to a `Fraction`; NFC normalization must also cover mapping keys and identifiers, and normalization-created duplicate keys/record IDs must be rejected rather than overwritten.
- **Cross-space exact-type matrix:** for every public measure/space/kernel/comparator API, pass numerically shape-compatible wrong types and duck-typed objects. Subclass checks alone do not prove callers cannot interchange spaces.
- **Mediated-accessor closure:** `FrozenInputSet` must expose no alternate public record/content accessor; returned content must be immutable or defensive; unknown IDs, use-after-close, repeated reads, and close replay need explicit behavior. Full AST taint enforcement may remain Sprint 2 if this runtime boundary is added now.
- **Forged result replay:** deserialization must reject unknown/missing fields, caller-supplied authority fields, invalid claim values, and a serialized `Supported` result whose manifest or gates do not independently re-verify.
- **Lifecycle truth table:** replace “all six illegal transitions” with an explicit 3×3 table that reconciles immutable values, idempotent re-freeze, and transition methods. State whether transitions return new values or mutate lifecycle wrappers.
- **Meaningful planted failure:** `--prove-failure-exit` must violate a real invariant through the same check pipeline and name that failed invariant; an unconditional special-case exit is not evidence that failures propagate.
- **Exact numeric input boundary:** if “all weights are `Fraction`” is normative, reject `int`, `bool`, `Decimal`, and float weights explicitly rather than testing floats alone.

## Decisions on the four questions

| Question | Evaluator decision |
| --- | --- |
| Interpreter pinning | **Revise.** Build-index `python3` is authoritative and works on the Evaluator host; supplemental 3.13 coverage is welcome. |
| Fraction-only arithmetic | **Accept**, with the exact input-boundary checks above. |
| Undeclared dependency mechanism | **Accept the Sprint split conditionally.** AST taint may remain Sprint 2, but Sprint 1 must close alternate runtime/public access routes. |
| Comparator gate split | **Accept the Sprint split conditionally.** Import enforcement remains Sprint 2; the Sprint 1 data view must not retain or serialize target data. |
