---
title: "Independent review — ticket 01 raw-process isolation"
kind: review
---

# Verdict

**OPEN — three actionable boundary defects remain.** The canonical suite passes 32/32 and the six reviewed source files remained byte-identical during review, but focused probes found false-negative isolation mutations, an opaque-payload route through configuration subclasses, and a ledger gate that trusts unbound/mutable marker metadata.

## High — the structural verifier misses forbidden object bindings and multiplication-form squares

**Where:** `verify.py:1549-1599`, mutation coverage at `verify.py:2191-2225`.

`_scan_source` checks `ast.Name`, `ast.Attribute`, and `Pow`, but not binding positions such as `FunctionDef.name` or imported `ast.alias` names. An out-of-tree mutant that defined `def hazard(...)` in `raw_config.py` and imported it with `from .raw_config import hazard as event_rule` in `raw_runner.py` returned **no graph problems**. This is a valid forbidden object-level dependency hidden behind an allowed module import. A second mutant computing `coupling * coupling` also returned no problems, contradicting the verifier/README claim that banning exponentiation means a raw module cannot form a squared coupling.

The conventional direct, two-hop, package-root, eager-root, star, and `importlib`/`__import__` mutants are caught, and the refactored `from . import X` branch correctly treats `X` as a module. The gap is the object imported *from* an allowed module and binding forms the AST visitor never inspects.

**Action:** scan every relevant binding position (`ast.alias.name/asname`, function/class names, arguments, assignment targets) against the forbidden vocabulary; distinguish allowed module traversal from imported-object validation; and replace the “no `Pow` means no square” claim with an enforceable rule. Add both demonstrated mutants to the live mutation battery.

## High — `validate_raw_config` preserves subclasses carrying arbitrary payloads

**Where:** `raw_runner.py:104-106`; configuration contract at `raw_config.py:295-350`.

The entry point uses `isinstance` and then `dataclasses.replace`, which preserves the dynamic class. A frozen dataclass subclass adding `predictor: object` was accepted, rebuilt as the same subclass, and retained the identical opaque predictor object. The boundary therefore does not guarantee that a run receives only the declared `RawEventConfig` fields, even though ordinary mappings, callables, arrays, unknown/non-string keys, booleans, non-finite values, forbidden predictor/hazard/amplitude/intensity names, and mutated base dataclasses are otherwise refused correctly.

**Action:** require exact `RawEventConfig` type at the runner boundary and rebuild an exact base instance from an explicit field allowlist. Apply the same exact-type policy to nested boundary types where subtype behavior could affect later event generation. Add dataclass and ordinary subclass probes.

## Medium — the closed-ledger gate does not validate the marker claims it returns

**Where:** `raw_ledger.py:105-151`, `raw_ledger.py:154-179`.

`require_closed_ledger` checks only payload non-emptiness and `content_digest`. The same two-row payload was accepted with `row_count` 1, 2, and 999. After construction, `object.__setattr__` changed a marker to `schema_version=999`, `row_count=0`, and `manifest_digest="not-a-digest"`; the gate still accepted and returned it. Thus the read boundary can return a marker asserting an unsupported schema, impossible trial count, and invalid manifest digest. It also provides no operation that binds `manifest_digest` to the manifest bytes. The SHA-256 bytes boundary itself is correct against an independent `hashlib.sha256` oracle, and text, empty, truncated, appended, and flipped payloads fail as documented.

**Action:** revalidate/canonicalize an exact `CloseMarker` at read time, bind the declared trial count to either independently parsed ledger rows or the frozen manifest’s expected trial count, and verify the supplied manifest bytes against `manifest_digest`. Add wrong-positive-count and post-construction-mutation probes.

# Evidence

- `python3 -m adler_born_two_channel.verify`: **32/32 pass** (Python 3.12.6, NumPy 2.3.5).
- `python3 -m adler_born_two_channel.verify --verbose`: **32/32 pass**, 77 output lines.
- `python3 adler_born_two_channel/verify.py`: **32/32 pass**.
- `PYTHONWARNINGS=error python3 -m adler_born_two_channel.verify`: **32/32 pass**, warning-clean.
- `python3 -m adler_born_two_channel.verify --prove-failure-exit`: **exit 1**, 32/33 with the deliberate probe failing.
- Fresh-import probe: bare package import loaded only `adler_born_two_channel`, bound no public attributes, and `pkg.analytic` raised `AttributeError`; explicit analytic import remained compatible.
- Declared counts are accurate: 32 registered checks, 26 acceptance criteria, and the public matrix independently reports 66 callables / 219 invalid calls / 134 parameters. README correctly distinguishes the original 26 checks from six isolation checks and makes no stochastic-event or Born claim.
- Pre-authorizing `model` is not itself a finding: the governing plan requires calibrated Adler drift later, check 12 independently constrains `model`, and the current raw graph does not reach it. The permission does enlarge the future boundary, so the object-import fix above must apply before that edge is used.
- The original deterministic residuals printed by the current suite match the recorded README values, including wrapping `8.452e-15`, relaxation `4.142e-06`, normalization `1.370e-05`, flux `2.104e-05`, and exponent `8.604e-07`.
- Pre/post SHA-256 hashes of `__init__.py`, `raw_config.py`, `raw_ledger.py`, `raw_runner.py`, `verify.py`, and `README.md` were identical. The package remains wholly untracked; no implementation file was edited, staged, committed, or reverted.

# Closure re-review — fix-up 1 — 2026-08-26

## Verdict

**OPEN — the configuration finding is closed, but two bounded defects remain.** The fix correctly closes the originally demonstrated object-import, direct self-multiplication, subclass, marker-mutation, and manifest-digest cases. Independent probes found one realistic square spelling and one binding family still outside the scanner, and confirmed that caller-supplied `expected_rows` is not actually bound to the verified manifest.

## High — the narrowed syntactic/binding claims still have direct false negatives

**Where:** `verify.py:1555-1691`; reported guarantee at `verify.py:1962-1972` and `README.md:258-282`.

The original `def hazard` / `from .raw_config import hazard as event_rule` mutant now fails twice, `coupling * coupling` fails, `coupling *= coupling` fails, and `np.square(coupling)` fails. However:

- `np.multiply(coupling, coupling)` returns **no graph problems**. In a NumPy-vectorized raw process this is a normal, direct syntactic spelling of the same self-product, so it falls inside the stated “may not write a square” guard rather than the documented alias/data-flow limitation.
- A match-pattern binding is not inspected. `case {"value": hazard}: return locals()` returns **no graph problems** even though it binds a banned name and exposes the bound object through the returned locals mapping. `ast.MatchAs.name`, `ast.MatchStar.name`, and `ast.MatchMapping.rest` are string binding positions, like `ExceptHandler.name`, not `ast.Name` nodes.

The documented `a = coupling; b = coupling; a * b` limitation is accurate and is not itself a finding. Applying the same syntactic rule to `model.py` and `simulate.py` causes no current regression: both remain warning-clean and their prior deterministic residuals are unchanged. The current defect is that the implementation and “every binding position” / direct-syntactic-square claims do not yet match.

**Bounded fix:** recognize calls to allowed multiplication helpers such as `numpy.multiply` when the two operands have the same AST expression, inspect Python pattern-binding string fields, and add the two mutants above. Keep the existing data-flow limitation language; no semantic analyzer is required.

## Medium — `expected_rows` can simply repeat the marker and contradict the verified manifest

**Where:** `raw_ledger.py:162-254`; self-check at `verify.py:2752-2768` and `verify.py:2863-2879`; claim at `README.md:361-370`.

Marker reconstruction, exact marker type, manifest digest verification, and ordinary expected-count disagreement are fixed. The remaining issue is provenance: the gate accepts whatever positive integer the caller labels `expected_rows`; it never reads that value from `manifest`.

Exact reproduction: with a two-row payload and verified manifest bytes `{"run_label":"pilot","trials":2}`, construct a marker with `row_count=999` and pass `expected_rows=999`. `require_closed_ledger(...)` accepts. It also accepts an **empty manifest** whose digest matches the marker when the caller supplies 999. Thus the gate proves only that two caller-supplied integers agree, not that the declared count agrees with the verified manifest. The self-check's comment `expected_rows = 2  # as read from the manifest above` supplies the relationship rather than testing it.

**Bounded fix:** either parse and validate the manifest's canonical trial-count field inside this gate (or accept an exact validated manifest object whose canonical bytes are what is hashed), or explicitly defer the trial-count guarantee until that parser exists and remove the current binding claim/API check. Counting parsed ledger rows can remain a later-ticket strengthening.

## Closed — exact configuration types and clean rebuilds

`validate_raw_config` now rejects both frozen-dataclass and ordinary `RawEventConfig` subclasses, rejects `RawClockGrid` subclasses at construction and after mutation, rebuilds an exact base configuration/grid, drops an opaque attribute injected into an exact base instance, and revalidates post-construction NaN edits. No actionable configuration-boundary defect remains.

## Re-run evidence

- `python3 -m adler_born_two_channel.verify`: **32/32 pass** (Python 3.12.6, NumPy 2.3.5).
- `python3 adler_born_two_channel/verify.py`: **32/32 pass**.
- `PYTHONWARNINGS=error python3 -m adler_born_two_channel.verify`: **32/32 pass**.
- `python3 -m adler_born_two_channel.verify --verbose`: **32/32 pass**; built-in mutation battery reports 18/18 caught; public matrix reports 67 callables / 232 invalid calls / 137 parameters, matching README.
- Direct ledger probes: valid input returns an equal, distinct exact `CloseMarker`; marker subclass, mutated schema/count/digests, wrong manifest, and ordinary expected-count mismatch all reject with the documented type.
- Fix-up source hashes were recorded before probing and remained unchanged afterward. The package remains wholly untracked; no implementation file was edited, staged, committed, or reverted.

# Closure re-review — fix-up 2 — 2026-08-26

## Verdict

**OPEN — both prior exact reproductions are fixed, but two narrow claim-level defects remain.** Plain `np.multiply(x, x)`, all requested match bindings, and manifest-derived authoritative trial counts now work as intended. Keyword-bearing multiply calls still evade the stated direct syntactic guard, and duplicate JSON member names evade the stated exact three-field manifest schema.

## Medium — direct `np.multiply` self-products with keyword options are missed

**Where:** `verify.py:1547-1551`, `verify.py:1617-1628`, `verify.py:1710-1717`; claim at `README.md:275-297`.

Independent results:

- `np.multiply(x, x)` is caught.
- `np.multiply(x, y)` is accepted, so unequal multiplication is not overblocked.
- `np.multiply(x, x, where=mask)` is **missed**.
- `np.multiply(x1=x, x2=x)` is **missed**.

The `ast.Call` rule requires exactly two positional arguments **and no keywords**. `where=` is an ordinary NumPy ufunc option and does not change the fact that the call directly writes a self-product. This falls within the documented named-multiplication/identical-operands guard, not its accurately disclosed alias, spread-argument, or data-flow limitations.

All requested unread pattern cases now fail independently: `MatchAs.name`, `MatchStar.name`, `MatchMapping.rest`, and `MatchClass.kwd_attrs`. The claim remains correctly syntactic; no semantic analyzer is needed.

**Bounded fix:** inspect the first two positional operands even when unrelated keyword options are present, and separately recognize the `x1=`/`x2=` spelling. Retain the unequal-operand control and add both mutants.

## Medium — duplicate manifest member names bypass the exact three-field schema

**Where:** `raw_ledger.py:254-300`; schema claim at `raw_ledger.py:92-102` and `README.md:387-406`.

`json.loads` collapses duplicate object names before the key-set check. Both of these digest-bound manifests are accepted:

```json
{"schema_version":1,"run_label":"pilot","trials":2,"trials":999}
{"schema_version":1,"run_label":"pilot","trials":999,"trials":2}
```

The accepted authoritative count is whichever duplicate appears last. Duplicate names are not insignificant formatting: different readers may choose the first, last, or reject, and the bytes contain four members despite the version-1 claim of exactly three fields. Canonical output is unique, but the reader deliberately accepts noncanonical formatting, so it must distinguish harmless whitespace/order from ambiguous duplicate declarations.

**Bounded fix:** parse with an `object_pairs_hook` that rejects duplicate names before constructing the mapping, and add first/last duplicate-trial mutants. Continue accepting reordered and whitespace-varied objects with three unique names.

## Closed regressions

- Plain `np.multiply(x, x)` and unread banned names in `MatchAs`, `MatchStar`, `MatchMapping.rest`, and `MatchClass` keyword attributes are caught; direct unequal multiplication passes.
- `require_closed_ledger(payload, marker, manifest)` has no caller count parameter. It verifies the exact manifest bytes against the reconstructed exact marker, parses an exact `RawManifest`, and rejects manifest-trials 2 / marker-row-count 999, empty and count-free manifests, unknown fields, wrong field types, unknown schema/run label, changed bytes, marker mutation, and marker subclasses.
- Canonical manifest bytes round-trip; noncanonical whitespace/key order is accepted when its own exact bytes are digest-bound; changing those bytes under the old marker fails.
- The row-level limitation is accurate: a manifest/marker declaring two can accompany payload bytes containing one data row because ledger parsing is explicitly a later ticket. The documentation says exactly that and makes no stronger claim.
- Exact `RawEventConfig` / `RawClockGrid` subtype rejection and clean explicit rebuild remain closed.

## Re-run evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **32/32 pass**.
- `--prove-failure-exit`: **exit 1**, 32/33 with the deliberate failure.
- Verbose mutation battery: **23/23 caught**; public matrix: **70 callables / 243 invalid calls / 141 parameters**, matching README.
- Deterministic residuals remain unchanged: wrapping `8.452e-15`, relaxation `4.142e-06`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`.
- Pre/post source hashes are identical; the package remains wholly untracked and no implementation file was edited, staged, committed, or reverted.

# Final narrow closure review — edge-case fix — 2026-08-26

## Verdict

**CLOSED — no actionable current defect remains.** The edge-case patch closes both findings from fix-up 2 without widening the documented guarantees beyond what the implementation enforces.

## Independent edge probes

- The raw graph rejects direct self-products written as `np.multiply(x, x, where=mask)`, `np.multiply(x1=x, x2=x)`, `np.multiply(x, x2=x)`, and `np.multiply(x1=x, x2=x, where=mask)`. It also rejects positional, `a=`/`b=`, mixed, and option-bearing self-products through `dot`, `inner`, and `outer`.
- Unequal positional, keyword, mixed, and option-bearing controls through the same helpers are accepted. The explicit alias case `a=x; b=x; np.multiply(a,b)` is accepted, matching the accurately stated direct-syntax/no-dataflow limitation rather than contradicting it.
- Independent `MatchAs`, `MatchStar`, `MatchMapping.rest`, and `MatchClass` keyword-pattern mutants still reject unread forbidden names.
- Digest-bound manifests with duplicate `trials`, `schema_version`, or `run_label` members reject during `object_pairs_hook` parsing. Both value orders and equal-value duplicates reject. Canonical bytes and unique reordered/whitespace bytes pass with their own exact digests; a byte change under the old marker fails.
- The prior ledger closure remains intact: no caller count parameter exists; manifest trials 2 / marker row count 999, empty and count-free manifests, unknown fields, wrong types/schema/run label, marker mutation, and marker subclasses reject. The exact three-field schema and the limitation that row contents are not yet parsed are stated explicitly, so a manifest-bound count is not overclaimed as row-count verification.
- Exact `RawEventConfig` and `RawClockGrid` enforcement remains closed: subclasses reject, post-construction non-finite mutation rejects, exact inputs rebuild to distinct exact base instances, and an opaque attribute injected into an exact base object is dropped.

## Re-run evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **32/32 pass**.
- `--prove-failure-exit`: **exit 1**, 32/33 with only the deliberate probe failing.
- Verbose mutation battery: **27/27 leaking packages rejected** and all **6 controls accepted**. Public matrix: **70 callables / 245 invalid calls / 141 parameters**, matching README.
- Deterministic residuals are unchanged, including wrapping `8.452e-15`, stable arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, outside-tongue slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, and exponent `8.604e-07`.
- Pre/post SHA-256 hashes of `__init__.py`, `raw_config.py`, `raw_ledger.py`, `raw_runner.py`, `verify.py`, and `README.md` are identical. The package remains wholly untracked; review used temporary directories only and edited no implementation file.
