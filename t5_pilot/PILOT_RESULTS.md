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

## Stage 2 (running): 30-day reduction

Extending the same CSV to the first 30 days of O3b H1 (~25–30 GB streamed,
nothing stored; ~11 h wall-clock). Goals: (i) separate the solar and sidereal
first harmonics (30 days ≈ 2 full cycle slips), (ii) report the residual
sidereal A₁ after fitting both periods jointly, (iii) recompute σ₁ on the
longer baseline. A joint solar+sidereal fit should be added to `fold.py`
before reading stage-2 results (the current fits are single-period).

## Honest limitations of the pilot estimator

Single detector (no coincidence/phase discriminant yet); no aux-channel
regression; crude band-median estimator rather than a calibrated squeezing
level; science-flag-only data selection. Each is an upgrade path listed in
the T5 note §3, not new work discovered here.
