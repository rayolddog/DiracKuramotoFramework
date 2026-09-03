#!/usr/bin/env python3
"""entry_time_order_statistics.py — where does the race's missing half power come from?

The two-channel race scales as tongue width times the SQUARE ROOT of the rate (spectral
controls, 2026-09-02), and the band-to-noise-spread candidate for the half power was not
supported by the tolerance sweep. The remaining candidate is the order statistics of the
clocks' entry times: with N eligible clocks starting at random phases, how fast the
fastest of them reaches the lock band, and how that depends on the coupling.

This script strips the race to its deterministic skeleton — NO noise, NO dwell resets from
noise — using the package's own drift and envelope (``model.adler_drift``,
``model.raised_cosine_envelope``), the frozen flat grid, the frozen band (0.35 rad, on the
contracting side) and dwell (0.5), uniform random initial phases, and asks what exponent
the entry-time order statistics alone produce. If it is about 1.5, the half power is
explained by geometry and random phases; if it is 1 or 2, it is not.

Variants:
  central   one clock per channel at detuning 0 — the pure entry-time race, with the closed
            form t = (1/K) ln( tan(|theta0|/2) / tan(eps/2) ) for |theta0| > eps, else 0
  constant  the full 16-clock grid at constant coupling K = peak over the whole window
  pulsed    the full grid under the raised-cosine pulse — the race's own geometry
For each: fitted exponent across the nine angles; per-coupling fraction of channel-trials
in which some clock starts inside the band (a width-only quantity); median first-entry
and first-commit times and their log-log slopes against K (an effective-hazard exponent).

No prediction is imported; the comparators are the same p = 1 and p = 2 curves as before.
"""

import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from adler_born_two_channel import model  # noqa: E402   (deterministic layer only)
from analysis import fit_exponent, wilson  # noqa: E402

EPS, DWELL, DURATION, CENTRE = 0.35, 0.5, 4.0, 0.0
GRID = np.array([-3.0 + (k + 0.5) * 0.375 for k in range(16)])
ANGLES = [10, 20, 30, 40, 45, 50, 60, 70, 80]
K_TOTAL = 2.0
DT = 2.0 ** -6
rng = np.random.default_rng(2026)


def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi


def channel_times(K_peak, detunings, trials, pulsed, dt=DT):
    """Deterministic skeleton. Returns (first_entry, first_commit, started_inside) per trial."""
    D = np.asarray(detunings, float)
    n = len(D)
    theta = rng.uniform(-np.pi, np.pi, size=(trials, n))
    inside_since = np.full((trials, n), np.nan)
    entry = np.full((trials, n), np.nan)
    commit = np.full((trials, n), np.nan)
    steps = int(round(DURATION / dt))
    t0 = CENTRE - DURATION / 2
    started_inside = None

    def K_at(t):
        return K_peak * (model.raised_cosine_envelope(t, CENTRE, DURATION) if pulsed else 1.0)

    for j in range(steps + 1):
        t = t0 + j * dt
        K = K_at(t)
        elig = K > np.abs(D)                                   # (n,)
        ratio = np.clip(np.where(elig, D / max(K, 1e-300), 0.0), -1.0, 1.0)
        stable = np.arcsin(ratio)                              # (n,)
        locked = elig[None, :] & (np.abs(wrap(theta - stable[None, :])) < EPS) & (np.cos(theta) > 0)
        if j == 0:
            started_inside = locked.any(axis=1)
        newly = locked & np.isnan(inside_since)
        inside_since = np.where(newly, t, inside_since)
        inside_since = np.where(locked, inside_since, np.nan)
        entry = np.where(locked & np.isnan(entry), t, entry)
        done = locked & np.isnan(commit) & ((t - inside_since) >= DWELL - 1e-12)
        commit = np.where(done, t, commit)
        if j == steps:
            break
        # RK4 on d theta/dt = Delta - K(t) sin theta, K piecewise in time
        K1, K2 = K_at(t + dt / 2), K_at(t + dt)
        k1 = model.adler_drift(theta, K, D[None, :])
        k2 = model.adler_drift(theta + 0.5 * dt * k1, K1, D[None, :])
        k3 = model.adler_drift(theta + 0.5 * dt * k2, K1, D[None, :])
        k4 = model.adler_drift(theta + dt * k3, K2, D[None, :])
        theta = theta + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.nanmin(entry, axis=1), np.nanmin(commit, axis=1), started_inside


def race(detunings, trials, pulsed, label):
    cells, rows = [], []
    print(f"\n===== {label}   trials/cell {trials}   dt {DT}")
    print(f" {'phi':>4} {'K_A':>6} {'K_B':>6} {'A':>6} {'B':>6} {'tie':>5} {'unr':>5} {'P_A':>7} {'[Wilson]':>16} {'Born':>6} "
          f"{'inside A/B':>11} {'med entry A/B':>14} {'med commit A/B':>15}")
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        eA, cA, iA = channel_times(KA, detunings, trials, pulsed)
        eB, cB, iB = channel_times(KB, detunings, trials, pulsed)
        a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
        A = int(np.sum(a_ok & (~b_ok | (cA < cB))))
        B = int(np.sum(b_ok & (~a_ok | (cB < cA))))
        tie = int(np.sum(a_ok & b_ok & (cA == cB)))
        unr = int(np.sum(~a_ok & ~b_ok))
        p = A / (A + B) if A + B else float("nan")
        lo, hi = wilson(A, A + B)
        rows.append((deg, KA, KB, A, B, tie, unr, p, lo, hi, iA.mean(), iB.mean(),
                     np.nanmedian(eA), np.nanmedian(eB), np.nanmedian(cA), np.nanmedian(cB)))
        cells.append((KA, KB, A, B))
        print(f" {deg:>4} {KA:6.3f} {KB:6.3f} {A:6d} {B:6d} {tie:5d} {unr:5d} {p:7.3f} [{lo:.3f}, {hi:.3f}] "
              f"{KA**2/(KA**2+KB**2):6.3f} {iA.mean():5.2f}/{iB.mean():<5.2f} "
              f"{np.nanmedian(eA):6.3f}/{np.nanmedian(eB):<6.3f} {np.nanmedian(cA):6.3f}/{np.nanmedian(cB):<6.3f}")
    p_hat, (p_lo, p_hi), _ = fit_exponent(cells)
    # effective-hazard exponent: slope of ln(1 / median first-commit time from window open) vs ln K
    Ks = np.array([r[1] for r in rows] + [r[2] for r in rows])
    Tc = np.array([r[14] for r in rows] + [r[15] for r in rows]) - (CENTRE - DURATION / 2)
    Te = np.array([r[12] for r in rows] + [r[13] for r in rows]) - (CENTRE - DURATION / 2)
    ok = np.isfinite(Tc) & (Tc > 0)
    sc = np.polyfit(np.log(Ks[ok]), np.log(1 / Tc[ok]), 1)[0]
    se = np.polyfit(np.log(Ks[ok]), np.log(1 / Te[ok]), 1)[0]
    print(f"   fitted exponent p = {p_hat:.3f} [{p_lo:.2f}, {p_hi:.2f}]   "
          f"(ties {sum(r[5] for r in rows)}, unresolved {sum(r[6] for r in rows)} of {trials * len(ANGLES)})")
    print(f"   log-log slope of 1/median first-entry time vs K: {se:.2f};  of 1/median first-commit time: {sc:.2f}")
    return p_hat, (p_lo, p_hi)


if __name__ == "__main__":
    print(__doc__)
    t0 = time.time()
    # closed-form check for the central clock, no pulse: t = (1/K) h(theta0)
    th = rng.uniform(-np.pi, np.pi, size=2_000_000)
    h = np.where(np.abs(th) > EPS, np.log(np.tan(np.abs(th) / 2) / np.tan(EPS / 2)), 0.0)
    print("Closed form, single central clock, constant K: entry time = h(theta0)/K with h as above.")
    print(f"  P(start inside band) = {np.mean(h == 0):.4f}  (= eps/pi = {EPS/np.pi:.4f});  "
          f"median h = {np.median(h):.3f}, mean h = {np.mean(h):.3f}, std ln h (h>0) = {np.std(np.log(h[h>0])):.3f}")
    cells = []
    for deg in ANGLES:
        KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
        hA, hB = h[:1_000_000], h[1_000_000:]
        tA, tB = hA / KA, hB / KB
        cells.append((KA, KB, int(np.sum(tA < tB)), int(np.sum(tB < tA))))
    p_hat, (lo, hi), _ = fit_exponent(cells)
    print(f"  two-channel exponent from the closed form (1e6 trials/angle): p = {p_hat:.3f} [{lo:.2f}, {hi:.2f}]")

    results = {}
    results["central, constant K"] = race([0.0], 20000, pulsed=False, label="single central clock per channel, constant K")
    results["central, pulsed"] = race([0.0], 20000, pulsed=True, label="single central clock per channel, raised-cosine pulse")
    results["grid, constant K"] = race(GRID, 20000, pulsed=False, label="full 16-clock grid, constant K")
    results["grid, pulsed"] = race(GRID, 20000, pulsed=True, label="full 16-clock grid, raised-cosine pulse (the race's geometry)")
    print("\nSUMMARY (deterministic skeleton, no noise):")
    for k, (p, (lo, hi)) in results.items():
        print(f"  {k:<22} p = {p:.2f} [{lo:.2f}, {hi:.2f}]")
    print(f"  measured with noise (main sweep, frozen criterion): p = 1.56 [1.44, 1.69]")
    print(f"run time {time.time() - t0:.0f} s")
