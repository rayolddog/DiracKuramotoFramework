# Review R4 — *One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary* (short form, v1.0, 2026-09-04)

**Persona:** R4, transactional-interpretation and scholarship referee.

## Standing and limitations

I am a language model: Claude Fable 5.1, made by Anthropic. I am the same model family as the manuscript's listed first author ("Claude Fable 5 (Anthropic)"), and I have treated that as a reason to be harder on the submission, not softer; where I found myself inclined to accept a phrasing because it is the kind of phrasing I would produce, I re-checked it against the record or the cited source.

What I can assess reliably: the manuscript's internal logic; whether its claims outrun their stated support; its consistency with itself, with the repository record it cites, and with textbook quantum mechanics; whether each cited work exists and is characterized accurately, which I checked against the sources themselves where I could reach them. What I cannot certify: specialist-level correctness of the exact-model numerics (I did not re-run any script); novelty against the complete literature (I checked the transactional and direct-action lineage closely and the rest only at the level of the reference list); and any one-loop QFT, of which this paper contains none.

**Record files consulted, in full:** `NEGATIVE_RESULT.md`; `adler_two_channel_exploratory/RESULTS.md`; `heisenberg_cut_recoverability/RESULTS.md`; `heisenberg_cut_recoverability/STAGE2_RESULTS.md`; `drafts/PAPER_one_world_one_cut.md` (the long form); `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md`. I read nothing else inside `one_world_one_cut_AI_review_2026-09/` except `REVIEWER_PROMPT.md`.

**Web verification used:** yes. I retrieved and read the text of Kastner (2012) arXiv:1204.5227, Kastner & Cramer (2018) arXiv:1711.04501, and Kastner's 2016 overview arXiv:1608.00660; the abstracts of Boisvert & Marchildon (2013) arXiv:1207.5230, Marchildon (2017) arXiv:1712.03060, and Kastner (2017) arXiv:1709.09367; the abstract of Cramer & Mead (2020) *Symmetry* 12, 1373; the IOP records for Davies (1971, 1972); the records for Pegg (1975) and Hoyle & Narlikar (1969); Steck's alkali-data revision history; and the table of contents of the York mirror of Cramer (1986). Every other reference in the list I checked against my own bibliographic knowledge only.

**Prompt-injection check:** none found. The only text addressed to anyone other than a scientific reader is the bracketed provenance note under the byline ("at the sponsor's request … Byline order per standing convention, the sponsor's decision before any circulation"), which addresses the human reader, not the reviewer or a model. Nothing in the manuscript asks a reviewer to score, skip, or ignore anything.

**Authorship integrity check:** the byline lists the AI first and the human second. The long form carries a Contributions statement ("Claude Fable 5 (Anthropic) performed the formalization, the manuscript prose, the simulations and their records, and the literature work. John M. Bramble, MD supplied the physical framing and research direction … adjudicated scope and interpretation, and is the accountable human sponsor"). That statement is consistent with the provenance visible in the ledger (nearly every simulation and edit is logged as done by the model "at JB's instruction" or "at the sponsor's word", with the framing questions, the sink formulation, the temperature dial, and the decision to record the negative result attributed to JB). The byline order is therefore honest. Two defects: the short form has **dropped** the Contributions statement, so a reader of the submitted paper cannot see this; and the byline names a model *family* ("Claude Fable 5") rather than a version and date, which for an AI author is the analogue of an ORCID and is needed for reproducibility of the authorship claim.

---

## 1. Recommendation

**Major revision.**

**Venue note:** an interpretation-of-quantum-mechanics venue (Foundations of Physics, Studies in History and Philosophy of Modern Physics, or the International Journal of Quantum Foundations, where the transactional exchange this paper engages actually lives). It is not a paper for a physics-results journal: by its own statement it "modifies no equation, introduces no constant, and makes no prediction that differs from quantum mechanics as used."

**Authorship recommendation:** byline honest as to order and credit; revise the front matter — restore the long form's Contributions statement to the short form, give the AI author's exact model version and the dates of its work, and replace "sponsor" with standard author-role language (corresponding and accountable author).

## 2. Summary (to fix terms)

The paper states an interpretation with four commitments: the Dirac and Maxwell fields are real; there is exactly one world; the Heisenberg cut is a physical crossover located at the absorption vertex of a detector site, sitting where the off-shell return rate of a partially excited site balances the coupling's population-transfer rate (κ_ret/K = 1), with a width that in the share variable is K/ω; and outcome selection is a stochastic event at that vertex whose hazard is the golden rule's, linear in absorbed energy, with a nonlocal one-quantum constraint that makes exactly one site complete. The cut claims are supported by exact calculations in a one-photon, one-absorber, many-mode-record model (location, order-one width in the rate variable, dense-record requirement, Bloch–Siegert shift only, amplifier kinks rather than sharpens). The selection claim is a postulate whose form is said to be constrained by a failed attempt to derive it from a race among phase-locked Adler clocks, which is recorded as a negative result. The paper claims everything in its cut section is decoherence-compatible and that what is its own is: recoverability ending in principle rather than FAPP, a coupling-set rather than mass-set boundary, one world with its nonlocality and a preferred foliation, and a numerical specification of what any mechanism for selection must supply. The transactional interpretation is named as the nearest neighbour; the paper says it adds to it "the address" of the cut and that neither interpretation derives the Born square.

## 3. Strengths

- The three-process decomposition of "measurement" (entangling interaction, decoherence, event) in §1 is stated cleanly and the paper is candid that it postulates the third rather than deriving it.
- The criterion of §4.1 — in-principle recoverability defined operationally as the partial Loschmidt echo with the environment untouched, distinguished from the experimenter's coupling flip — is a genuinely useful sharpening, and the record shows it was forced by a wrong prediction that was recorded rather than hidden.
- The dense-record requirement (one record mode gives coherent exchange; four leak nothing; sixteen recur; the continuum needs ~256) is a small, real, checkable result and is correctly presented as a physical requirement on detectors and on models.
- The pre-registration discipline is real: predictions are fixed before runs, wrong predictions are scored as wrong, and a mechanism that failed is published as a negative result. That is rarer than it should be.
- The reference list is entirely real. I found no fabricated or garbled entry; volume and page numbers are correct wherever I could check them.
- §2 is unusually explicit about what is shared with and bought from each neighbouring framework, which makes the paper reviewable at all.

## 4. Major concerns

### M1. §2 and §5.3 contradict each other on whether the transactional interpretation derives the Born rule, and §5.3's statement is neither accurate nor charitable

§2 says: "Kastner and Cramer define an absorber as an atom or molecule and derive the Born rule for radiative processes as the offer–confirmation product [Kastner & Cramer 2018]." §5.3 then says: "Both put actualization at the absorber and get the square from the structure of a rule. … Neither derives the square." And §2 again: "in neither is the square explained."

The sources are unambiguous about what they claim. Cramer (1986), abstract: the transaction "leads in a natural way to justification of … the Born probability law." Kastner (2012), §1: the 1986 paper "showed how the interpretation gives rise to a physical basis for the Born Rule"; and later, "In the standard approach, this final amplitude is squared to obtain the probability … but the squaring process has no physical basis — it is simply a mathematical device (the Born Rule). In contrast, according to PTI … The product of the offer … and the confirmation … corresponds to the Born Rule." Kastner (2016), §2 heading: "How TI explains von Neumann's Measurement Process and the Born Rule." Kastner & Cramer (2018), abstract: "the Born Rule is explicitly derived for radiative processes"; body: "the Born Rule is explicitly derived in the direct-action theory from the fact … that radiative processes … occur only when there is both emission and absorption; neither is a unilateral process … If, instead, we calculate the amplitude for both processes together, we actually end up squaring the amplitude for either process, arriving at the Born Rule."

So the transactional literature does claim a derivation, and the 2018 derivation is not "a rule about products" in the sense the manuscript's §5.3 gives it: it is an argument that in a direct-action theory a real photon requires both an emission vertex and an absorption vertex, each carrying one factor of the coupling amplitude, so that the probability of the observable half-process is the square of its amplitude. One can dispute that argument (the identification of the confirmation amplitude with ψ*, and of the coupling constant with an amplitude for response, can be read as stipulations that import the square), and that dispute is a legitimate thing for this paper to enter. But the manuscript does not enter it; it asserts the conclusion, in one sentence, against the explicit claim of the papers it cites, while §2 has just conceded the derivation exists. A reader who knows the literature will read §5.3 as either careless or as levelling the field so that the paper's own postulate does not look weaker than its neighbour's derivation.

**Fix.** Choose one. (a) Concede the asymmetry: "Kastner and Cramer claim a derivation of the square for radiative processes; this paper postulates it," and delete "Neither derives the square." Or (b) keep the claim and argue it: state precisely which step of the 2018 derivation you regard as a stipulation, and cite the critical exchange that already exists — Marchildon (2017) arXiv:1712.03060, Kastner's reply arXiv:1712.09697, and Marchildon's review of Cramer's *The Quantum Handshake* (cited by Kastner & Cramer themselves as their reference [11]). Either way, remove the flat "in neither is the square explained" from §2 or attribute it as this paper's opinion.

### M2. The paper's central novelty claim against TI — "the address" — is anticipated by Kastner's relativistic TI, and the paper does not engage that

§5.3: "What this paper adds is the address: a location for the cut that has been tested, a width, a dense-record requirement, and a timescale audit placing commitment at the vertex." §2: "it locates the cut, gives it a width, and has tested the location."

Kastner & Cramer (2018), the paper cited: "we can now quantify the circumstances of absorber response, which allows for identification of the typical scale at which the measurement transition takes place and allows for placement of the 'Heisenberg Cut' at the appropriate microscopic (or possibly mesoscopic) level of absorption by individual atoms or molecules." Kastner (2017), abstract: "absorption is quantitatively defined in unambiguous physical terms. RTI therefore provides a well-defined terminus to what appears to be a necessary infinite regress concerning 'absorption'." Kastner (2012): "'absorption' simply means annihilation of a quantum" via coupling between currents, with the micro/macro boundary set by the coupling amplitude and the number of charges (the (0.99995)^(10^23) argument, §4 of that paper).

That is: RTI already (i) places the cut at the absorption vertex of an atom or molecule, (ii) identifies the physical variable as the coupling (the fine-structure constant as the amplitude for an offer or confirmation), and (iii) claims the placement is physical, not conventional. The manuscript's "address" is the same address. What this paper adds beyond RTI is narrower than §5.3 says: a rate-balance criterion (κ_ret/K = 1) verified in a one-absorber toy model; the dense-record requirement; and the observation that the coupling flip is not the echo. The "width" is not an addition (see M8). The "timescale audit placing commitment at the vertex" is drawn from the ledger's E-16 thread, which the ledger itself labels as resting on literature-typical inputs spanning two orders of magnitude.

**Fix.** Rewrite the TI comparison so that it says what RTI already claims about the location of the cut and the coupling as its variable, and then states exactly what this paper adds: the rate-balance form of the location, its test, and the record-channel density requirement. Cite Kastner (2017) IJQF and Kastner & Cramer (2018) for the placement claim, not only for the absorber definition.

### M3. Boisvert & Marchildon (2013) is mischaracterized; the critique the paper wants is Marchildon (2017), which it does not cite

§2: "the absorber's definition has been criticized as underspecified [Boisvert & Marchildon 2013]."

The Boisvert & Marchildon abstract: the paper analyzes "different devices involving contingent absorbers or various types of interaction-free measurements [that] have been proposed as threatening the original version of the transactional interpretation," follows the waves through the quantum-liar Mach–Zehnder, and concludes "there is no need to resort to the hierarchy of transactions that some have proposed" and that TI "is consistent with the block-universe picture of time." It is a *defence* of TI's consistency in contingent-absorber scenarios, not a critique that the absorber is underspecified. The critique with that content is Marchildon (2017), "Remarks on the Relativistic Transactional Interpretation," whose abstract says Kastner and Kastner & Cramer "argue that [RTI] provides a clear definition of absorbers and a solution to the measurement problem … I then argue that a specific proposal to locate the origin of nonunitarity is flawed"; and the concern itself is acknowledged inside Kastner (2012): "A longstanding concern about the basic TI picture has been that the circumstances surrounding absorption are not well-defined, and that 'absorber' could therefore be seen as a primitive term." Note the structure of what the manuscript has done: it cites Kastner & Cramer (2018), which is the *reply* to Marchildon, and attributes the criticism it replies to, to a different paper by Marchildon that says something else.

**Fix.** Replace the Boisvert & Marchildon citation in that sentence with Marchildon (2017) arXiv:1712.03060 (and, for balance, Kastner's reply arXiv:1712.09697). If Boisvert & Marchildon is retained, characterize it as what it is: a treatment of contingent absorbers and interaction-free measurement that concludes TI survives them.

### M4. "Sets spin aside" is textually supported but presented as a structural limitation of RTI when the source says the opposite, and the paper's own Dirac-field ontology is inert in every calculation

§2: "Kastner's relativistic version adopts Davies' direct-action electrodynamics with fermionic currents as sources and sets spin aside [Davies 1971, 1972; Kastner 2012]."

Kastner (2012), §3: "For conceptual purposes I will discuss a simplified version of this process in which I ignore the spin of the fermions and treat the coupling strength … as a generic quantity g. (The basic points carry over to the detailed treatment with spinors.)" So the phrase is accurate about one worked example (Bhabha scattering, lowest order) and inaccurate about the theory: Davies' direct-action QED, which RTI adopts, is built on Dirac currents with their full spinor structure, and Kastner explicitly claims her points survive the spinor treatment. Presenting the pedagogical simplification as "sets spin aside" insinuates a gap the author denies. The long form makes the insinuation explicit ("no one in the transactional lineage has included the Dirac spinor structure in a microscopic description of the absorber"); the short form softens the wording but keeps the implication by placing it in the list of what TI lacks.

The implied contrast is also one this paper has not earned. Its ontology (§3.1) is "the Dirac field for matter," but the absorber in every exact calculation cited in §4 is a two-level system in the rotating-wave approximation, a quantum Rabi model, or a classical Stuart–Landau oscillator; no spinor appears anywhere in the tested physics. On the point of spin, this paper and RTI are in the same position.

**Fix.** Quote Kastner accurately, including the caveat, and drop the item from the list of what TI lacks unless the paper uses spinor structure somewhere.

### M5. The comparison with TI omits the one cost this paper pays that TI does not, and lumps two ontologies that differ on the paper's first commitment

§6: "Nonlocal commitments must be ordered, and the ordering is a preferred slicing … As written this is explicit low-energy Lorentz violation confined to measurement." §2 lists what is "Shared with this paper: actualization at the absorber, one world, nonlocality" and what is "Different: this paper has no advanced waves."

Both Cramer and Kastner claim that their nonlocality comes without a preferred frame. Kastner (2012), §1, restating Cramer (1986): "the realization of a transaction occurs with respect to the endpoints of a space-time interval or intervals, rather than at a particular instant of time, the latter being a non-covariant notion." Kastner (2016): the probabilities of transactions "are Poissonian (a requirement for relativistic covariance of the set)." Whether those claims succeed is arguable, but they are the claims, and they mean the honest ledger of costs is: TI buys one world plus nonlocality with advanced waves and no foliation; this paper buys one world plus nonlocality with a foliation and "explicit low-energy Lorentz violation" whose clearance of every established bound is, by §6's own admission, "owed." That is the largest difference in price between the two, it cuts against this paper, and the comparison does not state it.

Separately, §2 treats "Cramer's interpretation" and "Kastner's relativistic version" as one neighbour sharing this paper's first commitment. Kastner's *possibilist* TI holds that offer and confirmation waves are not spacetime fields at all but elements of a pre-spatiotemporal space of possibilities (Heisenberg's potentia, in her own framing). On the commitment "the wave is real [as a field on spacetime]," PTI is not a neighbour; Cramer's original TI is closer. The paper cites the 2012 possibilist paper by title and never mentions the word "possibilist" or what it denies.

**Fix.** Add the foliation to the TI/this-paper cost comparison in §2 and §5.3 and say TI claims to avoid it. Distinguish Cramer's TI from Kastner's PTI on the reality-of-the-wave commitment.

### M6. The direct-action and transactional lineage is thinly cited, and the one paper that supplies what the manuscript says the lineage lacks is missing

§2: Cramer "treated the absorber functionally, without microscopic description."

Three omissions matter. (i) Cramer & Mead (2020), "Symmetry, Transactions, and the Mechanism of Wave Function Collapse," *Symmetry* 12, 1373, gives exactly a microscopic two-atom dynamical model of transaction formation — electromagnetic coupling factored into matched retarded and advanced vector-potential Green's functions, with energy conservation enforced and the Born rule claimed to emerge from the mechanism. Whether one accepts it or not, its existence falsifies "without microscopic description" as a statement about the lineage. (ii) The direct-action lineage between Wheeler–Feynman and Davies is Hoyle & Narlikar (1969, *Ann. Phys.* 54, 207, "Electrodynamics of direct interparticle action. I. The quantum mechanical response of the universe"; and 1971), which Kastner & Cramer (2018) themselves invoke ("any quantized field theory can be re-expressed as a direct action theory, as shown by Narlikar"); and Pegg (1975, *Rep. Prog. Phys.* 38, 1339, "Absorber theory of radiation"), the standard review of quantum absorber theory. A paper that names TI as its nearest neighbour should locate TI in its own lineage. (iii) Kastner's later statements of RTI's account of measurement and of its relation to decoherence — Kastner (2017/2018) IJQF, "On the status of the measurement problem: recalling the relativistic transactional interpretation," and Kastner (2020) IJQF, "Decoherence and the transactional interpretation" — are the TI-side counterparts of this paper's §2 and §4.5 and are absent.

**Fix.** Cite Cramer & Mead (2020) and revise "without microscopic description"; add Hoyle & Narlikar and Pegg to the lineage sentence; cite Kastner (2017) for the placement claim (see M2) and Kastner (2020) where §2 discusses decoherence.

### M7. The §5.2 "requirements list" is presented as a specification any mechanism must meet, but three of its four clauses are properties of the discarded Adler-clock substrate, one of them is asserted against the record's own "not established," and one is a triviality dressed as a finding

§5.2: "An attempt to derive it from a synchronization dynamics … was tested exhaustively … Its residue is a specification."

Take the clauses in turn.

(a) "A first-to-align rule gives an outcome exponent of 1.5 in the coupling, with the site count entering only as its logarithm." This is a fact about self-sustaining phase oscillators with sharp Arnold tongues (RESULTS.md, entry-time order statistics: 1.52 from the deterministic skeleton). The ontology of §5.1 clause 1 is a *linear* absorber that "has no phase of its own"; for it "alignment" is undefined, so the clause constrains nothing a successor mechanism for *this* ontology could propose.

(b) "A memoryless hazard linear in absorbed energy gives 2.1–2.2, the Born value plus a tenth of a power that belongs to the sharp eligibility threshold of a self-sustaining oscillator and does not go away with grid, window, pulse, or noise." The numbers match the record (2.09–2.21). The attribution does not. RESULTS.md, adiabatic section: "**What is not established.** The mechanism of the residual. Three candidates remain unseparated"; and its final addendum, after the separating run: the extreme-value reading is "Consistent with, not established." The long form (§4.2) says of the same residual, "Its mechanism is an open item of the record, not of this paper." The short form has upgraded "consistent with, not established" to "belongs to."

(c) "the graded weight of clause 1 has no threshold and no residual." No simulation of a graded-Lorentzian race exists in RESULTS.md; the ledger (item 8 addendum, 2026-09-04, late) records this as a sentence added to §4.2 at the sponsor's word ("with a graded weight the square is per site and the exponent is exactly 2"). It is not a finding; it is the competing-exponentials identity: if site i has hazard h_i(t) = c|A_i|² f(t) with a common profile f, then P(i first) = |A_i|²/Σ_j|A_j|² exactly. That is the Born rule *assumed* in the hazard, and it should be said so in one line rather than listed as something the tests established.

(d) The exclusivity clause — the one-quantum stop must act within ~10⁻³ of the commitment time — is the only clause that survives the change of substrate, and it does match the record (9 × 10⁻⁴ at 45°, 3 × 10⁻³ at 20°). But the physical translation to "faster than light crosses the detector" rests on a race-time-to-physical-time mapping that RESULTS.md calls "a choice," and the "ensemble reading … excluded by two orders of magnitude" (record: ×400) excludes a model in which two ports of a one-photon field click independently with no exclusivity at all — a model no ensemble interpretation of quantum mechanics holds.

Finally, "tested exhaustively" is not the record's description of itself. RESULTS.md opens: "Every raw ledger behind these numbers carries the package's own `numerical_gate = "diagnostic_only"` … They are labelled `pilot` and can never enter a production estimate." NEGATIVE_RESULT.md: "every physics result stays labelled diagnostic." The short form carries none of those labels.

**Fix.** Carry the diagnostic label into §5.2. Delete (a) or restate it as a fact about phase-oscillator substrates; restate (b) with the record's own status ("consistent with, not established"); state (c) as the identity it is; keep (d) with its mapping caveat. Then say plainly what the specification reduces to once the substrate is gone: the hazard must be proportional to |ψ|² (which is the Born rule restated), and exclusivity must be nonlocal.

### M8. The abstract and §1 claim more than the body delivers on three points: differing predictions, the "computable width," and no-signalling

(i) Abstract: "no prediction differs from quantum mechanics." §6: "explicit low-energy Lorentz violation confined to measurement." §7: "sidereal modulation of multipartite correlations and of interferometric quantum noise … Sidereal nulls retire a cosmic frame." A positive sidereal modulation of Bell correlations would be a prediction that differs from quantum mechanics. The paper cannot promise none and then offer frame tests; it must say "no prediction differs from quantum mechanics if the frame is local; a cosmic frame would, and §7 says where."

(ii) Abstract: exact calculations "establish that … its width is a layer of share K/ω equivalent to a crossover of relative width order one in the return-rate variable." The equivalence is a change of variable, not a result: with share s = e/E₀ and deficit ΔE = (1 − s)ħω, κ_ret = (1 − s)ω, so κ_ret/K ~ 1 *is* 1 − s ~ K/ω. The exact model cannot see ω at all (RESULTS.md F4: "ω cannot appear in a rotating-wave model, and did not"), so nothing about a width in ω was established; the location claim was. And under the paper's own proxy K ~ Γ, the "width" K/ω = Γ/ω is the inverse quality factor; the tabulated 10⁻⁸ (alkali line), 10⁻¹⁸ (clock transition), 10⁻⁷–10⁻⁶ (transmon) are Q⁻¹ of familiar systems. Calling Q⁻¹ "the width of the Heisenberg cut" and then explaining that transmons "behave as clean two-level systems because their w is atomic-grade" is circular: a transmon is a clean two-level system because its coherence time is long compared with its period, which is what Q⁻¹ measures.

(iii) §6: "no-signalling is not assumed but follows from the hazard's linearity in the squared amplitude, which is Gisin's argument run in reverse." §8, open problem 3: "the covariant formulation of the selection event on the foliation, with its no-signalling proof independent of the statistics it reproduces … owed." The body claims the result and the open-problems list says it is owed. Gisin (1990) shows that a nonlinear evolution permits superluminal signalling; the converse, for a stochastic nonlocal one-quantum constraint acting on a preferred foliation, is not "Gisin in reverse" and is not proved anywhere in the paper.

**Fix.** Qualify the abstract's "no prediction differs" as conditional on a local frame; state the width as a change of variable and the table as Q⁻¹ under the proxy; replace "follows" in §6 with "is required for consistency and is owed (§8)."

### M9. Two citation characterizations outside the transactional literature are wrong, and one is used for a converse it does not contain

- §2: "Everett … with the Born weights supplied by decision-theoretic arguments whose adequacy is contested both ways [Everett 1957]." Everett (1957) contains no decision-theoretic argument; that programme is Deutsch (1999, *Proc. R. Soc. A* 455, 3129) and Wallace (2012, *The Emergent Multiverse*). Attributing it to Everett is a misattribution.
- §2: GRW, CSL and Diósi–Penrose: "Their natural parameter space has been largely removed by X-ray emission bounds and underground tests [Donadi et al. 2021]." Donadi et al. (2021) tests the Diósi–Penrose model only. CSL's parameter space is constrained, not "largely removed," and the cited paper makes no such claim about it. A review of non-interferometric tests (e.g., Carlesso et al. 2022, *Nature Phys.* 18, 243) is the citation the sentence needs, with the sentence weakened accordingly.
- §6: Gisin (1990) — see M8(iii).

**Fix.** Correct the attributions; cite the CSL constraints separately from the DP test.

### M10. Numbers quoted from the record: mostly faithful, with three that should be corrected and the status labels restored

I checked every number in §4.2's table, §4.3, §5.2 and §7 against the record. They agree, with these exceptions.

- §4.2 table: "centre shifts by −(1.1–1.5)K²/ω." STAGE2_RESULTS.md A2: s = 1.10, 1.11, 1.21, 1.51 at Γ = 0.2 and 1.27–1.72 at Γ = 0.5. The range is 1.1–1.7 unless Γ = 0.2 is stated.
- §4.2 table: "convergence only at 256." RESULTS.md F2: N = 64 agrees with N = 256 to 0.005 at t ≤ 3 and not at t = 10. "Only at 256" is true at the longest time only.
- §4.3: commitment "in a semiconductor the interband vertex, 10 fs–1 ps" carries no citation. The ledger's E-16 section gives it as "literature-typical," spanning "two orders," with the verdict "inside that span," and marks one adjacent claim "asserted from model knowledge, not verified against a source." The paper needs a source for the 10 fs–1 ps figure, or the ledger's uncertainty statement.
- §5.2's numbers are quoted without the `diagnostic_only` / `pilot` labels the record attaches to every one of them (see M7).

Everything else I checked matches: 1.3–2.0 across Γ = 0.05–1, t = 3–10; 25–75 % points at 1.2–3 (from the correction paragraph in RESULTS.md); half-width within 2 %; slopes 0.004 and 1.1; onset 0.355; exponents 1.56, 2.16, 1.70, 3.25, 2.09–2.21; the ×400 ensemble exclusion (quoted conservatively as "two orders"); the 10⁻³ exclusivity fraction.

## 5. Minor / presentational

- Reference list: Steck's "Rubidium 87 D Line Data" rev. 2.3.3 is dated 2024; the current revision is 2.3.4 (August 2025). Either the year or the revision number is wrong.
- Reference list: Levstein, Usaj & Pastawski (1998) has its subtitle truncated in the short form ("… nuclear magnetic resonance: A study of the emergence of dynamical irreversibility in many-body quantum systems"); the long form has it in full.
- Landauer (1961) is cited for "Landauer's bound prices the reversal at TΔS, which for a thermalized photon is the photon's own energy." Landauer's bound is kT ln 2 per erased bit; TΔS = E for a thermalized quantum is the first law. The citation is decorative there.
- §2: "Cramer noted that the Dirac and Klein–Gordon equations supply the advanced solutions." Consistent with Cramer (1986) §3.3 ("The Transactional Model and Relativistic Quantum Mechanics") and with Kastner's summary of it; I could not retrieve the section text from the mirror and did not verify the wording.
- Most of the reference list supports uncontested textbook statements (Hahn, Kurnit, Glauber, Hanbury Brown & Twiss, Tonomura, Lan, Foldy–Wouthuysen, Bialynicki-Birula). None of these is load-bearing for any claim the paper makes as its own; the only load-bearing citations are to the repository. That is not a defect in itself, but the paper should not describe itself as resting on the literature it cites.
- The repository is cited as the paper of record ("Every quantitative statement is cited to the repository record") without a DOI, archive, or commit hash in the manuscript. For a journal, the record must be archived (e.g., Zenodo) and the identifier given.
- "Sponsor" appears throughout the front matter; a journal will read it as a funding term. Use "corresponding author" or "accountable author."
- §2, Bohm: "Bohm's foliation is empirically inaccessible by construction; this paper's (§6) is carried openly and carries tests." §7's tests retire only a *cosmic* frame; a local frame remains, in the long form's own words, "unobserved-but-necessary." The advantage claimed over Bohm is conditional and should be stated as such.
- §4.4: the "projective limit" / "ensemble limit" / "repeated limit" / "integrating limit" taxonomy is useful; the emulsion reciprocity-failure argument is nice but Gurney & Mott (1938) is about latent-image formation, and the claim that reciprocity failure evidences a commitment/registration distinction is the paper's inference, not theirs — phrase accordingly.
- Copenhagen/QBism sentence: QBism holds the state is an agent's belief, so "the cut is a … boundary of an agent's knowledge" is fair for QBism; Bohr's position is not that the wave "does not evolve." Tighten.

## 6. Specific questions for the author

1. Do you accept Kastner & Cramer's (2018) derivation of the Born rule for radiative processes as a derivation? If not, which step do you regard as a stipulation, and why is that not cited and argued in §5.3?
2. Kastner & Cramer (2018) explicitly place the Heisenberg cut "at the appropriate microscopic … level of absorption by individual atoms or molecules" with the coupling constant as the variable. State in one paragraph what "the address" adds to that placement.
3. Is there a simulation of the graded-Lorentzian race anywhere in the record? If not, will §5.2's "no threshold and no residual" be labelled as the competing-exponentials identity?
4. What is the content of the width claim beyond the identity 1 − s = κ_ret/ω? Under K ~ Γ, is the table anything other than Q⁻¹?
5. Would a positive sidereal modulation in §7 be a departure from quantum mechanics? If so, how is the abstract's "no prediction differs" to be read?
6. Where is the no-signalling proof that §6 says "follows"? If it is the one §8 lists as owed, will §6 be reworded?
7. What is the race-time-to-physical-time mapping behind "faster than light crosses the detector," and what is its uncertainty?
8. Will the `diagnostic_only` / `pilot` status of every §5.2 number be carried into the paper?
9. Why is Boisvert & Marchildon (2013) cited for the underspecification critique rather than Marchildon (2017) and Kastner's reply?
10. Which exact model version and dates produced the manuscript, and why was the Contributions statement dropped from the short form?
11. Given that Kastner's PTI denies the wave is a spacetime field, in what sense is it a neighbour on your first commitment?

## 7. Rubric scores (1–5)

- **Novelty — 2.** What is precisely new is a re-description: a rate-balance form of a cut location that RTI already places at the absorption vertex with the coupling as its variable; a "width" that is a change of variable and, under the paper's proxy, Q⁻¹; one small genuine result (the dense-record requirement). The novelty claim against TI is inaccurate as stated (M1, M2).
- **Internal consistency — 2.** §2 versus §5.3 on whether TI derives the square; abstract versus §6–§7 on differing predictions; §6 versus §8 on no-signalling; §5.2's attribution versus the record's "not established" (M1, M7, M8).
- **Evidential grounding — 2.** The exact-model results are real but, by the paper's own statement, coincide with decoherence theory; nothing outside the text favours the interpretation over its neighbours; the numbers match the record but arrive stripped of the record's status labels (M7, M10).
- **Reproducibility — 3.** Pre-registered predictions, named scripts, exact calculations, and a record that logs its own wrong predictions are genuine assets; but the repository is not archived with an identifier in the manuscript, the diagnostic labels are dropped, and the AI author's version is unspecified.
- **Citation integrity — 3.** Every reference is real and bibliographically correct (one revision-date slip). Against that: one citation attributed to the wrong paper for the wrong claim (Boisvert & Marchildon), one misattribution (Everett for decision theory), one overstatement of a cited result (Donadi for CSL), one converse not in the source (Gisin), an uncharitable and internally contradicted account of TI's Born-rule claim, and a lineage missing Hoyle–Narlikar, Pegg, Cramer & Mead, and Kastner's later papers (M1, M3, M6, M9).

## 8. Overall assessment (0–5)

**2** — weak but in scope. The paper is honest about what it postulates, its record is unusually transparent, and it belongs at an interpretation venue; but its stated novelty relative to the transactional interpretation is not established and is in one place asserted against the sources it cites, its §5.2 specification is largely an artefact of a model the paper has discarded, and its abstract promises consistency with quantum mechanics that its own frame section withdraws.

## 9. Sign-off

Reviewer: Claude Fable 5.1 (Anthropic), persona R4 transactional-interpretation and scholarship referee, 2026-09-05. Standing note: I am the same model family as the manuscript's first author and reviewed accordingly.
