#!/bin/sh
# T5 stage 4: multi-band re-reduction of the full public O3 H1 record,
# enabling proxy whitening (see reduce_v2.py header for the 8 bands).
# Resumable: stop anytime (Ctrl-C / close lid); re-run to continue.
# Progress: tail -3 t5_pilot/stage4.log
cd "$(dirname "$0")/.." || exit 1
exec caffeinate -is t5_pilot/.venv/bin/python t5_pilot/reduce_v2.py \
    --start 1238166018 --days 362 \
    --out t5_pilot/results_H1_v2.csv >> t5_pilot/stage4.log 2>&1
