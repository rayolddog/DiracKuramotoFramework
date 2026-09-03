#!/usr/bin/env python3
"""
run_redesign_campaign.py — the REDESIGNED intended-configuration validation
campaign (sponsor's plan change): (a) the stationary path at 16x walkers,
(b) the dt/16 moving-band replay M6 as its own stage, overriding the stop rule
that halted it after M5.  Everything else stays as frozen; the frozen
added-resets cap is reported separately and is NOT re-frozen.

Reuses, read-only, the two verified runners beside it:
  ../pricing/price_validation_campaign.py  (tree snapshots, fingerprints, RSS
                                            sampling, priced rates)
  ./run_validation_campaign.py             (cells, frozen caps, moving ladder,
                                            stage rules, frozen budget)

Each stationary stage runs as TWO serial child processes so that the
walker-dependent construction never shares a process with a 1.5 GiB oracle
solve:  phase A (oracle on the stage grid + the oracle-margin grid -> reference
values and gap), then phase B (paired endpoint walk -> censoring -> frozen
dataset -> compare_refinement -> S3 procedure checks).  The parent kills any
child above 2 GiB, applies a 4-hour wall budget with preflight from the prices,
and writes observations_redesign.json after every step.

Walker count: S1 phase B is first run at 24,000 walkers as a memory-scaling
measurement; the walker count is then chosen as the largest of
(96000, 72000, 48000, 24000) whose linearly extrapolated phase-B peak RSS stays
under 2 GiB and whose preflight (including the O(walkers^2) identity check in
killed_diffusion._require_names, measured at 24,000 and extrapolated) fits the
remaining budget.

Modes:  --run | --phase KIND --out PATH [internal] | --derive-only | --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import resource
import subprocess
import sys
import time
import warnings
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

import numpy as np                                                    # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PKG = REPO / "adler_born_two_channel"
RESULTS = PKG / "results"
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "adler_two_channel_exploratory" / "pricing"))
sys.path.insert(0, str(HERE))
import price_validation_campaign as P                                  # noqa: E402
import run_validation_campaign as V                                    # noqa: E402

OBSERVATIONS = HERE / "observations_redesign.json"
PREVIOUS = HERE / "observations.json"          # last night's record, read-only
REPORT = HERE / "REDESIGN_REPORT.md"
SCRATCH = Path(os.environ.get(
    "REDESIGN_SCRATCH",
    "/private/tmp/claude-501/-Users-john-bramble-Projects-Physics-DiracKuramotoFramework/"
    "63b0fc51-d326-44ba-9e7c-eccecb8f1e8f/scratchpad")) / "redesign_stages"

WALL_BUDGET_S = 4 * 3600.0
RSS_CEILING_BYTES = 2 * 1024 ** 3
PRICE_CONTINGENCY = 1.5
WALKER_CANDIDATES = (96000, 72000, 48000, 24000)   # multiples of the 1500 chunk
PROBE_WALKERS = 24000
BASE_WALKERS = 6000

STAGES = {
    "S1": dict(kind="stationary", label="stationary probability, dt/16 at doubled space (16x walkers)", unit="probability", time_factor=16, space_factor=2, depends_on=None),
    "S2": dict(kind="stationary", label="stationary probability, dt/64 at quadrupled space (16x walkers)", unit="probability", time_factor=64, space_factor=4, depends_on="S1"),
    "S3": dict(kind="stationary", label="stationary probability, dt/256 at eightfold space (16x walkers)", unit="probability", time_factor=256, space_factor=8, depends_on="S2"),
    "S4": dict(kind="stationary_time", label="stationary time quantile, dt/256 at eightfold space (16x walkers)", unit="time", time_factor=256, space_factor=8, depends_on="S3"),
    "M6": dict(kind="moving", label="moving-band probability, dt/16 replay (stop rule after M5 overridden by the sponsor)", unit="probability", time_factor=16, trials_factor=1, depends_on=None),
}
ORDER = ["M6", "S1", "S2", "S3", "S4"]   # M6 first so the requested override stage cannot be starved by the stationary path

INTERPRETATIONS = V.INTERPRETATIONS + [
    ("16x walkers and the frozen contract", "The sampling design's cluster count is part of the hashed contract and is set from the data (96,000 walkers -> 96,000 clusters), exactly as verify.py sets it from _S3_WALKERS; the frozen S3 caps and their resolution floors (0.012 probability, 0.030 time) are applied unchanged although they were derived for 6,000 walkers' granularity (a floor can only excuse a reversal, so at 96,000 walkers it is looser, never stricter).  Seeds, resamples (200), coverage (2), estimators and observables are unchanged."),
    ("memory-scaling measurement", "The walker-dependent memory is the construction phase's process peak (walk + censoring + frozen dataset + compare_refinement), measured in its own child at 24,000 walkers and combined with the pricing session's 6,000-walker construction children (ru_maxrss 220-228 MiB, same code path without the comparison) for a two-point linear extrapolation; the oracle phase runs in a separate child whose peak is the solve's own (up to 1,589 MiB at eightfold space, measured in the pricing session) and never overlaps the construction."),
    ("O(walkers^2) identity check", "killed_diffusion._require_names runs `listed.count(e)` for every label (about 4.4 ns x n^2) and is executed 36 times per stationary stage (12 samples x construction, ValidationDataset rebuild, compare_refinement rebuild).  Its time is measured in the 24,000-walker probe as the dataset-construction and comparison seconds and extrapolated quadratically to the chosen walker count for the preflight; nothing inside the package is changed or bypassed."),
    ("M6 override", "M6 runs although its predecessor M5 returned numerical_no_result, by the sponsor's plan change; the frozen rule text is quoted and the override is stated.  M6 keeps its frozen design (40 master trials, 3 regime clocks, 4 replicates, strides (4,2,1) on the 2^-13 mesh over the 2048/2^-9 = 32768-step window).  The gate's added_resets_mean cap (3.0, frozen for the S3b cell) is reported as its own line beside the probability and time rows; it is not re-frozen."),
    ("execution order", "M6 (priced 23 min) runs before the stationary path so that the sponsor's explicitly requested override stage cannot be skipped by the 4-hour preflight in the branch where S1 and S2 both succeed (S3 alone is priced at about two hours at 96,000 walkers); the stationary path keeps its own dependency order S1 -> S2 -> S3 -> S4."),
    ("disposition sets", "Rows from this session replace last night's S1 rows (superseded by the 16x-walker S1) and add M6's rows; last night's M5 rows are kept (M6 does not supersede M5).  Three sets are run: redesign-only intended rows, all intended rows (S1-new [+S2,S3 if run] + M5-old + M6), and the 17 reference rows plus all intended rows."),
]


# ---------------------------------------------------------------------------
# Phase A: the oracle (its own child)
# ---------------------------------------------------------------------------
def oracle_phase(cell, time_factor, space_factor, log):
    from adler_born_two_channel import killed_diffusion as kdf
    lower, upper, starts, geometry = V.stationary_geometry(cell)
    M, N = cell["base_space"] * space_factor, cell["base_time"] * time_factor
    out = {"band": [lower, upper], "starts": starts.tolist(), "oracle_grid": [M, N], "timing": {}}
    t0 = time.perf_counter()
    with P.RssSampler() as s:
        oracle = kdf.solve_survival(geometry, starts, cell["horizon"], M, N)
    out["timing"]["oracle_seconds"] = time.perf_counter() - t0
    out["rss_oracle_phase_bytes"] = int(s.peak)
    out["oracle_closure_residual"] = oracle.closure_residual
    mode = "refined" if 2 * M <= 4800 else "coarsened"
    t0 = time.perf_counter()
    with P.RssSampler() as s:
        if mode == "refined":
            other = kdf.solve_survival(geometry, starts, cell["horizon"], 2 * M, 2 * N)
            gap = float(np.max(np.abs(oracle.survival - other.survival[:, ::2])))
            grid = [2 * M, 2 * N]
        else:
            other = kdf.solve_survival(geometry, starts, cell["horizon"], M // 2, N // 2)
            gap = float(np.max(np.abs(oracle.survival[:, ::2] - other.survival)))
            grid = [M // 2, N // 2]
        del other
    out["timing"]["oracle_margin_seconds"] = time.perf_counter() - t0
    out["rss_margin_phase_bytes"] = int(s.peak)
    out.update(oracle_margin_mode=mode, oracle_margin_grid=grid, oracle_gap=gap)
    out["reference"] = {
        "survival": oracle.survival[:, -1].tolist(),
        "exit_quantile_p35": oracle.quantiles([cell["quantile"]])[:, 0].tolist(),
        "exit_count_upper": oracle.upper_exit[:, -1].tolist(),
        "exit_count_lower": oracle.lower_exit[:, -1].tolist(),
    }
    if not all(np.all(np.isfinite(v)) for v in out["reference"].values()):
        raise RuntimeError("non-finite oracle reference")
    log(f"    oracle {M}x{N} in {out['timing']['oracle_seconds']:.1f}s; margin {mode} {grid} gap {gap:.3e}")
    return out


# ---------------------------------------------------------------------------
# Phase B: the paired endpoint walk, frozen dataset and gate (its own child)
# ---------------------------------------------------------------------------
def construction_phase(cell, time_factor, walkers, oracle_out, dataset_label, budgets_label, log):
    from adler_born_two_channel import killed_diffusion as kdf, stochastic as stoch
    lower, upper = oracle_out["band"]
    starts = np.array(oracle_out["starts"])
    reference = {k: np.array(v) for k, v in oracle_out["reference"].items()}
    fine_steps = cell["base_fine_steps"] * time_factor
    strides, chunk, window = cell["strides"], cell["chunk"], cell["window"]
    positions = starts.size
    step = cell["horizon"] / fine_steps
    labels = tuple(f"x={value:.6f}" for value in starts)
    out = {"walkers": walkers, "fine_steps": fine_steps, "timesteps": [step * s for s in strides],
           "oracle_grid": oracle_out["oracle_grid"], "oracle_gap": oracle_out["oracle_gap"],
           "oracle_margin_mode": oracle_out["oracle_margin_mode"],
           "oracle_margin_grid": oracle_out["oracle_margin_grid"],
           "cell": {k: (list(v) if isinstance(v, tuple) else v) for k, v in cell.items()},
           "timing": {}, "rss_phase_bytes": {}, "checks": {}}
    out["cell"]["walkers"] = walkers
    mesh = stoch.FinestMesh(0.0, step)
    stream = stoch.PhaseNoiseStream(cell["namespace"], mesh, cell["diffusion"])
    # ---- walk (verify.py _s3_measured) -------------------------------------
    t0 = time.perf_counter()
    paired = True
    exits = {s: np.full((walkers, positions), np.inf) for s in strides}
    uppers = {s: np.zeros((walkers, positions), dtype=bool) for s in strides}
    with P.RssSampler() as sampler:
        for base in range(0, walkers, chunk):
            clocks = np.arange(base, min(base + chunk, walkers))
            rows = clocks.size
            state = {s: {"phase": np.repeat(starts[None, :], rows, axis=0),
                         "alive": np.ones((rows, positions), dtype=bool)} for s in strides}
            for offset, block in stream.stream_leaf_blocks(0, clocks, 0, fine_steps, window):
                for s in strides:
                    groups = block.shape[1] // s
                    coarse = stoch._sum_left_to_right(block.reshape(rows, groups, s))
                    if base == 0 and offset == 0:
                        control = stream._coarse_kicks_uniform(0, clocks[:32], 0, window, s)
                        paired &= bool(np.array_equal(coarse[:32], control))
                    span = step * s
                    live = state[s]
                    for group in range(groups):
                        moment = (offset + (group + 1) * s) * step
                        live["phase"] = np.where(
                            live["alive"],
                            live["phase"] + (cell["detuning"] - cell["coupling"] * np.sin(live["phase"])) * span
                            + coarse[:, group:group + 1],
                            live["phase"])
                        left = live["alive"] & ((live["phase"] <= lower) | (live["phase"] >= upper))
                        if left.any():
                            rowsel = slice(base, base + rows)
                            block_exit = exits[s][rowsel]
                            block_exit[left] = moment
                            exits[s][rowsel] = block_exit
                            block_upper = uppers[s][rowsel]
                            block_upper |= left & (live["phase"] >= upper)
                            uppers[s][rowsel] = block_upper
                            live["alive"] &= ~left
    out["timing"]["walk_seconds"] = time.perf_counter() - t0
    out["rss_phase_bytes"]["walk"] = int(sampler.peak)
    log(f"    walk {walkers}x{fine_steps} in {out['timing']['walk_seconds']:.1f}s paired={paired} "
        f"rss {sampler.peak / 2**20:.0f}MiB")
    # ---- censoring + PairedSamples (12 x _require_names) --------------------
    t0 = time.perf_counter()
    with P.RssSampler() as sampler:
        stack = {name: [] for name in reference}
        for s in strides:
            times = exits[s]
            alive = np.isinf(times)
            stack["survival"].append(alive.astype(float))
            stack["exit_quantile_p35"].append(np.minimum(times, cell["horizon"]))
            stack["exit_count_upper"].append((uppers[s] & ~alive).astype(float))
            stack["exit_count_lower"].append((~uppers[s] & ~alive).astype(float))
        names = tuple(f"walker-{index}" for index in range(walkers))
        samples = []
        for name, pages in stack.items():
            block = np.stack(pages, axis=-1)
            for index, label in enumerate(labels):
                samples.append(kdf.PairedSample(name, label, block[:, index, :][:, None, :], None,
                                                float(reference[name][index]), names, ("outcome",)))
        del stack, exits, uppers
    out["timing"]["samples_seconds"] = time.perf_counter() - t0
    out["rss_phase_bytes"]["samples"] = int(sampler.peak)
    # ---- frozen contract, dataset (12 more rebuilds), budgets ---------------
    t0 = time.perf_counter()
    with P.RssSampler() as sampler:
        sampling = kdf.SamplingDesign(
            unit="endpoint walker: one independent keyed Brownian stream",
            clusters=walkers, replications=1,
            method="cluster bootstrap over walkers, one resample of clusters evaluated at every "
                   "refinement level so that level contrasts are paired",
            resamples=cell["resamples"], coverage=2.0, seed=cell["seed"])
        contract = kdf.RefinementContract(tuple(step * s for s in strides), 2.0, sampling)
        dataset = kdf.ValidationDataset(dataset_label, contract, tuple(samples))
        del samples
        budgets = kdf.FrozenBudgets(budgets_label, contract, tuple(
            kdf.ValidationBudget(name, unit, absolute, relative, floor, True, label, estimator, level)
            for name, (unit, estimator, level, absolute, relative, floor) in V.S3_CAPS.items()
            for label in labels))
        declared = budgets.digest
        dataset_digest = dataset.digest
    out["timing"]["dataset_seconds"] = time.perf_counter() - t0
    out["rss_phase_bytes"]["dataset"] = int(sampler.peak)
    out["dataset_digest"] = dataset_digest
    out["budgets_digest"] = declared
    out["contract_canonical"] = contract.canonical
    log(f"    samples {out['timing']['samples_seconds']:.1f}s, dataset {out['timing']['dataset_seconds']:.1f}s "
        f"rss {sampler.peak / 2**20:.0f}MiB")
    # ---- the gate (12 more rebuilds inside compare_refinement) --------------
    t0 = time.perf_counter()
    with P.RssSampler() as sampler:
        verdict = kdf.compare_refinement(dataset, budgets, declared)
    out["timing"]["compare_seconds"] = time.perf_counter() - t0
    out["rss_phase_bytes"]["compare"] = int(sampler.peak)
    out["verdict"] = verdict.verdict
    out["reasons"] = list(verdict.reasons)
    out["levels"] = V.levels_table(verdict)
    finest = min(level.timestep for level in verdict.levels)
    smallest = min(level.absolute_error for level in verdict.levels if level.timestep == finest)
    out["smallest_finest_error"] = smallest
    gap = oracle_out["oracle_gap"]
    checks = out["checks"]
    checks["paired_bitwise"] = bool(paired)
    checks["oracle_margin_ok"] = bool(gap * V.S3_ORACLE_MARGIN <= smallest)
    checks["oracle_margin_ratio"] = (smallest / gap) if gap > 0 else float("inf")
    checks["survival_sign_ok"] = all(level.measured - level.reference >= -V.S3_SIGN_SLACK
                                     for level in verdict.levels if level.observable == "survival")
    checks["nonzero_se_ok"] = all(level.standard_error != 0.0 for level in verdict.levels)
    checks["gate_pass"] = verdict.verdict == "pass"
    out["procedure_ok"] = all(checks[k] for k in ("paired_bitwise", "oracle_margin_ok",
                                                  "survival_sign_ok", "nonzero_se_ok"))
    out["quadratic_seconds"] = (out["timing"]["samples_seconds"] + out["timing"]["dataset_seconds"]
                                + out["timing"]["compare_seconds"])
    log(f"    gate {verdict.verdict} in {out['timing']['compare_seconds']:.1f}s rss {sampler.peak / 2**20:.0f}MiB; "
        f"checks {json.dumps(checks, sort_keys=True)}")
    return out


# ---------------------------------------------------------------------------
# Child entry
# ---------------------------------------------------------------------------
def run_phase(kind, out_path, args):
    record = {"kind": kind, "exit_state": "started", "warnings": [], "pid": os.getpid()}
    lines = []

    def log(text):
        lines.append(text)
        print(text, flush=True)

    try:
        record["source_digest"] = P.source_fingerprint()["digest"]
        t0 = time.perf_counter()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            if kind == "oracle":
                result = oracle_phase(V.STATIONARY_CELL, args["time_factor"], args["space_factor"], log)
            elif kind == "construction":
                oracle_out = json.loads(Path(args["oracle_path"]).read_text())["result"]
                result = construction_phase(V.STATIONARY_CELL, args["time_factor"], args["walkers"], oracle_out,
                                            args["dataset_label"], args["budgets_label"], log)
            elif kind == "moving":
                result = V.moving_ladder(V.MOVING_CELL, args["time_factor"], args["trials_factor"],
                                         args["dataset_label"], args["budgets_label"], log)
            else:
                raise RuntimeError(kind)
            record["warnings"] = [f"{w.category.__name__}: {w.message}" for w in caught]
        record["wall_seconds"] = time.perf_counter() - t0
        record["ru_maxrss_bytes"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        record["result"] = result
        record["exit_state"] = "completed"
    except Exception as exc:                                                   # noqa: BLE001
        import traceback
        record["exit_state"] = f"exception:{type(exc).__name__}"
        record["error"] = "".join(traceback.format_exception(exc))[-4000:]
    finally:
        record["log"] = lines
        Path(out_path).write_text(P.canonical_json(record))


def run_child(kind, out_path, args, deadline, log):
    import psutil
    cmd = [sys.executable, str(Path(__file__).resolve()), "--phase", kind, "--out", str(out_path),
           "--args", json.dumps(args)]
    t0 = time.perf_counter()
    child = subprocess.Popen(cmd, cwd=str(REPO), env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
        time.sleep(0.05)
    stdout, stderr = child.communicate()
    wall = time.perf_counter() - t0
    record = json.loads(Path(out_path).read_text()) if Path(out_path).exists() else None
    if record is None:
        record = {"kind": kind, "exit_state": ceiling or f"exception:child_rc_{child.returncode}",
                  "error": stderr[-4000:], "warnings": []}
    elif ceiling:
        record["exit_state"] = ceiling
    record["parent_observed_rss_peak_bytes"] = int(rss_peak)
    record["child_wall_seconds"] = wall
    record["child_returncode"] = child.returncode
    if stderr.strip():
        record["stderr_tail"] = stderr[-2000:]
    for line in stdout.splitlines():
        log("    | " + line)
    return record


# ---------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------
def stationary_work(stage, walkers):
    cell = V.STATIONARY_CELL
    f, s = stage["time_factor"], stage["space_factor"]
    M, N = cell["base_space"] * s, cell["base_time"] * f
    margin = (2 * M) * (2 * N) if 2 * M <= 4800 else (M // 2) * (N // 2)
    fine = cell["base_fine_steps"] * f
    return {"oracle_cells": M * N + margin,
            "endpoint_observations": walkers * 3 * sum(fine // st for st in cell["strides"]),
            "resample_observations": cell["resamples"] * walkers * 12 * 3}


def preflight_stationary(stage, walkers, rates, quad_probe):
    """Priced linear terms plus the measured quadratic identity-check term."""
    work = stationary_work(stage, walkers)
    linear = (rates["space_time_cells"] * work["oracle_cells"]
              + rates["endpoint_observations"] * work["endpoint_observations"]
              + rates["resample_observations"] * work["resample_observations"])
    quad = 0.0
    if quad_probe:
        quad = quad_probe["quadratic_seconds"] * (walkers / quad_probe["walkers"]) ** 2
    return {"work": work, "linear_seconds": linear, "quadratic_seconds_extrapolated": quad,
            "predicted_seconds": (linear + quad) * PRICE_CONTINGENCY}


def choose_walkers(probe, rates, elapsed, stage, log):
    """Largest candidate whose extrapolated phase-B peak RSS is under 2 GiB and
    whose preflight fits the remaining budget."""
    base_peak = probe["base_peak_bytes"]                     # 6,000-walker construction (pricing)
    probe_peak = probe["peak_bytes"]                          # 24,000-walker construction (this session)
    slope = max(0.0, (probe_peak - base_peak) / (PROBE_WALKERS - BASE_WALKERS))
    decision = {"base_walkers": BASE_WALKERS, "base_peak_bytes": base_peak,
                "probe_walkers": PROBE_WALKERS, "probe_peak_bytes": probe_peak,
                "slope_bytes_per_walker": slope, "candidates": []}
    chosen = None
    for w in WALKER_CANDIDATES:
        peak = probe_peak + slope * (w - PROBE_WALKERS)
        pf = preflight_stationary(stage, w, rates, probe)
        fits_memory = peak < RSS_CEILING_BYTES
        fits_budget = elapsed + pf["predicted_seconds"] <= WALL_BUDGET_S
        decision["candidates"].append({"walkers": w, "extrapolated_peak_bytes": peak,
                                       "fits_memory": fits_memory, "preflight": pf,
                                       "fits_budget": fits_budget})
        log(f"    candidate {w}: extrapolated peak {peak / 2**20:.0f}MiB ({'ok' if fits_memory else 'OVER'}), "
            f"preflight {pf['predicted_seconds']:.0f}s ({'ok' if fits_budget else 'OVER'})")
        if chosen is None and fits_memory and fits_budget:
            chosen = w
    decision["chosen_walkers"] = chosen
    return decision


# ---------------------------------------------------------------------------
# Session
# ---------------------------------------------------------------------------
def session():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    t_session = time.perf_counter()
    log_lines = []

    def log(text):
        line = f"[{time.perf_counter() - t_session:7.1f}s] {text}"
        log_lines.append(line)
        print(line, flush=True)

    log("redesigned validation campaign session start")
    identity = P.machine_identity()
    env_digest = P.environment_fingerprint(identity)
    fp = P.source_fingerprint()
    budget = V.frozen_budget()
    allowances = {"probability": budget.allowance("probability"), "time": budget.allowance("time"),
                  "count": budget.allowance("count")}
    rates, pricing_digest = V.pricing_rates()
    pricing_obs = json.loads(P.OBSERVATIONS.read_text())
    base_peak = max(rec["ru_maxrss_bytes"] for rec in pricing_obs["cases"]["stationary_construction"]
                    if rec.get("exit_state") == "completed")
    previous = json.loads(PREVIOUS.read_text())
    results_sha_start = P.results_sha_snapshot(RESULTS)
    results_stat_start = P.results_stat_snapshot(RESULTS)
    package_stat_start = P.package_stat_digest()
    observations = {
        "schema": "validation-campaign-redesign-observations/v1",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "repo_git_head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(REPO), capture_output=True,
                                        text=True).stdout.strip(),
        "machine": identity, "environment_digest": env_digest, "source_fingerprint": fp,
        "pricing_derivation_digest": pricing_digest, "pricing_rates": rates,
        "previous_session": {"path": str(PREVIOUS.relative_to(REPO)), "started_at": previous["started_at"],
                             "sha256": hashlib.sha256(PREVIOUS.read_bytes()).hexdigest()},
        "constraints": {"wall_budget_seconds": WALL_BUDGET_S, "rss_ceiling_bytes": RSS_CEILING_BYTES,
                        "price_contingency": PRICE_CONTINGENCY, "walker_candidates": list(WALKER_CANDIDATES),
                        "probe_walkers": PROBE_WALKERS},
        "intended": V.INTENDED, "stationary_cell": V.STATIONARY_CELL, "moving_cell": V.MOVING_CELL,
        "moving_clocks": [list(c) for c in V.MOVING_CLOCKS],
        "budget": {"digest": budget.digest, "allowances": allowances, "trials_per_cell": budget.trials_per_cell,
                   "coverage_sigma": budget.coverage_sigma, "intended_timestep": budget.intended_timestep},
        "stages_plan": STAGES, "order": ORDER, "rules": V.RULES, "interpretations": INTERPRETATIONS,
        "results_snapshot": {"entries": len(results_stat_start), "sha_start": results_sha_start,
                             "package_stat_start": package_stat_start},
        "memory_scaling": None, "walker_decision": None, "stages": {}, "events": [],
    }

    def flush():
        observations["log"] = log_lines
        observations["session_wall_seconds"] = time.perf_counter() - t_session
        OBSERVATIONS.write_text(json.dumps(observations, indent=1, sort_keys=True, default=P._json_default))

    flush()
    deadline = t_session + WALL_BUDGET_S
    verdicts = {}
    walkers = None
    quad_probe = None

    def launch(kind, name, args):
        before = P.results_stat_snapshot(RESULTS)
        out_path = SCRATCH / f"{name}.json"
        rec = run_child(kind, out_path, args, deadline, log)
        after = P.results_stat_snapshot(RESULTS)
        rec["results_unchanged"] = (before == after and before == results_stat_start)
        if not rec["results_unchanged"]:
            rec["exit_state"] = "precondition:results_changed"
        rec["name"] = name
        return rec, out_path

    try:
        for short in ORDER:
            stage = STAGES[short]
            rec = {"short": short, "label": stage["label"], "kind": stage["kind"], "unit": stage["unit"]}
            dep = stage.get("depends_on")
            if dep and verdicts.get(dep) != "success":
                rec.update(exit_state="stopped:dependency", stage_verdict="not_run",
                           stage_reasons=[f"stop rule: predecessor {dep} returned {verdicts.get(dep, 'nothing')}"])
                observations["stages"][short] = rec
                observations["events"].append(f"{short}: stopped by dependency on {dep} ({verdicts.get(dep)})")
                log(f"{short}: stopped — predecessor {dep} = {verdicts.get(dep)}")
                flush()
                continue
            elapsed = time.perf_counter() - t_session
            # ---------------- stationary stages: phase A, (probe), phase B ----
            if stage["kind"] == "stationary":
                pf_a = {"predicted_seconds": rates["space_time_cells"] * stationary_work(stage, 1)["oracle_cells"]
                        * PRICE_CONTINGENCY}
                log(f"{short} phase A (oracle): preflight {pf_a['predicted_seconds']:.0f}s; elapsed {elapsed:.0f}s")
                if elapsed + pf_a["predicted_seconds"] > WALL_BUDGET_S:
                    rec.update(exit_state="skipped:preflight", stage_verdict="not_run",
                               stage_reasons=["oracle phase preflight exceeds the remaining budget"])
                    observations["stages"][short] = rec
                    verdicts[short] = "not_run"
                    flush()
                    continue
                oracle_rec, oracle_path = launch("oracle", f"{short}-oracle",
                                                 {"time_factor": stage["time_factor"],
                                                  "space_factor": stage["space_factor"]})
                rec["oracle"] = {k: v for k, v in oracle_rec.items() if k != "result"}
                rec["oracle"]["result"] = {k: v for k, v in oracle_rec.get("result", {}).items()
                                           if k != "reference"}
                log(f"{short} phase A: {oracle_rec['exit_state']} wall {oracle_rec.get('child_wall_seconds', 0):.0f}s "
                    f"rss {oracle_rec.get('ru_maxrss_bytes', 0) / 2**20:.0f}MiB")
                if oracle_rec["exit_state"] != "completed":
                    rec.update(exit_state=oracle_rec["exit_state"], stage_verdict="not_completed",
                               stage_reasons=[f"oracle phase {oracle_rec['exit_state']}"])
                    observations["stages"][short] = rec
                    observations["events"].append(f"{short}: oracle phase {oracle_rec['exit_state']}")
                    verdicts[short] = "not_completed"
                    flush()
                    continue
                flush()
                # ---- memory-scaling probe at 24,000 walkers (S1 only) ----------
                if walkers is None:
                    elapsed = time.perf_counter() - t_session
                    pf_p = preflight_stationary(stage, PROBE_WALKERS, rates, None)
                    log(f"memory probe: S1 construction at {PROBE_WALKERS} walkers; preflight (linear terms only) "
                        f"{pf_p['predicted_seconds']:.0f}s; elapsed {elapsed:.0f}s")
                    probe_rec, probe_path = launch("construction", "S1-probe-24000", {
                        "time_factor": stage["time_factor"], "walkers": PROBE_WALKERS,
                        "oracle_path": str(oracle_path),
                        "dataset_label": "T07 redesign memory probe: intended stationary cell, 24000 walkers",
                        "budgets_label": "T07 redesign memory probe: S3 reference budgets at the intended cell"})
                    probe_path.unlink(missing_ok=True)
                    observations["memory_scaling"] = {k: v for k, v in probe_rec.items() if k != "result"}
                    if probe_rec["exit_state"] != "completed":
                        observations["events"].append(f"memory probe {probe_rec['exit_state']}")
                        rec.update(exit_state=probe_rec["exit_state"], stage_verdict="not_completed",
                                   stage_reasons=[f"memory-scaling probe {probe_rec['exit_state']}"])
                        observations["stages"][short] = rec
                        verdicts[short] = "not_completed"
                        flush()
                        continue
                    pr = probe_rec["result"]
                    observations["memory_scaling"]["result"] = {
                        k: pr[k] for k in ("walkers", "fine_steps", "timing", "rss_phase_bytes", "verdict",
                                           "checks", "quadratic_seconds", "dataset_digest")}
                    observations["memory_scaling"]["result"]["rule_rows"] = V.judge_rows(
                        pr["levels"], "probability", allowances["probability"])
                    observations["memory_scaling"]["result"]["levels"] = pr["levels"]
                    quad_probe = {"walkers": PROBE_WALKERS, "quadratic_seconds": pr["quadratic_seconds"],
                                  "base_peak_bytes": base_peak, "peak_bytes": probe_rec["ru_maxrss_bytes"]}
                    log(f"memory probe: ru_maxrss {probe_rec['ru_maxrss_bytes'] / 2**20:.0f}MiB, phase peaks "
                        f"{ {k: round(v / 2**20) for k, v in pr['rss_phase_bytes'].items()} } MiB, quadratic "
                        f"seconds {pr['quadratic_seconds']:.1f}, wall {probe_rec['child_wall_seconds']:.0f}s")
                    decision = choose_walkers(quad_probe, rates, time.perf_counter() - t_session, stage, log)
                    observations["walker_decision"] = decision
                    walkers = decision["chosen_walkers"]
                    log(f"walker decision: {walkers}")
                    flush()
                    if walkers is None:
                        rec.update(exit_state="skipped:preflight", stage_verdict="not_run",
                                   stage_reasons=["no candidate walker count fits both the 2 GiB extrapolated "
                                                  "peak and the remaining budget"])
                        observations["stages"][short] = rec
                        verdicts[short] = "not_run"
                        flush()
                        continue
                elapsed = time.perf_counter() - t_session
                pf_b = preflight_stationary(stage, walkers, rates, quad_probe)
                rec["preflight"] = pf_b
                rec["walkers"] = walkers
                log(f"{short} phase B: {walkers} walkers; preflight {pf_b['predicted_seconds']:.0f}s (linear "
                    f"{pf_b['linear_seconds']:.0f}s + quadratic {pf_b['quadratic_seconds_extrapolated']:.0f}s, x1.5); "
                    f"elapsed {elapsed:.0f}s; remaining {WALL_BUDGET_S - elapsed:.0f}s")
                if elapsed + pf_b["predicted_seconds"] > WALL_BUDGET_S:
                    rec.update(exit_state="skipped:preflight", stage_verdict="not_run",
                               stage_reasons=[f"phase B preflight {pf_b['predicted_seconds']:.0f}s (of which the "
                                              f"O(walkers^2) identity check {pf_b['quadratic_seconds_extrapolated']:.0f}s) "
                                              f"exceeds the remaining {WALL_BUDGET_S - elapsed:.0f}s"])
                    observations["stages"][short] = rec
                    observations["events"].append(f"{short}: phase B skipped by preflight")
                    verdicts[short] = "not_run"
                    flush()
                    continue
                cons_rec, cons_path = launch("construction", f"{short}-construction", {
                    "time_factor": stage["time_factor"], "walkers": walkers, "oracle_path": str(oracle_path),
                    "dataset_label": f"T07 redesign {short}: intended stationary cell, {walkers} walkers, frozen endpoint sample",
                    "budgets_label": f"T07 redesign {short}: S3 reference budgets at the intended cell"})
                oracle_path.unlink(missing_ok=True)
                rec.update({k: v for k, v in cons_rec.items() if k != "name"})
                if cons_rec["exit_state"] == "completed":
                    res = cons_rec["result"]
                    rows = V.judge_rows(res["levels"], "probability", allowances["probability"])
                    rec["rule_rows"] = rows
                    reasons = []
                    if res["verdict"] != "pass":
                        reasons.append("ladder gate: " + "; ".join(res["reasons"])[:600])
                    if not res["procedure_ok"]:
                        reasons.append(f"procedure checks failed: {res['checks']}")
                    failing = [r for r in rows if not r["fits"]]
                    if failing:
                        reasons.append(f"{len(failing)} of {len(rows)} probability rows exceed the allowance "
                                       f"{allowances['probability']:.6g}: " + "; ".join(
                                           f"{r['observable']}@{r['position']} bound {r['bound']:.4g} ({r['ratio']:.1f}x)"
                                           for r in failing))
                    rec["stage_verdict"] = "success" if not reasons else "numerical_no_result"
                    rec["stage_reasons"] = reasons
                    rec["two_se_rows"] = [{"observable": r["observable"], "position": r["position"],
                                           "two_se": 2 * r["standard_error"],
                                           "two_se_fits": 2 * r["standard_error"] <= allowances["probability"]}
                                          for r in rows]
                    if stage["time_factor"] == 256:
                        cons_path.rename(SCRATCH / "S3-construction-keep.json")
                else:
                    rec.update(stage_verdict="not_completed", stage_reasons=[cons_rec["exit_state"]])
                    observations["events"].append(f"{short}: {cons_rec['exit_state']}")
                cons_path.unlink(missing_ok=True)
            # ---------------- S4: judge S3's frozen ladder on the time rows -----
            elif stage["kind"] == "stationary_time":
                s3 = observations["stages"]["S3"]
                res = s3["result"]
                rows = V.judge_rows(res["levels"], "time", allowances["time"])
                reasons = []
                if res["verdict"] != "pass":
                    reasons.append("ladder gate: " + "; ".join(res["reasons"])[:600])
                failing = [r for r in rows if not r["fits"]]
                if failing:
                    reasons.append(f"{len(failing)} of {len(rows)} time rows exceed the allowance "
                                   f"{allowances['time']:.6g}: " + "; ".join(
                                       f"{r['observable']}@{r['position']} bound {r['bound']:.4g} ({r['ratio']:.1f}x)"
                                       for r in failing))
                rec.update(exit_state="completed", result={**res, "reused_from": "S3"}, rule_rows=rows,
                           stage_verdict="success" if not reasons else "numerical_no_result",
                           stage_reasons=reasons, child_wall_seconds=0.0, ru_maxrss_bytes=0,
                           walkers=s3.get("walkers"))
            # ---------------- M6 ----------------------------------------------
            elif stage["kind"] == "moving":
                work = V.stage_work({**stage, "kind": "moving", "trials_factor": 1})
                predicted = V.preflight_seconds(work, rates)
                rec["work"] = work
                rec["preflight_predicted_seconds"] = predicted
                log(f"{short}: preflight {predicted:.0f}s; elapsed {elapsed:.0f}s; remaining {WALL_BUDGET_S - elapsed:.0f}s; "
                    f"work {json.dumps(work, sort_keys=True)}")
                if elapsed + predicted > WALL_BUDGET_S:
                    rec.update(exit_state="skipped:preflight", stage_verdict="not_run",
                               stage_reasons=[f"preflight {predicted:.0f}s exceeds the remaining budget"])
                    observations["stages"][short] = rec
                    verdicts[short] = "not_run"
                    flush()
                    continue
                mrec, mpath = launch("moving", short, {
                    "time_factor": stage["time_factor"], "trials_factor": stage["trials_factor"],
                    "dataset_label": f"T07 redesign {short}: intended moving-band pooled frozen sample, dt/16",
                    "budgets_label": f"T07 redesign {short}: S3b reference budgets at the intended cell"})
                mpath.unlink(missing_ok=True)
                rec.update({k: v for k, v in mrec.items() if k != "name"})
                if mrec["exit_state"] == "completed":
                    res = mrec["result"]
                    rows = V.judge_rows(res["levels"], "probability", allowances["probability"])
                    time_rows = V.judge_rows(res["levels"], "time", allowances["time"])
                    rec["rule_rows"] = rows
                    rec["time_rows_informational"] = time_rows
                    cap_reasons = [r for r in res["reasons"] if "added_resets_mean" in r]
                    other_reasons = [r for r in res["reasons"] if "added_resets_mean" not in r]
                    rec["added_resets_cap"] = {
                        "frozen_cap": res["caps"]["added_resets_mean"],
                        "gate_reasons": cap_reasons,
                        "finest_level": next(lv for lv in res["levels"] if lv["observable"] == "added_resets_mean"
                                             and lv["timestep"] == min(x["timestep"] for x in res["levels"])),
                        "gate_verdict_with_cap": res["verdict"],
                        "gate_would_pass_without_this_cap": (not other_reasons),
                        "note": "frozen cap reported as found; not re-frozen"}
                    reasons = []
                    if res["verdict"] != "pass":
                        reasons.append("ladder gate: " + "; ".join(res["reasons"])[:600])
                    if not res["procedure_ok"]:
                        reasons.append(f"procedure checks failed: {res['checks']}")
                    failing = [r for r in rows if not r["fits"]]
                    if failing:
                        reasons.append(f"{len(failing)} of {len(rows)} probability rows exceed the allowance "
                                       f"{allowances['probability']:.6g}: " + "; ".join(
                                           f"{r['observable']}@{r['position']} bound {r['bound']:.4g} ({r['ratio']:.1f}x)"
                                           for r in failing))
                    rec["stage_verdict"] = "success" if not reasons else "numerical_no_result"
                    rec["stage_reasons"] = reasons
                else:
                    rec.update(stage_verdict="not_completed", stage_reasons=[mrec["exit_state"]])
                    observations["events"].append(f"{short}: {mrec['exit_state']}")
            verdicts[short] = rec.get("stage_verdict")
            observations["stages"][short] = rec
            log(f"{short}: {rec.get('exit_state')} verdict={rec.get('stage_verdict')} wall={rec.get('child_wall_seconds', 0):.0f}s "
                f"rss={rec.get('ru_maxrss_bytes', 0) / 2**20:.0f}MiB reasons={rec.get('stage_reasons')}")
            flush()
    finally:
        for leftover in SCRATCH.glob("*.json"):
            leftover.unlink()
        try:
            SCRATCH.rmdir()
        except OSError:
            pass
        observations["results_snapshot"]["sha_end"] = P.results_sha_snapshot(RESULTS)
        observations["results_snapshot"]["package_stat_end"] = P.package_stat_digest()
        observations["results_snapshot"]["results_unchanged"] = (
            observations["results_snapshot"]["sha_end"] == results_sha_start)
        observations["results_snapshot"]["package_unchanged"] = (
            observations["results_snapshot"]["package_stat_end"] == package_stat_start)
        observations["finished_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        log(f"session end: wall {time.perf_counter() - t_session:.0f}s; results/ unchanged="
            f"{observations['results_snapshot']['results_unchanged']} package unchanged="
            f"{observations['results_snapshot']['package_unchanged']}")
        flush()
    observations["disposition"] = dispositions(observations)
    flush()
    write_report(observations)
    print(f"wrote {OBSERVATIONS} and {REPORT}")


# ---------------------------------------------------------------------------
# Disposition
# ---------------------------------------------------------------------------
def rows_from(short, rec, configuration, description, source):
    from adler_born_two_channel import experiments as xpr
    res = rec["result"]
    clusters = res["walkers"] if source == "stationary_oracle" else res["trials"]
    finest = min(lv["timestep"] for lv in res["levels"])
    return [xpr.NumericalEvidence(source=source, observable=lv["observable"], unit=lv["unit"],
                                  position=lv["position"], timestep=lv["timestep"],
                                  measured=lv["absolute_error"], standard_error=lv["standard_error"],
                                  sample_clusters=clusters, verdict=res["verdict"],
                                  configuration=configuration, description=description[:300])
            for lv in res["levels"] if lv["timestep"] == finest and lv["observable"] != "added_resets_mean"]


def dispositions(observations):
    from adler_born_two_channel import experiments as xpr
    budget = V.frozen_budget()
    previous = json.loads(PREVIOUS.read_text())
    prev_rows = V.evidence_rows(previous)                     # reference (17) + intended (S1-old, M5)
    reference = prev_rows["reference"]
    m5_old = [r for r in prev_rows["intended"] if r.source == "moving_band_audit"]
    new = []
    for short in ("S1", "S2", "S3", "M6"):
        rec = observations["stages"].get(short, {})
        if rec.get("exit_state") != "completed" or "result" not in rec:
            continue
        if short == "M6":
            desc = (f"T07 redesign stage M6 at the intended configuration: dt/16 replay, 40 master trials on the "
                    f"2^-13 mesh, three regime clocks, four replicates")
            new += rows_from(short, rec, "intended", desc, "moving_band_audit")
        else:
            res = rec["result"]
            desc = (f"T07 redesign stage {short} at the intended configuration: {res['walkers']} walkers, oracle "
                    f"grid {res['oracle_grid']}, {res['fine_steps']} fine steps")
            new += rows_from(short, rec, "intended", desc, "stationary_oracle")
    out = {"budget_digest": budget.digest, "sets": {}, "previous_sha256": observations["previous_session"]["sha256"]}
    for name, items in (("redesign_intended_only", new),
                        ("intended_all_kept_M5", new + m5_old),
                        ("reference_plus_intended_all", reference + new + m5_old)):
        d = xpr.numerical_disposition(budget, items)
        out["sets"][name] = {
            "rows_in": len(items), "verdict": d.verdict, "blockers": list(d.blockers),
            "probability_admissible_trials": d.probability_admissible_trials,
            "time_admissible": d.time_admissible, "admissible_trials": d.admissible_trials,
            "limiting": {u: (list(d.limiting(u)) if d.limiting(u) else None) for u in ("probability", "time")},
            "rows": [{"source": r[0], "observable": r[1], "position": r[2], "unit": r[3], "bound": r[4],
                      "allowance": r[5], "fits": bool(r[6]), "ratio": r[4] / r[5], "excess": r[4] - r[5]}
                     for r in d.rows],
            "evidence_digest": d.evidence_digest, "disposition_digest": d.digest,
            "configurations": sorted({i.configuration for i in items})}
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def _hms(s):
    if s is None:
        return "—"
    return f"{s:.1f} s" if s < 120 else f"{s:.0f} s ({s / 60:.1f} min)"


def _mib(b):
    return "—" if b is None else f"{b / 2**20:.0f} MiB"


def write_report(o):
    m = o["machine"]
    L = ["# Redesigned intended-configuration validation campaign — report\n",
         "**Nothing here is a physical finding, an approval, or a sufficiency promise.**  The sponsor's plan change "
         "authorized 16x walkers on the stationary path and running M6 despite M5's `numerical_no_result`; every "
         "other rule stays frozen.  The frozen added-resets cap is reported as found and is not re-frozen.  M5 was "
         "not re-run; M7 was not launched.\n",
         f"Session {o['started_at']} → {o.get('finished_at')}, wall {_hms(o.get('session_wall_seconds'))} of the "
         f"{WALL_BUDGET_S:.0f} s budget; per-process RSS ceiling 2 GiB; previous record "
         f"`{o['previous_session']['path']}` (sha256 `{o['previous_session']['sha256'][:16]}…`) untouched.\n",
         "## Environment identity\n", "| Field | Value |\n| --- | --- |"]
    for key in ("platform", "cpu_brand", "physical_cpus", "memory_bytes", "os_version", "python_version",
                "numpy_version", "numpy_blas"):
        L.append(f"| {key} | `{m.get(key, '')}` |")
    L += [f"| environment digest | `{o['environment_digest']}` |",
          f"| package source fingerprint | `{o['source_fingerprint']['digest']}` |",
          f"| repo git HEAD | `{o['repo_git_head']}` |",
          f"| frozen ticket-07 budget digest | `{o['budget']['digest']}` (allowances {o['budget']['allowances']}) |",
          f"| pricing derivation used for preflight | `{o['pricing_derivation_digest']}` |", ""]
    snap = o["results_snapshot"]
    L += ["## Tree integrity\n",
          f"- `results/` ({snap['entries']} entries) unchanged by SHA-256 = **{snap.get('results_unchanged')}**; package tree "
          f"(incl. `__pycache__`) unchanged = **{snap.get('package_unchanged')}**.",
          "- Strictly serial child processes (oracle phase and construction phase separately for each stationary stage); "
          "the parent polled RSS every 50 ms with a 2 GiB kill.  No verifier, pilot, production, sensitivity or fit.\n"]
    if o.get("events"):
        L += ["### Events\n"] + [f"- {e}" for e in o["events"]] + [""]
    ms = o.get("memory_scaling")
    wd = o.get("walker_decision")
    L += ["## Memory-scaling measurement and walker decision\n"]
    if ms and ms.get("exit_state") == "completed":
        r = ms["result"]
        L += [f"- S1 construction phase at **{r['walkers']} walkers** ({r['fine_steps']} fine steps): child ru_maxrss "
              f"**{_mib(ms['ru_maxrss_bytes'])}** (parent-observed {_mib(ms['parent_observed_rss_peak_bytes'])}); phase peaks "
              f"{ {k: round(v / 2**20) for k, v in r['rss_phase_bytes'].items()} } MiB; timing {json.dumps(r['timing'], sort_keys=True)}; "
              f"quadratic (identity-check-dominated) seconds {r['quadratic_seconds']:.1f}; gate {r['verdict']}; wall "
              f"{_hms(ms['child_wall_seconds'])}.",
              f"- Probe rule rows (probability, |error| + 2 SE vs allowance): " + "; ".join(
                  f"{x['observable']}@{x['position']} {x['bound']:.4f} ({x['ratio']:.1f}x)" for x in r["rule_rows"]) + "."]
    else:
        L.append(f"- Memory probe: {ms.get('exit_state') if ms else 'not run'}")
    if wd:
        L += [f"- Linear model: 6,000-walker construction peak {_mib(wd['base_peak_bytes'])} (pricing session), "
              f"{wd['probe_walkers']}-walker peak {_mib(wd['probe_peak_bytes'])} → slope {wd['slope_bytes_per_walker']:.1f} B/walker.",
              "", "| Candidate walkers | Extrapolated peak RSS | Under 2 GiB | Preflight (linear + quadratic, x1.5) | Fits budget |",
              "| --- | --- | --- | --- | --- |"]
        for c in wd["candidates"]:
            pf = c["preflight"]
            L.append(f"| {c['walkers']} | {_mib(c['extrapolated_peak_bytes'])} | {c['fits_memory']} | "
                     f"{_hms(pf['predicted_seconds'])} (linear {_hms(pf['linear_seconds'])}, quadratic "
                     f"{_hms(pf['quadratic_seconds_extrapolated'])}) | {c['fits_budget']} |")
        L += ["", f"**Chosen walker count: {wd['chosen_walkers']}**.", ""]
    L += ["## Stages\n",
          "| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for short in o["order"]:
        rec = o["stages"].get(short, {})
        res = rec.get("result", {})
        if rec.get("exit_state") == "completed":
            if "oracle_grid" in res:
                cfg = (f"oracle {res['oracle_grid']}, fine steps {res['fine_steps']}, timesteps "
                       f"{[f'{t:.3g}' for t in res['timesteps']]}, walkers {res['walkers']}")
            else:
                cfg = (f"{res['trials']} trials x 3 clocks x 4 replicates, mesh step {res['step']:.3g}, {res['steps']} steps, "
                       f"timesteps {[f'{t:.3g}' for t in res['timesteps']]}")
            rows = rec.get("rule_rows", [])
            fitting = sum(1 for r in rows if r["fits"])
            rss = rec.get("ru_maxrss_bytes", 0)
            if "oracle" in rec:
                rss = max(rss, rec["oracle"].get("ru_maxrss_bytes", 0))
            L.append(f"| **{short}** {rec['label']} | {rec['exit_state']} | {cfg} | {res['verdict']} | "
                     f"{'ok' if res.get('procedure_ok') else 'FAIL'} {json.dumps(res.get('checks'), sort_keys=True)} | "
                     f"{fitting}/{len(rows)} fit ({rec.get('unit')}) | **{rec.get('stage_verdict')}** | "
                     f"{_hms((rec.get('child_wall_seconds') or 0) + (rec.get('oracle', {}).get('child_wall_seconds') or 0))} | "
                     f"{_mib(rss)} (construction {_mib(rec.get('ru_maxrss_bytes'))}) |")
        else:
            L.append(f"| **{short}** {rec.get('label', '')} | {rec.get('exit_state', '—')} | — | — | — | — | "
                     f"**{rec.get('stage_verdict', '—')}** | — | — |")
    L.append("")
    for short in o["order"]:
        rec = o["stages"].get(short, {})
        L.append(f"### {short} — {rec.get('label', '')}\n")
        L.append(f"- State `{rec.get('exit_state')}`, stage verdict **{rec.get('stage_verdict')}**.")
        for r in rec.get("stage_reasons", []):
            L.append(f"- Reason: {r}")
        if short == "M6":
            L.append(f"- Frozen stop rule overridden by the sponsor: {V.RULES['stage_stop']}")
        if rec.get("exit_state") != "completed":
            L.append("")
            continue
        res = rec["result"]
        unit = rec["unit"]
        L.append("- Rules applied: " + V.RULES["stage_success"].format(unit=unit, allowance=o["budget"]["allowances"][unit])
                 + "; " + V.RULES["stage_no_result"] + "; gate = " + V.RULES["gate"][:160] + "…")
        L.append(f"- Ladder gate **{res['verdict']}**" + (f"; reasons {res['reasons']}" if res["reasons"] else "")
                 + f".  Procedure checks {json.dumps(res['checks'], sort_keys=True)}"
                 + (f"; oracle gap {res['oracle_gap']:.3e} ({res['oracle_margin_mode']} grid {res['oracle_margin_grid']}), "
                    f"smallest finest error {res['smallest_finest_error']:.3e}" if "oracle_gap" in res else "")
                 + f".  Dataset digest `{res['dataset_digest'][:16]}…`, budgets digest `{res['budgets_digest'][:16]}…`.")
        if "oracle" in rec:
            orc = rec["oracle"]
            L.append(f"- Oracle phase: wall {_hms(orc.get('child_wall_seconds'))}, ru_maxrss {_mib(orc.get('ru_maxrss_bytes'))}, "
                     f"timing {json.dumps(orc.get('result', {}).get('timing'), sort_keys=True)}.")
        if "preflight" in rec:
            pf = rec["preflight"]
            L.append(f"- Construction phase: preflight {_hms(pf['predicted_seconds'])} (linear {_hms(pf['linear_seconds'])} + quadratic "
                     f"{_hms(pf['quadratic_seconds_extrapolated'])}); actual {_hms(rec.get('child_wall_seconds'))}; timing "
                     f"{json.dumps(res.get('timing'), sort_keys=True)}; phase peaks "
                     f"{ {k: round(v / 2**20) for k, v in res.get('rss_phase_bytes', {}).items()} } MiB; ru_maxrss "
                     f"{_mib(rec.get('ru_maxrss_bytes'))}; warnings {len(rec.get('warnings', []))}.")
        if "work" in rec:
            L.append(f"- Work {json.dumps(rec['work'], sort_keys=True)}; preflight {_hms(rec.get('preflight_predicted_seconds'))}; "
                     f"actual {_hms(rec.get('child_wall_seconds'))}; timing {json.dumps(res.get('timing'), sort_keys=True)}; "
                     f"ru_maxrss {_mib(rec.get('ru_maxrss_bytes'))}; warnings {len(rec.get('warnings', []))}.")
        if rec.get("added_resets_cap"):
            c = rec["added_resets_cap"]
            fl = c["finest_level"]
            L.append(f"- **Frozen added-resets cap (reported separately, not re-frozen):** cap {c['frozen_cap']}; finest level "
                     f"{fl['measured']:.4f} ± {fl['standard_error']:.4f} (2-sigma bound {fl['measured'] + 2 * fl['standard_error']:.4f}); "
                     f"gate verdict with the cap **{c['gate_verdict_with_cap']}**; the gate's other clauses "
                     f"{'all pass' if c['gate_would_pass_without_this_cap'] else 'also fail'}; gate reasons naming it: {c['gate_reasons']}.")
        if rec.get("two_se_rows"):
            L.append("- 2 SE alone at the chosen walker count vs the probability allowance "
                     f"{o['budget']['allowances']['probability']:.6g}: " + "; ".join(
                         f"{x['observable']}@{x['position']} {x['two_se']:.4f} ({'fits' if x['two_se_fits'] else 'exceeds'})"
                         for x in rec["two_se_rows"]) + ".")
        L += ["", "| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for lv in res["levels"]:
            L.append(f"| {lv['observable']} | {lv['position']} | {lv['timestep']:.4g} | {lv['measured']:.5f} | {lv['reference']:.5f} | "
                     f"{lv['absolute_error']:.5f} | {lv['standard_error']:.5f} | {lv['paired_error']:.5f} | {lv['span_error']:.5f} |")
        for title, key in ((f"Stage rule rows ({unit})", "rule_rows"), ("Time rows (informational for M6)", "time_rows_informational")):
            if rec.get(key):
                L += ["", f"{title}; bound = |error| + 2 SE vs allowance {rec[key][0]['allowance']:.6g}:", "",
                      "| Observable | Position | |error| | SE | bound | ratio | fits |", "| --- | --- | --- | --- | --- | --- | --- |"]
                for r in rec[key]:
                    L.append(f"| {r['observable']} | {r['position']} | {r['absolute_error']:.5f} | {r['standard_error']:.5f} | "
                             f"{r['bound']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
        L.append("")
    d = o.get("disposition")
    if d:
        L += ["## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)\n", V.RULES["disposition"], ""]
        for name, s in d["sets"].items():
            L += [f"### Evidence set `{name}` ({s['rows_in']} rows; configurations {s['configurations']})\n",
                  f"- Verdict **{s['verdict']}**; blockers {s['blockers']}; probability-admissible trials "
                  f"{s['probability_admissible_trials']} (needs {o['budget']['trials_per_cell']}); time admissible "
                  f"{s['time_admissible']}; overall admissible {s['admissible_trials']}.",
                  f"- Limiting rows: {json.dumps(s['limiting'], sort_keys=True)}", "",
                  "| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
            for r in sorted(s["rows"], key=lambda r: -r["ratio"]):
                L.append(f"| {r['source']} | {r['observable']} | {r['position']} | {r['unit']} | {r['bound']:.5f} | "
                         f"{r['allowance']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
            L.append("")
    L += ["## Rules quoted\n"] + [f"- **{k}**: {v}" for k, v in V.RULES.items()] + [""]
    L += ["## Ambiguities and choices\n"] + [f"{i}. **{t}.** {x}" for i, (t, x) in enumerate(o["interpretations"], 1)] + [""]
    L += ["## Reproduce\n", "```", f"cd {REPO}",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_redesign_campaign.py --run",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_redesign_campaign.py --derive-only",
          "```", "", "## Session log\n", "```"] + o.get("log", []) + ["```"]
    REPORT.write_text("\n".join(L) + "\n")


# ---------------------------------------------------------------------------
def selftest():
    def log(t):
        print("  " + t)
    tiny = dict(V.STATIONARY_CELL, base_fine_steps=1024, base_space=120, base_time=120, chunk=150,
                namespace="t07-selftest-redesign")
    orc = oracle_phase(tiny, 1, 1, log)
    con = construction_phase(tiny, 1, 300, orc, "selftest", "selftest budgets", log)
    print("construction selftest:", con["verdict"], json.dumps(con["checks"], sort_keys=True),
          "quad", round(con["quadratic_seconds"], 3), "phases", {k: round(v / 2**20) for k, v in con["rss_phase_bytes"].items()})
    rates, _ = V.pricing_rates()
    for short in ("S1", "S2", "S3"):
        for w in (24000, 96000):
            pf = preflight_stationary(STAGES[short], w, rates, {"walkers": 24000, "quadratic_seconds": 100.0})
            print(f"  {short}@{w}: linear {pf['linear_seconds']:.0f}s quad(probe=100s) {pf['quadratic_seconds_extrapolated']:.0f}s -> {pf['predicted_seconds']:.0f}s")
    print("  M6 work:", V.stage_work({**STAGES['M6'], 'kind': 'moving', 'trials_factor': 1}))
    b = V.frozen_budget()
    print("  budget", b.allowance("probability"), b.allowance("time"))
    prev = json.loads(PREVIOUS.read_text())
    rows = V.evidence_rows(prev)
    print("  previous rows: reference", len(rows["reference"]), "intended", len(rows["intended"]),
          "M5 rows", sum(1 for r in rows["intended"] if r.source == "moving_band_audit"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--derive-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--phase")
    ap.add_argument("--out")
    ap.add_argument("--args")
    a = ap.parse_args()
    if a.phase:
        run_phase(a.phase, a.out, json.loads(a.args))
    elif a.selftest:
        selftest()
    elif a.derive_only:
        o = json.loads(OBSERVATIONS.read_text())
        o["disposition"] = dispositions(o)
        write_report(o)
        print(json.dumps({k: (v["verdict"], v["blockers"]) for k, v in o["disposition"]["sets"].items()}, indent=1))
    elif a.run:
        session()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
