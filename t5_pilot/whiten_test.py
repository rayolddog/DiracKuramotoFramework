#!/usr/bin/env python
"""T5 whitening proof-of-concept on the multi-band (stage-4) data.

The pilot's sensitivity is red-noise-limited: the quantum-band estimator has a
~3.3 h autocorrelation time, so N_eff << N. Stage 4 recorded 6 auxiliary bands
(b1-b6, 25-950 Hz) alongside the quantum band (b7, 1200-1450 Hz) precisely so we
can REGRESS the classical non-stationarity out of b7. This script asks the one
gating question, using only local data (no streaming):

    does regressing b7 on b1-b6 shorten the autocorrelation time / raise N_eff?

If yes, the reach improves by ~sqrt(N_eff gain). This validates the METHOD; a new
sidereal bound needs the full baseline (48 d here is too short to separate solar
from sidereal).

Usage: whiten_test.py [--csv t5_pilot/results_H1_v2.csv]
"""
import argparse
import os
import numpy as np


def frac_detrend(gps, y):
    """Fractional deviation from a 3-day-smoothed daily-median trend (O(N))."""
    from scipy.ndimage import median_filter
    day = np.floor((gps - gps[0]) / 86400).astype(int)
    nd = day.max() + 1
    daily = np.full(nd, np.nan)
    for d in range(nd):
        sel = day == d
        if sel.any():
            daily[d] = np.median(y[sel])
    ok = ~np.isnan(daily)
    daily[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), daily[ok])
    return y / median_filter(daily, size=3)[day] - 1.0


def autocorr_tau(r):
    r = r - r.mean()
    v0 = np.dot(r, r) / len(r)
    tau = 1.0
    for k in range(1, min(4000, len(r) // 10)):
        rho = np.dot(r[:-k], r[k:]) / ((len(r) - k) * v0)
        if rho < 0.02:
            break
        tau += 2 * rho
    return tau


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(__file__)
    ap.add_argument("--csv", default=os.path.join(here, "results_H1_v2.csv"))
    a = ap.parse_args()

    data = np.loadtxt(a.csv, delimiter=",", skiprows=1)
    o = np.argsort(data[:, 0]); data = data[o]
    gps = data[:, 0]
    bands = data[:, 1:9]                 # b1..b8
    days = (gps[-1] - gps[0]) / 86400
    print(f"[whiten] {len(gps)} chunks, {days:.1f} d, 8 bands")

    # fractional deviation of every band
    xb = np.column_stack([frac_detrend(gps, bands[:, i]) for i in range(8)])
    x7 = xb[:, 6]                        # quantum band b7 (the target)
    regressors = xb[:, 0:6]             # b1..b6 auxiliary bands

    # raw quantum-band statistics
    tau_raw = autocorr_tau(x7)
    s1_raw = 1.4826 * np.median(np.abs(x7 - np.median(x7)))
    neff_raw = len(x7) / tau_raw

    # whiten: least-squares regress b7 on [1, b1..b6], take the residual
    A = np.column_stack([np.ones(len(x7)), regressors])
    coef, *_ = np.linalg.lstsq(A, x7, rcond=None)
    resid = x7 - A @ coef
    tau_w = autocorr_tau(resid)
    s1_w = 1.4826 * np.median(np.abs(resid - np.median(resid)))
    neff_w = len(resid) / tau_w
    var_removed = 1 - np.var(resid) / np.var(x7)

    print(f"[whiten] RAW    b7: sigma1 {s1_raw:.3e} | tau {tau_raw:.0f} chunks "
          f"({tau_raw*128/3600:.1f} h) | N_eff {neff_raw:.0f}")
    print(f"[whiten] WHITE  b7: sigma1 {s1_w:.3e} | tau {tau_w:.0f} chunks "
          f"({tau_w*128/3600:.1f} h) | N_eff {neff_w:.0f}")
    print(f"[whiten] classical variance removed by b1-b6 regression: "
          f"{var_removed*100:.0f}%")
    gain = neff_w / neff_raw
    print(f"[whiten] N_eff gain x{gain:.1f}  ->  amplitude reach improves "
          f"x{np.sqrt(gain):.1f}")
    # b8 cross-check: a real modulation must appear in BOTH quantum bands
    x8 = xb[:, 7]
    r = np.corrcoef(x7, x8)[0, 1]
    print(f"[whiten] b7-b8 quantum-band correlation (sanity): {r:+.2f}")
    print(f"[whiten] NOTE: 48 d is a METHOD test only; the whitened sidereal "
          f"bound needs the full baseline (solar/sidereal don't separate here).")


if __name__ == "__main__":
    main()
