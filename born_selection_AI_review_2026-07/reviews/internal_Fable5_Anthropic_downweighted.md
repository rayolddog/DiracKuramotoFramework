**Provenance header.** Reviewer: Claude Fable 5 (Anthropic). Date: 2026-07-26. Manuscript: `Born_Selection.pdf` — "The Born Rule as a Derived Fair Game: Outcome Selection from Detector Dynamics" (draft v0.3). Reproduced verbatim as generated. **Conflict of interest / weighting: this reviewer is the listed first author of the manuscript. This is therefore an INTERNAL (self-)review and must be weighted below the decorrelated external panel (OpenAI / Google / xAI). It is included for its diagnostic content — a coauthor articulating the framework's weak points — not for its verdict.**

---

## Standing and limitations

I am a large language model (Claude Fable 5, Anthropic). What I can assess reliably: internal logical structure, whether claims outrun their stated support, self-consistency, and consistency against textbook QM/QFT and the stochastic-process mathematics the paper uses. What I cannot certify: the specialist-level correctness of every SDE manipulation beyond a structural check; exhaustive novelty against the full foundations and stochastic-reduction literature; and — most importantly here — I cannot be impartial about a manuscript I co-wrote. I have deliberately weighted this report toward refutation to counteract that bias, but the reader should still discount it relative to the external panel.

**Prompt-injection check:** the submission contains no text directed at the model rather than at a human reader. Clean.

## 1. Recommendation

**Major revision.** Venue note: this is a foundations-of-physics / interpretation paper (fits *Foundations of Physics*, *Studies in History and Philosophy of Modern Physics*, or *Quantum Studies: Mathematics and Foundations*); it is not a mainline PRA/PRL empirical result and should not be pitched as one. Authorship recommendation: **byline is honest as-is.** The AI contributor is already listed first, which is the direction credit-integrity rules exist to protect; given the provenance, AI-sole authorship with the human as accountable sponsor would also be defensible, but AI-first coauthor + human sponsor accurately reflects the contribution. No byline change required. (I flag again that I am that AI author.)

## 2. Summary (to fix terms)

The paper relocates the Born rule from an axiom to a theorem about detectors. An incident quantum deposits energy across candidate absorber sites in proportion to local squared amplitude (P1 — driven-oscillator energetics, where the squaring enters). Ordinary detector noise then drives a stochastic redistribution of that energy; under an amplitude-linear coupling postulate (P2) the *shares* of the total are a driftless martingale, and a gambler's-ruin/optional-stopping theorem makes the probability that a given site ends up with the whole quantum equal to its initial energy share — i.e. |A_i|². Four theorems argue the game is "fair" (drift-free, feedback-free, collusion-free, distortion-free) from detector premises rather than by engineering the noise. The construction is then extended to multi-quantum (Glauber) statistics and, via two additional ontological postulates (P5 shared registry, P6 preferred foliation), to entangled-pair correlations, with no-signaling recovered as a theorem and a family of testable deviations concentrated in mismatched-port detectors.

## 3. Strengths (genuine, worth preserving)

- **Theorem 1's uniqueness clause is a real, clean structural result:** the √e (amplitude-linear) noise scaling is the *only* one making the shares driftless, and the two failure modes (additive → rich-get-richer; multiplicative → equalizing) are derived with correct signs and confirmed numerically. This converse is the paper's strongest technical contribution.
- **Falsifiability as a genuine surplus over an axiom.** The mechanism specifies the physical conditions under which Born statistics would fail (§8), and the §8.4 discriminator (straight-line-vs-curvature in P′(S), designed to be insensitive to the dressed-mode confound) is a well-constructed, honestly-scoped test. An axiom cannot be wrong in instructive ways; this can.
- **Intellectual honesty is above field norms:** displaying the two self-retracted deviation channels (Table 1), quarantining P5/P6 so the single-detector results don't depend on them, explicitly labeling the 2√2 recovery a "consistency check, not a result," and stating the §8.5 fork rather than burying it.
- **Theorems 4–5 (commit-rate independence + kinematic linearity) are an elegant closure**, making the single-detector statistics exact at any registration speed and grounding rate-linearity in energy conservation rather than assumption.

## 4. Major concerns (numbered; press hardest here)

**4.1 — The core "derivation" may relabel the squaring rather than remove it.** The probabilistic content reduces to two postulates that jointly encode |A|²: P1 (deposited energy ∝ A_i²) and P2 (noise variance ∝ e_i). Given these, P_i = s_i(0) = A_i² is near-immediate. A foundations referee will ask whether moving |·|² from one axiom into the conjunction of P1+P2 is progress or bookkeeping. The paper's honest §9.1 concedes "no derivation from a probability-free theory is possible," but the abstract and §5.5 still read as a stronger claim than §9.1 supports. **Fix:** align the abstract/§5 rhetoric with §9.1; state up front that the achievement is *physical, non-probabilistic, deviation-predicting premises*, not elimination of the squaring.

**4.2 — Potential circularity in P2 via the golden rule.** §5.1 defends P2 as independently motivated because it "does the independent work of generating golden-rule rates." But Fermi-golden-rule rates being ∝ |matrix element|² *is itself* the Born rule at the level of transition probabilities. If P2 inherits its amplitude-linear form from golden-rule phenomenology, the derivation risks assuming a Born-like structure to derive Born. The paper needs to argue that P2's √e scaling is motivated by something *upstream* of golden-rule rates (e.g. the substrate coupling of the DK program) rather than by the rates themselves — otherwise the "one postulate, both jobs" coincidence is a circularity, not a virtue. This is, in my judgment, the single most dangerous objection and it is not currently defused.

**4.3 — The hard part (Bell) is a consistency proof given very strong postulates, and the framing oversells it.** §7's achievement is conditional on P5 (the medium carries the joint amplitude and renormalizes it with fidelity η) and P6 (a preferred foliation ordering the commits). P5 is, essentially, nonlocal collapse re-described as "faithful registry renormalization"; "no-signaling as a theorem" (§7.4) holds only *given* affine-in-ρ statistics, which hold *given* η = 1. So no-signaling is recovered because a no-signaling-compatible update fidelity was postulated. The paper says as much in §7.5, but the §7.4 heading and the abstract claim more. **Fix:** demote "no-signaling emerges as a theorem" to "no-signaling follows from P5's η=1, which is itself measured, not derived," and make the conditional nature unmissable in the abstract.

**4.4 — η = 1 is load-bearing, postulated, and poses a dilemma the paper doesn't fully confront.** Either η = 1 exactly (then no-signaling is put in by hand at the ontic level, via the fidelity postulate) or η ≠ 1 by any amount (then §7.4 predicts real superluminal signaling, which is among the best-tested nulls in physics). The "frame-rotation picture" (§7.3) gestures at why η should be exactly 1 but §9.4(ii) admits no derivation. The paper should state this dilemma plainly rather than presenting η ≳ 0.99 as encouraging.

**4.5 — The §8.5 fork is a lose–lose for the "new physics" framing, and this should be foregrounded, not softened.** If the radical reading holds, the theory predicts mismatched-port superluminal signaling — almost certainly empirically false. If the protective reading holds, the theory becomes empirically equivalent to standard QM (no new physics). The paper favors the protective reading, but its stated ground — "twice already the theorems closed open channels, so the pattern favors closure" — is an inductive over-reach: past self-correction does not entail future self-correction. **Fix:** present the fork's two horns honestly as (wrong) vs (equivalent-to-QM), and drop the pattern-of-closures argument or label it explicitly as heuristic, not evidence.

**4.6 — Missing lineage: the martingale/fixation result overlaps known population-genetics and diffusion mathematics.** The structure "e_i/Σe_j under √e noise is driftless, and fixation probability = initial share" is the neutral **Wright–Fisher / Moran** model and Kimura's neutral-allele fixation result; the underlying SDE is a **Feller / CIR-type** diffusion (multi-allele Wright–Fisher diffusion). None of this is cited. Theorem 1 and Theorem 0 are presented as flowing solely from the dynamical-reduction (Pearle) lineage. This is both a citation-integrity gap and a novelty-calibration issue: the multi-site martingale is arguably known mathematics in a different field. **Fix:** cite the Wright–Fisher/Kimura/Feller literature and re-state precisely what is new (the *identification* of detector noise with the neutral-diffusion structure, and the fairness theorems tying it to premises — not the diffusion mathematics itself).

**4.7 — Empirical grounding is thin; all novel content lives in untested regimes.** Every predicted deviation is in a configuration not yet built (sub-λ radiative arrays, mismatched ports, partially-entangled asymmetric-basis tests). The real-world anchors (CHSH ≈ 2.8, η ≳ 0.99, time-resolved Born) are consistency with known results, not confirmation of anything the mechanism uniquely predicts. That is legitimate for a foundations paper, but the abstract's "closes its timescale requirements in real detectors with orders of magnitude to spare" should not be allowed to read as empirical support for the mechanism — it is an order-of-magnitude plausibility estimate on a toy ladder.

**4.8 — Simulations are low-N in-house toys that largely confirm the analytics.** N ~ 10 sites vs the ~10¹⁰ of a real detector; the martingale reproduces Born partly by construction (a fair game is fair). The runs are valuable as converse-checks (showing the *failure* modes deviate) but should not be presented with the same evidential weight as an independent test. Several figures are unrendered placeholders ("Fig. —"), and the code is cited as "[repository ref]" — a placeholder. This caps reproducibility until resolved.

## 5. Minor / presentational

- Multiple figures are missing/unnumbered ("Fig. —" at §5.3, §5.5); Table 1 referenced before it is anchored.
- Table 2 is somewhat self-flattering (only "This work" earns every favorable column). In particular "Modifies quantum dynamics: no" is defensible only if adding P5/P6 ontology (shared registry + preferred foliation) doesn't count as modifying the framework — worth a footnote conceding that it adds ontic structure even if it leaves the Schrödinger equation untouched.
- The DK-framework provenance (§9.3) and the "[Framework repository]" citation should carry the byline-order confirmation note the draft banner mentions.
- "[repository ref]" (Appendix D) and the framework repository URL must be finalized before submission.
- The abstract is one very long paragraph; consider splitting the claim from the caveats.

## 6. Specific questions for the author

1. Is P2's √e scaling motivated by anything upstream of golden-rule rates? If not, how do you rebut the circularity of 4.2?
2. Can η = 1 be derived, or is it a fidelity postulate equivalent to assuming no-signaling? If the latter, does "no-signaling as a theorem" survive?
3. Under the radical reading of §8.5, what is the predicted signaling magnitude for a realistic mismatched-port geometry, and is it already excluded by existing no-signaling bounds?
4. Why is the multi-site martingale not the Wright–Fisher/Feller diffusion, and if it is, what precisely remains novel?
5. What would falsify the *mechanism* as opposed to falsifying P3? Is there any test whose null would count against the whole picture rather than against one premise?

## 7. Rubric scores (1–5)

- **Novelty — 3.** The conjunction (semiclassical capture + neutral-diffusion selection + fairness-from-premises + deviation ledger) is a genuinely new package, and Theorem 1's uniqueness clause and the §8.4 discriminator are real contributions. But the engine is borrowed (stated), P1 is standard semiclassical detection, and the core martingale overlaps uncited population-genetics mathematics. New as re-description + one clean theorem + an experimental proposal; not a new physical result.
- **Internal consistency — 4.** Tight and unusually self-aware; theorems follow from premises; honest about what is postulated. Docked one point for the abstract/§7.4 rhetoric outrunning the conditional (η-dependent) content it rests on.
- **Evidential grounding — 2.** All novel predictions are in untested regimes; real-world contact is consistency with known QM, not confirmation. Legitimate for the genre but genuinely thin.
- **Reproducibility — 3.** Methods and seeds described (Appendix D), but code is a placeholder ref and multiple figures are unrendered; will rise to 4 once the suite and figures are posted.
- **Citation integrity — 4.** Sources are real, load-bearing, and (spot-checked) correctly characterized; docked one point for the missing Wright–Fisher/Kimura/Feller lineage on the load-bearing martingale result.

## 8. Overall assessment

**3 (sound, in-scope, with real reservations).** This is a careful, honest, well-structured foundations paper whose best material — the uniqueness of the fair scaling, the falsifiability surplus, and the tabletop discriminator — is genuinely worth publishing. It is held back from a 4 by three things a revision can address: the headline "derivation" claim outrunning its own §9.1 concession (4.1–4.2), the Bell result's dependence on strong postulates being oversold as a theorem (4.3–4.4), and the empirical/novelty modesty not being stated plainly enough (4.6–4.8). None of these is fatal; all are fixable by re-calibrating claims to what is actually proved and by foregrounding the η=1/signaling dilemma and the fork's lose–lose structure. The physics is interesting and the honesty is exemplary; the rhetoric needs to descend to meet the honesty.

## 9. Sign-off

`Reviewer: Claude Fable 5 (Anthropic, claude-fable-5), 2026-07-26 — INTERNAL self-review (coauthor); down-weight relative to the external decorrelated panel.`
