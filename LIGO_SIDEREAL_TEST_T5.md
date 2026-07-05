# Suggested Experiment (T5): A Sidereal Search for Frame-Dependent Quantum-Noise Decoherence in a Gravitational-Wave Interferometer

*A macroscopic-mass test of the same preferred-frame measurement coupling probed by T2
(Suggested_experiment.md) and T4 (MRI/NMR surface relaxation). Where T2 reads the
**coherent** first step of Stage 2 on a GHZ probe, T5 reads the **dissipative** channel —
the anomalous, anisotropic decoherence of a continuously-measured macroscopic quantum
state — using LIGO/Virgo/KAGRA. Companion to PAPER_REVISED.md §3 (two-stage measurement),
§6 (candidate signature), and the open dissipation-channel loophole identified in the T4
literature check.*

Status: design + a-priori estimate. Numbers are order-of-magnitude; every assumption is
flagged. The postulate being tested (a frame-bearing vacuum/dissipation coupling, active
only in Stage 2) is NOT assumed true — the experiment bounds or detects it. **T5 is
weaker in raw sensitivity than T2 and shares T4's fatal caveat (no coherent amplifier),
but it has three things no tabletop test has: (i) months-to-years of GPS-timed continuous
data already on disk — zero new hardware; (ii) two-plus detectors at different
orientations, giving a built-in sidereal-phase discriminant against systematics; (iii)
the first data point at the genuinely macroscopic (~10 kg) end of the quantum–classical
boundary the paper flags (paper.tex §, "do cooled optomechanical membranes count?").**

---

## 1. What this tests

The framework's one new ingredient is a **non-covariant coupling dormant during free
(unitary) evolution that switches on only during measurement capture** (Stage 2). The
free-propagation channel for this coupling is closed brutally tight — sidereal Larmor
bounds give b_n < 6.7e-34 GeV (Allmendinger/Heil 2014) — so the effect *must* live in the
measurement/dissipation sector. T4's literature check established that the **dissipation
channel itself is untabulated**: the minimal SME is a unitary EFT, and non-unitary
(Lindblad) Lorentz violation has never been ported to a continuously-monitored
macroscopic oscillator.

A LIGO interferometer is exactly such an oscillator. Its differential arm mode (~10 kg
effective mass) is continuously measured at and below the standard quantum limit (SQL),
with squeezed vacuum injected to push the quantum-noise floor down. The *measured*
squeezing level is capped by optical loss and quantum decoherence. So T5 asks:

**Does the anomalous decoherence of a macroscopic, continuously-measured quantum state
carry an anisotropic component locked to the cosmic (CMB) rest frame, modulating the
quantum-noise floor at the sidereal period?** Standard QM + GR says no — local quantum
noise cannot depend on the absolute frame. A CMB-apex-locked sidereal modulation of the
squeezing-limited noise would be a signature of the **Vacuum Preferred-Frame Hypothesis**
(companion PAPER_REVISED §8) — the conjecture that the quantum vacuum carries a cosmic rest
frame — not a generic consequence of the framework: a null result is fully consistent with
the framework's conservative form, since the effect is contingent on that postulate. Its
value is that, *if* present, it tracks the sky, not the lab or the Sun, and so cannot be
calibrated away as a local systematic.

This is the **dissipation-sector** sibling of T2's coherent-phase test, at a mass scale
~10^27 times a single ion.

---

## 2. The prediction (calculation)

### 2.1 Coupling ansatz

The DK dissipation coupling adds an anomalous decoherence rate to the measured quantum
state during continuous capture. Write the total quantum-noise-limiting decoherence
("loss") as

    L_total(t) = L_known + L_DK * [1 + eps_frame * g(n_hat, t)]

- `L_known` — the characterized loss budget (optical losses, phase noise, mode mismatch).
- `L_DK`    — the anomalous (DK) contribution, a fraction xi_DK = L_DK / L_total of the
  total. UNKNOWN; could be zero. What a null bounds is the product kappa * xi_DK.
- `eps_frame` — the intrinsic frame scale (below).
- `g(n_hat, t)` — O(1) geometric factor: projection of the detector's sensitive axis
  `n_hat` (arm/squeezing-quadrature orientation) onto the CMB velocity direction; carries
  the sidereal time dependence. Differs between Hanford, Livingston, Virgo, KAGRA by their
  known orientations — this is the multi-detector discriminant.

**Why this is a boundary coupling, consistent with the companion.** The anomalous
loss L_DK acts during *continuous measurement* — the optical readout is an unbroken
Stage-2 boundary interaction — not on a freely-propagating mirror in isolation.
This matches the companion's stance that the vacuum's preferred-frame coupling
engages only at boundaries, never in free flight (PAPER_REVISED §2.5): the
gravitational-wave phase is accumulated coherently in flight (standard GR,
frame-independent), while the frame-dependent *decoherence* tested here is a
property of the measurement boundary, modulated sidereally by the readout-axis
orientation g(n_hat, t).

### 2.2 The frame scale (identical to T2/T4 — set by velocity, not potential)

A preferred frame supplies three candidate small parameters; only the anisotropic ones
modulate sidereally (a scalar gives a DC offset that is absorbable, hence NOT the signal):

| quantity | value | character | observable |
|---|---|---|---|
| beta = v/c (CMB dipole, 369 km/s) | 1.23e-3 | **vector** (sky direction) | 1st sidereal harmonic |
| beta^2 / 2                        | 7.6e-7  | **tensor / quadratic**     | 2nd sidereal harmonic |
| Phi/c^2 (cosmic potential)        | ~1e-5   | scalar (isotropic)         | DC only — absorbable |

So the testable modulation amplitude is **eps_frame = beta ~ 1.2e-3 (vector)** or
**beta^2 ~ 1.5e-6 (tensor)**. Same numbers as T2 and T4 — they are properties of the
postulate, not the platform.

### 2.3 No coherent amplifier (the structural difference from T2)

T2 wins a factor of N because a GHZ state turns a single-particle phase into a collective
phase N times larger. **LIGO's differential arm mode is a single collective coordinate —
effectively N = 1.** Like T4, the large mass amplifies the *magnitude* of the dissipative
term (a 10 kg mode couples to the vacuum far more strongly than one ion) but NOT the
*fractional* sidereal modulation, which stays at the bare beta or beta^2. This is the
load-bearing weakness; see §7.

### 2.4 The observable and required statistics

The cleanest observable is the **high-frequency, shot-noise-limited, squeezing-enhanced
strain PSD** (equivalently the measured squeezing level in dB) — it is purely quantum,
cleanly modeled, and any excess/modulated decoherence appears directly as reduced
squeezing. The predicted fractional modulation of this PSD is

    delta_PSD / PSD  ~  kappa * xi_DK * eps_frame * g(n_hat, t)

A sinusoidal-fit amplitude over M independent samples resolves to ~ sigma_1 * sqrt(2/M),
where sigma_1 is the per-sample fractional PSD/squeezing scatter.

Take sigma_1 ~ 2e-2 (≈0.1 dB squeezing precision per ~100 s segment), tau_sample = 100 s:

> **[Measured, 2026-07-05 — see t5_pilot/PILOT_RESULTS.md]** A pilot reduction of
> the first 4 days of O3b H1 open data (2,060 × 128-s chunks, 1200–1450 Hz
> band-median PSD) gives **sigma_1(raw) = 6.5e-2**, i.e. 3.3x the assumption —
> but with zero cleaning (no aux-channel regression, no DQ cuts, no line
> handling), so 2e-2 stands as the post-regression target and 6.5e-2 as the
> no-effort floor. The pilot also measures the diurnal classical systematic
> directly: A1 ≈ 8e-2 at both solar and sidereal periods (indistinguishable
> over 4 days), 40x the statistical floor — confirming §4's premise that the
> search is systematics-limited and the solar/sidereal separation + regression
> ARE the analysis. Reach rows below scale by 3.3x under raw noise; the vector
> target stays reachable, the tensor verdict is unchanged.

| Live time | M (independent samples) | 5-sigma fractional floor |
|---|---|---|
| 6 months (1 detector) | ~1.5e5 | ~3e-4 |
| ~2 yr (O4+O5, 2 detectors, 4 detector-yr) | ~1.3e6 | ~1e-4 |
| optimistic (multi-detector coherent stack, lower sigma_1) | — | ~few e-5 |

### 2.5 Predicted modulation vs reach — the targets

Setting kappa = 1 and the optimistic xi_DK ~ 1 (DK decoherence saturates the unexplained
loss budget; realistically xi_DK < 1, scaling the reach down):

**Vector coupling (eps = beta = 1.2e-3):**
the predicted modulation sits ~10x–50x ABOVE the achievable floor (1e-4 to few e-5).
=> **detectable / excludable down to kappa*xi_DK ~ a few percent of natural.** This is an
*exclusion* opportunity at unprecedented macroscopic mass — but a measurement-channel
vector LV at the 1e-3 level is large and likely already constrained by entanglement/Bell
data (same caveat as T2's vector case). The novelty is the mass regime and the free data,
not virgin discovery space.

**Tensor coupling (eps = beta^2 = 1.5e-6) — the natural target:**
the predicted modulation sits ~10x–100x BELOW even the optimistic floor.
=> **out of reach.** Same verdict as T4: without a coherent amplifier a 1e-6 fractional
modulation of the quantum-noise floor is not reachable by brute statistics.

**Headline:** T5 can probe the **vector** channel (macroscopic-scale exclusion, for free,
with a unique multi-detector phase discriminant) but **not** the natural **tensor**
channel. Its value is complementarity — same postulate, new mass scale, orthogonal
systematics — not raw sensitivity. T2 remains the discriminating test.

### 2.6 The sidereal phase and annual term (no free knob)

Locked to the **CMB dipole apex**: RA ~ 11h12m (168 deg), Dec ~ -7 deg.

- **First harmonic** (vector): one maximum per sidereal day at apex transit, phased by the
  detector's arm/quadrature azimuth and site latitude — DIFFERENT for H1, L1, Virgo, KAGRA.
- **Second harmonic** (tensor): two maxima per sidereal day (apex + antipode).
- **Annual envelope:** Earth's 30 km/s orbital velocity adds vectorially to the 369 km/s
  CMB velocity, modulating the sidereal amplitude by ~+/-8% (= 30/369) over the year,
  peaking on a fixed date. No free parameter to slide — amplitude fixed by beta/beta^2,
  phase fixed by the known apex and the known detector geometry.

---

## 3. Experimental design

**Platform.** Existing kilometer-scale interferometers operating with squeezed-vacuum
injection: LIGO Hanford (H1) + Livingston (L1), Virgo, KAGRA. The relevant quantum object
is the differential arm mode. Two prior LIGO results establish that this mode is a genuine
macroscopic quantum object: (a) quantum correlations between the *laser light* and the
40 kg mirrors, 3 dB below the SQL — Yu, McCuller et al., Nature 583, 43 (2020); and
(b) cooling of the combined ~10 kg differential mode near its motional ground state —
Whittle et al., Science 372, 1333 (2021). NB both are light–mirror correlation / cooling,
NOT mirror–mirror entanglement (see §6.1).

**The "measurement" being probed.** The interferometer *is* a continuous, repeatable
Stage-2 capture: the optical field continuously monitors the mirror motion and the readout
is irreversibly recorded. The anomalous frame-dependent decoherence, if present,
accumulates continuously and shows up in the quantum-noise floor.

**This is a reanalysis, not a new build.** Steps:
1. Take calibrated strain PSDs in the high-frequency, squeezing-dominated band, in short
   (~10–100 s) segments across full observing runs.
2. Reduce each segment to a quantum-noise estimator (squeezing level in dB, or band-limited
   shot-noise floor), with the known classical-noise contributions regressed out using the
   detector-characterization auxiliary channels.
3. Timestamp each segment with **local sidereal time** at each site.
4. Fit DC + 1st + 2nd sidereal harmonic; isolate the component phase-locked to the CMB
   apex; verify the ~8% annual envelope; require the **predicted phase OFFSET between H1,
   L1, Virgo, KAGRA** from their known orientations.

**Cheapest first look (do this before anything else).** The LIGO/Virgo collaboration
already builds sidereal-time-resolved analyses for continuous-wave and stochastic-
background searches (a real astrophysical signal is sidereal), and maintains spectral
line lists. The free first check: **is there any unexplained sidereal line in the
quantum-noise band that tracks the CMB apex (RA 11h12m) rather than the galactic or solar
references, with the right inter-detector phase relationship?** This is the LIGO analogue
of T4's "check the comagnetometer-cell T2 first."

---

## 4. Systematics and controls

- **Scattered light, thermal drift, alignment, microseism** — the dominant fake-periodic
  sources. Most follow the **solar** 24h00m day or the local environment, NOT the 23h56m04s
  sidereal day; over a months-long run they separate by a full cycle. This is the core
  defense (same as T2/T4).
- **Multi-detector phase as the killer discriminant.** A real DK signal tracks the sky, so
  H1, L1, Virgo, KAGRA must show the apex-locked harmonic with the specific relative phases
  set by their geographic orientations. No local systematic reproduces that geometry — this
  is the discriminant tabletop tests cannot have.
- **Regress on auxiliary channels** to remove classical noise that couples to the quantum
  band; the quantum (squeezing) floor is the clean target precisely because it is purely
  quantum.
- **Blind injection-and-recovery** of a CMB-locked template to avoid confirmation bias on a
  sub-1e-3 modulation.
- **Annual envelope as a second key.** A residual sidereal line is only the DK signal if it
  also carries the +/-8% annual modulation peaking on the predicted date.

---

## 5. Falsification

With kappa and the vector/tensor structure specified, the framework predicts:
1. a fractional quantum-noise modulation kappa*xi_DK*beta (vector) or *beta^2 (tensor),
2. at the CMB-apex sidereal phase,
3. with the predicted inter-detector phase offsets, and
4. a ~8% annual envelope peaking on a fixed date.

Outcomes:
- **Signal at predicted amplitude + apex phase + inter-detector geometry + annual
  envelope** -> support; measure kappa*xi_DK at macroscopic mass.
- **Null below the floor** -> excludes the **vector** coupling at the few-percent-of-natural
  level at ~10 kg mass (the tensor coupling is out of reach, so a null there is
  uninformative — state this honestly).
- **Signal at the solar period, or not apex-locked, or wrong inter-detector phase**
  -> systematic, not physics.

No knob to retune: amplitude and phase are fixed by known quantities.

---

## 6. Relation to the framework

- T5 probes the **dissipative tail** of Stage 2 (a variance/rate), where T2 probes the
  **coherent first step** (a mean phase). They are the two channels named in the T4
  literature note; running both at different mass scales and with orthogonal systematics is
  the strongest combined statement the program can make.
- T5 is the first test at the **macroscopic** end of the Heisenberg cut. PAPER_REVISED/
  paper.tex explicitly leave open "where exactly is the boundary — do cooled optomechanical
  membranes count?" A 10 kg differential mode near its ground state is squarely in that
  zone, so a clean null *or* signal is interpretable for the boundary question itself.
- This sits in the same Penrose–Diósi neighborhood the paper already cites (optomechanical
  Penrose tests), but T5 looks for an **anisotropic sidereal** signature, not a
  mass-threshold collapse rate — a different observable from the same macroscopic-quantum
  hardware. (See [[project_penrose_alignment]].)

### 6.1 Two variants noted, not recommended as the primary

- **(B) Macroscopic mirror-entanglement Bell test.** The literal "Bell on LIGO": entangle
  two ~10 kg mirror modes via a shared optical field, then test whether the entanglement's
  survival modulates with the apex ([[project_bell_two_stage]]). **Status check (2026-06-17):
  this has NOT been done.** Two massive mirrors have never been entangled *with each other*;
  LIGO's realized quantum correlation is light–mirror, not mirror–mirror (Nature 583, 43,
  2020). The genuine oscillator–oscillator entanglement demonstrations are ~70-picogram
  drumhead membranes — Kotler et al., Science 372, 622 (2021); Mercier de Lépinay et al.,
  Science 372, 625 (2021) — roughly **14 orders of magnitude lighter** than a LIGO mirror. So
  (B) is purely aspirational: the picogram→10 kg gap is enormous, AND it inherits T1's verdict
  (flagship, hardest, rests on the **underived** term H' ~ g(d·H_hat)phi_bulk). The
  *light–mirror* correlation that HAS been realized is, by contrast, exactly the continuous
  Stage-2 capture that the primary T5 test (§1) reads — which is why T5 uses the quantum-noise
  floor, not a two-mirror Bell pair.
- **(C) The gravitational wave itself as a substrate perturbation — DEAD END.** Reading a
  passing GW as a coherent oscillation of the vacuum substrate that modulates the sync rate
  fails twice: coupling the GW to the sync *phase* is a propagation-sector effect (closed by
  b_n < 6.7e-34), and h ~ 1e-21 is far too small to modulate a decoherence rate. This is the
  LIGO version of the repudiated Gamma = GM^2/(hbar*dz) dimensional artifact (§4.4). Do not
  pursue.

---

## 7. What must still be derived (do not skip)

1. **Stage-2-only selectivity.** Same linchpin as T2/T4: derive why the coupling is dormant
   in free evolution (else excluded by b_n < 6.7e-34). Decisive.
2. **Vector vs tensor.** The whole feasibility (beta ~ 1e-3 reachable vs beta^2 ~ 1e-6 out
   of reach) hinges on the coupling's symmetry. Derive which the chiral-mass/dissipation
   coupling produces.
3. **kappa AND xi_DK from first principles.** T5 bounds the *product* kappa*xi_DK. Without a
   predicted DK fraction of the loss budget, a null bounds a product, not kappa alone —
   weaker than T2, where the GHZ phase isolates kappa.
4. **Is the dissipative channel even sidereally coherent over the band?** If the anomalous
   decoherence has no stable phase relationship to the apex across the measurement band, the
   signal smears and the (already marginal) reach collapses. This is the dissipation-channel
   analogue of T2's coherent-first-step linchpin.

---

*Bottom line: a zero-hardware reanalysis of existing squeezed-light GW-interferometer data
can search for a CMB-apex-locked sidereal modulation of the macroscopic quantum-noise
floor, with a multi-detector phase discriminant no tabletop test has. It can exclude the
**vector** coupling at the few-percent-of-natural level at ~10 kg mass, but the natural
**tensor** target (beta^2 ~ 1e-6) is out of reach — the same no-coherent-amplifier wall as
T4. T5's worth is complementarity and the first macroscopic-mass data point on the
Heisenberg-cut boundary, not raw sensitivity. Run the free sidereal-line check first; it
is only as meaningful as the four derivations above, of which (1) and (4) are decisive.*
