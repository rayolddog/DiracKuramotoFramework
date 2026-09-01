---
title: "Independent repair closure review — quantum-equilibrium selection revision"
kind: review
---

# Independent repair closure review — quantum-equilibrium selection revision

## Verdict

**PARTIAL CLOSURE.** The repaired [revision plan](..) closes the central conceptual defects: it treats the microstate preparation measure and quantum outcome measure as different objects on different spaces; reserves equivariance for a same-space flow; quarantines fixture code; and installs substantive anti-circularity, invalid-event, blinded-holdout, equivalence, nonequilibrium, negative-control, representation, and material-substitution requirements.

It is safe as a research-governance plan for tightly bounded nonphysical fixture work after the fixture gates actually close. It is not yet an executable physical-selection contract, manuscript authority, conditional-compatibility result, equilibrium-preservation result, or Born derivation.

Two operational repairs remain before the gate sequence itself can be called closed:

1. Phase II says to begin “after all gates close,” but G8 is the conditional analysis performed in Phase II. The sequence must be `G0–G7 close -> frozen run -> G8 analysis`, with any post-G5 dependency change invalidating the version and returning it through the affected gates.
2. The bounded result vocabulary has no unambiguous outcome for a completed equivalence test that fails. `conditional_outcome_compatibility_refused` does not distinguish refusal to test from tested incompatibility, despite the abstract obligation to report “passed, failed, or unresolved.” Add and define a result such as `conditional_outcome_compatibility_failed_for_frozen_domain`; likewise define the negative nonequilibrium result rather than listing only support.

## Remaining findings

### High — G8 is circularly sequenced and cannot encode an empirical failure

The gates are advertised as ordered and fail closed, but Phase II begins only “after all gates close” even though G8 is the analysis of the Phase II ledger. G8 also points to the result vocabulary, where the only conditional-compatibility states are `not_testable`, `refused`, and `supported_for_frozen_domain`. A properly run equivalence test can be testable, accepted for analysis, and fail; the enum cannot state that result without overloading “refused.” This is an implementability defect, not a physics objection.

**Required repair:** state that G0–G7 authorize a versioned physical raw run, G8 analyzes that immutable ledger, and any dependency change reopens G5 and every downstream gate. Define `refused`, `not_testable`, `failed`, and `supported` as disjoint outcomes. Add the analogous bounded negative state for the nonequilibrium campaign.

### High — the current Paper 1 remains directly contradictory and therefore non-authoritative

The current [Paper 1 draft](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:1) still calls the result a “Derived Fair Game”; claims physical fairness, ordinary-dynamics operation, and exact broader statistics in its abstract; says the Born weight is nowhere inserted by hand; calls the measurement postulate redundant; presents P1–P4 as standard detector physics; labels this work's fairness “derived”; says the DK framework already realizes the premises; and ends with fairness “proved rather than postulated.” Those claims conflict with the repaired plan's explicit imported-measure premise, fixture/material gates, one-event scope, and stop status.

The conflict is contained only because the revision plan blocks manuscript authority and requires a new scoped draft after its readiness conditions close. Until then the current draft must be treated as historical/non-authoritative for this program; no sentence in it can establish a gate.

### Medium — selector semantics are safely contained but not yet chosen

The plan correctly distinguishes a deterministic map conditional on a complete noise history from a primitive stochastic kernel and forbids switching descriptions. It also correctly says `F_DK` is only a placeholder. But it still opens with the deterministic event notation and later calls a deterministic or stochastic object a “map `F_DK`.” Before G3 can close, the versioned dependency contract should state one `selector_semantics` value, identify whether noise histories belong to `lambda`, and use either `F` or `K` consistently throughout raw generation, refinement, and analysis.

### Low — fixture authorization wording should match the fail-closed rule

Phase I says G0 and G5 need only be “defined,” while the gate table requires closure, and it calls the fixture inputs “fixed physical equations.” Replace this with fixture-scoped G0/G5 **closure** and “fixed fixture equations/parameters.” The structural prohibition on serializing a physical selector or physical conclusion is otherwise strong and sufficient.

## Prior finding dispositions

| Prior finding | Disposition | Closure adjudication |
| --- | --- | --- |
| 1. Undefined microstate probability space can contain the answer | **CLOSED as a planning defect; scientific contract remains open** | The plan distinguishes `(Lambda, Sigma_Lambda)` from outcome space, requires a normalized joint law, provenance, support, correlations, and state-dependence audit, and stops outcome simulation with `microstate_measure_undefined`. It intentionally does not pretend the contract has been supplied. |
| 2. Cross-space pushforward was mislabeled equilibrium preservation | **CLOSED** | Q2 is now conditional outcome compatibility; equivariance is reserved for `(T_t)#mu_micro` on the microstate space. No outcome-frequency test is allowed to prove preservation. |
| 3. `F_DK` may encode the actuality postulate | **PARTIAL** | The plan now rejects returned labels, threshold stops, primitive draws, and pre-actual registries unless physical currents, quench, exclusivity, and routing follow. G3 fails closed. The actual ontology and deterministic-versus-stochastic law remain deliberately unchosen, so physical selection is still open. |
| 4. Firewall lacked an auditable dependency contract | **CLOSED at specification level** | The content-addressed manifest covers preparation, correlations, couplings, thresholds, exposure, hazards, invalid events, state generation, sample size, and numerical tolerances; raw/comparator isolation and version invalidation are explicit. |
| 5. Tests did not distinguish compatibility from target fitting | **CLOSED at specification level** | The repair adds sealed adversarial holdouts, one shared detector-ready law and parameter set, equivalence margins, non-outcome calibration, preregistered nonequilibrium surfaces, mechanism-breaking controls, and independently measured material substitutions. |
| 6. Dirac–Kuramoto was not shown load-bearing | **CLOSED as a label/authority defect; physical evidence remains open** | Neutral “field–matter selector” and “phenomenological phase-reduction fixture” labels are mandatory until spinor structure, an autonomous phase, reduction, validity range, and commitment current are derived. Photon spin-1/helicity and quaternion representation caveats are explicit. |
| 7. Active manuscript asserted unearned physical conclusions | **PARTIAL** | The plan now orders those claims removed and blocks a revised draft until the readiness contract closes. The live Paper 1 file still makes the contradictory claims, so manuscript authority remains open and blocked. |
| 8. Existing Adler implementation could be promoted | **CLOSED** | Existing Adler code is fixed at `machinery_only` and `numerical_no_result`; pre-G1–G4 work must be nonphysical and structurally unable to emit a physical conclusion. |
| 9. Result vocabulary lacked exposed-contract failure states | **PARTIAL** | Ontology, measure, material, numerical, test-contract, fixture, and equivariance states are now present. A completed-but-failed compatibility result and a bounded negative nonequilibrium result are still missing, and `refused` is undefined. |

## Strict authorization verdicts

| Work or claim level | Verdict | Reason |
| --- | --- | --- |
| **Bounded nonphysical fixture work** | **CONDITIONAL GO** | Only after fixture-scoped G0 and G5 close, comparator access is absent, raw ledgers contain no probability verdict, and outputs are structurally unable to serialize physical authority. Existing Adler results remain machinery only. |
| **Physical implementation / physical raw run** | **NO-GO** | G1–G4 are not substantively closed: there is no selected ontology, completed preparation measure, physical one-record selector, or material reduction. G5–G7 must also close for the exact version before a run. |
| **Manuscript revision carrying scientific results** | **NO-GO** | The plan's readiness conditions are unmet and the current draft contradicts the repaired claim boundary. A new scoped draft may start only under the plan's stated readiness rule. |
| **Conditional outcome-compatibility claim** | **NO-GO now** | It becomes eligible only after G0–G7 close, the immutable ledger is analyzed at G8 without retuning or postselection, and the vocabulary can represent both failure and support over the frozen domain. |
| **Full Born derivation** | **REFUSED / NO-GO** | The quantum outcome comparator and microstate measure are premises, and Q4 has no independently reviewed typicality, uniqueness, equivariance, or relaxation result. Q2 success would not change this verdict. |

## Cross-document consistency

- The revised [author clarification](../../author-clarification-three-paper-foundation) agrees with the two-space, conditional-selector architecture and labels its detector cascade as proposed planning guidance.
- JAI-10 in the [candidate ledger](../../author-ai-update-candidates) agrees that the direction is accepted only for planning and that manuscript and physical implementation remain gate-blocked. JAI-09 remains fixture history.
- The [historical final synthesis](../../final-synthesis) is compatible when read as provenance: its martingale result is a conditional theorem and its ontic stakes, winner gating, registry flow, and specific Dirac role remain “derive before claiming.” It cannot supersede the newer gates.
- The current Paper 1 is the only direct contradiction in the reviewed set. Its status must remain historical/non-authoritative until replacement.

## Closure statement

No remaining hidden Born route was found in the repaired dependency, invalid-event, holdout, negative-control, nonequilibrium, representation, or material-substitution rules. The remaining defects are bounded and repairable: fix the G8 sequence and result enum; make fixture closure wording exact; and choose one selector semantics only when G3 is actually attempted. Until those changes and the substantive gates close, the plan's own final status is correct: microstate contract open, physical selector not demonstrated, conditional compatibility not testable, equivariance not demonstrated, and no Born derivation.
