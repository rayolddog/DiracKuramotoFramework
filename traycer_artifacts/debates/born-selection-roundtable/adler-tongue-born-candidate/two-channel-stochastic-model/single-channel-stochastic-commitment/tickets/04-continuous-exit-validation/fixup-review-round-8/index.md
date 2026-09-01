---
title: "Ticket 04 fix-up round 8 — schema documentation closure"
kind: ticket
status: 2
---

# Objective

Correct the final three stale schema-version statements and make the documentation check detect abbreviated legacy wording.

## Required corrections

- Replace the stale `v2` statements in the package README and the two identified `killed_diffusion.py` locations with accurate schema-v4 wording.
- Search the entire package for prose that describes the current validation report as v1, v2, or v3, including abbreviated forms not prefixed by the full schema name.
- Strengthen the documentation verifier so the exact three stale statements, and equivalent current-schema claims using v1/v2/v3, fail without rejecting legitimate historical migration notes that are clearly marked historical.
- Preserve all implementation behavior and all 85 checks; only documentation/check text should change.

## Completion gate

The same independent reviewer must return `CLOSED` after confirming the live schema is described consistently as v4.

## Implementation report — 2026-08-28

Documentation and check text only. Canonical suite **85/85**, exit 0, 84 s,
peak RSS 620 MB. Of the 85 rows shared with round 7, **84 carry byte-identical**
**residuals**; only the memory row moved. No row renamed, no check added or
removed, no numerical result or cap touched.

### 1 — The three stale statements

| Location | Was | Now |
| --- | --- | --- |
| `README.md:2041` | "The version is `v2` because the shape changed incompatibly and the tag had not." | "The live schema is **v4**. It reached that in three steps…", then the v1→v2→v3→v4 history in past tense |
| `killed_diffusion.py:2389` (`as_dict`) | "which is why the tag reads `v2`" | "Keys are stable under :data:`VALIDATION_SCHEMA`, which is **v4**." |
| `killed_diffusion.py:2453` (`REPORT_FIELDS`) | "The exact top-level keys a v2 report carries." | "The exact top-level keys a report under the live :data:`VALIDATION_SCHEMA` carries." |

A package-wide sweep found one more, in a `verify.py` mutation label: "a v1 tag
on a v2 shape" now reads "a superseded tag on the live shape". Nothing else in
the package asserts a live schema below v4.

### 2 — What the sweep deliberately preserved

Prose about earlier versions is load-bearing here — it is the record of why each
shape was superseded — so these were identified as legitimate and left intact:
`killed_diffusion.py` 192–211 (the v1→v4 migration block), `moving_band_audit.py`
139–145 (the audit key v1→v2 note), `README.md` 532–545, 632, 1367 (noise-key
schema history), 2048–2063 (the v3→v4 narrative), 2267–2274 (audit-key v1
history), and the `verify.py` fixtures that use superseded tags on purpose.

### 3 — The strengthened verifier

Round 7 added a forbidden **literal** list, and it was insufficient by
construction: it caught `dk-numerical-validation/v2` and missed all three real
statements, none of which names the schema. `check_readme` now applies a set of
**present-tense assertion patterns** to `README.md`, `killed_diffusion.py` and
`moving_band_audit.py` — the version *is*, the tag *reads*, "a v1 report", the
current/live report or schema *is* an earlier version, plus the fully-qualified
literals it already had. The superseded `terms // 2` description stays
README-only, because `killed_diffusion.py` explains at length why that test was
replaced and needs to say its name.

Historical wording passes without any marker: the patterns are present-tense
and assertive, so "v1 carried", "**v2.** The report shape changed", "in v1 it
did not" and "a v1 or v2 consumer must refuse this" do not match. Requiring a
marker comment would have made the check depend on somebody remembering to
write one.

**Ten fixtures pin both directions** and run inside the check: the three
original stale sentences plus two constructed variants must be caught, and five
pieces of genuine historical prose must pass. A pattern that rotted into
matching nothing would fail rather than pass silently — which is the failure
mode the literal list actually had.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 84 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 620,298,240 B max RSS |
| raw-run subprocess | oracle and audit absent from `raw_runner`'s module set |
| stale-prose scan | 0 hits across 3 sources; 10 fixtures held |
| documented counts | 210 callables / 697 invalid calls / 507 parameters / 85 checks |
| result files / git outside the package | none / byte-identical to the session-start snapshot |

### Preserved

Every implementation behaviour: scale-safe series arithmetic and the Péclet
boundary; the repaired case still returns `8.759717659060986e-05`; the 121-cell
high-precision sweep at worst ratio `5.107e-03`; schema-v4 rooted recomputation;
immutable byte-backed evidence and the refused TOCTOU sequence; bounded term
counts; the Unicode label and reason policy; folded bootstrap; injective
encoding; **unchanged caps**; pooled (1 reason) and per-regime (33 reasons)
`numerical_no_result`; bounded memory; raw isolation; every non-claim. No
exponent, population, detector-measurement or Born-rule claim exists anywhere
in the package.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
