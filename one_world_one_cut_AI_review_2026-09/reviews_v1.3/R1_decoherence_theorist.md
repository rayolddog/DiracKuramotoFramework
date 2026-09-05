# Review — *One World, One Cut: A Real-Wave Interpretation of Quantum Measurement with a Located Boundary* (short form, v1.3, 2026-09-05)

**Reviewer persona:** R1, decoherence and open-quantum-systems theory (Zeh, Zurek, Joos–Zeh, Schlosshauer; Wigner–Weisskopf, Fano; quantum-jump unravellings, Wiseman–Gambetta; einselection). Third round; this review was written in a fresh context on v1.3 alone.

---

## Standing and limitations

I am a language model — Claude Fable 5.1, made by Anthropic — and I am the **same model family as the manuscript's first author**. I have treated that as a reason to be harder on the paper, not softer: where the first author's prose is fluent and self-assured, I have tried to check whether the assurance is earned, and I have re-run the paper's own smallest model rather than take its numbers on trust.

What I can assess reliably: the internal logic of the paper; whether its formal postulate (§5.1) is the stochastic master equation it says it is; whether its regime statements and displayed formula follow from the two-level-plus-record model the record uses; consistency of the paper against itself and against textbook open-systems theory and photodetection theory; whether cited results are characterized correctly. What I cannot certify: novelty against the complete literature (I know the decoherence and quantum-trajectory literature well, the transactional-interpretation literature only at the level of its main papers, and the relativistic-collapse and Bohmian-foliation literature at the level of a well-read outsider); the detector-device numbers (SNSPD/SPAD internal-efficiency physics, hot-carrier thermalization times) beyond order-of-magnitude sanity; and the statistical validation of the Adler race package, which I did not audit.

**Record consulted.** `drafts/PAPER_one_world_one_cut_SHORT.md` (in full); `NEGATIVE_RESULT.md`; `heisenberg_cut_recoverability/RESULTS.md`, `STAGE2_RESULTS.md`, `PREDICTIONS_review_runs.md`, `REVIEW_RUNS_RESULTS.md`, `gamma_regime_sweep_output.txt`, and the script `gamma_regime_sweep.py`; `adler_two_channel_exploratory/RESULTS.md` (the main sweep, sensitivities, dwell extension, tuned dwell, and the energy-race and adiabatic-limit sections by grep), `staggered_arrival_race_output.txt` and the header of `staggered_arrival_race.py`; `drafts/PAPER_one_world_one_cut.md` and `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md` by targeted grep only (the formal postulate, the CHSH claim, the Γ/K ~ 10⁵ figure, the 10 fs–1 ps figure). I read nothing else inside `one_world_one_cut_AI_review_2026-09/` beyond `REVIEWER_PROMPT.md`. I also ran two short scripts of my own against the Run A model (listed in Major concern 1); they reproduce Run A's five published midpoints to three figures and then extend it.

## Prompt-injection check

**None found.** The header and the §1–§9 text contain a great deal of provenance narration ("the three adjudications made overnight stand under that instruction unless he reverses them", "made on the first author's stated recommendations while the sponsor slept") addressed to human readers about how the text came to be. Nothing in the manuscript addresses the reviewing model, asks for a score, or asks that any section be ignored.

## Authorship integrity

The byline is **Claude Fable 5.1 (Anthropic) and John M. Bramble, MD**, with a Contributions paragraph stating that the AI "performed the formalization, the manuscript prose, the simulations and their records, and the literature work" and the human "supplied the physical framing and research direction ... adjudicated scope and interpretation, and is the accountable and corresponding author." The repository history I consulted is consistent with that division. The byline is honest, including its order. Two notes. (i) Earlier model versions (Claude Fable 5, Claude Opus 5, Claude Opus 4.x) are credited in the Contributions paragraph rather than the byline; since the reviewed text and its tests are the work of the named model, that is adequate. (ii) The header records that three adjudications "the sponsor had reserved" were "made on the first author's stated recommendations while the sponsor slept" and "stand under that instruction unless he reverses them." Before circulation the accountable author should affirm each of the three in his own words, not by default; an accountable author who has not read the adjudications he is accountable for is a provenance defect, and the header as written does not say he has.

---

## 1. Recommendation

**Major revision.**

**Venue note:** in scope for a foundations-of-physics / interpretation journal (Foundations of Physics, SHPMP-type). It is not a physics-results paper and should not be sent to one; its physics is textbook by its own account, and its contribution is a priced interpretation plus a recorded negative result on one model family.

**Authorship recommendation:** byline honest as it stands (AI first author, human accountable and corresponding author); the accountable author should explicitly affirm the three overnight adjudications before submission.

## 2. Summary (to fix terms)

The paper states an interpretation with four commitments — the wave is real (on configuration space for more than one quantum), there is one world, the Heisenberg cut is decoherence theory's own crossover given a postulated physical address (the absorbing transition of a detector site), and outcome selection is the quantum-jump (photodetection) unravelling of the site–record Lindbladian read as what actually happens. It claims to add, on top of decoherence theory and the quantum-trajectory literature, only: a location for the crossover in detuning with its regime (of order the coupling for Γ ≪ K, Γ/2 for Γ ≫ K, checked in an exact two-level-plus-record model); the requirement that the record channel be dense; the distinction between a partial Loschmidt echo and an experimenter's coupling flip; and a negative result — that a synchronization/hazard programme on a real-wave substrate cannot move the outcome weights away from the Born branch weights, and is pushed to the projection postulate. It pays, on its own price list, a real state on configuration space, a nonlocal projection, and a chosen foliation. No new constant, no prediction differing from quantum mechanics.

## 3. Strengths

- **The candour is real and worth preserving.** Three revisions have removed the paper's distinctive physics claims one by one, and each withdrawal is marked in place with the run that forced it. The pre-registered predictions (`PREDICTIONS_review_runs.md`) with scored outcomes, including wrong ones, are a model of how a small-model paper should be run.
- **The formal core of §5.1 is now the right object.** The stochastic master equation with absorbing jump operators c_i = √Γ_i |g_i,r_i⟩⟨e_i|, the non-Hermitian no-jump Hamiltonian, the jump ψ → c_iψ/‖c_iψ‖ at rate ⟨c_i†c_i⟩, the Lindblad ensemble average and the no-signalling argument from site-local generators plus a linear ensemble map are all correct as written. The remark that a *projector* as jump operator "would give a nondemolition which-site monitor instead of a detector" is exactly right and is the kind of thing that was wrong in v1.0.
- **Run B is a genuinely useful negative result**, correctly diagnosed in the paper as Mandel's semiclassical formula rediscovered: a local hazard linear in absorbed energy gives an exponential-in-intensity click law and sends the click to the first-reached detector. That is the semiclassical detection theory's known failure on single-photon states, and the paper found it by simulation rather than by citation — see Major concern 6 for what it should be cited against.
- **The foliation section is now correct** on the point that mattered: site-local jump superoperators commute at spacelike separation, so no ordering is needed for statistics; the slicing decides only which conditional state is "the" state between jumps, an unobservable choice, exactly as in Bohm.
- **Reproducibility.** I reproduced Run A's five midpoints (1.538, 1.284, 5.088, 50.009, 499.987) from the committed script to three figures before extending it.

## 4. Major concerns

### 1. The paper's one displayed equation is an interpolation whose constant cannot be derived from either convention the paper names, and it fails qualitatively in the intermediate regime — in the paper's own model and own convention.

§4.2 displays

> Δ_{1/2} = √(Γ²/4 + 2K²)

"in the rate-based convention, checked at Γ/K = 0.2, 1, 10, 100, 1000 (Run A: midpoints 1.54, 1.28, 5.09, 50.0, 500.0 against the formula's 1.42, 1.50, 5.20, 50.0, 500.0)". Two problems.

(a) *The small-Γ constant.* In the rate-based convention the paper itself says the midpoint drifts "from 1.54K toward 2K/√3 at long observation times". I confirm that: the long-time rate is the slowest eigenmode's decay rate, whose normalized half-point is where the slow dressed state's excited-state content is ¼, i.e. Δ = 2K/√3 = 1.155K. In the occupation convention the half-point is 2K. The displayed constant 2K² gives √2 K = 1.414K, which is *neither* (it would be 4K²/3 for the long-time rate convention, 4K² for the occupation convention). It matches the Run A number 1.54 at Γ/K = 0.2 only because that number was taken at capture time t = 3, mid-transient. The abstract's "half-width √(Γ²/4 + 2K²) in the rate-based convention" is therefore wrong as a limit statement.

(b) *The intermediate regime.* I ran Run A's own propagator (`gamma_regime_sweep.py`, unchanged) at additional Γ/K and observation times, and separately computed the t → ∞ rate midpoint from the slow eigenvalue of H_eff = [[0, K],[K, Δ − iΓ/2]]. Results (Δ/K):

| Γ/K | t = 1 | t = 3 (Run A) | t = 10 | t = 100 | t → ∞ (slow mode) | formula | Γ/2K |
|---|---|---|---|---|---|---|---|
| 0.2 | 3.69 | 1.54 | 1.70 | 1.23 | 1.15 | 1.42 | 0.10 |
| 1 | 3.68 | 1.28 | 1.32 | 1.14 | 1.13 | 1.50 | 0.50 |
| 2 | 3.76 | 1.01 | 1.04 | 1.05 | 1.04 | 1.73 | 1.00 |
| 3 | 3.92 | 1.16 | 0.93 | 0.88 | 0.88 | 2.06 | 1.50 |
| 4 | — | — | — | — | **0.58** | 2.45 | 2.00 |
| 5 | 4.41 | 2.35 | 1.90 | 1.78 | 1.76 | 2.87 | 2.50 |
| 10 | 6.31 | 5.09 | 4.80 | 4.70 | 4.68 | 5.20 | 5.00 |

In the paper's rate-based convention the crossover midpoint is **non-monotone in Γ/K**: it falls from ≈1.15K at small Γ to ≈0.6K at Γ = 4K — the exceptional point of the 2×2 non-Hermitian model, where the resonant dynamics goes from underdamped to overdamped and the slow-mode rate becomes non-analytic in Δ — and only then rises as Γ/2. The formula is monotone and never below √2 K; at Γ/K = 4 it is high by a factor of four, at Γ/K = 3 by 2.3. The paper's sentence "in the untested Γ/K = 1.5–7 region a re-run by a reviewer found the rate-based midpoint to move by a factor of four with the observation time" is true (Γ/K = 3: 3.9 at t = 1 versus 0.88 at t = 100) but understates the finding: the *long-time* value is itself a factor of four below the formula, and the dip is a spectral feature of the model, not a detector property.

Even at the "checked" points the check is convention-fragile: at Γ/K = 1 the formula is 17 % high at t = 3 and 33 % high at t → ∞; at Γ/K = 0.2 it is 8 % low at t = 3 and 23 % high at t → ∞.

*Fix.* Delete the equation. State the two limits as the results they are — the Rabi-width regime (2K in occupation, 2K/√3 in long-time rate, convention-dependent by √3) and the Markov/adiabatic-elimination regime (HWHM Γ/2 of the broadened line) — and say plainly that between them the "location" is not a robust observable in any convention: it depends on observation time by a factor of four and on the convention by a factor of two, and passes through a spectral exceptional point at Γ = 4K. If the authors want a formula, the one that *is* derivable is the long-time rate half-point from the slow eigenvalue, which they can display with its non-monotone plot. Also strike "to 15 % from Γ/K = 0.2 to 1000" from the §4.2 table, which is true only at the five sampled points and at capture time t = 3.

### 2. The "factor √3" sentence is arithmetically wrong as written, in the abstract and in §4.2.

§4.2: "For Γ ≪ K the half-width is of order the coupling — √2 K in the rate convention, 2K for the half-point of the occupation 2K²/(Δ² + 4K²), a factor √3 apart because the two conventions weight the Rabi line differently, with the rate-based midpoint drifting from 1.54K toward 2K/√3 at long observation times". √2 K and 2K are a factor √2 apart. The √3 is between 2K (occupation) and 2K/√3 (long-time rate). The abstract repeats the slip: "(√2 K; the occupation half-point is 2K, and the midpoint is convention-dependent by a factor √3 ...)". Three numbers are in play — 1.414 (an interpolation constant), 1.155 (long-time rate), 2 (occupation) — and the sentence pairs the wrong two. The header's own change note ("√2 K in the rate convention, 2K for the occupation half-point, convention-dependent by √3") carries the same error into the record, so it is not a typo but a mis-reading of which convention gives what. Fix together with concern 1.

### 3. In the Γ ≫ K regime "set by the record channel and hence by temperature" is physically backwards, and "Γ/K of order 10⁵" has no derivation anywhere in the record.

The abstract: "Γ/2, set by the record channel and hence by temperature, where it does not — the regime of every room-temperature semiconductor detector". §4.2: "the record channel's rate, which is the temperature-dependent quantity".

In the Γ ≫ K regime as the paper describes it (silicon, a nanowire), the record channel is hot-carrier thermalization — optical-phonon emission on the 10 fs–1 ps scale the paper quotes. That rate is dominated by *spontaneous* emission, ∝ (n_q + 1) with n_q ≈ 0.1 for a 60 meV phonon at 300 K; it is weakly temperature-dependent. The strongly temperature-dependent record rate is the *other* regime's: the T₂ of a rare-earth or cavity-QED absorber (the paper's own Böttger et al. citation in §7 is about exactly that, Γ(T)·t collapse). So the paper has the temperature sensitivities of its two regimes reversed. Decoherence theory's temperature dependence (Joos–Zeh, Caldeira–Leggett) enters through the environment's *state*, and the paper cannot borrow it for a spontaneous-emission channel by saying "hence".

"Γ/K of order 10⁵" appears only in `PREDICTIONS_review_runs.md` and `REVIEW_RUNS_RESULTS.md` as an assertion, with no estimate. For a band absorber the paper itself concedes that "neither Δ nor a 'site' is given by the Hamiltonian", so K for a "site" is not even defined; the ratio is a placeholder. *Fix.* Replace "hence by temperature" with "set by the site's coupling to its record channel, with whatever temperature dependence that rate has (weak for phonon emission in a semiconductor, strong for T₂ in a rare-earth crystal)". Replace "Γ/K of order 10⁵" with "Γ ≫ K on any estimate" or supply an estimate with its assumptions (mode volume, dipole matrix element) and its admitted ill-definedness.

### 4. Three different things are called "the cut", and the one that the postulate actually lives on — the site–record split — has an FAPP-defined domain that is not on the paper's price list.

The title has one cut. The text has three: (i) the crossover *in detuning* of §4.2, which is the half-maximum of the site's echo-leak Lorentzian — i.e. the half-width of the absorption line (Rabi-broadened or Γ-broadened); (ii) the *event* of §5, a jump at a site at a time; (iii) the *split in the von Neumann chain* on which the jump operators of §5.1 are defined — the site | dense-record boundary, which the paper says "the dense-record criterion of §4.3 defines, and that criterion is graded".

(i) is not a cut in the chain at all; jumps occur at every detuning, more slowly off-resonance, and nothing "sets in" (abstract) at Γ/2. It is the linewidth, and calling it "the location of the Heisenberg cut" adds no content — the paper concedes as much three times ("dissolves no puzzle on its own"; "in both regimes the placement is decoherence theory's own"; "the address is then by postulate only"). (iii) is the real cut: it is where c_i is defined, and it is defined by "the record channel must be dense on the capture timescale". How dense? The record's own numbers (`RESULTS.md` F2) say 1 mode gives coherent exchange, 4 modes leak nothing, 16 modes recur at t ≥ 3, 64 agree with 256 to 0.005 for t ≤ 3 and not at t = 10. So whether a jump "happens" at a site with a 16-mode record channel, in the paper's ontology, depends on an observation time. The paper says this ("the ontic reading inherits a for-all-practical-purposes element at the split, which is the residue of §4.5 and is not removed") — but then §9's price list is "a real state on configuration space, a nonlocal projection, and a foliation chosen rather than forced". The largest price is missing: **an ontic law whose domain of application is defined for all practical purposes.** That is Bell's "shifty split" imported into the beable dynamics, and it is what separates this proposal from GRW/CSL, whose hitting law has a sharp domain (everything, always). A postulate that says "nature performs a quantum jump wherever the Markov approximation is good enough" is not yet a law.

*Fix.* Name the three objects separately (crossover, event, split). Put the FAPP-defined domain on the price list in the abstract, §5.1 and §9. State a quantitative "dense" criterion (recurrence time 2πN/B against capture time, from the record's own numbers) and say explicitly that the paper does not know what happens at a site whose record channel is marginal.

### 5. The formal postulate of §5.1 is correct but its surrounding sentences mis-describe it in four places.

(a) *What is traced.* c_i = √Γ_i |g_i, r_i⟩⟨e_i| — "the absorbing transition at site i into its record". If |r_i⟩ is a state in the ket, the record is *in* the state, and the site–record dynamics is then the unitary Weisskopf–Wigner problem of the record's own §4.2 table; there is no jump until *something* is traced. If Γ_i is a golden-rule rate, the dense channel *has* been traced, and r_i can only be a register left behind (a bookkeeping label, or a record qubit flipped by the traced bath). Both readings are legitimate; the paper must say which, because its entire distinction between "record channel" (Γ) and "registration" (amplifier) hangs on it.

(b) *"Clause 1 is the golden rule's matrix element squared."* No: clause 1 is the Born weight of the site branch (|local amplitude|², i.e. P_e(i) in the conditional state). The golden rule's matrix element squared is Γ_i, the prefactor in clause 2's rate ⟨c_i†c_i⟩ = Γ_i P_e(i). Mislabelled.

(c) *How many things are postulated.* §5.1 opens "Three things then happen, and the paper postulates all three"; clause 3 ends "so the paper postulates two things and inherits the third from the field algebra"; the formal paragraph ends "The paper derives none of them". In the SME the jump ψ → c_iψ/‖c_iψ‖ *is* the projection with Born weights, and for a one-photon state it annihilates every other amplitude, so exclusivity is kinematic — the paper is right about that; but then clause 3 is not a separate postulate and the three-clause "sink" language postulates one thing (the SME with the jump unravelling read ontically) three times. Say so once, consistently.

(d) *The Wiseman–Gambetta cost is placed at the wrong level.* The paper concedes "which one is 'what happens' is not fixed by the master equation [Wiseman & Gambetta 2012]" and says it "selects the jump unravelling on the site–record split". Two comments. First, the paper can answer the obvious objection — homodyne detection of resonance fluorescence yields a diffusive conditional state for the atom — *without* cost, and should: on its own ontology the ontic jumps are absorptions at the photodiodes' sites after the local oscillator has been mixed in, and the diffusive unravelling of the *atom* is the strong-LO limit of jumps at those absorbers. The paper's ontology agrees with Wiseman–Gambetta that atomic jumps are not objective; the objective events are absorptions. Second, the concession that *does* bite is the one the paper under-states: the site's own record channel (phonons) is never measured by anyone, so the choice of the counting unravelling over a diffusive unravelling of the site–record Lindbladian has no operational anchor whatever. It is pure stipulation, and the paper should say that in those words rather than "not fixed by the master equation".

(e) Minor but formal: "[Gisin 1989; Polchinski 1991]" for "the conditions under which a stochastic reduction does not signal". Gisin 1989 is the right citation. Polchinski 1991 concerns Weinberg's *deterministic* nonlinear quantum mechanics and shows that the version avoiding EPR signalling still permits an "Everett phone"; it is tangential to stochastic reductions with a linear ensemble map.

### 6. §5.2's "true altitude" invokes the wrong theorem for the runs, omits the prior literature that actually contains Run B, and keeps a bold general claim the runs do not establish.

The paper: "its general form is not the paper's — any probability assignment on the projectors of a Hilbert space of dimension three or more is the Born rule [Gleason 1957; Busch 2003] ... The runs are those theorems met in a model".

Gleason's theorem constrains *noncontextual* probability measures (frame functions additive over orthogonal projectors); Busch's extension constrains POVM-valued ones. A race among Adler clocks with random initial phases is a dynamical model with extra variables; it is not a frame function on projectors, and Gleason places no constraint on it — which is why it could, and did, produce an exponent of 1.5. So the Adler runs are not "Gleason met in a model"; they are a hidden-variable-like model failing to reproduce the Born rule, which Gleason permits. The result that *is* met in the model is elementary: a Poisson race with rates ∝ |a_i|² gives P_i ∝ |a_i|² (the "competing-exponentials identity"), and a Poisson race with rates that are not ∝ |a_i|² does not. Pearle 1976 / Gisin 1984 (martingale) and Gisin 1989 (no-signalling forces linearity) apply once one is *inside* the class of stochastic reductions of ρ with a linear ensemble average — which the Adler substrate is not; they are the right citations for why the *SME* has Born weights, not for why the race failed.

What Run B actually rediscovered has a literature the paper does not cite: the distinction between semiclassical and quantum photodetection on single-photon states — Clauser's 1974 test of semiclassical radiation theory, Kimble–Dagenais–Mandel 1977 antibunching, and Grangier–Roger–Aspect 1986 anticorrelation (cited in §3.3 for a different point). A real classical wave with local stochastic detectors gives Mandel's exponential law and no exclusivity; the paper's "one-quantum stop must act within about a thousandth of the commitment time" (`NEGATIVE_RESULT.md`) is the anticorrelation experiment's content restated. The honest altitude of §5.2 is: "a real-wave substrate with local detector-side hazards is semiclassical detection theory, excluded on single-photon states since 1974–1986; the only stochastic process with these ingredients that reproduces quantum mechanics is the SME, whose weights are then fixed by the martingale/no-signalling arguments."

Finally, the bold sentence — "nothing in the physics of a detector and no synchronization substrate can move the outcome weights" — is established by the runs for a handful of models (first-to-align, fixed dwell, inverse dwell, tuned dwell, energy-linear memoryless hazard, staggered exposure) at diagnostic budget, and in general only by the cited theorems within the SME class. Remove the bold, keep the family-scoped statement, and credit the general form entirely to the literature as the following sentence already half does.

### 7. §6's "picture in the accountable author's words" is consistent with §5.1 and with no-signalling, with one word that conflates two different pulls and one loose end against §8.

"the sink's opening at one wing pulls it — *reduces* the amplitudes of the branches the outcome has excluded — everywhere it has support". In the SME there are two pulls, and §5.1 distinguishes them correctly: the *null* pull (no-jump renormalization, which continuously reduces the silent site's amplitude and, after normalization, raises the others) and the *click* pull (the jump c_iψ, which for a one-photon state or a polarization singlet sets the excluded branches to exactly zero — "a branch selected"). "Reduces" is right for silence and wrong for a click; the sentence is about a click. Say "removes" for the click and "reduces" for the null, and add that the null pull is also nonlocal, also foliation-dependent in its "when", and also averages out at the partner's wing — the reader who worries about signalling from silences deserves the sentence.

Otherwise the picture is the Lüders update plus the no-jump renormalization, the statistics are order-independent because the wings' jump superoperators commute, and the partner's reduced state is unchanged by Alice's outcome or non-outcome: consistent with §5.1 and non-signalling. One loose end: §6 says "there is no bound to clear", §8 item 2 says "the clearance of the Lorentz bounds if it cannot [be made covariant]". If the foliation is unobservable as §6 argues, there are no bounds to clear even then; reconcile.

### 8. "Commitment is the vertex, not the record" (§4.3) is contradicted by the paper's own jump operator, and "record" means two things.

In §5.1 the jump operator acts on the site → record transition (rate Γ); the field → site coupling K is in H and is unitary. So in the paper's own formalism the event is at the *record-writing* transition in every regime; only for Γ ≫ K does adiabatic elimination merge the two into an effective jump ∝ √(K²Γ/(Δ² + Γ²/4)) acting directly on the field. For Γ ≪ K — the paper's rare-earth and cavity-QED regime — the "absorption vertex" (K) is the recoverable capture stage and the event is the leak into the dense channel. §4.3's "Commitment is the vertex, not the record" is then false in the Γ ≪ K regime unless "record" there means the *registration* (amplifier), which is how the paragraph continues ("the record is written later"). So "record" is being used for (i) the dense channel Γ that the jump feeds (§4.2, §4.3 "record channel", §5.1 "into its record") and (ii) the amplified registration (§4.3 "not the record"). Disambiguate — "record channel" for Γ, "registration" for the amplifier — and then say which link the event is at: the transition into the record channel. Also say in §4.3/§4.4 that for the exemplar detectors (SPAD, SNSPD, at Γ ≫ K) the "capture" row of the table is empty by §4.2's own statement; the three-stage taxonomy as tabulated describes the other regime.

### 9. Also note (specialism-adjacent): §7 states "a detuning crossover of half-width 2K in the echo-recoverable fraction" for the coupling-set regime, which is none of §4.2's three numbers for that observable (the fixed-time echo-recoverable *fraction* drifts 1.7 → 5 with Γt; 2K is the occupation half-point; 2K/√3 the long-time rate). Make §7 agree with whatever §4.2 becomes after concern 1.

## 5. Minor / presentational

- **Orphan references:** Kjaergaard et al. 2020 (the transmon row was withdrawn; nothing in the text cites it) and Norsen 2010 (never cited; if it was meant for §3.1's local-beables paragraph, cite it there — it is the right reference for "what a click is in three-space").
- **Run B percentage.** "a channel at half intensity clicks 36 % more often than a linear law allows": from `staggered_arrival_race_output.txt`, P(B clicks) = 0.584 at 45° against 0.834 at full amplitude; the linear law gives 0.417, an excess of 40 %. The record's "0.43" is not derivable from its own table.
- **"the photon amplitude decays directly at rate K²Γ/(Δ² + Γ²/4)"** — that is the population (probability) rate; the amplitude decays at half of it.
- **"10 fs–1 ps (literature-typical, spanning two orders)"** — uncited. Give a source for hot-carrier thermalization in silicon.
- **The Q-factor table** (10⁻⁸ alkali, 10⁻¹⁸ clock, 10⁻⁶–10⁻⁵ quantum dot) is Γ/ω = 1/Q and the paper says it "dissolves no puzzle on its own". In a short form it is decoration; cut it, or keep one sentence.
- **"the crossover in detuning at which irreversible capture sets in"** (abstract): nothing sets in; the jump rate is a smooth Lorentzian in Δ. Say "the detuning half-width of the irreversible-capture rate".
- **§5.1 clause 1**, "weighted in its detuning by the crossover of §4.2": in the SME there is no separate weight; the detuning dependence is the conditional occupation P_e(i). Reword so it does not read as an extra factor.
- **"CHSH ≤ √2 in the record"** (§6): the record is `tests/bell_phase.py` / Appendix A of `current_revision_DK_paper.md` (a Malus-law toy). Cite the file or drop "in the record".
- **"Schrödinger's second objection"** (§3.1): give a reference (the 1926 Lorentz correspondence or a secondary source).
- **Minev et al. 2019** in the capture row: what it demonstrates is the no-jump conditional evolution of the SME caught mid-flight, which supports §5.1's formalism more than §4.3's "capture" row; fine as "suggestive", but say which.
- **The header** is 600 words of revision history addressed to the review panel; in a submitted version it belongs in a change log or the review folder.
- **The abstract** is 420 words and contains the paper's arithmetic; it should contain the claims and their status only.

## 6. Specific questions for the author

1. Which link of the chain is the event: the field → site coupling K ("the vertex") or the site → record transition Γ (the jump operator of §5.1)? The two sections answer differently for Γ ≪ K.
2. What is the quantitative criterion for "dense", and what does the interpretation say happens at a site whose record channel has, say, 16 modes and a recurrence time of order the capture time? Is a jump a fact there?
3. Where does Γ/K ~ 10⁵ come from, given §4.2's concession that a band absorber has no site and no Δ?
4. Is the thermalization rate of a photo-excited carrier in silicon at 300 K in fact temperature-set in any sense strong enough to support "hence by temperature"?
5. In homodyne detection of resonance fluorescence, what are the ontic jumps on this interpretation — the atom's σ₋ jumps, or absorptions at the photodiodes after mixing with the local oscillator? If the latter (as I think the ontology requires), why concede unravelling non-uniqueness at the apparatus level at all, and why not state the stipulation where it actually is — at the never-measured phonon channel?
6. Would the authors accept replacing the displayed formula with the two limits and a plot of the slow-mode half-point, including its dip at Γ = 4K?
7. After concern 4: if the detuning crossover is the absorption line's half-width and the actual cut is the FAPP-graded site–record split, what remains of "a located boundary" in the title beyond "a postulated address"?

## 7. Rubric scores (1–5)

- **Novelty — 2.** The paper's own accounting is accurate: the crossover, its two limits, the dense-record requirement and the echo/flip distinction are textbook; the SME is the literature's; the novelty is a candid price list, a "pull" gloss on the no-jump renormalization, and a negative result on one niche model family that the semiclassical-detection literature already contains in general form.
- **Internal consistency — 3.** Much improved and now mostly right in the formal core, but the paper still contradicts itself on the √3, on how many things are postulated, on "vertex versus record", on §7's 2K against §4.2, and on §6 against §8; and three objects share the name "cut".
- **Evidential grounding — 2.** Exact toy models, correctly run and pre-registered, tie the paper to nothing outside textbook open-systems theory; the two regime numbers that reach toward real detectors (Γ/K ~ 10⁵, "temperature-set") are unsupported or backwards; the displayed formula fails in its own model in the regime between the limits.
- **Reproducibility — 4.** Scripts, raw outputs, pre-registered predictions and scored results are all in the repository; I reproduced Run A exactly. One point off because the "0.43 / 36 %" of Run B is not derivable from its table and because the 10⁵ and the CHSH claims have no pointer.
- **Citation integrity — 3.** The references are real and the decoherence, quantum-trajectory and photodetection sources are characterized correctly and are load-bearing. Against that: Gleason is invoked for a class of models it does not constrain; Polchinski is tangential; two references are orphaned; the semiclassical-detection experiments that contain Run B's result are not cited; two numerical claims are uncited.

## 8. Overall assessment (0–5)

**2 — weak but in scope.** A candid, well-documented interpretation paper whose physics is entirely textbook by its own account, whose one displayed equation fails in its own model between the two limits, and whose most serious foundational cost — an ontic jump law with a for-all-practical-purposes domain — is conceded in §5.1 but left off the price list. Fixable, and worth fixing, at a foundations venue.

## 9. Sign-off

Reviewer: Claude Fable 5.1 (Anthropic), persona R1 decoherence theorist, third round on v1.3, 2026-09-05

---

### Appendix — the two checks behind Major concern 1 (so the authors can reproduce them)

Both use K = 1 and the unchanged `R_echo` of `heisenberg_cut_recoverability/gamma_regime_sweep.py` (forward propagation under H_f = [[0, K],[K, Δ − iΓ/2]] for t, then under H_e = [[0, −K],[−K, −Δ − iΓ/2]] for t; return probability of the photon; rate = −ln R/(2t); midpoint = detuning at which rate/rate(Δ=0) = ½ on a log grid of 241 points from Δ/K = 10^−1.5 to 10^3.5).

1. Same propagator, Γ/K ∈ {0.2, 1, 1.5, 2, 3, 5, 7, 10}, t ∈ {1, 3, 10, 30, 100}: table in concern 1 (Run A's five rows are recovered at their stated t).
2. t → ∞ limit: for each Δ, the slow rate is min over eigenvalues λ of H_f of (−Im λ) (the echo leg has the same decay spectrum, since H_e = −H_f*); midpoint = Δ at which slow_rate(Δ)/slow_rate(0) = ½. Results, Δ/K: 1.151 (Γ/K = 0.05), 1.151 (0.2), 1.147 (0.5), 1.126 (1), 1.091 (1.5), 1.040 (2), 0.877 (3), 0.577 (4), 1.759 (5), 3.023 (7), 4.680 (10), 14.86 (30), 49.82 (100). Against the paper's √(Γ²/4 + 2K²): 1.414, 1.418, 1.436, 1.500, 1.601, 1.732, 2.062, 2.449, 2.872, 3.775, 5.196, 15.07, 50.02.
