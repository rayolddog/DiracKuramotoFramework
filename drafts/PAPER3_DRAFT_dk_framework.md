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

**Abstract (draft).** Two companion papers argue, from stated premises, that the Born
statistics are those of a fair game among detector absorber sites — conditional outcome
compatibility with the Born comparator, not a derivation of the Born measure [P1] — and
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

**What a framework paper owes.** The two companions are deliberately narrow: [P1] argues
that outcome selection is a fair game, conditional on stated detector premises — v0.7 of
that paper withdrew "proves" along with its claim to derive the Born measure, and states
its result as conditional outcome compatibility over a tested domain (round 2, item L3-5); [P2]
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
form ($\mathbf F_\pm = \mathbf E \pm i\mathbf B$; the Majorana–Oppenheimer formulation
of electromagnetism), splits into two decoupled Weyl-form equations — the two circular/helicity sectors. The photon is the framework's central
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
(created by apparatus sculpting of the mode function, the beamsplitter a coherent
boundary in the sense of [MCI §2.5], acting as a rotation on the register). Path superposition is therefore not a puzzle
about a delocalized photon; it *is* the delocalization, shaped — a mode function with
two branches is no stranger than a wide packet (Grangier–Roger–Aspect:
single-photon anticorrelation and interference demonstrated in one apparatus). The clean division the register picture
enforces: **delocalization is the wave's birthright; discreteness is the detector's
budget** — one quantum, one closure, however thinly the amplitude is spread [P1; MCI
§3.3]. Which-path is the register electromagnetic detectors einselect [MCI §3.7], which
is why path is the superposition detectors are best at destroying.

**A century of evidence, reorganized.** The framework's two-route structure — locking
for matter, occupancy for light, ensemble statistics yielding only noise-classicality
(§3) — is not a new empirical claim; it is a reorganization of what a century of
experiments already measured. The table reads them in the framework's terms:

| Experiment | What it probed | What it established, in these terms |
|---|---|---|
| Young 1801 (sunlight + pinhole) | ensemble light coaxed into wave behavior | coherence can be *manufactured* from ensemble light — visibility is source history (§4.4) |
| Einstein 1909 (fluctuation formula) | both routes at once | blackbody fluctuations carry two terms — shot noise at low occupancy, wave interference at high — the two classicalities in one equation |
| Planck 1900 / Rayleigh–Jeans | the ensemble route's breaking point | classical field theory fails exactly where mode occupancy drops below $\sim 1$: light's classical limit *is* an occupancy criterion |
| Taylor 1909 (feeble light) | interference with one photon at a time | light's wave-classicality is not inter-photon statistical mechanics |
| Hanbury Brown–Twiss 1956 | the two classicalities, distinguished | thermal bunching ($g^{(2)}=2$) vs. coherent flatness ($g^{(2)}=1$) — noise-classical and wave-classical light empirically separated |
| Laser 1960 / Glauber 1963 | the occupancy route, isolated and formalized | the coherent state as the classical wave; the phase manufactured by a matter-side locking transition (Haken) |
| Tonomura 1989 (electron buildup) | the fermion prohibition | no classical electron wave — matter's classicality arrives as records, dot by dot, one lock at a time |
| BCS / BEC / Josephson | the exception that enforces the rule | matter reaches the occupancy route only by first becoming bosonic |

None of these experiments needed the framework, and the framework claims none of them
as evidence *for* it over standard quantum mechanics. What the table shows is
different and worth showing: the two-route structure is not an interpretive novelty
bolted onto the physics but the organizing pattern the record already follows — the
framework names the axes the century was measuring along.

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
Classical *light* exists by a different route entirely: **occupancy** — the
macroscopically occupied single mode *with a common phase*, the coherent state,
fluctuations $\sqrt N$ against signal $N$. The route name is chosen with care.
Occupancy is not ensemble statistics: the coherent state is a pure state of one mode,
classical by being loud, with no averaging or thermalization anywhere — whereas the
*ensemble* route, applied to light, yields only thermal radiation, which is classical
as **noise** (intensities, ray optics, bunching) but carries no definite phase and is
no classical *wave*; the Glauber counting of [P1 §6] separates exactly these cases.
Nor is occupancy alone sufficient — a large-$N$ number state is loud and phaseless —
and the missing common phase is, on theme, borrowed from matter: the laser threshold
is a collective locking transition in the *gain medium* (Haken's theory, the direct
ancestor of Kuramoto's model), a matter-side sync transition manufacturing the phase
that light itself cannot lock. The framework therefore carries two distinct classical
limits — **matter classicalizes by locking; light by occupancy** — and the assignment
is *compelled, not chosen*: Bose statistics permits and stimulated emission enhances
the piling of quanta into one mode, while Pauli exclusion categorically bars matter
from it — which is why there is no classical electron field, and why matter accesses
the occupancy route only by first becoming bosonic (Cooper pairs, atomic condensates:
the superconductor's classical phase dynamics is the exception that enforces the
rule). Spin-statistics distributes the two classical limits; each species takes the
only road open to it. A single photon, too free to lock and too small to be loud, is
excluded from both. Reality and classicality, which travel together for matter,
separate cleanly for light: this is §2's uncoupled-limit result meeting the ladder,
one fact from two directions.

## 4. The anatomy of measurement: the clock dictionary

*(v0.1 first pass. The mechanism itself is inherited from [MCI §3] and the companions
and compressed in §4.1; §§4.2–4.7 draft the clock-dictionary arc from the framework
notes. Interpretive and speculative items keep their note-level flags.)*

### 4.1 The three stages, installed

A measurement separates into **capture, selection, registration** [MCI §3.1; P1 §2;
P2 §4]. Capture is reversible: a resonant, amplitude-sensitive coupling inside the
tongue ($|\Delta\omega| \lesssim K$), distributing excitation across every candidate
site in proportion to local intensity, committing to nothing — its laboratory
demonstrations are the spin echo, the catch-and-reverse of a monitored qubit, and
Stern–Gerlach recombination [MCI §3.2]. Selection is the commit: the noise-driven
exchange game among the captured shares, where the Born weights are set [P1]; and
registration is the reservoir-powered closure — charge-triggered, energy-blind,
equivariant by design: it copies whatever selection committed and contributes no
statistics of its own [MCI §3.1]. Where the first irreversibility sits is a
physical question with a detector-specific answer, and [P1 v0.8 §6.1] places it at the
end of selection — when an exposed site's holding converts to a real excitation, in a
semiconductor the interband vertex and thermalisation at 10 fs–1 ps — not in the
amplification, which writes the record but cannot un-write a thermalised carrier. The
stage boundaries are physical, not narrative:
formally the two clauses of the cut condition (an absorptive channel open; the bath
lock engaged — $\mathrm{Im}\,W \neq 0$, $\Gamma_{\rm cap} > 0$ [MCI §3.5], equivalently
the dressed Dirac mass pole leaving the real axis [MCI §3.6]); operationally the
recoverability criterion of the measurement companion [P2 §4]; quantitatively the
$\kappa_{\rm ret} \sim K$ layer of width $w = K/\omega$ [P2 §3]. One structural fact
from [MCI §3.7–3.8] governs everything downstream and is restated once: the
electromagnetic interaction couples through the vector current, so the pointer basis
real detectors einselect is **which-path/charge**, not the chiral channel — the chiral
register is the framework's *clock*, not its pointer.

### 4.2 The clocks: three hands, two registers

Per atom and per register, one clock; its **rate** is universal (a species constant set
by mass or transition energy), its **position on the face** is random across atoms.
That one sentence — *same rate, random position* — is the dictionary's core entry, and
premise P3(a) of the selection companion is its formal statement.

*(Interpretive, note-flagged; sponsor-originated, 2026-09-02.)* The core entry already
binds three quantities, and the binding deserves its name before the hands are
introduced. A hand's *rate* is an energy, $E = \hbar\,d\varphi/dt$; its *position* is
the informational variable — the thing a record can capture, and the thing thermal
matter leaves random; the hand itself is time. Three bounds make the binding
quantitative, and none of them is an identity. Time–energy uncertainty: a hand cannot be
read to $\Delta t$ without an energy spread $\hbar/\Delta t$, which [P1 §6.1] uses when
it saturates capture at $1/\omega$ for a massless quantum. Margolus–Levitin: the energy
sets the maximum rate, $2E/\pi\hbar$, at which a hand can pass between distinguishable
positions — energy is the clock rate of information. Landauer: erasing one position
costs $k_BT\ln 2$. So $\hbar$ and $k_BT$ are the two exchange rates, and there is no
third; one quantum can carry unboundedly many bits and one bit can ride on arbitrarily
little energy, which is why the three are *bound* and not *one*. The framework converts
between them at two definite places. At capture, the incident wave's phase history —
position information — is not destroyed but converted into the zero-mean noise that
drives selection (the diffused hologram, §4.3; [P1 §4]). At registration, dissipated
energy, many orders above $k_BT\ln 2$, buys one record. Between the two conversions
sits the game. And the three come apart at exactly one place: energy is conserved
through registration while position information is not — the hour hand's monotonicity
(§4.3, §4.5) is supplied by the very locks that lose it. That is the cut, stated in
information language; the measurement companion's criterion — the cut is where
in-principle recoverability ends [P2 §4.1] — is the same statement.

The full dial has three hands. The **hour hand** is universal, foliation time — the
irreversible-lock counter, owned by the substrate and not by any atom, frozen during
any single event. The **second hand** is the chiral/zitterbewegung phase
($\sim 10^{20}$ Hz for electrons), the register bound matter collectively disciplines.
The **minute hand** is the optical-transition phase ($\sim 10^{15}$ Hz), the recording
register — and it is *this* register that thermal matter leaves phase-random. "The
bulk is coherent" (second hand) and "the sites are mutually incoherent" (minute hand)
are statements about different oscillators in the same atoms; the framework needs both
and they do not compete. The second hand runs in three modes, by process: **held** at
capture (the drive imprints its phase — the memory that points home), **geared** at
entanglement formation (one shared orientation for the pair — the registry premise
[P1 P5] in clock language), **rotated** at measurement (the first lock re-forms the
joint orientation — the frame rotation of §5).

The clock face itself carries Dirac structure. A spin-½ phase is a half-angle: the
spinor returns to itself only after 720°, every observable (bilinear) after 360° —
equivalently, the Dirac phase runs at $\omega_C = mc^2/\hbar$ while the observable
zitterbewegung beat runs at $2\omega_C$. Choosing the 12-hour or the 24-hour face is
choosing which object you track; the ZBW beat is the 12-hour observable reading of a
24-hour spinor clock. The detector's fair game is played with minute hands at random
positions on faces whose deep dial is 24-hour.

### 4.3 The diffused hologram: one incoherence, two consequences

The noise that runs the selection game has a physical identity: the interference cross
term between each site's complex amplitude and the uncontrolled-phase fields of the
detector's own charges and the vacuum [P1 §4]. The holographic reading makes its
structure exact. Each absorbing atom is a recording site whose *reference beam* — its
transition-register phase — has an uncontrolled angle: same frequency as its neighbors
(a spectrally incoherent medium could not resonantly capture at all — white light
models a medium outside the game, not a detector playing it unfairly), but random
mutual phase. The decisive variable is what is *known* about the references, and it
sorts every measurement architecture into a trichotomy [P2 §4.1]: **common** reference
(the homodyne/local-oscillator limit — engineered fairness, engineered readout);
**known-different** references (the echo and atomic-frequency-comb media — an
angle-multiplexed hologram, invertible because the angles can be re-supplied);
**random-unrecorded** references (the detector bulk — the diffused hologram, written
but unreadable). The framework's central economy lives here: **one incoherence buys
both fairness and irreversibility.** Because the references are random, the cross-term
noise is zero-mean — no site is favored, the game is fair, and the Born weights are
protected [P1, Theorem 1]. Because the references are unrecorded, the record cannot be
inverted — the phase history is scrambled beyond recall, and the commit is permanent.
Fairness and the arrow of the measurement are the same fact about the same phases.
(Quantitative handle, open: each exchange hop adds one unrecorded reference, so
history fidelity should decay with hop count like angle-multiplexing crosstalk — the
volume-holography scaling laws are a candidate calibration, logged as a toy
calculation in the notes.)

### 4.4 Where history is redundant and where it is real

The unitary sector needs no history variable: the state is its own sufficient
statistic. Wave propagation is Markovian in the field — the field on any surface is
complete boundary data for everything downstream — so the present wave *is* the
integrated past, compressed; and interference reads only *differential* history, which
begins where paths split (everything upstream of the split is common-mode phase and
cancels — the discipline that only phase differences are physical, applied to
provenance). This is why the double-slit fringe calculation needs the slits and not
the source: fringe *spacing* is slit geometry, while the source's contribution —
coherence — enters as fringe *visibility* (van Cittert–Zernike). At dissipative
boundaries the accounting inverts: history becomes a real, non-redundant physical
resource. The first interaction has memory primacy (the held phase of §4.2 — the
memory that points home); reversal is possible exactly while the history still points
back, and the spin echo marks the regime boundary in the laboratory — T2* dephasing
refocusable because its history is locally stored, T2 irreversible because its history
has diffused into the bulk (§4.3). One sentence for the interpretive ledger: Bohmian
mechanics, whose guidance law needs no memory in flight (correctly — see above), has
no measurement-sector history mechanism at all; the diffused hologram is ours.

### 4.5 Backwards time, the energy ladder, and antimatter on the dial

*(Interpretive, note-flagged; Dirac-level where stated.)* Locking requires
bidirectional phase authority: in the Adler flow the instantaneous rate swings through
$[\omega - K,\ \omega + K]$, and retardation — the hand moving backward against its
reference — is half of what a lock *is*. The framework reads this at Dirac level: a
real oscillation is identically a sum of counter-rotating components, and the
negative-frequency sector is not optional — no localized packet exists without it, and
the zitterbewegung *is* the beat of the two senses across $2mc^2$
(Feynman–Stückelberg on the dial: a backward-running hand is a forward-running mirror
hand). The resolution that keeps causality intact: **backwards time is always
register-local — second hand relative to hour hand — never global**; the hour hand's
monotonicity is supplied by the irreversible locks themselves (§4.3). The energy
ladder then organizes the phenomenology: at common energies, backward rotation exists
only as bounded, repaid slips — the $\kappa_{\rm ret}$ give-back of a failed lock, the
virtual excursions of §3. At $2mc^2$ (or the Schwinger field) the counter-rotation is
promoted from rented transient to self-sustaining clock: pair production — the
ladder's virtual→real crossing (§3), with the quantity that goes real now
identified: the rotation sense itself. No
in-place reversal ever occurs: reversed clocks are only pair-created with a forward
partner and pair-destroyed by mutual unwinding (charge conservation, read on the
dial). And charge conjugation flips chirality for the same geometric reason a screw
reverses handedness when its rotation reverses while its arrow is kept: the
backward-running right-chiral clock *is* the forward-running left-chiral anti-clock —
one fact in two vocabularies, with the invariant statement about chirality, not
helicity. Slogan, flagged as slogan: eV physics rents backward time in closed loops;
MeV physics buys it outright, only in matched pairs; nothing touches the hour hand.

### 4.6 The clockmaker

The second hand's coupling is not free-standing: the Yukawa interaction is *defined*
as a chirality flip ($\bar\psi_L H \psi_R$ — a bare mass being gauge-forbidden), so
$K = m = y\,v/\sqrt2$: **the Kuramoto coupling of the chiral clocks is set by the
Higgs condensate**, and every second-hand tick is a transaction with the vacuum
(Penrose's zig-zag picture, made mechanical). The condensate plays exactly three
roles and refuses a fourth: it sets the denominator of every Compton clock; it
*creates* the clocks (no condensate, no mass coupling, no beat); and it is **not**
the frame — a scalar vacuum expectation value is Lorentz-invariant, and the
frame-breaking is done elsewhere, by the foliation vector (§5). The QCD chiral
condensate is the sibling clockmaker — it supplies ~99% of hadronic mass and hence of
every nuclear clock rate — and §2's photon result is this section's converse: the
condensate is neutral under the residual U(1), so the photon alone is sold no clock.
(Full three-role analysis: `NOTE_cut_crossover_higgs.md` §3.)

### 4.7 One mechanism, many detectors

Two numbers span the detector zoo along the single mechanism: the per-event **capture
strength** and the **commit threshold** $k$ — how many captures must accumulate at one
site within its memory time before selection commits [MCI §5]. The Bell/photon
detector is the projective limit ($k = 1$: one quantum, one capture, one commit, one
click — the only detector class for which per-event Born claims are properly made). Its
reversible window closes at the surface event, not at the avalanche: for a semiconductor
absorber the interband vertex and thermalisation end recoverability within 10 fs–1 ps,
and [P1 v0.8 §6.1] finds that window *marginal* against the selection game's final leg in
silicon and inverted in superconducting absorbers — so the recording clock downstream
(avalanche, hotspot, readout) is not the variable that can move the Born weights; the
photon-to-gap ratio is.
NMR/MRI is the ensemble limit (no single-quantum threshold; every free-induction decay
a watched Stage-2/3 relaxation). The cloud chamber is the weak/repeated limit — not
one drawn-out measurement but a *sequence* of partial capture–commit–register triplets
(Mott's problem, resolved as track-recording taxonomy). The photographic emulsion is
the integrating limit ($k \approx 3$–4, Gurney–Mott), and its reciprocity failure —
a sub-threshold latent speck *decaying* if not reinforced — is everyday laboratory
evidence that selection and registration are physically distinct stages: Stage-2
progress can be made and then lost. The chapter closes with the audit that makes the
whole anatomy calorimetric [P1 §8.6(vi)]: every click deposits the full quantum at one
site, at every fringe position; the distributed capture of Stage 1 is reversible
energy, returned at $\kappa_{\rm ret}$, never banked — so losing sites retain no
residue, and the energy in the fringe is small or nonexistent until the second stage
completes. Delocalization is the wave's birthright; the budget closes at one address.

## 5. The entangled sector

*(v0.1 first pass. This is the sector where the configuration-space objection of §1
lives; it is flagged open at the start and not glossed at the end. Everything here is
conditional on the selection companion's P5–P6 — the explicit nonlocal shared-registry
premise — over and above the single-detector premises.)*

### 5.1 The locus: two bulks, one configuration

Two physically different objects travel under the word "bulk," and the framework's
honesty depends on never letting them blur [MCI §7.5]. The **local thermal reference**
at each detector — the faint, parts-per-million bias that performs the local commit and
sets outcome visibility — is established in the common past of both wings and is
independent of the analyzer settings: it is exactly a Bell common-cause variable, and
by Bell's theorem it *cannot* source the correlations. The framework's own numerics
sharpen the exclusion into an internal no-go: a clock-as-local-variable model of the
outcomes is not merely bounded by the classical CHSH value of 2, it is **sub-classical**
— CHSH $\le \sqrt2$ [MCI App. A] — so whatever the clocks do locally, the correlation
must come from elsewhere. It comes from the second object: the **extended,
non-separable field configuration** carrying the entangled two-particle mode across
both wings — not a common cause at all, but one configuration of the real field
spanning A and B. Locating the nonlocality there adds no postulate; it restates the
ψ-ontic commitment. The framework is not superdeterministic (settings are free), and
no-signaling is not assumed (it is delivered as a theorem in §5.2).

### 5.2 The joint game and the fidelity law

The selection companion extends the single-detector game to entangled pairs as a
**two-stage joint game** [P1 §7]: the pair is one substrate object with one shared
internal orientation; the first wing's commit is stage one; the second wing then plays
against a registry re-formed by that commit. Two exact results carry the sector. The
**resync-fidelity law**, $S = 2\sqrt2\,\eta$: the CHSH value is the quantum maximum
degraded only by the registry fidelity $\eta$, with the local-realism bound crossed at
$\eta = 1/\sqrt2$ — which converts existing experiments into measurements of $\eta$
(photonic CHSH near 2.8 over $10^2$-km baselines implies $\eta \gtrsim 0.99$: whatever
the substrate's update mechanism is, it is near-perfect at terrestrial scales). And
**no-signaling as a theorem**: the inverted-Gisin result derives commit-rate linearity
— [P1]'s Theorem 5, hence marginal invariance — from the premises, rather than imposing
it as a constraint (v0.7 of that paper demoted Theorem 5 from the operative mechanism for
continuum absorbers to a robustness result; v0.8 withdraws that demotion in turn, its
corrected ladder placing commitment at first irreversibility and finding the separation
marginal in silicon and inverted in superconducting absorbers, so Theorem 5's linearity —
that of the first-irreversibility vertex, not of the downstream cascade — carries weight
again; the inverted-Gisin reading is a
consistency result, not a derivation — round 2, items L3-6 and round 1, item 9); within this framework, the impossibility of exploiting the nonlocal sector
is *emergent* [P1 §7]. A controlled measurement of $\eta$ itself (deliberate
cross-station injection, with its computable, angle-independent leak law) is part of
the experimental program (§6; [P1 §8.7]).

### 5.3 The frame rotation: influence without information

The mechanism on offer for the registry update is the **frame rotation** — the
sponsor's central-point picture, stated as the postulated mechanism of nonlocal
influence at exactly premise level (P5–P6), no higher. The entangled pair carries one
shared internal orientation (a plane/phase frame) anchored at the creation event; the
first lock does not send anything anywhere — it **rotates the shared frame**, and the
changed degree of freedom is an angle, not a field configuration crossing space.

The information-theoretic statement is the sharpest form. The rotation **transmits
zero signal bits while doing the work that costs a classical simulator exactly one
bit** (Toner–Bacon: simulating singlet correlations classically requires one bit of
communication per pair). Zero, not a fraction — and the zero is doubly protected:
*geometrically*, because a rotation of a shared frame changes only a relative quantity
with no local zero (nothing at either station moves — the discipline that only phase
differences are physical, now doing nonlocality's bookkeeping); *dynamically*, because
the rotation angle is set by the uncontrollable noise-driven outcome of the local game,
and the inverted-Gisin theorem makes marginal invariance exact. This is Shimony's
"uncontrollable nonlocality" — influence without information — given a mechanism.

The same geometry yields the sector's standing prediction: **a rotation has no
velocity, so there is no speed of quantum influence to measure** — experiments
bounding "spooky action" speeds will find only ever-growing lower bounds, never a
floor (the $10^4 c$ bounds of the Geneva and Chinese experiments are consistent
entries in an unbounded sequence). Before-before puzzles dissolve the same way: the
rotation happens at the shared object, ordered by the foliation, not at either wing.

### 5.4 The frame, priced

The foliation that orders the commits is the framework's openly carried preferred
frame: the constant-sync-phase slicing of the substrate (the khronon), entering
**through the measurement sector only** — Stage-1 dynamics is exactly Lorentz
covariant, and the frame appears where the lock does [MCI §8]. As written this is
explicit, low-energy Lorentz violation confined to measurement, not spontaneous
breaking; the Einstein-aether/khronometric construction that would make it spontaneous
is not carried out here. Ordinary matter couples to the frame, beyond the
electromagnetic locking itself, only gravitationally — the suppression that explains
why clock-comparison and Michelson–Morley bounds have not registered it — but the
quantitative demonstration that the residual anisotropy clears every established bound
remains **owed**, alongside the covariant formulation of the selection dynamics and
the configuration-space objection of §1, which this sector holds rather than answers:
the shared registry is precisely the many-particle structure that does not live in
physical 3-space, stated as a premise and priced as one. Whether the frame is local
(mass–energy rest frame) or cosmic (CMB) is an open, testable question — only a cosmic
frame produces sidereal signatures, and the experimental program (§6) is built to ask.

### 5.5 Outlook, fenced

*(Speculative — stacked on the most conjectural material in the program's notes;
nothing above depends on it.)* There is a picture in which the rotation's properties
stop being surprising: if the 3+1 arena itself emerges from a synchronizing 4D
substrate — the foliation as the condensate's global frame choice — then the pair's
shared frame is a *local, pair-specific* orientation in the same order-parameter space
out of which spacetime's split emerges, and a rotation of it is a change one level
below the domain where "speed" and "distance" are defined. Post-breaking,
reorientations within the degenerate vacuum manifold are Goldstone-type moves: locally
costless, locally invisible, only relative orientations physical. On that picture the
zero-bit property, the no-speed-floor prediction, and the emergence sketch are three
faces of one statement — the rotation is motion along a symmetry direction of the
medium spacetime is made of. We record the alignment and claim nothing from it.

## 6. The experimental program

*(v0.1 first pass. Organizing claim, stated once and used throughout: every live test
in the program probes one commitment — the preferred frame — or turns one dial — the
coupling. Tests are labeled by what a positive result would establish and, with equal
care, by what a null would and would not touch.)*

### 6.1 The coupling dial

The measurement companion's central experimental *direction* is that **coupling — not
mass, size, or gravitational self-energy — is the variable that decides where quantum
behavior ends** [P2 §8.3–8.4]. (Round-1 ledger item 12: [P2] §8.2 demoted the
one-parameter collapse from claim to research direction, and the surviving
discriminators are §8.3–8.4; the stronger wording here predated that demotion.) The cut sits at $\kappa_{\rm ret} \sim K$ with fractional
width $w = K/\omega$, and existing platforms already span that dial across sixteen
orders of magnitude — from atomic linewidths ($w \sim 10^{-8}$) through transmons to
broadband solid-state absorbers ($w \sim 10^{-2}$) [P2 §3]. That makes the framework
*differentially* testable against the collapse programs: CSL and Diósi–Penrose put the
classical boundary on mass and size; this framework puts it on $\gamma/K$, so an
engineered system moved along the coupling dial at fixed mass discriminates the
programs — the preregistrable circuit-QED protocol sketched in [P2 §8.2], with the
recoverability criterion ([P2 §4.1], applied in [P2 §8.3]) and Leggett–Garg-type
axes [P2 §8.4] as the readouts. Macromolecule interferometry, the collapse programs' home turf, is re-read
accordingly: interference should be lost where the *coupling* budget says so, not
where the mass budget does.

### 6.2 The selection game's own signatures

The selection companion carries its falsifiability in a deviation ledger with a
protective theorem: the port decomposition confines every observable deviation to one
experimental family [P1 §8.1–8.2]. The live configuration is the **mismatched-port
tabletop discriminator** [P1 §8.4]: single photons at a variable splitting ratio
$S:(1-S)$ into ports of deliberately mismatched collective structure. Any local POVM —
standard quantum mechanics with arbitrary physics inside each port — makes the
conditional port statistics exactly affine in $S$; the framework's live channel
predicts curvature $\kappa\,S(1-S)$. Nonzero curvature would discriminate against the
linear-POVM structure of quantum mechanics itself; a null at the $10^{-3}$ level
closes the last deviation channel and renders the mechanism empirically equivalent to
standard quantum mechanics — the fork stated in [P1 §8.5], whose protective horn our
own judgment favors, and which only the bench can decide. Around it sit the secondary
signatures [P1 §8.6]: time-resolved Born statistics; the warm-detector odds-bias
candidate at the $\hbar\omega \lesssim k_BT$ boundary of the fairness window; and the
**energy-audit interferometry** consistency test (§4.7): full quantum per click at
every fringe position, no calorimetric residue at losing sites — the audit that
existing energy-resolving detector data (MKID astronomical cameras, TES calorimetry)
could already begin, and that no experiment has yet been framed to perform.

### 6.3 The entangled sector's knobs

The fidelity law $S = 2\sqrt2\,\eta$ (§5.2) converts Bell tests into measurements of
the registry fidelity, and the **cross-station injection protocol** [P1 §8.7] makes
$\eta$ a controlled variable rather than an inferred one: deliberately injected
broadband cross-station noise leaks into the correlators only through registry
infidelity, with a computable, angle-independent signature ($\delta S = 4(1-\eta)L$) —
a near-term, systematics-robust measurement on any working Bell setup. The same
protocol's phase-locked-tone channel carries the sector's most radical flag: a
correlation excess **above the Tsirelson bound**, which no quantum-mechanical
mechanism can produce; its observation would be decisive, its null cheap. Standing
alongside: the **no-speed-floor** prediction (§5.3) — bounds on the "speed of quantum
influence" grow without ever finding a floor, because a rotation has no velocity.

### 6.4 The preferred frame's tests: the T-ledger

The frame enters through measurement only (§5.4), so its tests are boundary tests. The
program's ledger:

| | Test | Probes | Status |
|---|---|---|---|
| **T1** | Gravitational Bell vs. linewidth | the H′ postulate (below) | designed; never performed |
| **T2** | Sidereal GHZ | cosmic vs. local frame | designed |
| **T3** | AB visibility vs. $\gamma$ | in-flight (kinematic) frame coupling | companion draft |
| **T4** | MRI/NMR surface relaxation | frame coupling in the *dissipation* channel | designed |
| **T5** | LIGO sidereal quantum-noise modulation | cosmic frame, boundary anisotropy | drafted; pilot data streaming |

The literature already constrains the *free-precession* channel severely (neutron
bounds at $b_n < 6.7\times10^{-34}$ GeV close it); the framework's own scoping is that
its coupling acts at boundaries — in the **dissipation channel, which existing bounds
do not probe**. T4 and T5 live in exactly that loophole; T2 and T5 carry the sidereal
signatures that would distinguish a cosmic (CMB) frame from a local one; a null across
the ledger leaves the framework with only the gravitationally suppressed coupling and
retires the stronger VPFH forms.

### 6.5 The gravitational Bell test and its postulate, kept whole

The program's oldest candidate prediction is retained with its honesty apparatus
intact [MCI §6, App. C]. The candidate effect: two Bell detectors at different
gravitational potentials, entangled photons of *narrow* linewidth $\Delta\nu$; if the
local reference couples into the polarization projection, the redshift accumulates
$\delta\phi_{\rm grav} = \omega\,\Delta\Phi/c^2\Delta\nu$ over the coherence time, and
CHSH degrades as $\exp(-\delta\phi_{\rm grav}^2/2)$ — a $1/\Delta\nu^2$ visibility
exponent, discriminated by a joint linewidth × altitude scan (kHz linewidths at
km-scale splits reach order unity; Micius-class broadband photons sit seven orders
below sensitivity, which is why the signature has never been tested). The honesty
apparatus is the point: the effect **does not follow from the framework plus standard
QED** — the absorption amplitude factorizes into a polarization projection times a
temporal factor, the redshift lives entirely in the latter, and it cancels as a
common-mode phase in the normalized correlation ([MCI App. C]; every apparatus element
that might evade the factorization was checked and fails). The effect requires an
additional, non-covariant coupling H′ of the polarization projection to the local
reference rate (gauge-legal in its gradient form, still non-covariant, still absent
from QED). The experiment is therefore a clean falsification test *of that postulate*
— the preferred-frame commitment showing up at the level of a single measurement — and
not of the framework's core. Separately, the **Bose–Marletto–Vedral configuration**
discriminates the wave-energy *reading* of the ontology: a real-energy-density source
gravitates as a mean field and would *not* gravitationally entangle two masses — a BMV
null — where quantized gravity predicts entanglement [MCI §6.4]; far-future, and noted
as an ontology discriminator rather than a framework prediction.

### 6.6 What falsifies what

The map, plainly: curvature in the tabletop discriminator or an above-Tsirelson
injection excess would overturn quantum mechanics' linear structure in the framework's
favor — and their nulls close deviation channels while leaving the core intact, since
the core is built to be Born-exact [P1]. The coupling-dial protocols test the
framework *against* the collapse programs — a mass-located boundary falsifies us, a
coupling-located one falsifies them. The T-ledger and the H′ test probe the
preferred-frame commitment: sidereal nulls retire the cosmic frame, an H′ null retires
the one candidate signature and returns the frame to its unobserved-but-necessary
role. What no accessible experiment reaches is the fenced outlook of §5.5 — and the
program says so rather than borrowing credibility from it.

## 7. Many worlds, many clocks: placement, debts, and the ledger

*(v0.1 first pass.)*

### 7.1 The trade

The moment one insists on a single world with definite outcomes that reproduces
quantum statistics, Bell's theorem presents the bill: nonlocality. Everett escapes it
only by denying definite single outcomes — Many-Worlds buys **locality** at the price
of **many worlds**. This program makes the opposite trade: it buys a **single world**
at the price of **nonlocality** (in the Bell sense, never signaling — §5). No
interpretation pays neither price, and we present the choice as a trade, not a
conquest [MCI §7.2]. What "many clocks" replaces "many worlds" *with* is the
program's founding move, and it fits in a sentence: **every particle carries a clock;
measurement is the entrainment of clocks; the alternatives that Many-Worlds spreads
across branches are here the unoccupied basins of one world.** Where Everett's
superposed outcomes all persist, ours compete — the sync basins of the selection game
— and exactly one is occupied, with the Born weight as its occupation frequency,
argued fair from detector premises [P1], and conditional on them. Branching is replaced by locking; the
multiverse by a substrate; the preferred basis problem by the einselected which-path
register (§4.1); and the probability postulate by a race.

### 7.2 The family and the debts

The framework's honest address is the **single-world, ψ-ontic, nonlocal family** —
Bohm and Nelson are its neighbors, and naming the family is more durable than
positioning against any member [MCI §7.1]. Within the family, the debts and
distinctions after the companions:

- **Against Bohm.** Bohm has a guidance law and quantum equilibrium; the framework now
  answers with guidance inherited from the vacuum dressing ([MCI §7.3]) and a
  **fairness argued from detector physics, conditional on [P1]'s premises** — an answer
  of a different kind, though narrower in its difference than earlier drafts of this
  section claimed (round-1 ledger item 4). [P1] v0.7 carries an explicit preparation
  measure as a premise of its own, so the contrast is not measure against no-measure.
  It is *where the measure sits*: Bohm places a probability law over hidden
  configurations of the propagating system, whereas here the wave is the beable, the
  system factor is a Dirac delta — no probability law over hidden system variables at
  all — and the preparation measure is detector-side with independently measured
  provenance. Bohm's foliation
  is empirically inaccessible by construction; ours is physical and carries a test
  program (§6.4–6.5). Bohm's history debt is the measurement sector (§4.4). The
  remaining shared debt: the explicit covariant selection dynamics (§7.3, item 5).
- **Against Penrose–Diósi.** Both cast gravity as classicalizer; the operational split
  is now clean — they put the boundary on **mass**, we put it on **coupling**, and the
  §6.1 dial decides. The deep-isolation regime where their intrinsic mechanism runs
  and our dissipative one runs out of bath remains the arbiter [MCI §7.4].
- **Against Montevideo and the relational-clock tradition.** Closest kin: real clocks,
  real decoherence. The split: their coherence loss is fundamental (imperfect clocks
  referred to time itself), ours is environmental and dissipative — absent for a
  closed system however imprecise its clock; and we pay for definite outcomes with a
  beable and a frame that Montevideo does not require [MCI §7.6]. Page–Wootters
  supplies the natural formal home for the kinematics (the three-hand dial of §4.2 is
  a PW clock with an entropy monotone bare PW lacks); we note the fit, and claim no
  derivation.

### 7.3 The consolidated ledger

The program's open problems, merged across the trio and stated once:

1. **The κ_ret ansatz** — derive the sub-threshold return rate $\kappa_{\rm ret} =
   \Delta E/\hbar$ (and the legitimacy of contraction-eigenvalue modeling) from an
   explicit quantized field–absorber–bath Hamiltonian [P1 §9.4(viii); P2 §9]. The
   single deepest debt: §3's crossover, §4.1's stage boundaries, and the energy
   audit's residue clause all turn on it.
2. **The P1 identification** — energy share = outcome probability as a result rather
   than a premise: the closed conserving open-system calculation that would make the
   fair noise a consequence of surface wave mechanics [P1 §9.4(iv)].
3. **The continuous boundary-spanning model** — one dynamical model exhibiting the
   bifurcation at $\kappa_{\rm ret}/K = 1$ with detector-derived coefficients [P2 §9].
   Standing decision: if solved, ladder + crossover + solution may split out as its
   own paper — on evidence, not in advance.
4. **The fork** [P1 §8.5] — whether a deeper fairness principle closes the
   mismatched-port channel (protective reading) or the curvature is real (radical
   reading); the §6.2 bench decides.
5. **The covariant formulation** — the explicit selection dynamics on the foliation,
   with its no-signaling proof written independently of the statistics it reproduces;
   plus the quantitative clearance of every established Lorentz bound (§5.4).
6. **The configuration-space objection** — Schrödinger's second defeat, held open at
   the shared registry (§1, §5.4): a premise priced, not a problem solved.
7. **Sector completions** — GHZ/multipartite iteration of the joint game; the
   $\eta = 1$ derivation the frame-rotation picture suggests; the Stage-2 signaling
   edges (finite-commit-duration ordering; the multi-quantum tone treatment)
   [P1 §9.4].

### 7.4 What this program is not, and what it is

Out of scope by standing decision: cosmology and the QCD sector (separate papers);
the GR/QM discretization spinoff; the emergent-fields arc deriving the substrate's
own particle content. Each consumes this framework; none is consumed by it.

What it is, returning to the spine: Schrödinger built an equation that describes the
evolution of the wave and meant it as physics; the description was extended once to
relativity and fields, and then stopped, one postulate short, for a century. The
program assembled here — a fair game argued in the detector [P1], a cut with an
address and a width [P2], and the ladder, registers, and clocks of this paper —
is the case that the stopping was contingent, not necessary: that the measurement
event is the same substrate doing one more thing waves do, which is to lock. The
case is conditional, and every condition has been priced in the open — premises
stated, deviations ledgered, the frame carried honestly, the debts numbered above.
The wave does not collapse; it evolves — and where it locks, it records.

---

## References

*(v0.1 list — built from what this paper's text names directly; detector physics,
theorems, and measurement machinery are cited through the companion tags below and
carried by those papers' own verified lists. EVERY entry here is pending the round
protocol's URL-verification pass before freeze; entries whose details most need
checking are marked ⚠.)*

**Companions and predecessor:**

- **[P1]** Claude Fable 5 & Bramble, J. M. (2026). A Field–Matter Selector for Outcome
  Production, Conditioned on a Detector Ready-State Measure. v0.7, this repository
  (`drafts/PAPER1_DRAFT_born_selection.md`; adversarial-review round in
  `born_selection_AI_review_2026-07/`).
- **[P2]** Claude Fable 5 & Bramble, J. M. (2026). The Heisenberg Cut as a Physical
  Threshold: Location, Width, and Consequences of the Classical–Quantum Boundary in
  Detector Dynamics. v0.3, this repository (`drafts/PAPER2_DRAFT_heisenberg_cut.md`;
  review round in `heisenberg_cut_AI_review_2026-07/`).
- **[MCI]** Claude (Opus 4.6–4.8) & Bramble, J. M. (2026). The Many Clocks
  Interpretation: Quantum Measurement as Bath-Induced Synchronization. v8, frozen as
  the provenance record (`current_revision_DK_paper.md`); superseded by this paper.

**Named in the text (alphabetical):**

- Adler, R. (1946). A study of locking phenomena in oscillators. *Proc. IRE* **34**,
  351–357.
- Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique
  Fizika* **1**, 195–200.
- Bialynicki-Birula, I. (1996). Photon wave function. *Progress in Optics* **36**,
  245–294. (Riemann–Silberstein formulation and its history.)
- Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of
  "hidden" variables, I and II. *Phys. Rev.* **85**, 166–193.
- Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Z. Phys.* **37**, 863–867.
- Diósi, L. (1989). Models for universal reduction of macroscopic quantum
  fluctuations. *Phys. Rev. A* **40**, 1165–1174.
- Dirac, P. A. M. (1928). The quantum theory of the electron. *Proc. R. Soc. London A*
  **117**, 610–624.
- ⚠ Einstein, A. (1909). Zum gegenwärtigen Stand des Strahlungsproblems. *Phys. Z.*
  **10**, 185–193. (The fluctuation formula, §2 table.)
- Everett, H. (1957). "Relative state" formulation of quantum mechanics. *Rev. Mod.
  Phys.* **29**, 454–462.
- Gambini, R., & Pullin, J. (2018). The Montevideo interpretation of quantum
  mechanics: a short review. *Entropy* **20**, 413.
- Glauber, R. J. (1963). Coherent and incoherent states of the radiation field.
  *Phys. Rev.* **131**, 2766–2788.
- Grangier, P., Roger, G., & Aspect, A. (1986). Experimental evidence for a photon
  anticorrelation effect on a beam splitter. *Europhys. Lett.* **1**, 173–179.
- Gurney, R. W., & Mott, N. F. (1938). The theory of the photolysis of silver bromide
  and the photographic latent image. *Proc. R. Soc. London A* **164**, 151–167.
- ⚠ Haken, H. (1975). Cooperative phenomena in systems far from thermal equilibrium
  and in nonphysical systems. *Rev. Mod. Phys.* **47**, 67–121. (Laser threshold as
  locking transition, §§2–3.)
- Hanbury Brown, R., & Twiss, R. Q. (1956). Correlation between photons in two
  coherent beams of light. *Nature* **177**, 27–29.
- Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear
  oscillators. *Int. Symp. on Mathematical Problems in Theoretical Physics*, 420–422.
- ⚠ Lita, A. E., Miller, A. J., & Nam, S. W. (2008). Counting near-infrared
  single-photons with 95% efficiency. *Opt. Express* **16**, 3032–3040. (TES
  calorimetry, §6.2.)
- Mandel, L., & Wolf, E. (1995). *Optical Coherence and Quantum Optics*. Cambridge
  University Press. (van Cittert–Zernike theorem, §4.4.)
- ⚠ Mazin, B. A., et al. (2013). ARCONS: a 2024-pixel optical through near-IR
  cryogenic imaging spectrophotometer. *Publ. Astron. Soc. Pac.* **125**, 1348.
  (Energy-resolving MKID camera, §6.2.)
- Minev, Z. K., et al. (2019). To catch and reverse a quantum jump mid-flight.
  *Nature* **570**, 200–204.
- Mott, N. F. (1929). The wave mechanics of α-ray tracks. *Proc. R. Soc. London A*
  **126**, 79–84.
- Nelson, E. (1966). Derivation of the Schrödinger equation from Newtonian mechanics.
  *Phys. Rev.* **150**, 1079–1085.
- ⚠ Oppenheimer, J. R. (1931). Note on light quanta and the electromagnetic field.
  *Phys. Rev.* **38**, 725–746. (Majorana–Oppenheimer form, §2.)
- Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: dynamics
  described by stationary observables. *Phys. Rev. D* **27**, 2885–2892.
- Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Relativ.
  Gravit.* **28**, 581–600.
- Penrose, R. (2004). *The Road to Reality*. Jonathan Cape. (The zig-zag picture of
  the mass coupling, §4.6.)
- ⚠ Planck, M. (1900). Zur Theorie des Gesetzes der Energieverteilung im
  Normalspectrum. *Verh. Dtsch. Phys. Ges.* **2**, 237–245.
- ⚠ Salart, D., Baas, A., Branciard, C., Gisin, N., & Zbinden, H. (2008). Testing the
  speed of "spooky action at a distance." *Nature* **454**, 861–864.
- Schrödinger, E. (1926). Quantisierung als Eigenwertproblem. *Ann. Phys.* **79** (and
  series). (First rung, §1.)
- ⚠ Schrödinger, E. (1930). Über die kräftefreie Bewegung in der relativistischen
  Quantenmechanik. *Sitzungsber. Preuss. Akad. Wiss., Phys.-Math. Kl.* 418–428.
  (Zitterbewegung, §1.)
- ⚠ Shimony, A. (1984). Controllable and uncontrollable non-locality. In *Proc. Int.
  Symp. Foundations of Quantum Mechanics* (Tokyo), 225–230. ("Passion at a distance,"
  §5.3.)
- ⚠ Taylor, G. I. (1909). Interference fringes with feeble light. *Proc. Camb. Phil.
  Soc.* **15**, 114–115.
- Toner, B. F., & Bacon, D. (2003). Communication cost of simulating Bell
  correlations. *Phys. Rev. Lett.* **91**, 187904. (The one-bit simulation result,
  §5.3.)
- Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T., & Ezawa, H. (1989).
  Demonstration of single-electron buildup of an interference pattern. *Am. J. Phys.*
  **57**, 117–120.
- Volovik, G. E. (2003). *The Universe in a Helium Droplet*. Oxford University Press.
  (Emergent relativity near a Fermi point — cited ONLY by the fenced outlook §5.5;
  drop with it if the outlook does not survive scope pass.)
- ⚠ Yin, J., et al. (2013). Lower bound on the speed of nonlocal correlations without
  locality and measurement choice loopholes. *Phys. Rev. Lett.* **110**, 260407.
  (§5.3 speed bound.)
- ⚠ Yin, J., et al. (2017). Satellite-based entanglement distribution over 1200
  kilometers. *Science* **356**, 1140–1144. (Micius consistency check, §6.5.)
