---
title: "Physics Markdown corpus inventory"
kind: spec
---

# Physics Markdown corpus inventory

Inventory date: 2026-08-24
Workspace: `~/Projects/Physics`

## Scope result

The recursive filesystem count is **189 Markdown files**. For physics review, the usable corpus is **166 authored or project-document files**, containing **45,245 lines** and approximately **3.21 MB** of text. Three byte-identical duplicate pairs reduce this to **163 unique contents** before any semantic deduplication.

The other 23 files should not be sent to physics reviewers:

| Exclusion | Files | Reason |
| --- | --- | --- |
| `DiracKuramotoFramework/t5_pilot/.venv/` | 16 | Package licenses and dependency documentation |
| `_archive/SchrodingerBell/.claude/worktrees/` | 4 | Worktree copies, including exact duplicates |
| `DiracKuramotoFramework/.junie/memory/` | 3 | Empty AI-tool memory placeholders |

## Authored corpus by physics program

| Program | Markdown files | Lines | Inventory interpretation |
| --- | --- | --- | --- |
| `DiracKuramotoFramework` | 134 | 37,085 | Main active research notebook; manuscripts, derivations, reviews, simulations, notes, and submission material |
| `_archive/SchrodingerBell` | 9 | 5,196 | Archived predecessor theory and three existing critiques |
| `UltravioletCatastrophe` | 10 | 1,059 | Exploratory extension; explicitly described as a seed rather than a result |
| `VacuumMedia` | 8 | 738 | Separate speculative seed; gravity/vacuum-medium derivations and magnitude tests |
| `RetinalPhaseCoding` | 2 | 690 | Small standalone concept/formalization set |
| `NS-EOS` | 3 | 477 | Small standalone concept/conversation set |
| **Total** | **166** | **45,245** |  |

## Dirac–Kuramoto internal structure

| Area | Files | Role |
| --- | --- | --- |
| Repository root | 21 | Main, predecessor, and companion manuscripts plus orientation/reference files |
| `drafts/` | 41 | Three-paper sequence, outlines, derivations, notes, ledgers, and proposals |
| Prior AI review rounds | 20 | Born-selection and Heisenberg-cut prompts, reports, classifications, and responses |
| `Research/` | 7 | Cochain and integration additions |
| `references/` | 6 | Literature summaries and reference orientation |
| `submission/` | 6 | Referee report, email drafts, suggested referees/experiment |
| `sessions/` | 6 | Research-session narratives |
| `resolution/` | 5 | Dispute and resolution records |
| `limiting_curvature/` | 5 | Current/superseded section drafts and carry audits |
| `ZBW_synchronization/` | 4 | Mental model, source analysis, and section drafts |
| `discussions/` | 4 | Dated conceptual discussions |
| `results/` | 3 | Numerical result narratives |
| Sims/code/tests | 6 | Simulation/result documentation and test orientation |

## Manuscript spine identified by the repository

The repository README defines this sequence as the current manuscript spine:

1. `drafts/PAPER1_DRAFT_born_selection.md` — Born-rule selection statistics; previously panel-reviewed.
2. `drafts/PAPER2_DRAFT_heisenberg_cut.md` — physical-threshold interpretation of the Heisenberg cut; previously panel-reviewed.
3. `drafts/PAPER3_DRAFT_dk_framework.md` — framework synthesis; active draft.
4. `current_revision_DK_paper.md` — frozen Many Clocks predecessor/provenance record, superseded by Paper 3.

`PAPER_UNIFIED.md` is retained as an earlier long-form record. Six root-level companion/spinoff papers are explicitly marked development-phase and not for citation: `LIGO_SIDEREAL_TEST_T5.md`, `SIDEREAL_DECOHERENCE_PAPER.md`, `AB_VISIBILITY_PAPER.md`, `COSMIC_EXPANSION_PAPER.md`, `DISCRETIZATION_AS_SYNC_PAPER.md`, and `EMERGENT_FIELDS_PAPER.md`.

## Duplicate and version hazards

Exact duplicate pairs inside the authored set:

- Raw and curated copies of the GPT-5 Codex Born-selection review.
- Raw and curated copies of the Fable5 Born-selection review.
- `SECTION_LIMITING_CURVATURE_DRAFT.md` and its `v1_superseded` copy.

Explicit backup/superseded manuscripts that should be provenance-only unless a reviewer is assigned version comparison:

- `current_revision_DK_paper_backup_2026-08-23_2247.md`
- `drafts/PAPER_REVISED_v2_backup_20260615.md`
- Three `4D-3DandSpacetime_backup_*` files
- `limiting_curvature/SECTION_LIMITING_CURVATURE_v1_superseded_2026-08-23.md`

## Repository state affecting reproducibility

- `DiracKuramotoFramework`: branch `main`, ten commits ahead of `origin/main`, with modified and untracked manuscripts/assets.
- `NS-EOS`: clean `main`, tracking `origin/main`.
- `VacuumMedia`: clean `main`, no remote shown.
- `_archive/SchrodingerBell`: modified and untracked research files.

Review inputs therefore need a frozen manifest or commit/archive snapshot before results can be called reproducible. No files were changed, frozen, or submitted to reviewers during this inventory.

## Boundary for the next phase

The review design should operate on the 166-file authored corpus, use the 163-content deduplicated view for indexing, and distinguish current claims from provenance, prior reviews, exploratory seeds, and computational evidence. The approved design begins with a one-paper pilot and is recorded in [Multi-agent physics review design](../multi-agent-physics-review-design).

## Author's learning and preservation requirements

The review is primarily a learning process for John M. Bramble, not merely a verdict-generation exercise. The eventual multi-agent workflow must therefore satisfy these requirements:

- All inter-agent discussion, disagreement, and synthesis must be recorded in clear English for later human review.
- Agents must explain relevant established physics, assumptions, equations, and objections at a level that helps the author learn; unexplained scores or verdicts are insufficient.
- The framework's underlying ideas must be stated faithfully before they are criticized. Reviewers may sharpen, constrain, or reject claims, but must not silently substitute a different theory.
- Every proposed conceptual change must identify what original idea it preserves, modifies, or abandons and why.
- Criticism must distinguish mathematical error, conflict with evidence, unsupported inference, speculative extension, terminology problem, and missing derivation.
- Minority opinions and unresolved disagreements must remain visible in the record rather than being erased by the final synthesis.
- The human author retains the final decision over changes to the framework's foundational commitments. Agents should provide consequences and alternatives, not make hidden editorial decisions.
- Review artifacts should include a plain-English learning summary alongside technical findings and equations.
