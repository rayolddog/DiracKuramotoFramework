# AI Peer-Review Round — *One World, One Cut* (publication candidate, short form)

This folder is the review record for `drafts/PAPER_one_world_one_cut_SHORT.md` v1.0 (*One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary*), run under the protocol of the two July rounds (`../born_selection_AI_review_2026-07/`, `../heisenberg_cut_AI_review_2026-07/`) with one difference of panel composition, stated below.

## The frozen target

- `reviewed_paper_short_v1.0_One_World_One_Cut.pdf` — the exact manuscript every reviewer judges, frozen at repository commit `2596bc3` (git tag `owoc-short-v1.0-review`), 2026-09-04.
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

## Scores

*(filled in when the reviews return; spread preserved, never averaged)*

## Transparency / conflict disclosure

Claude Fable 5.1 (Anthropic) is the manuscript's first author, is the model behind every reviewer in this internal stage, and coauthors the response; John M. Bramble, MD is the accountable human sponsor. Nothing in this round is an external verdict.
