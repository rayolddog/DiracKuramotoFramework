# A Sidereal Search for Frame-Dependent Decoherence in the Quantum-Noise Floor of Gravitational-Wave Interferometers

**Claude Fable 5 (Anthropic)¹ and John Bramble, MD²**

*¹ AI system, Anthropic. ² Correspondence: jmbramblemd@gmail.com.*

*Status: development-phase draft (v0, 2026-07-06) — not for citation. Manuscript
form of the working note `LIGO_SIDEREAL_TEST_T5.md` (T5); pilot code and data
products in `t5_pilot/`; prior-constraints check in
`drafts/T5_CONSTRAINTS_CHECK.md`.*

## Author Contributions

**Claude (AI)** performed the prior-constraints literature survey, designed and
implemented the GWOSC pilot pipeline, executed the pilot analysis (including
the tidal-constituent decomposition), and wrote the manuscript, building on a
working note co-developed with J.B. across the T1–T5 test program. **J.B.**
conceived the research program the proposal descends from, set direction and
scope, and asked the two questions that materially shaped the analysis plan —
the feasibility question that scoped the pilot, and the tidal question that
exposed the K1 confound and its subtraction strategy. This paper is published
first on a public repository under an honest-workload authorship convention;
the byline will be adapted to any submission venue's policy, with this
paragraph retained as the record.

---

## Abstract

Every laboratory bound on Lorentz violation to date constrains the *unitary*
sector: coefficients of Hermitian operators in an effective Lagrangian
(Standard-Model Extension), tested through sidereal modulation of frequencies
and phases. The complementary possibility — Lorentz violation in the
*dissipative* sector, an anisotropy of decoherence rates locked to a cosmic
rest frame — is untabulated: the SME contains no Lindblad coefficients by
construction; existing open-system bounds (neutral kaons, astrophysical
neutrinos, collapse models) constrain additive, isotropic decoherence in free
propagation and have never been sidereally analyzed; and no published bound
exists on sidereal variation of any decoherence rate. We propose the first
search in this channel, at the macroscopic end of the quantum–classical
boundary: a sidereal-modulation analysis of the squeezing-limited quantum-noise
floor of gravitational-wave interferometers — a ~10 kg continuously monitored
quantum system with years of GPS-timed public data and, uniquely, a
multi-detector geometric phase discriminant no tabletop test possesses. A
pilot reanalysis of 20.6 days of public LIGO O3b Hanford strain (11,003
independent 128-s estimates of a band-limited quantum-noise proxy) measures
the raw per-sample scatter σ₁ = 2.7 × 10⁻², within 1.3× of our design
assumption before any auxiliary-channel regression; decomposes the ~2%
diurnal systematic into a solar-locked anthropogenic component (S1, peaking at
08:42 local time) and a genuinely tidal lunar component (M2 at 9σ, O1 at 13σ);
and identifies the K1 tidal constituent — whose period is exactly one sidereal
day — as the search's principal confound, together with its remedy: the
measured M2/O1 admittance predicts the K1 tidal contribution through fixed
potential ratios, allowing subtraction. With full multi-detector O3–O5 data
the search reaches fractional modulations of a few × 10⁻⁴, sufficient to
detect or exclude a vector (first-harmonic) frame coupling at the natural CMB
velocity scale β ≈ 1.2 × 10⁻³ down to ~10% of natural strength (a few percent
after regression); the quadratic tensor scale β² is out of reach, which we
state plainly. Amplitude, sidereal phase (CMB apex), inter-detector phase
offsets, and an 8% annual envelope are all fixed in advance: the search has no
free parameters to retune, and a null result cleanly bounds an otherwise
unprobed sector.

---

## 1. An untabulated channel

[Positioning against the three flanks, per the constraints check:]

**(a) The SME and its data tables are unitary by construction.** Kostelecký &
Russell's tables (RMP 83, 11; annually updated) span ~52 tables of coefficients
— every one multiplying a Hermitian operator in an action. Non-unitary Lorentz
violation has no coefficient there to bound.

**(b) The one sidereal LIGO instrument analysis is propagation-sector.**
Kostelecký, Melissinos & Mewes (PLB 761, 1 (2016)) sidereally binned LIGO
interferometer data to bound photon-sector coefficients (δn/n ≲ 10⁻¹⁹–10⁻²²) —
establishing that interferometer channels sidereal-bin to extreme fractional
precision, and leaving the *noise-floor/decoherence* observable untouched. The
present proposal is methodologically its descendant and physically its
complement.

**(c) Open-system bounds are additive, isotropic, and never sidereally
binned.** Kaon decoherence (CPLEAR/Ellis et al.: γ < 3.7 × 10⁻²¹ GeV; KLOE-2
ζ₀₀ ~ 10⁻⁷), IceCube neutrino decoherence (Γ₀ ≤ 1.17 × 10⁻¹⁵ eV), and CSL
collapse-rate bounds from GW detectors (λ < 3 × 10⁻⁸ s⁻¹, LISA Pathfinder) all
constrain a universal anomalous decoherence source acting in free propagation.
A coupling that *multiplicatively modulates environment-induced dissipation at
the measurement boundary* is invisible to all of them unless the ordinary
decoherence budget is itself resolved and sidereally binned — which has not
been done, anywhere. The KLOE ω-effect bound (|ω| ≲ 10⁻⁴), numerically below
our target, constrains an anomaly *in the preparation of an entangled state*;
the coupling searched for here acts *at detection* and does not feed ω.

The nearest existing dataset that could compete is the ³He/¹²⁹Xe
free-precession record (Allmendinger et al., PRL 112, 110801 (2014)), whose
amplitude-decay channel could be reanalyzed for sidereal T₂ modulation; no
such analysis is published. We encourage it as the tabletop companion to this
search.

## 2. Parametrization and targets

Write the total quantum-noise-limiting decoherence ("loss") of a continuously
monitored mode as

$$
L_{\rm tot}(t) = L_{\rm known} + L_X\,[\,1 + \varepsilon\, g(\hat n, t)\,],
$$

where $L_{\rm known}$ is the characterized loss budget, $L_X$ an anomalous
contribution of unknown (possibly zero) fraction $\xi = L_X/L_{\rm tot}$,
$\varepsilon$ the frame scale, and $g(\hat n, t)$ an order-unity geometric
projection of the detector's sensitive axis onto a fixed sky direction —
carrying the sidereal time dependence and differing between sites by their
known orientations. A preferred frame identified with the CMB rest frame
supplies two anisotropic scales: **vector**, $\varepsilon = \beta = v_{\rm
CMB}/c = 1.23\times10^{-3}$ (first sidereal harmonic), and **tensor**,
$\varepsilon = \beta^2 \approx 1.5\times10^{-6}$ (second harmonic). The
isotropic scalar $\Phi/c^2$ is absorbable and not a target.

The search is model-independent: any theory in which decoherence rates carry a
cosmic frame — anisotropic collapse models, Lindblad-sector Lorentz violation,
or measurement-sector preferred-frame proposals — populates $\varepsilon,
\xi$. One of us has developed a synchronization-based measurement framework
[companion: *Two Regimes of the Chiral Mass Coupling*] whose one added
postulate is exactly such a coupling, dormant in unitary evolution and active
only in the dissipative measurement stages; it motivated this search, and a
null bounds it. Nothing below depends on that framework's correctness.

## 3. Observable, statistics, and the pilot's measured inputs

The cleanest observable is the high-frequency, shot-noise-limited,
squeezing-enhanced strain PSD — purely quantum, cleanly modeled, and directly
degraded by any excess decoherence. A sinusoidal amplitude over $M$
independent samples resolves to $\sigma_1\sqrt{2/M}$.

**Pilot (this work; code public).** 20.59 days of O3b H1 public strain
(GWOSC), reduced to 11,003 band-median PSD estimates (1200–1450 Hz, 128 s
each, 79% duty), 3-day rolling-median detrend:

- **σ₁(raw) = 2.66 × 10⁻²** per 128-s sample — with *no* data-quality cuts
  beyond the science flag, no auxiliary-channel regression, no line handling.
  Design assumption 2 × 10⁻² (≈ 0.1 dB squeezing precision) is thus the
  post-regression target, and the raw number the demonstrated floor.
- Statistical floor after 20.6 detector-days: 3.6 × 10⁻⁴ (1σ).
- The systematic budget is *measured*, not assumed — next section.

Reach at 5σ, scaling from the raw σ₁ (post-regression values in parentheses):
6 months one detector ~1.3 × 10⁻³ (1 × 10⁻³); O4+O5 multi-detector, ~4
detector-years, ~5 × 10⁻⁴ (~1.5 × 10⁻⁴); optimistic coherent multi-detector
stack, ~10⁻⁴ range. Against the targets: the **vector** channel (signal
$\beta\,\kappa\xi \sim 1.2\times10^{-3}\,\kappa\xi$) is detectable or
excludable down to $\kappa\xi \sim 0.1$ raw, few × 10⁻² post-regression. The
**tensor** channel at β² is one to two orders below any achievable floor:
**out of reach, stated plainly.** The value of the search is the unprobed
channel and the macroscopic mass scale, not tensor-level sensitivity.

## 4. The systematic budget, measured

The pilot's diurnal systematic decomposes into named constituents (tidal-check
fit, condition number 3.1; 20.6 d separates lunar from solar lines via the
spring–neap beat):

| Constituent | Period | Amplitude | Significance | Origin |
|---|---|---|---|---|
| S1 (solar) | 24 h | 2.5 × 10⁻² | 27σ | anthropogenic/thermal (peaks 08:42 local) |
| S2 (solar) | 12 h | 1.6 × 10⁻² | 17σ | thermal harmonic + solar tide |
| M2 (lunar) | 12.421 h | 0.8 × 10⁻² | 9σ | **tidal** |
| O1 (lunar) | 25.819 h | 1.1 × 10⁻² | 13σ | **tidal** |

Two structural conclusions:

1. **The search is systematics-limited, and the limiting systematic is
   ~50× the statistical floor.** Solar/sidereal separation plus
   auxiliary-channel regression are the analysis, not refinements.
2. **K1 is the principal confound.** The lunisolar diurnal constituent K1 has
   period 23.9345 h — *exactly one sidereal day* — so a K1 tidal coupling
   cannot be separated from a true sidereal signal by period. The remedy is
   in the data: tidal constituents stand in fixed potential-amplitude ratios
   (K1/O1 ≈ 1.41 in the diurnal band), so the measured M2/O1 response
   calibrates the site's tidal admittance and *predicts* the K1 tidal
   amplitude for subtraction. The 9–13σ pilot detections of M2/O1 demonstrate
   this calibration is available. Residual-K1 discrimination then falls to
   the geometric keys below (K1 phase is set by local geography; its slow
   modulation is the 18.6-yr nodal cycle, not an annual envelope).

## 5. Design: the four pre-registered keys

A real frame signal must show, with **no free parameters**:

1. **Amplitude** $\kappa\xi\beta$ (vector) at the first sidereal harmonic;
2. **Sidereal phase locked to the CMB apex** (RA 11h12m, Dec −7°), not to any
   local or solar reference;
3. **Inter-detector phase offsets** fixed by the known orientations of H1, L1,
   Virgo, KAGRA — the discriminant no tabletop test has, and one no local
   systematic (including K1 tides, whose site phases follow the geoid rather
   than detector orientation) can mimic;
4. **An ~8% annual envelope** from Earth's 30 km/s orbital velocity adding
   vectorially to the 369 km/s CMB velocity, peaking on a fixed date.

Analysis protocol: segment PSDs in the squeezing-dominated band → quantum-noise
estimator per ~100 s → regress known classical contributions on
detector-characterization auxiliary channels → fit solar + sidereal + tidal
(M2, O1, with K1 predicted-and-subtracted) harmonic families jointly over
full observing runs → demand keys 2–4. Blind injection-and-recovery of
CMB-locked templates throughout. The "cheapest first look" — checking existing
LIGO spectral-line and stochastic-search sidereal products for an unexplained
apex-locked line — remains available to collaboration insiders at essentially
zero cost.

## 6. Falsification and outcomes

- **Signal** passing keys 1–4: measurement of $\kappa\xi$ at ~10 kg — a
  frame-bearing dissipative sector, at the macroscopic end of the
  quantum–classical boundary.
- **Null at the floor**: excludes a vector measurement-sector coupling at
  natural strength to ~10% (raw) / few % (regressed) — the first bound of any
  kind in this channel; the tensor channel remains open and is honestly
  labeled unreachable by this method.
- **Signal failing a key** (solar-locked, apex-unlocked, wrong inter-site
  phases, no annual envelope): systematic, identified as such by the same
  machinery.

## 7. Assumptions that remain theoretical

For the motivating framework specifically (not the model-independent search):
(i) the dormant-in-free-flight selectivity of the coupling must be derived,
else the closed propagation channel (b_n < 6.7 × 10⁻³⁴ GeV) already excludes
it; (ii) vector vs tensor character of the coupling decides reachability and
must be derived; (iii) a null bounds the product $\kappa\xi$, not $\kappa$
alone, absent a first-principles decoherence fraction; (iv) sidereal
coherence of the anomalous channel across the measurement band is assumed.
These are framework debts, stated so the search's model-independent value is
not confused with the framework's current standing.

## 8. Conclusion

There is an entire sector — dissipative, non-unitary Lorentz violation — in
which no experiment has ever looked for sidereal structure, and a free,
GPS-timed, multi-detector dataset in which to look. The pilot presented here
shows the noise is 1.3× the design assumption before any cleaning, measures
the systematic budget it must defeat, and converts this proposal's principal
confound into a calibrated subtraction. The search costs no new hardware,
carries four pre-registered keys and no tunable parameters, and its null is as
publishable as its signal.

---

## References (draft placeholders — to be completed)

- V. A. Kostelecký & N. Russell, Rev. Mod. Phys. 83, 11 (2011); arXiv:0801.0287 (2026 ed.).
- V. A. Kostelecký, A. Melissinos, M. Mewes, Phys. Lett. B 761, 1 (2016).
- J. Ellis et al. (CPLEAR), Phys. Lett. B 364, 239 (1995); KLOE-2, JHEP 04 (2022) 059; A. Di Domenico, ω-effect reviews (arXiv:1608.00241).
- IceCube Collaboration, Nature Physics (2024), arXiv:2308.00105; update arXiv:2507.12316.
- M. Carlesso et al., PRD 94, 124036 (2016); LISA Pathfinder, PRD 95, 084054 (2017).
- F. Allmendinger et al., PRL 112, 110801 (2014).
- H. Yu, L. McCuller et al., Nature 583, 43 (2020); C. Whittle et al., Science 372, 1333 (2021).
- GWOSC open data: R. Abbott et al., ApJS 267, 29 (2023).
- Tidal harmonics: A. T. Doodson, Proc. R. Soc. A 100, 305 (1921).
- [Companion framework paper: current_revision_DK_paper.md — "Two Regimes of the Chiral Mass Coupling."]
