#!/usr/bin/env python
"""T5 pilot, stage 2: sidereal fold + harmonic fit of the reduced estimator.

Reads the CSV written by reduce.py. Steps:
  1. fractional deviation x = psd / (slow rolling median) - 1
     (rolling window long vs 1 day so the 24 h harmonics survive detrending),
  2. per-chunk scatter sigma_1 = robust std of x  -> the number the reach
     table in LIGO_SIDEREAL_TEST_T5.md 2.4 assumes to be ~2e-2,
  3. least-squares fit of DC + 1st + 2nd harmonics in LOCAL SIDEREAL phase,
     with the identical fit in SOLAR phase as the systematics control,
  4. plots: time series, sidereal fold, solar fold.

Usage: fold.py [--csv t5_pilot/results_H1.csv] [--plots t5_pilot/plots]
"""
import argparse
import os

import numpy as np

H1_LONGITUDE_DEG = -119.40766  # LIGO Hanford
TREND_DAYS = 3.0               # rolling-median detrend window (>> 1 day)


def rolling_median(t, y, window):
    out = np.empty_like(y)
    for i, ti in enumerate(t):
        sel = np.abs(t - ti) < window / 2
        out[i] = np.median(y[sel])
    return out


def harmonic_fit(phase, x):
    """Fit x = a0 + sum_k (ak cos k*phase + bk sin k*phase), k=1,2."""
    A = np.column_stack([np.ones_like(phase),
                         np.cos(phase), np.sin(phase),
                         np.cos(2 * phase), np.sin(2 * phase)])
    coef, *_ = np.linalg.lstsq(A, x, rcond=None)
    resid = x - A @ coef
    # parameter covariance from residual scatter
    cov = np.linalg.inv(A.T @ A) * np.var(resid)
    err = np.sqrt(np.diag(cov))
    amp1 = np.hypot(coef[1], coef[2])
    amp2 = np.hypot(coef[3], coef[4])
    e1 = np.hypot(coef[1] * err[1], coef[2] * err[2]) / max(amp1, 1e-30)
    e2 = np.hypot(coef[3] * err[3], coef[4] * err[4]) / max(amp2, 1e-30)
    ph1 = np.arctan2(-coef[2], coef[1]) % (2 * np.pi)
    ph2 = (np.arctan2(-coef[4], coef[3]) % (2 * np.pi)) / 2
    return dict(coef=coef, amp1=amp1, err1=e1, ph1=ph1,
                amp2=amp2, err2=e2, ph2=ph2, resid_std=np.std(resid))


def main():
    ap = argparse.ArgumentParser()
    here = os.path.dirname(__file__)
    ap.add_argument("--csv", default=os.path.join(here, "results_H1.csv"))
    ap.add_argument("--plots", default=os.path.join(here, "plots"))
    args = ap.parse_args()

    gps, psd = np.loadtxt(args.csv, delimiter=",", skiprows=1,
                          usecols=(0, 1), unpack=True)
    order = np.argsort(gps)
    gps, psd = gps[order], psd[order]
    days = (gps[-1] - gps[0]) / 86400
    print(f"[fold] {len(gps)} chunks spanning {days:.2f} d "
          f"(duty {len(gps)*128/ (gps[-1]-gps[0]) *100:.0f}%)")

    # 1. detrend
    trend = rolling_median(gps, psd, TREND_DAYS * 86400)
    x = psd / trend - 1.0

    # 2. per-chunk scatter (robust, via MAD)
    sigma1 = 1.4826 * np.median(np.abs(x - np.median(x)))
    print(f"[fold] sigma_1 (robust per-128s fractional scatter) = {sigma1:.3e}")
    print(f"[fold]   (note S2.4 of LIGO_SIDEREAL_TEST_T5.md assumed 2e-2)")

    # 3. phases
    from astropy.time import Time
    from astropy import units as u
    from astropy.utils import iers
    iers.conf.auto_max_age = None  # tolerate stale IERS tables
    t = Time(gps, format="gps")
    lst = t.sidereal_time("mean", longitude=H1_LONGITUDE_DEG * u.deg)
    ph_sid = lst.to_value(u.rad)
    ph_sol = 2 * np.pi * ((t.unix / 86400.0) % 1.0)

    fits = {}
    for name, ph in [("sidereal", ph_sid), ("solar", ph_sol)]:
        f = harmonic_fit(ph, x)
        fits[name] = f
        print(f"[fold] {name:8s}: A1 = {f['amp1']:.3e} +- {f['err1']:.1e} "
              f"(phase {np.degrees(f['ph1']):5.1f} deg) | "
              f"A2 = {f['amp2']:.3e} +- {f['err2']:.1e}")

    # joint fit: both periods simultaneously (the discriminating fit once the
    # span exceeds ~2-3 weeks; heavily covariant on short baselines)
    A = np.column_stack([np.ones_like(x),
                         np.cos(ph_sid), np.sin(ph_sid),
                         np.cos(2 * ph_sid), np.sin(2 * ph_sid),
                         np.cos(ph_sol), np.sin(ph_sol),
                         np.cos(2 * ph_sol), np.sin(2 * ph_sol)])
    coef, *_ = np.linalg.lstsq(A, x, rcond=None)
    resid = x - A @ coef
    cov = np.linalg.inv(A.T @ A) * np.var(resid)
    err = np.sqrt(np.diag(cov))
    names = ["sid A1", "sid A2", "sol A1", "sol A2"]
    for lab, (ic, isn) in zip(names, [(1, 2), (3, 4), (5, 6), (7, 8)]):
        amp = np.hypot(coef[ic], coef[isn])
        e = np.hypot(coef[ic] * err[ic], coef[isn] * err[isn]) / max(amp, 1e-30)
        ph_deg = np.degrees(np.arctan2(-coef[isn], coef[ic]) % (2 * np.pi))
        print(f"[fold] joint {lab}: {amp:.3e} +- {e:.1e}  "
              f"(phase {ph_deg:5.1f} deg)")
    # condition number diagnostic: >> 1 means the periods are not yet separable
    print(f"[fold] joint-fit design condition number = "
          f"{np.linalg.cond(A.T @ A):.1f}")

    # tidal-constituent check: is the daily signal gravitational (tidal) or
    # solar-locked (anthropogenic/thermal)? Lunar constituents M2 (12.4206 h)
    # and O1 (25.8193 h) separate from the solar S1/S2 lines in ~15 d (the
    # spring-neap beat). NB the K1 constituent (23.9345 h) IS the sidereal
    # period - it cannot be separated by period alone; that is the tidal
    # confound the multi-detector phase + annual envelope must handle.
    M2_H, O1_H = 12.4206012, 25.81933871
    ph_m2 = 2 * np.pi * ((t.unix / 3600.0 / M2_H) % 1.0)
    ph_o1 = 2 * np.pi * ((t.unix / 3600.0 / O1_H) % 1.0)
    At = np.column_stack([np.ones_like(x),
                          np.cos(ph_sol), np.sin(ph_sol),
                          np.cos(2 * ph_sol), np.sin(2 * ph_sol),
                          np.cos(ph_m2), np.sin(ph_m2),
                          np.cos(ph_o1), np.sin(ph_o1)])
    ct, *_ = np.linalg.lstsq(At, x, rcond=None)
    rt = x - At @ ct
    covt = np.linalg.inv(At.T @ At) * np.var(rt)
    et = np.sqrt(np.diag(covt))
    for lab, (ic, isn) in [("solar S1 (24h)   ", (1, 2)),
                           ("solar S2 (12h)   ", (3, 4)),
                           ("lunar M2 (12.42h)", (5, 6)),
                           ("lunar O1 (25.82h)", (7, 8))]:
        amp = np.hypot(ct[ic], ct[isn])
        e = np.hypot(ct[ic] * et[ic], ct[isn] * et[isn]) / max(amp, 1e-30)
        print(f"[fold] tidal check {lab}: {amp:.3e} +- {e:.1e}"
              f"  ({amp/max(e,1e-30):.1f} sigma)")
    print(f"[fold] tidal-check condition number = {np.linalg.cond(At.T @ At):.1f}")
    # local solar time of the daily maximum (H1 is UTC-8 in winter)
    tmax_utc = (np.degrees(np.arctan2(ct[2], ct[1])) % 360) / 360 * 24
    print(f"[fold] solar-daily maximum at {tmax_utc:.1f} h UTC "
          f"= {(tmax_utc - 8) % 24:.1f} h local (PST)")

    # autocorrelation-honest errors: adjacent 128-s chunks of a drifting PSD
    # are NOT independent. Estimate the integrated autocorrelation time of
    # the tidal-fit residuals and rescale every quoted sigma by sqrt(tau).
    r_ord = rt  # already in gps order
    r_ord = r_ord - r_ord.mean()
    var0 = float(np.dot(r_ord, r_ord)) / len(r_ord)
    tau = 1.0
    for k in range(1, min(2000, len(r_ord) // 10)):
        rho = float(np.dot(r_ord[:-k], r_ord[k:])) / \
            ((len(r_ord) - k) * var0)
        if rho < 0.02:
            break
        tau += 2 * rho
    neff = len(x) / tau
    print(f"[fold] integrated autocorrelation time tau = {tau:.1f} chunks "
          f"({tau * 128 / 60:.0f} min); N_eff = {neff:.0f} of {len(x)}")
    print(f"[fold] ALL sigmas above are inflated by sqrt(tau) = "
          f"{np.sqrt(tau):.2f}; autocorrelation-corrected significances:")
    for lab, (ic, isn) in [("solar S1 (24h)   ", (1, 2)),
                           ("solar S2 (12h)   ", (3, 4)),
                           ("lunar M2 (12.42h)", (5, 6)),
                           ("lunar O1 (25.82h)", (7, 8))]:
        amp = np.hypot(ct[ic], ct[isn])
        e = np.hypot(ct[ic] * et[ic], ct[isn] * et[isn]) / max(amp, 1e-30)
        print(f"[fold]   {lab}: {amp/max(e*np.sqrt(tau),1e-30):.1f} sigma")
    print(f"[fold] corrected statistical floor ~ sigma1*sqrt(2/N_eff) = "
          f"{sigma1*np.sqrt(2/neff):.2e}")
    n_eff = len(x)
    print(f"[fold] statistical floor ~ sigma1*sqrt(2/M) = "
          f"{sigma1*np.sqrt(2/n_eff):.2e} (M = {n_eff})")

    # 4. plots
    os.makedirs(args.plots, exist_ok=True)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 3.2))
    ax.plot((gps - gps[0]) / 86400, x, ",", alpha=.5)
    ax.set(xlabel="days from start", ylabel="fractional PSD dev",
           title=f"band-PSD fractional deviation, sigma_1={sigma1:.2e}")
    fig.tight_layout()
    fig.savefig(os.path.join(args.plots, "timeseries.png"), dpi=130)

    for name, ph in [("sidereal", ph_sid), ("solar", ph_sol)]:
        f = fits[name]
        bins = np.linspace(0, 2 * np.pi, 25)
        idx = np.digitize(ph, bins) - 1
        bm = [np.mean(x[idx == i]) for i in range(24)]
        be = [np.std(x[idx == i]) / np.sqrt(max((idx == i).sum(), 1))
              for i in range(24)]
        fig, ax = plt.subplots(figsize=(7, 3.2))
        c = 0.5 * (bins[:-1] + bins[1:])
        ax.errorbar(c, bm, be, fmt="o", ms=3)
        pp = np.linspace(0, 2 * np.pi, 300)
        A = np.column_stack([np.ones_like(pp), np.cos(pp), np.sin(pp),
                             np.cos(2 * pp), np.sin(2 * pp)])
        ax.plot(pp, A @ f["coef"], "-", lw=1)
        ax.set(xlabel=f"{name} phase (rad)", ylabel="fractional PSD dev",
               title=f"{name} fold: A1={f['amp1']:.2e}, A2={f['amp2']:.2e}")
        fig.tight_layout()
        fig.savefig(os.path.join(args.plots, f"fold_{name}.png"), dpi=130)

    print(f"[fold] plots -> {args.plots}/")


if __name__ == "__main__":
    main()
