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

## Stage 2 (interim, 2026-07-06): 20 of 30 days banked

The 30-day reduction completed with the final ~10 days lost to 204 consecutive
GWOSC fetch failures (server-side/transient; retry running — the reducer only
re-attempts missing chunks). Interim numbers on 9,942 chunks / 20.02 d span
(74% duty):

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

## Honest limitations of the pilot estimator

Single detector (no coincidence/phase discriminant yet); no aux-channel
regression; crude band-median estimator rather than a calibrated squeezing
level; science-flag-only data selection. Each is an upgrade path listed in
the T5 note §3, not new work discovered here.
