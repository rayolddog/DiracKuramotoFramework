# The Dirac Equation as a Kuramoto Phase-Synchronization System:
## Mass as Chiral Coupling, Measurement as Re-Synchronization, and a Single-World Account of Decoherence

**J. Olddog¹**
¹ Independent Research

*Correspondence: rayolddog (GitHub)*
*Preprint — not yet peer reviewed*

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

This identification has three consequences developed in this paper. First, a
non-relativistic phase-clock model using only the temporal (large) Dirac component
yields a Bell correlation E(a,b) = −½cos(a−b), below even the classical Bell bound.
When the spatial (small) component is included via the relativistic mixing angle
θ_rel = arcsin(v/c), the full quantum result E(a,b) = −cos(a−b) is recovered
exactly through a three-term decomposition E = E_LL + E_SS + E_LS.

Second, quantum measurement is re-interpreted as Kuramoto re-synchronization: a
particle initially synchronized with its entangled partner re-synchronizes to the
macroscopic detector bulk, whose overwhelmingly greater Kuramoto inertia
(M_detector >> m_particle) forces conformity. Decoherence is not merely loss of
phase coherence with the partner — it is the positive process of gaining coherence
with the bulk. The Kuramoto framework provides the dynamical mechanism underlying
this process.

Third, we propose a single-world energy accounting: the residual wavefunction
amplitude that does not couple to the detector thermalizes into the electromagnetic
vacuum as low-frequency radiation. No branches are created. The energy is conserved
within a single world.

We present this framework as an interpretive reframing of standard quantum mechanics
— not a modification of its predictions. The Dirac equation is unchanged; Bell's
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
a mysterious collapse with no physical mechanism. Everett's many-worlds preserves
unitarity at the cost of infinite unobservable branches. Bohmian mechanics accepts
explicit nonlocality through a physically inert pilot wave.

### 1.2 What Is Missing: A Dynamical Mechanism for Decoherence

Environmental decoherence [Zurek 2003] has become the standard framework for
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

2. **Measurement is re-synchronization** (Section 4). When a particle interacts
   with a macroscopic detector, the Kuramoto dynamics drive the particle's phase
   from coherence with its entangled partner to coherence with the detector bulk.
   This provides a physical picture of decoherence. This is an interpretive claim.

3. **Residual energy thermalizes in a single world** (Section 5). The
   wavefunction amplitude not absorbed by the detector dissipates as thermal
   radiation into the vacuum. No branches are created. This is a speculative but
   physically motivated proposal.

### 1.4 What This Paper Does Not Claim

We state clearly at the outset:

- We do not challenge Bell's theorem. The quantum correlations E(a,b) = −cos(a−b)
  arise from the entangled singlet state and the full Dirac spinor structure —
  standard quantum mechanics.
- We do not modify the Dirac equation or any of its predictions.
- We do not propose new physics. We propose a new *mechanism* for known physics.
- The framework is an interpretation — it may or may not generate distinguishable
  predictions from standard decoherence theory. We are honest about this
  throughout.

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

### 2.2 The Kuramoto Identification

The standard Kuramoto model [Kuramoto 1975] describes the phase dynamics of N
coupled oscillators:

$$\frac{d\phi_i}{dt} = \omega_i + \frac{K}{N}\sum_j \sin(\phi_j - \phi_i)$$

Writing ψ_L = ρ_L^{1/2} e^{iφ_L} χ_L and ψ_R = ρ_R^{1/2} e^{iφ_R} χ_R, the
phase dynamics extracted from Equations (1) yield:

$$\frac{d\phi_L}{dt} = \omega_L + K\sin(\phi_R - \phi_L + \delta_{CP}) \qquad (2a)$$

$$\frac{d\phi_R}{dt} = \omega_R + K\sin(\phi_L - \phi_R - \delta_{CP}) \qquad (2b)$$

where the coupling constant is:

$$\boxed{K = y_f \cdot |\langle\phi\rangle| = y_f \cdot \frac{v}{\sqrt{2}} = m} \qquad (3)$$

**Equation (3) is the central result of this paper: the particle's mass equals
its Kuramoto coupling constant.**

The Higgs vacuum expectation value ⟨φ⟩ = v/√2 ≈ 174 GeV drives the two chiral
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
| Negative-energy Dirac solutions = reversed temporal phase | Standard (Feynman-Stückelberg) |
| **Mass term has Kuramoto coupling structure** | **New interpretation (this work)** |
| **K = m identification** | **New (this work)** |

---

## 3. The Three-Term Bell Correlation Decomposition

### 3.1 The Relativistic Mixing Angle

For a Dirac particle with momentum p and mass m, the relativistic mixing angle
between the temporal and spatial phase clocks is:

$$\sin\theta_{rel} = \frac{|\mathbf{p}|}{E} = \frac{v}{c} \qquad (5)$$

| Regime | v/c | θ_rel | Physical interpretation |
|---|---|---|---|
| Rest | 0 | 0° | Temporal clock only; no spatial phase |
| Non-relativistic | ≪1 | ≪90° | Small spatial component |
| Ultra-relativistic | → 1 | → 90° | Equal temporal and spatial |
| Massless (photon) | 1 | 90° | Permanently decoupled chiral clocks |

### 3.2 Large and Small Spinor Components

The positive-energy Dirac spinor for momentum p_z along z, spin up:

$$u(p, \uparrow) = N \cdot \begin{pmatrix} 1 \\ 0 \\ r \\ 0 \end{pmatrix}, \qquad
r = \frac{p}{E+m} = \tan\left(\frac{\theta_{rel}}{2}\right), \quad
N = \sqrt{\frac{E+m}{2E}} \qquad (6)$$

The upper two components are the **large components** (temporal clock); the lower
two are the **small components** (spatial clock). In the non-relativistic limit
the small components vanish; in the ultra-relativistic limit they equal the large
components.

### 3.3 The Decomposition

For two Dirac particles in a singlet state, the Bell correlation
E(a,b) = ⟨Ψ|(Σ_a)_A ⊗ (Σ_b)_B|Ψ⟩ decomposes as:

$$E(a, b) = E_{LL} + E_{SS} + E_{LS} \qquad (7)$$

where:
- **E_LL**: large × large — temporal clock contribution
- **E_SS**: small × small — spatial clock contribution
- **E_LS**: cross term — temporal-spatial coupling

### 3.4 Numerical Verification

The decomposition was verified numerically (see `dirac_extension.py`). At p = 1.0,
m = 1.0 (θ_rel ≈ 53°), a = 0, b = π/4:

| Term | Value | Physical meaning |
|---|---|---|
| E_LL | −0.354 | Temporal clock contribution |
| E_SS | −0.071 | Spatial clock contribution |
| E_LS | −0.282 | Rotation coupling (key term) |
| **E_LL + E_SS + E_LS** | **−0.707** | **Sum** |
| −cos(π/4) | −0.707 | QM prediction ✓ |

**The sum is exact to machine precision for all values of p and m tested.**

### 3.5 The Non-Relativistic Deficiency Explained

A non-relativistic phase-clock model that tracks only the temporal de Broglie
phase ω = E/ℏ retains only E_LL, discarding E_SS and E_LS. This gives:

$$E_{NR}(a, b) = -\frac{1}{2}\cos(a - b), \qquad \text{CHSH}_{NR} \leq \sqrt{2} \approx 1.414$$

This falls below even the classical Bell bound of 2.0. The deficiency is not a
failure of the phase-clock interpretation — it is a failure to include both clocks.
When the full four-component Dirac spinor is used, the exact quantum result is
recovered. The mass term K = m ensures both clocks are present and coupled.

---

## 4. Measurement as Re-Synchronization

### 4.1 The Physical Picture

This section develops the interpretive core of the framework. We propose that
quantum measurement is a specific type of Kuramoto synchronization event:

> **A particle initially phase-synchronized with its entangled partner
> re-synchronizes to the macroscopic detector bulk.**

The detector is a macroscopic system with overwhelmingly greater Kuramoto inertia
(M_detector >> m_particle). The measurement interaction forces the particle to
conform its phase to the detector's collective phase Φ_bulk, just as a small
oscillator entrained by a massive one must adopt the massive oscillator's
frequency.

### 4.2 Decoherence Is Half the Story

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

### 4.3 The Mass Asymmetry

The detector's macroscopic mass provides the asymmetry that ensures definite
outcomes. In Kuramoto dynamics, when a small oscillator (mass m) couples to a
large oscillator (mass M >> m), the small oscillator always conforms to the
large one. The reverse — the detector conforming to the particle — is
dynamically suppressed by a factor of m/M.

This is the physical content of "wavefunction collapse": the Kuramoto mass
asymmetry between particle and detector makes the measurement outcome definite,
not because of a postulated projection, but because of the dynamical inevitability
of a small oscillator locking to a massive one.

### 4.4 Gravitational Coherence of the Bulk

What maintains the coherence of the detector bulk itself? We propose that gravity
provides this role. The gravitational interaction between the ~10²⁶ atoms in a
macroscopic detector provides a collective Kuramoto coupling that maintains a
common phase Φ_bulk across the detector. This is analogous to the well-known
classical synchronization of metronomes on a shared massive platform.

The gravitational Kuramoto coupling for a mass M interacting with a bulk at
distance Δz is:

$$\Gamma_{grav} = \frac{GM^2}{\hbar \Delta z}$$

For macroscopic objects (M ~ 1 kg, Δz ~ 1 m), Γ_grav ~ 10⁻⁷ rad/s — small
compared to atomic frequencies but sufficient over macroscopic timescales to
maintain bulk phase coherence.

### 4.5 Connection to Penrose-Diósi

This picture has a natural connection to Penrose's proposal [Penrose 1996] that
gravity causes quantum state reduction. Penrose argues that a superposition of
two mass configurations with different spacetime geometries is unstable, with
collapse timescale τ ~ ℏ/E_g where E_g is the gravitational self-energy of the
superposition.

In the Kuramoto framework, this translates to: the gravitational bulk provides
a phase reference, and any quantum superposition that would require the particle
to maintain coherence against the gravitational synchronization pressure will
decohere on a timescale set by the gravitational coupling strength. The Penrose
energy E_g maps onto the Kuramoto coupling rate Γ_grav. The two frameworks
predict the same qualitative behavior — heavier objects decohere faster — from
different dynamical starting points.

### 4.6 What This Section Does Not Claim

The re-synchronization picture is interpretive. It does not:

1. Derive decoherence rates quantitatively from Kuramoto parameters (this would
   require a full quantum treatment of many-body Kuramoto dynamics)
2. ~~Explain how the Born rule probability P = |α|² emerges from synchronization
   dynamics~~ (addressed in Section 6)
3. Provide a Lorentz-covariant formulation of the measurement process

---

## 5. Single-World Energy Accounting

### 5.1 The Energy Bookkeeping Problem

Before measurement, a system ψ = α|0⟩ + β|1⟩ carries total energy E = ℏω. After
measurement produces outcome |0⟩, what happens to the energy associated with the
|β|² amplitude?

- Copenhagen: it vanishes — the wavefunction collapses
- Everett: it persists in an inaccessible branch
- Bohmian: the pilot wave carries no energy

Each answer is unsatisfying. We propose a fourth:

### 5.2 Thermalization of Residual Amplitude

In the Kuramoto measurement process (Section 4), the detector resonantly absorbs
the energy quantum ℏω₀ corresponding to the realized outcome. The residual
amplitude — the portion of the wavefunction that did not synchronize with the
detector — has no resonant absorber available.

We propose that this residual couples weakly to the broadband electromagnetic
environment and thermalizes as low-frequency radiation:

$$E_{residual} = (1 - P) \cdot \hbar\omega$$

where P = |α|² is the Born-rule probability of the realized outcome.

### 5.3 A Single World

This gives a definite single-world account:

1. ψ is a real physical field carrying energy
2. Measurement is resonant energy extraction (the detector takes ℏω₀)
3. The residual thermalizes into the vacuum
4. One classical fact results, with Born-rule probability
5. No branch is created; the residual energy is in this world as thermal radiation

### 5.4 Honest Caveats

This proposal is the most speculative part of the paper:

1. The thermalization rate is not derived from first principles
2. The mechanism by which residual amplitude "finds" the thermal bath is not
   specified beyond analogy with spontaneous emission
3. The Born rule is derived from synchronization statistics (Section 6)
4. We do not claim this resolves the measurement problem — it provides a physical
   picture that is more complete than Copenhagen's "collapse" but not yet a
   rigorous derivation

**What we explicitly do not claim:** We previously explored whether accumulated
thermal residuals could account for the observed dark energy density. While a
crude order-of-magnitude estimate was suggestive, detailed analysis revealed the
calculation to be unreliable, and we withdraw this as a prediction. The
thermalization proposal stands independently of any cosmological implications.

---

## 6. The Born Rule from Synchronization Statistics

### 6.1 The Problem

The Born rule — P = |ψ|² — is the bridge between the mathematical formalism and
experimental outcomes. In standard quantum mechanics it is postulated, not derived.
Copenhagen asserts it. Everett's many-worlds claims to derive it from branch
counting, but this remains contested. The measurement problem, at its core, is the
question of why probability equals the squared modulus of a complex amplitude.

### 6.2 The Kuramoto Order Parameter

The Kuramoto model provides a natural answer. For N coupled oscillators with
phases φ₁, φ₂, ..., φ_N, the degree of collective synchronization is measured by
the order parameter:

$$R \cdot e^{i\Psi} = \frac{1}{N}\sum_{j=1}^{N} e^{i\phi_j} \qquad (9)$$

where R ∈ [0,1] is the synchronization amplitude and Ψ is the collective phase.
The probability that a single oscillator with phase φ locks to the collective
is proportional to R² — the squared modulus of the complex order parameter.

This is not a coincidence. It is a general property of phase-coupled oscillator
systems: the coupling efficiency between a single oscillator and a synchronized
cluster depends on the squared amplitude of the cluster's complex coherence.

### 6.3 Application to Quantum Measurement

Consider a particle in superposition ψ = α|0⟩ + β|1⟩ arriving at a detector.
The detector is a macroscopic Kuramoto-synchronized bulk with N >> 1 oscillators
locked to phase Φ_bulk.

The particle carries two components, each a complex amplitude with a definite
phase:

- Component |0⟩ with amplitude α = |α|e^{iφ₀}
- Component |1⟩ with amplitude β = |β|e^{iφ₁}

The Kuramoto synchronization process couples the particle to the detector bulk.
The coupling strength between the particle component and the detector depends on
the complex overlap — the projection of the particle's phase oscillator onto
the detector's synchronized state.

For a complex oscillator with amplitude A·e^{iφ} coupling to a reference
oscillator, the synchronization probability is:

$$P_{sync} \propto |A \cdot e^{i\phi}|^2 = |A|^2 \qquad (10)$$

The phase determines *which* detector eigenstate is reached. The amplitude
determines *how likely* that synchronization is. Averaging over the random bulk
phase Φ_bulk (which is uniformly distributed over [0, 2π) from the particle's
perspective), all cross terms vanish:

$$\langle e^{i(\phi_0 - \phi_1)} \rangle_{\Phi_{bulk}} = 0 \qquad (11)$$

Only the diagonal terms survive:

$$P(|0\rangle) = |\alpha|^2, \qquad P(|1\rangle) = |\beta|^2 \qquad (12)$$

This is the Born rule, derived from Kuramoto synchronization statistics rather
than postulated.

### 6.4 Why the Squared Modulus?

The answer is geometric. The wave function is complex because the internal clock
is a phase oscillator — it lives on a circle in the complex plane. The probability
of synchronization between two oscillators is the squared modulus of their complex
overlap because:

1. The coupling is linear in the complex amplitude (Kuramoto sine coupling)
2. Probability is quadratic in the coupling (energy transfer ∝ amplitude²)
3. The complex phase averages out over the bulk, leaving only |amplitude|²

This is identical to why the intensity of a classical wave is proportional to the
squared amplitude — and it should be, because the wave function *is* a real
oscillating field in this framework. The Born rule is the statement that quantum
probability equals wave intensity, which is the natural measure for any physical
wave coupling to a detector.

### 6.5 Connection to the Zero-Point Floor

The zero-point phase noise σ_φ(0) = 1/√2 rad (Section 9 of the equations
reference) sets a minimum uncertainty in the synchronization process. Even at
T = 0, a particle cannot synchronize with perfect fidelity — the irreducible
phase noise means that the probability |α|² always has a minimum variance.
This connects the Born rule to the Heisenberg uncertainty principle: both
emerge from the same zero-point phase floor.

### 6.6 What This Derivation Requires

The derivation rests on three assumptions, all already present in the framework:

1. The wave function is a physical oscillating field (not merely a calculational
   tool)
2. Measurement is Kuramoto synchronization to a macroscopic bulk
3. The detector's bulk phase is uniformly distributed relative to the particle's
   phase basis

Assumption 3 is the most important. It is equivalent to the statement that the
detector has no prior knowledge of which outcome will occur — it is the
Kuramoto equivalent of the assumption of measurement independence in Bell's
theorem. The detector synchronizes to whichever component has the largest
coupling amplitude, with probability proportional to |amplitude|².

---

## 7. Zitterbewegung as a Beat Frequency

Zitterbewegung — the rapid oscillatory motion of a Dirac electron at frequency
2mc²/ℏ — is, according to accepted standards, attributed to interference between positive and negative
frequency components. In the phase-clock picture, it has a more intuitive
interpretation.

The temporal clock oscillates at ω_t = E/ℏ. The spatial clock oscillates at
ω_s = p²/(mγ·ℏ). Their beat frequency in the non-relativistic limit:

$$\omega_{Zitter} \approx \frac{2mc^2}{\hbar} \qquad (8)$$

This is exactly the known Zitterbewegung frequency. In the phase-clock
interpretation, Zitterbewegung is the **beat note between the temporal and spatial
clocks** — observable whenever the two clocks are not perfectly synchronized.

When K = m is large (heavy particle), synchronization is fast and the beat has
small amplitude. When K is small (light particle), the clocks are loosely coupled
and the beat has larger amplitude. A massless particle (K = 0) has permanently
unsynchronized clocks at θ_rel = 90° and no Zitterbewegung — consistent with
photons.

---

## 8. Antiparticles and CP Violation

### 7.1 Antiparticles as Time-Reversed Clocks

The negative-energy Dirac solution v(p,s)e^{+iEt/ℏ} has temporal phase running
in the opposite sense to a positive-energy particle. In the Kuramoto framework:
**antiparticles are particles with time-reversed phase clocks** (φ → −φ).

This is not a reinterpretation — it is already implicit in the Feynman-Stückelberg
interpretation. The phase-clock language makes it explicit.

### 7.2 CP Violation as Synchronization Asymmetry

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

## 9. The Massless Limit: An Open Question

For photons (m = 0, K = 0), the mixing angle θ_rel = 90° and the Dirac equation
decouples into independent Weyl equations. There is no Kuramoto coupling between
the chiral sectors.

Yet polarization-entangled photons achieve full Bell violation (CHSH = 2√2). How?

Two possible answers exist within the framework:

**Answer A:** For photons, the coupling K is set by energy rather than rest mass:
K = ω = E/ℏ. Photons synchronize through their oscillation frequency, not rest
mass. Since photons are always fully relativistic (θ_rel = 90°), all spinor
components contribute equally.

**Answer B:** The Maxwell equations for polarized light have their own two-sector
structure (Poincaré sphere), and the Kuramoto coupling may be derivable from
classical electrodynamics directly.

**We do not resolve this question here.** The photon-Bell connection requires
separate treatment. The core claim — that the Dirac mass term is a Kuramoto
coupling for massive fermions — stands regardless.

---

## 10. Qualitative Predictions and Consistency Checks

We distinguish between predictions that follow from the mathematical identification
(Section 2) and those that follow from the interpretive claims (Sections 4-6).

### 9.1 From the Mathematical Identification

**P1 — Three-term decomposition of Bell correlations.** For massive entangled
particles, the correlation E(a,b) = −cos(a−b) decomposes into E_LL + E_SS + E_LS,
with the relative contributions depending on θ_rel = arcsin(v/c). While E_total
is Lorentz-invariant, the decomposition itself is new and numerically verified.
A hypothetical experiment separately addressing large and small spinor components
could reveal this structure.

**P2 — Zitterbewegung as clock beat.** The identification of ω_Zitter = 2mc²/ℏ
as the beat frequency between temporal and spatial clocks is consistent with all
known properties of Zitterbewegung. Trapped-ion simulations with tunable effective
mass [Gerritsma et al. 2010] could probe the transition from locked to unlocked
clock behavior as effective mass passes through zero.

### 9.2 From the Interpretive Framework

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

### 9.3 Honest Assessment

These predictions are qualitative scaling arguments, not quantitative predictions
with computed coefficients. The framework in its current form is an interpretation
— it provides a physical mechanism consistent with known decoherence behavior but
does not yet make predictions distinguishable from standard decoherence theory.
This is the main limitation and the main avenue for future work.

---

## 11. Comparison with Existing Frameworks

### 10.1 Interpretations of Quantum Mechanics

| Property | Copenhagen | Everett MWI | Bohmian | GRW/CSL | Superdeterminism | **This work** |
|---|---|---|---|---|---|---|
| ψ is real? | No | Yes | Yes | Yes | Varies | **Yes** |
| Collapse? | Postulated | No | No | Stochastic | Not needed | **Re-synchronization** |
| Branching? | No | Yes (∞) | No | No | No | **No** |
| Residual energy? | Discarded | In branches | Pilot wave | Noise | Not addressed | **Thermal vacuum** |
| Single world? | By fiat | No | Yes | Yes | Yes | **Yes (by physics)** |
| Mechanism? | None | None | Pilot wave | Random hits | Initial conditions | **Kuramoto sync** |
| Bell's theorem? | Accepted | Accepted | Accepted (nonlocal) | Accepted | Denied (meas. indep.) | **Accepted** |
| Born rule | Postulated | Derived (contested) | Derived | Modified | Derived (contested) | **Derived (Section 6)** |

### 10.2 Decoherence Models

The closest existing framework is the Penrose-Diósi gravitational decoherence
model [Penrose 1996, Diósi 1989]. Both that model and ours identify gravity as
the agent of classicalization. The key differences:

- Penrose-Diósi: collapse timescale τ ~ ℏ/E_g (gravitational self-energy)
- This work: decoherence timescale set by Kuramoto re-synchronization rate to
  the gravitational bulk

The predictions are qualitatively similar (heavier → faster decoherence) but
derive from different dynamics. A quantitative comparison awaits a full
derivation of Kuramoto decoherence rates from first principles.

### 10.3 Zurek's Einselection

Zurek's quantum Darwinism [Zurek 2003, 2009] identifies "pointer states" as
states that survive interaction with the environment. In the Kuramoto picture,
pointer states are the synchronized states — the phase-locked configurations
that are stable under coupling to the macroscopic bulk. States that cannot
synchronize (superpositions of macroscopically distinct mass configurations)
are dynamically unstable and decohere. This is consistent with einselection
but provides a specific dynamical mechanism (phase locking) for why certain
states survive.

### 10.4 Superdeterminism

Superdeterminism [Bell 1976, 't Hooft 2016] escapes Bell's theorem by denying
measurement independence: the hidden variable λ and the detector settings (a, b)
are correlated because they share a common causal past. If ρ(λ|a,b) ≠ ρ(λ),
Bell's derivation does not go through, and local hidden variable models can
reproduce quantum correlations.

This comparison is important because an earlier version of this work [Olddog 2025,
Paper 1] explicitly invoked the measurement-independence loophole through the
gravitational bulk phase Φ_bulk — arguing that since both detectors and the
particle source share a common gravitational field, their states are
correlated. That claim has been withdrawn in the present paper.

**Why this framework is not superdeterministic:**

1. **We do not challenge Bell's theorem.** The quantum correlations
   E(a,b) = −cos(a−b) are accepted as arising from the entangled singlet state
   and the full Dirac spinor structure — standard quantum mechanics. No hidden
   variable model is proposed to replace them.

2. **Measurement independence is preserved.** The experimenter's choice of
   detector angle is not constrained by the framework. The gravitational bulk
   phase Φ_bulk maintains detector coherence (Section 4.4) but does not
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
   settings will be chosen in a 2015 Bell test. This framework requires only
   that macroscopic detectors are phase-coherent objects immersed in a
   gravitational field — a physically uncontroversial claim.

The distinction can be stated concisely: superdeterminism says the correlations
are classical but hidden in the initial conditions. This framework says the
correlations are quantum, and the Kuramoto mechanism explains how they are
*revealed* (measurement) and *degraded* (decoherence), not how they are
*produced*.

---

## 12. Discussion

### 11.1 The Interpretive Status

This paper presents a mathematical identification (Dirac = Kuramoto) and an
interpretive framework built on it (measurement = re-synchronization). The
mathematical identification is verifiable and, we believe, novel. The
interpretive framework is physically motivated but not yet quantitatively
predictive beyond standard decoherence.

We are in the category of interpretation papers — alongside many-worlds,
Bohmian mechanics, and relational QM. The contribution is not new equations
but a new way of reading existing equations that provides physical intuition
for the measurement process.

### 11.2 The Historical Note

The timeline is suggestive:

- 1928: Dirac equation (the two-clock structure)
- 1935: EPR paper ("spooky action at a distance")
- 1964: Bell's theorem
- 1975: Kuramoto model

The relativistic spinor structure that produces the full quantum correlation
existed 36 years before Bell showed it was needed. The synchronization framework
that describes the coupling existed 11 years after Bell. The identification
presented here connects these threads.

### 11.3 Future Directions

Three directions could elevate this from interpretation to testable theory:

1. **Quantitative decoherence rates.** Derive decoherence timescales from
   Kuramoto parameters in a many-body quantum setting. If these reproduce known
   rates for specific systems (e.g., superconducting qubits, trapped ions), the
   framework gains predictive power. If they differ, the framework makes testable
   predictions.

2. **Born rule — rigorous proof.** Section 6 argues that P = |α|² follows from
   Kuramoto synchronization statistics: the squared modulus of the complex
   coupling amplitude determines synchronization probability, and averaging over
   the detector bulk phase eliminates cross terms. A rigorous derivation would
   formalize this in a many-body quantum Kuramoto setting and prove that no
   other probability measure is consistent with the synchronization dynamics.

3. **Photon coupling.** Resolving the open question of Section 9 — what plays
   the role of K for massless particles — would either extend the framework to
   all of quantum mechanics or identify its boundary of applicability.

---

## 13. Conclusions

We have shown that:

1. **The Dirac mass term has Kuramoto synchronization structure.** In the Weyl
   basis, the Dirac equation couples ψ_L and ψ_R with coupling constant K = m.
   The Higgs-Yukawa interaction sets K = y_f · ⟨φ⟩ = m exactly.

2. **The NR phase-clock deficiency is traceable.** Retaining only the large
   (temporal) Dirac component gives E(a,b) = −½cos(a−b). The full four-spinor,
   with mass coupling K = m ensuring both clocks contribute, restores the exact
   quantum result through E = E_LL + E_SS + E_LS.

3. **Measurement is re-synchronization.** A particle decoheres from its
   entangled partner by cohering with the detector bulk. The Kuramoto mass
   asymmetry (M >> m) ensures definite outcomes. Decoherence is not merely loss
   of coherence — it is redirection of coherence.

4. **The Born rule follows from synchronization statistics.** The probability
   P = |α|² is the squared modulus of the complex coupling amplitude between
   particle and detector oscillators. The phase averages out; the amplitude
   squared remains. This is the natural probability measure for any physical
   wave coupling to a resonant absorber.

5. **Zitterbewegung is the beat frequency** between temporal and spatial phase
   clocks, at ω = 2mc²/ℏ.

6. **A single-world energy accounting is possible.** Residual wavefunction
   amplitude thermalizes into the vacuum rather than branching or vanishing.

The framework does not modify quantum mechanics or challenge Bell's theorem. It
provides a physical mechanism — Kuramoto phase synchronization — for processes
(decoherence, measurement, mass generation) that standard quantum mechanics
describes but does not mechanistically explain.

**In short: quantum mechanics produces the correlations. The Dirac mass term is
the Kuramoto coupling that makes particles what they are. And measurement is the
moment a small oscillator surrenders its phase to a large one.**

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

[9] Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox. *Physics*, 1(3),
195–200.

[10] Gerritsma, R., et al. (2010). Quantum simulation of the Dirac equation.
*Nature*, 463(7277), 68–71.

[11] ATLAS Collaboration (2012). Observation of a new particle in the search for
the Standard Model Higgs boson. *Phys. Lett. B*, 716(1), 1–29.

[12] CMS Collaboration (2012). Observation of a new boson at a mass of 125 GeV.
*Phys. Lett. B*, 716(1), 30–61.

[13] de Broglie, L. (1925). Recherches sur la théorie des quanta. *Ann. Phys.*,
3, 22–128.

[14] Aspect, A., Grangier, P., & Roger, G. (1982). Experimental Realization of
EPR-Bohm Gedankenexperiment. *Phys. Rev. Lett.*, 49(2), 91–94.

[15] Bohm, D. (1952). A Suggested Interpretation of the Quantum Theory in Terms
of "Hidden" Variables. *Phys. Rev.*, 85(2), 166–193.

[16] Everett, H. (1957). "Relative State" Formulation of Quantum Mechanics.
*Rev. Mod. Phys.*, 29(3), 454–462.

[17] Peskin, M. E., & Schroeder, D. V. (1995). *An Introduction to Quantum Field
Theory*. Westview Press.

[18] Sakurai, J. J. (1967). *Advanced Quantum Mechanics*. Addison-Wesley.

[19] 't Hooft, G. (2016). *The Cellular Automaton Interpretation of Quantum
Mechanics*. Springer.

[20] Bell, J. S. (1976). The theory of local beables. *Epistemological Letters*,
9, 11–24. [Reprinted in *Speakable and Unspeakable in Quantum Mechanics*, CUP.]

---

*Simulation code and numerical verification available at:
github.com/rayolddog/BellWithoutFasterThanLight*

*The three-term decomposition (Section 3) can be reproduced by running
`dirac_extension.py`. The Kuramoto phase dynamics (Section 2) are demonstrated
in `higgs_clock.py` and `kuramoto_sync.py`.*
