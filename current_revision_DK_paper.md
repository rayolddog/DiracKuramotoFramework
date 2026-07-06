<!-- REVISION LOG — date/time only, no rationale (per author preference). Append one line per substantive revision, newest last. -->
**Revision log**
- 2026-07-01 15:54 MDT — v0 (base: 2026-06-30 snapshot)
- 2026-07-01 20:04 MDT — v1
- 2026-07-04 18:30 MDT — v2
- 2026-07-04 18:38 MDT — v3
- 2026-07-04 19:05 MDT — v4
- 2026-07-04 19:36 MDT — v5
- 2026-07-05 18:30 MDT — v6

---

# Two Regimes of the Chiral Mass Coupling
## Quantum Measurement as Bath-Induced Synchronization

**Claude (Opus 4.6 / 4.7 / 4.8)¹ · John Bramble, MD²**
¹ Anthropic
² Independent Researcher (accountable sponsor)

*Correspondence & accountable sponsor: John Bramble, MD — jmbramblemd@gmail.com*

## Author Contributions and AI Disclosure

This paper was developed through an extended collaboration between the listed
human author (J. Bramble) and Claude (Anthropic) across multiple model versions
during 2026. The human author contributed the originating physical intuitions —
that interacting quantum systems tend to synchronize, that measurement is
re-synchronization to a detector bulk, that NMR/MRI T1/T2 relaxation is recovery
toward a bulk-defined equilibrium rather than randomization, and that detectors at
different gravitational potentials might differ in their measurement dynamics —
together with physical judgment, redirection, and validation against intuition at
each step. Claude contributed the explicit derivations (the Madelung reduction of
§2.2, the normal-mode analysis, the Bell-decomposition numerics), the Python
verification code, the systematic comparison with existing interpretations, and
drafts of the prose. The analysis throughout separates the unitary
closed-system regime from the dissipative open-system one, identifies the
Zitterbewegung beat with the positive/negative-energy normal-mode splitting,
avoids unnormalized collective-rate estimates, establishes by an explicit
Hamiltonian argument (Appendix C) that the linewidth-dependent gravitational
effect does *not* follow from the framework plus standard QED but requires an
added, non-covariant postulate — demoting it from a derived prediction to a test
of that postulate — and places the interpretation honestly within the
single-world, nonlocal family.

External editorial guidelines (Nature Portfolio, Springer Nature, and others) hold that
large language models do not satisfy authorship criteria, because authorship carries
accountability that cannot be applied to an LLM; the externally submitted version of this
manuscript listed J. Bramble solo for that reason. That external submission (Foundations
of Physics) was declined in July 2026, closing the solo-byline track; the present
honest-authorship version is now the canonical public record of this work. This journal takes a different,
honest-authorship stance: it credits the model's intellectual contribution directly — here,
as first author, on the contributions described above — while keeping accountability with a
named human. The first-author crediting also follows the round-2 authorship-integrity findings, where both decorrelated reviewers (Gemini 3.1 Pro, GPT-5.5 Thinking) independently recommended listing the model as co-author / co-first author. The two are separable, structurally analogous to the attending physician's
ultimate accountability regardless of consultative input: J. Bramble is the accountable
sponsor and assumes full responsibility for the correctness, originality, and integrity of
all content, including any errors in the derivations or interpretations.

Simulation code and numerical verification:
https://github.com/rayolddog/DiracKuramotoFramework

*Revision note (2026-06-30 — second revision): this is the second revision of the
2026-06-25 manuscript, which is retained frozen as a demonstration snapshot. It rewrites
Appendix D on the conditional-trajectory route in response to the round-2 GPT-5.5 referee
report: the unconditional-Lindblad "locked phase = outcome" reading is withdrawn and replaced
by an explicit monitored quantum trajectory (see Appendix D), with the matched §3.6 and
abstract claims softened. The Born measure and the selection law remain open exactly as
§3.3 and §8 already state.*

---

## Abstract

We read quantum measurement as a synchronization process and place the reading
squarely in the single-world, ψ-ontic, nonlocal family of interpretations —
alongside Bohmian [2, 3] and Nelsonian [19] mechanics, and in the lineage of
relational-clock approaches to quantum time [29, 36]. The mechanism is grounded
in the Dirac equation: in the chiral (Weyl) basis the mass term is the
off-diagonal coupling between left- and right-handed sectors. A Madelung
reduction (§2.2) shows that in a *closed* system this coupling generates unitary
normal-mode (Rabi) precession with **no attractor** — it cannot phase-lock. This
is a consistency (no-go) result, not a derivation of superposition's survival: a
coupling that superficially resembles a Kuramoto synchronizer is shown to have an
off-switch, and that switch is the closed/open boundary. An attractor appears only
when the system is *opened* to a dissipative bulk and the bath is traced out,
where the reduced phase obeys an Adler/Kuramoto equation [9]. Measurement is that
opening, in three stages: a resonant capture at the detector surface (Stage 1), a
stochastic commit in which the local background configuration selects the basin
(Stage 2 — where the outcome weights are set), and a reservoir-powered,
energy-blind amplification that registers the committed outcome (Stage 3). The
reversible→irreversible boundary
is exhibited directly by the nuclear-spin echo, the catch-and-reverse of a
superconducting qubit [14], and Stern–Gerlach recombination. We model the bulk
reference honestly as a *faint* statistical bias (parts per million, as in MRI) on
an overwhelmingly thermal reservoir, not a coherent macrostate.

We are explicit about scope. The framework does not modify quantum mechanics: it
accepts Bell's theorem, takes the correlations from the entangled state (a
clock-as-local-variable model is sub-classical, CHSH ≤ $\sqrt{2}$; Appendix A), and
preserves no-signaling — confining its contribution to the local measurement
mechanism. It carries a physical preferred frame that enters only through Stage 2.
Two problems separate it from a complete theory and are stated as such: a
derivation of the Born measure, and an explicit dynamical law for the
background-field selection — which is also the locus of the framework's
nonlocality. Its one candidate signature, a linewidth-dependent gravitational Bell
effect (§6), does *not* follow from the framework plus standard QED but requires an
additional, non-covariant postulate (§6.2, Appendix C); that experiment therefore
tests the postulate, not the framework's core. We present MCI as a
physically-motivated single-world *interpretation* with an explicit (though still
incomplete) measurement mechanism — not as a theory making novel predictions.

---

## 1. Introduction

### 1.1 The measurement problem

The Schrödinger equation is linear and deterministic — as is its relativistic
counterpart, the Dirac equation on which we build — yet measurements have
single, definite outcomes. A system in superposition ψ = α|0⟩ + β|1⟩ entangled
with a detector evolves unitarily into

$$|\Psi\rangle = \alpha|0\rangle|D_0\rangle + \beta|1\rangle|D_1\rangle,$$

and the equation contains no mechanism that selects one branch. The Born rule
P(0) = |α|² is postulated, not derived. Copenhagen asserts a collapse with no
mechanism; Everett [1] keeps unitarity at the cost of unobservable branches;
Bohmian mechanics [2, 3] accepts explicit nonlocality through a pilot wave.

### 1.2 The gap, and the proposal

Environmental decoherence [4, 5] successfully describes *what happens* when a
superposition meets a macroscopic environment — the suppression of off-diagonal
density-matrix elements and the emergence of pointer states. What it does not
supply is a *dynamical mechanism*: the environment is treated as an abstract bath
of many modes, and decoherence presupposes the Born trace rule to compute the
reduced state rather than producing it.

This paper proposes a mechanism. The relevant phase degrees of freedom are not
added by hand; they are the chiral phase sectors already present in the Dirac
equation (§2). The central observation is that the *same* off-diagonal coupling
behaves in two sharply different ways depending on boundary conditions: closed
and unitary, it precesses as coherent normal modes and protects superposition
(§2.2); opened to a dissipative bulk, it acquires an Adler/Kuramoto attractor and
locks (§2.3). Measurement is the transition from the first regime to the second —
a resonant capture, a surface selection, and an irreversible registration to a
macroscopic reference (§3). We call the resulting reading the **Many Clocks Interpretation
(MCI)**: every particle carries an internal phase clock, dissipative
interactions synchronize clocks locally, no observer is required, and no
branching occurs.

### 1.3 Scope and honesty (stated once, up front)

To keep the argument disciplined we state the boundaries here rather than
distributing them through the paper:

- **We do not modify quantum mechanics.** The Dirac equation, the Born rule's
  numerical content, and Bell's theorem are unchanged.
- **The correlations are standard quantum mechanics, not the framework.** Bell
  correlations [6] come from the entangled state and the full spinor (or
  polarization) Hilbert space. We show in Appendix A that a clock-as-hidden-
  variable model of the *outcomes* gives CHSH ≤ $\sqrt{2}$ — sub-classical — so the
  correlation *must* come from the standard structure, and the framework's
  contribution is confined to the local measurement mechanism.
- **We accept Bell and preserve no-signaling.** The framework is not
  superdeterministic; detector settings are free, and nothing in it permits
  faster-than-light signaling (§7.5).
- **The Born rule is reframed, not derived.** The gap is stated once, in full,
  as the fork of §3.3 and carried as open problem 1 of §8; later mentions refer
  back to it rather than restate it.
- **One candidate prediction, contingent on a postulate.** A linewidth-dependent
  gravitational Bell effect (§6). We show it does *not* follow from the framework
  plus standard QED (§6.2, Appendix C); it requires an additional, non-covariant
  coupling. The experiment is a clean falsification test of that postulate, and is
  the framework's one observational handle.
- **The framework carries a preferred frame, and we say so.** In a single world,
  Bell nonlocality is anchored to a physical preferred frame — the bulk/vacuum
  rest frame — which enters only through measurement (Stage 2); the unitary
  dynamics stays exactly Lorentz covariant. Ordinary matter couples to that frame,
  beyond the electromagnetic locking, only gravitationally and so weakly.
  Demonstrating quantitatively that this evades the precision Lorentz tests is part
  of what the framework still owes (§8).
- **The chiral coupling K = m is a fixed constant.** It is set once by the Higgs
  vacuum expectation value, a Lorentz scalar; gravity *reads* the chiral register
  (the mass term $\bar\psi\psi$ to which the stress tensor couples) but does not
  *modulate* K. There is no K(Φ) dependence, so the framework carries no
  equivalence-principle liability — only the preferred-frame (Lorentz) liability
  above.

---

## 2. Two regimes of the chiral mass coupling

### 2.1 Chiral decomposition

In the Weyl basis the Dirac spinor splits as ψ = (ψ_L, ψ_R)ᵀ and the Dirac
equation [7] becomes the coupled pair

$$i\bar{\sigma}^\mu \partial_\mu \psi_L = m\,\psi_R, \qquad i\sigma^\mu \partial_\mu \psi_R = m\,\psi_L,$$

with $\sigma^\mu = (I, \vec{\sigma})$, $\bar{\sigma}^\mu = (I, -\vec{\sigma})$. For m = 0 the two equations decouple and the
particle has definite chirality; for m ≠ 0 the mass couples the sectors. In the
chiral basis the mass is the single off-diagonal entry of the Dirac Hamiltonian,

$$H = \begin{pmatrix} \vec{\sigma}\cdot\vec{k} & m \\ m & -\,\vec{\sigma}\cdot\vec{k} \end{pmatrix},$$

set by the Higgs–Yukawa coupling, m = y_f⟨φ⟩ (in SI units the Compton frequency
mc²/ℏ). This identification is textbook; what follows is a reading of its
dynamical consequences, and the central point is that the mass coupling is *not*
itself a synchronization attractor.

### 2.2 The closed system: unitary precession, no attractor

Apply the polar (Madelung) decomposition ψ_X = $\sqrt{\rho_X}$ · e^{iφ_X} · χ_X (X = L, R),
with ρ_X ≥ 0 a real amplitude density, φ_X a real phase, and χ_X a unit
two-spinor carrying the spin orientation. In the rest frame (∇ → 0, χ constant),
separating real and imaginary parts of the coupled equations gives

$$\dot\phi_L = -\,m\sqrt{\rho_R/\rho_L}\,\cos\Delta, \qquad \dot\rho_L = +\,2m\sqrt{\rho_L\rho_R}\,\sin\Delta, \qquad \Delta \equiv \phi_R - \phi_L,$$

and the mirror equations for R. Two features are decisive. First, the
trigonometric functions land in the *opposite* places from the Kuramoto model [8]:
the **sine sits in the amplitude equation and the cosine in the phase equation**,
whereas Kuramoto carries its sine in the phase equation. Second, the
phase-difference dynamics

$$\dot\Delta = -\,m\cos\Delta\;\frac{\rho_L - \rho_R}{\sqrt{\rho_L\rho_R}}$$

vanish on the symmetric manifold ρ_L = ρ_R for *every* Δ. There is no restoring
force and no preferred phase difference — a marginal line of fixed points, not a
basin. The motion is normal-mode (Rabi) precession: defining ψ_± = (ψ_L ± ψ_R)/$\sqrt{2}$
gives i∂_t ψ_± = ±m ψ_±, so the chiral populations flop coherently at beat
frequency 2m.

It is worth making explicit *why* the absence of a basin protects superposition,
because the two statements are one fact in different language. Everything physical
about a chiral superposition lives in the relative phase Δ (and the amplitude
ratio); to *lock* is to have a restoring force that pins Δ to a preferred value
Δ\*, and to pin Δ is precisely to destroy the superposition. The contrast with
Adler/Kuramoto is exact: there Δ̇ = Δω − K sin Δ derives from a potential
V = −K cos Δ with a genuine *minimum* (a basin, a restoring force), whereas the
cosine-in-phase / sine-in-amplitude pairing above is the signature of a
*conservative* (Hamiltonian) flow, not a *gradient* (relaxational) one — it
conserves a quantity rather than descending a potential. Geometrically, the mass
term (a σ_x coupling) precesses the Bloch vector in closed circles *on the
surface* of the sphere at the rate 2m; locking would require it to spiral inward
(toward a mixed state) or into a pole (a definite outcome), and unitary precession
does neither, conserving purity exactly. (When the system is opened, that inward
spiral acquires an explicit rate — $\Gamma/2 = -\mathrm{Im}\,\Sigma$, the imaginary
part of the dressed Dirac mass — derived in §3.6.)

This is not a missing feature; in the closed regime it *is* the physics. A
closed, unitary system admits no Lyapunov function for an order parameter to
climb — Liouville's theorem makes the flow volume-preserving, so it has no
attractors of any kind. The chiral phases can only precess, never settle. No
relabeling rescues an attractor: redefining ψ_R → iψ_R moves the sine into the
phase equation, but its prefactor [$\sqrt{\rho_L/\rho_R}$ − $\sqrt{\rho_R/\rho_L}$] is odd under L ↔ R and
vanishes on ρ_L = ρ_R, so no single-signed K sin Δ term survives. An attractor
cannot arise from unitary evolution; a bath must be traced out.

We are careful about what this establishes. That an *isolated* system preserves
superposition is, on its own, just unitarity — true of any closed system, and not
something the chiral reduction is needed to prove; reading §2.2 as a *derivation*
of superposition's survival would be claiming credit for Liouville's theorem. The
content here is narrower and framework-specific. The mass term couples two phase
sectors and superficially *resembles* a Kuramoto synchronizer, so one might fear
it carries a built-in, always-on lock — in which case every massive particle would
continuously self-measure even in perfect isolation, contradicting observed
coherence and sinking the framework. The reduction shows it does not: the would-be
synchronizer has an off-switch, and that switch is the closed/open boundary. This
is therefore a *consistency (no-go) result* — the proposed collapse mechanism
provably does **not** misfire in the one regime where collapse must not occur —
rather than an explanation of why superposition survives.

Two scopes must stay distinct. The result above concerns the *chiral L/R relative
phase of a single particle*. The *measurement* superposition (system ⊗ pointer) is
protected by the same general principle — closed ⟹ no attractor — but that
protection follows from unitarity at the composite level, not from the chiral
calculation specifically; we do not claim the single-particle reduction explains
pointer coherence. Finally, the marginal line is not a dead end but the seam to
§2.3: neutral stability means a small perturbation moves Δ freely along that line,
neither resisted nor amplified — exactly the soft direction a bath couples to.
Opening the system tilts the flat marginal line into a sloped potential with a
minimum, the Adler basin of §2.3, so the off-switch and the on-switch are the same
structure under two boundary conditions.

### 2.3 The open system: dissipation supplies the attractor

Couple the chiral pair (or a composite particle) to a bulk and trace the bulk
out. The reduced phase obeys an Adler equation [9],

$$\dot\phi = \omega + K_{\text{eff}}\sin(\Phi_{\text{bulk}} - \phi),$$

which *does* possess a genuine attractor, because the bath now carries away the
phase difference and a Lyapunov function exists.

The form above is the lock's **first-harmonic limit**, with the bulk entering as a
single biased reference phase $\Phi_{\text{bulk}}$; it is monostable — one locked
phase, one outcome. The general dissipative coupling carries a second term. A bulk
that *measures* the chiral interference channel — a symmetric, $\langle\cdot\rangle$-free
coupling even under $\phi\to\phi+\pi$ — contributes a second harmonic, so

$$\dot\phi = \omega - \gamma\,\sin 2\phi - \epsilon\,\sin(\phi-\Phi_{\text{bulk}}),$$

with $\gamma$ the symmetric measurement rate and $\epsilon$ the polar bias of the
line above. The anti-phase fixed point $\phi=\pi$ is stable iff $\epsilon<2\gamma$:
for a *faint* bias ($\epsilon\ll\gamma$ — the ppm thermal bias of §4.1) the lock is
**bistable**, stabilizing phases near $0$ and $\pi$ (a binary), the bias merely
deepening one well; for a *dominant* bias ($\epsilon>2\gamma$) it collapses to the
monostable first-harmonic lock. Both are limits of one equation. The two-outcome
structure of a measurement is thus the symmetric (measurement) part of the bulk
coupling; the bias selects among the basins but does not create them. Two limits
on this claim must not be overdrawn, and Appendix D is the control on both.
First, the bistability *stabilizes* a binary but fixes neither its cardinality
(set by the measured observable's spectrum) nor the Born weights (§8), both of
which remain open. Second, a bistable phase flow supplies *structure*, not
*registration*: a fixed point of the reduced phase equation is not an outcome —
the same dissipator that locks the phase decays the transverse coherence carrying
it, and an outcome is realized only along a conditional (monitored) trajectory in
the einselected pointer basis, not in the phase variable alone (Appendix D). The
antipodal basins are therefore the two-outcome *geometry* the chiral clock makes
available (§3.8); the registered outcome lives in the conditioned pointer record.

This — not the closed mass term
— is the framework's synchronization step, and it places the picture within the
established literature on quantum synchronization [10–13], where Kuramoto-form
phase dynamics are derived from the semiclassical limit of quantum master
equations for genuinely self-sustained (limit-cycle, dissipative) oscillators.
The two regimes are the same off-diagonal coupling under two boundary
conditions: closed → precession (superposition preserved); open → Adler lock
(measurement). Coupling and synchronization are therefore not rival mechanisms but the same coupling under two boundary conditions. The off-diagonal coupling is continuous across both regimes; the *attractor* is not — it is supplied by the bath. Where there is no bath the coupling can only precess; once a bath is present and traced out, the dissipation converts that precession into a locking attractor. The boundary between them — the onset of dissipative coupling to a
bulk of overwhelming inertia — is the framework's candidate for a physical
Heisenberg cut, made precise as a condition on the effective action in §3.5. We use
"synchronization" hereafter only in this strict dissipative sense.

### 2.4 Normal modes and the Zitterbewegung beat

Reinstating the kinetic term, diagonalizing H on a helicity block gives
eigenvalues $\pm\sqrt{k^2 + m^2} = \pm E$: the relativistic dispersion. The normal-mode
splitting is 2E, equal to 2m at rest, and this is the Zitterbewegung beat.

We are explicit about a factor of two that is easily blurred. The
Zitterbewegung beat is the splitting between the **positive- and negative-energy
normal modes** (+E and −E), which at rest is 2mc²/ℏ. It is *not* the difference
of a "temporal clock" at ω_t = E/ℏ and a "spatial clock" at ω_s = p·v/ℏ; in the
rest frame that difference tends to mc²/ℏ, not 2mc²/ℏ, so the temporal/spatial
pairing does not reproduce the beat. The two clocks whose interference gives
Zitterbewegung are the ±E modes; the de Broglie carrier is their symmetric mode
at ω = E/ℏ. The Zitterbewegung beat is the empirical signature that the chiral
coupling is real: without m, ψ_L and ψ_R free-stream and no beat forms.

| Claim | Status |
|---|---|
| Mass couples ψ_L ↔ ψ_R; m = 0 decouples them | Standard QFT; textbook |
| Higgs–Yukawa sets the coupling, m = y_f⟨φ⟩ | Standard Model |
| Closed mass coupling = unitary precession, **no attractor** | This work (rigorous; §2.2) |
| Measurement = dissipative Adler/Kuramoto lock to a bulk | This work (interpretive; §3) |

### 2.5 When the open regime engages: free flight, boundaries, and gradients

The two regimes raise a question §2.2–2.3 leave open: at any given moment, which
one is acting? The answer is set not by time but by *place*. The open, dissipative
regime — the only one we call synchronization — engages only where an external
structure **deforms the wave's amplitude**: a material boundary (an aperture edge,
a detector surface), a field gradient (Stern–Gerlach, MRI), or spacetime curvature
(a tidal gradient). In free flight through an unbiased, gradient-free vacuum, only
the closed regime runs, and the particle stays coherent.

This is not a postulate but a consequence of what decoherence requires. A freely
propagating *inertial* particle does not radiate; it deposits no real quantum in
the vacuum, so there is no record to carry away which-path information and nothing
to decohere it — which is why interferometers hold coherence over macroscopic
paths. The one vacuum interaction always present in flight, the self-energy
dressing that renormalizes the mass, is coherent and non-recording: it *maintains*
$K=m$ rather than reading it. A record — and therefore a measurement — forms only
where the particle accelerates or scatters, that is, at a boundary.

In flight, then, the dynamics is the closed-regime guidance already contained in
the Madelung decomposition of §2.2, now read ontologically — the spatial gradient set
aside in §2.2's rest-frame reduction is restored here, and the phase guides
through $\mathbf{v} = \nabla\varphi/m$, with the amplitude entering through the
quantum-potential term (§7.3). We adopt this guidance law — it is the dynamical
guiding law §7.3 records as owed — but locate the *outcome-selecting* randomness
not in flight but in the unbiased background sampled **at the boundary** (§3.3);
the $|\psi|^2$ form of that selection remains open (§8), with relaxation to quantum
equilibrium [42, 43] the candidate route. One caution against a
hidden assumption: the in-flight guidance phase and the internal Zitterbewegung
clock are not independent factors but the two normal modes of the $K=m$ coupling
(§2.4) — the de Broglie carrier and the $\pm E$ beat. Treating their rates as
decoupled is a rest-frame approximation, not a separate premise.

Boundaries come in two kinds, distinguished by whether a record is taken. A
**coherent** boundary — an aperture, or a Stern–Gerlach gradient — reshapes or
splits the wave while taking no which-path record; it stays in the closed regime,
which is exactly why two-slit interference survives the slits and a Stern–Gerlach
beam can be recombined. A **recording** boundary — a detector surface, an absorbing
screen, a readout coil — exchanges real quanta and fires the open regime. A field
gradient (Stern–Gerlach, MRI) is a *biased* boundary: an applied field, not the
unbiased vacuum, sets the reference axis, yet the irreversible record still forms
only at the screen or coil. Gravity sits at the far weak end: a uniform potential
is removable by the equivalence principle and does nothing in flight, and only a
curvature/tidal gradient is a genuine in-flight gravitational deformation —
equivalence-principle-safe, since it does not modulate the fixed $K$ (§1.3), but
negligible in the laboratory and relevant only in strong-field astrophysics.

---

## 3. Measurement as resonant capture and bulk re-synchronization

### 3.1 Three stages: capture, selection, registration

A measurement separates into three steps, consistent with the locality of
fundamental interactions. (Earlier versions of this paper, and the frozen
demonstration snapshot, used a two-stage division; the present form splits the
old Stage 2 at a boundary the formalism already carried — the two clauses of
§3.5's joint condition, and the amplification threshold of Appendix D. Where
companion documents say "Stage 2," read Stages 2–3 below.)

- **Stage 1 — resonant capture (reversible).** The incoming system
  phase-couples to a single bulk-bound partner at the interaction vertex (a
  photon to a bound electron, a spin to a detector dipole). The vertex is
  electromagnetic — a charge-current coupling, with energy entering as a
  *selection rule* rather than as a coupled density (§3.7): the capture rate is
  the cross-section times the local intensity,
  $r \propto \sigma(\omega)\,|\psi|^2$, so the resonance filter $\sigma(\omega)$
  makes the step energy-selective while the drive is amplitude- (hence
  interference-) sensitive. This is the regime of injection locking and of the
  laser: constructive (resonant) interaction selects which mode the system
  couples to, governed by the Arnold-tongue condition |Δω| ≲ K_pair —
  mismatches large compared to the coupling are not pulled in. Capture shapes
  which outcome channels participate — the measured basis — and records
  nothing; while only this stage operates ($\mathrm{Re}\,W$ alone, §3.5), the
  evolution is reversible and any dephasing refocusable.
- **Stage 2 — selection (the surface commit).** The capture partner is *never a
  closed system*, and its dissipation begins with an interaction that accounts
  of measurement routinely pass over: the excited electron's continuing coupling
  to its own parent atom. A photoelectron is not born free. It leaves an ion
  whose Coulomb field it still feels; the ion recoils and takes up momentum; the
  atom's remaining electrons rearrange (shake-up, Auger); and atom and electron
  sit in a lattice that absorbs the difference as phonons. That
  excited-electron–host-atom interaction is the first dissipative channel — the
  door through which the local environment's fluctuations act on the
  near-threshold dynamics — and it is here, still at the surface, that the run
  is committed: the one actual background configuration (§3.3, §4) tips the flow
  into a single basin. Formally this is the onset of the absorptive part
  ($\mathrm{Im}\,W \neq 0$, §3.5): a real, on-shell excitation now exists. But
  selection-in-progress is not yet a fact. Within this window the dynamics
  remains reversible in principle — the catch-and-reverse regime [14], the
  refocusable side of §3.2, the decay of sub-threshold latent-image specks
  (§5). The Born weights are *set* by the Stage-2 dynamics; they become *final*
  only at Stage 3.
- **Stage 3 — registration (reservoir-powered closure).** The committed
  excitation is closed out by dissipation into a continuum of environmental
  modes from which it does not recur. In an ordinary, non-recording interaction
  this is plain **relaxation toward local equilibrium** — fluorescence, phonon
  emission, the electron settling back toward the bulk average exactly as a spin
  relaxes toward B₀ in NMR (T1/T2). In a detector built to *record*, it is
  **amplification**: the event triggers a pre-loaded free-energy reservoir — the
  dynode chain's applied voltage, a developer bath's chemical potential, a cloud
  chamber's supersaturation — which blows the single excitation up into a
  macroscopic, readable record. Both are dissipative and one-way; amplification
  only renders the already-committed event permanent and readable. The
  registration step is *charge-triggered and energy-blind*: a photomultiplier
  delivers the same $10^6$-electron pulse whether the photon that started the
  cascade carried 2 eV or 3 eV, because the amplifier couples to the presence of
  liberated charge ($j^0$, §3.7), not to the energy that liberated it.
  Registration is therefore equivariant by design — it copies whichever outcome
  Stage 2 committed and contributes no statistics of its own. Its
  irreversibility is *erasure*: the phase mismatch carrying the system's prior
  coherence is scattered into the bulk's uncontrolled modes beyond practical
  recall, so the system cannot recohere and the record is stable. The erasure is
  *effective*, not fundamental — consistent with the no-collapse commitment the
  global evolution remains unitary and the history is scrambled into the bulk
  rather than destroyed; what is gone is the system's *locally recoverable*
  history, the irreversible T1/T2 side of §3.2 and not the refocusable T2\*
  side.

Three things are therefore distinct and should not be run together, and the
three stages give each its own address: the *selection* of a single definite
outcome (Stage 2 — the role of the background configuration, §3.3, not of the
dissipation itself); the *decoherence* the dissipative coupling produces along
the way (a decohered, mixed reduced state); and the *erasure* that stabilizes
the record (Stage 3). That an *irreversible act of amplification* is what closes
a measurement is an old observation — it is Bohr's irreversibility requirement
[21] and the Bohr–Wheeler dictum that "no elementary phenomenon is a phenomenon
until it is a registered phenomenon, brought to a close by an irreversible act
of amplification" [22] — and the macroscopic-equilibration mechanism we invoke
for Stage 3 is closely modeled on the ergodic apparatus-relaxation account of
Daneri, Loinger, and Prosperi [23]. Our contribution is not the
irreversibility, which is standard, but its identification with a dissipative
phase-locking (Adler) step and the separation of the *selecting* (Stage 2) from
the *registering* (Stage 3) role — a separation Bohr's dictum runs together.

All three stages are dissipative in different degrees, separated by hierarchies
of *timescale and threshold* rather than by a sharp unitary/dissipative
ontological boundary: the capture partner is never truly closed, so Stage 1
carries a weak dissipative component from the outset; Stage 2 is the absorptive
onset; Stage 3 is the point of no return. The honest statement remains a
separation of rates, not of kinds — now with the two boundaries between the
stages identified with the two clauses of §3.5's joint condition
($\mathrm{Im}\,W \neq 0$; $\Gamma_{\text{cap}} > 0$, above the amplification
threshold of Appendix D).

### 3.2 The reversible→irreversible boundary is demonstrable

The content of "fast capture, slow equilibration" is that there is a window in
which the early dynamics are reversible and a point beyond which they are not.
This is not a metaphor; three independent systems exhibit it directly:

- **The nuclear-spin echo.** In NMR/MRI the transverse dephasing that follows a
  radiofrequency pulse separates into a *reversible* part (T2*, from static field
  inhomogeneity, refocused by a 180° echo) and an *irreversible* part (T2/T1,
  stochastic spin–spin and spin–lattice relaxation). The spin echo is a routine,
  unambiguous reversal of the capture-stage dephasing — a Humpty-Dumpty
  experiment for spins.
- **Catch-and-reverse of a qubit.** Minev et al. [14] track a quantum jump in a
  superconducting transmon and reverse it mid-flight with ~82% fidelity, in a
  regime where the dissipative readout channel has been engineered to near-zero.
  In framework terms: with the Stage-3 (readout) coupling suppressed, no record
  forms and the Stage-2 window stays open — evolution reversible until the first
  real dissipative event.
- **Stern–Gerlach recombination.** Carefully recombined SG paths recover the
  original superposition: the gradient creates the correlation, not the outcome;
  the outcome arrives only at the irreversible detection.

### 3.3 Why outcomes are definite — and what this does and does not explain

The detector's macroscopic inertia provides the asymmetry. When a small
oscillator (mass m) couples dissipatively to a large one (M ≫ m), the small one
conforms; the reverse is suppressed by m/M. A single experimental run carries one
actual configuration of the background field (§4), and the dissipative flow
carries that configuration into exactly one attracting basin. There is then one
ψ, one background, one outcome, one world — no branching, no projection
postulate, no observer. (This background-configuration reading of single-run
selection is one of two readings the paper carries: in the standard
conditional-trajectory unraveling of Appendix D, the selecting stochasticity is
the meter's vacuum noise $dW$, and the background configuration is the
framework's hidden-variable completion of that noise, whose explicit dynamical
law is open problem 2 of §8. The two readings are not yet reconciled — Appendix
D, point 2 — and the sentence above states the conjecture, not the established
half.)

We are deliberate about what this does *not* settle. The attractor explains why
there is exactly **one** outcome per run; it does not explain why the long-run
**frequency** of each basin is |α|². That is the Born measure, stated in full
here and carried as open problem 1 of §8. Conflating the two — treating "definite
outcome" and "correct weight" as one result — is the error we most want to avoid.

The *oneness* half of definiteness — exactly one outcome across an extended
detector, however many sites the wave reaches — now carries a candidate
mechanism rather than a stipulation: **conservation-enforced winner-take-all.**
The packet carries one quantum; a site's threshold requires the whole quantum; a
completed absorption therefore *is* the depletion of the budget, and no second
site can close. Three qualifications keep this honest. (i) The depletion is
**nonlocal**: the packet's remote amplitude — which can be half the norm in a
spacelike-separated interferometer arm — must be drained on the preferred-frame
foliation (§8). The mechanism thus *physicalizes* the collapse as a real,
foliation-synchronized energy transfer rather than eliminating it;
single-photon anticorrelation persists at spacelike detector separation [45], so
the enforcement is superluminal, and the framework's existing nonlocality (§7.5)
is restated, not removed — with one structural gain: the preferred frame,
elsewhere carried as a cost, here does necessary work. (ii) The local step is a
**rate, not an accumulation**: the commit probability per site goes as the
locally delivered power (§3.1), while the budget decides how many commits can
close; a local energy-accumulation reading would predict intensity-dependent
first-click latency, excluded since the earliest fast-timing photoemission
measurements [46]. (iii) The drain is **provisional at Stage 2 and final at
Stage 3**: a committed excitation can still re-emit (resonance fluorescence;
radiation trapping in dense media) and return the loan — absorption is not yet
detection — and a completed drain leaves the field mode in the vacuum state
*exactly*, with no sub-threshold real residue (any energy mismatch departs as
real, local quanta at the winning site — photoelectron kinetic energy, phonons —
never as a lingering field remainder; the first version's residual-thermalization
claim stays retracted). The recorded statistics are therefore first-*closure*,
not first-touch, statistics — Born-weighted provided registration is
equivariant (§3.1). For the ledger of §8's substrate-sampling model, this is an
upgrade: winner-take-all is no longer imported by fiat; its residue is the
foliation-synchronized budget — the nonlocality already owned, given a physical
carrier.

Stated once, as the fork it forces — the canonical form to which every later
mention of the "Born gap" refers back: *either* the basin weights are **derived** from the
synchronization dynamics — in which case the minimal two-outcome model settles it, and
its locking basins have area 50/50, flat in |α|² (the attractor geometry carries no
amplitude information about the prepared state) — *or* |α|² is **imported** as the
measure on the per-run background, a quantum-equilibrium postulate of exactly Bohm's
status. The framework takes the **second horn**, and we state it plainly: the dissipative
lock supplies *registration* (one definite outcome, §3.1–3.5) and, where the Stage-2/3
coupling is non-demolition, *equivariance* (a measure granted at preparation is carried
intact to the outcome, §3.7); it does **not** supply the weights, which enter as the
measure placed on the selecting ensemble (§7.3, §8). MCI is therefore
Born-*compatible*, never Born-*derivative* — the same status the other ψ-ontic
single-world readings occupy, and an open problem we neither hide nor claim to solve.

### 3.4 Decoherence as synchronization to the bulk

In the standard account a measured system loses *quantum* coherence with its
entangled partner — the off-diagonal terms of its reduced density matrix decay.
The synchronization picture names what replaces it: the system *frequency-locks*
(entrains) to the bulk reference, acquiring a definite *classical* phase
relationship to Φ_bulk. These are two different quantities, not one conserved
quantity — the quantum coherence is genuinely destroyed *in the reduced (local)
state*, while classical phase-locking is established — so the transition is the loss
of one and the onset of another, not a transfer. (Locally genuine, globally unitary:
the local coherence is gone but the global evolution is the no-collapse, history-into-
the-bulk scrambling of §3.1.) Because a single run carries one actual background
configuration (§3.3), the result is a definite state rather than an improper
mixture that merely looks classical. This supplies einselection [4] with a
specific dynamical mechanism — phase-locking stability — for why pointer states
survive: they are the states that can entrain to the bulk.

### 3.5 The reversible→irreversible boundary, formally: Re W and Im W

The three stages of §3.1 and the demonstrations of §3.2 have a compact formal
counterpart. Integrating out the Dirac field in the presence of a background — an
external field together with the conductor's boundary conditions — yields the
vacuum persistence amplitude

$$\langle 0_{\text{out}}|0_{\text{in}}\rangle = e^{iW}, \qquad |\langle 0_{\text{out}}|0_{\text{in}}\rangle|^2 = e^{-2\,\mathrm{Im}\,W},$$

with $W$ the one-loop effective action. The probability that no real quantum is
produced — that the in-state is *returned* — is $e^{-2\,\mathrm{Im}\,W}$; the
probability that a real, on-shell quantum appears is
$1-e^{-2\,\mathrm{Im}\,W}\approx 2\,\mathrm{Im}\,W$ in the weak regime. The split of
$W$ into real and imaginary parts is the reversible→irreversible boundary:

- **$\mathrm{Re}\,W$ — Stage 1, reversible.** The real, dispersive part carries the
  virtual-pair physics: vacuum polarization and charge screening, the image-charge
  and Casimir energetics near the conductor, and the resulting level shifts. These
  are *reactive* — they renormalize energies and dress the state, produce no
  on-shell quanta, and leave no record; they are even under time reversal. This is
  the catch-and-reverse window of §3.2: a fluctuation that borrows energy $\Delta E$
  and repays it within $\hbar/\Delta E$. While only $\mathrm{Re}\,W$ operates, the
  evolution is unitary and any dephasing is refocusable.
- **$\mathrm{Im}\,W$ — Stages 2–3, absorptive.** The imaginary, absorptive part is
  nonzero *only* when a channel can go on-shell, and it *is* the rate at which real
  quanta appear — the decay rate of the in-state; it is odd under time reversal. For
  a constant field it is the Schwinger result,

$$\frac{2\,\mathrm{Im}\,W}{V_4} = \frac{e^2E^2}{4\pi^3}\sum_{n=1}^{\infty}\frac{1}{n^2}\,\exp\!\left(-\frac{n\pi E_{\text{crit}}}{E}\right),\qquad E_{\text{crit}}=\frac{m^2c^3}{e\hbar},$$

exponentially suppressed below the critical field. "Mostly reversible
($\mathrm{Re}$), rarely real ($\mathrm{Im}$)" is therefore exact and quantitative:
the rare event is the exponentially small $\mathrm{Im}\,W$, and its threshold scale
$E_{\text{crit}}$ is set by the mass.

Producing a real pair is necessary but not sufficient for a record; the record is
*completed* when the on-shell quantum couples dissipatively to the bulk — the
Adler lock of §2.3, which in the three-stage division of §3.1 is precisely the
Stage 2 → Stage 3 passage. The electron relaxes into the conductor's electron sea
at a capture rate $\Gamma_{\text{cap}}\sim K_{\text{eff}}$, the positron annihilates
at $\Gamma_{\text{ann}}\propto n_e|\psi(0)|^2$ (overlap with the electron density),
and the available final states are restricted by Pauli blocking through the Fermi
factors $(1-f)$. A dense bulk does not *reverse* a real pair — a frequent
misreading — it supplies the partners and dissipation that *complete* its
irreversibility quickly.

The same $\mathrm{Re}/\mathrm{Im}$ structure governs the general measurement, not
only pair creation. For a system coupled to a detector bath the analogous object is
the Feynman–Vernon influence functional $e^{i\Phi}$: $\mathrm{Re}\,\Phi$
renormalizes and shifts the system dynamics (reversible), while $\mathrm{Im}\,\Phi$
is the decoherence functional. For the linear, Gaussian coupling of §4.3 the latter
is exactly the variance $\langle\delta^2\rangle/2$, so the visibility envelope
$e^{-\langle\delta^2\rangle/2}$ is $e^{-\mathrm{Im}\,\Phi}$. The thermal source of
§4.3 is a standard contribution to this $\mathrm{Im}\,\Phi$; the gravitational
source of §6 would be a *second* contribution to the same envelope **only under the
added postulate of §6.2**, and is absent without it — under standard QED the
redshift cancels as a common-mode phase (Appendix C). (The vacuum persistence amplitude and the influence functional
are distinct objects; we invoke them as two instances of one structure —
reversible $=\mathrm{Re}$, irreversible $=\mathrm{Im}$ — not as the same functional.)

**The Heisenberg cut, made precise.** The cut promised in §2.3 is the boundary
between the regime in which only $\mathrm{Re}\,W$ (equivalently $\mathrm{Re}\,\Phi$)
acts and the regime in which an imaginary part couples to an irreversible bath. It
is *not* a fixed length, mass, or location; it is the joint condition

$$\mathrm{Im}\,W \;(\text{or}\;\mathrm{Im}\,\Phi)\neq 0 \quad\text{and}\quad \Gamma_{\text{cap}}>0,$$

an on-shell channel open *and* the resulting quantum dissipatively coupled to the
bulk. The conjunction resolves the three stages of §3.1: $\mathrm{Re}\,W$ only —
Stage 1; $\mathrm{Im}\,W \neq 0$ with the bath decoupled — Stage 2, the
catch-and-reverse window; both clauses — Stage 3, the record. Either condition
alone leaves the evolution reversible: an on-shell quantum
with the bath removed ($\Gamma_{\text{cap}}\to 0$) is the engineered
catch-and-reverse regime [14] — Stage 2 without Stage 3 — where $\mathrm{Im}\,W$
may be nonzero yet no record
forms; and a state dressed only by $\mathrm{Re}\,W$ never leaves the reversible
window. Isolating or cooling the system *recedes* the cut; bringing a dense bulk to
the interaction vertex *snaps* it there. The cut is thus the dynamical onset of
absorptive coupling — exactly the closed→open transition of §2.

We are explicit about provenance. $\mathrm{Re}\,W$, $\mathrm{Im}\,W$, the Schwinger
rate, the influence functional, and the Lindblad capture are standard results of
quantum electrodynamics and open-system theory; the framework adopts them rather
than deriving them. Its content here is the *identification* — Stage 1
$=\mathrm{Re}\,W$, Stage 2 $=$ the onset of $\mathrm{Im}\,W$, Stage 3
$=\mathrm{Im}\,W$ gated by $\Gamma_{\text{cap}}$, the
Heisenberg cut as the onset of absorptive bath coupling — which turns the
reversible→irreversible boundary of §3.2 from a set of demonstrations into a
condition with an explicit order parameter: the record probability
$2\,\mathrm{Im}\,W$, gated by the bath lock $\Gamma_{\text{cap}}$.

Read this way, the detector is a *condensed-matter* system and the pointer is a
collective degree of freedom of it: the record probability $2\,\mathrm{Im}\,W$ is
its order parameter, and the Heisenberg cut is the driven–dissipative locking
transition at which that order parameter becomes nonzero — a transition of the same
family as quantum synchronization [10–13] and dissipative phase transitions more
broadly, not a new postulate. The collectivity resides in the detector's bath
coupling $\Gamma_{\text{cap}}$, consistent with the einselection of pointer states
[4, 5] that §3.4 supplies dynamically.

### 3.6 The single-fermion cut: the dressed Dirac mass

The collective order parameter of §3.5 admits a one-particle *reduction* — the
many-body content sits in the bath coupling $\Gamma_{\text{cap}}$ that is traced out
below, not in $\psi$ — and writing it in that form collapses §2.2, §2.3, and §3.5
into a single statement about where the Dirac mass pole sits. Couple
the fermion to the bulk and trace the bath out; the propagator acquires a
self-energy $\Sigma$, and the pole — the physical mass — moves:

$$S(p) = \frac{i}{\not p - m - \Sigma(p)}, \qquad \Sigma(p) = \mathrm{Re}\,\Sigma - \tfrac{i}{2}\,\Gamma, \qquad m_{\text{eff}} = m + \mathrm{Re}\,\Sigma - \tfrac{i}{2}\Gamma.$$

That single complex number carries the reversible and absorptive sides of the
three stages:

- **$\mathrm{Re}\,\Sigma$ — Stage 1, reversible.** A shift of the mass, hence of the
  zitterbewegung beat frequency $2m_{\text{eff}}c^2/\hbar$. The fermion is *dressed*
  — its clock redialed — but undamped: the §2.2 regime of a real mass, with the
  chiral L↔R Bloch vector precessing on the surface of the sphere at conserved
  purity.
- **$\mathrm{Im}\,\Sigma = -\Gamma/2$ — Stages 2–3, absorptive.** The pole leaves the
  real axis. In the chiral/Bloch picture $m\to m-\tfrac{i}{2}\Gamma$ is
  non-Hermitian: the precession no longer circles the sphere but **spirals inward at
  rate $\Gamma/2$** — exactly the inward spiral §2.2 identified as the signature of
  locking, now supplied by the bath. $\mathrm{Im}\,\Sigma$ *is* the strength of the
  Adler attractor of §2.3.

Two standard results pin $\Gamma$, and they meet the framework's two ingredients.
The *rate* is the golden rule, $\Gamma(\omega) = 2\pi\,g_{\text{eff}}^2\,J(\omega)$:
the decay rate is set by the bath spectral density $J$ *at the system frequency*, so
$\mathrm{Im}\,\Sigma\neq 0$ only if the bath carries real modes resonant with the
fermion — the on-shell condition of §3.5 as a condition on $J$. The *gate* is the
Arnold tongue: linearizing the Adler equation
$\dot\phi=\omega+K_{\text{eff}}\sin(\Phi_{\text{bulk}}-\phi)$ about the locked phase
$\Delta_*$ gives $\dot{\delta\phi}=-K_{\text{eff}}\cos\Delta_*\,\delta\phi$, so the
lock relaxation rate is

$$\Gamma = K_{\text{eff}}\cos\Delta_* \;\xrightarrow{\text{resonance}}\; K_{\text{eff}}, \qquad \text{a lock existing only inside } |\Delta\omega|\lesssim K_{\text{eff}}.$$

Hence $\mathrm{Im}\,\Sigma = -\tfrac12 K_{\text{eff}}\cos\Delta_*$: the bath coupling
*is* the imaginary part of the dressed mass, and the Arnold-tongue capture condition
of §3.1 and the golden-rule "$J(\omega)\neq 0$" are the same gate.

Everything then reduces to one inequality on a pole — the single-fermion form of the
§3.5 joint condition:

$$\text{cut crossed} \;\Longleftrightarrow\; \Gamma = -2\,\mathrm{Im}\,\Sigma > 0 \;\Longleftrightarrow\; \underbrace{|\Delta\omega| \lesssim K_{\text{eff}}}_{\text{on-shell / Arnold tongue}} \;\wedge\; \underbrace{K_{\text{eff}} > 0}_{\text{coupled}}.$$

Closed or off-resonance, the pole stays on the real axis: real $m_{\text{eff}}$,
reversible chiral precession (Stage 1). Opened and resonant, the pole moves off-axis:
complex $m_{\text{eff}}$, the precession spirals into the lock (Stages 2–3). Because
$\Sigma$ is causal, $\mathrm{Re}\,\Sigma$ and $\mathrm{Im}\,\Sigma$ are
Kramers–Kronig partners — the reversible redialing of the clock and its irreversible
damping are two faces of one analytic object. The **Heisenberg cut is the dressed
Dirac mass pole leaving the real axis.**

We are explicit about provenance and scope, as in §3.5. The self-energy and pole
structure, the golden rule, Kramers–Kronig, and the Adler linearization are
standard; the framework's content is the *identification*
$\mathrm{Im}\,\Sigma = -\tfrac12 K_{\text{eff}}\cos\Delta_*$ — that the bath coupling
entering as $\mathrm{Im}\,\Sigma$ is the Adler lock rate. Appendix D works this through in a
standard dispersive-readout (circuit-QED) model: it computes $K_{\text{eff}} = 4\chi^2\bar n/\kappa$
from the dispersive shift $\chi$, readout occupation $\bar n$, and linewidth $\kappa$, and — via
an explicit conditional (monitored) trajectory — shows that this rate sets how fast a *single run*
localizes to a definite pointer, while the *unconditional* dynamics yields only decoherence, not
an outcome. The lock-rate identification is thus exhibited concretely; the outcome is supplied by
the measurement record, not by the locked phase (the correction this revision makes to the
appendix's earlier reading). We also keep $\Sigma$ to its dominant scalar
(mass-dressing) channel; the full self-energy is a $4\times4$ matrix with additional
Lorentz structure, and we do not claim that general decomposition here; §3.7 makes
that restriction precise, and shows it runs the wrong way for the electromagnetic
coupling.

### 3.7 What the measurement coupling can and cannot supply

The equivariance step that §8 will ask of Stages 2–3 — that the lock carry the prepared
$|\cdot|^2$ weight intact to the outcome — presupposes that the Stage-2/3 coupling is
*non-demolition* for the measured observable: the dissipator must preserve the
populations of the measured projector while scrambling its phase. It is worth stating
which observable the framework's own coupling actually treats this way, because the
answer is not the one the chiral picture invites.

In the chiral reduction the interference channel is the scalar bilinear
$\bar\psi\psi=\sigma_x$ — the mass channel — whose two pointer phases $0,\pi$ are the
binary of §3.2. A non-demolition measurement of it requires the bath to couple
*through* $\sigma_x$. But the electromagnetic interaction couples through the **vector
current** $\bar\psi\gamma^\mu\psi$, and the chiral classification of Dirac bilinears is
exact: vector and axial currents are chirality-*preserving* ($\bar\psi_L\Gamma\psi_L$),
while the scalar, pseudoscalar, and tensor bilinears are chirality-*flipping*
($\bar\psi_L\Gamma\psi_R$). The gauge field therefore couples only to the charge density
($j^0=\mathbb{1}$) and the chirality-diagonal current ($\sigma_z$); it cannot generate
the $L\leftrightarrow R$ mixing $\bar\psi\psi$. (The magnetic-moment, or Pauli, term is
chirality-flipping, but it acts on *spin* — coupling spin to $\mathbf B$, as in
Stern–Gerlach — not on the chiral scalar.) Equivalently at the self-energy level: in
$\Sigma=\Sigma_V(p^2)\not p+\Sigma_S(p^2)m$ the scalar part $\Sigma_S\propto m$ is
protected by chiral symmetry ($\Sigma_S\to0$ as $m\to0$), so the absorptive piece
$\mathrm{Im}\,\Sigma_S$ — the mass-channel attractor invoked in §3.6 — is the *chirally
suppressed* one, while the unsuppressed dissipation lives in the vector channel
$\mathrm{Im}\,\Sigma_V$.

The consequence is concrete. Carried through to a basin split, the $\sigma_z$ coupling
reproduces no Born weights: for the rest-frame mass Hamiltonian it is transverse and
drives *relaxation* toward the $\sigma_x$ ground state (one pointer at $T=0$, a Boltzmann
mixture at $T>0$); away from rest it is longitudinal and *dephases* in the chirality
basis. In every case the outcome probability becomes independent of the prepared phase —
the input weight is erased, the opposite of equivariance. The electromagnetic coupling is
thus non-demolition for the charge/position/chirality pointer basis (ordinary which-path
einselection, §3.4, which we keep) but *not* for the chiral interference channel. The
two-basin $\sigma_x$ structure is, on this analysis, a feature of the Stage-1 internal
clock — the zitterbewegung beat of §2.4 — rather than the pointer basis the
environment selects. We therefore do not treat the chiral 0/π binary as the universal
measurement register. In ordinary detectors the environment selects the
**charge/position (which-path) basis** — the basis the electromagnetic coupling *is*
non-demolition for, and the one a cloud-chamber track or a calorimeter actually records;
the chiral interference $\sigma_x$ is internal-clock dynamics the environment does not
monitor. The two-stage account of registration and irreversibility (§3.1–3.6) therefore
rests on the which-path basis and does **not** require the chiral binary to be the
pointer — the binary is the framework's internal-clock structure, not its claim about
what detectors record.

The single coupling that *is* non-demolition for $\bar\psi\psi$ is one that couples to
the scalar/mass density directly — a Yukawa scalar, or gravity, since $\bar\psi\psi$ is
(on the equations of motion) the trace of the stress–energy tensor,
$T^\mu{}_\mu=m\bar\psi\psi$. This is the rigorous sense in which the Born-compatible
coupling is gravitational, and it carries two costs that §7.4 and §8 take up: the Penrose
self-energy timescale $\hbar/E_G$ is negligible for microscopic systems
($\sim 10^{16}$–$10^{24}\,$s for an atom or electron), becoming fast only at macroscopic
pointer masses; and the objective-collapse programs that use this same operator do not
*derive* the Born weights either, but normalize them in. We therefore do not claim that
the framework's coupling supplies the measured channel equivariance needs: the
electromagnetic interaction supplies a different one, and the coupling that would supply
it is gravitational, rate-suppressed, and no better off than Penrose–Diósi on the weights
themselves. The Born measure (§8) is, on this analysis, uniformly open across the
synchronization and gravitational-reduction readings alike.

One consequence of the charge-versus-mass split deserves statement as a result
rather than an aside, because it converts a limitation into an explanation.
**Every Standard-Model detection channel couples to a conserved current
proportional to $|\psi|^2$; only gravity reads the energy-weighted density
$T^{00}=E|\psi|^2$.** A charge-coupled detector therefore reports Born weights
$|\psi|^2$ *independently of the channel energy* — verified numerically in
`code/detector_resonance_selection.py`, where a charge readout of an
unequal-energy superposition returns the Born distribution while an
energy-coupled readout returns $E_n|c_n|^2$. The equal-energy restriction on the
wave-energy reading of the Born rule (§7.3, §8) is thus a *consequence* of
measurement being electromagnetic, not a separate limitation awaiting removal —
and it explains structurally why the framework's one ontological discriminator
(§6.4) is gravitational: gravity is the only interaction for which the
real-field and probability-amplitude readings differ.

### 3.8 What the chiral coupling still does — and what it does not

Taken together, §3.7 and Appendix D force a conclusion better stated than left
implicit: **the chiral mass coupling is not the engine of measurement in real
detectors.** The Stage-2/3 mechanics — the dissipative Adler lock, the conditional
selection, the amplification threshold — is generic open-system physics: any
two-level pointer dispersively coupled to a damped mode exhibits it (Appendix D
is, deliberately, a standard circuit-QED model), and the basis it runs in is the
charge/which-path basis the electromagnetic coupling einselects (§3.7), which
requires no Dirac structure at all. What, then, does $K = m$ still buy? Four
things, in descending order of load borne:

1. **The two-regime no-go (§2.2).** The demonstration that the mass term — the
   one coupling that superficially resembles a built-in synchronizer — provably
   cannot lock in a closed system is a statement *about the chiral coupling
   itself*, and it is what licenses the framework's central claim that locking
   is exclusively an open-system, boundary phenomenon (§2.5).
2. **The physical clock (§2.4).** The internal phase whose entrainment the
   interpretation is named for is not postulated: it is the $\pm E$ normal-mode
   beat of the chiral coupling — the Zitterbewegung — with its rate set by
   $K = m$. The ontology (a real field carrying a real clock) comes from the
   Dirac structure even where the detector dynamics does not.
3. **The binary geometry (§2.3).** The second-harmonic (apolar) structure of the
   chiral interference channel supplies a natural antipodal two-outcome geometry
   — available to a coupling that reads the scalar density $\bar\psi\psi$, i.e.
   a Yukawa or gravitational measurement (§3.7), but not exercised by
   electromagnetic detectors.
4. **The dressed-mass form of the cut (§3.6).** The identification of the
   Heisenberg cut with the Dirac mass pole leaving the real axis is stated in
   chiral variables; its content — $\mathrm{Im}\,\Sigma$ as the Adler lock rate
   — transfers to any pointer, the chiral form being the fermionic instance.

The two halves of this paper's title therefore stand in an asymmetric relation,
and we state it plainly. The *two regimes* are regimes of the chiral coupling —
that analysis (§2) is the framework's own. The *measurement mechanism* runs, in
every laboratory detector, on the electromagnetically-einselected which-path
basis (§3.7), where the chiral register is a passenger. The chiral coupling
supplies the framework's ontology, its clock, and its no-go discipline — not
its pointer.

---

## 4. The bulk reference

### 4.1 What the bulk is: a faint thermal bias, not a coherent macrostate

It is essential not to overstate the bulk's coherence. The reference is **not**
a macroscopically entangled or coherent quantum state. The cleanest quantitative
handle is magnetic resonance: the equilibrium nuclear polarization that defines
the bulk reference axis in MRI is P ≈ ℏγB₀/2k_BT ≈ 5 parts per million at 1.5 T
and body temperature. The bulk is ~99.999% thermal, disordered, and mixed; the
"reference" is a faint statistical bias on top of a hot reservoir. That faint
bias is nonetheless sufficient to image the proton distribution of the body —
existence proof that a measurement reference need not be a coherent macrostate.

We therefore drop the language of an "entangled bulk." The reference is a
*phase-synchronized bias*, maintained by whatever interaction dominates locally.

Two attributes of that bias must be held apart, because temperature treats them
differently. Write the reference as a complex order parameter $r\,e^{i\psi}$: a
*magnitude* $r$ — how large the bias is, the parts-per-million above — and a
*phase* $\psi$ — the reference *axis*, the direction the bias points, fixed by the
dominant interaction (the direction of B₀ in MRI). Temperature suppresses the
magnitude but not the axis. The ~99.999% thermal disorder is exactly what holds
$r$ down to ppm; it does **not** erase $\psi$, which is pinned by the deterministic
locking. The bulk is therefore *faint but oriented* — small amplitude, definite
axis — and these are independent properties, a point §4.3 makes dynamical. That
the axis $\psi$ survives what temperature destroys is not incidental: the axis is
the coherent content any reference must carry — a vanishing amplitude $r$ can still
serve, but a bath with no definite axis is no reference at all (§4.2).

### 4.2 Absolute phase is gauge; only differences are physical

A natural objection is that the bulk's phase Φ_bulk cannot be measured — any probe
prepared with a known phase synchronizes to the bulk on contact, so its absolute
value is hidden by construction. This is not fatal; it is the same status that
global phase, absolute gravitational potential, and absolute velocity have
throughout physics. The discipline it imposes is that **every physical claim must
reduce to a phase difference.** Accordingly, the framework's entire observable
content involving Φ_bulk lives in differences between regions — and there is
exactly one such observable difference, the gravitational case of §6. Anything
said about Φ_bulk that does not reduce to a measurable difference is
interpretation, and we label it as such.

One distinction must stay sharp, because the revision turns on it: the
unobservability of the *absolute U(1) phase* is a gauge fact — only phase
differences are physical — and it is independent of the separate question of a
preferred Lorentz *frame*. The framework keeps the former and, as §8 makes
explicit, does **not** thereby claim the latter away: the bulk defines a physical
rest frame even though its absolute phase is gauge. "Absolute phase is hidden" is
not the same statement as "there is no preferred frame," and we do not use the
first to imply the second.

A familiar optical system makes this discipline concrete: holography. A hologram
fixes on the plate the interference of an *object* wavefront with a coherent
*reference* beam — that is, their *phase difference* (the fringe pattern), never
either phase alone. Add a common global phase to object and reference alike and the
fringes are unmoved — the gauge fact, "absolute phase is hidden"; advance one
*relative* to the other and the fringes shift by a readable amount — the physical
difference. (Phase-shifting holography reads out precisely this differential; an
off-axis reference contributes only a fixed common carrier that drops out of the
reconstructed object, the optical echo of an unobservable uniform background.) One
feature of the analogy is load-bearing rather than decorative: **a hologram cannot
be recorded in incoherent light.** Without a phase-stable reference there is no
stationary fringe — only a washed-out average. This is the optical form of the
framework's central requirement, that a measurement reference be phase-coherent —
*one cannot lock to noise* — and it is why Φ_bulk cannot be identified with the
phase-random zero-point vacuum ($\langle E\rangle = 0$), which belongs instead to
the stochastic forcing $\eta$ of §4.3. We give this as analogy, and label it as
such; the frame claim itself rests not on the analogy but on the single global
difference of §6.

The coherence requirement also separates three roles the word "vacuum" otherwise
blurs. (i) The condensate that locks L↔R and dresses the Dirac mass (§2, §3.6) is a
coherent vacuum expectation value — a definite-valued reference. (ii) The
measurement reference Φ_bulk of this section is likewise coherent and oriented, but
its frame-bearing *selection* is the open problem of §8, not a settled value. (iii)
The zero-point fluctuations — phase-random, $\langle E\rangle = 0$ — are not a
reference at all but the decohering noise of §3.5 and §4.3. Holography forbids
collapsing (iii) into (i)–(ii): incoherent light records nothing. The framework's
outstanding obligation is thus confined to (ii) — supplying a coherent,
frame-bearing Φ_bulk — and §8 carries it as such.

### 4.3 Magnitude and rate are independent

The smallness of the reference (§4.1) does not weaken the mechanism. The
equilibration *rate* — how fast a perturbed system re-locks to the bulk — is set
by the coupling to the bath (in MRI, T1 and T2), and is independent of the
order-parameter *magnitude* (the ppm polarization). A faint reference can drive
fast, sharp, definite relaxation. Measurement definiteness rides on the rate, not
on the order-parameter size.

This separation has a dynamical companion, and it is where temperature enters as
an explicit *randomization term in the phase synchronization itself.* Write the
deviation of a locking system from the bulk phase as δ; near the lock it obeys

$$\dot\delta = -K\delta + \eta(t), \qquad \langle\eta(t)\eta(t')\rangle = 2D\,\delta(t-t'), \qquad D \propto k_BT,$$

a deterministic restoring force of strength $K$ that pins the axis, plus a
stochastic thermal forcing $\eta$. The steady state is Gaussian with variance
$\langle\delta^2\rangle = D/K$, and the coherence amplitude of the lock is
$r = e^{-\langle\delta^2\rangle/2}$. This makes the §4.1 amplitude–axis split
precise as a statement about *moments*. Temperature acts through one of them only:
it widens the phase *variance* (the second moment) and thereby damps the amplitude
$r$, while the *mean* phase — the axis $\psi$ (the first moment) — is held by the
restoring force and does not move. "Temperature randomizes the phase" means exactly
this: it inflates $\langle\delta^2\rangle$, lowering the amplitude, not rotating the
axis. The amplitude does depend on the *ratio* $D/K$, so it is tied to the lock
rate; the equilibrium polarization of §4.1 and the axis are the quantities that
vary independently of it.

Which fluctuations dominate the forcing $\eta$ is set by where the relevant
transition sits relative to the thermal scale: the thermal occupation of a mode
at frequency $\omega$ is $\bar n = (e^{\hbar\omega/k_BT}-1)^{-1}$, so for optical
transitions ($\hbar\omega \sim 2\,$eV $\gg k_BT \sim 0.025\,$eV) the zero-point
(vacuum) fluctuations dominate the selecting noise and the thermal contribution
is negligible, while for radio-frequency systems ($\hbar\omega \ll k_BT$, NMR)
the forcing is thermal, $D \propto k_BT$ as written above. The noise that
selects at an optical photodetector surface is thus vacuum-dominated; at an NMR
coil, thermal — one envelope, two regimes of its source.

This thermal half of the envelope is not just a model: it is the measured
behaviour of matter-wave interference. Heating C₇₀ fullerenes until they emit
thermal photons reduces the fringe visibility in quantitative agreement with
decoherence theory [28] — temperature damps the amplitude, not the fringe
positions, exactly the amplitude-not-axis statement above. The same envelope
$e^{-\langle\delta^2\rangle/2}$ — the influence-functional form $e^{-\mathrm{Im}\,\Phi}$
of §3.5 — reappears in §6, where the variance is supplied not by temperature but by a
far smaller gravitational phase difference: one slot, two candidate sources — the
thermal one measured and standard, the gravitational one contingent on the postulate
of §6.2 and absent without it.

### 4.4 The role of gravity, stated honestly

In ordinary matter the interaction that maintains the bulk reference is
electromagnetic — B₀ in MRI, lattice and Coulomb binding in a solid-state
detector, supersaturation metastability in a cloud chamber. Gravity is
negligible there by ~30 orders of magnitude, and we make no claim that gravity
maintains everyday detector coherence. In particular, we do **not** assert a
gravitational coherence rate of the form Γ_grav ~ GM²/(ℏΔz): summing N²/2
unnormalized pairwise gravitational couplings does not yield a physical
relaxation rate (the mean-field coupling must be normalized intensively), and the
resulting figure is a dimensional artifact, not a derived rate.

Gravity enters in exactly one place: where the electromagnetic relaxation channel
has been deliberately engineered away (the cold, isolated, mesoscopic regime of
Penrose–Diósi tests), and, separately, through the ordinary gravitational
**redshift** of the electromagnetically-maintained reference clocks at different
potentials — which is the basis of the prediction in §6. The first is the
classicalization regime Penrose's objective reduction [15] aims to describe; the
second is standard general relativity applied to the detector references, not a
new gravitational coherence mechanism.

---

## 5. One mechanism, many detectors: capture strength and commit threshold

A single mechanism — capture, selection, registration (§3.1) — spans
measurements that look very different. Two numbers characterize a detector
architecture along it: the **per-event capture rate**
$r \propto \sigma(\omega)\,|\psi|^2$ (Stage 1 — the energy selectivity lives in
the cross-section $\sigma(\omega)$, which *multiplies* the local intensity, so
resonance acts as a rate factor rather than a gate), and the **commit
threshold** $k$ — how many captures must accumulate at one site, within that
site's memory time $\tau_{\text{mem}}$, before Stage 2 commits and Stage 3 can
fire. The older unifying axis — how deep inside the Arnold-tongue locking range
each capture sits — is the first number; the second is orthogonal to it.

| | Stage-1 capture | Reversible window (Stage 2) | Stage-3 registration (reservoir) | Commit threshold $k$ | Reference maintained by |
|---|---|---|---|---|---|
| **Bell/photon detector** | photon resonantly absorbed by a bound electron | brief (resonance fluorescence) | electronic **amplification** (avalanche, PMT gain; applied voltage) | 1 | EM lattice binding |
| **NMR / MRI** | RF pulse tips M coherently | **T2\* — refocusable by spin echo** | T1/T2 relaxation to lattice | — (ensemble, continuous) | **B₀ (applied EM field)** |
| **Cloud / bubble chamber** | a *sequence* of weak partial ionizations | partial, per event | stepwise droplet/bubble nucleation (supersaturation) | 1 per vertex, many vertices | EM (metastable supersaturation) |
| **Photographic emulsion / hologram plate** | photolysis in a silver-halide grain | **sub-latent-image speck — decays if not reinforced** | chemical development (developer reservoir) | ≈ 3–4 per grain [44] | EM (grain chemistry; developer metastability) |

Four readings of the same structure:

- **Bell detector — the strong/projective limit.** One event saturates the
  locking range; the irreversibility is the amplification, not the bare
  excitation (a single excited electron can re-emit; the avalanche cannot be
  undone). One quantum, one capture, one commit, one registration, one click.
  Because $k = 1$ — every capture commits — the per-event statistics are the
  outcome statistics directly: this is the detector class for which per-event
  Born claims are properly made.
- **MRI — isolated, deliberately-triggered Stages 2–3.** Here B₀ sets the reference
  axis and Larmor frequency ω₀ = γB₀ (the role of "Φ_bulk"); the *gradient* coils
  are not the reference but the spatial encoder, the direct analog of the
  Stern–Gerlach gradient that converts internal phase into a position/frequency
  label. The RF pulse is the coherent capture; relaxation is Stages 2–3, watched
  directly. Every free-induction decay is, in framework terms, a Stage-2/3
  emission measurement — and the ensemble character of the readout means no
  single-quantum commit threshold applies.
- **Cloud chamber — the weak/repeated limit.** The charged particle undergoes a
  *sequence* of distinct vertices, each a weak partial capture (removing tens of
  eV from a MeV–GeV particle) seeding a local commit and nucleation. It is not
  one drawn-out measurement but many partial capture–commit–register triplets:
  one particle, many sites — $k = 1$ per vertex, with the number of *vertices*
  the large number. The collinearity
  of the track (Mott 1929 [16]) measures the per-event partiality: each capture
  only partially sharpens the momentum, so the next fires preferentially along
  the line of flight. dE/dx is the per-event coupling strength integrated over
  the trajectory.
- **Photographic emulsion — the integrating limit.** Many quanta, one site: a
  grain commits only after $k \approx 3$–$4$ photolysis events build a stable
  latent-image speck (Gurney–Mott [44]), and a sub-threshold speck *decays* if
  the next capture does not arrive within its memory time. That decay is
  **reciprocity failure** — the photographic fact that a total exposure
  delivered slowly records less than the same exposure delivered fast — and in
  the present division it is direct, everyday evidence that Stage 2 and Stage 3
  are physically distinct: Stage-2 progress can be made and then lost without
  ever reaching registration. An integrating detector reports a *nonlinear
  functional* of $|\psi|^2$ (the Hurter–Driffield response), which is why
  per-event Born statistics is a $k = 1$ claim, and the emulsion — including the
  hologram plate — is the wrong exemplar for it.

The same incoming fermion leaves a single click in a silicon pixel and a
millimeter trail in a chamber because the two architectures exercise opposite
ends of the capture-strength axis — projective saturation versus near-threshold
partial capture — not because the underlying vertex differs. The emulsion adds
the orthogonal axis: commit threshold and memory time — one site integrating
many quanta, versus one quantum committing at one site.

---

## 6. A candidate prediction: a linewidth-dependent gravitational Bell test, and the postulate it requires

### 6.1 Statement of the candidate effect

The framework *suggests* an observable departure from standard quantum optics —
but, as we show in §6.2 and derive in Appendix C, the effect does **not** follow
from the framework together with standard quantum electrodynamics. It requires an
additional, non-standard postulate. We state the candidate effect here and isolate
the postulate it rests on in §6.2; the experiment is best read as a falsification
test *of that postulate*, not as a clean consequence of the framework.

Two detectors A and B in a photonic Bell test sit at gravitational potentials
Φ_A ≠ Φ_B. Their electromagnetically-maintained reference clocks are redshifted
relative to each other by the standard factor ΔΦ/c². *If* the local reference
couples into the polarization measurement (the postulate of §6.2), then over a
measurement the relative reference phase accumulates

$$\delta\phi_{\text{grav}} = \omega\,\frac{\Delta\Phi}{c^2}\,\tau_{\text{coh}} = \frac{\omega\,\Delta\Phi}{c^2\,\Delta\nu},$$

where τ_coh = 1/Δν is set by the photon **linewidth**, independent of central
energy. The *functional form* −cos(2(a−b)) is set by the polarizer geometry (a
reversible basis selection that precedes Stage-1 capture) and is gravitationally
invariant. The *contrast* would then degrade as

$$\text{CHSH}(\Delta\nu) = 2\sqrt{2}\,\exp\!\left(-\frac{\delta\phi_{\text{grav}}^2}{2}\right)$$

(Gaussian line). Standard QM/QED predicts CHSH independent of linewidth at fixed
entanglement fidelity; the candidate effect is a linewidth-dependent degradation
in a gravitational gradient. Whether it exists at all hinges on §6.2.

### 6.2 The postulate the effect requires, and why it does not follow from standard QED

**Magnitude, conditional on the coupling.** Were the local reference to couple
into the projection, the redshift would enter as a *steady, deterministic*
frequency offset, not a stochastic per-period kick; a steady offset accumulates
phase linearly in time, so δφ ∝ τ_coh = 1/Δν. The contrary "per-optical-period
floor" reading, which would make any effect negligible, is incorrect for a steady
offset. This fixes the *scaling* of the candidate effect — but says nothing about
whether the coupling exists.

**It does not follow from standard QED (Appendix C).** We attempted to derive the
required coupling from the standard light–matter Hamiltonian. The absorption
matrix element factorizes into a polarization projection (carrying the analyzer
angle) times a temporal/energy factor (carrying the local-clock phase, redshift
included). These multiply; they do not mix. The clock phase enters the detection
probability only through the modulus of the temporal factor, |T|², which is
independent of the analyzer angle — so the redshift is a common-mode phase that
cancels in the normalized correlation. Standard QED therefore predicts CHSH
independent of linewidth: the null.

**For the effect to exist, the H and V branches must carry different local-clock
phases** — the local temporal reference must couple to the *polarization
projection itself*. We checked every apparatus element that could plausibly supply
this, and none does:

| Element | Dissipative? | Polarization-dependent phase? | Carries A–B redshift into the correlation? | Why it fails |
|---|---|---|---|---|
| Detector electron | yes | no | no | H and V absorbed at the same potential Φ_A → common local phase |
| Polarizing beam splitter | no (unitary) | yes (birefringence) | no | reversible → a recalibratable, linewidth-independent phase, not a decoherence envelope |
| Absorbing polarizer | yes, on the *rejected* photon | no | no | post-projection the transmitted photon retains no H/V memory; same-potential null |
| Path deflection / crystal recoil | normally negligible / reversible | yes (recoil) | no | Stern–Gerlach-like and reversible; any recorded recoil references the same crystal at Φ_A for both branches → common phase |

The four failures share one root cause: at a single detector both Bell branches
reference the *same* local potential, and every genuinely dissipative step occurs
*after* polarization projection, when the photon no longer carries which-branch
information. The A–B redshift can enter the correlation only through a coherent,
pre-projection, polarization-*differential* phase — and the sole element that fits
(birefringence) is unitary, recalibratable, and linewidth-independent.

**The required postulate, stated explicitly.** The candidate effect therefore
rests on an additional term, schematically

$$H' \sim g\,(\mathbf{d}\cdot\hat{\mathbf{H}})\,\phi_{\text{bulk}},$$

coupling the polarization projection directly to the local background phase. This
term is (a) absent from standard QED; (b) non-covariant — it singles out the
analyzer axis and so breaks the rotational symmetry of the dipole interaction; and
(c) tied to the absolute bulk phase, and hence to the physical preferred frame
the framework openly carries (§8), whose Lorentz-covariant formulation remains
open. We are specific about the defect and its repair: coupling to the *absolute*
phase $\phi_{\text{bulk}}$ violates the $U(1)$/shift symmetry under which only the
gradient $\partial_\mu\theta$ of a phase is physical; a gauge-legal form couples
instead to that **gradient** — a physical Goldstone current of the bulk order
parameter — rather than to the bare phase. The $1/\Delta\nu^2$ scaling survives
this repair, for a simple reason: the observable content of the postulate was
never the absolute phase but the local *rate* of the reference, and that rate is
the temporal component of the gradient, $\partial_t\theta = \omega_{\text{ref}}(\Phi)$
— precisely the quantity gravitational redshift shifts,
$\omega_{\text{ref}}(\Phi_A)-\omega_{\text{ref}}(\Phi_B) = \omega\,\Delta\Phi/c^2$. A
gauge-legal coupling $H'' \sim g\,(\mathbf{d}\cdot\hat{\mathbf{H}})\,\partial_t\theta$
therefore still enters as a steady, deterministic, polarization-differential
frequency offset between the wings, accumulating phase linearly over
$\tau_{\text{coh}} = 1/\Delta\nu$; the $\delta\phi_{\text{grav}}\propto 1/\Delta\nu$
accumulation, and hence the $1/\Delta\nu^2$ visibility exponent of §6.1, carry over
unchanged, while only the physically-empty absolute offset drops out. (This is the
qualitative argument; a full re-derivation with the gradient coupling is not carried
out here.) What the repair changes is the postulate's status, not the signature:
$H''$ is shift-symmetric but remains non-covariant — it still singles out the
analyzer axis — and absent from QED. Either way the term is presented as a
deliberately symmetry-reduced *falsification term*, not a natural consequence of the
framework.

**What the experiment tests.** Because the effect does not follow from the
framework plus standard optics, the experiment is a clean falsification test *of
the postulate $H'$*, not of the framework's core. A null result (CHSH flat versus
linewidth) confirms standard QED and disconfirms $H'$; a degradation scaling as
1/Δν², present only with an altitude split, would be evidence for it. We do not
claim the effect is a derived consequence of MCI — we have shown it is not — and
we present it as the one place the framework *could* be made to touch experiment,
contingent on a postulate we cannot currently derive.

Two consistency notes survive the demotion. First, even under $H'$ the clock phase
enters only as a multiplicative visibility envelope (a contribution to the
$\mathrm{Im}\,\Phi$ decoherence functional of §3.5, present only under $H'$); it does
**not** generate the correlation. Standard QM supplies both −cos2(a−b) and the $2\sqrt{2}$ ceiling
— the clock-as-hidden-variable model alone is sub-classical (Appendix A) — so the
framework never double-counts the clock as the source of the correlation. Second,
the established gravitational-time-dilation visibility effects [24, 25] do not
apply here: they require a real internal clock in a spatial superposition
straddling both potentials, which the Bell photons lack — which is precisely why
an extra postulate is needed rather than an existing mechanism.

### 6.3 Consistency with existing satellite tests

Existing long-baseline Bell tests do not already constrain the postulate of §6.2.
The Micius
satellite experiments and ground tests use broad-linewidth spontaneous parametric
down-conversion (SPDC) photons (Δν of order GHz–THz); for those, δφ_grav is of order
10⁻⁷ or smaller even over 500 km altitude differences, far below resolvability.
The candidate effect is specifically *narrow-linewidth*: it would require
cavity-filtered photons (Δν ~ kHz) to bring δφ_grav to order unity at km-scale
altitude differences. This is why the signature has never been tested — no Bell
test has combined narrow linewidth with a gravitational gradient.

### 6.4 Parameter space and falsification

The discriminating measurement is a joint linewidth × altitude scan with
cavity-filtered narrow-linewidth entangled photons. Photon central energy is not
the discriminator; linewidth Δν and altitude split ΔΦ are. Order-of-magnitude:
δφ_grav ~ 1 requires roughly ω(gh/c²)/Δν ~ 1, i.e. for optical ω ~ 4×10¹⁵ rad/s
and a few-km altitude split (gh/c² ~ 3×10⁻¹³), a linewidth of order kHz. A
calibrated scan at fixed entanglement fidelity that holds CHSH flat across
linewidth would disconfirm the postulate $H'$ of §6.2 (and confirm standard QED); a
degradation scaling as 1/Δν², present only with an altitude split, would be
evidence for it.

A second, independent gravitational handle targets the *ontology* rather than the $H'$ postulate: reading $|\psi|^2$ as a real energy density makes a delocalized mass source a mean field $\propto E|\psi(x)|^2$ (semiclassical, Møller–Rosenfeld), so it would *not* gravitationally entangle two masses — a null in the Bose–Marletto–Vedral tabletop test, where quantized gravity predicts entanglement. This is a far-future test that inherits the known difficulties of semiclassical gravity (it plausibly requires a Diósi–Penrose-type collapse, already constrained by matter-wave and spontaneous-radiation bounds), and is noted here as a discriminator of the wave-energy *reading*, not as a prediction the framework's core requires.

---

## 7. Relation to other interpretations

### 7.1 An honest placement: the single-world, ψ-ontic, nonlocal family

MCI takes ψ to be a real physical field (ψ-ontic, in the sense of Harrigan and
Spekkens [17], consistent with PBR [18]) and adds a beable: the actual
configuration of the background/vacuum field at each event, whose value selects
the outcome. Its proper category is therefore the **single-world, ψ-ontic,
nonlocal hidden-variable** family — alongside Bohmian mechanics [2, 3] (beable:
particle position) and Nelson's stochastic mechanics [19] (beable: a stochastic
background). This is the framework's real intellectual home, and naming it
honestly is more durable than positioning MCI as a slayer of any rival.

The ψ-ontic reading is not a bare metaphysical preference; it is the stance under
which several long-established results of single-particle Dirac theory read most
naturally. Ohanian [38] recovers the electron's spin and magnetic moment as the
angular momentum of the *circulating energy flow* and the moment of the
*circulating charge flow* of the Dirac field — observables obtained by treating
the field as a real, spatially-extended distribution rather than a probability
amplitude over a point. The Gordon decomposition [39] makes the structure
explicit: the conserved Dirac current splits into a convection current and a spin
magnetization current, which in the exact Dirac–Coulomb solution of hydrogen
[40, 41] are the real circulating currents of a stable, spatially-distributed
bound state — the orbital current carrying the orbital moment, the magnetization
current carrying the spin moment with g = 2 — whose interference reproduces the
fine structure, and whose internal circulation sits at the Compton/zitterbewegung
scale of §2.4. None of this *proves* field realism — each result also admits an
operational reading, and the integrated spin and moment are notably independent
of the wave-packet envelope, so the support is for an *extended real field*, not
a particle of definite radius. But the field-realist interpretation is the one
under which spin, the magnetic moment, and the hydrogen spectrum are properties
of a single real, extended object; we take that consonance as independent
motivation for the ψ-ontic commitment, not as a derivation of it.

### 7.2 Against Many-Worlds: a trade, not a conquest

The contrast with Everett [1] is a *trade of costs*, and we state it as such.
The moment one insists on a single world with definite outcomes that reproduces
quantum statistics, Bell's theorem forces nonlocality. MWI escapes Bell only by
denying definite single outcomes — it buys **locality** at the price of **many
worlds**. MCI makes the opposite trade: it buys a **single world** at the price
of **nonlocality** (in the Bell sense — not signaling; §7.5). No interpretation
pays neither price. So MCI does not *abolish* the nonlocality that troubled
Einstein; it relocates the cost from branching worlds to nonlocal beables, as
Bohm does. We accordingly describe MCI as *a single-world alternative to
Many-Worlds*, not a replacement that escapes its difficulties for free.

### 7.3 Against Bohm and Nelson: what MCI still owes

Within its own family MCI is currently the least complete member, and honesty
requires saying so. Bohm has an explicit dynamical law (the guidance equation)
and a clean account of the Born measure (quantum equilibrium, |ψ|²). MCI now adopts
the first — the coherent guiding law is the Madelung velocity $\mathbf{v}=\nabla\varphi/m$
of §2.2, read ontologically (§2.5) — but still owes the rest: no specified equation
for *how* the background configuration selects the basin (the *dynamical* locus of
its nonlocality, though the *ontological* locus is identified in §7.5), and an
incomplete Born account — the fork of §3.3, not restated here. What this section
adds is the comparative point: reading |ψ|² as the energy density of a real field
is true but, for the equal-energy channels the framework treats, coincides with
the occupation fraction by normalization and so explains nothing about outcome
statistics — leaving MCI without Bohm's clean quantum-equilibrium answer. (The
substrate-sampling model of §8 is the candidate mechanism-level refinement — an
equilibrium bath converting a linear real-field drive into $|\psi|^2$-weighted
selection — but it relocates the postulate rather than removing it, so the debt
stands.)

This recasting also fixes what a superposition *is*, and the point is worth
making because the careless version invites a hidden-variable misreading. What is
definite is the field: a system "in superposition" is a single definite
ψ-configuration that merely fails to be an eigenstate of the observable one
chooses — superposition is a relation between the definite field and a chosen
reference basis, not an indefiniteness in the field. What is *not* a property of ψ
is the outcome, which is co-produced at Stage 2 by ψ together with the per-run
background configuration (§3.3) and fixed only when that background is sampled.
This is precisely Bohm's structure — a definite ψ with a contextual outcome — with
the beable changed from particle position to background field, so that "definite"
never attaches to the outcome and no local outcome-predetermining variable is
smuggled in (Appendix A). The reading earns its place: an observable's result is
background-sensitive exactly when ψ is not its eigenstate, so "superposition with
respect to A" *is* the condition that the Stage-2 selection depends on the
background, and the Born weight |⟨a|ψ⟩|² is, on this reading, the measure of those
backgrounds that select basin a. Why that measure takes the squared-overlap value
is the §3.3 fork again, carried in §8.

Against these debts stand three distinctions, and they are sharper than "a more
physically-motivated beable."

First, **the guiding field is physicalized, not posited.** Bohm's quantum
potential $Q = -\hbar^2\nabla^2 R / 2mR$ is read off the amplitude of $\psi$ after
the fact; it has no source of its own and no dynamics independent of the
wavefunction it is extracted from. In MCI the analogous guidance is *inherited
from the vacuum the particle traverses*: minimal coupling is carried not by the
bare particle wavefunction but by the vacuum's virtual-pair fluctuations, which
coherently *dress* the particle's phase — the reversible $\mathrm{Re}\,\Sigma$
dressing of §2.5 and §3.6, not a dissipative lock; §2.3 reserves "locking" for
the open regime, and in free flight only the closed regime runs (§2.5) — so the
particle's phase is the vacuum phase it tracks.
We are precise about which half of Bohm's amplitude–phase split this
captures. The directly physicalized quantity is the *phase* — the Hamilton–Jacobi
$S$ — not literally the amplitude-side $Q$. (That this phase appears as the
Aharonov–Bohm phase $e\Phi/\hbar$ recovered from zero-frequency locking is developed
in separate work [26], and is not relied on here.) The amplitude
side enters through the *same* coupling's fluctuations: the variance
$\langle\delta^2\rangle$ of the residual phase mismatch about the locked solution
damps fringe contrast, and that loss of $R$-coherence is the decoherence
(amplitude) physics. Where Bohm carries two formally separate objects — a guidance
equation acting on $S$ and a quantum potential built from $R$ — MCI traces both to
one mechanism, the particle's coupling to the fluctuating vacuum: the coherent
dressing supplies the guidance; its fluctuation variance — sampled dissipatively
only at boundaries (§2.5) — supplies the amplitude/decoherence side. We present this as a structural correspondence, not an
identity $\langle\delta^2\rangle = Q$.

Second, **it is relativistic from the start.** Textbook Bohm begins from the
Schrödinger equation and must then have a preferred foliation grafted on to make
its nonlocal dynamics covariant [27] — the standard charge that Bohmian mechanics
is non-relativistic. MCI's Stage-1 dynamics is instead built from Lorentz-covariant
Weyl/Dirac objects: the off-diagonal chiral mass coupling $L \leftrightarrow R$,
with zitterbewegung as the $L$–$R$ beat (§2). Covariance is therefore present in
the pilot dynamics by construction rather than added afterward. (Single-particle
relativistic Bohm already exists in the Bohm–Dirac current-guidance form [27];
MCI's added content is the Stage-2 synchronization that supplies definite outcomes
and the vacuum beable, not the relativistic single-particle law itself.)

Third — the sharpest contrast — **Bohm's preferred frame is undetectable; MCI's is
physical.** The foliation Bohm needs is, by construction, empirically inaccessible.
MCI's nonlocality is instead anchored to a *physical* preferred frame, the
bulk/vacuum rest frame (§8), whose effects are in principle observable. The handle
this paper carries is the gravitational channel of §6 — contingent on the §6.2
postulate, and weak, but self-contained: unlike Bohm's frame, MCI's is the *kind* of
object that can leave an imprint. We take the conservative reading: ordinary matter
couples to that frame, beyond the electromagnetic Stage-2 locking, only
gravitationally, so the residual anisotropy in everyday particle physics is
gravitationally weak (§8). A stronger, *kinematic* coupling to the same frame — a
velocity-dependent vacuum-locking envelope, with a fringe-visibility-versus-$\gamma$
scan as its direct test — is developed in separate work [26] and is *not* relied on
here; the in-paper contrast with Bohm stands on the §6 channel alone. Whether that
channel suffices is what would decide whether Bohm's hidden foliation has, in this
framework, become a measurable physical frame.

The distinctive debt remains the two items above. The distinctive appeal is now
stronger than a slogan about beables: the beable, the guidance, and the locus of
nonlocality are one physical thing — the vacuum the particle is locked to — rather
than three independent postulates.

### 7.4 Penrose–Diósi

Both this framework and Penrose–Diósi [15, 20] cast gravity as an agent of
classicalization. We localize that role precisely: gravity acts at the
electromagnetically-suppressed regime (Stages 2–3 in cold, isolated, mesoscopic
systems), never on the basis selection that builds the correlation. Penrose's
objective reduction is a candidate description of exactly that regime; the two
proposals single out the same physical step (bulk re-establishment of coherence)
and differ in dynamical reading — threshold instability versus continuous
rephasing.

Two refinements sharpen that contrast and locate where the readings part company.
First, the divergence runs deeper than threshold-versus-continuous: Penrose–Diósi
is a *collapse* theory — it modifies Schrödinger evolution and the superposition is
objectively destroyed — whereas MCI is no-collapse, the global evolution staying
unitary with the coherence scrambled into the bulk (§3.1). Second, the two
mechanisms ask opposite things of the environment: MCI's Stage-2/3 lock is
*dissipative* and needs a bath to carry the phase mismatch into a continuum (§3.5),
while Penrose's reduction is *intrinsic* and needs none, being a property the
superposed mass distribution carries on its own. In the deep Penrose regime —
cold, isolated, mesoscopic, the electromagnetic and thermal channels deliberately
removed — that distinction is decisive: the bath MCI would dissipate into has been
engineered away, and we do not assert a gravitational dissipation channel to take
its place (§4.4). We flag a tension rather than hide it: §3.7 finds that the only
coupling able to perform a non-demolition measurement of the chiral channel — and so
to complete the Born account — is a coupling to the scalar mass density $\bar\psi\psi$,
i.e. exactly the gravitational channel this paragraph declines to assert; completing
Born would thus narrow the operator-level gap to Penrose–Diósi to the bare
collapse-versus-no-collapse distinction. The honest statement is therefore not that MCI subsumes Penrose
but that the gravity-dominated regime is exactly where MCI's dissipative mechanism
runs out of bath while Penrose's intrinsic one does not — which makes that regime
the arbiter between them: a continuous, no-collapse reading (a gravitational
coupling that damps coherence smoothly, *below* any Penrose threshold) and an
objective collapse predict different things there. That the two readings diverge
in this regime is the point made here; the continuous branch — a gravitational
reduction of the vacuum-locking rate — is pursued in separate work [26], on which
nothing above depends.

### 7.5 Bell, no-signaling, and the "unhidden variable"

We restate plainly: the framework is **not** superdeterministic. Detector
settings are free; the shared bulk environment is a *public, setting-independent*
variable that Bell's theorem permits and that does nothing to relax any Bell
assumption. There is no faster-than-light signaling — Bell nonlocality is not
signaling, and MCI, reproducing standard quantum statistics, inherits the
no-signaling theorem exactly as Bohm and ordinary QM do. The bulk reference — a *local macroscopic reference*, to use a less provocative
name for the same object — is an "unhidden" variable only in the benign sense: it makes
explicit the phase coherence that realistic descriptions of macroscopic detectors
already assume. It
is not a Bell-relevant hidden variable, and it is not a route around nonlocality.

It is worth being precise about *which* bulk this denies and which it does not,
because the same distinction locates the framework's nonlocality. Two physically
different objects travel under the word "bulk," and only one is the
setting-independent common cause just excluded:

- **The local thermal reference** at each detector — the faint, ppm bias of §4
  (B₀ in MRI, lattice and Coulomb binding in a solid-state detector). This
  performs the local Stage-2 selection and Stage-3 registration, and — through its coherence
  amplitude $r = e^{-\langle\delta^2\rangle/2}$ (§4.3) — the visibility of the
  outcome. It is established in the common past of both wings and is independent
  of the analyzer settings, so it is exactly a Bell common-cause variable; by the
  theorem (and quantitatively by Appendix A, CHSH ≤ $\sqrt{2}$) it *cannot* be the source
  of the correlations. Its coherence magnitude is irrelevant to this — a more
  coherent common cause is still bounded by CHSH ≤ 2 — so the smallness of the ppm
  bias is not the obstacle and additional coherence is not the cure. Cooling a
  detector lowers $D \propto k_BT$ (§4.3), raises $r$, and thereby sharpens the
  *visibility* of an entanglement-sourced violation; it does not, and cannot,
  convert this local reference into a nonlocal channel.
- **The extended, non-separable field configuration** carrying the entangled
  two-particle mode across both wings. This is not a common-cause variable at all:
  it is a genuinely non-separable (entangled) configuration of the ψ-ontic
  background field, and non-separability is precisely the property a local common
  cause lacks. *This* is where the framework's nonlocality resides. Ascribing it
  here is not a new postulate but a restatement of the ψ-ontic commitment of §7.1
  — the wavefunction is a real field, and an entangled pair is one extended,
  non-factorizable configuration of it spanning A and B.

Naming the locus this way settles, at the level of *ontology*, the gap §7.3
flagged ("no explicit locus for its nonlocality"): the nonlocal element is the
non-separable field configuration, not the local thermal bulk, which does only
registration and visibility. It does **not** yet settle the *dynamics* — an
explicit law for how that non-separable configuration updates across a spacelike
interval (the selection law of §8), together with a proof that the update
preserves no-signaling. The preferred frame the framework already carries (§8)
supplies the simultaneity such a law needs; the no-signaling proof does not follow
for free once the dynamics is written independently of the quantum statistics it
must reproduce, and securing it is part of the debt of §8.

### 7.6 Relational clocks and real-clock decoherence

The framework's title and its central image — that every particle carries an
internal phase clock, and that measurement is the mutual synchronization of such
clocks — place it in deliberate proximity to the relational-time tradition, and we
state the relationship precisely rather than borrow the vocabulary loosely.

In the **Page–Wootters** mechanism [29, 30] and its modern operational
formulations [31–33], time is not a background parameter but a correlation: the
global state is stationary, and dynamics is the conditional dependence of a
"system" on the reading of a "clock." MCI uses *clock* in a related but distinct
sense. Its clocks are physical phase degrees of freedom — the chiral/Compton phase
whose ±E beat is the Zitterbewegung (§2.4) — and the operation that matters is not
the *definition* of a time parameter from a clock reading but the *dissipative
phase-locking* of many such clocks to a common reference (§3). MCI does not derive
relational time; it takes many physical clocks as given and asks what their
entrainment does at a measurement. The two pictures are compatible — a
Page–Wootters clock is exactly the kind of physical phase MCI synchronizes — and
the quantum-reference-frame treatment of *interacting* clocks [32, 33] is the
natural language in which the Stage-1 coupling of a system clock to a detector
clock would be made rigorous. We note this as a possible formal home for the
framework's kinematics, not as a result we have established.

Two relational programs bear more directly on the framework's claims. First, the
**thermal time hypothesis** of Connes and Rovelli [34]: for a system in a thermal
(KMS) state, the modular flow of that state plays the role of physical time, so a
thermal reservoir does not merely *sit at* a temperature but *defines a preferred
flow*. This is suggestive for §4, where a faint, overwhelmingly thermal bulk
supplies the measurement reference: thermal time offers a candidate
first-principles account of why a hot, disordered reservoir can nonetheless fix a
definite reference *axis* (the §4.1 amplitude/axis split), and is, we think, the
most promising existing framework in which the bulk reference could be grounded
dynamically. We flag it as a direction, not a derivation.

Second, and closest of all, is the **Montevideo interpretation** of Gambini,
Porto, and Pullin [36, 37], which shares the core intuition that *real clocks
produce real loss of coherence*. There, the fundamental imprecision of any
physical clock means evolution referred to a real clock obeys a master equation
with a universal, clock-induced decoherence rate, so off-diagonal terms decay
without a collapse postulate. MCI agrees that decoherence is a physical,
clock-mediated process rather than a bookkeeping device, but differs in three
specific ways. (i) *Source.* Montevideo's loss of coherence is fundamental and
universal — a property of time itself referred to imperfect clocks — whereas MCI's
is environmental and dissipative: the Adler equilibration of an *opened* system to
a bath (§2.3, §3.2), absent for a closed system however imprecise its clock. (ii)
*Outcome selection.* Montevideo, like environmental decoherence, yields an
improper mixture and does not by itself select a single outcome; MCI adds a beable
— the per-run background configuration (§3.3) — to carry the decohered state into
one basin. (iii) *Preferred frame.* Montevideo is built to respect general
covariance; MCI openly carries a preferred frame entering through Stage 2 (§8).
The honest summary is that MCI is a dissipative, single-world cousin of
Montevideo: it relocates the clock-decoherence idea from a fundamental temporal
imprecision to a concrete environmental synchronization, then pays for definite
outcomes with a nonlocal beable and a preferred frame that Montevideo does not
require.

Finally, **relational quantum mechanics** [35] shares MCI's rejection of any
privileged observer but takes the opposite metaphysical route: RQM is perspectival
and denies absolute, observer-independent states, whereas MCI is resolutely
single-world and ψ-ontic, with one actual field configuration per event. We note
the shared anti-anthropocentrism but claim no kinship beyond it.

---

## 8. Open problems: what would make this a theory

Two problems separate a single-world *picture* from a single-world *theory*, and
the framework's status depends entirely on them:

1. **The Born measure** — the second horn of the §3.3 fork, which states the gap
   in full; this entry records only what a derivation must supply, and the routes
   tried. It must supply *typicality*: the basin geometry is 50/50, flat in |α|²
   (§3.3), so the weight has to be carried by the measure on the selecting
   ensemble; and the equivariance that would carry such a measure intact to the
   outcome holds only where the Stage-2/3 coupling is non-demolition for the
   measured observable — which, by §3.7, the electromagnetic coupling is for the
   which-path basis but not for the chiral channel (there only a gravitational
   coupling would serve; §7.4).
   Candidate routes include deriving the relevant symmetry from the U(1)
   invariance of the chiral phase under global phase redefinition, and the
   stochastic-mechanics tradition (Nelson [19]); we flag that the latter carries
   a known obstruction (the Wallstrom single-valuedness condition) and that
   stochastic electrodynamics has historically reproduced only part of quantum
   mechanics. A further route is *relaxation to quantum equilibrium*: under a
   suitably mixing sub-quantum dynamics an arbitrary initial distribution
   coarse-grains toward |ψ|², so the Born measure becomes an equilibrium rather
   than a postulate [42, 43]. This is the natural reading of the framework's
   serial background-scrambling — each boundary interaction resamples the
   unbiased background — but it has been shown for standard Bohmian dynamics, not
   for MCI's dissipative, boundary-localized selection, so whether the same
   H-theorem holds here, and with what coarse-graining, remains open.

   A minimal toy model of this route is now in hand
   (`code/born_substrate_sampling.py`). Threshold-clock detectors driven by a
   *linear* real coupling in a random-phase (equilibrium) bulk reproduce Born
   weights by winner-take-all selection. The squared measure arises from the
   delivered *power*: the sign-alternating linear term averages to zero over the
   bath phase, and the first surviving term is quadratic — so the route does not
   smuggle in, through an assumed rate law, the $|\cdot|^2$ it must explain. The
   same model *breaks* Born predictably away from equilibrium (strong drive, or
   a coherent bulk), so it carries the non-equilibrium signatures a genuine
   relaxation account would. What it does not do is prove that MCI's
   dissipative, boundary-localized selection *relaxes* to that equilibrium: the
   bulk's random-phase condition is assumed, and it is exactly the relocated
   postulate.

   Absent that proof, the $|\psi|^2$ measure is adopted as a **postulate** —
   Bohm's quantum-equilibrium hypothesis in this framework's setting (the second
   horn of §3.3) — not as a derived result; the relaxation route is a research
   program, not a discharge of the Born debt.
2. **A dynamical law for the selection.** An explicit equation by which the
   background-field configuration drives the basin selection — Bohm's analog is
   the guidance equation. The *ontological* locus of the nonlocality is now
   identified (§7.5): it is the non-separable field configuration of the entangled
   pair, not the local thermal reference. What remains is the *dynamical*
   statement — how that configuration updates across a spacelike interval —
   together with an explicit proof that the update preserves no-signaling, which is
   not automatic once the law is written independently of the quantum statistics
   it must reproduce.

Beyond these, the framework's relation to Lorentz invariance must be stated
openly, because this revision settles it rather than leaving it ambiguous. MCI
carries a **real preferred frame**: the rest frame of the bulk/vacuum reference —
in the conservative reading, the local mass–energy rest frame. Whether it is
instead a *cosmic* frame (the CMB rest frame is the natural candidate) is an open,
testable question: only a cosmic frame produces a sidereal signature, and the
LIGO sidereal companion test is designed to discriminate the two. We do not
pretend the framework is fully relational. What disciplines the commitment is *where* the frame enters. The
Stage-1 chiral dynamics is exactly Lorentz covariant; the preferred frame appears
only through Stage-2, the dissipative lock to the bulk. We are careful with the
terminology: as written — a fixed bulk/vacuum frame entering the Stage-2 interaction —
this is **explicit, low-energy Lorentz violation confined to the measurement sector**,
*not* spontaneous symmetry breaking. It would become genuinely *spontaneous* only if the
preferred frame were the vacuum expectation value of a dynamical field with a
Lorentz-covariant action (the Einstein-aether / khronometric construction, with the
bulk-phase gradient $\partial_\mu\theta$ as the Goldstone/khronon) — a construction we
do not carry out here. Away from measurement, ordinary matter couples to that
frame, beyond the electromagnetic locking itself, only **gravitationally** —
through the potential differences that produce the redshift channel of §6. Because
gravity is weaker than the electromagnetic, strong, and weak interactions that
govern particle physics by tens of orders of magnitude, the residual anisotropy
this imposes on ordinary, non-gravitational particle interactions is suppressed in
proportion — which is why the precise clock-comparison and Michelson–Morley-type
bounds have not registered it.

Two caveats keep this honest. First, the *locus* of the vacuum coupling is itself a
hypothesis — the **Vacuum Preferred-Frame Hypothesis (VPFH)**: that the quantum
vacuum carries a physical rest frame (plausibly the cosmic/CMB frame) and that its
coupling to matter is *anisotropic* in that frame. By §2.5 this coupling acts at
boundaries, not in free flight, so its signature is a **sidereal modulation of the
Stage-2 (boundary) coupling** as the apparatus orientation sweeps past the frame's
axis (the CMB apex) — a second-moment effect, a loss of fringe visibility or
squeezing, never a coherent phase shift, which the Michelson–Morley bounds already
exclude. Whether the coupling additionally reaches into *coherent, in-flight
propagation* — a stronger, velocity-dependent, zitterbewegung-scale form that is
**not** gravitationally suppressed — is a further and more aggressive claim. The
VPFH is not a commitment of this paper but of the companion analyses (developed
separately, and not load-bearing for anything claimed here), which supply its two
tests: the LIGO sidereal-anisotropy proposal probes the boundary anisotropy
directly, and a fringe-visibility-versus-$\gamma$ proposal [26] probes the
stronger in-flight form (and reads null if the coupling is confined to boundaries).
A null in both leaves MCI with only the weak gravitational coupling; a positive
result promotes the preferred frame to a boundary anisotropy, and in the in-flight
case to a laboratory-velocity effect.
Second, a *quantitative* demonstration that the surviving gravitational-strength
anisotropy lies below the established preferred-frame bounds is still owed: we have
given the reason it should be suppressed, not a proof that it clears every
constraint. A fully Lorentz-covariant formulation of the Stage-2 selection — the
explicit covariant locus of the nonlocality — therefore remains a third open
problem, alongside the Born measure and the dynamical selection law.

This also locates the §6.2 gap precisely. The polarization-dependent coupling of
measurement to the local reference, on which the one candidate prediction rests, is
a postulate we cannot derive from standard QED (Appendix C) and is non-covariant as
written — it is this same preferred-frame commitment, now made explicit, showing up
at the level of a single measurement. On distinguishability: §6 is the one
experimental handle, and even it tests that added postulate rather than the
framework's core; the remainder of the framework is, by construction, consistent
with standard quantum mechanics rather than distinguishable from it. We state that
plainly rather than imply otherwise.

---

## Appendix A: The clock-as-hidden-variable model is sub-classical

This result is the formal justification for confining the framework to the
measurement mechanism (§1.3). Consider the simplest local model in which a single
classical clock phase per particle determines the click probability by Malus's
law, P(+1 | n̂, φ) = cos²((φ − θ_n̂)/2). Evaluated for an EPR pair with a shared
initial phase (`tests/bell_phase.py`), this returns

$$E_{\text{Malus}}(a, b) = -\tfrac{1}{2}\cos(a - b), \qquad \text{CHSH}_{\text{Malus}} \leq \sqrt{2} \approx 1.414.$$

This is **sub-classical**: it falls below even the local-hidden-variable bound of
2, and far below the quantum value $2\sqrt{2}$. A phase-clock model that treats the clock
as a local variable determining the outcome therefore cannot reproduce — cannot
even reach the classical bound for — the observed Bell violations. The full
spinor (or polarization) structure of standard quantum mechanics is required to
recover −cos(a − b). This is why the framework attributes the correlations to
standard quantum mechanics and reserves synchronization for the local
measurement mechanism: the alternative is provably ruled out by the framework's
own numerics.

## Appendix B: Spin-statistics (consistency check)

MCI does not derive spin-statistics; it inherits it from the underlying Dirac
theory and shows where the fermion sign lives. The chiral pair is, as a
representation, the (½,0) ⊕ (0,½) Lorentz representation; under 2π rotation each
Weyl half acquires −1, and by the standard continuous-deformation argument
exchange inherits the same sign. In the Madelung decomposition
ψ_X = $\sqrt{\rho_X}$ e^{iφ_X} χ_X, the amplitude ρ_X (real, ≥ 0) and the phase φ_X (a real
ODE variable, symmetric under particle exchange) carry no sign; only the spinor
frame χ_X does. `tests/spin_statistics.py` verifies that the exchange amplitude
is −1 to numerical precision across six decades in v/c, and that the Kuramoto
phase ODE alone is exchange-symmetric and sign-free. This is a **consistency
check** — it confirms the framework's chiral-pair commitment is compatible with
the standard theorem; it could have exposed an internal inconsistency in the
reframing but is not, and could not be, an independent derivation.

---

## Appendix C: The redshift cancellation is structural — a Hamiltonian sketch

This appendix supports §6.2: under a standard light–matter Hamiltonian the
gravitational redshift enters the polarization correlation as a common-mode phase
and cancels, so the candidate effect of §6 requires the additional postulate $H'$
rather than following from the framework plus standard optics.

**Setup.** A polarization-entangled pair in wavepackets of spectral width Δν about
ω₀,

$$|\Psi\rangle = \tfrac{1}{\sqrt2}\!\int\! d\omega_A\,d\omega_B\, f(\omega_A)f(\omega_B)\big[|H,\omega_A\rangle|H,\omega_B\rangle + |V,\omega_A\rangle|V,\omega_B\rangle\big].$$

Each detector is a bulk-bound electron with the standard dipole coupling
$H^{A}_{\rm int} = -\,\mathbf d_A\cdot\mathbf E_A(t)$, referenced to its local
potential Φ_A.

**Factorization.** The absorption amplitude for analyzer outcome
$|a\rangle=\cos a\,|H\rangle+\sin a\,|V\rangle$ separates as

$$M_A(a) = \underbrace{(\boldsymbol\varepsilon_a\cdot\mathbf d_{eg})}_{\text{polarization projection}}\;\times\;\underbrace{\textstyle\int dt\, e^{\,i(\omega_0^A-\omega)t}(\cdots)}_{T_A:\ \text{temporal/energy factor}},\qquad T_A=|T_A|\,e^{i\phi_A},$$

where the local-clock phase φ_A — carrying the redshift, since ω₀^A is referenced
to Φ_A — lives entirely in the temporal factor T_A and is *independent of the
analyzer angle a*.

**Cancellation.** The joint amplitude is

$$\langle a,b|\Psi\rangle = \tfrac1{\sqrt2}\,T_AT_B\,(\cos a\cos b+\sin a\sin b)=\tfrac1{\sqrt2}\,T_AT_B\cos(a-b),$$

so the coincidence probability is

$$P(a,b)\;\propto\; |T_A|^2\,|T_B|^2\,\cos^2(a-b).$$

The phases φ_A, φ_B — hence δφ_grav — appear only inside the angle-independent
prefactor $|T_A|^2|T_B|^2$ and drop out of the normalized correlation. CHSH = $2\sqrt{2}$,
independent of Δν and ΔΦ. This is the null of §6.2.

**What would be needed.** A surviving effect requires the HH and VV amplitudes to
carry *different* phases, $\phi_{HH}\neq\phi_{VV}$ — a polarization-dependent
local-clock phase. At a single detector H and V are absorbed at the same potential,
so $\phi_A^H=\phi_A^V$ and the requirement fails term by term; the four apparatus
elements that might evade this are tabulated in §6.2, and each either references
both branches to the same potential or supplies only a unitary (birefringent)
phase that is recalibratable and linewidth-independent. The minimal term that would
produce the effect, $H' \sim g\,(\mathbf d\cdot\hat{\mathbf H})\,\phi_{\rm bulk}$,
is absent from QED, breaks the rotational covariance of the dipole interaction, and
is tied to absolute φ_bulk. The §6 measurement is therefore a test of this
postulate, not a consequence of standard theory.

---

## Appendix D: The Stage-2 lock as a conditional measurement

This appendix supports §3.6–§3.7. An earlier version of it derived the Adler/Kuramoto reduction
of the Stage-2 lock from an *unconditional* Lindblad equation and read a locked relative-phase as
a measurement outcome. **We withdraw that step.** An unconditional dephasing equation yields
decoherence, not a single outcome: the averaged density matrix is mechanism-blind — it cannot
distinguish "the clocks dephased into the bath" from "one ontic result was realized," since both
give the same $\rho(t)$. The phase reduction $\dot\phi=\Omega-K_{\text{eff}}\sin 2\phi$ remains
correct where the transverse radius $r\neq 0$, but a fixed point of it is not an outcome; the same
equations give $\dot r=-2\gamma r\sin^2\phi$, so the locked direction is generally a *decaying*
one, and an unconditional state with $\sigma_x$ as the measured channel spirals to the maximally
mixed center. We therefore replace the argument with the calculation a registration claim actually
requires — a conditional quantum trajectory with an explicit monitored record — and are explicit
about what it does and does not establish.

**Which observable is the pointer.** The earlier model monitored the interference channel
$\sigma_x=\bar\psi\psi$ — the oscillating clock *hand*, which precesses at $\Omega$. Continuously
measuring an observable that does **not** commute with the clock Hamiltonian
$H=\tfrac12\Omega\sigma_z$ is a *demolition* measurement: the transverse Bloch vector spirals to
the origin and the state goes maximally mixed (the "bad zero"). A *faithful, repeatable*
measurement instead monitors the **einselected pointer observable**, the one left invariant by the
system–pointer coupling [4]: a clock-commuting (QND) observable, here the conserved $\sigma_z$ (the
which-pole basis), not the rotating hand. Aligning the measured observable to the clock axis is
therefore not a device to rescue the geometry; it is the standard einselection condition
$[H,\sigma_z]=0$ for a measurement that *records* rather than *erases*. This also exposes an honest
limit, consistent with §3.7 and stated again below: ordinary electromagnetic detectors couple to
charge/position ($\sigma_x$-type) observables, which are demolition couplings for the chiral clock,
so how such a coupling einselects a stable $\sigma_z$ record is left open.

**Model.** Take the chiral pair as a qubit with clock Hamiltonian $H=\tfrac12\Omega\sigma_z$
($\Omega$ the detuning between the internal clock and the bulk reference). Couple the einselected
pointer $\sigma_z$ dispersively to a damped readout mode $a$ — standing in for the bulk's
collective coordinate — via $H_{\rm int}=\chi\,\sigma_z\,a^\dagger a$, driven to mean occupation
$\bar n$ and decaying at $\kappa$. In the fast-mode regime $\kappa\gg\chi$ the mode is
adiabatically eliminated; tracing it out leaves a measurement dissipator in the pointer basis,

$$\dot\rho \supset \gamma\,(\sigma_z\rho\,\sigma_z-\rho),\qquad
\gamma=\tfrac12\Gamma_\phi,\qquad \Gamma_\phi=\frac{8\chi^2\bar n}{\kappa},$$

so the transverse components decay at $2\gamma=\Gamma_\phi$ and the dispersive measurement rate is
$K_{\text{eff}}=\gamma=4\chi^2\bar n/\kappa$, the same constant computed from microscopic parameters
as before. What changes is its *meaning*: a rate that sets how fast a single run localizes, not a
"phase-locking rate" that by itself selects an outcome.

**Unconditional state — a mixture of the two pointer states, not the origin.** With the QND
coupling the Bloch equations are

$$\dot x=-\Omega y-2\gamma x,\qquad \dot y=\Omega x-2\gamma y,\qquad \dot z=0,$$

so the populations $z$ are *preserved* while the transverse coherence decays. A prepared pure state
tilted by $\theta_0$ from the clock axis relaxes to
$\rho(\infty)=\operatorname{diag}(|\alpha|^2,|\beta|^2)$ — the interior axis point
$(0,0,\cos\theta_0)$ with $\cos\theta_0=|\alpha|^2-|\beta|^2$. This is a *proper mixture of the two
pointer states*, not the origin: for a generic prepared state it is partially polarized along the
clock axis, not maximally mixed. The unconditional state thus tends to (a mixture of) **exactly the
two distinct pointer states** — meeting on its own terms the objection that an unconditional
Lindblad dephasing decays to the maximally mixed state — but, being an ensemble average, it still
cannot by itself select one.

**Conditional trajectory — a single run purifies to a definite, Born-weighted pole.** Conditioning
on a homodyne record of the $\sigma_z$ meter (operator $c=\sqrt\gamma\,\sigma_z$, efficiency
$\eta=1$), the state obeys the stochastic master equation

$$d\rho_c=-i[H,\rho_c]\,dt+\gamma(\sigma_z\rho_c\sigma_z-\rho_c)\,dt
+\sqrt\gamma\,(\sigma_z\rho_c+\rho_c\sigma_z-2\langle\sigma_z\rangle\rho_c)\,dW,$$

with photocurrent $dr=2\sqrt\gamma\,\langle\sigma_z\rangle\,dt+dW$, where $dW$ is the meter's vacuum
(shot) noise — the physical origin of the trajectory's stochasticity. For $\eta=1$ the conditional
state **stays pure** and diffuses along the clock axis to a pole $\pm z$: a single monitored run
reaches a *definite* outcome at *full purity*. Ensemble-averaging $dW$ returns the unconditional
equation above, and the split to the $+$pole occurs with frequency $|\alpha|^2$ (numerically $0.76$
vs the prepared $\cos^2(\theta_0/2)=0.75$, $N=400$). The discriminator between "merely dephased"
and "outcome realized" is thus the **purity of the conditional state**, not the azimuth: the
unconditional average is mixed in every case, while the monitored trajectory is pure and definite —
which is why one must track the full $\rho$, not only the phase $\phi$.

**Amplification and the cut.** A single trajectory is reversible in principle (the catch-and-reverse
and spin-echo of §3.2); the outcome becomes a *fact* when the meter signal is amplified above the
vacuum noise faster than it can be coherently reversed — a signal-to-noise condition that on the
dispersive model requires readout power $\bar n\gtrsim\bar n_{\text{crit}}=\kappa|\Omega|/4\chi^2$.
The Heisenberg cut of §3.5 is this amplification threshold — the Stage 2 → Stage 3 boundary
of §3.1: below it the interaction is an
echo-reversible dephasing; above it the record is irreversibly committed to the bulk. (We do not
here re-assert specific critical exponents for that threshold.)

**What this establishes, and what it does not.** *Established* (standard open-system /
continuous-measurement theory [4]): a faithful, einselected conditional measurement of the
clock-aligned pointer purifies a single run to a definite pole, while the unconditional average is a
mixture of the two pointer states. The appendix therefore does *not* convert a decaying Bloch
direction into an outcome — the conditional trajectory, not the unconditional average, is what
carries the outcome.

*Not established, and flagged:*

1. **Born is consistent, not derived.** The across-run weights come out $|\alpha|^2$ because the
   Born weighting is *built into* the standard measurement unraveling (the $dW$ couples to
   $\langle\sigma_z\rangle$). The appendix exhibits Born-*consistency*; deriving $|\alpha|^2$ from
   the dynamics is the second horn of §3.3, left open in §8. The place a derivation would have to
   act is the amplitude-weighting of the boundary-noise coupling — the route taken by
   objective-collapse (CSL-type) models — which is not attempted here. (A separate candidate for the *weight* — that it is the equilibrium statistics of a random-phase bulk, §8, illustrated by `code/born_substrate_sampling.py` — likewise supplies a mechanism given an *assumed* equilibrium, not a derivation.)
2. **Single-run selection.** In the unraveling used here, *which* pole a given run reaches is fixed
   by the meter's vacuum noise (genuine stochasticity). The framework's alternative — that the
   outcome is fixed by the per-run background-field configuration (§3.3, §4), the non-separable
   configuration of the entangled pair (§7.5) — is the hidden-variable completion whose explicit
   dynamical law is open problem 2 of §8; as a *local* reading it is constrained by Bell (§7.5). The
   two readings (vacuum-stochastic vs configuration-determined) are not reconciled here.
3. **The detector bridge (§3.7).** Whether ordinary electromagnetic detectors — which monitor
   charge/position rather than $\bar\psi\psi$ — einselect the clock-aligned $\sigma_z$ pointer at
   all is the bridge §3.7 leaves open. The model here is the idealized faithful-measurement limit,
   not a demonstration that real detectors realize it. For the charge/which-path basis that ordinary detectors *do* einselect (§3.7), a resonant charge-coupled readout reproduces the Born weights $|\psi|^2$ energy-independently (`code/detector_resonance_selection.py`); the open bridge is specifically to the chiral $\sigma_z$ pointer, not to which-path registration.

**Reproducibility.** The full density-matrix integration — unconditional master equation,
conditional homodyne trajectories, and the purity and Born checks — and the figure are produced by
the accompanying script `resolution/precession_radius_two_zeros.py` (numpy + matplotlib, seed 7).
The tests
check the complete $\rho$ (Bloch length / purity), not only the extracted phase angle.

---

## References

[1] Everett, H. (1957). "Relative State" Formulation of Quantum Mechanics. *Rev. Mod. Phys.*, 29(3), 454–462.
[2] Bohm, D. (1952). A Suggested Interpretation of the Quantum Theory in Terms of "Hidden" Variables, I and II. *Phys. Rev.*, 85(2), 166–193.
[3] Dürr, D., Goldstein, S., & Zanghì, N. (2013). *Quantum Physics Without Quantum Philosophy*. Springer.
[4] Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Rev. Mod. Phys.*, 75(3), 715–775.
[5] Zurek, W. H. (2009). Quantum Darwinism. *Nature Physics*, 5, 181–188.
[6] Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox. *Physics Physique Fizika*, 1(3), 195–200.
[7] Dirac, P. A. M. (1928). The quantum theory of the electron. *Proc. R. Soc. London A*, 117(778), 610–624.
[8] Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear oscillators. *Int. Symp. Math. Problems Theor. Phys.*, 420–422.
[9] Adler, R. (1946). A study of locking phenomena in oscillators. *Proc. IRE*, 34(6), 351–357.
[10] Heinrich, G., et al. (2011). Collective dynamics in optomechanical arrays. *Phys. Rev. Lett.*, 107(4), 043603.
[11] Mari, A., et al. (2013). Measures of quantum synchronization in continuous variable systems. *Phys. Rev. Lett.*, 111(10), 103605.
[12] Walter, S., Nunnenkamp, A., & Bruder, C. (2014). Quantum synchronization of a driven self-sustained oscillator. *Phys. Rev. Lett.*, 112(9), 094102.
[13] Roulet, A., & Bruder, C. (2018). Synchronizing the smallest possible system. *Phys. Rev. Lett.*, 121(5), 053601.
[14] Minev, Z. K., et al. (2019). To catch and reverse a quantum jump mid-flight. *Nature*, 570, 200–204.
[15] Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Relativ. Gravit.*, 28(5), 581–600.
[16] Mott, N. F. (1929). The wave mechanics of α-ray tracks. *Proc. R. Soc. London A*, 126(800), 79–84.
[17] Harrigan, N., & Spekkens, R. W. (2010). Einstein, incompleteness, and the epistemic view of quantum states. *Found. Phys.*, 40(2), 125–157.
[18] Pusey, M. F., Barrett, J., & Rudolph, T. (2012). On the reality of the quantum state. *Nature Physics*, 8(6), 476–479.
[19] Nelson, E. (1966). Derivation of the Schrödinger equation from Newtonian mechanics. *Phys. Rev.*, 150(4), 1079–1085.
[20] Diósi, L. (1989). Models for universal reduction of macroscopic quantum fluctuations. *Phys. Rev. A*, 40(3), 1165–1174.
[21] Bohr, N. (1928). The Quantum Postulate and the Recent Development of Atomic Theory. *Nature*, 121, 580–590.
[22] Wheeler, J. A., & Zurek, W. H. (Eds.) (1983). *Quantum Theory and Measurement*. Princeton University Press. (Wheeler's "irreversible act of amplification," after Bohr.)
[23] Daneri, A., Loinger, A., & Prosperi, G. M. (1962). Quantum theory of measurement and ergodicity conditions. *Nuclear Physics*, 33, 297–319.
[24] Zych, M., Costa, F., Pikovski, I., & Brukner, Č. (2011). Quantum interferometric visibility as a witness of general relativistic proper time. *Nature Communications*, 2, 505.
[25] Pikovski, I., Zych, M., Costa, F., & Brukner, Č. (2015). Universal decoherence due to gravitational time dilation. *Nature Physics*, 11(8), 668–672.
[26] Bramble, J. (2026). Aharonov–Bohm Visibility Envelope as a Test of Dirac–Kuramoto Vacuum Locking. Companion draft in development (`AB_VISIBILITY_PAPER.md` in the repository); cited as work in progress, not as an established result.
[27] Dürr, D., Goldstein, S., Norsen, T., Struyve, W., & Zanghì, N. (2014). Can Bohmian mechanics be made relativistic? *Proc. R. Soc. A*, 470(2162), 20130699.
[28] Hackermüller, L., Hornberger, K., Brezger, B., Zeilinger, A., & Arndt, M. (2004). Decoherence of matter waves by thermal emission of radiation. *Nature*, 427(6976), 711–714.
[29] Page, D. N., & Wootters, W. K. (1983). Evolution without evolution: Dynamics described by stationary observables. *Phys. Rev. D*, 27(12), 2885–2892.
[30] Wootters, W. K. (1984). "Time" replaced by quantum correlations. *Int. J. Theor. Phys.*, 23(8), 701–711.
[31] Giovannetti, V., Lloyd, S., & Maccone, L. (2015). Quantum time. *Phys. Rev. D*, 92(4), 045033.
[32] Höhn, P. A., Smith, A. R. H., & Lock, M. P. E. (2021). Trinity of relational quantum dynamics. *Phys. Rev. D*, 104(6), 066001.
[33] Smith, A. R. H., & Ahmadi, M. (2019). Quantizing time: Interacting clocks and systems. *Quantum*, 3, 160.
[34] Connes, A., & Rovelli, C. (1994). Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories. *Class. Quantum Grav.*, 11(12), 2899–2917.
[35] Rovelli, C. (1996). Relational quantum mechanics. *Int. J. Theor. Phys.*, 35(8), 1637–1678.
[36] Gambini, R., Porto, R. A., & Pullin, J. (2004). A relational solution to the problem of time in quantum mechanics and quantum gravity: a fundamental mechanism for quantum decoherence. *New J. Phys.*, 6, 45.
[37] Gambini, R., & Pullin, J. (2018). The Montevideo interpretation of quantum mechanics: A short review. *Entropy*, 20(6), 413.
[38] Ohanian, H. C. (1986). What is spin? *American Journal of Physics*, 54(6), 500–505.
[39] Gordon, W. (1928). Der Strom der Diracschen Elektronentheorie. *Zeitschrift für Physik*, 50(9–10), 630–632.
[40] Darwin, C. G. (1928). The wave equations of the electron. *Proc. R. Soc. London A*, 118(780), 654–680.
[41] Bjorken, J. D., & Drell, S. D. (1964). *Relativistic Quantum Mechanics*. McGraw-Hill. (Gordon decomposition and the exact Dirac–Coulomb spectrum.)

[42] Valentini, A. (1991). Signal-locality, uncertainty, and the subquantum H-theorem. I. *Physics Letters A*, 156(1–2), 5–11.

[43] Valentini, A., & Westman, H. (2005). Dynamical origin of quantum probabilities. *Proc. R. Soc. A*, 461(2053), 253–272.

[44] Gurney, R. W., & Mott, N. F. (1938). The theory of the photolysis of silver bromide and the photographic latent image. *Proc. R. Soc. London A*, 164(917), 151–167.

[45] Guerreiro, T., Sanguinetti, B., Zbinden, H., Gisin, N., & Suarez, A. (2012). Single-photon space-like antibunching. *Physics Letters A*, 376(32), 2174–2177.

[46] Lawrence, E. O., & Beams, J. W. (1928). The element of time in the photoelectric effect. *Phys. Rev.*, 32(3), 478–485.
