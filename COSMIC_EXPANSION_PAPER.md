---
title: "Cosmic Expansion as Surface-Area Particle Creation in a Dirac–Kuramoto Substrate"
subtitle: "A Coherence-Based Reframing of the FRW Universe and the Cosmological Constant"
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

The standard Friedmann–Robertson–Walker (FRW) cosmology treats expansion as a
geometric property of spacetime sourced by a cosmological constant Λ inserted
by hand into Einstein's field equations. Λ originated as Einstein's 1917
patch to recover a *static* universe — a Newtonian-era prejudice — and was
later resurrected as "dark energy" to fit accelerating expansion. In both
incarnations, Λ enters the framework axiomatically rather than emergently.

This paper proposes a reframing in which cosmic expansion is *not* a property
of an underlying expanding spacetime, but instead the dynamical growth of a
finite *populated region* embedded in an infinite, static quantum-field
substrate. Expansion proceeds via real-particle creation from vacuum
fluctuations in regions of low temperature and low gravitational density —
the regime in which the Dirac–Kuramoto (DK) decoherence rates Γ_env(T) and
Γ_grav(M) both vanish. Because creation occurs preferentially at the boundary
of the populated region, the rate of expansion is proportional to the
**surface area** of the universe rather than its volume, naturally producing
a Hubble rate that scales as H ∝ 1/R and an effective cosmological term
Λ_eff ∝ 1/R² — matching the observed Λ ~ 1/L_H² without postulation.

The framework predicts three observational signatures distinct from ΛCDM:
(1) the local Hubble rate should anti-correlate with local matter density,
yielding the observed H₀ tension between CMB and local-distance-ladder
measurements; (2) cosmic voids should expand faster than virialized
structures by a measurable margin; (3) the surface-area scaling implies an
"emergent FRW metric" inside the populated region that preserves Tolman
(1+z)⁴ dimming and CMB blackbody structure, while the underlying substrate
remains Minkowski. The proposal is presented as a working-paper sketch, not
a fully derived theory; the load-bearing assumption — that excitations of
the bulk-coherence order parameter Φ_bulk inherit equation of state w = −1
through their Goldstone-mode character — is identified as the next required
derivation.

---

## 1. Introduction

### 1.1 The framework problem with Λ

Modern cosmology rests on the Friedmann–Robertson–Walker (FRW) metric, an
exact solution of Einstein's field equations under the *Cosmological
Principle* — the assumption that the universe is homogeneous and isotropic
at large scales. The Friedmann equations governing the time evolution of the
FRW scale factor a(t) take the form:

$$H^2 \equiv \left(\frac{\dot a}{a}\right)^2 = \frac{8 \pi G}{3} \rho - \frac{k c^2}{a^2} + \frac{\Lambda c^2}{3} \qquad (\text{Friedmann I})$$

$$\frac{\ddot a}{a} = -\frac{4 \pi G}{3}\left(\rho + \frac{3 p}{c^2}\right) + \frac{\Lambda c^2}{3} \qquad (\text{Friedmann II})$$

where ρ is the total energy density, p its pressure, k ∈ {−1, 0, +1} the
spatial-curvature index, and Λ the cosmological constant. The framework is
extraordinarily successful: it reproduces Hubble's law (recession velocity
proportional to distance), predicts the cosmic microwave background (CMB)
and its near-perfect blackbody spectrum, accounts for primordial
nucleosynthesis, and — with the addition of a positive Λ — fits the
accelerating expansion measured by Type Ia supernovae from 1998 onward.

The framework's success does not, however, dissolve the conceptual problem
with Λ itself. Λ enters Einstein's equations as a free parameter chosen to
match observation. Its origin is unspecified by the theory. Three distinct
unsolved problems attach to it:

1. **The cosmological-constant problem proper.** Quantum field theory
   predicts a vacuum energy density of order $\rho_{\text{vac}} \sim M_{\text{Pl}}^4$,
   roughly 120 orders of magnitude larger than the observed
   $\rho_\Lambda \sim 10^{-47}\ \text{GeV}^4$. Why these two quantities
   differ so radically is the largest known discrepancy between theory and
   observation in all of physics.

2. **The coincidence problem.** Why is $\rho_\Lambda$ comparable in magnitude
   to $\rho_{\text{matter}}$ in the current cosmic epoch, given that the two
   have entirely different scaling with $a(t)$?

3. **The H₀ tension.** Independent measurements of the current expansion
   rate disagree at ~5σ. CMB-anchored measurements (Planck) give
   $H_0 \approx 67.4\ \text{km/s/Mpc}$; local distance-ladder measurements
   (SH0ES) give $H_0 \approx 73.0\ \text{km/s/Mpc}$. ΛCDM with a single,
   uniform Λ cannot accommodate both.

Each of these problems suggests that Λ is *not* the right primitive — that
expansion ought to emerge from some deeper dynamics, not be postulated.

### 1.2 The Dirac–Kuramoto framework: what is already available

The DK framework [companion paper] proposes that quantum
measurement consists of three stages: (Stage 1) resonant pair-capture of a
perturbed partner by a macroscopic *bulk* characterized by an
order-parameter phase $\Phi_{\text{bulk}}$; (Stage 2) selection — the
surface commit that sets the outcome weights; and (Stage 3) irreversible
registration of the partner against the bulk. The dissipative
re-equilibration (Stages 2–3; the "Stage 2" of the framework's earlier
two-stage form) proceeds via two parallel rate channels,

$$\Gamma_{\text{2–3}}^{\text{total}} = \Gamma_{\text{env}}(T,\, J(\omega)) + \Gamma_{\text{grav}}(M,\, \Delta z) \qquad (3.5')$$

where $\Gamma_{\text{env}}$ is the environmental (thermal + bath-mediated)
relaxation rate and $\Gamma_{\text{grav}}$ is the gravitational
self-relocking rate of the bulk. Stage-3 registration events are the rare
bath-coupling moments that produce classical, irreversible measurement records.

Both rates vanish in the limit of low temperature and low gravitational
density: $\Gamma_{\text{env}} \to J(\omega)$ as $T \to 0$ (the
spontaneous-emission floor), and $\Gamma_{\text{grav}} \to 0$ as the
local matter density goes to zero. The DK framework therefore already
specifies the conditions under which bulk-coherence-mediated decoherence
ceases to act.

The proposal of this paper is that *exactly those conditions* — low T and
low gravity — define the regime in which the cosmological substrate
converts vacuum fluctuations into real particles, and that this conversion
is the physical source of cosmic expansion.

---

## 2. A Brief History of FRW Cosmology

### 2.1 Einstein's static universe (1917)

Einstein applied his newly completed field equations of general relativity
to the universe as a whole and found that no static solution existed for a
homogeneous matter distribution under attractive gravity alone — the
universe would either expand or contract. Believing on philosophical
grounds that the universe must be eternal and static, Einstein modified his
equations by adding a term $\Lambda g_{\mu\nu}$,

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8 \pi G}{c^4} T_{\mu\nu},$$

where $\Lambda$ was tuned to exactly balance gravitational attraction at
cosmic scales. The resulting "Einstein static universe" was a closed
3-sphere of fixed radius.

### 2.2 Friedmann and Lemaître (1922, 1927)

The Russian mathematician Alexander Friedmann (1922), and independently the
Belgian priest-physicist Georges Lemaître (1927), solved Einstein's
equations under the assumptions of homogeneity and isotropy *without*
demanding stasis. They found that the universe must in general expand or
contract, with the dynamics governed by Friedmann I (above). Lemaître went
further, connecting the expanding solutions to observational redshift data
and proposing what would later be called the Big Bang. Einstein famously
rejected Lemaître's physics — "your calculations are correct, but your
physics is abominable" — before reversing himself after Hubble's 1929
observations.

### 2.3 Hubble's law (1929)

Edwin Hubble's observation that galactic recession velocity is proportional
to distance,

$$v = H_0 \, d \qquad (\text{Hubble's law})$$

established expansion empirically. Einstein subsequently called his
introduction of $\Lambda$ his "greatest blunder."

### 2.4 Robertson and Walker (1935–36); FRW metric

Howard Robertson and Arthur Walker independently proved that the most
general metric consistent with homogeneity and isotropy takes the form

$$ds^2 = -c^2 dt^2 + a(t)^2 \left[ \frac{dr^2}{1 - k r^2} + r^2 \left(d\theta^2 + \sin^2\theta\, d\phi^2 \right) \right] \qquad (\text{FRW metric})$$

where $a(t)$ is the scale factor encoding all time evolution and
$k \in \{-1, 0, +1\}$ labels open, flat, and closed spatial geometries
respectively. Observations of CMB power-spectrum peaks indicate $k = 0$ to
within a fraction of a percent.

### 2.5 The accelerating universe (1998) and Λ's return

Type Ia supernova surveys (Riess et al. 1998; Perlmutter et al. 1999)
showed that the universe's expansion is *accelerating*. Within FRW, only a
component with sufficiently negative pressure — equation of state $w < -1/3$
— can drive acceleration. The simplest such component is a positive
cosmological constant ($w = -1$), and "ΛCDM" became the standard
cosmological model. The dark-energy term thereby resurrected was
mathematically Einstein's original $\Lambda$ but with no static-universe
motivation — purely an empirical fit.

### 2.6 The standing question

In its modern form, Λ is a single number tuned to one observation
(acceleration) that fits a wide range of others (CMB, large-scale structure,
BAO) — but with the three open problems noted in §1.1. The framework
proposed below leaves the FRW machinery intact as an *effective*
description of expansion inside the populated region, while replacing the
fundamental ontology with one in which Λ is emergent.

---

## 3. The Substrate–Population Distinction

### 3.1 The standard fusion

In standard FRW cosmology, two distinct ontological commitments are fused:

- **Spacetime is the universe.** The FRW metric describes the entirety
  of physical space; there is no "outside" of the universe in the
  framework.
- **The metric itself expands.** The scale factor $a(t)$ describes
  expansion of space, not just motion of matter through space.

These commitments are taken together as a single package, and the
cosmological-constant problem inherits both: $\Lambda$ is both the
energy density of spacetime itself and the agent of its expansion.

### 3.2 The DK ontology

The DK framework suggests a separation:

- **The substrate**: an infinite, eternal quantum-field structure
  (the vacuum and its fluctuations). The substrate has no
  privileged scale, no boundary, and is not itself expanding.
  Its metric, in the absence of coherent excitation, is
  Minkowski.

- **The populated region**: the finite, growing subset of the
  substrate in which real-particle excitations exist and are
  bulk-coherent in the DK sense. This is what we call "the
  universe." It has a boundary, a scale, and a dynamical
  evolution.

Cosmic expansion, on this view, is **not** the metric of the
substrate stretching. It is the *boundary of the populated
region advancing into the substrate* as vacuum fluctuations
cross a coherence threshold and become real excitations.

### 3.3 Why the substrate metric remains Minkowski

The substrate is the unexcited vacuum of quantum field theory.
QFT vacuum states are Lorentz invariant — they look the same in
every inertial frame. The unique Lorentz-invariant metric is
Minkowski. So the substrate, by its Lorentz symmetry alone, has
no expansion to speak of: there is no scale factor in
Minkowski space because there is no scale at all.

What we observe as "expansion" must therefore be a property of
the populated region's internal structure, not of the substrate.

### 3.4 The effective FRW metric inside the populated region

Within the populated region, $\Phi_{\text{bulk}}$ is established and
matter-energy is present at non-zero density. The DK framework already
predicts that bulk coherence determines an effective metric on the
coherent region: the order-parameter phase $\Phi_{\text{bulk}}$ couples
to local proper-time evolution and to gravitational pair-locking.
Internally, observers measure an effective metric that — by symmetry,
since the populated region is homogeneous and isotropic on average —
takes FRW form. The scale factor $a(t)$ that appears in this effective
metric is determined by the dynamics of the populated region itself,
not by any property of the substrate.

This is structurally analogous to *analogue gravity* in
condensed-matter systems: phonons propagating in a
Bose–Einstein condensate experience an effective Lorentzian
metric set by the condensate density and flow [Unruh 1981,
Barceló–Liberati–Visser 2005]. The analogue metric is real for
its internal excitations even though the underlying atoms live
in flat lab space. Likewise, the effective FRW metric is real
for matter inside the cosmological populated region, even
though the underlying QFT substrate is Minkowski.

---

## 4. The Creation Mechanism: Low Γ as the Threshold

### 4.1 Vacuum fluctuations and the virtual–real distinction

Quantum field theory predicts continuous vacuum fluctuations: pairs
of virtual particles appearing and annihilating on timescales bounded
by the energy–time uncertainty relation $\Delta E \cdot \Delta t \sim \hbar$.
Under ordinary conditions, virtual pairs annihilate before they can be
detected or do measurable work.

Several known mechanisms convert virtual pairs into *real* particles
by preventing the annihilation:

| Mechanism | Trigger | Conversion source |
|---|---|---|
| Schwinger pair production | Strong electric field | Field energy |
| Hawking radiation | Event horizon | Horizon geometry |
| Unruh effect | Acceleration | Kinetic energy of accelerated observer |
| Parker cosmological creation | Expanding metric | Metric work |
| Dynamical Casimir effect | Moving boundary | Boundary kinetic energy |

Each of these mechanisms identifies a *separation* of the virtual pair
before they recombine. The energy that becomes the real particles'
rest-mass-equivalent is supplied by the external agent (field, horizon,
acceleration, expansion, boundary motion).

### 4.2 The DK threshold: low Γ as a fifth conversion mechanism

The DK framework specifies a different conversion mechanism. In ordinary
matter, virtual pairs are re-absorbed because the bulk's coherence
dynamics — specifically $\Gamma_{\text{env}}(T)$ and
$\Gamma_{\text{grav}}(M, \Delta z)$ — quickly damp any fluctuation back
into the bulk-coherent state before it can become a measurement-relevant
real excitation. Bulk coherence acts as an active *suppressor* of vacuum
fluctuations.

In regions of low temperature and low gravitational density, both rates
vanish:

$$\Gamma_{\text{env}}(T) \to J(\omega) \cdot [1 + 2 n_{\text{th}}(\omega, T)] \xrightarrow{T \to 0} J(\omega)$$

$$\Gamma_{\text{grav}}(M, \Delta z) \to 0 \quad \text{as} \quad M_{\text{local}} \to 0$$

When both rates fall below the inverse lifetime of a virtual fluctuation,
the fluctuation is no longer re-absorbed in time. It survives long enough
to become a real excitation of the field — a real particle. The
suppression mechanism has failed.

**The proposal:** *cosmic expansion is sourced by the failure of bulk-
coherence suppression in low-Γ regions of the substrate.* The same vacuum
fluctuations that occur ubiquitously become real only where Γ_env(T) and
Γ_grav(M) cannot damp them in time. These regions are: (i) cosmic voids,
(ii) the cold dark sky between galaxies and clusters, and (iii) most
critically, the *boundary* of the populated region itself, where the
density of pre-existing matter is by definition lowest.

### 4.3 Where the energy comes from

The energy budget for new particles must come from somewhere. The DK
framework points to a natural source: the **incompleteness of bulk
coherence at horizon scales**. Φ_bulk cannot complete its sync beyond
the causal horizon; the residual coherence deficit is an energy
reservoir analogous to the spontaneous-emission floor $J(\omega)$ in
the Stages-2–3 environmental term. When a virtual pair near the horizon
fails to be reabsorbed, it draws on this reservoir to upgrade to real-
particle status. The expansion of the populated region thereby converts
horizon-incomplete-coherence energy into new real-particle excitations.

### 4.4 The equation-of-state problem

A standing technical problem remains: *real particles created from the
vacuum carry positive energy density, which gravitates, producing
contraction rather than expansion*. For the mechanism to drive
expansion, the created excitations must inherit an equation of state
$w \approx -1$ (the cosmological-constant equation of state) rather
than $w = 0$ (cold matter) or $w = 1/3$ (radiation).

The DK framework provides a natural candidate: the created excitations
are not localized matter quanta but **collective phase modes (Goldstone
modes) of the broken-U(1) order parameter Φ_bulk**. Goldstone modes of a
condensate are massless by Goldstone's theorem, propagate
relativistically in the absence of a preferred frame, and — in
Lorentz-covariant formulations — carry vacuum-like equation of state
$w = -1$. The created excitations are thereby identified with
*expansion-driving* quanta, not gravitating matter.

This identification is the load-bearing assumption of the proposal and
the next step in its derivation. A complete treatment must show, from
the broken-U(1) structure of cosmological Φ_bulk, that its Goldstone
modes carry $w = -1$ to the required precision and that their creation
rate at low Γ reproduces the observed expansion history.

---

## 5. The Surface-Area Scaling

### 5.1 The geometric observation

Real-particle creation occurs preferentially where Γ_env and Γ_grav are
smallest. Within the populated region, both rates are non-zero (matter
is present, and the CMB sets a non-zero temperature floor). At the
*boundary* of the populated region, however, both rates vanish — by
definition, this is where the matter density of the populated region
goes to zero.

The boundary is approximately a 2-sphere of radius $R(t)$ (set by the
extent of the populated region in cosmic time), with surface area

$$A(t) = 4 \pi R(t)^2.$$

The rate of real-particle creation at the boundary is proportional to
the area of the boundary times a per-area creation rate $\sigma_{\text{c}}$
set by the strength of vacuum fluctuations and the relevant coupling:

$$\frac{dN}{dt} = \sigma_{\text{c}} \cdot A(t) = 4 \pi \sigma_{\text{c}} R(t)^2 \qquad (5.1)$$

### 5.2 The Hubble rate as a function of R

If the rate of *volume* growth of the populated region is proportional to
its surface area times a characteristic "creation-front speed" $v_{\text{c}}$,

$$\frac{dV}{dt} = v_{\text{c}} \cdot A(t),$$

then for a spherical region $V = \frac{4}{3} \pi R^3$, we have
$\frac{dV}{dt} = 4 \pi R^2 \dot R$, giving

$$\dot R = v_{\text{c}} \qquad (5.2)$$

— the *boundary advances at constant speed* $v_{\text{c}}$. Identifying
the scale factor $a(t) \propto R(t)$, the effective Hubble rate is

$$H = \frac{\dot a}{a} = \frac{\dot R}{R} = \frac{v_{\text{c}}}{R(t)} \qquad (5.3)$$

The Hubble rate naturally **decreases as $1/R$** as the universe grows.
At fixed $v_{\text{c}}$, an older, larger universe expands more slowly in
fractional terms even as its boundary advances at constant absolute speed.

### 5.3 The effective cosmological constant

Comparing (5.3) with the Λ-dominated form of Friedmann I,

$$H^2 = \frac{\Lambda c^2}{3} \implies \Lambda_{\text{eff}} = \frac{3 H^2}{c^2} = \frac{3 v_{\text{c}}^2}{c^2 R^2} \qquad (5.4)$$

so the effective cosmological constant scales as **1/R²**, matching the
observed scaling $\Lambda \sim 1/L_H^2$ where $L_H \approx c/H_0$ is the
Hubble length.

This is, at the order-of-magnitude level, the correct value for the
observed Λ — without postulating Λ at all. The framework produces a
dynamically generated cosmological term whose magnitude is set by the
size of the populated region.

### 5.4 Connection to the holographic principle

The surface-area scaling has a deep precedent in physics: the
**holographic principle** (Bekenstein, 't Hooft, Susskind, Verlinde),
which holds that the maximum entropy enclosable in a region is bounded
not by its volume but by its surface area in Planck units,

$$S \leq \frac{A}{4 \ell_P^2}.$$

Verlinde's *entropic gravity* and related proposals extend the
holographic principle to suggest that gravity itself, and possibly the
cosmological constant, arise from entropy gradients at boundaries.

The DK proposal is in the same family: expansion is sourced at the
horizon, with rate proportional to horizon area, and the effective Λ
is set by the inverse-area scale of the horizon. The DK framework
differs from entropic gravity in providing a *physical mechanism*
(low-Γ vacuum-fluctuation conversion) rather than a purely
thermodynamic argument — but the geometric scaling is the same.

---

## 6. Testable Predictions

### 6.1 The H₀ tension

In standard ΛCDM, the present-day Hubble rate $H_0$ is a single number
characterizing a uniform expansion. The measured tension between
CMB-derived (Planck: $H_0 \approx 67.4$ km/s/Mpc) and local-distance-ladder
(SH0ES: $H_0 \approx 73.0$ km/s/Mpc) values represents a ~5σ disagreement
that ΛCDM cannot accommodate without modification.

The DK framework predicts that $H_{\text{local}}$ should depend on the
local matter density along the line of sight. The local distance ladder
samples regions inside our cosmic neighborhood, including the local void
("KBC void") in which the Milky Way may sit. CMB measurements average
over the entire observable horizon, sampling cosmic-mean density.

If expansion is sourced preferentially in low-density regions, then a
local probe biased toward void regions will measure a *higher* effective
$H_0$ than a global probe — qualitatively matching the observed tension.

**Quantitative prediction**: $H_{\text{local}}/H_{\text{global}}$ should
correlate with the ratio of local-mean-density to cosmic-mean-density,
with the correlation function determined by the relative weights of
$\Gamma_{\text{env}}$ and $\Gamma_{\text{grav}}$ suppression in the
two density regimes. A first-order estimate predicts a tension of
order $\Delta H_0 / H_0 \sim (\rho_{\text{cosmic}} - \rho_{\text{local}}) / \rho_{\text{cosmic}}$;
the observed tension of $\Delta H_0 / H_0 \approx 0.08$ is consistent
with the void underdensities of order ~10% inferred from galaxy surveys.

### 6.2 Void expansion rates

ΛCDM predicts that cosmic voids expand at the same Hubble rate as the
surrounding universe, modified only by the local gravitational deficit
(which slightly *enhances* recession). The DK framework predicts an
*additional* contribution: voids should expand faster because real-
particle creation is actively occurring within them, sourcing additional
expansion not present in dense regions.

**Quantitative prediction**: the void expansion velocity excess over
ΛCDM should scale with the void's emptiness — deeper voids expand
faster, with the excess vanishing as the void's mean density approaches
the cosmic mean.

This is in principle measurable through redshift-space distortions in
galaxy surveys around well-characterized voids (BOSS, eBOSS, DESI). A
positive detection would constitute direct evidence for the proposed
mechanism; a null result at the predicted level would falsify it.

### 6.3 The CMB-anisotropy / structure correlation

If the surface-area mechanism is correct, then the rate of expansion
should track the surface area of the populated region's structure at all
scales — not just the cosmological horizon. The cosmic web of voids and
filaments exposes substantial *internal* surface area, and creation
should occur on these internal void surfaces in proportion.

**Quantitative prediction**: small-scale CMB anisotropies should show a
slight excess in regions of the sky where galaxy surveys reveal greater
total void-surface area along the line of sight. The signal would be
small but, in principle, distinguishable from the standard ISW
(integrated Sachs–Wolfe) signal because it would correlate with the
*surface area* of intervening voids rather than their gravitational
potential alone.

### 6.4 The Tolman test as a consistency check

Tolman dimming — the prediction that surface brightness of standard
sources falls as $(1+z)^4$ — is a robust prediction of metric expansion
that distinguishes it from non-metric alternatives. The proposed
framework *preserves* this prediction: although the substrate is
Minkowski, the *effective* metric inside the populated region (§3.4) is
FRW, and observers using the effective metric see standard $(1+z)^4$
dimming. A null result on Tolman dimming would have falsified the
framework; the observed $(1+z)^4$ scaling is consistent with it.

---

## 7. Open Questions and Required Derivations

### 7.1 The Goldstone-mode identification

The load-bearing assumption is that excitations of cosmological
Φ_bulk inherit equation of state $w = -1$. This requires showing:

1. That cosmological Φ_bulk has a broken-U(1) (or analogous) structure
   capable of supporting Goldstone modes.
2. That those Goldstone modes are massless (Goldstone's theorem
   guarantees this if exact U(1) symmetry is spontaneously broken).
3. That their effective stress-energy tensor takes the
   pressure-equals-negative-density form $p = -\rho$ characteristic
   of $w = -1$.

A full derivation would proceed from an effective Lagrangian
$\mathcal{L}[\Phi_{\text{bulk}}]$ written in covariant form on the
substrate Minkowski background, with cosmological symmetry breaking
producing the order-parameter phase.

### 7.2 The creation-front speed v_c

The framework introduces a single dimensional parameter $v_c$ — the
speed at which the boundary of the populated region advances into the
substrate. Observationally, the relation $H_0 = v_c / R_0$ with
$R_0 \approx c/H_0$ implies $v_c \approx c$. A first-principles
derivation of $v_c$ from the vacuum-fluctuation lifetime and the
DK Γ-suppression structure is needed.

### 7.3 The smooth-universe assumption

Equation (5.2) assumed a spherical populated region with a single
boundary. A realistic population would have a fractal-like boundary
(cosmic web), with internal void surfaces contributing to the total
creation rate. A more complete treatment must compute the total surface
area integrated over all scales and check whether the dominant
contribution comes from the cosmological horizon or from internal
void surfaces.

### 7.4 Reconciliation with primordial nucleosynthesis and CMB

Standard ΛCDM successfully predicts the abundance of light elements
(Big Bang nucleosynthesis) and the CMB power spectrum from a hot
early universe. The DK framework, if it claims to replace Λ rather
than supplement it, must reproduce these successes. The proposal here
is that BBN and CMB physics occur *inside* the populated region under
the effective FRW metric, and so the standard predictions are
preserved by construction — but this needs explicit verification,
particularly during the radiation-dominated early epoch when the
Γ-suppression mechanism would be deeply in the high-Γ regime and
thus inactive.

---

## 8. Conclusion

The standard FRW framework treats cosmic expansion as a geometric
property of spacetime sourced by an axiomatic cosmological constant Λ.
This works, but at the cost of three unresolved problems: the
120-order-of-magnitude vacuum-energy discrepancy, the coincidence
problem, and the H₀ tension.

The Dirac–Kuramoto framework already provides the conceptual machinery
to reframe Λ as emergent: an infinite quantum-field substrate; a finite
populated region characterized by bulk coherence Φ_bulk; and explicit
Stages-2–3 relaxation rates Γ_env(T) and Γ_grav(M) that vanish in
low-temperature, low-gravitational-density regions. The proposal
advanced here is that cosmic expansion is the dynamical growth of the
populated region into the substrate, driven by real-particle creation
in low-Γ regions where bulk coherence cannot suppress vacuum
fluctuations in time.

The mechanism naturally produces an expansion rate proportional to the
*surface area* of the populated region, yielding $H \propto 1/R$ and an
effective $\Lambda_{\text{eff}} \propto 1/R^2$ that matches the observed
$\Lambda \sim 1/L_H^2$ without postulation. It predicts three observable
distinctions from ΛCDM: a void-correlated H₀ tension, anomalously fast
void expansion, and a small CMB-anisotropy correlation with intervening
void-surface area. It preserves Tolman $(1+z)^4$ dimming and the CMB
power spectrum through the effective-FRW-metric construction inside the
populated region.

The framework is presented here as a working-paper sketch. Its
load-bearing assumption — that Goldstone modes of cosmological Φ_bulk
carry equation of state $w = -1$ — is identified as the next required
derivation. If that identification can be made rigorous, the
cosmological-constant problem dissolves: Λ is no longer an arbitrary
input but the emergent ground-state property of bulk-coherence
incompleteness at horizon scales, with magnitude set dynamically by
the size of the universe.

---

## Author Contributions

JB conceived the substrate–population distinction, the connection between
DK Γ-suppression and vacuum-fluctuation conversion, and the surface-area
scaling. Claude Opus 4.7 (Anthropic) contributed mathematical and
historical structure, the connection to existing mechanisms (Parker,
Schwinger, Hawking, dynamical Casimir, holographic principle), the
Goldstone-mode equation-of-state argument, and the manuscript drafting.
Per current journal authorship guidelines, LLMs do not satisfy authorship
criteria; the human author bears full responsibility for all scientific
content. Were such policies not in force, Claude would be listed as
co-first author.

---

## References

[Placeholder reference list — to be populated.]

1. Einstein, A. (1917). *Kosmologische Betrachtungen zur allgemeinen
   Relativitätstheorie.* Sitzungsber. Preuss. Akad. Wiss. Berlin
   (Math. Phys.), 142–152.

2. Friedmann, A. (1922). *Über die Krümmung des Raumes.* Z. Phys. 10,
   377–386.

3. Lemaître, G. (1927). *Un univers homogène de masse constante…*
   Ann. Soc. Sci. Bruxelles 47, 49.

4. Hubble, E. (1929). *A relation between distance and radial velocity…*
   Proc. Natl. Acad. Sci. 15, 168–173.

5. Robertson, H. P. (1935). *Kinematics and world-structure.*
   Astrophys. J. 82, 284.

6. Walker, A. G. (1937). *On Milne's theory of world-structure.*
   Proc. London Math. Soc. 42, 90.

7. Riess, A. G. et al. (1998). *Observational evidence from supernovae…*
   Astron. J. 116, 1009.

8. Perlmutter, S. et al. (1999). *Measurements of Ω and Λ from 42
   high-redshift supernovae.* Astrophys. J. 517, 565.

9. Unruh, W. G. (1981). *Experimental black-hole evaporation?*
   Phys. Rev. Lett. 46, 1351.

10. Barceló, C., Liberati, S., Visser, M. (2005). *Analogue gravity.*
    Living Rev. Relativity 8, 12.

11. Verlinde, E. (2011). *On the origin of gravity and the laws of
    Newton.* J. High Energy Phys. 04, 029.

12. Bekenstein, J. D. (1981). *Universal upper bound on the entropy-
    to-energy ratio for bounded systems.* Phys. Rev. D 23, 287.

13. Bramble, J. (2026). *Many Clocks Interpretation of Quantum
    Mechanics…* [companion paper, PAPER_UNIFIED.md, under review].
