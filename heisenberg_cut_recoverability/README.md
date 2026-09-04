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

```bash
python3 fano_recoverability.py
```
