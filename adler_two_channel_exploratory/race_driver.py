#!/usr/bin/env python3
"""race_driver.py — exploratory two-channel Adler race, built on the validated one-channel
raw race of ``adler_born_two_channel`` without modifying it.

WHAT THIS IS. The two-channel plan defines the race as: two populations of absorber clocks
on the identical detuning grid, one common photon-pulse envelope, peak couplings
K_A = K cos(phi) and K_B = K sin(phi) from the input polarization angle phi, independent
phase noise for every clock and channel, a fixed physical dwell shared by both channels,
and the trial outcome = the channel of the EARLIEST committing clock (tie if both commit at
the same sampled time; unresolved if neither commits before the pulse closes). Because the
channels do not couple to each other, that race is exactly the pairwise minimum of two
independent one-channel races run on the same envelope with independent keyed noise
streams. This driver therefore runs the package's own ``raw_runner.write_raw_run`` once per
(angle, channel) cell; the pairing, outcome assignment, and every comparison happen in a
separate process (``analysis.py``) that opens the closed ledgers through the package's own
gate. Nothing here imports the analytic prediction, and the driver passes the raw runner
only numbers and labels.

WHAT THIS IS NOT. Every manifest the package writes carries ``numerical_gate =
"diagnostic_only"`` because the package's frozen numerical budget (ticket 07) is not met;
its own analysis layer will call any scaling verdict ``machinery_only``. This run does not
change that. It is an exploratory diagnostic at a reduced budget — fewer clocks and a
coarser timestep than the frozen configuration — labelled ``pilot`` so it can never enter
a production estimate. It does not derive the Born rule, does not establish exclusivity
(the first-winner stop is imposed bookkeeping), and a "commitment" here is one clock
staying inside a declared band around its moving target for a declared time — not a
click, an absorption, or a measurement outcome. The fixed physical dwell is kept fixed:
no inverse-coupling dwell, no amplitude dependence anywhere in the criterion.

Usage:
  python3 race_driver.py --tag t1 --N 16 --dtexp 7 --trials 300 --K 2.0 \
      --angles 10,20,30,40,45,50,60,70,80 --channels A,B [--shard i/m] [--dry-run]

Runs are written beneath ``adler_born_two_channel/results/`` (gitignored by that package)
under names ``x2-<tag>-<chan>-phi<deg>-N<N>-dt<dtexp>``; an existing closed run is skipped,
so the driver is resumable and shardable across processes.
"""

import argparse
import json
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from adler_born_two_channel.raw_config import RawClockGrid, RawEventConfig  # noqa: E402
from adler_born_two_channel import raw_runner  # noqa: E402

# The frozen physics of ticket 07, kept verbatim; only N, timestep and trials are reduced.
PHYSICS = dict(half_width=3.0, phase_diffusion=0.08, lock_tolerance=0.35,
               dwell_time=0.5, pulse_duration=4.0, pulse_centre=0.0)


def run_name(tag, chan, deg, n, dtexp):
    return f"x2-{tag}-{chan}-phi{deg:02d}-N{n}-dt{dtexp}"


def channel_coupling(K, deg, chan):
    phi = math.radians(deg)
    return K * math.cos(phi) if chan == "A" else K * math.sin(phi)


def build_config(name, n, dtexp, trials, K_chan, dwell=None, diffusion=None, pulse=None):
    """Sensitivity overrides (Experiments 5 and 6) change one physical input at a time;
    the fixed dwell stays the same for both channels and every amplitude."""
    return RawEventConfig(
        grid=RawClockGrid(half_width=PHYSICS["half_width"], n_points=n),
        peak_coupling=K_chan,
        pulse_duration=PHYSICS["pulse_duration"] if pulse is None else pulse,
        phase_diffusion=PHYSICS["phase_diffusion"] if diffusion is None else diffusion,
        lock_tolerance=PHYSICS["lock_tolerance"],
        dwell_time=PHYSICS["dwell_time"] if dwell is None else dwell,
        timestep=2.0 ** (-dtexp),
        trials=trials,
        stream_namespace=name,          # independent keyed stream per (angle, channel)
        run_label="pilot",              # quarantined label: never a production estimate
        pulse_centre=PHYSICS["pulse_centre"],
        shadow_trials=1,
    )


def closed(name):
    d = raw_runner.raw_results_directory(name)
    return os.path.isfile(os.path.join(d, "CLOSED.json"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", required=True)
    ap.add_argument("--N", type=int, required=True)
    ap.add_argument("--dtexp", type=int, required=True, help="timestep = 2**-dtexp")
    ap.add_argument("--trials", type=int, required=True)
    ap.add_argument("--K", type=float, default=2.0, help="total peak coupling")
    ap.add_argument("--angles", default="10,20,30,40,45,50,60,70,80")
    ap.add_argument("--channels", default="A,B")
    ap.add_argument("--shard", default="0/1", help="i/m: run jobs[i::m]")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--dwell", type=float, default=None, help="sensitivity: fixed dwell (default 0.5)")
    ap.add_argument("--diffusion", type=float, default=None, help="sensitivity: phase diffusion (default 0.08)")
    ap.add_argument("--pulse", type=float, default=None, help="sensitivity: pulse duration (default 4.0)")
    ap.add_argument("--dwell-mode", choices=("fixed", "inverse", "power"), default="fixed",
                    help="LABELLED CONTROLS ONLY: 'inverse' sets each channel's dwell to "
                         "dwell0 * dwell_ref / K_chan (the plan's positive control); 'power' sets it to "
                         "dwell0 * (dwell_ref / K_chan) ** alpha (a TUNED interpolation between fixed and "
                         "inverse). Both are amplitude-DEPENDENT criteria; never the primary model")
    ap.add_argument("--dwell-ref", type=float, default=math.sqrt(2.0),
                    help="coupling at which the scaled dwell equals dwell0 (default sqrt 2 = the 45-degree coupling)")
    ap.add_argument("--dwell-alpha", type=float, default=1.0, help="exponent for --dwell-mode power")
    a = ap.parse_args()

    angles = [int(x) for x in a.angles.split(",")]
    chans = a.channels.split(",")
    i, m = (int(x) for x in a.shard.split("/"))
    jobs = [(deg, ch) for deg in angles for ch in chans][i::m]

    for deg, ch in jobs:
        name = run_name(a.tag, ch, deg, a.N, a.dtexp)
        K_chan = channel_coupling(a.K, deg, ch)
        dwell0 = PHYSICS["dwell_time"] if a.dwell is None else a.dwell
        if a.dwell_mode == "fixed":
            dwell = dwell0
        elif a.dwell_mode == "inverse":
            dwell = dwell0 * a.dwell_ref / K_chan
        else:
            dwell = dwell0 * (a.dwell_ref / K_chan) ** a.dwell_alpha
        rec = dict(run=name, chan=ch, deg=deg, K_chan=K_chan, N=a.N,
                   timestep=2.0 ** (-a.dtexp), trials=a.trials,
                   dwell=dwell, dwell_mode=a.dwell_mode, diffusion=a.diffusion, pulse=a.pulse)
        if closed(name):
            rec["status"] = "exists"
            print(json.dumps(rec), flush=True)
            continue
        if a.dry_run:
            rec["status"] = "dry"
            print(json.dumps(rec), flush=True)
            continue
        cfg = build_config(name, a.N, a.dtexp, a.trials, K_chan,
                           dwell=dwell, diffusion=a.diffusion, pulse=a.pulse)
        t0 = time.perf_counter()
        rep = raw_runner.write_raw_run(cfg, name)
        rec["seconds"] = round(time.perf_counter() - t0, 1)
        rec["categories"] = dict(rep.categories)
        rec["status"] = "written"
        print(json.dumps(rec), flush=True)


if __name__ == "__main__":
    main()
