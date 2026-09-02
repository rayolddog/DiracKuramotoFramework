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

**Totals: 18 items · 6 applied · 12 pending disposition.**

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

| **E-16** | **HIGH** *(raised 2026-09-02 after computing the ladder — see the E-16 result section; severity is provisional on the two flagged uncertainties, either of which could return it to MED)* | [P1] §6.1 (ladder); §4 (noise origin); §5.4 | **Cooling inverts the ladder's top rung, and §6.1 is computed only at room temperature.** *(Rewritten 2026-09-02 — the first version of this item named the wrong failure; see the correction paragraph below.)* §4 writes P2's noise as one increment from "the wave packets of the detector's other bound charges *and* the vacuum/environment field," conflating a **thermal** source with a **zero-point** one. The asymmetry is real and large: the free-field thermal occupation at optical frequency is already negligible at room temperature ($\hbar\omega/k_BT \approx 97$ at $\lambda = 500\,$nm, $T = 300$ K, giving $n \sim 10^{-42}$ — which is just [P1]'s own fairness window $\hbar\omega \gg k_BT$), while the near-surface noise that actually drives the game is set by the material's dissipation and *is* thermal. P3(b) gives both channels: $\Gamma_{\rm loc} \sim 10^{13}$–$10^{14}\,\mathrm{s^{-1}}$ (phonon, carrier–carrier — thermal) against $\Gamma_{\rm rad} \sim 10^{8}\,\mathrm{s^{-1}}$ (radiative/vacuum — not thermal), five to six orders apart. Freeze the phonons out entirely and $\tau_c$ runs from tens of fs to ~10 ns. | **Accept. JB-originated 2026-09-02** (asking whether temperature affects the vacuum as it affects matter). **The correction:** that does *not* break whiteness, because $\tau_{\rm game} \sim 2\ln^2\!N/\Gamma$ scales as $1/\Gamma$ **too** — both middle rungs stretch together and the separation $\tau_{\rm game}/\tau_c = 2\ln^2\!N$ is invariant, whichever channel dominates. The first version of this item claimed cryogenic operation endangers whiteness; that was wrong. **The actual risk is the top rung.** $\tau_{\rm commit}$ (ns–$\mu$s) is set by avalanche physics and readout electronics and does *not* scale with $\Gamma$, so cooling pushes $\tau_{\rm game}$ **up toward it**: a two-order drop in $\Gamma$ takes $\tau_{\rm game}$ from ~80 ps to ~8 ns, i.e. into the commit window. That matters because v0.7's entire restructuring rests on this rung — commitment being slow is why first passage settles the outcome before any commit-rate law acts, and why Theorems 4–5 were demoted from operative mechanism to robustness rider (§5.4). **Invert the rung and the fast-commit reading v0.7 withdrew comes back.** §6.1's ladder is computed only for a room-temperature silicon SPAD, while §8 discusses SNSPDs, which run at 1–4 K. Recompute the ladder for the cryogenic families §8 actually names, and state the $\Gamma$-invariance of the middle separation while doing so — it is a free robustness result the paper currently does not claim. |
| **E-17** | LOW | [P1] §2 (notation/premises) or §6.1 | **Selection and registration are spatially orthogonal, and the paper relies on this silently.** The Born pattern varies over the detector face: $|A_i|^2$ lives in $xy$, and the selection game is a competition among sites at different $(x_i, y_i)$, decided by *differences* between them. Registration is an out-of-plane process — the avalanche develops along $z$, driven by the junction bias. A spatially uniform $z$ field is invariant under $xy$ translation and therefore **structurally incapable** of biasing which site wins: it cannot distinguish site $i$ from site $j$. Stage 2 and Stage 3 are thus not merely sequential in time but orthogonal in space, and the field that powers registration is geometrically barred from touching selection. [P1] treats sites as an abstract index $i$ with no geometry beyond the spacing $d$, yet the geometry it does use is already in-plane (P3(b)'s $d \gg \ell$; §8's polarization signature stated "relative to the **array axis**"). | **JB-originated 2026-09-02; accept.** State it in §2 or §6.1 — one or two sentences. It cheaply answers a referee objection that would otherwise need magnitude estimates ("your SPAD has hundreds of volts across it; how is that not a bias?"), answering by symmetry instead. **Residual channel, correctly located:** not the bias but its $xy$ **non-uniformity** — guard rings, edge effects, doping variation, field crowding at the active-area perimeter — plausibly acting through Stark-shifted detunings to make capture site-dependent. That is the tractable question for a real device: not "is there a field" (yes, large) but "how flat is it across the active area." **Correction recorded:** `window_tests.py` Test B's catastrophic common-mode result ("bright wins 100%") applies to *fluctuating* common-mode noise, where multiplicative $\sqrt e$ coupling hands the leader a proportionally larger increment each step. It does not describe a *static* common bias, and was misapplied to one in session before JB's geometric argument corrected it. |
| **E-18** | **MED–HIGH** | [P1] §6.1 (parenthetical after the $\tau_{\rm game}$ estimate) | **A dismissal that E-15 invalidates.** §6.1 estimates $\tau_{\rm game} \sim 2\ln^2\!N/\Gamma$ for "$N \sim 5\times10^{10}$ sites in the diffraction volume" and then sets the question aside: *"(Only $\ln^2 N$ enters; **the answer is insensitive to the coarse-graining of 'sites'**.)"* That was fair while $N$ merely set the game duration. It is not fair now. E-15 showed the whiteness separation **is** $2\ln^2\!N$ — the same quantity — and that the failure when whiteness lapses is *total* (shares collapse to $1/N$) rather than graceful. So the definition of a "site," and more sharply the size of the region within which sites actually compete, becomes a physical parameter the Born result depends on. Range across plausible choices: $2\ln^2\!N$ = 1212 at $5\times10^{10}$, 382 at $10^6$, 95 at $10^3$, 42 at $10^2$, 11 at $N=10$ — a factor of ~29, against measured behaviour that is safe at persistence 0.18 and broken at 3.5. **JB-originated 2026-09-02** (from the medical-imaging framing: a detection event draws from a finite aperture, and no screen resolves single atoms). | **Accept; log the dependency, do not yet claim a defect.** Two sub-questions, both answerable: (i) what physically bounds the competing region — the diffraction volume (§6.1's implicit choice), the distance energy can hop through the common field during $\tau_{\rm game}$, or the pattern scale? (ii) Does $N$ in the ladder mean illuminated sites or sites-per-competing-region? These are the same "what is the discrete exchange model a discretisation *of*" question that blocks E-15, reached from the geometry side. **Note also what does *not* help:** coarse-graining cannot rescue the $1/N$ collapse, since uniform is scale-invariant — binning $N$ uniform sites into $P$ pixels gives uniform over $P$ pixels. Aperture changes the margin, it does not restore an erased pattern. |

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

**OWED: recompute silicon under the same definition.** The definition must be applied where
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
2. **OWED — recompute the silicon ladder under the first-irreversibility definition of
   commitment** (E-16, uncertainty #2). §6.1's ns–$\mu$s is the avalanche-and-quench cycle,
   not the point of no return. If the true figure is ps–ns, §6.1's "two to four orders to
   spare at every rung" needs restating for its own detector, and the safe case is not as
   safe as the paper says. **This is the item most likely to be quietly skipped, because it
   only costs the theory** — flagged here for that reason.
3. **Small-$N$ whiteness / frozen speckle** — see above. The two-site knife-edge runs sit
   at $\approx 1$ correlation time of game duration, i.e. in the static-speckle regime, while
   assuming white noise. Needs a check of which conclusions depend on $N=2$, and ideally a
   re-run with coloured noise at the sims' own $\tau_c/\tau_{\rm game}$ ratio to confirm the
   knife-edge results are not artefacts of the whiteness assumption at small $N$.
3. **EQUATIONS.md §4's Bell account vs [P1] §7's** — never reconciled; flagged in the E-1 fix
   as open rather than asserted equivalent.
4. **The $2\ln^2\!N$ robustness result** — derived here, not stated in [P1].
