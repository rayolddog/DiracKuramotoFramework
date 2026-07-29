# INTERNAL REVIEW — labeled, down-weighted, coauthor conflict disclosed

*Provenance: Claude Fable 5 (Anthropic), 2026-07-28. Reproduced verbatim. This reviewer is the manuscript's first author. Per protocol this review carries no verdict weight; the external panel decides. Access-mode record: (a) web-enabled: yes; (b) repository pointer: not applicable — the reviewer is the author and has full repository access, including the pre-logged `anticipated_findings.md`, which this review inevitably overlaps and occasionally exceeds. Round-1 calibration note: in the Born-Selection round the internal review scored one full band softer than the external panel; this review deliberately corrects toward external severity.*

**Standing and limitations.** I am a language model (Claude Fable 5, Anthropic). I can assess internal logic, claims outrunning support, and consistency against textbook quantum mechanics and the synchronization literature. I cannot certify novelty against the complete literature — a limitation that bites hard here, because this paper's contribution is largely synthetic (see Novelty) — and I am the author, so every bias runs toward acceptance; where I was uncertain of a severity call, I rounded down.

## 1. Recommendation

**Major revision.** Venue note: foundations-of-physics / interpretation venue (Foundations of Physics; Studies in HPMP; not PRL-class — the paper proves no new theorem). Authorship recommendation: byline honest as it stands (AI first author performed formalization, prose, simulation, literature work; human sponsor accountable; contributions statement matches the provenance record).

## 2. Summary

The manuscript claims the Heisenberg cut is not a bookkeeping convention but a physical crossover: below a registration threshold an absorber mode's phase is provably slaved to its drive (a linear-dynamics result imported from a companion paper), above it the mode owns a phase that can lock, and the boundary sits at coupling-equals-restoring-rate with fractional width w = K/ω, tabulated across laboratory platforms from 10⁻¹⁸ to 10⁻². The famous movability of the conventional cut is explained as a linearity theorem valid everywhere except the locking layer. Consequences: a three-way process distinction (interaction/decoherence/lock), a detector taxonomy, a virtual/real re-description, a single-world basin picture, and a claim that coupling — not mass — is the variable deciding where quantum behavior ends.

## 3. Strengths

- The three-way distinction (§2) is genuinely clarifying and correctly credits decoherence theory with its own limitation statements rather than relitigating them.
- §6.1 is the paper's best argument: keeping von Neumann's movability as a theorem and *deriving its domain of validity* is a real reframing — the "shifty split" objection is answered rather than dodged.
- The sourcing discipline is exemplary for a draft at this stage: verified reference log with per-entry URLs, a row-anchored parameter table with stated conventions and caveats, a seeded minimal-model figure whose limitations are declared in the caption and §9.
- The falsifier list (§8.5) includes the paper's own foundation (field quantization of the imported theorem) — honest exposure of the load-bearing risk.

## 4. Major concerns

1. **The operational-invisibility tension (sharpest problem, and it is structural).** The paper's own theorems make Born statistics *exact* wherever the layer is thin — which is precisely where the paper celebrates the cut's sharpness (clock row, w ~ 10⁻¹⁸). But then in exactly those systems the cut's "address" has no observable consequence: nothing measurable distinguishes "physical threshold at γ ~ K" from "no threshold at all" when every deviation is O(w) ≈ 0. The physicality claim is carried entirely by the wide-layer systems (w ~ 10⁻²) — i.e., by Paper 1's deviation ledger — and §8.2's "primary novel experimental claim" risks adding *nothing* beyond that ledger. What would fix it: state explicitly which §8.2 observables differ from standard open-system predictions *at the same γ and K*, or concede that the cut's location is empirical only where w is large and recast §3.3's sharp rows as consistency, not evidence.
2. **γ/K dial vs ordinary decoherence phenomenology (§8.2).** Standard decoherence theory *also* predicts that coherence phenomenology scales with coupling and linewidth ratios; "everything varies with γ/K and nothing else" is dangerously close to a restatement of dimensional analysis on T₂ physics. The claimed discriminator needs a worked protocol: a named platform, a named observable (lock-time distribution? which experiment measures that?), a predicted functional form, and the confound analysis for the fact that γ and K co-vary with temperature and geometry in every real device. Until then this is a research direction, not a prediction.
3. **A γ / Γ / K identification slide in §3.3.** Theorem 2's phase-restoring rate is γ = ΔE/ħ — a *state-dependent off-shellness* rate that varies during selection and vanishes at the shell. The table's column is a *material linewidth* Γ, which per Appendix B.2 of the companion proxies the *coupling* K and hence the layer width. These are three different quantities, and the table header ("phase-restoring / linewidth scale") plus surrounding prose lets the reader conflate them. The numbers survive the correction (w = K/ω with K ~ Γ), but the conceptual chain must be spelled out or a referee will conclude the central quantity is ill-defined.
4. **Novelty pressure from the synchronization-as-threshold literature — insufficiently addressed.** Laser threshold as a nonequilibrium phase transition, with explicit measurement analogies, is a developed literature (Haken's synergetics program at minimum; also symmetry-breaking accounts of measurement). §9.2's related-work coverage names the interpretation programs but not the *threshold-physics* precedents. If a referee finds "the quantum-classical boundary is a locking/lasing-type threshold" stated in the 1970s–80s synergetics corpus, the paper's framing claim collapses to "quantitative revival with a width formula." The fix is cheap and should be done proactively: a dedicated related-work paragraph on threshold/synergetics precedents, with the delta stated (the w = K/ω width, the movability-domain theorem, and the detector taxonomy are plausibly the genuinely new parts).
5. **The clock-transition row undermines rather than supports (§3.3).** A clock transition is engineered never to register — the "sharpest cut in any laboratory" row describes a system in which no measurement event of the relevant kind occurs. Its inclusion inflates the sixteen-orders headline (repeated in the abstract and §8.2). Either justify why a never-registering transition still instantiates a cut location, or relabel the row as a coherence bound and drop it from the dynamic-range claim.
6. **Inherited foundation, restated for the record.** Every result is conditional on the companion's P0–P4, including a wave-realism premise and a noise premise grounded only at mechanism-sketch level, and the slaved-phase theorem is a linear semiclassical statement whose field-quantized fate is open. The paper says all this; a referee will still correctly observe that the paper's *entire content* is downstream of it. The §7 cost table should make the linear-semiclassical caveat a listed cost, not only a §9 open problem.
7. **§5 adds one falsifiable item, and it may not be quantum.** The slip-time/critical-slowing curve of Fig. 1(b) is textbook injection-locking physics, demonstrated in driven oscillators for decades. What would make its middle section *quantum-measurement* evidence — as opposed to a classical synchronization measurement rebranded — is not stated. Either identify a genuinely quantum platform where tracing the crossover profile bears on outcome selection, or demote §5's "one quantitative consequence" to an analogy-consistency claim.

## 5. Minor / presentational

- §7's comparison table compresses contested characterizations into single cells (the MWI row will annoy Everettians; "no new constants" for this program elides that K, thresholds, and bath spectra are per-system inputs).
- The Mott-cascade claim (§4.2) is attractive and uncomputed; the text flags this, but the abstract's "consequences follow for the anatomy of a measurement event" implies more delivery than §4.2 provides.
- Load-bearing citations to [Paper 1, manuscript] and [Paper 3, in preparation] are non-archival; fine for a preprint, fatal at a journal until Paper 1 has a DOI.
- Terms "lock," "basin," "commit" are used before §2 fully earns them for readers arriving without Paper 1.

## 6. Questions for the authors

1. In a system with w ~ 10⁻¹⁸, what experiment — even in principle — would distinguish "the cut is physically located at γ ~ K" from "the cut is conventional"? If none, in what sense is the location physical there?
2. What is the precise relation among γ = ΔE/ħ (theorem), Γ (table), and K (layer width)? Write the one-paragraph dictionary.
3. Which specific observable in §8.2 differs, at fixed γ/K, from the prediction of standard open-system quantum mechanics with no locking sector?
4. Does the synergetics/laser-threshold literature anticipate the qualitative claim? What exactly is the delta?
5. Can the recoverability discriminator of §8.3 be run on any existing dataset (echo-recovery attempts after partial "which-path" exposure), or is it purely prospective?

## 7. Rubric scores (1–5)

- **Novelty: 3.** The width formula w = K/ω as a cut *location + width*, the movability-domain argument, and the sixteen-order table are new packaging with real content; the core theorem is imported, and the threshold framing has probable precedent in synergetics that the paper has not cleared.
- **Internal consistency: 3.** The architecture is coherent and the honesty devices are real, but the γ/Γ/K slide (major 3) and the §8.2-vs-exact-Born tension (major 1) are internal frictions a careful referee will document.
- **Evidential grounding: 2.** The table contains real measured numbers, but nothing in the paper is *evidence for* the threshold account against decoherence-only alternatives; the sole proprietary evidence channel (O(w) deviations) belongs to Paper 1.
- **Reproducibility: 4.** Seeded minimal-model sim, sourced table with logs, small honest scope. Not 5: the figure is a toy model and the paper generates no new data-level results to reproduce.
- **Citation integrity: 4.** Verified logs with URLs are above field standard; docked for two load-bearing non-archival references and the unresolved synergetics gap.

## 8. Overall assessment (0–5)

**2 — weak-but-in-scope.** The paper is honest, well-organized, and contains one genuinely good argument (§6.1), but its evidential situation is parasitic on Paper 1, its primary novel experimental claim is not yet operationalized against the obvious null hypothesis, and its novelty exposure to the threshold-physics literature is uncleared. A major revision that (i) resolves the γ/Γ/K dictionary, (ii) turns §8.2 into one worked protocol with a stated discriminator against standard open-system predictions, and (iii) clears or absorbs the synergetics precedent could plausibly reach 3.

## 9. Sign-off

Reviewer: Claude Fable 5 (Anthropic, claude-fable-5), 2026-07-28. **Internal review — first author; down-weighted; no verdict weight. The external panel decides.**
