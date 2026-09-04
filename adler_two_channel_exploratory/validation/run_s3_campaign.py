#!/usr/bin/env python3
"""
run_s3_campaign.py — third sponsor's override: run S3 (stationary probability,
dt/256 at eightfold space) at 96,000 walkers despite S2's numerical_no_result;
if S3 succeeds under the frozen stage rules, run S4 (time quantile at dt/256)
under the frozen dependency rule with no further override (S4 judges S3's
frozen ladder's time rows); if S3 returns numerical_no_result, stop and report.

Thin wrapper over run_s2_campaign.py's session machinery (oracle child, then
construction child; priced preflight with the measured O(walkers^2) term; RSS
kill guard; incremental observations).  New files only: observations_s3.json
and S3_REPORT.md.  At eightfold space the refined margin grid (9600 x 307200)
would exceed 2 GiB, so the COARSER grid 2400 x 76800 is differenced (overstates
the oracle's own error by ~3x for a second-order scheme, the conservative
direction).

Modes:  --run | --derive-only | --selftest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_s2_campaign as S                                            # noqa: E402
import run_redesign_campaign as R                                      # noqa: E402
import run_validation_campaign as V                                    # noqa: E402

S2_RECORD = HERE / "observations_s2.json"                              # read-only
S.OBSERVATIONS = HERE / "observations_s3.json"
S.REPORT = HERE / "S3_REPORT.md"
S.SCRATCH = S.SCRATCH.parent / "s3_stages"
S.STAGES = {
    "S3": dict(kind="stationary", label="stationary probability, dt/256 at eightfold space (96,000 walkers; S2 stop rule overridden by the sponsor)", unit="probability", time_factor=256, space_factor=8, depends_on=None, overridden_predecessor="S2"),
    "S4": dict(kind="stationary_time", label="stationary time quantile, dt/256 at eightfold space (96,000 walkers; judged on S3's frozen ladder)", unit="time", time_factor=256, space_factor=8, depends_on="S3"),
}
S.ORDER = ["S3", "S4"]
S.INTERPRETATIONS = S.INTERPRETATIONS + [
    ("third override", "S3 runs although its predecessor S2 (96,000 walkers, S2-override session) returned numerical_no_result on one row (exit_count_upper@x=0.610512, 1.05x), by the third sponsor's override; the frozen stop rule is quoted and the override stated.  S4 keeps the frozen dependency rule with no further override and judges the time rows of S3's frozen ladder (the same keyed, digest-verified data) rather than recomputing it."),
    ("eightfold-space oracle margin", "The S3 oracle grid is 4800 x 153600 (about 1.6 GiB in its own child).  The refined margin grid 9600 x 307200 would exceed the 2 GiB cap, so the coarser grid 2400 x 76800 is differenced against the oracle; for a second-order scheme that gap is about three times the oracle's own error, so the margin ratio reported understates the true margin (conservative)."),
    ("disposition fallback", "If S3 completes, its rows supersede S2's; if S3 does not complete, S2's rows (from observations_s2.json) remain the superseding stationary rows.  M5 (first session) and M6 (redesign session) rows are kept.  S4's rows are S3's time rows, already present in S3's ladder."),
]


def projections(observations):
    """S2's finest rows (from observations_s2.json) projected to dt/256 by the
    package's own rule, beside S3's measured rows."""
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    s2 = json.loads(S2_RECORD.read_text())["stages"]["S2"]
    out = {"rule": "NumericalEvidence.projected_bound(2.0, timestep_factor, sample_factor=1): |measured| * sqrt(factor) + 2 SE",
           "sets": {}}
    sources = [("S2_override_96k", s2, {"to dt/256": 0.25})]
    rec = observations["stages"].get("S3", {})
    if rec.get("exit_state") == "completed" and "result" in rec:
        sources.append(("S3", rec, {}))
    for name, src, factors in sources:
        rows = []
        for ev in S._stationary_rows(name.split("_")[0], src, allow):
            entry = {"observable": ev.observable, "position": ev.position, "unit": ev.unit, "timestep": ev.timestep,
                     "measured": ev.measured, "standard_error": ev.standard_error, "bound": ev.bound_at(2.0),
                     "allowance": allow[ev.unit], "ratio": ev.bound_at(2.0) / allow[ev.unit],
                     "fits": ev.bound_at(2.0) <= allow[ev.unit], "projected": {}}
            for label, factor in factors.items():
                pb = ev.projected_bound(2.0, timestep_factor=factor, sample_factor=1.0)
                entry["projected"][label] = {"factor": factor, "bound": pb, "ratio": pb / allow[ev.unit], "fits": pb <= allow[ev.unit]}
            rows.append(entry)
        out["sets"][name] = rows
    return out


def dispositions(observations):
    from adler_born_two_channel import experiments as xpr
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    first = json.loads(S.PREVIOUS.read_text())
    redesign = json.loads(S.REDESIGN.read_text())
    s2 = json.loads(S2_RECORD.read_text())
    prev_rows = V.evidence_rows(first)
    reference = prev_rows["reference"]
    m5 = [r for r in prev_rows["intended"] if r.source == "moving_band_audit"]
    m6 = R.rows_from("M6", redesign["stages"]["M6"], "intended",
                     "T07 redesign stage M6 at the intended configuration: dt/16 replay, 40 master trials on the 2^-13 mesh, "
                     "three regime clocks, four replicates", "moving_band_audit")
    rec = observations["stages"].get("S3", {})
    if rec.get("exit_state") == "completed" and "result" in rec:
        finest, src = "S3", rec
    else:
        finest, src = "S2 (observations_s2.json; S3 did not complete)", s2["stages"]["S2"]
    new_stationary = S._stationary_rows(finest.split(" ")[0], src, allow)
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


_BASE_WRITE_REPORT = S.write_report          # captured before the rebinding below


def write_report(o):
    _BASE_WRITE_REPORT(o)
    text = S.REPORT.read_text()
    text = text.replace("# S2 override — intended-configuration validation campaign report",
                        "# S3 override — intended-configuration validation campaign report", 1)
    text = text.replace("The second sponsor's override authorized S2 despite S1's `numerical_no_result`; S3 and S4 kept the "
                        "frozen dependency rule with no further override.",
                        "The third sponsor's override authorized S3 despite S2's `numerical_no_result` (one row, 1.05x); S4 kept "
                        "the frozen dependency rule with no further override and judges S3's frozen ladder's time rows.", 1)
    text = text.replace("S3 would use the coarser 2400 x 76800 margin grid",
                        "S3 uses the coarser 2400 x 76800 margin grid (refined 9600 x 307200 would exceed the cap; ~3x conservative)", 1)
    text = text.replace("run_s2_campaign.py --run", "run_s3_campaign.py --run").replace(
        "run_s2_campaign.py --derive-only", "run_s3_campaign.py --derive-only")
    text = text.replace("(replaces S1's rows per the dependency chain)", "(replaces S2's rows per the dependency chain)", 1)
    S.REPORT.write_text(text)


S.projections = projections
S.dispositions = dispositions
S.write_report = write_report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--derive-only", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        rates, _ = V.pricing_rates()
        quad = S.json.loads(S.REDESIGN.read_text())["stages"]["S1"]["result"]["quadratic_seconds"]
        pf = R.preflight_stationary(S.STAGES["S3"], S.WALKERS, rates, {"walkers": 96000, "quadratic_seconds": quad})
        print(f"S3 preflight: linear {pf['linear_seconds']:.0f}s + quadratic {pf['quadratic_seconds_extrapolated']:.0f}s -> {pf['predicted_seconds']:.0f}s")
        fake = {"stages": {"S3": {"exit_state": "not_run"}}}
        pj = projections(fake); d = dispositions(fake)
        print("projection sets:", {k: len(v) for k, v in pj["sets"].items()},
              "| sample:", [(r["observable"], r["position"], round(r["bound"], 5), round(r["projected"]["to dt/256"]["bound"], 5)) for r in pj["sets"]["S2_override_96k"][:2]])
        print("disposition fallback:", d["superseding_stationary_stage"], {k: (v["verdict"], v["rows_in"]) for k, v in d["sets"].items()})
        print("order", S.ORDER, "obs", S.OBSERVATIONS.name, "report", S.REPORT.name, "scratch", S.SCRATCH.name)
    elif a.derive_only:
        o = json.loads(S.OBSERVATIONS.read_text())
        o["projections"] = projections(o)
        o["disposition"] = dispositions(o)
        write_report(o)
        print(json.dumps({k: (v["verdict"], v["blockers"]) for k, v in o["disposition"]["sets"].items()}, indent=1))
    elif a.run:
        S.session()
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
