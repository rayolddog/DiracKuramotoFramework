---
title: "Ticket 04 fix-up round 9 — live-schema wording boundary"
kind: ticket
status: 2
---

# Objective

Correct only the live-schema prose checker’s final false negatives and historical false positive.

## Required corrections

- The checker must reject these present-tense live-schema claims:
  - `Current report: v3`
  - `Live schema: v1`
  - `The report version is v2`
  - `Current version: v3`
  - `Validation schema: v2`
  - `This report uses v2`
- It must accept the clearly historical sentence `Before v4, the live schema was v3`.
- Add all seven exact sentences as discriminating fixtures.
- Keep the source scan clean and preserve legitimate migration history and deliberate old-version rejection tests.
- Do not change numerical code, scientific behavior, caps, or results.

## Completion gate

The same independent reviewer must return `CLOSED` after the fixture boundary and full unchanged verifier matrix pass.

## Implementation report — 2026-08-28

Checker text only. **No source prose, numerical code, cap or result changed** —
`verify.py` is the only file modified this round; `killed_diffusion.py`,
`moving_band_audit.py` and `README.md` still carry their round-8 bytes.
Canonical suite **85/85**, exit 0, 84 s. Of the 85 rows shared with round 8,
**84 carry byte-identical residuals**; only the memory row moved.

### The defect

All seven cases reproduced exactly before the change:

| Sentence | Before | Now |
| --- | --- | --- |
| `Current report: v3` | passed | rejected |
| `Live schema: v1` | passed | rejected |
| `The report version is v2` | passed | rejected |
| `Current version: v3` | passed | rejected |
| `Validation schema: v2` | passed | rejected |
| `This report uses v2` | passed | rejected |
| `Before v4, the live schema was v3` | **rejected** | accepted |

One pattern caused the false positive: `\bthe (?:current|live) (?:report|schema)\b[^.]{0,60}?\bv[123]\b`. Its `[^.]{0,60}` filler
spans anything without a period — including a past-tense verb — so it could not
tell a claim from a history. The six misses were the mirror image: four
hand-written patterns, each written for a sentence a review had already found,
matching phrasings rather than the construction underneath them.

### The fix

Enumerating sentences was the mistake, so the grammar is now what is matched.
A stale claim is a **subject naming the live artifact**, a **present-tense**
**link**, and an **earlier version**, in that order:

```
\b(?:current|live|validation|schema|report|this|the)\s+
(?:report|schema|version|tag)\s*
(?::|=|\b(?:is|are|uses|reads|carries|remains|stays)\b)\s*
[`'"*]{0,3}\s*v[123]\b
```

- The subject is two words from a closed vocabulary, which covers "the tag",
"report version", "validation schema" and every other pairing without
listing them.
- The link is present tense, or a colon or equals sign standing in for one.
`was`, `were`, `carried` and `had` are absent **by construction** — that
single omission is the entire distinction, and it is why the historical
sentence passes while `the live schema is v1`, one word away, does not.
- The version follows the link immediately; only quoting may intervene. So
"the schema is v4, which replaced v3" is about v4 and does not match.

Two patterns are kept beside it: `\ba v[123] report\b`, because that sentence
puts the version before its subject where the grammar cannot see it, and the
fully-qualified `dk-numerical-validation/v[123]`, which needs no grammar around
it to be wrong. The README-only `terms // 2` rule is unchanged.

### Fixtures

**17 fixtures, run inside `check_readme`** — up from 10. All seven ticket
sentences are present verbatim: the six live claims must be rejected, and
`Before v4, the live schema was v3` must be accepted. Eleven stale, six
historical. Each is asserted in both directions, so a pattern that stopped
matching fails rather than passing silently.

### Scan scope

The scan covers `README.md`, `killed_diffusion.py` and `moving_band_audit.py`,
and reports **0 hits**. The broader grammar introduced no false positive on any
real prose: the migration blocks, the noise-key and audit-key histories, and
the v3→v4 narrative all still pass.

`verify.py` is deliberately excluded, and this round proved it must be — running
the grammar over it returns 25 hits, every one of them the fixture table, the
comment quoting the stale sentences, or a deliberate old-tag rejection mutation
(`dk-numerical-validation/v1` payloads that must be refused). That exclusion,
and its cost — prose inside `verify.py` is not covered — is now stated at
`_PROSE_SOURCES` rather than left implicit.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 84 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 649,953,280 B max RSS |
| seven ticket sentences | 6 rejected, 1 accepted, all 7 present as fixtures |
| stale-prose scan | 0 hits across 3 sources; 17 fixtures held |
| raw-run subprocess | oracle and audit absent from `raw_runner`'s module set |
| documented counts | 210 callables / 697 invalid calls / 507 parameters / 85 checks |
| result files / git outside the package | none / byte-identical to the session-start snapshot |

### Preserved

Every implementation behaviour and every documented result: scale-safe series
arithmetic and the Péclet boundary (repaired case still
`8.759717659060986e-05`); the 121-cell high-precision sweep at worst ratio
`5.107e-03`; schema-v4 rooted recomputation; immutable byte-backed evidence and
the refused TOCTOU sequence; bounded term counts; the Unicode label and reason
policy; folded bootstrap; injective encoding; **unchanged caps**; pooled
(1 reason) and per-regime (33 reasons) `numerical_no_result`; bounded memory;
raw isolation; every non-claim. No exponent, population, detector-measurement or
Born-rule claim exists anywhere in the package.

Only `adler_born_two_channel/verify.py` and this artifact were modified; nothing
staged, committed or reverted.
