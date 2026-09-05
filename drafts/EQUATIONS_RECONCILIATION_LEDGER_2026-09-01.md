# EQUATIONS.md reconciliation ledger — 2026-09-01

*Instrument: a directed sweep of `EQUATIONS.md` (the Many Clocks equation reference)
against Paper 1 v0.7, prompted by the observation that neither tri-paper propagation
round covered it — round 1 swept four documents, round 2 swept two, and EQUATIONS.md
appears in neither, despite being an actively maintained companion (last touched by
`373f5c3`, "propagated to all companion papers") that carries its own independent
Born-rule account in §12 with **no cross-reference to Paper 1 in either direction**.*

*Not an independent audit. Same agent as the E-1–E-6 edits. Items E-7 onward were
surfaced by author questions during the session rather than by systematic sweep, so
coverage is opportunistic, not exhaustive. Items E-9 onward reach outside EQUATIONS.md
into Paper 1 and the sidereal/frame material; they are logged here only because this
is where they surfaced, and they belong in a tri-paper round.*

**Totals: 20 items · 7 applied · 13 pending disposition.** *(2026-09-02: E-16 applied to Papers 1–3 as v0.8; E-19 added.)*

---

## Applied 2026-09-01 (EQUATIONS.md §12 and §14)

| # | Sev | Location | Finding | Fix applied |
|---|---|---|---|---|
| **E-1** | **HIGH** | §12 closing ¶ | **Both halves false against [P1].** "structurally a hidden-variable theory in which the hidden variable is the instantaneous background-field configuration; it satisfies Bell's theorem because it does not use this story to explain Bell correlations." [P1] §4: the noise "carries no outcome information of its own; it is not a hidden variable" — its magnitude provably drops out. [P1] §7 *does* extend the mechanism to Bell, via P5's shared registry, yielding $S = 2\sqrt2\eta$. | Withdrawn with both refutations stated inline; consistency-with-Bell re-grounded on P5/P6 nonlocality at premise level. Noted that §4's Dirac-spinor Bell account and [P1] §7's registry account are **nowhere reconciled** — logged as open, not asserted equivalent. |
| **E-2** | **HIGH** | §12 "Energy-partition mechanism" | Grounded the discrete click on per-channel quantized thresholds, which do not forbid two channels crossing. [P1] v0.7 added **P4(a)** for exactly this: closed pot $\sum_i e_i = \hbar\omega$ + full-quantum threshold ⇒ exclusivity from conservation. | Corrected, with [P1] §1/§9's standing caveat imported: exclusivity, quench, and energy routing remain **owed and not discharged**. |
| **E-3** | MED | §12 "Honest limitation" opening | Postulate set (wave realism + equal-energy channels + unbiased background) is smaller than [P1] v0.6's, which separates two probability spaces and holds a **detector ready-state preparation measure** as an explicit premise. | Stated the gap; boxed law flagged as conditional on a preparation measure. |
| **E-4** | MED | §12 ¶ after boxed law; gap 2 | Filed "why squared" as an open gap likened to Deutsch–Wallace branch counting. [P1] §1 partitions it oppositely: the square is **"not the contested quantity"** — driven-oscillator energetics plus Gleason, "neither ours to claim." | Disagreement stated explicitly; the square relocated to premise P1; Deutsch–Wallace comparison withdrawn as aimed at a different problem. |
| **E-5** | MED | §12 opening ¶ | "not as an independent probability axiom" is the claim v0.6 withdrew. | Replaced by **conditional outcome compatibility** over a tested domain. |
| **E-6** | LOW | §14 dictionary, Born row | Framework column read as a replacement claim. | Preparation-measure conditional added; "compatibility, not replacement (§12)". |

Rebuilt via the same pandoc invocation `build_pdfs.sh` uses (equations targets only).

---

## Applied 2026-09-02 (Papers 1–3, v0.8 corrections from E-16)

At JB's instruction ("correct the inconsistencies in the papers"). Every edit is marked
in-text as v0.8 or dated 2026-09-02, and withdrawn claims are quoted, not deleted.

| item | paper / section | edit |
|---|---|---|
| **E-16** | [P1] header | v0.8 revision note: ladder corrected against the paper's own commitment definition; v0.7 demotion of Theorems 4–5 withdrawn in turn; consequences (i)–(iv) listed. |
| E-16 | [P1] §2, P4(a) | Clause (a) marked as a premise about the quantum wherever $E_{\rm photon} > 2E_{\rm gap}$ (Si below 553 nm; all superconducting absorbers): the gap does not enforce exclusivity there. |
| E-16 | [P1] §2, P4(b)(ii) | v0.7's first-passage-only paragraph replaced: a commitment channel operates alongside selection, gated at $\theta$; Theorems 4–5 load-bearing for class (ii). |
| E-16 | [P1] §5.4 | Lead sentence and four paragraphs rewritten: demotion withdrawn; the linearity Theorem 5 must supply identified as that of the first-irreversibility vertex, the downstream cascade being photon-agnostic and so unable to carry which-site weight; the `theorem5_check` numbers reinterpreted (the paper operates between the two points). |
| E-16 | [P1] §6.1 | Losses bullet rewritten with $\theta$ explicit; exposed-window bullet added; "two to four orders at every rung" withdrawn and replaced by the corrected ladder (marginal Si, inverted NbN); $\Gamma$-invariance of $2\ln^2\!N$ stated (closes open item 4); temporal-structure paragraph's irreversibility moved up the ladder. |
| E-16 | [P1] §8.1 Table 1 | Threshold-gated commitment added as a live candidate channel; the "exclusively failures of P3" sentence corrected. |
| E-16 | [P1] §8.6(vii) | Gap-ratio-graded silicon test added as a candidate. |
| E-16 | [P1] §9.4(xi) | Share-ontology fork and the owed discrete-exchange threshold-gated simulation added. |
| E-16 | [P2] §4.1 table and prose; §4.2 | Registration row reworded (first irreversibility precedes record-writing); v0.8 update appended to the Theorem 4 sentence; "rate process throughout selection" replaced by the $\theta$-gated statement; a further correction appended to L2-1. |
| E-16 | [P3] §4.1, §4.7, §5.2 | First irreversibility placed at the end of selection (the surface event), not the amplification; the Bell-detector paragraph gains the clause that the recording clock is not the variable, the photon-to-gap ratio is; the v0.7 parenthetical in §5.2 updated. |
| E-16 | [MCI] `current_revision_DK_paper.md` | **Not edited** — frozen as the provenance record by JB's 2026-07-31 decision ([P3] header). Its §5 row "Reversible window: brief (resonance fluorescence)" and its reading "the irreversibility is the amplification, not the bare excitation (a single excited electron can re-emit)" are superseded by [P3] §4.1/§4.7 as corrected: a semiconductor's reversible window closes at the vertex and thermalisation (fs–ps), and "a single excited electron can re-emit" is an atomic statement that does not transfer to a thermalised carrier in a 300 K continuum. |

| — | [P3] §4.2; [P2] §4.1 | **Sponsor-requested addition, not a reconciliation item.** Time/energy/information triad paragraph inserted after the "same rate, random position" entry and before the three hands, flagged interpretive and sponsor-originated: rate = energy, position = information, hand = time; the three bounds (time–energy uncertainty, Margolus–Levitin, Landauer) with $\hbar$ and $k_BT$ as the only two exchange rates; the framework's two conversions (capture: phase history → selecting noise; registration: dissipation → record); and the divergence at registration (energy conserved, position information not) identified with the cut. Stated as a binding, not an identity, at JB's agreement. Cross-reference added from [P2] §4.1's recoverability criterion. |

`Born_Selection.pdf` rebuilt from [P1] v0.8. [P2] and [P3] have no PDF targets in
`build_pdfs.sh`.

### Applied later the same day: [P1] v0.9 — reading B adopted (open item 5), on the results of 2a and 2b

At JB's instruction ("proceed automatically and work on the 3 suggestions"), after 2a
and 2b returned. Recorded as a *choice*, in the header, with the grounds.

| section | edit |
|---|---|
| [P1] header | v0.9 note: reading B adopted as the working ontology; grounds (the 576-state model enforces it; QED agrees at the vertex; reading A quantified in the paper's own engine over-predicts; the 505 nm $g^{(2)}(0)$ bound); consequences; what is retained as reading A's prediction; what the substrate still owes (the actualization law). |
| [P1] §2, P4(b)(ii) | v0.9 paragraph: no gate under B; Theorems 4–5 carry class (ii) at any speed; the $\theta$-gated statement retained as reading A's. |
| [P1] §5.4 | v0.9 paragraph: the gate tested — ungated linear law gives Born at every speed (Theorem 4 confirmed), any gate biases even the linear law (+0.04 at $r=1$; +0.12/+0.19 at $r=10$), exposure 40–90% of the game; corrects v0.8's "linearity, not slowness, protects the window"; what the game is *for* under B. |
| [P1] §6.1 | v0.9 paragraph: top rung not a condition under B; under A the discrete engine puts $t_{\rm exp} \approx \tau_{\rm game}$ (whole-game accounting, inverted, not marginal) and the gated bias at ~+0.1; the v0.8 "routine SPAD data" sentence replaced by 2b's finding (no asymmetric-split test below 553 nm located; coincidence branch bounded at $2\times10^{-3}$). |
| [P1] §8.1 Table 1 | Threshold-gated row reclassified "Reading A only": closed under B by Theorem 4; open and over-predicting under A; discriminator, not prediction. Follow-on sentence updated. |
| [P1] §8.6(vii) | v0.9 note: both owed checks done; predicted null under B; discriminates the readings. |
| [P1] §9.1 | Boundary sharpened: frequencies enter through the hazard's linearity in the share (P1 with Theorem 5); the game's theorems state what the substrate must not do; the actualization law is tested in the framework companion. |
| [P1] §9.4(xi) | Marked done; what is now owed in its place (the actualization law). |
| [P2] §4.1 | One sentence: v0.9 adopts the gate-free reading; "completion" is the whole-quantum vertex at whichever site fires. |
| [P3] §4.7, §5.2 | §4.7: under v0.9 the photon-to-gap ratio does not move the weights either; the substrate owes the actualization law (the Adler race, §6). §5.2: Theorem 5's linearity carries all the weight under B. |
| README | Paper 1 row to v0.9; claims bullet rewritten. |
| `g3_drain_tests/README.md` | Rows for `theorem5_check.py` and `threshold_gated_commit.py`. |

`Born_Selection.pdf` rebuilt from [P1] v0.9.

---

## Pending disposition

| # | Sev | Location | Finding | Recommended |
|---|---|---|---|---|
| **E-7** | **HIGH** | §12 "Connection to Nelson stochastic mechanics" | Endorses a **hidden-system-variable** structure that [P1] §4 disclaims and that Paper 3 §7.2 (round-2b item M-4) was rewritten the same week to distinguish the program from — Bohm-style probability law over hidden system configurations, where [P1] has the wave as beable, a Dirac-delta system factor, and the measure detector-side. Three further conflicts: [P1] cites Nelson **nowhere**; Nelson's $\nu=\hbar/2m$ is a *pinned, load-bearing* magnitude where [P1]'s noise magnitude is *provably irrelevant*; Nelson's diffusion is frictionless, violating fluctuation–dissipation, where [P1] tracks the damping companion terms explicitly. | **Rewrite, not delete.** The honest paragraph is that [P1]'s noise *is* the interference cross term (§4), and that its coherence-time dependence is precisely why it is not Nelson's $\nu$. Keeps the author's actual idea. Scope to §12 only — §11's and §14's Nelson uses are MCI-internal (diffusion coefficients, ZPF) and not Born-rule claims. |
| **E-8** | MED | §12 gap 1 + opening ¶ | **"Channel" conflates two decompositions.** §12 slides between system eigenstates ($\psi = \alpha\lvert0\rangle+\beta\lvert1\rangle$; "if instead energy eigenstates with $E_0 \neq E_1$") and detector hardware ("available detector channels"; "each detector channel is itself a quantized resonator"). [P1] uses **neither**: its index is *spatial* — $N$ candidate absorber sites at a common $\omega$, local amplitude $A_i$, closed pot. So "equal energy per quantum" is **not a restriction in [P1]** — it is automatic, and the non-degenerate case §12 worries about never arises. Gap 1 is a limitation of §12's own framing, mis-attributed as one of the mechanism. | Rewrite gap 1; state [P1]'s actual scope restriction instead (spatially compact detector, else P5/P6 consumed). |
| **E-9** | MED | §12 Nelson ¶; §11 | **Overstates Nelson independently of [P1].** "Nelson showed that a real particle undergoing stochastic motion… satisfies the Schrödinger equation." Wallstrom's objection: Nelson's equations are equivalent to Madelung's, and Madelung → Schrödinger requires separately imposing single-valuedness, $\oint\nabla S\cdot d\ell = 2\pi n\hbar$, which the stochastic story does not supply. Also relevant: Nelson's own later position on multi-time correlations in entangled systems, which bears on [P1] §7. | **Verify before editing.** Asserted from model knowledge, not from any repo source. Literature check on Wallstrom 1994 and Nelson's recantation owed. |
| **E-10** | MED | EQUATIONS.md §2 L51, §3 L55 | **Zero phase offset asserted where only frequency locking is generic.** "Fixed point of synchronization: $\varphi^\star = \Phi_{\text{bulk}}$" and "$\Phi_{D_1} = \Phi_{D_2} = \Phi_{\text{bulk}}$ (both detectors, before the experiment)." From the document's own equation $\dot\varphi = \omega + K\sin(\Phi_{\text{bulk}}-\varphi)$: $\sin\psi^\star = (\Omega-\omega)/K$, so $\psi^\star = 0$ **only at exact resonance**. Generic Kuramoto locking is a common frequency plus a *distribution* of detuning-set offsets. §2's own capture range (L59) already implies this. | Add the detuning offset; state that identical phases are the zero-detuning special case. |
| **E-11** | MED | EQUATIONS.md §3 L55, L87 vs [P1] P3(a) | **Shared phase located in the wrong place.** EQUATIONS.md puts phase identity in the *detectors* ($\Phi_{D_1}=\Phi_{D_2}$; "the hidden state is $\lambda = (\varphi_0, \Phi_{\text{bulk}})$… the same variable at both detectors"), which collides head-on with [P1] P3(a) — sites mutually incoherent, no shared reference. [P1] §7 puts it **pair-side** instead: "the pair was created as a single excitation of the shared medium, and the two waves retain a stored phase relationship." | **Adjudicated by JB 2026-09-01: adopt [P1]'s location (pair-side).** This makes E-11 an EQUATIONS.md correction rather than an open conflict, and dissolves the P3(a) collision. Note this also deepens E-1: §3's Bell mechanism is *structurally* a hidden-variable model, not a stray remark. |
| **E-12** | **HIGH** | `SIDEREAL_DECOHERENCE_PAPER.md` L158 vs `NOTE_cut_crossover_higgs.md` (uncommitted) | **The program has two incompatible answers for what the preferred frame *is*.** Sidereal paper: "the CMB *radiation* plays no dynamical role here. The hypothesis is that **the vacuum possesses a rest frame**; the CMB dipole serves only as the best available marker." Higgs note Role 4: MSW "defines a frame — the matter rest frame — **SR-safely, because it is ordinary stuff with a rest frame rather than a modification of the vacuum**… which matters precisely because **Stage-2's frame is cosmic radiation, not vacuum**." A third phrasing in `DERIVATION_bell_pair_joint_game.md`'s glossary: foliation "identified with the CMB frame," which does not disambiguate. Physically consequential: vacuum rest frame ⇒ genuine Lorentz violation under the full weight of clock-comparison constraints; radiation/matter frame ⇒ SR-safe, Fizeau/MSW class, constraints largely inapplicable. | **JB adjudication required.** Not a wording slip — a fork in what the program claims physically. Escaped both propagation rounds by sitting in uncommitted work. |
| **E-13** | LOW | `DERIVATION_bell_pair_joint_game.md` §6b | The frame-rotation model's logged repair for the Gisin tension is **inverted Gisin**, which became [P1] Theorem 5 — demoted in v0.7 to a robustness result. The note-level dependency was never revisited after the demotion. | Note-level only; record the weakened dependency. No paper claim rests on it. |
| **E-14** | LOW–MED | [P1] §2 P3(a); §4 (noise-origin ¶ and diffused-hologram ¶) | **One defect at two levels: the premise and the argument both say "distinct" where the physics requires "re-randomizing."** **(a) Premise level.** P3(a) is stated as an initial condition — "The internal phases of the absorber sites are **initially** mutually incoherent… **before capture**" — but §4's zero-mean argument consumes it as an ongoing dynamical property: "averaging over the phase of $\delta b_i$ kills it in expectation." Static-but-mutually-random offsets satisfy the premise as worded, yet within a shot they give a **constant** cross term — a drift, not zero-mean noise — and Theorem 1's converse already shows what drift does to the shares. **(b) Argument level.** §4 grounds the diffused hologram's non-invertibility on "a phase standard **nobody recorded**." That is epistemic, and it has a standing counterexample: wavefront shaping and optical phase conjugation invert scattering media whose phase standard nobody recorded either, by measuring the transmission matrix. *Unrecorded is not unrecordable.* The physical ground is that the references re-randomize every 10–70 fs, so no stable transmission matrix exists to learn. In magnetic-resonance terms the premise says $T_2^\*$ (mutually distinct) where the physics requires $T_2$ (stochastically re-randomizing); only the latter is non-invertible. | **Precision fix, not a physics failure** — the conclusion survives on the correct ground. See below. Recommend: P3(a) gains an explicit persistence clause cross-referenced to §6.1's ladder, and §4's non-invertibility claim is re-grounded on re-randomization rather than on non-recording. |

| **E-15** | **MED–HIGH** | [P1] Theorem 1 proof; Appendix D | **The stochastic calculus is chosen but never justified, and the physical noise selects the other one.** Theorem 1's proof applies **Itô's lemma** to $s_i = e_i/\sum_j e_j$; Appendix D integrates by **Euler–Maruyama**, which is Itô by construction. Neither says why Itô rather than Stratonovich. For multiplicative noise the choice is physical, not cosmetic. By **Wong–Zakai**, noise of any finite correlation time converges as $\tau_c \to 0$ to the *Stratonovich* equation, never the Itô one, and for $a(e) = \sqrt e$ the two differ by a drift $\sigma^2 a a'/2 = \sigma^2/4$ — identical on every site, hence share-**equalising** (a leader gains proportionally less from an equal absolute increment), which is precisely the failure mode Theorem 1's converse attributes to multiplicative noise. Physical detector noise has $\tau_c \sim 10$–$70\,$fs and is therefore colored, so it selects Stratonovich. The question is not whether correlation time perturbs Born but whether the paper's Itô baseline is the small-$\tau_c$ limit of the physical process at all. | ~~**Likely resolved by a premise the paper already has.** The $\sigma^2/4$ drift requires the total to grow; a closed pot forbids it, and v0.7's P4(a) closes the pot.~~ **That recommendation was written before the exchange test and is withdrawn — it is false.** Conservation does not resolve it: the projection form leaves the result unchanged (0.2953 vs 0.2934), and the genuinely conserving, antisymmetric exchange formulation breaks Born *worse*, collapsing every configuration to $1/N$. See both result sections below. The standing recommendation is now only the weaker half: state the Itô choice and its grounds explicitly, since a reader who notices it has no answer in the text — and treat the grounds themselves as **open**, pending the discretisation question. Numerical checks: `colored_noise_knife_edge.py`, `colored_noise_exchange.py`. |

| **E-16** *(APPLIED 2026-09-02 — Papers 1–3 v0.8; see "Applied 2026-09-02")* | **HIGH** *(raised 2026-09-02 after computing the ladder — see the E-16 result section; severity is provisional on the two flagged uncertainties, either of which could return it to MED)* | [P1] §6.1 (ladder); §4 (noise origin); §5.4 | **Cooling inverts the ladder's top rung, and §6.1 is computed only at room temperature.** *(Rewritten 2026-09-02 — the first version of this item named the wrong failure; see the correction paragraph below.)* §4 writes P2's noise as one increment from "the wave packets of the detector's other bound charges *and* the vacuum/environment field," conflating a **thermal** source with a **zero-point** one. The asymmetry is real and large: the free-field thermal occupation at optical frequency is already negligible at room temperature ($\hbar\omega/k_BT \approx 97$ at $\lambda = 500\,$nm, $T = 300$ K, giving $n \sim 10^{-42}$ — which is just [P1]'s own fairness window $\hbar\omega \gg k_BT$), while the near-surface noise that actually drives the game is set by the material's dissipation and *is* thermal. P3(b) gives both channels: $\Gamma_{\rm loc} \sim 10^{13}$–$10^{14}\,\mathrm{s^{-1}}$ (phonon, carrier–carrier — thermal) against $\Gamma_{\rm rad} \sim 10^{8}\,\mathrm{s^{-1}}$ (radiative/vacuum — not thermal), five to six orders apart. Freeze the phonons out entirely and $\tau_c$ runs from tens of fs to ~10 ns. | **Accept. JB-originated 2026-09-02** (asking whether temperature affects the vacuum as it affects matter). **The correction:** that does *not* break whiteness, because $\tau_{\rm game} \sim 2\ln^2\!N/\Gamma$ scales as $1/\Gamma$ **too** — both middle rungs stretch together and the separation $\tau_{\rm game}/\tau_c = 2\ln^2\!N$ is invariant, whichever channel dominates. The first version of this item claimed cryogenic operation endangers whiteness; that was wrong. **The actual risk is the top rung.** $\tau_{\rm commit}$ (ns–$\mu$s) is set by avalanche physics and readout electronics and does *not* scale with $\Gamma$, so cooling pushes $\tau_{\rm game}$ **up toward it**: a two-order drop in $\Gamma$ takes $\tau_{\rm game}$ from ~80 ps to ~8 ns, i.e. into the commit window. That matters because v0.7's entire restructuring rests on this rung — commitment being slow is why first passage settles the outcome before any commit-rate law acts, and why Theorems 4–5 were demoted from operative mechanism to robustness rider (§5.4). **Invert the rung and the fast-commit reading v0.7 withdrew comes back.** §6.1's ladder is computed only for a room-temperature silicon SPAD, while §8 discusses SNSPDs, which run at 1–4 K. Recompute the ladder for the cryogenic families §8 actually names, and state the $\Gamma$-invariance of the middle separation while doing so — it is a free robustness result the paper currently does not claim. |
| **E-17** | LOW | [P1] §2 (notation/premises) or §6.1 | **Selection and registration are spatially orthogonal, and the paper relies on this silently.** The Born pattern varies over the detector face: $|A_i|^2$ lives in $xy$, and the selection game is a competition among sites at different $(x_i, y_i)$, decided by *differences* between them. Registration is an out-of-plane process — the avalanche develops along $z$, driven by the junction bias. A spatially uniform $z$ field is invariant under $xy$ translation and therefore **structurally incapable** of biasing which site wins: it cannot distinguish site $i$ from site $j$. Stage 2 and Stage 3 are thus not merely sequential in time but orthogonal in space, and the field that powers registration is geometrically barred from touching selection. [P1] treats sites as an abstract index $i$ with no geometry beyond the spacing $d$, yet the geometry it does use is already in-plane (P3(b)'s $d \gg \ell$; §8's polarization signature stated "relative to the **array axis**"). | **JB-originated 2026-09-02; accept.** State it in §2 or §6.1 — one or two sentences. It cheaply answers a referee objection that would otherwise need magnitude estimates ("your SPAD has hundreds of volts across it; how is that not a bias?"), answering by symmetry instead. **Residual channel, correctly located:** not the bias but its $xy$ **non-uniformity** — guard rings, edge effects, doping variation, field crowding at the active-area perimeter — plausibly acting through Stark-shifted detunings to make capture site-dependent. That is the tractable question for a real device: not "is there a field" (yes, large) but "how flat is it across the active area." **Correction recorded:** `window_tests.py` Test B's catastrophic common-mode result ("bright wins 100%") applies to *fluctuating* common-mode noise, where multiplicative $\sqrt e$ coupling hands the leader a proportionally larger increment each step. It does not describe a *static* common bias, and was misapplied to one in session before JB's geometric argument corrected it. |
| **E-18** | **MED–HIGH** | [P1] §6.1 (parenthetical after the $\tau_{\rm game}$ estimate) | **A dismissal that E-15 invalidates.** §6.1 estimates $\tau_{\rm game} \sim 2\ln^2\!N/\Gamma$ for "$N \sim 5\times10^{10}$ sites in the diffraction volume" and then sets the question aside: *"(Only $\ln^2 N$ enters; **the answer is insensitive to the coarse-graining of 'sites'**.)"* That was fair while $N$ merely set the game duration. It is not fair now. E-15 showed the whiteness separation **is** $2\ln^2\!N$ — the same quantity — and that the failure when whiteness lapses is *total* (shares collapse to $1/N$) rather than graceful. So the definition of a "site," and more sharply the size of the region within which sites actually compete, becomes a physical parameter the Born result depends on. Range across plausible choices: $2\ln^2\!N$ = 1212 at $5\times10^{10}$, 382 at $10^6$, 95 at $10^3$, 42 at $10^2$, 11 at $N=10$ — a factor of ~29, against measured behaviour that is safe at persistence 0.18 and broken at 3.5. **JB-originated 2026-09-02** (from the medical-imaging framing: a detection event draws from a finite aperture, and no screen resolves single atoms). | **Accept; log the dependency, do not yet claim a defect.** Two sub-questions, both answerable: (i) what physically bounds the competing region — the diffraction volume (§6.1's implicit choice), the distance energy can hop through the common field during $\tau_{\rm game}$, or the pattern scale? (ii) Does $N$ in the ladder mean illuminated sites or sites-per-competing-region? These are the same "what is the discrete exchange model a discretisation *of*" question that blocks E-15, reached from the geometry side. **Note also what does *not* help:** coarse-graining cannot rescue the $1/N$ collapse, since uniform is scale-invariant — binning $N$ uniform sites into $P$ pixels gives uniform over $P$ pixels. Aperture changes the margin, it does not restore an erased pattern. |
| **E-19** | LOW–MED | [P1] §6.1; P3(b); §8.1 Table 1 (P3(b) row) | **The SNSPD is the nearest deployed detector to the correlated-noise channel, for the reason JB gave.** JB-originated 2026-09-02: the white noise that drives the game is supplied by thermal scattering of electron phases in matter; cooling to superconducting temperatures freezes that out, leaving the vacuum/radiative contribution relatively larger; and the nanowire's topology keeps the whole competing region within a fraction of a wavelength, with the signal carried in a surface layer for the nanoseconds of the readout. Computed: $f = \Gamma_{\rm rad}/\Gamma_{\rm tot}$ rises from $\sim10^{-6}$ (silicon, P3(b)) to $\sim10^{-3}$ (NbN at 2 K: $\Gamma_{\rm loc}\sim5\times10^{10}$–$10^{11}$ from $\tau_{ep}$, against $\Gamma_{\rm rad}\sim10^{8}$ carried over from P3(b) — whether that radiative figure transfers to a superconducting film is uncertain, the same species as E-16 uncertainty #1). The competing region ($\sim$100 nm $\times$ 50 nm) is sub-wavelength at 1550 nm, so the radiative part is fully correlated across it. Table 1's P3(b) row has deviations $\propto f$, "large only as $f\to1$": three orders above silicon but still $\sim10^{-3}$. Separately, $\tau_{\rm game}$ for NbN is 3.8–7.6 ns, comparable to the electrical reset $L_k/R\sim5$–50 ns, so game and readout overlap in time — the ordering §6.1 assumes for silicon (game $\ll$ record-writing) fails in the nanowire. Whether that matters depends on whether readout dynamics can feed back on the shares; [P1] assumes not, and the device physics reads the current redistribution as the hotspot's consequence rather than the game's input. | **Accept as a computable candidate; log, do not yet claim.** Two things to carry. (i) JB's original whiteness worry — the motivation for simulating an SNSPD at all — is answered: whiteness survives cooling because $\tau_c$ and $\tau_{\rm game}$ both scale as $1/\Gamma$ (the E-16 correction, now stated in [P1] §6.1 v0.8); the surviving cold-detector effects are the top-rung inversion (E-16) and this rise in $f$. (ii) Table 1's P3(b) row should name the SNSPD as the nearest deployed detector to that channel, at $f\sim10^{-3}$, when §8.1 is next revised. A direct SNSPD simulation, the original plan, now has its inputs: $\Gamma$, $N$, $\theta$, $f$, and the exposed-leg/commit ratio from E-16. |

---

## E-16 computed: the SNSPD ladder (`code/snspd_ladder_check.py`, 2026-09-02)

**Read the uncertainty statement at the end of this section before citing any number in
it.** The result is potentially serious, and it rests on two inputs this program has not
measured.

Script validates against §6.1 first, reproducing the paper's own silicon figures
($\tau_c$ 10–66.7 fs against the quoted 10–70; $\tau_{\rm game}$ 12.1–80.9 ps against the
quoted 12–81).

| detector | $\tau_{\rm game}/\tau_c$ (middle) | $\tau_{\rm game}/\tau_{\rm commit}$ (top) | verdict |
|---|---|---|---|
| Si SPAD, 300 K (§6.1's own) | 1214 | $10^{-5}$ – 0.08 | safe by 1–5 orders |
| NbN SNSPD, ~2 K, commit = hotspot (ps) | 382 | **76 – 763** | **inverted by 2–3 orders** |
| NbN SNSPD, ~2 K, commit = electrical reset (ns) | 382 | 0.076 – **1.5** | straddles unity |

The middle rung behaves exactly as the $\Gamma$-invariance predicts. **The unprotected top
rung does not survive on either reading of "commitment,"** against §6.1's claim of "two to
four orders of magnitude to spare at every rung." Robust to $N$: even at $N = 10^3$ the
game outlasts a 30 ps commitment by 32×.

**Why this is more than a caveat.** An inverted ladder puts SNSPDs in the *fast-commit*
regime, where Theorems 4–5 stop being a robustness rider and become the operative
mechanism — so the construction there **requires commit-rate linearity**. But v0.7's stated
reason for demoting those theorems in the first place was that the continuum-detector
literature *does not support* linearity, citing exponential SNSPD efficiency at low photon
energy and supralinear response in SPADs and SNSPDs. v0.7's own check reports **0.719
against Born's 0.500** for a wrong commit law at fast commit. SNSPDs are meanwhile in wide
use and return QM-consistent results.

### Uncertainty — stated prominently, as the finding requires

Two inputs are estimates, **both flagged in the script**, and the second alone decides the
outcome:

1. **Is $\tau_{ep}$ the right analogue of §6.1's "final-state width" for a superconductor?**
   A judgement, not a derivation. Less decisive: an order either way leaves the top rung in
   trouble on the picosecond reading.
2. ~~**What does "commitment" mean for an SNSPD?**~~ **RESOLVED 2026-09-02 — see below.**
   Was: hotspot-to-resistive-transition (ps) gives inversion; electrical reset (ns) gives a
   ratio straddling 1, a two-order swing on a term [P1] never defines operationally.

### Uncertainty #2 resolved: the commitment definition, fixed before application

*Method note. At JB's instruction the definition was derived and fixed **before** applying
it to any device, precisely to foreclose selecting the reading that gives the preferred
answer. This is the pre-registration discipline, and it is recorded because the term was
underdetermined and the temptation was real.*

**Definition.** Four places in [P1] constrain what commitment must mean, and they agree:
Theorem 2 (a slaved phase "points back to the drive, which is why $\kappa_{\rm ret}$-return
is possible at all; an autonomous phase has forgotten the drive, **which is why only
above-threshold sites can commit**"); §4's diffused hologram ("reversibility below the
layer and commitment above it are **the same fact about memory**"); §3 (capture is
reversible, evidenced by echo and quantum-memory experiments); §8.6(vi) ("deposition
completes only at registration," losing sites retaining no calorimetric residue). Hence:

> $\tau_{\rm commit}$ is the time from capture at which the deposited excitation **ceases to
> be coherently returnable to the common field** — the first moment after which no
> operation (echo, phase conjugation, cavity re-absorption) could recover it and re-run the
> competition. **First irreversibility.** Not the electrical pulse, not the readout.

**What makes that clock slow — [P1]'s own answer.** §6.1: "multiphonon dissipation of a
2.5 eV *virtual* excitation is **blocked by the absence of sub-gap final states** — the same
discreteness that sharpens the threshold (Th. 2) **protects the stakes**." Reversibility
during the game is not free; it is bought by a gap that removes decay channels. The
excitation stays virtual and returnable *because it has nowhere to go*. Generalising that,
without reference to any device:

> **The mechanism requires the absorber to have no dense manifold of final states below the
> registration threshold — $E_{\rm photon}$ comparable to $E_{\rm gap}$, within a small
> factor.** Where the photon vastly exceeds the gap, a down-conversion cascade is available
> immediately, the excitation becomes real and thermalised, and commitment occurs as fast as
> that cascade runs.

**Applied:**

| detector | $E_{\rm photon}$ | $E_{\rm gap}$ | ratio | stakes protected? |
|---|---|---|---|---|
| Si SPAD @ 500 nm (§6.1's own) | 2.5 eV | 1.12 eV | **2.2** | yes |
| InGaAs SPAD @ 1550 nm | 0.80 eV | 0.75 eV | **1.1** | yes |
| Ge SPAD @ 1550 nm | 0.80 eV | 0.66 eV | **1.2** | yes |
| **NbN SNSPD @ 1550 nm** | 0.80 eV | **1.5 meV** | **≈ 530** | **no** |
| TES (at transition) | — | ≈ 0 | — | **no** |

The criterion separates gapped semiconductor absorbers from superconducting ones. A 1550 nm
photon carries ~530× the NbN gap, so the quasiparticle cascade has abundant final states and
runs immediately: **there is no virtual sub-threshold regime for the game to occupy.** The
SNSPD therefore takes the picosecond reading and **the ladder inverts. Uncertainty #2
resolves against the theory.**

**What it means.** Not falsification, but a domain: *the mechanism applies to gapped
absorbers with $E_{\rm photon} \sim E_{\rm gap}$, and superconducting detectors fall outside
it.* [P1] could own that boundary explicitly.

**Bias flag, recorded deliberately.** The domain restriction happens to exclude the detector
families used in the most stringent Bell tests. However derived, that has the shape of the
selection bias JB raised in session. What redeems it is that it makes a *dangerous*
prediction rather than a safe one: **Born statistics should differ between SPAD and SNSPD
measurements of the same optical setup** — same photons, same beamsplitter, two families on
opposite sides of the criterion. The field's working assumption is that they agree. If they
do, the mechanism is in trouble, not excused.

**OWED: recompute silicon under the same definition.** *(**Discharged 2026-09-02** — see
"E-16 silicon recomputed" below. The paragraph is kept as written so the order of
operations stays visible.)* The definition must be applied where
it costs something. §6.1's quoted $\tau_{\rm commit}$ of ns–$\mu$s is the avalanche-and-quench
*cycle*, whereas first irreversibility is the virtual→real transition preceding it. If
silicon's true $\tau_{\rm commit}$ is ps–ns, **the safe case's margin shrinks by one to three
orders too**, and §6.1's "two to four orders to spare at every rung" would need restating for
its own detector. Not yet recomputed. Until it is, no claim should rest on silicon being
comfortable either.

All SNSPD inputs are literature-typical, not measured by this program.

**A standing reason for caution.** SNSPDs are widely deployed and give QM-consistent
results, which the chain above should make difficult. When a quick estimate says a
well-tested technology ought to be visibly broken, the estimate is usually what is wrong.
The likeliest resolutions are that commitment for an SNSPD really is the nanosecond
process, or that the real commit law is nearer linear than the efficiency curves imply —
though [P1] cites those curves itself and cannot have it both ways without saying which.
**This entry is logged as an open question with a computed estimate attached, not as a
result, and certainly not as a falsification.**

**Convergence worth noting.** Three ledger items now turn on the same defect: the model has
a term whose physical referent is unpinned, and the answer depends on which referent is
chosen — the discretisation of the exchange (E-15), the size of the competing region
(E-18), and the operational definition of commitment (here). That convergence is a better
signal than any individual number in this file.

---

## E-16 silicon recomputed: owed item #2 discharged (`code/silicon_commit_recompute.py`, 2026-09-02)

**Read the uncertainty statement at the end of this section before citing any number in
it.** The silicon timescales are literature-typical, and the accounting that decides the
verdict rests on §6.1's diffusive scaling at leg lengths where E-15 says that scaling is
least trustworthy.

*Method note.* The definition was fixed in the preceding section before this computation
was attempted. The script was written to run silicon at five wavelengths, InGaAs, and NbN
under two commitment readings, all by one rule, before any result was read. It validates
against §6.1 first ($\tau_c$ 10–66.7 fs, $\tau_{\rm game}$ 12.1–80.9 ps, as before).

**What the definition does to silicon.** Under first irreversibility the share axis of a
gapped absorber splits at
$$\theta = E_{\rm gap}/E_{\rm photon},$$
the share below which a site's holding $e_i = s_i E_{\rm photon}$ has *no* real final
state. Below $\theta$ the excitation is virtual and its only exit is return to the field:
protected, exactly as §6.1 says. Above $\theta$ a real electron–hole pair is available,
with $e_i - E_{\rm gap}$ going to phonons, and the interband vertex plus thermalisation is
the first irreversibility. For silicon that clock is **10 fs–1 ps** (the SPAD
device-physics review's three-event structure: photon-annihilation irreversibility
fs–100 fs; which-site distinguishability 10 fs–1 ps; field-driven seed unrecoverability
~1 ps). §6.1's quoted ns–$\mu$s is the avalanche-and-quench cycle, three to six orders
downstream, and is not $\tau_{\rm commit}$ under the paper's own definition.

Three things follow for §6.1's own detector before any ladder is computed:

1. At 500 nm, $\theta = 0.45$. §6.1's sentence — "multiphonon dissipation of a 2.5 eV
   *virtual* excitation is blocked by the absence of sub-gap final states" — is true for
   45% of the share axis and false for the other 55%.
2. $E_{\rm photon} = 2.2\,E_{\rm gap}$: **the closed pot can pay for two real pairs.** The
   gap does not enforce exclusivity at 500 nm; only P4(a) does, as a premise about the
   quantum rather than a fact about the absorber. The boundary $E_{\rm photon} = 2E_{\rm gap}$
   sits at 553 nm in silicon.
3. On the whole-game accounting E-16 used for the SNSPD, "two to four orders of magnitude
   to spare at every rung" becomes $\tau_{\rm game}/\tau_{\rm commit} = 12$–$8100$:
   inverted by one to four orders. **The paper's safe case is not safe by its own
   definition.**

**The accounting that matters, applied to both detectors by one rule.** The whole-game
comparison overstates the exposure. Only a site above $\theta$ can commit; under a closed
pot with $\theta \ge 1/2$ that is at most one site, and only during its final climb from
$\theta$ to 1. Under §6.1's own diffusive log-share scaling that leg takes
$t_{\rm exp} \sim 2\ln^2(1/\theta)/\Gamma$. The physically relevant top rung is
$t_{\rm exp}/\tau_{\rm commit}$:

| detector | $E_{\rm ph}/E_{\rm gap}$ | $\theta$ | pairs the pot pays for | whole-game $\tau_{\rm game}/\tau_{\rm commit}$ | exposed-leg $t_{\rm exp}/\tau_{\rm commit}$ | verdict |
|---|---|---|---|---|---|---|
| Si SPAD 405 nm | 2.7 | 0.37 | 2 | 12–8100 | 0.02–13 | marginal |
| **Si SPAD 500 nm (§6.1's own)** | **2.2** | **0.45** | **2** | **12–8100** | **0.013–8.4** | **marginal** |
| Si SPAD 650 nm | 1.7 | 0.59 | 1 | 12–8100 | 0.006–3.8 | marginal |
| Si SPAD 800 nm | 1.4 | 0.72 | 1 | 12–8100 | 0.002–1.4 | marginal |
| Si SPAD 1000 nm | 1.1 | 0.90 | 1 | 12–8100 | 0.0002–0.14 | marginal, near safe |
| InGaAs SPAD 1550 nm (silicon inputs, flagged) | 1.07 | 0.94 | 1 | 12–8100 | 0.0001–0.06 | safe |
| NbN SNSPD 1550 nm, commit = hotspot 10–50 ps | 533 | 0.002 | 533 | 76–760 | **16–160** | **inverted** |
| NbN SNSPD 1550 nm, commit = cascade onset 0.1–1 ps | 533 | 0.002 | 533 | 3800–76000 | **790–16000** | **inverted** |

Reading it: **silicon is marginal, not safe.** The range straddles unity by about an order
of magnitude on each side at every visible wavelength, closing toward safe only near the
band edge. **The SNSPD stays inverted on the exposed-leg accounting too**, on either
reading of its commitment, because $\theta \approx 0.002$ makes the exposed leg 6.3
log-units — about 79 exchange steps at $\tau_c$ = 10–20 ps, i.e. 0.8–1.6 ns against a
10–50 ps commit. So the SPAD/SNSPD asymmetry E-16 found survives, weakened: not "safe by
2–4 orders against inverted by 2–3," but "straddling unity against inverted by 1–2 (or 3–4)."

**What is at stake if the exposed channel fires.** If commitment were instantaneous once
a share crossed $\theta$, the two-site outcome for a Born 0.80/0.20 split would be
$P_1 = 1.00$ at 650 and 800 nm, 0.87 at 1000 nm, and 0.84 even for InGaAs at
$\theta = 0.94$ — §6.1's own "stopping at any finite share introduces a computable
$O(1-\text{threshold})$ bias," made explicit by the martingale hitting probabilities
(`two_site_instant_commit` in the script). For $\theta < 1/2$ (silicon below 553 nm) both
sites of a two-way split can be exposed at once and the two-pair channel is open; the
two-site formula no longer applies. *Asserted from model knowledge, not verified against a
source:* routine Si SPAD calibrations at asymmetric splits are consistent with Born at the
percent level or better. If so, the exposed reading is compatible with data only where
$t_{\rm exp}/\tau_{\rm commit}$ sits at the low end of its range, $\lesssim 0.1$ — i.e.
only if silicon's first irreversibility for an exposed site is $\gtrsim 0.1$–1 ps, the
slow end of the device range, at every wavelength in use. **That is a constraint the
mechanism now carries, not a refutation of it.**

**Disposition.** E-16 stays **HIGH**, with its substance restated. The defect is no longer
"cooling inverts the top rung," nor even "the SNSPD inverts." It is that **§6.1's top rung
is mis-specified for every detector, including its own**: the quoted $\tau_{\rm commit}$ is
the downstream avalanche cycle, not commitment as the paper defines it; with commitment
correctly placed, silicon is marginal and NbN inverted; and at 500 nm the gap does not
enforce the full-quantum threshold P4(a) relies on. §6.1 needs (i) $\theta$ made explicit,
(ii) "two to four orders to spare at every rung" withdrawn or re-derived on the
exposed-leg accounting, and (iii) the "absence of sub-gap final states" sentence
qualified to $s_i < \theta$. §2 should say that P4(a) is a premise about the quantum, not a
consequence of the absorber's gap, wherever $E_{\rm photon} > 2E_{\rm gap}$.

**The dangerous prediction, reshaped.** Yesterday's form — Born statistics differ between
SPAD and SNSPD on the same optics — survives but is confounded: material, $\Gamma$, $N$,
temperature and efficiency all change at once. The recomputation gives a cleaner form on
the paper's own detector family. **The deviation is graded in $E_{\rm photon}/E_{\rm gap}$**,
through $\theta$ (the exposed fraction of the share axis) and through
$\lfloor E_{\rm photon}/E_{\rm gap}\rfloor$ (how many real sub-gap excitations the pot can
pay for). One Si SPAD pair, one deliberately *asymmetric* splitter (§8.2 protects symmetric
ones), heralded single photons at two wavelengths straddling 553 nm. Standard QM: the same
ratio, and $g^{(2)}(0) = 0$, at both. The exposed reading: a bright-favoured shift that
grows with $1-\theta$, and below 553 nm an excess-coincidence channel from the open
two-pair possibility. Every downstream variable — avalanche, quench, readout — is held
fixed by construction. This is also the honest answer to the selection-bias flag in the
previous section: the test lands on the paper's own detector family, not on the one it
would prefer to exclude.

**What this says about the recording-time-frame hypothesis.** The DK-paper taxonomy's slow
recorders (cloud chamber, emulsion) differ from a SPAD in *record structure* — many
vertices, or $k \approx 3$–4 captures per grain within a memory time — not in where first
irreversibility sits. Under the fixed definition, every $k = 1$ detector's recording clock
(avalanche ns, hotspot ps, CCD readout ms, developer minutes) is downstream of first
irreversibility and, by Paper 3's own result that Stage 3 contributes no statistics,
cannot move the Born weights. A precipitous-versus-slow *recorder* comparison at $k = 1$ is
therefore predicted null on both readings. The live variable is the gap ratio, not the
readout time.

### Uncertainty — stated prominently

1. **The exposed-leg time uses §6.1's continuum diffusive scaling at a leg of ~1 exchange
   step** (0.8 log-units at 500 nm). That is exactly where E-15 says the scaling is least
   trustworthy; in the discrete-exchange simulations one step moves a share by at most 25%
   of the smaller holding, so the leader's climb from 0.45 to 1 takes several steps, not
   one. That correction lengthens $t_{\rm exp}$ and worsens silicon's verdict. A
   discrete-exchange run with a threshold-gated commit channel would replace this
   estimate with a curve; see open items.
2. **Silicon's first-irreversibility clock, 10 fs–1 ps, is literature-typical and spans
   two orders**; the verdict sits inside that span. The device review's own placement of
   "seed commitment" at field-driven separation (~1 ps) is the slow end and the kind end.
3. **Whether a partial share above $\theta$ can form a real pair at all is the
   share-ontology question** — the same unpinned referent as E-15 and E-18. If shares are
   off-shell amplitude bookkeeping that becomes energy only at $s = 1$ (Theorem 2's picture
   for class (i), extended to class (ii) by P4(a)), then there is no exposed channel, no
   independent commit clock, and the top rung is not a timescale at all but the premise
   P4(a). On that reading silicon *and* NbN are both first-passage detectors and the
   SPAD/SNSPD prediction dissolves. The paper cannot have it both ways: §6.1's "gap protects
   the stakes" argument presupposes that shares are energies which would decay if they could.
4. InGaAs was run with silicon's $\Gamma$ and commit clock, flagged in the script. NbN
   inputs are E-16's, unchanged, including uncertainty #1 ($E_{\rm gap}$ = 1.5 meV is the
   single-particle gap; $2\Delta$ would halve the ratio and change nothing above).
5. The claim that routine asymmetric-split SPAD data bound the deviation at the percent
   level is from model knowledge. A citation is owed before it is used as a constraint.

---

## Open item 2a discharged: the threshold-gated commit channel in the discrete exchange (`g3_drain_tests/threshold_gated_commit.py`, 2026-09-02)

**What was asked.** [P1] v0.8 §6.1 estimated the leader's exposed leg — its share above
$\theta = E_{\rm gap}/E_{\rm photon}$, where a real final state exists — at
$t_{\rm exp} \approx 2\ln^2(1/\theta)/\Gamma$, about one exchange step, and compared it
with the commit clock. Uncertainty #1 of the silicon section flagged that estimate as
least trustworthy at exactly that leg length. This run replaces it with a measurement in
the paper's own discrete engine (the stakes-scaled exchange of `theorem5_check.py`), and
then asks what a $\theta$-gated commit channel does to the outcome as a function of
$r = \lambda\,t_{\rm exp0}$ — the expected number of commit opportunities during the
winner's exposed leg, i.e. §6.1's $t_{\rm exp}/\tau_{\rm commit}$ — for a linear hazard
(Theorem 5's law, $f(e) = e$) and an Arrhenius one ($f(e) = e^{\beta(e-1)}$, $\beta = 10$).
Exposed sites fire with probability $\min(1, \lambda f(e_i))$ per step; the first to fire
takes the whole quantum (P4(a)); otherwise the game absorbs at $s \ge 0.995$. The
$\theta = 0$ rows are the ungated control, i.e. Theorem 4 as stated. Nothing samples an
outcome from $|A_i|^2$.

**Result 1 — exposure is most of the game, not one step.**

| configuration | $\theta$ | $t_{\rm exp0}$ (winner's steps above $\theta$) | game length (steps) | fraction |
|---|---|---|---|---|
| 2-site 0.80/0.20 | 0.45 | 96 | 106 | 0.91 |
| | 0.72 | 88 | 105 | 0.84 |
| | 0.90 | 65 | 106 | 0.61 |
| | 0.94 | 52 | 108 | 0.48 |
| 10-site, bright 0.500 (paper's) | 0.45 | 5807 | 7025 | 0.83 |
| | 0.72 | 4879 | 7002 | 0.70 |
| | 0.90 | 3319 | 7009 | 0.47 |
| | 0.94 | 2611 | 7013 | 0.37 |

The eventual winner sits above $\theta$ for **40–90% of the game**. The reason is the
kernel: a step moves $\delta = \pm 0.25\min(e_i, e_j)$, so as the losers drain the steps
shrink, and the leader's climb from $\theta$ to the 0.995 boundary is the *slow* part of
the game, not the fast part. The continuum estimate assumed constant log-share
diffusivity and is off by about two orders. Which kernel is physical is E-15's question,
unchanged — but the paper's own simulations use this one, so the paper's own accounting
for reading A must be the whole-game one: $t_{\rm exp} \approx \tau_{\rm game}$, and for
silicon $\tau_{\rm game}/\tau_{\rm commit} = 12$–$8100$, i.e. $r \gg 1$. The v0.8
"marginal" verdict for silicon does not survive the paper's own engine; under reading A
silicon is inverted.

**Result 2 — the ungated linear law is Theorem 4; any gate is not.** Deviation
$P(\text{bright}) - \text{Born}$, MC $1\sigma \approx 0.005$–$0.006$; columns are $r$.

*2-site 0.80/0.20, linear hazard:*

| $\theta$ | 0.01 | 0.03 | 0.1 | 0.3 | 1 | 3 | 10 |
|---|---|---|---|---|---|---|---|
| **0 (ungated)** | +0.001 | +0.009 | +0.012 | +0.001 | +0.001 | +0.003 | −0.006 |
| 0.02 | −0.000 | +0.003 | −0.005 | +0.001 | −0.004 | +0.007 | +0.002 |
| 0.37 | −0.002 | +0.001 | +0.009 | +0.014 | **+0.039** | **+0.075** | **+0.122** |
| 0.45 | +0.000 | +0.003 | +0.004 | +0.013 | **+0.041** | **+0.067** | **+0.121** |
| 0.59 | −0.004 | +0.013 | +0.011 | +0.017 | **+0.041** | **+0.071** | **+0.125** |
| 0.72 | −0.005 | +0.003 | +0.006 | +0.003 | **+0.041** | **+0.070** | **+0.110** |
| 0.90 | +0.003 | −0.008 | +0.007 | +0.012 | +0.012 | +0.029 | **+0.051** |
| 0.94 | +0.005 | +0.003 | +0.002 | +0.001 | +0.010 | +0.021 | +0.027 |

*10-site, bright site Born 0.500, linear hazard:*

| $\theta$ | 0.01 | 0.03 | 0.1 | 0.3 | 1 | 3 | 10 |
|---|---|---|---|---|---|---|---|
| **0 (ungated)** | −0.003 | +0.015 | +0.007 | +0.004 | −0.004 | −0.001 | −0.003 |
| 0.02 | +0.008 | +0.003 | −0.005 | +0.006 | +0.005 | +0.003 | +0.009 |
| 0.37 | +0.005 | +0.015 | +0.012 | +0.012 | **+0.036** | **+0.097** | **+0.189** |
| 0.45 | +0.004 | −0.003 | −0.001 | +0.023 | **+0.040** | **+0.092** | **+0.186** |
| 0.59 | +0.006 | −0.014 | −0.004 | +0.002 | **+0.038** | **+0.066** | **+0.121** |
| 0.72 | −0.011 | +0.005 | −0.006 | +0.003 | +0.027 | +0.036 | +0.054 |
| 0.90 | +0.003 | −0.005 | −0.006 | −0.006 | +0.011 | +0.015 | +0.025 |
| 0.94 | +0.009 | −0.001 | −0.002 | +0.001 | +0.012 | +0.008 | +0.015 |

Reading it. (i) The ungated linear law reproduces Born at every $r$ to Monte-Carlo
precision, on both configurations: **Theorem 4 confirmed as stated.** (ii) **Every gated
row deviates**, bright-favoured, once $r \gtrsim 0.3$: about $+0.04$ at $r = 1$, $+0.07$
to $+0.10$ at $r = 3$, $+0.12$ to $+0.19$ at $r = 10$ for $\theta$ in the silicon range
(0.37–0.59), smaller at $\theta \ge 0.9$ where the exposed leg is short. A gate sets the
conditional pick to zero for the unexposed sites, so a gated law is not Theorem 4's law,
however linear it is above the gate. **This corrects [P1] v0.8 §5.4's sentence that
"what protects the statistics in the exposed window is the linearity of the vertex law,
not the slowness of commitment": under reading A only slowness ($r \ll 1$) protects it.**
(iii) The deviation is negligible only for $r \lesssim 0.1$–$0.3$. With Result 1 putting
silicon at $r \sim 10$–$10^4$ under reading A, that reading predicts bright-favoured
shifts of order $+0.1$ at asymmetric splits, saturating as $r$ grows.

*Arrhenius hazard, $\beta = 10$ (both configurations):* deviations are **smaller** than
the gated-linear ones at the same nominal $r$ — at most $+0.05$–$0.06$ (2-site) and
$+0.03$ (10-site) at $r = 10$, within MC below $r = 1$. This is not the 0.719 of
`theorem5_check.py`, and the difference is the model: there, a *global* firing at rate
$q$ picked a site with weight $e^{\beta e}$ (a pick law); here each site's *hazard* is
$e^{\beta(e-1)}$, which at partial share is tiny ($e^{-5.5}$ at $e = 0.45$), so an
Arrhenius hazard barely fires before first passage and acts like a soft stopping rule
near $s = 1$. The dangerous law under a gate is the one that fires readily at partial
share — the linear one. (A barrier that *suppresses* partial-share commitment protects
the statistics; a golden-rule law does not, once gated.)

**What it decides.** Reading A of the share ontology, run on the paper's own engine,
predicts deviations that are large where the engine says silicon sits. That is one of
the two grounds on which [P1] v0.9 adopts reading B (the other is that the only
microscopic model in the program, `first_mark_two_absorber/`, enforces B by
construction). Under B there is no gate, the $\theta = 0$ rows are the physical case, and
Theorem 4 with a linear hazard is the whole of the registration argument. The fork is
kept testable: reading A's channel is retained in [P1] Table 1 as "reading A only," with
these magnitudes, and the 505 nm heralded bound of item 2b applies to its no-P4(a)
version.

**100-site Gaussian fringe (bright site Born 0.027; 1500 trials/run).** Exposure rows
complete; they confirm Result 1 at $N = 100$:

| $\theta$ | $t_{\rm exp0}$ (steps) | game length (steps) | fraction |
|---|---|---|---|
| 0.45 | 626,905 | 810,242 | 0.77 |
| 0.72 | 545,795 | 835,184 | 0.65 |
| 0.90 | 360,061 | 801,811 | 0.45 |

The ungated linear row ($\theta = 0$) gives $-0.003$, $+0.003$, $+0.001$ at $r = 0.03$, $0.3$,
$3$ (MC $1\sigma \approx 0.004$): Theorem 4 again. **Gated linear rows, appended as they
completed (later on 2026-09-02):**

| $\theta$ | $r = 0.03$ | $0.3$ | $3$ |
|---|---|---|---|
| 0.02 | −0.002 | −0.001 | +0.000 |
| 0.45 | +0.005 | +0.001 | +0.002 |
| 0.72 | −0.006 | +0.003 | −0.003 |
| 0.90 | −0.001 | +0.002 | +0.005 |

**No gate bias at $N = 100$**, within MC, at every $r$ — unlike the $+0.04$ to $+0.19$ of
the two-site and ten-site configurations. The difference is where the bright site starts.
In the 80/20 and ten-site cases the bright site begins above or near $\theta$, so the gate
creates an asymmetry at $t = 0$: it can commit and the others cannot. In the 100-site
fringe (bright site 0.027) no site starts exposed; the gate acts only in the end-game,
after a fair process has already picked the leader, and a linear pick among at most two
exposed sites is then close to first passage. So reading A's gate bias is a
**large-initial-share effect**: it afflicts asymmetric two-port splits in which one arm
carries more than $\theta$ of the intensity (any silicon beamsplitter test more asymmetric
than about 45/55 at 500 nm), and not many-site patterns such as a diffraction fringe.
This sharpens rather than weakens the v0.9 grounds: the two-port asymmetric-split data
that would show the effect are exactly the data item 2b found unpublished below 553 nm.
All four gated linear rows are in and null. Arrhenius rows ($\beta = 10$), complete:
$\theta = 0$: $+0.003$, $-0.010$, $+0.000$; $0.02$: $-0.004$, $+0.003$, $-0.005$; $0.45$:
$+0.002$, $-0.003$, $-0.001$; $0.72$: $+0.000$, $-0.005$, $+0.008$; $0.90$: $+0.001$,
$-0.004$, $-0.001$ — null as well. The sweep finished after 24,791 s (6.9 h); the script is
seeded and the full table is in `results_threshold_gated_commit.txt` (gitignored,
regenerable). At $N = 100$ no gate, linear or Arrhenius, moves the outcome.

**Caveats.** (a) $r$ is defined per exposed-leg step of *this* engine; mapping steps to
physical time is E-15's unpinned discretisation, so the absolute placement of silicon on
the $r$ axis inherits that uncertainty — but Result 1 is a ratio within the engine and
does not. (b) The Arrhenius normalisation $f(1) = 1$ makes its effective hazard at
partial share much smaller than the linear law's at the same $r$; the comparison across
laws is therefore at equal *full-share* hazard, not equal total firing. (c) Ties among
simultaneously firing sites are broken uniformly; at these hazards they are rare.

---

## Open item 2b discharged: sub-553 nm single-photon data taken with silicon SPADs (web search, 2026-09-02)

*Scope: a web search of the published record, not a systematic review; model-knowledge
claims are marked. Looked for: (i) $g^{(2)}(0)$ measurements below 553 nm taken with
silicon avalanche detectors, because there $E_{\rm photon} > 2E_{\rm gap}$ and the closed
pot could pay for two real pairs; (ii) percent-level Born-ratio tests at asymmetric
splits below 553 nm.*

**(i) Found, and it binds one version of reading A hard.**

| source | $\lambda$ | $E_{\rm ph}/E_{\rm gap}$ (Si) | $\theta$ | $g^{(2)}(0)$ | detectors |
|---|---|---|---|---|---|
| Heralded SPDC in BBO, pairs at 562/505 nm — the Kwiat-group source used for the single-photon vision experiments (arXiv 1806.08430; Tinsley et al. 2016) | 505 nm | **2.19** | 0.456 | **0.0023** (heralded, 80 kHz) | Si SPAD herald; heralded HBT on the 505 nm arm (model not stated in the review) |
| hBN "blue" quantum emitters, ZPL 436 nm (arXiv 2301.04269 and related) | 436 nm | 2.54 | 0.394 | ≈ 0.07 (background-corrected) | Si APDs, HBT |
| InGaN/GaN quantum dot, quasi-resonant 375 nm excitation, 9 K (APL Materials 9, 061106, 2021) | blue, ≈ 400–470 nm (class, not extracted) | ≈ 2.5–2.8 | ≈ 0.36–0.40 | **0.043 ± 0.009, raw, no correction** | Si APDs, HBT |
| InGaN/GaN QD, room temperature (same family) | blue | ≈ 2.5–2.8 | | 0.126 ± 0.003, uncorrected | Si APDs, HBT |

Every entry is below 553 nm, taken with silicon avalanche detectors, and shows
near-perfect anticorrelation. The heralded 505 nm source is the sharpest. Note what a
50/50 HBT split does at that wavelength: each arm holds share 0.5, above
$\theta = 0.456$, so under reading A **both** sites are exposed from $t = 0$ for the
whole game, not just the final leg, and the two-pair channel is open throughout (a
2.455 eV photon can pay for two 1.12 eV pairs with 0.2 eV to spare). Symmetry protects
the *ratio* (§8.2) but not the *coincidence* branch.

What the bound constrains depends on which version of reading A is meant:

- **Reading A without P4(a) as a premise** (a site whose holding exceeds $E_{\rm gap}$ can
  form a real pair on its own): both arms could fire, giving a double click. With
  per-site hazard $\lambda$ over a game of $\tau_{\rm game}$, $P(\text{double}) \sim
  (\lambda\tau_{\rm game})^2 \lesssim 2\times10^{-3}$ gives $\lambda\tau_{\rm game}
  \lesssim 0.05$, and since the exposed leg is $\sim 1$–$2$ of $\sim 1200$ exchange steps,
  $t_{\rm exp}/\tau_{\rm commit} = \lambda\,t_{\rm exp} \lesssim 10^{-4}$. **That version is
  pushed four orders below the marginal range** — first passage dominates and §6.1's
  original "safe" verdict is restored for it, though by data rather than by the argument
  the paper gave.
- **Reading A with P4(a) as a premise** (the first exposed site to fire takes the whole
  quantum; the model item 2a simulates): no double click can occur by construction, and
  $g^{(2)}(0)$ says nothing about the hazard. Its constraint must come from splitting
  *ratios*, which is (ii).
- **Reading B**: $g^{(2)}(0) \to 0$ is what QM predicts and carries no information about
  the game.

**(ii) Not found.** No purpose-built, percent-level test of Born splitting ratios at an
*asymmetric* split below 553 nm was located. Nearest evidence: (a) absolute SPAD
detection-efficiency calibrations with a focused beam tunable over 250–1000 nm
(PTB-type, 2019) and Klyshko twin-photon calibrations — single-detector,
wavelength-resolved efficiency measurements, which constrain linearity of response, not a
ratio at a split; (b) detector tomography (Lundeen et al. 2009) reconstructing a linear
POVM for a silicon SPAD, at $\sim$780 nm, i.e. above 553 nm. So the asymmetric-split
test of §8.6(vii) remains unperformed as such below 553 nm, and the "percent-level"
bound asserted in [P1] §6.1 (v0.8) should be read as an inference from calibration
practice, not a measurement. **Recommended [P1] phrasing:** "no published asymmetric-split
Born-ratio test below 553 nm was located (2026-09 search); the coincidence branch is
bounded at $2\times10^{-3}$ by heralded 505 nm data."

Sources: [arXiv 1806.08430](https://arxiv.org/abs/1806.08430) (vision-experiment review;
505 nm heralded source, $g^{(2)}(0) = 0.0023$); [Tinsley et al. 2016, Nat. Commun. 7,
12172](https://www.nature.com/articles/ncomms12172); [hBN blue emitters, arXiv
2301.04269](https://arxiv.org/pdf/2301.04269); [InGaN/GaN QD, APL Materials 9, 061106
(2021)](https://pubs.aip.org/aip/apm/article/9/6/061106/123137/Pure-single-photon-emission-from-an-InGaN-GaN);
[GaN QD temperature dependence, Sci. Rep. 7 (2017)](https://www.nature.com/articles/s41598-017-16040-x);
[PTB tunable 250–1000 nm SPAD calibration (2019)](https://www.researchgate.net/publication/332744312_Detection_efficiency_measurement_of_single_photon_avalanche_photodiodes_by_using_a_focused_monochromatic_beam_tunable_from_250_nm_to_1000_nm).

---

## E-15 numerical result (`born_selection_sims/colored_noise_knife_edge.py`, 2026-09-01)

Colored-noise variant of `noise_scaling_born.py` (#6, the knife-edge script feeding Fig. 2):
same configurations, same $\sigma = 0.3$, $\Delta t = 0.02$, threshold $0.9$, 4000 trials,
$\sqrt e$ law. OU noise normalised to unit intensity, so the white limit is recovered as
$\tau_c \to 0$.

| config | Itô white (paper's) | colored $\tau_c = 0.1$ | colored $\tau_c = 1$ | colored $\tau_c = 10$ |
|---|---|---|---|---|
| 10-site, Born bright $= 0.5$ | **0.5310** | 0.2934 | 0.2234 | 0.1660 |
| 3-site, Born bright $= 0.5$ | **0.5436** | 0.4496 | 0.4309 | 0.4037 |
| 10-site, conserving projection | **0.5355** | 0.2953 | 0.2220 | 0.1578 |

**The knife-edge does not survive colored noise in this engine.** At $\tau_c = 0.1$ — a
properly resolved regime, $\Delta t \ll \tau_c \ll \tau_{\rm game}$ — the ten-site bright
weight falls from $0.53$ to $0.29$ against a Born value of $0.50$. The direction is
equalising (toward $1/N = 0.1$), as the Wong–Zakai drift predicts, and the deviation grows
monotonically with $\tau_c$.

**$N$-dependence matches the mechanism.** The 3-site config moves only $0.54 \to 0.45$
against the 10-site's $0.53 \to 0.29$, because equalisation drives shares toward $1/N$ and
the bright site's Born weight of $0.5$ is much further from $0.1$ than from $0.33$.

**The closed-pot hypothesis FAILED — and the reason is instructive.** Conservation was
expected to forbid the drift, since $\sigma^2/4$ on every site requires the total to grow.
Implemented as a projection (rescale to fixed total each step) it changes nothing:
$0.2953$ against the open pot's $0.2934$. The algebra is immediate — adding a constant $c$
to every site and renormalising sends $s_i \mapsto (s_i + c/E)/(1 + nc/E)$, which is
*still* a pull toward $1/n$. Fixing the total does not fix the shares.

### The exchange formulation is NOT immune (`colored_noise_exchange.py`, 2026-09-01)

The prediction above was that `gambler_ruin_born3.py`'s conserving exchange
$\delta = \pm\,\mathrm{step}\cdot\min(e_i,e_j)$ would be protected, since the increment is
antisymmetric in $(i,j)$ and a common-mode drift is not merely forbidden but
unrepresentable. **That prediction is false.** White baselines reproduce Born to 1.5–2.7%,
matching the README's "~2% at absorb 0.95", so the harness is validated; the colored runs
then break Born comprehensively.

| config (Born bright) | white | $\tau_{\rm game}/\tau_c = 1210$ | $= 11$ | $= 1$ | $1/N$ |
|---|---|---|---|---|---|
| ten-site (0.5000) | 0.5187 | 0.3483 | 0.1240 | 0.1167 | **0.100** |
| two-site (0.8000) | 0.8273 | 0.8197 | 0.6180 | 0.5470 | **0.500** |
| three-site (0.6429) | 0.6580 | 0.6360 | 0.4050 | 0.3513 | **0.333** |

**The failure is total, not a bias.** Every colored run converges on $1/N$ — 0.117 against
0.100, 0.547 against 0.500, 0.351 against 0.333. The initial energy shares are not
perturbed, they are **erased**. With persistent noise the winner is set by which site drew
the favourable fluctuation, not by what it started with, so the outcome forgets $|A_i|^2$
entirely.

**The controlling parameter is not $\tau_{\rm game}/\tau_c$.** Note the two-site row is
fine at separation 1210 while the ten-site row is already broken there. The two-site game
lasts 220 steps, so separation 1210 puts $\tau_c$ at 0.18 *steps* — sub-step, i.e. white by
construction. The ten-site game lasts 21281 steps, so the same ratio gives $\tau_c = 17.6$
steps. What matters is $\tau_c$ measured against **a site's own inter-exchange interval**
($n/2$ steps under pairwise serialisation): persistence $\approx 3.5$ for the ten-site row
at 1210, $\approx 0.18$ for the two-site row. Deviation tracks persistence, not the ratio.

**Consequence for the mechanism, and it is not small.** Whiteness is not a technical
convenience in this construction — *it is what carries the Born weights at all*. If the
tie-breaker noise persists across a site's successive exchanges, the shares wash out to
uniform. That makes §6.1's timescale ladder load-bearing in a way the paper does not claim,
and it **raises E-14's stakes**: the difference between "mutually distinct" ($T_2^\*$) and
"stochastically re-randomising" ($T_2$) is not a precision fix but the difference between
Born statistics and uniform statistics.

**What remains genuinely open.** Mapping persistence to the physical detector requires
knowing how many exchanges a site makes per correlation time. §6.1 sets *both* the exchange
step and the surface-field correlation time from the same $\Gamma$ ("one exchange step per
10–70 fs"), which suggests persistence $\approx 1$ — the marginal regime, between the safe
0.18 and the broken 3.5 rows. The pairwise serialisation of the simulations introduces an
inter-play interval that has no evident counterpart in the physical picture, where all
sites couple to the common field simultaneously. **That mapping is not stated anywhere in
the paper, and it now matters.** No verdict should be drawn from these runs about the real
detector until it is made explicit.

**Two methodological cautions for anyone repeating this.** (i) $\tau_c < \Delta t$ is not a
small-$\tau_c$ probe but an under-resolved one — the $\tau_c = 0.01$ column was discarded
for this reason. (ii) The white-Stratonovich baseline is unreliable in the ten-site config
(98% of trials never absorb, because the equalising drift holds every share below the
threshold), so it cannot be used as the comparison point; the colored runs are compared
against the Itô baseline instead.

---

## Why E-14's severity is low, and where it is not

The physics supplies what the wording omits, for real detectors. §6.1's ladder gives the
surface-field correlation time as the exchange step, $10$–$70\,$fs (from $\Gamma \sim
1.5\times10^{13}$–$10^{14}\,\mathrm{s^{-1}}$ via fluctuation–dissipation), against
$\tau_{\rm game} \sim 12$–$81\,$ps. The phases re-randomize some **1200 times during the
game**, so P3(a) holds dynamically whether or not the premise says so.

That separation is more robust than the paper claims. From its own two rungs,
$\tau_{\rm game} \sim 2\ln^2\!N/\Gamma$ against an exchange step $\sim 1/\Gamma$, the ratio
is $2\ln^2\!N$ — **independent of $\Gamma$**. Narrow-line and broadband detectors get the
same separation, because both timescales scale as $1/\Gamma$ together. At $N \sim
5\times10^{10}$ this is $\approx 1210$, matching the quoted rungs. *This robustness result
is not stated anywhere in the paper and probably should be.*

**Where it does bite: small $N$ — the frozen-speckle regime.** The optical statement of
the same point, and the one that makes it concrete. A wavefront scattered from an object
*without* a coherent reference does not produce white noise at the plate: it produces
**fully developed speckle**, contrast $\sigma_I/\langle I\rangle = 1$, negative-exponential
intensity statistics — and if the scatterer and illumination are static, that pattern is
**frozen**. Arbitrarily long exposure records the same high-contrast pattern. What washes
speckle out is decorrelation (object motion, source bandwidth), never exposure alone. The
governing variable is therefore not exposure time but **exposure measured in correlation
times**, which is exactly the $2\ln^2\!N$ ratio above:

| $N$ | Game duration in correlation times | Regime |
|---|---|---|
| $5\times10^{10}$ (real detector) | $\approx 1210$ | fully washed out — white noise, as assumed |
| $10$ (ten-site sim) | $\approx 11$ | marginal |
| $2$ (two-site sim) | $\approx 1$ | **frozen speckle** |

So the two-site configuration runs in the static-speckle regime while assuming the
white-noise one, and the ten-site configuration is marginal. These are the configurations
the knife-edge simulations use (`gambler_ruin_born2.py`, `window_tests.py`). The theorems
are continuum statements and may be untouched, but the **simulations** carry the
knife-edge argument. Which conclusions rest on $N=2$ should be established: it appears in
§4(a)'s extreme-value refutation — where the 2:1 result ($0.791$ vs Born's $0.800$) is
itself flagged as "an accident of arcsine statistics" — and in Appendix D's
boundary-placement bias check.

**Two independent demonstrations that the distinction is real.** Both are experimental, and
both show that absence of a shared reference does *not* by itself buy irreversibility:

- **Spin echo** (magnetic resonance): $T_2^\*$ dephasing from static, spatially fixed
  offsets — chemical shift, susceptibility, field inhomogeneity — is undone completely by a
  $180°$ pulse. The coherence was never destroyed, only hidden in offsets a rephasing
  operation reverses. Only stochastic $T_2$ dephasing is unrecoverable.
- **Wavefront shaping / optical phase conjugation**: opaque scattering media with no
  coherent reference beam are inverted routinely by measuring the transmission matrix
  (Vellekoop & Mosk 2007 and successors). The medium's phase standard was never recorded,
  and it is inverted anyway — because it is static, hence learnable.

The common lesson is E-14(b): **re-randomization, not non-recording, is what forecloses
inversion.**

**Already covered, and worth recording as clean.** The failure mode is *not* new to the
paper. §8's ledger carries it: "Pre-established absorber coherence (phase-locked
ensembles) | P3(a) | **Live**," with the caveat that maintaining coherence requires
driving, which exits the single-quantum sector. And §8.6(iv) scopes it further: for the
P3(a) channel "the active variable is the **difference** in pre-established coherence
between ports, **symmetric pre-coherence being protected by §8.2**." So residual coherence
that is statistically uniform across the detector face — the expected case for a
homogeneous substrate — does **not** bias Born. Only differential pre-coherence does.

**One cross-reference the paper is missing.** §4's homodyne limit *is* the static-reference
case: "beat the signal against a strong coherent reference wave… and the same cross term
stops averaging away and becomes a signal linear in the complex amplitude." That is the
$T_2^\*$/common-reference end of §4's own magnetic-resonance trichotomy twenty lines later,
and the two passages are not connected. Joining them would make the premise's character
requirement self-evident and largely discharge E-14 editorially.

---

## The actualization law, tested at diagnostic budget: the two-channel Adler race (`adler_two_channel_exploratory/`, 2026-09-02)

*Status line first.* Every raw ledger behind this section carries the package's own
`numerical_gate = "diagnostic_only"` — the ticket-07 frozen budget of
`adler_born_two_channel/` is unmet and its moving-band audit stands at
`numerical_no_result`. These runs use 16 (and 32) clocks per channel against the frozen
64, timestep $2^{-7}$ (and $2^{-8}$) against the frozen $2^{-9}$, and 200–300 trials per
cell against the 2 406 the power calculation asked for. They are labelled `pilot` and can
never enter a production estimate. JB's instruction was "proceed with the Adler race"; the
package was not modified and remains untracked by his earlier choice.

**What was run.** The two-channel plan's race — earliest committing clock across two
populations on the identical detuning grid, one common raised-cosine envelope,
independent keyed noise per clock and channel, one fixed physical dwell — is exactly the
pairwise minimum of two independent one-channel raw races on the same clock time, since
the channels do not couple to each other. `race_driver.py` therefore calls the package's
own `raw_runner.write_raw_run` once per (polarization angle, channel) with
$K_A = K\cos\varphi$, $K_B = K\sin\varphi$, $K = 2.0$; `analysis.py` is the separate
comparison process that pairs the closed ledgers through the package's gate and is the
only place the analytic prediction is loaded. Estimand: the unconstrained exponent $p$ in
$P_A/(P_A+P_B) = K_A^p/(K_A^p+K_B^p)$, by binomial maximum likelihood with a
profile-likelihood 95% interval. Comparators, each scored by binomial deviance: $p=1$;
$p=2$ (Born, $\cos^2\varphi$); strongest wins; the Poisson race on the bare relaxation-rate
sum over the exact grid (quadratic on these grids: exponent 1.92 at $N=16$, 1.99 at 64);
the Poisson race on the eligible-clock count (linear: 0.94–0.96).

**Main sweep** ($N=16$, $dt=2^{-7}$, 300 trials/cell, nine angles 10°–80°):

| comparator | deviance (9 cells) |
|---|---|
| linear ($p=1$) | 102.6 |
| **Born ($p=2$)** | **51.9** |
| strongest wins | 36 968 |
| rate-sum race | 42.7 |
| width-only race | 133.6 |
| fitted $p = 1.56$ | 13.1 (8 dof) |

**Fitted exponent $p = 1.56$, 95% [1.44, 1.69]**: both predeclared families rejected.
Symmetric control at 45°: 0.470 [0.414, 0.526]. Ties 0.5%; unresolved 1 of 2700. The
curve is flatter than Born at both extremes (10°: 0.916 vs 0.970; 80°: 0.084 vs 0.030).

**Sensitivities** (three angles, 200 trials/cell): timestep $2^{-8}$ gives 1.42 [1.18,
1.67] and $N=32$ gives 1.50 [1.26, 1.76] — inside the main interval, so within this budget
the exponent is neither a discretisation nor a population-count artefact. The physical
knobs move it: pulse 8.0 → 4.0 → 2.0 gives 1.38 → 1.56 → 1.68; diffusion 0.02 → 0.08 → 0.32
gives 1.38 → 1.56 → 1.66; and the dwell, run as a full nine-angle sweep at each value,
gives **1.42 (0.25, three angles) → 1.56 [1.44, 1.69] (0.5) → 1.78 [1.60, 1.96] (1.0)**,
with Born still rejected at dwell 1.0 (deviance 23.5 on 9 cells; residual at 80°, 0.084
against 0.030, and at 45°, 0.429). At dwell 2.0, 82% of trials produce no commitment and
the exponent is undetermined [1.12, 2.40]. Each of those directions makes commitment
harder, and the unresolved fraction rises from 0 to 7–14% as $p$ rises.

**Reading.** Where nearly every trial commits, the race is decided by which channel's
fastest clock locks first, and that scales as roughly $K^{1.4\text{–}1.5}$ — more than
tongue width ($K^1$), less than width times rate ($K^2$). Where commitment is unreliable,
surviving the dwell selects for strongly contracting clocks, the rate factor enters more
fully, and the frequencies move toward the rate-weighted flux — but the efficiency
collapses before they reach it. Three
rows of the plan's predeclared interpretation matrix fire together: *the law is
criterion-dependent, not universal*; *the proposed selection propensity is time-window
dependent*; *quadratic analytic flux, nonquadratic direct outcomes* at the frozen dwell.

**What it means for the program.** [P1] v0.9 moved the whole burden onto the
actualization law: a substrate dynamics whose first-firing hazard is linear in the share
without that linearity being inserted. The Dirac–Kuramoto candidate for it is this race.
At diagnostic budget the race does not supply a universal hazard linear in the share (it
supplies $p \approx 1.5$ at the frozen criterion, $1.8$ at twice the dwell with Born still
rejected, and nothing determinable where the efficiency collapses). It is therefore not, as it stands, the actualization law B needs. The plan's
labelled positive control, the inverse-coupling dwell, was run afterwards at JB's request
(open item 6(a)) and overshoots to $p = 3.81$ [3.50, 4.15]: Born lies between the
amplitude-neutral and the scale-similar criterion and is reached by neither — and a
tuned dwell $\propto K^{-1/4}$, run as a demonstration, reaches it exactly ($p = 2.00$
[1.84, 2.16]), which quantifies how tuned a Born-producing criterion is and is not a
mechanism. The lock-tolerance and spectral sensitivities were then run and the missing
half power computed (open item 6(b)): the race scales as tongue width times the square
root of the rate because each clock's entry is a near-deterministic slide from its
starting phase and the fastest of $N$ such slides gains only logarithmically in $N$; a
Born-producing race would need memoryless per-site commitment with hazard proportional
to the local relaxation rate, so that hazards add across the tongue — which, read the
other way, is the golden rule reading B already imports. It is not a falsification of the
framework: the frozen production budget remains unrun, and a substrate rule that made
per-site commitment a Poisson process with that rate would do what the deterministic
slide does not. Full write-up with the per-angle tables in
`adler_two_channel_exploratory/RESULTS.md`.

### The energy-tracking race: memoryless commitment with hazard proportional to absorbed energy (`energy_hazard_race.py`, 2026-09-02)

Run at JB's request ("run an energy-tracking race variant where commitment hazard grows
with absorbed energy") after the order-statistics computation said what a Born-producing
race would need. Dwell replaced by a memoryless hazard $c\,E_i$; energy law the Adler
clock's own, power $K\cos\theta$ (zero on average over a slip, $\sqrt{K^2-\Delta^2}$ for a
locked clock) accumulated with its sign only while the clock is inside the tongue; Paper
1's quadratic deposit as the contrast. **Prediction stated first:** $p \approx 2$ for
Adler's power, $\approx 3$ for the square. **Artefact on record:** the first run clipped
energy at zero each step, rectifying the ineligible clocks' slip cycles into a spurious
$K^{1.33}$ residue and giving $p \approx 1.05$; ungated signed accumulation fails the same
way. Gated: **$p = 2.16$ [2.14, 2.19]** (Adler's power, $c = 1$, noise), 2.16–2.19 across a
decade of $c$ and with noise off; per-angle within $\approx 0.02$ of Born everywhere;
channel energy $\propto K^{2.20}$, which the exponent tracks; P1's square gives 3.20 with
energy $\propto K^{3.20}$. So the plan's mechanism — the rate-weighted tongue flux as the
outcome frequency — is realised once commitment is memoryless, and the square is *not*
inserted: it is tongue width ($\propto K$) times a locked clock's absorbed power ($\propto
K$). The residual 0.16–0.2 above 2 is the time-integrated flux on this grid and pulse
(stationary rate-sum exponent 1.91; central clocks eligible longer than edge clocks), not
the race. What was put in by hand is exactly the golden rule's structure — memorylessness
and hazard linearity in energy — i.e. Theorem 5 and reading B; what the substrate supplies
is the amplitude dependence. **Checks:** hazard $c\,E^m$ with $m = \tfrac12$ gives $p =
1.70$ [1.68, 1.73] and $m = 2$ gives 3.25 [3.21, 3.29] at unchanged energy scaling — only
the linear hazard lands near 2, so hazard linearity (Theorem 5) is load-bearing; a
stationary drive gives 2.09 [2.06, 2.11], energy $\propto K^{2.17}$, the residual above the
grid's stationary rate-sum exponent 1.91 being the locking transient. Open item 6 is
updated accordingly: the fixed-dwell race is not the actualization law; the memoryless
energy-hazard race is a candidate for it at diagnostic budget, conditional on a physical
commitment process having the golden rule's structure, which is the E-16 question.

### The E-16 first-irreversibility check for a memoryless hazard (`e16_memoryless_hazard_check.py`, 2026-09-02)

Run at JB's request. **Part 1, the detectors' Markov ratio** $\lambda\tau_c$ (bath
correlation time over first-irreversibility clock; the golden rule's constant rate needs
$\ll 1$), from the E-16 inputs: Si SPAD 500 nm **0.01–6.7** (marginal, the third time this
ratio has straddled unity for silicon, each time with a different meaning); NbN SNSPD
hotspot reading 0.2–2.0 (marginal); NbN cascade reading **10–200** (not memoryless — a
cascade completing inside a fraction of the electron–phonon time is an avalanche, not a
rate process). **Part 2, the race with a lagged hazard** (absorbed energy becomes
hazard-bearing after a first-order lag $\tau_{\rm mem}$; prediction fixed first: flat while
$\lambda\tau_{\rm mem}$ is small, rising as the lag pushes commitment toward the pulse end):
$p = 2.21, 2.16, 2.21, 2.18, 2.18, 2.18$ at $\lambda\tau_{\rm mem} = 0, 0.1, 0.3, 1, 3, 10$,
no unresolved trials, the 45° control at 0.501 throughout. **The prediction's second half
failed: nothing moves.** A lag common to every clock reparametrizes time identically for
both channels and leaves the ratio of hazards, hence the outcome, unchanged. **Part 3,
what it decides:** the Markov ratio is not the quantity that decides whether a detector
can carry the energy race's mechanism; memory in the hazard's *timing* is harmless, while
its *form* is not (square-root and squared hazards gave 1.70 and 3.25; a deterministic
slide gave 1.5). What the detector must supply is a *stochastic* commitment whose
probability per unit time is linear in the site's absorbed energy with a site-independent
time profile — the structure of the absorption vertex itself, in both families — while the
deterministic physics downstream (avalanche, hotspot, quench) is a cascade the device
review had already found photon-agnostic. On this reading the SNSPD's non-Markov cascade
is downstream of selection and irrelevant to it; the SPAD/SNSPD asymmetry does not arise
from this mechanism either; and the picture is reading B's: weights fixed at the vertex,
stochastically and linearly, everything slower writing the record. Still unanswered by any
simulation: whether the vertex's stochastic selection is one-world actualization or a rate
over an ensemble — the measurement problem.

### Ensemble versus one-world at the vertex: the exclusivity discriminator (`vertex_exclusivity_discriminator.py`, 2026-09-02)

Run at JB's request. The observable separating "independent golden-rule rates at every
site" from "exactly one site commits per quantum" is the coincidence rate of a balanced
split fed with single photons — item 2b's $g^{(2)}(0) = 0.0023$ at 505 nm. In the energy
race (20 000 trials, step $2^{-8}$): independent hazards give $P(\text{both commit}) =
1.000$ at 45°, a coincidence ratio of 1.00 — **the ensemble reading is excluded by a factor
of ~400**. The first-commit stop gives zero by rule. A one-world stop that propagates with
a delay $\tau_x$ leaves doubles growing linearly in $\tau_x$ (density 1.5 per race unit at
45°, 0.5 at 20°) and meets the bound only for $\tau_x \le 1.5\times10^{-3}$ race units,
$9\times10^{-4}$ of the mean commit latency. Through E-16's first-irreversibility clocks:
silicon **0.01–0.9 fs**, in which light travels 3 nm–0.3 µm; SNSPD hotspot 9–45 fs,
3–13 µm; against 1 mm–1 m port separations (3 ps–3 ns light-crossing). The mapping of race
time to physical time is a choice; every mapping leaves the critical delay at
$10^{-3}$–$10^{-4}$ of a femtosecond-to-picosecond interaction time, so the margin of
$10^3$–$10^8$ is robust. **What it decides:** the vertex selection is one-world, and the
stop rule is not droppable bookkeeping — it must act across the separation faster than
light by orders of magnitude, i.e. it is the nonlocal closed-pot constraint P5 that v0.7
already conceded the single-detector sector consumes. The Grangier argument, inside the
race, with numbers. Nothing here derives the constraint; the simulations have now said
what it must do and how fast.

### Spectral controls (Experiment 7; `spectral_driver.py`, `spectral_analysis.py`, 2026-09-02)

The raw boundary admits only a flat grid, so the densities were realised through the
package's public factories (a clock path at any detuning, a declared population, the
validated race) with the commit times recorded in exploratory CSVs rather than the closed
ledger. Five densities of 16 clocks per channel, five angles, 200 trials per cell; the
flat case re-run through the same path as the reference. Comparators computed on the same
detunings the race used.

| spectrum | direct $p$ [95%] | rate-sum exponent | eligible-count exponent | dev. Born | dev. rate-sum | dev. width | dev. linear |
|---|---|---|---|---|---|---|---|
| flat | 1.51 [1.32, 1.71] | 1.91 | 0.97 | 22.2 | 17.0 | 45.5 | 34.4 |
| Gaussian ($\sigma = 1$) | 1.29 [1.13, 1.47] | 1.82 | 0.81 | 51.8 | 26.9 | 47.9 | 14.4 |
| Lorentzian ($\gamma = 0.75$) | 1.09 [0.95, 1.25] | 1.69 | 0.69 | 101.0 | 40.4 | 51.6 | 4.7 |
| central peak | 1.01 [0.86, 1.16] | 1.48 | 0.36 | 131.5 | 39.2 | 85.5 | 4.6 |
| central notch | 3.01 [2.62, 3.45] | 2.46 | 1.14 | 36.5 | **2.0** | 47.5 | 196.0 |

(5 cells per spectrum; deviances of fixed comparators are $\chi^2$ with 5 dof.)

**Reading.** (i) The plan's falsification — "outcome frequencies remain exactly quadratic
while the analytic flux changes strongly" — did not happen: the direct exponent moves
with the spectrum, monotonically and in the same order as both the rate-sum and the
eligible-count exponents. The events are driven by the spectrum the tongue sweeps
through; in the plan's matrix, "supports the spectral-flux interpretation but creates an
empirical detector-spectrum burden." (ii) On the four spectra without a threshold, the
direct exponent is not the rate-sum exponent (one power above the width) but about **one
half power above the eligible-count exponent**: 0.97 + ½ = 1.47 against 1.51; 0.81 + ½ =
1.31 against 1.29; 0.69 + ½ = 1.19 against 1.09; 0.36 + ½ = 0.86 against 1.01. The direct
race scales as *width times the square root of the rate*, not width times rate. (iii) The
notch is the exception that explains itself: with an empty centre no clock is eligible
until $K$ exceeds 0.56, so at 10° and 80° the weak channel cannot commit at all and the
direct curve is a threshold; the rate-sum race, which carries the same threshold, fits it
(deviance 2.0) while Born does not (36.5). (iv) The missing half power is the one the tuned dwell supplied by hand. The
band-to-spread candidate for it (a locked clock's in-band probability going as $K^{1/2}$
through its noise spread $\sqrt{D/r}$) was recorded as a prediction and then tested by the
tolerance sweep, which did not support it (open item 6(b)): the half power survives a
band wide enough to remove it. Its source was then computed (open item 6(b)): the entry-time order
statistics of near-deterministic Adler slides from random phases, which gain only
logarithmically in the number of eligible clocks where a Poisson race would gain a full
power.

---

## Open items

1. **Multi-site re-pinning is unsimulated.** §6.1 claims "a long wavepacket continually
   re-pins the *shares* to the instantaneous Born pattern." Every script in
   `born_selection_sims/` sets `e0` once and runs drive-free; `first_mark_two_absorber` has
   fixed mode coefficients and no spatial degree of freedom at all. The one Gaussian-envelope
   test that exists — `code/complex_rotation_exclusivity.py` E3, click timing vs
   $|f(t)|^2$ — runs on a **single site** (`w = [1.0]`), so it tests timing, not share
   re-pinning. `adler_born_two_channel` has a time-dependent envelope but a *shared*
   raised-cosine one, deliberately common across channels; a spatially extended packet would
   give each site its own local envelope, which is the untested case.
2. ~~**OWED — recompute the silicon ladder under the first-irreversibility definition of
   commitment** (E-16, uncertainty #2).~~ **Discharged 2026-09-02** — see "E-16 silicon
   recomputed." Result: silicon is marginal, not safe; the SNSPD stays inverted; §6.1's top
   rung is mis-specified for every detector. Three new items replace it:
   - ~~**2a. Discrete-exchange run with a threshold-gated commit channel.**~~ **Done
     2026-09-02 — see "Open item 2a discharged."** Exposure is 40–90% of the game in the
     paper's own engine (not one step); the ungated linear law gives Born at every speed
     (Theorem 4 confirmed); any gate biases even the linear law (+0.04 at $r = 1$, +0.12 to
     +0.19 at $r = 10$). Grounds for [P1] v0.9. The 100-site grid was still running when
     logged; its rows are to be appended. Was: Extend
     `g3_drain_tests/theorem5_check.py`: commitment can fire only at sites with
     $s_i > \theta$, at rate $\propto e_i$ (Theorem 5) and, separately, Arrhenius; sweep
     $\theta \in \{0.37, 0.45, 0.59, 0.72, 0.90, 0.94\}$ and the commit hazard across the
     marginal range $t_{\rm exp}/\tau_{\rm commit} = 10^{-2}$–$10^{1}$. This replaces the
     analytic instant-commit bound and the ~1-step diffusive leg estimate (uncertainty #1)
     with a curve, and gives the wavelength-graded prediction its magnitude.
   - ~~**2b. Literature check, owed before use:**~~ **Done 2026-09-02 — see "Open item 2b
     discharged."** $g^{(2)}(0)$ below 553 nm with Si SPADs: found (505 nm heralded,
     0.0023; 436 nm hBN, ≈0.07; InGaN QDs, 0.043 raw); binds the no-P4(a) version of
     reading A to $t_{\rm exp}/\tau_{\rm commit} \lesssim 10^{-4}$, says nothing about the
     P4(a) version. Asymmetric-split Born-ratio tests below 553 nm: **not found**; the
     percent-level bound in [P1] §6.1 v0.8 is an inference from calibration practice.
   - ~~**2c. §6.1 and §2 restatement**~~ **Done 2026-09-02 ([P1] v0.8; propagated to [P2], [P3]).** Was: per the disposition: $\theta$ explicit; "two to four
     orders at every rung" withdrawn or re-derived on the exposed-leg accounting; the
     sub-gap-final-states sentence qualified to $s_i < \theta$; P4(a) stated as a premise
     about the quantum wherever $E_{\rm photon} > 2E_{\rm gap}$.
3. **Small-$N$ whiteness / frozen speckle** — see above. The two-site knife-edge runs sit
   at $\approx 1$ correlation time of game duration, i.e. in the static-speckle regime, while
   assuming white noise. Needs a check of which conclusions depend on $N=2$, and ideally a
   re-run with coloured noise at the sims' own $\tau_c/\tau_{\rm game}$ ratio to confirm the
   knife-edge results are not artefacts of the whiteness assumption at small $N$.
3. **EQUATIONS.md §4's Bell account vs [P1] §7's** — never reconciled; flagged in the E-1 fix
   as open rather than asserted equivalent.
4. ~~**The $2\ln^2\!N$ robustness result** — derived here, not stated in [P1].~~ Stated in [P1] §6.1 (v0.8), 2026-09-02.
6. **The Adler race, after the diagnostic run** (see "The actualization law, tested"). In
   the plan's own order: (a) ~~the **inverse-coupling dwell** as a labelled positive control~~
   **Run 2026-09-02 at JB's request — it does not produce Born; it overshoots it.** Dwell
   $= 0.5\sqrt2/K_{\rm chan}$ (45° cell unchanged), nine angles, 300 trials: fitted exponent
   **$p = 3.81$ [3.50, 4.15]**, Born rejected at deviance 204 on nine cells, the curve
   more extreme than Born at every angle (0.99 at 20° against 0.88; 0.017 at 70° against
   0.117); the $dt/2$ check gives 4.55 [3.71, 5.71]. So the fixed dwell gives $p \approx
   1.5$, the inverse dwell $p \approx 3.8$, and the Born exponent lies *between* two
   choices of the criterion's amplitude dependence — the plan's own falsification row ("a
   universal Born candidate must not require one finely tuned numerical criterion")
   reached from both sides. **The tuned interpolation was then run: dwell $\propto K^{-1/4}$ gives $p = 2.00$
   [1.84, 2.16], Born deviance 4.7 on nine cells, every cell inside its Wilson interval.**
   A one-parameter amplitude-dependent criterion reproduces the Born curve at this budget;
   the parameter was chosen from the answer (one interpolation, one run), the sensitivity
   $dp/d\alpha \approx 2.3$ pins it to $\alpha = 0.25 \pm 0.07$, and nothing in the model
   fixes a quarter-power dwell — the plan's falsification row with the tuning quantified.
   Recorded as a lead for a *different* commitment rule (one that carried an effective
   $K^{-1/4}$ for a reason of its own would produce Born), not as support for this one.
   The $dt/2$ check's 45° outlier (0.385 on 200 trials) re-ran at 0.525 [0.469, 0.581] on
   300: a fluctuation. (b) the
   **lock-tolerance** sensitivity (the one criterion knob not yet turned) — **prediction
   fixed before the result was opened (2026-09-02; the 0.175 and 0.70 rad sweeps were
   running):** a locked clock's stationary phase spread under noise is $\sqrt{D/r}$, about
   0.24 rad at the central contraction rate, so its probability of sitting inside a fixed
   band scales as $K^{1/2}$ while the band is narrower than the spread and saturates once
   it is wider. If that is where the race's missing half power lives, the exponent should
   **rise** above 1.56 at tolerance 0.175 and **fall** toward the fastest-clock value near
   1.4 at 0.70; no movement, or movement the other way, kills the lead. **Scored
   (2026-09-02, nine angles, 200 trials):** tolerance 0.175 gives $p = 1.75$ [1.56, 1.96]
   with **25% of trials unresolved** — a rise, but confounded with commitment becoming
   harder, the same signature as long dwell and short pulse; tolerance 0.70 gives
   $p = 1.63$ [1.48, 1.80] with 0% unresolved — **no fall**, inside the frozen band's
   interval, at a band about three times the noise spread where the in-band probability
   should have saturated. Half the prediction held and was confounded; half failed. **The
   band-to-spread reading of the half power is not supported.** It survives a band wide
   enough to remove it, so it lives elsewhere. **Computed 2026-09-02 at JB's request
   (`entry_time_order_statistics.py`): it is the entry-time order statistics.** The
   deterministic skeleton — the package's drift and envelope, frozen grid, band and dwell,
   uniform random initial phases, *no noise* — gives $p = 1.52$ [1.51, 1.53] against the
   noisy race's 1.56 [1.44, 1.69]. Decomposition: a single central clock per channel,
   whose entry time is $h(\theta_0)/K$ in closed form, gives 1.13 (the rate's
   contribution is one power, sharpened by the spread of $\ln h$); the other fifteen
   clocks add only $\approx 0.4$, because the fastest of $N$ near-deterministic slides is
   set by the closest starting phase, an order statistic that gains logarithmically in $N$
   (the chance some clock starts inside the band is $1-(1-\varepsilon/\pi)^N$: 0.21 at
   $N=2$, 0.69 at $N=10$, matching the run), where a Poisson race would gain a full power.
   So "width times root rate" is $K^{1.1}$ from the slide times $K^{0.4}$ from the order
   statistic. **What a Born-producing race would need:** memoryless per-clock commitment,
   an exponential waiting time with hazard proportional to the local relaxation rate, so
   that hazards add across the tongue and width contributes its full power. The Adler
   slide is the opposite of memoryless. Read the other way, that requirement is the golden
   rule — a hazard linear in the site's coupling squared — i.e. what reading B already
   imports. Noise-assisted entry is then a small correction (1.52 → 1.56), not the source.
   **The fixed-area pulse sweep was run too (2026-09-02; $K\cdot T = 8$ on a ±6 support with
   32 clocks, three angles, 200 trials):** $T = 2, K = 4$ gives $p = 1.16$ [0.94, 1.40];
   $T = 4, K = 2$ gives 1.55 [1.30, 1.81] (the main sweep reproduced on the wider grid);
   $T = 8, K = 1$ gives 1.51 [1.27, 1.78]; $T = 16, K = 0.5$ is a grid-threshold artefact
   (a coupling of 0.17 admits no clock at 0.375 spacing). The channel ratio is not
   preserved at fixed area: a short strong pulse makes every eligible clock lock at once,
   the width gain saturates, and the race falls to the single-slide exponent. Time-window
   dependent from the fixed-area side as well; (c) ~~the **spectral controls** (Gaussian, Lorentzian, structured
   densities), which test whether the rate-weighted flux is what drives the events at all~~
   **Run 2026-09-02 (see "Spectral controls" below): the direct events move with the
   spectrum in the same order as both analytic comparators, so the mechanism is spectrally
   driven, and on every non-threshold spectrum the direct exponent sits about one half
   power above the eligible-count exponent — the same missing half;**
   (c′) **added 2026-09-02, the energy-tracking race** (see "The energy-tracking race"
   above): with commitment memoryless and its hazard linear in the energy a clock absorbs
   inside its tongue, under Adler's own power law and no inserted square, the same clocks
   and pulse give $p = 2.16$ [2.14, 2.19], within $\approx 0.02$ of Born at every angle,
   tracking the tongue flux; 2.09 under a stationary drive; 3.20 with P1's square; 1.70
   and 3.25 with square-root and squared hazards. The plan's mechanism works once
   commitment has the golden rule's structure. What remains owed for it: a physical
   argument that a site's first irreversibility is a Poisson process with hazard linear
   in its absorbed energy (E-16's continuum/thermalisation reading is the candidate),
   the exclusivity rule (still imposed), and production budget. (d) ~~the production
   question~~ **The validation-campaign pricing benchmark was run 2026-09-02 at JB's
   request** (`adler_two_channel_exploratory/pricing/`, outside the package; protocol from
   the ticket-07 pricing plan: four kernel components at three sizes, warmup plus three
   timed repeats, slowest rate × 1.5 contingency, one-hour wall and 2 GiB ceilings). All
   twelve cases completed clean in 2 493 s of the 3 600 s ceiling, digests identical
   across repeats, no warnings, no ceiling event; the package's `results/` tree and every
   source file verified unchanged. Component rates, all *priced*: stationary solve 481
   ns per space-time cell (1.59 GiB peak, 0.46 GiB under the ceiling); endpoint and sample
   construction 21.3 ns per endpoint observation; moving-band replay 136 µs per physical
   interval (two counters, collapsible); refinement comparison 52.4 ns per
   cluster-sample observation. **Stage prices:** S1 (dt/16, doubled space) 28 s; S2
   (dt/64, quadrupled) 136 s; S3 (dt/256, eightfold) 13.3 min; S4 (time quantile at
   dt/256) 13.3 min; M5 (moving-band probability, 64× master trials) 23.0 min; M6 (dt/16
   replay) 5.7 min; **M7 (time quantile, 1 024× master trials) `pricing_unresolved`**.
   Dependency paths: S1→S4 29.4 min at 1.59 GiB; M5→M6 28.7 min at 0.4 GiB; the six
   resolved stages sum to **58 min**; the worst-case sum is unresolved because M7 is. Why
   M7 is unresolved: its replay work is 128× the largest measured point against the
   plan's 16× rule (pricing it needs a ≥2 560-trial replay case, about 1.3 h on its own),
   and its 40 960-cluster comparison sits in a quadratic regime of
   `killed_diffusion.compare_refinement` — `_require_names` runs an O(n²) membership check
   on every `PairedSample` rebuild, so ns per observation is U-shaped (44 at 1 200
   clusters, 188 at 20 480) and no 16× ladder passes the 1.5× band; that is a finding for
   the package owner, not a change made here. Ambiguities in the plan and the choices
   made (empty-`results/` read as unchanged-`results/`; solve priced at the largest stage
   space, the conservative direction; S4 priced as a full stage) are listed in
   `PRICING_REPORT.md`. **A price is not an approval and not a sufficiency promise.** What
   it says: the intended-configuration validation campaign, short of M7, costs about an
   hour of compute at 1.6 GiB — affordable; whether running it can turn the ticket-07
   `numerical_no_result` green is a separate question the plan reserves for after a
   reviewed price. **JB authorized the campaign the same evening ("proceed with the
   validation plan without my input") and it was run overnight**
   (`adler_two_channel_exploratory/validation/`, outside the package; strictly serial,
   peak RSS 635 MiB against the 2 GiB cap JB's memory history made a hard constraint;
   60.5 min of a 2-hour budget; the package's `results/` tree and every source file
   verified unchanged; the reference S3 and S3b ladders re-run through the kernels first
   and reproducing the README's published numbers — oracle gap $1.2\times10^{-4}$, margin
   37, survival bound 0.04125, p35 bound 0.15290, p20 shift bound 0.17700 — which
   validates the mirror). **Outcome: both launched stages returned
   `numerical_no_result` under their predeclared rules; the stop rule halted every
   dependent stage; M7 was not launched; the frozen ticket-07 disposition does not
   change.** S1 (stationary probability, dt/16 at doubled space; 21 s): the refinement
   gate fired a repeated-reversal clause on one row (errors 0.0036 → 0.0043 → 0.0051,
   within noise) and, decisively, **0 of 9 probability rows fit** the allowance of
   0.00499 — bounds 0.010–0.028, i.e. 2.0–5.5× — for a structural reason: at 6 000
   walkers two standard errors alone are 0.007–0.012, so S1–S3 cannot meet the
   allowance whatever their bias. S2–S4 not run (stop rule). M5 (moving-band
   probability, 64× master trials, 2 560 trials × 3 regime clocks × 4 replicates on the
   intended $2^{-9}$ mesh; 59.8 min): the ladder gate fired on the added-resets mean
   (3.61 ± 0.08 against the cap of 3.0 frozen for the reference cell's granularity), and
   independently **3 of 4 probability rows exceed the allowance** by 1.7–2.3× (the fourth,
   survival shift at 0.45, fits at 0.89×); the p20 commit-time shift bound is 0.0836
   against the time allowance 0.0220, **3.8×** (down from 8× at the reference cell). M6
   not run (stop rule). Feeding the 17 intended-configuration rows into the package's own
   frozen disposition: the only blocker that clears is `no_evidence_at_intended_
   configuration`; the other five stand (moving-band no-result carried through; endpoint
   and audit envelopes exceed allowance; probability window empty — 78 admissible trials
   per cell against 2 406; time bounds fail at every trial count). Ambiguities and the
   choices made (three regime clocks rather than all 22 eligible, which would cost ~8 h;
   peak coupling 1.0; the frozen added-resets cap applied unchanged although it has no
   continuum limit) are listed in `VALIDATION_REPORT.md`. **What it means:** the endpoint
   dwell scheme's discretisation error at $dt = 2^{-9}$ is two to five times what the
   frozen production precision allows, now measured at the intended configuration rather
   than inferred from a reference cell; the production design as frozen is not feasible
   at this timestep, which is what ticket 07 concluded and is now confirmed. The
   diagnostic results of 2026-09-02 stay diagnostic. **Next boundary, JB's call:** the
   stationary shortfall is cheap to address — the SE floor needs ~16× the walkers, and
   S1 took 21 s — and the time rows are timestep-driven, with S3 at $dt/256$ priced at
   13 min; the moving-band rows need the $dt/16$ replay (M6, 5.7 min, halted by the stop
   rule) and a re-frozen added-resets cap, which is a plan change; a redesigned campaign
   along those lines is affordable but is a design decision the plan reserves for the
   sponsor. **JB made that decision on 2026-09-03 ("run the redesigned campaign with 16x
   walkers and the dt/16 replay") and it was run** (`validation/REDESIGN_REPORT.md`,
   `observations_redesign.json`; 44.7 min serial, peak RSS 509 MiB, memory scaling
   measured at 24 000 walkers before committing to 96 000; package unchanged by digest;
   reset cap applied as frozen and reported separately, not re-frozen). **Outcome: the gate
   is still red, but the redesign localised what remains.** S1 at 96 000 walkers: the
   refinement gate now *passes* (oracle margin 335, all procedure checks) and 3 of 9
   probability rows fit; the other six exceed the allowance by **1.1–1.7×** (bounds
   0.0052–0.0085 against 0.0050), down from 2.0–5.5× — so what is left at $dt/16$ is bias
   of about 1.4× the allowance, no longer the statistical floor. The stop rule halted S2–S4;
   the $dt/64$ stage that would test whether the bias falls with the timestep (the option
   table's $\sqrt{\text{factor}}$ projection would put it under the allowance) can run
   only on a further override; the bias falls by about 1.55× per halving of the step, the
   $\sqrt{dt}$ rate ticket 04 asserted, and the package's own `projected_bound` rule puts
   the worst stationary row at ≈ 0.0045 at $dt/256$, under the allowance — a projection,
   not evidence. The three stationary time rows already fit at $dt/16$ (0.5–0.8×). Of S1's
   27.6-minute construction phase, 25.7 minutes went to the package's O(walkers²)
   identity check, a finding for the package owner. M6, the $dt/16$ replay: **all four
   probability rows fit, but trivially** — they are exactly zero with zero standard error,
   no shift event in 480 audited histories, uninformative below about 0.002 rather than
   resolved; and the ladder gate fires twice — the added-resets mean is 14.1 ± 2.5 against the cap of
   3.0 frozen for the reference granularity (the count has no continuum limit and grows
   with the step count), and the p20 commit-time shift is **not converging**: 0.0055 at
   $4\,dt$ against 0.0283 at $dt$, growing under refinement past the whole-ladder allowance
   of 0.022. Disposition with the new rows: `numerical_no_result`, same five blockers;
   probability-admissible trials 824 (from 78 last night; needs 2 406); time admissible
   false. **What it means:** the stationary probability rows are within a factor of 1.4 of
   the production allowance and would be settled by one more refinement stage; the
   moving-band probability rows are settled at $dt/16$; the moving-band *time* observable
   diverges under refinement, which more trials will not fix and which is the substantive
   numerical finding of the two campaigns — the dwell-endpoint scheme's commit-time
   quantile is not converging in the audit at the intended cell, and the frozen
   reset-count cap cannot be used to judge it. **JB overrode the stop rule a second time
   ("override the stop rule and run S2 at 96k walkers") and S2 ran** (`validation/
   S2_REPORT.md`, `observations_s2.json`; 36.6 min serial; oracle phase peak 1 909 MiB,
   under the 2 GiB cap with 140 MiB to spare, construction 308 MiB; package unchanged by
   digest). **S2 at $dt/64$, quadrupled space, 96 000 walkers: gate pass (oracle margin
   943), 8 of 9 probability rows fit, all three time rows fit (0.3–0.5×), and the one
   miss is by 5%** — exit-count-upper at $x = 0.61$, bound 0.00523 against 0.00499. The
   bias fell at the $\sqrt{dt}$ rate from S1 (the S1 projections to $dt/64$ landed within
   a few percent of the S2 measurements, so the package's projection rule is accurate on
   this cell), and every S2 row projects under the allowance at $dt/256$, the worst at
   0.78×. S3 and S4 stopped under the frozen rule on that one row. **Disposition, stationary
   rows only** (S2 superseding S1): verdict *unresolved* rather than `numerical_no_result`
   — blockers reduced to the one envelope row and a probability window of 2 198
   admissible trials against 2 406 (91% of the target), time admissible. **Disposition,
   all intended rows** (S2 + M5 + M6): still `numerical_no_result`, and now entirely on
   the moving-band audit — M5's probability rows at $dt$ (survival shift at 0.80, 2.3×;
   commit probability, 2.3×), M5's p20 time shift 3.8×, and M6's gate (the frozen
   reset-count cap, and the p20 shift diverging under refinement), with M6's own
   probability rows trivially zero. **Where the three campaigns leave the package:** the
   stationary path is one further refinement from clearing — S3 at $dt/256$ with 96 000
   walkers, about an hour, projected to pass on every row — on a third override; the
   moving-band path is blocked by its time observable, which diverges under refinement
   in the audit, and by a reset-count cap frozen for a coarser cell, neither of which more
   trials or finer steps will fix. **JB took the third override on 2026-09-04 ("override
   the stop rule and run S3 at 96k walkers") and S3 ran** (`validation/S3_REPORT.md`,
   `observations_s3.json`; 67.3 min serial; oracle 4800 × 153 600 with the coarser
   2400 × 76 800 margin grid to stay under the cap, conservative by about 3×, peak
   1 536 MiB; construction 332 MiB; package unchanged by digest). **S3 at $dt/256$,
   eightfold space, 96 000 walkers: `numerical_no_result`, and not for the reason the
   projection allowed for.** The survival field converges cleanly (0.0028 → 0.0021 →
   0.0016 at one start) and all three time rows fit at 0.30–0.35× — the stationary time
   observable is admissible for the first time — but the exit-count fields do not
   converge: the upper-exit count drifts *upward* under refinement at two starts (0.0009
   → 0.0015 → 0.0018; 0.0014 → 0.0017 → 0.0019), with paired bootstrap errors of
   0.0002–0.0004 on the steps, so the gate's repeated-reversal clause fires on resolved
   increments, not noise; and three lower-exit rows sit over the allowance at 1.03×,
   1.12×, 1.28×. The three fields sum to one, so what remains at $dt/256$ is a systematic
   offset of about 0.002–0.003 in how exits are attributed to the two edges between the
   endpoint scheme and the oracle, which no longer falls with the timestep. The
   $\sqrt{dt}$ projection rule, checked against S3, **under-predicted every exit-count
   row** (worst 0.0019 projected against 0.0056 measured) while staying conservative for
   survival; it is not conservative for the edge-split observables on this cell. S4 not
   run (frozen rule). One observation for the package owner, not an action: the
   package's oracle-margin check differences the survival field only, so an oracle
   discretisation error confined to the exit fields would be invisible to it; whether
   the offset belongs to the endpoint scheme or the oracle is not established. **Where
   the campaigns leave the package:** the stationary path is no longer "one refinement
   away" — refinement has done what it can, and a residual edge-attribution offset
   remains whose origin is a numerics question inside the package; disposition with the
   stationary rows only, `numerical_no_result` with 1 477 admissible trials against
   2 406 and time admissible; with all intended rows, unchanged, the moving-band audit's
   rows still blocking by the larger factors (p20 3.8× and 2.8×, M5 probability rows
   2.3×). The decisions that remain are the sponsor's: whether the exit-count
   attribution and the commit-time quantile are production observables, or whether the
   production design is re-frozen on the observables that converge. **JB decided on
   2026-09-04: "Re-freeze the production design on survival and the time rows."**
   Implemented outside the package as a hashed manifest (`validation/REFROZEN_DESIGN.json`,
   digest `13f3bf1f…`, reproduced by `--check`; `REFREEZE_REPORT.md`; no run, no package
   change, package verified unchanged). Retained: stationary survival and the p35 time
   rows; moving-band commit-probability and survival-shift rows. Dropped, with the
   measured reasons quoted: the two exit-count fields (S3's edge-attribution offset that
   does not fall with $dt$) and the p20 commit-time shift (diverging under refinement in
   M6). **Not re-frozen, stated in the manifest and flagged:** the ladder gates, including
   the moving-band added-resets cap of 3.0, and the budget allowances. **Result on the
   re-frozen set:** the stationary path at $dt/256$ with 96 000 walkers **fits every
   allowance** — survival 0.53–0.65×, p35 0.30–0.35× — giving 5 704 admissible trials,
   which by the package's own power model buys an exponent half-width of **0.162**
   against the frozen target of 0.25. Yet the frozen disposition still reads
   `numerical_no_result` in every evidence set, for a bookkeeping reason rather than a
   measurement: `numerical_disposition` carries each ladder's *gate verdict* through, and
   every gate on record failed — S3's on a dropped observable (the upper exit count's
   reversals), the three moving-band gates on the un-re-frozen reset cap and the dropped
   p20 row. Two labelled hypotheticals, authorizing nothing: with the gates re-decided on
   the retained identities, the stationary-only set is **satisfied** with no blockers, and
   the all-intended set is *unresolved* on M5's retained probability shifts at the intended
   step (survival shift at 0.80, 2.34×; commit probability, 2.31×; survival shift at 0.60,
   1.71×), which the re-freeze does not touch and which the M5 ladder shows falling as
   $\sqrt{dt}$. Cheapest priced run that would clear them (proposal only): an M5-size
   moving-band ladder (2 560 trials × 3 clocks × 4 replicates) at $dt/16$ — every retained
   row projected under the allowance, worst 0.0044 — priced at **25 h** (16.6 h at the
   measured rate) and about 80 MiB; it would matter only if the moving-band gate were
   also re-frozen, since the reset cap fails at every step measured (3.6 at $dt$, 14.1 at
   $dt/16$). **The two decisions now left to the sponsor are both decisions, not runs:**
   whether to re-decide the two gate verdicts on the retained identities (for S3 this can
   be done from the recorded per-identity reasons; a fresh verdict object under a
   re-frozen contract would need S3 re-run, 67 min), and whether to buy the 25-hour
   moving-band ladder. **JB decided on 2026-09-04: "Re-decide the two gate verdicts on the
   retained identities."** Done as a derivation (`validation/REDECIDED_GATES.json`, digest
   `3f924ffc…`, chained to the re-freeze manifest and reproduced by `--check`;
   `REDECIDE_REPORT.md`; no run, no package change, package verified unchanged): the
   package's own per-identity clause function (`killed_diffusion._ladder_codes`, frozen
   caps, coverage 2) was applied to the recorded ladders restricted to the retained
   identities, after first confirming that applying it to *all* identities reproduces
   every recorded failing reason verbatim for all five ladders. The added-resets cap was
   set aside for these verdicts, as part of the decision and stated in the manifest, because
   it judges a diagnostic count with no continuum limit that is not a retained observable;
   its status is reported separately (it would still block M5 at 3.8 and M6 at 19.2), and
   it is *not* re-frozen, so a future moving-band ladder's gate carries it again unless the
   decision is extended. No clause was softened. **Result: every retained identity in every
   ladder passes all four clauses** — S3 (survival 0.0026–0.0076 against caps 0.09,
   p35 against 0.30, converging, at most one reversal), M5, M6 and the reference S3b — so
   all five ladders re-decide to *pass*. **Dispositions with the re-decided verdicts
   carried:** stationary only, **`satisfied`**, no blockers, 5 704 admissible trials, exponent
   half-width 0.162 against the target 0.25; all intended, **`unresolved`** — blocked only by
   M5's retained probability shifts at the intended step (survival shift at 0.80, 2.34×;
   commit probability, 2.31×; survival shift at 0.60, 1.71×), 439 admissible trials,
   half-width 0.585; reference plus intended, `unresolved` on the reference rows. **No
   evidence set is `numerical_no_result` any more.** What remains is one measurement, not a
   decision: the M5-size moving-band ladder at $dt/16$ (2 560 trials, 440 M physical
   intervals), priced at 25 h (16.6 h at the measured rate), about 80 MiB, every retained row
   projected under the allowance at 0.0044 worst; the records suggest nothing cheaper (fewer
   trials fail on SE, a coarser step with more trials costs more). Its gate would carry the
   reset cap again unless the decision is extended to it. The package's
   own next authorization boundary is whether to price the intended-configuration
   validation campaign. The diagnostic exponent's stability under $dt/2$ and $2N$ says the
   production direction is unlikely to be large; it does not say it is zero. None of (a)–(d)
   can be entered into the package's production estimate; all of them can be run through
   `adler_two_channel_exploratory/race_driver.py` at diagnostic budget in minutes.
5. ~~**Reading B and a v0.9 of [P1] — awaiting explicit go-ahead.**~~ **Applied 2026-09-02
   as [P1] v0.9** (see "Applied later the same day"), on JB's instruction to proceed with
   all three items, after 2a and 2b returned. Original entry retained below. JB's disposition
   2026-09-02, in session: "I guess B is the only choice." Grounds: the 576-state
   two-absorber model (`first_mark_two_absorber/`) enforces B by construction — the
   absorber's reversible excitation carries the full quantum, $E_e = \hbar\omega$, and what
   is split between arms is amplitude, so reading A is not representable in it; and QED
   agrees at the vertex (absorption is single-vertex and whole-quantum; sub-threshold
   excitation is reactive polarization, Theorem 2's slaved phase). Recorded as a *choice*,
   not a result: B is forced by writing a QED-like Hamiltonian, and an SED-like substrate
   with continuous energy accumulation and threshold firing would keep reading A, at the
   price of producing the whole-quantum vertex as emergent. Both readings pay the same
   nonlocality (P5). **What B costs, for the record:** no $\theta$, no exposed window;
   commitment $\propto |A_i|^2$ from any site at the golden-rule rate; Theorem 4 gives Born at
   any commit speed, so the exchange game is statistically inert and the Born weight
   enters through the linear rate law (P0+P1, as v0.6 already conceded); the SPAD/SNSPD
   and gap-ratio predictions (E-16, §8.6(vii)) dissolve; E-15/E-18/E-16's three unpinned
   terms are answered at once (share = local $|A|^2$; region = wherever amplitude is
   nonzero; discretisation = of the golden-rule race). What survives is the actualization
   question — which site's clock fires first, in one world, at the right rates — which is
   the SPAD review's owed "first actual mark" law and the question `adler_born_two_channel/`
   is built to ask (do noisy Adler clocks at amplitude-linear coupling give first-commitment
   frequencies $\propto$ coupling$^2$?). It has produced no number yet. **If B is adopted, [P1]
   needs a v0.9:** §6.1 and §5.4 restated without $\theta$ and the exposed window, Table 1's
   v0.8 row retired, §8.6(vii) withdrawn, and the claim boundary moved from "the game
   realizes the Born measure" to "the game actualizes one site among golden-rule-weighted
   candidates." Not applied: it changes the claim boundary, and the v0.8 corrections were
   made within reading A because that is the reading §6.1 was written in.

---

## The cut, tested: recoverability in the smallest exact model (open item 7, 2026-09-04)

**Sponsor's decision, 2026-09-04.** The Born-selection program is recorded as a negative
result (`NEGATIVE_RESULT.md`), and the work turns to Paper 2, refined by microscopic tests.
The first test is the recoverability crossover, run with predictions on record
(`heisenberg_cut_recoverability/PREDICTIONS.md`, results in `RESULTS.md` there).

**Uncertainty first.** The calculation is exact (single-excitation sector, eigendecomposition,
no integrator, no sampling). Its limits are scope: one linear absorber, a linear record
bath of N modes, rotating-wave capture, no competition among sites. Two of the seven
predictions were wrong in a stated detail, both mine: (i) the operational coupling-flip
was written down as if it were the in-principle reversal, and the no-bath calibration
refuted it (R = 0.044 off resonance); the observable was corrected to the partial
Loschmidt echo (system reversed, record channel untouched) before the corrected run,
and passes the calibration to 2×10⁻¹⁵; (ii) the leak exponent is 2Γ_eff t, not Γ_eff t,
because the echo leg leaks too.

**Findings.**
- *Location (P2-L) survives.* With a dense record channel (N = 256, recurrence time 40),
  recoverability leaks at Γ × (absorber occupation) per leg; the occupation is
  2K²/(Δ²+4K²) with half-point Δ = 2K, the resonant Rabi frequency; the measured
  rate-based midpoint is Δ/K = 1.3–2.0 across Γ = 0.05–1 and t = 3–10. The cut sits
  where the deficit-induced return rate κ_ret = Δ balances the coupling's
  population-transfer rate: κ_ret/K = 1 within a factor 1.6 if K is that rate, 2 if it is
  the matrix element. The midpoint read at fixed observation time drifts outward with Γt
  (1.7 → 5 over Γt = 0.15 → 10); the location is a statement about rates.
- *Width (P2-W) is out of scope for a linear absorber.* Relative width 0.8–1.6 in every
  run; ω cannot appear in a rotating-wave model and did not. Not a falsification: a scope
  restriction. The sharp layer w = K/ω, if real, belongs to a nonlinear self-sustaining
  absorber with counter-rotating terms. Stage-2 model fixed by this: a limit-cycle
  absorber, many-mode record channel, no RWA; test whether the width scales as K/ω.
  Prediction on record for stage 2: counter-rotating terms alone (quantum Rabi model)
  shift the location by the Bloch–Siegert amount ∝ K²/ω and do not sharpen; sharpening
  needs the limit cycle.
- *Completion (P2-C):* the ordering holds (capture reversible, record irreversible);
  recoverability degrades continuously, no switch at any occupation; sharpness not shown,
  same scope as the width.
- *A single record degree of freedom is not a cut.* N = 1 gives coherent exchange,
  oscillatory in g·t (the 576-state model's 0.83 → 0.09 → 0.25 is this); N = 4 leaks
  nothing; N = 16 recurs at t ≥ 3. The existing 576-state model cannot exhibit an
  irreversible step with one record qubit per absorber; a dense record channel is a
  physical requirement on the model and on detectors.
- *Bath memoryless* on the grid: R independent of bandwidth at fixed Γ to 0.001.

**Owed to Paper 2 (proposed, not applied):** define recoverability as the echo with the
environment untouched and distinguish the operational coupling-flip; state the location
as a rate balance; restrict w = K/ω to nonlinear absorbers; state the dense-record
requirement. Pending the sponsor's word.

**Correction to item 7, 2026-09-04, before the Paper 2 edits.** The width bullet above
misread w = K/ω as a relative width in κ_ret/K. Paper 2 §3.1 defines it as the layer's
extent in share (ΔE ≲ ħK ⇔ 1 − s ≲ K/ω), which in the deficit-rate variable is a
crossover of relative width order one — what the test measured. The width claim is
therefore consistent with the linear model, not out of scope; the open question is
sharpness (smooth crossover vs bifurcation) for a self-sustaining absorber, and stage 2
is redefined to test it (`heisenberg_cut_recoverability/PREDICTIONS_STAGE2.md`). Edit 3
applied in corrected form. The Paper 2 edits (v0.4) are applied at the sponsor's word,
2026-09-04.

**Item 7, stage 2 (2026-09-04, `heisenberg_cut_recoverability/STAGE2_RESULTS.md`).**
Predictions fixed first (`PREDICTIONS_STAGE2.md`); 7 of 8 confirmed, one numerical bound
wrong (the stored energy changes by up to 70 % per 0.1 in gain at the running onset, not
under 30 %; continuous with a kink as predicted). Findings: (S1) the carrier frequency
enters the recoverability crossover only as the Bloch–Siegert shift of its centre,
−(1.1–1.5)K²/ω, with the half-width unchanged to 2 % from ω/K = 64 down to 8 — ω belongs
in the share conversion and nowhere else; (S2) in Paper 2's own injected Stuart–Landau
model the leak-relevant stored energy sits at the field-set value F²/Δ² through the free
Hopf point and through the Hopf of the forced fixed point (slope 0.004) and rises with
slope 1.1 only beyond the winding onset near g = 0.355 — the three regimes slaved /
engaged / running appear in one energy observable, continuous with a kink, no jump, so a
self-sustaining absorber kinks the recoverability crossover rather than sharpening it,
and only the phase-winding observable switches; (S3) Paper 2's Figure 1 caption and
Appendix A misattribute the onset near g ≈ 0.35 to noise smearing — it is deterministic
(50 % onset 0.355 at D = 0, 0.352 at D = 10⁻⁴), the Adler estimate 0.1225 fails because
F/√g = 1 there, the true loss of lock is a Hopf bifurcation of the forced fixed point at
g = 0.241 — corrected in Paper 2 v0.4 (caption and Appendix A), beyond the four edits,
flagged to the sponsor; (S4) a record channel Γ_rec = 0.1 shifts the onset to 0.397 and
changes nothing else. Paper 2 v0.4 applied: the four edits (§3.1 location result; §3.2
what the width is a width of, corrected form; §4.1 echo definition; §4.1 dense-record
requirement), the §6.2 parenthetical, §8.6(v) (renumbered when §8.5 was added), the header note, and the S3 correction.
Proposed, not applied: a §4.1 refinement — the engaged regime leaves recoverability where
the field set it (slope 0.004), the energy handover is at the running onset and smooth.
Open, unchanged: the quantum self-sustaining absorber with a record channel (§9); the
location κ_ret/K = 1 is untestable in the forced sub-threshold oscillator because K is
set by the response (the §3.1 circularity), and stage 2 does not resolve it.

**Item 7, addendum (2026-09-04, later the same day).** At the sponsor's word, Paper 2 gains
§8.5 "Temperature as a dial on the record channel: a collapse test" (sponsor-originated:
heat writes the record; the count of configurations e^{S/k_B}, ~10⁴² for a 500 nm photon
thermalised at 300 K; Landauer prices the reversal at the photon's own energy — Paper 3
§4.2's triad with numbers). Predictions from the exact model: (i) retrieval efficiency vs
storage time collapses in Γ(T)·t if the record channel is memoryless (a non-collapse
measures the E-16 Markov ratio); (ii) the detuning crossover sits at |Δ| ≈ 2K and does not
move with temperature while Γ(T) ≪ K, moving inward by at most a factor 1.5 as Γ → K, never
outward. Stated honestly as coinciding with Markovian decoherence theory: the test cannot
discriminate the framework; the paper owes the prediction. Falsification list renumbered
§8.6. Six references added (Landauer 1961; Levstein et al. 1998; Pastawski et al. 2000;
Equall et al. 1995; Könz et al. 2003; Hackermüller et al. 2004).

**Item 7, addendum 2 (2026-09-04).** At the sponsor's word, Paper 2 §2 gains a lineage
paragraph placing the paper against the decoherence programme's treatment of the cut
(Zeh 1970; Zurek 1981, 1982, 2003, 2009; Joos & Zeh 1985; Tegmark 1993; Brune et al. 1996;
Ollivier et al. 2004; Schlosshauer 2004; Schlosshauer & Camilleri 2008; Camilleri &
Schlosshauer 2015; Bell 1990), and states what remains distinctively the paper's after
v0.4: recoverability ending in principle rather than for all practical purposes (the
§4.1 random-reference argument) and a coupling-set location with a computable share
width; the location and crossover results are decoherence-compatible, and the
single-outcome claim is the companion's negative result. §2 item (3), which still said
the lock's statistics are "provably Born under stated premises", gets a one-line v0.4
qualification to Paper 1 v0.9 / NEGATIVE_RESULT.md — an inconsistency the negative
result had left standing. Six references added.
