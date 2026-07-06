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
128-s estimates of a band-limited quantum-noise proxy) delivers the search's
design inputs as measurements: the raw per-sample scatter is σ₁ = 2.7 × 10⁻²,
within 1.3× of our design assumption before any auxiliary-channel regression;
the ~2% diurnal systematic decomposes into a solar-locked component peaking at
workday onset (08:42 local) plus lunar constituents (M2, O1) whose point
amplitudes suggest a genuinely tidal share — though with red-noise-honest
error bars (residual autocorrelation time ≈ 5.5 h, N_eff ≈ 70) no constituent
exceeds 2.2σ at this baseline, so the attribution is suggestive rather than
established, and the pilot sets **no sidereal bound** (the solar and sidereal
regressors remain collinear over 20 days by design). The pilot's structural
lesson is thus quantitative: the analysis is red-noise limited, and
auxiliary-channel whitening is a precondition, not a refinement. We identify
the K1 tidal constituent — whose period is exactly one sidereal day — as the
search's principal confound, note that the adjacent P1 constituent gives the
diurnal tidal line a natural annual envelope that partially mimics the
CMB-orbital key, and specify the required treatment: a joint diurnal-band
admittance fit (K1, P1, S1, O1) with free-core-nutation-aware priors, rather
than naive potential-ratio subtraction. With full multi-detector O3–O5 data
and demonstrated whitening, the search reaches 5σ fractional modulations of
~1.7 × 10⁻⁴ (raw-noise scaling; ~1.2 × 10⁻⁴ at the post-regression target),
i.e. a vector (first-harmonic) frame coupling at the natural CMB velocity
scale β ≈ 1.2 × 10⁻³ is detectable or excludable down to ~10–15% of natural
strength, with a few percent reachable only under an optimistic coherent
multi-detector stack; the quadratic tensor scale β² is out of reach, which we
state plainly. Amplitude, sidereal phase (CMB apex), inter-detector phase
offsets, and the annual envelope are fixed in advance: the search has no free
parameters to retune, and a null result cleanly bounds an otherwise unprobed
sector.

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
decoherence budget is itself resolved and sidereally binned — which, to the
best of our knowledge after a dedicated literature search across the SME
tables, the open-system LV literature, sidereal entanglement/coherence
analyses, LIGO instrumental analyses, and collapse-model bounds, has not been
done anywhere (`drafts/T5_CONSTRAINTS_CHECK.md` documents the search). The KLOE ω-effect bound (|ω| ≲ 10⁻⁴), numerically below
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

**What "decoherence" means here, operationally.** A quantum-noise referee
will correctly note that at kilohertz frequencies reduced squeezing is
bookkept as *optical loss and phase noise on the light* — a beamsplitter
vacuum admixture — not as decoherence of the mirror mode, and that the ~10 kg
differential arm mode is quantum-radiation-pressure-relevant below ~100 Hz
(the regime of Yu et al. 2020 and Whittle et al. 2021), not in our band. We
accept both points and define the observable accordingly: the target is an
**anomalous, sidereally modulated loss channel in the squeezed-state budget**
of a continuously monitored interferometer — "decoherence" in the operational
sense of unaccounted vacuum admixture into a macroscopic apparatus's quantum
readout. The macroscopic-mass significance is then indirect but real: the
squeezed field is entangled with a 10 kg mechanical system under continuous
measurement, and an anomalous measurement-sector coupling anywhere in that
loop modulates the recorded noise floor. We also restore here the structural
sensitivity fact the working note carried: the differential arm mode is a
*single collective coordinate* — effectively N = 1, with no GHZ-type coherent
amplifier — which is precisely why the tensor (β²) target is unreachable by
brute statistics and the vector target is the honest ceiling of this method.

The search is model-independent: any theory in which measurement-sector
dissipation carries a cosmic frame — anisotropic collapse models,
Lindblad-sector Lorentz violation, or measurement-sector preferred-frame
proposals — populates $\varepsilon, \xi$. One of us has developed a synchronization-based measurement framework
[companion: *Two Regimes of the Chiral Mass Coupling*] whose one added
postulate is exactly such a coupling, dormant in unitary evolution and active
only in the dissipative measurement stages; it motivated this search, and a
null bounds it. Nothing below depends on that framework's correctness.

## 3. Observable, statistics, and the pilot's measured inputs

The observable is the high-frequency, shot-noise-limited, squeezing-enhanced
strain PSD, reduced to a band statistic. The pilot's band-median proxy is
*not* purely quantum — its measured 2% diurnal modulation is classical
non-stationarity leaking into the band — which is exactly why the analysis
plan treats auxiliary-channel regression as a precondition (§4–5). A
sinusoidal amplitude over $M_{\rm eff}$ *effectively independent* samples
resolves to $\sigma_1\sqrt{2/M_{\rm eff}}$; the distinction between raw and
effective sample counts is load-bearing (below).

**Pilot (this work; code public).** 20.59 days of O3b H1 public strain
(GWOSC), reduced to 11,003 band-median PSD estimates (1200–1450 Hz, 128 s
each, 79% duty), 3-day rolling-median detrend. Methods for the reproducer:
GPS window 1256655618 + 30 d (166 four-ks file-blocks unavailable
server-side, 2019-11-21→12-01, skipped); 4-s median-Welch PSDs; σ₁ is the
MAD-robust scatter of the fractional band-median deviation;
science-flag-only selection. Results:

- **σ₁(raw) = 2.66 × 10⁻²** per 128-s sample — with *no* data-quality cuts
  beyond the science flag, no auxiliary-channel regression, no line handling.
  Design assumption 2 × 10⁻² (≈ 0.1 dB squeezing precision) is thus the
  post-regression target, and the raw number the demonstrated floor.
- **Residual autocorrelation is severe and quantified**: integrated
  autocorrelation time τ ≈ 156 samples (≈ 5.5 h), so the pilot's N_eff ≈ 70
  of 11,003, and its unwhitened statistical floor is 4.5 × 10⁻³ — not the
  naive 3.6 × 10⁻⁴. Whitening (regression to near-white residuals) is what
  converts calendar time into sensitivity; demonstrating it on auxiliary
  channels is the first task of the full analysis.
- The systematic budget is *measured*, not assumed — next section.
- **No sidereal bound is claimed from the pilot**: over 20 days the solar and
  sidereal first harmonics are collinear (joint-fit condition number 470);
  their separation was never the pilot's deliverable.

Reach at 5σ, assuming whitened residuals (so M_eff → M), from
σ₁ = 2.66 × 10⁻² raw (post-regression target σ₁ = 2 × 10⁻² in parentheses):
6 months one detector, M ≈ 1.5 × 10⁵: **4.9 × 10⁻⁴** (3.7 × 10⁻⁴); O4+O5
multi-detector, ~4 detector-years, M ≈ 1.3 × 10⁶: **1.7 × 10⁻⁴**
(1.2 × 10⁻⁴); optimistic coherent multi-detector stack: few × 10⁻⁵. Against
the targets: the **vector** channel (signal $\beta\,\kappa\xi \sim
1.2\times10^{-3}\,\kappa\xi$) is detectable or excludable down to $\kappa\xi
\approx 0.14$ raw / $0.10$ at the regression target, reaching a few percent
only under the coherent-stack assumption. The **tensor** channel at β² is one
to two orders below any achievable floor: **out of reach, stated plainly** —
the structural reason being the N = 1 absence of a coherent amplifier (§2).
The value of the search is the unprobed channel, not tensor-level
sensitivity.

## 4. The systematic budget, measured

The pilot's diurnal systematic decomposes into named constituents (tidal-check
fit over the full 20.59-d span; design condition number 3.1 — lunar and solar
lines separate via the ~15-d spring–neap beat). Significances are given both
naively (white-residual assumption) and corrected for the measured residual
autocorrelation (τ ≈ 156 samples ⇒ every σ inflates by √τ ≈ 12.5):

| Constituent | Period | Amplitude (point est.) | Naive | **Corrected** | Candidate origin |
|---|---|---|---|---|---|
| S1 (solar) | 24 h | 2.5 × 10⁻² | 27σ | **2.2σ** | anthropogenic/thermal (peaks 08:42 local) |
| S2 (solar) | 12 h | 1.6 × 10⁻² | 17σ | **1.4σ** | thermal harmonic + solar tide |
| M2 (lunar) | 12.421 h | 0.8 × 10⁻² | 9σ | **0.7σ** | tidal |
| O1 (lunar) | 25.819 h | 1.1 × 10⁻² | 13σ | **1.0σ** | tidal |

With honest error bars, **no constituent is individually established at this
baseline**: the residuals are red (5.5-h correlation time), and against red
noise a 20-day record cannot certify even the 2.5% daily line, let alone the
lunar share. We present the decomposition as what it is — point estimates
whose pattern (workday-onset solar phase; nonzero lunar-period amplitudes) is
*consistent with* a mixed anthropogenic + tidal origin — and as a
demonstration that the constituent-fitting machinery works. Certifying the
decomposition requires whitening; that is the same precondition the reach
table already carries, arrived at independently.

Two structural conclusions survive unchanged:

1. **The search is red-noise/systematics-limited.** Whitening via
   auxiliary-channel regression is the analysis, not a refinement — the
   pilot now states this as a measured fact (τ, N_eff), not a caution.
2. **K1 is the principal confound, and its treatment must be a joint fit,
   not a ratio subtraction.** The lunisolar diurnal constituent K1 has period
   23.9345 h — *exactly one sidereal day* — so a K1 tidal coupling cannot be
   separated from a true sidereal signal by period. We do **not** propose
   predicting K1 from other constituents by bare potential ratios: (i) the
   free-core-nutation resonance sits in the diurnal band adjacent to K1,
   making its admittance anomalous relative to O1 (Wahr); (ii) M2 is
   semidiurnal — different Love numbers and ocean loading — and cannot
   calibrate the diurnal band; (iii) instrumental coupling paths (e.g.,
   tidal-actuator activity into alignment) need not be linear in the
   potential. The required treatment is an **empirical joint fit of the
   diurnal-band family (K1, P1, S1, O1) with FCN-aware admittance priors**,
   over baselines long enough to separate the family members. P1 matters
   doubly: the K1+P1 beat (2 cycles/yr, potential ratio ≈ 0.33) endows the
   diurnal tidal line with a natural ~±30% annual envelope — so an annual
   envelope alone does *not* certify the CMB-orbital origin (key 4 below is
   correspondingly weakened from "unfakeable" to "distinguishing in
   conjunction with phase and geometry": the CMB envelope has a specific
   phase date and the same amplitude at every site, the K1/P1 beat does not).

## 5. Design: the four pre-registered keys

A real frame signal must show, with **no free parameters**:

1. **Amplitude** $\kappa\xi\beta$ (vector) at the first sidereal harmonic;
2. **Sidereal phase locked to the CMB apex** (RA 11h12m, Dec −7°), not to any
   local or solar reference;
3. **Inter-detector phase offsets** fixed by the known orientations of H1, L1,
   Virgo, KAGRA — the discriminant no tabletop test has. For a projection
   ansatz $g(\hat n, t) = (\hat n \cdot \hat u_{\rm apex}(t))^2$, with $\hat
   n$ the coupling's sensitive axis in the local frame, the sidereal phase at
   each site is set by its latitude and the axis azimuth, whereas the K1
   body-tide phase follows site *longitude* (Greenwich phase lag) — two
   different, computable phase patterns across the network. **Honesty note:
   the sensitive axis $\hat n$ for a squeezing-loss coupling (arm bisector?
   squeezer injection path?) is not yet derived from any microscopic model;
   producing $g$ and the predicted four-site phase table is a prerequisite
   for the full analysis and is listed in §7.** Until then this key is a
   design requirement, not a computed prediction;
4. **An annual envelope** from Earth's 30 km/s orbital velocity adding
   vectorially to the 369 km/s CMB velocity: ±8%, peaking on a fixed date,
   *identical at every site*. As §4 notes, the K1+P1 tidal beat also produces
   an annual envelope (~±30%, site-dependent, different phase date), so key 4
   discriminates only jointly with keys 2–3 — the fixed date and the
   site-universality are the operative content.

Analysis protocol: segment PSDs in the squeezing-dominated band → quantum-noise
estimator per ~100 s → regress known classical contributions on
detector-characterization auxiliary channels → fit solar + sidereal + tidal
(the diurnal family K1, P1, S1, O1 fit jointly with FCN-aware admittance
priors, plus M2) harmonic families over
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

For the search itself, two analysis debts stand between this proposal and a
collaboration-ready method paper: (v) the coupling's sensitive axis $\hat n$
and hence the explicit $g(\hat n, t)$ with its predicted four-site sidereal
phase table (§5, key 3); and (vi) a demonstration, on real auxiliary-channel
data, that regression whitens the band statistic to near-independence at the
128-s scale — the pilot's measured τ ≈ 5.5 h is the number this must beat,
and every reach figure in §3 is conditional on it.

## 8. Conclusion

There is an entire sector — dissipative, non-unitary Lorentz violation — in
which, to our knowledge, no experiment has ever looked for sidereal
structure, and a free, GPS-timed, multi-detector dataset in which to look.
The pilot presented here shows the noise is 1.3× the design assumption before
any cleaning; measures, with red-noise-corrected error bars, the systematic
budget the search must defeat and the whitening requirement that defines the
analysis; and names the principal confound (K1, with its P1 annual beat)
together with the joint-fit treatment it requires. The search costs no new
hardware, carries four pre-registered keys and no tunable parameters, and its
null is as publishable as its signal.

---

## Figures

Working figures accompany the pilot code: `t5_pilot/figures/timeseries.png`
(fractional band-PSD deviation over the 20.6-d span),
`t5_pilot/figures/fold_sidereal.png` and `fold_solar.png` (binned folds with
harmonic fits — visually near-identical, the collinearity statement in
pictures). Publication figures (constituent decomposition with corrected
error bars; reach-vs-baseline) are a packaging task on existing outputs.

## References (draft placeholders — to be completed)

- V. A. Kostelecký & N. Russell, Rev. Mod. Phys. 83, 11 (2011); arXiv:0801.0287 (2026 ed.).
- V. A. Kostelecký, A. Melissinos, M. Mewes, Phys. Lett. B 761, 1 (2016).
- J. Ellis et al. (CPLEAR), Phys. Lett. B 364, 239 (1995); KLOE-2, JHEP 04 (2022) 059; A. Di Domenico, ω-effect reviews (arXiv:1608.00241).
- IceCube Collaboration, Nature Physics (2024), arXiv:2308.00105; update arXiv:2507.12316.
- M. Carlesso et al., PRD 94, 124036 (2016); LISA Pathfinder, PRD 95, 084054 (2017).
- F. Allmendinger et al., PRL 112, 110801 (2014).
- H. Yu, L. McCuller et al., Nature 583, 43 (2020); C. Whittle et al., Science 372, 1333 (2021).
- M. Tse et al., *Quantum-Enhanced Advanced LIGO Detectors in the Era of Gravitational-Wave Astronomy*, PRL 123, 231107 (2019) — squeezing operational in O3. L. McCuller et al., PRD 104, 062006 (2021) — O3 squeezing/loss budget.
- GWOSC open data: R. Abbott et al., ApJS 267, 29 (2023).
- Tidal harmonics: A. T. Doodson, Proc. R. Soc. A 100, 305 (1921); J. M. Wahr, Geophys. J. R. astr. Soc. 64, 677 (1981) — FCN resonance in the diurnal admittance.
- [Companion framework paper: current_revision_DK_paper.md — "Two Regimes of the Chiral Mass Coupling."]
