# T5 pilot — GWOSC quantum-noise sidereal-fold pipeline

Pilot implementation of the "cheapest first look" of `../LIGO_SIDEREAL_TEST_T5.md`
§3: measure the real per-chunk scatter σ₁ of a band-limited quantum-noise
estimator on public O3b H1 strain, and run a null sidereal fold with the solar
fold as the systematics control.

- `reduce.py` — streams open data (nothing cached to disk), reduces each 128-s
  chunk to a median band PSD in 1200–1450 Hz, checkpoints to `results_H1.csv`.
  Restartable; already-reduced chunks are skipped.
- `fold.py` — detrends (3-day rolling median), measures σ₁, fits DC + 1st + 2nd
  harmonics in local sidereal and solar phase, writes `plots/`.

```
.venv/bin/python reduce.py --days 4      # ~1-2 h, network-bound
.venv/bin/python fold.py
```

Deliverable #1 is σ₁ (the reach table in the T5 note assumes 2×10⁻² per ~100 s).
The sidereal A₁, A₂ amplitudes from a few days are NOT yet meaningful — solar and
sidereal periods need ≳2 weeks to decorrelate; the pilot only validates the method.
