# The Dirac–Kuramoto Framework

**A research notebook: one physics program, developed and adversarially reviewed in
human–AI collaboration, with the full record kept.**

---

## What this repository is

This repository is a **research notebook** — the recorded steps and progression of an
attempt to build a framework that helps understanding of quantum mechanics. It is
deliberately not a polished artifact: the papers, the framework notes, the dead ends,
the adversarial review rounds, the corrections, and the revisions are all here,
because the record of *how the understanding was reached* is treated as a first-class
output alongside the physics itself.

It is also, candidly, a demonstration of something beyond the physics:

- **How AI accelerates research.** The formalization, theorem-proving, simulation,
  literature work, and manuscript drafting throughout this program were performed by
  AI in collaboration with a human researcher — at a pace and breadth a single
  independent researcher could not otherwise reach.
- **How AI educates the researcher.** The collaboration runs in both directions: the
  discussions recorded here repeatedly show a concept being tested, a misconception
  being corrected, and the research direction being sharpened as a result. The human
  author's internal model of the physics is a product of this repository as much as
  the papers are.
- **How adversarial AI review disciplines the work.** Each paper is frozen and
  submitted to a multi-model review panel (independent AI labs, byte-identical
  referee instructions, findings pre-registered before reading the reports, verbatim
  reviews and author responses published in the round folders). The panels have
  twice demonstrated that *reproducible is not the same as correct*, and their
  findings drove substantive corrections — including one reviewer independently
  re-running a public simulation script and catching a mislabeled threshold.

The authors' own assessment, stated plainly: **the Dirac–Kuramoto framework itself
may never become an accepted physics construct — but the process of research
facilitated by AI is already established practice.** What this repository adds is
the complete, honest, end-to-end record of that process: papers, reviews,
corrections, and the learning itself, kept together.

---

## The physics in one paragraph

Written in the chiral (Weyl) basis, the Dirac equation exposes the fermion mass as
the off-diagonal coupling between two chiral phase sectors: **K = m**. Closed and
unitary, that coupling can only precess — it provably cannot lock, which is why
isolated superpositions survive. Opened to a dissipative bulk, the same coupling
acquires an Adler/Kuramoto attractor — and that locking, the framework argues, is
what measurement *is*. From this one identification the program develops: the Born
rule as the statistics of a **proved fair game** among detector absorber sites
(Paper 1); the Heisenberg cut as a **physical threshold with a computable location
and width** (Paper 2); and a synthesis in which persistence (virtual→real) and
classicality (quantum→classical) are one locking mechanism at two scales (Paper 3,
in draft). Every claim is conditional on stated premises, every deviation channel is
ledgered, and the framework's one exotic commitment — a preferred frame entering
through the measurement sector only — is carried openly and given a test program.

---

## The papers

| Paper | File | Status |
|---|---|---|
| **Paper 1 — A Field–Matter Selector for Outcome Production, Conditioned on a Detector Ready-State Measure** | [drafts/PAPER1_DRAFT_born_selection.md](drafts/PAPER1_DRAFT_born_selection.md) | v0.7. Retitled at v0.6; the former title, *The Born Rule as a Derived Fair Game*, was withdrawn with the derivation claim it asserted. Reviewed 2026-07 (panel: GPT-5 Codex, Gemini, SuperGrok + internal reviewer, down-weighted); round record in [born_selection_AI_review_2026-07/](born_selection_AI_review_2026-07/) |
| **Paper 2 — The Heisenberg Cut as a Physical Threshold** | [drafts/PAPER2_DRAFT_heisenberg_cut.md](drafts/PAPER2_DRAFT_heisenberg_cut.md) | v0.3. Reviewed 2026-07; round record in [heisenberg_cut_AI_review_2026-07/](heisenberg_cut_AI_review_2026-07/) |
| **Paper 3 — One Mechanism at Two Scales** (framework synthesis) | [drafts/PAPER3_DRAFT_dk_framework.md](drafts/PAPER3_DRAFT_dk_framework.md) | v0.1 draft, in progress; pre-freeze consistency check ledgered in [drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-01.md](drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-01.md) (round 1, independent) and [drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-31.md](drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-31.md) (round 2, propagation of Paper 1 v0.7) |
| **The Many Clocks Interpretation** (predecessor) | [current_revision_DK_paper.md](current_revision_DK_paper.md) | v8, **frozen as the provenance record** — the program's original main paper (externally submitted solo-byline to Foundations of Physics, declined 2026-07; that decline closed the conventional-journal track). Superseded by Paper 3; retained unrevised. |

The three papers form a deliberate sequence: Paper 1 argues the selection statistics
from detector premises — conditional outcome compatibility over a tested domain, not
a derivation of the Born measure; Paper 2 consumes one theorem of Paper 1 and locates
the classical–quantum boundary; Paper 3 assembles the framework, prices every premise,
and consolidates the open problems. Earlier long-form versions
([PAPER_UNIFIED.md](PAPER_UNIFIED.md), [paper.pdf](paper.pdf)) are retained as the
first-version record.

**Why no journal?** The program's honest bylines credit the AI's intellectual
contribution directly (see [AUTHORSHIP.md](AUTHORSHIP.md) and
[CITATION.cff](CITATION.cff)), with a named human as accountable sponsor. Standard
editorial policy holds that an AI cannot be an author; the solo-byline alternative
was tried and declined. The trio is therefore published here — papers, verbatim
adversarial reviews, and revisions together — as the proceedings of one research
program, which no journal format could carry anyway.

---

## The review process

Each review round follows the same instrument: the manuscript is frozen (PDF +
tag), a byte-identical critical-referee rubric goes to a panel of independent
frontier models from different labs, the authors pre-register an
anticipated-findings ledger *before* reading any report, reviewer access modes are
recorded, and the verbatim reviews, the classification of findings against the
pre-registered ledger, and the authors' response are all published in the round
folder. The internal reviewer (same model family as the AI author) is disclosed and
down-weighted; its scores have landed inside the external range in both rounds.
Recurrent meta-findings across rounds: **reproducible ≠ correct** (twice), and
reviewer access mode correlates with finding severity (twice). Cross-round
corrections propagate with attribution — e.g., a Paper 2 panel finding (N2) forced a
rename and status clarification in Paper 1.

A second instrument runs alongside the frozen-manuscript rounds: **multi-model debate
and adversarial pressure-testing**, orchestrated across models from different labs and
archived in [traycer_artifacts/](traycer_artifacts/). It is continuous rather than
round-based, and it operates on plans and claims rather than finished manuscripts. Its
largest output to date is the quantum-equilibrium selection revision and its two
independent pressure tests, which forced the separation of the quantum outcome measure
from the microstate preparation measure, installed the gate ladder now used to price
the program's claims, and produced the finding that the previous Paper 1 draft was
"directly contradictory and therefore non-authoritative" against its own revision plan.
Consistency across the trio is tracked separately in the ledgers; round 2 (2026-08-31)
is labelled a *propagation* round rather than an audit, because it was performed by the
same agent that made the revisions it propagates.

---

## Repository map

| Location | Contents |
|---|---|
| [drafts/](drafts/) | The three papers; framework notes (`NOTE_*.md` — the exploration layer feeding the papers); derivations; outlines; the plain-language [GLOSSARY.md](drafts/GLOSSARY.md); consistency ledgers; and the gate contracts `CONTRACT_G1_G2_*` (microstate ontology and preparation measure — proposed closure, not independently reviewed) and `CONTRACT_G3_*` (physical selector — **open**; the commitment current is absent) |
| [born_selection_AI_review_2026-07/](born_selection_AI_review_2026-07/), [heisenberg_cut_AI_review_2026-07/](heisenberg_cut_AI_review_2026-07/) | Complete review rounds: frozen PDFs, panel prompts, verbatim reviews, pre-registered findings ledgers, author responses |
| [EQUATIONS.md](EQUATIONS.md) | Compact equation reference |
| `tests/`, `paper2_sims/`, `two_station_sims/`, `born_selection_sims/`, `code/`, `results/`, `resolution/` | Numerical verification (seeds pinned; failing configurations retained as diagnostics) |
| [g3_drain_tests/](g3_drain_tests/) | Probes behind the G3 contract: whether a registration "drain" preserves Born statistics (it does as a sink opening on commitment, and does not as an attractor pulling during competition), and whether the field-derived exchange kernel gives Born where the manuscript's ad hoc `min` rule does |
| `adler_born_two_channel/`, `first_mark_two_absorber/`, `hologram_phase_test/` | Mechanism-feasibility simulation packages. Status `machinery_only` / `numerical_no_result` — **not** evidence of individual selection or of a Born derivation, and not promoted by any revision |
| [traycer_artifacts/](traycer_artifacts/) | One-way mirror of the multi-model debate, plan, and review artifacts that Traycer keeps in its own store; refresh with [sync_traycer_artifacts.sh](sync_traycer_artifacts.sh). Mirrors drift — the store is authoritative |
| [LIGO_SIDEREAL_TEST_T5.md](LIGO_SIDEREAL_TEST_T5.md), [SIDEREAL_DECOHERENCE_PAPER.md](SIDEREAL_DECOHERENCE_PAPER.md), [AB_VISIBILITY_PAPER.md](AB_VISIBILITY_PAPER.md), [COSMIC_EXPANSION_PAPER.md](COSMIC_EXPANSION_PAPER.md), [DISCRETIZATION_AS_SYNC_PAPER.md](DISCRETIZATION_AS_SYNC_PAPER.md), [EMERGENT_FIELDS_PAPER.md](EMERGENT_FIELDS_PAPER.md) | Companion and spinoff drafts — **development phase, not for citation** |
| [build_pdfs.sh](build_pdfs.sh) | Pandoc + xelatex build script for all manuscripts |

---

## The central result

In the Weyl basis the Dirac equation separates into two coupled equations whose
single off-diagonal entry is the mass — the coupling **K = m** between the chiral
sectors. The Madelung (polar) reduction in the rest frame gives

```
d(phi_L)/dt = -K * sqrt(rho_R/rho_L) * cos(phi_R - phi_L)
d(rho_L)/dt = +2K * sqrt(rho_L * rho_R) * sin(phi_R - phi_L)
```

— the *cosine in the phase equation*, the reverse of the Kuramoto model: no
attractor, no locking, coherent normal-mode precession only (the de Broglie carrier
and the zitterbewegung beat, rest-frame splitting 2mc²/ℏ). The would-be synchronizer
has an off-switch, and the switch is the closed/open boundary: genuine Adler/Kuramoto
locking enters only when the system opens to a dissipative bulk — proposed as the
measurement step, and the least settled claim in the program: no autonomous oscillator
capable of Adler locking has been documented in a passive absorber, and the
superconducting detectors that do carry one commit by an Arrhenius barrier rather than
the occupation-linear law the mechanism wants (see the G3 contract). The Higgs vacuum expectation value sets K for each species
(K = y_f·v/√2 = m); the photon, with no chiral coupling, is the framework's K = 0
limit — no internal clock, no lock, classical only by occupancy.

---

## The state of the model

The three papers propose the steps a complete microscopic model of detector selection
would include: capture, a fair competition that sets the odds, and commitment at a
locking threshold with a computable location and width. **The model is not complete.**
The commitment current and the quench are absent, material authority is open, and the
framework layer that would supply them requires an autonomous oscillator that has not
been documented in any passive absorber. Whether these are the right steps is what the
program is proposing, not what it has established.

The trio is not one model in three parts, and it is more useful read as two things of
different maturity. Papers 1 and 2 cohere tightly — Paper 2 consumes Paper 1's Theorem 2
and locates the cut at the layer where an autonomous phase can first emerge — and both
are generic field–matter physics; neither requires Dirac structure. Paper 3 adds the
Dirac–Kuramoto ontology on top, which the first two do not need. A complete microscopic
model of measurement would need Papers 1–2's steps if the program is right; whether it
also needs Paper 3's is a separate open question, and Paper 1's success would not by
itself count as evidence for the framework.

The incompleteness bites at the joint between them. The missing commitment current — the
step from *one site holds ħω* to *one site has registered* — is where a clock mechanism
would have to do real work, and it is empty from both sides. Its gate contract is
[drafts/CONTRACT_G3_field_matter_selector.md](drafts/CONTRACT_G3_field_matter_selector.md),
and it stands open.

---

## What this framework does not claim

- It does not modify the Dirac equation, the Born rule's numerical content, or
  Bell's theorem.
- Paper 1 does not derive the *square* (that is Gleason's theorem plus
  driven-oscillator energetics), and as of v0.7 it does not claim to derive the Born
  measure at all. It offers a candidate *selection process*, conditional on stated
  detector premises including wave realism, and tests whether that process is
  compatible with the Born comparator over a tested domain.
- Paper 1 supplies, at most, the selector half of a larger theory. The quantum outcome
  measure is adopted as a comparator and the microstate preparation measure is an
  explicit premise; neither is derived there.
- Producing exactly *one* record — exclusivity, quench, and the routing of the losing
  sites' energy — is owed by the selection dynamics and is discharged nowhere in the
  trio. The gate contract for it stands open at
  [drafts/CONTRACT_G3_field_matter_selector.md](drafts/CONTRACT_G3_field_matter_selector.md).
- Paper 2's cut location rests on a physically motivated ansatz (κ_ret = ΔE/ℏ) whose
  microscopic derivation is an open problem, logged as such.
- The preferred frame is a real commitment, carried openly and given falsification
  channels rather than hidden. Earlier drafts described it as confined to the
  multi-quantum and entangled sectors; v0.7 withdrew that. A single quantum whose
  candidate registration sites are spacelike separated — a beam-splitter — consumes it
  too, because exclusivity is a constraint on an energy ledger closed across the
  separation.
- The consolidated open-problem ledger is Paper 3 §7.3; nothing there is glossed.

---

## Development history

The program evolved from
[BellWithoutFasterThanLight](https://github.com/rayolddog/BellWithoutFasterThanLight)
(Bell correlations via local clock synchronization), through the Many Clocks
Interpretation main paper and its three-lab review cycle (2026-06), into the present
three-paper sequence with per-paper adversarial rounds (2026-07–). The discussions
behind the notes — where misconceptions were corrected and directions sharpened —
are summarized in the `NOTE_*.md` files; the notebook's structure is the history.

## Inspirations

- **de Broglie** — pilot wave; the wave is real
- **Bohm** — a definite world beneath the statistics
- **Dirac** — the equation that started it all
- **Schrödinger** — the wave realism this program re-litigates, and the discoverer
  of the zitterbewegung it couples
- **Kuramoto** — phase synchronization of coupled oscillators (1975)
- **Adler** — locking phenomena in oscillators (1946)
- **Bell** — rigorously identifying what any local theory must satisfy
- **Penrose** — objective reduction; the zig-zag picture of mass

---

## About

Developed in sustained collaboration between **John M. Bramble, MD** — a radiologist
whose physical intuitions (measurement as re-synchronization; MRI relaxation as
recovery toward a bulk reference; the diffused-hologram reading of detector noise)
originate the program and who adjudicates every scope and interpretation decision as
accountable sponsor — and **Claude (Anthropic)**, across model generations, which
performed the formalization, proofs, simulations, literature work, and prose.
Authorship, per-paper bylines, and the honest-authorship rationale are documented in
[AUTHORSHIP.md](AUTHORSHIP.md) and [CITATION.cff](CITATION.cff).

> *"In many ways, the paper is the history of my learning how to turn the concepts
> into real physical principles — an exploration of physical concepts forming a
> framework."* — JB, 2026-08

---

## License

[MIT](LICENSE)
