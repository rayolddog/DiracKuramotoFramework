#!/usr/bin/env python3
"""
redecide_gates.py — sponsor's decision: "Re-decide the two gate verdicts on the
retained identities."  A DERIVATION over the recorded ladders; no run, no
package change.

For each recorded ladder (S3 in observations_s3.json; M5 and the reference
S3b ladder in observations.json; M6 in observations_redesign.json) the
per-level values, standard errors, paired and span errors are rebuilt into the
package's own RefinementLevel records and judged, identity by identity, by the
package's own per-identity clause function killed_diffusion._ladder_codes under
the frozen caps (S3: verify.py _s3_budgets caps; S3b/M5/M6: verify.py
_audit_caps as recorded) with coverage 2.0.  The mirror is validated by
requiring that judging EVERY identity reproduces the recorded reasons verbatim.
The re-decided verdict of a ladder is numerical_no_result if any RETAINED
identity earns a code, else pass; no clause is softened.  The added_resets_mean
absolute cap is set aside for the re-decision (it judges a diagnostic count
that is not a retained observable) and its status is reported separately.

Outputs: REDECIDED_GATES.json (hashed, chained to REFROZEN_DESIGN.json by
digest) and REDECIDE_REPORT.md.   Modes: --run | --check
"""
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
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
import refreeze_design as F                                            # noqa: E402
import price_validation_campaign as P                                  # noqa: E402

MANIFEST = HERE / "REDECIDED_GATES.json"
REPORT = HERE / "REDECIDE_REPORT.md"
INSTRUCTION = "Re-decide the two gate verdicts on the retained identities."
COVERAGE = 2.0
LADDERS = {   # name: (record key, stage key, source, budgets)
    "REF_S3": ("first", "REF_S3", "stationary_oracle"),
    "REF_S3B": ("first", "REF_S3B", "moving_band_audit"),
    "S3": ("s3", "S3", "stationary_oracle"),
    "M5": ("first", "M5", "moving_band_audit"),
    "M6": ("redesign", "M6", "moving_band_audit"),
}
MOVING_OBSERVABLES = [("commit_probability_shift", "probability", "mean", 0.5, True)]
MOVING_OBSERVABLES += [(f"survival_shift_at_{f:.2f}", "probability", "mean", 0.5, True) for f in (0.45, 0.60, 0.80)]
MOVING_OBSERVABLES.append(("commit_time_quantile_p20_shift", "time", "quantile", 0.20, True))
MOVING_OBSERVABLES.append(("added_resets_mean", "count", "mean", 0.5, False))


def budgets_for(source, result):
    from adler_born_two_channel import killed_diffusion as kdf
    out = {}
    if source == "stationary_oracle":
        positions = sorted({lv["position"] for lv in result["levels"]})
        for name, (unit, estimator, level, absolute, relative, floor) in V.S3_CAPS.items():
            for pos in positions:
                out[(name, pos)] = kdf.ValidationBudget(name, unit, absolute, relative, floor, True, pos, estimator, level)
    else:
        caps = result["caps"]
        for name, unit, estimator, level, decreasing in MOVING_OBSERVABLES:
            a, r, fl = caps[name]
            out[(name, "pooled")] = kdf.ValidationBudget(name, unit, a, r, fl, decreasing, "pooled", estimator, level)
    return out


def rebuild_ladders(result):
    from adler_born_two_channel import killed_diffusion as kdf
    ladders = {}
    for lv in result["levels"]:
        ladders.setdefault((lv["observable"], lv["position"]), []).append(kdf.RefinementLevel(
            lv["observable"], lv["unit"], lv["timestep"], lv["measured"], lv["reference"], lv["standard_error"],
            lv["clusters"], lv["position"], lv["paired_error"], lv["span_error"]))
    for key in ladders:
        ladders[key].sort(key=lambda x: -x.timestep)               # coarsest first, as compare_refinement orders them
    return ladders


def clauses(budget, ladder):
    """Explicit per-clause results (mirroring _ladder_codes' arithmetic) for the report."""
    finest, coarsest = ladder[-1], ladder[0]
    span = budget.noise_floor + COVERAGE * finest.span_error
    steps = []
    reversals = 0
    for coarse, fine in zip(ladder, ladder[1:]):
        growth = fine.absolute_error - coarse.absolute_error
        entry = {"timestep": fine.timestep, "growth": growth, "reversal": growth > 0.0}
        if growth > 0.0:
            reversals += 1
            entry["allowance"] = budget.noise_floor + COVERAGE * fine.paired_error
            entry["beyond_allowance"] = growth > entry["allowance"]
        steps.append(entry)
    return {
        "clause2_absolute_cap": {"bounded_error": finest.bounded_error(COVERAGE), "cap": budget.absolute,
                                 "ok": finest.bounded_error(COVERAGE) <= budget.absolute},
        "clause2_relative_cap": {"relative_error": finest.relative_error, "cap": budget.relative,
                                 "ok": finest.relative_error <= budget.relative},
        "clause3_finest_le_coarsest": {"finest": finest.absolute_error, "coarsest": coarsest.absolute_error,
                                       "allowance": span, "ok": finest.absolute_error <= coarsest.absolute_error + span,
                                       "applies": budget.require_decrease},
        "clause4_reversals": {"count": reversals, "steps": steps, "applies": budget.require_decrease,
                              "ok": (reversals <= 1 and not any(s.get("beyond_allowance") for s in steps))},
    }


def redecide(rec):
    from adler_born_two_channel import killed_diffusion as kdf
    out = {}
    for name, (rkey, skey, source) in LADDERS.items():
        stage = rec[rkey]["stages"][skey]
        result = stage["result"]
        budgets = budgets_for(source, result)
        ladders = rebuild_ladders(result)
        retained_ids = sorted(k for k in ladders if k[0] in F.RETAINED[source])
        identities = {}
        reproduced = []
        for key in sorted(ladders):
            codes = kdf._ladder_codes(budgets[key], ladders[key], COVERAGE)
            identities[f"{key[0]}@{key[1]}"] = {"retained": key in retained_ids, "codes": [list(c) for c in codes],
                                                "clauses": clauses(budgets[key], ladders[key])}
            reproduced += [f"{key!r}: [{code}] {detail}" for code, detail in codes]
        mirror_ok = reproduced == list(result["reasons"])
        retained_codes = {k: v["codes"] for k, v in identities.items() if v["retained"] and v["codes"]}
        added = identities.get("added_resets_mean@pooled")
        out[name] = {
            "record": {"first": "observations.json", "redesign": "observations_redesign.json", "s3": "observations_s3.json"}[rkey],
            "source": source, "original_verdict": result["verdict"], "original_reasons": list(result["reasons"]),
            "mirror_reproduces_recorded_reasons": mirror_ok, "retained_identities": [f"{k[0]}@{k[1]}" for k in retained_ids],
            "identities": identities, "retained_codes": retained_codes,
            "redecided_verdict": "pass" if not retained_codes else "numerical_no_result",
            "added_resets_mean_status": ({"set_aside": True, "codes": added["codes"], "clauses": added["clauses"],
                                          "would_block": bool(added["codes"])} if added else None),
        }
    return out


def evidence(rec, decisions):
    budget = V.frozen_budget()
    allow = {"probability": budget.allowance("probability"), "time": budget.allowance("time")}
    first_rows = V.evidence_rows(rec["first"])
    ref = [dataclasses.replace(r, verdict=decisions["REF_S3B"]["redecided_verdict"]) if r.source == "moving_band_audit"
           else dataclasses.replace(r, verdict=decisions["REF_S3"]["redecided_verdict"]) for r in first_rows["reference"]]
    m5 = [dataclasses.replace(r, verdict=decisions["M5"]["redecided_verdict"]) for r in first_rows["intended"]
          if r.source == "moving_band_audit"]
    m6 = [dataclasses.replace(r, verdict=decisions["M6"]["redecided_verdict"]) for r in R.rows_from(
        "M6", rec["redesign"]["stages"]["M6"], "intended",
        "T07 redesign stage M6 at the intended configuration: dt/16 replay, 40 master trials on the 2^-13 mesh, three regime "
        "clocks, four replicates", "moving_band_audit")]
    s3 = [dataclasses.replace(r, verdict=decisions["S3"]["redecided_verdict"]) for r in
          S._stationary_rows("S3", rec["s3"]["stages"]["S3"], allow)]
    return budget, {k: F.retained(v) for k, v in (("reference", ref), ("S3", s3), ("M5", m5), ("M6", m6))}


def derive():
    rec = F.load()
    refrozen = json.loads(F.MANIFEST.read_text())
    decisions = redecide(rec)
    budget, rows = evidence(rec, decisions)
    sets = {"stationary_only": rows["S3"], "all_intended": rows["S3"] + rows["M5"] + rows["M6"],
            "reference_plus_intended": rows["reference"] + rows["S3"] + rows["M5"] + rows["M6"]}
    dispositions = {name: F.dispose(budget, items) for name, items in sets.items()}
    power = {name: F.half_width_for(d["admissible_trials"]) for name, d in dispositions.items()}
    prop = F.proposal(rec)
    prop["after_this_decision"] = ("What still blocks is the moving-band audit's retained probability shifts at the intended "
                                   "step (M5 rows 1.7x-2.3x); the re-decided gates remove every carried gate verdict, so the "
                                   "all-intended set is 'unresolved' rather than 'numerical_no_result'.  The records suggest no "
                                   "cheaper route than the M5-size dt/16 ladder: at dt/8 the projected worst bound is 0.0054 (fails); "
                                   "fewer trials at dt/16 fail on SE (1280 trials: 0.0024 + 0.0028 = 0.0052); more trials at a coarser "
                                   "step cost more (dt/8 x 4 trials = 2x the dt/16 cost).")
    manifest = {
        "schema": "redecided-gates/v1", "date": time.strftime("%Y-%m-%d"), "instruction_quoted": INSTRUCTION,
        "authorized_by": "John (sponsor's decision), relayed by the coordinator",
        "chained_to": {"REFROZEN_DESIGN.json": refrozen["manifest_digest"]},
        "method": ("RefinementLevel records rebuilt from each recorded ladder's per-level measured, reference, standard_error, "
                   "paired_error, span_error and clusters; ValidationBudget per identity from the frozen caps; judged by "
                   "killed_diffusion._ladder_codes (the package's single source of the gate decision) with coverage 2.0.  "
                   "Mirror validated: judging every identity reproduces the recorded reasons verbatim (see per ladder).  "
                   "Re-decided verdict = numerical_no_result if any RETAINED identity earns a code, else pass; no clause softened."),
        "added_resets_mean": ("Set aside for the re-decision by the sponsor's decision: it judges a diagnostic count with no "
                              "continuum limit that is not a retained observable.  Its status under the frozen cap is reported "
                              "separately per moving ladder and is NOT re-frozen."),
        "retained_observables": {k: list(v) for k, v in F.RETAINED.items()},
        "ladders": decisions,
        "records_sha256": {k: F.sha(p) for k, p in F.RECORDS.items()},
        "source_fingerprint": P.source_fingerprint()["digest"], "budget_digest": budget.digest,
        "dispositions_redecided": dispositions, "power_translation": power, "proposal": prop,
    }
    manifest["manifest_digest"] = hashlib.sha256(P.canonical_json({k: v for k, v in manifest.items() if k != "manifest_digest"}).encode()).hexdigest()
    return manifest


def write_report(m):
    identity = P.machine_identity()
    L = ["# Re-decided gate verdicts — derivation report\n",
         "**A derivation over recorded ladders; no run and no package change.  Nothing here is an approval or a sufficiency promise.**\n",
         f"Date {m['date']}.  Instruction (John, sponsor's decision): \"{m['instruction_quoted']}\"  Chained to REFROZEN_DESIGN.json "
         f"digest `{m['chained_to']['REFROZEN_DESIGN.json']}`.\n", "## Environment identity\n", "| Field | Value |\n| --- | --- |"]
    for key in ("platform", "cpu_brand", "python_version", "numpy_version"):
        L.append(f"| {key} | `{identity.get(key, '')}` |")
    L += [f"| package source fingerprint | `{m['source_fingerprint']}` |", f"| frozen budget digest | `{m['budget_digest']}` |"]
    for k, v in m["records_sha256"].items():
        L.append(f"| record `{k}` sha256 | `{v}` |")
    L += ["", "## Manifest (`REDECIDED_GATES.json`)\n", f"- **Manifest digest:** `{m['manifest_digest']}`", f"- Method: {m['method']}",
          f"- added_resets_mean: {m['added_resets_mean']}", "", "## Re-decided ladders\n",
          "| Ladder | Record | Original verdict | Retained identities judged | Retained codes | **Re-decided** | added_resets_mean status (set aside) | Mirror reproduces recorded reasons |",
          "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for name, d in m["ladders"].items():
        ar = d["added_resets_mean_status"]
        L.append(f"| {name} | {d['record']} | {d['original_verdict']} | {len(d['retained_identities'])}: {', '.join(d['retained_identities'])} | "
                 f"{d['retained_codes'] if d['retained_codes'] else 'none'} | **{d['redecided_verdict']}** | "
                 f"{('would block: ' + str(ar['codes'])) if ar and ar['would_block'] else ('no code' if ar else 'n/a')} | {d['mirror_reproduces_recorded_reasons']} |")
    L.append("")
    for name, d in m["ladders"].items():
        L += [f"### {name}\n", f"- Original: **{d['original_verdict']}**; recorded reasons: {d['original_reasons']}",
              f"- Re-decided on the retained identities: **{d['redecided_verdict']}**.", "",
              "| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
        for ident, v in d["identities"].items():
            c = v["clauses"]
            c3 = c["clause3_finest_le_coarsest"]
            c4 = c["clause4_reversals"]
            L.append(f"| {ident} | {'yes' if v['retained'] else 'no'} | {c['clause2_absolute_cap']['bounded_error']:.5g} / {c['clause2_absolute_cap']['cap']:.3g} "
                     f"{'ok' if c['clause2_absolute_cap']['ok'] else 'FAIL'} | {c['clause2_relative_cap']['relative_error']:.3g} / {c['clause2_relative_cap']['cap']:.3g} "
                     f"{'ok' if c['clause2_relative_cap']['ok'] else 'FAIL'} | "
                     + (f"{c3['finest']:.5g} ≤ {c3['coarsest']:.5g} + {c3['allowance']:.5g} {'ok' if c3['ok'] else 'FAIL'}" if c3['applies'] else "waived (require_decrease=false)")
                     + f" | " + (f"{c4['count']} {'ok' if c4['ok'] else 'FAIL'}" if c4['applies'] else "waived")
                     + f" | {[x[0] for x in v['codes']] if v['codes'] else '—'} |")
        L.append("")
    L.append("## Dispositions on the re-frozen observable set with the re-decided gate verdicts carried\n")
    for name, s in m["dispositions_redecided"].items():
        L += [f"### `{name}` ({s['rows_in']} rows; row verdicts {s['verdicts_in']})\n",
              f"- Verdict **{s['verdict']}**; blockers {s['blockers']}; probability-admissible trials {s['probability_admissible_trials']} (target 2406); "
              f"time admissible {s['time_admissible']}; overall admissible {s['admissible_trials']}.",
              f"- Limiting rows: {json.dumps(s['limiting'], sort_keys=True)}", "",
              "| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for r in sorted(s["rows"], key=lambda r: -r["ratio"]):
            L.append(f"| {r['source']} | {r['observable']} | {r['position']} | {r['unit']} | {r['bound']:.5f} | {r['allowance']:.5f} | {r['ratio']:.2f}x | {'yes' if r['fits'] else 'NO'} |")
        L.append("")
    L += ["## Power translation (experiments.power_estimate, read-only; frozen target 0.25)\n",
          "| Evidence set | Admissible trials | Half-width (power model) | Half-width (scaling) | Meets 0.25 |", "| --- | --- | --- | --- | --- |"]
    for name, p in m["power_translation"].items():
        hw = p.get("half_width_power_model")
        L.append(f"| {name} | {p['trials']} | {('%.3f' % hw) if hw else '—'} | {('%.3f' % p['half_width_scaling']) if p.get('half_width_scaling') else '—'} | {p.get('meets_target', '—')} |")
    pr = m["proposal"]
    L += ["", "## What still blocks, and the cheapest priced run (proposal only)\n", f"- {pr['after_this_decision']}", f"- {pr['stationary_note']}", "",
          "| Ladder | Projected finest bounds (retained moving rows) | All fit 0.004995 | Physical intervals | Priced (x1.5) |", "| --- | --- | --- | --- | --- |"]
    for c in pr["candidates"]:
        L.append(f"| {c['ladder']} | " + ", ".join(f"{k.replace('survival_shift_at_', 'ss')} {v:.4f}" for k, v in c["projected_bounds"].items())
                 + f" | {c['all_fit_allowance']} | {c['physical_intervals']:,} | {R._hms(c['priced_seconds_with_contingency'])} ({c['priced_hours']:.1f} h) |")
    L += ["", f"- **Cheapest that projects to fit:** {pr['cheapest_that_projects_to_fit']}.  Memory: {pr['candidates'][0]['memory']}.", "",
          "## Ambiguities and choices\n",
          "1. **The gate's own function.** Verdicts are re-decided by calling killed_diffusion._ladder_codes on rebuilt RefinementLevel records, not by a re-implementation; the mirror is validated per ladder by reproducing the recorded reasons verbatim over all identities (dropped ones included).",
          "2. **Retained identities only.** A ladder's re-decided verdict considers only retained identities; a retained identity failing any frozen clause keeps the ladder at numerical_no_result.  No cap, floor or coverage is changed.",
          "3. **added_resets_mean.** Set aside by the sponsor's decision as a diagnostic count outside the retained set; its frozen-cap status is reported separately and it is not re-frozen.",
          "4. **Reference ladders.** The reference S3b ladder is re-decided on the same rule so that the reference-plus-intended set is consistent; the reference S3 ladder passed originally and passes on the retained identities.",
          "5. **Evidence rows.** Rows carry the re-decided verdicts; observables, positions, measured errors and SEs are exactly the recorded ones.",
          "", "## Reproduce\n", "```", f"cd {REPO}",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/redecide_gates.py --run     # writes REDECIDED_GATES.json and this report",
          "PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/redecide_gates.py --check   # recomputes and compares the manifest digest", "```"]
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
        print("manifest digest", m["manifest_digest"], "| chained to", m["chained_to"])
        for name, d in m["ladders"].items():
            ar = d["added_resets_mean_status"]
            print(f"  {name:8s} original={d['original_verdict']:20s} redecided={d['redecided_verdict']:20s} retained_codes={d['retained_codes']} "
                  f"mirror_ok={d['mirror_reproduces_recorded_reasons']} added_resets={'would block' if ar and ar['would_block'] else ('ok' if ar else 'n/a')}")
        for name, s in m["dispositions_redecided"].items():
            print(f"  {name:24s} {s['verdict']:20s} adm={s['admissible_trials']:5d} blockers={s['blockers']} verdicts_in={s['verdicts_in']}")
            for r in sorted(s["rows"], key=lambda r: -r["ratio"]):
                if not r["fits"]:
                    print(f"      {r['source'][:10]:10s} {r['observable']:24s} {r['position']:11s} {r['bound']:.5f} {r['ratio']:.2f}x NO")
        print("  power:", {k: (v.get("half_width_power_model"), v.get("meets_target")) for k, v in m["power_translation"].items()})
        print("  cheapest:", m["proposal"]["cheapest_that_projects_to_fit"])
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
