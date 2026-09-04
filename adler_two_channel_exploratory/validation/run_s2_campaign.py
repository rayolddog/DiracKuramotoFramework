#!/usr/bin/env python3
"""
run_s2_campaign.py — second sponsor's override: run S2 (stationary probability,
dt/64 at quadrupled space) at 96,000 walkers despite S1's numerical_no_result;
if S2 succeeds under the frozen stage rules continue to S3 (dt/256 at eightfold
space) and S4 (time quantile at dt/256) under the frozen dependency rules with
no further override; if S2 returns numerical_no_result, stop and report every
row's bound against the allowance and the package's own projected_bound at
dt/256.

Reuses run_redesign_campaign.py's child phases (oracle phase, construction
phase), priced preflight (including the O(walkers^2) identity check measured
at 96,000 walkers in the redesign session), RSS-guarded serial children and
report shape.  New files only: observations_s2.json and S2_REPORT.md.

Modes:  --run | --derive-only | --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PKG = REPO / "adler_born_two_channel"
RESULTS = PKG / "results"
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "adler_two_channel_exploratory" / "pricing"))
sys.path.insert(0, str(HERE))
import price_validation_campaign as P                                  # noqa: E402
import run_validation_campaign as V                                    # noqa: E402
import run_redesign_campaign as R                                      # noqa: E402

OBSERVATIONS = HERE / "observations_s2.json"
PREVIOUS = HERE / "observations.json"                 # M5 rows (read-only)
REDESIGN = HERE / "observations_redesign.json"        # S1@96k and M6 rows, 96k quadratic seconds (read-only)
REPORT = HERE / "S2_REPORT.md"
SCRATCH = Path(os.environ.get(
    "S2_SCRATCH",
    "/private/tmp/claude-501/-Users-john-bramble-Projects-Physics-DiracKuramotoFramework/"
    "63b0fc51-d326-44ba-9e7c-eccecb8f1e8f/scratchpad")) / "s2_stages"

WALL_BUDGET_S = 3 * 3600.0
RSS_CEILING_BYTES = 2 * 1024 ** 3
WALKERS = 96000

STAGES = {
    "S2": dict(kind="stationary", label="stationary probability, dt/64 at quadrupled space (96,000 walkers; S1 stop rule overridden by the sponsor)", unit="probability", time_factor=64, space_factor=4, depends_on=None, overridden_predecessor="S1"),
    "S3": dict(kind="stationary", label="stationary probability, dt/256 at eightfold space (96,000 walkers)", unit="probability", time_factor=256, space_factor=8, depends_on="S2"),
    "S4": dict(kind="stationary_time", label="stationary time quantile, dt/256 at eightfold space (96,000 walkers)", unit="time", time_factor=256, space_factor=8, depends_on="S3"),
}
ORDER = ["S2", "S3", "S4"]

INTERPRETATIONS = R.INTERPRETATIONS + [
    ("second override", "S2 runs although its predecessor S1 (96,000 walkers, redesign session) returned numerical_no_result, by the second sponsor's override; the frozen stop rule is quoted and the override stated.  S3 and S4 keep the frozen dependency rule with no further override."),
    ("walker count", "96,000 walkers, the count chosen by the redesign session's memory-scaling measurement (construction-phase peak 273 MiB measured there); no new probe.  The O(walkers^2) identity-check seconds measured at 96,000 walkers in that session (1545 s per stationary stage) enter the preflight directly."),
    ("oracle margin grids", "S2: refined grid 4800 x 76800 (1,589 MiB in the pricing session, under the 2 GiB cap, in its own oracle child).  S3/S4: the refined grid 9600 x 307200 would exceed the cap, so the COARSER grid 2400 x 76800 is differenced, which overstates the oracle's own error by about 3x for a second-order scheme (the conservative direction)."),
    ("projected bounds", "For every S2 row the package's own NumericalEvidence.projected_bound(coverage_sigma=2, timestep_factor, sample_factor=1) is reported at dt/128 (factor 0.5) and dt/256 (factor 0.25): bias x sqrt(factor) + 2 SE.  These are planning projections by the package's stated rule (bias falls like sqrt(dt)), not evidence; they are also computed from the redesign S1 rows to dt/64 beside the measured S2 rows, so the rule's accuracy on this cell is visible."),
    ("disposition sets", "Per the dependency chain the finest completed stationary stage supersedes its predecessors (S2 replaces S1; S3 would replace S2); M5's rows (first session) and M6's rows (redesign session) are kept.  Sets: new stationary rows only; all intended rows (new stationary + M5 + M6); the 17 reference rows plus all intended rows."),
]


def _hms(s):
    return R._hms(s)


def _mib(b):
    return R._mib(b)


def session():
    from adler_born_two_channel import experiments as xpr                     # noqa: F401
    SCRATCH.mkdir(parents=True, exist_ok=True)
    t_session = time.perf_counter()
    log_lines = []

    def log(text):
        line = f"[{time.perf_counter() - t_session:7.1f}s] {text}"
        log_lines.append(line)
        print(line, flush=True)

    log("S2 override session start")
    identity = P.machine_identity()
    env_digest = P.environment_fingerprint(identity)
    fp = P.source_fingerprint()
    budget = V.frozen_budget()
    allowances = {"probability": budget.allowance("probability"), "time": budget.allowance("time"),
                  "count": budget.allowance("count")}
    rates, pricing_digest = V.pricing_rates()
    redesign = json.loads(REDESIGN.read_text())
    s1 = redesign["stages"]["S1"]
    quad_probe = {"walkers": s1["result"]["walkers"], "quadratic_seconds": s1["result"]["quadratic_seconds"]}
    results_sha_start = P.results_sha_snapshot(RESULTS)
    results_stat_start = P.results_stat_snapshot(RESULTS)
    package_stat_start = P.package_stat_digest()
    observations = {
        "schema": "validation-campaign-s2-override-observations/v1",
        "started_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "repo_git_head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(REPO), capture_output=True,
                                        text=True).stdout.strip(),
        "machine": identity, "environment_digest": env_digest, "source_fingerprint": fp,
        "pricing_derivation_digest": pricing_digest, "pricing_rates": rates,
        "previous_session": {"path": str(REDESIGN.relative_to(REPO)), "started_at": redesign["started_at"],
                             "sha256": hashlib.sha256(REDESIGN.read_bytes()).hexdigest(),
                             "first_session_sha256": hashlib.sha256(PREVIOUS.read_bytes()).hexdigest()},
        "constraints": {"wall_budget_seconds": WALL_BUDGET_S, "rss_ceiling_bytes": RSS_CEILING_BYTES,
                        "price_contingency": R.PRICE_CONTINGENCY, "walkers": WALKERS},
        "quadratic_probe": quad_probe,
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

    def launch(kind, name, args):
        before = P.results_stat_snapshot(RESULTS)
        out_path = SCRATCH / f"{name}.json"
        rec = R.run_child(kind, out_path, args, deadline, log)
        after = P.results_stat_snapshot(RESULTS)
        rec["results_unchanged"] = (before == after and before == results_stat_start)
        if not rec["results_unchanged"]:
            rec["exit_state"] = "precondition:results_changed"
        return rec, out_path

    try:
        for short in ORDER:
            stage = STAGES[short]
            rec = {"short": short, "label": stage["label"], "kind": stage["kind"], "unit": stage["unit"],
                   "walkers": WALKERS}
            dep = stage.get("depends_on")
            if dep and verdicts.get(dep) != "success":
                rec.update(exit_state="stopped:dependency", stage_verdict="not_run",
                           stage_reasons=[f"stop rule: predecessor {dep} returned {verdicts.get(dep, 'nothing')}"])
                observations["stages"][short] = rec
                observations["events"].append(f"{short}: stopped by dependency on {dep} ({verdicts.get(dep)})")
                log(f"{short}: stopped — predecessor {dep} = {verdicts.get(dep)}")
                flush()
                continue
            if stage.get("overridden_predecessor"):
                rec["override"] = (f"predecessor {stage['overridden_predecessor']} returned numerical_no_result "
                                   f"(redesign session); stop rule overridden by the sponsor")
            if stage["kind"] == "stationary":
                elapsed = time.perf_counter() - t_session
                pf = R.preflight_stationary(stage, WALKERS, rates, quad_probe)
                rec["preflight"] = pf
                log(f"{short}: preflight {pf['predicted_seconds']:.0f}s (linear {pf['linear_seconds']:.0f}s + quadratic "
                    f"{pf['quadratic_seconds_extrapolated']:.0f}s, x1.5); elapsed {elapsed:.0f}s; remaining "
                    f"{WALL_BUDGET_S - elapsed:.0f}s; work {json.dumps(pf['work'], sort_keys=True)}")
                if elapsed + pf["predicted_seconds"] > WALL_BUDGET_S:
                    rec.update(exit_state="skipped:preflight", stage_verdict="not_run",
                               stage_reasons=[f"preflight {pf['predicted_seconds']:.0f}s (of which the O(walkers^2) "
                                              f"identity check {pf['quadratic_seconds_extrapolated']:.0f}s) exceeds the "
                                              f"remaining {WALL_BUDGET_S - elapsed:.0f}s of the 3-hour budget"])
                    observations["stages"][short] = rec
                    observations["events"].append(f"{short}: skipped by preflight")
                    verdicts[short] = "not_run"
                    flush()
                    continue
                oracle_rec, oracle_path = launch("oracle", f"{short}-oracle",
                                                 {"time_factor": stage["time_factor"], "space_factor": stage["space_factor"]})
                rec["oracle"] = {k: v for k, v in oracle_rec.items() if k != "result"}
                rec["oracle"]["result"] = {k: v for k, v in oracle_rec.get("result", {}).items() if k != "reference"}
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
                cons_rec, cons_path = launch("construction", f"{short}-construction", {
                    "time_factor": stage["time_factor"], "walkers": WALKERS, "oracle_path": str(oracle_path),
                    "dataset_label": f"T07 S2-override {short}: intended stationary cell, {WALKERS} walkers, frozen endpoint sample",
                    "budgets_label": f"T07 S2-override {short}: S3 reference budgets at the intended cell"})
                oracle_path.unlink(missing_ok=True)
                cons_path.unlink(missing_ok=True)
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
                                           f"{r['observable']}@{r['position']} bound {r['bound']:.4g} ({r['ratio']:.2f}x)"
                                           for r in failing))
                    rec["stage_verdict"] = "success" if not reasons else "numerical_no_result"
                    rec["stage_reasons"] = reasons
                    rec["two_se_rows"] = [{"observable": r["observable"], "position": r["position"],
                                           "two_se": 2 * r["standard_error"],
                                           "two_se_fits": 2 * r["standard_error"] <= allowances["probability"]}
                                          for r in rows]
                else:
                    rec.update(stage_verdict="not_completed", stage_reasons=[cons_rec["exit_state"]])
                    observations["events"].append(f"{short}: {cons_rec['exit_state']}")
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
                                       f"{r['observable']}@{r['position']} bound {r['bound']:.4g} ({r['ratio']:.2f}x)"
                                       for r in failing))
                rec.update(exit_state="completed", result={**res, "reused_from": "S3"}, rule_rows=rows,
                           stage_verdict="success" if not reasons else "numerical_no_result",
                           stage_reasons=reasons, child_wall_seconds=0.0, ru_maxrss_bytes=0)
            verdicts[short] = rec.get("stage_verdict")
            observations["stages"][short] = rec
            log(f"{short}: {rec.get('exit_state')} verdict={rec.get('stage_verdict')} wall="
                f"{rec.get('child_wall_seconds', 0):.0f}s rss={rec.get('ru_maxrss_bytes', 0) / 2**20:.0f}MiB "
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
    observations["projections"] = projections(observations)
    observations["disposition"] = dispositions(observations)
    flush()
    write_report(observations)
    print(f"wrote {OBSERVATIONS} and {REPORT}")


# ---------------------------------------------------------------------------
# Projections (the package's own NumericalEvidence.projected_bound)
# ---------------------------------------------------------------------------
def _stationary_rows(short, rec, budget_allowances):
    desc = (f"T07 override stage {short} at the intended configuration: {rec['result']['walkers']} walkers, oracle grid "
            f"{rec['result']['oracle_grid']}, {rec['result']['fine_steps']} fine steps")
    return R.rows_from(short, rec, "intended", desc, "stationary_oracle")


def projections(observations):
    out = {"rule": "NumericalEvidence.projected_bound(2.0, timestep_factor, sample_factor=1): |measured| * sqrt(factor) + 2 SE",
           "sets": {}}
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    redesign = json.loads(REDESIGN.read_text())
    sources = [("S1_redesign_96k", redesign["stages"]["S1"], {"to dt/64": 0.25, "to dt/256": 1 / 16})]
    for short in ("S2", "S3"):
        rec = observations["stages"].get(short, {})
        if rec.get("exit_state") == "completed" and "result" in rec:
            factors = {"to dt/128": 0.5, "to dt/256": 0.25} if short == "S2" else {}
            sources.append((short, rec, factors))
    for name, rec, factors in sources:
        rows = []
        for ev in _stationary_rows(name.split("_")[0], rec, allow):
            entry = {"observable": ev.observable, "position": ev.position, "unit": ev.unit, "timestep": ev.timestep,
                     "measured": ev.measured, "standard_error": ev.standard_error,
                     "bound": ev.bound_at(2.0), "allowance": allow[ev.unit],
                     "ratio": ev.bound_at(2.0) / allow[ev.unit], "fits": ev.bound_at(2.0) <= allow[ev.unit],
                     "projected": {}}
            for label, factor in factors.items():
                pb = ev.projected_bound(2.0, timestep_factor=factor, sample_factor=1.0)
                entry["projected"][label] = {"factor": factor, "bound": pb, "ratio": pb / allow[ev.unit],
                                             "fits": pb <= allow[ev.unit]}
            rows.append(entry)
        out["sets"][name] = rows
    return out


# ---------------------------------------------------------------------------
# Disposition
# ---------------------------------------------------------------------------
def dispositions(observations):
    from adler_born_two_channel import experiments as xpr
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    first = json.loads(PREVIOUS.read_text())
    redesign = json.loads(REDESIGN.read_text())
    prev_rows = V.evidence_rows(first)
    reference = prev_rows["reference"]
    m5 = [r for r in prev_rows["intended"] if r.source == "moving_band_audit"]
    m6 = R.rows_from("M6", redesign["stages"]["M6"], "intended",
                     "T07 redesign stage M6 at the intended configuration: dt/16 replay, 40 master trials on the 2^-13 mesh, "
                     "three regime clocks, four replicates", "moving_band_audit")
    finest = None
    for short in ("S3", "S2"):
        rec = observations["stages"].get(short, {})
        if rec.get("exit_state") == "completed" and "result" in rec:
            finest = short
            break
    new_stationary = _stationary_rows(finest, observations["stages"][finest], allow) if finest else []
    out = {"budget_digest": budget.digest, "superseding_stationary_stage": finest, "sets": {}}
    for name, items in (("new_stationary_only", new_stationary),
                        ("intended_all_kept_M5_M6", new_stationary + m5 + m6),
                        ("reference_plus_intended_all", reference + new_stationary + m5 + m6)):
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
# Report (same structure as REDESIGN_REPORT.md, plus the projection table)
# ---------------------------------------------------------------------------
def write_report(o):
    m = o["machine"]
    L = ["# S2 override — intended-configuration validation campaign report\n",
         "**Nothing here is a physical finding, an approval, or a sufficiency promise.**  The second sponsor's override "
         "authorized S2 despite S1's `numerical_no_result`; S3 and S4 kept the frozen dependency rule with no further "
         "override.  Every other rule stays frozen.\n",
         f"Session {o['started_at']} → {o.get('finished_at')}, wall {_hms(o.get('session_wall_seconds'))} of the "
         f"{WALL_BUDGET_S:.0f} s budget; per-process RSS ceiling 2 GiB; previous records "
         f"`{o['previous_session']['path']}` (sha256 `{o['previous_session']['sha256'][:16]}…`) and the first session "
         f"(`{o['previous_session']['first_session_sha256'][:16]}…`) untouched.\n",
         "## Environment identity\n", "| Field | Value |\n| --- | --- |"]
    for key in ("platform", "cpu_brand", "physical_cpus", "memory_bytes", "os_version", "python_version",
                "numpy_version", "numpy_blas"):
        L.append(f"| {key} | `{m.get(key, '')}` |")
    L += [f"| environment digest | `{o['environment_digest']}` |",
          f"| package source fingerprint | `{o['source_fingerprint']['digest']}` |",
          f"| repo git HEAD | `{o['repo_git_head']}` |",
          f"| frozen ticket-07 budget digest | `{o['budget']['digest']}` (allowances {o['budget']['allowances']}) |",
          f"| pricing derivation used for preflight | `{o['pricing_derivation_digest']}` |",
          f"| O(walkers^2) identity-check seconds at 96,000 walkers (redesign S1) | {o['quadratic_probe']['quadratic_seconds']:.0f} s |", ""]
    snap = o["results_snapshot"]
    L += ["## Tree integrity\n",
          f"- `results/` ({snap['entries']} entries) unchanged by SHA-256 = **{snap.get('results_unchanged')}**; package tree "
          f"(incl. `__pycache__`) unchanged = **{snap.get('package_unchanged')}**.",
          "- Strictly serial child processes (oracle phase, then construction phase, per stage); parent RSS poll every 50 ms "
          "with a 2 GiB kill.  No verifier, pilot, production, sensitivity or fit.\n"]
    if o.get("events"):
        L += ["### Events\n"] + [f"- {e}" for e in o["events"]] + [""]
    L += ["## Walker count and memory\n",
          f"- {WALKERS} walkers (chosen by the redesign session's memory-scaling measurement; construction-phase peak "
          f"273 MiB there).  Oracle phases run in their own child: S2 margin grid 4800 x 76800 (1,589 MiB in the pricing "
          f"session); S3 would use the coarser 2400 x 76800 margin grid.\n",
          "## Stages\n",
          "| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for short in o["order"]:
        rec = o["stages"].get(short, {})
        res = rec.get("result", {})
        if rec.get("exit_state") == "completed":
            cfg = (f"oracle {res['oracle_grid']}, fine steps {res['fine_steps']}, timesteps "
                   f"{[f'{t:.3g}' for t in res['timesteps']]}, walkers {res['walkers']}")
            rows = rec.get("rule_rows", [])
            fitting = sum(1 for r in rows if r["fits"])
            rss = max(rec.get("ru_maxrss_bytes", 0), rec.get("oracle", {}).get("ru_maxrss_bytes", 0))
            L.append(f"| **{short}** {rec['label']} | {rec['exit_state']} | {cfg} | {res['verdict']} | "
                     f"{'ok' if res.get('procedure_ok') else 'FAIL'} {json.dumps(res.get('checks'), sort_keys=True)} | "
                     f"{fitting}/{len(rows)} fit ({rec.get('unit')}) | **{rec.get('stage_verdict')}** | "
                     f"{_hms((rec.get('child_wall_seconds') or 0) + (rec.get('oracle', {}).get('child_wall_seconds') or 0))} | "
                     f"{_mib(rss)} (oracle {_mib(rec.get('oracle', {}).get('ru_maxrss_bytes'))}, construction {_mib(rec.get('ru_maxrss_bytes'))}) |")
        else:
            L.append(f"| **{short}** {rec.get('label', '')} | {rec.get('exit_state', '—')} | — | — | — | — | "
                     f"**{rec.get('stage_verdict', '—')}** | — | — |")
    L.append("")
    for short in o["order"]:
        rec = o["stages"].get(short, {})
        L.append(f"### {short} — {rec.get('label', '')}\n")
        L.append(f"- State `{rec.get('exit_state')}`, stage verdict **{rec.get('stage_verdict')}**.")
        if rec.get("override"):
            L.append(f"- Override: {rec['override']}.  Overridden rule: {V.RULES['stage_stop']}")
        for r in rec.get("stage_reasons", []):
            L.append(f"- Reason: {r}")
        if rec.get("exit_state") != "completed":
            L.append("")
            continue
        res = rec["result"]
        unit = rec["unit"]
        L.append("- Rules applied: " + V.RULES["stage_success"].format(unit=unit, allowance=o["budget"]["allowances"][unit])
                 + "; " + V.RULES["stage_no_result"] + "; gate = " + V.RULES["gate"][:160] + "…")
        L.append(f"- Ladder gate **{res['verdict']}**" + (f"; reasons {res['reasons']}" if res["reasons"] else "")
                 + f".  Procedure checks {json.dumps(res['checks'], sort_keys=True)}; oracle gap {res['oracle_gap']:.3e} "
                 f"({res['oracle_margin_mode']} grid {res['oracle_margin_grid']}), smallest finest error "
                 f"{res['smallest_finest_error']:.3e}.  Dataset digest `{res['dataset_digest'][:16]}…`, budgets digest "
                 f"`{res['budgets_digest'][:16]}…`.")
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
        if rec.get("two_se_rows"):
            L.append(f"- 2 SE alone vs the probability allowance {o['budget']['allowances']['probability']:.6g}: " + "; ".join(
                f"{x['observable']}@{x['position']} {x['two_se']:.4f} ({'fits' if x['two_se_fits'] else 'exceeds'})"
                for x in rec["two_se_rows"]) + ".")
        L += ["", "| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |",
              "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        for lv in res["levels"]:
            L.append(f"| {lv['observable']} | {lv['position']} | {lv['timestep']:.4g} | {lv['measured']:.5f} | {lv['reference']:.5f} | "
                     f"{lv['absolute_error']:.5f} | {lv['standard_error']:.5f} | {lv['paired_error']:.5f} | {lv['span_error']:.5f} |")
        if rec.get("rule_rows"):
            L += ["", f"Stage rule rows ({unit}); bound = |error| + 2 SE vs allowance {rec['rule_rows'][0]['allowance']:.6g}:", "",
                  "| Observable | Position | |error| | SE | bound | ratio | fits |", "| --- | --- | --- | --- | --- | --- | --- |"]
            for r in rec["rule_rows"]:
                L.append(f"| {r['observable']} | {r['position']} | {r['absolute_error']:.5f} | {r['standard_error']:.5f} | "
                         f"{r['bound']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
        L.append("")
    pj = o.get("projections")
    if pj:
        L += ["## Projected bounds (the package's own `NumericalEvidence.projected_bound`)\n", pj["rule"] + "\n"]
        for name, rows in pj["sets"].items():
            labels = list(rows[0]["projected"].keys()) if rows and rows[0]["projected"] else []
            L += [f"### From {name} (finest level measured at timestep {rows[0]['timestep']:.4g})\n",
                  "| Observable | Position | Unit | Measured bound | ratio | " + " | ".join(f"projected {l}" for l in labels) + " |",
                  "| --- | --- | --- | --- | --- |" + " --- |" * len(labels)]
            for r in sorted(rows, key=lambda r: -r["ratio"]):
                cells = " | ".join(f"{r['projected'][l]['bound']:.5f} ({r['projected'][l]['ratio']:.2f}x, "
                                   f"{'fits' if r['projected'][l]['fits'] else 'NO'})" for l in labels)
                L.append(f"| {r['observable']} | {r['position']} | {r['unit']} | {r['bound']:.5f} | {r['ratio']:.2f}x | {cells} |")
            L.append("")
    d = o.get("disposition")
    if d:
        L += ["## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)\n", V.RULES["disposition"],
              f"\nSuperseding stationary stage: **{d['superseding_stationary_stage']}** (replaces S1's rows per the dependency chain).\n"]
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
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_s2_campaign.py --run",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_s2_campaign.py --derive-only",
          "```", "", "## Session log\n", "```"] + o.get("log", []) + ["```"]
    REPORT.write_text("\n".join(L) + "\n")


def selftest():
    rates, dg = V.pricing_rates()
    redesign = json.loads(REDESIGN.read_text())
    s1 = redesign["stages"]["S1"]
    quad = {"walkers": s1["result"]["walkers"], "quadratic_seconds": s1["result"]["quadratic_seconds"]}
    print("quadratic probe:", quad)
    for short in ("S2", "S3"):
        pf = R.preflight_stationary(STAGES[short], WALKERS, rates, quad)
        print(f"  {short}@{WALKERS}: linear {pf['linear_seconds']:.0f}s + quadratic {pf['quadratic_seconds_extrapolated']:.0f}s -> "
              f"{pf['predicted_seconds']:.0f}s; work {pf['work']}")
    fake = {"stages": {"S2": {"exit_state": "not_run"}}}
    pj = projections(fake)
    print("  projection sets:", {k: len(v) for k, v in pj["sets"].items()})
    r = pj["sets"]["S1_redesign_96k"][0]
    print("  sample projection row:", r["observable"], r["position"], round(r["bound"], 5), {k: round(v["bound"], 5) for k, v in r["projected"].items()})
    d = dispositions(fake)
    print("  disposition sets (no new stationary rows):", {k: (v["verdict"], v["rows_in"]) for k, v in d["sets"].items()})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--derive-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
    elif a.derive_only:
        o = json.loads(OBSERVATIONS.read_text())
        o["projections"] = projections(o)
        o["disposition"] = dispositions(o)
        write_report(o)
        print(json.dumps({k: (v["verdict"], v["blockers"]) for k, v in o["disposition"]["sets"].items()}, indent=1))
    elif a.run:
        session()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
