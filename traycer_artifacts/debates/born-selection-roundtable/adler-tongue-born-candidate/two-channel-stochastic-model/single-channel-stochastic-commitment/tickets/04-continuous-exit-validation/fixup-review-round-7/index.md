---
title: "Ticket 04 fix-up round 7 — immutable byte evidence and final boundary hygiene"
kind: ticket
status: 2
---

# Objective

Eliminate the remaining writable-owner path and close two bounded public-contract/documentation gaps without altering any numerical result or cap.

## Required corrections

### 1. Store authoritative observations in genuinely immutable backing

- Reproduce `sample.values.base.setflags(write=True)` and the mapping-subclass mutation that changes no-result evidence into pass evidence before parser snapshotting.
- Do not rely on NumPy write flags when a public `.base`, buffer owner, or view chain can reach writable memory.
- Store the authoritative observation bytes in an immutable object (`bytes` or an equivalently non-writable canonical representation), together with bound dtype, byte order, shape, arm role, and dimensions.
- Any array exposed for computation must be reconstructed from immutable backing or be an untrusted copy; mutating it or traversing `.base` must not alter the authoritative evidence, digest, or later recomputation.
- `PairedSample` and `ValidationDataset` digests must derive from immutable backing only. Parser recomputation must operate from the same immutable snapshot.
- Add attacks through `.base`, repeated `.base` traversal, `setflags`, `memoryview`, buffer interfaces, source aliases, derived arrays, mapping callbacks during serialization, and post-construction metadata mutation.
- Prove the exact reviewer TOCTOU sequence is harmless or refused and that valid datasets remain deterministic.

### 2. Bound term counts before numeric conversion

- All public series helpers must validate term count as an integer within a documented finite operational maximum before any float conversion, array allocation, multiplication, or loop.
- `terms = 10**400` must raise the named public exception, never bare `OverflowError`, in survival, certificate, and truncation-bound APIs.
- Test booleans, negative/zero, huge integers, platform-sized boundaries, and the exact maximum/maximum-plus-one controls.

### 3. Finish label and documentation consistency

- Apply the shared Unicode label policy to ordinary `reasons` strings as well as blocking rows and identity fields in both inspection and rooted parsing.
- Test Cc/Cf/Cs/Co/Cn characters in reasons plus valid non-ASCII reasons.
- Correct every stale schema reference; README and source must identify the current report as v4 and mechanically forbid the stale “v2” sentence in the relevant section.

## Verification contract

- Preserve the closed scale-safe series behavior, Péclet boundary, high-precision certificate sweep, schema-v4 recomputation, folded bootstrap, unchanged caps, pooled/per-regime no-results, memory bound, raw isolation, and all scientific non-claims.
- Run canonical, verbose, direct-script, warnings-as-errors, deliberate-failure, compile, hash-seed, RSS, TOCTOU/buffer attacks, raw-isolation, and no-file paths.

## Completion gate

Round 7 is complete only after the same reviewer returns `CLOSED`. No public object graph may reach mutable authoritative observation memory, and no oversized integer or forbidden label may escape through an incidental runtime error or policy gap.

## Implementation report — 2026-08-28

Canonical suite **85/85**, exit 0, 85 s, peak RSS 664 MB. Of the 85 rows shared
with round 6, **84 carry byte-identical residuals**; only the memory row moved.
No row renamed. Pooled `numerical_no_result` (1 reason), per-regime
`numerical_no_result` (33 reasons) and the passing S3 gate preserved under
**unchanged caps**.

### 1 — Immutable byte-backed evidence

`_sealed` no longer returns a read-only view of an owned array. It
canonicalizes to little-endian binary64, serializes to a `bytes`, and
reconstructs with `np.frombuffer`. The base chain is now

```text
ndarray(writeable=False, owndata=False)
  -> ndarray(writeable=False, owndata=False)
    -> bytes
```

with **no writable owner anywhere in it**. The review's exact probe:

| Attack | Before | After |
| --- | --- | --- |
| direct write | refused | refused |
| `values.setflags(write=True)` | refused | refused |
| `values.base.setflags(write=True)` + write | **SUCCEEDED** | refused (`ValueError`) |
| `values.base.base.setflags` | n/a | refused (`AttributeError`, it is `bytes`) |
| `memoryview` write | refused | refused |
| dataset digest after the attack | changed | unchanged |

The mapping-subclass TOCTOU is refused. Its `items()` callback now walks six
links of the base chain calling `setflags`/`[...] = 0` at each, fires during the
parser's serialization, and the dataset is unchanged afterwards — the parser
also takes its trusted snapshot **before** any untrusted payload method runs, so
the window is removed rather than merely made harmless.

The digest binds dtype, byte order and arm role alongside the shape and bytes.

### 2 — Bounded term count

New `MAX_SERIES_TERMS = 1_000_000`, validated **before** any float conversion or
allocation. `terms = 10**400` and `10**100` now raise the named `ValueError` in
all three public helpers instead of a bare `OverflowError: int too large to convert to float` or NumPy's generic `Maximum allowed size exceeded`. Booleans
raise `TypeError`, zero and negatives `ValueError`, and the declared maximum
itself still evaluates — asserted as a positive control so the bound is a
maximum rather than a blanket refusal.

### 3 — Reason policy and documentation

`_require_reason` applies the shared Unicode category policy, so all six
forbidden categories in an ordinary reason are refused by both the inspector and
rooted parsing, while ordinary non-ASCII reason text is accepted (positive
control). `check_readme` now carries a **forbidden-phrase list** — the stale
`dk-numerical-validation/v1|v2|v3` strings and the superseded `terms // 2`
description — so prose that has stopped being true fails a check rather than
waiting to be read.

### Verification matrix

| Command | Result |
| --- | --- |
| `python3 -m adler_born_two_channel.verify` | 85/85, exit 0, 85 s |
| `--verbose` / direct script / `-W error` | 85/85 each |
| `--prove-failure-exit` | exit 1 |
| `compileall` | clean |
| `PYTHONHASHSEED` 0 vs 987654321 | 84 of 85 rows byte-identical |
| `/usr/bin/time -l` | 664,469,504 B max RSS |
| base-traversal / memoryview / callback attacks | all refused; digest unchanged |
| `terms` bounds | named refusals; declared maximum still evaluates |
| high-precision sweep | 121 cells, worst error/certificate ratio 5.107e-03 |
| raw-run subprocess | oracle and audit absent |
| result files / unexpected git changes | none / none |

### Preserved

Scale-safe series behaviour and the Péclet boundary; the repaired case still
returns `8.759717659060986e-05`; schema-v4 rooted recomputation; folded
bootstrap; injective encoding; unchanged caps; pooled and per-regime
`numerical_no_result`; bounded memory; raw isolation; every non-claim. No
exponent, population, detector-measurement or Born-rule claim exists anywhere.

Only `adler_born_two_channel/` and this artifact were modified; nothing staged,
committed or reverted.
