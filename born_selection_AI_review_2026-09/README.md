# AI Peer-Review Round — Paper 1 v0.10 (*A Field–Matter Selector for Outcome Production*, with Addendum A)

**Status: prepared, not frozen, no reviewer launched.** This folder was opened on 2026-09-14 at the
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
