---
title: "Discretization as Synchronization: Quantum Spectra Without Quantizing Spacetime"
subtitle: "Two Continuous-Substrate Routes to Quantum Discreteness: Phase Closure and Dissipative Locking"
author: "John Bramble, MD"
date: "May 2026"
---

**John Bramble, MD¹**

¹ Independent Research

*Correspondence: rayolddog (GitHub)*

*Preprint — not yet peer reviewed*

*AI Disclosure: This work was developed in collaboration with Claude (Anthropic),
across model versions, as described in the Author Contributions section. Per
current journal guidelines, LLMs do not satisfy authorship criteria; the human
author bears full responsibility for all content.*

*Companion paper to: Bramble, J. (2026), "Two Regimes of the Chiral Mass
Coupling: Quantum Measurement as Bath-Induced Synchronization" [PAPER_REVISED,
under review].*

*Note on conventions: "synchronization"/"locking" is used here in the companion's
strict open-system, dissipative (Adler/Kuramoto) sense — discrete spectra arise from
closed-system **phase closure**, not locking (§1.3). The preferred frame, and the
Vacuum Preferred-Frame Hypothesis, enter only through the dissipative sector
(PAPER_REVISED §8).*

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

This paper proposes that the tension is misdirected, and that the discreteness
of quantum mechanics is not a fundamental feature of nature but is *derived* on
a continuous substrate by **two distinct routes** that should not be conflated.
The first is **phase closure**: the standing-wave / single-valuedness conditions
that make the spectrum of a *linear* operator discrete under boundary conditions.
This is closed-system, unitary, and entirely standard — it accounts for
Bohr–Sommerfeld quantization, atomic line spectra, energy bands, cavity and
Casimir modes, and (representation-theoretically) the spin multiplets, and it is
the *same* mechanism that makes the purely classical black-hole quasinormal-mode
spectrum discrete. No nonlinearity, dissipation, or synchronization is involved.
The second route is **dissipative locking**: the nonlinear Adler/Kuramoto
attractor that forms when an open system equilibrates to a bath. This is the
companion framework's measurement mechanism [1], and within the catalog below it
is responsible only for *discrete detection events* — the threshold-crossing of a
bulk-coupled detector that registers a definite outcome. Both routes derive
discreteness on a continuous substrate; only the second is "synchronization" in
the companion's strict (dissipative) sense.

We are explicit about what this does and does not buy. If both routes are
substrate-emergent, then the *matter-side* empirical evidence for fundamental
discreteness — the integers, eigenvalues, and clicks — no longer points to a
discrete *spacetime*, and the motivating premise of the explicitly
discrete-substrate programs (loop quantum gravity, causal sets, causal dynamical
triangulations) is removed. This is *not* a dissolution of the GR/QM problem.
String theory and asymptotic safety already keep spacetime continuous while
quantizing gravity, so the discreteness argument does not bear on them; and the
hard technical core — how a superposed matter sector sources classical curvature
(the semiclassical-gravity inconsistency) — is untouched here and remains
contingent on a measurement mechanism the companion paper leaves incomplete. The
position is *aligned* with Penrose's argument [2, 3] that general relativity is
correct and quantum mechanics is what gives way, but we do **not** claim to
supply Penrose's gravitational-collapse threshold: the companion paper explicitly
declines to derive a gravitational synchronization rate (§4.4 of [1]) and finds
its dissipative mechanism *runs out of bath* in exactly the cold, isolated regime
Penrose's objective reduction describes (§7.4 of [1]). The alignment is
ontological, not a mechanistic completion. The paper is an *interpretive
proposal*, not a complete theory; the load-bearing derivations — particularly the
basin-of-attraction measure that should recover the Born rule for the
detection route — are identified as next steps.

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

This paper speaks to the *second* gap. The dissipative-locking route (§2, §3.4)
supplies a mechanism by which a definite discrete outcome is selected — the
detector's bulk-coupled threshold — in the non-gravitational regime where a bath
is present. It does **not** close the *first* gap: the companion framework [1]
explicitly declines to derive Penrose's $\tau \sim \hbar/E_G$ threshold from its
sync dynamics, and identifies the cold, isolated, bath-free regime in which OR is
supposed to act as exactly the regime where its own dissipative mechanism has no
bath to dissipate into (§4.4, §7.4 of [1]). We therefore present the relationship
to Penrose as an *ontological alignment* (GR correct; QM gives way), not as a
derivation of his threshold.

### 1.3 The proposal

The proposal is this: the discreteness of quantum mechanics is not a
fundamental feature of nature but is *derived* on a continuous substrate, by two
distinct mechanisms that must be kept separate. Specifically:

1. The underlying field dynamics — the Dirac equation for fermions, the
   Maxwell equations for photons, the linearized Einstein equations for
   weak gravity — are continuous partial differential equations on a
   smooth manifold. None of them are intrinsically discrete.

2. **Route A — phase closure (standing waves).** Imposing boundary conditions on
   a *linear* field equation makes its spectrum discrete: only those solutions
   whose phase is single-valued (closes on itself) over the orbit, cavity, or
   periodic cell survive, and they are countable. This is closed-system, unitary,
   and dissipation-free; the integer indices are winding numbers and mode counts.
   It is standard mathematics, and it is the route behind *spectra* — bound-state
   energies, bands, cavity modes — and, representation-theoretically, the spin
   multiplets. It involves no Kuramoto coupling, no attractor, and no bath.

3. **Route B — dissipative locking (synchronization, strict sense).** When an
   *open* system equilibrates to a bath, the reduced phase acquires a nonlinear
   Adler/Kuramoto attractor and locks to a reference [10]. This is the only route
   that is "synchronization" in the companion framework's strict dissipative sense
   [1, §2.3], and within the catalog below it is responsible for *discrete
   detection events* — the threshold-crossing by which a bulk-coupled detector
   registers one definite outcome. It requires a bath, dissipation, and a
   reference axis, and the discreteness it produces is a *selection* among basins,
   not a spectrum.

4. Both routes derive discreteness on a continuous substrate. Consequently the
   matter-sector discreteness usually cited as evidence for a discrete spacetime
   has, in each case, an origin *within the matter sector* on a continuous
   substrate; none of the examples requires a discrete substructure in spacetime
   itself.

The position is *aligned* with Penrose's — that GR is correct and QM is what
gives way — and Route B supplies, for the non-gravitational case, the
outcome-selection dynamics Penrose's threshold formula left unspecified. We do
**not**, however, claim that Penrose's $\tau \sim \hbar/E_G$ emerges as a limit of
this mechanism: the companion paper [1, §4.4, §7.4] explicitly declines to derive
a gravitational synchronization rate and finds Route B has no bath to act in
exactly Penrose's regime. The alignment is ontological; the gravitational
threshold remains Penrose's to supply, not ours.

### 1.4 What this paper does and does not claim

This paper makes one claim: that the discreteness of quantum mechanics is
substrate-emergent — by phase closure (Route A) and dissipative locking (Route B)
— and that consequently the matter-sector discreteness usually offered as
evidence for fundamental discreteness does not, by itself, motivate a discrete
*spacetime*. We are careful not to overstate the consequence. This removes the
motivating premise of the explicitly discrete-substrate programs (LQG, causal
sets, CDT); it does **not** resolve the GR/QM conflict as a whole. The
continuous-spacetime quantum-gravity programs (string theory, asymptotic safety)
are untouched by a discreteness argument, and the genuinely hard part of the
problem — reconciling a superposed, operator-valued matter sector with classical
curvature — is not addressed here and depends on a measurement mechanism the
companion paper leaves incomplete (§6).

The paper does not claim to derive the Standard Model coupling constants,
to predict new particles, or to compute corrections to known QED
results. It does not claim to derive the hydrogen spectrum to spectroscopic
precision from first principles in the sync language (this is an
acknowledged open task — §6). It does not propose new dynamics; the
dissipative-locking mechanism is what is developed in [1], and the phase-closure
route is standard spectral theory. Its contribution is *interpretive relocation*:
showing that QM discreteness is substrate-emergent by these two routes, and that
this removes the matter-side motivation for a discrete spacetime — *without*
dissolving the GR/QM conflict as a whole (§4.2).

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
the left- and right-handed Weyl components $\psi_L, \psi_R$ — as two phase
clocks coupled by the off-diagonal mass term $K = m$, with mismatch
frequencies set by the kinematic terms. In the closed system this coupling is
unitary: it does not lock the two phases but sets their normal modes, and a
particle of definite mass and four-momentum is the symmetric normal mode of
the pair (the de Broglie carrier), not a synchronized configuration. Genuine
phase-locking — and with it the bifurcation structure that yields a discrete
locked-mode spectrum — appears only in the dissipative, open-system regime
that the next paragraph identifies with measurement.

Measurement, in [1], is the re-synchronization of an external system's
chiral pair with that of a detector. The two-stage process (Stage 1: fast
resonant capture by a bulk-bound partner — injection locking, an Adler
attractor; Stage 2: irreversible relaxation to the detector's bulk reference)
reproduces the phenomenology of "collapse" without a non-unitary axiom: the
system's locked configuration is driven into a new basin of attraction, the wave
function re-merged with the bulk rather than destroyed. We follow the companion's
revised account in modelling that reference honestly as a *faint, overwhelmingly
thermal bias* (parts per million, as in MRI), **not** a coherent macrostate [1,
§4.1]; the reference is a phase-synchronized bias with a definite axis, not an
"entangled bulk."

The point relevant to this paper is a precise — and limited — one. The
companion's dissipative-locking move is Route B of §1.3, and it is the origin of
*discrete detection events*: open the system to a bath and a continuum of
unsynchronized states collapses onto a discrete set of locked basins, one of
which the run selects. It is **not** the origin of discrete *spectra*. Those come
from Route A — phase closure on a *closed*, unitary, dissipation-free system —
which the companion's own §2.2 keeps rigorously distinct from locking (a closed
chiral pair has only a marginal line of fixed points, *not* a basin). Two further
distinctions matter and are easy to blur. First, the locking relevant to
measurement is the *Adler* limit — one system oscillator entraining to a *given*
bulk reference — not the full self-consistent Kuramoto transition with an
emergent order parameter and a critical coupling $K_c$; the bifurcation language
of §2.1 describes the latter, while measurement uses the former. Second, the
locked discreteness is a *selection among basins* (which outcome), whereas
spectral discreteness is an *eigenvalue count* (which level); conflating the two
is the error this paper is written to avoid.

---

## 3. A Catalog of Quantum Discreteness, Re-Read

This section walks through the canonical examples of discreteness in QM and
identifies, in each case, the continuous-substrate structure that produces the
discreteness. The aim is *not* to show that one mechanism recurs everywhere — an
earlier version of this argument overreached in exactly that way. It is to sort
the examples into the two routes of §1.3 and to be honest about which is which.
The great majority are **Route A (phase closure)**: Bohr–Sommerfeld (§3.1), the
spin multiplets (§3.2, where "closure" means the representation-theoretic
counting of SU(2)), atomic spectra (§3.3), energy bands (§3.5), cavity and
Casimir modes (§3.6), and — tellingly, in a theory that is not quantum at all —
black-hole quasinormal modes (§3.7). These are closed-system, unitary, linear
eigenvalue/standing-wave problems; no Kuramoto coupling, dissipation, or basin of
attraction appears in any of them, and the word "synchronization" is *not* used
in the companion's strict sense for any of them. Only **photon detection (§3.4)**
is Route B — the dissipative Adler/Kuramoto lock — and it is the one place the
companion mechanism does the work. Keeping these apart is the substantive content
of the catalog; the common thread is the weaker, standard statement that boundary
conditions on continuous field equations generically produce discrete spectra,
which by itself already suffices to show no discrete substrate is required.

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
end of the orbit. This is a phase-closure (single-valuedness) condition: the wave at $q(T)$
must be in phase with the wave at $q(0)$.

This is Route A in its purest form, and we are careful to label it as such. The
condition is *phase closure on a closed orbit* — a standing-wave, single-valuedness
requirement on a continuous de Broglie wave — not a dissipative lock; no bath, no
attractor, no basin is involved, and the dynamics stays unitary throughout. The
integer $n$ is the winding number, a topological invariant of the closed
configuration, not a fundamental quantum. The substrate (the wavefunction's
continuous evolution) is undisturbed; discreteness enters only through the closure
requirement. This is the *same* mechanism whether one phrases it as Bohr's
condition or as the boundary-value spectrum of the Schrödinger operator — and it
has nothing to do with the chiral-pair *locking* of the measurement route (§3.4),
which is why we no longer describe the bound de Broglie wave as a "locked mode."

This accounts for the discreteness of bound-state spectra in the WKB regime; the
full quantum-mechanical treatment generalizes it (WKB becomes exact for
harmonic-oscillator-like potentials) without changing the structural point: the
integers come from phase closure, not from intrinsic discreteness in the
substrate. We claim no new calculation here — only that the existing one already
derives its integers from a continuous wave.

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

This is Route A, and it is important to resist over-reading it as Route B. The
multiplet count $2s+1$ is fixed entirely by the representation theory of a
continuous group; it is the closure-type discreteness of an irreducible
representation, and the DK framework neither needs nor improves on that
derivation. What the dissipative-locking route *can* contribute is narrower and
should be stated precisely: it is a mechanism of **registration**, not of
counting. In a spin measurement, the spin orientation — the Pauli two-spinor
$\chi$, equivalently the Bloch/magnetization vector — relaxes dissipatively toward
the bulk reference *axis* (literally NMR $T_1/T_2$ toward $B_0$; §3.4, §4 of [1]),
and the run selects one of the stable locked orientations that axis defines. That
is how a *definite* value gets recorded from a continuous orientation.

We flag a real limit of this picture rather than paper over it. The dissipative
alignment of a magnetization toward a field is, by itself, *monostable*: a dipole
of energy $-\vec\mu\cdot\vec B$ has one stable fixed point (aligned) and one
unstable one (anti-aligned), so simple $T_1$ relaxation toward $B_0$ does not, on
its own, generate even the *two* basins a spin-$\tfrac12$ measurement needs — let
alone $2s+1$ for higher spin. The two-or-more outcome basins are a property of the
*detector's* pointer structure (its bistability or multistability), and their
*number* is fixed by the $2s+1$ eigenstates of the projected observable, which is
SU(2) representation theory (Route A). So the honest division of labor is: the
multiplet cardinality $2s+1$ is closure-type discreteness from the representation
theory, and the locking route supplies only the *registration* of one orientation
once the detector's basins exist. We do **not** claim the number of Stern–Gerlach
outcomes is "the cardinality of a locked-mode spectrum"; that earlier formulation
conflated the two routes, and the dissipative dynamics borrows the count from
representation theory rather than generating it.

A natural question is what *would* supply a second stable basin, and the answer
sharpens this limit into a concrete derivation target rather than dissolving it. On
the phase circle $S^1$ the fixed points of a gradient flow come in stable/unstable
pairs — their indices sum to $\chi(S^1)=0$ — so the monostable case is not a lone
basin but one attractor together with an antipodal repeller; a genuine *binary*
requires promoting that antipode from repeller to attractor. That promotion needs a
coupling invariant under $\phi\to\phi+\pi$, i.e. an even, second-harmonic term
$\propto\cos 2\phi$, which is the signature not of a polar (vector) coupling but of
an *apolar* one — a director $\hat n\equiv-\hat n$ coupling quadratically to the
field, $-\cos^2\theta=-\tfrac12(1+\cos 2\theta)$, as in nematic or induced-dipole
alignment. The polar dipole coupling $-\vec\mu\cdot\vec B$ is precisely the
monostable case; the bistable $0/\pi$ case is its quadratic, sign-blind counterpart.
This is why "the phase difference relaxes to $0$ or $\pi$" is not generic to coupling
at all: it presupposes the even-harmonic structure, and a first-harmonic Adler term
yields one basin, not two.

Two features of the companion framework could supply that structure, which is what
makes this a test rather than a hope. The zitterbewegung interference of the chiral
pair beats at $2m_ec^2/\hbar$ — the second harmonic of the rest-phase clock [1] —
and a coupling to it is $\cos 2\phi$ by construction; and the Stage-2 dissipative
rate is second order in the coupling (the golden-rule $\mathrm{Im}\,\Sigma\propto
|V|^2$ of [1]), hence even in the field, so the irreversible side of measurement is
exactly where an apolar term would live. This obligation can be discharged, and the
answer is a conditional *yes*. Reducing the chiral pair to a two-level system whose
relative phase $\phi$ is the equatorial Bloch azimuth ($\phi=0$ in-phase, $\phi=\pi$
anti-phase), a Lindblad dissipator $D[\sigma_x]$ — continuous *measurement* of the
$L\!\leftrightarrow\!R$ interference (mass) channel — yields the exact phase flow
$\dot\phi=-\gamma\sin 2\phi$: a pure second harmonic with stable fixed points at
*both* $\phi=0$ and $\phi=\pi$ and repellers at $\pm\pi/2$. With a residual
precession $\Omega$ in the measured plane this becomes a second-harmonic Adler
equation $\dot\phi=\Omega-\gamma\sin 2\phi$, which locks to two antipodal phases
precisely when the measurement dominates, $|\Omega|<\gamma$ (we carry out the
reduction, fixed-point classification, locking tongue, and a quantum-trajectory
confirmation in the supplementary `code/phi_dissipative_check.py`). The condition is
the substance: $D[\sigma_x]$ is quadratic in $\sigma_x$ and hence even under
$\phi\to\phi+\pi$, so it carries the apolar second harmonic, whereas *polar*
relaxation toward a fixed axis (amplitude damping toward a single pointer) gives the
first-harmonic flow $\dot\phi\propto-\sin\phi$ and the single basin of the
monostable case above. This also sharpens the relation to the companion's §2.3,
whose dissipative reduction is written in the first-harmonic form
$\dot\phi=\omega+K\sin(\Phi_{\text{bulk}}-\phi)$ — injection-locking to a *biased*
(polar) reference, which is monostable and selects a single phase; the bistable
$0/\pi$ binary instead requires the *apolar* coupling, a symmetric measurement of
the interference observable, and the two are different bath couplings rather than
the same one. We stress that even so, the result secures only the *stability of a
binary*, not its cardinality —
the basin count remains $2s+1$ from representation theory, as above — nor the
*weights* with which the basins are selected, which remain the open Born-measure
problem of §6.1. This is therefore a narrowing of the registration story (a
candidate for why the selected values are the antipodal, maximally distinct ones)
and not a revival of the withdrawn claim that locking generates the count.

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

This is a phase-closure condition in the same sense as Bohr–Sommerfeld: the bound
wavefunction must close on itself, with phase coherent across the orbital
geometry. The discreteness is in the closure spectrum, not in the underlying
field — Route A throughout. We keep two things separate that are easy to merge.
The *spectrum* (the discrete set of levels) is the closure spectrum admitted by
the Coulomb geometry, a closed-system unitary eigenproblem; it is **not** a
locked-mode spectrum and involves no bath. A *transition* between levels is driven
by coupling to the electromagnetic field, and the discreteness of the line is just
the difference of two closure energies. Only the eventual *detection* of the
emitted photon — its registration as a click — is a Route-B dissipative-locking
event (§3.4). So atomic spectroscopy mixes both routes, but cleanly: closure sets
the level structure, locking registers the photons that report transitions
between levels.

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

This is Route A — a phase-closure (commensurability) phenomenon, not a dissipative
lock. The Bloch phase advances *in step with* the lattice period, which is a
single-valuedness condition on a continuous wave in a periodic potential, and the
band index $n$ counts the closure modes the periodicity admits. We deliberately do
**not** call this "synchronization" in the companion's strict sense: there is no
bath, no dissipation, and no attractor; the Bloch spectrum is the eigenvalue
spectrum of a closed, unitary, linear operator. Both the lattice and the
wavefunction are continuous fields, and the bands are discrete for the same reason
the hydrogen levels are — boundary/periodicity conditions on a continuous PDE —
which is all the thesis needs: periodicity is fully compatible with a continuous
substrate.

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

A continuous-substrate reading of the same calculation interprets the boundary
conditions as a phase-closure condition (Route A): the EM field's oscillation must
close on itself at the plates. The "modes" are the closure-allowed configurations;
the discreteness is in the closure spectrum. The Casimir force is then the
difference in vacuum energy between the closure-constrained configuration (between
plates) and the unconstrained one (outside). The result is the same numerical
prediction by a different ontological route. The substrate remains continuous; the
discreteness is in the standing-wave spectrum — no dissipative locking, no bath,
and (as in every Route-A case) no need to call this "synchronization" in the
strict sense.

### 3.7 Black-hole quasinormal modes

The ringdown spectrum of a perturbed black hole — the discrete frequencies
at which a Kerr or Schwarzschild black hole oscillates following a
perturbation — provides a particularly clean example because the
underlying theory (linearized GR on a black-hole background) is
explicitly *not* a quantum theory at all. The quasinormal mode spectrum
$\omega_n$ is discrete: the spectrum is computed by solving the
Regge–Wheeler or Teukolsky equation with outgoing boundary conditions at
infinity and ingoing at the horizon [13].

The discreteness is purely a boundary-condition / phase-closure phenomenon in a
*classical* continuous theory. No quantization of the gravitational field is
involved — and, equally to the point, no synchronization: there is no Kuramoto
coupling, no bath, and no attractor anywhere in a quasinormal-mode calculation.
The discreteness is derived; nothing in the substrate is discrete.

This example does double duty, and the second duty is a check on our own thesis.
It is structurally identical to atomic spectra — continuous field equations +
boundary conditions = discrete spectrum — which shows that discreteness *per se*
is not a uniquely quantum phenomenon and needs no quantum substrate to produce.
But it also shows that the honest common factor across Route A is *phase closure*,
not *synchronization*: a purely classical, dissipation-free GR computation
delivers a discrete spectrum with none of the Kuramoto machinery, so attaching
"locked-mode" or "sync" language to the Route-A examples would be importing a
mechanism (dissipative locking) that demonstrably is not present in the cleanest
member of the family. We let the quasinormal-mode case discipline the vocabulary
of the whole section.

### 3.8 The pattern

Across the cases surveyed, the discreteness shares a *weak* common structure and
splits on a *strong* one. The weak common structure — all that the thesis
actually requires — is:

1. A continuous field on a continuous substrate.
2. A condition (boundary condition, periodicity, threshold) selecting a
   countable subset of configurations.
3. Integer indices labeling them.

The discreteness is real but emergent, and the substrate carries no discrete
structure. That much holds in every case, and it already suffices to show that no
example forces a discrete spacetime.

Where the cases differ is the *mechanism* of step 2, and this is the distinction
the section exists to draw. In Route A — Bohr–Sommerfeld, spin multiplets, atomic
spectra, bands, cavities, quasinormal modes — the condition is **phase closure**:
single-valuedness / standing-wave conditions on a *linear, closed, unitary*
system. The integers are winding numbers, mode counts, and representation
dimensions; there is no bath, no dissipation, and no attractor, so this is not
"synchronization" in the companion's strict sense. In Route B — photon detection —
the condition is a **dissipative Adler/Kuramoto lock** in an *open* system, and the
discreteness is a selection among basins. Honesty about this split is the whole
point: an earlier framing claimed "the underlying dynamics is phase synchronization
in each case," and that is not true. Most of QM's discreteness is closure, not
locking. What the catalog establishes is the weaker and more secure claim — that
*both* routes derive discreteness on a continuous substrate — not the stronger and
false claim that one sync mechanism underlies them all.

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

The DK proposal cuts against one specific link in that chain. If the discreteness
of the matter sector is substrate-emergent (Section 3), then the integers,
eigenvalues, and clicks no longer point to a discrete *substructure*, and the
extrapolation from "matter is discrete" to "spacetime is also discrete" loses its
motivating premise. We are careful about the size of this conclusion. It tells
against the explicitly **discrete-substrate** programs — LQG, causal sets, CDT —
whose central move is exactly that extrapolation. It does **not** tell against the
*continuous*-spacetime quantum-gravity programs (string theory, asymptotic
safety), which never relied on matter discreteness, and it does not by itself
remove the need for a quantum theory of gravity. "Must spacetime be discrete?" and
"must gravity be quantized?" are different questions; Section 3 bears on the first,
not the second.

What remains of the QG problem is therefore most of its hard core, and we do not
claim to dissolve it. The genuinely difficult piece is reconciling an
operator-valued, superposable $T_{\mu\nu}$ with a classical $G_{\mu\nu}$ — the
semiclassical-gravity inconsistency (Eppley–Hannay, Page–Geilker): a mass in
superposition has no single classical stress-energy to source curvature. The DK
reading *reframes* this rather than solving it. If measurement keeps the matter
sector effectively localized — if the dissipative-locking mechanism of [1] drives
a superposition into one definite basin fast enough — then $T_{\mu\nu}$ is
effectively classical at the scales where it sources curvature, and semiclassical
gravity could be self-consistent without quantizing the metric. That is the
Penrose-style escape, and it is genuinely attractive. But it is *contingent on the
measurement mechanism actually working*, which is to say on the two derivations
the companion paper lists as unsolved — the Born measure and an explicit selection
law (§6, and §7.3/§8 of [1]). Until those close, "the conflict dissolves" is an
overstatement; the honest claim is "the matter-side motivation for discrete
spacetime is removed, and a continuous, Penrose-aligned resolution becomes
*available* if the measurement problem is solved."

Whether gravity itself participates in the locking mechanism we leave open, and
here we correct an earlier version of this paper. We do **not** claim that
Penrose's $\tau \sim \hbar/E_G$ is a limit of the DK mechanism. The companion paper
in its current form declines to derive a gravitational synchronization rate at all
— it shows that the naive $\Gamma_{\rm grav}\sim GM^2/(\hbar\,\Delta z)$ is a
dimensional artifact, not a physical rate (§4.4 of [1]) — and it identifies the
cold, isolated, mesoscopic regime in which Penrose's objective reduction is
supposed to act as precisely the regime where the DK dissipative mechanism *has no
bath to dissipate into* (§7.4 of [1]). So in the gravitational regime the two
proposals diverge rather than nest: MCI's mechanism runs out of bath there, while
Penrose's intrinsic threshold does not. Penrose's OR is best read as a *rival*
candidate for that regime, not a special case of DK. The alignment we do claim is
ontological — GR correct, QM gives way — not a derivation of his threshold.

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

First, the universal validity of the *closed-system linear* Schrödinger
description as an account of measurement. We are careful to state this in a way
consistent with the companion, which is **no-collapse**: the global evolution
stays exactly unitary, with the coherence scrambled irreversibly into the bath
rather than destroyed (§3.1, §7.4 of [1]). What is given up is not global
unitarity but the idea that the *closed, linear* Schrödinger equation describes an
open measurement: once the bath is traced out, the reduced dynamics on transitions
between basins (detector clicks, Stern–Gerlach selections) is effectively
non-linear and dissipative. Operationally the linear Schrödinger evolution is
recovered whenever the system stays in one basin. This is the standard
open-systems statement, not a new non-unitary axiom. Penrose's OR, by contrast,
posits a *genuinely* non-unitary, intrinsic collapse at the gravitational
threshold — a different and stronger move than the effective, bath-induced
non-linearity here — so we treat OR as a rival reading of the gravitational
regime, not an instance of the DK mechanism.

Second, the universality of QM as a complete fundamental theory. In the DK
reading the foundational layer is the continuous substrate; QM's *closed-system*
content (unitary evolution and the closure spectra of Route A) is the substrate's
continuous dynamics read off directly, and QM's *measurement* axiom is the
effective description of Route-B dissipative locking. The Schrödinger equation's
predictions are not modified at all in conditions where the system stays well
inside one basin; what changes is the status of the projection postulate, which
becomes a derived (if still incompletely derived) consequence of locking rather
than a separate axiom.

This is the same ontological trade Penrose has argued for since the 1980s — GR
correct, QM what gives way. The DK proposal supplies a *candidate* dynamical
content for the non-gravitational case; it does not yet supply it for the
gravitational threshold, which is exactly the part the companion paper leaves
open (§4.4, §7.4 of [1]).

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
required if matter's discreteness is itself substrate-emergent (by phase closure
or dissipative locking).

The empirical situation is symmetric. Neither program has produced a
confirmed prediction distinct from standard GR + standard QM. LQG's
discrete-area predictions are below all current experimental reach; the
DK proposal's prediction of *no* fundamental discreteness in spacetime
is likewise not directly tested. The question is which is the cleaner
working hypothesis for the *discrete-substrate* issue specifically. We argue: the
one that requires fewer ontological commitments and removes, rather than
amplifies, the matter-side motivation for discretizing spacetime — granting that
neither this nor LQG settles whether gravity must be quantized continuously.

### 5.2 Causal-set theory

Causal-set theory takes a discrete causal partial order as the
fundamental structure of spacetime [5], with continuous Lorentzian
geometry recovered as a coarse-graining. The discreteness here is more
radical than LQG's — there is no underlying continuum at all — and the
program faces particularly sharp difficulties in recovering smooth GR
predictions.

The DK proposal is the inverse: smooth Lorentzian geometry is
fundamental, and the apparent discreteness is in the matter sector — its closure
spectra and its detection basins. Causal-set theory and DK are most directly
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

The DK proposal's relation to Penrose–Diósi is the one developed in [1, §7.4],
and it is a *contrast*, not a subsumption — an earlier version of this section
mis-stated it as a completion, and we correct that here. The two frameworks share
one commitment (GR is correct; QM is what gives way) and single out the same
physical step (the bulk re-establishment of classicality). They part company on
two points that are decisive in exactly the gravitational regime:

- **Collapse vs no-collapse.** Penrose–Diósi is an objective *collapse* theory: it
  modifies Schrödinger evolution and the superposition is genuinely destroyed. MCI
  is no-collapse: the global evolution stays unitary and the coherence is scrambled
  into the bath (§3.1, §7.4 of [1]).
- **What each asks of the environment.** MCI's lock is *dissipative* and needs a
  bath to carry the phase mismatch into a continuum; Penrose's reduction is
  *intrinsic* and needs no environment at all.

In the deep Penrose regime — cold, isolated, mesoscopic, with the electromagnetic
and thermal channels deliberately removed — this distinction is sharp: the bath
MCI would dissipate into has been engineered away, and the companion paper does
**not** assert a gravitational dissipation channel to replace it (§4.4 of [1]). So
that regime is where MCI's mechanism *runs out of bath* while Penrose's intrinsic
one does not — which makes it the experimental **arbiter** between the two, not a
place where one contains the other. We therefore do not claim that
$\tau \sim \hbar/E_G$ emerges as a DK limit, and we do not present DK as a
completion of Penrose; we present the gravitational regime as the clean test that
would distinguish a continuous, no-collapse reading from an objective collapse.

---

## 6. Open Questions and Tests

### 6.1 The Born-rule basin measure

The most pressing open derivation is the Born measure: that the long-run selection
frequencies are $|\langle\phi_n|\psi\rangle|^2$. It is important to say what this is
*not*. It is not the basin-of-attraction *volume* — the fraction of initial
relative-phases that flow to each well — which for the bistable lock of §3.2 is
demonstrably $50/50$, independent of $|\alpha|^2$ (`code/born_weights_check.py`). The
squared weights are recovered only when the $|\cdot|^2$ measure is placed on the
*ensemble* (the selecting noise, equivalently the golden-rule rate
$\propto|\langle\phi_n|\psi\rangle|^2$); what is owed is a justification of *that
measure*, since the attractor geometry does not carry it.

The companion paper [1, §7.3, §8] carries this as an explicitly *unsolved*
problem, and we adopt its honest framing rather than a more optimistic one. A
wave-realist reading in which the basin selected has maximum overlap with the
incoming phase profile gives the right *ordering* of probabilities, but it does
not by itself give the squared measure: reading $|\psi|^2$ as the energy density
of a real field coincides with the occupation fraction only by normalization and
so "explains nothing about outcome statistics" for the equal-energy channels at
issue, and a genuinely unbiased background would weight basins by their measure —
tending to equal odds — rather than by $|\alpha|^2$. This is the "why squared"
gap, the framework's counterpart of Bohm's quantum-equilibrium assumption, and it
is shared with the contested branch-counting derivations. A rigorous derivation
that the ensemble distribution is exactly $|\langle\phi_n|\psi\rangle|^2$ for all
$\psi$ and all detector mode sets is owed; the framework's claim to *derive*
(rather than merely accommodate) Born depends on it.

This derivation is the single most important open task. The dynamics supplies one
half of it — *equivariance*: the projector weight $|\langle\phi_n|\psi\rangle|^2$ is
conserved under the lock, so a $|\cdot|^2$ measure granted at preparation propagates
intact to the outcome, the status of Bohm's quantum equilibrium. What it does not
supply is *typicality* — nothing makes an arbitrary ensemble relax *to* that measure,
and inserting it is what every route (Bohm, Zurek envariance, decision-theoretic
Everett) ultimately does. If that missing half succeeds, the framework reproduces
Born exactly from sync dynamics; if it fails, the framework reduces to a
Born-compatible interpretation rather than a Born-derivative one — still informative
but less complete.

A concrete candidate for that missing *typicality* half is now in hand
(`code/born_substrate_sampling.py`; companion [1] §8). If selection is not basin-volume
flow but *competition among threshold detectors*, each driven **linearly** by the local
wave amplitude, then a random-phase (equilibrium) bulk makes the per-detector firing rate
go as the delivered **power**, $|\psi|^2$ — the squaring appearing as the first
non-cancelling term of the phase average, not inserted as a golden-rule postulate. This
*sharpens* the gap rather than closing it: it locates the weight in the drive **amplitude**
rather than the basin **geometry**, so the "an unbiased background would give equal odds"
objection above — a statement about basin *volume* — does not apply to the
detector-competition channel; but it still **assumes** the bulk's random-phase equilibrium
(Bohm's quantum-equilibrium in this setting) and **breaks** Born predictably once that
equilibrium is spoiled (strong drive, or a coherent bulk). It is a candidate for
typicality, not a proof that the sync dynamics relaxes to it.

### 6.2 Continuous spectra

QM admits not only discrete spectra (bound states) but also continuous
ones (scattering states, free particles, plane-wave bases). The DK
reading must accommodate these naturally: free particles are the unitary
normal-mode states of the chiral pair, parametrized continuously by momentum,
with no closure condition forcing discreteness.

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
   process [1, §3.1, §3.2] predicts a non-zero, calculable timescale between
   the fast Stage-1 resonant capture and the slower Stage-2 bulk relaxation.
   Standard QM has no analog (collapse is instantaneous). Quantum eraser experiments
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

The stakes for the GR/QM problem are real but narrower than an earlier draft
claimed. The standard framing requires that *either* spacetime be quantized *or*
QM be modified. The DK proposal leans toward the second horn — but it supplies a
candidate dynamical mechanism only for the *non-gravitational* measurement case
(Route B), and explicitly not for Penrose's gravitational threshold, which the
companion leaves open (§4.4, §7.4 of [1]). The modification of QM it offers is the
recognition that the projection postulate is the effective description of
dissipative locking; it does not touch QM's closed-system content, which is the
Route-A closure physics.

If the proposal is correct, what changes is the *motivation*, not the difficulty,
of quantum gravity: the matter-side evidence for a discrete spacetime is removed,
so the discrete-substrate programs lose their premise, but the hard core remains.
Three problems in particular stay open and are calculations on a continuous
substrate rather than dissolved: how an effectively-localized matter sector
sources classical curvature (the semiclassical-consistency question), how the
bulk reference evolves under cosmological dynamics [17], and how the basin
structure of detection reproduces detailed QED statistics (the Born measure,
§6.1). None of these *requires* quantizing the gravitational field — but none of
them is solved here, and we present them as the residue of the problem, not its
resolution.

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

The proposal does, however, claim that this relocation has consequences. If the
discreteness is substrate-emergent, then:

- No *discrete* spacetime is required by the matter-sector evidence. (Whether
  gravity must nonetheless be *quantized* — continuously, as in string theory or
  asymptotic safety — is a separate question this paper does not settle.)
- Measurement is not a separate axiom but, in the non-gravitational case, the
  Route-B regime of dissipative locking [1] — with the caveat that the *quantitative*
  Born measure is still owed (§6.1).
- Many-worlds is not required: the multiplicity of apparent outcomes is the basin
  structure of detection attractors in a single world, not a branching ontology
  (consistent with [1, §7.2]).
- *Speculatively* — and we mark it as such, since it does not follow from the
  discreteness argument alone — the cosmological constant *might* be tied to the
  substrate's vacuum state rather than a fundamental constant (see [17]); we list
  this as a direction, not a consequence.

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
identification*: the recognition that the *measurement* step in a
continuous-substrate reading of QM is precisely dissipative phase
synchronization, with the analytic tools of nonlinear dynamics (bifurcation
analysis, Adler locking, basin-of-attraction theory) directly applicable to it.
We are careful not to over-extend the identification: it applies to the detection
route (Route B), not to the closure spectra (Route A), which are standard linear
spectral theory and borrow nothing from Kuramoto. The contribution is to bring to
the *measurement* problem a mathematical framework developed in detail elsewhere
(neuroscience, condensed-matter physics, oscillator networks) but not
systematically applied to the QM/QG interface.

What the framework adds to this lineage, for the *non-gravitational* measurement
case, is a candidate for *what is happening at the moment of registration* (the
system relaxes into one of a discrete set of detection basins) and *why* the
outcome is one of a discrete set (the basins are discrete). We are careful not to
extend this to Penrose's gravitational threshold: Penrose proposed *when* collapse
should happen in the cold, isolated regime, and the companion framework does not
reproduce that threshold (§4.4, §7.4 of [1]). The dynamical content offered here
is for the bath-coupled detector, not for the gravitational OR regime.

---

## 8. Conclusion

The discreteness of quantum mechanics is not a foundational feature of nature but
is derived on a continuous substrate by two distinct routes. Discrete *spectra* —
bound-state energies, bands, cavity modes, and (representation-theoretically) the
spin multiplets — come from **phase closure**: standing-wave, single-valuedness
conditions on linear, closed, unitary field equations, exactly as the purely
classical black-hole quasinormal spectrum does. Discrete *detection events* come
from **dissipative locking** — the Adler/Kuramoto attractor an open detector forms
with its bath — which is the only one of the two that is "synchronization" in the
companion's strict sense. The substrate is continuous in both cases; the
discreteness is derived; and the earlier claim that a single sync mechanism
underlies all of it was an overreach we have withdrawn.

The consequence for quantum gravity is correspondingly bounded. Because the
matter-sector discreteness is substrate-emergent, it no longer constitutes
evidence for a discrete *spacetime*, and the explicitly discrete-substrate
programs (LQG, causal sets, CDT) lose their motivating premise. This is not a
dissolution of the GR/QM conflict. The continuous-spacetime quantum-gravity
programs are untouched by a discreteness argument, and the hard core — how a
superposed matter sector sources classical curvature — is reframed but not solved:
a continuous, Penrose-aligned resolution becomes *available* only if the
measurement mechanism is completed, which it is not.

The proposal is conservative in its commitments: it adds no postulates to GR, and
it recasts QM's projection postulate as the effective description of dissipative
locking rather than a separate axiom — while keeping the global evolution unitary,
as the companion's no-collapse reading requires. It is aligned with Penrose's
position that GR is correct and QM is what gives way. It does **not** claim to
supply Penrose's gravitational threshold: the companion paper declines to derive a
gravitational synchronization rate and finds its dissipative mechanism runs out of
bath in exactly Penrose's regime, which makes that regime the arbiter between a
no-collapse reading and objective collapse rather than a place where one contains
the other.

The most important open task is the basin-of-attraction derivation of the Born
measure for the detection route; the most important falsifiable test is the
quantum-eraser bulk-resync timescale; the most important broader question is
whether the framework extends consistently to the gauge structure of the Standard
Model. None of these closures has been performed here. Their absence is the honest
measure of how far the proposal has come and how far it has yet to go.

What the proposal does claim is narrower than its first telling, and more secure
for being narrower: most of QM's discreteness is phase closure on a continuous
substrate, the rest is dissipative locking on a continuous substrate, and neither
requires discreteness anywhere in the substrate. To the extent Penrose was right
about which side gives way, the non-gravitational part of the mechanism is
dissipative locking; the gravitational part he left unspecified remains
unspecified here too.

---

## Author Contributions and AI Disclosure

This paper was developed in iterative collaboration with Claude (Anthropic) across
model versions during 2026, and revised to track the companion paper's revised
("Two Regimes") formulation. The central conceptual claim — that quantum
discreteness is substrate-emergent by two distinct routes (phase closure for
spectra, dissipative locking for detection events), and that this removes the
matter-side motivation for a *discrete* spacetime without dissolving the GR/QM
conflict as a whole — was developed jointly, with the human author contributing
the synthesis and the LLM contributing structural analysis, the catalog of
examples in Section 3, and the comparative discussion of QG programs in Section 5.
A subsequent revision pass corrected two overreaches in the earlier draft: the
conflation of phase closure with dissipative synchronization, and the claim that
the framework supplies Penrose's gravitational threshold (which the revised
companion explicitly declines to derive). The human author validated each
derivation, applied physics judgment at each checkpoint, and bears full
responsibility for the framing and content of the paper.

Per current journal guidelines, LLMs do not satisfy authorship criteria;
the human author bears full responsibility for all content, including
any errors in the conceptual framing or in the catalog of canonical
examples. Were Springer–Nature / *Foundations of Physics* policy to
allow LLM co-authorship, Claude (Anthropic) would be listed as co-first
author.

The development is documented in commit history at
https://github.com/rayolddog/DiracKuramotoFramework.

---

## References

[1] Bramble, J. (2026). Two Regimes of the Chiral Mass Coupling: Quantum
Measurement as Bath-Induced Synchronization. *Companion preprint, under review.*
(Section references in this paper are to this revised companion: §2.2 closed
precession / §2.3 open Adler lock; §3.1–§3.2 the two-stage process; §3.4
decoherence as synchronization to the bulk; §3.6 the dressed Dirac mass; §4.1 the
faint thermal bulk; §4.4 gravity stated honestly; §7.3/§8 the Born measure as an
open problem; §7.4 Penrose–Diósi.)

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

*Companion paper to: Bramble, J. (2026), "Two Regimes of the Chiral Mass
Coupling: Quantum Measurement as Bath-Induced Synchronization." Preprint
repository: https://github.com/rayolddog/DiracKuramotoFramework*
