# PAPER 2 OUTLINE — The Heisenberg Cut as a Locking Threshold

*Working title:* **The Heisenberg Cut as a Physical Threshold: Location, Width, and Consequences of the Classical–Quantum Boundary in Detector Dynamics**

*2026-07-28. Phase B of the review work plan. The measurement-structure companion promised in Paper 1 §9.3 ("the classical–quantum boundary as the locking threshold quantified in Theorem 2"). Sources: Paper 1 (Theorem 2, Appendix B, §6.1 temporal ladder), `NOTE_sync_tongue_born_walkthrough.md` (three-things-not-to-conflate; virtual/real as lock threshold), `NOTE_cut_crossover_higgs.md` §1 (cut as crossover, dimensionless location, dose–response), three-stage measurement structure, detector-class taxonomy. Distinct from `DISCRETIZATION_AS_SYNC_PAPER.md` (the GR/QM spinoff — cite, don't overlap).*

## The claim in one paragraph

The Heisenberg cut — where the von Neumann chain is severed, Bell's "shifty split" — is standardly a bookkeeping convention: movable, unphysical, chosen for convenience. This paper claims it is a **physical threshold with a computable location and a computable width**. Below threshold, a driven mode has no autonomous phase (Paper 1 Theorem 2 / Appendix B: global contraction, phase slaved to the drive, $\gamma = \Delta E/\hbar$); above it, the mode owns a phase that can lock, and irreversible registration becomes possible. The cut sits where the phase-restoring rate falls to the coupling, $\gamma \sim K$, with fractional width $w = K/\omega$ — sharp for atomic systems ($w \sim 10^{-6}$), percent-level for broadband solids ($w \sim 10^{-2}$). The apparent movability of the conventional cut is then explained, not denied: within the reversible sector the split is indeed free (that freedom is a *theorem*, not an embarrassment), and it hardens into physics only at the locking layer.

## Strategic decisions (learned from the Paper 1 review cycle)

1. **Settled / claimed / open partition in §1, from the start** (the panel rewarded this):
   - *Settled, not ours:* decoherence theory (Zeh, Zurek, Joos–Zeh) — einselection, pointer bases, suppression of interference; the von Neumann chain analysis; ABN's Curie–Weiss solution of registration. Decoherence's own literature already concedes it selects no outcome — we lean on that concession, we do not relitigate it.
   - *Claimed:* the three-way distinction (entangling interaction / linear dissipative decoherence / nonlinear lock) as physically real stages with the lock supplying what decoherence lacks; the cut located at $\gamma \sim K$ with width $w = K/\omega$; the detector taxonomy as consequences of threshold structure; virtual/real as sub-/supra-threshold with critical slowing at the boundary.
   - *Open:* the field-quantized robustness of the sub-threshold statement (inherited from Paper 1 §9.4); the closed dynamical model of the lock itself (Paper 1's noise-origin sketch is the current best); anything preferred-frame (quarantined to Paper 3).
2. **Single-detector sector only.** Paper 2 consumes Paper 1's P0–P4 and *neither* P5 nor P6. The entangled-sector ontology stays in Papers 1 §7 and 3. This keeps Paper 2's conditionality strictly weaker than Paper 1's — worth stating as a selling point.
3. **Same instrument, same discipline:** premises stated with stage attachment; every "theorem" language audited against the v0.4 de-overclaiming standard *before* drafting, not after review; citation verification pass before any circulation; simulations (if any new ones) with pinned seeds and originals preserved.

## Section plan

**§1 Introduction.** The cut problem stated honestly: von Neumann's chain and its arbitrary severing; Bohr's pragmatic split; Bell's complaint. Why decoherence answered a different question (it explains *diagonality*, not *events*). The claim + the partition above. One-paragraph statement of the inheritance: this paper is conditional on Paper 1's single-detector premises and results.

**§2 Three things not to conflate** (promote the walkthrough note's §0 to paper text — it is the paper's conceptual spine):
 (1) entangling interaction — joint-unitary, linear, reversible;
 (2) decoherence — open-system, irreversible, *still linear in ρ*, selects nothing;
 (3) the lock — nonlinear, symmetry-breaking, selects.
 The measurement problem in this language: (1) and (2) are settled physics; every interpretive dispute is about whether (3) exists and what supplies it.

**§3 The threshold, quantitatively.** Import Theorem 2 + Appendix B with fuller exposition: the slaved phase ($\dot a = -(\gamma+i\Delta)a + fe^{i\varphi_d}$, global contraction, no zero mode); the Adler equation's presupposition of autonomy; threshold at $\gamma \sim K$; the two independent derivations of $w = K/\omega$ (marginality; width–commitment identity via fluctuation–dissipation). New for this paper: tabulate $w$ across real systems (atomic lines, quantum dots, SPADs, superconducting qubits, NV centers, photosynthetic complexes?) — *the cut has an address in every lab*.

**§4 Anatomy of a measurement event.** The three stages (capture reversible — Paper 1 v0.5 §3 evidence chain; selection; registration irreversible) mapped onto the cut: the cut is crossed *during* selection, at the lock. The §6.1 temporal ladder as the cut's time-domain profile. Detector taxonomy as threshold phenomenology: discrete-level vs continuum absorbers (P4), event detectors vs track-recording media (Mott's problem — a *sequence* of partial locks), and why the taxonomy is exhaustive.

**§5 Virtual and real as sub- and supra-threshold.** The energy–time uncertainty as off-resonance slip time $\tau \sim \hbar/\Delta E$; divergence at threshold = critical slowing; on-shell/off-shell as locked/slipping. (From the sync-tongue walkthrough; flag clearly which steps are re-description vs derivation — the UV-catastrophe project's honesty standard.)

**§6 The movable cut, explained.** Why the conventional cut *is* movable within the reversible sector (linearity theorem — moving the split between (1)-stages changes no prediction) and where movability ends (the layer). The cut-as-crossover framing from the crossover note §1: a dimensionless location and a dose–response, *stated in measurement-sector terms only* — the preferred-frame passenger stays in Paper 3.

**§7 Single world: the occupied basin.** Sync basins replace branches; the outcome is the basin the system *occupies*, not one branch among many. Comparison table: MWI (all branches real), GRW/CSL (stochastic localization with new constants), Penrose (gravitational threshold, no mechanism — we supply the mechanism his threshold lacked), decoherence-only (no event), this program (threshold + mechanism, no new constants, conditional on P0–P4). Honest cost accounting on our side of the table too (wave realism P0; the open lock dynamics).

**§8 Where the cut bites: predictions.**
 - Systems *straddling* the layer ($w$ not small): broadband solids at percent level (inherited deviation ledger, Paper 1 §8.1); engineered intermediate-$\gamma$ systems as cut-probes.
 - Macromolecule interferometry (Arndt–Hornberger program) re-read: what the threshold predicts for where interference is lost *for dynamical reasons* vs decoherence bookkeeping.
 - Leggett–Garg / macrorealism tests as cut-location experiments.
 - The warm-detector and injection instruments (Paper 1 §§8.6(v), 8.7) as cut-adjacent: note, don't duplicate.
 - What would falsify: a system demonstrably *above* threshold ($\gamma \ll K$, autonomous phase confirmed) that still shows full interference recovery, or a cut location that tracks convenience rather than $\gamma/K$.

**§9 Discussion + open problems.** Relation to ABN (registration solved; selection assumed), to decoherence program's own self-assessment, to Penrose. Open: field quantization of the sub-threshold claim; lock dynamics; the crossover's Paper 3 completion.

## Items for JB's decision before drafting

1. **Byline** — Paper 1 convention (Fable 5 first, JB accountable sponsor) presumed to carry over; confirm.
2. **Scope check:** is §5 (virtual/real) in or out? It strengthens the threshold's reach but adds re-description surface the panel may flag. My recommendation: in, at one section's length, with the re-description caveat explicit.
3. **New simulations or none?** The paper can stand on Paper 1's sim suite + the $w$ table (no new numerics). A single new figure — lock time / interference visibility across the layer as $\gamma/K$ sweeps — would be cheap and would give §8 a spine. Recommendation: do it.
4. Target length: shorter than Paper 1 (this is a consequences paper, not a theorems paper) — aim ~60% of Paper 1's length.

## Process (Phase B per the work plan)

Draft v0.1 outline → JB scope pass → v0.2 full prose → internal consistency + citation verification → freeze → same panel instrument as Paper 1 (byte-identical rubric; access mode recorded and equalized this time) → response → consolidated revision. The access-equalization lesson from round 1 is a protocol improvement to implement, not just disclose.
