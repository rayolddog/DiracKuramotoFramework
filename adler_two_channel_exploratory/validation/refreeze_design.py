#!/usr/bin/env python3
"""
refreeze_design.py — sponsor's plan change: "Re-freeze the production design on
survival and the time rows."  A DERIVATION over the existing records; no run,
no package change.  Produces REFROZEN_DESIGN.json (hashed manifest) and
REFREEZE_REPORT.md beside it.

Re-frozen production observable set
  stationary : survival, exit_quantile_p35 (the time rows)
  moving-band: commit_probability_shift, survival_shift_at_0.45/0.60/0.80
  DROPPED    : exit_count_upper, exit_count_lower (S3: edge-attribution offset
               that does not fall with dt), commit_time_quantile_p20_shift
               (M6: diverging under refinement)
NOT re-frozen by this decision: the ladder gates (compare_refinement under the
frozen caps, including the moving-band added-resets cap) and the frozen budget
allowances.  Gate verdicts are therefore still carried into the disposition.

Modes:  --run (derive and write) | --check (recompute and compare the digest)
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import run_validation_campaign as V                                    # noqa: E402
import run_redesign_campaign as R                                      # noqa: E402
import run_s2_campaign as S                                            # noqa: E402
import price_validation_campaign as P                                  # noqa: E402

MANIFEST = HERE / "REFROZEN_DESIGN.json"
REPORT = HERE / "REFREEZE_REPORT.md"
RECORDS = {"first": HERE / "observations.json", "redesign": HERE / "observations_redesign.json",
           "s2": HERE / "observations_s2.json", "s3": HERE / "observations_s3.json",
           "pricing": REPO / "adler_two_channel_exploratory" / "pricing" / "observations.json"}
INSTRUCTION = "Re-freeze the production design on survival and the time rows."
RETAINED = {"stationary_oracle": ("survival", "exit_quantile_p35"),
            "moving_band_audit": ("commit_probability_shift", "survival_shift_at_0.45",
                                  "survival_shift_at_0.60", "survival_shift_at_0.80")}
DROPPED = ("exit_count_upper", "exit_count_lower", "commit_time_quantile_p20_shift")
TARGET_HALF_WIDTH = 0.25


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load():
    return {k: json.loads(p.read_text()) for k, p in RECORDS.items()}


def all_rows(rec):
    """Every evidence row available: reference (17), S3 (superseding S2/S1), M5, M6."""
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    first_rows = V.evidence_rows(rec["first"])
    reference = first_rows["reference"]
    m5 = [r for r in first_rows["intended"] if r.source == "moving_band_audit"]
    m6 = R.rows_from("M6", rec["redesign"]["stages"]["M6"], "intended",
                     "T07 redesign stage M6 at the intended configuration: dt/16 replay, 40 master trials on the 2^-13 mesh, "
                     "three regime clocks, four replicates", "moving_band_audit")
    s3 = S._stationary_rows("S3", rec["s3"]["stages"]["S3"], allow)
    return budget, {"reference": reference, "S3": s3, "M5": m5, "M6": m6}


def retained(rows):
    return [r for r in rows if r.observable in RETAINED[r.source]]


def relabel(rows, sources, verdict="pass"):
    return [dataclasses.replace(r, verdict=verdict) if r.source in sources else r for r in rows]


def dispose(budget, items):
    from adler_born_two_channel import experiments as xpr
    d = xpr.numerical_disposition(budget, items)
    return {"rows_in": len(items), "verdict": d.verdict, "blockers": list(d.blockers),
            "probability_admissible_trials": d.probability_admissible_trials,
            "time_admissible": d.time_admissible, "admissible_trials": d.admissible_trials,
            "limiting": {u: (list(d.limiting(u)) if d.limiting(u) else None) for u in ("probability", "time")},
            "rows": [{"source": r[0], "observable": r[1], "position": r[2], "unit": r[3], "bound": r[4],
                      "allowance": r[5], "fits": bool(r[6]), "ratio": r[4] / r[5]} for r in d.rows],
            "evidence_digest": d.evidence_digest, "disposition_digest": d.digest,
            "verdicts_in": sorted({f"{i.source}:{i.verdict}" for i in items})}


def half_width_for(trials):
    """The exponent half-width the package's power model says ``trials`` per cell
    buys: the smallest target half-width whose power_estimate needs <= trials.
    Bisection on SamplingTarget.exponent_half_width; also the 1/sqrt(n) scaling."""
    from adler_born_two_channel import experiments as xpr
    arms = (("full", 64, 0.10, 0.95, 1.0, 0.05, True), ("central_control", 1, 0.02, 0.95, 1.0, 0.10, False),
            ("width_only_control", 64, 0.05, 0.95, 1.0, 0.05, True))

    def needed(h):
        """Trials per cell the package's power model needs for half-width ``h``;
        infinity when the analysis layer or the power model refuses the target."""
        try:
            target = xpr.SamplingTarget(exponent_half_width=h, minimum_causal_contrast=0.5, coupling_low=0.5,
                                        coupling_high=2.0, cells=6, pairing_inflation=2.0, conservative_factor=1.25,
                                        resampling_unit="master_trial", arm_envelopes=tuple(xpr.ArmEnvelope(*e) for e in arms),
                                        shadow_fraction=0.05, maximum_trials_per_cell=200000)
            return xpr.power_estimate(target).trials_per_cell
        except Exception:                                                    # noqa: BLE001
            return float("inf")

    if trials <= 0:
        return {"trials": trials, "half_width_power_model": None, "half_width_scaling": None,
                "note": "no admissible trial count"}
    lo, hi = 0.02, 1.0                       # analysis.MAX_EXPONENT_HALF_WIDTH = 1.0 is the loosest admissible target
    if needed(hi) > trials:
        return {"trials": trials, "half_width_power_model": None,
                "half_width_scaling": TARGET_HALF_WIDTH * math.sqrt(2406 / trials), "target": TARGET_HALF_WIDTH,
                "meets_target": False,
                "note": f"even the loosest admissible half-width 1.0 needs {needed(hi)} trials per cell, more than the admissible {trials}"}
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if needed(mid) <= trials:
            hi = mid
        else:
            lo = mid
    return {"trials": trials, "half_width_power_model": hi, "trials_needed_at_that_half_width": needed(hi),
            "half_width_scaling": TARGET_HALF_WIDTH * math.sqrt(2406 / trials), "target": TARGET_HALF_WIDTH,
            "meets_target": hi <= TARGET_HALF_WIDTH}


def proposal(rec):
    """Cheapest priced run addressing what still blocks: an M5-size moving-band ladder
    at a finer step, priced from the pricing rates (proposal only)."""
    rates, dg = V.pricing_rates()
    m5 = [r for r in rec["first"]["disposition"]["sets"]["intended_only"]["rows"] if r["source"] == "moving_band_audit"
          and r["observable"] in RETAINED["moving_band_audit"]]
    # M5's retained probability rows at dt: bias-dominated (SE ~ 0.001 at 2560 trials).  The M5 ladder itself
    # measured the bias falling ~ sqrt(dt) (commit_probability_shift 0.0187 -> 0.0129 -> 0.0095 across 4dt, 2dt, dt).
    worst = max(m5, key=lambda r: r["bound"])
    out = {"what_blocks": "the moving-band audit's retained probability shifts at the intended step dt = 2^-9 "
                          "(M5, 2560 master trials): bias-dominated, 1.7x-2.3x the allowance",
           "rule": "bias projected with the package's sqrt(dt) rule, SE unchanged at 2560 trials (about 0.001)",
           "candidates": []}
    m5_levels = {lv["observable"]: lv for lv in rec["first"]["stages"]["M5"]["result"]["levels"]
                 if lv["timestep"] == min(x["timestep"] for x in rec["first"]["stages"]["M5"]["result"]["levels"])}
    allow = V.frozen_budget().allowance("probability")
    for factor, label in ((0.5, "dt/2"), (0.25, "dt/4"), (0.125, "dt/8"), (0.0625, "dt/16")):
        projected = {}
        for name in RETAINED["moving_band_audit"]:
            lv = m5_levels[name]
            projected[name] = abs(lv["absolute_error"]) * math.sqrt(factor) + 2.0 * lv["standard_error"]
        fits = all(v <= allow for v in projected.values())
        step = V.MOVING_CELL["base_step"] * factor
        steps = int(V.MOVING_CELL["base_steps"] / factor)
        phys, elig = V.count_moving_intervals(V.MOVING_CELL, step, steps)
        trials = 2560
        work_phys = phys * trials
        seconds = rates["physical_intervals"] * work_phys * 1.5
        out["candidates"].append({"ladder": f"M5-size (2560 master trials x 3 clocks x 4 replicates) at {label}: mesh step {step:.3g}, {steps} steps, strides (4,2,1)",
                                  "projected_bounds": projected, "all_fit_allowance": fits,
                                  "physical_intervals": work_phys, "audited_evaluations": elig * trials * 4,
                                  "priced_seconds_with_contingency": seconds, "priced_hours": seconds / 3600,
                                  "memory": "M5 measured 76 MiB, M6 79 MiB with the streaming validation runner (records digested, "
                                            "not stored); the pricing session's linear memory model (54.7 B per physical interval) "
                                            "applied only to the pricing children, which kept every AuditedRun record"})
    cheapest = next((c for c in out["candidates"] if c["all_fit_allowance"]), None)
    out["cheapest_that_projects_to_fit"] = cheapest["ladder"] if cheapest else None
    out["stationary_note"] = ("Under the re-frozen set nothing stationary blocks except S3's carried gate verdict, which came from "
                              "exit_count_upper (dropped).  Re-deciding that gate on the retained identities is a decision, not a "
                              "run; a fresh verdict object would need S3 re-run under a re-frozen FrozenBudgets: 4040 s measured "
                              "(7249 s priced), oracle child 1536 MiB, construction child 332 MiB.")
    out["pricing_derivation_digest"] = dg
    return out


def derive():
    rec = load()
    budget, rows = all_rows(rec)
    s3 = rec["s3"]["stages"]["S3"]
    m6 = rec["redesign"]["stages"]["M6"]
    m5 = rec["first"]["stages"]["M5"]
    ret = {k: retained(v) for k, v in rows.items()}
    sets = {"stationary_only": ret["S3"],
            "all_intended": ret["S3"] + ret["M5"] + ret["M6"],
            "reference_plus_intended": ret["reference"] + ret["S3"] + ret["M5"] + ret["M6"]}
    dispositions = {name: dispose(budget, items) for name, items in sets.items()}
    hyp1 = {name: dispose(budget, relabel(items, ("moving_band_audit",))) for name, items in sets.items()}
    hyp2 = {name: dispose(budget, relabel(items, ("moving_band_audit", "stationary_oracle"))) for name, items in sets.items()}
    power = {name: half_width_for(d["admissible_trials"]) for name, d in dispositions.items()}
    power_hyp2 = {name: half_width_for(d["admissible_trials"]) for name, d in hyp2.items()}
    prop = proposal(rec)
    s3_levels = s3["result"]["levels"]
    finest = min(lv["timestep"] for lv in s3_levels)
    ecu = {lv["position"]: [x["absolute_error"] for x in s3_levels if x["observable"] == "exit_count_upper" and x["position"] == lv["position"]]
           for lv in s3_levels if lv["observable"] == "exit_count_upper"}
    ecl = {lv["position"]: [x["absolute_error"] for x in s3_levels if x["observable"] == "exit_count_lower" and x["position"] == lv["position"]]
           for lv in s3_levels if lv["observable"] == "exit_count_lower"}
    manifest = {
        "schema": "refrozen-production-design/v1",
        "date": time.strftime("%Y-%m-%d"),
        "instruction_quoted": INSTRUCTION,
        "authorized_by": "John (sponsor's plan change), relayed by the coordinator",
        "retained_observables": {k: list(v) for k, v in RETAINED.items()},
        "dropped_observables": {
            "exit_count_upper": {
                "reason": "S3 (dt/256 at eightfold space, 96,000 walkers): ladder gate numerical_no_result on this observable at two starts; the error RISES under refinement with paired bootstrap SEs far below the steps",
                "quoted_gate_reasons": s3["result"]["reasons"],
                "errors_by_level_coarse_to_fine": ecu,
                "record": "observations_s3.json"},
            "exit_count_lower": {
                "reason": "S3: the edge-attribution offset does not fall with dt; the three finest-level rows are the only stationary rows over the allowance",
                "quoted_stage_reason": s3["stage_reasons"][1],
                "errors_by_level_coarse_to_fine": ecl,
                "record": "observations_s3.json"},
            "commit_time_quantile_p20_shift": {
                "reason": "M6 (dt/16 replay, 40 master trials): gate clause 3 [not_converging] on this observable; M5 (2560 trials) and the reference audit also fail the time allowance on it (3.81x, 8.06x)",
                "quoted_gate_reasons": m6["result"]["reasons"],
                "finest_levels": {"M6": [lv for lv in m6["result"]["levels"] if lv["observable"] == "commit_time_quantile_p20_shift"],
                                  "M5": [lv for lv in m5["result"]["levels"] if lv["observable"] == "commit_time_quantile_p20_shift"]},
                "record": "observations_redesign.json, observations.json"}},
        "not_refrozen": {
            "statement": "The ladder gates (killed_diffusion.compare_refinement under the frozen verify.py caps, INCLUDING the moving-band added_resets_mean absolute cap 3.0) and the frozen ticket-07 budget allowances (probability 0.004995, time 0.021953) are NOT re-frozen by this decision.",
            "flag": "FLAG: every moving-band ladder verdict on record (reference S3b, M5, M6) is numerical_no_result under the un-re-frozen gate (added-resets cap and/or p20 non-convergence), and experiments.numerical_disposition carries that verdict through as the blocker moving_band_numerical_no_result regardless of which observables are retained.  Likewise S3's stationary gate verdict is numerical_no_result on exit_count_upper (a dropped observable) and is carried as endpoint_envelope_exceeds_allowance.  Unless the sponsor separately re-freezes the gates, the disposition cannot leave numerical_no_result whatever the observable set.  The hypothetical recomputations below show what changes if the gates were re-decided; they are labelled hypothetical and authorize nothing."},
        "evidence_chain": {"stationary": "S3 (observations_s3.json) supersedes S2 and S1 per the dependency chain",
                           "moving": "M5 (observations.json) and M6 (observations_redesign.json) kept",
                           "reference": "17 ticket-04 rows reproduced in observations.json"},
        "records_sha256": {k: sha(p) for k, p in RECORDS.items()},
        "source_fingerprint": P.source_fingerprint()["digest"],
        "budget_digest": budget.digest,
        "dispositions_refrozen_set": dispositions,
        "hypothetical_audit_gate_not_carried": hyp1,
        "hypothetical_audit_and_stationary_gates_not_carried": hyp2,
        "power_translation": {"frozen": power, "hypothetical_both_gates": power_hyp2, "target_half_width": TARGET_HALF_WIDTH},
        "proposal": prop,
    }
    manifest["manifest_digest"] = hashlib.sha256(P.canonical_json({k: v for k, v in manifest.items() if k != "manifest_digest"}).encode()).hexdigest()
    return manifest


def _hms(s):
    return R._hms(s)


def write_report(m):
    identity = P.machine_identity()
    L = ["# Re-frozen production design — derivation report\n",
         "**A derivation over existing records; no run and no package change.  Nothing here is an approval or a sufficiency promise.**\n",
         f"Date {m['date']}.  Instruction (John, sponsor's plan change): \"{m['instruction_quoted']}\"\n",
         "## Environment identity\n", "| Field | Value |\n| --- | --- |"]
    for key in ("platform", "cpu_brand", "python_version", "numpy_version"):
        L.append(f"| {key} | `{identity.get(key, '')}` |")
    L += [f"| package source fingerprint | `{m['source_fingerprint']}` |", f"| frozen budget digest | `{m['budget_digest']}` |"]
    for k, v in m["records_sha256"].items():
        L.append(f"| record `{k}` sha256 | `{v}` |")
    L += ["", "## Manifest (`REFROZEN_DESIGN.json`)\n", f"- **Manifest digest:** `{m['manifest_digest']}`",
          f"- Retained: {json.dumps(m['retained_observables'], sort_keys=True)}",
          f"- Dropped: {list(m['dropped_observables'].keys())}"]
    for name, d in m["dropped_observables"].items():
        L.append(f"  - **{name}**: {d['reason']}.  Quoted: " + "; ".join(d.get("quoted_gate_reasons", [d.get("quoted_stage_reason", "")]))[:700])
        if "errors_by_level_coarse_to_fine" in d:
            L.append(f"    errors by level (coarse → fine): {json.dumps({k: [round(x, 5) for x in v] for k, v in d['errors_by_level_coarse_to_fine'].items()}, sort_keys=True)}")
    L += ["", f"- **Not re-frozen:** {m['not_refrozen']['statement']}", f"- **{m['not_refrozen']['flag']}**", ""]

    def table(sets, title):
        nonlocal L
        L.append(f"## {title}\n")
        for name, s in sets.items():
            L += [f"### `{name}` ({s['rows_in']} rows; row verdicts {s['verdicts_in']})\n",
                  f"- Verdict **{s['verdict']}**; blockers {s['blockers']}; probability-admissible trials {s['probability_admissible_trials']} "
                  f"(target 2406); time admissible {s['time_admissible']}; overall admissible {s['admissible_trials']}.",
                  f"- Limiting rows: {json.dumps(s['limiting'], sort_keys=True)}", "",
                  "| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
            for r in sorted(s["rows"], key=lambda r: -r["ratio"]):
                L.append(f"| {r['source']} | {r['observable']} | {r['position']} | {r['unit']} | {r['bound']:.5f} | {r['allowance']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
            L.append("")

    table(m["dispositions_refrozen_set"], "Dispositions on the re-frozen observable set (gate verdicts carried, as frozen)")
    table(m["hypothetical_audit_gate_not_carried"], "HYPOTHETICAL — moving-band gate verdict not carried (audit gate re-frozen by the sponsor)")
    table(m["hypothetical_audit_and_stationary_gates_not_carried"], "HYPOTHETICAL — moving-band AND stationary gate verdicts not carried (both gates re-decided on the retained identities)")
    L += ["## Power translation (experiments.power_estimate, read-only)\n",
          "The smallest exponent half-width whose power estimate needs no more than the admissible trial count (bisection on "
          "SamplingTarget.exponent_half_width), beside the 1/sqrt(n) scaling 0.25 x sqrt(2406/n); frozen target 0.25.\n",
          "| Evidence set | Gates | Admissible trials | Half-width (power model) | Half-width (scaling) | Meets 0.25 |", "| --- | --- | --- | --- | --- | --- |"]
    for label, block in (("as frozen", m["power_translation"]["frozen"]), ("hypothetical, both gates re-decided", m["power_translation"]["hypothetical_both_gates"])):
        for name, p in block.items():
            hw = p.get("half_width_power_model")
            L.append(f"| {name} | {label} | {p['trials']} | {('%.3f' % hw) if hw else '—'} | "
                     f"{('%.3f' % p['half_width_scaling']) if p.get('half_width_scaling') else '—'} | {p.get('meets_target', '—')} |")
    pr = m["proposal"]
    L += ["", "## What still blocks, and the cheapest priced run (proposal only)\n", f"- {pr['what_blocks']}.", f"- {pr['stationary_note']}",
          f"- Projection rule: {pr['rule']}.", "", "| Ladder | Projected finest bounds (retained moving rows) | All fit 0.004995 | Physical intervals | Priced (x1.5) |", "| --- | --- | --- | --- | --- |"]
    for c in pr["candidates"]:
        L.append(f"| {c['ladder']} | " + ", ".join(f"{k.replace('survival_shift_at_', 'ss')} {v:.4f}" for k, v in c["projected_bounds"].items())
                 + f" | {c['all_fit_allowance']} | {c['physical_intervals']:,} | {_hms(c['priced_seconds_with_contingency'])} ({c['priced_hours']:.1f} h) |")
    L += ["", f"- **Cheapest that projects to fit:** {pr['cheapest_that_projects_to_fit']}.  Memory: {pr['candidates'][0]['memory']}.",
          f"- Pricing derivation used: `{pr['pricing_derivation_digest']}`.", "",
          "## Ambiguities and choices\n",
          "1. **Gates carried.** The instruction re-freezes the observable set only; the gate verdicts on record are carried into the disposition exactly as experiments.numerical_disposition does.  Because S3's gate failed on a dropped observable and every moving-band gate failed on the added-resets cap and/or the dropped p20 row, two hypotheticals are shown, both labelled, neither authorizing anything.",
          "2. **Stationary gate hypothetical.** compare_refinement judges each (observable, position) identity on its own; S3's recorded reasons name only exit_count_upper, so on the retained identities the recorded ladder would carry no reason.  The hypothetical relabels S3's rows as pass on that basis without re-running anything; a fresh verdict object would require re-running S3 under a re-frozen FrozenBudgets.",
          "3. **Reference rows.** The reference set is restricted to the same retained observables, so the reference-plus-intended set is 24 rows rather than 39.",
          "4. **Power translation.** power_estimate is inverted by bisection on the target half-width with every other SamplingTarget field frozen (maximum_trials_per_cell raised to 200,000 only so that half-widths below 0.25 can be resolved); the scaling column is the closed form.",
          "5. **Proposal.** Bias projected with the package's sqrt(dt) rule, which on this cell was conservative for the retained (survival-type) rows and non-conservative only for the dropped edge-split rows; the M5 ladder's own levels show the retained shifts falling like sqrt(dt).  Prices use the pricing session's slowest replay rate with the 1.5x contingency; memory from the streaming validation runner's measured peaks.",
          "", "## Reproduce\n", "```", f"cd {REPO}",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/refreeze_design.py --run     # writes REFROZEN_DESIGN.json and this report",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/refreeze_design.py --check   # recomputes and compares the manifest digest", "```"]
    REPORT.write_text("\n".join(L) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.run:
        m = derive()
        MANIFEST.write_text(json.dumps(m, indent=1, sort_keys=True, default=P._json_default))
        write_report(m)
        print("manifest digest", m["manifest_digest"])
        for block, label in ((m["dispositions_refrozen_set"], "frozen"), (m["hypothetical_audit_gate_not_carried"], "hyp1"),
                             (m["hypothetical_audit_and_stationary_gates_not_carried"], "hyp2")):
            for name, s in block.items():
                print(f"  {label:6s} {name:24s} {s['verdict']:20s} adm={s['admissible_trials']:5d} prob_adm={s['probability_admissible_trials']:5d} time_ok={s['time_admissible']} blockers={s['blockers']}")
        print("power:", json.dumps(m["power_translation"], indent=None, default=str)[:900])
        print("proposal cheapest:", m["proposal"]["cheapest_that_projects_to_fit"])
        for c in m["proposal"]["candidates"]:
            print("   ", c["ladder"][:60], {k[:6]: round(v, 4) for k, v in c["projected_bounds"].items()}, c["all_fit_allowance"], f"{c['priced_hours']:.1f} h")
    elif a.check:
        m = derive()
        stored = json.loads(MANIFEST.read_text())
        same = m["manifest_digest"] == stored["manifest_digest"]
        print("manifest digest reproduced:", same, m["manifest_digest"])
        sys.exit(0 if same else 1)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
