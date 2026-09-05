# heisenberg_cut_recoverability

The first microscopic test of Paper 2 (*The Heisenberg Cut as a Physical Threshold*): does
in-principle recoverability of a captured quantum end at a computable location with a
computable width, in the smallest exact model that has capture, off-resonant return and an
irreversible record channel?

- `PREDICTIONS.md` — fixed before the run, with the addendum recording a definition error
  caught by the calibration and corrected before the corrected run.
- `fano_recoverability.py` — the model (single-excitation Fano / Wigner–Weisskopf with a
  coherent photon channel), exact propagation, both recoverability observables. Runs in
  5 s on a laptop; peak memory a few MB.
- `RESULTS.md` — the scorecard (5 of 7 predictions confirmed, 2 wrong in a stated detail)
  and the findings: the location claim survives, the width claim is out of scope for a
  linear absorber and fixes what the stage-2 model must be.
- `run_output.txt`, `results.json` — the raw output and data.

Stage 2 (same day), after the correction logged at the end of `RESULTS.md`:

- `PREDICTIONS_STAGE2.md` — fixed before running: Part A, does the carrier frequency enter
  (quantum Rabi absorber, no rotating-wave approximation); Part B, is the crossover sharp
  for a self-sustaining absorber (Paper 2's own injected Stuart–Landau model with a record
  channel and a counter-rotating drive).
- `stage2_rabi_carrier.py`, `stage2_stuart_landau_sharpness.py` — the two scripts, 53 s
  and 16 s.
- `STAGE2_RESULTS.md` — 7 of 8 predictions confirmed, one bound wrong: the carrier is a
  Bloch–Siegert shift and not a width; the recoverability-relevant energy is continuous
  with a kink at the running onset and no signature at the Hopf; Paper 2's Figure 1
  onset is deterministic, not noise-smeared.
- `stage2_*_output.txt`, `stage2_*_results.json` — raw output and data.

```bash
python3 fano_recoverability.py
```
