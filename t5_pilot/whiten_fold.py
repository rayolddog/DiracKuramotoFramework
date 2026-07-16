#!/usr/bin/env python
"""T5 stage-4 completion: whitened sidereal fit on the multi-band (v2) data.

Combines the two half-steps that already existed separately:
  * whiten_test.py  — regress the quantum band b7 (1200-1450 Hz) on the six
    auxiliary bands b1-b6 (25-950 Hz) to shorten its autocorrelation time.
  * fold_diurnal.py — fit DC + sidereal(1st,2nd) + solar/lunar-tidal family and
    read the sidereal-line amplitude as an upper limit on a CMB-frame signal.

Stage 4's goal was never just "does whitening reduce variance" (whiten_test.py
answered that) but "does whitening improve the actual SIDEREAL BOUND." So this
runs the identical constituent fit on BOTH raw b7 and whitened b7 over the
fullest v2 baseline on disk, and reports both kappa*xi (vector) upper limits.

Physical note on whether whitening can eat a real signal: the regressors are the
low-frequency CLASSICAL strain bands. A genuine DK quantum-noise modulation
lives in the quantum bands (b7,b8 track at +0.83) and not in b1-b6, so regressing
b1-b6 out of b7 removes classical (incl. any classical sidereal-locked) power
while preserving a true quantum modulation. Whitening should therefore sharpen,
not suppress, a real bound. The sidereal line still shares K1's period, so the
fitted amplitude remains a conservative upper limit either way.

Caveat unchanged from fold_diurnal: over this baseline solar/sidereal separation
is only partial (see the reported design condition number) — the definitive bound
stays with the 256.8-d v1 fit; this is the whitened method result on v2.

Usage: whiten_fold.py [--csv t5_pilot/results_H1_v2.csv]
"""
import argparse
import os
import numpy as np

H1_LON_DEG = -119.40766
APEX_RA_HR = 11.2                       # CMB dipole apex, RA 11h12m
BETA = 1.23e-3                          # CMB v/c, the vector frame scale
CONSTITUENTS = {                        # separable de-confounders (fixed period)
    "S1_solar_24h": 24.000000,
    "S2_solar_12h": 12.000000,
    "P1_24.066h":   24.065890,
    "O1_25.819h":   25.819342,
    "M2_12.421h":   12.420601,
}


def frac_detrend(gps, y):
    """Fractional deviation from a 3-day-smoothed daily-median trend (O(N)).
    Identical to whiten_test.frac_detrend / fold_diurnal.fast_detrend."""
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


def sidereal_fit(gps, x, ph_sid, label):
    """DC + sidereal(1st,2nd) + tidal-family least squares with red-noise-honest
    errors. Mirrors fold_diurnal.main exactly. Returns a result dict."""
    cols = [np.ones_like(x),
            np.cos(ph_sid), np.sin(ph_sid),
            np.cos(2 * ph_sid), np.sin(2 * ph_sid)]
    names = ["sidereal_1st", "sidereal_2nd"]
    for cname, per in CONSTITUENTS.items():
        ph = 2 * np.pi * ((gps / 3600.0 / per) % 1.0)
        cols += [np.cos(ph), np.sin(ph)]
        names.append(cname)
    A = np.column_stack(cols)
    coef, *_ = np.linalg.lstsq(A, x, rcond=None)
    resid = x - A @ coef
    tau = autocorr_tau(resid)
    cond = np.linalg.cond(A.T @ A)
    cov = np.linalg.inv(A.T @ A) * np.var(resid) * tau
    err = np.sqrt(np.diag(cov))

    a1c, a1s = coef[1], coef[2]
    amp_sid = np.hypot(a1c, a1s)
    e_sid = np.hypot(a1c * err[1], a1s * err[2]) / max(amp_sid, 1e-30)
    lst_max = (np.degrees(np.arctan2(a1s, a1c)) % 360) / 360 * 24
    apex_off = (lst_max - APEX_RA_HR + 12) % 24 - 12
    ul95 = amp_sid + 1.645 * e_sid
    s1 = 1.4826 * np.median(np.abs(x - np.median(x)))

    print(f"\n[{label}] sigma_1 {s1:.3e} | design condition {cond:.1f} | "
          f"tau {tau:.0f} chunks ({tau*128/3600:.1f} h) | N_eff {len(x)/tau:.0f}")
    print(f"[{label}] constituent amplitudes (red-noise-honest errors):")
    for i, nm in enumerate(names):
        ic, isn = 1 + 2 * i, 2 + 2 * i
        amp = np.hypot(coef[ic], coef[isn])
        e = np.hypot(coef[ic] * err[ic], coef[isn] * err[isn]) / max(amp, 1e-30)
        print(f"         {nm:14s} {amp:.3e} +- {e:.1e}  "
              f"({amp/max(e,1e-30):.1f} sigma)")
    print(f"[{label}] SIDEREAL (UL on CMB signal; includes K1): "
          f"{amp_sid:.3e} +- {e_sid:.1e} ({amp_sid/max(e_sid,1e-30):.1f} sigma)")
    print(f"[{label}]   95% UL {ul95:.3e} | max at LST {lst_max:.1f} h "
          f"(apex {APEX_RA_HR:.1f} h, offset {apex_off:+.1f} h)")
    print(f"[{label}]   kappa*xi (vector) UL = {ul95/BETA:.2f} of natural")
    return dict(label=label, coef=coef, s1=s1, cond=cond, tau=tau,
                amp_sid=amp_sid, e_sid=e_sid, ul95=ul95, kxi=ul95 / BETA,
                lst_max=lst_max, apex_off=apex_off, sigma=amp_sid / max(e_sid, 1e-30))


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(__file__)
    ap.add_argument("--csv", default=os.path.join(here, "results_H1_v2.csv"))
    ap.add_argument("--plots", default=os.path.join(here, "plots"))
    a = ap.parse_args()

    data = np.loadtxt(a.csv, delimiter=",", skiprows=1)
    o = np.argsort(data[:, 0]); data = data[o]
    gps = data[:, 0]
    days = (gps[-1] - gps[0]) / 86400
    print(f"[whiten_fold] {len(gps)} chunks, {days:.1f} d, 8 bands")

    xb = np.column_stack([frac_detrend(gps, data[:, 1 + i]) for i in range(8)])
    x7_raw = xb[:, 6]                    # quantum band b7
    A_w = np.column_stack([np.ones(len(gps)), xb[:, 0:6]])   # [1, b1..b6]
    coef_w, *_ = np.linalg.lstsq(A_w, x7_raw, rcond=None)
    x7_white = x7_raw - A_w @ coef_w
    var_removed = 1 - np.var(x7_white) / np.var(x7_raw)
    print(f"[whiten_fold] classical variance removed by b1-b6 regression: "
          f"{var_removed*100:.0f}%")

    from astropy.time import Time
    from astropy import units as u
    from astropy.utils import iers
    iers.conf.auto_max_age = None
    lst_hr = Time(gps, format="gps").sidereal_time(
        "mean", longitude=H1_LON_DEG * u.deg).to_value(u.hourangle)
    ph_sid = 2 * np.pi * (lst_hr / 24.0)

    raw = sidereal_fit(gps, x7_raw, ph_sid, "RAW b7")
    white = sidereal_fit(gps, x7_white, ph_sid, "WHITE b7")

    print(f"\n[whiten_fold] SUMMARY ({days:.1f} d, {len(gps)} chunks):")
    print(f"  raw   b7: kxi(vector) UL {raw['kxi']:.2f} of natural "
          f"(sidereal {raw['sigma']:.1f} sigma)")
    print(f"  white b7: kxi(vector) UL {white['kxi']:.2f} of natural "
          f"(sidereal {white['sigma']:.1f} sigma)")
    impr = raw['kxi'] / white['kxi'] if white['kxi'] else float('nan')
    print(f"  whitening improves the bound x{impr:.2f}")

    os.makedirs(a.plots, exist_ok=True)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
    bins = np.linspace(0, 2 * np.pi, 25)
    idx = np.digitize(ph_sid, bins) - 1
    c = 0.5 * (bins[:-1] + bins[1:]) * 24 / (2 * np.pi)
    for ax, x, res, ttl in ((axes[0], x7_raw, raw, "raw b7"),
                            (axes[1], x7_white, white, "whitened b7")):
        bm = [np.mean(x[idx == i]) if (idx == i).any() else np.nan
              for i in range(24)]
        be = [np.std(x[idx == i]) / np.sqrt(max((idx == i).sum(), 1))
              * np.sqrt(res['tau']) for i in range(24)]
        ax.errorbar(c, bm, be, fmt="o", ms=3)
        pp = np.linspace(0, 2 * np.pi, 300)
        cf = res['coef']
        ax.plot(pp * 24 / (2 * np.pi), cf[0] + cf[1] * np.cos(pp)
                + cf[2] * np.sin(pp) + cf[3] * np.cos(2 * pp)
                + cf[4] * np.sin(2 * pp), "-", lw=1)
        ax.axvline(APEX_RA_HR, color="r", ls="--", lw=1, label="CMB apex")
        ax.set(xlabel="local sidereal time (h)",
               title=f"{ttl}: kxi<{res['kxi']:.1f}, "
                     f"A1={res['amp_sid']:.1e} ({res['sigma']:.1f}s)")
        ax.legend()
    axes[0].set_ylabel("fractional PSD deviation")
    fig.suptitle(f"T5 stage-4 whitened sidereal fold (v2, {days:.0f} d)")
    fig.tight_layout()
    out = os.path.join(a.plots, "sidereal_whitened_fit.png")
    fig.savefig(out, dpi=120)
    print(f"[whiten_fold] plot -> {out}")


if __name__ == "__main__":
    main()
