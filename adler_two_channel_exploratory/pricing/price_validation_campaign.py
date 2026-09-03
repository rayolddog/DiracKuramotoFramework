#!/usr/bin/env python3
"""
price_validation_campaign.py — the bounded benchmark-and-pricing session for
the intended-configuration validation campaign (Ticket 07 pricing plan).

Plan being implemented (read it first; it is the authority for every rule
below):

  traycer_artifacts/debates/born-selection-roundtable/adler-tongue-born-candidate/
  two-channel-stochastic-model/single-channel-stochastic-commitment/tickets/
  07-feasibility-pilot-and-freeze/validation-campaign-pricing-plan/index.md

This file lives OUTSIDE the package ``adler_born_two_channel`` and imports its
kernels read-only.  It never writes into the package, never runs the package's
verifier, never runs a validation stage, pilot, production run, sensitivity or
exponent fit, and never opens pilot/exponent outputs.  Every fixture it uses is
in memory, in a child process that exits when its case is done; the only files
it writes are its own ``observations.json`` and ``PRICING_REPORT.md`` beside
this script, and a per-case JSON handoff in the scratchpad that is removed in
``finally``.

Modes
-----
  --run          the recorded one-hour session (parent orchestrator)
  --case C I     [internal] run case I of component C in this process
  --derive-only  rebuild every price and digest from observations.json
  --selftest     run each kernel path once at a tiny size (not recorded)

The four components, their timed boundaries and their work units are the
plan's; the size cases, the stage-work definitions and every interpretation of
an ambiguous phrase are recorded in ``INTERPRETATIONS`` and printed in the
report so that a reviewer can disagree with a named choice rather than an
unnamed one.
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
import platform
import resource
import subprocess
import sys
import threading
import time
import tracemalloc
import warnings
from pathlib import Path

sys.dont_write_bytecode = True                  # never touch the package's __pycache__
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

import numpy as np                               # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PKG = REPO / "adler_born_two_channel"
RESULTS = PKG / "results"
PLAN = (REPO / "traycer_artifacts/debates/born-selection-roundtable/"
        "adler-tongue-born-candidate/two-channel-stochastic-model/"
        "single-channel-stochastic-commitment/tickets/"
        "07-feasibility-pilot-and-freeze/validation-campaign-pricing-plan/index.md")
OBSERVATIONS = HERE / "observations.json"
REPORT = HERE / "PRICING_REPORT.md"
SCRATCH = Path(os.environ.get(
    "PRICING_SCRATCH",
    "/private/tmp/claude-501/-Users-john-bramble-Projects-Physics-DiracKuramotoFramework/"
    "63b0fc51-d326-44ba-9e7c-eccecb8f1e8f/scratchpad")) / "pricing_cases"

sys.path.insert(0, str(REPO))

# ---------------------------------------------------------------------------
# Frozen protocol constants (from the plan)
# ---------------------------------------------------------------------------
WALL_CEILING_S = 3600.0            # one-hour cumulative wall for the session
RSS_CEILING_BYTES = 2 * 1024 ** 3  # 2 GiB per-process peak RSS
CONTINGENCY = 1.5                  # frozen time contingency
RATE_BAND = 1.5                    # normalized rate may vary by at most this
MIN_SPAN = 4.0                     # cases must span at least this in work
STAGE_SPAN = 16.0                  # planned stage within this of the largest case
MEMORY_REVERSAL = 0.20             # no unexplained reversal above 20%
REPEATS = 3
WARMUPS = 1
PREFLIGHT_SAFETY = 1.25            # on top of the slowest measured rate

# ---------------------------------------------------------------------------
# Baseline shapes, copied from the package verifier's frozen constants.
# (verify.py is read here as TEXT for provenance; it is never imported.)
# ---------------------------------------------------------------------------
S3 = dict(coupling=0.8, detuning=0.3, tolerance=0.4, diffusion=0.05,
          horizon=2.0, fractions=(0.25, 0.5, 0.75), fine_steps=2048,
          strides=(8, 4, 2), walkers=6000, chunk=1500, window=1024,
          space=600, time=600, quantile=0.35, resamples=200,
          namespace="t04-s3-endpoint", seed=20260828)
S3_QUANTILE_NAME = f"exit_quantile_p{int(S3['quantile'] * 100)}"
AUDIT = dict(peak=1.0, duration=4.0, tolerance=0.25, dwell=0.30,
             diffusion=0.02, fine_step=0.008, origin=-2.0, steps=500,
             strides=(4, 2, 1), trials=40, replicates=4, resamples=200,
             clocks=((0, 0.0, "central"), (1, 0.45, "interior+"),
                     (2, -0.88, "near_edge-")),
             survival_fractions=(0.45, 0.60, 0.80), quantile=0.20,
             seed=20260901, physical_namespace="t04-audit-physical",
             audit_namespace="t04-audit-auxiliary")
AUDIT_QUANTILE_NAME = f"commit_time_quantile_p{int(AUDIT['quantile'] * 100)}_shift"

# The seven frozen stages: verify.py ``_T07_STAGES`` (label, unit, attacks,
# kernel, timestep factor, sample factor, spatial factor, depends_on).
T07_STAGES = (
    ("stationary probability, dt/16 at doubled space", "probability",
     "timestep_bias", "oracle_cell", 0.0625, 1.0, 4, ""),
    ("stationary probability, dt/64 at quadrupled space", "probability",
     "timestep_bias", "oracle_cell", 0.015625, 1.0, 16,
     "stationary probability, dt/16 at doubled space"),
    ("stationary probability, dt/256 at eightfold space", "probability",
     "timestep_bias", "oracle_cell", 0.00390625, 1.0, 64,
     "stationary probability, dt/64 at quadrupled space"),
    ("stationary time quantile, dt/256 at eightfold space", "time",
     "timestep_bias", "oracle_cell", 0.00390625, 1.0, 64,
     "stationary probability, dt/256 at eightfold space"),
    ("moving-band probability, 64x master trials", "probability",
     "sampling_error", "resample_observation", 1.0, 64.0, 64, ""),
    ("moving-band probability, dt/16 replay", "probability",
     "timestep_bias", "resample_observation", 0.0625, 1.0, 16,
     "moving-band probability, 64x master trials"),
    ("moving-band time quantile, 1024x master trials", "time",
     "sampling_error", "resample_observation", 1.0, 1024.0, 1024,
     "moving-band probability, 64x master trials"),
)
STAGE_SHORT = ("S1", "S2", "S3", "S4", "M5", "M6", "M7")
# Space factor per stationary stage, read from the labels "doubled",
# "quadrupled", "eightfold" (the frozen ``spatial`` shape 4/16/64 is that
# factor squared, i.e. the dense-propagator relative cost, not a grid factor).
SPACE_FACTOR = {"S1": 2, "S2": 4, "S3": 8, "S4": 8}

COMPONENTS = ("refinement_comparison", "stationary_construction",
              "moving_replay", "stationary_solve")

INTERPRETATIONS = [
    ("results/ precondition",
     "The plan requires an 'empty results/ state'.  The package's results/ "
     "holds 198 pre-existing run directories from unrelated exploratory work "
     "that this session must not touch.  None of the four kernels reads or "
     "writes results/.  The verifiable condition applied instead is 'results/ "
     "unchanged': a stat snapshot (path, size, mtime, mode) of every entry is "
     "taken before and after every case, and a SHA-256 snapshot of every file "
     "at session start and end; any difference is a failed precondition."),
    ("stationary solve — unit and cases",
     "Unit is the plan's 'space-time cell' = space_steps x time_steps.  The "
     "propagator is dense (killed_diffusion._propagator: 'Dense rather than "
     "banded'), so cost per cell grows ~linearly with space_steps and a case "
     "series that varies space cannot pass the 1.5x band.  To keep the plan's "
     "unit AND stay conservative for every stationary stage, all three cases "
     "are run at the LARGEST stage space (M = 4800, 'eightfold' of the 600 "
     "reference grid) and vary only time_steps; a per-cell rate measured at "
     "M = 4800 bounds the per-cell rate at M = 1200 and 2400 from above."),
    ("stationary solve — stage grids",
     "'dt/f at s-fold space' is read as the oracle grid (600*s) x (600*f): "
     "the campaign refines the oracle's time grid with the endpoint timestep "
     "it is the reference for, and its space grid by the stated factor "
     "('space refined separately from time').  Stage cells: S1 1200x9600, "
     "S2 2400x38400, S3/S4 4800x153600."),
    ("stationary endpoint and sample construction — boundary",
     "'From solved ladder outputs through exit-time/censoring arrays and "
     "ValidationDataset construction' is read as: the oracle SurvivalSolution "
     "is an untimed input; the timed region is the paired endpoint walk that "
     "GENERATES the exit-time/edge arrays (verify.py _s3_measured, mirrored "
     "call for call), the censoring, the PairedSample and ValidationDataset "
     "construction, and the dataset digest.  The alternative reading (walk "
     "excluded) would leave the 'stationary endpoint generation' the plan says "
     "was omitted from pricing still unpriced."),
    ("stationary endpoint and sample construction — unit",
     "'walker-position-level observation' is read as one endpoint observation "
     "of one walker at one start position at one refinement level, i.e. "
     "walkers x positions x sum_over_levels(fine_steps / stride).  This is the "
     "count of endpoint evaluations the scheme performs and it scales with "
     "the timestep lever (x16 at dt/16).  The alternative reading (walkers x "
     "positions x levels, a shape count) does not move with dt and would "
     "price dt/256 at the reference cost."),
    ("stationary endpoint and sample construction — cases",
     "6000 walkers (sample factor 1 in every stationary stage), chunk 1500, "
     "window 1024, strides (8,4,2), fine steps 49152 / 98304 / 196608 "
     "(dt/24, dt/48, dt/96 relative to the 2048-step reference).  A 4x span: "
     "the ValidationDataset construction carries a fixed ~3.8 s cost at 6000 "
     "walkers (an O(walkers^2) identity-uniqueness check in "
     "killed_diffusion._require_names, re-run on every PairedSample rebuild), "
     "so a wider span starting lower would fail the 1.5x band for a reason "
     "that is not the walk."),
    ("moving-band replay — counters",
     "Counter 1 'physical interval' = elementary intervals of strictly "
     "positive duration walked by replay_pulse (the walk is shared by all "
     "replicates), summed over trials x clocks x strides.  Counter 2 'audited "
     "interval evaluation' = intervals whose schedule state is 'interior' "
     "(rising + falling in AuditedRun) times the replicate count: every such "
     "interval is classified and decided once per auxiliary replica.  Both "
     "are exact functions of (clock, stride, mesh) and the trial count."),
    ("moving-band replay — cases and dataset",
     "20 / 80 / 320 master trials at the reference pulse, mesh (origin -2.0, "
     "step 0.008, 500 steps), 3 clocks, strides (4,2,1), 4 replicates, initial "
     "phases the verifier's deterministic sweep of the circle over the case's "
     "own trial count.  The pooled ValidationDataset is assembled AFTER the "
     "timed region exactly as verify.py _audit_samples does, untimed; its "
     "seconds are recorded as a diagnostic and its digest is the output "
     "identity."),
    ("moving-band replay — stage work",
     "M5 = 64 x 40 = 2560 master trials on the reference mesh; M6 = 40 trials "
     "on a 16x finer mesh (step 0.0005, 8000 steps, same strides, so the "
     "ladder timesteps are 0.002/0.001/0.0005); M7 = 40960 trials.  Counters "
     "for every stage are computed exactly from the schedule."),
    ("refinement comparison — cases",
     "Synthetic datasets with the moving-band layout (6 samples: commit "
     "probability shift, three survival shifts, the p20 commit-time quantile "
     "shift with a baseline arm, added_resets_mean without one; 12 audited "
     "members = 3 clocks x 4 replicates; 3 primary members; 3 levels), "
     "generated by a seeded RNG, at 600 / 1200 / 2400 clusters (a 4x span, "
     "the plan's minimum), 200 resamples.  Values do not affect the "
     "bootstrap's cost; the layout does.  The moving layout carries 15 "
     "members per cluster-level against the stationary layout's one, so its "
     "per-observation rate bounds the stationary comparisons from above (a "
     "design probe of the true stationary-layout comparison at 6000 walkers "
     "gave 53.6 ns per observation).  A 16x span is impossible under the 1.5x "
     "band: the per-observation cost is U-shaped (see the next item), and the "
     "best 16x ladder probed, 300/1200/4800, varies 1.585x."),
    ("refinement comparison — quadratic term",
     "compare_refinement rebuilds every PairedSample and pays "
     "_require_names' O(clusters^2) duplicate check per sample "
     "(killed_diffusion.py, `listed.count(e)` for every label).  Design "
     "probes of nanoseconds per resample-observation against cluster count: "
     "200: 73.1, 300: 59.8, 400: 53.3, 600: 48.3, 800: 45.3, 1200: 44.1, "
     "1600: 46.3, 2400: 50.5, 3200: 54.7, 4800: 69.9, 6400: 83.3, and from "
     "earlier probes 20480: 188.  Below ~800 clusters the fixed per-resample "
     "Python overhead dominates; above ~3000 the quadratic check does.  The "
     "plan's unit is therefore valid only in that window, and the cases are "
     "placed inside it.  Consequences: M6's comparison (40 clusters) is "
     "overhead-dominated and its priced term understates a cost that is "
     "tens of milliseconds in absolute terms; M7's comparison (40960 "
     "clusters, ~0.5 us per observation extrapolated) is 17x beyond the "
     "largest measured point and fails the 16x rule."),
    ("tracemalloc",
     "The untimed warmup runs under tracemalloc and supplies the traced peak; "
     "the three timed repeats run untraced so that the price reflects the "
     "kernel and not the tracer (tracemalloc inflates the pure-Python replay "
     "4.5x).  All four outputs (warmup + 3 repeats) must be digest-identical."),
    ("process peak RSS",
     "Each case runs in a fresh child process; 'process peak RSS' is the "
     "child's ru_maxrss at exit (bytes on Darwin), which includes the untimed "
     "fixture construction — the conservative reading.  A sampled peak over "
     "the timed repeats is recorded beside it.  The parent polls the child's "
     "RSS every 20 ms and kills it above 2 GiB."),
    ("'within 16x' and '1.5x'",
     "Both are read inclusively: stage_work <= 16 x largest measured work, "
     "and max_rate / min_rate <= 1.5, with a 1e-9 relative tolerance."),
    ("stage S4",
     "Priced as a full independent stage (solve + walk + comparison at "
     "dt/256, eightfold space).  If S3's solve and walk are reused, S4's "
     "marginal cost is its comparison alone; the report shows both."),
    ("preflight",
     "A case is launched only if elapsed + predicted <= 3600 s, where "
     "predicted = declared work x (slowest normalized rate so far in the "
     "component, or a declared prior for the first case) x (3 + traced-warmup "
     "factor) x 1.25.  A skipped case makes its component pricing_unresolved."),
]

# Declared priors for the first case of each component (seconds per unit and
# traced-warmup factor), from short design probes on this machine.  Only the
# preflight reads them; no price does.
PREFLIGHT_PRIORS = {
    "stationary_solve": (6.0e-7, 1.3),          # s per cell at M=4800
    "stationary_construction": (0.7e-7, 1.6),   # s per endpoint observation
    "moving_replay": (1.4e-4, 5.0),             # s per physical interval
    "refinement_comparison": (8.0e-8, 1.6),     # s per resample-observation
}


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def sha256_bytes(*parts: bytes) -> str:
    h = hashlib.sha256()
    for part in parts:
        h.update(len(part).to_bytes(8, "big"))
        h.update(part)
    return h.hexdigest()


def canonical_json(payload) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"),
                      allow_nan=False, default=_json_default)


def _json_default(value):
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, tuple):
        return list(value)
    if dataclasses.is_dataclass(value):
        return dataclasses.asdict(value)
    raise TypeError(f"not serializable: {type(value).__name__}")


def digest_arrays(*arrays) -> str:
    return sha256_bytes(*[np.ascontiguousarray(a, dtype="<f8").tobytes()
                          for a in arrays])


def results_stat_snapshot(root: Path):
    """(relative path, size, mtime_ns, mode) for every entry under ``root``."""
    rows = []
    if not root.exists():
        return ("<absent>",)
    for path in sorted(root.rglob("*")):
        st = path.lstat()
        rows.append((str(path.relative_to(root)), st.st_size, st.st_mtime_ns,
                     st.st_mode))
    return tuple(rows)


def results_sha_snapshot(root: Path) -> str:
    h = hashlib.sha256()
    if not root.exists():
        return "absent"
    for path in sorted(root.rglob("*")):
        rel = str(path.relative_to(root)).encode()
        h.update(len(rel).to_bytes(4, "big")); h.update(rel)
        if path.is_file():
            h.update(hashlib.sha256(path.read_bytes()).digest())
        else:
            h.update(b"<dir>")
    return h.hexdigest()


def package_stat_digest() -> str:
    """Digest of every entry under the package EXCEPT results/ (covered
    separately), including __pycache__, so a stray .pyc write is caught."""
    rows = []
    for path in sorted(PKG.rglob("*")):
        if RESULTS in path.parents or path == RESULTS:
            continue
        st = path.lstat()
        rows.append((str(path.relative_to(PKG)), st.st_size, st.st_mtime_ns))
    return hashlib.sha256(canonical_json(rows).encode()).hexdigest()


def machine_identity() -> dict:
    def sysctl(name):
        try:
            return subprocess.run(["sysctl", "-n", name], capture_output=True,
                                  text=True, timeout=5).stdout.strip()
        except Exception:                                   # noqa: BLE001
            return ""
    import psutil                                            # noqa: PLC0415
    blas = ""
    try:
        cfg = np.show_config(mode="dicts")
        blas = cfg.get("Build Dependencies", {}).get("blas", {}).get("name", "")
    except Exception:                                        # noqa: BLE001
        pass
    return {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "cpu_brand": sysctl("machdep.cpu.brand_string"),
        "physical_cpus": sysctl("hw.physicalcpu"),
        "logical_cpus": sysctl("hw.ncpu"),
        "performance_cores": sysctl("hw.perflevel0.physicalcpu"),
        "efficiency_cores": sysctl("hw.perflevel1.physicalcpu"),
        "memory_bytes": sysctl("hw.memsize"),
        "os_version": sysctl("kern.osproductversion"),
        "python_version": platform.python_version(),
        "python_executable": sys.executable,
        "numpy_version": np.__version__,
        "numpy_blas": blas,
        "psutil_version": psutil.__version__,
    }


def environment_fingerprint(identity: dict) -> str:
    keys = ("platform", "machine", "cpu_brand", "physical_cpus", "logical_cpus",
            "memory_bytes", "os_version", "python_version", "numpy_version",
            "numpy_blas")
    return hashlib.sha256(canonical_json({k: identity[k] for k in keys})
                          .encode()).hexdigest()


def source_fingerprint() -> dict:
    """The package's own fingerprint (experiments.source_fingerprint) plus
    the per-file SHA-256 list it is taken over."""
    from adler_born_two_channel import experiments as xpr                 # noqa
    fp = xpr.source_fingerprint()
    return {"digest": fp.digest, "files": [list(pair) for pair in fp.files],
            "python_version": fp.python_version,
            "numpy_version": fp.numpy_version, "platform": fp.platform}


# ---------------------------------------------------------------------------
# Kernel fixtures — each returns (input_digest, run, digest_of_output, meta)
# ---------------------------------------------------------------------------
def _band_and_starts():
    from adler_born_two_channel import moving_band_audit as mba
    lower, upper = mba.admissible_band(S3["coupling"], S3["detuning"],
                                       S3["tolerance"])
    starts = np.array([lower + (upper - lower) * f for f in S3["fractions"]])
    return lower, upper, starts


def fixture_stationary_solve(spec):
    from adler_born_two_channel import killed_diffusion as kdf
    lower, upper, starts = _band_and_starts()
    geometry = kdf.BandGeometry(lower, upper, S3["diffusion"], S3["coupling"],
                                S3["detuning"])
    M, N = spec["space_steps"], spec["time_steps"]
    input_digest = hashlib.sha256(canonical_json({
        "kernel": "killed_diffusion.solve_survival",
        "geometry": [geometry.lower, geometry.upper, geometry.diffusion,
                     geometry.coupling, geometry.detuning],
        "positions": starts.tolist(), "horizon": S3["horizon"],
        "space_steps": M, "time_steps": N}).encode()).hexdigest()

    def run():
        return kdf.solve_survival(geometry, starts, S3["horizon"], M, N)

    def digest(sol):
        finite = all(np.all(np.isfinite(a)) for a in
                     (sol.survival, sol.lower_exit, sol.upper_exit))
        return (digest_arrays(sol.positions, sol.times, sol.survival,
                              sol.lower_exit, sol.upper_exit), finite,
                {"closure_residual": sol.closure_residual})

    return input_digest, run, digest, {"space_steps": M, "time_steps": N,
                                       "positions": 3, "horizon": S3["horizon"]}


def fixture_stationary_construction(spec):
    """Mirror of verify.py ``_s3_measured`` + ``_s3_dataset`` (verbatim
    algorithm, data layout and numerical path), timed as one region."""
    from adler_born_two_channel import killed_diffusion as kdf
    from adler_born_two_channel import stochastic as stoch
    lower, upper, starts = _band_and_starts()
    walkers, fine_steps = spec["walkers"], spec["fine_steps"]
    strides, chunk, window = S3["strides"], S3["chunk"], S3["window"]
    positions = starts.size
    step = S3["horizon"] / fine_steps
    mesh = stoch.FinestMesh(0.0, step)
    stream = stoch.PhaseNoiseStream(S3["namespace"], mesh, S3["diffusion"])
    # The solved oracle is an UNTIMED input (reference values only).
    geometry = kdf.BandGeometry(lower, upper, S3["diffusion"], S3["coupling"],
                                S3["detuning"])
    oracle = kdf.solve_survival(geometry, starts, S3["horizon"], S3["space"],
                                S3["time"])
    reference = {
        "survival": oracle.survival[:, -1],
        S3_QUANTILE_NAME: oracle.quantiles([S3["quantile"]])[:, 0],
        "exit_count_upper": oracle.upper_exit[:, -1],
        "exit_count_lower": oracle.lower_exit[:, -1],
    }
    labels = tuple(f"x={value:.6f}" for value in starts)
    timesteps = tuple(step * s for s in strides)
    sampling = kdf.SamplingDesign(
        unit="endpoint walker: one independent keyed Brownian stream",
        clusters=walkers, replications=1,
        method="cluster bootstrap over walkers, one resample of clusters "
               "evaluated at every refinement level so that level contrasts "
               "are paired", resamples=S3["resamples"], coverage=2.0,
        seed=S3["seed"])
    contract = kdf.RefinementContract(timesteps, 2.0, sampling)
    input_digest = hashlib.sha256(canonical_json({
        "kernel": "stationary endpoint walk + ValidationDataset",
        "stream_prefix": stream.stream_prefix, "mesh": mesh.identity,
        "walkers": walkers, "fine_steps": fine_steps, "strides": strides,
        "chunk": chunk, "window": window, "positions": starts.tolist(),
        "band": [lower, upper], "reference_grid": [S3["space"], S3["time"]],
        "reference": {k: v.tolist() for k, v in reference.items()},
        "contract": contract.canonical}).encode()).hexdigest()

    def run():
        paired = True
        exits = {s: np.full((walkers, positions), np.inf) for s in strides}
        uppers = {s: np.zeros((walkers, positions), dtype=bool) for s in strides}
        for base in range(0, walkers, chunk):
            clocks = np.arange(base, min(base + chunk, walkers))
            rows = clocks.size
            state = {s: {"phase": np.repeat(starts[None, :], rows, axis=0),
                         "alive": np.ones((rows, positions), dtype=bool)}
                     for s in strides}
            for offset, block in stream.stream_leaf_blocks(0, clocks, 0,
                                                           fine_steps, window):
                for s in strides:
                    groups = block.shape[1] // s
                    coarse = stoch._sum_left_to_right(
                        block.reshape(rows, groups, s))
                    if base == 0 and offset == 0:
                        control = stream._coarse_kicks_uniform(
                            0, clocks[:32], 0, window, s)
                        paired &= bool(np.array_equal(coarse[:32], control))
                    span = step * s
                    live = state[s]
                    for group in range(groups):
                        moment = (offset + (group + 1) * s) * step
                        live["phase"] = np.where(
                            live["alive"],
                            live["phase"]
                            + (S3["detuning"]
                               - S3["coupling"] * np.sin(live["phase"])) * span
                            + coarse[:, group:group + 1],
                            live["phase"])
                        left = live["alive"] & ((live["phase"] <= lower)
                                                | (live["phase"] >= upper))
                        if left.any():
                            rowsel = slice(base, base + rows)
                            block_exit = exits[s][rowsel]
                            block_exit[left] = moment
                            exits[s][rowsel] = block_exit
                            block_upper = uppers[s][rowsel]
                            block_upper |= left & (live["phase"] >= upper)
                            uppers[s][rowsel] = block_upper
                            live["alive"] &= ~left
        # ---- censoring arrays and ValidationDataset (verify._s3_dataset) --
        stack = {name: [] for name in reference}
        for s in strides:
            times = exits[s]
            alive = np.isinf(times)
            stack["survival"].append(alive.astype(float))
            stack[S3_QUANTILE_NAME].append(np.minimum(times, S3["horizon"]))
            stack["exit_count_upper"].append(
                (uppers[s] & ~alive).astype(float))
            stack["exit_count_lower"].append(
                (~uppers[s] & ~alive).astype(float))
        names = tuple(f"walker-{index}" for index in range(walkers))
        samples = []
        for name, pages in stack.items():
            block = np.stack(pages, axis=-1)
            for index, label in enumerate(labels):
                samples.append(kdf.PairedSample(
                    name, label, block[:, index, :][:, None, :], None,
                    float(reference[name][index]), names, ("outcome",)))
        dataset = kdf.ValidationDataset(
            "pricing: stationary frozen endpoint sample", contract,
            tuple(samples))
        return dataset, dataset.digest, paired, exits, uppers

    def digest(out):
        dataset, ddigest, paired, exits, uppers = out
        raw = digest_arrays(*[exits[s] for s in strides],
                            *[uppers[s].astype(float) for s in strides])
        finite = all(np.all(np.isfinite(sm.values)) for sm in dataset.samples)
        return (sha256_bytes(ddigest.encode(), raw.encode()), finite and paired,
                {"dataset_digest": ddigest, "paired_bitwise": bool(paired),
                 "samples": len(dataset.samples)})

    work = walkers * positions * sum(fine_steps // s for s in strides)
    return input_digest, run, digest, {"walkers": walkers,
                                       "fine_steps": fine_steps,
                                       "strides": strides, "positions": positions,
                                       "endpoint_observations": work}


def _audit_objects(step, namespace_suffix=""):
    from adler_born_two_channel import (commitment as cmt, dynamics as dyn,
                                        model as mdl, moving_band_audit as mba,
                                        stochastic as stoch)
    train = dyn.PulseTrain((mdl.RaisedCosinePulse(AUDIT["peak"],
                                                  AUDIT["duration"],
                                                  center=0.0),))
    criterion = cmt.LockCriterion(AUDIT["tolerance"], AUDIT["dwell"])
    mesh = stoch.FinestMesh(AUDIT["origin"], step)
    stream = stoch.PhaseNoiseStream(AUDIT["physical_namespace"], mesh,
                                    AUDIT["diffusion"])
    audit = mba.AuditUniformStream(AUDIT["audit_namespace"], mesh, 0)
    paths = {clock: dyn.ClockPath(det, train, "full", 0.0)
             for clock, det, _ in AUDIT["clocks"]}
    return train, criterion, mesh, stream, audit, paths


def count_replay_intervals(step, steps, strides):
    """Exact per-trial counters for one mesh: (physical intervals with
    positive duration, eligible 'interior' intervals) summed over clocks and
    strides — mirrors paired_leaves' coarse-segment construction without
    generating any leaf."""
    from adler_born_two_channel.raw_experiments import elementary_segments
    train, criterion, mesh, stream, audit, paths = _audit_objects(step)
    physical = 0
    eligible = 0
    per = {}
    for stride in strides:
        for clock, _, _ in AUDIT["clocks"]:
            path = paths[clock]
            crossings = path._cached_schedule.crossings(clock, train.digest)
            if stride == 1:
                segments = elementary_segments(mesh, 0, steps, crossings)
            else:
                moments = sorted({c.time for c in crossings})
                segments = []
                for group in range(steps // stride):
                    first = mesh.time_at(group * stride)
                    second = mesh.time_at((group + 1) * stride)
                    inner = [m for m in moments if first <= m < second]
                    bounds = [first] + inner + [second]
                    segments.extend(zip(bounds, bounds[1:]))
            phys = sum(1 for a, b in segments if b > a)
            elig = sum(1 for a, b in segments if b > a and
                       path._cached_schedule.interval_state(a, b) == "interior")
            per[f"stride={stride}/clock={clock}"] = (phys, elig)
            physical += phys
            eligible += elig
    return physical, eligible, per


def build_audit_dataset(kdf, primary, audited, added, clusters, timesteps,
                        label):
    """verify.py ``_audit_samples`` + ``_audit_dataset``, position 'pooled'."""
    horizon = AUDIT["origin"] + AUDIT["duration"]           # train.support()[1]
    start = AUDIT["origin"]
    moments = tuple(start + (horizon - start) * f
                    for f in AUDIT["survival_fractions"])
    primary = np.minimum(primary, horizon)
    audited = np.minimum(audited, horizon)
    committed = lambda block: (block < horizon).astype(float)         # noqa
    trials = tuple(f"trial-{index}" for index in range(clusters))
    arms = [clock for clock, _, _ in AUDIT["clocks"]]
    audited_members = tuple(f"clock-{clock}/replicate-{rep}"
                            for clock in arms
                            for rep in range(AUDIT["replicates"]))
    primary_members = tuple(f"clock-{clock}" for clock in arms)
    pair = lambda v, b: (v, b, 0.0, trials, audited_members, primary_members)   # noqa
    samples = [kdf.PairedSample("commit_probability_shift", "pooled",
                                *pair(committed(audited), committed(primary)))]
    for moment, fraction in zip(moments, AUDIT["survival_fractions"]):
        samples.append(kdf.PairedSample(
            f"survival_shift_at_{fraction:.2f}", "pooled",
            *pair((audited > moment).astype(float),
                  (primary > moment).astype(float))))
    samples.append(kdf.PairedSample(AUDIT_QUANTILE_NAME, "pooled",
                                    *pair(audited, primary)))
    samples.append(kdf.PairedSample("added_resets_mean", "pooled", added, None,
                                    0.0, trials, audited_members))
    sampling = kdf.SamplingDesign(
        unit="master trial identifier: one initial phase, shared by every "
             "clock and by every refinement level",
        clusters=clusters, replications=AUDIT["replicates"],
        method="cluster bootstrap over master trial identifiers, one resample "
               "of clusters evaluated at every refinement level so that level "
               "contrasts are paired; auxiliary replications travel with their "
               "cluster", resamples=AUDIT["resamples"], coverage=2.0,
        seed=AUDIT["seed"])
    contract = kdf.RefinementContract(timesteps, 2.0, sampling)
    return kdf.ValidationDataset(label, contract, tuple(samples)), contract


def audit_budgets(kdf, contract, label, coarsest_step):
    rows = [("commit_probability_shift", "probability", "mean", 0.5, True,
             (0.10, 4.0, 0.010))]
    rows += [(f"survival_shift_at_{f:.2f}", "probability", "mean", 0.5, True,
              (0.10, 4.0, 0.010)) for f in AUDIT["survival_fractions"]]
    rows.append((AUDIT_QUANTILE_NAME, "time", "quantile", AUDIT["quantile"],
                 True, (0.10, 4.0, coarsest_step)))
    rows.append(("added_resets_mean", "count", "mean", 0.5, False,
                 (3.0, 30.0, 0.0)))
    budgets = tuple(kdf.ValidationBudget(n, u, a, r, fl, d, "pooled", e, lv)
                    for n, u, e, lv, d, (a, r, fl) in rows)
    return kdf.FrozenBudgets(label, contract, budgets)


def fixture_moving_replay(spec):
    """Mirror of verify.py ``_audit_ladder`` (timed) + ``_audit_dataset``
    (untimed diagnostic)."""
    from adler_born_two_channel import (killed_diffusion as kdf, model as mdl,
                                        moving_band_audit as mba)
    trials, steps, step = spec["trials"], spec["steps"], spec["fine_step"]
    strides, replicates = AUDIT["strides"], AUDIT["replicates"]
    train, criterion, mesh, stream, audit, paths = _audit_objects(step)
    clocks = len(AUDIT["clocks"])
    physical_per_trial, eligible_per_trial, per = count_replay_intervals(
        step, steps, strides)
    input_digest = hashlib.sha256(canonical_json({
        "kernel": "moving_band_audit.replay_pulse ladder",
        "train_digest": train.digest, "criterion": [AUDIT["tolerance"],
                                                    AUDIT["dwell"]],
        "physical_stream": stream.stream_prefix,
        "audit_stream": audit.stream_prefix, "mesh": mesh.identity,
        "steps": steps, "strides": strides, "trials": trials,
        "replicates": replicates,
        "clocks": [list(c) for c in AUDIT["clocks"]]}).encode()).hexdigest()
    timesteps = tuple(step * s for s in strides)
    post = {}

    def run():
        out = {}
        records = []
        subset = True
        counted_eligible = 0
        counted_bridged = 0
        for stride in strides:
            primary = np.full((trials, clocks), np.inf)
            audited = np.full((trials, clocks, replicates), np.inf)
            added = np.zeros((trials, clocks, replicates))
            for column, (clock, _, regime) in enumerate(AUDIT["clocks"]):
                path = paths[clock]
                for trial in range(trials):
                    phase = -math.pi + mdl.TWO_PI * (trial + 0.5) / trials
                    runs = mba.replay_pulse(path, criterion, stream, audit,
                                            trial, clock, phase, 0, steps,
                                            f"pricing/ladder/{regime}",
                                            replicates=replicates,
                                            stride=stride)
                    if runs[0].primary_committed_at is not None:
                        primary[trial, column] = runs[0].primary_committed_at
                    counted_eligible += (runs[0].rising_intervals
                                         + runs[0].falling_intervals)
                    counted_bridged += runs[0].evaluated_intervals
                    for rep, record in enumerate(runs):
                        subset &= record.subset_holds
                        added[trial, column, rep] = record.added_resets
                        if record.audited_committed_at is not None:
                            audited[trial, column, rep] = \
                                record.audited_committed_at
                        records.append(dataclasses.asdict(record))
            out[stride] = (primary, audited, added)
        return out, records, subset, counted_eligible, counted_bridged

    def digest(result):
        out, records, subset, counted_eligible, counted_bridged = result
        rec_digest = hashlib.sha256(canonical_json(records).encode()).hexdigest()
        arrays = []
        for stride in strides:
            arrays.extend(out[stride])
        raw = digest_arrays(*[np.where(np.isinf(a), 1e300, a) for a in arrays])
        # Untimed post-processing: the pooled dataset, as _audit_dataset does.
        t0 = time.perf_counter()
        primary = np.stack([out[s][0] for s in strides], axis=-1)
        audited = np.stack([out[s][1].reshape(trials, -1) for s in strides],
                           axis=-1)
        added = np.stack([out[s][2].reshape(trials, -1) for s in strides],
                         axis=-1)
        dataset, _ = build_audit_dataset(
            kdf, primary, audited, added, trials, timesteps,
            "pricing: moving-band pooled frozen sample")
        post["dataset_seconds"] = time.perf_counter() - t0
        post["dataset_digest"] = dataset.digest
        finite = all(np.all(np.isfinite(sm.values)) for sm in dataset.samples)
        assert counted_eligible == eligible_per_trial * trials, (
            counted_eligible, eligible_per_trial * trials)
        return (sha256_bytes(rec_digest.encode(), raw.encode()),
                finite and subset,
                {"records_digest": rec_digest, "dataset_digest": dataset.digest,
                 "subset_holds": bool(subset),
                 "eligible_intervals_from_records": counted_eligible,
                 "bridged_intervals_from_records": counted_bridged,
                 "uniform_draws": counted_bridged * replicates,
                 "dataset_seconds_untimed": post["dataset_seconds"]})

    meta = {"trials": trials, "steps": steps, "fine_step": step,
            "strides": strides, "replicates": replicates, "clocks": clocks,
            "physical_intervals": physical_per_trial * trials,
            "audited_evaluations": eligible_per_trial * trials * replicates,
            "per_trial": {"physical": physical_per_trial,
                          "eligible": eligible_per_trial, "by_cell": per}}
    return input_digest, run, digest, meta


def fixture_refinement_comparison(spec):
    from adler_born_two_channel import killed_diffusion as kdf
    clusters = spec["clusters"]
    rng = np.random.default_rng(spec["seed"])
    c, k, r = clusters, len(AUDIT["clocks"]), AUDIT["replicates"]
    horizon = AUDIT["origin"] + AUDIT["duration"]
    primary = np.where(rng.random((c, k, 3)) < 0.6,
                       rng.uniform(-1.0, horizon, (c, k, 3)), np.inf)
    audited = np.where(rng.random((c, k * r, 3)) < 0.6,
                       rng.uniform(-1.0, horizon, (c, k * r, 3)), np.inf)
    added = rng.integers(0, 3, (c, k * r, 3)).astype(float)
    timesteps = tuple(AUDIT["fine_step"] * s for s in AUDIT["strides"])
    t0 = time.perf_counter()
    dataset, contract = build_audit_dataset(
        kdf, primary, audited, added, c, timesteps,
        "pricing: synthetic moving-band layout")
    budgets = audit_budgets(kdf, contract, "pricing: reference caps",
                            max(timesteps))
    declared = budgets.digest
    build_seconds = time.perf_counter() - t0
    input_digest = hashlib.sha256(canonical_json({
        "kernel": "killed_diffusion.compare_refinement",
        "dataset_digest": dataset.digest, "budgets_digest": declared,
        "resamples": AUDIT["resamples"], "clusters": c,
        "samples": len(dataset.samples), "levels": 3,
        "seed": spec["seed"]}).encode()).hexdigest()

    def run():
        return kdf.compare_refinement(dataset, budgets, declared)

    def digest(verdict):
        payload = verdict.as_dict()
        text = canonical_json(payload)
        finite = all(math.isfinite(level.measured) and
                     math.isfinite(level.standard_error)
                     for level in verdict.levels)
        return (hashlib.sha256(text.encode()).hexdigest(), finite,
                {"verdict": verdict.verdict, "levels": len(verdict.levels)})

    work = AUDIT["resamples"] * c * len(dataset.samples) * 3
    return input_digest, run, digest, {
        "clusters": c, "samples": len(dataset.samples), "levels": 3,
        "resamples": AUDIT["resamples"], "members_audited": k * r,
        "members_primary": k, "resample_observations": work,
        "dataset_digest": dataset.digest, "budgets_digest": declared,
        "fixture_build_seconds_untimed": build_seconds}


FIXTURES = {
    "stationary_solve": fixture_stationary_solve,
    "stationary_construction": fixture_stationary_construction,
    "moving_replay": fixture_moving_replay,
    "refinement_comparison": fixture_refinement_comparison,
}


# ---------------------------------------------------------------------------
# The case series (three deterministic sizes per component)
# ---------------------------------------------------------------------------
def case_specs():
    return {
        "stationary_solve": [
            {"label": "M4800xN4800", "space_steps": 4800, "time_steps": 4800},
            {"label": "M4800xN19200", "space_steps": 4800, "time_steps": 19200},
            {"label": "M4800xN76800", "space_steps": 4800, "time_steps": 76800},
        ],
        "stationary_construction": [
            {"label": "W6000xF49152", "walkers": 6000, "fine_steps": 49152},
            {"label": "W6000xF98304", "walkers": 6000, "fine_steps": 98304},
            {"label": "W6000xF196608", "walkers": 6000, "fine_steps": 196608},
        ],
        "moving_replay": [
            {"label": "T20", "trials": 20, "steps": 500, "fine_step": 0.008},
            {"label": "T80", "trials": 80, "steps": 500, "fine_step": 0.008},
            {"label": "T320", "trials": 320, "steps": 500, "fine_step": 0.008},
        ],
        "refinement_comparison": [
            {"label": "C600", "clusters": 600, "seed": 20260902},
            {"label": "C1200", "clusters": 1200, "seed": 20260902},
            {"label": "C2400", "clusters": 2400, "seed": 20260902},
        ],
    }


# Work-unit names per component (and the two moving counters).
UNITS = {
    "stationary_solve": ("space_time_cells",),
    "stationary_construction": ("endpoint_observations",),
    "moving_replay": ("physical_intervals", "audited_evaluations"),
    "refinement_comparison": ("resample_observations",),
}
UNIT_TEXT = {
    "space_time_cells": "space-time cell",
    "endpoint_observations": "walker-position-level (endpoint) observation",
    "physical_intervals": "physical interval",
    "audited_evaluations": "audited interval evaluation",
    "resample_observations": "resample-cluster-sample-level observation",
}


def work_of(component, meta):
    if component == "stationary_solve":
        return {"space_time_cells": meta["space_steps"] * meta["time_steps"]}
    if component == "stationary_construction":
        return {"endpoint_observations": meta["endpoint_observations"]}
    if component == "moving_replay":
        return {"physical_intervals": meta["physical_intervals"],
                "audited_evaluations": meta["audited_evaluations"]}
    return {"resample_observations": meta["resample_observations"]}


# ---------------------------------------------------------------------------
# Stage work (declared), in every component's own unit
# ---------------------------------------------------------------------------
def stage_specs(replay_counts):
    """replay_counts: {'reference': (phys, elig), 'dt16': (phys, elig)} per
    trial."""
    strides = S3["strides"]
    positions = 3
    base_walkers = S3["walkers"]
    stat_cmp = S3["resamples"] * base_walkers * 12 * 3
    stages = []
    for short, (label, unit, attacks, kernel, tf, sf, spatial, dep) in zip(
            STAGE_SHORT, T07_STAGES):
        entry = {"short": short, "label": label, "unit": unit,
                 "attacks": attacks, "kernel": kernel,
                 "timestep_factor": tf, "sample_factor": sf,
                 "frozen_spatial_shape": spatial, "depends_on": dep,
                 "work": {}, "components": []}
        if short in SPACE_FACTOR:
            s = SPACE_FACTOR[short]
            f = int(round(1.0 / tf))
            M, N = S3["space"] * s, S3["time"] * f
            fine = S3["fine_steps"] * f
            entry["shape"] = {"oracle_grid": [M, N], "fine_steps": fine,
                              "walkers": base_walkers, "space_factor": s,
                              "time_factor": f}
            entry["components"] = ["stationary_solve",
                                   "stationary_construction",
                                   "refinement_comparison"]
            entry["work"] = {
                "stationary_solve": {"space_time_cells": M * N},
                "stationary_construction": {
                    "endpoint_observations":
                        base_walkers * positions * sum(fine // st
                                                       for st in strides)},
                "refinement_comparison": {"resample_observations": stat_cmp},
            }
        else:
            if short == "M6":
                trials = AUDIT["trials"]
                phys, elig = replay_counts["dt16"]
                mesh = {"fine_step": AUDIT["fine_step"] / 16,
                        "steps": AUDIT["steps"] * 16}
            else:
                trials = int(AUDIT["trials"] * sf)
                phys, elig = replay_counts["reference"]
                mesh = {"fine_step": AUDIT["fine_step"], "steps": AUDIT["steps"]}
            entry["shape"] = {"master_trials": trials, **mesh,
                              "replicates": AUDIT["replicates"],
                              "clocks": len(AUDIT["clocks"])}
            entry["components"] = ["moving_replay", "refinement_comparison"]
            entry["work"] = {
                "moving_replay": {
                    "physical_intervals": phys * trials,
                    "audited_evaluations": elig * trials * AUDIT["replicates"]},
                "refinement_comparison": {
                    "resample_observations": AUDIT["resamples"] * trials * 6 * 3},
            }
        stages.append(entry)
    return stages


# ---------------------------------------------------------------------------
# Measurement of one case (child process)
# ---------------------------------------------------------------------------
class RssSampler:
    def __init__(self, interval=0.01):
        import psutil                                        # noqa: PLC0415
        self.proc = psutil.Process()
        self.interval = interval
        self.peak = 0
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._loop, daemon=True)

    def _loop(self):
        while not self._stop.is_set():
            try:
                self.peak = max(self.peak, self.proc.memory_info().rss)
            except Exception:                                # noqa: BLE001
                pass
            self._stop.wait(self.interval)

    def __enter__(self):
        self._thread.start()
        return self

    def __exit__(self, *exc):
        self._stop.set()
        self._thread.join(timeout=1.0)
        try:
            self.peak = max(self.peak, self.proc.memory_info().rss)
        except Exception:                                    # noqa: BLE001
            pass


def measure_case(component, index, out_path, expected_source, expected_env):
    spec = case_specs()[component][index]
    record = {"component": component, "index": index, "label": spec["label"],
              "spec": spec, "exit_state": "started", "warnings": [],
              "repeats": [], "pid": os.getpid()}
    try:
        # 1. verify fingerprints (source, environment) before anything runs
        fp = source_fingerprint()
        env = environment_fingerprint(machine_identity())
        if expected_source and fp["digest"] != expected_source:
            raise RuntimeError(f"source fingerprint changed: {fp['digest']} "
                               f"vs {expected_source}")
        if expected_env and env != expected_env:
            raise RuntimeError("environment fingerprint changed")
        record["source_digest"] = fp["digest"]
        record["environment_digest"] = env
        rss_before_fixture = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        # 2. build the fixture (untimed) and its input digest
        t0 = time.perf_counter()
        input_digest, run, digest_fn, meta = FIXTURES[component](spec)
        record["fixture_seconds_untimed"] = time.perf_counter() - t0
        record["input_digest"] = input_digest
        record["meta"] = meta
        record["work"] = work_of(component, meta)
        rss_after_fixture = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        def one(traced):
            caught = []
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                if traced:
                    tracemalloc.start()
                t = time.perf_counter()
                out = run()
                wall = time.perf_counter() - t
                peak = None
                if traced:
                    peak = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()
                caught = [f"{x.category.__name__}: {x.message}" for x in w]
            d, finite, extra = digest_fn(out)
            del out
            return {"wall_seconds": wall, "tracemalloc_peak_bytes": peak,
                    "digest": d, "finite": bool(finite), "warnings": caught,
                    "extra": extra}

        # 3. one untimed warmup (traced), then three timed repeats (untraced)
        with RssSampler() as sampler:
            warm = one(traced=True)
            record["warmup"] = warm
            for _ in range(REPEATS):
                record["repeats"].append(one(traced=False))
        record["rss_sampled_peak_bytes"] = int(sampler.peak)
        record["ru_maxrss_bytes"] = int(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        record["ru_maxrss_before_fixture_bytes"] = int(rss_before_fixture)
        record["ru_maxrss_after_fixture_bytes"] = int(rss_after_fixture)
        record["tracemalloc_peak_bytes"] = warm["tracemalloc_peak_bytes"]
        walls = [r["wall_seconds"] for r in record["repeats"]]
        record["slowest_seconds"] = max(walls)
        record["fastest_seconds"] = min(walls)
        digests = {warm["digest"]} | {r["digest"] for r in record["repeats"]}
        record["digest"] = warm["digest"]
        record["digests_identical"] = len(digests) == 1
        record["finite"] = warm["finite"] and all(r["finite"]
                                                  for r in record["repeats"])
        record["warnings"] = warm["warnings"] + [w for r in record["repeats"]
                                                 for w in r["warnings"]]
        record["exit_state"] = "completed"
    except Exception as exc:                                  # noqa: BLE001
        import traceback
        record["exit_state"] = f"exception:{type(exc).__name__}"
        record["error"] = "".join(traceback.format_exception(exc))[-4000:]
    finally:
        if tracemalloc.is_tracing():
            tracemalloc.stop()
        record["ru_maxrss_bytes_final"] = int(
            resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        Path(out_path).write_text(canonical_json(record))


# ---------------------------------------------------------------------------
# Parent: the recorded session
# ---------------------------------------------------------------------------
def run_child(component, index, out_path, source_digest, env_digest,
              deadline, log):
    import psutil                                            # noqa: PLC0415
    cmd = [sys.executable, str(Path(__file__).resolve()), "--case", component,
           str(index), "--out", str(out_path), "--source", source_digest,
           "--env", env_digest]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    t0 = time.perf_counter()
    child = subprocess.Popen(cmd, cwd=str(REPO), env=env,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True)
    proc = psutil.Process(child.pid)
    rss_peak = 0
    ceiling = None
    while child.poll() is None:
        try:
            rss = proc.memory_info().rss
            rss_peak = max(rss_peak, rss)
            if rss > RSS_CEILING_BYTES:
                ceiling = "ceiling:rss"
                child.kill()
                break
        except psutil.Error:
            break
        if time.perf_counter() > deadline:
            ceiling = "ceiling:wall"
            child.kill()
            break
        time.sleep(0.02)
    stdout, stderr = child.communicate()
    wall = time.perf_counter() - t0
    record = None
    if Path(out_path).exists():
        record = json.loads(Path(out_path).read_text())
    if record is None:
        record = {"component": component, "index": index,
                  "label": case_specs()[component][index]["label"],
                  "spec": case_specs()[component][index],
                  "exit_state": ceiling or f"exception:child_rc_{child.returncode}",
                  "repeats": [], "warnings": [], "error": stderr[-4000:]}
    elif ceiling:
        record["exit_state"] = ceiling
    record["parent_observed_rss_peak_bytes"] = int(rss_peak)
    record["child_wall_seconds"] = wall
    record["child_returncode"] = child.returncode
    if stderr.strip():
        record["stderr_tail"] = stderr[-2000:]
    log(f"    child rc={child.returncode} wall={wall:.1f}s "
        f"rss_peak={rss_peak / 2**20:.0f}MiB state={record['exit_state']}")
    return record


def preflight_estimate(component, index, observed, spec_work):
    """Conservative predicted seconds for the whole case (warmup + repeats)."""
    prior_rate, prior_trace = PREFLIGHT_PRIORS[component]
    units = UNITS[component]
    rates = []
    traces = []
    for rec in observed.get(component, []):
        if rec.get("exit_state") != "completed":
            continue
        for unit in units:
            rates.append(rec["slowest_seconds"] / rec["work"][unit])
        if rec["warmup"]["wall_seconds"] > 0 and rec["fastest_seconds"] > 0:
            traces.append(rec["warmup"]["wall_seconds"] / rec["fastest_seconds"])
    rate = max(rates) if rates else prior_rate
    trace = max(traces) if traces else prior_trace
    trace = max(trace, 1.0)
    work = spec_work[units[0]]
    single = rate * work
    return single * (REPEATS + trace) * PREFLIGHT_SAFETY, single, trace


def predicted_work(component, spec):
    """Declared work of a case without building its fixture (for preflight)."""
    if component == "stationary_solve":
        return {"space_time_cells": spec["space_steps"] * spec["time_steps"]}
    if component == "stationary_construction":
        return {"endpoint_observations": spec["walkers"] * 3 * sum(
            spec["fine_steps"] // s for s in S3["strides"])}
    if component == "moving_replay":
        phys, elig, _ = count_replay_intervals(spec["fine_step"], spec["steps"],
                                               AUDIT["strides"])
        return {"physical_intervals": phys * spec["trials"],
                "audited_evaluations": elig * spec["trials"] * AUDIT["replicates"]}
    return {"resample_observations": AUDIT["resamples"] * spec["clusters"] * 6 * 3}


def session(args):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    t_session = time.perf_counter()
    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    log_lines = []

    def log(text):
        stamp = time.perf_counter() - t_session
        line = f"[{stamp:7.1f}s] {text}"
        log_lines.append(line)
        print(line, flush=True)

    log("pricing session start")
    identity = machine_identity()
    env_digest = environment_fingerprint(identity)
    fp = source_fingerprint()
    plan_digest = hashlib.sha256(PLAN.read_bytes()).hexdigest()
    git_head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(REPO),
                              capture_output=True, text=True).stdout.strip()
    log(f"source fingerprint {fp['digest'][:16]}  env {env_digest[:16]}")

    results_sha_start = results_sha_snapshot(RESULTS)
    results_stat_start = results_stat_snapshot(RESULTS)
    package_stat_start = package_stat_digest()
    log(f"results/ snapshot: {len(results_stat_start)} entries, "
        f"sha {results_sha_start[:16]}; package stat {package_stat_start[:16]}")

    # Exact per-trial replay counters on the reference and dt/16 meshes.
    ref_phys, ref_elig, ref_cells = count_replay_intervals(
        AUDIT["fine_step"], AUDIT["steps"], AUDIT["strides"])
    dt16_phys, dt16_elig, dt16_cells = count_replay_intervals(
        AUDIT["fine_step"] / 16, AUDIT["steps"] * 16, AUDIT["strides"])
    replay_counts = {"reference": (ref_phys, ref_elig),
                     "dt16": (dt16_phys, dt16_elig)}
    stages = stage_specs(replay_counts)
    log(f"replay counters per trial: reference phys={ref_phys} elig={ref_elig}; "
        f"dt/16 phys={dt16_phys} elig={dt16_elig}")

    observations = {
        "schema": "pricing-observations/v1",
        "started_at": started_at,
        "plan_path": str(PLAN.relative_to(REPO)), "plan_sha256": plan_digest,
        "repo_git_head": git_head,
        "machine": identity, "environment_digest": env_digest,
        "source_fingerprint": fp,
        "protocol": {"wall_ceiling_seconds": WALL_CEILING_S,
                     "rss_ceiling_bytes": RSS_CEILING_BYTES,
                     "contingency": CONTINGENCY, "rate_band": RATE_BAND,
                     "min_span": MIN_SPAN, "stage_span": STAGE_SPAN,
                     "memory_reversal": MEMORY_REVERSAL, "repeats": REPEATS,
                     "warmups": WARMUPS, "preflight_safety": PREFLIGHT_SAFETY,
                     "component_order": list(COMPONENTS)},
        "baseline": {"S3": S3, "AUDIT": AUDIT},
        "replay_counters_per_trial": {
            "reference": {"physical": ref_phys, "eligible": ref_elig,
                          "by_cell": ref_cells},
            "dt16": {"physical": dt16_phys, "eligible": dt16_elig,
                     "by_cell": dt16_cells}},
        "stages": stages,
        "case_specs": case_specs(),
        "interpretations": INTERPRETATIONS,
        "results_snapshot": {"entries": len(results_stat_start),
                             "sha_start": results_sha_start,
                             "package_stat_start": package_stat_start},
        "cases": {c: [] for c in COMPONENTS},
        "events": [],
    }

    def flush():
        observations["log"] = log_lines
        OBSERVATIONS.write_text(json.dumps(observations, indent=1,
                                           sort_keys=True, default=_json_default))

    flush()
    deadline = t_session + WALL_CEILING_S
    try:
        for component in COMPONENTS:
            stopped = False
            for index, spec in enumerate(case_specs()[component]):
                label = spec["label"]
                if stopped:
                    rec = {"component": component, "index": index,
                           "label": label, "spec": spec,
                           "exit_state": "skipped:component_stopped",
                           "repeats": [], "warnings": []}
                    observations["cases"][component].append(rec)
                    continue
                elapsed = time.perf_counter() - t_session
                work = predicted_work(component, spec)
                predicted, single, trace = preflight_estimate(
                    component, index, observations["cases"], work)
                log(f"{component}/{label}: preflight predicted {predicted:.0f}s "
                    f"(single {single:.1f}s, trace x{trace:.2f}); elapsed "
                    f"{elapsed:.0f}s; remaining {WALL_CEILING_S - elapsed:.0f}s")
                if elapsed + predicted > WALL_CEILING_S:
                    rec = {"component": component, "index": index,
                           "label": label, "spec": spec, "work": work,
                           "exit_state": "skipped:preflight",
                           "preflight_predicted_seconds": predicted,
                           "elapsed_at_preflight": elapsed,
                           "repeats": [], "warnings": []}
                    observations["cases"][component].append(rec)
                    observations["events"].append(
                        f"{component}/{label} not launched: preflight "
                        f"{predicted:.0f}s exceeds remaining "
                        f"{WALL_CEILING_S - elapsed:.0f}s")
                    stopped = True
                    flush()
                    continue
                before = results_stat_snapshot(RESULTS)
                out_path = SCRATCH / f"{component}-{index}.json"
                try:
                    rec = run_child(component, index, out_path, fp["digest"],
                                    env_digest, deadline, log)
                finally:
                    if out_path.exists():
                        out_path.unlink()
                after = results_stat_snapshot(RESULTS)
                rec["results_unchanged"] = (before == after
                                            and before == results_stat_start)
                rec["preflight_predicted_seconds"] = predicted
                rec["elapsed_at_launch"] = elapsed
                if not rec["results_unchanged"]:
                    rec["exit_state"] = "precondition:results_changed"
                observations["cases"][component].append(rec)
                if rec["exit_state"] != "completed":
                    observations["events"].append(
                        f"{component}/{label}: {rec['exit_state']}")
                    stopped = True
                else:
                    walls = [round(r["wall_seconds"], 3) for r in rec["repeats"]]
                    log(f"    repeats {walls} slowest {rec['slowest_seconds']:.3f}s "
                        f"warmup(traced) {rec['warmup']['wall_seconds']:.3f}s "
                        f"tm_peak {rec['tracemalloc_peak_bytes'] / 2**20:.1f}MiB "
                        f"ru_maxrss {rec['ru_maxrss_bytes'] / 2**20:.0f}MiB "
                        f"digest {rec['digest'][:12]} identical="
                        f"{rec['digests_identical']} warnings="
                        f"{len(rec['warnings'])}")
                flush()
    finally:
        results_sha_end = results_sha_snapshot(RESULTS)
        package_stat_end = package_stat_digest()
        observations["results_snapshot"]["sha_end"] = results_sha_end
        observations["results_snapshot"]["package_stat_end"] = package_stat_end
        observations["results_snapshot"]["results_unchanged"] = (
            results_sha_end == results_sha_start)
        observations["results_snapshot"]["package_unchanged"] = (
            package_stat_end == package_stat_start)
        observations["session_wall_seconds"] = time.perf_counter() - t_session
        observations["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        try:
            for leftover in SCRATCH.glob("*.json"):
                leftover.unlink()
            SCRATCH.rmdir()
        except OSError:
            pass
        log(f"session end: wall {observations['session_wall_seconds']:.1f}s; "
            f"results/ unchanged={observations['results_snapshot']['results_unchanged']} "
            f"package unchanged={observations['results_snapshot']['package_unchanged']}")
        flush()
    derived = derive(observations)
    write_report(observations, derived)
    print(f"wrote {OBSERVATIONS} and {REPORT}")
    return derived


# ---------------------------------------------------------------------------
# Derivation: observations -> component verdicts -> stage prices
# ---------------------------------------------------------------------------
def _within(x, bound):
    return x <= bound * (1.0 + 1e-9)


def component_verdict(component, cases):
    units = UNITS[component]
    reasons = []
    valid = []
    for rec in cases:
        state = rec.get("exit_state")
        if state != "completed":
            reasons.append(f"case {rec.get('label')}: exit state {state}")
            continue
        if rec.get("warnings"):
            reasons.append(f"case {rec['label']}: {len(rec['warnings'])} "
                           f"warning(s): {rec['warnings'][0][:120]}")
        if not rec.get("finite", False):
            reasons.append(f"case {rec['label']}: non-finite or invariant-"
                           f"failing output")
        if not rec.get("digests_identical", False):
            reasons.append(f"case {rec['label']}: output drift across repeats")
        if not rec.get("results_unchanged", True):
            reasons.append(f"case {rec['label']}: results/ changed")
        if rec.get("ru_maxrss_bytes", 0) > RSS_CEILING_BYTES or \
                rec.get("parent_observed_rss_peak_bytes", 0) > RSS_CEILING_BYTES:
            reasons.append(f"case {rec['label']}: RSS ceiling crossed")
        valid.append(rec)
    if len(valid) != 3:
        reasons.append(f"{len(valid)} valid case(s) of the required 3")
    out = {"component": component, "units": list(units), "cases": [],
           "rates": {}, "collapse": None, "memory_model": None}
    for rec in valid:
        out["cases"].append({
            "label": rec["label"], "work": rec["work"],
            "slowest_seconds": rec["slowest_seconds"],
            "repeats": [r["wall_seconds"] for r in rec["repeats"]],
            "ru_maxrss_bytes": rec["ru_maxrss_bytes"],
            "rss_sampled_peak_bytes": rec["rss_sampled_peak_bytes"],
            "tracemalloc_peak_bytes": rec["tracemalloc_peak_bytes"],
            "digest": rec["digest"]})
    if len(valid) == 3:
        works = [rec["work"][units[0]] for rec in valid]
        span = max(works) / min(works)
        if span < MIN_SPAN * (1 - 1e-9):
            reasons.append(f"declared-work span {span:.2f}x is below {MIN_SPAN}x")
        order = sorted(range(3), key=lambda i: works[i])
        walls = [valid[i]["slowest_seconds"] for i in order]
        if not (walls[0] < walls[1] < walls[2]):
            reasons.append(f"total time not monotone with work: {walls}")
        for unit in units:
            rates = [rec["slowest_seconds"] / rec["work"][unit] for rec in valid]
            ratio = max(rates) / min(rates)
            out["rates"][unit] = {"per_case": rates, "ratio": ratio,
                                  "slowest": max(rates),
                                  "flat": _within(ratio, RATE_BAND),
                                  "largest_work": max(rec["work"][unit]
                                                      for rec in valid)}
            if not _within(ratio, RATE_BAND):
                reasons.append(f"normalized rate per {UNIT_TEXT[unit]} varies "
                               f"{ratio:.2f}x across the three cases (band "
                               f"{RATE_BAND}x)")
        if len(units) == 2:
            a, b = units
            r = [rec["work"][b] / rec["work"][a] for rec in valid]
            same = _within(max(r) / min(r), RATE_BAND)
            out["collapse"] = {"counter_ratio_per_case": r,
                               "allowed": bool(same and all(
                                   out["rates"][u]["flat"] for u in units))}
        # memory model over ru_maxrss (process peak)
        mem = [valid[i]["ru_maxrss_bytes"] for i in order]
        w = [works[i] for i in order]
        ratio = max(mem) / min(mem)
        model = {"peaks_bytes": mem, "works": w, "max_bytes": max(mem)}
        if _within(ratio, 1.0 + MEMORY_REVERSAL):
            model["kind"] = "flat"
        else:
            reversal = any(mem[i + 1] < mem[i] * (1 - MEMORY_REVERSAL)
                           for i in range(2))
            slope, intercept = np.polyfit(w, mem, 1)
            fit = [intercept + slope * x for x in w]
            resid = max(abs(f - m) / m for f, m in zip(fit, mem))
            if not reversal and slope >= 0 and resid <= MEMORY_REVERSAL:
                model["kind"] = "linear"
                model["slope_bytes_per_unit"] = float(slope)
                model["intercept_bytes"] = float(intercept)
                model["max_relative_residual"] = float(resid)
            else:
                model["kind"] = "unresolved"
                reasons.append(f"memory neither flat nor linear (peaks {mem}, "
                               f"reversal={reversal}, residual={resid:.2f})")
        out["memory_model"] = model
    out["verdict"] = "priced" if not reasons else "pricing_unresolved"
    out["reasons"] = reasons
    return out


def price_stage(stage, verdicts):
    price = {"short": stage["short"], "label": stage["label"],
             "components": {}, "time_seconds": None, "memory_bytes": None,
             "verdict": "priced", "reasons": [], "notes": []}
    total = 0.0
    memory = 0
    for component in stage["components"]:
        v = verdicts[component]
        entry = {"verdict": v["verdict"], "work": stage["work"][component],
                 "seconds_before_contingency": None, "memory_bytes": None}
        if v["verdict"] != "priced":
            entry["reason"] = "component " + "; ".join(v["reasons"])
            price["reasons"].append(f"{component}: pricing_unresolved "
                                    f"({'; '.join(v['reasons'])})")
            price["components"][component] = entry
            continue
        units = UNITS[component]
        # 16x rule on every counter
        beyond = []
        for unit in units:
            largest = v["rates"][unit]["largest_work"]
            factor = stage["work"][component][unit] / largest
            entry[f"span_factor_{unit}"] = factor
            if not _within(factor, STAGE_SPAN):
                beyond.append(f"{UNIT_TEXT[unit]} work is {factor:.1f}x the "
                              f"largest measured point (limit {STAGE_SPAN}x)")
        if beyond:
            entry["reason"] = "; ".join(beyond)
            price["reasons"].append(f"{component}: {'; '.join(beyond)}")
            price["components"][component] = entry
            continue
        if len(units) == 1:
            unit = units[0]
            seconds = v["rates"][unit]["slowest"] * stage["work"][component][unit]
            entry["rule"] = f"slowest rate x work ({UNIT_TEXT[unit]})"
        else:
            terms = {u: v["rates"][u]["slowest"] * stage["work"][component][u]
                     for u in units}
            if v["collapse"] and v["collapse"]["allowed"]:
                seconds = max(terms.values())
                entry["rule"] = ("scalar collapse allowed (both counters flat "
                                 "and proportional): max of the two single-"
                                 "counter terms")
            else:
                seconds = sum(terms.values())
                entry["rule"] = ("sum of independently conservative terms "
                                 "(collapse not allowed)")
            entry["terms"] = terms
        entry["seconds_before_contingency"] = seconds
        entry["seconds_with_contingency"] = seconds * CONTINGENCY
        total += seconds
        # memory
        model = v["memory_model"]
        if model["kind"] == "flat":
            mem = model["max_bytes"]
        elif model["kind"] == "linear":
            unit = units[0]
            work = stage["work"][component][unit]
            mem = max(model["max_bytes"] if work <= max(model["works"]) else 0,
                      model["intercept_bytes"] + model["slope_bytes_per_unit"] * work)
        else:
            mem = None
        entry["memory_bytes"] = mem
        if mem is None:
            price["reasons"].append(f"{component}: memory unresolved")
        else:
            memory = max(memory, mem)
        price["components"][component] = entry
    if price["reasons"]:
        price["verdict"] = "pricing_unresolved"
    else:
        price["time_seconds"] = total * CONTINGENCY
        price["time_seconds_before_contingency"] = total
        price["memory_bytes"] = memory
    return price


def derive(observations):
    verdicts = {c: component_verdict(c, observations["cases"].get(c, []))
                for c in COMPONENTS}
    stages = observations["stages"]
    prices = {s["short"]: price_stage(s, verdicts) for s in stages}
    by_label = {s["label"]: s["short"] for s in stages}
    # dependency paths (every root-to-node chain)
    def chain(short):
        st = next(s for s in stages if s["short"] == short)
        return (chain(by_label[st["depends_on"]]) if st["depends_on"] else []) + [short]
    paths = []
    for s in stages:
        members = chain(s["short"])
        unresolved = [m for m in members if prices[m]["verdict"] != "priced"]
        paths.append({"path": members,
                      "verdict": "priced" if not unresolved else "pricing_unresolved",
                      "time_seconds": (sum(prices[m]["time_seconds"] for m in members)
                                       if not unresolved else None),
                      "memory_bytes": (max(prices[m]["memory_bytes"] for m in members)
                                       if not unresolved else None),
                      "unresolved_members": unresolved})
    resolved = [p for p in prices.values() if p["verdict"] == "priced"]
    worst = {"verdict": "priced" if len(resolved) == 7 else "pricing_unresolved",
             "time_seconds_resolved_stages_only": sum(p["time_seconds"]
                                                       for p in resolved),
             "resolved_stages": [p["short"] for p in resolved],
             "unresolved_stages": [p["short"] for p in prices.values()
                                   if p["verdict"] != "priced"],
             "memory_bytes_resolved_stages_only": max(
                 [p["memory_bytes"] for p in resolved] or [0])}
    bench_cases = sum(rec.get("child_wall_seconds", 0.0)
                      for c in COMPONENTS for rec in observations["cases"].get(c, []))
    benchmark = {"session_wall_seconds": observations.get("session_wall_seconds"),
                 "child_processes_wall_seconds": bench_cases}
    derived = {"components": verdicts, "stages": prices, "paths": paths,
               "worst_case": worst, "benchmark_only": benchmark}
    derived["derivation_digest"] = hashlib.sha256(
        canonical_json(derived).encode()).hexdigest()
    return derived


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def _hms(seconds):
    if seconds is None:
        return "—"
    if seconds < 120:
        return f"{seconds:.1f} s"
    if seconds < 7200:
        return f"{seconds:.0f} s ({seconds / 60:.1f} min)"
    return f"{seconds:.0f} s ({seconds / 3600:.2f} h)"


def _mib(b):
    return "—" if b is None else f"{b / 2**20:.0f} MiB"


def write_report(observations, derived):
    m = observations["machine"]
    fp = observations["source_fingerprint"]
    L = []
    L.append("# Validation-campaign pricing report (Ticket 07 pricing plan)\n")
    L.append("**A price is not an approval and not a sufficiency promise.**  "
             "Nothing here authorizes a validation stage, pilot, production "
             "run, sensitivity, fit or Ticket 08; every stage keeps its "
             "predeclared success, `numerical_no_result`, dependency and stop "
             "rules, and no stage is promised to resolve the numerical block.  "
             "The scientific disposition is unchanged: the moving-band result "
             "is `numerical_no_result`.\n")
    L.append(f"Plan: `{observations['plan_path']}` (sha256 "
             f"`{observations['plan_sha256']}`).  Session started "
             f"{observations['started_at']}, finished "
             f"{observations.get('finished_at')}, wall "
             f"{_hms(observations.get('session_wall_seconds'))} of the "
             f"{WALL_CEILING_S:.0f} s ceiling.\n")
    L.append("## Machine and environment identity\n")
    L.append("| Field | Value |\n| --- | --- |")
    for key in ("platform", "cpu_brand", "physical_cpus", "performance_cores",
                "efficiency_cores", "logical_cpus", "memory_bytes", "os_version",
                "python_version", "python_executable", "numpy_version",
                "numpy_blas", "psutil_version"):
        L.append(f"| {key} | `{m.get(key, '')}` |")
    L.append(f"| environment digest | `{observations['environment_digest']}` |")
    L.append(f"| repo git HEAD | `{observations['repo_git_head']}` (the package "
             f"itself is untracked) |")
    L.append(f"| package source fingerprint (`experiments.source_fingerprint`) "
             f"| `{fp['digest']}` |")
    L.append("")
    L.append("<details><summary>Per-file SHA-256 of the package sources "
             "fingerprinted</summary>\n")
    L.append("| File | SHA-256 |\n| --- | --- |")
    for name, digest in fp["files"]:
        L.append(f"| {name} | `{digest}` |")
    L.append("\n</details>\n")
    snap = observations["results_snapshot"]
    L.append("## Preconditions and tree integrity\n")
    L.append(f"- `results/` entries at start: {snap['entries']}; SHA snapshot "
             f"start `{snap['sha_start'][:16]}…`, end "
             f"`{str(snap.get('sha_end', ''))[:16]}…`; unchanged = "
             f"**{snap.get('results_unchanged')}**.  (The plan's literal "
             f"'empty results/' precondition is NOT met by this tree — see "
             f"interpretation 1 — so 'unchanged' is the condition verified "
             f"before and after every case.)")
    L.append(f"- Package tree (every entry except `results/`, including "
             f"`__pycache__`) unchanged = **{snap.get('package_unchanged')}**.")
    L.append("- No fixture touched disk: every fixture is in memory in a child "
             "process that exits with its case; the per-case JSON handoff in "
             "the scratchpad is removed in `finally`.")
    L.append("- The package verifier was not run; no validation stage, pilot, "
             "production, sensitivity or exponent fit was entered; no "
             "pilot/exponent output was opened.\n")
    if observations.get("events"):
        L.append("### Stop / skip events\n")
        for e in observations["events"]:
            L.append(f"- {e}")
        L.append("")

    L.append("## Components\n")
    for component in COMPONENTS:
        v = derived["components"][component]
        L.append(f"### `{component}` — **{v['verdict']}**\n")
        units = UNITS[component]
        head = "| Case | " + " | ".join(f"work ({UNIT_TEXT[u]})" for u in units) + \
               " | repeats (s) | slowest (s) | traced warmup (s) | " + \
               " | ".join(f"ns per {u}" for u in units) + \
               " | tracemalloc peak | ru_maxrss | sampled RSS | digest | warnings | exit |"
        L.append(head)
        L.append("| --- |" + " --- |" * (len(units) * 2 + 9))
        for rec in observations["cases"].get(component, []):
            if rec.get("exit_state") == "completed":
                rates = " | ".join(f"{rec['slowest_seconds'] / rec['work'][u] * 1e9:.2f}"
                                   for u in units)
                works = " | ".join(f"{rec['work'][u]:,}" for u in units)
                L.append(
                    f"| {rec['label']} | {works} | "
                    f"{', '.join(f'{r['wall_seconds']:.3f}' for r in rec['repeats'])} | "
                    f"{rec['slowest_seconds']:.3f} | {rec['warmup']['wall_seconds']:.3f} | "
                    f"{rates} | {_mib(rec['tracemalloc_peak_bytes'])} | "
                    f"{_mib(rec['ru_maxrss_bytes'])} | {_mib(rec['rss_sampled_peak_bytes'])} | "
                    f"`{rec['digest'][:12]}`{'' if rec['digests_identical'] else ' DRIFT'} | "
                    f"{len(rec['warnings'])} | {rec['exit_state']} |")
            else:
                works = " | ".join(f"{rec.get('work', {}).get(u, '—')}" for u in units)
                L.append(f"| {rec.get('label')} | {works} |" + " — |" * (len(units) + 7)
                         + f" {rec.get('exit_state')} |")
        L.append("")
        for unit, r in v.get("rates", {}).items():
            L.append(f"- Normalized rate per {UNIT_TEXT[unit]}: "
                     f"{', '.join(f'{x * 1e9:.2f} ns' for x in r['per_case'])}; "
                     f"ratio {r['ratio']:.3f}x (band {RATE_BAND}x) → "
                     f"{'flat' if r['flat'] else 'NOT flat'}; slowest "
                     f"{r['slowest'] * 1e9:.2f} ns; largest measured work "
                     f"{r['largest_work']:,}.")
        if v.get("collapse") is not None:
            L.append(f"- Two-counter scalar collapse: counter ratio per case "
                     f"{[round(x, 4) for x in v['collapse']['counter_ratio_per_case']]}; "
                     f"allowed = {v['collapse']['allowed']}.")
        if v.get("memory_model"):
            mm = v["memory_model"]
            L.append(f"- Memory (ru_maxrss over the three cases, ascending "
                     f"work): {[round(x / 2**20) for x in mm['peaks_bytes']]} MiB "
                     f"→ model **{mm['kind']}**"
                     + (f" (slope {mm['slope_bytes_per_unit']:.3g} B/unit)"
                        if mm["kind"] == "linear" else "") + ".")
        for reason in v["reasons"]:
            L.append(f"- **Unresolved:** {reason}")
        # extra diagnostics
        for rec in observations["cases"].get(component, []):
            if rec.get("exit_state") == "completed":
                extra = rec["warmup"].get("extra", {})
                bits = []
                for key in ("closure_residual", "paired_bitwise", "subset_holds",
                            "verdict", "dataset_seconds_untimed",
                            "eligible_intervals_from_records",
                            "bridged_intervals_from_records", "uniform_draws"):
                    if key in extra:
                        val = extra[key]
                        bits.append(f"{key}={val:.3g}" if isinstance(val, float)
                                    else f"{key}={val}")
                if bits:
                    L.append(f"  - {rec['label']}: " + ", ".join(bits))
        L.append("")

    L.append("## Stage work (declared) and per-stage prices\n")
    L.append("Baseline shapes (ticket-04 reference, verify.py constants): "
             f"oracle grid {S3['space']}x{S3['time']}; endpoint ladder "
             f"{S3['walkers']} walkers x 3 starts x {S3['fine_steps']} fine "
             f"steps at strides {S3['strides']}; stationary comparison "
             f"{S3['resamples']} resamples x {S3['walkers']} clusters x 12 "
             f"samples x 3 levels; audit ladder {AUDIT['trials']} master trials "
             f"x 3 clocks x strides {AUDIT['strides']} x {AUDIT['replicates']} "
             f"replicates on mesh (origin {AUDIT['origin']}, step "
             f"{AUDIT['fine_step']}, {AUDIT['steps']} steps); moving comparison "
             f"{AUDIT['resamples']} resamples x clusters x 6 samples x 3 levels.\n")
    rc = observations["replay_counters_per_trial"]
    L.append(f"Exact replay counters per master trial: reference mesh "
             f"physical={rc['reference']['physical']}, eligible="
             f"{rc['reference']['eligible']} (x{AUDIT['replicates']} replicates "
             f"= {rc['reference']['eligible'] * AUDIT['replicates']} audited "
             f"evaluations); dt/16 mesh physical={rc['dt16']['physical']}, "
             f"eligible={rc['dt16']['eligible']}.\n")
    L.append("| Stage | Shape | Component work | Price (time, x1.5 contingency) | "
             "Memory | Verdict |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for st in observations["stages"]:
        p = derived["stages"][st["short"]]
        works = "<br>".join(
            f"{c}: " + ", ".join(f"{u}={w:,}" for u, w in sorted(st["work"][c].items()))
            for c in st["components"])
        shape = ", ".join(f"{k}={v}" for k, v in sorted(st["shape"].items()))
        L.append(f"| **{st['short']}** {st['label']} | {shape} | {works} | "
                 f"{_hms(p['time_seconds'])} | {_mib(p['memory_bytes'])} | "
                 f"**{p['verdict']}** |")
    L.append("")
    L.append("### Per-stage detail\n")
    for st in observations["stages"]:
        p = derived["stages"][st["short"]]
        L.append(f"- **{st['short']}** — {p['verdict']}"
                 + (f"; time {_hms(p['time_seconds'])} (before contingency "
                    f"{_hms(p.get('time_seconds_before_contingency'))}); memory "
                    f"{_mib(p['memory_bytes'])}" if p["verdict"] == "priced" else ""))
        for c, e in p["components"].items():
            if e.get("seconds_before_contingency") is not None:
                L.append(f"  - {c}: {_hms(e['seconds_before_contingency'])} before "
                         f"contingency ({e.get('rule')}); memory {_mib(e['memory_bytes'])}"
                         + (f"; span factor(s) " + ", ".join(
                             f"{k.split('span_factor_')[1]}={v:.2f}x"
                             for k, v in sorted(e.items()) if k.startswith("span_factor_"))))
            else:
                L.append(f"  - {c}: unresolved — {e.get('reason')}")
        if st["short"] == "S4":
            L.append("  - S4 is priced as a full independent stage; if S3's "
                     "solve and walk are reused, its marginal cost is its "
                     "comparison term alone.")
        if st["short"] == "M7":
            L.append("  - M7's comparison runs at 40960 clusters, in the "
                     "quadratic regime of `compare_refinement` (see "
                     "interpretation 'refinement comparison — quadratic term'); "
                     "even where the 16x rule is formally met its comparison "
                     "term would understate the cost.")
    L.append("")
    L.append("## Dependency-path totals\n")
    L.append("| Path | Time (with contingency) | Memory | Verdict |\n| --- | --- | --- | --- |")
    for p in derived["paths"]:
        L.append(f"| {' → '.join(p['path'])} | {_hms(p['time_seconds'])} | "
                 f"{_mib(p['memory_bytes'])} | {p['verdict']}"
                 + (f" (unresolved: {', '.join(p['unresolved_members'])})"
                    if p["unresolved_members"] else "") + " |")
    w = derived["worst_case"]
    L.append("")
    L.append(f"**Worst-case sum (every declared stage runs):** {w['verdict']}.  "
             f"Sum over the resolved stages only "
             f"({', '.join(w['resolved_stages']) or 'none'}): "
             f"{_hms(w['time_seconds_resolved_stages_only'])}; unresolved stages: "
             f"{', '.join(w['unresolved_stages']) or 'none'}.  This sum is not "
             f"an approval estimate and not a sufficiency promise.\n")
    b = derived["benchmark_only"]
    L.append(f"**Benchmark-only cost:** session wall {_hms(b['session_wall_seconds'])} "
             f"(child processes {_hms(b['child_processes_wall_seconds'])}); design "
             f"probes before the session, not recorded here, took about two "
             f"minutes.\n")
    L.append(f"Derivation digest (SHA-256 of the derived prices; `--derive-only` "
             f"must reproduce it): `{derived['derivation_digest']}`\n")
    L.append("## Interpretations of ambiguous plan definitions\n")
    for i, (title, text) in enumerate(observations["interpretations"], 1):
        L.append(f"{i}. **{title}.** {text}")
    L.append("")
    L.append("## Reproduce\n")
    L.append("```\ncd " + str(REPO) + "\n"
             "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/pricing/"
             "price_validation_campaign.py --run\n"
             "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/pricing/"
             "price_validation_campaign.py --derive-only   # prices from observations.json\n```\n")
    L.append("## Session log\n")
    L.append("```")
    L.extend(observations.get("log", []))
    L.append("```")
    REPORT.write_text("\n".join(L) + "\n")


# ---------------------------------------------------------------------------
# Self-test (tiny sizes, not recorded)
# ---------------------------------------------------------------------------
def selftest():
    print("selftest: tiny fixtures, one run each")
    tiny = {
        "stationary_solve": {"label": "t", "space_steps": 600, "time_steps": 600},
        "stationary_construction": {"label": "t", "walkers": 1500,
                                    "fine_steps": 2048},
        "moving_replay": {"label": "t", "trials": 2, "steps": 500,
                          "fine_step": 0.008},
        "refinement_comparison": {"label": "t", "clusters": 50, "seed": 1},
    }
    for component, spec in tiny.items():
        t0 = time.perf_counter()
        input_digest, run, digest_fn, meta = FIXTURES[component](spec)
        t1 = time.perf_counter()
        out = run()
        t2 = time.perf_counter()
        d, finite, extra = digest_fn(out)
        d2, _, _ = digest_fn(run())
        print(f"  {component}: fixture {t1 - t0:.2f}s run {t2 - t1:.2f}s "
              f"work={work_of(component, meta)} finite={finite} "
              f"repeat-identical={d == d2} extra={extra}")
    counts = count_replay_intervals(AUDIT["fine_step"], AUDIT["steps"],
                                    AUDIT["strides"])
    print(f"  replay counters (reference mesh) per trial: {counts[:2]}")
    stages = stage_specs({"reference": counts[:2], "dt16": counts[:2]})
    for s in stages:
        print(f"  {s['short']}: {s['work']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--derive-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--case", nargs=2, metavar=("COMPONENT", "INDEX"))
    ap.add_argument("--out")
    ap.add_argument("--source", default="")
    ap.add_argument("--env", default="")
    args = ap.parse_args()
    if args.case:
        measure_case(args.case[0], int(args.case[1]), args.out, args.source,
                     args.env)
        return
    if args.selftest:
        selftest()
        return
    if args.derive_only:
        observations = json.loads(OBSERVATIONS.read_text())
        derived = derive(observations)
        write_report(observations, derived)
        print(json.dumps({"derivation_digest": derived["derivation_digest"],
                          "stages": {k: (v["verdict"], v["time_seconds"],
                                         v["memory_bytes"])
                                     for k, v in derived["stages"].items()}},
                         indent=1))
        return
    if args.run:
        session(args)
        return
    ap.print_help()


if __name__ == "__main__":
    main()
