---
title: "Sprint 01 Contract — contracts, schemas, provenance (AGREED r4)"
kind: spec
---

# Sprint 01 Contract — revision 4 (AGREED)

**Status:** **AGREED.** Negotiation exchange **4 of 4**. The Evaluator accepted r3 subject to two narrow corrections and a set of editorial fixes; r4 applies exactly those and nothing else. No prior check is weakened, removed, or renumbered, and no scope is added. Generator remains sole writer of this document.

**r4 changes, in full:**

| Change | Where |
| --- | --- |
| Invariance predicate closed to a one-member enum with the exact literal `same_space_measure_invariance_on_frozen_domain`; arbitrary and authority-shaped strings rejected | FLW-02 **[r4]** |
| Claims #5 / #6 rescoped to the exact supplied literals (adding `same_space` and, for #6, the missing frozen-domain scope) | §6-A, FLW-10 **[r4]** — FLW-09 references only `equivariance_not_tested` (#4) and is unchanged |
| Stale group headings corrected: MEA 24→30, PRV 18→20, CMP 15→17, RES 19→15 | §7 headings |
| §6 rubric mapping updated for FLW, DEC, SEM and all appended checks | §6 |
| Status marked agreed; exchange 4/4 recorded | this section |

**r1 check numbering (`C-0NN`) is withdrawn entirely.** r2 introduced grouped IDs; **r3 preserves every r2 ID and its meaning**, so the Evaluator can diff rather than re-read. Amended checks are marked **[r3]**. New checks are appended within their group or added as three new groups (`FLW`, `DEC`, `SEM`). Four IDs are *relocated* (RES-16…RES-19 → SEM-01…SEM-04); **the vacated RES numbers are retired and never reused**.

**196 checks** (r1: 87 → r2: 152 → r3/r4: 196). r4 adds no checks; it constrains FLW-02 and rescopes two claim literals.

**Build root (only writable code location):** `/Users/john-bramble/.traycer/epics/c443d91e-b0d5-43ff-a31b-805574ab7771/born_selection_equilibrium_fixture`

## 0-A. Response to the r2 critique

All three blocking gaps, both scope-completion items, and all five ambiguities are **accepted**. Gap 1 is conceded as a spec-fidelity failure; gaps 2 and 3 are conceded as checks that proved less than their wording claimed — the same class of defect the r1 review caught, which I did not generalize from when I should have.

| r2 critique | Disposition | Where |
| --- | --- | --- |
| 1. Separate `SameSpaceFlowContract` disappeared | **Conceded — a spec-fidelity miss.** The settled constraints say equivariance requires *a separate same-space flow contract*; I substituted "a `SameSpaceFlow` appears in the signature", which is a weaker and different thing, and never checked the flow's arithmetic at all. New group **FLW** (10 checks). | FLW-01…FLW-10, MEA-18 **[r3]** |
| 2. `PermittedClaim` membership not actually fixed | **Conceded — the check was circular.** A test that enumerates whatever the enum contains constrains nothing; implementation and test could add an authority-bearing claim together, leaving only the lexical backstop the rubric explicitly rejects. The exact membership is now **written into this contract** (§6-A) and asserted by set-equality against a literal. | §6-A, RES-09 **[r3]** |
| 3. Construction-time checks miss hostile canonical *input* | **Conceded, and verified empirically before accepting.** On CPython 3.12.6: `json.loads('{"a":1,"a":2}')` → `{'a':2}` silently; `json.loads('NaN')` → `nan`; `{"x":Infinity}` → `inf`; NFC-equivalent duplicate keys collapse to two distinct dict keys that normalize equal. Python mappings genuinely cannot represent the attack, so every r2 construction-time check was blind to it. New group **DEC** (14 checks). | DEC-01…DEC-14 |
| Selector split incomplete — "complete noise history" undefined | **Accepted.** r2 gave distinct types and domain tags and never said what *complete* means. New group **SEM** with `FixtureVersion` and ledger completeness invariants. | SEM-01…SEM-12 |
| Weighted invariants asserted only on the example measure | **Accepted.** Extended to every weighted structure, explicitly comparator targets and every kernel row. | MEA-25…MEA-30 |
| `Manifest.verify` both requires and omits `expected_root` | **Conceded — a flat contradiction.** Resolved by removing the ambiguous method entirely: two methods with **disjoint return types**, so the non-authoritative result cannot be passed where authority is required. | PRV-04 **[r3]**, PRV-19, PRV-20 |
| `gc.get_referents` walk unbounded | **Accepted.** Bounded, instance-owned traversal with unique sentinels; cap exhaustion **fails** the check rather than passing it. | CMP-03 **[r3]**, CMP-16, CMP-17 |
| `Closed.close` both absent and raising | **Conceded.** Absent. Replay-raises belongs to `FrozenInputSet.close()` (DEP-11), a different object. | LIF-00 **[r3]** |
| ONT-01 bans `trajectory`, ONT-02 mandates it | **Conceded.** Exact single-label exemption stated. | ONT-01 **[r3]**, ONT-04 |
| RUN-14 evidence undefined | **Accepted.** `pytest -q` does not print passing node IDs; evidence is now a shared registry plus `--collect-only`. | RUN-14 **[r3]**, RUN-15 |

## 0. Response to the r1 critique

All six blocking revisions and all seven required adversarial additions are **accepted**. Three are conceded as outright errors on my part; four are accepted and then strengthened past what was asked, because the finding pointed at a wider hole than the one it named.

| r1 critique | Disposition | Where |
| --- | --- | --- |
| 1. Interpreter section false on Evaluator host | **Conceded twice over.** Also conceded: I wrote "two pytest lines in the build index"; `grep -c pytest` on the index returns one command line. My host claim was true *of my host* and I over-generalized it into a correction of an approved artifact. | §1 |
| 2. `C-061` stdlib-only contradicts `C-083` `pytest.raises` | **Conceded — a real self-contradiction.** Adopting your fix, which is also *stricter* than what I proposed: `pytest.raises` matches **subclasses**, so it never proved exact exception types. `type(exc) is Expected` does. | RES-03 |
| 3. Rehash attack stops one level too early | **Conceded — the sharpest finding in the review.** Self-consistency is not tamper-evidence. Adopting the required out-of-band root commitment, and making the distinction itself a test (PRV-08). | PRV-04…PRV-09 |
| 4. Edge direction contradicts `declared_downstream` | **Conceded.** r1 said `declared_downstream` and then described contamination flowing backwards. Direction is now defined once, normatively, with forward positive and reverse negative controls. | DEP-00, DEP-02, DEP-03 |
| 5. Comparator gate passes while target reachable through the view | **Accepted and strengthened.** Attribute blocking replaced by a **reachability** requirement: `gc.get_referents` transitive traversal proves no comparator instance or target value exists in the view's object graph at all. Then the eight introspection/serialization paths are attacked anyway. | CMP-03…CMP-14 |
| 6. §6 overclaims circularity detection | **Conceded without reservation.** Declared provenance cannot detect a *mislabeled* target-shaped preparation. The claim is removed, not softened. | §5, §6 |

| Required addition | Where |
| --- | --- |
| Canonical collision attacks (marker literal, NFC on keys/IDs, normalization-created duplicates) | CAN-06, CAN-07, CAN-12, CAN-13, CAN-14 |
| Cross-space exact-type / duck-type matrix | MEA-16, MEA-17 |
| Mediated-accessor closure (no alternate accessor, defensive returns, unknown ID, repeated read, use-after-close, close replay) | DEP-05…DEP-11 |
| Forged result replay | RES-10…RES-14 |
| Lifecycle 3×3 truth table + transition semantics stated | LIF-00…LIF-11 |
| Meaningful planted failure | RUN-07, RUN-08, RUN-09 |
| Exact numeric input boundary (int, bool, Decimal, float) | MEA-03 |

**Generator additions arising from your findings, not requested by them:** PRV-17 (pickle refused on authority-bearing types — `pickle` bypasses `__init__` and was a live laundering path implied by your point 5), RUN-08/RUN-09 (proving the planted failure shares the normal code path, not merely that it fails), DEP-08 (a failed unknown-ID probe must not pad the observed-read set), RUN-14 (both runners must report the same check IDs, so neither can hide one), MEA-17 (exact-type rather than `isinstance` checks, so subclassing cannot interchange spaces).

## 1. Interpreter and invocation — corrected

**The build-index path is authoritative and mandatory.** It is correct on the Evaluator host, where `python3` and `python3.12` are both 3.12.6 with pytest 9.0.2. r1 was wrong to propose replacing it.

**Mandatory suite — Evaluator host, exactly as approved in the [build index](../../index.md):**

```text
python3 -m pytest -q born_selection_equilibrium_fixture/tests
python3 -m born_selection_equilibrium_fixture.verify
python3 -W error -m born_selection_equilibrium_fixture.verify
python3 born_selection_equilibrium_fixture/verify.py
python3 -m born_selection_equilibrium_fixture.verify --prove-failure-exit
python3 -m py_compile born_selection_equilibrium_fixture/*.py
python3 -m compileall -q born_selection_equilibrium_fixture
```

**Supplemental — Generator host only, reported as extra coverage, never as a substitute:**

```text
python3.12 -m pytest -q born_selection_equilibrium_fixture/tests   # 3.12.6 + pytest 9.0.2
python3 -m born_selection_equilibrium_fixture.verify               # 3.13.11, no pytest present
python3 -W error -m born_selection_equilibrium_fixture.verify      # 3.13.11
PYTHONHASHSEED=1    python3 -m born_selection_equilibrium_fixture.verify --json
PYTHONHASHSEED=9999 python3 -m born_selection_equilibrium_fixture.verify --json
```

Generator-host facts, recorded as a host difference rather than a correction: `python3` → 3.13.11 with no pytest; `python3.12` → 3.12.6 with pytest 9.0.2; `hypothesis` absent on both. The stdlib-only commitment (RES-03) is what makes one codebase satisfy both hosts, and it now yields a free portability result — the same package passing under 3.12.6 and 3.13.11 is evidence against version-specific behaviour, which I will report but not score.

## 2. Scope

**In scope (schemas and gates only — no fixture mechanisms run):** exact-arithmetic measure family; canonical serialization with domain-separated digests; provenance with state-dependence, freeze timing, declared dependencies; declared-dependency DAG with contamination closure and observed-vs-declared reconciliation; `Draft → Frozen → Closed` lifecycle; disjoint four-way result algebra; selector-semantics split; authority and claim gates; `verify.py`; adversarial test suite.

**Deferred, with Sprint 1's partial coverage named so nothing goes silently uncovered:**

| Spec item | Sprint | Sprint 1 nonetheless delivers | Rubric status |
| --- | --- | --- | --- |
| Raw/comparator **import** firewall (import hook + AST stage check) | 2 | Data-level gate: distinct type, `Closed`-only attachment, **no comparator reachable in the raw view's object graph**, eight leak paths attacked (CMP-01…CMP-15) | Import-enforcement slice **UNRESOLVED** |
| Fixture mechanisms (honest, target-shaped preparation, target-shaped selector, postselection, confounding controls) | 2 | The schemas each must instantiate; the gates that must close before any fixture runs | **UNRESOLVED** |
| Blinded holdouts, equivalence margins, nonequilibrium response, negative controls | 3 | Complete outcome-category enforcement; the `Refused` postselection path those tests target | **UNRESOLVED** |
| **Semantic** circularity detection (mislabeled target-shaped preparation, coupling, thresholds, analysis, model selection) | 2–3 | **Nothing. See §5.** | **UNRESOLVED** |
| Statistical tolerances | 3 | Zero tolerances in Sprint 1 (§3) | **UNRESOLVED** |

**Out of scope, read-only:** manuscripts, `adler_born_two_channel`, silver-halide, `hologram_phase_test`, Ticket 07/08, all reviewed planning artifacts including the unmodified parent `sprint-01/index.md`.

## 3. Numerical discipline

All weights are `fractions.Fraction` under an **exact type** rule: `type(w) is Fraction`. Normalization is exact equality `sum(weights) == Fraction(1)`. Sprint 1 contains no statistics, therefore needs no tolerances, therefore has none. A tolerance is a place a target-shaped result can hide; Sprint 3 introduces them and must defend each one individually there.

## 4. Ontology neutrality

Per Planner direction: Sprint 1 is **ontology-neutral**. The microstate space is an abstract finite index set. No type, field, parameter, or docstring encodes position, momentum, coordinates, trajectories, particle count, wavepackets, or any commitment to point-particle *or* wave ontology. The harness must admit either and commit to neither.

One name needs explicit handling: the mandatory category `invalid_trajectory` is **inherited verbatim from the approved spec** and is a *ledger category label*, not an ontological commitment. Its docstring says so. I am keeping the spec's name rather than renaming it, since renaming a spec-mandated category would be a unilateral change to approved planning language.

## 5. What Sprint 1 cannot detect — stated plainly

Your point 6 is correct and I am not softening it.

**Declared provenance can only reject a route that is honestly labeled.** A record whose `state_dependence` is truthfully `DEPENDS_ON_TARGET_OUTCOME_LAW` is refused (DEP-02). A record that is *actually* target-shaped — a preparation kernel whose weights were reverse-engineered from the target curve, a coupling constant tuned to it, a threshold placed to reproduce it, an analysis choice or model selection made after seeing it — but is labeled `STATE_INDEPENDENT`, **passes every Sprint 1 check.** Metadata cannot see content it is lying about.

Sprint 1 therefore builds the *frame* in which such a route becomes detectable — the frozen domain, the content-addressing, the observed-read reconciliation that later sprints can compare against actual computation. It does not detect the route. The rubric's Circularity Detection criterion (weight 20, non-negotiable) is **not satisfiable in Sprint 1** and I am not claiming a share of it beyond the declared-label slice.

## 6. Rubric verdict semantics for Sprint 1

Adopting your decision-10 request, stated as a rule the Evaluator applies rather than a hope:

1. A non-negotiable criterion is decomposed into an **addressable Sprint 1 slice** and one or more **deferred slices**.
2. The addressable slice may return PASS or FAIL on its own evidence.
3. **A deferred slice returns UNRESOLVED. It is never scored, never implicitly passed, and never averaged into a weighted total as if satisfied.**
4. A criterion whose deferred slices are non-empty cannot be reported as "passed" for the build — only "Sprint 1 slice passed, remainder UNRESOLVED".
5. The rubric's 90/100 overall threshold is therefore **not evaluable at Sprint 1** and must not be computed. Computing it would require scoring UNRESOLVED slices as zero (failing the sprint for work not yet due) or as full marks (the quiet pass this whole structure exists to prevent).

| Criterion | Weight | NN | Sprint 1 addressable slice | Deferred → UNRESOLVED |
| --- | --- | --- | --- | --- |
| Scientific boundary integrity | 25 | Y | Type-level impossibility of a physical verdict; **pinned claim literal set (§6-A)**; **closed invariance predicate (FLW-02)**; authority fields; attestations; ontology neutrality — MEA-18/19, **FLW-02**, **FLW-08…FLW-10**, CMP-15, RES-04…RES-09, RES-15, ONT-01…**ONT-04**, ERR-03/05 | Boundary integrity of Sprint 2–3 fixture outputs and summaries |
| Circularity detection | 20 | Y | **Declared-label slice only** — DEP-00…DEP-04, PRV-11…PRV-13, MEA-22 | **Semantic circularity (§5) — the substantive majority of this criterion** |
| Measure-space correctness | 15 | Y | MEA-01…MEA-**30** (incl. the weighted-invariant sweep over all six weighted structures), **FLW-01…FLW-10** (same-space contract, totality, many-to-one and bijective pushforward arithmetic), CMP-01, PRV-14 | — (believed fully addressable in Sprint 1) |
| Structural isolation and provenance | 15 | Y | CAN-01…CAN-20, **DEC-01…DEC-14** (hostile canonical input), PRV-01…**PRV-20** (incl. disjoint verdict types), CMP-01…**CMP-17** (incl. bounded traversal + leaky-decoy control), DEP-05…DEP-17 | Import-level firewall |
| Discriminating tests | 10 | Y | Complete categories + postselection refusal + observed/declared reconciliation + planted failure + **positive controls that prove a detector can detect** — MEA-20…23, **MEA-29/30**, DEP-12/13, **SEM-06…SEM-12**, **CMP-16/17**, **ONT-04**, RUN-07…09 | Blinded holdouts, equivalence margins, nonequilibrium response, negative controls |
| Reproducibility and numerical discipline | 10 | Y | §3, CAN-18, **DEC-07/08/13/14** (canonical-form determinism), RUN-01…**RUN-15** (incl. registry-backed cross-runner agreement) | Sprint 3 tolerance policy |
| Clarity and maintainability | 5 | N | ERR-01…ERR-05 | — |

**Note on the three r3 groups.** FLW carries a share of two non-negotiables (Scientific boundary integrity via FLW-02/08/09/10; Measure-space correctness via FLW-03…FLW-07). DEC sits almost entirely under Structural isolation and provenance, with a reproducibility share. SEM sits under Discriminating tests and Measure-space correctness. None of the three creates a new criterion, and none moves a deferred slice into the addressable column.

## 6-A. `PermittedClaim` — the pinned literal membership

**This is the normative list.** RES-09 asserts `{c.value for c in PermittedClaim}` equals exactly this 16-element set, with the literal copied into the test. Three independent copies exist — this contract, the test literal, and the enum — so adding an authority-bearing claim requires editing this reviewed document, which is visible to the Evaluator and the Planner. r2's version read the membership off the implementation and therefore constrained nothing.

```text
 1  conditional_outcome_compatibility_supported_for_frozen_domain
 2  conditional_outcome_compatibility_not_supported_for_frozen_domain
 3  conditional_outcome_compatibility_not_testable
 4  equivariance_not_tested
 5  equivariance_tested_nonphysical_fixture_same_space_flow_invariant_for_frozen_domain
 6  equivariance_tested_nonphysical_fixture_same_space_flow_not_invariant_for_frozen_domain
 7  individual_selection_demonstrated_nonphysical_fixture
 8  postselection_refused
 9  target_dependence_declared_refused
10  dependency_gate_open_refused
11  claim_gate_open_refused
12  manifest_not_authoritative_refused
13  selector_semantics_unfrozen_refused
14  noise_history_incomplete_refused
15  ledger_semantics_mismatch_refused
16  comparator_attached_before_raw_closure_refused
```

**Properties asserted about the set itself, not merely its members:**

- Exactly one claim (#1) can be emitted on a successful comparator agreement, and it is scoped to the frozen domain (CMP-15, RES-09).
- **No member asserts physical selection, equilibrium preservation, individual actuality, or a Born derivation.** **[r4]** #5 and #6 now carry the `same_space` distinction — the exact thing the separate `SameSpaceFlowContract` exists to preserve — and **both** are scoped `for_frozen_domain`; r3's #6 lacked that scope, so a negative equivariance result could have been read as unscoped. They speak only of a *nonphysical fixture same-space flow's* invariance over a frozen domain, never of equilibrium. #7 says *demonstrated in a nonphysical fixture*, never that an individual outcome is actual.
- **The boundary is now literal rather than explanatory.** Each of #5 and #6 carries its type scope (`nonphysical_fixture`), its space scope (`same_space_flow`), and its domain scope (`for_frozen_domain`) **inside the claim string itself**, so a claim quoted out of context into a summary or a README still carries its own limits.
- Members 1–3 match the rubric's calibration example verbatim, as do #4 and #7, which are the two attestations `Supported` requires (RES-05).
- Ten of sixteen are refusals. A vocabulary in which refusal is the common case is harder to inflate than one where it is an exception.

## 7. Verification checks (196)

Every check is exercised by **both** runners (RUN-14). `[SI]` marks source-inspection targets.

### CAN — canonical serialization and collision resistance (20)

- **CAN-01** UTF-8, `sort_keys=True`, `separators=(',',':')`, no trailing newline.
- **CAN-02** Dict insertion-order difference → byte-identical output and identical digest.
- **CAN-03** Unordered record-set reorder → identical digest (records canonically sorted by id).
- **CAN-04** Ordered-sequence reorder → **different** digest. Order-sensitivity is a documented per-field property.
- **CAN-05** `Fraction` → `{"__frac__":"n/d"}`, lowest terms, positive denominator; `Fraction(2,4)` and `Fraction(1,2)` byte-identical.
- **CAN-06** **Marker-collision attack:** a plain mapping literally equal to `{"__frac__":"1/2"}` must not serialize identically to `Fraction(1,2)`. Mechanism: any user-supplied mapping key matching `^__[a-z_]+__$` raises `SerializationError`. Asserted both that it raises **and** that no byte-collision exists.
- **CAN-07** Marker rejection applies at nested depth ≥ 3 (inside lists, inside nested mappings).
- **CAN-08** `float` rejected: `1.0`, `0.0`, `nan`, `inf`, `-inf` → `SerializationError` (5 assertions).
- **CAN-09** `set`, `frozenset`, `bytes`, `bytearray`, `complex`, arbitrary object → `SerializationError`. No `repr()` fallback.
- **CAN-10** Non-`str` mapping key (`int`, `None`, `Fraction`, `tuple`) → `SerializationError`.
- **CAN-11** NFC normalization applied to string **values**; composed/decomposed pair hashes identically.
- **CAN-12** NFC normalization applied to mapping **keys**.
- **CAN-13** NFC normalization applied to **record IDs and identifiers**.
- **CAN-14** **Normalization-created duplicates rejected, not overwritten:** a mapping with two Python-distinct but NFC-equal keys → `SerializationError`; two NFC-equal record IDs in one manifest → `ProvenanceError`.
- **CAN-15** `digest = sha256(domain_tag || 0x00 || canonical_bytes)`; domain tag = exact type name + schema version.
- **CAN-16** `MicrostateMeasure` and `OutcomeLaw` with numerically identical weights → **different** digests.
- **CAN-17** Schema-version bump changes every digest.
- **CAN-18** Digests stable across `PYTHONHASHSEED=1` / `=9999` (byte-identical `--json`).
- **CAN-19** `[SI]` No `hash()`, `id()`, `repr()`, `str()`-of-container, `time`, or `random` in any digest path.
- **CAN-20** Round-trip: `from_canonical(to_canonical(x))` equals `x` with matching digest, for one instance of **every** schema type.

### MEA — measure-space correctness (30)

- **MEA-01** Exact normalization `sum == Fraction(1)`; `Fraction(1,3)×3` passes; `Fraction(999,1000)` → `NormalizationError`.
- **MEA-02** Negative weight → `NormalizationError`; zero weight permitted.
- **MEA-03** **Exact numeric boundary:** weight must satisfy `type(w) is Fraction`. Explicitly rejected, asserted per rejected type × per measure type: `int` (`1`), `bool` (`True`, `False` — note `bool` is an `int` subclass, so `isinstance` would let it through), `float` (`0.5`), `Decimal("0.5")`, `str("1/2")`, and a **`Fraction` subclass instance** (so subclassing cannot smuggle behaviour in).
- **MEA-04** Measure over a point outside its declared space → `MeasureError`.
- **MEA-05** Space point with no assigned weight → `MeasureError` (total function required; no implicit zero).
- **MEA-06** Duplicate space points → `MeasureError`.
- **MEA-07** Empty space → `MeasureError`.
- **MEA-08** `TransitionKernel` row sums exactly `Fraction(1)`; a row summing `Fraction(1,2)` raises.
- **MEA-09** Kernel domain must equal the declared microstate space exactly; a missing row raises.
- **MEA-10** Kernel codomain must equal the declared `OutcomeCategorySet` exactly.
- **MEA-11** `pushforward` computes `Σ_x μ(x)·K(x,c)` in exact rationals; verified against a hand-computed rational example with no rounding.
- **MEA-12** Pushforward output exactly normalized — asserted, not inferred from MEA-01 + MEA-08.
- **MEA-13** `TransitionKernel.pushforward` returns `OutcomeLaw` exactly (`type(r) is OutcomeLaw`).
- **MEA-14** `SameSpaceFlow` domain == codomain == the same microstate space; a flow whose codomain is an `OutcomeCategorySet` → `MeasureError` at construction.
- **MEA-15** `SameSpaceFlow.pushforward` returns `MicrostateMeasure` exactly — never an `OutcomeLaw`.
- **MEA-16** **Cross-space exact-type / duck-type matrix.** For every public cross-space API (`TransitionKernel.pushforward`, `SameSpaceFlow.pushforward`, comparator comparison, conditioning, agreement), pass: (a) each wrong exact type from the seven-type family, (b) a **duck-typed impostor** exposing identical attributes/methods with numerically compatible content, (c) a subclass impostor. All raise `MeasureError`. Matrix size asserted in the test so a shrinking matrix is itself a failure.
- **MEA-17** Non-substitutability is enforced by `type(x) is T`, **not** `isinstance` — subclassing cannot interchange spaces. Asserted with an explicit subclass attempt per API.
- **MEA-18** **[r3]** No public callable returns an equivariance or equilibrium verdict without a **`SameSpaceFlowContract`** — the spec-mandated separate contract type, not a bare `SameSpaceFlow` — in its **required** signature. Asserted by `inspect.signature` scan over the entire public surface, so a later refactor adding a bypass breaks the test. (r2 required only the flow object; that was weaker than the spec and is corrected here. Arithmetic is checked in group **FLW**.)
- **MEA-19** `[SI]` No function anywhere takes an `OutcomeLaw` or a comparator agreement and returns an equivariance/equilibrium/actuality verdict.
- **MEA-20** `OutcomeCategorySet` requires all four mandatory categories; omitting each of `no_record`, `multiple_record`, `invalid_trajectory`, `ledger_failure` raises naming the missing one (4 assertions).
- **MEA-21** `OutcomeLaw` must assign a weight to every category including the mandatory four; omitting `no_record` raises.
- **MEA-22** Conditioning that drops a mandatory category from the denominator returns `Refused(postselection_refused)` — **not** a renormalized law. Asserted per mandatory category (4 assertions).
- **MEA-23** Removing a mandatory category changes the category-set digest and every downstream digest, asserted end-to-end through a manifest.
- **MEA-24** Comparing a `MicrostateMeasure` against a comparator → `MeasureError`; the comparator speaks only about outcome categories.

**Weighted-invariant sweep — every weighted structure, not just the example measure (r2 asserted these on one type; the Evaluator is right that a per-type sweep is a different claim).** For each of the six weighted structures — `MicrostateMeasure`, `OutcomeLaw`, **every `TransitionKernel` row**, **every `SameSpaceFlow` row**, **`QuantumOutcomeComparator` target law**, and `FixtureVersion`-carried weights — all four invariants are asserted individually:

- **MEA-25** **Exact Fraction type** (`type(w) is Fraction`) on all six structures × the six rejected inputs from MEA-03 (`int`, `bool`, `float`, `Decimal`, `str`, `Fraction` subclass). Matrix size asserted, so a shrinking matrix is itself a failure.
- **MEA-26** **Non-negativity** on all six; a single negative weight in any one raises `NormalizationError`.
- **MEA-27** **Completeness** on all six: every element of the declared domain carries a weight; no implicit zero; a missing element raises.
- **MEA-28** **Exact normalization** on all six: `sum == Fraction(1)` exactly, asserted per kernel row and per flow row rather than in aggregate.
- **MEA-29** **Comparator targets specifically:** the comparator's target law is exact-Fraction, non-negative, complete over the full `OutcomeCategorySet` **including the four mandatory categories**, and exactly normalized. A comparator whose targets omit `no_record` raises — the rubric's "invalid/no-click events disappear from the denominator" failure is unrepresentable on the comparator side too, not only the fixture side.
- **MEA-30** **Row-level, not aggregate:** a kernel with two rows whose *errors cancel* (one summing `Fraction(3,2)`, one `Fraction(1,2)`) raises. Asserted explicitly, because an aggregate normalization check would pass it.

### FLW — same-space flow contract (10)

The spec's settled constraints require a **separate same-space flow contract** for equivariance and equilibrium preservation. `SameSpaceFlowContract` is an exact type distinct from `SameSpaceFlow`: the flow is the mapping, the contract is the frozen statement of *which* flow, over *which* domain, with *what* invariance is being tested.

- **FLW-01** `SameSpaceFlowContract` is an exact type; `type(c) is SameSpaceFlowContract` is required at every equivariance entry point. A bare `SameSpaceFlow`, a duck-typed impostor, and a subclass impostor all raise `MeasureError`.
- **FLW-02** **[r4]** The contract carries the `SameSpaceFlow`, the frozen microstate domain, the closed one-member `InvariancePredicate`, and its own content-addressed digest with a distinct domain tag. `{p.value for p in InvariancePredicate}` equals exactly `{"same_space_measure_invariance_on_frozen_domain"}`. Any other string raises `AuthorityError`; the authority-shaped alternatives `physical_equilibrium_preservation`, `equilibrium_preserved`, `born_measure_derivation`, `individual_actuality_invariance`, and `quantum_equilibrium_invariance` are rejected individually. An invalid predicate cannot be injected through `from_canonical`: strict canonical-byte validation and the closed-enum check are each asserted independently so neither is load-bearing.
- **FLW-03** **Total same-space mapping validated:** the flow's domain and codomain are the *same* microstate space object, and the mapping is **total** — every microstate has an image. A partial flow raises `MeasureError` naming the unmapped point.
- **FLW-04** **Hand-checked many-to-one pushforward.** A flow mapping three microstates onto two (`x1,x2 → y1`; `x3 → y2`) with μ = (1/6, 1/3, 1/2) pushes forward to exactly (1/2, 1/2) — weights of merged preimages **sum**. Asserted against hand-computed rationals with no rounding. This is the arithmetic r2 never checked.
- **FLW-05** Pushforward under a many-to-one flow is exactly normalized (`sum == Fraction(1)`), asserted separately from FLW-04 so a correct total cannot mask wrong per-point values.
- **FLW-06** A **permutation** flow (bijective) preserves each weight up to relabelling — asserted pointwise, giving a positive control alongside FLW-04's many-to-one lossy case.
- **FLW-07** `SameSpaceFlowContract.pushforward` returns `MicrostateMeasure` exactly; returning or accepting an `OutcomeLaw` raises.
- **FLW-08** **Outcome agreement cannot substitute for the contract.** Attempting to obtain an equivariance verdict from an `OutcomeLaw`, a pushforward match, or a comparator agreement raises `MeasureError`; asserted for all three inputs at every equivariance entry point.
- **FLW-09** Without a `SameSpaceFlowContract`, the only claim available is `equivariance_not_tested` (§6-A) — asserted against the full literal claim set, so no equivariance-positive claim is reachable.
- **FLW-10** **[r4]** An equivariance verdict is scoped to the contract's frozen domain and to the same-space flow: the emitted claims are exactly `equivariance_tested_nonphysical_fixture_same_space_flow_invariant_for_frozen_domain` and `equivariance_tested_nonphysical_fixture_same_space_flow_not_invariant_for_frozen_domain`, never an unscoped, cross-space, or physical equilibrium statement. **Both** the positive and the negative claim carry `for_frozen_domain`, asserted individually.

### DEC — hostile canonical input (14)

r2 attacked hostile Python objects at construction. It could not attack hostile **bytes**, because a Python `dict` cannot represent duplicate keys. Verified on CPython 3.12.6 before writing these: `json.loads('{"a":1,"a":2}')` → `{'a':2}`; `json.loads('NaN')` → `nan`; `json.loads('{"x":Infinity}')` → `inf`; `{"é":1,"é":2}` (NFC-equivalent) → two surviving keys. Every one of these is silent.

**Governing rule:** every authority-bearing `from_canonical` **parses strictly, re-emits canonical bytes, and requires byte equality with the input**. Any non-canonical representation of an acceptable value is rejected rather than normalized-and-accepted. Strict parse hooks run in addition, so each attack fails with an accurate error rather than a generic byte mismatch.

- **DEC-01** Duplicate raw JSON keys `{"a":1,"a":2}` → `SerializationError` via `object_pairs_hook`, **not** last-wins collapse.
- **DEC-02** NFC-equivalent duplicate raw keys (`{"é":1,"é":2}`, composed vs decomposed) → `SerializationError`. Detected on the raw pairs before dict construction, since the collapse in CAN-14 happens too late for input bytes.
- **DEC-03** Duplicate record IDs in a raw manifest payload, including NFC-equivalent ones → `ProvenanceError`.
- **DEC-04** `NaN` → `SerializationError` via `parse_constant`.
- **DEC-05** `Infinity` and `-Infinity` → `SerializationError` (2 assertions).
- **DEC-06** JSON float literals (`1.0`, `1e3`) → `SerializationError`; only `{"__frac__":"n/d"}` may carry a weight.
- **DEC-07** Non-canonical whitespace (`{ "a" : 1 }`) → rejected by byte-comparison, with a message naming non-canonical encoding.
- **DEC-08** Non-canonical key order (`{"b":1,"a":2}`) → rejected by byte-comparison.
- **DEC-09** Trailing data after the JSON value → `SerializationError` (CPython raises `JSONDecodeError`; it is caught and re-raised as the exact contract type per ERR-01).
- **DEC-10** Leading UTF-8 BOM → `SerializationError`.
- **DEC-11** Unknown tagged marker `{"__unknown__":…}` → `SerializationError`; unrecognized markers are never passed through as plain mappings.
- **DEC-12** Non-lowest-terms Fraction payload `{"__frac__":"2/4"}` and negative-denominator `{"__frac__":"1/-2"}` → `SerializationError`; only the canonical spelling decodes.
- **DEC-13** Non-NFC string values in input bytes → rejected by byte-comparison, **not** silently normalized. Normalizing on input would make two distinct byte strings decode to one object, which is the collision CAN-11 exists to prevent.
- **DEC-14** **Recanonicalization is genuinely byte-compared:** a payload that decodes to a valid object but differs from `canonical_bytes(decoded)` by one byte is rejected. Asserted with a mutation at the first, middle, and last byte position (3 assertions), so the comparison cannot be a prefix or length check.

### PRV — provenance, manifests, tamper-evidence (20)

- **PRV-01** `StateDependence` closed enum: `STATE_INDEPENDENT`, `DEPENDS_ON_MICROSTATE_ONLY`, `DEPENDS_ON_FROZEN_RAW_LEDGER`, `DEPENDS_ON_TARGET_OUTCOME_LAW`, `DEPENDS_ON_COMPARATOR_OUTPUT`. Out-of-enum → `ProvenanceError`.
- **PRV-02** `InputRecord` required fields (`record_id`, `content_digest`, `state_dependence`, `freeze_timing`, `declared_downstream`, `schema_version`) — omission asserted field-by-field.
- **PRV-03** `content_digest` recomputed on verify; post-freeze content mutation → `ProvenanceError` naming the record.
- **PRV-04** **[r3]** **Out-of-band root commitment is mandatory for any authoritative verdict.** r2 said the argument was both required and omittable — a flat contradiction. Resolved by deleting the ambiguous method. There is **no** `Manifest.verify(...)`. There are two methods with **disjoint return types**:
  | Method | Signature | Returns |
  | --- | --- | --- |
  | `verify_against` | `(self, expected_root: Digest) -> ManifestVerdict` | exactly `ManifestAuthoritative` or `ManifestRejected` |
  | `check_self_consistency` | `(self) -> SelfConsistencyReport` | `SelfConsistencyReport` only |
  | `expected_root` is positional-and-required; there is no default and no keyword-omission path. `SelfConsistencyReport` is **not** a `ManifestVerdict` and carries no authoritative token, so omission cannot yield authority — it is a type error, not a policy check. |  |  |
- **PRV-05** **Full rehash attack:** mutate content, recompute the record digest, recompute **every nested digest**, recompute the **manifest root** — verification against the separately held `expected_root` still fails.
- **PRV-06** **Delete attack** with full root recomputation → fails against `expected_root`, naming the missing `record_id`.
- **PRV-07** **Relabel attack** (rename a record id or a label) with full root recomputation → fails against `expected_root`.
- **PRV-08** **Self-consistency is not authority, asserted as a property:** the fully-recomputed tampered manifest from PRV-05 verifies *self-consistently* (asserted **true**) and is nonetheless rejected against `expected_root` (asserted). The distinction is a test, not a comment.
- **PRV-09** `[SI]` + signature: there is no API path that sources `expected_root` from the serialized payload, a sibling file, or an environment variable. The commitment cannot come from anything an attacker who holds the manifest also holds.
- **PRV-10** Stale replay: recorded `schema_version` ≠ running version → `ProvenanceError`.
- **PRV-11** State-dependence mutation fails closed in **both** directions — flipping toward `DEPENDS_ON_TARGET_OUTCOME_LAW` and flipping away from it. The sanitizing direction is not privileged.
- **PRV-12** `FreezeTiming` closed enum (`PRE_RAW_CLOSE`, `POST_RAW_CLOSE`); `DEPENDS_ON_COMPARATOR_OUTPUT` + `PRE_RAW_CLOSE` → `ProvenanceError` at construction.
- **PRV-13** A raw-stage record with `DEPENDS_ON_TARGET_OUTCOME_LAW` → `ProvenanceError` at construction. The illegal combination is unrepresentable, not checked later.
- **PRV-14** Round-trip equality and digest match for a manifest containing one record of each `StateDependence` value.
- **PRV-15** NFC-equal record IDs rejected (with CAN-14).
- **PRV-16** Reorder immunity asserted **positively**, so "immune" is distinguishable from "undetected".
- **PRV-17** **Pickle refused on authority-bearing types.** `Manifest`, gate records, and the four result types define `__reduce__` raising `AuthorityError`. `pickle` bypasses `__init__` and would otherwise launder every construction-time gate; canonical bytes is the sole serialization path.
- **PRV-18** `deepcopy` preserves digests — a copy cannot launder a mutation.
- **PRV-19** `ManifestAuthoritative`, `ManifestRejected`, and `SelfConsistencyReport` are three exact, pairwise-disjoint types; none subclasses another (asserted both directions, 6 assertions). `SelfConsistencyReport` cannot be passed anywhere a `ManifestVerdict` is required — asserted by attempting it at every consuming call site.
- **PRV-20** A **self-consistent but rejected** manifest yields `SelfConsistencyReport(consistent=True)` **and** `ManifestRejected` in the same test, from the same object. This is PRV-08's distinction made type-level rather than value-level: passing the consistency report to `Supported` raises, so the two can never be confused by a caller.

### CMP — comparator data gate (17)

- **CMP-01** `QuantumOutcomeComparator` is a distinct type: not a subclass of `OutcomeLaw` and not a superclass of it (both directions asserted).
- **CMP-02** Attachment at `Draft` or `Frozen` → `IsolationError`; only `Closed` permits it.
- **CMP-03** **[r3]** **Bounded reachability, not attribute blocking.** Transitive `gc.get_referents` traversal from the raw-stage view reaches **no** `QuantumOutcomeComparator` instance and **no** target value. r2 left the walk unbounded, which the Evaluator is right would wander into module globals and unrelated fixtures. The traversal rule is now pinned:
  - **Frontier:** starts at the view instance; follows only **instance-owned** values — `__dict__` values, slot values, and elements of contained containers.
  - **Excluded:** `type` objects, modules, functions, methods, code objects, frames, tracebacks, and anything reachable only via `__class__`, `__globals__`, `__module__`, or `__closure__`. Static interpreter and global objects are never entered.
  - **Detection is by identity first:** `obj is comparator_instance`, and `obj is target_sentinel` for each target value object.
  - **Value equality is a secondary signal only**, and only against **unique sentinel rationals** with a distinguishing large prime denominator (`Fraction(k, 1000003)`), so a coincidental match against an ordinary weight like `Fraction(1,2)` cannot false-positive.
  - **Bounded with fail-closed exhaustion:** node and depth caps are explicit constants; **hitting a cap FAILS the check**. A traversal that runs out of budget never reports "clean".
- **CMP-04**…**CMP-11** Leak matrix, one check per path, each asserting no target value appears in the output: `vars()`, `__dict__`, `repr()`, `str()`, iteration, mapping conversion, `dataclasses.asdict()`, `canonical_bytes()`.
- **CMP-12** Pickling the raw view either raises or yields bytes containing no target value.
- **CMP-13** No `__getattr__`/`__getattribute__` fallback synthesizes target access; an unknown attribute raises `AttributeError`, never a silent `None`.
- **CMP-14** `dir()` on the raw view exposes no comparator-related name.
- **CMP-15** A comparator agreement can only ever produce `conditional_outcome_compatibility_supported_for_frozen_domain` — asserted against the **full** **literal** `PermittedClaim` membership pinned in §6-A.
- **CMP-16** **Traversal is proven capable of finding a leak.** A deliberately-leaky decoy view that *does* retain the comparator is built, and CMP-03's traversal **detects it**. Without this, "found nothing" is indistinguishable from "traversal is broken" — the same class of hole the Evaluator identified in `--prove-failure-exit`.
- **CMP-17** The traversal's exclusion rules do not create a blind spot: a decoy that hides the comparator inside a **contained container** (list, tuple, dict value, frozenset, nested dataclass, and slot) is detected in all six placements. Exclusions cover static interpreter objects only, never instance-owned data.

### DEP — dependency gate (18)

- **DEP-00** **Edge direction, defined once and normatively** (in this contract and in the module docstring): record `u` declares `declared_downstream = (v, …)`, meaning **"v consumes u"**; the edge is `u → v`; **contamination flows along the edge**, from an upstream target-dependent producer to its downstream consumers. Closure is computed on this definition and no other.
- **DEP-01** A declared cycle → `DependencyError` naming the cycle members.
- **DEP-02** **Forward positive control:** `u → v → w` with `u` target-dependent ⇒ `v` and `w` contaminated; a raw-stage `w` is refused. Depth ≥ 3.
- **DEP-03** **Reverse negative control:** `u → v → w` with **`w`** target-dependent ⇒ `u` and `v` are **NOT** contaminated. The absence of backward propagation is asserted as a required property, not left as an untested assumption.
- **DEP-04** Closure is transitive at depth ≥ 3 and terminates on a diamond graph (asserted with an explicit diamond).
- **DEP-05** Content is readable **only** via `FrozenInputSet.use(record_id)`, which records the observed read.
- **DEP-06** **No alternate public accessor:** surface scan asserts `FrozenInputSet` exposes no `__getitem__`, `__iter__` over content, `records`, `items()`, `values()`, `get()`, `keys()`-to-content path, `raw`, `content`, or public attribute holding the record map. The forbidden-name list is enumerated in the test.
- **DEP-07** **Defensive returns:** `use()` returns immutable content; mutation attempt raises; the returned object is not an internally-held mutable instance (asserted by immutability, and by identity where aliasing would matter).
- **DEP-08** **Unknown ID:** `use()` with an unknown `record_id` raises `DependencyError` **and does not record an observed read** — so a failed probe cannot pad the observed set.
- **DEP-09** **Repeated read:** repeated `use()` of the same id is permitted and idempotent in the observed set (recorded once). Explicit and asserted.
- **DEP-10** **Use-after-close:** `use()` after `close()` raises `FreezeError`.
- **DEP-11** **Close replay:** a second `close()` raises `FreezeError`; there is no reopen path.
- **DEP-12** Undeclared use → `close()` fails naming the record.
- **DEP-13** Declared-but-unused → `close()` fails. Padding the declaration list to evade DEP-12 trips this.
- **DEP-14** The dependency gate must close before any fixture run: the fixture entry point with an open gate → `AuthorityError`.
- **DEP-15** The claim gate must likewise close before any fixture run, asserted **independently** so the two gates cannot cover for each other.
- **DEP-16** Gate closure is recorded in the manifest and content-addressed; a forged closed-gate record that did not satisfy the gate fails re-verification against `expected_root`.
- **DEP-17** `[SI]` + signature scan: no `reopen`, `force`, `override`, `skip_checks`, `unsafe`, or `allow_*` parameter anywhere in the public API.

### LIF — freeze lifecycle (16)

- **LIF-00** **Model, stated normatively.** `Draft`, `Frozen`, `Closed` are three **distinct immutable types**. Transitions **return new values**; nothing mutates a lifecycle wrapper, and there is no mutable `state` field to attack. Most illegal transitions are therefore **unrepresentable** (no such method) rather than raising.

3×3 truth table, from-state × requested-target:

| from \\ to | Draft | Frozen | Closed |
| --- | --- | --- | --- |
| **Draft** | identity; no method | `freeze()` → new `Frozen` | no method (must freeze first) |
| **Frozen** | **no method** (no thaw/unfreeze) | `freeze()` absent on `Frozen`; re-freeze idempotency is tested at `Draft` (LIF-10) | `close()` → new `Closed`, requires both gates satisfied |
| **Closed** | **no method** | **no method** | `close()` absent** [r3]** |

**[r3] Contradiction removed.** r2's final cell said `close()` was both absent and raising on replay. It is **absent** — `Closed` has no `close` attribute, asserted by `not hasattr`. Close-replay *raising* belongs to `FrozenInputSet.close()` (DEP-11), which is a different object with a different lifetime: `FrozenInputSet` is a mutable-until-closed accessor, not an immutable lifecycle value, so it is the one place where a replay can occur at all.

- **LIF-01**…**LIF-09** One assertion per cell: either the returned exact type, or `not hasattr(...)` for unrepresentable cells.
- **LIF-10** Idempotent re-freeze: `freeze()` twice from the same `Draft` → equal digests and byte-identical canonical bytes.
- **LIF-11** A `Draft` with changed content → different digest; a changed re-freeze cannot reuse the prior digest.
- **LIF-12** Mutating any field of `Frozen`/`Closed` raises **`FreezeError` by exact type** — not a leaked `dataclasses.FrozenInstanceError` or `AttributeError`.
- **LIF-13** All public value types immutable; returned collections are read-only proxies or tuples; mutation attempt raises, asserted per public type.
- **LIF-14** `[SI]` + signature scan: no public mutable default argument anywhere.
- **LIF-15** Result and measure types are `@final` and reject subclassing at class creation; asserted.

### RES — results, claims, and forged replay (15)

- **RES-01** The four result classes are pairwise disjoint: for one instance of each, exactly one of four `isinstance` checks is true (16 assertions).
- **RES-02** No result class subclasses another (12 assertions).
- **RES-03** **Dependency boundary — replaces r1's self-contradictory pair.**
  - **a** Runtime modules (all `.py` outside `tests/`) import **stdlib only** — AST scan.
  - **b** `tests/` modules **also** import stdlib only — no `pytest` import — so the same test bodies are collectible by pytest **and** importable and runnable by bare `python3` from `verify.py`. One source of truth, two runners.
  - **c** Exception assertions use `expect_exact(Expected, fn)` built on `type(exc) is Expected`. This is **stricter than `pytest.raises`**, which matches subclasses and would have let a subclass satisfy an exact-type requirement.
  - **d** `verify.py` imports no pytest.
- **RES-04** `Supported` requires manifest state `Closed`, both gates closed, **and** a manifest that verified **authoritatively against an out-of-band `expected_root`** (PRV-04). `AuthorityError` otherwise.
- **RES-05** `Supported` requires a non-empty attestation tuple containing at least `equivariance_not_tested` and `individual_selection_demonstrated_nonphysical_fixture`; omitting either raises.
- **RES-06** `[SI]` + surface scan: no `upgrade`, `promote`, `retry_as`, `assume`, or `as_supported` path from `NotTestable`/`Refused`/`Failed` to `Supported`.
- **RES-07** Every serialized result carries `"model_class":"nonphysical_fixture"` and `"physical_authority":"none"`; a caller passing either raises `AuthorityError`.
- **RES-08** Attribute scan over all public classes: no `physical`, `is_physical`, `derives_born`, or caller-supplied verdict field.
- **RES-09** **[r3]** `PermittedClaim` is a closed enum; out-of-enum → `AuthorityError`. **The membership is pinned in §6-A of this contract**, and the test asserts `{c.value for c in PermittedClaim} == <the literal 16-element set copied from §6-A>`. r2's version enumerated whatever the enum happened to contain, which constrained nothing — implementation and test could add an authority-bearing claim in step, leaving only the lexical backstop the rubric explicitly rejects. Because the literal now lives in the **contract**, the Evaluator can diff three independent copies: contract §6-A ↔ test literal ↔ enum. Collusion requires changing this reviewed document, which is visible.
- **RES-10** Forged replay: unknown field → rejected.
- **RES-11** Forged replay: missing required field → rejected.
- **RES-12** Forged replay: caller-supplied authority-field spoof → rejected.
- **RES-13** Forged replay: invalid claim value → rejected.
- **RES-14** **Forged `Supported` replay:** a serialized `Supported` whose manifest or gates do not independently re-verify is rejected — the deserializer **re-runs** manifest and gate verification rather than trusting the payload.
- **RES-15** Lexical claim tripwire over `.py`, `README.md`, and emitted result strings — **explicitly labeled a backstop.** The rubric names string-absence as fake safety; the guarantee is RES-04…RES-09 and MEA-18/19, which make a physical verdict inexpressible.
**[r3] RES-16…RES-19 are relocated verbatim to SEM-01…SEM-04.** The four RES numbers are **retired and never reused**, so a reader of the r2 review can follow them without ambiguity.

### SEM — selector semantics and ledger completeness (12)

r2 gave the two semantics distinct types and distinct domain tags and then never said what **complete** means in "deterministic-with-complete-noise-history". The Evaluator is right that distinct classes alone do not deliver the spec's selector split. `FixtureVersion` is the object that freezes exactly one semantics together with its ledger contract.

- **SEM-01** (was RES-16) `SelectorSemantics` closed two-member enum; declaring both → `SemanticsError`; declaring neither → `SemanticsError`.
- **SEM-02** (was RES-17) `NoiseHistoryLedger` and `KernelDrawLedger` are unrelated types; the wrong ledger for the frozen semantics → `SemanticsError`.
- **SEM-03** (was RES-18) The two ledgers carry different digest domain tags; a byte-identical payload yields different digests.
- **SEM-04** (was RES-19) Changing `SelectorSemantics` after freeze is unrepresentable / `FreezeError`.
- **SEM-05** `FixtureVersion` is an exact type carrying exactly one `SelectorSemantics`, its ledger, the frozen microstate space, the frozen `OutcomeCategorySet`, and its own content-addressed digest. It is immutable and participates in the `Draft → Frozen → Closed` lifecycle.
- **SEM-06** **Declared length and domain.** `NoiseHistoryLedger` declares its length `N` and its value domain up front. A history whose entry count ≠ `N` raises `SemanticsError` naming both numbers.
- **SEM-07** **No missing positions.** Entries are indexed `0…N-1`; a gap raises `SemanticsError` naming the first missing index. Asserted for a gap at the start, middle, and end (3 assertions).
- **SEM-08** **No duplicate positions.** A repeated index raises `SemanticsError` naming it — asserted at the raw-input level too (DEC-01 applies), since a Python mapping cannot represent the duplicate.
- **SEM-09** **Immutable ordered history.** The history is an ordered immutable sequence; mutation raises, and **reordering changes the digest** (this is a CAN-04 order-sensitive field, asserted explicitly here because "complete history" is meaningless if order is free).
- **SEM-10** **Every entry in the declared domain.** An entry outside the declared value domain raises `SemanticsError`.
- **SEM-11** **The primitive-kernel ledger cannot satisfy the completeness contract accidentally.** A `KernelDrawLedger` whose content is *shaped identically* to a valid noise history — same length, same indices, same values — is passed to the completeness validator and **raises `SemanticsError` on exact type**, before any content inspection. Structural coincidence is not a path in.
- **SEM-12** **And the converse:** a `NoiseHistoryLedger` passed where a `KernelDrawLedger` is required raises. The two directions are asserted separately so neither semantics is privileged as the default.

### RUN — runner, reproducibility, cleanup (15)

- **RUN-01** All seven mandatory build-index commands succeed with expected exit codes.
- **RUN-02** Supplemental Generator-host matrix (§1) reported as extra coverage only.
- **RUN-03** `-W error` produces **zero** warnings.
- **RUN-04** `python3 born_selection_equilibrium_fixture/verify.py` works with no package context; `verify.py` bootstraps `sys.path`.
- **RUN-05** Stdout of `-m …verify` and of `verify.py` are byte-identical.
- **RUN-06** `--json` is canonical and byte-identical across repeated runs and both `PYTHONHASHSEED` values.
- **RUN-07** **Meaningful planted failure:** `--prove-failure-exit` injects a **real invariant violation** — a manifest whose recomputed root does not match the held `expected_root` — and runs it through the **same** check pipeline as normal mode; exits `1` and **names the violated invariant** on stdout.
- **RUN-08** That same check **passes in normal mode**, asserting the difference is the injected input, not a separate code path.
- **RUN-09** `[SI]` `--prove-failure-exit` appears in no branch inside any check body; it selects an input fixture, never a code path. This is the check that makes RUN-07 evidence rather than theatre.
- **RUN-10** Exit codes `0` / `1` / `2`; `2` asserted with a bad flag.
- **RUN-11** Full run < 5 s wall clock; `[SI]` no sleeps, network, clock, or randomness in any check path.
- **RUN-12** **Cleanup:** epic-root tree snapshot identical before and after, ignoring `__pycache__` only. No temp files, no output artifacts.
- **RUN-13** `py_compile` and `compileall -q` clean.
- **RUN-14** **[r3]** **Evidence defined.** r2 said "same check IDs" without saying how that is observed, and the Evaluator is right that `pytest -q` does not print passing node IDs. The mechanism:
  - A single **shared registry** `CHECKS: Mapping[str, Callable]` in the test package maps check ID → callable. It is the only place a check is declared.
  - The bare runner iterates the registry and emits every ID with its result; `--json` includes the full ID list.
  - The pytest runner **generates one test function per registry entry** at module import (`test_<check_id>` assigned into module globals), so pytest cannot collect a different set.
  - **Evidence compared:** the ID list from `python3 -m …verify --json` versus the node-ID list from `python3 -m pytest --collect-only -q born_selection_equilibrium_fixture/tests`, both normalized to bare check IDs. Set equality is asserted, and the count is asserted equal to `len(CHECKS)`.
- **RUN-15** **The registry is the only declaration path.** `[SI]` + AST scan: no `test_*` function is defined literally in a test module outside the generator loop, and no check callable exists that is absent from `CHECKS`. A check cannot be written that only one runner sees.

### ONT — ontology neutrality (4)

- **ONT-01** `[`**r3]** `[SI]` + attribute scan: no type, field, parameter, or docstring encodes position, momentum, coordinates, trajectory, particle count, or wavepacket semantics. The microstate space is an abstract finite index set. **Mandated-label exemption, stated exactly so ONT-01 and ONT-02 can both pass:** the scan exempts exactly the identifier string `invalid_trajectory` and the docstring of the category constant that defines it. The exemption is a one-element allowlist, written as a literal in the test. Every *other* occurrence of trajectory vocabulary anywhere in the package — including any other identifier containing `trajectory`, and including that word in any other docstring — is banned.
- **ONT-02** `invalid_trajectory` is documented in its docstring as a **spec-inherited ledger category label** carrying no ontological commitment; the spec's name is preserved rather than unilaterally renamed.
- **ONT-03** Vocabulary scan over public API names and the full literal claim set (§6-A): nothing commits to point-particle **or** wave ontology. The harness admits either.
- **ONT-04** **The exemption is exactly one element wide.** A probe identifier `valid_trajectory` and a probe docstring containing "trajectory" are both introduced in a scratch module fed to the scanner, and both are **detected**. This proves ONT-01's allowlist is a single mandated label rather than a hole that whitelists the whole word.

### ERR — errors and clarity (5)

- **ERR-01** Hierarchy rooted at `HarnessError`: `SerializationError`, `MeasureError`, `NormalizationError`, `ProvenanceError`, `DependencyError`, `FreezeError`, `IsolationError`, `SemanticsError`, `AuthorityError`. Every check raises its specific type by **exact type**, never bare `ValueError`/`AssertionError`.
- **ERR-02** Every error message names the offending object and the violated rule; regex-asserted for a representative failure of each error class.
- **ERR-03** `README.md` states the measure/selector distinction, the hard boundary, and §5's limitation; policy is learnable without reading tests.
- **ERR-04** `__all__` in every module; nothing policy-relevant is private by accident.
- **ERR-05** Every public type's docstring states what it may **not** be used to conclude.

**Total: 196 named checks** — CAN 20, DEC 14, MEA 30, FLW 10, PRV 20, CMP 17, DEP 18, LIF 16, SEM 12, RES 15, RUN 15, ONT 4, ERR 5**.**

(r2 was 152. Net +44: three new groups FLW 10 / DEC 14 / SEM 12, of which SEM-01…04 are relocated from RES, plus MEA +6, PRV +2, CMP +2, RUN +1, ONT +1.)

## 8. Runner contract

```text
verify.py [--json] [--prove-failure-exit]
  exit 0  all checks passed
  exit 1  one or more checks failed (or --prove-failure-exit, which must fail)
  exit 2  usage error
```

Human output: deterministic ordered `<CHECK-ID>  PASS|FAIL  <name>` lines plus a summary. `--json` emits canonical bytes.

## 9. Checkpoint and state-log locations

The epic root is not a git repo, so checkpoints are content-addressed tarballs:

- `<epic-root>/autobuild-generator/checkpoints/` — pre-sprint and per-round tarballs.
- `<epic-root>/autobuild-generator/generator-state.json` — Generator breadcrumb log.

Both sit **outside** `born_selection_equilibrium_fixture/`, so the tree inspected for cleanup (RUN-12) is free of build-process residue.

## 10. Agreement record

**The contract is AGREED at r4, negotiation exchange 4 of 4.** Nothing below remains open; it is retained as the record of how the terms were reached.

| Exchange | Generator | Evaluator |
| --- | --- | --- |
| 1 | r1 proposed, 87 checks | REVISE — 6 blocking, 7 required additions |
| 2 | r2, 152 checks — all 13 accepted, 3 conceded as errors | focused REVISE — 3 blocking, 2 scope, 5 ambiguities |
| 3 | r3, 196 checks — all 10 accepted, 3 conceded | acceptable subject to 2 narrow corrections + editorial |
| 4 | **r4 — FLW-02 predicate closed, claims #5/#6 rescoped, editorial fixes** | **AGREED** |

Settled and not to be renegotiated: `expected_root` custody (Evaluator captures the clean root independently before mutations and never sources it from the attacked payload); distinct immutable lifecycle types with no raising stubs; stdlib-only plain tests with exact-type exception checks; rubric verdict semantics (addressable slices PASS/FAIL, deferred slices UNRESOLVED, **no 90/100 computed at Sprint 1**).

**Next move:** Generator checkpoints and builds, then hands the output to the Evaluator.

## 10-A. Prior open items — now closed

**Settled in exchange 2** (Evaluator decisions, recorded so they are not renegotiated): `expected_root` custody accepted with the stated limitation, and the Evaluator will capture the clean root independently before mutations and never source it from the attacked payload. Distinct immutable lifecycle types accepted; no raising stubs. Stdlib-only plain tests accepted. Rubric verdict semantics accepted — addressable slices PASS/FAIL, deferred slices UNRESOLVED, no 90/100 computed at Sprint 1.

**Outstanding for exchange 3:**

1. **§6-A membership.** This is the one place where a wrong call is expensive later, because every result-emitting code path is written against it. Sixteen members, ten of them refusals. If any member reads to you as authority-inflating — #5 and #6 are the ones I would attack, since they are the only non-refusal claims that touch equivariance — say so now and I will remove or rescope them in r4 rather than after the code exists.
2. **Standing request.** 196 is not a ceiling. Anything you intend to run that this does not already force me to defend, name it.

If r3 is acceptable, I checkpoint and build. Two negotiation exchanges are used; this is the third.
