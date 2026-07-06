# T5 pilot results — stage 1 (first 4 days of O3b, H1)

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
human or thermal schedule follows) to the solar fit, on 20.02 d (condition
number 3.1 — clean separation via the ~15 d spring–neap beat):

| Constituent | Amplitude | Significance |
|---|---|---|
| Solar S1 (24 h) | 2.42 × 10⁻² | 25σ |
| Solar S2 (12 h) | 1.78 × 10⁻² | 19σ |
| **Lunar M2 (12.42 h)** | **0.98 × 10⁻²** | **10σ** |
| **Lunar O1 (25.82 h)** | **1.16 × 10⁻²** | **12σ** |

Solar-daily maximum at 08:42 local (PST) — the workday-onset signature of an
anthropogenic/thermal origin for the dominant S1 line. But the M2 and O1
detections are unambiguous: **roughly half the "diurnal" systematic is
genuinely tidal — lunisolar gravity-gradient driven** (via residual tidal
strain after feed-forward, ocean-loading tilt, and/or tidal-actuator
couplings into alignment and the noise band).

**Consequences for the T5 analysis plan (important):**
1. **K1 is the named confound.** The lunisolar K1 tidal constituent has
   period 23.9345 h — *exactly one sidereal day*. A K1 tidal coupling is
   indistinguishable from a true sidereal signal by period alone. The
   manuscript must name this explicitly.
2. **Predict-and-subtract via the tidal family.** Tidal constituents come in
   fixed potential-amplitude ratios (Doodson expansion; K1/O1 ≈ 1.41 in the
   diurnal potential). Measuring the site's response to M2 and O1 — cleanly
   separable from sidereal — calibrates the tidal admittance and *predicts*
   the K1 tidal amplitude, which can then be subtracted from the sidereal
   band. The 10–12σ M2/O1 detections above prove this calibration is
   available in the data itself.
3. The pre-registered discriminants already in §4–5 of the T5 note remain
   decisive against residual K1: its phase is set by local geography/geoid
   (different at each site in a way unrelated to detector orientation),
   whereas the DK signal is CMB-apex-locked with orientation-set inter-site
   phases and an ~8% annual envelope (K1's modulations are nodal, 18.6 yr,
   not annual).

## Honest limitations of the pilot estimator

Single detector (no coincidence/phase discriminant yet); no aux-channel
regression; crude band-median estimator rather than a calibrated squeezing
level; science-flag-only data selection. Each is an upgrade path listed in
the T5 note §3, not new work discovered here.
