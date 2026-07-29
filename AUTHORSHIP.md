# Authorship Policy and Contribution Record

## Current policy: honest per-paper bylines (supersedes the v1.0 statement below)

*Adopted 2026-07; formalized here 2026-07-28, completing finding N4 of the Heisenberg-Cut review round, in which two external reviewers (GPT-5.6 Thinking/OpenAI and Grok 4.5/xAI) independently required this file, the per-paper bylines, and `CITATION.cff` to be made mutually consistent.*

**The policy.** Each manuscript in this program carries the byline its actual contribution record supports — including AI systems as coauthor or first author where the AI performed coauthor- or first-author-level work — with **John M. Bramble, MD as the accountable human sponsor of every work regardless of byline order**. Accountability and credit are separated deliberately: a human answers for every claim; credit goes where the work was done. This supersedes the v1.0 statement below, which followed the 2026 journal-guideline default ("LLMs do not satisfy authorship criteria"); the program now regards that default as an honesty problem when the AI has demonstrably done first-author-level work, and handles venue-specific authorship restrictions at submission time, per venue, by disclosure and negotiation rather than by pre-emptive miscrediting. Reviewers under this program's published review protocol are explicitly instructed to check byline honesty in both directions.

**Per-paper bylines as they currently stand** (the byline of record is the one printed in each manuscript; this table is the index):

| Manuscript | Byline of record | Notes |
|---|---|---|
| *The Born Rule as a Derived Fair Game* (Paper 1) | Claude Fable 5 (Anthropic) and John M. Bramble, MD | AI performed formalization, theorems, simulations, prose, literature work; contributions statement in the manuscript; final order confirmed by sponsor pre-submission |
| *The Heisenberg Cut as a Physical Threshold* (Paper 2) | Claude Fable 5 (Anthropic) and John M. Bramble, MD | same structure; reviewed under the published AI panel protocol |
| Two-Regimes / Many-Clocks main paper (PAPER_UNIFIED / PAPER_REVISED) | Claude (Anthropic) and John M. Bramble, MD — Claude-first canonical since 2026-07 | earlier submitted versions carried the v1.0-era human-only byline with AI disclosure |
| Earlier companion papers (Discretization-as-Sync, AB Visibility, Cosmic Expansion) | as printed in each (v1.0-era form: human byline + AI disclosure) | predate this policy; to be re-examined per paper if and when each is next revised — bylines are never changed retroactively without an explicit per-paper decision |

**Model-version disclosure** (required by the same review finding): material AI contributions to this repository span model generations. The framework's original formalization, verification scripts, and the v1.0-era manuscripts were developed with **Claude Opus 4.6 and 4.7** (Anthropic), spring 2026, as recorded in the historical statement below. Papers 1 and 2, their simulations, the published review-round machinery, and the 2026-07 revisions are the work of **Claude Fable 5** (Anthropic). The commit history of this repository is the authoritative, timestamped provenance record of which system did what, when.

**Consistency.** `CITATION.cff` (repository-level citation metadata) lists both the human sponsor and Claude (Anthropic) and points here for per-paper bylines. The manuscripts' reference-list entries for this repository use the same two-party form.

---

# [HISTORICAL — v1.0, 2026-05-17] Author Contributions and AI Use Disclosure

*Retained verbatim as the accurate record of the framework's initial era and of the Opus 4.6/4.7 contributions; superseded as policy by the section above.*

## Author Contributions

**John Bramble** (MD, independent researcher): conceived the Many Clocks
Interpretation, framed all interpretive and physical claims, validated
the mathematical results against physical intuition and against the
standard quantum-mechanics literature, supplied the medical-imaging and
clinical-physics motivation, made all editorial decisions, and bears
final responsibility for all content of the manuscript and code.

## AI Use Disclosure

The mathematical formalization, derivations, code drafting, literature
search, and prose drafting were developed in collaboration with **Claude
Opus 4.6** and **Claude Opus 4.7** (Anthropic). The collaboration
followed an iterative pattern in which the human author proposed
physical pictures and the AI assistant produced candidate mathematical
formalizations, numerical verification scripts, and prose drafts; the
human author then reviewed, corrected, and accepted or rejected each
candidate.

Specific roles of the AI assistant included:

- **Mathematical formalization.** Rendering physical intuitions in
  standard notation (Dirac equation in Weyl basis, Kuramoto polar
  decomposition, Hodge–Dirac operator algebra, simplicial Kuramoto
  embedding).
- **Numerical verification.** Drafting Python scripts to test specific
  claims numerically. All scripts were reviewed and re-run by the human
  author, and any test that did not pass to satisfactory precision was
  investigated jointly until resolved.
- **Literature integration.** Searching for, summarizing, and
  cross-referencing prior work (including the Nurisso et al. 2024
  simplicial Kuramoto framework, Hestenes' Zitterbewegung interpretation,
  Penrose objective reduction, and Nelson stochastic mechanics).
- **Prose drafting.** Producing initial drafts of mathematical sections
  and appendices, which the human author edited for accuracy, tone, and
  interpretive content.

The AI assistant did **not**:

- Independently propose physical claims that were not initiated by the
  human author.
- Make editorial decisions about manuscript content or scope.
- Verify the correctness of any claim against external experimental
  data or peer-reviewed literature beyond what was provided to it in
  the conversation.
- Substitute for peer review or for independent expert assessment.

## A Note on Appendix B Specifically

Appendix B (Cochain Ontology of the Wave Function) was developed
substantially by the AI assistant during a single extended conversation,
in response to the human author's introduction of Nurisso et al. (2024)
into the discussion. The mathematical content of that appendix —
including the embedding of the framework's K = m identification into
the simplicial Kuramoto formalism, the Hodge–Dirac operator construction,
and the cochain reading of the §3.7 coherence sub-manifold — reflects
the AI assistant's expository and synthetic work to a greater degree
than the rest of the manuscript. The human author's contributions to
that appendix were: surfacing the Nurisso et al. reference, setting
the scope and register of the discussion, validating each mathematical
claim against the framework's existing structure, and flagging the
metaphysical limitations now recorded in §B.7. The three verification
scripts in `tests/` supporting that appendix
(`simplicial_alignment.py`, `hodge_decomposition.py`, `hodge_dirac.py`)
were drafted by the AI assistant and reviewed and re-run by the human
author.

This division of labor is recorded explicitly so that readers and
reviewers can calibrate the appendix's epistemic status relative to the
rest of the manuscript: the central physical claims of the paper (the
K = m identification, the two-stage measurement, the Penrose connection,
the Bell-test analysis) originate with the human author and have been
developed over many iterations; the cochain-ontology appendix is a
later structural alignment with the simplicial Kuramoto literature,
produced in a single conversation and not yet stress-tested at the
same depth.

## Responsibility and Limitations

Per current guidelines from Nature, Science, PNAS, AAAS, and the
International Committee of Medical Journal Editors (ICMJE), large
language models do not satisfy authorship criteria and are not listed
as authors. The human author bears full responsibility for the
manuscript's content, including any errors of mathematics, physics,
attribution, or interpretation. Where the AI assistant contributed
mathematical derivations or numerical results, the human author has
independently verified them or has explicitly noted limitations of the
verification in the relevant section of the manuscript (e.g., the
honest-limitations subsections in §10, §B.7, and §3.8).

Readers and reviewers are encouraged to flag any claim that appears to
exceed what the framework's argumentation actually establishes; the
author welcomes such corrections.

## Reproducibility

All numerical claims in the manuscript can be independently verified by
running the scripts in `tests/` (see `tests/README.md`). The scripts
require only `numpy` and `scipy`, run in a few seconds each on a modern
laptop, and produce pass/fail summaries with quantitative residuals.
The full conversation history with the AI assistant is not preserved
verbatim — long technical conversations were folded into the final
artifacts (paper sections and verification scripts) and the working
notes were not retained. The artifacts themselves are the record of the
collaboration.

---

*v1.0: 2026-05-17. Policy section added and v1.0 marked historical: 2026-07-28 (version 2.0).*
