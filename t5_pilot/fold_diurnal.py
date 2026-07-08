#!/usr/bin/env python
"""T5 definitive diurnal-band fit on the 8.5-month O3 H1 reduction.

The scientific question the pilot can answer without new data: once the full
solar + lunar-tidal family is fit, does any signal survive at the SIDEREAL
period, and does its phase point at the CMB apex?

Physics of the degeneracy (stated honestly): the sidereal line (23.9345 h) is
identical in period to the lunisolar K1 tidal constituent — they cannot be
separated by period. So the fitted sidereal amplitude is an UPPER LIMIT on any
CMB-frame signal (it also contains any K1 tide) — conservative, which is what we
want for a bound. The de-confounders that CAN be separated over 256 days:
  S1 (24.000 h solar) — beats against sidereal at 1/yr (0.70 cycle over 256 d)
  P1 (24.066 h)       — beats against sidereal at 2/yr (1.40 cycle) -> separable
  O1 (25.819 h), M2 (12.421 h), S2 (12.000 h)
Diagnostic: the sidereal-line PHASE. CMB-apex-locked -> max near LST = RA_apex
(11h12m = 168 deg). K1-tidal -> a local-geographic phase. At pilot amplitude
the phase is likely uninformative, but we report it and the apex offset.

Usage: fold_diurnal.py [--csv t5_pilot/results_H1.csv]
"""
import argparse
import os
import numpy as np

H1_LON_DEG = -119.40766
APEX_RA_HR = 11.2                       # CMB dipole apex, RA 11h12m
SIDEREAL_H = 23.934469591
CONSTITUENTS = {                        # separable de-confounders (fixed period)
    "S1_solar_24h": 24.000000,
    "S2_solar_12h": 12.000000,
    "P1_24.066h":   24.065890,
    "O1_25.819h":   25.819342,
    "M2_12.421h":   12.420601,
}


def fast_detrend(gps, psd):
    """Divide by a 3-day-smoothed daily-median trend (O(N); preserves the
    intra-day harmonics, removes slow drift). Returns fractional deviation."""
    from scipy.ndimage import median_filter
    day = np.floor((gps - gps[0]) / 86400).astype(int)
    ndays = day.max() + 1
    daily = np.full(ndays, np.nan)
    for d in range(ndays):
        sel = day == d
        if sel.any():
            daily[d] = np.median(psd[sel])
    # fill gaps, smooth with 3-day median
    ok = ~np.isnan(daily)
    daily[~ok] = np.interp(np.flatnonzero(~ok), np.flatnonzero(ok), daily[ok])
    trend = median_filter(daily, size=3)[day]
    return psd / trend - 1.0


def autocorr_tau(resid):
    r = resid - resid.mean()
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
    ap.add_argument("--csv", default=os.path.join(here, "results_H1.csv"))
    ap.add_argument("--plots", default=os.path.join(here, "plots"))
    a = ap.parse_args()

    gps, psd = np.loadtxt(a.csv, delimiter=",", skiprows=1,
                          usecols=(0, 1), unpack=True)
    o = np.argsort(gps); gps, psd = gps[o], psd[o]
    x = fast_detrend(gps, psd)
    sig1 = 1.4826 * np.median(np.abs(x - np.median(x)))
    days = (gps[-1] - gps[0]) / 86400
    print(f"[diurnal] {len(gps)} chunks, {days:.1f} d, sigma_1 = {sig1:.3e}")

    # sidereal phase via true LST; solar/tidal via fixed periods
    from astropy.time import Time
    from astropy import units as u
    from astropy.utils import iers
    iers.conf.auto_max_age = None
    t = Time(gps, format="gps")
    lst_hr = t.sidereal_time("mean", longitude=H1_LON_DEG * u.deg).to_value(u.hourangle)
    ph_sid = 2 * np.pi * (lst_hr / 24.0)

    cols = [np.ones_like(x),
            np.cos(ph_sid), np.sin(ph_sid),        # sidereal 1st (= K1, vector)
            np.cos(2 * ph_sid), np.sin(2 * ph_sid)]  # sidereal 2nd (tensor)
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
    cov = np.linalg.inv(A.T @ A) * np.var(resid) * tau      # red-noise inflated
    err = np.sqrt(np.diag(cov))
    print(f"[diurnal] design condition {cond:.1f} | autocorr tau {tau:.0f} "
          f"chunks ({tau*128/3600:.1f} h) | N_eff {len(x)/tau:.0f}")

    print("[diurnal] constituent amplitudes (red-noise-honest errors):")
    for i, nm in enumerate(names):
        ic, isn = 1 + 2 * i, 2 + 2 * i
        amp = np.hypot(coef[ic], coef[isn])
        e = np.hypot(coef[ic] * err[ic], coef[isn] * err[isn]) / max(amp, 1e-30)
        tag = f"{amp:.3e} +- {e:.1e}  ({amp/max(e,1e-30):.1f} sigma)"
        print(f"           {nm:14s} {tag}")

    # sidereal-line phase vs CMB apex
    a1c, a1s = coef[1], coef[2]
    amp_sid = np.hypot(a1c, a1s)
    e_sid = np.hypot(a1c * err[1], a1s * err[2]) / max(amp_sid, 1e-30)
    lst_max = (np.degrees(np.arctan2(a1s, a1c)) % 360) / 360 * 24    # LST of max
    apex_off = (lst_max - APEX_RA_HR + 12) % 24 - 12
    ul95 = amp_sid + 1.645 * e_sid          # one-sided 95%
    beta = 1.23e-3
    print(f"[diurnal] SIDEREAL LINE (upper limit on CMB signal; includes K1):")
    print(f"           amplitude {amp_sid:.3e} +- {e_sid:.1e} "
          f"({amp_sid/max(e_sid,1e-30):.1f} sigma) -> 95% UL {ul95:.3e}")
    print(f"           phase: max at LST {lst_max:.1f} h; CMB apex {APEX_RA_HR:.1f} h"
          f" (offset {apex_off:+.1f} h)")
    print(f"           kappa*xi (vector) UL = UL/beta = {ul95/beta:.2f} of natural")

    os.makedirs(a.plots, exist_ok=True)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    bins = np.linspace(0, 2 * np.pi, 25)
    idx = np.digitize(ph_sid, bins) - 1
    bm = [np.mean(x[idx == i]) if (idx == i).any() else np.nan for i in range(24)]
    be = [np.std(x[idx == i]) / np.sqrt(max((idx == i).sum(), 1)) * np.sqrt(tau)
          for i in range(24)]
    fig, ax = plt.subplots(figsize=(8, 4))
    c = 0.5 * (bins[:-1] + bins[1:])
    ax.errorbar(c * 24 / (2 * np.pi), bm, be, fmt="o", ms=3)
    pp = np.linspace(0, 2 * np.pi, 300)
    ax.plot(pp * 24 / (2 * np.pi), coef[0] + coef[1] * np.cos(pp)
            + coef[2] * np.sin(pp) + coef[3] * np.cos(2 * pp)
            + coef[4] * np.sin(2 * pp), "-", lw=1)
    ax.axvline(APEX_RA_HR, color="r", ls="--", lw=1, label="CMB apex")
    ax.set(xlabel="local sidereal time (h)", ylabel="fractional PSD dev",
           title=f"sidereal fold, A1={amp_sid:.2e} ({amp_sid/max(e_sid,1e-30):.1f}σ)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(a.plots, "sidereal_diurnal_fit.png"), dpi=120)
    print(f"[diurnal] plot -> {a.plots}/sidereal_diurnal_fit.png")


if __name__ == "__main__":
    main()
