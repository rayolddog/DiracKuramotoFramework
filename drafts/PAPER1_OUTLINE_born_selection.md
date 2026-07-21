# Paper 1 Outline — Outcome Selection: The Born Rule as a Derived Fair Game

*Drafted 2026-07-20 from the day's thread. Sources: WALKTHROUGH_born_outcome_selection.md (narrative skeleton), NOTE_born_gamblers_ruin.md, DERIVATION_slaved_phase_subthreshold.md, DERIVATION_vacuum_noise_correlation.md, DERIVATION_bell_pair_joint_game.md, DERIVATION_inverted_gisin.md, DERIVATION_multiquantum_rho_linearity.md, DERIVATION_stage2_signaling.md, PRIOR_WORK_born_selection.md (citations + referee traps).*

**Byline: DECISION PENDING (JB to decide explicitly — session was genuinely joint).**
**Venue candidates (JB to decide): Foundations of Physics (fit; note FoP declined DK main paper — different paper, cleaner claim), Quantum (open access, technical), Phys. Rev. A (if framed as detector-physics + quantum optics), Entropy (fallback).**
**Length target: 20–25 pp + appendices. Position in trilogy: Paper 1 of 3 (→ Heisenberg Cut paper → DK framework revision).**

---

## Title candidates
1. "The Born Rule as a Derived Fair Game: Outcome Selection from Detector Dynamics" *(leading candidate)*
2. "Outcome Selection in Quantum Measurement: Born Statistics from a Martingale That Physics Forces"
3. "Why One Electron Wins: Measurement Probabilities from Energy Competition in Detectors"

## Abstract skeleton (5 sentences)
(1) Born rule = only entry point of probability in QM; derivation programs to date give the *measure* (Gleason, envariance, typicality) or postulate the noise that gives outcomes (Pearle/CSL). (2) We present a dynamical mechanism in the detector: a photon tips all absorber electrons (energy ∝ A², oscillator energetics), which then compete for the quantum in a stochastic exchange; a classical martingale theorem (Pearle's gambler's ruin) makes win probabilities = energy shares = Born — *if* the game is fair. (3) Main results: the fairness is *derived*, not postulated — amplitude-linear coupling ⇒ drift-free shares (Itô); no autonomous phase below the lock threshold (slaved-phase theorem) ⇒ no rich-get-richer; noise locality ⇒ site independence; energy-conservation vertex counting ⇒ commit rates linear in occupation, all sectors ⇒ statistics affine in ρ. (4) The mechanism reproduces exact Born at any registration speed, Glauber joint counting including bunching/anti-bunching, and CHSH = 2√2 with a resync-fidelity law S = 2√2·η; no-signaling emerges as a theorem rather than an axiom. (5) Unlike an axiom, the mechanism predicts its own failure conditions — concentrated in one experimental family (mismatched-collective two-port detectors), with a tabletop discriminator.

---

## §1 Introduction (~3 pp)
- The two strangenesses: why probability at all; why the square. Born as the un-derived axiom.
- Landscape in two rows (→ comparison table, §9): *measure derivations* (Gleason 1957; Deutsch 1999/Wallace, + Barnum et al. critique; Zurek envariance 2003/05; DGZ 1992 typicality; Valentini relaxation; Masanes–Galley–Müller 2019 + 2025 controversy) vs *dynamical models* (Pearle 1976/1982; GRW/CSL; Diósi; Gisin; Hughston; Brody–Hughston; Adler trace dynamics; ABBH 2001 martingale models; Allahverdyan–Balian–Nieuwenhuizen 2013).
- **Credit paragraph up front (referee trap #1):** the martingale ⇒ Born engine is Pearle/ABBH; excitation ∝ |E|² is Lamb–Scully/Mandel–Wolf; our contribution is exclusively the *physical realization* and the *derivation of fairness* — the piece every dynamical predecessor postulated (and, per Gisin's theorems, had to).
- Claim statement, bounded: **given the framework's ontology (stated as four premises in §2), the measurement postulate is redundant** — outcomes, definiteness, Born weights, quantum optics counting statistics, and Bell correlations follow from dynamics + noise. Explicitly NOT claimed: derivation of QM, of probability-from-nothing, or of entanglement.
- Reader contract: paper written conditionally — premises are physical statements about detectors; a reader need not adopt the full DK framework to evaluate the theorems.

## §2 Premises and setup (~2 pp)
Four premises, numbered and referenced throughout (this list IS the paper's spine):
- **P1 (energetics):** detector excitation = energy accumulation in driven bound oscillators; tip energy e_i ∝ A_i². [Stage 1; Lamb–Scully credit; MRI/NMR small-tip parallel]
- **P2 (coupling):** all couplings, including vacuum noise, are amplitude-linear. [The framework's standing postulate — does four jobs: Born form, fairness, commit linearity, no-signaling]
- **P3 (detector state):** absorber clocks initially mutually incoherent; dominant detector noise is local (correlated radiative fraction f ~ 10⁻⁶ in solids). [Checkable detector physics]
- **P4 (registration):** discrete-level absorbers commit at full assembly (threshold); continuum absorbers commit as a rate process. [Detector taxonomy; both cases resolved by theorems]
- Three-stage structure (capture/selection/registration) as organizing frame — forward pointer to Paper 2 (Heisenberg Cut).

## §3 Stage 1 — capture: where the squaring enters (~1.5 pp)
- Coherent tipping of all sites; keep-the-plural-alive discipline (the Feynman-vertex trap: reducing the sum to one diagram already uses Born).
- e ∝ A² from oscillator energetics; phase-independence of the secular tip; NMR sin²(θ/2) parallel.
- What Lamb–Scully have and lack (exclusivity) — sets up Stage 2. [Sources: walkthrough §3; NOTE §1 steps 1–3]

## §4 Stage 2 — the game and the engine theorem (~2 pp)
- Exchange dynamics, absorbing barriers (lock threshold / relaxation), vacuum seed (tie-breaker, not hidden variable — Bell guardrail flagged early).
- **Theorem (Pearle/ABBH, restated):** fair game + absorption ⇒ P(i) = e_i/E exactly, any N. Casino statement for accessibility.
- Motivating failures (why fairness is a knife-edge): one-shot max-overlap fails (bright-among-nine 79% vs 50%); biased exchange fails. [Figure: failed vs fair game sims]

## §5 The fairness theorems — the paper's core novelty (~5 pp)
Four objections, four theorems (walkthrough §5 structure):
- **5.1 Noise scaling (P2 ⇒ fair dice):** Itô drift of shares ≡ 0 for variance ∝ e; knife-edge table (additive ⇒ rich-get-richer, multiplicative ⇒ equalizing, √e ⇒ fair) with sims. [DERIVATION_slaved §3–4]
- **5.2 No autonomous phase below threshold (P1+P4 ⇒ no rich-get-richer):** driven damped mode is linear, eigenvalues −γ±iΔ, γ = ΔE/ℏ; phase slaved, Adler entrainment tail structurally absent; free clock only in layer w = K/ω; level discreteness enforces sharpness; feedback hierarchy (uptake √e concave, decay e neutral, autonomous gain amplifying and layer-confined). Deviation vs layer-width sims (tailed vs gapped). [DERIVATION_slaved §1–2, §4]
- **5.3 Noise independence (P3):** general correlated-noise drift formula (linear in C); fine-fringe danger at f=1 (+20% at λ/2 — sinc-zero protection overturned, reported honestly); locality protection dev ∝ f ~ 10⁻⁶; polarization-dependent vector-vacuum kernels. [DERIVATION_vacuum_noise]
- **5.4 Commitment (P4):** rate-linearity theorem (linear pick + martingale + optional stopping ⇒ exact Born at any speed); kinematic vertex counting — k-quantum commit has exactly k vertices ⇒ rate linear in G^(k), corrections O(w²); sector-by-sector. [DERIVATION_slaved §9; DERIVATION_inverted_gisin §1; DERIVATION_multiquantum §2]

## §6 Reproducing quantum statistics (~3 pp)
- Single-photon Born exact; timescale ladder for a real detector (Si SPAD: fs → ps → ns, closes with orders of margin; both pulse orderings benign; time-resolved Born). [DERIVATION_slaved §7]
- Multi-quantum: registry formulation; sequential commits ⇒ Glauber joint counting P(i,j) = |ψ(i,j)|²; bunching/anti-bunching sims (identical marginals, opposite correlations — intensity-only models fail); two-photon absorbers as linear POVMs; ρ-affinity and decomposition-independence. [DERIVATION_multiquantum; figure: bunching table]

## §7 Entangled pairs and no-signaling (~3 pp)
- Two-stage joint game: local games do marginals; first lock (preferred foliation) resyncs the shared registry; conditional game; joint = marginal × conditional = Born; order-independence = no-signaling; CHSH sim S = 2.82. [DERIVATION_bell]
- **Fidelity law S = 2√2·η** (the publishable quantitative handle — referee trap #4 honored: the 2√2 itself is consistency, not novelty); experiments ⇒ η ≳ 0.99.
- Resync mechanism: shared-frame rotation at the source (JB's central-point picture); phase-velocity-like, no propagation ⇒ prediction: spooky-action-speed experiments find only growing lower bounds (Salart 5.4×10⁴c; Yin 1.38×10⁴c — corrected number), never a floor; before-before dissolved. [DERIVATION_bell §6b]
- **Inverted Gisin:** no-signaling emergent — forward (kinematic linearity §5.4 ⇒ affine-in-ρ ⇒ no signaling) and inverse (signaling amplitude of hypothetical violation, closed form; symmetry protection at maximal entanglement; sensitive config = partial entanglement + asymmetric bases). Honest split: consistency proof w.r.t. entanglement ontology; substrate carrying the joint amplitude is P-level, postulated. [DERIVATION_inverted_gisin]

## §8 Predictions and falsifiability (~2.5 pp)
- Deviation ledger with status (a table — includes the two in-thread retractions as a feature: the mechanism predicts its own failure modes and we falsified two candidate deviations ourselves): soft-threshold broadband deviation RETRACTED (rate-linearity); nonlinear-commit deviations RETRACTED all sectors (kinematics).
- Surviving channels are exclusively Stage-2: (i) mismatched-collective two-port detectors — port decomposition theorem (within-port deviations never signal; matched ports exactly protected — why all data are safe with 10⁶ margin); port bias κ ≈ −Δc_eff; state-dependent no-click; (ii) differential pre-coherence (same structure). [DERIVATION_stage2]
- **Referee trap #2 honored:** the atom-array claim = deviation from standard collective-mode (dressed-state) QM, not from naive per-site weighting; comparison to cooperative-optics literature (Asenjo-Garcia et al., Javanainen–Ruostekoski).
- **The tabletop discriminator:** P'(S) curvature κS(1−S) + state-dependent no-click vs QM's constant-efficiency rescaling — single-photon, no Bell test needed.
- **The fork, stated plainly (referee trap #3 resolved by honesty):** radical reading (engineered mismatched-port Bell ⇒ marginal shifts) vs protective reading (deeper fairness principle ⇒ derivable empirical equivalence to QM; our stated judgment). Framework cannot yet decide; this is the designated open problem.

## §9 Discussion (~2 pp)
- Is this a derivation? Three-layer answer (impossible sense: no, for anyone; theorem-from-physical-premises: yes, exactly, no |A|² by hand; stronger than the axiom: predicts failure conditions). [walkthrough §8]
- Comparison table: rows = programs (Gleason, Deutsch/Wallace, Zurek, DGZ/Valentini, Pearle/CSL, ABBH, Hughston, Adler, Khrennikov, ABN, this work); columns = dynamical? noise physical? fairness derived? exact Born? modifies QM dynamics? predicts deviations?
- Relation to Valentini (deviations from Born as relaxation physics — closest landscape analogue) and Khrennikov (threshold detectors, approximate Born — closest detector-side analogue).
- Forward pointers: Paper 2 (Heisenberg Cut = lock threshold, now quantitative); Paper 3 (DK framework revision).
- Open problems (honest list): deeper-fairness fork; GHZ/three-station; e ∝ A² inside ZBW proper; cluster residual; general-N induction; LO-driven detectors beyond single-quantum sector.

## Appendices
- A: Itô fairness proof (all noise laws) + correlated-noise drift formula derivation.
- B: Slaved-phase linear-system analysis; layer-width derivation from two directions.
- C: Vertex-counting/kinematic linearity, sector by sector.
- D: Simulation methods + code availability (all sims from 2026-07-20 scratchpad, to be archived in repo before submission — TODO: copy scripts into a `born_selection_sims/` folder and pin seeds).
- E: Signaling amplitude closed forms (inverted-Gisin Theorem 3; port-game κ model).

## Figures plan (7)
1. Three-stage measurement schematic (capture → selection → registration), with premises P1–P4 placed on it.
2. The knife-edge: share drift under three noise scalings (analytic curves + sim points).
3. Failed vs fair games: one-shot selection and biased exchange vs martingale (bright-among-nine bar chart).
4. Born deviation vs lock-layer width w, tailed vs gapped profiles; physical detector regimes marked.
5. Bunching/anti-bunching: game vs Glauber vs intensity-only model (the |1,1⟩ / (|2,0⟩+|0,2⟩)/√2 pair).
6. Bell game: S vs resync fidelity η (sim + law), with experimental η floor marked.
7. The tabletop discriminator: P'(S) curvature (framework) vs constant-efficiency line (QM), with state-dependent no-click inset.

## Claims discipline (one-line register, keep during drafting)
CLAIM: fairness derived from P2 (novel). CLAIM: kinematic commit linearity (novel). CLAIM: slaved-phase sharpness (novel). CLAIM: exact-Born-any-speed (novel). CLAIM: emergent no-signaling + fidelity law (novel framing). DO NOT CLAIM: martingale ⇒ Born (Pearle/ABBH); excitation ∝ |E|² (Lamb–Scully); CHSH = 2√2 as novelty; atom-array deviations without the dressed-state comparison; any probability-from-nothing.

## Drafting order (suggested)
1. §2 premises + §5 core theorems first (the load-bearing physics, mostly transcription from derivation notes).
2. §4, §3, §6 (mechanics + statistics).
3. §7, §8 (Bell, predictions — the delicate claims; write with PRIOR_WORK open).
4. §1, §9, abstract last (framing after content is fixed).
5. Figures from existing sims (re-run with pinned seeds into repo folder).
