# T5 pilot results — stages 1–4 (O3 H1)

## Stage 4 completion (2026-07-16): whitened sidereal fit on the full v2 baseline

The 8-band re-stream on disk had grown past the 48.3 d documented below to
**85.9 d (39,653 chunks**, GPS 1238166082→1245589440) before the GWOSC fetch
failures stopped it — but the analysis was never re-run on the fuller set, and
the data sat uncommitted. This section completes stage 4 on the data already on
disk (no new streaming): re-run the whitening on the full v2 baseline, then run
the sidereal + solar/lunar-tidal fit on **both** raw and whitened b7, so the
whitening is measured at the level of the actual κξ bound, not just N_eff.
Script: `whiten_fold.py` (combines `whiten_test.py` whitening with the
`fold_diurnal.py` constituent fit); plot `plots/sidereal_whitened_fit.png`.

**Whitening on 85.9 d** (was 48.3 d): b1–b6 regression removes **66%** of b7's
classical variance; autocorrelation τ **3.5 h → 2.0 h**, N_eff **406 → 706
(×1.7)** → amplitude reach ×1.3. Consistent with the 48-d method test, slightly
better with the longer baseline.

**The new result — whitening improves the sidereal bound itself, matched fit:**

| b7 on the same 85.9 d | sidereal 1st amp | significance | 95% UL | κξ (vector) UL |
|---|---|---|---|---|
| raw | 1.67 × 10⁻² | 1.1σ | 4.20 × 10⁻² | **34.2** of natural |
| whitened (− regression on b1–b6) | 0.86 × 10⁻² | 1.3σ | 1.98 × 10⁻² | **16.1** of natural |

**Whitening tightens the bound ×2.1** on identical data/baseline/fit. That is
*more* than the ×1.3 the √N_eff error-shrink alone predicts, because whitening
also **halves the sidereal amplitude point estimate** (1.67 → 0.86 × 10⁻²): it
removes classical power that was sitting in the sidereal band, not just noise
around it — exactly the desired behaviour, since a genuine DK quantum-noise
modulation lives in b7/b8 (correlation +0.83) and not in the classical
regressors b1–b6. Both fits remain non-detections consistent with zero, and the
fold peaks ~9 h from the CMB apex (LST 19.9 h raw / 20.5 h whitened vs apex
11.2 h) — noise phase at this significance, not apex-locked.

**Honest caveat — this does NOT supersede the pilot bound.** Over 85.9 d the
design condition number is **653** (raw and whitened alike — whitening changes
the data, not the design matrix): solar, sidereal, and P1 are still collinear at
this baseline, so κξ < 16 is *not* competitive with the definitive 256.8-d v1
fit (condition 5.4, **κξ < 5.3**, the "Definitive diurnal-band fit" section
below). The v2 result is a **method result**: it demonstrates the whitening
propagates through to the bound at ~×2. Projecting that factor onto the v1
baseline suggests a whitened full-baseline bound near **κξ ~ 2–3** — an
improvement on 5.3 but still *above* natural (κξ = 1), consistent with stage 4's
softened expectation (nearer 5/2 than the old optimistic 0.2–0.4). Reaching
natural strength still needs the full 256.8-d baseline re-streamed in 8-band
form (blocked on unmetered bandwidth) or the collaboration's internal aux
channels — unchanged from below.

---

## Stage 4 (2026-07-08): multi-band data + whitening proof-of-concept — PARTIAL

The 8-band re-stream reached **48.3 d (20,344 chunks)** before GWOSC returned
5,211 consecutive fetch failures for the bulk of the later window (server-side;
resumable — needs unmetered wifi, not the data-capped hotspot). Enough to answer
the **gating question** with zero further streaming (`whiten_test.py`): does
regressing the quantum band (b7, 1200–1450 Hz) on the six auxiliary bands
(b1–b6, 25–950 Hz) whiten the red noise?

| quantity | raw b7 | whitened (b7 − regression on b1–b6) |
|---|---|---|
| σ₁ | 2.12 × 10⁻² | **1.57 × 10⁻²** (−26%) |
| autocorrelation time τ | 3.5 h | **2.2 h** |
| N_eff (of 20,344) | 209 | **322** |

- Classical variance removed by the b1–b6 regression: **70%**.
- N_eff gain **×1.5 → amplitude reach improves ×1.2** — *not* the ~×3 the
  manuscript's reach table optimistically assumed for "fully whitened."
- b7–b8 quantum-band correlation **+0.85** (sanity: a real modulation must
  appear in both quantum bands; they track together).

**Honest implication.** Simple *instantaneous linear* proxy whitening from
strain bands removes most of the classical *power* but only partly shortens the
*correlation time* — residual red noise (2.2 h) survives, so the reach gain is
modest. Closing the rest likely needs either (i) time-lagged / spectral
whitening rather than instantaneous regression, or (ii) the collaboration's
internal detector-characterization auxiliary channels (not available in public
GWOSC strain). **The manuscript's reach numbers that assumed M_eff → M under
whitening should be softened**: realistic proxy whitening buys ~×1.2–1.5 in
N_eff on this baseline, so κξ likely settles nearer the current ~5 than the
projected ~0.2–0.4 until better whitening or real aux channels are brought in.
(48 d is a method test only — too short to separate solar from sidereal.)

---


## Definitive diurnal-band fit (2026-07-07, `fold_diurnal.py`) — the pilot's scientific bound

Full solar + lunar-tidal family fit on the 256.8-d dataset (108,810 chunks),
well-conditioned (design condition 5.4 — the lines separate over 8.5 months),
red-noise-honest errors (τ = 3.3 h, N_eff = 1163). σ₁ = 1.98×10⁻² (= design
assumption). Constituents (amplitude, red-noise σ):

| Line | Period | Amplitude | Significance |
|---|---|---|---|
| **sidereal 1st (= K1, vector target)** | 23.9345 h | 2.9 × 10⁻³ ± 2.2 × 10⁻³ | **1.3σ** |
| sidereal 2nd (tensor) | 11.967 h | 0.9 × 10⁻³ | 0.5σ |
| S1 solar | 24.000 h | 5.2 × 10⁻³ | 2.2σ |
| S2 solar | 12.000 h | 2.5 × 10⁻³ | 1.3σ |
| P1 (K1's annual-beat partner) | 24.066 h | 2.2 × 10⁻³ | 1.0σ |
| O1 / M2 (lunar) | 25.82 / 12.42 h | 1.3 / 1.6 × 10⁻³ | 0.7 / 0.9σ |

**The bound:** the sidereal line is consistent with zero (1.3σ); one-sided 95%
UL = 6.5 × 10⁻³ → **κξ (vector) < 5.3 of natural strength**. This is *the*
defensible pilot number — slightly weaker than the stage-3 quick-fit value
(~4.7) because the full tidal family (P1, O1, M2), being partially correlated
with the sidereal line, is now properly de-confounded, and because it is
conservative by construction (the sidereal line still *contains* any K1 tide,
period-degenerate with it). Nothing is significantly detected; even the
anthropogenic solar S1 is only 2.2σ once red noise is honored.

**Phase curiosity, flagged and quarantined:** the sidereal fold peaks at
LST ≈ 10.2 h, ~1 h from the CMB apex transit (11.2 h) — visually the maximum
sits near the apex line (see `plots/sidereal_diurnal_fit.png`). This is *not
significant*: at 1.3σ the phase uncertainty is ±several hours, and noise peaks
somewhere. Recorded only because it is exactly the coincidence whitening must
test — if the peak survives real error bars at the apex phase, it becomes
interesting; today it is noise that happens to land near the apex.

**Status vs the framework:** κξ < 5.3 is still *above* natural (κξ = 1), so the
VPFH is neither supported nor constrained. The gap is red noise: N_eff is 1163
of 108,810 (τ = 3.3 h). Whitening (stage 4) is the only lever that closes it —
the sensitivity is limited by residual autocorrelation, not by calendar time.

---


## Stage 3 (2026-07-07): 8.5 months — first valid solar/sidereal separation

108,810 chunks spanning 256.8 d (O3a complete + O3b through 2019-12-14; the
Dec–Mar tail hit 2,014 consecutive fetch failures — likely rate-limiting after
~150 GB overnight — and is retryable). Joint-fit condition number **3.4**: the
two periods are now fully decorrelated. Autocorrelation on this baseline:
τ = 95 chunks (3.4 h), N_eff = 1,145; corrected errors = naive × 9.75.

| Quantity | Value | Corrected significance |
|---|---|---|
| σ₁(raw) | **2.04 × 10⁻²** | — (matches the design assumption 2 × 10⁻²) |
| joint solar A₁ | 6.43 × 10⁻³ (phase → max 07:06 local) | 3.1σ |
| joint sidereal A₁ | **2.41 × 10⁻³ ± 2.05 × 10⁻³** | **1.2σ — consistent with zero** |
| solar S1 (tidal fit) | 5.83 × 10⁻³ | 3.0σ |
| S2 / M2 / O1 | 2.6 / 1.8 / 1.2 × 10⁻³ | 1.3σ / 0.9σ / 0.6σ |

**First bound in the channel (weak but real):** the sidereal-period amplitude
is consistent with zero; the one-sided 95% upper limit is A₁(sid) < 5.8 × 10⁻³,
i.e. **κξ < ~4.7 of natural vector strength** (taking g ~ 1; note this
sidereal-period band *includes* any K1 tidal coupling, so it is conservative).
Not yet at natural strength (κξ = 1) — the unwhitened corrected floor is
8.5 × 10⁻⁴ vs the naive 8.7 × 10⁻⁵: **whitening is worth a factor ~10 in
N_eff (√ → ~3 in amplitude) and remains the gate.** With demonstrated
whitening this same dataset would probe κξ ≈ 0.2–0.4.

Phase note, stated with appropriate flatness: the measured sidereal phase
(187° ± ~49°) is 19° from the CMB-apex transit prediction (168°). At 1.2σ
amplitude this is uninformative — recorded only as a demonstration that the
apex-phase key is now a computable check in the pipeline.

Diurnal picture at this baseline: the systematic is dominantly solar
(6.4 × 10⁻³, max at 07:06 local — workday onset), the lunar constituents
remain individually unestablished (<1σ corrected), and the amplitudes are ~4×
smaller than the 20-d estimates — consistent with partial seasonal averaging
of a non-stationary daily systematic.

Next: (i) retry the Dec–Mar tail; (ii) add P1 + apex-locked template to the
constituent fit; (iii) whitening attempt — requires multi-band re-reduction
(regressor bands were not stored in v1; a v2 reducer storing 3–4 auxiliary
bands per chunk would enable strain-derived proxy regression at the cost of
re-streaming, ~2–3 apartment nights).

---

# Stage 1 (first 4 days of O3b, H1)

*Date: 2026-07-05. Pipeline: `reduce.py` → `results_H1.csv` → `fold.py`.
2,060 chunks × 128 s (73 h live, 78% duty), band 1200–1450 Hz, 11 fetch
failures (missing GWOSC files; skipped).*

## Deliverable 1: the measured per-chunk scatter

**σ₁(raw) = 6.5 × 10⁻²** per 128-s chunk (robust/MAD, after 3-day rolling-
median detrend). The reach table in `LIGO_SIDEREAL_TEST_T5.md` §2.4 assumed
2 × 10⁻² — the raw scatter is **3.3× worse**, BUT this estimator has had *no*
cleaning: no data-quality cuts beyond the science flag, no auxiliary-channel
regression, no line removal, and the band-median PSD tracks real detector
non-stationarity, not just quantum noise. The note's assumption should be
read as a post-regression target; the raw number is the no-effort floor.

Scaled reach at 5σ with the raw σ₁ (fractional modulation):
- 6 months, 1 detector: ~1 × 10⁻³ (was ~3 × 10⁻⁴)
- 4 detector-years: ~4 × 10⁻⁴ (was ~1 × 10⁻⁴)

The **vector target (β = 1.2 × 10⁻³) survives**: κ·ξ_DK excludable to
~10–30% of natural with raw noise, recovering toward the note's "few percent"
as regression approaches the 2 × 10⁻² assumption. The tensor channel remains
out of reach (unchanged conclusion).

## Deliverable 2 (method validation): the diurnal systematic is real and dominant

Harmonic fits over 3.91 days:
- sidereal: A₁ = 7.86 × 10⁻² ± 0.26 × 10⁻² (phase 180.5°), A₂ = 2.2 × 10⁻²
- solar:    A₁ = 7.87 × 10⁻² ± 0.26 × 10⁻² (phase 103.7°), A₂ = 2.3 × 10⁻²

An ~8% daily modulation of the band PSD, equally well fit at either period —
over 4 days the solar and sidereal folds are the *same* fold (they separate at
~4 min/day; full decorrelation needs ≳2–3 weeks). This is the anticipated
classical diurnal systematic (thermal/anthropogenic/scattered-light), and it
is 40× larger than the statistical floor: **the analysis is systematics-
limited, not statistics-limited, exactly as the note's §4 assumed.** The
solar-vs-sidereal discrimination + auxiliary-channel regression are not
refinements — they are the analysis.

## Stage 2 (FINAL, 2026-07-06): 20.6 of 30 days banked — pilot complete

The 30-day reduction plus one retry banked 11,003 chunks over a 20.59-d span
(79% duty). The remaining ~10 days (166 file-blocks, 2019-11-21 → 12-01) fail
persistently across two attempts — server-side unavailability, accepted as-is.
**Final headline numbers: σ₁(raw) = 2.66 × 10⁻²** (within 1.3× of the note's
assumed 2 × 10⁻², with zero cleaning), statistical floor 3.6 × 10⁻⁴ (1σ),
diurnal systematic decomposed below. Joint solar/sidereal fit remains
collinear at this baseline (condition 470) — as designed, the sidereal verdict
belongs to the full-O3b multi-detector analysis, not the pilot. Interim
history follows.

- **σ₁(raw) = 3.1 × 10⁻²** — stable from the 16-day snapshot and half the
  4-day value: the longer baseline lets the 3-day rolling detrend work. Raw,
  uncleaned scatter is now within 1.5× of the note's assumed 2 × 10⁻². The
  statistical floor is 4.4 × 10⁻⁴ (1σ) and still integrating down.
- **Diurnal systematic**: A₁ ≈ 2.2 × 10⁻² at both solar (phase 101°) and
  sidereal (phase 178°) single-period fits — unchanged interpretation: one
  daily classical signal read at two nearly-identical periods.
- **Joint two-period fit: not yet valid.** Design condition number 552 (805 at
  16 d); the joint amplitudes (~0.22) are the collinearity artifact of
  splitting one daily signal into two nearly-degenerate regressors — not
  physics. Over T days the two periods separate by ~T/365 cycles; 20 d ≈ 0.055
  cycles is not enough. The full 30-day window improves this; a genuinely
  clean separation wants months (full O3b = 147 d — available to the real
  analysis, out of scope for the pilot).

**No sidereal verdict yet** — by design the pilot's deliverables were the
machinery, σ₁, and the systematics picture, all delivered. The honest
statement for the manuscript: any pilot-scale sidereal residual is bounded by
the diurnal systematic (~2 × 10⁻²) until the two periods decorrelate;
separation is a baseline-length problem, not a sensitivity problem.

## Tidal-constituent decomposition (2026-07-06, J.B.'s question: is the diurnal effect gravitational?)

Adding lunar tidal regressors (M2 = 12.4206 h, O1 = 25.8193 h — periods no
human or thermal schedule follows) to the solar fit; final-run values
(20.59 d, condition number 3.1). **Reappraised 2026-07-06 with
autocorrelation-honest errors** (referee finding): the fit residuals have
integrated autocorrelation time τ ≈ 156 chunks (≈ 5.5 h), so N_eff ≈ 70 of
11,003 and every naive σ is inflated by √τ ≈ 12.5:

| Constituent | Amplitude (point est.) | Naive σ | **Corrected σ** |
|---|---|---|---|
| Solar S1 (24 h) | 2.51 × 10⁻² | 27.5 | **2.2** |
| Solar S2 (12 h) | 1.56 × 10⁻² | 17.1 | **1.4** |
| Lunar M2 (12.42 h) | 0.82 × 10⁻² | 9.0 | **0.7** |
| Lunar O1 (25.82 h) | 1.14 × 10⁻² | 12.6 | **1.0** |

**Downgrade (supersedes the "detection" language used earlier in this file's
history and in the 2026-07-06 session):** with red-noise-honest error bars no
constituent is individually established at this baseline. The decomposition
stands as point estimates whose pattern — workday-onset solar phase (max
08:42 local), nonzero lunar-period amplitudes — is *consistent with* a mixed
anthropogenic + tidal origin, and as a demonstration that the
constituent-fitting machinery works. Certifying it requires whitening; the
unwhitened statistical floor is 4.5 × 10⁻³, not the naive 3.6 × 10⁻⁴.

**Consequences for the T5 analysis plan:**
1. **K1 is the named confound.** Period 23.9345 h — exactly one sidereal day;
   indistinguishable from a true sidereal signal by period alone.
2. **Treatment: joint diurnal-band fit, NOT potential-ratio subtraction.**
   Bare K1/O1 ratio prediction fails for three reasons: the free-core-
   nutation resonance sits adjacent to K1 (anomalous admittance, Wahr 1981);
   M2 is semidiurnal (wrong Love numbers/ocean loading for diurnal
   calibration); instrumental coupling paths need not be linear in the
   potential. Required: empirical joint fit of K1, P1, S1, O1 with FCN-aware
   priors. **P1 (24.066 h) matters doubly:** the K1+P1 beat gives the diurnal
   tidal line a natural ~±30% annual envelope, so the CMB-orbital ~8% annual
   envelope is NOT by itself a discriminant — its fixed phase date and
   site-universality are.
3. The geometric discriminants (CMB-apex phase, orientation-set inter-site
   offsets vs longitude-set K1 phases) remain decisive, but the sensitive
   axis and explicit g(n̂,t) still need deriving (manuscript §7).

## Honest limitations of the pilot estimator

Single detector (no coincidence/phase discriminant yet); no aux-channel
regression; crude band-median estimator rather than a calibrated squeezing
level; science-flag-only data selection. Each is an upgrade path listed in
the T5 note §3, not new work discovered here.
