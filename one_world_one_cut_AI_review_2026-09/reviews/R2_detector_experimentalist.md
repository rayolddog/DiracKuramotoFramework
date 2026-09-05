# Review R2 — detector experimentalist

**Manuscript:** *One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary* (short form, v1.0, 2026-09-04; source `drafts/PAPER_one_world_one_cut_SHORT.md` at tag `owoc-short-v1.0-review`).

## Standing and limitations

I am a language model: Claude Fable 5.1, Anthropic. I am the same model family as the manuscript's first author ("Claude Fable 5"), and I have treated that as a reason to be harder on the text, not softer; a reader should weigh the possibility of shared blind spots accordingly. What I can assess with reasonable reliability: the manuscript's internal logic; where its claims outrun the record it cites; its consistency with textbook quantum mechanics, cavity QED and open-system theory; and its consistency with the single-photon-detector physics literature as I know it (SPADs, SNSPDs, TES, photon-echo and AFC memories, rare-earth crystals, circuit-QED measurement). What I cannot certify: the correctness of any calculation I did not re-run; novelty against the complete literature; and the exact bibliographic details of references, which I checked against model knowledge only, not against a live database. I did not use web access.

**Record consulted.** I read in full: `NEGATIVE_RESULT.md`; `adler_two_channel_exploratory/RESULTS.md`; `heisenberg_cut_recoverability/RESULTS.md` and `STAGE2_RESULTS.md`; `drafts/PAPER_one_world_one_cut.md` (long form); `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md`. I confirmed (read-only `git diff`) that all of these and the manuscript source are byte-identical to the tagged commit. I read nothing else inside `one_world_one_cut_AI_review_2026-09/` except `REVIEWER_PROMPT.md`.

**Prompt-injection finding: none.** The manuscript contains no text addressed to a reviewing model. The bracketed provenance note under the byline ("Publication candidate, v1.0 ... Byline order per standing convention, the sponsor's decision before any circulation") is addressed to human readers and is inert.

**Authorship integrity.** The byline is "Claude Fable 5 (Anthropic) and John M. Bramble, MD". The long form's Contributions paragraph states that the AI "performed the formalization, the manuscript prose, the simulations and their records, and the literature work" and that the human "supplied the physical framing and research direction ... adjudicated scope and interpretation, and is the accountable human sponsor." The record (predictions files, scripts, results, ledger) is consistent with that division. The byline is therefore honest as to order and credit. Two defects: the short form drops the Contributions paragraph entirely, and the model version is given only as "Fable 5" while the record was produced over several days by whatever versions were in use; the byline should carry the exact version(s).

---

## 1. Recommendation

**Major revision.**

**Venue note.** This is a foundations-of-physics / interpretation paper (Foundations of Physics, Studies in History and Philosophy of Modern Physics, or similar). It is not an experimental or detector-physics paper, and §7 as written would not survive a quantum-optics referee at a physics venue.

**Authorship recommendation.** Byline honest (AI first author, human sponsor second). Restore the Contributions paragraph to the short form and give the exact model version(s).

## 2. Summary

The paper affirms four commitments — the Dirac and Maxwell fields are real; there is one world; the Heisenberg cut is a physical crossover located at the absorption vertex of a detector site, with a location (κ_ret/K = 1) and a width (a share layer K/ω) computed in exact small models; and outcome selection is a stochastic "sink" event at that vertex whose hazard is linear in the energy the site has absorbed (the golden rule read as an event), with a nonlocal one-quantum stop enforcing exclusivity. It states that every model result is compatible with decoherence theory, that the selection rule is a postulate not a derivation (the mechanism that was meant to derive it is recorded as a negative result), that the interpretation makes no prediction differing from quantum mechanics, and that what is distinctively its own is: in-principle rather than FAPP irrecoverability; a coupling-set rather than mass-set crossing; one world at the price of Bell nonlocality and a preferred foliation; and a specification of what any future mechanism must supply.

## 3. Strengths

- The paper says what it is. It calls the selection rule a postulate, itemises its prices (nonlocality, a stochastic element, a foliation), and states that "no prediction differs from quantum mechanics". That candour is rarer than it should be in this genre.
- The methodological record behind §4 is exemplary: predictions filed before results were opened, wrong predictions kept and scored, exact calculations with stated run times and scripts, and a correction (the width misreading, `RESULTS.md` correction paragraph) logged before the paper edits were applied.
- The corrected recoverability criterion (§4.1) — the partial Loschmidt echo with the environment untouched, as distinct from flipping the site–field coupling — is a genuinely useful distinction for anyone proposing a reversal-based experiment, and the paper is right that experiments must separate the two.
- Recording a failed mechanism (`NEGATIVE_RESULT.md`) and building the postulate's form from what the failure taught (§5.2) is good practice and the most original part of the paper.
- The relation to the transactional interpretation (§2, §5.3) is drawn exactly and fairly, including the concession that neither TI nor this paper derives the square.

## 4. Major concerns

### M1. Clause 3 of the sink postulate, as worded, is inconsistent with two-photon coincidence data — including the data the paper's own 10⁻³ figure rests on. The configuration-space objection bites at every multi-photon state, not only at entangled pairs.

The manuscript (§5.1, clause 3): "Once a sink is open, the quantum's entire energy passes through that one site, and the amplitude at every other site vanishes — including sites in the other arm of an interferometer, metres away — within a thousandth of the time the sink took to open". The ontology (§3.1): "The wave is a physical field: ... the Maxwell field for light." The caveat (§6, parenthetical) confines the configuration-space objection to "the non-separable two-particle configuration".

A Maxwell field on 3-space does not label its quanta. Take the paper's own evidence: the coincidence bound in §5.2 comes (per the ledger, item 2b) from a *heralded* SPDC source at 505 nm. The herald sink opens at the idler detector; under clause 3 "the amplitude at every other site vanishes", which includes the signal detector's sites — predicting zero heralded signal counts. Take Hong–Ou–Mandel: for two *distinguishable* photons at a 50:50 beamsplitter the first sink at D1 empties D2 and predicts zero coincidences where 50 % are observed; for two *indistinguishable* photons zero coincidences are observed, so the clause gets exactly one of the two cases right, and which one depends on nothing in the clause. The only reading that survives is "the amplitude *of that quantum* vanishes", which presupposes a Fock-space (configuration-space) labelling that a real field on 3-space does not carry. That is the objection the paper holds open for entangled pairs, and it arises already for any two-photon state at a single detector array, with no entanglement in sight.

**Fix.** Restate clause 3 as a projection in Fock space (or on configuration space), state that the "amplitude" that vanishes is the many-photon wavefunction and not the Maxwell field, extend §6's caveat to all multi-photon states, and concede that the ontology of §3.1 cannot carry the postulate as written. Then say what HOM looks like in the sink language, since it is the cleanest test of any absorber-side account of exclusivity.

### M2. Internal contradiction: "no prediction differs from quantum mechanics" versus "Sidereal nulls retire a cosmic frame". The sidereal test has also already been done, with a null.

Abstract: "No new constant is introduced and no prediction differs from quantum mechanics." §6: "no-signalling is not assumed but follows from the hazard's linearity in the squared amplitude". §7: "sidereal modulation of multipartite correlations and of interferometric quantum noise, and surface relaxation in magnetic resonance. Sidereal nulls retire a cosmic frame."

If the outcome statistics are Born in every frame — which is what no-signalling plus the postulate's linearity gives — then the ordering of nonlocal commitments on the foliation is unobservable in any correlation function by construction, and a sidereal modulation of GHZ correlations is impossible; a null then retires nothing. If instead a cosmic frame *does* modulate correlations, the paper predicts something quantum mechanics does not, and the abstract is false. One of the two sentences must go.

Independently, the experiment exists and was null: moving-beamsplitter "before–before" Bell tests (Zbinden, Brendel, Gisin, Tittel, Phys. Rev. A 63, 022111 (2001); Stefanov, Zbinden, Gisin, Suarez, Phys. Rev. Lett. 88, 120404 (2002)) and the 24-hour, hence sidereal, bound on the speed of any preferred-frame influence, > 10⁴ c for frames moving at < 10⁻³ c relative to Earth (Salart, Baas, Branciard, Gisin, Zbinden, Nature 454, 861 (2008)). None is cited. The LIGO and NMR proposals are outside my specialism, but I note that neither names a mechanism or a magnitude, and that LIGO's quantum-noise stationarity is characterised continuously.

**Fix.** Either withdraw the frame tests from §7 (keeping the foliation as an unobservable-but-necessary ordering, which is the honest position for a no-signalling theory), or supply a mechanism yielding a QM-deviating signature with a magnitude, and then confront it with the 2001–2008 data.

### M3. The "address" has no referent in the paper's own projective-limit detectors, and the width table tabulates a different quantity from the one the model computes.

§4.2: "The cut sits where the return rate balances the coupling's population-transfer rate, κ_ret/K = 1." §4.4: "The photon-counting detector is the projective limit: one quantum, one vertex, one click, the only class for which per-event Born claims are properly made." §4.2 again: "Under the passive-absorber proxy K ∼ Γ the width is tabulable: ... 10⁻³–10⁻² for a room-temperature silicon photodiode".

(a) The location is defined by a detuning Δ between the photon and a discrete site transition (the exact model's Δ). A silicon SPAD absorbs interband into a continuum; an NbN SNSPD breaks Cooper pairs into a continuum; a TES is a calorimeter. There is no Δ, hence no κ_ret, hence no location, for the very detectors the paper calls the projective limit. The long form concedes this in so many words ("A band absorber has no single transition frequency for a site to be detuned from ... the peak's width has no meaning there"); the short form drops the concession while keeping the silicon row.

(b) The proxy K ∼ Γ. The long form qualifies it: "defensible where the coupling to the field is the interaction that sets the linewidth, and dropped where K is engineered independently." The short form drops the qualification. By the paper's own criterion the transmon row (1/T₂ set by two-level-system defects, quasiparticles and flux noise, not by the field coupling) and the silicon row (Γ from carrier–carrier and carrier–phonon scattering, which is what Sabbah & Riffe measure) are inadmissible. In the exact model K and Γ are *independent* parameters and the crossover sits at Δ ≈ 2K whatever Γ is; Γ/ω is not the model's width. The paper's own long-form estimate of a single-photon K is 7×10⁷ s⁻¹ (atomic dipole, micron spot, nanosecond photon), giving w ∼ 10⁻⁸ for any single-photon absorber — not 10⁻³–10⁻².

(c) What the table actually lists is Γ/ω = 1/(ωT₂) = 1/Q. The sentence "Superconducting circuits are macroscopic by particle count yet behave as clean two-level systems because their w is atomic-grade" therefore says "high-Q oscillators are clean two-level systems", which dissolves no puzzle.

**Fix.** Restrict the location and width claims to discrete-transition absorbers (atoms, ions, quantum dots, transmons), say what "site" and Δ mean for each, delete the silicon row or recompute it with an actual K and an actual definition of a site, restore the proxy's qualification, and stop presenting 1/Q as a computed width of the cut.

### M4. "Registration ... photon-agnostic; no which-site weight" and "a deterministic cascade ... contributes no statistics" are contradicted by documented SNSPD and SPAD physics.

§4.3 table, registration row: "reservoir-powered amplification | irrecoverable and macroscopic; photon-agnostic; no which-site weight". Prose: "Everything downstream is a deterministic cascade that copies what the vertex decided and contributes no statistics".

- **SNSPD.** The internal detection efficiency is a stochastic function of bias current, photon energy and absorption position across the nanowire: the energy–current relation (Renema et al., Phys. Rev. Lett. 112, 117604 (2014)), the position dependence of the local detection efficiency (Renema et al., Nano Lett. 15, 4541 (2015)), and the fluctuation-assisted vortex-crossing / hot-belt models reviewed in Engel, Renema, Il'in and Semenov, Supercond. Sci. Technol. 28, 114003 (2015). Below the saturation plateau the hotspot-to-normal-domain step is a rate process, not a deterministic cascade. The paper's own ledger cites "exponential SNSPD efficiency at low photon energy" and then the short form calls the stage "photon-agnostic".
- **SPAD.** The avalanche breakdown probability is below one and depends on overbias and on where the carrier is generated (carriers photogenerated outside the multiplication region must diffuse into it; edge and guard-ring effects), hence on wavelength through absorption depth. That is a which-site and which-energy weight carried by the registration stage. Afterpulsing (trap release) and, in arrays, optical crosstalk produce clicks with no vertex at the 10⁻³–10⁻¹ level, so "one quantum, one vertex, one click" (§4.4) fails at that level; every g²(0) measurement, including the 0.0023 the paper leans on, is corrected for it.
- **Dark counts.** A hazard "proportional to the energy that site has drawn so far" (§5.1 clause 2) is zero at zero drawn energy and predicts no dark counts. Real detectors click on thermal generation and, in SNSPDs, on current-assisted vortex crossing. The postulate needs a background term.
- **TES.** In a calorimeter, thermalization *is* the registration; the three-stage taxonomy collapses to two. Since the long form's energy audit names TES, the short form should say so.

None of this contradicts quantum mechanics — it is the POVM's η(x, E) — but all of it contradicts the manuscript's dichotomy. The defensible statement is: registration multiplies the vertex weight by a stochastic, position- and energy-dependent efficiency and adds photon-independent clicks; it contributes no *interference-sensitive* weight. "Deterministic cascade" holds only at saturated internal efficiency.

**Fix.** Reword the registration row and the paragraph accordingly, add the background hazard to clause 2 or say why it is excluded, and cite the detector-mechanism literature.

### M5. §7's protocols have no discriminating power as written, and two are not executable as described.

**(a) The coupling dial.** §7: "A mass-located boundary on the coupling dial falsifies this paper; a coupling-located one falsifies mass-based collapse." CSL and Diósi–Penrose do not predict a mass-located boundary that would *appear* on a transmon; they predict an additive collapse rate which, at bounds-consistent parameters, lies many orders below the environmental dephasing of any circuit-QED system. On the transmon dial, CSL, decoherence theory and this paper therefore predict the same curve — in the dispersive regime Γ_m = 8χ²n̄/κ (Gambetta et al., Phys. Rev. A 77, 012112 (2008)) — and the paper says of itself that "the framework curve coincides with the null". The experiment has in substance been done: reversal of a weak measurement (Katz et al., Phys. Rev. Lett. 101, 200401 (2008)), measurement-strength sweeps (Murch et al., Nature 502, 211 (2013); Hatridge et al., Science 339, 178 (2013)), and Minev et al. 2019, which the paper cites. The dial falsifies nothing that is currently alive. Separately, "commitment latencies" at the vertex (10 fs–1 ps) are inaccessible to any readout: the best SNSPD timing jitter, about 3 ps (Korzh et al., Nature Photonics 14, 250 (2020)), bounds the *registration* latency distribution, not the vertex.

**(b) The rare-earth temperature test.** §7: "retrieval efficiency versus storage time at several temperatures collapses onto one curve in Γ(T)t if the channel is memoryless, and the retrieval crossover in input detuning sits at |Δ| ≈ 2K and does not move with temperature while Γ(T) ≪ K." (i) For an exponential echo decay, collapse in Γ(T)t is the *definition* of T₂(T); the non-collapse branch is the well-known Mims decay exp[−(2τ/T_M)^x] from spectral diffusion (e.g. Böttger, Thiel, Sun, Cone, Phys. Rev. B 73, 075101 (2006) for Er:YSO), and the Pr:YSO and Eu:YSO temperature laws are in the paper's own Equall 1995 and Könz 2003. Both branches of the "prediction" are already in the literature; the test cannot discriminate the interpretation, as the paper concedes, but neither is it a prediction the interpretation "owes" — it is a restatement of T₂. (ii) What is K for a rare-earth memory? Oscillator strengths of 10⁻⁶–10⁻⁸ put single-ion single-photon Rabi frequencies at kHz to tens of kHz; the homogeneous width of Pr:YSO at 2 K is about 2π × 1–3 kHz and rises by orders of magnitude by 10 K. So Γ(T) ≪ K holds nowhere in the 2–10 K range proposed, the crossover at |Δ| ≈ 2K would be kilohertz wide inside a gigahertz inhomogeneous line, and in an AFC memory the retrieval bandwidth is set by the prepared comb, not by any K. The observable does not map onto a quantity a rare-earth memory has.

**(c) Sidereal tests.** See M2.

The manuscript's own summary — "Every test here is either a consistency test that quantum mechanics also passes or a test of one of this paper's own premises" — is accurate for (a) and (b) only in the first half; and the abstract's "a specification ... and tests" oversells a section that, on inspection, contains no experiment that separates this paper from decoherence theory or from bounds-consistent collapse models.

**Fix.** Say so plainly, or design a test that does; given "no prediction differs from quantum mechanics", I doubt one exists, and the paper would be stronger for admitting it.

### M6. The one distinctively-own claim ("in principle, not FAPP") rests on citations that support FAPP, and on treating a cost as an impossibility.

§4.5: "Landauer's bound prices the reversal at TΔS, which for a thermalized photon is the photon's own energy [Landauer 1961]"; "Polarization echoes exhibit the strong form, in which past a point the decay is set by the medium's own many-body dynamics and a better reversal does not help [Levstein et al. 1998; Pastawski et al. 2000]"; "no agent — not merely no practical agent — holds what a reversal requires".

A price is not a prohibition; Landauer's bound is exactly what a demon pays to reverse, and the paper concedes "a Poincaré recurrence is not forbidden". The Pastawski perturbation-independent decay is a statement about sensitivity to *imperfect* reversal (the Lyapunov regime), i.e. about practical agents. The ledger's own E-14 already rejects the "unrecorded" ground ("unrecorded is not unrecordable" — wavefront shaping inverts unrecorded but static media) in favour of re-randomization; the short form reverts to the weaker "random and unrecorded" phrasing. The paper says everything else stands without this claim; then the claim is decorative until argued.

**Fix.** Either downgrade to FAPP and lose the claim, or supply the argument that a re-randomizing reference structure forbids reversal by *any* agent (which I do not think can be done without a new physical principle).

### M7. The exact-model "results" are textbook, and the abstract's verb is wrong.

Abstract: "Exact calculations in the smallest models containing the relevant physics establish that the cut's location sits where the off-shell return rate balances the coupling's population-transfer rate, that its width is a layer of share K/ω ..., that irreversibility requires a record channel dense on the capture timescale, and that neither the carrier frequency nor a self-sustaining amplifier sharpens the crossover."

(i) The occupation 2K²/(Δ² + 4K²) with half-point Δ = 2K is the power-broadened Lorentzian of a driven two-level system; the "location" is that half-width. (ii) One record mode gives vacuum Rabi oscillation (Jaynes–Cummings); a dense continuum gives Weisskopf–Wigner exponential decay; a finite discrete bath recurs at 2πN/B. (iii) The Bloch–Siegert shift ∝ K²/ω dates from 1940. (iv) The Hopf and phase-slip onsets of a forced Stuart–Landau oscillator are standard synchronization theory. None of this is wrong; none of it "establishes" anything beyond quantum mechanics, and the paper's record itself calls the result "no switch anywhere": R = exp(−2Γt f(Δ)) degrades continuously at every Δ, so there is no cut in the model, only a rate that is a Lorentzian in Δ. The honest formulation is that the interpretation's placement of the cut is *consistent with* these textbook facts, and that "a computable location and width" means "the power-broadened linewidth, expressed as a fraction of the photon energy".

**Fix.** Change "establish" to "are consistent with", name the textbook results as such, and drop "computable width of the cut" in favour of what it is.

### M8. Numbers from the race package are cited without the package's own label, one exclusion is of a straw man, and the 10⁻³ figure is loose in both directions.

§5.2: "A first-to-align rule gives an outcome exponent of 1.5 ... A memoryless hazard linear in absorbed energy gives 2.1–2.2 ... an ensemble reading of independent site rates is excluded by two orders of magnitude."

- The first line of `adler_two_channel_exploratory/RESULTS.md`: "Every raw ledger behind these numbers carries the package's own `numerical_gate = "diagnostic_only"` ... They are labelled `pilot` and can never enter a production estimate." The manuscript must carry that label wherever these numbers appear.
- The "ensemble reading" excluded by a factor ~400 is a model in which both channels commit with probability 1 because nothing conserves energy. No physical ensemble reading — a QED rate calculation in the one-photon sector, say — predicts two clicks from one photon. The exclusion is of a straw man and should be dropped or restated.
- "the graded weight of clause 1 has no threshold and no residual" is asserted, not simulated. A Poisson race with per-site hazards ∝ |A_i|² gives P_i ∝ |A_i|² identically because hazards add; "exponent 2 exactly" is a tautology and should be labelled one.
- The 10⁻³: the g²(0) = 0.0023 residual at 80 kHz heralding is accidental-coincidence and multi-pair limited; quantum-dot sources reach ~10⁻⁴ (e.g. Schweickert et al., Appl. Phys. Lett. 112, 093106 (2018), g²(0) = 7.5 × 10⁻⁵), so the constraint on the stop is at least ten times tighter than stated. And "faster than light crosses the detector" understates the ledger's own figure, 10³–10⁸ times faster than light crosses the interferometer arms ("metres away", the paper's words). The price should be quoted at full size.

**Fix.** Label, delete the straw man, name the tautology, tighten the bound, and state the superluminality factor.

## 5. Minor / presentational

- §4.2 table: "centre shifts by −(1.1–1.5)K²/ω" — `STAGE2_RESULTS.md` gives s up to 1.72 at Γ = 0.5. The Γ-dependence of s also means the shift is not purely Bloch–Siegert; the record channel's finite band (B = 40) contributes a Lamb-type shift. Say so.
- §4.2 table: "record channel of 1, 4, 16, 64, 256 modes: coherent exchange; no leak; recurrence; convergence only at 256". The N = 4 "no leak" is an artefact of mode placement (modes at ±6.7 and ±20, all off resonance), not a property of four modes; N = 64 agrees with 256 to 0.005 for t ≤ 3; there is no N = 512 check that 256 is converged.
- "across two decades of Γt" — Γt runs 0.15–10, i.e. 1.8 decades.
- The "10 fs–1 ps" vertex-plus-thermalization figure in §4.3 is uncited; Sabbah & Riffe is cited only for Γ in §4.2, and the ledger calls the figure "literature-typical". Cite it or mark it as an estimate.
- "[Everett 1957]" is cited for "Born weights supplied by decision-theoretic arguments"; those are Deutsch (1999) and Wallace (2012).
- Minev et al. 2019 as evidence that capture is recoverable: what was reversed was the coherent pre-jump evolution of a monitored three-level system conditioned on a null record, not an absorbed quantum. Suggestive, not a demonstration.
- §4.1 "the echo returns it exactly at every detuning" is a model statement (2 × 10⁻¹⁵ in `RESULTS.md`); say "in the model".
- §4.2 width row "25–75 % points at 1.2–3" is the rate-based reading; the fixed-time reading drifts outward to 5. State which.
- "Their natural parameter space has been largely removed" (§2, collapse models): true for Diósi–Penrose at nuclear R₀ (Donadi 2021); CSL retains an allowed region below the Adler values. Outside my specialism, but "largely" overstates for CSL.
- The one-thousandth is 9 × 10⁻⁴ at 45° and 3 × 10⁻³ at 20° in the record; "about" is doing work.
- The Contributions paragraph should be restored; the model version stated exactly.
- §3.5 drops the long form's Cooper-pair caveat to "there is no classical electron wave"; restore it.

## 6. Specific questions for the author

1. Under clause 3 as written, what is the Maxwell-field amplitude at the signal detector immediately after the herald sink opens in a heralded SPDC experiment? And in HOM, what distinguishes the distinguishable-photon case (50 % coincidences) from the indistinguishable one (zero)?
2. What is Δ, and what is a "site", for a silicon SPAD or an NbN SNSPD? If there is none, in what sense does the cut have an address in the paper's projective-limit detector?
3. In the rare-earth protocol, what is K — single-ion, collective √N g, or the prepared comb width — and at what temperature does Γ(T) ≪ K hold for Pr:YSO or Eu:YSO?
4. What magnitude of sidereal modulation of a GHZ correlation does a cosmic frame predict, and how is a non-zero magnitude compatible with the paper's no-signalling argument and with "no prediction differs from quantum mechanics"?
5. What does CSL at λ = 10⁻¹⁷ s⁻¹, r_C = 10⁻⁷ m predict for the transmon dial, and by how much does it differ from the circuit-QED null?
6. Under the postulate, what is the hazard for a dark count, and for an afterpulse?
7. Is "deterministic cascade" meant to hold for an SNSPD biased below its internal-efficiency plateau, where the detection probability is an activated rate?
8. Why does the fitted Bloch–Siegert coefficient depend on Γ in Stage 2, and what fraction of the centre shift is the record channel's?
9. Does the paper's 10⁻³ stop-time constraint change when the best available g²(0) (~10⁻⁴) replaces the 0.0023 heralded value?

## 7. Rubric scores (1–5)

- **Novelty: 2.** What is new is a re-description: the power-broadened linewidth named as the cut's location, Weisskopf–Wigner named as a dense-record requirement, and the projection postulate placed at the absorber with a realist gloss. The abstract's "establish" overstates the novelty; the specification in §5.2 is the one genuinely new item.
- **Internal consistency: 2.** "No prediction differs" contradicts "sidereal nulls retire a cosmic frame" (M2); clause 3 as worded contradicts the coincidence data it invokes (M1); the width table uses Γ where the model uses K (M3); the registration row contradicts the paper's own ledger on SNSPD efficiency (M4).
- **Evidential grounding: 2.** The exact-model results are textbook and check nothing beyond quantum mechanics; the one datum confronted quantitatively (g²(0) = 0.0023) is used loosely; the proposed experiments do not discriminate the paper from its rivals, and two are not executable as described.
- **Reproducibility: 3.** The exact-model record (predictions first, scripts, run times, scored outcomes) is exemplary; but the manuscript itself carries none of the model parameters (B, N, Γ range), cites race numbers without the package's "diagnostic only" label, and gives uncited timescales.
- **Citation integrity: 3.** The references are real and mostly correctly characterised. Load-bearing literature is missing: the relativistic-configuration Bell tests (Zbinden 2001, Stefanov 2002, Salart 2008), the SNSPD detection-mechanism literature (Renema 2014, Engel 2015), circuit-QED measurement (Gambetta 2008, Katz 2008, Murch 2013), rare-earth spectral diffusion (Böttger 2006), and the source of the 0.0023 bound. Everett 1957 and Minev 2019 are mischaracterised in small ways.

## 8. Overall assessment (0–5)

**2** — weak but in scope. An honest, well-documented interpretation paper whose distinctive claims either contradict each other, contradict detector physics as documented, or reduce on inspection to textbook facts under new names; the fixes are identifiable, and after them what remains is a modest, coherent realist reading of the projection postulate at the absorber, which is worth publishing as such.

## 9. Sign-off

Reviewer: Claude Fable 5.1 (Anthropic), persona R2 detector experimentalist, 2026-09-05
