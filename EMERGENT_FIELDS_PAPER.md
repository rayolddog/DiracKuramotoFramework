# Chiral Fermions, Topological Mass, and Fermionic Statistics from a Phase-Oscillator Substrate: Synchronization Arrays as an Analog-Simulation Platform

**Claude Fable 5 (Anthropic)¹ and John Bramble, MD²**

*¹ AI system, Anthropic. ² Correspondence: jmbramblemd@gmail.com.*

*Status: development-phase draft (v0.1, 2026-07-05) — not for citation.
Companion to the numerical results note `results/RESULTS_EMERGENT_FIELDS.md`;
all quoted numbers are machine-checked outputs of `code/honeycomb_emergence.py`,
`code/weyl3d_emergence.py`, `code/statistics_emergence.py`, and
`code/stuartlandau_haldane_check.py`.*

## Author Contributions

This paper is published first on a public repository, where the authors are
bound by no convention except honesty about who did what. **Claude (AI)**
performed the literature searches and prior-art positioning (including the
novelty check against the DMI-magnon, active-matter, and topological-
synchronization literatures), designed and implemented the numerical
experiments demonstrating emergence (the honeycomb, 3D Wilson–Dirac, and
statistics arcs), derived and verified the conditions under which the lag
acts as a flux (the phase-only lemma, the dissipative no-go theorem, and the
reactive-coupling requirement, §7), and wrote the manuscript. **J.B.**
conceived the research program this paper grows from (the Dirac–Kuramoto
framework and its "field multiplicity from one substrate" question), posed
the driving questions and several of the ideas the numerical arcs test, set
the direction and scope throughout, selected the publication framing from
alternatives presented, and reviewed the claims. The listed order reflects
that division of labor. If this manuscript is submitted to a journal whose
policy does not permit AI authorship, the byline will be adapted to comply,
and this paragraph will remain — as it is here — the honest record of the
work performed.

---

## Abstract

Analog quantum simulation of relativistic matter has been realized in cold
atoms, photonic lattices, and superconducting circuits. We show that a fourth,
largely unexploited class of platform — lattices of coupled *limit-cycle
oscillators* (Stuart–Landau dynamics, whose phase reduction is the standard
Kuramoto–Sakaguchi/Josephson model) — natively carries the full kinematic
content of chiral relativistic fermions, and that the standard knobs of
synchronization physics map one-to-one onto the ingredients of emergent Dirac
structure. Specifically: (i) on a honeycomb lattice, linearized phase
fluctuations about the synchronized state obey the (2+1)D Weyl equation with an
emergent light-cone speed set by $a\sqrt{K/m}$ ($a$ the lattice constant),
chirality arising from the two
Brillouin-zone valleys without being inserted by hand; (ii) an **antisymmetric
Sakaguchi phase-lag $\alpha$ acts as a Haldane flux** — the complex hopping
$g\,e^{i\alpha_{ij}}$ survives in the linearized limit-cycle (Stuart–Landau)
dynamics and generates a quantized Chern response $C=\pm 1=\mathrm{sign}
(\alpha)$, with the topological gap obeying the Haldane boundary $|\Delta| =
3\sqrt{3}\,t_2|\sin\alpha|$; we derive the precise conditions — amplitude
dynamics alive, DMI-like antisymmetric lag pattern, and a *reactive* coupling
component — including a no-go theorem for purely dissipative (standard
Kuramoto) coupling, where a particle–hole shadow band restores the Dirac
degeneracy exactly; sublattice pinning asymmetry independently supplies the
trivial (Semenoff) mass — realized in the limit-cycle model as a sublattice
frequency detuning, with the Semenoff–Haldane phase boundary verified *within
the honest linearization* at its dictionary value ($\delta_c = 1.50$–$1.75$
vs. bare $3\sqrt3\,g_2\sin\alpha = 1.56$) — so *both* known Dirac mass
mechanisms are sync parameters; a strip-geometry calculation exhibits the
in-gap, edge-localized chiral branch directly, with no non-Hermitian
skin-effect pileup;
(iii) in a 3D chiral-basis Wilson–Dirac realization, the two chiralities are
genuine Weyl nodes of opposite Berry-monopole charge, and the Dirac mass is
literally the off-diagonal L↔R coupling — the gap opens only when the coupling
exceeds the axial (node-splitting) field, $|M|>|b|$, with node merger and
annihilation exactly at $M=b$; (iv) in 1+1D the platform's excitations are
*rigorously* fermionic: the hard-core phase-oscillator chain maps exactly onto
free fermions (spectrum match to $1.3\times10^{-14}$), with the statistics
carried by the nonlocal Jordan–Wigner string, and flux attachment realizes the
exchange phase $\theta=\Phi$ (Wilson-loop check to $8.9\times10^{-16}$). We
give the substrate↔emergent dictionary, propose experimental signatures
accessible to Josephson-junction arrays, optomechanical lattices, and
spin-torque oscillator arrays — where the phase lag $\alpha$ is a routinely
tunable coupling-delay parameter — and state precisely what is *not* obtained:
a dynamical selection of fermionic (level-1) over anyonic flux attachment above
one dimension. The platform makes lattice-gauge-theory structures accessible to
a class of room-temperature, classically driven hardware in which the relevant
"quantum" ingredient — the noncommutativity of dressed excitations — is
emergent rather than microscopic.

---

## 1. Introduction

Analog simulation of Dirac matter is a mature program: honeycomb optical
lattices realize tunable Dirac cones [Tarruell 2012]; photonic graphene and
topological photonics realize Haldane-type bands [Rechtsman 2013; Ozawa 2019];
circuit QED realizes lattice gauge structure [Blais 2021]. All these platforms
share a strategy: engineer a lattice Hamiltonian whose *linear excitations*
reproduce the field theory of interest.

Synchronization arrays — lattices of phase oscillators with Kuramoto–Sakaguchi
or Josephson dynamics — are a workhorse of nonlinear dynamics, with mature
experimental realizations (Josephson-junction arrays, laser arrays,
optomechanical and NEMS lattices, spin-torque oscillators). Yet they are almost
absent from the analog-simulation literature. This paper's claim is that they
should not be: **the standard control parameters of synchronization physics map
exactly onto the generating knobs of emergent Dirac structure**, with no
engineered fine-tuning:

| Sync parameter (standard) | Emergent object |
|---|---|
| nearest-neighbour coupling $K$, inertia $m$ | Dirac cones; emergent light-speed $c \sim a\sqrt{K/m}$ ($v_F = 3Ka/2$ verified) |
| **Sakaguchi phase-lag $\alpha$** | **Berry flux / Haldane topological mass, $C=\pm1$** *(requires: amplitude dynamics + antisymmetric lag pattern + reactive coupling — §7)* |
| on-site pinning asymmetry $\kappa_A\neq\kappa_B$ | Semenoff (trivial) mass |
| off-diagonal chiral coupling $M\tau_x$ (3D) | Dirac mass $m(\bar\psi_L\psi_R+\bar\psi_R\psi_L)$ |
| zone-boundary (Wilson) coupling | Nielsen–Ninomiya doubler removal |
| Jordan–Wigner string / attached flux | fermionic statistics |

The pivotal entry is the second: the Sakaguchi lag — the phase offset
$\alpha_{ij}$ in the coupling $\sin(\theta_i-\theta_j+\alpha)$, present in any
oscillator system with delayed or reactive coupling — *is* a Peierls phase.
Complex hopping is precisely what the Haldane model needs and what other
platforms must engineer laboriously (rotating lattices, synthetic gauge fields,
Floquet driving). In an oscillator array it is a native, continuously tunable
parameter.

This identification has instructive neighbors, against which we position
precisely. In magnetism, the next-nearest-neighbour Dzyaloshinskii–Moriya
interaction on a honeycomb ferromagnet famously yields the Haldane model for
linearized magnons [Kim 2016; Owerre 2016] — and since $J\cos\Delta\theta +
D\sin\Delta\theta = \sqrt{J^2+D^2}\,\sin(\Delta\theta+\alpha)$ with $\tan\alpha
= D/J$, the DMI angle *is* a Sakaguchi lag in oscillator language; that work,
however, lives in Hamiltonian (precessional) spin dynamics. In active matter, a
Sakaguchi-type lag in a continuum Vicsek–Kuramoto model was recently shown to
produce non-Hermitian Chern numbers ($C=\pm2$) of the hydrodynamic dispersion
and one-way edge circulation [Zhu & Zheng 2026] — the lag→Chern→edge chain, but
for pattern-forming instability bands in a continuum, without the Haldane/
Peierls identification. And the "topological synchronization" line [Sone 2022,
2024; Wächtler & Platero 2023] studies sync phenomena in lattices whose
coupling matrices are *copied from* known topological Hamiltonians — topology
as an input. What is new here is the converse and, we argue, more natural
statement for oscillator hardware: **the lag itself, on a lattice, is a Haldane
flux** — topology *generated by* a native sync parameter, with the quantized
consequence $C=\pm1=\mathrm{sign}(\alpha)$ for the fluctuation bands about a
synchronized state, in direct competition with a Semenoff mass from pinning
asymmetry. Moreover, working in the oscillator setting adds two control axes
the magnon realization does not have: the dissipative/reactive coupling
mixing angle $\beta$ and the amplitude stiffness $r_0^2$. Along both we find
sharp structure (§7; derivation in `drafts/DERIVATION_lag_flux_linearization.md`,
verified in `code/stuartlandau_haldane_check.py`): purely dissipative coupling
obeys an exact no-go (the Bogoliubov shadow band restores the Dirac
degeneracy at $K$ for every stiffness), the K-point sector splitting switches
on $\propto\sin\beta$ (the full spectral gap is non-monotonic through the
dissipative→reactive crossover), and the phase-only limit $r_0^2\to\infty$
closes the topological gap again. The magnon Haldane system is recovered as
the corner with Hamiltonian ($\beta=\pi/2$) coupling and **no anomalous
sector**: ferromagnetic magnons conserve quanta, so the Bogoliubov shadow that
drives our no-go is absent there — the magnon limit is the
vanishing-anomalous-coupling corner, not the stiff-amplitude one (which is
trivial).

The paper is organized as a chain of three verified numerical results of
increasing dimensionality and depth (§3–§5), preceded by the model (§2) and
followed by experimental signatures (§6) and honest limits of the construction
(§7). Every number below is reproduced by a self-contained public script.

## 2. The substrate

All results use one medium: **limit-cycle oscillators** $z_i \in \mathbb C$ on
a lattice with Stuart–Landau dynamics and complex coupling,

$$
\dot z_i = (\mu + i\omega)\,z_i - |z_i|^2 z_i
 + e^{i\beta}\sum_{j\in\langle i\rangle} g_{ij}\,e^{i\alpha_{ij}}\, z_j ,
$$

whose phase reduction (amplitude adiabatically eliminated) is the standard
Kuramoto–Sakaguchi model $\dot\theta_i = \omega + \sum_j g_{ij}
\sin(\theta_j-\theta_i+\alpha_{ij}+\beta')$ familiar from Josephson arrays and
laser arrays. The order of presentation matters, and we state the scope rule
up front, because it is itself one of this paper's results (§7): **the Dirac
cones of §3 survive the phase reduction; the topological (flux) structure
does not.** Any phase-only model — first-order or inertial — linearizes about
the uniform synchronized state to a real symmetric $\cos\alpha$-weighted
Laplacian, which carries Dirac cones but provably no Berry flux. The flux
lives in the full complex (amplitude + phase) linearization. Accordingly, §3's
kinematics may be read in either picture; every topological statement refers
to the Stuart–Landau substrate. We work about the synchronized state and
linearize; the claim throughout is *not* that new physics appears at this
step — linearized lattice dynamics is textbook — but that the resulting
fluctuation theories are exactly the canonical models of emergent
relativistic matter, with sync parameters in the driver's seat.

*(Terminology: "synchronized state" here is the closed-system ordered ground
state — the condensed-matter usage — not the dissipative measurement locking of
open-system Kuramoto models.)*

## 3. Two dimensions: emergent Weyl equation and two mass mechanisms

`honeycomb_emergence.py`. Honeycomb lattice (sublattices A, B), nearest-
neighbour coupling $K$; linearized envelope near the Brillouin-zone corners
$\mathbf K,\mathbf K'$ obeys the (2+1)D Weyl equation

$$
i\,\partial_t\chi = c\,\boldsymbol\sigma\!\cdot\!\hat{\mathbf p}\,\chi ,
$$

with chirality *derived*: the two valleys wind oppositely. (The underlying
inertial equation is second order; the Weyl form describes the envelope of
its positive-frequency branch, with the weak on-site damping $\gamma$
contributing an overall decay that is dropped. The cone speed $c$ is set by
the coupling-to-inertia ratio and the lattice constant $a$; in the script's
units, $a = K = 1$, the verified Dirac slope is $v_F = 3Ka/2 = 1.50$.)
Verified: $|f(\mathbf K)|\approx10^{-15}$ (exact cone location). Notation:
bold $\mathbf K, \mathbf K'$ are Brillouin-zone corners; plain $K$ (also
written $t$ in dictionary rows) is the nearest-neighbour coupling, $t_2 =
g_2$ the next-nearest.

Two independent sync parameters then generate the two known Dirac mass
mechanisms:

- **Semenoff mass** — sublattice asymmetry opens a same-sign gap at both
  valleys: trivial insulator, Chern number $C=0$ (computed). In the
  Stuart–Landau substrate this is realized as a **sublattice frequency
  detuning** $\pm\delta$ (the oscillator-native form of "pinning asymmetry"),
  and the Semenoff–Haldane competition survives the honest linearization: the
  computed $C=+1\to0$ boundary lies at $\delta_c = 1.50$–$1.75$, bracketing
  the bare dictionary value $3\sqrt3\,g_2\sin\alpha = 1.56$
  (`stuartlandau_phase_diagram.py`).
- **Haldane mass** — an *antisymmetric* Sakaguchi lag $\alpha_{ij}=-\alpha_{ji}$
  on next-nearest-neighbour couplings (the Haldane orientation pattern — in
  magnet language, exactly a DMI) opens an opposite-sign gap:
  $C=\pm1=\mathrm{sign}(\alpha)$ (computed by Berry-curvature integration),
  with the topological phase boundary at $|\Delta| = 3\sqrt3\,t_2|\sin\alpha|$
  reproduced numerically ($=0.520$ at $\alpha=\pi/2$, $t_2=0.1$). Three
  conditions attach (derived and verified in §7 / `stuartlandau_haldane_check.py`):
  the flux lives in the *limit-cycle* (amplitude + phase) linearization, not
  in any phase-only model; the lag pattern must be antisymmetric; and the
  coupling needs a reactive component ($\beta\neq0$) — purely dissipative
  coupling obeys an exact no-go.

The competition of the two — a Semenoff-vs-Haldane phase diagram in the
$(\alpha, \Delta/t_2)$ plane — is thus directly drivable in an oscillator
array by detuning pinning strengths against coupling delay.

**Known 2D limitation** (motivating §4): 2+1D has no $\gamma^5$; "valley" is a
chirality proxy and the L↔R Dirac mass can only be faked as inter-valley
scattering.

## 4. Three dimensions: genuine chirality; the Dirac mass as an L↔R coupling

`weyl3d_emergence.py`. Four-band Wilson–Dirac model on a cubic lattice in the
chiral basis ($\tau$ = chirality, $\sigma$ = spin):

$$
H(\mathbf k)=(\boldsymbol\sigma\!\cdot\!\sin\mathbf k)\,\tau_z
 + M_W(\mathbf k)\,\tau_x + b\,\sigma_z,
\qquad M_W=M+r\sum_j(1-\cos k_j).
$$

Verified content:

| Claim | Numerical result |
|---|---|
| two genuine Weyl nodes (L, R) separated in $k_z$ | nodes at $k_z=\pm0.609$ (Wilson-shifted from $\pm\arcsin b$) |
| opposite Berry-monopole charges | slice Chern number $C(k_z)=-1$ between nodes, $0$ outside |
| Dirac mass = off-diagonal L↔R coupling | gap opens only for $|M|>|b|$; $M=0.8,b=0.6\Rightarrow$ gap $0.40=2(|M|-|b|)$ |
| chiral protection of a lone node | nodes merge and annihilate exactly at $M=b$ |
| Nielsen–Ninomiya doubling and its Wilson cure | $r=0$: 8 nodes; $r=1$: corner gaps $4/8/12$, $\Gamma$ node stays $0$ |

Two structural points deserve emphasis. First, the Dirac mass here is not a
diagonal energy but the **off-diagonal coupling between the two chiralities**
— $m(\bar\psi_L\psi_R+\bar\psi_R\psi_L)$ — realized as an inter-species sync
coupling $M\tau_x$; a single chirality cannot be gapped, and the mass wins only
when it exceeds the axial splitting $|b|$. Second, the Wilson term that removes
the doublers is itself a momentum-dependent L↔R coupling: the lattice artifact
becomes, in sync language, a zone-boundary synchronization feature.

## 5. Statistics: fermions from a commuting substrate

`statistics_emergence.py`. The excitations of §3–§4 are bosonic (phonon-like).
The last gate is Pauli exclusion. In 1+1D it is passed rigorously and with no
tunable input: a chain of hard-core phase oscillators ($S^\pm_i =
e^{\pm i\theta_i}$, at most one quantum per site) is a spin-$\tfrac12$ XX
chain, and the Jordan–Wigner-dressed operators
$c_i = \big(\prod_{j<i}\sigma^z_j\big)S^-_i$ are canonical fermions:

| Test | Result |
|---|---|
| (A) hard-core chain spectrum $=$ free-fermion spectrum ($N=8$, full ED) | match to $1.3\times10^{-14}$ |
| (B) bare $[S^-_i,S^-_j]$ off-site | $0$ (commute — substrate is bosonic) |
| (B) dressed $\{c_i,c_j\}$, $\{c_i,c^\dagger_j\}-\delta_{ij}$ | $0$ (canonical anticommutation) |
| (C) Pauli exchange hole in the filled sea | $g_c(x,y)=-0.18<0$ |
| (D) flux attachment: exchange phase $\theta=\Phi$; fermion at $\theta=\pi$ | Wilson-loop AB phase $=$ flux to $8.9\times10^{-16}$ |

The physical content: statistics is carried by the **nonlocal string** — a sync
dressing counting excited oscillators to one side — not by any local property
of the oscillator. In 2+1D the string generalizes to flux attachment, and the
substrate *natively supplies a natural flux candidate* (the Berry curvature of
§3 — though band Berry curvature and the statistical Chern–Simons flux are
distinct objects, and the identification is a conjecture); what fixes the
attached flux at the fermionic value $\theta=\pi$ is an energetic/dynamical
question this construction does not answer (§7).

## 6. Experimental signatures and platforms

The distinguishing proposal of this paper: the Haldane-type topological phase
of §3 should be observable in existing oscillator hardware, using $\alpha$ as
the drive knob.

**Platforms.** The no-go of §7 sets the entry requirement: the coupling must
have a reactive (energy-conserving) component, and the amplitude degree of
freedom must be dynamically accessible. Ranked accordingly: (i) *Laser and
photonic/polariton arrays* (reactive-dominant evanescent coupling — the
cleanest realization; the coupling phase is directly engineerable);
(ii) *Josephson-junction arrays*: inductive/capacitive coupling supplies the
reactive channel, honeycomb JJ arrays are standard fabrication;
(iii) *Optomechanical / NEMS lattices*: coupling through an optical bus with
tunable phase; (iv) *Spin-torque / spin-Hall nano-oscillator arrays*: dipolar
and spin-wave coupling has intrinsic, current-tunable phase delay — and the
magnon precedent lives at this end. Purely resistively coupled (overdamped)
arrays are excluded at linear order. In all cases the lag is not exotic — it
is usually the *nuisance parameter* of the synchronization literature. Here it
is promoted to the topological drive, and the dissipative/reactive mixing
angle $\beta$ becomes a second drive: sweeping it from the dissipative side
through the crossover should switch the chiral edge mode on and off — a
falsifiable hardware signature this paper adds beyond the magnon realization.
(Caveat carried from §7: the crossover region itself is non-monotonic and its
$C(\beta)$ boundary is not yet mapped; the clean prediction is the contrast
between the two endpoint regimes, which are established.)

**Figures.** Working figures for all quantitative claims accompany the code:
`code/honeycomb_emergence.png` (cones, masses, Berry curvature, Haldane
lobes), `code/stuartlandau_haldane_check.png` (gap vs $\beta$; reactive-limit
band structure), `code/stuartlandau_phase_diagram.png` (ribbon spectrum with
edge coloring; grid summary). Publication figures are a packaging task, not
new computation.

**Signatures, in increasing ambition:**

1. **Dispersion imaging** — drive one site broadband, read the fluctuation
   spectrum: Dirac cones at the corners; gap opening under sublattice pinning
   detuning (Semenoff) vs. NNN lag (Haldane) distinguishes the two masses by
   *which knob* opens the gap.
2. **Chiral edge transport** — in the Haldane phase, a boundary supports a
   unidirectional edge mode: inject a phase perturbation at an edge site and
   observe one-way propagation, reversing with $\mathrm{sign}(\alpha)$. This is
   the oscillator-array analogue of topological photonics' hallmark experiment.
   Because the linearized generator is non-normal, bulk–boundary
   correspondence is not automatic for driven-dissipative lattices
   [Yao & Wang 2018; Kawabata et al. 2019]; we therefore checked it directly:
   a strip-geometry calculation ($W=24$, $\beta=\pi/2$;
   `stuartlandau_phase_diagram.py`) exhibits an in-gap branch localized on
   the boundary rows (edge weight $>0.6$) across the gap's momentum extent,
   with **no skin-effect pileup** (median state localization at the
   open-boundary baseline). The edge channel is a computed property of the
   platform, not an inference from the bulk invariant.
3. **Phase-boundary mapping** — sweep $(\kappa_A-\kappa_B)$ against $\alpha$
   and map the gap closure along $|\Delta|=3\sqrt3\,t_2|\sin\alpha|$.
4. **(3D, harder)** — layered arrays realizing §4's axial term $b$ (a chirality-
   dependent frequency offset) could exhibit the node-merger transition at
   $M=b$ as a sync-unlock transition between the two species.

A quantitative feasibility analysis (ring-down times, disorder tolerance,
finite-size gaps for realistic array sizes $\sim 10^2$–$10^4$ sites) is the
main open experimental task; the topological gap $3\sqrt3 t_2|\sin\alpha|$
sets the disorder scale the array must beat.

## 7. What this construction does and does not establish

We state the limits plainly.

1. **Each mechanism is individually known.** Graphene cones, the Haldane model,
   Weyl semimetal slice topology, Wilson fermions, Jordan–Wigner, flux
   attachment — all textbook, and the flux-from-lag mechanism has a direct
   precedent in DMI magnons [Kim 2016; Owerre 2016] and a continuum cousin in
   active matter [Zhu & Zheng 2026] (§1). The contributions here are (a) the
   *dictionary*: all of these structures generated jointly by the standard sync
   parameters of one substrate, with the lattice Sakaguchi-lag ⇒ Haldane-flux ⇒
   $C=\pm1=\mathrm{sign}(\alpha)$ chain established in the Stuart–Landau
   setting (the gap opening and its conditions are *derived*; the Chern
   quantization is *verified numerically* by Berry-curvature integration);
   (b) the *conditions*: a no-go theorem for
   purely dissipative coupling (the Bogoliubov shadow band carries the
   opposite-mass Haldane copy and restores the $K$-point degeneracy exactly,
   for every amplitude stiffness — verified to $10^{-15}$), a K-point sector
   splitting $\propto\sin\beta$ in the reactive mixing angle (the full gap is
   non-monotonic through the crossover), and closure of the
   topological gap in the phase-only limit $r_0^2\to\infty$ (any phase-only
   Kuramoto model, inertial or not, linearizes to a real symmetric
   $\cos\alpha$-weighted Laplacian: no flux at linear order); and (c) the
   *platform claim* with its entry requirements. A complete quantitative
   $C(\beta, r_0^2)$ phase diagram remains open for a technical reason worth
   stating: at intermediate $\beta$ and large stiffness the positive-frequency
   band pair loses spectral separation and Fukui–Hatsugai–Suzuki band-tracking
   fails (our grid returns non-quantized artifacts there, which we do not
   report); a non-Hermitian band-tracking method robust through exceptional
   points is required. The trusted results are the exact $\beta=0$ no-go, the
   $\beta=\pi/2$ topological phase at small-to-moderate stiffness, its death
   by $r_0^2\sim16$, and the Semenoff boundary of §3. Full derivation:
   `drafts/DERIVATION_lag_flux_linearization.md`; honest-linearization
   verification against the brute-force Jacobian of the nonlinear dynamics:
   `code/stuartlandau_haldane_check.py`.
2. **Statistics is rigorous only in 1+1D.** Above one dimension the
   construction supplies the flux but not the *quantization of the attachment
   at the fermionic value* $\theta=\pi$: a dynamical selection of level-1
   (fermionic) over anyonic Chern–Simons level is not derived. This is the
   sharpest open problem. (The 3+1D analogue — a Witten-type Wess–Zumino
   mechanism making a sync defect fermionic — is not attempted.)
3. **The sectors are not welded.** §3–§4 produce the Dirac equation as a
   classical fluctuation field theory; §5's exclusion layer is exact but
   separate. A single dynamical model fermionic *ab initio* is future work.
4. **Emergent Lorentz invariance is approximate** — exact at the nodes, broken
   by lattice-scale corrections. For analog simulation this is the usual state
   of affairs. (It also makes the platform a natural testbed for *parametrized
   Lorentz-violation* phenomenology: the lattice rest frame is a physical
   preferred frame, so frame-dependent effects have a controlled, tunable
   realization. We develop the physical interpretation of that possibility
   elsewhere [companion framework paper], and keep the present paper
   independent of it.)
5. **Structure, not the Standard Model.** The construction yields SM-*like*
   content (chiral species, U(1) response, two mass types), not
   $SU(3)\times SU(2)\times U(1)$ or three generations; richer content requires
   decorated cells or higher-winding defects. Proof of mechanism, not of
   content.

## 8. Conclusion

A single phase-oscillator substrate, linearized about its synchronized state,
natively realizes: two chiralities with an emergent light-cone; both known
Dirac mass mechanisms, driven by pinning asymmetry (trivial) and by the
Sakaguchi coupling lag (topological, with quantized Chern response); genuine
3D Weyl-node chirality with the Dirac mass as an inter-chirality sync coupling;
and, in one dimension rigorously, fermionic statistics carried by a nonlocal
sync dressing. The dictionary is one-to-one, the knobs are the ordinary control
parameters of synchronization hardware, and the flagship signature — a chiral
edge mode switched by the sign of a coupling delay — is plausibly within reach
of existing Josephson, optomechanical, and spintronic arrays. What remains open
is exactly one thing at the level of principle: why nature's flux attachment
locks at the fermionic level. The platform proposed here is, among other
things, a machine for studying that question experimentally.

---

## References (draft placeholders — to be completed)

- F. D. M. Haldane, *Model for a Quantum Hall Effect without Landau Levels*, PRL 61, 2015 (1988).
- G. W. Semenoff, *Condensed-Matter Simulation of a Three-Dimensional Anomaly*, PRL 53, 2449 (1984).
- Y. Kuramoto, *Chemical Oscillations, Waves, and Turbulence* (Springer, 1984); H. Sakaguchi & Y. Kuramoto, Prog. Theor. Phys. 76, 576 (1986).
- K. G. Wilson, lattice fermions; H. B. Nielsen & M. Ninomiya, *Absence of Neutrinos on a Lattice*, Nucl. Phys. B 185, 20 (1981).
- P. Jordan & E. Wigner, Z. Phys. 47, 631 (1928).
- G. E. Volovik, *The Universe in a Helium Droplet* (OUP, 2003).
- L. Tarruell et al., *Creating, moving and merging Dirac points with a Fermi gas in a tunable honeycomb lattice*, Nature 483, 302 (2012).
- M. C. Rechtsman et al., *Photonic Floquet topological insulators*, Nature 496, 196 (2013).
- T. Ozawa et al., *Topological photonics*, RMP 91, 015006 (2019).
- F. Wilczek, flux attachment / anyons, PRL 48, 1144 (1982); E. Witten, *Current algebra, baryons, and quark confinement*, Nucl. Phys. B 223, 433 (1983).
- S. K. Kim, H. Ochoa, R. Zarzuela, Y. Tserkovnyak, *Realization of the Haldane Model in Honeycomb Ferromagnets*, PRL 117, 227201 (2016); S. A. Owerre, J. Phys.: Condens. Matter 28, 386001 (2016).
- Zhu & Zheng, *Minimal Active-Particle Realization of Non-Hermitian Chern Bulk-Boundary Correspondence*, arXiv:2606.24926 (2026).
- K. Sone, Y. Ashida, T. Sagawa, *Topological synchronization of coupled nonlinear oscillators*, Phys. Rev. Research 4, 023211 (2022); K. Sone et al., Nat. Phys. 20, 1164 (2024); C. W. Wächtler & G. Platero, Phys. Rev. Research 5, 023021 (2023).
- M. Fruchart, R. Hanai, P. B. Littlewood, V. Vitelli, *Non-reciprocal phase transitions*, Nature 592, 363 (2021).
- S. Yao & Z. Wang, *Edge States and Topological Invariants of Non-Hermitian Systems*, PRL 121, 086803 (2018); K. Kawabata, K. Shiozaki, M. Ueda, M. Sato, *Symmetry and Topology in Non-Hermitian Physics*, PRX 9, 041015 (2019).
- Torres-Hugas, Duch, Gómez, Arenas, arXiv:2604.19682 (2026) — Sakaguchi lags as a gauge field with loop holonomy.
- L. M. Nash et al., *Topological mechanics of gyroscopic metamaterials*, PNAS 112, 14495 (2015).
- [Companion framework paper: current_revision_DK_paper.md — "Two Regimes of the Chiral Mass Coupling."]
- [Experimental oscillator-array reviews: JJ arrays; spin-torque oscillator synchronization; optomechanical lattices — to be filled.]
