#!/bin/sh
# T5 stage 3: full public O3 H1 record (O3a 2019-04-01 through O3b 2020-03-27).
# Resumable: stop anytime (Ctrl-C / close lid); re-run to continue.
# Progress: tail -3 t5_pilot/stage3.log
cd "$(dirname "$0")/.." || exit 1
exec t5_pilot/.venv/bin/python t5_pilot/reduce.py \
    --start 1238166018 --days 362 \
    --out t5_pilot/results_H1.csv >> t5_pilot/stage3.log 2>&1
