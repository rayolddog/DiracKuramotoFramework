# AI Peer-Review Round — *The Born Rule as a Derived Fair Game*

This folder is a complete, openly published record of an **AI-facilitated adversarial peer review** of the manuscript *The Born Rule as a Derived Fair Game: Outcome Selection from Detector Dynamics* (v0.3). It is a working instance of the review model this project proposes: the paper, the critiques it drew, the authors' point-by-point response, and — kept separate from the original — the revision those critiques produced, all readable side by side.

**Why a reader should care about the reviews, not only the paper.** The reviews are not gatekeeping paperwork to be discarded once a verdict is reached; they are part of the scientific content. A reader trying to judge whether the paper's postulates hold will learn more from the *disagreement* than from the manuscript alone: three independent frontier models, from three different labs, converge on exactly where the argument is strong (the uniqueness of the fair noise scaling, the falsifiability), where it overreaches (the squared-amplitude premise, the nonlocal ontology doing the Bell work), and what remains genuinely open (a microscopic derivation of the noise; whether the sub-threshold lock survives field quantization). That converged map of strengths, weaknesses, and open problems is the substance the paper *brought about*, and it is preserved here so the next reader inherits it rather than re-deriving it. Published adversarial review is, on this view, a way of handing the reader the live debate.

## The process

1. **Frozen manuscript.** All reviewers assessed the identical v0.3 PDF (`reviewed_paper_v0.3_Born_Selection.pdf`) plus the paper's simulation code. No reviewer saw another's critique — the panel is decorrelated across labs, not a single model with a stutter.
2. **Standard instrument.** Every model received a byte-identical reviewer prompt (a critical-referee rubric with fixed 1–5 dimensions and a coarse 0–5 overall), so the scores are comparable.
3. **Independent reviews.** Three external labs plus one internal (down-weighted) review — see the scores below and the full texts in `reviews/`.
4. **Verification.** The authors independently re-ran every code-level claim before responding; the specific simulation defects one reviewer identified were confirmed correct and then corrected (see `../corrected_python_programs_after_reviews/`).
5. **Authors' response.** A per-critique disposition (`authors_response.md`): accept-and-revise / accept-as-conditional / partial / defer-to-companion-paper, with two explicitly reasoned rebuttals of over-severe framing. No consensus is manufactured; where reviewers diverged, the stricter standard was adopted.
6. **Single consolidated revision.** One documented revision (v0.4) responds to the whole panel at once — **added alongside the original, never substituted for it** (see *Preservation* below).

## The numeric scores

Overall is a coarse integer (5 exemplary · 4 strong · 3 sound · 2 weak-but-in-scope · 1 serious-reservations · 0 does-not-clear-the-bar). Rubric dimensions are 1–5.

| Reviewer (lab) | Recommendation | Overall | Novelty | Internal consist. | Evidential | Reproducibility | Citation |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT-5 Codex (OpenAI) | reject | **0** | 2 | 1 | 1 | 1 | 2 |
| Gemini 1.5 Pro (Google) | major revision | **2** | 3 | 4 | 2 | 5 | 4 |
| SuperGrok (xAI) | major revision | **2** | 4 | 3 | 2 | 3 | 4 |
| *Fable 5 (Anthropic) — internal, down-weighted* | *major revision* | *3* | *3* | *4* | *2* | *3* | *4* |

The external verdict is **major-revision-to-reject**, harsher than the internal self-review — which is itself evidence of, and a correction for, coauthor bias. The scores are **not collapsed into an average**: the spread (e.g. reproducibility 5 vs 1, novelty 2 vs 4) is information, and it is preserved deliberately. The reproducibility split is instructive — one reviewer scored the pinned-seed code 5/5, another audited it line-by-line and scored it 1/5; the audit was right, and *reproducible ≠ correct*.

**Reviewer-access caveat (comparability).** The reviewers did not have equal access to context. GPT-5 Codex ran web-enabled and followed the public repository pointer printed in the manuscript's own references (checking authorship provenance and auditing the code line-by-line); the other two assessed the manuscript (and, for one, the code) without following that pointer. This asymmetry partly explains the depth of the harshest review, and it means this round is not yet an access-equalized instrument. Future rounds will record and equalize reviewer access mode. Nothing private was read — all provenance is public. We regard provenance-aware review (a referee who reads the methodology, discussion, and references, not the abstract alone) as the correct default.

## Preservation principle

**The revision does not replace the reviewed paper.** The exact manuscript the panel judged is frozen here as `reviewed_paper_v0.3_Born_Selection.pdf`, and the consolidated revision (v0.4) is added as a *separate* artifact when complete — never written over v0.3. The reviews are anchored to a fixed text, the response is anchored to those reviews, and the revision is anchored to the response, so the whole trajectory — claim → critique → answer → change — stays auditable in place. A reader can always see what was said, about which version, and what changed as a result.

## Transparency / conflict disclosure

Claude Fable 5 (Anthropic) is the manuscript's first author, produced the internal review, and coauthored the authors' response; John M. Bramble, MD is the accountable human sponsor. The internal review is therefore labeled and down-weighted; the **external panel carries the verdict**. This is disclosed rather than hidden — the point of the model is that a coauthor-model articulating the framework's weaknesses is informative to the reader precisely *because* the conflict is visible and the external critiques are published in full.

## Contents

- `reviewed_paper_v0.3_Born_Selection.pdf` — the frozen manuscript every reviewer judged.
- `reviews/`
  - `external_GPT5_Codex_OpenAI.md` — reject, 0/5 (code-audited, provenance-aware).
  - `external_Gemini_1.5Pro_Google.md` — major revision, 2/5.
  - `external_SuperGrok_xAI.md` — major revision, 2/5.
  - `internal_Fable5_Anthropic_downweighted.md` — major revision, 3/5 (coauthor; down-weighted).
  - `GPT5_followup_energy_and_amplitudes.md` — a follow-up exchange on energy conservation and the amplitude→weight sequence.
- `authors_response.md` — the per-critique disposition and the v0.4 change checklist.
- Corrected simulations (referenced): `../corrected_python_programs_after_reviews/` (originals preserved unchanged in `../born_selection_sims/`).
- The v0.4 revision will be added here as a separate PDF when complete.
