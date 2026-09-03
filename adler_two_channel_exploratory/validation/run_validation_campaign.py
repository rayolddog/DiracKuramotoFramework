#!/usr/bin/env python3
"""
run_validation_campaign.py — the intended-configuration validation campaign
(ticket-07 alternative A, the six priced stages), run OUTSIDE the package.

Nothing in ``adler_born_two_channel`` is modified; its kernels are imported
read-only:  ``killed_diffusion`` (oracle, frozen contract, ``compare_refinement``),
``moving_band_audit`` (``replay_pulse``/``paired_leaves`` ladder), ``stochastic``,
``dynamics``, ``commitment``, ``model`` and ``experiments`` (the frozen ticket-07
budget and ``numerical_disposition``).  The verifier is never imported or run.

Each stage runs in its own child process (strictly one at a time); the parent
kills a child whose RSS exceeds 2 GiB, applies a 2-hour total wall budget with
a per-stage preflight against the prices in ../pricing/observations.json, and
writes observations.json after every stage so that a stop loses nothing.

Frozen rules applied (quoted in ``RULES`` and in the report):
  * the stage success / no-result / stop rules of verify.py ``_t07_campaign``;
  * the ticket-04 gate ``killed_diffusion.compare_refinement`` under the frozen
    reference caps (verify.py ``_s3_budgets`` / ``_audit_caps``) and the S3 / S3b
    procedure checks of verify.py (bitwise pairing, oracle margin, bias sign,
    nonzero standard errors; reset-only subset, both pulse edges covered);
  * the ticket-07 disposition rule of ``experiments.numerical_disposition`` with
    the frozen ``_t07_budget`` (probability allowance 0.004995, time allowance
    0.021953, bound = |measured| + 2 SE).

Modes:  --run | --stage NAME --out PATH [internal] | --derive-only | --selftest
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
import resource
import subprocess
import sys
import time
import tracemalloc
import warnings
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

import numpy as np                                                    # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PKG = REPO / "adler_born_two_channel"
RESULTS = PKG / "results"
PRICING_DIR = REPO / "adler_two_channel_exploratory" / "pricing"
OBSERVATIONS = HERE / "observations.json"
REPORT = HERE / "VALIDATION_REPORT.md"
SCRATCH = Path(os.environ.get(
    "VALIDATION_SCRATCH",
    "/private/tmp/claude-501/-Users-john-bramble-Projects-Physics-DiracKuramotoFramework/"
    "63b0fc51-d326-44ba-9e7c-eccecb8f1e8f/scratchpad")) / "validation_stages"

sys.path.insert(0, str(REPO))
sys.path.insert(0, str(PRICING_DIR))
import price_validation_campaign as P                                  # noqa: E402

# ---------------------------------------------------------------------------
# Hard constraints
# ---------------------------------------------------------------------------
WALL_BUDGET_S = 7200.0             # 2-hour total wall budget for the session
RSS_CEILING_BYTES = 2 * 1024 ** 3  # plan's 2 GiB per-process ceiling
PRICE_CONTINGENCY = 1.5            # the priced contingency, reused for preflight
INTENDED_TIMESTEP = 0.001953125    # verify.py _T07_TIMESTEP = 2**-9
COVERAGE_SIGMA = 2.0               # experiments.COVERAGE_SIGMA (checked at runtime)

# ---------------------------------------------------------------------------
# The intended configuration (verify.py _t07_config / _t07_matrix) and the two
# cells the stages are run on.  Declared here, before anything runs.
# ---------------------------------------------------------------------------
INTENDED = dict(grid_half_width=3.0, clocks=64, peak_coupling=1.0,
                pulse_duration=4.0, pulse_centre=0.0, phase_diffusion=0.08,
                lock_tolerance=0.35, dwell_time=0.5, timestep=INTENDED_TIMESTEP)

# 64 midpoint clocks on [-3, 3]: detuning_k = -3 + (k + 0.5) * 0.09375.  The
# three S3b regime clocks (0.0 central, +0.45 interior, -0.88 near-edge at
# K = 1) mapped to the nearest intended-grid clock (ties broken upward).
GRID_SPACING = 2 * INTENDED["grid_half_width"] / INTENDED["clocks"]
def grid_detuning(index):                                              # noqa: E302
    return -INTENDED["grid_half_width"] + (index + 0.5) * GRID_SPACING

MOVING_CLOCKS = ((32, grid_detuning(32), "central"),
                 (36, grid_detuning(36), "interior+"),
                 (22, grid_detuning(22), "near_edge-"))

STATIONARY_CELL = dict(
    coupling=INTENDED["peak_coupling"], detuning=grid_detuning(36),
    tolerance=INTENDED["lock_tolerance"], diffusion=INTENDED["phase_diffusion"],
    horizon=2.0, fractions=(0.25, 0.5, 0.75), walkers=6000, chunk=1500,
    window=1024, strides=(8, 4, 2), base_fine_steps=2048, base_space=600,
    base_time=600, quantile=0.35, resamples=200, seed=20260828,
    namespace="t07-campaign-stationary")
MOVING_CELL = dict(
    peak=INTENDED["peak_coupling"], duration=INTENDED["pulse_duration"],
    centre=INTENDED["pulse_centre"], tolerance=INTENDED["lock_tolerance"],
    dwell=INTENDED["dwell_time"], diffusion=INTENDED["phase_diffusion"],
    origin=INTENDED["pulse_centre"] - 0.5 * INTENDED["pulse_duration"],
    base_step=INTENDED_TIMESTEP,
    base_steps=int(math.ceil(INTENDED["pulse_duration"] / INTENDED_TIMESTEP)),
    strides=(4, 2, 1), replicates=4, resamples=200, seed=20260901,
    clocks=MOVING_CLOCKS, survival_fractions=(0.45, 0.60, 0.80), quantile=0.20,
    base_trials=40, physical_namespace="t07-campaign-physical",
    audit_namespace="t07-campaign-auxiliary", label_prefix="T07/campaign")

# The ticket-04 reference cells, reproduced once to (a) validate this mirror
# against the README's published bounds and (b) supply the 17 non-intended
# evidence rows the frozen disposition was built from.
REFERENCE_STATIONARY = dict(
    coupling=P.S3["coupling"], detuning=P.S3["detuning"],
    tolerance=P.S3["tolerance"], diffusion=P.S3["diffusion"],
    horizon=P.S3["horizon"], fractions=P.S3["fractions"], walkers=P.S3["walkers"],
    chunk=P.S3["chunk"], window=P.S3["window"], strides=P.S3["strides"],
    base_fine_steps=P.S3["fine_steps"], base_space=P.S3["space"],
    base_time=P.S3["time"], quantile=P.S3["quantile"], resamples=P.S3["resamples"],
    seed=P.S3["seed"], namespace=P.S3["namespace"])
REFERENCE_MOVING = dict(
    peak=P.AUDIT["peak"], duration=P.AUDIT["duration"], centre=0.0,
    tolerance=P.AUDIT["tolerance"], dwell=P.AUDIT["dwell"],
    diffusion=P.AUDIT["diffusion"], origin=P.AUDIT["origin"],
    base_step=P.AUDIT["fine_step"], base_steps=P.AUDIT["steps"],
    strides=P.AUDIT["strides"], replicates=P.AUDIT["replicates"],
    resamples=P.AUDIT["resamples"], seed=P.AUDIT["seed"], clocks=P.AUDIT["clocks"],
    survival_fractions=P.AUDIT["survival_fractions"], quantile=P.AUDIT["quantile"],
    base_trials=P.AUDIT["trials"], physical_namespace=P.AUDIT["physical_namespace"],
    audit_namespace=P.AUDIT["audit_namespace"], label_prefix="S3b/ladder")

# Frozen reference caps (verify.py _s3_budgets / _audit_caps), NOT re-derived.
S3_CAPS = {   # observable: (unit, estimator, level, absolute, relative, floor)
    "survival": ("probability", "mean", 0.5, 0.09, 0.30, 0.012),
    "exit_quantile_p35": ("time", "quantile", 0.35, 0.30, 0.45, 0.030),
    "exit_count_upper": ("probability", "mean", 0.5, 0.07, 0.45, 0.012),
    "exit_count_lower": ("probability", "mean", 0.5, 0.08, 0.45, 0.012),
}
S3_ORACLE_MARGIN = 20.0            # verify.py _S3_ORACLE_MARGIN
S3_SIGN_SLACK = 0.02               # verify.py: "fell below the oracle by" > 0.02

# The seven frozen stages (verify.py _T07_STAGES) with this runner's plan.
STAGES = [
    dict(short="REF_S3", kind="reference_stationary", label="ticket-04 S3 stationary reference ladder (reproduction, non_intended)", depends_on=None, time_factor=1, space_factor=1, unit=None),
    dict(short="REF_S3B", kind="reference_moving", label="ticket-04 S3b pooled moving-band ladder (reproduction, non_intended)", depends_on=None, trials_factor=1, time_factor=1, unit=None),
    dict(short="S1", kind="stationary", label="stationary probability, dt/16 at doubled space", unit="probability", attacks="timestep_bias", time_factor=16, space_factor=2, depends_on=None),
    dict(short="S2", kind="stationary", label="stationary probability, dt/64 at quadrupled space", unit="probability", attacks="timestep_bias", time_factor=64, space_factor=4, depends_on="S1"),
    dict(short="S3", kind="stationary", label="stationary probability, dt/256 at eightfold space", unit="probability", attacks="timestep_bias", time_factor=256, space_factor=8, depends_on="S2"),
    dict(short="S4", kind="stationary_time", label="stationary time quantile, dt/256 at eightfold space", unit="time", attacks="timestep_bias", time_factor=256, space_factor=8, depends_on="S3"),
    dict(short="M5", kind="moving", label="moving-band probability, 64x master trials", unit="probability", attacks="sampling_error", trials_factor=64, time_factor=1, depends_on=None),
    dict(short="M6", kind="moving", label="moving-band probability, dt/16 replay", unit="probability", attacks="timestep_bias", trials_factor=1, time_factor=16, depends_on="M5"),
    dict(short="M7", kind="not_launched", label="moving-band time quantile, 1024x master trials", unit="time", attacks="sampling_error", trials_factor=1024, time_factor=1, depends_on="M5"),
]
ORDER = ["REF_S3", "REF_S3B", "S1", "S2", "S3", "S4", "M5", "M6", "M7"]

RULES = {
    "stage_success": "verify.py _t07_campaign success_rule: \"every {unit} row of this ladder must land, bias plus 2.0 standard errors, under the frozen {unit} allowance {allowance:.6g} at the trial count the matrix proposes\"",
    "stage_no_result": "verify.py _t07_campaign no_result_rule: \"a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided\"",
    "stage_stop": "verify.py _t07_campaign stop_rule: \"stop at the first stage whose own predecessor returned a numerical_no_result; a later stage never runs on an unresolved one.  There is no resource cap here because there is no measured cost to cap\"",
    "matrix_failure": "verify.py _t07_matrix failure_rule: \"a refinement ladder that misses the frozen numerical budget, or a moving-band audit that returns numerical_no_result, blocks scientific interpretation of the whole sweep; no fit window is reselected and no budget is widened after results are opened\"",
    "gate": "killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) budgeted and sampled with the contract's cluster and level count; (2) at the finest timestep the uncertainty-aware absolute error |error| + coverage*SE is within the absolute cap and the relative point estimate within the relative cap; (3) the finest error is no larger than the coarsest within ONE allowance (resolution floor + coverage * paired bootstrap SE of the end-to-end change); (4) at most one adjacent pair may go the wrong way, inside the floor + coverage * paired SE of that step.  Failure of any clause yields numerical_no_result.",
    "frozen_contract": "README 'The frozen contract': \"FrozenBudgets hashes its own contents, and compare_refinement refuses to produce a verdict at all unless the caller hands back the digest it recorded earlier.\"  The reference caps of verify.py _s3_budgets and _audit_caps are used unchanged; no tolerance is invented.",
    "s3_oracle_margin": "verify.py (S3 check): \"the oracle moved by {gap} under its own refinement, which is not a factor 20 below the smallest endpoint error it is the reference for\" -> problem; i.e. oracle_gap * 20 <= smallest finest-level absolute error.",
    "s3_sign": "verify.py (S3 check): \"endpoint survival fell below the oracle by {x}; missing a between-step exit can only overcount uninterrupted dwell\" -> problem when measured - reference < -0.02.",
    "s3_zero_se": "verify.py (S3 check): \"a level reports a zero bootstrap standard error; every S3 observable is a Monte Carlo estimate and none of them is deterministic\".",
    "s3_paired": "verify.py _s3_measured: each coarse increment must be the bit-for-bit left-to-right sum of the same fine leaves (control against PhaseNoiseStream._coarse_kicks_uniform).",
    "s3b_subset": "moving_band_audit reset-only contract (README 'The audit'): \"Every audited commitment is a delayed copy of an endpoint one at every level and in every cell\" -> AuditedRun.subset_holds for every record.",
    "s3b_edges": "README 'The reduced matrix': \"Both pulse edges are covered by construction ... measured, by requiring every cell to report eligible intervals on both the rising and the falling side of its window\".",
    "evidence_rows": "verify.py _t07_evidence: every observable at every position at each ladder's finest level, added_resets_mean excluded (frozen with require_decrease=false, no continuum limit), measured = absolute_error, standard_error = bootstrap SE, sample_clusters = walkers / master trials, verdict = the ladder's verdict.",
    "disposition": "experiments.numerical_disposition: bound = |measured| + coverage_sigma * SE compared with budget.allowance(unit) (probability: 0.25 * planned 95% half-width at 2406 trials = 0.004995; time: 0.25 * 0.08 + one intended timestep = 0.021953); blockers: a numerical_no_result row is carried through; bound > allowance; not measured at the intended configuration; probability window empty below 2406 trials; any time row failing fails at every trial count.  README: \"A measured discrepancy, inflated by the budget's own frozen coverage sigma, must sit under one quarter of the planned production 95 % half-width, with one intended timestep added for a commit-time quantile.\"",
}

INTERPRETATIONS = [
    ("'intended configuration' versus 'relative to the ticket-04 ladder'", "The frozen stage candidates say 'timestep x{f}, sample x{s}, spatial x{sp} relative to the ticket-04 ladder', while the ticket-07 blocker no_evidence_at_intended_configuration and NumericalBudget.intended_timestep (2^-9) define 'intended' by the production physics.  As instructed, the stages are run on the intended physics (pulse 4.0 at peak coupling 1.0, phase diffusion 0.08, tolerance 0.35, dwell 0.5, dt = 2^-9 on the 64-clock +-3 grid) with the outline's refinement factors and trial counts: stationary dt/f means finest endpoint step 2^-9/f (fine steps 2048*f over horizon 2.0) with the oracle grid (600*space_factor) x (600*f); moving 'x1 timestep' means the ladder (4dt, 2dt, dt) with dt = 2^-9 over the 2048-step pulse window, and dt/16 means (4,2,1) x 2^-13 over 32768 steps."),
    ("the stationary cell at the intended configuration", "The S3 procedure is one fixed coupling, one fixed band, three starts.  At the intended configuration: coupling = the intended peak coupling 1.0, detuning = the intended-grid clock nearest the S3b interior regime (+0.45 -> index 36, 0.421875; the S3 reference ratio 0.3/0.8 = 0.375 maps to the same clock under an upward tie-break), tolerance 0.35, diffusion 0.08, horizon 2.0 and quantile p35 exactly as S3, starts at 0.25/0.5/0.75 of the admissible band, 6000 walkers (sample factor 1), chunk 1500 / window 1024 / strides (8,4,2) as S3."),
    ("the moving cell and '64 clocks'", "The S3b pooled ladder is 3 regime clocks x master trials x 3 strides x 4 auxiliary replicates.  The outline scales its master trials (64x -> 2560) and its timestep; it does not change the clock set.  Running all 22 eligible clocks of the 64-clock grid at 2560 trials would cost ~7x more than M5's price (about 8 hours) and cannot fit the 2-hour budget, so the three regime clocks are mapped onto the intended grid (central -> index 32, 0.046875; interior+ -> 36, 0.421875; near_edge- -> 22, -0.890625; the even-parity grid has no clock at exactly 0) and keyed by their grid index.  Peak coupling 1.0 is the benchmark fixture's (_t07_config) and S3b's; the production matrix sweeps six nodes and its own dt-halving refinement at 0.6598/1.1487 is a different, unpriced design."),
    ("the oracle-margin check at eightfold space", "verify.py refines the oracle (2M, 2N) and requires the change to be 20x below the smallest endpoint error.  At M = 4800 the refined grid (9600 x 307200) needs ~740 MB per dense matrix and cannot stay under 2 GiB, so for S3/S4 the check differences against the COARSER grid (2400 x 76800); for a second-order scheme that overstates the oracle's own error by about 3x, the conservative direction.  S1 and S2 use the refined grid as verify.py does."),
    ("S4", "S4 is 'the same three with time observable' on the dt/256 eightfold ladder S3 already computed; the keyed streams are deterministic and digest-verified, so S4 judges the time rows of S3's frozen ladder instead of recomputing it (13 minutes), and its own stage rule is applied to the time-unit rows."),
    ("frozen caps at the intended cell", "The S3 reference caps (survival 0.09/0.30/floor 0.012; p35 0.30/0.45/0.030; exit counts 0.07 and 0.08/0.45/0.012) and the S3b caps (0.10/4.0/floor 0.010; quantile floor = coarsest timestep; added_resets 3.0/30.0) are applied unchanged, as the frozen contract requires; their floors were derived for 6000 walkers / 40 trials x 4 replicates and are kept as frozen even where the sample is larger."),
    ("stage verdict", "A stage 'succeeds' only if (i) compare_refinement under the frozen reference caps returns pass, (ii) the procedure's own checks pass (S3: bitwise pairing, oracle margin, bias sign, nonzero SE; S3b: reset-only subset on every record, both pulse edges on every clock), and (iii) every row of the stage's unit at the finest level satisfies |error| + 2 SE <= the frozen allowance.  Anything else is numerical_no_result and the stop rule applies to its dependents."),
    ("reference reproduction", "REF_S3 and REF_S3B re-run the ticket-04 reference ladders through the same kernels (not the verifier) to validate this mirror against the README's published bounds (stationary survival 0.04125, p35 0.15290, moving p20 0.17700) and to supply the 17 non_intended rows; they are not stages."),
    ("preflight", "predicted seconds = 1.5 x sum(component slowest rate from ../pricing/observations.json x the stage's work at the intended configuration, oracle-margin solve included); a stage is launched only if elapsed + predicted <= 7200 s."),
]


# ---------------------------------------------------------------------------
# Kernel procedures (parametrised mirrors of verify.py _s3_* and _audit_*)
# ---------------------------------------------------------------------------
def stationary_geometry(cell):
    from adler_born_two_channel import killed_diffusion as kdf, moving_band_audit as mba
    lower, upper = mba.admissible_band(cell["coupling"], cell["detuning"], cell["tolerance"])
    starts = np.array([lower + (upper - lower) * f for f in cell["fractions"]])
    geometry = kdf.BandGeometry(lower, upper, cell["diffusion"], cell["coupling"], cell["detuning"])
    return lower, upper, starts, geometry


def stationary_ladder(cell, time_factor, space_factor, dataset_label, budgets_label,
                      oracle_margin_mode, log):
    """verify.py _s3_oracle + _s3_measured + _s3_dataset + _s3_budgets +
    compare_refinement + the S3 check's own procedure checks."""
    from adler_born_two_channel import killed_diffusion as kdf, stochastic as stoch
    lower, upper, starts, geometry = stationary_geometry(cell)
    fine_steps = cell["base_fine_steps"] * time_factor
    M, N = cell["base_space"] * space_factor, cell["base_time"] * time_factor
    strides, chunk, window, walkers = cell["strides"], cell["chunk"], cell["window"], cell["walkers"]
    positions = starts.size
    step = cell["horizon"] / fine_steps
    out = {"cell": {k: (list(v) if isinstance(v, tuple) else v) for k, v in cell.items()},
           "band": [lower, upper], "starts": starts.tolist(), "oracle_grid": [M, N],
           "fine_steps": fine_steps, "timesteps": [step * s for s in strides],
           "timing": {}, "checks": {}}
    t0 = time.perf_counter()
    oracle = kdf.solve_survival(geometry, starts, cell["horizon"], M, N)
    out["timing"]["oracle_seconds"] = time.perf_counter() - t0
    out["oracle_closure_residual"] = oracle.closure_residual
    log(f"    oracle {M}x{N} solved in {out['timing']['oracle_seconds']:.1f}s")
    # --- the oracle's own discretization error (verify.py S3 check) ---------
    t0 = time.perf_counter()
    if oracle_margin_mode == "refined":
        other = kdf.solve_survival(geometry, starts, cell["horizon"], 2 * M, 2 * N)
        gap = float(np.max(np.abs(oracle.survival - other.survival[:, ::2])))
        out["oracle_margin_grid"] = [2 * M, 2 * N]
    else:
        other = kdf.solve_survival(geometry, starts, cell["horizon"], M // 2, N // 2)
        gap = float(np.max(np.abs(oracle.survival[:, ::2] - other.survival)))
        out["oracle_margin_grid"] = [M // 2, N // 2]
    del other
    out["oracle_margin_mode"] = oracle_margin_mode
    out["oracle_gap"] = gap
    out["timing"]["oracle_margin_seconds"] = time.perf_counter() - t0
    log(f"    oracle margin ({oracle_margin_mode} {out['oracle_margin_grid']}): gap {gap:.3e}")
    reference = {
        "survival": oracle.survival[:, -1],
        "exit_quantile_p35": oracle.quantiles([cell["quantile"]])[:, 0],
        "exit_count_upper": oracle.upper_exit[:, -1],
        "exit_count_lower": oracle.lower_exit[:, -1],
    }
    out["reference"] = {k: v.tolist() for k, v in reference.items()}
    if not all(np.all(np.isfinite(v)) for v in reference.values()):
        raise RuntimeError("the oracle reference is not finite (a quantile the "
                           "solution never reaches within the horizon)")
    labels = tuple(f"x={value:.6f}" for value in starts)
    # --- the paired endpoint ladder (verify.py _s3_measured) ---------------
    mesh = stoch.FinestMesh(0.0, step)
    stream = stoch.PhaseNoiseStream(cell["namespace"], mesh, cell["diffusion"])
    t0 = time.perf_counter()
    paired = True
    exits = {s: np.full((walkers, positions), np.inf) for s in strides}
    uppers = {s: np.zeros((walkers, positions), dtype=bool) for s in strides}
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
    log(f"    endpoint walk {walkers}x{fine_steps} in {out['timing']['walk_seconds']:.1f}s; paired={paired}")
    # --- censoring, frozen samples, dataset (verify.py _s3_dataset) --------
    t0 = time.perf_counter()
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
    sampling = kdf.SamplingDesign(
        unit="endpoint walker: one independent keyed Brownian stream",
        clusters=walkers, replications=1,
        method="cluster bootstrap over walkers, one resample of clusters evaluated at every "
               "refinement level so that level contrasts are paired",
        resamples=cell["resamples"], coverage=2.0, seed=cell["seed"])
    contract = kdf.RefinementContract(tuple(step * s for s in strides), 2.0, sampling)
    dataset = kdf.ValidationDataset(dataset_label, contract, tuple(samples))
    budgets = kdf.FrozenBudgets(budgets_label, contract, tuple(
        kdf.ValidationBudget(name, unit, absolute, relative, floor, True, label, estimator, level)
        for name, (unit, estimator, level, absolute, relative, floor) in S3_CAPS.items()
        for label in labels))
    declared = budgets.digest                       # recorded before the verdict
    out["timing"]["dataset_seconds"] = time.perf_counter() - t0
    out["dataset_digest"] = dataset.digest
    out["budgets_digest"] = declared
    out["contract_canonical"] = contract.canonical
    # --- the gate ----------------------------------------------------------
    t0 = time.perf_counter()
    verdict = kdf.compare_refinement(dataset, budgets, declared)
    out["timing"]["compare_seconds"] = time.perf_counter() - t0
    out["verdict"] = verdict.verdict
    out["reasons"] = list(verdict.reasons)
    out["levels"] = levels_table(verdict)
    finest = min(level.timestep for level in verdict.levels)
    smallest = min(level.absolute_error for level in verdict.levels if level.timestep == finest)
    out["smallest_finest_error"] = smallest
    checks = out["checks"]
    checks["paired_bitwise"] = bool(paired)
    checks["oracle_margin_ok"] = bool(gap * S3_ORACLE_MARGIN <= smallest)
    checks["oracle_margin_ratio"] = (smallest / gap) if gap > 0 else float("inf")
    checks["survival_sign_ok"] = all(
        level.measured - level.reference >= -S3_SIGN_SLACK
        for level in verdict.levels if level.observable == "survival")
    checks["nonzero_se_ok"] = all(level.standard_error != 0.0 for level in verdict.levels)
    checks["gate_pass"] = verdict.verdict == "pass"
    out["procedure_ok"] = all(checks[k] for k in ("paired_bitwise", "oracle_margin_ok",
                                                  "survival_sign_ok", "nonzero_se_ok"))
    log(f"    gate {verdict.verdict}; checks {checks}")
    return out


def moving_objects(cell, step):
    from adler_born_two_channel import (commitment as cmt, dynamics as dyn, model as mdl,
                                        moving_band_audit as mba, stochastic as stoch)
    train = dyn.PulseTrain((mdl.RaisedCosinePulse(cell["peak"], cell["duration"], center=cell["centre"]),))
    criterion = cmt.LockCriterion(cell["tolerance"], cell["dwell"])
    mesh = stoch.FinestMesh(cell["origin"], step)
    stream = stoch.PhaseNoiseStream(cell["physical_namespace"], mesh, cell["diffusion"])
    audit = mba.AuditUniformStream(cell["audit_namespace"], mesh, 0)
    paths = {clock: dyn.ClockPath(det, train, "full", 0.0) for clock, det, _ in cell["clocks"]}
    return train, criterion, mesh, stream, audit, paths


def count_moving_intervals(cell, step, steps):
    """Exact per-trial (physical, eligible) counters, mirroring paired_leaves'
    segment construction without generating leaves (as in the pricing script)."""
    from adler_born_two_channel.raw_experiments import elementary_segments
    train, criterion, mesh, stream, audit, paths = moving_objects(cell, step)
    physical = eligible = 0
    for stride in cell["strides"]:
        for clock, _, _ in cell["clocks"]:
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
            physical += sum(1 for a, b in segments if b > a)
            eligible += sum(1 for a, b in segments if b > a and
                            path._cached_schedule.interval_state(a, b) == "interior")
    return physical, eligible


def moving_ladder(cell, time_factor, trials_factor, dataset_label, budgets_label, log):
    """verify.py _audit_ladder + _audit_dataset + _audit_budgets +
    compare_refinement + the S3b procedure checks (subset, both edges)."""
    from adler_born_two_channel import killed_diffusion as kdf, model as mdl, moving_band_audit as mba
    step = cell["base_step"] / time_factor
    steps = cell["base_steps"] * time_factor
    trials = int(cell["base_trials"] * trials_factor)
    strides, replicates = cell["strides"], cell["replicates"]
    train, criterion, mesh, stream, audit, paths = moving_objects(cell, step)
    clocks = len(cell["clocks"])
    physical_per_trial, eligible_per_trial = count_moving_intervals(cell, step, steps)
    out = {"cell": {k: (list(v) if isinstance(v, tuple) else v) for k, v in cell.items()},
           "mesh": mesh.identity, "step": step, "steps": steps, "trials": trials,
           "timesteps": [step * s for s in strides], "train_digest": train.digest,
           "physical_stream": stream.stream_prefix, "audit_stream": audit.stream_prefix,
           "physical_intervals": physical_per_trial * trials,
           "audited_evaluations": eligible_per_trial * trials * replicates,
           "timing": {}, "checks": {}}
    t0 = time.perf_counter()
    records = hashlib.sha256()
    subset = True
    regimes = {}
    ladder = {}
    for stride in strides:
        primary = np.full((trials, clocks), np.inf)
        audited = np.full((trials, clocks, replicates), np.inf)
        added = np.zeros((trials, clocks, replicates))
        for column, (clock, detuning, regime) in enumerate(cell["clocks"]):
            path = paths[clock]
            rising = falling = 0
            for trial in range(trials):
                phase = -math.pi + mdl.TWO_PI * (trial + 0.5) / trials
                runs = mba.replay_pulse(path, criterion, stream, audit, trial, clock, phase, 0,
                                        steps, f"{cell['label_prefix']}/{regime}",
                                        replicates=replicates, stride=stride)
                if runs[0].primary_committed_at is not None:
                    primary[trial, column] = runs[0].primary_committed_at
                rising += runs[0].rising_intervals
                falling += runs[0].falling_intervals
                for replicate, record in enumerate(runs):
                    subset &= record.subset_holds
                    added[trial, column, replicate] = record.added_resets
                    if record.audited_committed_at is not None:
                        audited[trial, column, replicate] = record.audited_committed_at
                    records.update(P.canonical_json(dataclasses.asdict(record)).encode())
            regimes.setdefault(regime, {})[f"stride={stride}"] = {"rising": rising, "falling": falling}
            if trials >= 200:
                log(f"    stride {stride} clock {clock} ({regime}) done at "
                    f"{time.perf_counter() - t0:.0f}s")
        ladder[stride] = (primary, audited, added)
    out["timing"]["ladder_seconds"] = time.perf_counter() - t0
    out["records_digest"] = records.hexdigest()
    out["regimes"] = regimes
    log(f"    ladder {trials} trials x {clocks} clocks x {len(strides)} strides in "
        f"{out['timing']['ladder_seconds']:.0f}s; subset={subset}")
    # --- dataset and frozen budgets (verify.py _audit_samples/_audit_budgets)
    t0 = time.perf_counter()
    horizon = train.support()[1]
    start = train.support()[0]
    moments = tuple(start + (horizon - start) * f for f in cell["survival_fractions"])
    primary = np.minimum(np.stack([ladder[s][0] for s in strides], axis=-1), horizon)
    audited = np.minimum(np.stack([ladder[s][1].reshape(trials, -1) for s in strides], axis=-1), horizon)
    added = np.stack([ladder[s][2].reshape(trials, -1) for s in strides], axis=-1)
    committed = lambda block: (block < horizon).astype(float)                       # noqa: E731
    names = tuple(f"trial-{index}" for index in range(trials))
    arms = [clock for clock, _, _ in cell["clocks"]]
    audited_members = tuple(f"clock-{clock}/replicate-{rep}" for clock in arms for rep in range(replicates))
    primary_members = tuple(f"clock-{clock}" for clock in arms)
    pair = lambda v, b: (v, b, 0.0, names, audited_members, primary_members)          # noqa: E731
    qname = f"commit_time_quantile_p{int(cell['quantile'] * 100)}_shift"
    samples = [kdf.PairedSample("commit_probability_shift", "pooled", *pair(committed(audited), committed(primary)))]
    for moment, fraction in zip(moments, cell["survival_fractions"]):
        samples.append(kdf.PairedSample(f"survival_shift_at_{fraction:.2f}", "pooled",
                                        *pair((audited > moment).astype(float), (primary > moment).astype(float))))
    samples.append(kdf.PairedSample(qname, "pooled", *pair(audited, primary)))
    samples.append(kdf.PairedSample("added_resets_mean", "pooled", added, None, 0.0, names, audited_members))
    sampling = kdf.SamplingDesign(
        unit="master trial identifier: one initial phase, shared by every clock and by every refinement level",
        clusters=trials, replications=replicates,
        method="cluster bootstrap over master trial identifiers, one resample of clusters evaluated at "
               "every refinement level so that level contrasts are paired; auxiliary replications travel "
               "with their cluster", resamples=cell["resamples"], coverage=2.0, seed=cell["seed"])
    timesteps = tuple(step * s for s in strides)
    contract = kdf.RefinementContract(timesteps, 2.0, sampling)
    dataset = kdf.ValidationDataset(dataset_label, contract, tuple(samples))
    caps = {"commit_probability_shift": (0.10, 4.0, 0.010),
            qname: (0.10, 4.0, max(timesteps)),
            "added_resets_mean": (3.0, 30.0, 0.0)}
    for fraction in cell["survival_fractions"]:
        caps[f"survival_shift_at_{fraction:.2f}"] = (0.10, 4.0, 0.010)
    observables = [("commit_probability_shift", "probability", "mean", 0.5, True)]
    observables += [(f"survival_shift_at_{f:.2f}", "probability", "mean", 0.5, True) for f in cell["survival_fractions"]]
    observables.append((qname, "time", "quantile", cell["quantile"], True))
    observables.append(("added_resets_mean", "count", "mean", 0.5, False))
    budgets = kdf.FrozenBudgets(budgets_label, contract, tuple(
        kdf.ValidationBudget(name, unit, caps[name][0], caps[name][1], caps[name][2], decreasing, "pooled", estimator, level)
        for name, unit, estimator, level, decreasing in observables))
    declared = budgets.digest
    out["timing"]["dataset_seconds"] = time.perf_counter() - t0
    out["dataset_digest"] = dataset.digest
    out["budgets_digest"] = declared
    out["contract_canonical"] = contract.canonical
    out["caps"] = {k: list(v) for k, v in caps.items()}
    t0 = time.perf_counter()
    verdict = kdf.compare_refinement(dataset, budgets, declared)
    out["timing"]["compare_seconds"] = time.perf_counter() - t0
    out["verdict"] = verdict.verdict
    out["reasons"] = list(verdict.reasons)
    out["levels"] = levels_table(verdict)
    checks = out["checks"]
    checks["subset_holds"] = bool(subset)
    checks["both_edges_every_clock"] = all(
        v["rising"] > 0 and v["falling"] > 0 for regime in regimes.values() for v in regime.values())
    checks["gate_pass"] = verdict.verdict == "pass"
    out["procedure_ok"] = checks["subset_holds"] and checks["both_edges_every_clock"]
    log(f"    gate {verdict.verdict}; checks {checks}")
    return out


def levels_table(verdict):
    return [{"observable": lv.observable, "position": lv.position, "unit": lv.unit,
             "timestep": lv.timestep, "measured": lv.measured, "reference": lv.reference,
             "absolute_error": lv.absolute_error, "relative_error": lv.relative_error,
             "standard_error": lv.standard_error, "paired_error": lv.paired_error,
             "span_error": lv.span_error, "clusters": lv.clusters}
            for lv in verdict.levels]


# ---------------------------------------------------------------------------
# The frozen ticket-07 budget (verify.py _t07_budget, rebuilt read-only)
# ---------------------------------------------------------------------------
def frozen_budget():
    from adler_born_two_channel import experiments as xpr
    arms = (("full", 64, 0.10, 0.95, 1.0, 0.05, True),
            ("central_control", 1, 0.02, 0.95, 1.0, 0.10, False),
            ("width_only_control", 64, 0.05, 0.95, 1.0, 0.05, True))
    target = xpr.SamplingTarget(
        exponent_half_width=0.25, minimum_causal_contrast=0.5, coupling_low=0.5,
        coupling_high=2.0, cells=6, pairing_inflation=2.0, conservative_factor=1.25,
        resampling_unit="master_trial", arm_envelopes=tuple(xpr.ArmEnvelope(*e) for e in arms),
        shadow_fraction=0.05, maximum_trials_per_cell=20000)
    power = xpr.power_estimate(target)
    budget = xpr.NumericalBudget(
        label="T07 production numerical budget, tied to planned uncertainty",
        allowed_fraction=xpr.ALLOWED_NUMERICAL_FRACTION, coverage_sigma=xpr.COVERAGE_SIGMA,
        probability_half_width=xpr.CONFIDENCE_Z * math.sqrt(0.25 / power.trials_per_cell),
        time_half_width=0.08, trials_per_cell=power.trials_per_cell,
        reference_probability=0.5, intended_timestep=INTENDED_TIMESTEP)
    assert power.trials_per_cell == 2406, power.trials_per_cell
    assert abs(budget.allowance("probability") - 0.004995) < 5e-7
    assert abs(budget.allowance("time") - 0.021953) < 5e-7
    assert budget.coverage_sigma == COVERAGE_SIGMA
    return budget


def judge_rows(levels, unit, budget_allowance):
    """The stage success rule on the finest-level rows of one unit."""
    finest = min(lv["timestep"] for lv in levels)
    rows = []
    for lv in levels:
        if lv["timestep"] != finest or lv["unit"] != unit or lv["observable"] == "added_resets_mean":
            continue
        bound = abs(lv["absolute_error"]) + COVERAGE_SIGMA * lv["standard_error"]
        rows.append({"observable": lv["observable"], "position": lv["position"], "unit": unit,
                     "timestep": lv["timestep"], "absolute_error": lv["absolute_error"],
                     "standard_error": lv["standard_error"], "bound": bound,
                     "allowance": budget_allowance, "fits": bound <= budget_allowance,
                     "ratio": bound / budget_allowance, "excess": bound - budget_allowance})
    return rows


# ---------------------------------------------------------------------------
# Child: one stage
# ---------------------------------------------------------------------------
def run_stage(short, out_path, allowances, reuse_path=None):
    stage = next(s for s in STAGES if s["short"] == short)
    record = {"short": short, "label": stage["label"], "kind": stage["kind"],
              "unit": stage["unit"], "exit_state": "started", "warnings": [], "pid": os.getpid()}
    lines = []

    def log(text):
        lines.append(f"[{time.strftime('%H:%M:%S')}] {text}")
        print(text, flush=True)

    try:
        fp = P.source_fingerprint()
        record["source_digest"] = fp["digest"]
        t0 = time.perf_counter()
        with P.RssSampler() as sampler, warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            if stage["kind"] == "reference_stationary":
                result = stationary_ladder(REFERENCE_STATIONARY, 1, 1,
                                           "S3 stationary killed-diffusion, frozen endpoint sample",
                                           "S3 stationary killed-diffusion, reference budgets",
                                           "refined", log)
            elif stage["kind"] == "reference_moving":
                result = moving_ladder(REFERENCE_MOVING, 1, 1,
                                       "S3b moving-band audit, pooled frozen sample",
                                       "S3b moving-band audit, pooled reference budgets", log)
            elif stage["kind"] == "stationary":
                mode = "refined" if stage["space_factor"] * STATIONARY_CELL["base_space"] * 2 <= 4800 else "coarsened"
                result = stationary_ladder(STATIONARY_CELL, stage["time_factor"], stage["space_factor"],
                                           f"T07 campaign {short}: intended stationary cell, frozen endpoint sample",
                                           f"T07 campaign {short}: S3 reference budgets at the intended cell",
                                           mode, log)
            elif stage["kind"] == "stationary_time":
                result = json.loads(Path(reuse_path).read_text())["result"]
                result["reused_from"] = "S3"
            elif stage["kind"] == "moving":
                result = moving_ladder(MOVING_CELL, stage["time_factor"], stage["trials_factor"],
                                       f"T07 campaign {short}: intended moving-band pooled frozen sample",
                                       f"T07 campaign {short}: S3b reference budgets at the intended cell", log)
            else:
                raise RuntimeError(f"stage {short} is not launchable")
            record["warnings"] = [f"{w.category.__name__}: {w.message}" for w in caught]
        record["wall_seconds"] = time.perf_counter() - t0
        record["rss_sampled_peak_bytes"] = int(sampler.peak)
        record["ru_maxrss_bytes"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        record["result"] = result
        # --- stage verdict -------------------------------------------------
        unit = stage["unit"]
        if unit is None:
            record["stage_verdict"] = "reference"
            record["rule_rows"] = []
            record["stage_reasons"] = []
        else:
            rows = judge_rows(result["levels"], unit, allowances[unit])
            record["rule_rows"] = rows
            reasons = []
            if result["verdict"] != "pass":
                reasons.append("ladder gate: " + "; ".join(result["reasons"])[:600])
            if not result["procedure_ok"]:
                reasons.append(f"procedure checks failed: {result['checks']}")
            failing = [r for r in rows if not r["fits"]]
            if failing:
                reasons.append(f"{len(failing)} of {len(rows)} {unit} rows exceed the allowance "
                               f"{allowances[unit]:.6g}: " + "; ".join(
                                   f"{r['observable']}@{r['position']} bound {r['bound']:.4g} "
                                   f"({r['ratio']:.1f}x)" for r in failing))
            record["stage_verdict"] = "success" if not reasons else "numerical_no_result"
            record["stage_reasons"] = reasons
        record["exit_state"] = "completed"
    except Exception as exc:                                                   # noqa: BLE001
        import traceback
        record["exit_state"] = f"exception:{type(exc).__name__}"
        record["error"] = "".join(traceback.format_exception(exc))[-4000:]
    finally:
        record["log"] = lines
        record["ru_maxrss_bytes_final"] = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        Path(out_path).write_text(P.canonical_json(record))


# ---------------------------------------------------------------------------
# Parent: preflight, serial execution, incremental observations, disposition
# ---------------------------------------------------------------------------
def pricing_rates():
    obs = json.loads(P.OBSERVATIONS.read_text())
    derived = P.derive(obs)
    rates = {}
    for component, v in derived["components"].items():
        if v["verdict"] != "priced":
            raise RuntimeError(f"pricing component {component} is not priced; no preflight possible")
        for unit, r in v["rates"].items():
            rates[unit] = r["slowest"]
    return rates, derived["derivation_digest"]


def stage_work(stage):
    """Declared work of a stage at the configuration it will actually run."""
    if stage["kind"] in ("reference_stationary", "stationary"):
        cell = REFERENCE_STATIONARY if stage["kind"] == "reference_stationary" else STATIONARY_CELL
        f, s = stage["time_factor"], stage["space_factor"]
        M, N = cell["base_space"] * s, cell["base_time"] * f
        margin = (2 * M) * (2 * N) if 2 * M <= 4800 else (M // 2) * (N // 2)
        fine = cell["base_fine_steps"] * f
        return {"space_time_cells": M * N + margin,
                "endpoint_observations": cell["walkers"] * 3 * sum(fine // st for st in cell["strides"]),
                "resample_observations": cell["resamples"] * cell["walkers"] * 12 * 3}
    if stage["kind"] == "stationary_time":
        return {}
    if stage["kind"] in ("reference_moving", "moving"):
        cell = REFERENCE_MOVING if stage["kind"] == "reference_moving" else MOVING_CELL
        step = cell["base_step"] / stage["time_factor"]
        steps = cell["base_steps"] * stage["time_factor"]
        trials = int(cell["base_trials"] * stage["trials_factor"])
        phys, elig = count_moving_intervals(cell, step, steps)
        return {"physical_intervals": phys * trials,
                "audited_evaluations": elig * trials * cell["replicates"],
                "resample_observations": cell["resamples"] * trials * 6 * 3}
    return {}


def preflight_seconds(work, rates):
    seconds = 0.0
    for unit, amount in work.items():
        if unit == "audited_evaluations":
            continue                     # collapsed onto the physical counter (priced so)
        seconds += rates[unit] * amount
    return seconds * PRICE_CONTINGENCY


def run_child(short, out_path, allowances, reuse_path, deadline, log):
    import psutil
    cmd = [sys.executable, str(Path(__file__).resolve()), "--stage", short, "--out", str(out_path),
           "--allowances", json.dumps(allowances)]
    if reuse_path:
        cmd += ["--reuse", str(reuse_path)]
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
        record = {"short": short, "exit_state": ceiling or f"exception:child_rc_{child.returncode}",
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


def session():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    t_session = time.perf_counter()
    log_lines = []

    def log(text):
        line = f"[{time.perf_counter() - t_session:7.1f}s] {text}"
        log_lines.append(line)
        print(line, flush=True)

    log("validation campaign session start")
    identity = P.machine_identity()
    env_digest = P.environment_fingerprint(identity)
    fp = P.source_fingerprint()
    budget = frozen_budget()
    allowances = {"probability": budget.allowance("probability"), "time": budget.allowance("time"),
                  "count": budget.allowance("count")}
    rates, pricing_digest = pricing_rates()
    results_sha_start = P.results_sha_snapshot(RESULTS)
    results_stat_start = P.results_stat_snapshot(RESULTS)
    package_stat_start = P.package_stat_digest()
    log(f"source {fp['digest'][:16]} env {env_digest[:16]} budget {budget.digest[:16]} "
        f"allowances {allowances}; pricing derivation {pricing_digest[:16]}")
    observations = {
        "schema": "validation-campaign-observations/v1",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "repo_git_head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(REPO),
                                        capture_output=True, text=True).stdout.strip(),
        "machine": identity, "environment_digest": env_digest, "source_fingerprint": fp,
        "pricing_derivation_digest": pricing_digest, "pricing_rates": rates,
        "constraints": {"wall_budget_seconds": WALL_BUDGET_S, "rss_ceiling_bytes": RSS_CEILING_BYTES,
                        "price_contingency": PRICE_CONTINGENCY},
        "intended": INTENDED, "stationary_cell": STATIONARY_CELL, "moving_cell": MOVING_CELL,
        "moving_clocks": [list(c) for c in MOVING_CLOCKS],
        "budget": {"digest": budget.digest, "allowances": allowances,
                   "trials_per_cell": budget.trials_per_cell,
                   "coverage_sigma": budget.coverage_sigma,
                   "intended_timestep": budget.intended_timestep,
                   "probability_half_width": budget.probability_half_width,
                   "time_half_width": budget.time_half_width},
        "stages_plan": STAGES, "order": ORDER, "rules": RULES, "interpretations": INTERPRETATIONS,
        "results_snapshot": {"entries": len(results_stat_start), "sha_start": results_sha_start,
                             "package_stat_start": package_stat_start},
        "stages": {}, "events": [],
    }

    def flush():
        observations["log"] = log_lines
        observations["session_wall_seconds"] = time.perf_counter() - t_session
        OBSERVATIONS.write_text(json.dumps(observations, indent=1, sort_keys=True,
                                           default=P._json_default))

    flush()
    deadline = t_session + WALL_BUDGET_S
    verdicts = {}
    try:
        for short in ORDER:
            stage = next(s for s in STAGES if s["short"] == short)
            rec = {"short": short, "label": stage["label"], "kind": stage["kind"], "unit": stage["unit"]}
            if stage["kind"] == "not_launched":
                rec["exit_state"] = "not_launched"
                rec["stage_verdict"] = "not_launched"
                rec["stage_reasons"] = ["pricing_unresolved in the pricing session: replay work 128x and "
                                        "comparison work 17.1x beyond the largest measured points (16x limit)"]
                observations["stages"][short] = rec
                observations["events"].append(f"{short}: not launched (pricing_unresolved)")
                flush()
                continue
            dep = stage.get("depends_on")
            if dep and verdicts.get(dep) != "success":
                rec["exit_state"] = "stopped:dependency"
                rec["stage_verdict"] = "not_run"
                rec["stage_reasons"] = [f"stop rule: predecessor {dep} returned "
                                        f"{verdicts.get(dep, 'nothing')}; a later stage never runs on an "
                                        f"unresolved one"]
                observations["stages"][short] = rec
                observations["events"].append(f"{short}: stopped by dependency on {dep} "
                                              f"({verdicts.get(dep)})")
                log(f"{short}: stopped — predecessor {dep} = {verdicts.get(dep)}")
                flush()
                continue
            work = stage_work(stage)
            predicted = preflight_seconds(work, rates)
            elapsed = time.perf_counter() - t_session
            rec["work"] = work
            rec["preflight_predicted_seconds"] = predicted
            rec["elapsed_at_preflight"] = elapsed
            log(f"{short}: preflight {predicted:.0f}s predicted; elapsed {elapsed:.0f}s; "
                f"budget remaining {WALL_BUDGET_S - elapsed:.0f}s; work {work}")
            if elapsed + predicted > WALL_BUDGET_S:
                rec["exit_state"] = "skipped:preflight"
                rec["stage_verdict"] = "not_run"
                rec["stage_reasons"] = [f"preflight {predicted:.0f}s would exceed the remaining "
                                        f"{WALL_BUDGET_S - elapsed:.0f}s of the 2-hour budget"]
                observations["stages"][short] = rec
                observations["events"].append(f"{short}: skipped by preflight")
                verdicts[short] = "not_run"
                flush()
                continue
            before = P.results_stat_snapshot(RESULTS)
            out_path = SCRATCH / f"{short}.json"
            reuse = (SCRATCH / "S3.json") if stage["kind"] == "stationary_time" else None
            try:
                child = run_child(short, out_path, allowances, reuse, deadline, log)
            finally:
                if out_path.exists() and stage["kind"] != "stationary":
                    out_path.unlink()
            after = P.results_stat_snapshot(RESULTS)
            child["results_unchanged"] = (before == after and before == results_stat_start)
            rec.update(child)
            if not rec["results_unchanged"]:
                rec["exit_state"] = "precondition:results_changed"
            if rec["exit_state"] != "completed":
                rec["stage_verdict"] = "not_completed"
                rec.setdefault("stage_reasons", []).append(rec["exit_state"])
                observations["events"].append(f"{short}: {rec['exit_state']}")
            verdicts[short] = rec.get("stage_verdict")
            observations["stages"][short] = rec
            log(f"{short}: {rec['exit_state']} verdict={rec.get('stage_verdict')} "
                f"wall={rec.get('child_wall_seconds', 0):.0f}s rss={rec.get('ru_maxrss_bytes', 0) / 2**20:.0f}MiB "
                f"reasons={rec.get('stage_reasons')}")
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
# Disposition (experiments.numerical_disposition, read-only)
# ---------------------------------------------------------------------------
def evidence_rows(observations):
    from adler_born_two_channel import experiments as xpr
    rows = {"reference": [], "intended": []}
    descriptions = {
        "REF_S3": ("stationary_oracle", "non_intended", "the ticket-04 S3 stationary reference cell: one fixed coupling, one fixed band, three declared starts, no pulse and no population"),
        "REF_S3B": ("moving_band_audit", "non_intended", "the ticket-04 S3b reduced moving-band matrix, pooled over three independently keyed clocks at the finest declared step"),
    }
    for short, rec in observations["stages"].items():
        if rec.get("exit_state") != "completed":
            continue
        result = rec["result"]
        if short in descriptions:
            source, configuration, description = descriptions[short]
            bucket = "reference"
        else:
            kind = rec["kind"]
            source = "stationary_oracle" if kind.startswith("stationary") else "moving_band_audit"
            configuration = "intended"
            description = (f"T07 campaign stage {short} ({rec['label']}) at the intended configuration: "
                           + (f"coupling {STATIONARY_CELL['coupling']}, detuning {STATIONARY_CELL['detuning']:.6f}, "
                              f"tolerance {STATIONARY_CELL['tolerance']}, diffusion {STATIONARY_CELL['diffusion']}, "
                              f"oracle grid {result['oracle_grid']}, {result['fine_steps']} fine steps"
                              if source == "stationary_oracle" else
                              f"pulse {MOVING_CELL['duration']} at peak {MOVING_CELL['peak']}, diffusion "
                              f"{MOVING_CELL['diffusion']}, tolerance {MOVING_CELL['tolerance']}, dwell "
                              f"{MOVING_CELL['dwell']}, {result['trials']} master trials, finest step {result['step']:.6g}"))[:300]
            bucket = "intended"
        if short == "S4":
            continue                      # S4 judges S3's ladder; its rows are S3's rows
        clusters = result["cell"]["walkers"] if source == "stationary_oracle" else result["trials"]
        finest = min(lv["timestep"] for lv in result["levels"])
        for lv in result["levels"]:
            if lv["timestep"] != finest or lv["observable"] == "added_resets_mean":
                continue
            rows[bucket].append(xpr.NumericalEvidence(
                source=source, observable=lv["observable"], unit=lv["unit"], position=lv["position"],
                timestep=lv["timestep"], measured=lv["absolute_error"], standard_error=lv["standard_error"],
                sample_clusters=clusters, verdict=result["verdict"], configuration=configuration,
                description=description))
    return rows


def dispositions(observations):
    from adler_born_two_channel import experiments as xpr
    budget = frozen_budget()
    rows = evidence_rows(observations)
    out = {"budget_digest": budget.digest, "sets": {}}
    for name, items in (("reference_only", rows["reference"]),
                        ("reference_plus_intended", rows["reference"] + rows["intended"]),
                        ("intended_only", rows["intended"])):
        d = xpr.numerical_disposition(budget, items)
        table = [{"source": r[0], "observable": r[1], "position": r[2], "unit": r[3], "bound": r[4],
                  "allowance": r[5], "fits": bool(r[6]), "ratio": r[4] / r[5] if r[5] else None,
                  "excess": r[4] - r[5]} for r in d.rows]
        out["sets"][name] = {
            "rows_in": len(items), "verdict": d.verdict, "blockers": list(d.blockers),
            "probability_admissible_trials": d.probability_admissible_trials,
            "time_admissible": d.time_admissible, "admissible_trials": d.admissible_trials,
            "limiting": {unit: (list(d.limiting(unit)) if d.limiting(unit) else None)
                         for unit in ("probability", "time", "count")},
            "rows": table, "evidence_digest": d.evidence_digest, "disposition_digest": d.digest,
            "configurations": sorted({i.configuration for i in items})}
    return out


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def _hms(s):
    if s is None:
        return "—"
    return f"{s:.1f} s" if s < 120 else f"{s:.0f} s ({s / 60:.1f} min)"


def write_report(observations):
    m = observations["machine"]
    L = ["# Intended-configuration validation campaign — report\n",
         "**Nothing here is a physical finding, an approval, or a sufficiency promise.**  Every stage keeps "
         "its predeclared success, `numerical_no_result`, dependency and stop rules; a stage that misses its "
         "target is a numerical no-result, never a reason to widen a budget.  M7 was not launched "
         "(`pricing_unresolved`).\n",
         f"Session {observations['started_at']} → {observations.get('finished_at')}, wall "
         f"{_hms(observations.get('session_wall_seconds'))} of the {WALL_BUDGET_S:.0f} s budget; per-process "
         f"RSS ceiling {RSS_CEILING_BYTES / 2**30:.0f} GiB.\n",
         "## Environment identity\n", "| Field | Value |\n| --- | --- |"]
    for key in ("platform", "cpu_brand", "physical_cpus", "memory_bytes", "os_version", "python_version",
                "numpy_version", "numpy_blas"):
        L.append(f"| {key} | `{m.get(key, '')}` |")
    L += [f"| environment digest | `{observations['environment_digest']}` |",
          f"| package source fingerprint | `{observations['source_fingerprint']['digest']}` |",
          f"| repo git HEAD | `{observations['repo_git_head']}` |",
          f"| frozen ticket-07 budget digest | `{observations['budget']['digest']}` (trials/cell "
          f"{observations['budget']['trials_per_cell']}, allowances {observations['budget']['allowances']}) |",
          f"| pricing derivation used for preflight | `{observations['pricing_derivation_digest']}` |", ""]
    snap = observations["results_snapshot"]
    L += ["## Tree integrity\n",
          f"- `results/` ({snap['entries']} entries) unchanged by SHA-256 snapshot = **{snap.get('results_unchanged')}**; "
          f"package tree (incl. `__pycache__`) unchanged = **{snap.get('package_unchanged')}**.",
          "- One child process at a time; the parent polled its RSS every 50 ms.  No verifier run, no pilot, "
          "production, sensitivity or exponent fit, no exponent output opened.\n"]
    if observations.get("events"):
        L += ["### Events\n"] + [f"- {e}" for e in observations["events"]] + [""]
    L += ["## Intended configuration and cells\n",
          f"- Production physics (verify.py `_t07_config`/`_t07_matrix`): {json.dumps(observations['intended'], sort_keys=True)}",
          f"- Stationary cell: {json.dumps(observations['stationary_cell'], sort_keys=True)}",
          f"- Moving cell: {json.dumps(observations['moving_cell'], sort_keys=True)}",
          f"- Moving clocks (grid index, detuning, regime): {observations['moving_clocks']}\n",
          "## Stages\n",
          "| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for short in observations["order"]:
        rec = observations["stages"].get(short, {})
        res = rec.get("result", {})
        if rec.get("exit_state") == "completed":
            if "oracle_grid" in res:
                cfg = (f"oracle {res['oracle_grid']}, fine steps {res['fine_steps']}, timesteps "
                       f"{[f'{t:.3g}' for t in res['timesteps']]}, walkers {res['cell']['walkers']}")
            else:
                cfg = (f"{res['trials']} trials x 3 clocks x 4 replicates, mesh step {res['step']:.3g}, "
                       f"{res['steps']} steps, timesteps {[f'{t:.3g}' for t in res['timesteps']]}")
            rows = rec.get("rule_rows", [])
            fitting = sum(1 for r in rows if r["fits"])
            rulecell = f"{fitting}/{len(rows)} fit ({rec.get('unit')})" if rows else "—"
            L.append(f"| **{short}** {rec['label']} | {rec['exit_state']} | {cfg} | {res['verdict']} | "
                     f"{'ok' if res.get('procedure_ok') else 'FAIL'} {json.dumps(res.get('checks'), sort_keys=True)} | {rulecell} | "
                     f"**{rec.get('stage_verdict')}** | {_hms(rec.get('child_wall_seconds'))} | "
                     f"{rec.get('ru_maxrss_bytes', 0) / 2**20:.0f} MiB |")
        else:
            L.append(f"| **{short}** {rec.get('label', '')} | {rec.get('exit_state', '—')} | — | — | — | — | "
                     f"**{rec.get('stage_verdict', '—')}** | — | — |")
    L.append("")
    for short in observations["order"]:
        rec = observations["stages"].get(short, {})
        L.append(f"### {short} — {rec.get('label', '')}\n")
        L.append(f"- State `{rec.get('exit_state')}`, stage verdict **{rec.get('stage_verdict')}**.")
        for r in rec.get("stage_reasons", []):
            L.append(f"- Reason: {r}")
        if rec.get("exit_state") != "completed":
            L.append("")
            continue
        res = rec["result"]
        L.append(f"- Rules applied: {RULES['gate'][:120]}…; stage rule: "
                 + RULES["stage_success"].format(unit=rec["unit"] or "-", allowance=(
                     observations["budget"]["allowances"].get(rec["unit"] or "probability")))
                 + f"; {RULES['stage_no_result']}")
        L.append(f"- Ladder gate verdict **{res['verdict']}**" + (f"; reasons: {res['reasons']}" if res["reasons"] else "")
                 + f".  Procedure checks: {json.dumps(res['checks'], sort_keys=True)}" + (f"; oracle gap {res['oracle_gap']:.3e} "
                 f"({res['oracle_margin_mode']} grid {res['oracle_margin_grid']}), smallest finest error "
                 f"{res['smallest_finest_error']:.3e}" if "oracle_gap" in res else "")
                 + f".  Dataset digest `{res['dataset_digest'][:16]}…`, budgets digest `{res['budgets_digest'][:16]}…`.")
        if "work" in rec:
            L.append(f"- Work {json.dumps(rec['work'], sort_keys=True)}; preflight {_hms(rec.get('preflight_predicted_seconds'))}; "
                     f"actual {_hms(rec.get('child_wall_seconds'))}; timing {json.dumps(res.get('timing'), sort_keys=True)}; "
                     f"peak RSS {rec.get('ru_maxrss_bytes', 0) / 2**20:.0f} MiB (parent-observed "
                     f"{rec.get('parent_observed_rss_peak_bytes', 0) / 2**20:.0f} MiB); warnings {len(rec.get('warnings', []))}.")
        L += ["", "| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for lv in res["levels"]:
            L.append(f"| {lv['observable']} | {lv['position']} | {lv['timestep']:.4g} | {lv['measured']:.5f} | "
                     f"{lv['reference']:.5f} | {lv['absolute_error']:.5f} | {lv['standard_error']:.5f} | "
                     f"{lv['paired_error']:.5f} | {lv['span_error']:.5f} |")
        if rec.get("rule_rows"):
            L += ["", f"Stage rule rows ({rec['unit']}, finest level; bound = |error| + 2 SE vs allowance "
                      f"{rec['rule_rows'][0]['allowance']:.6g}):", "",
                  "| Observable | Position | |error| | SE | bound | ratio to allowance | fits |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
            for r in rec["rule_rows"]:
                L.append(f"| {r['observable']} | {r['position']} | {r['absolute_error']:.5f} | {r['standard_error']:.5f} | "
                         f"{r['bound']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
        L.append("")
    d = observations.get("disposition")
    if d:
        L += ["## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)\n",
              RULES["disposition"], ""]
        for name, s in d["sets"].items():
            L += [f"### Evidence set `{name}` ({s['rows_in']} rows; configurations {s['configurations']})\n",
                  f"- Verdict **{s['verdict']}**; blockers {s['blockers']}; probability-admissible trials "
                  f"{s['probability_admissible_trials']} (needs {observations['budget']['trials_per_cell']}); "
                  f"time admissible {s['time_admissible']}; overall admissible trials {s['admissible_trials']}.",
                  f"- Limiting rows: {json.dumps(s['limiting'], sort_keys=True)}", "",
                  "| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- |"]
            for r in sorted(s["rows"], key=lambda r: -r["ratio"]):
                L.append(f"| {r['source']} | {r['observable']} | {r['position']} | {r['unit']} | {r['bound']:.5f} | "
                         f"{r['allowance']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
            L.append("")
    L += ["## Rules quoted\n"] + [f"- **{k}**: {v}" for k, v in RULES.items()] + [""]
    L += ["## Ambiguities and choices\n"] + [f"{i}. **{t}.** {x}" for i, (t, x) in enumerate(observations["interpretations"], 1)] + [""]
    L += ["## Reproduce\n", "```", f"cd {REPO}",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_validation_campaign.py --run",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_validation_campaign.py --derive-only",
          "```", "", "## Session log\n", "```"] + observations.get("log", []) + ["```"]
    REPORT.write_text("\n".join(L) + "\n")


# ---------------------------------------------------------------------------
def selftest():
    def log(t):
        print("  " + t)
    tiny = dict(STATIONARY_CELL, walkers=300, chunk=150, base_fine_steps=1024, base_space=120, base_time=120,
                namespace="t07-selftest-stationary")
    r = stationary_ladder(tiny, 1, 1, "selftest", "selftest budgets", "refined", log)
    print("stationary selftest:", r["verdict"], r["checks"], "timesteps", r["timesteps"])
    print("  rule rows:", [(x["observable"], round(x["bound"], 4), x["fits"]) for x in
                           judge_rows(r["levels"], "probability", 0.004995)][:3])
    tinym = dict(MOVING_CELL, base_trials=3, base_steps=256, base_step=INTENDED["pulse_duration"] / 256,
                 physical_namespace="t07-selftest-physical", audit_namespace="t07-selftest-auxiliary")
    r = moving_ladder(tinym, 1, 1, "selftest moving", "selftest moving budgets", log)
    print("moving selftest:", r["verdict"], r["checks"], "counters", r["physical_intervals"], r["audited_evaluations"])
    b = frozen_budget()
    print("frozen budget ok:", b.trials_per_cell, b.allowance("probability"), b.allowance("time"))
    rates, dg = pricing_rates()
    for s in STAGES:
        if s["kind"] in ("not_launched",):
            continue
        w = stage_work(s)
        print(f"  {s['short']}: work {w} -> preflight {preflight_seconds(w, rates):.0f}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--derive-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--stage")
    ap.add_argument("--out")
    ap.add_argument("--allowances")
    ap.add_argument("--reuse")
    args = ap.parse_args()
    if args.stage:
        run_stage(args.stage, args.out, json.loads(args.allowances), args.reuse)
    elif args.selftest:
        selftest()
    elif args.derive_only:
        observations = json.loads(OBSERVATIONS.read_text())
        observations["disposition"] = dispositions(observations)
        write_report(observations)
        print(json.dumps({k: (v["verdict"], v["blockers"]) for k, v in observations["disposition"]["sets"].items()}, indent=1))
    elif args.run:
        session()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
