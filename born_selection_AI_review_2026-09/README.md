# AI Peer-Review Round — Paper 1 v0.10 (*A Field–Matter Selector for Outcome Production*, with Addendum A)

**Status (2026-09-14, later): internal stage run and returned; findings classified; no external verdict; no revision yet.** The paragraph below is the folder's state as first opened and is kept as written. This folder was opened on 2026-09-14 at the
sponsor's instruction to write the anticipated-findings ledger before a second review round of
Paper 1 (`drafts/PAPER1_DRAFT_born_selection.md`, v0.10, which adds Addendum A from the MathX
explorations to the v0.9 negative result). The first round (`../born_selection_AI_review_2026-07/`)
reviewed v0.3 and returned major-revision-to-reject.

## Order of operations, as the protocol requires

1. `anticipated_findings.md` — **this commit**, written before any PDF is frozen and before any
   reviewer is asked. Its position in git history ahead of the freeze is what makes it audit-proof.
2. References marked `[verify]` in the manuscript checked against the sources (eleven added at
   v0.10, all from memory).
3. `Born_Selection.pdf` rebuilt from the v0.10 source with `../build_pdfs.sh` (pandoc + xelatex;
   not available in the drafting environment), copied here as `reviewed_paper_v0.10_Born_Selection.pdf`,
   and the freeze tagged.
4. Panel composition decided by the sponsor: the internal stage first (four Claude Fable 5.1
   reviewers with distinct specialisms, labelled and down-weighted, as in
   `../one_world_one_cut_AI_review_2026-09/`), then external models if it passes; or external
   directly, as in July.
5. `REVIEWER_PROMPT.md` with the July rubric body byte-identical; reviews to `reviews/`;
   `findings_classification.md` against the ledger; `authors_response.md`; any revision as a
   separate artifact beside the frozen PDF, never over it.

## Reviewer package (to be listed in the prompt)

The frozen PDF and its Markdown source; `../NEGATIVE_RESULT.md`;
`../drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md`;
`../drafts/MATHX_ADDENDUM_LEDGER_2026-09-14.md`; `../g3_drain_tests/`;
`../adler_two_channel_exploratory/RESULTS.md`; and the MathX repository
(`rayolddog/MathX`: `MODEL_SECTION.md`, `vacuum_race/`, `spad_surface_contact/`, `pair_case/`,
`second_spinor_phase_race/`), whose numbers Addendum A cites.

## Transparency

Claude Fable 5.1 (Anthropic) is the manuscript's first author, wrote the MathX studies Addendum A
reports, wrote this ledger, and would be the model behind any internal-stage reviewer; John M.
Bramble, MD is the accountable human sponsor. No external verdict exists for v0.10.


## The round as run (2026-09-14)

- **Freeze.** The manuscript reviewed is `drafts/PAPER1_DRAFT_born_selection.md` at commit `4e213dbf26fbf9508334023f4c1d4dbcad3c5a35` (main after PR #3). A local tag `born-selection-v0.10-review` was made at that commit; the drafting environment's proxy refused the tag push, so the commit hash is the freeze. No PDF was built (no pandoc or xelatex in the drafting environment); reviewers read the Markdown source.
- **Instrument.** `REVIEWER_PROMPT.md`: framing for this round plus the rubric body byte-identical to the July and September instruments (verified by diff).
- **Panel.** Five reviewers, all Claude (`claude-fable-5-1` as configured; serving model not verified from inside the reviews), each in a separate context, each assigned a specialism, none with access to the ledger or to each other: R1 probability and stochastic processes; R2 experimental quantum optics and detector physics; R3 philosophy and foundations; R4 scholarship, citations and cross-document consistency; R5 reproducibility and numerical audit, who re-ran every MathX script Addendum A cites. Reviews in `reviews/`.
- **Classification.** `findings_classification.md` against `anticipated_findings.md`: seventeen ledger items hit, most of them sharpened; sixteen findings genuinely new, three of which change claims rather than wording.

## Scores (spread preserved, never averaged)

| reviewer | recommendation | overall | novelty | internal consist. | evidential | reproducibility | citation |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 stochastic-process theorist | major revision | **2** | 2 | 2 | 2 | 4 | 3 |
| R2 detector experimentalist | major revision | **1** | 2 | 2 | 1 | 4 | 3 |
| R3 foundations philosopher | reject | **1** | 1 | 2 | 2 | 3 | 3 |
| R4 scholarship and consistency | major revision | **1** | 2 | 1 | 2 | 4 | 2 |
| R5 reproducibility auditor | major revision | **2** | 2 | 3 | 2 | 3 | 4 |

**The reviewers did not pass the paper.** R5 checked 294 numbers and found none wrong in the manuscript's body; the failures are in claims about what the numbers show, in consistency across the six documents, and in three places of substance: Addendum A.2's clause is wrong as stated (an infinite-mean artefact), A.3's wavelength lines are a fill-factor artefact and its Grangier citation is to a photomultiplier experiment, and A.7 as amended is the projection postulate and should say so.

## Two disclosures about this round

1. The anticipated-findings ledger was amended in the same commit as a manuscript change (`b1c5e20`, item 3 marked removed) before the freeze. Two reviewers found this from the commit history. It weakens the "audit-proof" claim of the order of operations and is recorded here as a defect of the round.
2. The ledger's own pre-freeze "fix" of Addendum A.3's citation introduced a second error (Grangier 1986 used photomultipliers, not silicon), which two reviewers caught. The correction was wrong in a new way; the round did its job.

## Next

`authors_response.md` (per-finding dispositions) and any revision as a separate artifact beside the frozen source, never over it. The sponsor decides whether the paper is revised to the A.7 model, retired to `NEGATIVE_RESULT.md` with the theorems as an appendix, or left as the record of this round.
