# Author Contributions and AI Use Disclosure

*This section is intended for inclusion in `PAPER_UNIFIED.md` (or as a
standalone `AUTHORSHIP.md` in the repository root). Adapt as appropriate
for the target journal's specific AI disclosure format. As of 2026, all
major physics journals — Nature, Science, PNAS, Phys. Rev., Chaos
(AIP) — require disclosure of LLM use; this template follows the most
detailed of those (Nature's policy).*

---

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

*Last updated: 2026-05-17.  Version: 1.0.*
