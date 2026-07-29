# Findings classification — panel vs the pre-logged ledger

*The ledger (`anticipated_findings.md`) was committed at the freeze (`c3e7115`), before any review was requested; all three external reviewers complied with the scoped exclusion and did not read it. Every panel finding is classified below as ANTICIPATED (ledger item cited), ANTICIPATED-SHARPENED (ledger area, but with new technical content the ledger lacked), or GENUINELY NEW. This classification is part of the round's published output.*

## Convergence map (what all or most reviewers found independently)

All four reviews (3 external + internal) converge on four diagnoses — all anticipated (ledger 1, 2, 4, 6):
1. The foundation is external and open: everything rests on the companion's Theorem 2 and the unclosed lock dynamics (ledger 1–2; GPT majors 1–2, 5; Gemini majors 1–2; Grok majors 1–2, 4; internal major 6).
2. The K ~ Γ identification is unproven and the table converts linewidths into "cut widths" under it (ledger 6; GPT major 4; Grok major 3; internal major 3).
3. §5's virtual/real reading overreaches its declared re-description status (ledger 3; GPT major 7; Gemini major 3; internal major 7).
4. The experimental program is not yet quantitatively discriminating against standard open-system physics (ledger 4; GPT major 8; Grok major 5; internal major 2).

The pre-registration worked: the paper's authors demonstrably knew its four deepest problems before the panel confirmed them. What the panel added is below — and it is substantial.

## Genuinely new findings

- **N1. Figure 1(a) threshold mislabeling — factual error, independently verified (GPT-5.6 major 3).** The reviewer re-ran `paper2_sims/threshold_clock.py` and showed the winding onset occurs near g ≈ 0.35–0.4 (the injection-locking boundary g > (F/Δ)² = 0.1225, noise-smeared upward), NOT at the g = 0 line the caption and marker call "threshold." The g = 0 line is the unforced Hopf (self-oscillation) threshold; the caption conflates two distinct thresholds. **Accepted on sight — the simulation's own data points (zero winding through g = 0.3) confirm it.** Must fix: caption, marker, and the §3.1 sentence tying the figure to "the layer."
- **N2. γ = ΔE/ħ: detuning is not generically a decay rate (GPT-5.6 major 1).** The foundational identification of off-shell deficit with a *dissipative* rate is asserted; in standard driven-system theory detuning is Hamiltonian/rotational, damping comes from a bath with a spectral density, and a detuned state can be long-lived. The ledger's circularity item (7) gestured nearby; this formulation is sharper and strikes at the companion paper's Theorem 2 premise as much as at this manuscript. Escalate to the Paper 1 open-problems ledger.
- **N3. Lock reversible vs committing — internal contradiction in exposition (GPT-5.6 major 6).** §2 makes the lock the commitment boundary; §4.1 (importing the companion's temporal ladder) says the lock "engages reversibly" with irreversibility supplied by slow registration. Both cannot pin the cut in the same operational sense. A real editorial/conceptual defect the internal review missed; requires one operational criterion for "the cut" and a consistent time-ordering.
- **N4. Authorship-documentation harmonization (GPT-5.6 recommendation §1 + question 13; Grok question 5).** The repo's AUTHORSHIP.md (older, framework-level, more human-centric, pre-dating the per-paper policy) conflicts with this paper's Fable-5-first byline, and CITATION.cff lists only the human author. Both web-enabled reviewers found it. Per-paper byline policy must be stated as superseding, and the metadata reconciled. (Long-pending item — Paper 1 checklist item 10 — now formally demanded by two external reviewers.)
- **N5. Practical-reversibility scope (Gemini major 4).** Echo-type reversibility is demonstrated for controlled ensembles; extending "capture is reversible" to broadband continuum absorbers overgeneralizes. Scope the claim by detector class.
- **N6. Protocol finding — invitation ≠ equalization.** Gemini could not use web access (environment constraints), so equalized *invitation* still produced unequal *access*, and the access–severity correlation of round 1 reproduced (web-enabled: 1, 2; manuscript-only: 4). Future rounds should record access *capability* ex ante and consider supplying provenance materials in-package (attach the companion PDF and key logs directly) so access does not depend on the reviewer's environment. Log alongside protocol §8.

## Anticipated-sharpened

- **S1. "K does not appear in the linear equation" (GPT-5.6 major 2).** Ledger 5/7 anticipated the minimal-model and circularity objections; the panel's version is sharper: the sub-threshold linear system contains no K at all, so "γ falls below K" compares a model parameter with a quantity external to the model, and the transition is imported wholesale by switching to Stuart–Landau. The fix demanded (one continuous model spanning both sides, with the bifurcation exhibited) is well-posed.
- **S2. Grok's field-quantization question 1** (does vacuum coupling restore an effective free phase below the classical threshold?) is the ledger-2 open problem stated as a precise technical question — useful phrasing for the Paper 1 open-problems list.
- **S3. Citation source-to-claim validity (GPT-5.6 major 9).** Ledger anticipated the clock-row objection; the panel generalizes: echo/quantum-memory citations establish rephasing/retrieval, not the manuscript's capture ontology. Each load-bearing citation needs its established-vs-conjectured split stated.

## Scoring/spread observations (for the round record)

- External spread 1 / 2 / 4 (reject / major / major): information, not noise — severity tracks provenance-aware access, again.
- Internal review (2) landed inside the external range; round 1's internal-leniency bias did not recur after deliberate calibration.
- Internal-consistency spread is the widest dimension (1 vs 4 vs 4): GPT-5.6's 1 is driven by N1 + N3 + S1 — concrete, checkable defects rather than taste.
- Gemini's 4/5-heavy scores came from the only reviewer unable to audit the repository — consistent with round 1's finding that depth of access, not lab identity, predicts severity.
