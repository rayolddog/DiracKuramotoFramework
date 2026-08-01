# One Mechanism at Two Scales: The Dirac–Kuramoto Framework for Persistence, Measurement, and the Classical–Quantum Boundary

**Claude Fable 5 (Anthropic) and John M. Bramble, MD**

*[DRAFT v0.1 — 2026-07-31. Skeleton draft from `PAPER3_OUTLINE_dk_framework.md`: full
prose for the three JB-confirmed elements (§1 spine; §2 framework statement with the
register/superposition package; §3 ladder), source-mapped stubs for §§4–7. Relationship
to the main paper (`current_revision_DK_paper.md` v8, "The Many Clocks Interpretation"):
JB DECIDED 2026-07-31 — **Paper 3 completely supersedes it**. [MCI] stays frozen in the
repo as the provenance record (the FoP-declined canonical version and its review
history); everything living moves here. JB's explicit keep-list from [MCI]: (a) the
experimental-test ideas — the linewidth-dependent gravitational Bell test with its
honestly-isolated H′ postulate and the Appendix-C cancellation null, the parameter
space/falsification analysis, and the Bose–Marletto–Vedral ontology discriminator
(→ §6); (b) the Many-Worlds-versus-Many-Clocks contrast — [MCI] carries its first
statement — including the trade-not-conquest framing and the interpretation's name
(→ §7, and the name question in the title decision). Byline order per standing
convention, sponsor's decision before any circulation.]*

**Contributions.** Claude Fable 5 (Anthropic) performed the formalization, the manuscript
prose, and the literature work. John M. Bramble, MD supplied the physical framing and
research direction — including the spine, the ladder confirmation, the register package,
and the history and frame-rotation readings developed in the framework notes —
adjudicated scope and interpretation, and is the accountable human sponsor.

**Abstract (draft).** Two companion papers established, from stated premises, that the
Born rule is the statistics of a proved fair game among detector absorber sites [P1] and
that the Heisenberg cut is a physical threshold with a computable location and width
[P2]. This paper supplies the framework those results install into: a real wave substrate
whose single organizing mechanism — phase locking — operates at two scales. At the
single-mode scale the lock threshold draws the virtual/real line: an excitation
off-resonance beyond its coupling slips and dies on the energy–time clock, while inside
the tongue it persists — matter as locked, self-sustaining waves. At the collective scale
the same mechanism becomes a genuine nonequilibrium transition: the Kuramoto threshold at
which a macroscopic assembly locks irreversibly, which is the cut. The two boundaries
differ in exactly two properties — scale and reversibility — and the framework's entropy
monotone lives only at the second. Between them sits everything this paper organizes:
superposition as coexistent clocks whose beat at the Bohr frequency (zitterbewegung its
founding instance) is the laboratory signature that both components are present; the
photon as the framework's uncoupled limit, real but never classical, classical light
arising by occupancy where classical matter arises by locking; and a single two-sector
register type — chiral pair, helicity pair, which-arm pair — storing every observable as
a relative amplitude and phase. The historical claim is stated plainly: the Schrödinger
and Dirac equations progressively extended the domain over which "the wave evolves" is
the whole story, and this program extends it across the measurement event, dynamizing the
projection postulate — the last element of quantum theory still imposed rather than
evolved. All claims are conditional on the companion papers' premises, and the paper
closes with the consolidated open-problem ledger of the whole program.

---

## 1. Introduction: the spine

Quantum mechanics has one dynamical law and one interruption of it. The dynamical law —
that the wave evolves — has been extended twice, each time swallowing territory that
previously required separate postulates. This paper is about the third extension.

**The first rung.** Schrödinger's equation (1926) describes the evolution of the wave
function, and its author meant that description realistically: $\psi$ was to be a
physical wave — he read $|\psi|^2$ as a literal charge density — and he resisted the
Born probability interpretation to the end of his life. The realism was defeated in his
own time by two objections, and we will need both later, so we state them now. First,
*wave packets spread*: a free packet disperses, while electrons persist. Second, *the
many-particle wave function lives in configuration space*: for $N$ particles $\psi$ is a
function on $\mathbb{R}^{3N}$, not a wave in physical space. Schrödinger lost the
argument; the equations stayed, the realism left.

**The second rung.** Dirac's equation (1928) extended the same evolution description to
special relativity, and the extension paid for itself: spin, the hydrogen fine
structure, and antimatter emerged unasked-for, and the negative-energy problem forced
quantum field theory into existence. At this rung the vocabulary must shift — the object
becomes a field, and we say "the wave" rather than "the wave function" — but the
description's character is unchanged: linear, deterministic, continuous evolution. One
discovery at this rung belongs to the spine's closing loop: analyzing Dirac's equation
in 1930, Schrödinger himself found the *zitterbewegung* — the trembling interference of
the positive- and negative-energy components at the Compton beat $2mc^2/\hbar$. The
founder's realism and the founder's trembling motion both feed what follows: the
zitterbewegung is the internal clock this framework couples, and the framework's name
records the debt — Dirac supplies the clock, Kuramoto supplies the lock.

**The third rung.** After Schrödinger and Dirac, exactly one element of quantum theory
remained outside the evolution description: the projection postulate, imposed by hand at
the measurement. Decoherence theory is deliberately not a rung here — it is linear
evolution of the density matrix, living entirely inside the second rung's description;
it explained diagonality, not events (the companion measurement paper [P2, §2] owns that
argument). This program's claim is that the last non-dynamical element is also dynamics:
a nonlinear lock, stochastic at the single-trajectory level and linear on average,
engaging only at dissipative boundaries. Each rung, then, extends the domain over which
"the wave evolves" is the whole story — nonrelativistic matter; relativistic matter and
fields; the measurement event itself.

**The honesty anchors.** The equations form a continuous lineage; the realism does not.
Dirac was an instrumentalist, and the realist thread is Schrödinger's alone until this
program re-litigates it — premise P0 of the selection companion [P1] is precisely that
re-litigation. A re-litigation must answer what defeated the original, so we score the
two objections now. *Spreading*: answered, and the answer is the framework's central
mechanism — locking is what makes waves persist; bound matter locks; a real particle is
a persisting wave because it sits inside its tongue (§3). The objection survives
everywhere the lineage's own tools reach — relativistic packets still spread, and field
theory inherited the problem rather than solving it — and is discharged only by the
lock. *Configuration space*: partially answered at best. The entangled sector carries
it (§5), where the companion's shared-registry premise [P1, P5–P6] is an explicit
ontological commitment, and we flag the objection **open** rather than glossed.

**What a framework paper owes.** The two companions are deliberately narrow: [P1] proves
that outcome selection is a fair game, conditional on stated detector premises; [P2]
locates the cut and computes its width, conditional on [P1]'s Theorem 2. This paper is
where the conditional structure is assembled into one picture and priced honestly:
premises in one place, the settled/claimed/open partition maintained across the whole
program, and the consolidated open-problem ledger at the end. Nothing here strengthens
the companions' claims; the framework earns its keep by what the assembly explains that
the parts do not — the ladder of §3, the register unification of §2, and the
two-classical-limits result that falls out of them.

*(Stub, decided: this paper **supersedes** the main interpretation paper [MCI], which
remains frozen as the provenance record. One paragraph here states the inheritance:
the interpretation's name — the Many Clocks Interpretation, with its founding contrast
against Many-Worlds — its three-stage measurement anatomy, bulk reference, detector
taxonomy, and gravitational-Bell candidate all move into this paper (§§4, 6, 7), revised
against the companions rather than merely cited.)*

## 2. The framework statement

*(Confirmed content in full; connective prose to be expanded at drafting session.)*

The ontology is a phase substrate: a real medium whose excitations are waves, on which
"particle" is the name for a wave that persists. Persistence, not substance, is the
framework's fundamental distinction, and it is earned dynamically — by locking. The
machinery is inherited from the companions and stated once: an internal clock for every
massive excitation (the chiral/zitterbewegung beat, §2.4 of [MCI]); a locking interaction
whose closed-system form provably cannot lock (the two-regime no-go, [MCI §2.2]) and
whose open, dissipative form is an Adler/Kuramoto attractor; and the three-way
distinction the measurement companion made load-bearing — entangling interaction,
decoherence, nonlinear lock — with every interpretive dispute located in the third
[P2 §2].

**Superposition as coexistent clocks.** A superposition is both outcomes' clocks running
simultaneously with a definite relative phase — coexistence, never alternation. When the
two components differ in energy, their beat at the Bohr frequency $\Delta E/\hbar$ is the
laboratory-real signature that both are present: quantum beats in fluorescence, Ramsey
fringes, and — the founding instance — the zitterbewegung itself, the beat of the $\pm E$
pair across the gap $2mc^2$. Degenerate superpositions are the silent case: both clocks
present, zero gap, frozen relative phase, no beat. The Born-compatibility constraint is
geometric and worth stating as a constraint: on the Bloch sphere the free dynamics
precesses the *phase at fixed latitude* — the outcome populations are constants of the
unitary motion, and literal alternation between outcomes would time-average every
superposition to even odds and destroy the Born weights. The latitude carries the weight;
the noise-driven diffusion from latitude to pole is the measurement, and it is a
separate, dissipative event [P1; MCI App. D]. The zitterbewegung is the exemplar, not a
universal rate: the chiral register is the framework's clock, not its universal pointer
[MCI §3.7–3.8].

**The photon as the uncoupled limit.** Vacuum Maxwell, written in Riemann–Silberstein
form ($\mathbf F_\pm = \mathbf E \pm i\mathbf B$), splits into two decoupled Weyl-form
equations — the two circular/helicity sectors. The photon is the framework's central
structure with the off-diagonal coupling set to zero: no gap, hence no beat, no internal
clock, and no lock. The Higgs condensate that clocks every fermion ($K = m = y_f\langle
\phi\rangle$) leaves the photon unclocked because the residual U(1) is unbroken. Matter
can switch the coupling on — a plasma gives the photon an effective mass, a magnetized
plasma splits the two helicities (Faraday rotation), chiral media likewise — so
everything clock-like about light is borrowed from matter. Three caveats fence the
correspondence: the sectors are spin-1 objects, not literal spinors; $|\mathbf F|^2$ is
an energy density, not a Born amplitude; and the medium-induced mass, not a fundamental
Proca term, is the physically realized case.

**Polarization as the sector pair.** The photon's polarization degree of freedom *is*
the helicity pair: the Poincaré sphere is its Bloch sphere — poles circular, equator
linear, latitude the relative amplitude, azimuth the relative phase. Every polarization
state is a superposition-as-coexistence: one definite field configuration with both
sectors present, degenerate and therefore silent. The observable is stored as a relative
phase — rotating the R–L phase by $\varphi$ rotates the linear axis by $\varphi/2$, the
half-angle double cover that makes polarization behave spinorially at spin 1 — in
exact obedience to the discipline that every physical claim reduce to a phase
difference [MCI §4.2]. The claim is scoped to polarization; path, frequency, and number
superpositions live in other degrees of freedom.

**Registers, intrinsic and geometric.** The electron's chiral pair, the photon's
helicity pair, and the interferometer's which-arm pair are one register type — a
two-sector SU(2) structure storing its observable in relative amplitude and phase —
differing in origin: intrinsic (sector pairs of the field itself) versus geometric
(created by apparatus sculpting of the mode function, the beamsplitter acting as a
coherent-boundary rotation [MCI §2.5]). Path superposition is therefore not a puzzle
about a delocalized photon; it *is* the delocalization, shaped — a mode function with
two branches is no stranger than a wide packet. The clean division the register picture
enforces: **delocalization is the wave's birthright; discreteness is the detector's
budget** — one quantum, one closure, however thinly the amplitude is spread [P1; MCI
§3.3]. Which-path is the register electromagnetic detectors einselect [MCI §3.7], which
is why path is the superposition detectors are best at destroying.

## 3. Two boundaries, one mechanism: the ladder

*(Confirmed content in full; Figure 1 = the ladder.)*

The framework's two great boundaries — virtual→real and quantum→classical — are the same
lock mechanism at two scales. Standard physics explains them with unrelated machinery: a
pole of the propagator on one side, decoherence and einselection on the other. Here they
differ in exactly two properties.

| Rung | Lock status | Persistence | Reversible? |
|---|---|---|---|
| **Virtual** (off-shell) | unlocked — slips against the substrate | transient, $\tau_{\rm slip}$ | — |
| **Real** (on-shell) | locked, single mode inside its tongue | $\infty$ or $\hbar/\Gamma$ | **yes** — threshold |
| **Classical record** | collective lock, supercritical | committed | **no** — ratchet |

- **Scale.** One mode locking to the substrate, versus a macroscopic assembly locking to
  each other.
- **Reversibility.** A threshold versus a ratchet. A real particle can be scattered back
  off-shell; a committed record cannot un-commit. The framework's entropy monotone lives
  only at the second boundary — which resolves the reversible-lock/committing-lock
  tension the measurement companion's panel flagged, quantified there as the
  recoverability criterion [P2 §4].

**Terminology, as discipline.** For a single mode, lock/unlock at the tongue edge is a
saddle-node bifurcation — a qualitative change in a system with few variables. A phase
transition proper requires the thermodynamic limit, and that is the second boundary:
the Kuramoto transition at $K_c$, a genuine nonequilibrium phase transition. We
therefore write **lock threshold** for the single-mode boundary and **sync transition**
for the collective one, and never "quantum transition" (which collides with atomic
quantum jumps and with the condensed-matter term "quantum phase transition"). What the
two share is critical slowing at the boundary. The honest summary: *the virtual/real
boundary is the single-oscillator shadow of the transition whose many-body form is the
Heisenberg cut.*

**The quantitative content is the companion's, cited not re-derived.** The slip-time
curve spanning both regimes — the energy–time-uncertainty clock $\tau \approx
2\pi\hbar/\Delta E$ far off-shell, the saddle-node divergence $\tau \propto (\Delta E -
\hbar K)^{-1/2}$ at the tongue edge, the crossover profile as the falsifiable middle —
is [P2 §5], scoped there, after panel review, as a heuristic correspondence; this paper
inherits that scoping and adds none.

**The boundary is soft, and the softness is structure.** An unstable real particle has
width $\Gamma = \hbar/\tau$: the shell is a resonance peak, a delta function only for
stable particles — persistence is depth in the tongue, continuously graded. And the
tongue's *width* is the coupling: a mode can sit off the bare shell by up to $K$ and
still lock. That is a bound state — an atomic electron is off its free-particle shell
and persists because the coupling holds it there; the displaced pole of the dressed
particle, read as in-tongue-but-off-bare-shell, with no new ingredient.

**Representation-independent grounding.** Virtual particles are perturbative
bookkeeping; nonperturbative formulations contain none, and the boundary should not
rest on Feynman diagrams. It does not have to: the representation-independent statement
is **propagating versus evanescent** — real wavenumber, phase advancing, energy carried
away; versus imaginary wavenumber, exponentially damped, clinging to its source
(frustrated total internal reflection is the virtual excitation made
laboratory-tangible). Propagating/evanescent is the locked/slipping dichotomy in
dispersion-relation terms, and no one disputes that *that* boundary is physical.

**Corollary: light is real but never classical.** A photon crosses the first boundary —
goes on-shell — and is barred from the second twice over: in flight it has no lock
partner (no environment, no decoherence; stellar interferometry survives light-years),
and at interaction it is annihilated — it dies at the cut, converting itself into a
lock in matter, the photoelectron cascade being matter crossing on the photon's behalf.
Classical *light* exists by a different route entirely: the macroscopically occupied
coherent state, fluctuations $\sqrt N$ against signal $N$. The framework therefore
carries two distinct classical limits — **matter classicalizes by locking; light by
occupancy** — and a single photon, too free to lock and too small to be loud, is
excluded from both. Reality and classicality, which travel together for matter,
separate cleanly for light: this is §2's uncoupled-limit result meeting the ladder, one
fact from two directions.

## 4. The anatomy of measurement — [STUB: the clock-dictionary chapter]

*Sources, in drafting order: [MCI §3] (three stages: capture/selection/registration;
the Re/Im W boundary; the dressed-mass pole form of the cut; what the coupling can and
cannot supply) as the installed mechanism, cited; then the clock-dictionary arc from
`NOTE_detector_engineering_surface_interference.md` — the three-hand clock (hour =
foliation, second = chiral/ZBW, minute = transition register), same-rate/random-position,
the 12/24-hour spinor double cover, the diffused-hologram account of the noise (reference
trichotomy; fairness and irreversibility from one incoherence), backwards time as
register-local retardation, the 2mc² energy ladder, antimatter chirality on the dial,
the Higgs clockmaker (`NOTE_cut_crossover_higgs.md` §3); the history principle (where
history is redundant vs real: state as sufficient statistic in the unitary sector;
history as physical resource at boundaries; echo T2*/T2 as the regime boundary); the
detector taxonomy table [MCI §5; P2 §4] and the energy-audit consistency test
[P1 §8.6(vi)].*

## 5. The entangled sector — [STUB]

*Sources: [MCI §7.5] (two bulks distinguished; nonlocality located in the non-separable
field configuration), [P1 §7] (two-stage joint game; resync-fidelity law $S = 2\sqrt2\,
\eta$; no-signaling as theorem via inverted Gisin), the frame-rotation mechanism with
its information-theoretic formulation (zero signal bits transmitted while doing the work
that costs a classical simulator one bit — Toner–Bacon; two protections: geometric,
rotations change only relative quantities; dynamical, the angle set by uncontrollable
noise), the no-speed-floor prediction; the preferred-frame passenger quarantined out of
[P2 §6] lands here in measurement-sector terms (constant-sync-phase foliation, VPFH
scoping from [MCI §8]). The 4D→3+1 grounding of the rotation
(`NOTE_pagewootters_chiral_clock.md` §7 + addendum) enters ONLY as a flagged speculative
outlook paragraph, if at all — scope fence per the note.*

## 6. The experimental program — [STUB]

*Sources: the T1–T5 ledger (memory + `LIGO_SIDEREAL_TEST_T5.md`) as probes of the single
preferred-frame postulate; **absorbed whole from [MCI §6 + App. C], per JB's keep-list**:
the linewidth-dependent gravitational Bell test — the candidate effect, the explicit
demonstration that it does NOT follow from the framework plus standard QED (the
factorization/cancellation null of App. C), the H′ postulate honestly isolated with its
gauge-legal gradient repair, the Micius consistency check, and the linewidth × altitude
parameter space (kHz linewidths, km-scale splits) — presented as a falsification test of
the postulate, not of the core; plus the Bose–Marletto–Vedral discriminator of the
wave-energy *reading* ([MCI §6.4]: a real-energy-density ontology predicts a BMV null).
Then [P1 §8] (deviation ledger, tabletop discriminator, cross-station injection,
energy-audit interferometry) and [P2 §8] (the γ/K dial: coupling, not mass, decides
where quantum behavior ends — the discriminator against collapse and
gravitational-reduction programs; transmon protocol sketch). Organizing claim: every
live test probes one commitment — the preferred frame — or one dial — the coupling.*

## 7. Discussion and the consolidated ledger — [STUB]

*Sources: **absorbed from [MCI §7], per JB's keep-list — the Many-Worlds-versus-
Many-Clocks contrast leads this section**: the trade-not-conquest framing ([MCI §7.2] —
insist on a single world with definite outcomes and Bell forces nonlocality; MWI buys
locality at the price of many worlds, MCI buys one world at the price of nonlocality; no
interpretation pays neither price), with branches-replaced-by-sync-basins as the
one-line statement of what "many clocks" replaces "many worlds" WITH — every particle a
clock, measurement their entrainment, one world occupied rather than branching. The
naming contrast is the program's founding move and [MCI] holds its first statement;
this section preserves it as the framework's interpretive identity. Then the honest
placement (single-world, ψ-ontic, nonlocal family [MCI §7.1]), Bohm/Nelson debts
updated post-[P1] ([MCI §7.3] + the fair-game answer), Penrose–Diósi ([MCI §7.4] + the
[P2 §8] coupling-not-mass discriminator), Montevideo and relational clocks ([MCI §7.6]).
Open problems merged across [P1 §9.4] (κ_ret microscopic derivation; P1 identification;
Stage-2 signaling edges; GHZ), [P2 §9] (continuous boundary-spanning model — with the
standing escape hatch: if solved during drafting, ladder+crossover+solution may split
out as its own paper, on evidence), [MCI §8] (Born measure status after [P1]: relocated
into premises; the dynamical selection law; the covariant formulation debt). Out of
scope, standing decisions: cosmology and QCD (separate papers); GR/QM discretization
spinoff; emergent-fields arc.*

---

## References — [STUB]

*Union of [P1] and [P2] reference lists plus [MCI]; new to this paper: Toner & Bacon
(2003) communication cost of simulating Bell correlations [verify per round protocol];
Riemann–Silberstein/Majorana–Oppenheimer formulation (Bialynicki-Birula review);
van Cittert–Zernike (Mandel & Wolf); Volovik (2003) if the §5 outlook paragraph
survives scope pass.*

*[P1] Claude Fable 5 & Bramble, J. M. — The Born Rule as a Derived Fair Game (v0.5.4).*
*[P2] Claude Fable 5 & Bramble, J. M. — The Heisenberg Cut as a Physical Threshold (v0.3).*
*[MCI] Claude (Opus 4.6–4.8) & Bramble, J. M. — The Many Clocks Interpretation (v8,
`current_revision_DK_paper.md`).*
