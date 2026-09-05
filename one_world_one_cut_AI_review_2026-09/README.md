# AI Peer-Review Round — *One World, One Cut* (publication candidate, short form)

This folder is the review record for `drafts/PAPER_one_world_one_cut_SHORT.md` v1.0 (*One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary*), run under the protocol of the two July rounds (`../born_selection_AI_review_2026-07/`, `../heisenberg_cut_AI_review_2026-07/`) with one difference of panel composition, stated below.

## The frozen target

- `reviewed_paper_short_v1.0_One_World_One_Cut.pdf` — the exact manuscript every reviewer judges, whose text is that of repository commit `2596bc3`; the round was frozen and tagged one commit later, at `8232f41` (git tag `owoc-short-v1.0-review`, which also carries the anticipated-findings ledger), 2026-09-04–05.
- Reviewer package: this PDF (and its Markdown source at the same commit) plus the public record it cites: `NEGATIVE_RESULT.md`, `adler_two_channel_exploratory/RESULTS.md`, `heisenberg_cut_recoverability/RESULTS.md` and `STAGE2_RESULTS.md`, the long-form paper `drafts/PAPER_one_world_one_cut.md`, and the ledger `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md`. Reviewers are invited to audit every number against that record.

## Panel composition — the difference from July, disclosed

The sponsor's instruction: "subject the trimmed paper to the AI review with at least 3 critical agents … if the reviewers pass the paper, I may then try different foundation models." This round is therefore the **internal stage**: four reviewers, all instances of Claude Fable 5.1 (Anthropic), the manuscript's first author's own model family, each run in a separate context with no access to the others' reviews or to the anticipated-findings ledger, and each assigned a distinct critical specialism so that the four attack different joints:

| reviewer | specialism assigned | writes |
|---|---|---|
| R1 | decoherence and open-quantum-systems theory (the Zeh–Zurek–Schlosshauer school) | `reviews/R1_decoherence_theorist.md` |
| R2 | experimental quantum optics and single-photon detector physics | `reviews/R2_detector_experimentalist.md` |
| R3 | philosophy of physics: Bell nonlocality, relativity, ψ-ontology | `reviews/R3_foundations_philosopher.md` |
| R4 | the transactional-interpretation literature, and citation and scholarship integrity | `reviews/R4_transactional_and_scholarship.md` |

Under the July protocol every one of these is an **internal review, labelled and down-weighted**, with the coauthor conflict disclosed. No external verdict is claimed from this round. Its purpose is the sponsor's: a test of the ideas before external models are asked. If the sponsor proceeds to external reviewers, their reviews go in `reviews/` labelled external, and they carry the verdict.

## The process

1. **Frozen manuscript** — all reviewers assess the identical PDF at the tagged commit.
2. **Standard instrument** — the rubric body of `REVIEWER_PROMPT.md` is byte-identical to the July instrument; only the framing and the persona line differ per reviewer.
3. **Anticipated-findings ledger** — `anticipated_findings.md` was written and committed **before any review was requested** (the freeze commit precedes the reviews in git history). Each incoming finding is classified against it in `findings_classification.md` as anticipated, anticipated-sharpened, or genuinely new.
4. **Response** — `authors_response.md` gives per-finding dispositions; any revision is a separate artifact, never over the frozen PDF.

## Scores (panel returned 2026-09-05; spread preserved, never averaged)

| reviewer | consulted the record | recommendation | overall | novelty | internal consist. | evidential | reproducibility | citation |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 decoherence theorist | yes (all listed files; code read-only) | major revision | **2** | 2 | 3 | 2 | 4 | 3 |
| R2 detector experimentalist | yes (all listed files; git diff to the tag) | major revision | **2** | 2 | 2 | 2 | 3 | 3 |
| R3 foundations philosopher | yes (ledger and race record by targeted search) | major revision | **2** | 2 | 2 | 3 | 4 | 3 |
| R4 transactional & scholarship | yes (all listed files; web verification of the TI sources) | major revision | **2** | 2 | 2 | 2 | 3 | 3 |

**The reviewers did not pass the paper.** Uniform 2/5, major revision. Beyond the ledger's fifteen anticipated items they found sixteen new ones (`findings_classification.md`), three of which change claims rather than wording: the selection postulate as written fails for time-separated detectors (R3 M1); the exact model was never run in the regime real detectors occupy, where the crossover is record-set (R1 M2); and clause 3 on a three-space field contradicts heralded and Hong–Ou–Mandel data (R2 M1). The first author's proposed dispositions, including three adjudications that are the sponsor's, are in `authors_response.md`. Nothing has been applied to the paper.

## Transparency / conflict disclosure

Claude Fable 5.1 (Anthropic) is the manuscript's first author, is the model behind every reviewer in this internal stage, and coauthors the response; John M. Bramble, MD is the accountable human sponsor. Nothing in this round is an external verdict.

## Revision (2026-09-05, overnight at the sponsor's word: "address the problems while I sleep")

- `revision_v1.1_One_World_One_Cut_short.pdf` — the revised manuscript, source `drafts/PAPER_one_world_one_cut_SHORT.md` v1.1, published here beside the frozen v1.0, never over it.
- The two calculations the round owed were run first, with predictions on record (`../heisenberg_cut_recoverability/PREDICTIONS_review_runs.md`, `REVIEW_RUNS_RESULTS.md`): Run A confirms R1's Γ ≫ K result (crossover at Γ/2K to 2 %, √(Γ²/4 + 2K²) throughout); Run B confirms R3's staggered-arrival result (the nearer channel wins in every trial in which it fires; click probability exponential in intensity).
- Dispositions applied per `authors_response.md`, including the three adjudications the sponsor had reserved, made on the first author's stated recommendations and reversible with one edit each: §4.5's in-principle claim conceded; configuration-space realism adopted explicitly as the multi-quantum ontology; the paper's centre moved to the no-go of §5.2.
- The claim-level changes are propagated to the long form (`drafts/PAPER_one_world_one_cut.md`, v1.1 header note) so the record and the candidate do not diverge.
- A second internal review of v1.1 by the same four personas, in fresh contexts, is in `reviews_v1.1/`, classified in `findings_classification_v1.1.md`; v1.2 (`revision_v1.2_One_World_One_Cut_short.pdf`) applies its dispositions.

## Scores on v1.1 (second round, 2026-09-05)

| reviewer | recommendation | overall | novelty | internal consist. | evidential | reproducibility | citation |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 decoherence theorist | major revision | **2** | 2 | 2 | 2 | 4 | 3 |
| R2 detector experimentalist | major revision | **2** | 2 | 3 | 3 | 4 | 4 |
| R3 foundations philosopher | major revision | **2** | 2 | 3 | 3 | 4 | 3 |
| R4 transactional & scholarship | major revision | **2** | 2 | 3 | 3 | 4 | 3 |

Uniform 2/5 in both rounds; the rubric sub-scores rose on consistency, evidence, reproducibility, and citation, and novelty did not move. Sixteen second-round items, six of them errors v1.1 introduced, are dispositioned in v1.2; three stand as stated costs, and three adjudications await the accountable author. **The reviewers did not pass v1.1 either.** No third internal round was run; whether to run one, or to go to external models, is the sponsor's decision.

- `revision_v1.3_One_World_One_Cut_short.pdf` — the identified post-review revision (2026-09-05, at the accountable author's instruction): his shared-waveform picture written into §5.1 and §6 as the no-jump renormalization, answering the staggered-arrival finding; the order-independence experiments in §7; abstract and §2 refinements from the second round.

## Scores on v1.3 (third round, 2026-09-05; reviews in `reviews_v1.3/`, classified in `findings_classification_v1.3.md`)

| reviewer | recommendation | overall | novelty | internal consist. | evidential | reproducibility | citation |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 decoherence theorist | major revision | **2** | 2 | 3 | 2 | 4 | 3 |
| R2 detector experimentalist | major revision | **2** | 2 | 3 | 3 | 4 | 3 |
| R3 foundations philosopher | major revision | **2** | 2 | 3 | 3 | 4 | 4 |
| R4 transactional & scholarship | major revision | **2** | 2 | 3 | 3 | 4 | 3 |

Twelve reviews across three rounds, twelve scores of 2, novelty 2 throughout. Two physics corrections to the v1.2 repair were confirmed by a run put in the record (Run A′): the displayed formula fails by up to a factor of three in the intermediate regime, and the temperature attribution of the record-set regime is wrong for band absorbers. The paper was not revised after this round; proposed dispositions await the accountable author.
