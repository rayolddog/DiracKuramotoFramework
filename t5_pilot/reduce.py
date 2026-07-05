#!/usr/bin/env python
"""T5 pilot, stage 1: stream O3b H1 open strain from GWOSC and reduce it.

For each 4096-s GWOSC file span intersecting an H1 science segment:
  - fetch once (no raw-data cache kept),
  - chop into 128-s chunks,
  - per chunk compute a median-averaged PSD (4-s FFTs) and take the median
    across a shot-noise-dominated band chosen between the violin-mode
    harmonic clusters,
  - append (gps_center, band_psd, n_avg) to a CSV checkpoint.

Restartable: chunks already in the CSV are skipped, so the expensive
download+reduce runs once and every downstream iteration reads the CSV.

Usage:
  reduce.py [--start GPS] [--days N] [--out t5_pilot/results_H1.csv]
"""
import argparse
import csv
import os
import sys

import numpy as np

O3B_START = 1256655618  # 2019-11-01 15:00 UTC
FILE_SPAN = 4096        # GWOSC open-data file alignment (s)
CHUNK = 128             # s, per-sample estimator resolution
FFTLEN = 4              # s
BAND = (1200.0, 1450.0)  # Hz; shot-noise dominated, between violin clusters
DETECTOR = "H1"


def existing_gps(path):
    done = set()
    if os.path.exists(path):
        with open(path) as f:
            for row in csv.reader(f):
                if row and row[0] != "gps_center":
                    done.add(float(row[0]))
    return done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=float, default=O3B_START)
    ap.add_argument("--days", type=float, default=4.0)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "results_H1.csv"))
    args = ap.parse_args()

    from gwosc.timeline import get_segments
    from gwpy.timeseries import TimeSeries

    end = args.start + args.days * 86400
    segs = get_segments(f"{DETECTOR}_DATA", int(args.start), int(end))
    total = sum(s1 - s0 for s0, s1 in segs)
    print(f"[reduce] {len(segs)} science segments, {total/3600:.1f} h live time "
          f"in {args.days:g} d window", flush=True)

    done = existing_gps(args.out)
    new_file = not os.path.exists(args.out)
    out = open(args.out, "a", newline="")
    writer = csv.writer(out)
    if new_file:
        writer.writerow(["gps_center", "band_psd", "n_avg"])

    n_chunks = n_skipped = n_failed = 0
    for s0, s1 in segs:
        b0 = (int(s0) // FILE_SPAN) * FILE_SPAN
        for block in range(b0, int(s1), FILE_SPAN):
            lo, hi = max(block, int(s0)), min(block + FILE_SPAN, int(s1))
            if hi - lo < CHUNK:
                continue
            # skip whole block if every chunk in it is already reduced
            starts = [t for t in range(lo, hi - CHUNK + 1, CHUNK)
                      if (t + CHUNK / 2) not in done]
            if not starts:
                n_skipped += (hi - lo) // CHUNK
                continue
            try:
                ts = TimeSeries.fetch_open_data(DETECTOR, lo, hi,
                                                sample_rate=4096, cache=False)
            except Exception as e:  # missing file, network hiccup: log and move on
                print(f"[reduce] fetch failed {lo}-{hi}: {e}", flush=True)
                n_failed += 1
                continue
            for t in starts:
                chunk = ts.crop(t, t + CHUNK)
                if np.isnan(chunk.value).any():
                    continue
                psd = chunk.psd(fftlength=FFTLEN, overlap=FFTLEN / 2,
                                method="median")
                sel = (psd.frequencies.value >= BAND[0]) & \
                      (psd.frequencies.value < BAND[1])
                est = float(np.median(psd.value[sel]))
                writer.writerow([t + CHUNK / 2, f"{est:.6e}",
                                 int(CHUNK / (FFTLEN / 2)) - 1])
                n_chunks += 1
            out.flush()
            if (n_chunks // 100) != ((n_chunks - len(starts)) // 100):
                print(f"[reduce] {n_chunks} chunks reduced "
                      f"(gps {block}, {n_failed} fetch failures)", flush=True)

    out.close()
    print(f"[reduce] DONE: {n_chunks} new chunks, {n_skipped} already present, "
          f"{n_failed} fetch failures -> {args.out}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
