# Prior-Work Report — Born-Rule Outcome-Selection Paper (due diligence)

*Compiled 2026-07-20 by literature-search agent; reviewed by Claude. Purpose: complete citation base for Paper 1 (outcome selection), honest novelty line, and referee-trap list. Companion to WALKTHROUGH_born_outcome_selection.md and the four derivation notes.*

**Top-line: the mathematical engine (martingale + absorbing barriers + optional stopping ⇒ P = initial share) is Pearle (1976, 1982) and Adler–Brody–Brun–Hughston (2001) and must never be presented as new. The claimed novelty is confined to: (a) the martingale living in physical detector-site energies driven by vacuum noise (no modification of fundamental dynamics), (b) the fairness being DERIVED from amplitude-linear coupling rather than postulated, (c) slaved-phase/level-discreteness threshold sharpness, (d) exact-Born-at-any-commit-speed for rate-linear absorbers, (e) the falsifiable deviation package (each with adjacent precedent — see traps).**

---
## 1. Pearle's gambler's ruin — CLOSEST PRECEDENT

- **Pearle, P., "Reduction of the state vector by a nonlinear Schrödinger equation," Phys. Rev. D 13, 857–868 (1976).** Squared amplitudes execute a drift-free random walk with absorption at 0 and 1; reduction probabilities = initial |a_i|². Structurally our martingale step, 50 years earlier — but on Hilbert-space amplitudes, with fairness POSTULATED as a noise condition.
- **Pearle, P., "Toward explaining why events occur," Int. J. Theor. Phys. 18, 489–518 (1979).** Outcome = which noise realization; multi-channel Brownian absorption.
- **Pearle, P., "Might God toss coins?," Found. Phys. 12, 249–263 (1982).** THE explicit gambler's-ruin ⇒ Born paper: superposed states "play against each other" in a fair game; P(win) = initial stake. Credit this for the whole game metaphor.
- **Pearle, P., Phys. Rev. A 39, 2277 (1989)**; **Ghirardi, Pearle, Rimini, Phys. Rev. A 42, 78 (1990).** CSL: the gambler's ruin embedded in a norm-preserving stochastic SDE; new fundamental constants, testable anomalies. OURS differs: no modification of fundamental dynamics; noise = ordinary vacuum/detector noise.

## 2. Martingale structure in collapse models

- **Bassi, A., Ghirardi, G.C., "Dynamical reduction models," Phys. Rep. 379, 257–426 (2003), arXiv:quant-ph/0302164.** Canonical review; general theorem: martingale squared-amplitudes + absorbing eigenstates ⇒ Born exactly.
- **Adler, S.L., Brody, D.C., Brun, T.A., Hughston, L.P., "Martingale models for quantum state reduction," J. Phys. A 34, 8795–8820 (2001), arXiv:quant-ph/0107153.** Cleanest prior statement of martingale + optional stopping ⇒ Born; recovers Lüders rule. Our optional-stopping step is mathematically identical — cite prominently.
- **Diósi, L., J. Phys. A 21, 2885 (1988).** Independent early formulation.
- **Adler & Bassi, J. Phys. A 40, 15083 (2007)** (colored noise); **Adler, Science 325, 275 (2009).** Noise-spectrum family resemblance to our correlated-noise analysis.

## 3. Energy-driven reduction, Gisin no-signaling constraints

- **Gisin, N., Phys. Rev. Lett. 52, 1657 (1984); Helv. Phys. Acta 62, 363 (1989); Phys. Lett. A 143, 1 (1990).** Stochastic collapse with Born statistics; no-superluminal-signaling essentially FORCES the martingale structure; generic nonlinearities allow signaling. ⚠ Directly relevant to our nonlinear-commit-rate deviation prediction — see referee trap #3 below.
- **Hughston, L.P., Proc. R. Soc. A 452, 953 (1996).** Energy-driven stochastic SDE on projective Hilbert space; Born by martingale argument. NOTE: "energy-driven" there = Hamiltonian drives Hilbert-space collapse, NOT deposited oscillator energy as stake — distinguish explicitly to avoid confusion.
- **Brody & Hughston:** J. Math. Phys. 43, 5254 (2002); J. Math. Phys. 46, 082101 (2005), arXiv:quant-ph/0503231; J. Phys. A 39, 833 (2006); review arXiv:1611.02664 (in *Collapse of the Wave Function*, CUP 2018).
- **Percival, I.C., Proc. R. Soc. A 447, 189 (1994)**; *Quantum State Diffusion*, CUP 1998; Gisin & Percival, J. Phys. A 25, 5677 (1992). Planck-scale noise origin proposal; ours (vacuum noise at the detector) is more prosaic and testable.

## 4. Adler trace dynamics

- **Adler, S.L., *Quantum Theory as an Emergent Phenomenon*, CUP (2004).** Quantum theory as statistical mechanics of matrix models; residual fluctuations = CSL-type noise. Shares the architecture "substrate statistics + martingale collapse"; different substrate; fairness again postulated via noise coupling.

## 5. Semiclassical photodetection (our Stage 1 is theirs)

- **Lamb, W.E., Scully, M.O., "The photoelectric effect without photons," in *Polarisation, Matière et Rayonnement* (Kastler jubilee), PUF Paris (1969), 363–369.** Quantized detector + classical field: threshold, instantaneity, rate ∝ |E|². Our tip-energy-∝-A² step must credit this. What they LACK: single-quantum exclusivity (a classical field fires two detectors at once) — our martingale winner-take-all exists precisely to supply it. Say this explicitly.
- **Mandel, L., Sudarshan, E.C.G., Wolf, E., Proc. Phys. Soc. 84, 435 (1964)**; **Mandel & Wolf, *Optical Coherence and Quantum Optics*, CUP 1995, ch. 9, 14.** Photocount rate ∝ intensity; the rate-linearity of our continuum-absorber step is standard here; novel part is only its combination with martingale shares (exact Born at any commit speed).

## 6. Threshold detectors + classical random fields

- **Khrennikov, A., Found. Phys. 39, 997 (2009), arXiv:0805.1511; J. Mod. Opt. 59, 667 (2012), arXiv:1105.4269; arXiv:1212.0756 (2012); arXiv:1111.1907 (CHSH from threshold detectors); *Beyond Quantum*, Pan Stanford (2014).** PCSFT: classical random fields + threshold detectors, hitting-time analysis ⇒ Born APPROXIMATELY, calibration-dependent, with predicted deviations. Closest in spirit on the detector side; differences: no winner-take-all martingale over sites, Born only approximate; his "beyond Born" deviations predate our prediction package — cite there.
- **Marshall, T.W., Santos, E., Found. Phys. 18, 185 (1988).** Stochastic optics: detection = field above ZPF threshold; struggles with exact single-photon anticorrelation — our martingale exclusivity is the claimed fix.
- **de la Peña, Cetto, Valdés-Hernández, *The Emerging Quantum*, Springer (2015).** SED; vacuum field as randomness source; no detector-side game mechanism.

## 7. Born-derivation landscape (framing citations)

- **Gleason, J. Math. Mech. 6, 885 (1957)** — uniqueness of the measure, not a mechanism.
- **Deutsch, Proc. R. Soc. A 455, 3129 (1999)**; **Wallace, *The Emergent Multiverse*, OUP 2012**; critique **Barnum, Caves, Finkelstein, Fuchs, Schack, Proc. R. Soc. A 456, 1175 (2000)**.
- **Zurek, PRL 90, 120404 (2003); PRA 71, 052105 (2005)** — envariance.
- **Dürr, Goldstein, Zanghì, J. Stat. Phys. 67, 843 (1992)** — quantum equilibrium; **Valentini, Phys. Lett. A 156, 5 & 158, 1 (1991); Valentini & Westman, Proc. R. Soc. A 461, 253 (2005)** — relaxation to |ψ|², possible primordial deviations (closest landscape analogue of our deviation predictions).
- **Masanes, Galley, Müller, Nat. Commun. 10, 1361 (2019), arXiv:1811.11060** — "measurement postulates operationally redundant" (note live controversy: critique Quantum 9, 1749 (2025); response Quantum 9, 1592 (2025)). Our claim-form echoes theirs; ours is dynamical, theirs operational — compare in the intro.

## 8. Winner-take-all / symmetry-breaking measurement models

- **Allahverdyan, Balian, Nieuwenhuizen, "Understanding quantum measurement from the solution of dynamical models," Phys. Rep. 525, 1–166 (2013), arXiv:1107.2138**; Curie–Weiss model, Europhys. Lett. 61, 452 (2003). Metastable apparatus tipped into one ferromagnetic well — physical winner-take-all registration with Born weights from unitary QM + stat mech. MUST cite; "detector as metastable system tipped into a basin" is their territory.
- **van Wezel, J., Symmetry 2, 582 (2010), arXiv:0912.4202**; spontaneous unitarity violation program (Mertens et al. arXiv:2301.03233; Proc. R. Soc. A 481, 20250254 (2025) — CSL as white-noise limit of SUV). Born only for tuned noise — supports our "fairness needs deriving" point.
- **Grady, M., arXiv:hep-th/9409049 (1994).** Early sketch.
- FINDING: no prior work derives Born from Kuramoto-style synchronization or oscillator competition — that quadrant is genuinely open.

## 9. Sub-wavelength atom arrays (prediction novelty check)

- **Asenjo-Garcia, Moreno-Cardoner, Albrecht, Kimble, Chang, PRX 7, 031024 (2017), arXiv:1703.03382** — selective radiance.
- **Javanainen, Ruostekoski, Li, Yoo, PRL 112, 113603 (2014); Javanainen & Ruostekoski, Opt. Express 24, 993 (2016); Ruostekoski, PRA 108, 030101 (2023)** — cooperative response beyond standard optics.
- **Rui et al., Nature 583, 369 (2020)** — subradiant atomic-layer mirror.
- Single-photon superradiance: **Scully et al., arXiv:0804.3767**; array emission statistics: arXiv:2503.16624.
- ⚠ FINDING: nobody frames array response as "which-atom-absorbs deviates from per-site |A|²" — because in standard QM the which-atom distribution still obeys Born on the COLLECTIVE (dressed) modes. Our novel claim must be a deviation from the standard-QM collective-mode prediction, not from naive per-site weighting (the latter is ordinary cooperative optics). Sharpest referee trap in the predictions section.

## 10. Speed-of-collapse bounds (corrected numbers)

- **Salart, Baas, Branciard, Gisin, Zbinden, Nature 454, 861 (2008), arXiv:0808.3316.** 18 km, 24 h: influence speed > 10⁴ c (≈5.4×10⁴ c for CMB-like frame), for preferred-frame speeds ≤ 10⁻³ c.
- **Yin, Cao, Yong, Ren et al., PRL 110, 260407 (2013), arXiv:1303.0614.** Bound **1.38 × 10⁴ c**. (The "10¹³ c" figure circulating in our notes is WRONG — correct exponent is 4.)
- **Zbinden, Brendel, Gisin, Tittel, PRA 63, 022111 (2001)** — moving-frame before-before, correlations undiminished; **Stefanov, Zbinden, Gisin, Suarez, PRL 88, 120404 (2002)** — multisimultaneity refuted.

---

## Must-credit shortlist (in order)

1. Pearle 1976 + 1982 — the gambler's-ruin ⇒ Born argument itself.
2. Adler–Brody–Brun–Hughston 2001 (+ Bassi–Ghirardi 2003, Hughston 1996) — the martingale/optional-stopping theorem in mature form.
3. Lamb & Scully 1969 + Mandel–Sudarshan–Wolf 1964 — excitation/rate ∝ |E|².
4. Khrennikov 2009–2013 — threshold detectors + classical fields ⇒ approximate Born + deviations.
5. Allahverdyan–Balian–Nieuwenhuizen 2013 — winner-take-all metastable registration, solved dynamically.

## Genuinely novel (nothing found doing these)

(a) Martingale in PHYSICAL detector-site energies driven by vacuum noise — collapse-model mathematics without modifying fundamental dynamics. (b) Fairness DERIVED (Itô drift-free shares from amplitude-linear coupling) — every predecessor postulates it (Gisin's no-signaling results explain why they had to). (c) Slaved-phase / level-discreteness threshold sharpness. (d) Exact Born at any commit speed for rate-linear continuum absorbers. (e) The falsifiable deviation package — with adjacent precedents per item (Khrennikov, Valentini for deviations generally; cooperative optics for arrays).

## Referee traps (address before submission)

1. **Never present the martingale engine as new** — it is Pearle/ABBH. Ours is the physical realization + fairness derivation.
2. **Atom-array prediction must be sharpened against standard collective-mode QM** (Born on dressed states), not naive per-site weighting — else it is just cooperative optics restated.
3. **Gisin no-signaling tension:** our nonlinear-commit-rate deviation prediction implies (via the Bell-pair structure) that such a detector could shift the far wing's marginals — an in-principle signaling channel. Either embrace as a radical prediction with explicit discussion, or show the framework forbids exploitable configurations. Must be confronted head-on; a referee will find it.
4. CHSH = 2√2 reproduction is a consistency check, not a novelty (any Born-faithful mechanism yields it); the publishable part is the fidelity law S = 2√2·η and its link to the §10 speed bounds.
5. Correct Yin 2013 to 1.38×10⁴ c anywhere it appears.
