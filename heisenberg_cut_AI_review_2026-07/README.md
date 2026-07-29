# AI Peer-Review Round — *The Heisenberg Cut as a Physical Threshold* (Paper 2)

This folder is the review record for the manuscript *The Heisenberg Cut as a Physical Threshold: Location, Width, and Consequences of the Classical–Quantum Boundary in Detector Dynamics* (v0.2), run under the same published protocol as the Born-Selection round (`../born_selection_AI_review_2026-07/`), with one protocol improvement (reviewer-access equalization, below).

## The frozen target

- `reviewed_paper_v0.2_Heisenberg_Cut.pdf` — the exact manuscript every reviewer judges. Frozen at repository commit `aed9567` (git tag `paper2-v0.2-review`), 2026-07-28, with the reference list fully verified (19 confirmed, 1 corrected; log at `../drafts/PAPER2_citation_verification_2026-07-28.md`) and the §3.3 layer-width table sourced row-by-row (same log, addendum).
- Reviewer package: this PDF + the figure simulation `../paper2_sims/threshold_clock.py` (seed pinned) + its output figure. The companion paper and its complete published review round (`../born_selection_AI_review_2026-07/`) are citable context; the manuscript is deliberately evaluable as a conditional result on the companion's premises P0–P4.

## The process (identical instrument, one improvement)

1. **Frozen manuscript** — all reviewers assess the identical v0.2 PDF. No reviewer sees another's critique (decorrelation across labs).
2. **Standard instrument** — every model receives the byte-identical critical-referee rubric of the journal protocol (`REVIEWER_PROMPT_paper2.md`; rubric section unchanged from round 1 — cross-paper comparability under a fixed instrument is itself a finding of the journal experiment). Only the paper-specific framing differs.
3. **Access-mode equalization (new this round).** In the Born-Selection round, reviewer access was unequal — one reviewer ran web-enabled and audited the public repository; two did not — and the round's README disclosed this as a comparability caveat. This round *equalizes upward*: every reviewer is explicitly invited to consult the public repository pointer in the manuscript, and every review must record (a) whether the model was web-enabled, (b) whether it followed the repository pointer. Provenance-aware review is the protocol default, now uniformly offered rather than accidentally distributed.
4. **Panel composition** — verdict panel: ≥2 non-Anthropic frontier models from ≥2 labs. A Claude Fable 5 review runs as well but is published as a labeled **internal review**, down-weighted, with the coauthor conflict disclosed; the external panel carries the verdict.
5. **Anticipated-findings ledger** — `anticipated_findings.md` in this folder was written and committed **before any review was requested**. Each incoming finding will be classified against it as *known-open* (anticipated) or *genuinely new*; that classification is part of the published output.
6. **Response and revision** — authors' response with per-critique dispositions; a single consolidated revision (v0.3) added alongside the frozen v0.2, never over it; bounded resolution loop (≤5 rounds) for load-bearing disputes.

## Scores

*(To be filled verbatim as reviews return; spread preserved, never averaged.)*

| Reviewer (lab) | Web-enabled | Followed repo pointer | Recommendation | Overall | Novelty | Internal consist. | Evidential | Reproducibility | Citation |
|---|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| — | — | — | — | — | — | — | — | — | — |

## Preservation principle

Identical to round 1: the reviewed v0.2 stays frozen here; reviews anchor to it; the response anchors to the reviews; the revision is a separate artifact. Claim → critique → answer → change stays auditable in place.

## Transparency / conflict disclosure

Claude Fable 5 (Anthropic) is the manuscript's first author, will produce the internal review, and coauthors the authors' response; John M. Bramble, MD is the accountable human sponsor. The internal review is labeled and down-weighted; the external panel carries the verdict.
