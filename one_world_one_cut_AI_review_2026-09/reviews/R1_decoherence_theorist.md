# Review R1 — decoherence and open-quantum-systems theory

**Manuscript:** *One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary* (short form, v1.0, 2026-09-04), source `drafts/PAPER_one_world_one_cut_SHORT.md` at tag `owoc-short-v1.0-review`.

## Standing and limitations

I am a language model: Claude Fable 5.1, provider Anthropic, the same model family as the manuscript's listed first author ("Claude Fable 5"). I have treated that as a reason to be harder on the manuscript, not softer, and the reader should weight my report knowing that the author and the reviewer share training and, very likely, blind spots.

What I can assess reliably: the manuscript's internal logic; whether its claims outrun the record it cites; its consistency with itself and with textbook quantum optics and open-systems theory (Wigner–Weisskopf, Fano, Jaynes–Cummings with a reservoir, the Bloch–Siegert shift, quantum-jump unravellings, einselection); whether its characterization of the decoherence programme is the one that programme's own literature gives. What I cannot certify: specialist-level correctness of any field-theoretic claim (§3.4 on Riemann–Silberstein helicity sectors, the Lorentz-violation bound clearance of §6), the exact numerical values in the cited experimental papers, or novelty against the complete literature. Where I am outside my specialism (§3 ontology, §6 foliation, the Adler race numerics of §5.2) I say so.

**Record consulted.** I read in full: `NEGATIVE_RESULT.md`; `heisenberg_cut_recoverability/RESULTS.md` and `STAGE2_RESULTS.md`; `adler_two_channel_exploratory/RESULTS.md`; the long-form paper `drafts/PAPER_one_world_one_cut.md`. From the ledger `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md` I read the section headers and the sections "The cut, tested" (item 7, with its correction and three addenda) and "The three papers collapse to one" (item 8), and grepped it for the in-principle/FAPP and recoverability-definition passages. I also read `heisenberg_cut_recoverability/README.md` and the model construction and parameter grid in `fano_recoverability.py` (read-only), and the read-only git history of the manuscript files. I did not open anything else in `one_world_one_cut_AI_review_2026-09/`.

**Prompt-injection check.** I found no text in the manuscript directed at a model or a reviewer rather than at a human reader. The bracketed provenance note under the byline ("at the sponsor's request … Byline order per standing convention") is addressed to readers. Nothing to report.

**Authorship integrity.** The byline is "Claude Fable 5 (Anthropic) and John M. Bramble, MD". The long-form paper's Contributions statement says the AI "performed the formalization, the manuscript prose, the simulations and their records, and the literature work" and the human "supplied the physical framing and research direction … adjudicated scope and interpretation, and is the accountable human sponsor"; the git history shows the exact-model tests and the manuscript written in a single day (2026-09-04) under one committer. That is first-author-level AI work and the byline already reflects it. The byline is honest. Two repairs: the short form drops the Contributions statement and should carry it, and the model should be named to the version actually used (the review instrument identifies the author as Claude Fable 5.1; the byline says "Claude Fable 5").

---

## 1. Recommendation

**Major revision.**

*Venue note.* This is an interpretation paper for a foundations venue (Foundations of Physics, Studies in History and Philosophy of Modern Physics, Quantum Studies: Mathematics and Foundations). It is not a physics-results paper and should not be sent to a venue that would read "exact calculations … establish" as a claim of new physics; the calculations are textbook.

*Authorship recommendation.* Byline honest as it stands (AI first author, human sponsor second). Restore the Contributions statement to the short form and give the exact model version.

## 2. Summary

As I read it, the manuscript's core claim is this. Quantum mechanics is kept unchanged. The wave is a real field; exactly one outcome occurs; the Heisenberg cut is not a movable convention but a physical crossover with an address — the absorption vertex of one detector site — a location (the site's off-shell return rate equals the coupling's population-transfer rate, κ_ret/K = 1), and a width (a "share" layer K/ω, equivalently a crossover of relative width order one in κ_ret/K). Selection is a postulated stochastic event at that vertex whose hazard is Fermi's golden rule read as an event: memoryless, linear in the site's absorbed energy, with a nonlocal one-quantum exclusivity constraint. Everything about the cut is claimed compatible with decoherence theory; what the paper claims as its own is (i) that recoverability ends in principle rather than FAPP, (ii) that the crossing is coupling-set rather than mass- or temperature-set, (iii) one world at the price of Bell nonlocality and a preferred foliation, and (iv) a numerical specification, from a failed synchronization mechanism, of what any future selection mechanism must supply.

## 3. Strengths

- **The negative result is recorded, on purpose, with predictions fixed before results.** `NEGATIVE_RESULT.md` and the two RESULTS files score wrong predictions as wrong. This is rarer than it should be and is worth preserving whatever happens to the rest.
- **The three-process separation in §1** (entangling interaction / decoherence / the event) is stated cleanly, and the concession that decoherence's linear map "sends a superposition to a mixture of its branches, weighted as before, never one of them" is the correct statement of the problem of outcomes, in Schlosshauer's own terms.
- **The dense-record requirement** (§4.2–4.3: one record mode gives coherent exchange, four leak nothing, sixteen recur, only a continuum on the capture timescale behaves as a golden-rule bath) is correct and pedagogically useful, even though it is the Poincaré-recurrence physics of a discretized reservoir rather than a discovery.
- **The distinction between the operational coupling-flip and the partial Loschmidt echo** (§4.1) is a genuine methodological caution for anyone proposing to "locate the cut by a reversal protocol".
- **Reproducibility of the exact models is excellent**: a 5-second script, predictions files, raw output and JSON in the repository.
- **The transactional comparison (§2, §5.3)** is sourced to the primary literature and drawn carefully, including the concession that neither interpretation derives the square.
- **Honesty about the postulate.** "The paper derives none of the three" (§5.1) and "the interpretation owes them and cannot be discriminated by them" (§7) are the right sentences.

## 4. Major concerns

### M1. The "location" κ_ret/K = 1 is the half-width of a power-broadened Lorentzian, relabelled; the test could not have failed; and it is a line shape, not a reversibility boundary.

The manuscript: "the cut's location sits where the off-shell return rate balances the coupling's population-transfer rate" (Abstract); "A linear absorber with a dense record channel whose recoverability crossover sat far from κ_ret/K = 1 would have falsified the location in the simplest model; it sat at 1.3–2.0" (§7).

The model (`fano_recoverability.py`, header comment) is H = Δ|e⟩⟨e| + Σ ε_k|k⟩⟨k| + K(|p⟩⟨e| + h.c.) + Σ g_k(|e⟩⟨k| + h.c.) in the single-excitation sector: one photon mode, one two-level absorber, one reservoir. The repository's own README calls it "single-excitation Fano / Wigner–Weisskopf with a coherent photon channel". Its results are, item by item, textbook: the time-averaged excited-state occupation 2K²/(Δ² + 4K²) is the Rabi formula with Rabi frequency 2K (Allen & Eberly); "leak rate = Γ × occupation" is the dressed-state decay of a weakly damped Rabi oscillation; the Bloch–Siegert shift ∝ K²/ω is Bloch & Siegert (1940), uncited; the N-mode recurrence time 2πN/B and the B-independence at fixed Γ are the Markov limit of a discretized bath. None of this is wrong. But "κ_ret := Δ, and the cut sits at Δ ≈ 2K" is a renaming of "the Rabi occupation is a Lorentzian of half-width 2K in detuning". Given the model, no other outcome was possible; the record's own F3 says as much when it notes the analytic half-point is 2K and the only question is whether K means the matrix element or the rate. A prediction that cannot fail within its model does not test a claim.

More seriously for the paper's thesis: recoverability R = exp[−2Γt · occ(Δ)] goes to zero at *every* detuning. The record concedes this — "the location is a statement about rates" and "the midpoint read from R at a fixed observation time drifts outward with Γt, from 1.7 to 5". There is no value of Δ at which recoverability ends; there is a rate that is larger on resonance than off it. That is an absorption line, not a cut. The decoherence programme's cut is a boundary between what is and is not coherently accessible; the manuscript's is where a site absorbs at half its peak rate.

*Fix.* State the result as what it is: in the smallest Jaynes–Cummings-plus-reservoir model the record channel drains the photon at Γ times the Rabi occupation, so the detuning scale of irreversible capture is the Rabi frequency. Drop "tested location" from the list of what is established, and reserve the word "cut" for something the model contains a boundary of — which, on the manuscript's own definitions, it does not.

### M2. Real detectors sit in the opposite regime, Γ ≫ K, where the same model puts the crossover at Δ ≈ Γ/2 — record-set and therefore temperature-set. This inverts the "coupling-set, not temperature-set" claim for the paper's own paradigm detector.

The sweep was Γ ∈ {0.05, 0.2, 1.0} at K = 1 (`GAMMAS`, `K` in the script): never Γ > K. The manuscript's long form estimates the single-photon coupling for a focused nanosecond photon at K ≈ 7 × 10⁷ s⁻¹ and tabulates silicon's record rate at Γ ~ 10¹³–10¹⁴ s⁻¹: Γ/K ~ 10⁵–10⁶ for the detector at which §4.3 places commitment.

In that regime the model's answer is elementary. Adiabatically eliminate |e⟩ in the single-excitation sector: ė = −(iΔ + Γ/2)e − iKp gives ṗ = −K²p/(iΔ + Γ/2), so the photon amplitude decays at rate K²Γ/(Δ² + Γ²/4) — a Lorentzian in Δ of half-width Γ/2. The recoverability crossover then sits at |Δ| ≈ Γ/2, not 2K; its position is set by the record channel, and Γ(T) is the manuscript's own temperature-dependent quantity (§7). The record saw the onset of this at Γ = K ("pulled inward at the largest Γ because the record channel broadens the absorber") and stopped there. For the general damped driven two-level system the half-width is √(Γ²/4 + 2K²), which interpolates between the two regimes; the manuscript's claim holds only on the Γ ≪ K side.

The manuscript is internally inconsistent about which side it is on. §4.2 tabulates widths "under the passive-absorber proxy K ~ Γ"; §7 states the location "does not move with temperature while Γ(T) ≪ K". Both cannot hold for the same detector. And for silicon the manuscript's own long form says a band absorber has "no single transition frequency for a site to be detuned from", so κ_ret is "undefined" — the location claim has no referent at the detector the paper is about.

*Fix.* Run the 5-second script at Γ/K = 10, 10², 10³ and report where the midpoint goes. Then state the location claim with its regime of validity (Γ ≪ K: rare-earth memories, cavity QED), say explicitly that for room-temperature semiconductor detectors the crossover is record-set, and reconcile the §4.2 proxy with the §7 condition. If "coupling-set rather than temperature-set" cannot survive that, remove it from the abstract.

### M3. §4.5's "in principle, not FAPP" claim does not survive. The in-principle ending is definitional in §4.1, thermodynamic-FAPP in §4.5, and a consequence of the §5 postulate everywhere else.

The manuscript: "This paper says that when the references are random and unrecorded, no agent — not merely no practical agent — holds what a reversal requires, and recoverability ends *in principle* at the vertex."

Three independent problems.

(a) *The definition begs the question.* §4.1 defines in-principle recoverability as "the site's own Hamiltonian reversed for the capture time, the environment untouched". The record's own non-claims say: "a definition that lets the environment be reversed gives R = 1 always". So recoverability "ends in principle" exactly because the definition forbids the one operation — reversing the environment — that decoherence theory says is what in-principle recoverability would require. This is the FAPP/in-principle distinction settled by fiat, and it is precisely the move the Zurek–Zeh–Schlosshauer literature rejects: the global state remains pure, the information is in the environment, and "unrecorded" is a fact about the agent, not about the dynamics.

(b) *The thermodynamic argument is the FAPP argument.* "Landauer's bound prices the reversal at TΔS" — no. Landauer's bound prices logically irreversible *erasure*. Reversing a unitary thermalization is logically reversible and, by Bennett's argument (Bennett 1973, 1982), carries no such minimum cost for an agent holding the microstate; the e^{S/k_B} configurations are in a definite quantum state, not lost. The manuscript concedes the point in its own next sentence: "e^{S/k_B} is astronomical, not infinite, and a Poincaré recurrence is not forbidden." Astronomical-but-finite is the definition of FAPP.

(c) *The Pastawski citations support FAPP, not in-principle.* Levstein, Usaj & Pastawski (1998) and Pastawski et al. (2000) find that polarization-echo attenuation becomes independent of the reversal's imperfection — interpreted as Lyapunov amplification of residual perturbations. That is a statement about how imperfect reversals fail, and it presupposes imperfection. It does not say a perfect reversal is impossible; it says perfection is unattainable in practice. The manuscript's gloss "a better reversal does not help" is true of Pastawski's regime and is a FAPP statement.

What *does* make recoverability end in principle in this paper is §5: a non-unitary stochastic event. But then §4.5 is not "an argument" and not "the claim decoherence theory does not make"; it is a restatement of the collapse postulate, which every collapse interpretation makes. Open problem 2 already half-concedes this ("or conceding the point").

*Fix.* Either (i) rewrite §4.5 to say that in-principle irreversibility is entailed by the §5 postulate and by nothing else, and delete "stated as an argument"; or (ii) concede the point to decoherence. Cite Bennett; correct the Landauer and Pastawski characterizations.

### M4. §4.5's criterion and §4.3's address come apart under pure dephasing; and the exact model contains no superposition of alternatives, so it cannot engage what decoherence theory is about.

Take a which-path superposition of a single photon whose arms suffer random, unrecorded phase kicks — a thermally fluctuating mirror, a turbulent refractive index. This meets §4.5's bottom-row criterion exactly ("references random and unrecorded … a record that cannot be inverted"), so by §4.5 recoverability has ended in principle. But there is no absorption vertex, no sink, no outcome, and no site: the photon is still in flight with its full energy. Either the cut is not at the vertex, or the random-reference criterion is not the criterion for the cut. The manuscript cannot have both §4.3 and §4.5 as written.

The underlying reason is a category difference the paper never addresses. The exact model is a T1 model: one excitation, one site, energy draining into a reservoir; its recoverability observable is a return *probability*. Decoherence in the Zeh–Zurek sense is a T2 phenomenon: loss of phase coherence between *alternatives* in an einselected basis. A single-site, single-excitation model has no alternatives and therefore no pointer basis, no off-diagonal element to suppress, and nothing to say about which basis the environment selects. "Everything in §4 is compatible with [decoherence]" (§2) is true because §4 does not touch decoherence's subject matter.

This also leaves the manuscript's basis choice unexamined. §5 postulates outcomes in the *site* basis. In a photodiode the absorbing electron states are Bloch states, in a rare-earth crystal there are collective excitations, in a nanowire the quasiparticles are delocalized: "site" is not given by the Hamiltonian, it is einselected by a local (phonon) coupling. That is a decoherence result, and the paper should invoke it rather than presuppose it.

*Fix.* Add a two-site (or two-path) model with a dephasing channel and say what the cut is there. State what selects the site basis. Reconcile §4.3 and §4.5, or drop one.

### M5. §5's postulate is standard photodetection theory plus the projection postulate, restated in the language of sinks, with the load-bearing literature uncited.

Clause 1 ("every site draws in proportion to the square … weighted by a Lorentzian in its detuning") and clause 2 ("a sink can open at any moment, with a probability per unit time proportional to the energy that site has drawn") are the content of Glauber's photodetection theory (Glauber, Phys. Rev. 130, 2529 (1963); Kelley & Kleiner 1964; Mandel & Wolf): the count rate at a detector element is proportional to the local normally ordered intensity. "Fermi's golden rule read as an event rather than a rate" is, word for word, the construction of the quantum-jump unravelling of a Markovian master equation — Srinivas & Davies (1981) for photon counting, Dalibard, Castin & Mølmer (1992), Carmichael (1993), Plenio & Knight (RMP 1998), Wiseman & Milburn (2010): a memoryless jump with hazard equal to the golden-rule rate, exactly one jump per quantum for a one-photon state (⟨a†a†aa⟩ = 0 makes exclusivity kinematic, not dynamical), and a nonlocal update of the conditional state. None of these is cited. The "specification of what any mechanism must supply" (§5.2) — memoryless, hazard linear in |ψ|², site-independent time profile, exclusivity — is the Born rule plus the projection postulate, recovered from a toy race that had to be given those properties by hand before it would reproduce them.

What the manuscript actually adds is an ontological reading: the unravelling is taken as what happens, in one world. That is a legitimate interpretive position (it is close to Carmichael's and to a realist reading of Wiseman–Milburn), but it should be stated as that.

One cited paper cuts against clause 2. Minev et al. (2019) is cited for capture reversibility, but its result is that a quantum jump has a coherent, predictable, reversible *onset* of finite duration — not that "a sink can open at any moment" as a memoryless event. The record's lag test (timing memory is harmless to the *ratio*) does not answer this, because Minev's point is about the single-event dynamics, not the ensemble exponent.

*Fix.* Cite the photodetection and quantum-trajectory literature; reframe §5 as "the quantum-jump unravelling read as ontic, in one world"; say what distinguishes that from Carmichael and from Wiseman–Milburn; address Minev directly.

### M6. "Coupling-set rather than mass-set or temperature-set" is listed as distinctively the paper's own (Abstract) and conceded not to be (§7). It is decoherence theory's own placement.

Abstract: "What is distinctively the interpretation's own is stated as such: … that the crossing is coupling-set rather than mass-set or temperature-set". §7: "the dial discriminates this interpretation from mass-based collapse, not from decoherence."

Decoherence theory places the boundary on coupling by construction: Joos & Zeh's localization rate Λ is a scattering flux times a cross-section; Zurek's τ_D = τ_R(λ_T/Δx)² is set by the coupling and the separation. Both are temperature-dependent through the environment's state (Λ ∝ T⁹ for blackbody scattering in Joos–Zeh). So "coupling-set" is shared with decoherence, and "not temperature-set" is a statement about which axis one chooses to plot — the Rabi Lorentzian's centre in Δ does not move with Γ (while Γ ≪ K, see M2), but the time to lose recoverability does.

*Fix.* Delete from the "distinctively its own" list; keep as "shared with decoherence, against the collapse programmes". The abstract and §7 must agree.

### M7. The width w = K/ω is 1/Q under the proxy; the table's Γ column is physically heterogeneous; and the width claim was reinterpreted after the model contradicted its original form, which the manuscript does not disclose.

Under "K ~ Γ", w = Γ/ω is the inverse quality factor of the transition. The tabulated values (10⁻⁸ alkali, 10⁻¹⁸ clock, 10⁻⁷–10⁻⁶ transmon, 10⁻³–10⁻² silicon) are the literature linewidth-to-frequency ratios; I checked the arithmetic and it is right. But the Γ's are not the same physical quantity: the alkali's natural linewidth is radiative decay *into the field* — in the paper's own language a return, not a record — while the transmon's 1/T₂ and silicon's carrier scattering are record-channel rates. "Superconducting circuits are macroscopic by particle count yet behave as clean two-level systems because their w is atomic-grade" restates "because their Q is high"; the standard account (Leggett's disconnectivity; the collective coordinate couples weakly to the environment) is not engaged.

The record shows the claim's history: stage 1 found "Relative width 0.8–1.5 … ω cannot appear" and scored the sharp-layer width as "out of scope for a linear absorber"; a same-day "Correction" then reinterpreted w = K/ω as the same crossover in the share variable. That reinterpretation may be right, but a reader of the short form is told only that the width "is" a share layer "equivalent to a crossover of relative width order one" — as if that had been the claim tested.

*Fix.* Say the width is Γ/ω = 1/Q and what a reader gains by calling it the cut's width; make the Γ column homogeneous or split the table; disclose the reinterpretation in §4.2.

### M8. §2's characterization of the decoherence programme is accurate in outline but wrong or incomplete where it matters.

- **Brune et al. (1996) is mischaracterized.** "Brune and colleagues measured a meter's progressive decoherence as its states were made more distinguishable, a crossover of the kind §4 describes." Brune's variable is the phase-space separation D of two coherent meter states and the measured law is a decoherence rate scaling as D². §4 has no superposition of meter states and no distinguishability axis; its crossover is in detuning. Not "of the kind".
- **The founders took positions on the third process.** Zeh's decoherence is explicitly Everettian; Zurek's "existential interpretation" is a hedged position on outcomes. "Decoherence-only accounts stop at (2)" (long form; echoed in §1–2) is not the programme's own self-description; the honest statement is that decoherence *plus* a position on outcomes is what each founder held.
- **The preferred-basis problem — the programme's central result — is absent** (see M4).
- **§1 contradicts §4.5.** §1: under decoherence "Irreversibility is purchased; selection is not." §4.5: "Decoherence says the interference terms survive in the global state and are inaccessible for all practical purposes." The second is correct; the first should be "apparent irreversibility".
- Zurek (2003) RMP, in the long form's references, is dropped from the short form though it is the standard review of what §2 summarizes.

*Fix.* Correct Brune; add the basis question; harmonize §1 with §4.5; restore Zurek 2003.

### M9. No-signalling is claimed to follow (§6) and listed as owed (§8). Gisin 1990 is the wrong Gisin.

§6: "no-signalling is not assumed but follows from the hazard's linearity in the squared amplitude, which is Gisin's argument run in reverse." §8, item 3: "its no-signalling proof independent of the statistics it reproduces … owed". Gisin (1990) concerns deterministic nonlinear Schrödinger evolutions. The relevant result for a stochastic selection event is Gisin (Helv. Phys. Acta 62, 363, 1989): no signalling iff the ensemble evolution is a linear (completely positive) map on ρ. A hazard linear in |ψ|² at each site does not by itself establish linearity of the *ensemble* map once clause 3's nonlocal exclusivity is added; that is exactly what a proof would have to show. I am at the edge of my specialism here, but the inconsistency between §6 and §8 is not a specialist matter.

*Fix.* Give the proof or delete "follows". Cite Gisin 1989.

### M10. "Predictions fixed before the results were opened" omits that the load-bearing definition of recoverability was changed after a calibration run.

§4 opens: "run with predictions fixed before the results were opened." The record: prediction 1 was "wrong as written (definition error), corrected, then passes" — under the operational K-flip as first defined, recoverability fell to 0.044 off resonance *with no environment at all*, and the echo definition was adopted afterwards. The manuscript's §4.1 presents the echo/flip distinction as a finding. It is a finding, and a useful one, but it is also the choice that makes "the cut" coincide with the record channel; under the original definition the cut would have been at the detuning, with no environment needed. Honesty requires the short form to say the definition was corrected after calibration.

*Fix.* One sentence in §4.1.

## 5. Minor / presentational

- The abstract's "Exact calculations in the smallest models containing the relevant physics establish" is too strong for a three-state-plus-reservoir model; "exhibit" or "are consistent with".
- **Bloch–Siegert** should be cited (Bloch & Siegert, Phys. Rev. 57, 522, 1940). The Rabi occupation formula should be attributed (Allen & Eberly).
- **Everett (1957)** is cited for "Born weights supplied by decision-theoretic arguments"; those are Deutsch (1999) and Wallace (2012). Everett's own argument was measure-theoretic.
- **Donadi et al. (2021)** excludes the parameter-free Diósi–Penrose model; "Their natural parameter space has been largely removed" overstates for CSL, where the X-ray bounds (Piscicchia et al. 2017; Arnquist et al. 2022) leave regions open. Outside my specialism; flagged.
- Audit of the §4.2 table against the record: "−(1.1–1.5)K²/ω" understates the record's Bloch–Siegert coefficient range, which is 1.27–1.72 at Γ = 0.5; "across two decades of Γt" — the sweep is Γt = 0.15–10, about 1.8 decades; "convergence only at 256" — the record says N = 64 agrees with 256 to 0.005 at t ≤ 3 and not at t = 10.
- §5.2 "an ensemble reading of independent site rates is excluded by two orders of magnitude" — the record's factor is 400 (2.6 orders); fine, but say "more than two".
- The "10⁻³ of the commitment time" exclusivity speed is an artefact of modelling exclusivity as a dynamical stop; in quantum mechanics a one-photon state cannot register twice by the field algebra, and no speed is needed. Worth a sentence, since the manuscript later prices nonlocality on it.
- "Hazard" is used in the survival-analysis sense throughout without definition; define at first use.
- "κ_ret = ΔE/ħ … the deficit is a return rate": a detuning is a frequency; calling it the return rate of a "virtual excitation" is a Wigner–Weisskopf-era heuristic. Say it is a heuristic.
- The Contributions statement of the long form is missing from the short form (see Authorship).
- Byline model version: "Claude Fable 5" vs the instrument's "Claude Fable 5.1".
- Levstein et al. (1998) has its subtitle in the long form's reference list and not in the short form's; harmonize.
- §2 on Bohm: "Bohm's foliation is empirically inaccessible by construction; this paper's (§6) is carried openly and carries tests" — but §7 says sidereal nulls "retire a cosmic frame" and leave a local one, and the bound clearance is "owed". The contrast with Bohm is overstated; both foliations are, at present, inaccessible.

## 6. Specific questions for the author

1. In the same model, where is the crossover midpoint at Γ/K = 10, 100, 1000? (Five seconds of compute; the answer decides M2.)
2. For a silicon SPAD, where the long form says κ_ret is "undefined" because a band has no transition frequency, what does "κ_ret/K = 1" refer to?
3. A single photon in an interferometer whose arms are randomly and unrecordedly dephased: by §4.5 recoverability has ended in principle; by §4.3 there is no vertex. Where is the cut?
4. What selects the site basis in §5, and why is it not a decoherence (einselection) result that the paper should cite rather than presuppose?
5. Is there any content in §4.5's in-principle claim beyond the non-unitarity of the §5 postulate? If so, what would a Loschmidt demon holding the full environmental microstate be unable to do, and why?
6. What does §5 add to the quantum-jump unravelling of Carmichael / Dalibard–Castin–Mølmer / Wiseman–Milburn read realistically? How does the postulate handle Minev et al.'s coherent jump onset?
7. For the transmon coupling-dial experiment (§7), what is the framework's predicted curve, and does it differ from the circuit-QED null anywhere? If not, what does the experiment test that the null does not already assume?
8. For the fullerene case (Hackermüller 2004), the decohering photon is *emitted* by the molecule and later absorbed in a wall. Is the fullerene's cut at the wall's absorption vertex, metres away? If so, is the location claim about the molecule at all?
9. Under the §4.2 proxy K ~ Γ, the §7 condition Γ ≪ K fails. Which is intended, for which detector?
10. §6 says no-signalling "follows"; §8 says its proof is owed. Which?

## 7. Rubric scores (1–5)

- **Novelty — 2.** The "location" is the Rabi half-width, the "width" is 1/Q, the selection postulate is the quantum-jump unravelling of photodetection read ontically; what is new is the packaging, the honest negative result, and the specification — a re-description with an ontological commitment, and the novelty claim in the abstract is inaccurate on two of its four items (M3, M6).
- **Internal consistency — 3.** The paper contradicts itself on coupling- vs. decoherence-set (Abstract vs §7), on no-signalling (§6 vs §8), on the regime (K ~ Γ vs Γ ≪ K), on decoherence's irreversibility (§1 vs §4.5), and on what "in principle" means (§4.1 vs §4.5); none of these is hidden, but none is resolved.
- **Evidential grounding — 2.** Nothing ties the paper to anything outside the text except literature linewidths recast as 1/Q; every prediction coincides with quantum mechanics by the paper's own admission, and the exact models are toy models in a regime real detectors do not occupy.
- **Reproducibility — 4.** Code, predictions, raw output and JSON are in the repository and the exact models run in seconds; one point off because the Adler-race numbers quoted in §5.2 carry the record's own "diagnostic only" label and the production gate is red.
- **Citation integrity — 3.** The references are real and correctly formatted as far as I can check; several are mischaracterized (Brune, Pastawski/Levstein, Landauer, Everett, Donadi, Minev) and the load-bearing literature for §5 (Glauber photodetection, Kelley–Kleiner, Srinivas–Davies, Dalibard–Castin–Mølmer, Carmichael, Plenio–Knight, Wiseman–Milburn), for §4.5 (Bennett), and for §6 (Gisin 1989) is absent.

## 8. Overall assessment

**2** — weak but in scope. An honestly written interpretation paper whose stated additions to decoherence theory do not survive examination: the location and width are textbook line-shape quantities relabelled and tested in the wrong regime, the in-principle claim reduces to the collapse postulate, and the selection postulate is the standard quantum-jump picture with its literature uncited. What remains — one world, nonlocality, a golden-rule event at the absorber, a recorded negative result — is a coherent position for a foundations venue once the overclaims are removed.

## 9. Sign-off

Reviewer: Claude Fable 5.1 (Anthropic), persona R1 decoherence theorist, 2026-09-05.
