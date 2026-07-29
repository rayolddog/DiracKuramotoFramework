# Anticipated-findings ledger — Paper 2 review round

*Written and committed BEFORE any review was requested (freeze commit; see git history for the timestamp ordering — that ordering is what makes this ledger audit-proof). Each incoming panel finding will be classified against this list: KNOWN-OPEN (anticipated below) or GENUINELY NEW. The classification is part of the published output of the round.*

## Anticipated major findings

1. **Inherited conditionality.** The paper stands on Paper 1's P0–P4, including wave realism (P0) and the amplitude-linear noise premise (P2, grounded only at mechanism-sketch level). Reviewers may treat every downstream claim as conditional-on-unproven. *Status: acknowledged in §1 and §7's cost table; the conditionality is the paper's stated form.*
2. **Field quantization of Theorem 2** (the decisive inherited open problem, §8.5(iv)/§9): the sub-threshold slaved-phase statement is a linear semiclassical result; a fully quantized common field might admit a weak sub-threshold channel. *Status: known-open, flagged as the live theoretical risk in the paper's own falsifier list.*
3. **§5 (virtual/real) altitude.** Expect at least one reviewer to press that §5 is re-description without new predictive content, and/or that "virtual particle lifetime" glosses a propagator integral that needs no dynamical story. *Status: anticipated in-text — §5 carries an explicit "status" paragraph claiming exactly one falsifiable addition (the crossover profile); the dispute would be over whether that suffices.*
4. **Operationalization of the γ/K dial (§8.2).** "Outcome statistics should vary with γ/K and nothing else" needs a concrete protocol: which observable, which platform, what precision, what confounds (temperature and coupling co-vary in real devices). *Status: known gap — §9(iii) lists the first-principles crossover profile as open; a reviewer demand for a worked experimental design would be fair and actionable in revision.*
5. **Figure 1 is a minimal model.** Stuart–Landau + Adler are generic oscillator models, not the physical absorber with P4(i) level structure; a reviewer may object that the figure illustrates rather than derives. *Status: acknowledged in §9(iii); caption says "minimal model."*
6. **Which Γ disputes in the table (§3.3).** The identification of "the" phase-restoring rate per platform (natural vs broadened; 1/T₂ vs 1/2T₁; spectral diffusion as inhomogeneous-in-time; density dependence in Si) invites specialist pushback row by row. *Status: partially preempted by the "which Γ" paragraph and caveats (i)–(iv); expect refinement demands anyway.*
7. **Possible circularity objection.** The cut is defined via the lock; the lock's premises (P1–P4) are statements about detectors described partly in classical terms (baths, dissipation, thresholds). A reviewer may argue the classical boundary is presupposed in the premises rather than derived. *Status: anticipated; the §6 answer is that the premises are open-system quantum statements (decay rates, level structure) not classicality assumptions — expect to have to sharpen this in response.*
8. **Crossover vs phase transition.** The §6.2 naming (dimensionless location, finite width, no non-analyticity) may draw the objection that nothing singular marks the boundary, so calling it "physical" overclaims. *Status: anticipated; the reply is that a crossover with computed width IS the claim — sharpness was never asserted, and §3.3's sixteen-order spread is the point.*
9. **Mott-track cascade without calculation.** §4.2 reinterprets tracks as conditional lock cascades but the worked statistics are deferred (§9(iv)). *Status: known-open by construction.*
10. **Relation to prior threshold/criticality proposals.** Expect demands to compare against specific decoherence-timescale calculations (Joos–Zeh scattering rates), quantum Darwinism, and possibly Bohr's own "irreversible amplification" language — i.e., novelty pressure on whether "cut = threshold" has genuine precedent. *Status: §9 credits the adjacent programs; a dedicated related-work pass may be demanded.*

## Anticipated minor findings

- Length/imbalance: §§3–4 dense, §7 table compressed; demands to expand comparisons.
- The abstract's "sixteen orders of magnitude" table span leans on the clock row, whose relevance as a *detector* (a clock transition is deliberately never registered) may be questioned — expect a demand to justify or relabel the row.
- Terminology: "the lock," "basin," "commit" used before full definition for readers who have not read Paper 1; a glossary or expanded §2 may be requested.
- The [Paper 3, in preparation] and [Paper 1, manuscript] citations are non-archival; reviewers may object to load-bearing references without DOIs.

## What would count as genuinely new

Anything not reducible to items above — in particular: a technical error in the Theorem-2 import or the width identities; a platform where the γ/K story demonstrably contradicts existing data; a named prior work that anticipates the quantitative cut-location claim; an argument that the movability theorem of §6.1 fails somewhere above the layer.
