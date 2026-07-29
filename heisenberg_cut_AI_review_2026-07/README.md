# AI Peer-Review Round — *The Heisenberg Cut as a Physical Threshold* (Paper 2)

This folder is the review record for the manuscript *The Heisenberg Cut as a Physical Threshold: Location, Width, and Consequences of the Classical–Quantum Boundary in Detector Dynamics* (v0.2), run under the same published protocol as the Born-Selection round (`../born_selection_AI_review_2026-07/`), with one protocol improvement (reviewer-access equalization, below).

## The frozen target

- `reviewed_paper_v0.2_Heisenberg_Cut.pdf` — the exact manuscript every reviewer judges. Frozen at repository commit `aed9567` (git tag `paper2-v0.2-review`), 2026-07-28, with the reference list fully verified (19 confirmed, 1 corrected; log at `../drafts/PAPER2_citation_verification_2026-07-28.md`) and the §3.3 layer-width table sourced row-by-row (same log, addendum).
- Reviewer package: this PDF + the figure simulation `../paper2_sims/threshold_clock.py` (seed pinned) + its output figure. The companion paper and its complete published review round (`../born_selection_AI_review_2026-07/`) are citable context; the manuscript is deliberately evaluable as a conditional result on the companion's premises P0–P4.

## The process (identical instrument, one improvement)

1. **Frozen manuscript** — all reviewers assess the identical v0.2 PDF. No reviewer sees another's critique (decorrelation across labs).
2. **Standard instrument** — every model receives the byte-identical critical-referee rubric of the journal protocol (`REVIEWER_PROMPT_paper2.md`; rubric section unchanged from round 1 — cross-paper comparability under a fixed instrument is itself a finding of the journal experiment). Only the paper-specific framing differs.
3. **Access-mode equalization (new this round).** In the Born-Selection round, reviewer access was unequal — one reviewer ran web-enabled and audited the public repository; two did not — and the round's README disclosed this as a comparability caveat. This round *equalizes upward*: every reviewer is explicitly invited to consult the public repository pointer in the manuscript, and every review must record (a) whether the model was web-enabled, (b) whether it followed the repository pointer, (c) whether it complied with the **scoped exclusion**: reviewers must not read this round's own folder, which contains the pre-logged ledger and the internal review — reading either would anchor the reviewer and destroy the independent-discovery signal the ledger exists to measure. Findings made after disclosed exposure are classified as *post-exposure*, not independent. Provenance-aware review is the protocol default, now uniformly offered rather than accidentally distributed. *(Refinement adopted for future rounds, logged in the journal protocol: pre-register the ledger as a committed SHA-256 hash and publish the plaintext only after all reviews are in — timestamp proof without exposure risk.)*
4. **Panel composition** — verdict panel: ≥2 non-Anthropic frontier models from ≥2 labs. A Claude Fable 5 review runs as well but is published as a labeled **internal review**, down-weighted, with the coauthor conflict disclosed; the external panel carries the verdict.
5. **Anticipated-findings ledger** — `anticipated_findings.md` in this folder was written and committed **before any review was requested**. Each incoming finding will be classified against it as *known-open* (anticipated) or *genuinely new*; that classification is part of the published output.
6. **Response and revision** — authors' response with per-critique dispositions (`authors_response.md`); the single consolidated revision is published here as `revision_v0.3_Heisenberg_Cut.pdf`, added alongside the frozen v0.2, never over it. The round also produced a cross-paper correction: panel finding N2 propagated into the companion Born-Selection paper as its v0.5.3 ($\kappa_{\rm ret}$ rename, ansatz status, escalated open problem) — an external critique of one paper improving its already-reviewed companion, with the causal chain in the commit record. Bounded resolution loop (≤5 rounds) remains available for load-bearing disputes.

## Scores (panel returned 2026-07-28; spread preserved, never averaged)

| Reviewer (lab) | Web-enabled | Followed repo pointer | Recommendation | Overall | Novelty | Internal consist. | Evidential | Reproducibility | Citation |
|---|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5.6 Thinking (OpenAI) | yes | yes | reject | **1** | 3 | 1 | 1 | 3 | 3 |
| Gemini, "standard" (Google) | no† | no† | major revision | **4** | 4 | 4 | 3 | 4 | 5 |
| Grok 4.5 (xAI) | yes | yes | major revision | **2** | 3 | 4 | 2 | 4 | 4 |
| *Fable 5 (Anthropic) — internal, down-weighted* | *author* | *author* | *major revision* | *2* | *3* | *3* | *2* | *4* | *4* |

† Gemini reported it could not use web access due to environment constraints — so this round's access *invitation* did not achieve access *equalization* (see the protocol finding in `findings_classification.md`). All three externals complied with the scoped exclusion of this folder.

The external verdict is **major-revision-to-reject**, with the spread (1/2/4) again carrying information: the two provenance-aware (web-enabled, repository-auditing) reviewers scored 1 and 2; the manuscript-only reviewer scored 4 — the same access–severity correlation as round 1, now visible under equalized *invitation*. The internal review (2) sits inside the external range this round, unlike round 1 where it sat above it. One reviewer (GPT-5.6) independently re-ran the public figure script and identified a genuine threshold-labeling error in Figure 1(a) — reproducible ≠ correct, for the second consecutive round. Findings are classified against the pre-logged ledger in `findings_classification.md`.

## Preservation principle

Identical to round 1: the reviewed v0.2 stays frozen here; reviews anchor to it; the response anchors to the reviews; the revision is a separate artifact. Claim → critique → answer → change stays auditable in place.

## Transparency / conflict disclosure

Claude Fable 5 (Anthropic) is the manuscript's first author, will produce the internal review, and coauthors the authors' response; John M. Bramble, MD is the accountable human sponsor. The internal review is labeled and down-weighted; the external panel carries the verdict.
