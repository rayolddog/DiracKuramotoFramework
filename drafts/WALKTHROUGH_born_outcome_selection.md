# How One Electron Wins: The Born Rule as a Fair Game

### A plain-language walkthrough of the outcome-selection results (2026-07-20)

*This document ties together the full derivation chain from the 2026-07-20 session in ordinary language. Technical backup: `NOTE_born_gamblers_ruin.md`, `DERIVATION_slaved_phase_subthreshold.md`, `DERIVATION_vacuum_noise_correlation.md`, `DERIVATION_bell_pair_joint_game.md`. Every specialist term is glossed where it first appears; a short glossary closes the document.*

---

## 1. The question

Quantum mechanics has one rule it never explains: the **Born rule**. It says that if a particle's wave has amplitude $A$ at some location, the *probability* of finding the particle there is $A^2$ — the amplitude *squared*. Every textbook states it; none derives it. It is pure axiom, and it is where all the probability in quantum mechanics enters.

Notice that the rule is strange twice over. First, why probability at all — what is being decided, and by what? Second, why the *square*? The wave itself is linear; detectors couple to it linearly; yet the statistics come out quadratic.

The claim of this work: in the DK framework, both strangenesses dissolve. The probability comes from noise (real, physical noise in the detector and vacuum), and the squaring comes from energy (the elementary fact that the energy of an oscillator is the square of its swing). The Born rule stops being an axiom and becomes a theorem about a **fair game** — with the fairness itself derived, not assumed.

## 2. The cast of characters

Picture a single photon arriving at a detector — say the screen behind a double slit.

- **The photon** is a real wave, spread across the whole illuminated patch of the screen. It is not a little ball that has secretly already chosen its landing spot. Its amplitude varies across the patch: high at bright fringes, low at dim ones.
- **The detector electrons** — billions of them across the patch — are bound to atoms. Each one is a tiny oscillator with a natural frequency (set by its orbital energy gap) and, crucially, its own internal *clock* (its phase). Before the photon arrives, these clocks are unsynchronized: each electron ticks on its own, with no phase relationship to its neighbors.
- **The vacuum** contributes a faint, ever-present random jitter — small, structureless, carrying no information about the outcome. It is the dice, not the decision.

## 3. Step one: everyone gets tipped (the MRI step)

When the photon wave washes over the patch, it drives *every* electron whose frequency it matches — exactly like an RF pulse in MRI tips nuclear spins. The analogy is precise, not decorative:

- In MRI, the RF pulse tips each spin away from equilibrium by an angle proportional to the local RF field strength, and stamps the pulse's own phase onto the spin's precession.
- Here, the photon tips each electron into oscillation with a swing proportional to the *local wave amplitude* $A_i$, and stamps the wave's phase onto that oscillation.

Now the first key fact, borrowed from freshman mechanics: **the energy stored in an oscillator is proportional to the square of its swing.** So after this "tipping" stage, electron $i$ holds a little parcel of energy

$$e_i \propto A_i^2.$$

*This is where the squaring enters — and it enters as physics, not as an axiom.* The same fact shows up in NMR (a small tip angle $\theta$ excites with probability $\sim \theta^2$) and in optics (field energy density is amplitude squared). Nothing quantum has been assumed; a classical antenna engineer would write the same equation.

At this point nothing has been *decided*. The photon's one quantum of energy is smeared across billions of electrons in exact proportion to the brightness pattern $A^2$. The measurement problem, stated honestly, is: how does this smear become *one* electron holding *all* of it — and why with probability proportional to $A_i^2$?

## 4. Step two: the tug-of-war (Pearle's casino)

The framework's answer: the tipped electrons play a long, noisy **tug-of-war** for the quantum. Energy sloshes between sites in many small random exchanges, driven by the vacuum jitter, until one electron accumulates the whole quantum — at which point it *locks* (crosses the on-shell threshold, becomes a real excitation, and triggers the detector's avalanche — the "click"). The losers relax back to equilibrium. One winner, discrete outcome, single world.

Here is the beautiful old theorem that makes this work, and it comes from gambling. Imagine a casino game among $N$ players, where player $i$ starts with $e_i$ chips and the game is **fair** — every exchange is an even coin flip, no player systematically favored. Play until one player holds everything. Then a classical theorem (the *optional stopping theorem* for *martingales* — a martingale is just the mathematician's word for a fair game, one with zero built-in drift) says:

$$P(\text{player } i \text{ wins everything}) = \frac{e_i}{\text{total chips}} \quad \textbf{exactly.}$$

Your chance of walking away with the pot equals your share of the chips. Not approximately — exactly, for any number of players, any starting distribution.

Apply it here: the chips are the tip energies $e_i \propto A_i^2$. If the tug-of-war is fair,

$$P(\text{electron } i \text{ clicks}) = \frac{A_i^2}{\sum_j A_j^2} \quad \text{— the Born rule.}$$

**Credit where due:** this gambler's-ruin route to Born statistics is Philip Pearle's insight, from the 1970s, and it underlies the modern "collapse models" (CSL). What those models could never say is *why the game is fair* — they engineer the noise to have exactly the fairness property, by hand. Everything new in our work is about removing that "by hand."

## 5. Why the game is fair: four objections, four answers

A fair game is a knife-edge. Our own simulations showed brutally that plausible-looking alternatives fail: if the winner is just "whoever has the biggest instantaneous pull," the bright site wins far too often; if the noise has the wrong strength profile, the game drifts. Fairness must be *forced* by physics, or the whole story collapses. Four objections, each answered:

### Objection 1: "The rich will cheat." (rich-get-richer)

A leader accumulating energy might become a stronger player — pulling energy in faster because it has more. Winner-take-all systems (laser mode competition) usually behave exactly this way, and it destroys Born statistics.

**Answer: below the threshold, you have no clock of your own.** To systematically pull energy from a neighbor, an oscillator needs to *hold a steady phase relationship* with it — you can only siphon from someone you're in step with. But an electron holding only *part* of the quantum is not a real excitation: there is no orbital state at 0.7 of the gap energy (this was JB's key point — the discreteness of atomic levels means there is no partial credit). Such a "virtual" excitation is a *forced* oscillation: its phase is not its own; it is **slaved** to the driving field, like a cork bobbing on a wave rather than a swimmer. We proved this in the oscillator mathematics: below threshold the phase always relaxes to a value dictated by the drive — it never runs free, so it can never entrain a neighbor, so the leader has no lever to cheat with. A free-running clock — the thing that could bias the game — emerges only at the moment the full quantum is assembled. The barrier that creates the discreteness is the same barrier that enforces the fairness.

(MRI echo: a spin only precesses on its own after it's been *really* tipped; and the reason a partial excitation can't "bank" its winnings is the same reason you can't half-absorb an RF quantum into a spin transition.)

### Objection 2: "The dice might be loaded." (noise scaling)

Fairness in the casino theorem requires the coin flips to be even. In physics terms: the random energy kicks from the vacuum must have exactly the right *strength profile*. If the noise kicks every site with equal strength regardless of holdings, the leaders are favored (we proved this — it's a short calculation). If the noise kicks proportional to holdings, the game actively equalizes — also wrong.

**Answer: the framework's own coupling law lands exactly on the fair point.** The framework has always postulated that couplings are *amplitude-linear* — forces act on the wave's amplitude, not its energy. A noise force acting on amplitude does work proportional to $(\text{amplitude}) = \sqrt{e}$, which makes the energy jitter's *variance* proportional to $e$ itself. Run that through the stochastic calculus (Itô's lemma — the chain rule for random processes) and the drift of every player's *share* comes out **identically zero**. Amplitude-linear coupling *is* the fair-coin condition. The single postulate that produced the Born rule's *form* in the framework's old golden-rule argument turns out to also produce the Born rule's *probability*. One assumption, both jobs — that convergence is the strongest internal evidence that the picture is right.

### Objection 3: "The players might collude." (correlated noise)

The fairness theorem needs each site's noise to be *independent*. But vacuum fluctuations are correlated over about half a wavelength — neighboring electrons feel partly the *same* jitter. We computed what shared noise does: it is genuinely dangerous (with fully shared noise, the brightest site wins essentially always — we saw it in simulation, and the drift formula shows why).

**Answer: in any real detector, the dangerous noise is a millionth of the total.** The noise that actually drives the tug-of-war in a solid detector is dominated by *local* scattering — phonons, carrier collisions — with correlation lengths of nanometers, utterly uncorrelated between competing sites. The wavelength-scale-correlated (radiative) component is weaker by a factor of about $10^{-6}$. The deviation from Born scales linearly with that correlated fraction (proved and simulated), so the residual bias is one part in ten million. The protection is the *locality of detector noise* — an honest physical fact, not a convenient assumption. (Where the protection fails — free-space atom arrays whose only noise *is* radiative — we predict real deviations. That's a feature: it's a test. See §7.)

### Objection 4: "The finish line might distort the race." (commitment)

How exactly does the game end? Here the framework's detector taxonomy pays off, because there are two cases, and both come out exact:

- **Discrete-level absorbers** (atoms): there are no final states below the full quantum, so the game *must* run to completion — first player to assemble everything wins. That is precisely the casino theorem's setting: exact Born.
- **Continuum absorbers** (silicon, photographic grain): final states exist at every energy, so the detector doesn't wait — registration fires *during* the game, at a rate proportional to each site's current holdings (this proportionality is just the golden rule, the most standard rate law in physics). And here a small theorem gives an exact result: if the pick probability at the moment of firing equals the share (which is what a proportional rate means), and the shares are a fair game, then the outcome probability equals the *initial* share — **regardless of when the firing happens**. Fast detector, slow detector, doesn't matter: exact Born either way. It's a raffle where your tickets are your chips, drawn at a random moment of a fair game — your odds are your original stake, always.

We verified all four answers in simulation, including the failure modes: wrong noise scaling breaks Born visibly, shared noise breaks it dramatically, nonlinear registration rates break it in exactly the direction the theorems predict. The fairness is a knife-edge — and the physics sits on the edge, held there by identifiable laws rather than by tuning. That falsifiable rigidity is what makes this feel like a real mechanism rather than a just-so story.

## 6. Two casinos, one bankroll: the Bell experiment

The hardest test of any outcome-selection story is the entangled pair. Two photons, two distant stations, analyzer angles $a$ and $b$; quantum mechanics predicts correlations ($\cos 2(a-b)$) that provably cannot come from any pair of *independent* local games.

The framework's account, run through the game machinery:

- At each station, the local wave is unpolarized — fifty-fifty in every basis, carrying **no information about the angles**. Each station's local fair game therefore produces the correct *marginals* (50/50) and nothing more. This is exactly right: local statistics in a Bell experiment are pure coin flips.
- The correlation lives in the **joint** structure — the pair was born as a single substrate excitation, and the two waves share a phase thread through the substrate. This shared structure is the framework's *unhidden variable*: perfectly real, just ignored by local bookkeeping. (Never "hidden" — that word buys objections that don't apply.)
- Whichever station's game **locks first** (ordered by the framework's preferred time-slicing — the cosmic/CMB frame the framework already carries for other reasons) triggers a *resync* of the shared thread: the joint amplitude re-forms around the outcome — evolution, not collapse — which physically resets the far station's game to the *conditional* odds. The far station's fair game then completes on those.
- Marginal (exact, by fairness) × conditional (exact, same reason) = the quantum joint probabilities. And because that decomposition holds *whichever* station goes first, the statistics are order-independent — which is also exactly the no-signaling requirement.

We simulated the whole thing: the game reproduces the maximal quantum Bell violation ($S = 2\sqrt2 = 2.83$ against the classical limit of 2), no-signaling holds, and the result is identical whether A or B locks first. One new quantitative handle emerged: if the resync were *imperfect* — fidelity $\eta$ — the violation would be $S = 2\sqrt2\,\eta$. Existing experiments therefore *measure* the substrate's resync fidelity: $\eta \gtrsim 0.99$ over hundred-kilometer scales.

Honesty box: this part is a **consistency proof, not a derivation of entanglement**. The game machinery composes perfectly with the framework's entanglement ontology, but that the substrate carries the joint amplitude and resyncs it faithfully is postulated. The nonlocality is not explained away — it is located, openly, in the substrate and the preferred frame, which is where this framework has always said it lives. Deriving the resync dynamics (and why $\eta = 1$) is the top remaining problem.

## 7. What would prove this wrong (or right)

A mechanism, unlike an axiom, has failure modes — and each of the four fairness conditions marks a place where Born statistics should *bend* if the condition is physically broken:

1. **Pre-cohered detectors.** Fairness rests on the detector electrons' clocks being unsynchronized. An absorber ensemble *prepared* with mutual phase coherence (Dicke/superradiant-style preparation) should show non-Born statistics.
2. **Nonlinear registration.** The continuum-absorber result requires the registration rate to be *linear* in occupation. Any detector whose commitment needs a cooperative two-carrier step (effective rate $\propto$ share$^2$) should over-select bright sites; a saturating detector should under-select them — with the deviation largest for fast registration. Surveying real detector types for such nonlinearity is an open task.
3. **Radiative-noise absorbers.** Sub-wavelength atom arrays, where all the noise is the shared radiative kind, should deviate substantially from per-site Born weighting — with a distinctive signature: the deviation's *sign flips* with the polarization of the light relative to the array axis. (Caution: this sits close to known collective sub/superradiance physics; the literature check must precede any novelty claim.)
4. **The resync knob.** Any physical degradation of the substrate thread between Bell stations would pull $S$ below the quantum value at fixed local visibility. All data to date say it doesn't degrade — which is itself informative (it pushes the framework toward a global, non-propagating resync).

One retraction from the same session, for the record: an earlier estimate suggested broadband solid-state detectors might show percent-level deviations from a soft locking threshold. The rate-linearity theorem killed that prediction — properly modeled, broadband detectors give exact Born. The framework is *more* consistent with observation than our own first estimate was.

## 8. So: is this a derivation of the Born rule?

The honest answer has three layers.

**In the strongest sense — probability from nothing — no, and nothing ever will be.** You cannot derive probabilities from a theory that contains no probabilistic ingredient; something must break ties. Every "derivation of the Born rule" in the literature — Gleason's theorem, Everettian decision theory, Zurek's envariance, Bohmian typicality — is a derivation *from premises*, and the game is really about how physical, independent, and few the premises are.

**In the sense that matters — Born as a theorem from physical premises rather than an axiom about outcomes — yes.** The premises are: (i) detector excitation is energy accumulation in driven oscillators (squaring from energetics); (ii) couplings are amplitude-linear (fairness from Itô — and this postulate was already in the framework doing other work, not added for the occasion); (iii) detector clocks start incoherent and dominant detector noise is local (fairness protected — both are facts about real detectors, checkable and checked); (iv) registration is threshold-complete or rate-linear (the two detector classes — golden-rule physics). From these, the Born rule follows *exactly*, by theorems, with the deviations from each premise-failure computed and testable. Nothing in the premises mentions probability-of-outcomes; the $|A|^2$ never has to be put in by hand.

**And in one specific respect it is stronger than the axiom it replaces:** it predicts the *conditions under which Born fails* (§7). An axiom can't do that. That is the practical content of calling this a mechanism.

What it is *not*: a derivation of quantum mechanics itself. The substrate ontology, the wave dynamics, the entangled joint amplitudes, the resync — all framework postulates. The claim is precisely bounded: **given the framework's ontology, the measurement postulate is redundant** — outcomes, definiteness, Born weights, and Bell correlations all follow from the dynamics plus noise.

## 9. The one-paragraph version

A photon spreads its energy over many detector electrons in proportion to brightness (amplitude squared — that's just oscillator energetics). The electrons then play a noisy tug-of-war for the quantum. The game is provably fair — the leader can't cheat because a partial excitation has no clock of its own; the dice can't cheat because amplitude-linear coupling gives the noise exactly the fair-game profile; the players can't collude because detector noise is local; the finish line can't distort because registration rates are linear. And a fair game, by a classical theorem, hands the pot to each player with probability equal to their share of the chips. The shares are amplitude-squared. That is the Born rule — as the bookkeeping of a fair fight, in one world, with testable ways to make the fight unfair.

---

## Glossary

**Born rule** — QM's probability axiom: P = |amplitude|². • **Amplitude** — the strength of the wave at a point (its "swing"). • **Martingale** — a stochastic process with zero drift; the mathematics of a fair game. • **Optional stopping theorem** — for a fair game run to a stopping condition, expected final holdings = initial holdings; hence P(win all) = initial share. • **On-shell / off-shell** — a real, self-sustaining excitation (full quantum, energy-conservation-satisfying) vs. a virtual, borrowed-energy one. • **Slaved phase** — the phase of a driven-below-threshold oscillator, dictated by the drive rather than free-running; contrast a *limit cycle* (self-sustained oscillation with a free phase). • **Adler equation** — the standard equation for how a free-running oscillator's phase locks to a drive; applies only above threshold. • **Itô's lemma** — chain rule for stochastic processes; adds a curvature term that is where the fairness calculation lives. • **Golden rule (Fermi's)** — standard first-order rate law: transition rate proportional to occupation and density of final states. • **CSL / collapse models** — modified-QM theories (Pearle, Ghirardi et al.) that add noise engineered to produce Born outcomes; our work replaces "engineered" with "derived." • **Unhidden variable** — the framework's term for the real, physical detector–substrate entanglement carrying Bell correlations; not a local hidden variable. • **Preferred foliation** — the framework's cosmic time-slicing (CMB frame), which orders the two locks in a Bell experiment. • **Resync fidelity η** — how faithfully the substrate updates the far wing after the first lock; Bell violation requires η > 1/√2 ≈ 0.71; experiment says η ≳ 0.99. • **Dicke sub/superradiance** — modified collective emission/absorption when emitters within a wavelength share vacuum modes; the physics behind our atom-array prediction.
