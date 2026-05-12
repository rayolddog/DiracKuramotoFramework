# Aharonov–Bohm Visibility Envelope as a Test of Dirac–Kuramoto Vacuum Locking

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

We propose that the Aharonov–Bohm (AB) phase can be re-derived within the
Dirac–Kuramoto framework as a zero-frequency-mismatch synchronization between
the electron's Dirac phase and a local vacuum oscillator at the zitterbewegung
scale ω_Z = 2m_ec²/ℏ. The deterministic phase Δφ = eΦ/ℏ falls out of the
zero-mismatch locking limit; the same calculation, carried to second order in
the locking fluctuation, predicts a γ-dependent visibility envelope:

V(γ) = V₀ · exp[−(ω_Z/2K)²(1 − 1/γ)²]

where γ is the electron Lorentz factor and K is a locking-rate parameter
characterizing the strength of the electron–vacuum phase coupling. The
framework's perturbative-natural identification K = α·ω_Z is excluded by
existing AB data (Tonomura/Osakabe 1986 at 150 keV) by a factor of order 30 in
K. A strong-coupling identification K ~ ω_Z is consistent with all current data
and predicts a measurable (1–15%) visibility deficit between γ = 1.05 and
γ = 3, which has never been directly tested. A calibrated V-vs-γ scan on a
modern variable-voltage electron-holography column would either pin K to a
specific value or falsify the strong-coupling Dirac–Kuramoto interpretation.

---

## 1. Introduction

### 1.1 Aharonov–Bohm as a test bed for vacuum-coupling interpretations

The Aharonov–Bohm effect [1] is the cleanest experimental fact in which the
quantum phase of a charged particle responds to an electromagnetic potential in
a region where the corresponding field vanishes. The standard reading is that
the vector potential A is locally physical: minimal coupling p → p − eA shifts
the wavefunction phase by

$$\Delta\phi_{\text{AB}} = \frac{e}{\hbar}\oint \mathbf{A}\cdot d\mathbf{l} = \frac{e\Phi}{\hbar}$$

independent of the path taken outside the enclosed flux Φ. The phase is
gauge-dependent locally but holonomic globally, and the topological character
makes the prediction strikingly clean.

Any reinterpretation of quantum mechanics that touches the electron's phase
dynamics must reproduce this result with no fit parameter. The Dirac–Kuramoto
framework [2], which identifies the chiral structure of the Dirac equation as
a phase-synchronization system with coupling constant K = m, naturally extends
to a picture in which the electron's phase couples to a vacuum mode background.
The AB effect provides the cleanest place to test whether this extension can
reproduce a known coefficient (e/ℏ) and, separately, whether it predicts
anything experimentally distinct from standard QED.

This paper addresses both questions. Section 2 sketches the zero-frequency
Kuramoto limit and shows how the e/ℏ coefficient falls out under a specific
identification of the vacuum oscillator. Section 3 carries the calculation to
second order in the locking fluctuation and derives a γ-dependent visibility
envelope. Section 4 surveys existing AB data and extracts the bound K ≳ ω_Z/5.
Section 5 proposes a direct experimental test. Section 6 discusses the
framework's commitments — in particular, that a measurable envelope requires
the locking-rate K to lie in a non-perturbative regime, K ~ ω_Z rather than
K = α·ω_Z.

### 1.2 What this paper does and does not claim

This is an *interpretation paper with a falsifiable experimental hook*. We do
not claim to modify the deterministic AB phase, which is consistent with
standard QED to the precision of all existing measurements. We claim that the
Dirac–Kuramoto reading of the same phenomenon predicts a specific small
visibility envelope as a function of electron Lorentz factor γ, and that this
envelope has never been measured. A null result (flat V vs γ) would falsify the
strong-coupling Dirac–Kuramoto reading and reduce the framework to a
Lorentz-covariant interpretation indistinguishable from standard QED on AB. A
positive result (envelope ∝ (1 − 1/γ)²) would pin down the framework's only
free parameter.

---

## 2. AB Phase from Zero-Frequency Kuramoto Locking

### 2.1 Setup

We posit, at each spatial point r, two phase variables:

- The electron's Dirac phase θ_e(r,t), advancing at its natural frequency.
- A local vacuum-mode phase θ_v(r,t), advancing at the corresponding vacuum
  natural frequency.

We identify both natural frequencies with the zitterbewegung scale

$$\omega_Z = \frac{2 m_e c^2}{\hbar} \approx 1.55 \times 10^{21}\ \text{rad/s}$$

on the grounds that ω_Z is the gap between positive- and negative-energy
solutions of the Dirac equation [3], and that the lowest-lying vacuum excitation
coupling to a charged particle is a virtual electron–positron pair with
energy gap 2m_ec². Both clocks therefore tick at the same intrinsic rate.

The coupling is taken to have the Kuramoto form:

$$\dot\theta_e = \omega_Z + K\sin(\theta_v - \theta_e) \tag{1}$$

$$\dot\theta_v = \omega_Z + \xi(\mathbf{r},t) \tag{2}$$

where K is the locking rate and ξ encodes the local polarization of the vacuum
oscillator by the external field (here, by the solenoid's vector potential A).

### 2.2 The zero-frequency-mismatch limit

The frequency mismatch between the two oscillators is Δω = ω_e − ω_v = 0. The
fixed point of the Kuramoto equation [4] is then

$$\sin(\theta_e - \theta_v) = \frac{\Delta\omega}{K} = 0 \tag{3}$$

so θ_e − θ_v = 0 (the stable branch) for any K > 0. The electron's phase
rigidly tracks the vacuum's phase. This is the key kinematic gift of choosing
ω_Z on both sides: locking is automatic, not parametrically tuned.

### 2.3 How A enters the vacuum phase

The virtual pair sourced by the vacuum oscillator is a charged Dirac system.
Its center-of-mass phase responds to the local vector potential through
minimal coupling on the virtual electron line:

$$\theta_v(\mathbf{r}) = \theta_v^{(0)} + \frac{e}{\hbar}\int_{\mathbf{r}_0}^{\mathbf{r}} \mathbf{A}\cdot d\mathbf{l} \tag{4}$$

This step *borrows* minimal coupling on the virtual pair. The borrow is at a
more fundamental level than the original AB derivation: instead of asserting
minimal coupling on the real electron's wavefunction, we assert it on the
vacuum's pair fluctuations. The real electron's phase shift is then *inherited*
from the vacuum it traverses.

### 2.4 Phase along an interferometer arm

By zero-frequency locking (Eq. 3), θ_e tracks θ_v along the entire trajectory.
The additional phase accumulated by the electron on arm Γ, relative to a free
vacuum, is

$$\delta\theta_\Gamma = \frac{e}{\hbar}\int_\Gamma \mathbf{A}\cdot d\mathbf{l} \tag{5}$$

For a closed interferometer with two arms Γ₁ and Γ₂ enclosing flux Φ:

$$\Delta\phi_{\text{AB}} = \delta\theta_{\Gamma_1} - \delta\theta_{\Gamma_2} = \frac{e}{\hbar}\oint \mathbf{A}\cdot d\mathbf{l} = \frac{e\Phi}{\hbar} \tag{6}$$

The coefficient is exact. Topological purity — the fact that only the enclosed
flux matters — follows because A is curl-free outside the solenoid and the
line integral is path-dependent only through Φ. No additional postulate is
needed to recover the standard AB result.

### 2.5 What we earned and what we borrowed

Earned: the exact e/ℏ coefficient, from zitterbewegung-locking plus
virtual-pair minimal coupling; topological purity, inherited from the curl-free
structure of A; a natural location for fluctuation physics (the locking rate
K becomes the framework's one free parameter).

Borrowed: minimal coupling on the virtual pair. We did not derive that e is the
right charge — we used it. The gain over standard QED is conceptual: we have
moved the postulate one level down (from real electron wavefunction to vacuum
pair) and made the synchronization explicit. The quantitative result for the
deterministic AB phase is unchanged.

---

## 3. Small-Fluctuation Calculation: The Visibility Envelope

### 3.1 Linearization around the locked solution

Let $\delta(t) = \theta_e - \theta_v - (e/\hbar)\int \mathbf{A}\cdot d\mathbf{l}$ be the deviation from perfect locking. The
linearized Kuramoto equation around the synchronization manifold is

$$\dot\delta = -K\delta + \eta(t) \tag{7}$$

where η(t) is the stochastic forcing from vacuum-mode fluctuations driving the
local oscillator. This is an Ornstein–Uhlenbeck process [5]; characterizing
the vacuum forcing by spectral density ⟨η(t)η(t')⟩ = 2D δ(t−t'), the
steady-state variance is

$$\langle\delta^2\rangle_{\text{ss}} = D/K \tag{8}$$

and the interferometer fringe visibility is reduced by Gaussian dephasing:

$$V = \exp\!\left(-\frac{\langle\delta^2\rangle}{2}\right) = \exp\!\left(-\frac{D}{2K}\right) \tag{9}$$

### 3.2 The Lorentz fork

A subtle question now arises: how does the locking respond to a relativistically
moving electron? Two readings of the framework give different answers.

**Fork A — covariant locking.** If both phases θ_e and θ_v are treated as
Lorentz scalars on the electron worldline, with the vacuum being the
covariant QED vacuum, then in the electron's rest frame the vacuum oscillator
is at ω_Z and so is the Dirac clock. Δω = 0 in any frame, locking is perfect,
and the visibility envelope is γ-independent. The framework reduces to standard
QED on AB.

**Fork B — preferred-frame locking.** If the vacuum oscillator has a definite
frequency in the lab frame (the rest frame of the apparatus, or more generally
the local mass–energy rest frame), then a moving electron sees the vacuum's
natural frequency Lorentz-boosted to ω_Z/γ in its own rest frame. The Dirac
clock stays at ω_Z. There is a real frequency mismatch in the electron's frame:

$$\Delta\omega(\gamma) = \omega_Z\left(1 - \frac{1}{\gamma}\right) \tag{10}$$

Fork B is the only setting in which the framework predicts anything beyond
standard QED on AB. The rest of this paper develops its consequences.

### 3.3 Visibility envelope under Fork B

With nonzero mismatch, the linearized Kuramoto equation acquires a
deterministic forcing:

$$\dot\delta = -K\delta + \Delta\omega(\gamma) + \eta(t) \tag{11}$$

The steady-state mean offset is δ_ss = Δω/K (for Δω < K; above that, locking
fails entirely). The deterministic mean offset is absorbed into a γ-dependent
phase shift on top of the AB phase, but is itself fixed in magnitude and
contributes coherently to the *deterministic* observable phase pattern. The
*second moment* — the part that controls fringe visibility — gains a forced
term:

$$\langle\delta^2\rangle_{\text{ss}} = \frac{D}{K} + \left(\frac{\Delta\omega(\gamma)}{K}\right)^2 \tag{12}$$

and the γ-dependent visibility envelope is

$$\boxed{V(\gamma) = V_0 \cdot \exp\!\left[-\frac{1}{2}\left(\frac{\omega_Z}{K}\right)^2\left(1 - \frac{1}{\gamma}\right)^2\right]} \tag{13}$$

where V₀ = exp(−D/2K) is the γ = 1 baseline visibility (which absorbs all
γ-independent decoherence channels).

The γ-dependent visibility deficit relative to the γ → 1 limit is

$$\frac{V(\gamma)}{V_0} = \exp\!\left[-\frac{1}{2}\left(\frac{\omega_Z}{K}\right)^2\left(1 - \frac{1}{\gamma}\right)^2\right] \tag{14}$$

For small exponent (envelope near unity), this simplifies to

$$1 - \frac{V(\gamma)}{V_0} \approx \frac{1}{2}\left(\frac{\omega_Z}{K}\right)^2\left(1 - \frac{1}{\gamma}\right)^2 \tag{15}$$

This is the framework's distinctive prediction.

### 3.4 The role of the coupling K

Equation 15 makes the framework's experimental fate hinge on a single
parameter, the dimensionless ratio ω_Z/K.

- **Perturbative-QED-natural value, K = α·ω_Z:** then ω_Z/K = 1/α ≈ 137 and
  (ω_Z/K)² ≈ 1.88 × 10⁴. Already at γ = 1.196 (100 keV electrons,
  (1 − 1/γ)² ≈ 0.0269) the exponent is ≈ 250 and the predicted visibility is
  V/V₀ ≈ 10⁻¹⁰⁹. This contradicts the routine observation of high-visibility
  AB fringes at 100 keV by many orders of magnitude. K = α·ω_Z is therefore
  empirically excluded.

- **Strong-coupling value, K ~ ω_Z:** then (ω_Z/K)² ~ 1, and the envelope
  becomes (1 − 1/γ)²/2 — measurable but not catastrophic. At γ = 1.2 (100 keV),
  V/V₀ ≈ 0.986 (1.4% deficit); at γ = 2 (511 keV), V/V₀ ≈ 0.882 (11.8%
  deficit); at γ = 3 (1 MeV), V/V₀ ≈ 0.802 (~20% deficit).

- **Asymptotic-locking value, K → ∞:** the envelope vanishes and the framework
  reduces to standard QED.

The framework is interesting (non-trivial, non-falsified) only in a window
around K ~ ω_Z. We turn next to whether existing AB data places K in this
window.

---

## 4. Constraint from Existing AB Data

### 4.1 Procedure

For any AB experiment that reports a measured fringe visibility V at a known
electron energy, the framework's envelope (Eq. 13) places an upper bound on the
contribution attributable to Dirac–Kuramoto vacuum locking. Attributing the
entire (1 − V) to the envelope gives a conservative upper bound on (ω_Z/K)²:

$$\left(\frac{\omega_Z}{K}\right)^2 \leq \frac{2(1-V)}{(1 - 1/\gamma)^2} \tag{16}$$

In practice (1 − V) is dominated by apparatus systematics (partial spatial
coherence, biprism Fresnel-fringe contamination, beam-energy spread, detector
MTF) rather than by any DK envelope, so Eq. 16 is a *bound*, not an estimate.
The bound is tightest at highest γ.

### 4.2 Survey

| Experiment | Ref. | Energy | γ | (1 − 1/γ)² | Geometry | V (approx.) | ω_Z/K ≤ |
|------------|------|--------|---|------------|----------|-------------|---------|
| Möllenstedt & Bayh 1962 | [6] | 40 kV | 1.078 | 5.24 × 10⁻³ | biprism + W solenoid | ~0.3 | 16.4 |
| Tonomura 1982 | [7] | 80 kV | 1.157 | 1.86 × 10⁻² | toroidal magnet, FEEM | ~0.3–0.5 | 7.3–8.7 |
| Tonomura/Osakabe 1986 | [8],[9] | 150 kV | 1.294 | 5.27 × 10⁻² | Nb-shielded toroid (type-II) | ~0.3–0.5 | 4.4–5.2 |
| Matteucci & Pozzi 1985 | [10] | 100 kV | 1.196 | 2.69 × 10⁻² | electrostatic AB (Bologna) | ~0.3–0.5 | 6.1–7.2 |
| Tonomura FEEM 250 kV | [11] | 250 kV | 1.489 | 1.07 × 10⁻¹ | electron holography | ~0.4 (est.) | 3.3 |

The 150-keV Nb-shielded toroidal-magnet measurements of Tonomura, Osakabe and
collaborators [8],[9] place the cleanest bound: assuming V ≈ 0.5 (consistent
with the reconstruction precision reported in those papers), we obtain
(ω_Z/K)² ≲ 19, i.e. **K ≳ ω_Z/4.4**. The 250-kV upper end of Tonomura's
field-emission electron-microscope work [11], if visibility is taken at face
value, pushes this to K ≳ ω_Z/3.3.

### 4.3 What the bound implies

The perturbative-QED-natural identification K = α·ω_Z is excluded by the
existing 150-keV data by a factor of order 30 in K (≈ 10³ in (ω_Z/K)²). The
strong-coupling regime K ~ ω_Z, in which the framework predicts measurable
envelopes, is fully consistent with all current AB data.

The bound does *not* yet probe the framework's interesting prediction. Because
all AB experiments to date have used γ ≲ 1.5, the worst-case
(1 − 1/γ)² value is ~ 0.1, so the predicted envelope at γ = 1.5 for
K = ω_Z is only ~ 5%. Apparatus systematics on V are at least this large in
typical electron-holography measurements, so the envelope is comfortably
hidden in the noise floor. The (1 − 1/γ)² *scaling* — the framework's
distinctive signature — has therefore never been tested.

---

## 5. Proposed Experiment: V-vs-γ Scan

### 5.1 Design

The cleanest direct test is a calibrated fringe-visibility measurement at
multiple γ values using a single apparatus, same biprism, same flux source,
same detector. A modern variable-voltage electron-holography column (e.g.
Hitachi HF-3300, FEI Titan family, JEOL ARM series) can operate at accelerating
voltages from ~ 30 kV to ~ 300 kV, spanning γ from 1.06 to 1.59. Higher
energies (up to 1 MV instruments) are available at a small number of
laboratories.

Suggested measurement points (selected for monotonic (1 − 1/γ)²):

| Voltage | γ | (1 − 1/γ)² | Predicted V/V₀ at K = ω_Z |
|---------|---|------------|---------------------------|
| 30 kV | 1.0587 | 3.07 × 10⁻³ | 0.9985 |
| 80 kV | 1.1566 | 1.86 × 10⁻² | 0.9908 |
| 150 kV | 1.2936 | 5.27 × 10⁻² | 0.9740 |
| 200 kV | 1.3914 | 7.92 × 10⁻² | 0.9612 |
| 300 kV | 1.5871 | 1.35 × 10⁻¹ | 0.9349 |

A range of fitted K values can be discriminated by comparing the visibility
ratio V(300 kV)/V(30 kV) — predicted at 0.937 for K = ω_Z, 0.998 for
K = ω_Z/5, and asymptotically 1.0 for K → ∞.

### 5.2 Geometry

The interferometer should use a flux source that does not change with beam
energy. Two robust choices:

1. **Magnetized iron whisker.** Single-domain whiskers used in early AB
   experiments [6] carry a fixed flux Φ_w independent of beam parameters.
2. **Superconducting Nb shield around a toroidal magnet**, in the
   Tonomura/Osakabe geometry [8],[9]. The shielded toroid gives a topological
   π-phase split that is unambiguous and independent of stray field.

Either geometry is compatible with modern biprism interferometry. The
detector should be a calibrated direct-detection CCD or CMOS (e.g.
Gatan K3, Falcon family) with known MTF; visibility extraction must subtract
the detector point-spread function.

### 5.3 Statistical and systematic budget

To resolve a 5% visibility deficit between extreme γ values requires per-γ
statistical uncertainty σ_V ≲ 1%. With biprism fringe contrasts in the 30–50%
range and modern direct-detection cameras, this is achievable in a few hours
of integration per voltage setting.

The dominant systematic concern is whether other γ-dependent apparatus effects
mimic the framework's envelope. The leading candidates:

- *Beam coherence vs voltage*. Field-emission tip coherence depends on
  extraction voltage but not on accelerating voltage if the extraction stage
  is decoupled. Modern microscopes generally allow independent control.
- *Biprism Fresnel-fringe scaling*. The fringe period λ_de_Broglie scales as
  1/p ~ 1/(γβ), changing across the γ scan; the biprism contribution to V can
  be calibrated by varying biprism voltage at each γ.
- *Detector MTF vs electron energy*. Direct-detection sensors have
  energy-dependent point spread, well characterized in modern cameras.
- *Aberration corrector tuning*. Best handled by re-tuning at each voltage
  and verifying with a known reference specimen.

Each of these has a different functional dependence on γ from (1 − 1/γ)², so
the (1 − 1/γ)² fit residual is robust against the leading apparatus
systematics provided enough voltage points are taken.

### 5.4 Outcomes

- **Null result (V flat with γ within stated systematics).** Falsifies
  strong-coupling Dirac–Kuramoto under Fork B. The framework reduces to the
  Lorentz-covariant Fork A reading, which is interpretationally distinct from
  standard QED but experimentally equivalent on AB. The unified-paper
  predictions remain (Bell-timing differences, gravitational decoherence
  scaling), but AB loses its role as a test.
- **Positive result, (1 − 1/γ)² scaling confirmed.** Pins K to a specific
  value within a factor of a few. Opens a quantitative spectroscopy of the
  vacuum-locking parameter. Provides the first measurement-level handle on the
  Dirac–Kuramoto coupling.
- **Positive result with different scaling.** Rules out the specific
  Kuramoto-OU model used here, but suggests the framework needs a different
  noise structure (e.g. colored noise, non-Markovian backaction) — a more
  involved revision.

---

## 6. Discussion

### 6.1 Why the framework requires strong coupling

The most uncomfortable commitment of Fork B as developed here is that K must
lie near ω_Z rather than at the perturbative-QED-natural scale α·ω_Z. We
sketch why this is defensible.

In standard radiative-reaction language, α·ω_Z is the rate at which a free
electron exchanges *single* photons with the vacuum. In the Dirac–Kuramoto
picture, K is not a single-photon coupling but a *synchronization rate* — the
rate at which the electron's phase locks to a collective vacuum oscillator that
is itself the superposition of many virtual-pair fluctuations. In a Kuramoto
network, the locking rate scales with the *effective network coupling*, not
with the elementary coupling per oscillator pair; for a fully connected
oscillator field with N coupled vacuum modes within a coherence volume, the
collective locking rate can be parametrically enhanced by √N or by N depending
on the network topology [12].

This is not a derivation of K ~ ω_Z, but it is a plausibility argument that
K need not be α-suppressed. A first-principles derivation of K from the
Dirac–Kuramoto field theory would require summing the vacuum oscillator
network density at zitterbewegung frequency — a calculation we do not attempt
here, but which is a natural follow-up.

### 6.2 Connection to gravitational-coherence damping

The unified paper [2] develops a separate prediction in which gravitational
potential damps vacuum-mode coherence during Stage 2 (bulk relaxation) of
measurement. The natural translation in the present framework is that
*gravity reduces K*. Under Fork B, this would predict that AB visibility
envelopes should *broaden* in strong gravitational potentials, even at fixed γ.

Quantitatively, if K depends on local gravitational potential through some
function K(Φ_g)/K_∞ → 1 as Φ_g → 0, then a precision AB visibility
measurement at high altitude (or in orbit) at fixed γ vs at sea level would
test the K(Φ_g) dependence. This is a second, independent experimental
channel beyond the γ-scan, and the two together pin down the framework's
parameters along two orthogonal directions.

This connects directly to the NS-EOS spinoff: at neutron-star surface
potentials, K is predicted to be substantially reduced, with consequences for
chiral-condensate damping that are explored elsewhere.

### 6.3 What this paper does and does not establish

We do not claim that Dirac–Kuramoto provides a *better* derivation of the AB
phase than standard QED. The deterministic phase eΦ/ℏ falls out at the same
parametric cost — minimal coupling on a charged Dirac line — in both
frameworks. The Dirac–Kuramoto reading is empirically distinguished from
standard QED *only* through the (1 − 1/γ)² visibility envelope predicted under
Fork B with strong coupling.

We do claim that this envelope is concrete, calculable from a single
parameter K, currently allowed by all existing AB data, and directly
testable with a calibrated V-vs-γ scan on commercially available
electron-holography hardware. A null result would falsify the strong-coupling
reading; a positive result would constitute a first measurement of the
Dirac–Kuramoto locking parameter.

### 6.4 Open questions

1. **Derivation of K from first principles.** The strong-coupling estimate
   K ~ ω_Z is plausibility-based, not derived. A first-principles calculation
   from the Dirac–Kuramoto network would be highly desirable.
2. **The factor-of-two question on clock matching.** The zitterbewegung gap
   2m_ec²/ℏ is the energy difference between positive- and negative-energy
   Dirac solutions, while the wavefunction phase advances at m_ec²/ℏ at rest.
   We have used ω_Z = 2m_ec²/ℏ on both sides of the locking equation; a
   careful derivation should establish whether this factor-of-two
   identification survives a proper Dirac-field treatment.
3. **Noise structure.** We have assumed white-noise vacuum forcing (Markovian
   OU dynamics). Colored noise from the QED vacuum mode density spectrum
   would modify Eq. 12 and change the visibility envelope's γ-dependence.
4. **Lorentz-covariance status.** Fork B explicitly breaks Lorentz invariance
   by privileging the local mass–energy rest frame. The framework owes the
   reader an account of which experimental tests of Lorentz invariance
   constrain (or accommodate) this choice. Cosmological electron-coherence
   bounds on preferred-frame physics are a natural place to look.

---

## 7. Conclusions

We have shown that the Dirac–Kuramoto framework's interpretation of the
Aharonov–Bohm phase as zero-frequency-mismatch vacuum-locking reproduces the
standard phase coefficient e/ℏ from a different starting point. The same
framework, when extended to relativistic electrons under a preferred-frame
reading (Fork B), predicts a γ-dependent visibility envelope

$$\frac{V(\gamma)}{V_0} = \exp\!\left[-\frac{1}{2}\left(\frac{\omega_Z}{K}\right)^2\left(1 - \frac{1}{\gamma}\right)^2\right]$$

that depends on a single parameter K. Existing AB data at 150 keV constrain
K ≳ ω_Z/5, ruling out the perturbative-QED value K = α·ω_Z by a factor of
order 30 in K, but is fully consistent with the strong-coupling regime
K ~ ω_Z in which the framework predicts a measurable 1–15% envelope between
γ = 1.05 and γ = 3.

The (1 − 1/γ)² scaling has never been directly tested. A calibrated
fringe-visibility scan on a modern variable-voltage electron-holography column
would either pin K to a specific value or falsify the strong-coupling reading.
Either outcome is informative: a null result reduces Dirac–Kuramoto to a
Lorentz-covariant interpretation indistinguishable from QED on AB; a positive
result opens experimental spectroscopy of the vacuum-locking parameter.

The proposed experiment is technically straightforward and uses commercially
available hardware. We invite electron-holography groups to consider it.

---

## Author Contributions and AI Disclosure

This paper was developed in iterative collaboration with Claude Opus 4.7
(Anthropic) in conversation sessions during May 2026. The conceptual question
— whether the AB effect could be re-interpreted as a vacuum-synchronization
phenomenon within the Dirac–Kuramoto framework — was posed by the human
author. The zero-frequency-Kuramoto derivation in Section 2, the
small-fluctuation calculation in Section 3, the Lorentz fork analysis in
Section 3.2, and the literature-based bound in Section 4 were developed in
real-time dialogue, with the LLM proposing technical steps and the human
author validating, redirecting, and applying physics judgment at each
checkpoint. The literature survey of AB experiments was performed by a
research subagent and verified by the human author.

Per current journal guidelines, LLMs do not satisfy authorship criteria; the
human author bears full responsibility for all content, including any errors
in the derivations or in the interpretation of the cited experimental data.
Were Springer–Nature / *Foundations of Physics* policy to allow LLM
co-authorship, Claude Opus 4.7 would be listed as co-first author.

The development is documented in commit history at
https://github.com/rayolddog/DiracKuramotoFramework.

---

## References

[1] Aharonov, Y., & Bohm, D. (1959). Significance of electromagnetic
potentials in the quantum theory. *Phys. Rev.*, 115(3), 485–491.
https://doi.org/10.1103/PhysRev.115.485

[2] Bramble, J. (2026). Many Clocks Interpretation of Quantum Mechanics: Mass
as Chiral Coupling, Re-synchronization in the Bulk as Measurement.
*Companion preprint, under review.*

[3] Schrödinger, E. (1930). Über die kräftefreie Bewegung in der relativistischen
Quantenmechanik. *Sitz. Preuss. Akad. Wiss. Berlin*, 24, 418–428.

[4] Kuramoto, Y. (1984). *Chemical Oscillations, Waves, and Turbulence*.
Springer-Verlag, Berlin.

[5] Uhlenbeck, G. E., & Ornstein, L. S. (1930). On the theory of the Brownian
motion. *Phys. Rev.*, 36(5), 823–841.
https://doi.org/10.1103/PhysRev.36.823

[6] Möllenstedt, G., & Bayh, W. (1962). Messung der kontinuierlichen
Phasenschiebung von Elektronenwellen im kraftfeldfreien Raum durch das
magnetische Vektorpotential einer Luftspule. *Naturwissenschaften*, 49(4),
81–82. https://doi.org/10.1007/BF00622023

[7] Tonomura, A., Matsuda, T., Suzuki, R., Fukuhara, A., Osakabe, N., Umezaki,
H., Endo, J., Shinagawa, K., Sugita, Y., & Fujiwara, H. (1982).
Observation of Aharonov–Bohm effect by electron holography. *Phys. Rev.
Lett.*, 48(21), 1443–1446. https://doi.org/10.1103/PhysRevLett.48.1443

[8] Tonomura, A., Osakabe, N., Matsuda, T., Kawasaki, T., Endo, J., Yano, S.,
& Yamada, H. (1986). Evidence for Aharonov–Bohm effect with magnetic field
completely shielded from electron wave. *Phys. Rev. Lett.*, 56(8), 792–795.
https://doi.org/10.1103/PhysRevLett.56.792

[9] Osakabe, N., Matsuda, T., Kawasaki, T., Endo, J., Tonomura, A.,
Yano, S., & Yamada, H. (1986). Experimental confirmation of
Aharonov–Bohm effect using a toroidal magnetic field confined by a
superconductor. *Phys. Rev. A*, 34(2), 815–822.
https://doi.org/10.1103/PhysRevA.34.815

[10] Matteucci, G., & Pozzi, G. (1985). New diffraction experiment on the
electrostatic Aharonov–Bohm effect. *Phys. Rev. Lett.*, 54(23), 2469–2472.
https://doi.org/10.1103/PhysRevLett.54.2469

[11] Tonomura, A. (1999). *Electron Holography* (2nd ed.). Springer Series in
Optical Sciences, vol. 70. Springer-Verlag, Berlin.

[12] Strogatz, S. H. (2000). From Kuramoto to Crawford: exploring the onset of
synchronization in populations of coupled oscillators. *Physica D*, 143(1–4),
1–20. https://doi.org/10.1016/S0167-2789(00)00094-4

[13] Hasselbach, F. (1988). A ruggedized miniature UHV electron biprism
interferometer for new fundamental experiments and applications. *Z. Phys. B*,
71(4), 443–449. https://doi.org/10.1007/BF01313930

[14] Lichte, H., & Lehmann, M. (2008). Electron holography — basics and
applications. *Rep. Prog. Phys.*, 71(1), 016102.
https://doi.org/10.1088/0034-4885/71/1/016102

---

*Companion paper to: Bramble, J. (2026), "Many Clocks Interpretation of
Quantum Mechanics: Mass as Chiral Coupling, Re-synchronization in the Bulk as
Measurement." Preprint repository:
https://github.com/rayolddog/DiracKuramotoFramework*
