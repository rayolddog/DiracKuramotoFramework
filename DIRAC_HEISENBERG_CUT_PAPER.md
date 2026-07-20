# Measurement Without Collapse: The Heisenberg Cut as Apparatus-Dependent Registration
## The reversible→irreversible boundary as continued unitary evolution — a three-stage account across binary and continuous detectors

**Claude (Fable 5)¹ · John Bramble, MD²**
¹ Anthropic
² Independent Researcher (accountable sponsor)

*Correspondence & accountable sponsor: John Bramble, MD — jmbramblemd@gmail.com*

*Status: working draft. Companion to "Two Regimes of the Chiral Mass Coupling"
(`current_revision_DK_paper.md`). The chiral-clock ontology that **motivated** this work is
developed there, along with the preferred-frame and gravitational material, none of which is
carried here. The account below is a general one of measurement *registration* and does **not
depend on the Dirac chiral structure** for any of its claims: the chiral clock enters only as
motivating ontology (§2), and whether it does load-bearing work is an open question left to
the companion paper.*

## Author Contributions and AI Disclosure

Developed through an extended collaboration between the human author (J. Bramble), who
contributed the originating physical intuitions — that measurement is a re-synchronization
of the incident wavefunction to a detector, that the interaction is localized at the
detector boundary, that the wavefunction persists in the condensed-matter state rather than
being destroyed, and that the recorded variable and its irreversibility are set by the
apparatus — together with physical judgment and redirection at each step; and Claude
(Anthropic), which contributed the derivational structure, the comparison with standard
decoherence and continuous-measurement theory, and drafts of the prose. J. Bramble is the
accountable sponsor and assumes full responsibility for the correctness, originality, and
integrity of all content. Citations marked with a dagger (†) are standard references whose
page-level details should be verified against the originals.

---

## Abstract

Environmental decoherence explains why a measured system settles into a pointer basis and
loses interference, but the *unconditional* reduced state it produces is a stable improper
mixture: it does not single out one outcome, and it does not describe how one pointer
alternative becomes a durable, irreversible material record. We take decoherence's account
in full and ask what comes *after* it: what becomes of the wavefunction as a selected outcome
is registered? Our answer replaces the projection postulate's discarding of the wavefunction
with **continued unitary evolution** — the wavefunction is not collapsed but keeps evolving,
and its amplification into a macroscopic record *is* that evolution. Measurement is a
three-stage transition of the persisting wavefunction — resonant capture, a provisional (still
reversible) commitment, and reservoir-powered registration — with the detector's *ordinary
electromagnetic* open-system coupling supplying the measuring interaction throughout. (The work
was motivated by reading the Dirac mass term in the chiral basis as two coupled phase-clocks
whose closed-regime precession has no attractor — a natural ontology for the reversible state,
§2 — but nothing in the account depends on that reading.) The relative phase settles into the (inherited) einselected pointer
basin — the attractors of the dissipative reduced dynamics — the *selection* of which basin
being inherited from standard conditional-measurement theory, not derived here. The Heisenberg cut is the
reversible→irreversible boundary of this transition, and it is *apparatus-dependent*: we work
four canonical setups — Stern–Gerlach, a Bell test with single-photon detectors, a hologram
recorded on film, and a cloud chamber — spanning binary pointer basins (fixed by spinor
structure) and continuous pointer manifolds (accumulated exposure; particle trajectory). The
irreversibility is not a collapse but the effective, thermodynamic dispersal of the incident
particle's information across the many particles of the amplifying record — local entropy
production under globally unitary evolution — and the registration dynamics falls into two
classes (phase-locking for meter-oscillator readouts, amplitude-branching for direct
counters), unified as dissipative entrainment into the apparatus's pointer basins. We
are explicit about the facet this addresses — the *registration* of a selected outcome into an
irreversible record and the location of the cut, replacing the projection postulate's
discarding of the wavefunction with continued unitary evolution — and about what it does not:
it *inherits which* outcome is selected (from standard conditional-measurement theory) and
neither derives the Born rule nor supplies an outcome-selection law, both stated as open.

---

## 1. Introduction: which measurement problem

"The measurement problem" names not one problem but several, and conflating them is the source
of much confusion:

1. **The preferred-basis problem** — why measurements have definite *bases* (position,
   spin-along-an-axis) rather than arbitrary superpositions of them.
2. **The selection / single-outcome problem** — why a particular run yields *one* definite
   result, and which one (and, for a no-collapse ontology, in what sense a single world).
3. **The registration / Heisenberg-cut problem** — how a selected outcome becomes a stable,
   macroscopic, *irreversible* record, and where along the chain the reversible→irreversible
   boundary falls.
4. **The Born-probability problem** — why the outcomes occur with frequencies $|\psi|^2$.

Environmental decoherence [2, 3, 13, 14†] answers (1) decisively. It does not, by itself,
supply the individual outcome (2), the irreversible record (3), or the weights (4).

**This paper addresses facet (3), the registration — and it is important to be exact about how
narrow that is.** Its question is: *given* that an outcome is selected, what becomes of the
wavefunction? Textbook quantum mechanics answers with the projection postulate — the
wavefunction is *replaced* by the outcome eigenstate and the rest is discarded. We replace that
discarding with **continued unitary evolution**: the wavefunction is not projected but keeps
evolving, and its amplification into a macroscopic record *is* that evolution, dispersing the
outcome's information irreversibly (§3). Facet (2) — *which* outcome is realized, and why a
single one — we **inherit**: we take the outcome as an input, exactly as conditional-measurement
theory conditions on an observed record, and we neither derive it nor claim to explain it.
Facet (4), Born, we park. So the paper is a *registration mechanism*, not a solution to the
measurement problem, and it earns that modesty deliberately: naming the facets and claiming
only (3) is the discipline that keeps the account honest.

Two framings organize everything that follows, and we state them at the outset so they are
not mistaken later.

**Framing I — division of labor.** The Dirac chiral structure supplies the *ontology* of the
measured object: the internal clock, what "coherent" and "reversible" mean, and what a
"definite outcome" *is* at the level of a phase. The detector's *ordinary electromagnetic*
open-system physics supplies the *measurement engine*: resonant capture, environment-induced
selection of a charge/position pointer, dissipation, and reservoir-powered amplification. We
do **not** claim that any laboratory detector monitors the chiral scalar $\bar\psi\psi$; the
companion paper's channel analysis shows it does not. The chiral clock *rides* the pointer
the electromagnetic interaction selects; it is never itself the monitored observable. And we
state the consequence plainly: the registration account of §§3–7 **does not depend on the
chiral structure for any claim.** The chiral clock is the *motivating* ontology of "what
evolves and what is reversible"; strip it out and the account is a general one of measurement
registration. Whether the chiral structure does genuine load-bearing work — as opposed to
supplying a suggestive ontology — is an open question we leave to the companion paper (§8).

**Framing II — relation to decoherence.** We concede decoherence its entire domain and pick
up where it goes silent. Decoherence describes the *unconditional* reduced dynamics —
pointer-basis selection and the suppression of interference — and we adopt that account
without modification. What it does not describe is the *conditional, apparatus-dependent*
process by which a selected pointer alternative — the *singling-out* is inherited, via
conditioning on the record — is *stabilized* into a durable, effectively irreversible record.
That post-decoherence, post-selection registration is this paper's subject.

---

## 2. The motivating ontology: the Dirac chiral clock

*This section is the motivating ontology, not a load-bearing input: the registration account of
§§3–7 does not depend on it (Framing I). It is kept because it is where the ideas originated and
because it gives a concrete picture of "what evolves and what is reversible."*

In the chiral (Weyl) basis the Dirac equation separates into two coupled first-order
equations for the left- and right-handed sectors,

$$ i\,\bar\sigma^\mu \partial_\mu \psi_L = m\,\psi_R, \qquad i\,\sigma^\mu \partial_\mu \psi_R = m\,\psi_L, $$

so that the fermion mass $m$ is the single off-diagonal entry coupling the two sectors: a pair
of phase-clocks with coupling strength $K = m$ [1†]. Writing $\psi_L, \psi_R$ in amplitude–phase
(Madelung) form in the rest frame, the companion paper's §2.2 reduces the coupling to

$$ \dot\varphi_L = -K\sqrt{\rho_R/\rho_L}\,\cos(\varphi_R-\varphi_L), \qquad \dot\rho_L = +2K\sqrt{\rho_L\rho_R}\,\sin(\varphi_R-\varphi_L), $$

with $K=m$. The coupling enters the phase equation as a *cosine* — the reverse of the Kuramoto
form — and on the symmetric manifold $\rho_L=\rho_R$ the relative phase $\varphi_R-\varphi_L$ is
stationary for *every* value: the closed system has **no attractor**. This is the crucial
ontological fact for what follows. In the closed regime the chiral clock precesses unitarily
and reversibly; there is no preferred phase, nothing locks, and the full quantum state —
including any entanglement with a partner system — is coherently recoverable. This is exactly
the behaviour a correct account of a coherent superposition must exhibit, and it is what
"reversible" and "coherent" *mean* in this framework: a chiral phase relationship that is not
yet pinned to any value.

A note on clocks by particle type, needed for the detector examples. The chiral $K=m$ clock is
a property of *massive fermions*. A photon is not a Dirac spinor; its relevant clock is its
frequency $\omega$. Where an incident photon drives a bound electron (the photoelectric case),
the synchronization is between the photon's $\omega$-clock and the electron's chiral clock, not
between two chiral clocks. We flag the clock type at each detector rather than speak of a
universal chiral clock.

---

## 3. Where decoherence ends and this account begins

Decoherence, obtained by tracing the environment out of the joint system–environment state,
produces a reduced density matrix that (i) becomes diagonal in a preferred pointer basis
selected by the interaction Hamiltonian, and (ii) loses its off-diagonal coherences. We adopt
this in full. It is the correct account of *why* the pointer basis is what it is and *why*
interference is suppressed, and nothing here modifies it.

Two things it does not do, and both are essential to measurement:

- **It does not single out one outcome.** The diagonal reduced state is an *improper*
  mixture: a catalogue of alternatives with weights, not a statement that one alternative is
  the case. Reading a definite result requires *conditioning* on a record — a conditional
  quantum trajectory — and the same unconditional dynamics admits physically different
  unravelings depending on what is monitored and how [6†]. The unconditional equation alone
  does not privilege the trajectory that is realized.
- **It does not describe the transition to an irreversible fact.** Diagonalization in the
  pointer basis is, in principle, still reversible: the coherence has leaked into the
  environment but is not yet dispersed beyond recovery. The step from a recoverable
  correlation to a stabilized macroscopic record is a further, physical, *apparatus-dependent*
  process.

The Heisenberg cut is the boundary of that further step. It is not a size or a place fixed
once for all systems; it is the point at which the provisional, still-recoverable correlation
becomes stabilized by a reservoir into an effectively irreversible record. "Effectively" is
load-bearing: the irreversibility is practical, not fundamental. Global evolution remains
unitary, and — a point we take seriously as ontology — **the wavefunction is not destroyed at
the cut; it persists in the condensed-matter state of the detector.** What is lost is local
recoverability of the phase relationship, not the wavefunction.

What makes the step irreversible is not a collapse but the *dispersal of information*. The
incident particle's wavefunction carries information about it; through capture and
amplification that information is spread across the many particles that participate in the
record. Under globally unitary evolution the *total, fine-grained* entropy is conserved —
nothing is destroyed — but the *locally accessible* entropy rises, because no local probe can
any longer re-collect and re-phase the astronomically many degrees of freedom across which the
information now lives. Measurement irreversibility is, in this sense, local entropy production
by information dispersal, and the arrow it carries is the ordinary thermodynamic arrow, rooted
in the low-entropy initial condition rather than in any time-asymmetry of the dynamics
[15, 16†]. Two distinct dispersals occur together and should not be conflated: the *outcome
value* is copied **redundantly** across many particles, which is what makes the record
objective and readable (the quantum-Darwinism face [17, 18†]), while the *relative phase* is
**scrambled** across them, which is what makes it irreversible (the scrambling face [19, 20†]).
The number of particles across which the incident information has spread is thus the natural
order parameter for reversibility: a handful (Stages 1–2) is still re-collectable, hence
reversible; an amplification-scale multitude (Stage 3) is not. The Heisenberg cut is where that
count crosses from re-collectable to not — an information-theoretic criterion for the boundary,
complementing the formal one of §7.

---

## 4. Measurement in three stages

Measurement resolves into three stages, distinguished by timescale, threshold, and
reversibility rather than by any sharp ontological seam.

**Stage 1 — capture.** The incident system couples resonantly to a single detector degree of
freedom at the detector surface: a photon to a bound electron, a spin to a detector dipole.
This is where the boundary matters, and the claim must be stated operationally. It is *not*
that decoherence occurs only at boundaries — a particle can certainly decohere in free flight
through residual-gas collisions or ambient-photon scattering. It is that, *conditioned on the
particle being recorded by this detector*, the record-forming interaction is the one at the
detector boundary; a free-flight interaction is either negligible in a well-designed
experiment (good vacuum, cold, dark) or is itself a which-path measurement by a different
environment that removes the particle from the detected ensemble. The capture records
nothing; while only this stage operates the evolution is reversible.

**Stage 2 — provisional commitment.** The captured excitation begins to lock: the incident
clock synchronizes with the absorber, and the *relative* phase is drawn toward one of the
detector's stable pointer configurations (§5). This stage is **reversible in principle** — it
is the catch-and-reverse regime of a monitored qubit [6†], the decay of sub-threshold
latent-image specks, the refocusable side of a spin echo. It is the seat of the outcome
weighting, but it is *not yet an outcome*: no observer-independent instant certifies a result
before the record exists, and we do not give Stage 2 more ontological content than that. It
is a provisional microscopic commitment, not a realized fact.

**Stage 3 — registration.** The committed excitation is closed out by a free-energy reservoir
— a dynode chain, a developer bath, a supersaturated vapour — that amplifies it into a stable,
macroscopic, readable record and disperses the residual phase information into a continuum of
uncontrolled modes from which it does not return. This is where the Heisenberg cut sits: the
2→3 transition is the reversible→irreversible boundary. Registration is reservoir-powered and,
in the counting detectors, charge-triggered and energy-blind; it copies whichever alternative
Stage 2 committed and contributes no statistics of its own.

Throughout, the *engine* is electromagnetic (Framing I). Capture is a charge–current vertex;
einselection acts on charge/position; the reservoir is a condensed-matter free-energy store.
The chiral structure names *what is being synchronized* and *what is reversible*; it does not
perform the measurement.

---

## 5. The registration dynamics: how a selected outcome settles into the record

We now give the dynamical content of Stage 2 — the description of how the *inherited* outcome
settles into a stable record. Nothing in this section selects the outcome (that is inherited,
§1); it describes the *settling*. A more ambitious reading, in which the settling dynamics also
*determines* the outcome from a sub-quantum variable, is offered below as a speculative
candidate for the parked selection law, clearly flagged as such.

**The wavefunction persists; the relative phase locks.** When the incident particle is
captured, its wavefunction is not annihilated but continues, now as part of the detector's
condensed-matter state. Its clock synchronizes with the absorbing particle's. In the closed
regime this synchronization has no attractor (§2); once the system is opened to the detector's
dissipative environment, the reduced relative phase $\delta$ acquires an Adler/Kuramoto flow
[4†, 5†],

$$ \dot\delta = \Delta\omega - \gamma\,\sin(N\delta) + \eta(t), $$

whose stable fixed points are $N$ equally spaced basins. The relative phase is carried into one
basin; that is the provisional commitment.

**A speculative candidate for the selection (parked, not claimed).** One may ask whether the
settling dynamics also *determines* which basin, turning the inherited outcome into a derived
one. A candidate suggests itself: the absolute phase of a wavefunction is gauge — unobservable,
hence necessarily unpredictable — while only *relative* phases are physical, so the relative
initial phase between incident and absorber could serve as a sub-quantum variable whose value
the dissipative flow maps to the nearest basin (a hidden-variable reading with the relative
phase as beable). We offer this, and do not assert it, for two honest reasons: it faces a
consistency problem across detectors — a *number*-measuring counter has no such phase (§7) —
and even for phase measurements a *symmetric* landscape gives equal weights, not Born weights
(the amplitude would have to bias the basins, which is precisely the selection law we have
parked). It therefore belongs to the open problems (facets 2 and 4; §8), and none of the
paper's registration claims rest on it.

**Einselection sets the attractor landscape; it is not itself the attractor.** A word on
terminology, because the distinction matters. *Einselection* is the environment-induced
*process* that selects the stable pointer states; it is done by the electromagnetic
interaction Hamiltonian and picks out a charge/position pointer basis. Those einselected
pointer states *are* the attractors of the dissipative reduced dynamics — pointer states are
precisely the stable states of the open-system flow [2, 3, 13†]. So einselection fixes the
attractor *landscape* — the *set* of basins, i.e. $N$ and their geometry — while *which* basin a
given run reaches is the individual outcome, set (in this reading) by the relative chiral
phase. Einselection names the selecting; the attractors are the selected states; the
individual outcome is beyond einselection. One should therefore say "the einselected pointer
states are the attractors," never "the attractor is the einselection."

**Born, and the route to it.** The candidate above cannot by itself give Born weights: a
*symmetric* landscape yields equal frequencies ($\tfrac12,\tfrac12$ for $N=2$), and reproducing
$|\alpha|^2, |\beta|^2$ would need the amplitudes to bias the basin measures — again, the parked
selection law. The natural way to close that gap is relaxation to quantum equilibrium (the
sub-quantum $H$-theorem [7†]), with the relative phase as the equilibrating variable. We name it
and leave Born open; nothing in the registration account depends on it.

The account preserves no-signaling: the correlations of an entangled pair come from the full
composite state, not from anything local to a chiral pair (§6, Bell).

---

## 6. Four detectors, one structure, different pointer manifolds

The claim that the cut is *apparatus-dependent* is made concrete by working four setups that
share the three-stage structure but differ in what is recorded and how many basins the
landscape has. Two are binary — with the binarity fixed by spinor structure — and two encode
the result in a continuous pointer manifold.

**Stern–Gerlach (spin-½): a binary, spinor-fixed pointer.** A spin-½ particle in a field
gradient splits into two spatial packets; the measurement completes only when a packet
interacts irreversibly with the screen. The spinor two-valuedness is *why* there are exactly
two outcomes: the attractor landscape is a double well ($N=2$), basins at $\delta=0,\pi$. Below
the cut the split is coherent and recombinable (Stern–Gerlach recombination); the cut falls at
the irreversible screen interaction.

**Spin-1 (nuclear) Stern–Gerlach: three basins, from a real einselected observable.** The
three-outcome generalization is *spin*, not color. Color charge, though genuinely three-valued,
is confined and gauge — never isolated, never gauge-invariantly labeled, and so never
einselected by any detector; it is the analog of the absolute phase (unobservable), not of a
pointer. A spin-1 system, by contrast, has three projections $m=-1,0,+1$ that *are* einselected
and directly measured. Concrete nuclear examples are the spin-1 nuclei deuterium ($^2$H) and
$^{14}$N. The landscape is a three-well ($N=3$); the apparatus is the same Stern–Gerlach, one
basin richer. A spin-$I$ system gives $2I+1$ basins — the discrete pointer count is set by a
real observable, not asserted.

**Bell test, single-photon detectors: binary click plus amplification.** Each detector
registers click / no-click: a binary pointer whose "1" is a reservoir-powered avalanche
following a single absorption. The entanglement of the pair is a property of the full composite
state $|\Psi_{AB}\rangle \in \mathcal H_A\otimes\mathcal H_B$ — *not* of any chiral pair internal to
one photon — and the correlations are taken from that state; no-signaling is preserved. The
incident clocks here are photon $\omega$-clocks driving the detectors' electrons. This example
is where the "chiral pair carries the entanglement" reading must be explicitly disavowed.

**Hologram on film: a continuous accumulated-dose manifold.** A photographic emulsion records
not a binary phase but an integrated exposure: the local grain density tracks the local optical
intensity $I(\mathbf x)=|\psi_1(\mathbf x)+\psi_2(\mathbf x)|^2$, so the *relative phase of the
interfering field is written into the spatial intensity pattern*. Each microscopic photon–grain
event is its own weak capture–commit–register triplet with a latent-image threshold; the
macroscopic image is the aggregate of many such events. The pointer manifold is continuous
(dose over position), not a set of discrete basins.

**Cloud chamber: a continuous trajectory from repeated weak vertices.** The incident particle is
not captured whole at any vertex; it makes many small energy transfers, each seeding a local
metastable nucleation that grows a droplet [8†]. The recorded variable is a trajectory or
deflection angle — continuous in position — assembled from a sequence of local commit–register
events. The correlated geometry of successive ionizations is fixed by the incident wavefunction,
while each vertex is an independent local record.

The lesson is the spread itself: binary (Stern–Gerlach, Bell click; spinor-fixed) versus
continuous (hologram dose, cloud-chamber trajectory) shows that the number of basins, the
recorded variable, and the location of the cut are properties of the *apparatus*, not of a
universal collapse law. The same three-stage structure runs in every case; only the pointer
manifold changes.

---

## 7. The Heisenberg cut as the reversible→irreversible boundary

The cut is the Stage 2→3 transition: the point at which a provisional, recoverable commitment
becomes reservoir-stabilized and effectively irreversible. Three standard facts make the
*reversibility below the cut* directly demonstrable: the nuclear-spin echo refocuses dephasing
that has not been dispersed to a reservoir; a superconducting qubit can be caught and reversed
mid-measurement [6†]; and a Stern–Gerlach beam can be recombined before the screen. In each,
the system sits below the cut — decohered in the pointer basis, perhaps, but not yet registered.

A formal criterion for the boundary can be written in effective-action language: the onset of
an absorptive part ($\operatorname{Im}W \neq 0$) marks the appearance of a real, on-shell
excitation and the beginning of the irreversible channel, while $\operatorname{Re}W$ alone is
the reversible, refocusable regime. We present this as a structural, effective-action account
and label the correspondences (imaginary part $\leftrightarrow$ record onset; imaginary
self-energy $\leftrightarrow$ locking rate) as **analogies** pending a microscopic derivation,
rather than as identities. They are suggestive of where the cut lies; they are not, as written,
proven to be the same object. This formal criterion should coincide with the
information-theoretic one of §3 — the cut as the point where the count of participating
particles crosses re-collectability — which is the more physical statement of the same boundary.

**Two reduction classes, one worked.** Whether "synchronization" is a mechanism or a metaphor
turns on whether a genuine dynamical reduction can be derived from the microscopic Hamiltonian
for a real detector. Carrying that program out for the single-photon avalanche (a companion
derivation) shows that measurement reductions fall into (at least) two classes, and that
forcing a single form on all detectors would be an overreach.

*Amplitude-branching (direct counters).* For a Geiger-mode single-photon detector, the reduction
from the capture vertex $H_{\rm c}=\hbar g\,(a\sigma_+ + a^\dagger\sigma_-)$ through the avalanche
is a **bistable / branching-escape** dynamics in the carrier number $n$,

$$ \dot n = \gamma(V)\,n - c\,n^2 + \sqrt{2Dn}\,\xi(t), \qquad \gamma(V)=[\alpha(E)-\beta_{\rm loss}]\,v_d, $$

with the rate $\gamma(V)$ **derived from real electromagnetism** — the impact-ionization
coefficient $\alpha(E)$ [21†], the drift velocity, and the bias field $E=V/w$. The two outcomes
are extinction (no click) and a self-sustaining avalanche (click); the click probability is the
branching non-extinction probability $P_{\rm trig}$ [22†], and the cut is the avalanche-triggering
threshold, still quenchable (reversible) below it. This is a real, worked reduction — but its
order parameter is an *amplitude* ($n$), not a phase: there is no $\delta$, no $\sin N\delta$, no
Adler equation. Nor should there be, and the derivation shows why — a single photon leaves no
persistent phase to lock to, and a counter measures number, which is conjugate to phase.

*Phase-Adler (meter oscillators).* The Adler form $\dot\delta = \Delta\omega - \gamma\sin(N\delta)
+ \eta$ of §5 is instead the correct reduction for a *dispersive / QND* readout, in which a
genuine meter-oscillator phase is injection-locked by the system. The circuit-QED / homodyne
model of the companion paper's Appendix D is exactly this case; writing it out cleanly is the
natural next step, and it is where "synchronization" is literal rather than generalized.

The two classes are unified — as the §6 zoo already hinted — as **dissipative entrainment into
the apparatus's stable pointer basins**: one three-stage structure and one reversibility
criterion (§3), realized as phase-locking or as amplitude-branching according to whether the
pointer is an oscillator phase or a carrier count. The paper therefore claims the umbrella, with
one class worked and one assigned — not a single universal law.

---

## 8. Scope, placement, and open problems

**What this paper claims.** A post-decoherence, apparatus-dependent account of the *registration*
of a *selected* outcome: measurement as the three-stage transition of a persisting wavefunction
— reversible provisional settling into the inherited pointer basin, then reservoir-powered
irreversible registration — described across binary and continuous pointer manifolds. Its one
interpretive novelty over textbook practice is to replace the projection postulate's discarding
of the wavefunction with continued unitary evolution: the record forms by the outcome's
information dispersing, not by $\psi$ being collapsed. The chiral structure supplies the ontology
of the measured object; ordinary electromagnetism supplies the engine.

**What it does not claim, stated as open problems.**

- **Which outcome is selected, and why a single one** — facet (2) — is *inherited*, not
  addressed: the paper conditions on an outcome exactly as standard measurement theory does.
  The single-world realization is therefore as open here as it is there; this paper does not
  close it, and the no-collapse ontology it adopts is, on this point, incomplete pending the
  selection law below.
- The **Born rule** is not derived. The symmetric lock gives equal weights; Born weights
  require an amplitude-biased landscape, i.e. the selection law below.
- The **outcome-selection law** — what fixes the amplitude-biased basin measures and thereby
  which basin a run enters — is not supplied. Relaxation to quantum equilibrium [7†] is named
  as the candidate route.
- The **chiral-coupling-to-detector bridge** is a separate hypothesis, deferred to the
  framework paper: nothing here requires the detector to monitor the chiral scalar, and the
  channel analysis says it does not. The chiral clock is the ontology of the measured object,
  not the pointer of the apparatus.
- No **preferred-frame or gravitational** claims are made here; that material stays in the
  companion paper.

**Placement.** The account sits in the single-world, $\psi$-ontic, nonlocal family of
interpretations, alongside Bohmian [10†] and Nelsonian [11†] mechanics. It does not modify
quantum mechanics, accepts Bell's theorem [9†], takes correlations from the entangled state,
and preserves no-signaling. Its relation to decoherence is additive, not competitive: it
adopts decoherence's account of the pointer basis and the loss of interference in full and
supplies only the post-decoherence, conditional, apparatus-dependent registration that
decoherence leaves open.

What would turn this into a theory is a derivation of the Born measure and an explicit selection
law — the two facets we inherit or park. On the registration side, we have *identified* the two
reduction classes and their per-detector assignment but derived neither from the microscopic
Hamiltonian in full: the single-photon case (§7) identifies the amplitude-branching class and
reads its rate off known device physics [21, 22†], and the phase-Adler case awaits a clean
write-up from the companion paper's Appendix D. Carrying out one such reduction from the
Hamiltonian is the decisive next step. We have tried to be clear about which parts are argued
and which are owed.

---

## References

*Standard references; those marked † should be verified against the originals at the page
level.*

1. Dirac PAM. "The quantum theory of the electron." *Proc. R. Soc. A* 1928;117:610–624. †
2. Zurek WH. "Decoherence, einselection, and the quantum origins of the classical." *Rev. Mod. Phys.* 2003;75:715–775.
3. Zurek WH. "Pointer basis of quantum apparatus: into what mixture does the wave packet collapse?" *Phys. Rev. D* 1981;24:1516–1525. †
4. Adler R. "A study of locking phenomena in oscillators." *Proc. IRE* 1946;34:351–357. †
5. Kuramoto Y. *Chemical Oscillations, Waves, and Turbulence.* Springer, 1984. †
6. Wiseman HM, Milburn GJ. *Quantum Measurement and Control.* Cambridge Univ. Press, 2009. †
7. Valentini A. "Signal-locality, uncertainty, and the subquantum H-theorem." *Phys. Lett. A* 1991;156:5–11. †
8. Mott NF. "The wave mechanics of α-ray tracks." *Proc. R. Soc. A* 1929;126:79–84. †
9. Bell JS. "On the Einstein Podolsky Rosen paradox." *Physics* 1964;1:195–200. †
10. Bohm D. "A suggested interpretation of the quantum theory in terms of 'hidden' variables. I & II." *Phys. Rev.* 1952;85:166–193. †
11. Nelson E. "Derivation of the Schrödinger equation from Newtonian mechanics." *Phys. Rev.* 1966;150:1079–1085. †
12. Joos E, Zeh HD. "The emergence of classical properties through interaction with the environment." *Z. Phys. B* 1985;59:223–243. †
13. Schlosshauer M. *Decoherence and the Quantum-to-Classical Transition.* Springer, 2007. †
14. Gabor D. "A new microscopic principle." *Nature* 1948;161:777–778. †
15. Landauer R. "Irreversibility and heat generation in the computing process." *IBM J. Res. Dev.* 1961;5:183–191. †
16. Bennett CH. "The thermodynamics of computation—a review." *Int. J. Theor. Phys.* 1982;21:905–940. †
17. Ollivier H, Poulin D, Zurek WH. "Objective properties from subjective quantum states: environment as a witness." *Phys. Rev. Lett.* 2004;93:220401. †
18. Zurek WH. "Quantum Darwinism." *Nat. Phys.* 2009;5:181–188. †
19. Hayden P, Preskill J. "Black holes as mirrors: quantum information in random subsystems." *J. High Energy Phys.* 2007;2007(09):120. †
20. Sekino Y, Susskind L. "Fast scramblers." *J. High Energy Phys.* 2008;2008(10):065. †
21. Chynoweth AG. "Ionization rates for electrons and holes in silicon." *Phys. Rev.* 1958;109:1537–1540. †
22. McIntyre RJ. "On the avalanche initiation probability of avalanche diodes above the breakdown voltage." *IEEE Trans. Electron Devices* 1973;20:637–641. †
