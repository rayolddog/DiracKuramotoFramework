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

**Totals: 14 items · 6 applied · 8 pending disposition.**

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

| **E-15** | **MED–HIGH** | [P1] Theorem 1 proof; Appendix D | **The stochastic calculus is chosen but never justified, and the physical noise selects the other one.** Theorem 1's proof applies **Itô's lemma** to $s_i = e_i/\sum_j e_j$; Appendix D integrates by **Euler–Maruyama**, which is Itô by construction. Neither says why Itô rather than Stratonovich. For multiplicative noise the choice is physical, not cosmetic. By **Wong–Zakai**, noise of any finite correlation time converges as $\tau_c \to 0$ to the *Stratonovich* equation, never the Itô one, and for $a(e) = \sqrt e$ the two differ by a drift $\sigma^2 a a'/2 = \sigma^2/4$ — identical on every site, hence share-**equalising** (a leader gains proportionally less from an equal absolute increment), which is precisely the failure mode Theorem 1's converse attributes to multiplicative noise. Physical detector noise has $\tau_c \sim 10$–$70\,$fs and is therefore colored, so it selects Stratonovich. The question is not whether correlation time perturbs Born but whether the paper's Itô baseline is the small-$\tau_c$ limit of the physical process at all. | **Likely resolved by a premise the paper already has, but does not invoke here.** The $\sigma^2/4$ drift requires the *total* to grow; a closed pot forbids it. v0.7's **P4(a)** makes the pot closed ($\sum_i e_i = \hbar\omega$), added for exclusivity. If conservation restores Born under colored noise, P4(a) does double duty and Theorem 1 gains the justification it currently lacks — worth stating explicitly either way, since a reader who notices the Itô choice has no answer in the text. Numerical check: `born_selection_sims/colored_noise_knife_edge.py`. |

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

**What this does not settle.** The physical dynamics is exchange-type — energy *moved*
between sites, as in `gambler_ruin_born3.py`'s $\delta = \pm\,\mathrm{step}\cdot\min(e_i,e_j)$
— not independent-per-site noise with a projection. A genuine exchange formulation may be
immune, since there the increment is antisymmetric in $(i,j)$ by construction and no
common-mode drift can exist at all. That test has **not** been run, and until it is, the
right statement is: *the knife-edge as verified in the paper's own engine is calculus-
sensitive, and the obvious repair does not work.*

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
2. **Small-$N$ whiteness / frozen speckle** — see above. The two-site knife-edge runs sit
   at $\approx 1$ correlation time of game duration, i.e. in the static-speckle regime, while
   assuming white noise. Needs a check of which conclusions depend on $N=2$, and ideally a
   re-run with coloured noise at the sims' own $\tau_c/\tau_{\rm game}$ ratio to confirm the
   knife-edge results are not artefacts of the whiteness assumption at small $N$.
3. **EQUATIONS.md §4's Bell account vs [P1] §7's** — never reconciled; flagged in the E-1 fix
   as open rather than asserted equivalent.
4. **The $2\ln^2\!N$ robustness result** — derived here, not stated in [P1].
