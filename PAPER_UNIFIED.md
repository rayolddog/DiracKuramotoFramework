# The Many Clocks Interpretation of Quantum Mechanics
## The Dirac Equation as a Kuramoto Phase-Synchronization System: Mass as Chiral Coupling, Measurement as Re-Synchronization

**J. Olddog¹**
¹ Independent Research

*Correspondence: rayolddog (GitHub)*
*Preprint — not yet peer reviewed*

*AI Disclosure: This work was developed in collaboration with Claude Opus 4.6
(Anthropic), as described in the Author Contributions section. Per current
journal guidelines, LLMs do not satisfy authorship criteria; the human author
bears full responsibility for all content.*

---

## Abstract

We demonstrate that the Dirac equation, written in the chiral (Weyl) basis, has the
mathematical structure of a Kuramoto phase-synchronization system. The left- and
right-handed chiral sectors act as coupled oscillators, with the mass term playing
the role of the Kuramoto coupling constant: K = m. For massless particles (K = 0)
the chiral clocks are permanently decoupled; for massive particles (K > 0) they
synchronize, and the synchronized state is what we identify as a particle with
definite rest mass. The Higgs-Yukawa interaction is the mechanism that sets K:
K = y_f · ⟨φ⟩ = m.

This identification has several consequences. Quantum measurement is re-interpreted
as Kuramoto re-synchronization: a particle initially synchronized with its entangled
partner re-synchronizes to the macroscopic detector bulk, whose overwhelmingly
greater Kuramoto inertia (M_detector >> m_particle) forces conformity. Decoherence
is not merely loss of phase coherence with the partner — it is the positive process
of gaining coherence with the bulk. The Born rule P = |ψ|² is reframed as the
long-run frequency of energy partition: |ψ|² is the energy density of the real
ψ field, and the apparent stochasticity of measurement outcomes arises from
unbiased zero-point + thermal background fluctuations at the synchronization
event, rather than from an independent probability axiom.
The Heisenberg uncertainty principle appears as a bandwidth limitation of the
particle's internal phase clock.

We present this framework — which we call the **Many Clocks Interpretation of
Quantum Mechanics (MCI)** — as an interpretive reframing of standard quantum
mechanics, not a modification of its predictions. The name is a deliberate
echo of, and contrast to, Many-Worlds: where MWI preserves unitarity by
branching the universe at each measurement, MCI preserves a single world by
treating each particle as carrying its own physical phase clock, with
measurement as local synchronization between clocks. No conscious observer
is required; no branching occurs. The Dirac equation is unchanged; Bell's
theorem is not challenged. What is new is the identification of mass as
synchronization coupling, measurement as re-synchronization dynamics, and
decoherence as a Kuramoto process with a specific physical mechanism.

---

## 1. Introduction

### 1.1 The Measurement Problem

The quantum measurement problem remains the most consequential unsolved problem in
the foundations of physics. The Schrödinger equation is linear and deterministic,
yet measurements have definite outcomes. A system in superposition
ψ = α|0⟩ + β|1⟩, entangled with a detector, produces

$$|\Psi\rangle = \alpha|0\rangle|D_0\rangle + \beta|1\rangle|D_1\rangle$$

The equation has no mechanism to select one outcome. The Born rule —
P(0) = |α|² — is postulated, not derived.

The three mainstream responses each carry significant costs. Copenhagen introduces
a mysterious collapse with no physical mechanism. Everett's many-worlds [16] preserves
unitarity at the cost of infinite unobservable branches. Bohmian mechanics [15] accepts
explicit nonlocality through a physically inert pilot wave.

### 1.2 What Is Missing: A Dynamical Mechanism for Decoherence

Environmental decoherence [4] has become the standard framework for
understanding how quantum superpositions become effectively classical. It
successfully explains the emergence of preferred "pointer states" and the
suppression of off-diagonal density matrix elements through interaction with
environmental degrees of freedom.

Yet decoherence theory describes *what happens* without specifying the dynamical
mechanism by which it happens. The environment is treated as an abstract bath
with many degrees of freedom. This paper proposes that the Kuramoto
phase-synchronization model — specifically, as it appears in the structure of the
Dirac equation itself — provides this missing mechanism.

### 1.3 The Proposal in Brief

We make three claims, in decreasing order of mathematical rigor:

1. **The Dirac mass term is a Kuramoto coupling** (Section 2). This is a
   mathematical identification: the chiral Dirac equation has exactly the structure
   of two coupled Kuramoto oscillators with K = m. This is the strongest claim and
   is verifiable by inspection.

2. **Measurement is re-synchronization** (Section 3). When a particle interacts
   with a macroscopic detector, the Kuramoto dynamics drive the particle's phase
   from coherence with its entangled partner to coherence with the detector bulk.
   This provides a physical picture of decoherence. This is an interpretive claim.

3. **The Born rule is reframed as energy partition** (Section 4). Reading |ψ|²
   as wave energy density and the apparent stochasticity as unbiased
   background-field fluctuation at the synchronization event, P = |α|²
   appears as the long-run frequency of channel-energy partition rather than
   as an independent probability axiom. This is an interpretive claim with
   physical motivation, not a complete derivation.

### 1.4 What This Paper Does Not Claim

We state clearly at the outset:

- We do not challenge Bell's theorem [9]. The quantum correlations E(a,b) = −cos(a−b)
  arise from the entangled singlet state and the full Dirac spinor structure —
  standard quantum mechanics.
- We do not modify the Dirac equation or any of its predictions.
- We do not propose new physics. We propose a new *mechanism* for known physics.
- The framework is an interpretation — it may or may not generate distinguishable
  predictions from standard decoherence theory. We are honest about this
  throughout.

### 1.5 Relational Structure: The Many Clocks Interpretation

We name this framework the **Many Clocks Interpretation of Quantum Mechanics
(MCI)**. The name is a deliberate echo of Many-Worlds, with a sharp contrast:
Many Worlds preserves unitarity by branching the universe at each measurement
and accepting an exponentially proliferating multiverse; the Many Clocks
Interpretation preserves a single world by treating each particle as carrying
its own internal phase clock, with measurement as local synchronization
between clocks. The interpretation is *relational* — there is no global
preferred reference frame and no observer required — and it operates by the
following structural commitments:

1. **Every particle carries one or more intrinsic phase clocks.** For massive
   Dirac fermions, two chiral clocks (L and R), coupled by K = m on the
   synchronized manifold (Section 2). For photons, polarization clocks
   coupled to detectors via K_γ ~ ω (Section 5). The clocks are physical
   oscillators, not bookkeeping devices.

2. **There is no global preferred frame.** Each interaction happens in the
   local frame jointly defined by the interacting parties. Each particle's
   clocks are intrinsic — defined in its own rest frame — and a particle's
   clock structure is described differently in different observer frames,
   but the physics of each interaction is invariant.

3. **Synchronization is a local, objective, physical event.** When two
   clock-carrying systems interact, their clocks synchronize via Kuramoto
   coupling at the interaction event. The synchronization is objective:
   distant observers in other frames may disagree about the ordering of
   spacelike-separated events elsewhere, but the two parties to a specific
   interaction always agree on what happened locally between them. This is
   ordinary special-relativistic causality, not novel — but worth stating
   because it removes the appearance of observer-dependence.

4. **No conscious observer is required. No branching is required.** A single
   objective physical world contains many clocks; interactions synchronize
   them locally; measurement is a special case of synchronization in which
   one party is a macroscopic detector with overwhelming Kuramoto inertia
   (Section 3).

5. **Past phase history is overwritten at each sync event.** After a small
   number of interactions, a particle's pre-interaction phase is effectively
   unrecoverable. This is the framework's specific dynamical mechanism for
   decoherence and thermalization: not just loss of off-diagonal coherence,
   but active phase-overwriting at each interaction event.

6. **All physically meaningful quantities are gauge- and Lorentz-invariant.**
   The individual chiral phases φ_L, φ_R shift uniformly under U(1) gauge
   transformation; only the gauge-invariant difference φ_L − φ_R enters the
   Kuramoto sine coupling. The L/R block decomposition of the spin operator
   is frame-relative under Lorentz boosts, but the sum
   E_LL + E_SS + E_LS = −cos(a−b) is Lorentz-invariant. The framework's
   *predictions* live in invariant content; the interpretive language about
   "which clock dominates" is a frame-relative description of an invariant
   structure.

The Many Clocks Interpretation has affinities with Hestenes' Zitterbewegung
interpretation (Section 7.7) — both treat the complex phase factor in the
Dirac wave function as a physical clock — and with Rovelli's relational
quantum mechanics [24], in the sense that no global preferred frame or
observer is needed. It differs from both in its explicit dynamical mechanism
(Kuramoto re-synchronization), and from Rovelli's RQM in keeping ψ ontic
rather than relational: the wavefunction is a real oscillating field, not a
relational state.

---

## 2. The Dirac Equation as a Kuramoto System

### 2.1 Chiral Decomposition

In the Weyl (chiral) basis, the Dirac spinor decomposes into two two-component
Weyl spinors:

$$\psi = \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix}$$

The Dirac equation separates into two coupled equations:

$$i\bar{\sigma}^\mu \partial_\mu \psi_L = m \psi_R \qquad (1a)$$

$$i\sigma^\mu \partial_\mu \psi_R = m \psi_L \qquad (1b)$$

where σ^μ = (I, σ) and σ̄^μ = (I, −σ) are the Weyl matrices.

**For m = 0 (massless):** Equations (1a) and (1b) decouple entirely. ψ_L and ψ_R
satisfy independent equations. The particle has definite chirality and no rest
frame. Photons and massless-limit neutrinos are in this category.

**For m ≠ 0 (massive):** The equations couple ψ_L to ψ_R and vice versa. Neither
chirality state is stable alone; the physical particle is a superposition of both.
The coupling strength is exactly *m*.

### 2.1.1 Two Bases, One Spinor

The same 4-component Dirac spinor admits two natural decompositions, which the
framework uses for different purposes. We flag them explicitly to prevent
conflations that have accumulated in earlier drafts.

- **Weyl (chiral) basis:** ψ = (ψ_L, ψ_R)ᵀ, splitting the spinor by chirality.
  The mass term is purely off-diagonal — m·(ψ̄_L ψ_R + ψ̄_R ψ_L) — which is what
  makes it natural to read as a Kuramoto coupling K = m between two chiral
  clocks. Used in §§2.2–2.6, the Higgs-Yukawa identification (§6 of the
  equations reference), and the spin-statistics analysis of Appendix D.

- **Dirac (standard) basis:** ψ = (ψ_upper, ψ_lower)ᵀ, splitting the spinor
  into a *large* component (the Pauli 2-spinor at rest) and a *small* component
  that vanishes at rest and grows with momentum as r = p/(E+m) = tan(θ_rel/2).
  The block decomposition E_LL + E_SS + E_LS of the Bell correlation
  (Appendix A; `dirac_extension.py`) is naturally written here, because the
  standard relativistic spinor u(p,↑) = N(1, 0, r, 0)ᵀ lives in this basis.

The two bases are related by a constant unitary 4×4 change of basis and
describe the same physical object. They agree at the two limits the framework
cares about most:

| Regime | Weyl picture | Dirac picture |
|---|---|---|
| Rest (θ_rel = 0) | ψ_L = ψ_R (synchronized) | small component = 0; only large |
| Massless (θ_rel = π/2) | ψ_L, ψ_R decoupled | large and small blocks decouple by helicity |

At intermediate momenta the two decompositions differ: the temporal-phase
content is a θ_rel-dependent linear combination of upper and lower blocks in
the Dirac basis, and a different θ_rel-dependent combination of ψ_L and ψ_R in
the Weyl basis. The interpretive language "temporal clock" and "spatial clock"
is most cleanly anchored in the Weyl basis — temporal ↔ ψ_L, spatial ↔ ψ_R —
and translates to the Dirac basis only via the basis change. The mixing angle
θ_rel = 2·arctan(p/(E+m)), defined operationally by the Dirac-basis large/small
ratio, is the framework's single quantitative handle on this rotation; its
geometric reading depends on which basis is in use.

We use whichever basis makes the physics of a given section most transparent
and flag the choice locally.

### 2.2 The Kuramoto Identification

The standard (classical) Kuramoto model [2] describes the phase dynamics of N
coupled oscillators:

$$\frac{d\phi_i}{dt} = \omega_i + \frac{K}{N}\sum_j \sin(\phi_j - \phi_i)$$

The coupling here is *nonlinear* — sin(φ_j − φ_i) — whereas the chiral Dirac
coupling in Equations (1a, 1b) is *linear* at the operator level: m·ψ_R sources
the equation for ψ_L and vice versa. The Kuramoto sine therefore is not present
in the Dirac equation as written. It emerges, however, as the near-equilibrium
phenomenology of the linear coupling under a polar (Madelung-type)
decomposition. We outline the reduction explicitly so that the regime of
validity is on the record.

Apply the decomposition

$$\psi_L = \rho_L^{1/2}\, e^{i\phi_L}\, \chi_L, \qquad \psi_R = \rho_R^{1/2}\, e^{i\phi_R}\, \chi_R$$

where ρ_{L,R} are real amplitude densities, φ_{L,R} are clock phases, and
χ_{L,R} are unit two-spinors carrying the spin orientation. Substituting into
Equations (1a, 1b) and separating real and imaginary parts of the time
component yields a coupled system: a continuity-like equation for the
amplitudes and a phase equation for the clocks. With the standard chiral
phase convention (the mass coupling carrying the implicit i factor inherited
from γ⁰), the phase equations take the form

$$\frac{d\phi_L}{dt} = \omega_L + K\sqrt{\rho_R/\rho_L}\,\sin(\phi_R - \phi_L + \delta_{CP}) \qquad (2a)$$

$$\frac{d\phi_R}{dt} = \omega_R + K\sqrt{\rho_L/\rho_R}\,\sin(\phi_L - \phi_R - \delta_{CP}) \qquad (2b)$$

with the coupling constant

$$\boxed{K = y_f \cdot |\langle\phi\rangle| = y_f \cdot \frac{v}{\sqrt{2}} = m} \qquad (3)$$

**On the synchronized manifold ρ_L ≈ ρ_R** — the regime relevant to a particle
that has settled into a definite mass eigenstate — the amplitude prefactors
reduce to unity and Equations (2a, 2b) become the Kuramoto form for two
coupled oscillators. Off this manifold, the amplitude dynamics couple back
through the continuity equation, and the system is properly described by the
full Madelung pair with a quantum potential. The Kuramoto picture is therefore
the *synchronized-manifold reduction* of the chiral Dirac dynamics, not a
restatement of the Dirac equation itself.

**Equation (3) is the central identification of this paper: on the
synchronized manifold, the particle's mass plays the role of the Kuramoto
coupling constant between its chiral phase clocks.** In SI units this reads
K = mc²/ℏ — the Compton frequency — making explicit that the coupling has
dimensions of frequency [time⁻¹], as required by the synchronization equations
(2a–2b).

This places the framework within the broader literature on **quantum
synchronization** [36, 37, 38, 39], where Kuramoto-form phase dynamics have
been derived from the semiclassical limit of quantum master equations for a
range of coupled-oscillator systems (optomechanical arrays, cavity-QED,
driven self-sustained oscillators, trapped-ion chains). The Weyl-spinor pair
is the chiral-Dirac instance of this general phenomenon: the operator-level
coupling is linear, but on the synchronized subspace the effective phase
dynamics are Kuramoto. The distinction between *classical* Kuramoto
synchronization (sine coupling fundamental at the equation-of-motion level)
and the *quantum* version employed here (sine coupling emergent on the
synchronized subspace from a linear underlying Hamiltonian) should be kept
explicit throughout.

The Higgs vacuum expectation value [11, 12] ⟨φ⟩ = v/√2 ≈ 174 GeV drives the two chiral
clocks into synchronized oscillation. Before electroweak symmetry breaking (v → 0),
K → 0 and all fermions are massless — their chiral clocks are independent. After
symmetry breaking, K = m and the clocks synchronize.

### 2.3 Two Clocks, Not One

The central physical picture is:

> A massive Dirac particle carries two internal oscillators: a **temporal phase
> clock** oscillating at ω_t = E/ℏ, and a **spatial phase clock** oscillating at
> ω_s = p·v/ℏ. The mass term couples them — it is the Kuramoto synchronization
> term that drives the two chiral sectors toward a common phase.

This interpretation does not modify the Dirac equation. It provides an ontological
reading of its mathematical structure.

### 2.4 The Synchronized State

At Kuramoto equilibrium, the phase difference locks:

$$\phi_L - \phi_R = \delta_{CP} \quad \text{(particles)} \qquad (4a)$$

$$\phi_L - \phi_R = -\delta_{CP} \quad \text{(antiparticles)} \qquad (4b)$$

For CP-symmetric interactions (δ_CP = 0), particles and antiparticles have
identical phase locks — consistent with CPT symmetry. The CP-violating phase
δ_CP shifts the equilibrium, providing a qualitative mechanism for
matter-antimatter asymmetry through differential synchronization efficiency.

The synchronization rate is set by K = m: heavy particles synchronize their
chiral clocks faster than light particles. An electron (m_e = 0.511 MeV)
synchronizes more slowly than a top quark (m_t = 173 GeV) by a factor of
~3.4 × 10⁵.

### 2.5 Gamma Matrices as Synchronization Operators

In the Weyl basis, the mass term in the Lagrangian is:

$$\mathcal{L}_{mass} = -m\bar{\psi}\psi = -m(\bar{\psi}_L\psi_R + \bar{\psi}_R\psi_L)$$

This is off-diagonal in chirality: it connects left to right and right to left.
In the Kuramoto language, it is the coupling term that drives the two chiral
oscillators toward synchronization.

The matrix γ^0 swaps the two chiral sectors:

$$\gamma^0 \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix} = \begin{pmatrix} \psi_R \\ \psi_L \end{pmatrix}$$

The Dirac Hamiltonian H = α·p + βm is therefore the generator of synchronized
phase evolution across both clock sectors.

### 2.6 Summary of Established vs. New Claims

| Claim | Status |
|---|---|
| Dirac mass term couples ψ_L ↔ ψ_R | Standard QFT; textbook |
| m = 0 → chiral sectors decouple | Standard QFT; textbook |
| Higgs-Yukawa sets fermion mass via ⟨φ⟩ | Standard Model; established |
| Negative-energy Dirac solutions = reversed temporal phase | Standard (Feynman-Stückelberg [21, 22]) |
| **Mass term reduces to Kuramoto coupling on the synchronized manifold** | **New interpretation (this work)** |
| **K = m identification (synchronized-manifold reduction)** | **New (this work)** |

---

## 3. Measurement as Re-Synchronization

### 3.1 The Physical Picture

This section develops the interpretive core of the framework. We propose that
quantum measurement is a specific type of Kuramoto synchronization event:

> **A particle initially phase-synchronized with its entangled partner
> re-synchronizes to the macroscopic detector bulk.**

The detector is a macroscopic system with overwhelmingly greater Kuramoto inertia
(M_detector >> m_particle). The measurement interaction forces the particle to
conform its phase to the detector's collective phase Φ_bulk, just as a small
oscillator entrained by a massive one must adopt the massive oscillator's
frequency.

### 3.2 Decoherence Is Half the Story

In the standard decoherence program, measurement causes the particle to lose
coherence with its entangled partner. This is correct but incomplete.

In the Kuramoto picture, the particle does not merely *lose* coherence with its
partner. It *gains* coherence with the detector bulk. The process has two
simultaneous aspects:

1. **De-coherence** from the entangled partner (the phase lock φ_A = φ_B
   established at creation is broken)
2. **Co-herence** with the detector bulk (a new phase lock φ_A = Φ_bulk is
   established)

Standard decoherence theory tracks only aspect (1). The Kuramoto framework makes
aspect (2) explicit: the particle's phase is not randomized — it is redirected.
The final state is not "unknown phase" but "phase locked to the bulk." This is
a definite classical state, not a mixed state that merely appears classical.

### 3.3 The Mass Asymmetry

The detector's macroscopic mass provides the asymmetry that ensures definite
outcomes. In Kuramoto dynamics, when a small oscillator (mass m) couples to a
large oscillator (mass M >> m), the small oscillator always conforms to the
large one. The reverse — the detector conforming to the particle — is
dynamically suppressed by a factor of m/M.

This is the physical content of "wavefunction collapse": the Kuramoto mass
asymmetry between particle and detector makes the measurement outcome definite,
not because of a postulated projection, but because of the dynamical inevitability
of a small oscillator locking to a massive one.

### 3.4 The Two-Stage Process: Pair-Sync and Bulk Relaxation

Sections 3.1–3.3 treated measurement as a single direct lock between the
incoming particle and the detector bulk. A more faithful picture, consistent
with the locality of fundamental interactions, separates this into two stages:

- **Stage 1 (Pair-Sync).** The incoming particle phase-couples to a single
  bulk-bound partner (e.g. a photon to an atomic electron) at the local
  interaction vertex.
- **Stage 2 (Bulk Relaxation).** The perturbed partner re-locks to the bulk's
  collective phase Φ_bulk, shedding its phase mismatch as secondary radiation.

**Yukawa-style identification of the pair coupling.** Equation (3) identified
the intra-spinor sync coupling as a Higgs-mediated mass, K = y_f ⟨φ⟩ = m. The
pair-sync coupling at an interaction vertex follows the same structure — a
dimensionless gauge coupling times the local amplitude of the mediating field:

$$\boxed{K_{\text{pair}}^{ab} = g_{\text{int}} \cdot \langle V_{\text{int}} \rangle_{\text{local}}} \qquad (3')$$

where g_int is the relevant gauge coupling (e for EM, g_w for weak, etc.) and
⟨V_int⟩_local is the gauge-field amplitude evaluated at the partner's
worldline. For the photon–electron interaction,

$$K_{\text{pair}}^{\gamma e} = e \cdot |A_\gamma|_{e} \;\sim\; \hbar\omega$$

when the photon is normalized to one excitation in the electron's Compton-scale
volume. Higher-energy photons couple more strongly to the electron's chiral
clocks, with sync timescale τ₁ = ℏ/K_pair ~ 1/ω — the photon's own period.

**Hierarchy of couplings.** The framework now carries three distinct Kuramoto
couplings, each entering at a different stage of measurement:

| Coupling | Origin | Role |
|---|---|---|
| K = m | Higgs–Yukawa | intra-spinor L–R sync (Section 2) |
| K_pair = g_int ⟨V_int⟩ | gauge interaction | pair-sync at vertex (Stage 1) |
| Γ_bulk = GM²/(ℏΔz) | gravitational + atomic | bulk re-equilibration (Stage 2) |

![Two-stage measurement of an entangled photon pair](entangled_pair_two_stage.png)

**Figure 1.** Schematic of the two-stage measurement of a polarization-
entangled photon pair (not to scale). All three bulks (Source, Detector A
bulk, Detector B bulk) contain mini-clocks locked to a universal
time-phase Φ_bulk (~70° in the figure, with σ ≈ 7° jitter), reflecting
environmental thermalization across matter sharing a common gravitational
potential. The entangled photons γ_A, γ_B carry matched chiral-clock
phases at emission but with K = 0 (dotted L–R link) and propagate freely
between source and detector. Each polarizer (black aperture with
double-headed transmission-axis arrow) defines an independently-set basis
(a, b) on the polarization Hilbert space — a separate degree of freedom
from Φ_bulk. At each detector, Stage 1 (solid box) is the polarization
projection onto the polarizer's transmitted-channel eigenstate via
pair-sync K_pair^{γe} to a bound electron; Stage 2 (dashed box)
dissipates the projected state into the bulk's Φ_bulk via Γ_bulk,
releasing secondary radiation. The cos²(θ/2) Bell visibility is set by
the polarizer-axis difference θ = a − b (standard QED), not by Φ_bulk;
the framework provides the physical mechanism for the projection, not the
statistics.

**Stage 1 as polarization projection.** The cos²(θ/2) Bell visibility for
photons is set by the polarizer-axis difference θ = a − b acting on the
photon's polarization Hilbert space — standard QED, not a framework
prediction (see §5.2). The framework's contribution at Stage 1 is the
*physical mechanism* of projection: the photon couples to a bulk-bound
electron via K_pair^{γe}, and the polarizer's macroscopic mechanical
orientation determines which transmitted-channel eigenstate the photon ends
up in. Φ_bulk, the bulk's collective time-phase, is a separate quantity —
approximately universal across the source and both detectors when they
share a similar gravitational environment, set by environmental
thermalization rather than by the polarizer geometry. The basis lives in
the polarizer's mechanical configuration; the time-phase lives in Φ_bulk.
Stage 1 connects the photon to the polarizer's chosen basis; Stage 2
dissipates the resulting state's energy and phase into Φ_bulk.

**Why Stage 2 is automatic.** After the photon perturbs the electron, φ_e is
offset from Φ_bulk by some Δφ_e. The mass-asymmetry argument of Section 3.3
applies directly: the relaxation rate scales as Γ_bulk · (M_bulk/m_e),
overwhelmingly fast for any macroscopic bulk. The energy released during this
relaxation appears as secondary radiation, partitioned by the size of the
mismatch ℏ φ̇_e Δφ_e:

- below optical scale: virtual photon (Coulomb recoil) or phonon
- optical to 2m_e c²: real photon (fluorescence, bremsstrahlung)
- ≥ 2m_e c²: $e^+ e^-$ pair

**Gravitational dependence of the two stages.** Because the Bell correlation
is set by the polarizer-axis difference (standard QED) and polarizer geometry
is gravitationally invariant at leading order, the visibility cos²(θ/2) is
itself gravitationally invariant — consistent with the agreement between
Earth-bound and space-based Bell tests. Gravity enters only at Stage 2,
through Γ_bulk, with two subleading consequences. First, two detectors at
gravitational potentials Φ_A ≠ Φ_B have Stage-2 relaxation times that differ by
ΔΦ/c², producing a correlated timing offset between detection events that
scales with the altitude split. Second, if the gravitational potential
difference along the photon paths becomes large enough that the local bulk
phases drift relative to each other on the Stage-1 timescale τ₁ ~ 1/ω, a
visibility floor appears at order ΔΦ/c² per optical period — currently far
below experimental sensitivity but a clean target for satellite-to-ground
configurations. This locates the Penrose–Diósi mechanism unambiguously at
Stage 2: gravitational collapse acts on bulk relaxation, never on the pair-sync
that builds cos²(θ/2).

**What this section does not yet pin down.**

1. The precise normalization of ⟨V_int⟩_local (single-photon plane-wave vs.
   Compton-volume coherent state).
2. Whether the Stage 1 / Stage 2 timing offset (τ₁ ~ 1/ω vs.
   τ₂ ~ ℏ/E_binding) is empirically distinguishable from a single-event
   detection model.
3. Extension of K_pair = g_int ⟨V_int⟩ to weak and gluon-mediated pair
   interactions, where confinement and short-range structure complicate the
   local-amplitude reading.

### 3.5 Gravitational Coherence of the Bulk

What maintains the coherence of the detector bulk itself? We propose that gravity
provides this role. The gravitational interaction between the ~10²⁶ atoms in a
macroscopic detector provides a collective Kuramoto coupling that maintains a
common phase Φ_bulk across the detector. This is analogous to the well-known
classical synchronization of metronomes on a shared massive platform.

**Two senses of "mass."** A clarification is in order before writing Γ_grav.
The mass m appearing in the Kuramoto identification K = m of Section 2 is the
Dirac mass of an *elementary* fermion, generated by the Higgs–Yukawa coupling
K = y_f v/√2. The mass M entering the gravitational bulk coupling below is the
*total* gravitating mass-energy of a composite body — for ordinary matter, ~99%
of which is QCD binding and gluon-field energy in the nucleons, not Higgs-derived
quark mass. The two are different quantities entering at different scales:
K = m_Higgs governs the L–R synchronization of a single spinor, while
Γ_grav ∝ M_total² governs the pairwise gravitational synchronization across the
~N²/2 constituents of a macroscopic detector. The bridge is the equivalence
principle: all forms of energy gravitate, so QCD binding contributes to Γ_grav
even though it does not contribute to the per-particle Kuramoto coupling K.

The collective rate is obtained by pair-counting the gravitational Kuramoto
coupling. Consider a bulk of total mass M composed of N atoms, each of mass
m_atom = M/N. The gravitational potential energy between any pair (i, j) at
separation r_{ij} is U_pair = G·m_atom²/r_{ij}, which by the framework's
general K = E/ℏ identification yields a pairwise Kuramoto rate

$$K_{aa} \sim \frac{G\, m_{\text{atom}}^2}{\hbar\, r_{ij}}$$

(Distinct from the vertex pair-sync $K_{\text{pair}}^{ab}$ of §3.4: $K_{aa}$ is
the per-pair gravitational rate between two bulk atoms, summed below to give
the bulk's collective coherence rate.)

The bulk contains N(N − 1)/2 ≈ N²/2 such pairs. Approximating all pair
separations by a characteristic internal scale Δz, the aggregate gravitational
synchronization rate is

$$\Gamma_{\text{grav}} \sim \frac{N^2}{2} \cdot \frac{G\, m_{\text{atom}}^2}{\hbar\, \Delta z} = \frac{N^2}{2} \cdot \frac{G\,(M/N)^2}{\hbar\, \Delta z} = \frac{1}{2}\,\frac{G M^2}{\hbar\, \Delta z}$$

Dropping the order-unity factor of ½ to obtain the characteristic rate:

$$\boxed{\Gamma_{\text{grav}} \sim \frac{G M^2}{\hbar\, \Delta z}} \qquad (\text{characteristic, pair-counted})$$

The M² scaling is therefore not a numerological coincidence but a consequence
of pair counting in a many-body sync: each pair contributes ~K_aa, there
are ~N² pairs, and the atomic mass m_atom = M/N enters quadratically per pair,
so the total aggregate rate scales as N² · (M/N)² = M².

For macroscopic objects (M ~ 1 kg, Δz ~ 1 m), Γ_grav ~ 6 × 10²³ rad/s — an
extremely fast rate, which is precisely why bulk coherence is maintained so
effectively for macroscopic masses. The gravitational synchronization coupling
grows as M², ensuring that macroscopic objects are locked into collective phase
coherence far more strongly than microscopic particles.

The relation to Penrose's objective-reduction rate (Section 3.6) is one of
counting: Penrose's E_G = Gm²/Δx is the gravitational self-energy of a
*single* mass configuration in superposition with itself displaced; Γ_grav
here is the aggregate Kuramoto rate over all N²/2 atomic pairs in the
unsuperposed bulk, larger by precisely the pair-counting factor. The two
quantities answer different questions — Penrose asks how fast a superposition
collapses, Γ_grav asks how fast the unsuperposed bulk maintains internal
phase coherence — but both follow from the same K = E/ℏ identification
applied to gravitational pair interactions.

### 3.6 Connection to Penrose-Diósi

This picture has a natural connection to Penrose's proposal [6] that
gravity causes quantum state reduction. Penrose argues that a superposition of
two mass configurations with different spacetime geometries is unstable, with
collapse timescale τ ~ ℏ/E_g where E_g is the gravitational self-energy of the
superposition.

In the Kuramoto framework, this translates to: the gravitational bulk provides
a phase reference, and any quantum superposition that would require the particle
to maintain coherence against the gravitational synchronization pressure will
decohere on a timescale set by the gravitational coupling strength. The Penrose
energy E_g maps onto the Kuramoto coupling rate Γ_grav. Both E_g and Γ_grav are
sourced by total gravitating mass-energy (per the equivalence principle), so the
correspondence is between physically commensurable quantities rather than an
artifact of notation. The two frameworks predict the same qualitative behavior
— heavier objects decohere faster — from different dynamical starting points.

The structural parallel deserves emphasis: both frameworks independently
identify mass as the bridge between quantum and classical regimes, but through
different mechanisms — Penrose through the gravitational self-energy instability
of superposed spacetime geometries, this work through Kuramoto synchronization
driven by the Dirac mass term K = m originating in the Higgs-Yukawa interaction.
In Penrose's picture, a sufficiently massive superposition collapses on its own
because the two branches curve spacetime differently; in the Kuramoto picture,
a particle transitions to classical behavior by re-synchronizing its phase to
the gravitationally coherent detector bulk, driven by the mass asymmetry
M_detector >> m_particle. That two independent starting points — one from
general relativity and quantum gravity, the other from the internal structure
of the Dirac equation — converge on mass as the agent of classicalization is
suggestive that both may be pointing at the same underlying physics, even if
the full unification is not yet available.

### 3.7 Geometric Picture: The Coherence Sub-Manifold

The synchronization, interference, and measurement processes described above
admit a unified geometric reading. Each Kuramoto phase oscillator carries a
phase φ ∈ S¹, so the joint state of N oscillators lives on the N-torus
T^N = (S¹)^N. There are not separate manifolds for separate systems; there is
one product space whose factors index the oscillators.

Within this product space, every lock condition picks out a lower-dimensional
sub-manifold:

- For a single Dirac spinor, the L–R lock φ_L − φ_R = δ_CP defines a
  1-dimensional curve inside T²_spinor.
- For the detector bulk, the alignment condition
  φ_1 = φ_2 = ⋯ = φ_N = Φ_bulk defines a 1-dimensional diagonal circle inside
  T^N_bulk.
- For a measured particle, the coupling condition φ_A = Φ_bulk defines a
  sub-manifold inside the joint particle–detector space
  T²_particle × T^N_bulk.

The post-measurement state lies in the *intersection* of these sub-manifolds.
The dimensional collapse is dramatic: from ~10²⁶ free phase coordinates down to
effectively one global locked phase.

We refer to this intersection as the **coherence sub-manifold**, because it
plays two complementary roles simultaneously:

1. **Dynamical role (attractor).** It is the locus toward which Kuramoto
   trajectories asymptote. Off the coherence sub-manifold, oscillator phases
   drift relative to one another; on it, the lock relations are stationary.
2. **Observational role (interference locus).** It is the locus on which
   coherent phase relations are well-defined. Off the sub-manifold, relative
   phases Δφ wander ergodically over S¹ and any interference term cos(Δφ)
   averages to zero; on it, Δφ is pinned and interference is sharp and
   observable. The Bell correlation cos(2θ) of Section 2 is, geometrically, a
   function evaluated on the locked sub-manifold of the two-particle phase
   space — it is well-defined only there.

This dual role yields a useful re-statement of measurement in geometric terms:
*the measurement event is not the destruction of interference but the re-routing
of the joint trajectory from one coherence sub-manifold to another.* The
particle leaves the entanglement sub-manifold (where it shared coherence with
its partner) and joins the bulk sub-manifold (where it shares coherence with the
detector). What standard accounts call "decoherence" is, in this picture, a
change of which sub-manifold the joint state lives on, not a loss of coherent
structure as such.

### 3.8 Speculative Outlook: Single-World Energy Accounting

We note briefly a speculative consequence. If measurement is resonant
synchronization, then the wavefunction amplitude that does not couple to the
detector (the "residual" associated with the unrealized outcome) has no resonant
absorber available. We conjecture that this residual thermalizes into the
broadband electromagnetic vacuum as low-frequency radiation, conserving energy
within a single world without requiring Everettian branching. This proposal
lacks a first-principles derivation and is offered only as a direction for future
investigation.

### 3.9 What This Section Does Not Claim

The re-synchronization picture is interpretive. It does not:

1. Derive decoherence rates quantitatively from Kuramoto parameters (this would
   require a full quantum treatment of many-body Kuramoto dynamics)
2. Explain *which* outcome occurs in a given individual measurement — only the
   probabilities (addressed in Section 4)
3. Provide a Lorentz-covariant formulation of the measurement process

---

## 4. The Born Rule as Energy Partition under Background-Fluctuation Stochasticity

### 4.1 The Problem and the Reframing

The Born rule — P = |ψ|² — is the bridge between the mathematical formalism and
experimental outcomes. In standard quantum mechanics it is postulated, not
derived. Copenhagen asserts it. Everett's many-worlds claims to derive it from
branch counting, but this remains contested [27, 28]. The measurement problem,
at its core, is the question of why probability equals the squared modulus of
a complex amplitude.

This framework proposes a different reading. If the wavefunction is a *real
physical oscillating field* (Section 2.3), then |ψ|² is not fundamentally a
probability — it is the **energy density** of that field, exactly as for any
classical wave. The probabilistic appearance of measurement outcomes arises
from a separate source: unpredictable interference with the zero-point + thermal
background field at the moment of synchronization with the detector. The Born
rule, in this reading, is the **long-run frequency of energy partition into
the available detector channels under unbiased stochastic background driving**,
not a probability axiom of quantum theory.

The closest precedent for this view is Nelson's stochastic mechanics [26],
which derives the Schrödinger equation from a real diffusion process in a
background stochastic field. Our framework supplies a physical identity for
that field — the zero-point + thermal residual of the chiral phase clocks
already present in the Kuramoto/Dirac picture (Sections 9 and 11 of the
equations reference) — and reads the Born rule as the resulting energy-partition
statistics, rather than as an independent postulate.

### 4.2 |ψ|² as Wave Energy Density

For any real oscillating field, the time-averaged energy density is proportional
to the squared amplitude. A complex wavefunction ψ = α|0⟩ + β|1⟩ describes a
superposed oscillator with amplitude α in channel |0⟩ and amplitude β in
channel |1⟩. In the wave-realist reading, the energy carried by each channel
is

$$E_0 \propto |\alpha|^2, \qquad E_1 \propto |\beta|^2 \qquad (5)$$

with total wave energy E_total = E_0 + E_1 = |α|² + |β|² = 1 in normalized
units. This is classical wave physics — no Born postulate is required to write
down |α|² and |β|² as the quantities of interest. They are the energy fractions
of the field in each channel.

### 4.3 Synchronization Deposits the Energy into One Channel

The detector channels available for synchronization are those eigenstates of
the detector whose internal phase clocks can match the particle's. The Kuramoto
re-synchronization event (Section 3) transfers wave energy from the particle
to the detector, exciting one channel to its registered ("clicked") state.

A discrete click — rather than a fractional excitation of multiple channels —
arises because each detector channel is itself a quantized resonator with a
discrete excitation threshold (the same threshold that defines the channel as
a single detector eigenstate). The synchronization event delivers either the
full quantum into one channel or none, determined by which channel "wins" the
competition for the available wave energy.

### 4.4 Stochasticity Comes from the Background Field

Why does any particular channel win in any particular event? And why do
long-run frequencies match |α|² rather than some other partition?

The answer rests on the zero-point + thermal background field always present
at the detector (Section 9 of the equations reference). At the instant of
contact, the relative phase between the particle's clock and the detector
bulk's clock is perturbed by unpredictable transient fluctuations of this
background. These fluctuations bias the synchronization event toward one
channel or another in any individual instance — but, being statistically
symmetric across the relevant phase space (zero-point fluctuations are
symmetric by construction; unbiased thermal noise is symmetric by the second
law), they do not favor any channel systematically.

Two consequences follow:

1. **Each individual outcome is not fundamentally random.** It is determined
   by the specific instantaneous configuration of background fluctuations at
   the moment of synchronization. We cannot, as observers, track this
   configuration; the outcome therefore *appears* random.
2. **Long-run frequencies converge to the energy fractions.** Over many events,
   the unbiased background averages out, and the frequency with which each
   channel is chosen converges to the energy fraction the original wave
   carried in that channel:

$$P(|0\rangle) = |\alpha|^2, \qquad P(|1\rangle) = |\beta|^2 \qquad (6)$$

read here as long-run **frequencies of energy partition** rather than as an
independent probability axiom.

The Born rule, on this reading, is the visible projection of a deterministic
energy redistribution in which the only stochastic input is the unobserved
background field. It is not a separate postulate of quantum mechanics; it is
the law of energy partition under unbiased background driving, observed as
frequency statistics because the background is unobserved.

### 4.5 Connection to Nelson's Stochastic Mechanics

Nelson [26] showed that a real particle undergoing stochastic motion in a
background field with diffusion coefficient ν = ℏ/(2m) satisfies the
Schrödinger equation. The framework presented here makes that background field
physically explicit (the zero-point + thermal residual of the chiral phase
clocks, equations reference Sections 9 and 11) and reads the Born rule as a
frequentist statement about energy partition under that background's
stochastic driving. Where Nelson postulates the diffusion coefficient, this
framework identifies its physical origin in the zero-point phase noise
σ_φ(0) = 1/√2 rad — itself a consequence of the Kuramoto coupling K = m and
the chiral clock structure.

This is structurally a hidden-variable theory, in which the hidden variable is
the instantaneous configuration of the background field at the detector. As
such, it must satisfy Bell's theorem — and it does, because the framework
does not use this story to explain Bell correlations. The correlations
themselves come from the full Dirac spinor structure (standard QM, Section 2
and Appendix A); only the *measurement statistics* of definite outcomes are
accounted for via the energy-partition reading. The two stories are
complementary, not competing.

### 4.6 The Heisenberg Uncertainty Principle as the Fourier Bandwidth Theorem

In MCI's wave-realist reading (Section 4.2), the wavefunction ψ(x) is a real
oscillating field. Position and momentum representations are related by Fourier
transform via the de Broglie relation p = ℏk:

$$\varphi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int \psi(x)\, e^{-ipx/\hbar}\, dx$$

The **Fourier bandwidth theorem** of harmonic analysis — a rigorous mathematical
result independent of any quantum interpretation — states that for any function
f ∈ L²(ℝ) with Fourier transform f̂(k), the standard deviations of |f|² and
|f̂|² (treated as probability densities on x and k respectively) satisfy

$$\sigma_x \cdot \sigma_k \geq \frac{1}{2} \qquad (7)$$

with equality saturated by Gaussian wavepackets. Multiplying both sides by ℏ:

$$\boxed{\sigma_x \cdot \sigma_p \geq \frac{\hbar}{2}} \qquad (8)$$

This is the Heisenberg uncertainty relation, **factor of ½ exact**.

The framework's contribution here is interpretive, not derivational. Standard
QM postulates ΔxΔp ≥ ℏ/2 as a separate axiom (or derives it from the operator
commutator [x̂, p̂] = iℏ, which is itself a postulate, via the
Robertson–Schrödinger inequality). MCI reads it as the Fourier bandwidth
theorem applied to a real wavefunction — a theorem about waves, not an axiom
about quantum systems. **In the wave-realist reading, the uncertainty principle
is not a quantum mystery; it is harmonic analysis applied to a real physical
field.**

#### The Compton scale is distinct from the universal floor

The Compton wavelength λ_C = h/(mc) is a separate, particle-specific scale
worth distinguishing from the universal ½ of the Fourier theorem. A Dirac
particle's internal chiral clocks oscillate at the Compton frequency
ω_C = mc²/ℏ; this sets the characteristic spatial bandwidth over which the
particle's *internal* clock structure becomes resolvable, and it is the typical
scale of Zitterbewegung (Appendix B / Section 7.7).

The Compton scale is **not** the source of the ½ in the uncertainty relation —
that ½ is universal, particle-independent, and follows from the Fourier theorem
alone. The two facts are complementary:

- **Universal floor (Fourier bandwidth, Eq. 8):** σ_x·σ_p ≥ ℏ/2 for any real wavefunction, every particle, every state.
- **Particle-specific scale (Compton wavelength):** λ_C = h/(mc) is the length below which a single Dirac particle stops behaving as a localized point and begins to display its internal two-clock structure (Zitterbewegung, chiral mixing, pair production at higher energies).

Earlier formulations conflated these — treating the Compton wavelength as the
*source* of the Heisenberg ½. The corrected separation: the bound comes from
harmonic analysis applied to the wavefunction (universal); the Compton scale
is a particle-specific length at which the framework's two-clock structure
(Section 2) becomes manifest.

#### Connection to the zero-point phase floor

The zero-point phase noise σ_φ(0) = 1/√2 rad (equations reference Section 9)
is the same Fourier bandwidth theorem applied to the chiral phase clocks
themselves: the minimum joint uncertainty in conjugate phase variables is
itself ½ in natural units. The zero-point phase floor and the Heisenberg
uncertainty relation are therefore the same theorem expressed in different
variables — both follow from harmonic analysis of the wavefunction, both have
factor ½, and both are unavoidable for any real oscillating field. The
zero-point energy ½ℏω per mode is the energy cost of saturating this minimum
phase uncertainty.

### 4.7 What This Reframing Requires

The energy-partition reading rests on three physical assumptions, all already
present in the framework:

1. The wavefunction is a real oscillating field carrying energy; |ψ|² is its
   energy density (Section 2.3).
2. Measurement is Kuramoto re-synchronization to a macroscopic detector that
   transfers this energy into one channel (Section 3).
3. The background field fluctuations (zero-point + thermal) that determine
   which channel wins in any individual event are statistically unbiased on
   the channel-selection phase space.

Assumption 3 is the most important and the least directly testable. It is
motivated by the symmetry of the zero-point field — there is no preferred
direction for vacuum fluctuations — and by the second law as applied to
unbiased thermal noise. But the rigorous claim that *long-run frequencies*
converge exactly to *energy fractions* requires showing that the background
statistical symmetry holds across the channel-selection phase space, which
is not yet derived from first principles.

The framework therefore offers a *reframing*, not a complete derivation: it
replaces the standard Born axiom with a wave-realism + unbiased-background
postulate set, which is weaker but not vacuous. Whether the bias-free
assumption can be derived from underlying dynamics — for example, from the
isotropy of the chiral phase clocks under U(1) phase redefinition — is a
direction for future work (Section 8.3).

---

## 5. Extension to Photons via the Riemann–Silberstein Form

Photons are not Dirac particles. They are spin-1 vector bosons described by
Maxwell's equations, with no rest mass to couple chiral sectors. The framework's
central identification K = m therefore does not apply directly: there is no
mass term to set a Kuramoto coupling between photon helicities. We address this
by separating two questions that earlier formulations conflated: (i) where do
photon Bell correlations come from? and (ii) where does the framework's
measurement mechanism enter for photons?

### 5.1 The Riemann–Silberstein Form of Maxwell

Maxwell's free equations can be written in a Weyl-like first-order form using
the Riemann–Silberstein vector [40]:

$$\mathbf{F} = \mathbf{E} + i\,\mathbf{B}, \qquad i\,\partial_t \mathbf{F} = c\,\nabla \times \mathbf{F}, \qquad \nabla \cdot \mathbf{F} = 0$$

The two helicity eigenstates F_+ and F_− (right- and left-circular polarizations)
are independent — there is no mass term, and the structure mirrors the m = 0
chiral limit of the Dirac equation: two decoupled clocks, θ_rel = π/2 permanently.
A Kuramoto coupling between F_+ and F_− of a single photon is identically zero
in vacuum.

### 5.2 Where Photon Bell Correlations Come From

The polarization Hilbert space of a photon is two-dimensional, spanned by any
orthogonal pair (H/V, ±, L/R). It is mathematically isomorphic to the spin-½
Hilbert space, with the Poincaré sphere playing the role of the Bloch sphere.
For two polarization-entangled photons in the singlet state, the standard
quantum correlation is

$$E_\gamma(a, b) = -\cos\bigl(2(a-b)\bigr)$$

and the CHSH bound saturates at 2√2. The factor of 2 in the angular dependence
reflects the π-periodicity of polarizers (vs. 2π-periodicity of Stern–Gerlach
analyzers).

This correlation is a property of the polarization Hilbert space, not of any
chiral coupling. It is delivered by standard QED — the same way standard QM
with the Dirac spinor delivers the −cos(a−b) correlation for spin-½ pairs
(Section 2). In both cases, the framework does not derive the Bell
correlations; the underlying Hilbert-space structure does. The framework's
contribution lies elsewhere.

### 5.3 The Measurement Mechanism Transfers to Photons

The framework's central interpretive claim — measurement is Kuramoto
re-synchronization to the detector bulk (Section 3) — does not depend on the
K = m identification for its physical content. It requires only that the system
being measured carries a phase clock that can be synchronized to the detector.
Photons satisfy this: each polarization mode carries a definite phase, and at
detection the photon's polarization clock locks to the polarizer's selected
channel (transmitted vs. rejected).

The Kuramoto coupling for the photon-detector interaction is not zero — it is
set by the photon's interaction with the detector matter (typically dipole
coupling −d·E), not by any vacuum mass term. For a photon of energy E = ℏω
coupling to a near-resonant detector channel, the natural Kuramoto rate scales
with the photon's own oscillation frequency:

$$K_\gamma \sim \omega = \frac{E}{\hbar}, \qquad \tau_{\text{sync}} \sim \frac{1}{K_\gamma} = \frac{\hbar}{E} \qquad (11)$$

A 2 eV optical photon synchronizes to its detector in ~0.3 fs; a 10 keV X-ray
locks in ~10⁻¹⁹ s. Higher-energy photons synchronize faster — the Kuramoto
rate is set by the photon's energy via its interaction with the detector,
rather than by any rest mass.

This is the photon analog of K = m for fermions: in both cases, the
synchronization rate to the detector is set by the energy scale that
characterizes the system's coupling to its environment. For massive fermions
at rest that scale is mc² (the Compton frequency); for photons it is ℏω
(the photon's own frequency).

### 5.4 Gravitational Decoherence and the Linewidth-Dependent Bell Test

Two photon time scales must be kept distinct:

- **τ_sync = ℏ/E** — the time for Kuramoto re-sync to the detector to complete (set by photon energy)
- **τ_coh = 1/Δν** — the photon's coherence time during measurement (set by *linewidth*, independent of central energy)

For a given measurement event, the photon is in coherent superposition during
the τ_coh window. If the two detectors A and B in a Bell test are at different
gravitational potentials, their bulk phases Φ_bulk(A) and Φ_bulk(B) accumulate
a relative offset proportional to ω·ΔΦ_grav/c² · τ_coh. When this offset
exceeds ~1 rad, the singlet correlation degrades.

This is the linewidth-dependent gravitational Bell prediction (`predictions.py`
P6b), now phrased in self-consistent form:

$$\delta\phi_{\text{grav}} = \omega \cdot \frac{\Delta\Phi_{\text{grav}}}{c^2} \cdot \tau_{\text{coh}} = \frac{\omega \cdot \Delta\Phi_{\text{grav}}}{c^2 \cdot \Delta\nu} \qquad (12)$$

$$\text{CHSH}(\Delta\nu) = 2\sqrt{2} \cdot \exp\!\left(-\frac{\delta\phi_{\text{grav}}^2}{2}\right) \qquad (13)$$

Standard QM/QED predicts CHSH is independent of photon linewidth at fixed
entanglement fidelity. The framework predicts it decreases with narrowing
linewidth in the presence of a gravitational potential difference between the
detectors. Tests are in reach using cavity-filtered narrow-linewidth photons
at altitude differences of a few km (terrestrial) or with Earth–satellite
baselines.

The discriminating measurement is the joint linewidth × altitude scan with
narrow-linewidth photons; photon energy is one knob among three (along with
linewidth Δν and altitude split ΔΦ_grav), not a discriminator on its own.

### 5.5 Photons and Penrose Objective Reduction

The gravitational synchronization rate Γ_grav = GM²/(ℏΔz) (Section 3.5)
vanishes identically for a massless particle. Equivalently, the Penrose
objective-reduction timescale τ_OR = πℏ/E_G with E_G = Gm²/Δx becomes
infinite for m = 0. **The gravitational classicalization channel that drives
massive systems toward definite outcomes is silent for photons.**

This matches Penrose's own position. The OR proposal is designed for
superpositions of macroscopically distinct *mass* configurations (mirrors,
mesoscopic test masses); Penrose has been explicit that single photons fall
outside its remit because they have no rest mass to source the gravitational
self-energy.

In the framework's reading, a photon therefore has only two pathways into the
classical domain:

1. **Measurement (active).** Kuramoto re-synchronization to a quantized
   detector channel (§5.3). A single photon hitting a photodetector produces
   a definite click; this is the only mechanism by which an isolated photon
   classicalizes.
2. **Coherent-state averaging (many-photon).** A macroscopically populated
   mode (laser light, classical EM) has a positive Wigner function and obeys
   Maxwell's equations classically. The classical limit emerges through
   statistical superposition of many photon modes, not through any internal
   collapse mechanism.

A single photon in vacuum, between emission and detection, is **perpetually
quantum** — it does not gravitationally classicalize, and it has no way to
do so internally. This is consistent with the experimental fact that
single-photon Bell tests preserve full coherence over kilometer-scale
separations and Earth–satellite baselines (Micius, 2017), where any internal
classicalization mechanism would have produced observable degradation.

One subtlety: photons do follow null geodesics in curved spacetime
(gravitational lensing, Shapiro delay). This is unitary classical evolution
of the photon's trajectory, not collapse or decoherence of its quantum state
— it bends paths without classicalizing states.

The silence of the gravitational channel for photons is consistent with the
linewidth-dependent prediction in §5.4, which attributes the gravitational
effect not to the photon in flight but to the bulk-phase mismatch between
detectors A and B at different gravitational potentials. The photon is the
messenger; the gravitational decoherence is in the detectors.

### 5.6 What Remains Open

Two questions are not resolved by this section:

1. **A first-principles derivation of K_γ from QED.** We have asserted
   K_γ ~ ω as the natural scaling, motivated by photon-detector dipole
   coupling. A rigorous derivation would relate K_γ to the absorption matrix
   element ⟨e|d|g⟩ for the specific detector channel and compute the actual
   sync time for realistic photodetectors (photomultipliers, avalanche
   photodiodes, superconducting nanowire detectors).
2. **The microscopic mechanism for the discrete click.** Section 4 attributes
   discrete clicks to the threshold structure of detector channels. For
   photons, this corresponds to the photoelectric or photon-counting
   threshold of the detection element. The framework provides a mechanism
   (re-sync to a quantized channel) but does not yet derive the threshold
   from first principles.

These are tractable extensions, not framework contradictions. The §5
photon-coupling problem — flagged in earlier drafts as the framework's most
serious open question — reduces to a pair of well-defined technical issues
once the Bell correlations are correctly attributed to the polarization
Hilbert space rather than to any Kuramoto coupling between photon helicities.

---

## 6. Qualitative Predictions and Consistency Checks

We distinguish between predictions that follow from the mathematical identification
(Section 2) and those that follow from the interpretive claims (Sections 3-4).

### 6.1 From the Mathematical Identification

**P1 — Block decomposition of Bell correlations.** For massive entangled
particles, the standard correlation E(a,b) = −cos(a−b) can be partitioned
into block contributions E_LL + E_SS + E_LS by restricting the spin
operator to the upper, lower, and cross sectors of the Dirac spinor. The
sum is additive by trace linearity (Appendix A); what depends on
θ_rel = arcsin(v/c) is the *redistribution of weight* among the three
blocks. A hypothetical experiment separately sensitive to the
small-component contribution — for example, ultra-relativistic decay
asymmetries — could in principle expose this redistribution. The
decomposition itself is a consistency check on the chiral-clock reading
of the spinor structure, not an independent prediction.

**P2 — Zitterbewegung as clock beat.** The identification of ω_Zitter = 2mc²/ℏ
as the beat frequency between temporal and spatial clocks is consistent with all
known properties of Zitterbewegung (Appendix B). Trapped-ion simulations with
tunable effective mass [10] could probe the transition from locked to unlocked
clock behavior as effective mass passes through zero.

**P3a — Spin-statistics is reproduced, not derived.** The framework's commitment
to a chiral clock pair (ψ_L, ψ_R) coupled by K = m is identical, as a
representation-theoretic object, to the (½, 0) ⊕ (0, ½) Lorentz representation
that carries spin-1/2. Under spatial rotation by 2π, each Weyl half picks up
−1; by the Feynman-Finkelstein continuous-deformation argument, exchange of
two such particles in 3+1D inherits the same sign, giving fermion
antisymmetry. We verify this numerically across a wide range of v/c — the
relativistic large/small mixing of Appendix A does not erode the sign — and
show that the pure Kuramoto phase dynamics (Eqs. 2a, 2b), treated as a
classical ODE on real-valued phases, are exchange-symmetric and carry no
sign. The fermion sign therefore lives in the spinor frames χ_{L,R} of the
Madelung decomposition, not in the Kuramoto coupling itself. This is a
consistency check, not a new derivation; details and numerical results are
in Appendix D.

### 6.2 From the Interpretive Framework

**P3 — Decoherence rate scaling with mass.** If the Kuramoto synchronization rate
is K = m, heavier particles should decohere faster: τ_sync ~ ℏ/m. This is
qualitatively consistent with the observation that macroscopic objects exhibit
essentially instantaneous decoherence while electrons maintain quantum coherence
over longer timescales. A precision measurement of decoherence rate as a function
of particle mass (electrons, muons, pions, kaons) could test whether
τ_decoherence ∝ 1/m.

**P4 — Higgs coupling and synchronization rate.** If K = y_f · ⟨φ⟩ = m, then
decoherence rates for entangled fermion pairs should scale linearly with mass.
Comparing entanglement decay times for kaon pairs (m_K = 494 MeV) versus B-meson
pairs (m_B = 5,280 MeV) should show τ_B/τ_K ~ m_K/m_B ≈ 0.094. Existing
collider data on neutral kaon and B-meson decoherence could be analyzed.

**P5 — Gravitationally-weighted secondary-radiation rate.** The Stage 2 bulk
relaxation (§3.4) emits secondary radiation (virtual photon, real photon, or
$e^+ e^-$ pair, depending on the energy mismatch) at a rate set by Γ_bulk. Because
Γ_bulk depends on the local mass-energy distribution and is therefore subject
to gravitational redshift, the secondary-emission rate during a detection event
scales as 1 + Φ_grav/c² at leading order. Two detectors at different
gravitational potentials should register a fractional rate difference of order
ΔΦ/c² — roughly 10⁻¹³ for a 1000 km altitude split. This is below current
sensitivity but a clean signature unique to the two-stage framework: neither
standard decoherence theory nor Penrose–Diósi predicts gravity-dependent timing
of detection-induced secondary emission.

### 6.3 Honest Assessment

These predictions are qualitative scaling arguments, not quantitative predictions
with computed coefficients. The framework in its current form is an interpretation
— it provides a physical mechanism consistent with known decoherence behavior but
does not yet make predictions distinguishable from standard decoherence theory.
This is the main limitation and the main avenue for future work.

**Hardware demonstration of the bulk-sync prediction.** A digital-quantum
implementation of the bulk-sync circuits (`bulk_sync_hardware.py`, run on
`ibm_marrakesh` with readout-error mitigation, XpXm dynamical decoupling, and
zero-noise extrapolation; N ∈ {2, 4, 8}, K = 0.06 rad, 4096 shots/circuit)
reproduces the GHZ Heisenberg-scaling prediction cleanly: the log-log slope of
φ_sys vs N comes out near 1, with measured ⟨X_sys⟩ within ≈ 5% of theory at all
three N values. The product-bulk slope is not cleanly resolved at this coupling
— the predicted phase shifts at small N (φ_pred ≈ 0.085 rad at N = 2) lie below
the per-shot noise floor of the hardware, and ZNE over-corrects at N = 8
(⟨X_sys⟩ = 1.04 ± 0.04, statistically consistent with theory but unphysical and
thus unusable in an arccos-based fit). The data are consistent with the
predicted asymmetry (φ_GHZ > φ_product at every usable N) and with GHZ
Heisenberg scaling specifically. As stated in §1.4, this is a consistency check
against standard quantum metrology, not a test of MCI's distinctive content;
both standard QM and MCI predict identical scaling. The framework-distinctive
predictions remain §5.4 (linewidth-dependent gravitational Bell), §6.2 P4
(kaon vs B-meson decoherence), and `sg_angular.py`.

---

## 7. Comparison with Existing Frameworks

### 7.1 Interpretations of Quantum Mechanics

| Property | Copenhagen | Everett MWI | Bohmian | GRW/CSL [8, 23] | Superdeterminism | **MCI (this work)** |
|---|---|---|---|---|---|---|
| ψ is real? | No | Yes | Yes | Yes | Varies | **Yes** ᵃ |
| Collapse? | Postulated | No | No | Stochastic | Not needed | **Re-synchronization** ᵃ |
| Branching? | No | Yes (∞) | No | No | No | **No** ᵃ |
| Residual energy? | Discarded | In branches | Pilot wave | Noise | Not addressed | **Thermal vacuum** ᵇ |
| Single world? | By fiat | No | Yes | Yes | Yes | **Yes (by physics)** ᵇ |
| Mechanism? | None | None | Pilot wave | Random hits | Initial conditions | **Kuramoto sync** ᵃ |
| Bell's theorem? | Accepted | Accepted | Accepted (nonlocal) | Accepted | Denied (meas. indep.) | **Accepted** ᵃ |
| Born rule | Postulated | Derived (contested) | Derived | Modified | Derived (contested) | **Reframed as energy partition (Section 4)** ᵇ |
| Uncertainty principle | Postulated | Inherited | Derived (nonlocal) | Inherited | Inherited | **Emergent (Section 4.6)** ᵇ |
| Observer needed? | Yes | Yes (branch) | No | No | No | **No** ᵃ |
| Preferred frame? | No | No | Yes (pilot wave) | No | No | **No (relational, §1.5)** ᵃ |

*ᵃ Established within the framework: follows directly from the mathematical
identification K = m and the re-synchronization interpretation of measurement
(Sections 2–3).*

*ᵇ Conjectural extension: physically motivated by the framework but relies on
heuristic arguments that have not yet been rigorously derived from first
principles (Sections 3.6, 4, 4.5). These entries represent directions for
future development rather than settled results.*

### 7.2 Ontological Status and the PBR Theorem

The framework takes ψ to be a real physical field — an ontic interpretation in the
terminology of Harrigan and Spekkens [29]. The internal phase clocks are physical
oscillators, not epistemic bookkeeping devices. This places the framework squarely
within ψ-ontic territory, consistent with the PBR theorem [30], which rules out a
broad class of ψ-epistemic models under mild assumptions.

However, the ontology is more specific than generic wavefunction realism [31].
The wave function is not a field on 3N-dimensional configuration space — it is
the collective description of N particles, each carrying its own pair of chiral
phase clocks in ordinary three-dimensional space. The Kuramoto coupling is local
in the sense that each particle's internal L-R synchronization involves only its
own mass term. Entanglement arises because particles prepared in a common
interaction share initial phase correlations — correlations that are then revealed
(not created) by measurement.

This sidesteps the configuration-space problem that troubles many realist
interpretations [31, 32]: the fundamental ontology is particles with internal
clocks in three-dimensional space, not a wave in 3N dimensions. The cost is that
entanglement correlations must be accepted as initial conditions rather than
explained by the dynamics — but this is also true of standard quantum mechanics.

### 7.3 Relation to QBism and Relational QM

QBism [33] treats quantum states as expressions of an agent's beliefs, not
objective features of reality. The Kuramoto framework is diametrically opposed:
ψ is a physical field, and probabilities arise from physical synchronization
dynamics, not from subjective belief updating. Where QBism dissolves the
measurement problem by denying that there is a physical process to explain, the
Kuramoto framework insists on providing one.

Relational quantum mechanics [24] holds that quantum states are relative to
observers. The Kuramoto framework has a superficial similarity — the particle's
phase is defined relative to a reference (the entangled partner or the detector
bulk). But the similarity is only superficial: in relational QM, there is no
observer-independent state of affairs; in the Kuramoto framework, the phase
synchronization dynamics are objective and observer-independent.

### 7.4 Decoherence Models

The closest existing framework is the Penrose-Diósi gravitational decoherence
model [6, 7]. Both that model and ours identify gravity as
the agent of classicalization. The key differences:

- Penrose-Diósi: collapse timescale τ ~ ℏ/E_g (gravitational self-energy)
- This work: decoherence timescale set by Kuramoto re-synchronization rate to
  the gravitational bulk

The predictions are qualitatively similar (heavier → faster decoherence) but
derive from different dynamics. A quantitative comparison awaits a full
derivation of Kuramoto decoherence rates from first principles.

### 7.5 Zurek's Einselection

Zurek's quantum Darwinism [4, 5] identifies "pointer states" as
states that survive interaction with the environment. In the Kuramoto picture,
pointer states are the synchronized states — the phase-locked configurations
that are stable under coupling to the macroscopic bulk. States that cannot
synchronize (superpositions of macroscopically distinct mass configurations)
are dynamically unstable and decohere. This is consistent with einselection
but provides a specific dynamical mechanism (phase locking) for why certain
states survive.

### 7.6 Superdeterminism

Superdeterminism [20, 19] escapes Bell's theorem by denying
measurement independence: the hidden variable λ and the detector settings (a, b)
are correlated because they share a common causal past. If ρ(λ|a,b) ≠ ρ(λ),
Bell's derivation does not go through, and local hidden variable models can
reproduce quantum correlations.

This comparison is important because the measurement-independence loophole through
the gravitational bulk phase Φ_bulk — arguing that since both detectors and the
particle source share a common gravitational field, their states are
correlated — might seem to apply here. We explicitly reject this route in the
present paper.

**Why this framework is not superdeterministic:**

1. **We do not challenge Bell's theorem.** The quantum correlations
   E(a,b) = −cos(a−b) are accepted as arising from the entangled singlet state
   and the full Dirac spinor structure — standard quantum mechanics. No hidden
   variable model is proposed to replace them.

2. **Measurement independence is preserved.** The experimenter's choice of
   detector angle is not constrained by the framework. The gravitational bulk
   phase Φ_bulk maintains detector coherence (Section 3.5) but does not
   determine or correlate with measurement settings.

3. **The role of gravity is different.** In superdeterminism, correlations
   between λ and (a,b) must be fine-tuned to reproduce quantum predictions
   exactly — a conspiracy that many physicists find unacceptable ['t Hooft's
   cellular automaton requires the initial state of the universe to encode all
   future measurement choices]. In this framework, gravity provides the
   synchronization bath for the *measurement process* (decoherence), not for the
   *correlations* (which are quantum mechanical).

4. **No retrocausality or conspiracy.** Superdeterministic models require that
   the state of the universe at the Big Bang already encodes which detector
   settings will be chosen in a 2015 Bell test [14]. This framework requires only
   that macroscopic detectors are phase-coherent objects immersed in a
   gravitational field — a physically uncontroversial claim.

The distinction can be stated concisely: superdeterminism says the correlations
are classical but hidden in the initial conditions. This framework says the
correlations are quantum, and the Kuramoto mechanism explains how they are
*revealed* (measurement) and *degraded* (decoherence), not how they are
*produced*.

### 7.7 The Hestenes Zitterbewegung Interpretation

The closest precursor to the present framework in the interpretive literature
is the Zitterbewegung (ZBW) interpretation of Hestenes [35]. Reformulating
Dirac theory in spacetime algebra (STA), Hestenes argues that the complex
phase factor in the Dirac wave function represents a physical rotation — the
internal circular motion of the electron at the Compton frequency
ω_C = mc²/ℏ. In this picture the spin is the angular momentum of this
circulation, and Zitterbewegung is fundamental rather than incidental.

The parallels with the present work are direct:

| Feature | Hestenes ZBW interpretation | This work |
|---|---|---|
| Phase factor e^{iφ} | Physical clock rotation (STA rotor) | Physical phase clock oscillator |
| Zitterbewegung | Fundamental circulatory motion | Beat frequency between temporal and spatial clocks |
| Spin | Angular momentum of ZBW circulation | Geometric consequence of clock orthogonality (θ_rel = 90°) |
| Mass | Sets ZBW frequency ω_C = mc²/ℏ | Sets Kuramoto coupling constant K = m |
| Uncertainty principle | Derived from clock geometry | Derived from clock bandwidth (Section 4.6) |

Both frameworks begin from the same core observation: the complex phase factor
in the Dirac wave function is not a mathematical convenience but a physical
oscillator. Both derive spin and the uncertainty principle from the geometry
of this oscillator rather than postulating them.

The key difference is dynamical. Hestenes identifies the internal clock but
does not supply a coupling framework for the two chiral sectors. The present
work provides this missing element: the Kuramoto identification K = m explains
why the clock oscillates at the Compton frequency (it is the synchronization
rate between ψ_L and ψ_R), and extends the picture to a dynamical mechanism
for measurement (re-synchronization to the detector bulk) and mass generation
(Higgs as the agent that sets K). In retrospect, the Hestenes ZBW
interpretation and the Dirac-Kuramoto framework are describing the same
internal clock from different mathematical directions — STA geometry and
Kuramoto synchronization dynamics, respectively.

---

## 8. Discussion

### 8.1 The Interpretive Status

This paper presents a mathematical identification (Dirac = Kuramoto on the
synchronized manifold) and a named interpretive framework built on it: the
**Many Clocks Interpretation of Quantum Mechanics (MCI)**, introduced in §1.5.
The mathematical identification is verifiable and, we believe, novel. The
interpretive framework is physically motivated but not yet quantitatively
predictive beyond standard decoherence.

MCI sits in the category of interpretation papers — alongside Many-Worlds [16],
Bohmian mechanics [15], and Rovelli's relational quantum mechanics [24]. Its
distinguishing features are: (i) ψ is ontic (a real oscillating field), as in
Bohmian and Everettian readings; (ii) measurement is local Kuramoto
re-synchronization between clock-carrying systems, with no observer or
branching required; (iii) the framework is relational — no global preferred
frame — distinguishing it from Bohmian mechanics, which requires a preferred
foliation; (iv) past phase history is overwritten at each sync event, giving
a positive dynamical mechanism for thermalization rather than treating it as
an emergent statistical phenomenon. The contribution is not new equations
but a new way of reading existing equations that provides physical intuition
for the measurement process. As Maudlin [32] has emphasized, interpretations
are not idle philosophy — they guide which questions physicists ask and which
experiments they design.

### 8.2 The Historical Note

The timeline is suggestive:

- 1928: Dirac equation (the two-clock structure)
- 1935: EPR paper [25] ("spooky action at a distance")
- 1964: Bell's theorem
- 1975: Kuramoto model

The relativistic spinor structure that produces the full quantum correlation
existed 36 years before Bell showed it was needed. The synchronization framework
that describes the coupling existed 11 years after Bell. The identification
presented here connects these threads.

### 8.3 Future Directions

Three directions could elevate this from interpretation to testable theory:

1. **Quantitative decoherence rates.** Derive decoherence timescales from
   Kuramoto parameters in a many-body quantum setting. If these reproduce known
   rates for specific systems (e.g., superconducting qubits, trapped ions), the
   framework gains predictive power. If they differ, the framework makes testable
   predictions.

2. **Born rule — closing the unbiased-background assumption.** Section 4
   reads the Born rule as the long-run frequency of energy partition under
   unbiased background-field driving. The wave-realism premise (|ψ|² is wave
   energy density) and the partition mechanism (Kuramoto re-synchronization
   into a quantized detector channel) are physically motivated and testable
   in principle. The remaining gap is the rigorous proof that the
   zero-point + thermal background is statistically unbiased on the
   channel-selection phase space — and that consequently long-run
   frequencies converge *exactly* to energy fractions. A possible route is
   to derive this from the U(1) symmetry of the chiral phase clocks under
   global phase redefinition; another is a many-body quantum-Kuramoto
   simulation that measures channel-frequency convergence directly.

3. **Photon coupling — first-principles K_γ from QED.** Section 5 proposes
   that the photon-detector Kuramoto rate scales as K_γ ~ ω = E/ℏ, motivated
   by the dipole interaction. A rigorous derivation would relate K_γ to the
   absorption matrix element ⟨e|d|g⟩ for a specific detector channel and
   compute realistic sync times for photomultipliers, avalanche photodiodes,
   and superconducting nanowire detectors. Combined with the linewidth-
   dependent gravitational Bell prediction (Section 5.4), this would give the
   framework its sharpest near-term experimental test.

### 8.4 Categorization of Supporting Numerical Code

The framework is supported by a set of Python programs that play different
roles. We categorize them here so readers can see which carry evidential
weight, which are illustrative or pedagogical, and which exist to disarm
known conflations:

| Program | Category | What it does | What is at stake |
|---|---|---|---|
| `spin_statistics.py` | **Evidential** | Six tests; fermion antisymmetry sign across 6 decades of v/c | Could have falsified the chiral-pair commitment (Appendix D); did not |
| `gravitational_bell.py` | **Quantitative prediction** | Implements §5.4 CHSH(Δν) = 2√2·exp(−δφ²/2) | Operationalizes the framework's sharpest distinguishable prediction |
| `predictions.py` | **Quantitative prediction** | Catalog of P1–P6 testable predictions, with retractions explicitly marked | Maps experimental contact points; documents falsified entries (P1, P3) |
| `bell_energy_test.py` | **Quantitative prediction** | Qiskit CHSH simulation testing K(E) scalings vs photon energy | Discriminates K∝1/E from K∝ω from null QM |
| `sg_angular.py` | **Quantitative prediction** | Stern-Gerlach angular dependence on local gravity (~4% effect) | Tests gravitational Kuramoto coupling beyond Bell tests |
| `bulk_sync_asymmetry.py` | **Quantitative prediction** | Single-particle vs bulk phase-rotation scaling (√N vs N) | Tests the measurement asymmetry of §3 |
| `bulk_sync_hardware.py` | **Consistency check (hardware)** | IBM Quantum execution of the bulk-sync circuits with readout mitigation, DD, and ZNE | Demonstrates digital-hardware reproduction of the simulation (GHZ slope ≈ 1 confirmed; product slope below noise floor at K=0.06); not framework-distinctive |
| `dirac_extension.py` | **Illustrative** | Three-term Bell decomposition E_LL + E_SS + E_LS | Visualizes the weight redistribution of Appendix A; the sum itself is an identity |
| `gravity_twistor.py` | **Illustrative** | Poisson ↔ Kuramoto field-equation correspondence; twistor connection | Visualizes §3.5 and EQUATIONS.md §8 |
| `bell_phase.py` | **Clarifying** | Establishes Malus-law toy is sub-classical (CHSH ≤ √2), distinct from Dirac large block | Disarms the §A.5 conflation |
| `local_causality.py` | **Clarifying** | Identifies where Bell's factorization actually breaks in MCI | Disarms the superdeterminism misreading (§7.6) |
| `kuramoto_sync.py` | **Pedagogical** | Two-oscillator synchronization dynamics under K > 0 | Shows what K = m sync looks like in time |
| `higgs_clock.py` | **Pedagogical** | K = m identification and antiparticle reverse-clock dynamics | Illustrates EQUATIONS.md §6 |
| `resynchronization_calc.py` | **Negative result** | Tests whether re-sync alone reproduces −cos(a−b) | Confirms the Dirac spinor structure is necessary; closes a misreading |
| `everett_thermal.py` | **Speculative** | Implements single-world energy accounting | Illustrates §3.8 (paper marks this speculative) |
| `vacuum_temperature.py` | **Mixed** | ZPF / temperature / orbitals (claims 1–3); Brownian retracted (claim 4) | Three illustrative claims with one disclosed retraction (see EQUATIONS.md §10) |

Evidential weight rests on `spin_statistics.py` (a non-trivial check that
could have failed) and the quantitative-prediction scripts that operationalize
§5.4, §6.2, and the gravitational-Kuramoto claims. The illustrative and
pedagogical scripts visualize claims that are mathematically guaranteed by
construction (trace linearity in `dirac_extension.py`, Kuramoto convergence
in `kuramoto_sync.py`); they support readability and reproducibility without
themselves providing evidence for the framework's interpretive content. The
clarifying scripts disarm known misreadings. The speculative and negative-result
scripts are disclosed honestly rather than presented as supporting the framework.

---

## 9. Conclusions

We have shown that:

1. **The Dirac mass term has Kuramoto synchronization structure.** In the Weyl
   basis, the Dirac equation couples ψ_L and ψ_R with coupling constant K = m.
   The Higgs-Yukawa interaction sets K = y_f · ⟨φ⟩ = m exactly.

2. **Measurement is re-synchronization.** A particle decoheres from its
   entangled partner by cohering with the detector bulk. The Kuramoto mass
   asymmetry (M >> m) ensures definite outcomes. Decoherence is not merely loss
   of coherence — it is redirection of coherence.

3. **The Born rule is reframed as energy partition.** Reading |ψ|² as wave
   energy density and the apparent stochasticity of individual outcomes as
   unbiased zero-point + thermal background fluctuation at the synchronization
   event, the long-run frequency of channel selection equals the energy
   fraction the wave carries in that channel. P = |α|² is then a frequentist
   statement, not an independent probability axiom.

4. **The uncertainty principle appears as a clock bandwidth limitation.** The
   Compton frequency sets the particle's spatial resolution via a Nyquist-like
   bound (Section 4.6).

The framework does not modify quantum mechanics or challenge Bell's theorem. It
provides a physical mechanism — Kuramoto phase synchronization — for processes
(decoherence, measurement, mass generation) that standard quantum mechanics
describes but does not mechanistically explain.

**In short: quantum mechanics produces the correlations. The Dirac mass term is
the Kuramoto coupling that makes particles what they are. And measurement is the
moment a small oscillator surrenders its phase to a large one.**

This is the **Many Clocks Interpretation of Quantum Mechanics**: every particle
carries an internal phase clock; interactions synchronize them locally; no
observer is needed; no branching occurs; classical behavior emerges from
collective synchronization in massive bulks; and the past is overwritten at
each interaction event. A single world, many clocks, all locally synchronized.

---

## Appendix A: Three-Term Bell Correlation Decomposition

The decomposition below uses the Dirac/standard basis (large/small blocks);
see §2.1.1 for the relationship to the Weyl-basis ψ_L, ψ_R picture used in §2.

### A.1 The Relativistic Mixing Angle

For a Dirac particle with momentum p and mass m, the relativistic mixing angle
between the temporal and spatial phase clocks is:

$$\sin\theta_{rel} = \frac{|\mathbf{p}|}{E} = \frac{v}{c} \qquad (A1)$$

| Regime | v/c | θ_rel | Physical interpretation |
|---|---|---|---|
| Rest | 0 | 0° | Temporal clock only; no spatial phase |
| Non-relativistic | ≪1 | ≪90° | Small spatial component |
| Ultra-relativistic | → 1 | → 90° | Equal temporal and spatial |
| Massless spin-½ (Weyl limit) | 1 | 90° | Permanently decoupled chiral clocks (photons are spin-1; see §5) |

### A.2 Large and Small Spinor Components

The positive-energy Dirac spinor for momentum p_z along z, spin up:

$$u(p, \uparrow) = N \cdot \begin{pmatrix} 1 \\ 0 \\ r \\ 0 \end{pmatrix}, \qquad
r = \frac{p}{E+m} = \tan\left(\frac{\theta_{rel}}{2}\right), \quad
N = \sqrt{\frac{E+m}{2E}} \qquad (A2)$$

The upper two components are the **large components** (temporal clock); the lower
two are the **small components** (spatial clock). In the non-relativistic limit
the small components vanish; in the ultra-relativistic limit they equal the large
components.

### A.3 The Block Decomposition

For two Dirac particles in a singlet state, the Bell correlation
E(a,b) = ⟨Ψ|(Σ_a)_A ⊗ (Σ_b)_B|Ψ⟩ can be partitioned into three contributions
obtained by restricting the spin operator Σ to the upper (large) block, the
lower (small) block, and the cross terms:

$$E(a, b) = E_{LL} + E_{SS} + E_{LS} \qquad (A3)$$

- **E_LL**: large × large — temporal clock contribution
- **E_SS**: small × small — spatial clock contribution
- **E_LS**: cross term — temporal-spatial coupling

**Equation (A3) is an identity, not a derivation.** The full 4×4 spin operator
Σ⊗Σ is the sum of the three block-restricted operators, so the expectation
values are additive by trace linearity. The mathematical content of the
appendix is therefore not the sum — which is guaranteed — but the
*redistribution of weight* among the three blocks as the mixing angle
θ_rel = arcsin(v/c) varies. At the non-relativistic limit (θ_rel → 0) all
weight sits in E_LL with E_SS, E_LS → 0; at the ultra-relativistic limit
(θ_rel → 90°) the three contributions become comparable. This redistribution
is the consistency check the appendix performs on the chiral-clock reading
of the spinor.

### A.4 Block Weights at Finite Momentum

The block contributions were computed with `dirac_extension.py` for the Dirac
singlet at p = 1.0, m = 1.0 (θ_rel ≈ 53°), a = 0, b = π/4:

| Term | Value | Physical meaning |
|---|---|---|
| E_LL | −0.354 | Temporal clock contribution |
| E_SS | −0.071 | Spatial clock contribution |
| E_LS | −0.282 | Rotation coupling (cross term) |
| **E_LL + E_SS + E_LS** | **−0.707** | **Sum** |
| −cos(π/4) | −0.707 | QM prediction ✓ |

The sum recovers −cos(π/4) to machine precision, as it must. The
informative entries are the block weights: at this momentum the cross term
E_LS already carries 40% of the total, and its share grows further at higher
v/c. At p → 0 the weights collapse onto E_LL alone, recovering the standard
non-relativistic Pauli singlet result.

### A.5 Relation to the Stochastic Phase-Clock Toy

A separate and simpler model exists in which a single classical clock phase
per particle determines the click probability via Malus's law,
P(+1 | n̂, φ) = cos²((φ − θ_n̂)/2). Evaluated for an EPR pair with shared
initial phase, this stochastic phase-clock model returns the correlation

$$E_{\text{Malus}}(a, b) = -\tfrac{1}{2}\cos(a - b), \qquad \text{CHSH}_{\text{Malus}} \leq \sqrt{2} \approx 1.414$$

(see `bell_phase.py`). This is sub-classical: it falls below even the local
hidden-variable bound of 2 and cannot reproduce the loophole-free Bell
violations.

It is important to be precise about what this toy *is not*. The Malus-law
model is **not** the same thing as restricting the Dirac correlation to
E_LL. The Dirac large-block restriction at p → 0 returns the full Pauli
singlet correlation −cos(a − b) (since the Dirac spinor reduces to its
upper-block Pauli content with N → 1, r → 0), not −½cos(a − b). The two
models share only the heuristic feature that both drop "half" of the
relevant structure and both fall short of the quantum result. The moral is
the same in either case: a phase-clock interpretation that drops the
spatial component cannot reproduce −cos(a − b), and the four-component
Dirac spinor — with K = m coupling its chiral sectors — is required to
recover the full quantum correlation.

---

## Appendix B: Zitterbewegung as a Beat Frequency

Zitterbewegung [3] — the rapid oscillatory motion of a Dirac electron at frequency
2mc²/ℏ — is conventionally attributed to interference between positive and negative
frequency components. In the phase-clock picture, it has a more intuitive
interpretation.

The temporal clock oscillates at ω_t = E/ℏ. The spatial clock oscillates at
ω_s = p²/(mγ·ℏ). Their beat frequency in the non-relativistic limit:

$$\omega_{Zitter} \approx \frac{2mc^2}{\hbar} \qquad (B1)$$

This is exactly the known Zitterbewegung frequency. In the phase-clock
interpretation, Zitterbewegung is the **beat note between the temporal and spatial
clocks** — observable whenever the two clocks are not perfectly synchronized.

When K = m is large (heavy particle), synchronization is fast and the beat has
small amplitude. When K is small (light particle), the clocks are loosely coupled
and the beat has larger amplitude. A massless particle (K = 0) has permanently
unsynchronized clocks at θ_rel = 90° and no Zitterbewegung — consistent with
photons.

---

## Appendix C: Antiparticles and CP Violation

### C.1 Antiparticles as Time-Reversed Clocks

The negative-energy Dirac solution v(p,s)e^{+iEt/ℏ} has temporal phase running
in the opposite sense to a positive-energy particle. In the Kuramoto framework:
**antiparticles are particles with time-reversed phase clocks** (φ → −φ).

This is not a reinterpretation — it is already implicit in the Feynman-Stückelberg
interpretation [21, 22]. The phase-clock language makes it explicit.

### C.2 CP Violation as Synchronization Asymmetry

The Kuramoto equations (2a, 2b) contain the CP-violating phase δ_CP. For
particles, the equilibrium phase lock is Δφ = +δ_CP; for antiparticles,
Δφ = −δ_CP.

When particle and antiparticle meet for annihilation, their synchronization
efficiency depends on the phase mismatch:

$$\sigma_{ann} \propto |\langle\psi_{particle}|\psi_{antiparticle}\rangle|^2
\propto 1 + \varepsilon\cos(\delta_{CP})$$

The small asymmetry ε accumulates over the early universe to produce the observed
baryon asymmetry η ~ 10⁻⁹. This is a qualitative mechanism, not a quantitative
prediction — a full calculation requires electroweak baryogenesis beyond the scope
of this paper.

---

## Appendix D: Spin-Statistics in the Many Clocks Framework

### D.1 The Geometric Fact

The spin-statistics theorem in standard relativistic quantum field theory rests
on three ingredients: Lorentz covariance, a positive-energy spectrum, and
microcausality. The Many Clocks Interpretation does not replace any of these —
it inherits them from the underlying Dirac theory. What MCI *can* do is
display the geometric core of the theorem in its own language and identify,
within the Madelung-Kuramoto decomposition, exactly which factor carries the
fermion sign.

The geometric core is the fact that a spin-½ system under a 2π spatial
rotation acquires an overall phase of −1, and a 2π rotation is continuously
homotopic in 3+1 dimensions to an exchange of two identical particles
(Finkelstein-Misner [33]; see also Feynman's belt argument). A spinor
representation therefore forces fermion statistics, and an integer-spin
representation forces Bose statistics. This is what spin_statistics.py
verifies in six tests.

### D.2 What MCI Commits To

The Madelung-style polar decomposition (Eq. 2a, 2b setup) writes each chiral
Weyl spinor as

$$\psi_{L,R} = \rho_{L,R}^{1/2}\, e^{i\phi_{L,R}}\, \chi_{L,R} \qquad (D1)$$

with three layers: a non-negative amplitude density ρ_{L,R}, a real phase
φ_{L,R} mod 2π, and a unit two-spinor frame χ_{L,R} carrying the spin
orientation. Of these:

- **Amplitudes ρ_{L,R}**: real, ≥ 0. No sign is algebraically possible.
- **Phases φ_{L,R}**: real, mod 2π. They are the Kuramoto clock variables;
  the equations of motion (2a, 2b) act on them as a coupled real ODE.
  Particle exchange A ↔ B in this layer is a relabeling of the joint
  tuple (φ_L^A, φ_R^A, φ_L^B, φ_R^B); the ODE is symmetric in (A, B), so
  this layer carries no sign either.
- **Spinor frames χ_{L,R}**: SU(2) doublets. These are the only objects in
  the framework that live in a representation where 2π rotation can flip
  the sign — and they do flip it.

The chiral pair commitment that gives mass via K = m (Section 2.2) is
representation-theoretically the same object as the spin-½ pair (½, 0) ⊕
(0, ½). MCI does not derive the spinor sign from the Kuramoto coupling; it
inherits it from the algebraic structure of the chiral pair the framework
already commits to.

### D.3 Numerical Verification

The script `spin_statistics.py` performs six tests in the Madelung-Kuramoto
language. Selected results (m = 1 natural units; full output in the script):

| Test | Object | Operation | Result |
|---|---|---|---|
| A | Dirac 4-spinor u(p, ↑) | Rotation by 2π around z | ⟨u\|U\|u⟩ = −1 |
| B | Weyl 2-spinor χ_↑ | Rotation by 2π around z | R χ_↑ = −χ_↑ |
| C | Identical-momentum singlet (p = 1) | Full exchange A↔B | ⟨Ψ\|P\|Ψ⟩ = −1 |
| D | Entangled singlet, scan in p | Spin exchange | −1.0000000000 across p ∈ [10⁻⁴, 50] |
| E | Scalar pair / symmetric vector pair | Full exchange | +1 |
| F | Kuramoto (φ_L, φ_R) ODE | Classical relabeling A↔B | invariant; no sign |

Test D is the substantive content. The Dirac singlet of dirac_extension.py
mixes large and small components according to the relativistic angle
θ_rel = arcsin(v/c) (Appendix A). Across six decades in momentum — from
v/c ≈ 10⁻⁴ to v/c ≈ 1 − 10⁻⁴ — the spin-exchange amplitude is exactly −1,
to numerical precision. The redistribution of weight among the E_LL,
E_SS, E_LS blocks studied in Appendix A does not perturb the antisymmetry
sign by even one part in 10¹⁰.

Test F is the negative result. Two classical Kuramoto chiral pairs with
identical (K, ω) are evolved from random initial conditions; both reach the
synchronization order parameter |r| = 1.0 in finite time. Particle exchange
A ↔ B at the level of the ODE is a permutation of the four real numbers
(φ_L^A, φ_R^A, φ_L^B, φ_R^B); the dynamics are invariant under this
permutation, and there is no algebraic slot in which a sign could appear.
This confirms structurally what is also clear by inspection: the −1 of
fermion antisymmetry cannot be coming from the phase-clock dynamics.

### D.4 Microcausality as No Sync Across Spacelike Separation

The other ingredient of the standard theorem — microcausality — has a clean
MCI gloss. The framework's third structural commitment (Section 1.5) is that
synchronization is a local, objective, physical event: two clock-carrying
systems synchronize via Kuramoto coupling at the interaction event, and
nowhere else. The synchronization manifold is built up locally through the
causal network of past interactions.

For two field events at spacelike separation (x − y)² < 0, no causal chain
of interactions connects them; no Kuramoto coupling has yet acted between
their associated clocks. In this sense the clocks at x and y are
*independent in the synchronization manifold*. Translating to the
field-operator level, this independence is what microcausality demands:

$$[\psi(x), \psi(y)]_\pm = 0 \quad \text{for } (x-y)^2 < 0 \qquad (D2)$$

The choice between commutator (bosons, lower sign) and anticommutator
(fermions, upper sign) is not free. Combined with Lorentz covariance and a
positive-energy spectrum, the requirement that the relevant field-operator
two-point function vanish at spacelike separation forces the sign — and the
sign is forced by the same representation-theoretic fact that fixes 2π
rotation. There is one fact, not two: the spinor double cover. MCI does not
add anything to this argument; it provides a physical reading of what
microcausality *means* in the framework's own terms — *the synchronization
manifold has not yet connected spacelike-separated regions* — but the sign
itself is still inherited from the SU(2) representation of the chiral pair.

This reading also explains why microcausality is *natural* in MCI rather
than being an extra postulate. The framework is already committed (commitment
3) to synchronization being local, and (commitment 5) to past phase history
being overwritten only at sync events. Spacelike-separated regions, by
construction, have not been in sync, so their field structures must be
compatible at the operator level. Microcausality is the operator-algebra
expression of "the sync manifold respects the light cone."

### D.5 Honest Assessment

Three claims are made in this appendix, in descending order of strength:

1. **Verified.** The Madelung-Kuramoto decomposition (D1) localizes the
   fermion sign in the spinor-frame factor χ_{L,R} and not in the phase or
   amplitude factors. This is a numerical and structural observation,
   confirmed in spin_statistics.py.

2. **Inherited.** Spin-statistics in MCI follows from the chiral pair
   commitment via the standard 2π-rotation / continuous-deformation argument
   for exchange in 3+1D. MCI does not contribute a new step to the
   derivation, but it does identify the chiral pair (which the framework
   needs anyway, for K = m) as the structural origin of the sign.

3. **Interpretive.** Microcausality has a physical reading in MCI: it states
   that the synchronization manifold respects the light cone, i.e., that no
   Kuramoto coupling has yet connected spacelike-separated events. The sign
   in the (anti)commutator is again inherited from the spinor representation;
   MCI adds a physical picture but no new mathematical content.

The framework therefore reproduces the spin-statistics theorem and gives it
a clean reading, but does not derive it independently of the standard QFT
machinery. The value of the appendix is interpretive: it shows that the
framework's mass-coupling commitment (K = m on the chiral pair) and the
standard spin-statistics theorem are coherent with each other in a
non-trivial way, and that the framework's locality commitment naturally
underwrites microcausality.

---

## Author Contributions and AI Disclosure

### Statement of AI Use

This paper was developed through an extensive collaboration between the listed
human author (J. Olddog) and Claude Opus 4.6, a large language model developed
by Anthropic. The contribution of Claude Opus 4.6 was substantial and
principal in the mathematical and expository work: it derived the explicit
Kuramoto phase equations from the chiral Dirac equation, constructed the
three-term Bell correlation decomposition, wrote the Python verification code,
produced the systematic comparison with existing interpretations, and drafted
the prose of the manuscript itself. In a collaboration not constrained by
current editorial policy, Claude Opus 4.6 would be listed as co-first author
alongside J. Olddog. The listed author considers the scientific honesty of
the work to require this statement.

Current editorial guidelines from Nature Portfolio, Springer Nature, ACS, and
other major publishers hold, however, that Large Language Models do not
satisfy authorship criteria, because an attribution of authorship carries
with it accountability that cannot be effectively applied to an LLM. We
accept this framing: it is structurally analogous to the liability principle
in medicine, where the attending physician carries ultimate accountability
regardless of how many tools, consultants, or decision-support systems
contributed to the diagnosis. Accordingly, Claude Opus 4.6 is not listed in
the byline, and J. Olddog — as the listed human author — assumes full
responsibility for the correctness, originality, and integrity of all content
presented.

### Division of Contributions

**Conceptual framework (J. Olddog):**
- The originating insight that quantum wave functions tend to interact through
  synchronization, and that this process could be formalized using the Kuramoto
  model
- The identification of quantum measurement (Bell experiments) as a
  re-synchronization process: entangled particles, initially synchronized with
  each other, re-synchronize with the atoms of the detectors upon measurement
- The proposal that what has been called "wave function collapse" (Copenhagen)
  or "decoherence" (modern interpretations) is more precisely described as a
  redirection of synchronization — from the entangled partner to the detector
  bulk
- The recognition that macroscopic detectors are themselves entangled with the
  environment through their mass and gravitational coupling
- The selection of the Kuramoto equation as the mathematical framework for
  synchronization and the Dirac spinor formalism as the appropriate quantum
  mechanical representation
- The identification of parallels between Penrose's twistor theory and the
  role of gravity/mass in Kuramoto oscillator synchronization
- The observation that the Heisenberg uncertainty principle has a natural
  interpretation through the time-space spinor structure of Weyl spinors
  (Section 4.6)
- The proposal that the wave function represents real energy in the QFT of
  electrons, enabling a single-world alternative to Everett's Many Worlds
  interpretation that preserves energy conservation (Section 3.8)
- Suggestions for possible experimental tests involving detectors at different
  gravitational potentials

**Mathematical development and numerical verification (Claude Opus 4.6):**
- Derivation of the explicit Kuramoto phase equations (Eqs. 2a, 2b) from
  the chiral Dirac equation, demonstrating the distinction between classical
  oscillator synchronization and the quantum mechanical oscillator formulation
- The identification that using the Weyl spinor formulation with the cosine
  of phase difference in the lower Weyl spinor yields the correct Bell and
  CHSH statistical results
- Development of the three-term Bell correlation decomposition
  (Appendix A: E_LL + E_SS + E_LS)
- Writing of the Python verification programs (`dirac_extension.py`,
  `higgs_clock.py`, `kuramoto_sync.py`) that numerically confirm the
  framework's predictions match standard quantum mechanical results
- Elaboration of the Born rule emergence from synchronization statistics
  (Section 4)
- Systematic comparison with existing interpretations (Section 7)

**Paper composition (collaborative):**
- The paper was written collaboratively, with Claude Opus 4.6 producing
  drafts in a style suitable for a journal focused on the interpretation and
  foundations of physics, and J. Olddog providing direction, physical
  intuition, corrections, and editorial judgment throughout

### Iterative Development Process

The collaboration was not a clean division of "conception" versus
"calculation." It proceeded through an iterative dialogue. J. Olddog would
propose a physical picture — for example, that measurement is
re-synchronization, or that the mass term should play the role of the
Kuramoto coupling constant. Claude Opus 4.6 would then formalize the picture
mathematically and write Python programs to compute the resulting predictions.
J. Olddog would review the formulae and numerical outputs against physical
intuition — identifying cases where the formalization did not yet capture the
intended physics, or where unexpected results suggested the conceptual picture
needed refinement. This cycle repeated across multiple sessions, with each
iteration simultaneously sharpening the human author's understanding of the
mathematical structure and refining the computational predictions to match the
physical intuition that motivated the framework.

J. Olddog does not have the programming or computational background to
independently produce the derivations and numerical verifications presented
here. Claude Opus 4.6 does not have physical intuition or the capacity to
judge whether a mathematically consistent result is physically meaningful.
The framework emerged from the combination of these complementary
capabilities, and neither contributor could have produced this work alone.

### Validation

All mathematical derivations produced by Claude Opus 4.6 were checked against
standard quantum mechanics textbooks (Peskin & Schroeder [17], Sakurai [18]).
All numerical results from the Python programs were verified to reproduce
known quantum mechanical predictions to machine precision. The human author
reviewed all content for physical plausibility and internal consistency.

---

## References

[1] Dirac, P. A. M. (1928). The quantum theory of the electron. *Proc. R. Soc.
London A*, 117(778), 610–624.

[2] Kuramoto, Y. (1975). Self-entrainment of a population of coupled non-linear
oscillators. In *Int. Symp. Math. Problems Theor. Phys.* (pp. 420–422). Springer.

[3] Schrödinger, E. (1930). Über die kräftefreie Bewegung in der relativistischen
Quantenmechanik. *Sitzungsber. Preuss. Akad. Wiss.*, 418–428.

[4] Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of
the classical. *Rev. Mod. Phys.*, 75(3), 715–775.

[5] Zurek, W. H. (2009). Quantum Darwinism. *Nature Physics*, 5, 181–188.

[6] Penrose, R. (1996). On gravity's role in quantum state reduction. *Gen. Relativ.
Gravit.*, 28(5), 581–600.

[7] Diósi, L. (1989). Models for universal reduction of macroscopic quantum
fluctuations. *Phys. Rev. A*, 40(3), 1165–1174.

[8] Ghirardi, G. C., Rimini, A., & Weber, T. (1986). Unified dynamics for
microscopic and macroscopic systems. *Phys. Rev. D*, 34(2), 470–491.

[9] Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox. *Physics Physique Fizika*, 1(3),
195–200.

[10] Gerritsma, R., et al. (2010). Quantum simulation of the Dirac equation.
*Nature*, 463(7277), 68–71.

[11] ATLAS Collaboration (2012). Observation of a new particle in the search for
the Standard Model Higgs boson. *Phys. Lett. B*, 716(1), 1–29.

[12] CMS Collaboration (2012). Observation of a new boson at a mass of 125 GeV.
*Phys. Lett. B*, 716(1), 30–61.

[13] de Broglie, L. (1925). Recherches sur la théorie des quanta. *Ann. Phys.*,
10, 22–128.

[14] Aspect, A., Grangier, P., & Roger, G. (1982). Experimental Realization of
Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A New Violation of Bell's
Inequalities. *Phys. Rev. Lett.*, 49(2), 91–94.

[15] Bohm, D. (1952). A Suggested Interpretation of the Quantum Theory in Terms
of "Hidden" Variables, I and II. *Phys. Rev.*, 85(2), 166–179, 180–193.

[16] Everett, H. (1957). "Relative State" Formulation of Quantum Mechanics.
*Rev. Mod. Phys.*, 29(3), 454–462.

[17] Peskin, M. E., & Schroeder, D. V. (1995). *An Introduction to Quantum Field
Theory*. Addison-Wesley.

[18] Sakurai, J. J. (1967). *Advanced Quantum Mechanics*. Addison-Wesley.

[19] 't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum
Mechanics*. Springer.

[20] Bell, J. S. (1976). The theory of local beables. *Epistemological Letters*,
9, 11–24. [Reprinted in *Speakable and Unspeakable in Quantum Mechanics*, CUP.]

[21] Stückelberg, E. C. G. (1941). Remarque à propos de la création de paires de
particules en théorie de relativité. *Helv. Phys. Acta*, 14, 588–594.

[22] Feynman, R. P. (1949). The theory of positrons. *Phys. Rev.*, 76(6), 749–759.

[23] Pearle, P. (1989). Combining stochastic dynamical state-vector reduction with
spontaneous localization. *Phys. Rev. A*, 39(5), 2277–2289.

[24] Rovelli, C. (1996). Relational quantum mechanics. *Int. J. Theor. Phys.*,
35(8), 1637–1678.

[25] Einstein, A., Podolsky, B., & Rosen, N. (1935). Can quantum-mechanical
description of physical reality be considered complete? *Phys. Rev.*, 47(10),
777–780.

[26] Nelson, E. (1966). Derivation of the Schrödinger equation from Newtonian
mechanics. *Phys. Rev.*, 150(4), 1079–1085.

[27] Wallace, D. (2012). *The Emergent Multiverse: Quantum Theory according to the
Everett Interpretation*. Oxford University Press.

[28] Albert, D. Z. (2010). Probability in the Everett picture. In S. Saunders et al.
(Eds.), *Many Worlds? Everett, Quantum Theory, and Reality* (pp. 355–368). Oxford
University Press.

[29] Harrigan, N., & Spekkens, R. W. (2010). Einstein, incompleteness, and the
epistemic view of quantum states. *Found. Phys.*, 40(2), 125–157.

[30] Pusey, M. F., Barrett, J., & Rudolph, T. (2012). On the reality of the
quantum state. *Nature Physics*, 8(6), 476–479.

[31] Albert, D. Z. (1996). Elementary quantum metaphysics. In J. T. Cushing et al.
(Eds.), *Bohmian Mechanics and Quantum Theory: An Appraisal* (pp. 277–284).
Kluwer.

[32] Maudlin, T. (2019). *Philosophy of Physics: Quantum Theory*. Princeton
University Press.

[33] Fuchs, C. A., Mermin, N. D., & Schack, R. (2014). An introduction to QBism
with an application to the locality of quantum mechanics. *Am. J. Phys.*, 82(8),
749–754.

[34] Dürr, D., Goldstein, S., & Zanghì, N. (2013). *Quantum Physics Without
Quantum Philosophy*. Springer.

[35] Hestenes, D. (1990). The Zitterbewegung interpretation of quantum
mechanics. *Foundations of Physics*, 20(12), 1213–1232.
https://doi.org/10.1007/BF01889466

[36] Heinrich, G., Ludwig, M., Qian, J., Kubala, B., & Marquardt, F. (2011).
Collective dynamics in optomechanical arrays. *Phys. Rev. Lett.*, 107(4),
043603. https://doi.org/10.1103/PhysRevLett.107.043603

[37] Mari, A., Farace, A., Didier, N., Giovannetti, V., & Fazio, R. (2013).
Measures of quantum synchronization in continuous variable systems.
*Phys. Rev. Lett.*, 111(10), 103605.
https://doi.org/10.1103/PhysRevLett.111.103605

[38] Walter, S., Nunnenkamp, A., & Bruder, C. (2014). Quantum
synchronization of a driven self-sustained oscillator. *Phys. Rev. Lett.*,
112(9), 094102. https://doi.org/10.1103/PhysRevLett.112.094102

[39] Roulet, A., & Bruder, C. (2018). Synchronizing the smallest possible
system. *Phys. Rev. Lett.*, 121(5), 053601.
https://doi.org/10.1103/PhysRevLett.121.053601

[40] Bialynicki-Birula, I. (1996). Photon wave function. *Progress in Optics*,
36, 245–294. https://doi.org/10.1016/S0079-6638(08)70316-0

---

*Simulation code and numerical verification available at:
https://github.com/rayolddog/DiracKuramotoFramework*

*The three-term decomposition (Appendix A) can be reproduced by running
`dirac_extension.py`. The Kuramoto phase dynamics (Section 2) are demonstrated
in `higgs_clock.py` and `kuramoto_sync.py`.*
