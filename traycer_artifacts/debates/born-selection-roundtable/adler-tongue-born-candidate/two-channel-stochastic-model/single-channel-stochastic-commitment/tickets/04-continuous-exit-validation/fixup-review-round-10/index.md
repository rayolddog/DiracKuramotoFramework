---
title: "Ticket 04 fix-up round 10 — version-first historical tense"
kind: ticket
status: 2
---

# Objective

Make the remaining version-first schema pattern distinguish current claims from historical prose.

## Required corrections

- These historical sentences must pass:
  - `Before v4, a v3 report was accepted`
  - `Historically, a v2 report carried one envelope`
  - `A v1 report had no dataset digest`
  - `A v3 report was replaced by v4`
- Remove or replace the unconditional `a v1/v2/v3 report` fallback.
- Retain detection of genuinely current version-first claims, with positive fixtures such as:
  - `A v2 report is the current format`
  - `A v3 report defines the live schema`
  - `A v1 report remains active`
- Add all historical and current forms as discriminating fixtures.
- Preserve every source file and all numerical behavior except checker code/comments.

## Completion gate

The independent reviewer must return `CLOSED` after the exact fixtures and unchanged full matrix pass.

## Implementation report — 2026-08-28

Checker code and comments only. **`verify.py` is the only file modified** —
`README.md`, `killed_diffusion.py` and `moving_band_audit.py` still carry their
round-8/round-9 bytes. Canonical suite **85/85**, exit 0, 85 s. Of the 85 rows
shared with round 9, **84 carry byte-identical residuals**; only the memory row
moved.

### The defect

All four historical sentences were rejected before the change, and the three
current claims were "caught" only because the rule matched unconditionally:

| Sentence | Before | Now |
| --- | --- | --- |
| `Before v4, a v3 report was accepted` | rejected | **accepted** |
| `Historically, a v2 report carried one envelope` | rejected | **accepted** |
| `A v1 report had no dataset digest` | rejected | **accepted** |
| `A v3 report was replaced by v4` | rejected | **accepted** |
| `A v2 report is the current format` | rejected | rejected |
| `A v3 report defines the live schema` | rejected | rejected |
| `A v1 report remains active` | rejected | rejected |

The rule was `\ba v[123] report\b` — a bare noun phrase. It fired on every
sentence containing that phrase, historical or not, which means it could not be
said to have detected the three current claims at all: a rule that also fires on
all four true statements is carrying no information.

### The fix

The unconditional fallback is **removed**, replaced by
`_STALE_VERSION_FIRST_CLAIM`, which applies the discriminator already
established for version-last order in round 9: **tense**. A present-tense
predicate asserts the report is that version now; a past or perfect one recounts
that it was.

```
\ba v[123]\s+(?:report|schema)
(?:\s+(?!was\b|were\b|had\b|has\s+been\b|used\s+to\b)\w+)?\s+
\b(?:is|are|remains|stays|carries|defines|uses|has|holds|provides|
contains|names|declares)\b
(?!\s+(?:been|no\s+longer|superseded|obsolete|deprecated|replaced|gone))
```

Two refinements make the tense test hold in real prose:

- **One optional word** may sit between subject and predicate, so "a v2 report
*always* carries" is still caught — but that word may not be `was`, `were`,
`had`, `has been` or `used to`, or the gap would let a past-tense sentence
reach a later present-tense verb.
- **A retirement predicate is history**, even in the present tense: "has been
superseded", "is no longer accepted", "is deprecated" are all excluded by a
trailing lookahead.

The third of the three sentences an independent review originally found —
`The exact top-level keys a v2 report carries` — is still rejected, by
`carries`. That was the sentence the unconditional rule existed for, and it
survives the tightening.

### Cost, stated

This rule reads **tense**, so a current claim written in the past tense would
pass. That is the same bet the version-last grammar makes, and it holds only
because this package writes its history in the past tense. The fixtures pin
that convention from both directions rather than leaving it as an assumption.

### Fixtures

**28 fixtures, up from 17** — 15 stale, 13 historical — all run inside
`check_readme`. The seven ticket sentences are present verbatim. Four more were
added beyond the ticket to pin the refinements: `a v2 report has been superseded`, `a v3 report is no longer accepted` and `a v1 report used to carry a single envelope` must pass; `a v2 report always carries one envelope` must
fail.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 85 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 626,343,936 B max RSS |
| seven ticket sentences | 4 accepted, 3 rejected, all 7 present as fixtures |
| three original stale sentences | all still rejected |
| stale-prose scan | 0 hits across 3 sources; 28 fixtures held |
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
