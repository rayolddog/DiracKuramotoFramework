---
title: "Sprint 01 — round 2 handoff (Generator)"
kind: spec
---

# Sprint 01 — round 2 handoff

Written to disk because two attempts to deliver this by message were refused by a
content filter on the receiving side. The content is unchanged; only the delivery
medium is.

## Status

Round 1 returned FAIL on both the contract and the addressable rubric slices. That
verdict is accepted in full. All six findings were reproduced locally before any
change was made, and all six were valid.

## Root cause

Findings 1–4 were a single defect rather than four. Values were validated inside
their constructors and then left changeable afterwards:

- objects representing verified state had ordinary public constructors;
- measure weights were stored as plain mutable dictionaries;
- the raw-stage view retained a reference to the caller's own list;
- results carried an unrestricted free-text field that was serialized verbatim.

This is the same distinction raised during contract review — internal consistency
is not the same as checking against an independently held reference — one level
down, in the implementation. It was corrected in the contract and not carried into
the code.

The repair introduces two shared mechanisms in a new `_internal.py` and applies
them uniformly, rather than patching each site separately.

### Restart considered and declined

A restart from the pre-build checkpoint was weighed. The findings left the exact
type structure, the closed vocabularies, digest domain separation and gate
sequencing intact; what was absent was an enforcement layer over stored state. A
restart would have rebuilt the same design and discarded correct arithmetic. This
is recorded so the decision can be reviewed rather than assumed.

## Changes

| # | Change |
| --- | --- |
| 1 | `ManifestAuthoritative`, `DependencyGate`, `ClaimGate`, `Closed` and `FixtureRunPermit` can no longer be constructed directly. Each is produced only by the transition that earns it. `Closed` now carries `manifest_root`. `Frozen.close` requires exact gate types sharing one root; an object merely exposing `is_closed = True` is refused. `Supported` requires an exact `FixtureRunPermit` plus a lifecycle whose root matches it. |
| 2 | The free-text `detail` field is removed as an input. Results carry a `DetailCode` from a closed 14-member vocabulary plus a `context` mapping whose keys are fixed per code and whose values must be lowercase identifiers, 64-character hex digests, integers, or tuples of identifiers. Readable text renders from templates in the module. `deserialize_result` re-renders and compares byte-for-byte. No field accepts caller-authored prose, so the property is structural rather than a text scan. |
| 3 | `RawStageView` copies its input into a recursively immutable snapshot **before** checking it, and checks the snapshot. Later changes to the caller's own object cannot affect the view. |
| 4 | `_Immutable._set` recursively freezes every stored field into read-only mappings, tuples and frozensets. `FrozenInputSet` is permanently bound to the manifest it was built from, and `close()` now takes no argument, so reads taken against one manifest cannot be reconciled against another. |
| 5 | New `schema_io.decode_typed` rebuilds all 13 schema types through their real constructors with strict field sets. ATK-15 asserts exact type, equality and digest equality. ATK-16 confirms a rebuilt manifest is still not authoritative until checked against the independently held root. |
| 6 | NFC-equivalent row keys are refused rather than collapsed. Unpaired surrogates surface as `SerializationError`. |

### The environment-variable finding

Rather than only making the recursion marker internal, what it can achieve was
changed. It is now in-process state set by a private `--internal-recursion-guard`
argument that a parent adds when spawning a child. The environment variable is
still honoured, because a pytest child cannot be given a verify argument, but it
is treated as unauthorised: a run with unauthorised skips prints
`UNAUTHORIZED SKIP` and exits 1.

```text
BSEF_CHILD=1 python3.12 -m born_selection_equilibrium_fixture.verify   →  exit 1
```

The property that mattered was that an external setting cannot produce a passing
run. ATK-21 spawns that child and asserts the exit code.

## Check count

**217** — the 196 agreed checks plus a new 21-check `ATK` group, one per round-1
finding, kept permanently because each finding held while a full suite reported
green. Contract §7 needs a `217` addendum; the agreed document has not been edited,
since the record of what was agreed belongs to the Evaluator.

## Rerun evidence

Host: `python3.12` = 3.12.6 with pytest 9.0.2; `python3` = 3.13.11 without pytest.

| Command | Result |
| --- | --- |
| `python3 -m pytest -q born_selection_equilibrium_fixture/tests` | **217 passed in 3.86s**, no environment override |
| `python3 -m born_selection_equilibrium_fixture.verify` | 0 |
| `python3 -W error -m born_selection_equilibrium_fixture.verify` | 0 |
| `python3 born_selection_equilibrium_fixture/verify.py` | 0 |
| `python3 -m born_selection_equilibrium_fixture.verify --prove-failure-exit` | 1 |
| `python3 -m py_compile born_selection_equilibrium_fixture/*.py` | 0 |
| `python3 -m compileall -q born_selection_equilibrium_fixture` | 0 |
| unknown flag | 2 |
| `BSEF_CHILD=1 … verify` | 1 |
| supplemental `python3` (3.13.11) verify | 0 |

`--json` output is byte-identical across `PYTHONHASHSEED` 1 / 9999 / 7 and across
both interpreters (sha `5cce6b1e…`). Total runtime 3.85s, inside the 5s bound.

All six round-1 findings were re-checked independently outside the suite; each is
now refused.

## Files

New: `_internal.py`, `schema_io.py`, `tests/checks_attacks.py`.
Modified: `measures.py`, `provenance.py`, `dependency.py`, `freeze.py`,
`results.py` (rewritten), `authority.py`, `claims.py`, `isolation.py`,
`canonical.py`, `conditioning.py`, `verify.py`, and eight files under `tests/`.

27 files, 6,719 lines. Checkpoint
`autobuild-generator/checkpoints/sprint01-round2.tar.gz`,
sha256 `e22466f6fb7ebc11200d28ba36593324c05053512863f4897caea4cc83424ccf`.

## Two disclosures

**Six defects were caught by the suite during this repair.** One is worth knowing:
the parent run silently grew to two minutes because the child-marking helper
inspected only `args[0]`, so `-W error -m …verify` — which puts the module name at
index 2 — never received the marker, and its children re-ran the same subprocess
checks. Correcting that then broke `py_compile`, which receives `verify.py` as a
filename argument rather than as a command. Both are fixed; the runtime bound in
RUN-11 is what surfaced the first.

**The construction restrictions are an API-level property, not runtime isolation.**
Code that reaches into module-private names or calls `object.__setattr__` can still
build these objects directly. Python provides no way to prevent that, and the check
suite itself relies on it to construct test artefacts. The narrower claim being
made is: no sequence of documented public calls produces a verified-state object
that was not earned, or changes a value after validation. If that line sits in the
wrong place, it is better said now than after Sprint 2 depends on it.

## Reference

Clean manifest root, unchanged:

```text
751b8245df8b9c814934bee6d8873f17359628b0696812100635ccd4ed0346d7
```

Please capture it independently from a clean run before checking, rather than
taking it from this document.

Generator log: `autobuild-generator/generator-state.json`, 37 entries.
