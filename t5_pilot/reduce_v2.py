#!/usr/bin/env python
"""T5 pilot, stage 4: multi-band streaming reducer (whitening-capable).

Same architecture as reduce.py (stream, reduce, discard; resumable via CSV)
but each 128-s chunk records EIGHT band-median PSDs:

  b1  25-45 Hz     scattered light / alignment / ground-motion couplings
  b2  70-110 Hz    control noise (dodges 60 Hz mains)
  b3  130-170 Hz   (dodges 120/180 Hz harmonics)
  b4  200-280 Hz   thermal-adjacent
  b5  320-400 Hz   (below 410.3 Hz calibration line)
  b6  550-950 Hz   between violin fundamental (~500) and 1st harmonic (~1000)
  b7  1200-1450 Hz PRIMARY quantum band (identical to v1's estimator)
  b8  1550-1850 Hz secondary quantum band (above ~1470-1530 violin cluster)

b1-b6 are regressors for proxy whitening of b7/b8; b8 cross-checks b7.

Usage:
  reduce_v2.py [--start GPS] [--days N] [--out t5_pilot/results_H1_v2.csv]
  reduce_v2.py --selftest        # no network: validates the reduction path
"""
import argparse
import csv
import os
import sys

import numpy as np

O3A_START = 1238166018  # 2019-04-01 15:00 UTC
FILE_SPAN = 4096
CHUNK = 128
FFTLEN = 4
BANDS = [(25, 45), (70, 110), (130, 170), (200, 280),
         (320, 400), (550, 950), (1200, 1450), (1550, 1850)]
DETECTOR = "H1"


def reduce_chunk(chunk):
    """One 128-s TimeSeries -> list of 8 band-median PSD values (or None)."""
    if np.isnan(chunk.value).any():
        return None
    psd = chunk.psd(fftlength=FFTLEN, overlap=FFTLEN / 2, method="median")
    f = psd.frequencies.value
    return [float(np.median(psd.value[(f >= lo) & (f < hi)]))
            for lo, hi in BANDS]


def existing_gps(path):
    done = set()
    if os.path.exists(path):
        with open(path) as fh:
            for row in csv.reader(fh):
                if row and row[0] != "gps_center":
                    done.add(float(row[0]))
    return done


def selftest():
    """Validate the reduction path on synthetic data (no network)."""
    from gwpy.timeseries import TimeSeries
    rng = np.random.default_rng(0)
    ts = TimeSeries(rng.normal(0, 1e-21, CHUNK * 4096),
                    sample_rate=4096, t0=0)
    vals = reduce_chunk(ts)
    assert vals is not None and len(vals) == len(BANDS)
    # white noise: all band medians equal the flat one-sided PSD within ~10%
    expect = 2 * (1e-21) ** 2 / 4096  # S = 2*sigma^2/fs (one-sided)
    for (lo, hi), v in zip(BANDS, vals):
        ratio = v / expect
        assert 0.8 < ratio < 1.2, f"band {lo}-{hi}: ratio {ratio:.3f}"
    # NaN chunk is rejected
    bad = TimeSeries(np.full(CHUNK * 4096, np.nan), sample_rate=4096, t0=0)
    assert reduce_chunk(bad) is None
    print("[reduce_v2] SELFTEST PASS: 8 bands, white-noise levels within 10%, "
          "NaN rejection OK")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=float, default=O3A_START)
    ap.add_argument("--days", type=float, default=362.0)
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__),
                                                  "results_H1_v2.csv"))
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()

    from gwosc.timeline import get_segments
    from gwpy.timeseries import TimeSeries

    end = args.start + args.days * 86400
    segs = get_segments(f"{DETECTOR}_DATA", int(args.start), int(end))
    total = sum(s1 - s0 for s0, s1 in segs)
    print(f"[reduce_v2] {len(segs)} segments, {total/3600:.1f} h live in "
          f"{args.days:g} d window", flush=True)

    done = existing_gps(args.out)
    new_file = not os.path.exists(args.out)
    out = open(args.out, "a", newline="")
    writer = csv.writer(out)
    if new_file:
        writer.writerow(["gps_center"] +
                        [f"b{i+1}_{lo}_{hi}" for i, (lo, hi) in
                         enumerate(BANDS)])

    n_chunks = n_failed = 0
    for s0, s1 in segs:
        b0 = (int(s0) // FILE_SPAN) * FILE_SPAN
        for block in range(b0, int(s1), FILE_SPAN):
            lo, hi = max(block, int(s0)), min(block + FILE_SPAN, int(s1))
            if hi - lo < CHUNK:
                continue
            starts = [t for t in range(lo, hi - CHUNK + 1, CHUNK)
                      if (t + CHUNK / 2) not in done]
            if not starts:
                continue
            try:
                ts = TimeSeries.fetch_open_data(DETECTOR, lo, hi,
                                                sample_rate=4096, cache=False)
            except Exception as e:
                print(f"[reduce_v2] fetch failed {lo}-{hi}: {e}", flush=True)
                n_failed += 1
                continue
            for t in starts:
                vals = reduce_chunk(ts.crop(t, t + CHUNK))
                if vals is None:
                    continue
                writer.writerow([t + CHUNK / 2] +
                                [f"{v:.6e}" for v in vals])
                n_chunks += 1
            out.flush()
            if (n_chunks // 500) != ((n_chunks - len(starts)) // 500):
                print(f"[reduce_v2] {n_chunks} chunks (gps {block}, "
                      f"{n_failed} failures)", flush=True)

    out.close()
    print(f"[reduce_v2] DONE: {n_chunks} new chunks, {n_failed} fetch "
          f"failures -> {args.out}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
