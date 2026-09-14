# The Dirac–Kuramoto Framework

**A study into an interpretation of quantum mechanics based on wave realism, kept as a
complete record — including the mechanism it postulated, the tests that refuted it, and
the understanding that was gained instead.**

---

## What this repository is

This repository is a study into an interpretation of quantum mechanics based on wave
realism: the wave function is taken to be real, there is one world, and the question
asked was what physical process, if any, underlies the equations of quantum mechanics at
a measurement.

It was postulated that synchronization of Dirac spinors — phase locking of the chiral
sectors of the Dirac field to a detector's matter, by a mechanism such as Kuramoto or
Adler synchronization — could add to the mechanism underlying the equations of quantum
mechanics, and in particular could produce the Born statistics and the single outcome of
a measurement from dynamics rather than by postulate.

**That postulate was refuted.** All the tests run — exact calculations in the smallest
models containing the relevant physics, stochastic races among synchronizing clocks at
every criterion the ledger could name, and three rounds of adversarial review by AI
referees instructed to find the errors — failed to support any mechanism of phase shift
other than an immediate one: a detector site's phase relation to the wave is set from
the first instant by its detuning and return rate, commitment is a memoryless jump, and
the gradual approach of a synchronizing oscillator either gives the wrong statistics or
acts downstream of the event and touches nothing. The development of a phase-
synchronization mechanism is recorded as a negative result (`NEGATIVE_RESULT.md`), with
the predictions that were written before each test and the ones that were wrong.

What was left standing, after the mechanism went, is the projection postulate read
realistically at the decoherence crossover, honestly priced: real waves on configuration
space, a nonlocal projection, a foliation chosen rather than forced, and a Heisenberg cut
that is a crossover with a location and a width — all of it decoherence and open-systems
theory, and all of it said to be so.

**None of the papers here are for submission for publication.** They are the record of
one person gaining a better understanding of Dirac's equation and of the decoherence
interpretation of quantum mechanics, in collaboration with an AI, with the dead ends,
the corrections, the review rounds, and the learning kept together as the output.

Three things about the process are worth stating, since they are what the record shows:

- **The AI did the formalization, simulation, literature work, and drafting; the human
  supplied the physical questions and adjudicated.** Several of the corrections that
  mattered most came from the human's questions from outside the field — commitment at
  the absorption vertex, the shared-waveform picture that repaired the postulate, the
  two-absorber entanglement calculation.
- **Every test was pre-registered.** Definitions were fixed before they were applied,
  predictions were written before results were opened, and wrong predictions are scored
  as wrong in the same files as the right ones.
- **Adversarial AI review found what the authors had not.** Each frozen paper was
  reviewed by panels with byte-identical referee instructions and the findings
  classified against a ledger of anticipated criticisms committed in advance. The panels
  caught mislabelled thresholds, a postulate that failed for detectors reached at
  different times, a formula that failed in the regime it was quoted for, and misread
  sources; three rounds on the final paper converged on its status rather than on a
  passing version.

---

## The physics in one paragraph, as it ended

Written in the chiral basis, the Dirac equation exposes the fermion mass as the coupling
between two chiral phase sectors, and the programme asked whether that coupling, opened
to a dissipative detector, could lock and thereby select an outcome. It cannot: the
sub-threshold site has no autonomous phase to entrain, the locking race of self-sustaining
clocks gives an outcome exponent of 1.5 rather than Born's 2, reaches Born only when the
golden rule's structure is put in by hand, fails on narrow spectra and on staggered
arrival, and requires a nonlocal one-quantum constraint it does not supply. What the
exact models did establish is decoherence theory's own account with numbers attached: the
crossover at which irreversible capture sets in is coupling-set where the coupling exceeds
the record channel's rate and record-set where it does not; irreversibility needs a
record channel dense on the capture timescale; the carrier frequency enters only as a
Bloch–Siegert shift; a self-sustaining amplifier kinks the crossover and does not sharpen
it; and for a pair of absorbers the same machinery gives the three known shapes of
entanglement loss, including a finite-time death with nothing sharp at either site. The
selection itself remained a postulate — the quantum-jump unravelling of photodetection
read as what happens — and the programme's one result is that no detector dynamics, and
no synchronization substrate, could have done the choosing.

---

## The papers

| Paper | File | Status |
|---|---|---|
| **Paper 1 — A Field–Matter Selector for Outcome Production, Conditioned on a Detector Ready-State Measure** | [drafts/PAPER1_DRAFT_born_selection.md](drafts/PAPER1_DRAFT_born_selection.md) | **v0.11 (2026-09-14, late: consistency pass after the internal review round — stale front-matter claims withdrawn in place, the 2026-09-05 registration correction propagated, the "thousandth of the commitment time" figure withdrawn as established, A.7's amendment integrated, A.1 to A.4 corrected on what was reproduced, on the G1/G2 contract, on the Mandel-Q gloss, on the toy's wavelength lines and on Grangier 1986's photomultipliers, "independent" removed; claim-level decisions from the round not taken)** · v0.10 (2026-09-14: Addendum A — results of the MathX explorations bearing on this paper: the extreme-value rule of §4(a) completed, a decorrelation clause and its Fano-factor observable added to the actualization-law specification, reading A excluded at a balanced split conditional on sub-gap re-emission leaving the device; the refined microscopic model of MathX `MODEL_SECTION.md` §12 stated and mapped onto Paper 3 §4.1's three stages as the candidate replacement for the selection stage; corroborations of P5, Theorem 2 and §7 from an independent construction; §§1–9 unchanged; reopens the record closed 2026-09-05 at the sponsor's instruction; PDF not yet rebuilt)** · v0.9 (2026-09-02: v0.8 corrected the §6.1 timescale ladder against the paper's own definition of commitment and withdrew the v0.7 demotion of Theorems 4–5; v0.9 adopts reading B of the share ontology — amplitude bookkeeping that becomes energy only at the whole-quantum vertex — after the threshold-gated alternative was quantified in the paper's own engine and found to over-predict; see [drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md](drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md), E-16 and open items 2a, 2b, 5). Retitled at v0.6; the former title, *The Born Rule as a Derived Fair Game*, was withdrawn with the derivation claim it asserted. Reviewed 2026-07 (panel: GPT-5 Codex, Gemini, SuperGrok + internal reviewer, down-weighted); round record in [born_selection_AI_review_2026-07/](born_selection_AI_review_2026-07/) |
| **Paper 2 — The Heisenberg Cut as a Physical Threshold** | [drafts/PAPER2_DRAFT_heisenberg_cut.md](drafts/PAPER2_DRAFT_heisenberg_cut.md) · [PDF](Heisenberg_Cut_v0.4.pdf) | v0.4 (2026-09-04: first microscopic test of the recoverability criterion, predictions on record — [heisenberg_cut_recoverability/](heisenberg_cut_recoverability/RESULTS.md); location claim survives, width restated). Reviewed 2026-07 at v0.3; round record in [heisenberg_cut_AI_review_2026-07/](heisenberg_cut_AI_review_2026-07/) |
| **One World, One Cut** (short form — not for submission; the final statement of the interpretation, three review rounds recorded) | [drafts/PAPER_one_world_one_cut_SHORT.md](drafts/PAPER_one_world_one_cut_SHORT.md) · [PDF v1.5](One_World_One_Cut_short_v1.5.pdf) · [v1.4](One_World_One_Cut_short_v1.4.pdf) · [v1.3](One_World_One_Cut_short_v1.3.pdf) · [v1.2](One_World_One_Cut_short_v1.2.pdf) · [v1.1](One_World_One_Cut_short_v1.1.pdf) · [v1.0 frozen](One_World_One_Cut_short_v1.0.pdf) | v1.5 (2026-09-05: two statements added — virtual particles as bookkeeping of the evanescent amplitude whose effects are phase shifts, the jump being real; and phase alignment playing no role in selection. v1.4: §4.6, the cut for a pair — entanglement loss under three noises, scored against Yu–Eberly and Levitt; the two corrections of fact from the third review round applied; the rest of that round unapplied by the sponsor's decision), revised after the four-reviewer internal round in [one_world_one_cut_AI_review_2026-09/](one_world_one_cut_AI_review_2026-09/): the postulate restated as the quantum-jump unravelling read as ontic after the record's own model falsified the v1.0 hazard for staggered arrival; the cut's location given its regime (coupling-set for Γ ≪ K, record-set for Γ ≫ K); the in-principle claim conceded; the transactional comparison rewritten against the sources; frame tests withdrawn; the paper's one result stated as a no-go |
| **One World, One Cut** (long form — the paper of record for how every number was obtained; not for submission) | [drafts/PAPER_one_world_one_cut.md](drafts/PAPER_one_world_one_cut.md) · [PDF](One_World_One_Cut_v1.0.pdf) | v1.0 draft: the interpretation without synchronization — real waves, one world, a located cut, selection at absorption as a postulate; the transactional interpretation placed as nearest neighbour |
| **Paper 3 — One Mechanism at Two Scales** (superseded) | [drafts/PAPER3_DRAFT_dk_framework.md](drafts/PAPER3_DRAFT_dk_framework.md) | v0.1, **frozen 2026-09-04 as the record of the synchronization program**; was: draft in progress; pre-freeze consistency check ledgered in [drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-01.md](drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-01.md) (round 1, independent) and [drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-31.md](drafts/TRIPAPER_CONSISTENCY_LEDGER_2026-08-31.md) (round 2, propagation of Paper 1 v0.7) |
| **The Many Clocks Interpretation** (predecessor) | [current_revision_DK_paper.md](current_revision_DK_paper.md) | v8, **frozen as the provenance record** — the program's original main paper (externally submitted solo-byline to Foundations of Physics, declined 2026-07; that decline closed the conventional-journal track). Superseded by Paper 3; retained unrevised. |

The papers are a sequence in time, not a programme for submission: Paper 1 developed the selection game and is now the recorded negative result; Paper 2 located the cut and was tested into its final, decoherence-compatible form; Paper 3 assembled the synchronization framework and is frozen as its record; the single paper *One World, One Cut* is what survived the tests and three review rounds — an interpretation, priced, that claims no prediction beyond quantum mechanics. Earlier long-form versions ([PAPER_UNIFIED.md](PAPER_UNIFIED.md), [paper.pdf](paper.pdf)) are retained as the first-version record.

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

**Status of the Born-selection program (2026-09-04): a negative result, recorded on
purpose.** The attempt to derive the Born square from a microscopic mechanism in a
real-wave substrate did not succeed: the substrate produces the square only by containing
a commitment process with the golden rule's structure and a nonlocal one-quantum
constraint, neither of which it derives. What was learned, what failed, and what remains
are stated plainly in [NEGATIVE_RESULT.md](NEGATIVE_RESULT.md); the papers below carry
their de-claimed boundaries.

A plain-terms glossary of the program's physics, simulation and statistical vocabulary,
with medical and statistical relatives, is at [GLOSSARY.md](GLOSSARY.md).

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
- Paper 1 no longer claims (as of v0.9) that the selection game supplies the Born
  frequencies. With reading B of the share ontology adopted — a sub-threshold holding is
  an amplitude, and commitment is available from every site at a hazard linear in its
  share — the frequencies enter through that linearity (P1 with Theorem 5), Theorem 4
  makes the commit speed irrelevant, and the exchange game's theorems state what the
  substrate must not do to the shares before commitment. The alternative reading, in
  which the gap gates commitment, was quantified in the paper's own engine and
  over-predicts. What the substrate still owes is the actualization law itself — which
  site fires, in one world, with hazard linear in its share — tested in Paper 3's
  program, not in Paper 1. A first diagnostic-budget test of that law, the two-channel
  Adler race ([adler_two_channel_exploratory/RESULTS.md](adler_two_channel_exploratory/RESULTS.md),
  2026-09-02), gives a coupling exponent of 1.56 [1.44, 1.69] at the frozen criterion,
  neither linear nor quadratic, and criterion-dependent; the plan's positive control, an
  inverse-coupling dwell, overshoots to 3.8 [3.5, 4.2], and a tuned dwell scaling as the
  inverse quarter power of the coupling lands on 2.00 [1.84, 2.16] — a fitted criterion,
  not a mechanism. The race as specified does not supply the law, and Born sits between
  its two natural criteria. The tolerance and spectral sensitivities leave the exponent
  between 1.6 and 1.8 and show the race scaling as tongue width times the square root of
  the rate. The missing half power is entry-time order statistics: the race's
  deterministic skeleton with no noise reproduces the exponent, because the fastest of N
  near-deterministic Adler slides gains only logarithmically in N where a Poisson race
  would gain a full power. A Born-producing race needs memoryless per-site
  commitment with hazard proportional to the local locking rate, which is the golden
  rule in the substrate's language — and run as a variant, with the Adler clock's own
  power law and no inserted square, that is what it produces: an exponent of 2.16,
  within about 0.02 of Born at every angle, the square arising as tongue width times
  locked absorption rate. A lagged-hazard sweep shows the result indifferent to the
  hazard's timing and sensitive only to its form, so what a detector must supply is a
  stochastic commitment linear in absorbed energy at the absorption vertex, which both
  detector families have; the deterministic cascade downstream carries no which-site
  weight. The selection is one-world, not an ensemble rate: independent site rates give a
  coincidence ratio of 1 at a balanced split against the observed 0.002, and the
  one-quantum stop reproduces the data only if it acts within about a thousandth of the
  commitment time, orders of magnitude faster than light could cross the port
  separation — the nonlocal constraint P5, which nothing here derives. The production
  budget remains unrun.
  *(2026-09-14: the "thousandth" is a bound from the discarded race model on a dynamical stop
  the projection does not have — One World, One Cut v1.5 §5.1; Paper 1 v0.11 A.4. Kept as history.)*
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
