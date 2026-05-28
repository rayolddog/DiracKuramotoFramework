---
title: "Discretization as Synchronization: Quantum Spectra Without Quantizing Spacetime"
subtitle: "A Mechanistic Completion of Penrose's Modify-QM-Not-GR Program"
author: "John Bramble, MD"
date: "May 2026"
---

**John Bramble, MD¹**

¹ Independent Research

*Correspondence: rayolddog (GitHub)*

*Preprint — not yet peer reviewed*

*AI Disclosure: This work was developed in collaboration with Claude Opus 4.7
(Anthropic), as described in the Author Contributions section. Per current
journal guidelines, LLMs do not satisfy authorship criteria; the human author
bears full responsibility for all content.*

*Companion paper to: Bramble, J. (2026), "Many Clocks Interpretation of Quantum
Mechanics: Mass as Chiral Coupling, Re-synchronization in the Bulk as
Measurement" [PAPER_UNIFIED, under review].*

---

## Abstract

The standard formulation of quantum mechanics treats discreteness — discrete
spectra, discrete spin values, discrete detection events — as a foundational
feature requiring postulation. General relativity, in contrast, is formulated
on a continuous, differentiable manifold. The tension between these two
ontologies has driven nearly a century of attempts to either quantize
spacetime (loop quantum gravity, causal sets, string theory, causal dynamical
triangulations) or to derive a discrete substructure from a more fundamental
theory. None has produced a confirmed prediction.

This paper proposes that the tension is misdirected. The discreteness of
quantum mechanics is not a fundamental feature of nature but an *emergent
property of synchronization on a continuous substrate*. Discrete spectra are
the locked-mode spectra of nonlinear oscillator dynamics; discrete
detection events are the threshold-crossing kinematics of bulk-coupled
detectors; discrete spin values are the irreducible-representation
dimensions of an underlying continuous symmetry group. In each case the
substrate remains continuous and the discreteness is derived. If this
reading is correct, the manifold of general relativity need not be
quantized — and the GR/QM conflict, as traditionally posed, dissolves.

The proposal builds on the Dirac–Kuramoto (DK) framework developed in the
companion paper [1], which identifies the chiral structure of the Dirac
equation as a phase-synchronization system and re-interprets measurement as
a two-stage re-synchronization process. Here we extract the broader
consequence: that the mechanism developed there for measurement generalizes
to a *uniform mechanism for QM discreteness*, of which the standard examples
(Bohr–Sommerfeld quantization, spin multiplets, atomic line spectra,
photodetection, energy bands, cavity quantization, black-hole ringdown
spectra) are all special cases. The position aligns with Penrose's
long-standing argument [2, 3] that general relativity is correct and quantum
mechanics requires modification; the DK mechanism is the dynamical content
that Penrose's gravitational-collapse threshold left unspecified. The paper
is an *interpretive proposal*, not a complete theory; the load-bearing
derivations — particularly the basin-of-attraction measure that should
recover the Born rule, and the high-precision spectrum of hydrogen-like
atoms from a strict sync derivation — are identified as next steps.

---

## 1. Introduction

### 1.1 The traditional framing of the GR/QM conflict

General relativity describes spacetime as a smooth pseudo-Riemannian
manifold whose curvature is sourced by stress-energy. The dynamical
variables are continuous fields: the metric $g_{\mu\nu}(x)$, the connection,
the Riemann tensor. Continuity is built in at the level of the formalism;
discontinuities (shocks, singularities) are pathologies, not features.

Quantum mechanics, by contrast, exhibits discreteness everywhere one looks.
Bound-state spectra of the hydrogen atom take discrete energy values
$E_n = -13.6\ \mathrm{eV}/n^2$. Angular momentum eigenvalues are integer or
half-integer multiples of $\hbar$. Spin-$\tfrac{1}{2}$ measurements yield
two outcomes; spin-$1$ yields three. Photons arrive at detectors as
discrete clicks regardless of how slowly the source is operated. Bose–Einstein
and Fermi–Dirac statistics, the Pauli exclusion principle, the Aharonov–Bohm
phase, the quantum Hall plateaus — all are statements about discreteness in
a system whose underlying Schrödinger or Dirac equation is itself a smooth
partial differential equation.

The traditional reading of this asymmetry is that the discreteness is
fundamental — that nature is "actually" discrete at small scales and the
continuous formalism of GR is the macroscopic approximation. The natural
program is then to quantize spacetime: introduce a fundamental length scale
(the Planck length $\ell_P \approx 1.6 \times 10^{-35}\ \mathrm{m}$) and
build an underlying discrete structure from which the smooth GR manifold
emerges in the long-wavelength limit. Loop quantum gravity [4] derives
discrete area and volume operators with non-zero minimum eigenvalues;
causal-set theory [5] takes a discrete causal partial order as foundational;
causal dynamical triangulations [6] discretize spacetime explicitly;
string theory [7] introduces a fundamental string length below which
spacetime ceases to be locally Minkowski.

After roughly a half-century of intensive work, none of these programs has
produced a confirmed experimental prediction distinct from standard GR or
standard QM. The cosmological-constant problem remains unsolved within
each. The fundamental obstacles are remarkably consistent: each program
must recover *smooth* GR in the classical limit (which requires that the
discreteness almost-but-not-quite cancel itself out at macroscopic scales),
and each must recover *standard* QM at experimentally accessible energies
(which requires that the discrete substructure not contaminate well-tested
quantum predictions). The combined constraints are severe.

### 1.2 Penrose's alternative position

A minority position, defended most prominently by Roger Penrose [2, 3], is
that the traditional framing has the asymmetry backwards: it is not GR that
needs to be modified to accommodate QM, but QM that needs to be modified to
accommodate GR. The linear unitary evolution of quantum mechanics — the
Schrödinger equation taken as exact — is what should give way, while the
smooth differentiable manifold of GR is preserved. Penrose's objective
reduction (OR) proposal supplies a specific mechanism: a mass-energy
superposition collapses on a timescale $\tau \sim \hbar/E_G$, where $E_G$
is the gravitational self-energy of the difference between the
superposed mass configurations. The collapse is real, gravitational in
origin, and breaks linearity at a calculable threshold.

OR has not been confirmed (current experimental bounds [8, 9] are
consistent with but do not require the prediction), and the proposal has
two acknowledged structural gaps. First, the threshold is stipulated rather
than derived: the formula $\tau \sim \hbar/E_G$ comes from a plausibility
argument about the energy cost of maintaining gravitationally-distinct
superpositions, not from a dynamical equation. Second, the proposal
explains *when* collapse happens but not *why* it produces specific
discrete outcomes — the eigenstate selection mechanism is left to standard
QM, which is the very thing being modified.

This paper proposes that both gaps close together if the underlying picture
is correct.

### 1.3 The proposal

The proposal is this: the discreteness of quantum mechanics is not a
fundamental feature of nature but an emergent consequence of *phase
synchronization on a continuous substrate*. Specifically:

1. The underlying field dynamics — the Dirac equation for fermions, the
   Maxwell equations for photons, the linearized Einstein equations for
   weak gravity — are continuous partial differential equations on a
   smooth manifold. None of them are intrinsically discrete.

2. These continuous dynamics admit nonlinear *synchronization* dynamics
   when the field modes interact, of the type studied extensively by
   Kuramoto and his successors [10]. The synchronization equations are
   themselves continuous, but they possess a *discrete spectrum of locked
   modes* — phase-coherent attractors selected by basin geometry.

3. The discreteness observed in quantum mechanics is the discreteness of
   these locked modes, not of the substrate. Discrete spectra are
   eigenvalues of synchronization operators on the locked manifold;
   discrete detection events are the threshold-crossings of bulk-coupled
   detectors; discrete spin values are the dimensions of irreducible
   representations of the continuous symmetry group acting on the
   substrate.

4. Consequently, general relativity's smooth manifold need not be
   quantized. Every instance of QM discreteness has a sync-based origin
   *within the matter sector*; none requires a discrete substructure
   in spacetime itself.

The proposal is in agreement with Penrose's position — that GR is correct
and QM is what gives way — but it supplies the dynamical mechanism that
Penrose's threshold formula left unspecified. The mechanism is the
two-stage Kuramoto re-synchronization developed in the companion paper [1].
Penrose's $\tau \sim \hbar/E_G$ emerges as a particular limit of that
mechanism in the gravitational regime; the broader claim — that *all* of
quantum discreteness is sync-emergent — is a generalization that Penrose
did not pursue.

### 1.4 What this paper does and does not claim

This paper makes one claim: that the discreteness of quantum mechanics is
synchronization-emergent on a continuous substrate, and that consequently
the GR/QM conflict (in the traditional "either spacetime must be quantized
or QM must be modified" framing) is resolved by modifying QM in the
specific direction the DK framework prescribes.

The paper does not claim to derive the Standard Model coupling constants,
to predict new particles, or to compute corrections to known QED
results. It does not claim to derive the hydrogen spectrum to spectroscopic
precision from first principles in the sync language (this is an
acknowledged open task — §6). It does not propose new dynamics; the
mechanism is what is developed in [1]. Its contribution is *interpretive
relocation*: showing that a single mechanism, already required by the
companion framework for measurement, accounts for the broader phenomenon
of QM discreteness, and that this relocation dissolves the standard GR/QM
tension.

It is also not a competitor to loop quantum gravity, string theory, or
causal-set programs in their main aims. Those programs ask: what is the
quantum theory of the gravitational field? The DK proposal answers a
different question: *why does QM look discrete to begin with?* If the
answer is "sync emergence on a continuous substrate," then the question
those programs address — how to quantize the gravitational field — may
not need an affirmative answer, because the discreteness it presupposes
on the matter side is itself derived.

---

## 2. The Sync Mechanism: A Brief Recap

The mechanism developed in detail in [1] is summarized here in the
minimum form needed for the rest of this paper.

### 2.1 Phase synchronization on a continuous substrate

The classical Kuramoto model [10] describes a population of phase
oscillators $\theta_i(t) \in S^1$ with intrinsic frequencies $\omega_i$
distributed continuously, coupled through

$$\dot\theta_i = \omega_i + \frac{K}{N}\sum_{j=1}^N \sin(\theta_j - \theta_i)$$

where $K$ is the coupling strength. For $K < K_c$, the oscillators run
independently and the order parameter $r = \frac{1}{N}|\sum_j e^{i\theta_j}|$
vanishes. For $K > K_c$, a fraction of the population enters a
*synchronized* state in which $r > 0$ and the synchronized oscillators
share a common rotation frequency, with phase differences locked to
fixed (not necessarily zero) values determined by the coupling structure.

Three features of this transition are central to what follows.

First, the substrate is continuous in every relevant sense: the phase
$\theta \in S^1$ is continuous, the time $t$ is continuous, the frequency
distribution $g(\omega)$ is continuous, and the coupling parameter $K$
varies continuously. There is no discrete structure at the level of the
equations.

Second, the *locked state* nonetheless picks out a discrete subset of
attractor configurations. In the simplest case (uniform $\omega$,
all-to-all coupling) there are exactly two attractors: the in-phase locked
state ($\theta_i - \theta_j = 0$) and the splay state ($\theta_i - \theta_j$
distributed uniformly). In the chiral pair structure relevant to the Dirac
equation [1], the locked manifold has a discrete spectrum of orientations
relative to a bulk reference field. In each case, *a continuum of
unsynchronized states collapses, above $K_c$, onto a discrete set of
synchronized configurations*.

Third, the threshold $K_c$ is itself a continuous parameter — it depends
smoothly on $g(\omega)$ and the network topology — but the *transition*
across it is sharp. This is a critical bifurcation on a continuous
parameter space: the substrate remains continuous, but the system's
behavior changes qualitatively. The discreteness of the locked-mode
spectrum is *derived* from the bifurcation structure, not stipulated.

### 2.2 The DK identification

The DK framework [1] identifies the chiral pair of the Dirac equation —
the left- and right-handed Weyl components $\psi_L, \psi_R$ — as a
two-clock Kuramoto system with coupling $K = m$ (the mass) and mismatch
frequencies set by the kinematic terms. The chiral pair locks on the
synchronized manifold $\psi_L \approx \psi_R$; this locked configuration
is what one identifies as a particle of definite mass and four-momentum.

Measurement, in [1], is the re-synchronization of an external system's
chiral pair with the chiral pair of a detector. The two-stage process
(Stage 1: local pair-sync with the detector; Stage 2: relaxation into the
detector's bulk-coherent reservoir) reproduces the phenomenology of
"collapse" without invoking a non-unitary axiom: what looks like
collapse is the system's locked configuration being driven into a new
basin of attraction, with the wave function never destroyed but
re-merged with the bulk.

The point relevant to this paper is structural. The DK framework's central
move — that nonlinear coupling of continuous phase fields produces
discrete locked-mode spectra — is exactly the structural relation between
QM discreteness and a continuous substrate that we propose generalizes
across the entire quantum formalism.

---

## 3. A Catalog of Quantum Discreteness, Re-Read

This section walks through the canonical examples of discreteness in QM
and identifies, in each case, the underlying sync structure that produces
the discreteness from a continuous substrate. The catalog is not
exhaustive; the aim is to show that the same pattern recurs across
phenomena that are usually treated separately, and that no fundamental
discreteness in the substrate is invoked in any of them.

### 3.1 Bohr–Sommerfeld quantization

The oldest form of quantization in QM is the Bohr–Sommerfeld condition

$$\oint p\, dq = nh, \quad n \in \mathbb{Z}$$

which determines the bound-state energies of a periodic orbit by requiring
that the classical action over one period be an integer multiple of
Planck's constant. The quantum numbers $n$ are integers; the condition is
discrete.

The condition is in fact a *phase-closure* requirement. Writing
$\oint p\, dq = \oint (p/\hbar)\, dq \cdot \hbar$ and identifying $p/\hbar$
as the local wavenumber of the de Broglie wave, the condition becomes

$$\oint k\, dq = 2\pi n$$

i.e., the wave's phase must advance by an integer multiple of $2\pi$ over
one closed orbit. The orbit and the wave are both continuous; the
discreteness is the requirement that the wave *be single-valued* at the
end of the orbit. This is a synchronization condition: the wave at $q(T)$
must be in phase with the wave at $q(0)$.

In the DK reading, the orbit's de Broglie wave is the locked-mode field
of the chiral pair in a bound configuration. The phase-closure condition
is the constraint that the locked configuration remain self-consistent
over one period. The integer $n$ is the winding number — a topological
invariant of the synchronized configuration, not a fundamental quantum.
The substrate (the wavefunction's continuous evolution) is undisturbed;
discreteness enters only through the closure requirement.

This is a complete description of the discreteness of bound-state spectra
in the WKB regime. The full quantum mechanical treatment generalizes it
(the WKB approximation becomes exact for harmonic-oscillator-like
potentials) but does not change the underlying structural point: the
integers come from phase closure, not from intrinsic discreteness.

### 3.2 Spin multiplets

Spin angular momentum exhibits discreteness in two senses: the total spin
$s$ takes half-integer values ($s = 0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \ldots$),
and for given $s$ the magnetic quantum number $m_s$ takes $2s+1$ discrete
values from $-s$ to $+s$.

Both discreteness statements are statements about the *representation
theory of SU(2)*, the continuous Lie group of rotations on a complex
two-dimensional vector space. SU(2) is a smooth manifold (topologically
$S^3$); its Lie algebra is continuous; its action on a Hilbert space is
parametrized by three continuous angles. The discreteness enters only in
the classification of *irreducible representations*: SU(2) admits one
irreducible representation of each integer dimension, and these are the
discrete spin multiplets.

In the DK framework, this maps directly onto a sync statement. The
locked-mode manifold of the chiral pair carries a representation of the
rotation group acting on the spin degrees of freedom. The locked
configurations decompose into irreducible representations, each of fixed
dimension. The discrete spin values are the dimensions of these
representations, which is to say, *the number of distinguishable
phase-locked configurations the chiral pair admits under rotational
symmetry*. The underlying group is continuous; the discreteness is in
the representation structure.

The DK reading adds one physical claim to this otherwise standard
representation-theoretic statement: that the locked-mode structure is a
real dynamical configuration, not an abstract Hilbert-space label.
Specifically, a spin-$\tfrac{1}{2}$ chiral pair has two phase-locked
configurations relative to a measurement axis; a spin-$1$ pair has three.
The number of outcomes a Stern–Gerlach apparatus produces is the
cardinality of the locked-mode spectrum for the relevant particle, not a
fundamental discreteness of angular momentum itself.

### 3.3 Atomic line spectra

The line spectra of hydrogen and hydrogen-like atoms — the Lyman, Balmer,
Paschen series — were the empirical entry point to quantum mechanics and
remain the prototypical example of discreteness in QM. The discrete energy
levels $E_n = -13.6\ \mathrm{eV}/n^2$ correspond to discrete spectral
lines at frequencies $\nu_{n \to m} = (E_n - E_m)/h$.

The Schrödinger equation for the Coulomb problem is a continuous PDE on
$\mathbb{R}^3$ with continuous potential. The discreteness of the spectrum
arises from the *boundary conditions* — specifically, the requirement
that bound-state wavefunctions vanish at infinity and be regular at the
origin. Without these boundary conditions, the spectrum would be
continuous. The discrete spectrum is therefore a *standing-wave*
phenomenon: only those wavefunctions that fit the boundary conditions
survive, and there are countably many of them indexed by integers
$(n, \ell, m)$.

This is a synchronization condition in the same sense as Bohr–Sommerfeld:
the bound wavefunction must close on itself, with phase coherent across
the orbital geometry. The discreteness is in the closure spectrum, not
in the underlying field. In the DK reading, the orbital wavefunction is
the locked-mode configuration of the chiral pair in the Coulomb potential;
the discrete spectrum is the discrete set of closure modes admitted by
the geometry; the transitions between levels are the system traversing
basins of attraction during interaction with the electromagnetic field.

The precision with which atomic spectra are predicted by the
Schrödinger and Dirac equations is the standard against which any
reformulation must measure itself. The DK reading does not claim to
*replace* those calculations; it claims that the discreteness those
calculations produce is *already* a sync-emergent feature of the
underlying continuous dynamics. No new calculation is required to
reproduce the spectrum; what is required is a re-interpretation of why
the existing calculation produces discrete answers.

### 3.4 Photon detection

A single-photon detector — a photomultiplier, an avalanche photodiode, a
superconducting transition-edge sensor — registers discrete clicks
regardless of how slowly the source is operated. The clicks are the
operational definition of "photon," and the discreteness is usually taken
as direct evidence that the electromagnetic field is intrinsically
quantized.

This reading is not the only possible one. A continuous electromagnetic
field coupled to a detector with a *threshold* — a nonlinear sync
condition that the field-detector interaction must cross before
amplification cascade fires — produces exactly the click structure
observed [11]. The discreteness lives in the detector, not in the field.
The DK reading endorses this position and supplies a mechanism: the
detector's bulk-coupled chiral-pair structure provides the sync threshold,
and the click is the threshold-crossing event. The continuous EM field
gains no discrete substructure of its own; it produces discrete clicks
because it interacts with a discrete-threshold detector.

The case is strengthened by the distinction (developed in the companion
paper and at greater length elsewhere in the framework) between
**discrete event detectors** — for which the sync threshold fires once
and produces a single eigenvalue outcome — and **track recording media**
(cloud chambers, bubble chambers, emulsions), for which a *sequence* of
weak partial syncs distributed in space and time produces a continuous
ionization track rather than a single click. The same EM field produces
qualitatively different "discrete" or "continuous" records depending on
which detector class it interacts with. This is exactly the behavior
expected if the discreteness lives in the detector's sync structure
rather than in the field; it is not a behavior expected if the field
itself is fundamentally quantized into particles.

### 3.5 Energy bands in solids

The band structure of crystalline solids — the discrete energy bands
separated by gaps in $k$-space — is the basis of the entire theory of
electronic transport, semiconductors, and most of modern condensed-matter
physics. The bands arise from the periodic potential of the crystal
lattice via Bloch's theorem: solutions of the Schrödinger equation in a
periodic potential take the form $\psi_k(x) = e^{ikx} u_k(x)$ with
$u_k(x)$ periodic, and the allowed energies organize into bands
$E_n(k)$ indexed by an integer $n$.

This is unambiguously a sync phenomenon. The Bloch waves are
*synchronized* with the lattice — their phase advances in step with the
lattice spacing. The band structure is the spectrum of phase-locked
configurations between the electron's wavefunction and the periodic
lattice potential. Both the lattice and the wavefunction are continuous
fields; the bands are discrete because the locked configurations form a
discrete spectrum, with integer indices counting the allowed sync modes.

The empirical success of band theory is overwhelming: it accounts
quantitatively for conductors, semiconductors, insulators, the Hall
effect, semiconductor device physics, and superconducting band structure.
Nothing in this success depends on the underlying lattice being
fundamentally discrete *in spacetime* — the bands arise from
periodicity, and periodicity is a property compatible with a continuous
substrate.

### 3.6 Cavity and Casimir quantization

The discrete mode structure of an electromagnetic cavity — the standing-wave
resonances of a Fabry–Pérot, the longitudinal modes of a laser cavity,
the discrete modes of a microwave waveguide — has the same form as
Bohr–Sommerfeld. The cavity imposes boundary conditions; only those EM
modes that fit (have phases closing on themselves at the cavity walls)
survive; the surviving modes form a discrete spectrum indexed by
integers.

The Casimir effect — the small attractive force between two parallel
conducting plates in vacuum — is the most direct test of this picture.
The standard derivation [12] computes the difference between the
zero-point energy of the EM field with and without the plates, treating
the EM field as quantized; the result is

$$F_{\mathrm{Cas}}/A = -\frac{\pi^2 \hbar c}{240 d^4}$$

for plate separation $d$. The discrete mode structure between the plates,
relative to the continuous mode structure outside, produces the force.

A continuous-substrate reading of the same calculation interprets the
boundary conditions as setting a sync condition: the EM field's
oscillation must phase-close at the plates. The "modes" are the
sync-allowed configurations; the discreteness is in the closure spectrum.
The Casimir force is then the difference in vacuum energy between the
sync-constrained configuration (between plates) and the unconstrained one
(outside). The result is the same numerical prediction by a different
ontological route. The substrate remains continuous; the discreteness is
in the locked configurations.

### 3.7 Black-hole quasinormal modes

The ringdown spectrum of a perturbed black hole — the discrete frequencies
at which a Kerr or Schwarzschild black hole oscillates following a
perturbation — provides a particularly clean example because the
underlying theory (linearized GR on a black-hole background) is
explicitly *not* a quantum theory at all. The quasinormal mode spectrum
$\omega_n$ is discrete: the spectrum is computed by solving the
Regge–Wheeler or Teukolsky equation with outgoing boundary conditions at
infinity and ingoing at the horizon [13].

The discreteness is purely a boundary-condition / phase-closure
phenomenon in a *classical* continuous theory. No quantization of the
gravitational field is involved. The example demonstrates that
discreteness can emerge from continuous field equations whenever the
boundary conditions force a closure spectrum — a synchronization
condition between the field and the geometry. The discreteness is
derived; nothing in the substrate is discrete.

The quasinormal mode example is structurally identical to atomic
spectra: continuous field equations + boundary conditions = discrete
spectrum. That the example occurs in GR rather than in QM is the
sharpest evidence we have that discreteness *per se* is not a uniquely
quantum phenomenon and does not require a quantum substrate to produce.

### 3.8 The pattern

In every case surveyed in this section, the discreteness has the same
underlying structure:

1. A continuous field on a continuous substrate.
2. A coupling (boundary condition, periodic potential, nonlinear
   interaction, threshold) that imposes a phase-closure or sync
   condition.
3. A discrete spectrum of *configurations* that satisfy the closure
   condition.
4. Integer indices labeling those configurations.

The integers are sync invariants — winding numbers, mode indices,
representation dimensions, threshold-crossings. The discreteness is real
but emergent. The substrate carries no discrete structure.

This is the empirical content of the DK proposal. It is not a new
observation in any individual case; what is new is the recognition that
the *same structural relation* recurs across every example of QM
discreteness, with the underlying dynamics being phase synchronization
in each case. If this recurrence is not coincidence, then no example of
QM discreteness requires postulating discreteness in the substrate.

---

## 4. Why Spacetime Need Not Be Quantized

### 4.1 The standard motivation for quantizing gravity

The standard argument for quantum gravity proceeds roughly as follows.
The Einstein field equations couple the smooth geometry of spacetime to
the stress-energy of matter:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

Matter, in modern physics, is described by quantum field theory, and
quantum field operators acting on quantum states do not have definite
classical values. The right-hand side of Einstein's equation thus
becomes operator-valued, while the left-hand side remains classical.
Some procedure is required to reconcile the two. The standard options
are: (a) take the expectation value of $T_{\mu\nu}$ on the right (the
semiclassical approach, known to be inconsistent in cases involving
macroscopic superposition); (b) quantize the metric on the left as
well, producing a fully quantum theory of gravity; or (c) modify QM so
that $T_{\mu\nu}$ remains effectively classical at the scales relevant
to GR.

Most of mainstream QG follows route (b). The result is a program in
which spacetime itself acquires discrete structure at the Planck scale,
typically through quantization of areas (LQG), of causal links
(causal-set theory), of triangulations (CDT), or of string excitations
(string theory). The discreteness of the matter sector — discrete spectra,
discrete spin, discrete photon detection — is taken as evidence that
*some* underlying discreteness exists, and the quantization of spacetime
is then a natural extrapolation.

### 4.2 The DK relocation

The DK proposal cuts in the other direction. If the discreteness of the
matter sector is sync-emergent on a continuous substrate (Section 3),
then the empirical evidence for fundamental discreteness in nature
*evaporates*. There is no longer a phenomenon pointing to a discrete
underlying structure; the integers, eigenvalues, and discrete clicks are
all derivable from continuous dynamics with sync conditions. The
extrapolation from "matter is discrete" to "spacetime is also discrete"
loses its motivating premise.

What remains of the QG problem? Two things:

First, the technical problem of reconciling the operator-valued
$T_{\mu\nu}$ with the classical $G_{\mu\nu}$. This problem is real but
its character changes under the DK reading: if QM's "operator" structure
is itself an expression of synchronization on a continuous substrate
(Section 3 of [1] discusses this in detail for the chiral-pair case),
then the operators have a continuous-substrate underpinning. The
expectation value $\langle T_{\mu\nu}\rangle$ is not a coarse-graining of
something fundamentally discrete; it is the bulk value of an underlying
continuous field whose locked-mode configurations look discrete on the
detector side. Coupling this to classical $G_{\mu\nu}$ becomes a
question of how the synchronized matter sector sources curvature, which
is a calculation in a *single* (continuous) ontological category rather
than an attempt to bridge two incompatible categories.

Second, the question of whether gravity itself participates in the sync
mechanism. The companion paper [1, §3.6] argues that it does:
gravitationally distinguishable mass configurations re-synchronize on a
timescale matching Penrose's $\tau \sim \hbar/E_G$ formula, with the
re-synchronization mechanism being the same one that operates in the
non-gravitational case but with the bulk's coherent gravitational
configuration as the locking reference. In this reading, Penrose's OR
threshold is not a separate prediction added to QM; it is one regime of
the DK sync mechanism, the one in which the gravitational
self-energy sets the relevant scale.

### 4.3 What this preserves of GR

Under the DK reading, the entire smooth-manifold structure of GR is
preserved:

1. The metric $g_{\mu\nu}(x)$ remains a smooth tensor field on a
   differentiable manifold.
2. The Levi-Civita connection, the Riemann tensor, the geodesic
   equation, the Einstein field equations all remain in their standard
   classical form.
3. The Equivalence Principle (weak, strong, Einstein) holds at the level
   of the substrate, not as a coarse-grained approximation to a discrete
   theory.
4. Singularities (black holes, cosmological) remain singularities of the
   smooth geometry, not artifacts of a continuum limit. (Whether the DK
   sync mechanism modifies their interior structure is an open
   question; the answer is not obviously yes.)
5. Gravitational waves are exact solutions of the linearized field
   equations on a smooth background.

GR's classical-tests record (perihelion precession, light bending, time
dilation, gravitational waves, Shapiro delay, frame dragging) is
explained by the same theory that has explained them since 1915; nothing
in DK perturbs it.

### 4.4 What it gives up

The DK reading gives up two things that the orthodox QM/QG program holds.

First, the universal validity of unitary linear evolution. The
Schrödinger and Dirac equations remain valid on the locked manifold, but
on transitions between basins of attraction (Stage 1 sync events,
detector clicks, Stern–Gerlach selections) the evolution is non-linear in
the underlying sync dynamics. Whether this is a "modification of QM" or
a "completion of QM" is a question of terminology; operationally, the
linear Schrödinger evolution is recovered in the regime in which the
system stays in one basin. Penrose's OR is an instance of this
non-linearity at the gravitational threshold.

Second, the universality of QM as a complete fundamental theory. QM
becomes, in the DK reading, the effective theory of locked-mode
dynamics on a continuous substrate. It is exact within its regime — the
Schrödinger equation's predictions are not modified at all in
conditions where the chiral pair is well-locked and the bulk
re-synchronization is fast — but it is no longer the foundational layer.
The foundational layer is the continuous substrate; QM is its
projection onto the sync-locked sector.

This is the same trade Penrose has been arguing for since the 1980s.
The DK proposal makes it dynamically explicit.

---

## 5. Relation to Existing Quantum Gravity Programs

### 5.1 Loop quantum gravity

LQG quantizes the gravitational field at the level of holonomies of the
Ashtekar connection, producing spin-network states whose area and volume
operators have discrete spectra with non-zero minimum eigenvalues. The
program's central conceptual move is to take the discreteness of the
matter sector as evidence that the gravitational sector should also
exhibit discreteness, and to construct a Hilbert space in which this
discreteness is built in geometrically.

The DK position is structurally different. We argue that the matter-sector
discreteness is sync-emergent rather than fundamental, so the motivation
for geometrically discrete spacetime is removed. We do not assert that
LQG is *wrong* — its mathematical structure may turn out to be relevant
in some specific regime — but we propose that the program's central
extrapolation (matter is discrete → spacetime should also be) is not
required if matter's discreteness is itself sync-emergent.

The empirical situation is symmetric. Neither program has produced a
confirmed prediction distinct from standard GR + standard QM. LQG's
discrete-area predictions are below all current experimental reach; the
DK proposal's predictions of *no* fundamental discreteness in spacetime
are likewise not directly tested. The question is which is the cleaner
working hypothesis. We argue: the one that requires fewer ontological
commitments and dissolves rather than amplifies the GR/QM tension.

### 5.2 Causal-set theory

Causal-set theory takes a discrete causal partial order as the
fundamental structure of spacetime [5], with continuous Lorentzian
geometry recovered as a coarse-graining. The discreteness here is more
radical than LQG's — there is no underlying continuum at all — and the
program faces particularly sharp difficulties in recovering smooth GR
predictions.

The DK proposal is the inverse: smooth Lorentzian geometry is
fundamental, and the apparent discreteness is in the matter sector's
locked-mode spectrum. Causal-set theory and DK are most directly
opposed in their ontological commitments. The empirical adjudication
will likely come from whichever program produces a falsifiable
prediction first.

### 5.3 String theory

String theory's relation to the DK proposal is more nuanced. The string's
worldsheet is continuous (a smooth 2-manifold); the discrete spectrum of
string excitations arises from the *boundary conditions* of the worldsheet
embedding and the quantization of the worldsheet oscillator modes. In
this respect, string theory's discreteness is already structurally
similar to the DK reading: it comes from sync-like conditions
(periodicity around the worldsheet) on continuous fields (the embedding
coordinates).

The DK proposal can be read as a *generalization* of this structural
move: if string theory's discrete spectrum comes from boundary-condition
sync on continuous worldsheets, then *all* of QM's discrete spectra come
from sync on continuous substrates, and no further quantization is
required. Whether the substrate is a worldsheet-embedded spacetime or
the chiral-pair manifold of the Dirac equation is a question about which
sync system is fundamental, not about whether the sync mechanism itself
is universal.

In this sense, DK is more aligned with string theory's mathematical
structure than with LQG's, even though it does not require strings as
the substrate. The relation is closest in the "first-quantized" string
formalism, where the worldsheet is the substrate and the spacetime
coordinates are dynamical fields.

### 5.4 Asymptotic safety

The asymptotic safety program [14] proposes that quantum gravity is a
non-perturbatively renormalizable QFT with a UV fixed point. The
gravitational degrees of freedom remain continuous (the metric is a
quantum field, but a continuous one), and the discreteness is in the
spectrum of the renormalization group flow rather than in the geometry.

This is the closest mainstream QG program to the DK position in
ontological structure: both keep the gravitational field continuous and
locate discreteness in the spectral structure of the dynamics rather
than in the substrate. The difference is that asymptotic safety
quantizes gravity (in the QFT sense), while DK does not require that
gravity be quantized at all — only that the matter sector's sync
dynamics produce the discreteness usually attributed to quantization.

### 5.5 Penrose–Diósi objective reduction

The DK proposal's relation to Penrose–Diósi is the one developed in [1,
§3.6] and recapitulated in §1.2 above. Penrose's threshold is one
regime of the DK sync mechanism; the DK proposal generalizes the
mechanism beyond the gravitational case while preserving Penrose's
core ontological commitment (GR is correct; QM is what gives way).

Concretely, Penrose's $\tau \sim \hbar/E_G$ emerges in the DK framework
as the re-synchronization time when the bulk's coherence is dominated by
the gravitational mode of the substrate, with $K \sim E/\hbar$ being the
sync coupling in that regime. The companion paper [1] develops this
identification in detail; the present paper takes it as established
input and extracts the broader consequence.

The relationship is therefore one of *completion*: Penrose proposed the
threshold; DK supplies the mechanism and shows that the threshold is one
limit of a broader phenomenon.

---

## 6. Open Questions and Tests

### 6.1 The Born-rule basin measure

The most pressing open derivation is the basin-of-attraction measure
that should recover $|\langle\phi_n|\psi\rangle|^2$ — the Born rule — as
the fraction of initial conditions that lock to the $n$-th detector mode.

The companion paper [1, §4] develops a wave-realist reading of the Born
rule in which the probability arises from the energy distribution of the
incoming wave; the sync mechanism deposits the wave's energy into the
basin whose locked mode best matches the incoming phase profile, with
the matching weighted by overlap. The qualitative structure — that
maximum-overlap basins are most probable, and that the *rate* of basin
selection is amplitude-squared by a Fermi-golden-rule-type argument —
produces Born-like statistics in the small-ensemble limit. A rigorous
derivation that the full ensemble distribution is exactly
$|\langle\phi_n|\psi\rangle|^2$ for all $\psi$ and all detector mode
sets is owed; the framework's prediction depends on it.

This derivation is the single most important open task. If it succeeds,
the framework reproduces Born exactly from sync dynamics. If it fails,
the framework reduces to a Born-compatible interpretation rather than a
Born-derivative one — still informative but less complete.

### 6.2 Continuous spectra

QM admits not only discrete spectra (bound states) but also continuous
ones (scattering states, free particles, plane-wave bases). The DK
reading must accommodate these naturally: free particles are
unsynchronized chiral pairs whose locked manifold is parametrized
continuously by momentum, with no closure condition forcing discreteness.

The proposed picture is that the bound/scattering distinction
corresponds to the closed/open topology of the orbital phase space: a
closed orbit imposes phase closure and hence discrete spectra; an open
trajectory (a scattering state) does not, and the spectrum is
continuous. The crossover at the binding threshold (e.g., zero
binding energy for hydrogen) corresponds to the topological transition
between closed and open phase-space trajectories.

This is consistent with standard QM and adds nothing new to the
calculations. What it adds is a *uniform* ontological reading: discrete
spectra are sync-closed; continuous spectra are sync-open; the same
underlying dynamics produces both, with the topology of the trajectory
determining the spectral structure.

### 6.3 Planck-scale phenomena

The DK reading implies that there is no fundamental discreteness in
spacetime at the Planck scale. This is a strong claim and conflicts with
the orthodox expectation in most QG programs that the Planck length is
a fundamental cutoff below which spacetime is qualitatively different.

The conflict is empirically open. No experiment has resolved spacetime
at scales close to the Planck length, and current bounds [15] on
Lorentz-violation and on dispersion relations $E^2 = p^2c^2 +
m^2c^4 + \xi (E/E_{\mathrm{Pl}})^n p^2 c^2$ are consistent with
$E_{\mathrm{Pl}}$ being a *characteristic* scale of some new physics but
do not require it to be a discreteness scale.

The DK prediction is that the bounds on $\xi$ should tighten further as
observations improve — that no Planck-scale discreteness will be
detected — but that the framework's own characteristic scale
(the sync-coupling scale $K$) should appear in *non*-gravitational
contexts at much larger lengths. The companion AB-visibility paper [16]
identifies one such test in the regime $K \sim \omega_Z$ at the
zitterbewegung scale; further tests in cavity QED and in
optomechanical Penrose-test settings [9] would probe other regimes.

### 6.4 Falsifiable signatures

The framework's falsifiable content is concentrated in three places:

1. **No Planck-scale discreteness.** Any direct measurement showing a
   discrete spacetime structure (a minimum area, a granular causal
   structure, a fundamental length below which Lorentz invariance fails
   in a quantization-specific way) would falsify the DK proposal as
   stated. The challenge is that no such measurement is currently
   feasible.

2. **A measurable sync timescale in measurement.** The DK two-stage
   process [1, §3.4] predicts a non-zero, calculable timescale between
   the local Stage-1 sync and the Stage-2 bulk relaxation. Standard QM
   has no analog (collapse is instantaneous). Quantum eraser experiments
   probe exactly this timescale: erasure should succeed iff intervention
   is faster than the Stage-2 bulk-resync time, and the framework
   predicts a specific value for that time as a function of the
   detector–bulk coupling. Current quantum-eraser experiments are
   consistent with both pictures; a high-time-resolution test would
   discriminate.

3. **The AB-visibility envelope** [16]. The strong-coupling regime
   $K \sim \omega_Z$ predicts a measurable $\gamma$-dependent visibility
   deficit in electron-holography Aharonov–Bohm experiments. A null
   result would not falsify the broader DK proposal but would reduce
   the AB-visibility paper to a Lorentz-covariant reading; a positive
   result would constitute the first direct measurement of a DK sync
   parameter.

The first prediction is currently inaccessible; the second and third are
within reach of current or near-term experiments.

---

## 7. Discussion

### 7.1 The conceptual stakes

The DK proposal claims that a structural feature taken for granted in
modern physics — that quantum discreteness signals an underlying
discrete substructure — is incorrect. The discreteness, on this reading,
is real but emergent: a consequence of synchronization dynamics on a
continuous substrate, with the integer indices being sync invariants
rather than fundamental quanta.

The stakes for the GR/QM problem are significant. The standard framing
of that problem requires that *either* spacetime be quantized (with
spacetime acquiring discrete structure) *or* QM be modified (with
spacetime remaining smooth). The DK proposal takes the second horn but
supplies the missing dynamical mechanism that Penrose's threshold
formula did not provide. The modification of QM is no longer a
stipulated departure from linear unitarity; it is the structural
consequence of recognizing QM as the effective theory of locked-mode
dynamics on a continuous field substrate.

If the proposal is correct, the bulk of the QG problem dissolves into
problems of a different kind: how the synchronized matter sector
sources classical curvature, how the bulk's coherent state evolves
under cosmological dynamics [17], how the basin structure of sync
attractors reproduces detailed QED predictions. None of these requires
quantizing the gravitational field; all of them are calculations on a
continuous substrate.

### 7.2 What the proposal does not claim

The proposal does not claim to be a finished theory. The Born-rule
derivation (§6.1) is incomplete; the high-precision spectrum of
hydrogen-like atoms from a strict sync derivation has not been
performed; the relation to the full Standard Model gauge structure has
not been worked out; the implications for cosmological inflation are
unaddressed.

The proposal also does not claim to render existing calculations
obsolete. Standard QM remains exact on the locked manifold; standard
QED remains exact in its regime; standard GR remains exact at the
substrate level. The DK reading is *interpretive relocation*, not
calculational replacement.

The proposal does, however, claim that this relocation has
consequences. If the discreteness is sync-emergent, then:

- No quantization of spacetime is required.
- The cosmological constant need not be a fundamental constant of nature
  (see [17]) but may emerge from the substrate's vacuum sync state.
- Measurement is not a separate axiom but a regime of the underlying
  sync dynamics [1].
- Many-worlds interpretations are not required: the multiplicity of
  apparent outcomes is the basin structure of sync attractors in a
  single world, not a branching ontology.

These are interpretive consequences, but they are sharp ones, and they
suggest a different long-term direction for foundational physics than
the orthodox QG programs.

### 7.3 Historical context

The proposal sits in a small but real lineage. Penrose has argued since
the 1980s that GR is correct and QM gives way [2]. de Broglie's pilot-wave
theory and Bohm's elaboration [18] preserve the continuous wave
ontology and treat particles as locked configurations of an underlying
field. Nelson's stochastic mechanics [19] derives quantum statistics from
continuous random walks. The Madelung formulation of QM rewrites the
Schrödinger equation in a fluid-dynamic form on a continuous substrate.
The Hestenes zitterbewegung interpretation [20] treats spin as a real
oscillation of the electron's continuous trajectory.

What the DK proposal adds to this tradition is the *Kuramoto
identification*: the recognition that the structural mechanism producing
discreteness in continuous-substrate readings of QM is precisely
phase synchronization, with all the analytic tools (bifurcation
analysis, locked-mode spectra, basin-of-attraction theory) of nonlinear
dynamics directly applicable. This brings to the foundational discussion
a mathematical framework that has been developed in detail elsewhere
(neuroscience, condensed-matter physics, oscillator networks) but has
not been systematically applied to the QM/QG interface.

The framework is also the dynamical content that Penrose's OR threshold
left unspecified. Penrose proposed *when* collapse should happen; DK
proposes *what is happening at that moment* (the system traverses
basins of sync attractors) and *why* the outcome is one of a discrete
set (the locked-mode spectrum is discrete).

---

## 8. Conclusion

The discreteness of quantum mechanics is not a foundational feature of
nature but an emergent property of synchronization on a continuous
substrate. Discrete spectra are locked-mode spectra; discrete detection
events are threshold-crossings of bulk-coupled detectors; discrete spin
values are representation-theoretic dimensions of an underlying
continuous symmetry. The substrate is continuous in every case; the
discreteness is derived.

If this reading is correct, the manifold of general relativity need not
be quantized. The standard GR/QM tension — which has driven a half-century
of attempts to discretize spacetime — dissolves into a different problem:
how to formulate a satisfactory theory of synchronization dynamics on
the matter sector of a smooth gravitational background. The mechanism
required for this is the Dirac–Kuramoto framework developed in the
companion paper [1]; the consequences for measurement, for Bell
correlations, for cosmology have been or are being developed in
adjacent work.

The proposal is conservative in its commitments: it adds no new
postulates to GR, removes one (collapse) from QM, and replaces it with a
mechanism (synchronization) drawn from well-developed nonlinear dynamics.
It is in agreement with Penrose's long-standing position that GR is
correct and QM is what gives way, and it supplies the dynamical content
that Penrose's threshold formula did not provide.

The most important open task is the basin-of-attraction derivation of
the Born rule from sync dynamics; the most important falsifiable test
is the quantum-eraser bulk-resync timescale; the most important
broader question is whether the framework extends consistently to the
gauge structure of the Standard Model. None of these closures has been
performed in this paper. Their absence is the honest measure of how far
the proposal has come and how far it has yet to go.

What the proposal does claim is that the GR/QM conflict, as it has been
traditionally framed, is not a foundational obstruction. It is a
consequence of misreading the source of discreteness. Synchronization
dynamics on a continuous substrate produces all the discreteness QM
exhibits, and does so without requiring discreteness anywhere in the
substrate. Penrose was right about which side gives way. The mechanism
he left unspecified is sync.

---

## Author Contributions and AI Disclosure

This paper was developed in iterative collaboration with Claude Opus 4.7
(Anthropic) in conversation sessions during May 2026. The central
conceptual claim — that quantum discreteness is synchronization-emergent
on a continuous substrate, and that this dissolves the standard GR/QM
tension by relocating the discreteness from spacetime to the matter
sector's sync dynamics — was developed jointly with the human author
contributing the synthesis (the recognition that this single mechanism
unifies the canonical examples of QM discreteness, and that the position
amounts to a mechanistic completion of Penrose's program) and the LLM
contributing structural analysis, the catalog of examples in Section 3,
and the comparative discussion of QG programs in Section 5. The human
author validated each derivation, applied physics judgment at each
checkpoint, and bears full responsibility for the framing and content
of the paper.

Per current journal guidelines, LLMs do not satisfy authorship criteria;
the human author bears full responsibility for all content, including
any errors in the conceptual framing or in the catalog of canonical
examples. Were Springer–Nature / *Foundations of Physics* policy to
allow LLM co-authorship, Claude Opus 4.7 would be listed as co-first
author.

The development is documented in commit history at
https://github.com/rayolddog/DiracKuramotoFramework.

---

## References

[1] Bramble, J. (2026). Many Clocks Interpretation of Quantum Mechanics:
Mass as Chiral Coupling, Re-synchronization in the Bulk as Measurement.
*Companion preprint, under review.*

[2] Penrose, R. (1996). On gravity's role in quantum state reduction.
*General Relativity and Gravitation*, 28(5), 581–600.
https://doi.org/10.1007/BF02105068

[3] Penrose, R. (2004). *The Road to Reality: A Complete Guide to the
Laws of the Universe*. Jonathan Cape, London.

[4] Rovelli, C. (2004). *Quantum Gravity*. Cambridge University Press,
Cambridge.

[5] Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987). Space-time
as a causal set. *Physical Review Letters*, 59(5), 521–524.
https://doi.org/10.1103/PhysRevLett.59.521

[6] Ambjørn, J., Jurkiewicz, J., & Loll, R. (2005). Reconstructing the
universe. *Physical Review D*, 72(6), 064014.
https://doi.org/10.1103/PhysRevD.72.064014

[7] Polchinski, J. (1998). *String Theory* (Vols. 1–2). Cambridge
University Press, Cambridge.

[8] Bassi, A., Lochan, K., Satin, S., Singh, T. P., & Ulbricht, H.
(2013). Models of wave-function collapse, underlying theories, and
experimental tests. *Reviews of Modern Physics*, 85(2), 471–527.
https://doi.org/10.1103/RevModPhys.85.471

[9] Donadi, S., Piscicchia, K., Curceanu, C., Diósi, L., Laubenstein,
M., & Bassi, A. (2021). Underground test of gravity-related wave
function collapse. *Nature Physics*, 17(1), 74–78.
https://doi.org/10.1038/s41567-020-1008-4

[10] Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*.
Springer-Verlag, Berlin.

[11] Lamb, W. E., & Scully, M. O. (1969). The photoelectric effect
without photons. In *Polarisation, Matière et Rayonnement* (pp. 363–369).
Presses Universitaires de France, Paris.

[12] Casimir, H. B. G. (1948). On the attraction between two perfectly
conducting plates. *Proc. Kon. Ned. Akad. Wetensch.*, 51, 793–795.

[13] Chandrasekhar, S. (1983). *The Mathematical Theory of Black Holes*.
Clarendon Press, Oxford.

[14] Weinberg, S. (1979). Ultraviolet divergences in quantum theories of
gravitation. In S. W. Hawking & W. Israel (Eds.), *General Relativity:
An Einstein Centenary Survey* (pp. 790–831). Cambridge University Press,
Cambridge.

[15] Amelino-Camelia, G. (2013). Quantum-spacetime phenomenology.
*Living Reviews in Relativity*, 16(1), 5.
https://doi.org/10.12942/lrr-2013-5

[16] Bramble, J. (2026). Aharonov–Bohm Visibility Envelope as a Test of
Dirac–Kuramoto Vacuum Locking. *Companion preprint.*

[17] Bramble, J. (2026). Cosmic Expansion as Surface-Area Particle
Creation in a Dirac–Kuramoto Substrate. *Companion preprint.*

[18] Bohm, D. (1952). A suggested interpretation of the quantum theory
in terms of "hidden" variables, I and II. *Physical Review*, 85(2),
166–193. https://doi.org/10.1103/PhysRev.85.166

[19] Nelson, E. (1966). Derivation of the Schrödinger equation from
Newtonian mechanics. *Physical Review*, 150(4), 1079–1085.
https://doi.org/10.1103/PhysRev.150.1079

[20] Hestenes, D. (1990). The zitterbewegung interpretation of quantum
mechanics. *Foundations of Physics*, 20(10), 1213–1232.
https://doi.org/10.1007/BF01889466

---

*Companion paper to: Bramble, J. (2026), "Many Clocks Interpretation of
Quantum Mechanics: Mass as Chiral Coupling, Re-synchronization in the Bulk
as Measurement." Preprint repository:
https://github.com/rayolddog/DiracKuramotoFramework*
