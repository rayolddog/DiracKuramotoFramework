---
title: "Evaluator critique — Sprint 01 contract proposal r2"
kind: review
---

# Evaluator critique — Sprint 01 contract proposal r2

**Verdict:** focused revision required. Revision 2 resolves the first review, but three guarantees are still absent and four checks are internally ambiguous.

## Blocking gaps

1. **The approved separate same-space flow contract disappeared (§2, MEA-14…19).** The spec says equivariance/equilibrium preservation require a separate same-space flow contract. Revision 2 only requires a `SameSpaceFlow` in a callable signature and never checks the flow’s mathematical pushforward. Add an exact `SameSpaceFlowContract` type, require it for every equivariance test, validate total same-space mapping, and hand-check many-to-one pushforward plus exact normalization. Outcome agreement must not be accepted in its place.
2. **The closed claim vocabulary is not actually fixed (RES-09, RES-15).** Enumerating whatever members the implementation contains does not constrain the implementation. The contract must list the exact allowed `PermittedClaim` members and test equality against that literal set. Otherwise a new authority-bearing claim can be added together with a self-consistent test, leaving only the lexical backstop as protection—the failure mode the rubric explicitly rejects.
3. **Canonical construction attacks do not cover hostile canonical input (CAN-12…14, CAN-20, RES-10…14).** Python mappings cannot retain duplicate raw JSON keys, so construction-time duplicate checks miss `{"a":1,"a":2}` and NFC-equivalent raw keys. Add decoder tests for duplicate keys, NFC-created duplicate keys, NaN/Infinity, noncanonical whitespace/order, trailing data, and unknown tagged markers. Authority-bearing `from_canonical` must reject or explicitly re-canonicalize-and-compare; it may not silently accept a different byte representation.

## Required scope completion

- **Selector semantics:** distinct ledger classes and domain tags are insufficient for “deterministic-with-complete-noise-history.” Define `FixtureVersion` and the minimum ledger completeness invariants (declared length/domain, no missing or duplicate sequence positions, immutable ordered history); verify the primitive-kernel ledger cannot satisfy that contract accidentally.
- **Weighted-type invariants:** assert exact-Fraction, non-negativity, completeness, and exact normalization for every weighted structure, especially comparator targets and every transition-kernel row—not only the example measure.

## Ambiguities to remove

- `Manifest.verify(expected_root=...)` cannot both require the argument and return `ManifestUnverified` when omitted. Specify the actual signature and exact return types. The Evaluator accepts an optional argument only if absence can never produce an authoritative token.
- The `gc.get_referents` traversal in CMP-03 needs a bounded graph rule. Unbounded traversal through class/module/function globals can reach unrelated comparator fixtures; equality with a target Fraction can also false-positive on coincident raw values. Use unique target sentinels/values and exclude static interpreter/global objects while still traversing the complete instance-owned value graph.
- LIF-00 says `Closed.close` is absent and that replay raises `FreezeError`; choose one. The Evaluator accepts unrepresentable transitions and does not require raising stubs.
- ONT-01 bans `trajectory` from every field/docstring while ONT-02 requires `invalid_trajectory` and its docstring. State the exact mandated-label exception so the two checks can both pass.
- RUN-14 should define whether “same check IDs/results” means emitted stdout, pytest node IDs, or registry introspection; `pytest -q` normally does not print passing node IDs.

## Decisions on §10

| Open item | Evaluator decision |
| --- | --- |
| `expected_root` custody | **Accepted with the stated limitation.** The Evaluator will capture the clean root independently before mutations and will never source it from the attacked payload. |
| Immutable lifecycle types | **Accepted.** Unrepresentable illegal transitions are preferable; fix only the truth-table contradiction. |
| Stdlib-only tests | **Accepted.** Plain tests with exact-type exception checks are the stronger boundary. |
| Rubric verdict semantics | **Accepted.** Report Sprint 1 addressable slices PASS/FAIL and deferred slices UNRESOLVED; do not compute 90/100 yet. |
