#!/usr/bin/env python3
"""spectral_driver.py — Experiment 7 of the two-channel plan (spectral controls), run through
the package's PUBLIC raw API without modifying it.

The raw configuration boundary admits only a flat midpoint grid wider than the coupling, and
refuses arrays, so a non-uniform detuning density cannot be declared to ``write_raw_run``.
But the public factories compose: ``raw_runner.raw_one_clock_path(config, detuning)`` builds
the package's own clock dynamics at any detuning, ``raw_race.PopulationIdentity`` declares
any detuning tuple, ``raw_race.ClockPopulation`` checks the paths against it, and
``raw_race.race_one_channel`` runs the validated race on that population with the
package's keyed noise stream, lock criterion and run window. This driver does exactly that,
one channel per (spectrum, angle, channel), and records each trial's category and commit
time in its own CSV. That record is NOT the package's closed, hashed ledger and passes no
gate; it is an exploratory diagnostic like everything else in this directory, and every
input the package would have stamped ``diagnostic_only`` still is.

Densities (N clocks per channel, symmetric about zero; the flat one is the primary grid,
re-run here so every spectrum shares one code path):
  flat     midpoints of [-3, 3]
  gauss    quantiles of a normal density, sigma = 1.0, at midpoint probabilities
  lorentz  quantiles of a Cauchy density, gamma = 0.75
  peak     flat with N-4 clocks plus four extra clocks at +-0.1 and +-0.3 (narrow central peak)
  notch    flat with the two innermost clocks moved out to +-2.6 (empty centre)
Nothing coupling-dependent enters the population; the same detunings serve every angle and
both channels. Isolation: this file imports no prediction; comparators are computed in
``spectral_analysis.py``.
"""

import argparse
import csv
import json
import math
import os
import sys
import time
from statistics import NormalDist

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from adler_born_two_channel.raw_config import RawClockGrid, RawEventConfig  # noqa: E402
from adler_born_two_channel import raw_runner  # noqa: E402
from adler_born_two_channel.raw_race import (PopulationIdentity, ClockPopulation,  # noqa: E402
                                             race_one_channel)
from race_driver import PHYSICS, channel_coupling  # noqa: E402

SPECTRA = ("flat", "gauss", "lorentz", "peak", "notch")


def flat_midpoints(n, half=3.0):
    return [-half + (k + 0.5) * (2 * half / n) for k in range(n)]


def detunings(spectrum, n):
    ps = [(k + 0.5) / n for k in range(n)]
    if spectrum == "flat":
        d = flat_midpoints(n)
    elif spectrum == "gauss":
        nd = NormalDist(0.0, 1.0)
        d = [nd.inv_cdf(p) for p in ps]
    elif spectrum == "lorentz":
        d = [0.75 * math.tan(math.pi * (p - 0.5)) for p in ps]
    elif spectrum == "peak":
        d = flat_midpoints(n - 4) + [-0.3, -0.1, 0.1, 0.3]
    elif spectrum == "notch":
        base = flat_midpoints(n)
        inner = sorted(base, key=abs)[:2]
        d = [x for x in base if x not in inner] + [-2.6, 2.6]
    else:
        raise ValueError(spectrum)
    d = sorted(float(x) for x in d)
    # exact symmetry, so channel A and channel B are the same material
    for x, y in zip(d, reversed(d)):
        if abs(x + y) > 1e-12:
            raise ValueError(f"{spectrum} detunings are not symmetric: {x} vs {y}")
    return d


def run_name(tag, spectrum, chan, deg, n, dtexp):
    return f"spec-{tag}-{spectrum}-{chan}-phi{deg:02d}-N{n}-dt{dtexp}"


def race(tag, spectrum, chan, deg, n, dtexp, trials, K, outdir):
    name = run_name(tag, spectrum, chan, deg, n, dtexp)
    path = os.path.join(outdir, name + ".csv")
    if os.path.isfile(path):
        return dict(run=name, status="exists")
    K_chan = channel_coupling(K, deg, chan)
    config = RawEventConfig(
        grid=RawClockGrid(half_width=PHYSICS["half_width"], n_points=n),   # validation only
        peak_coupling=K_chan, pulse_duration=PHYSICS["pulse_duration"],
        phase_diffusion=PHYSICS["phase_diffusion"], lock_tolerance=PHYSICS["lock_tolerance"],
        dwell_time=PHYSICS["dwell_time"], timestep=2.0 ** (-dtexp), trials=trials,
        stream_namespace=name, run_label="pilot", pulse_centre=PHYSICS["pulse_centre"],
        shadow_trials=1)
    dets = detunings(spectrum, n)
    paths = tuple(raw_runner.raw_one_clock_path(config, d) for d in dets)
    identity = PopulationIdentity(model="full", pulse_digest=paths[0].train.digest,
                                  detunings=tuple(dets))
    population = ClockPopulation(paths, identity)
    mesh, start_index, steps = raw_runner.raw_run_window(config)
    stream = raw_runner.raw_noise_stream(config, mesh.time_at(0))
    criterion = raw_runner.raw_lock_criterion(config)

    t0 = time.perf_counter()
    rows = []
    for trial in range(trials):
        out = race_one_channel(population, criterion, stream, trial, start_index, steps)
        rows.append(dict(trial=trial, category=out.category,
                         commit_time="" if out.commit_time is None else repr(out.commit_time),
                         winners="|".join(str(w) for w in out.winners)))
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as f:
        f.write("# " + json.dumps(dict(run=name, spectrum=spectrum, chan=chan, deg=deg,
                                       K_chan=K_chan, N=n, timestep=2.0 ** (-dtexp),
                                       trials=trials, detunings=dets,
                                       physics=PHYSICS, numerical_gate="diagnostic_only",
                                       ledger="exploratory CSV, not the package's closed ledger")) + "\n")
        w = csv.DictWriter(f, fieldnames=["trial", "category", "commit_time", "winners"])
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, path)
    cats = {}
    for r in rows:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    return dict(run=name, status="written", seconds=round(time.perf_counter() - t0, 1),
                categories=cats, K_chan=K_chan)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--N", type=int, default=16)
    ap.add_argument("--dtexp", type=int, default=7)
    ap.add_argument("--trials", type=int, default=200)
    ap.add_argument("--K", type=float, default=2.0)
    ap.add_argument("--angles", default="10,30,45,60,80")
    ap.add_argument("--spectra", default=",".join(SPECTRA))
    ap.add_argument("--channels", default="A,B")
    ap.add_argument("--shard", default="0/1")
    ap.add_argument("--outdir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "spectral_runs"))
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    angles = [int(x) for x in a.angles.split(",")]
    i, m = (int(x) for x in a.shard.split("/"))
    jobs = [(s, deg, ch) for s in a.spectra.split(",") for deg in angles for ch in a.channels.split(",")][i::m]
    for s, deg, ch in jobs:
        rec = race(a.tag, s, ch, deg, a.N, a.dtexp, a.trials, a.K, a.outdir)
        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
