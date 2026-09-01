---
title: "Independent review — ticket 02 keyed Brownian tree"
kind: review
---

# Verdict

**OPEN — five actionable defects remain.** The current verifier passes **38/38**, including all 32 pre-ticket checks with their recorded residuals unchanged and all six Ticket 02 checks. Independent distributional and mutation probes support the central Gaussian and conditional-split construction. The remaining defects are at the exact contracts the built-in checks do not join together: canonical per-leaf identity, irregular-leaf refinement, direct split geometry, representable numerical range, and unsigned clock validation.

## High — the public leaf key collides for all 1,024 leaves in a block

**Where:** `stochastic.py:560-573`, consumed at `stochastic.py:617-631`; documented schema at `README.md:465-494`.

`leaf_key(trial, clock, index)` is documented as the immutable key of one finest-grid kick, but it returns only `block=index//1024`. Consequently indices 0, 1, and 1023 return the same string; only the hidden offset used later by `_normals` distinguishes their values. A key therefore does not identify one elementary kick, contrary to the ticket and plan schema, and a manifest or audit record that stores the public key cannot reconstruct which of the 1,024 values it meant.

Exact probe:

```python
from adler_born_two_channel.stochastic import *
s = PhaseNoiseStream("probe", FinestMesh(0.0, 0.01), 0.1)
print([s.leaf_key(1, 2, i) for i in (0, 1, 1023, 1024)])
```

The first three strings end in `block=0`; only two unique strings are returned. The 1,024-value generation optimization itself is compatible with window and order invariance, but the canonical leaf address must include an offset (or full step index) in addition to the block seed.

**Bounded fix:** distinguish the private block seed from the public leaf address. For example, add a private `block_key`, make `leaf_key` include `block` plus `offset` or `step`, and have the value derivation resolve that address to the block draw. Add an all-1,024 uniqueness assertion and cross-block controls without changing the existing values unless the schema version is deliberately bumped.

## High — coarse refinement never sums the irregular elementary leaves

**Where:** `stochastic.py:660-683`; verifier coverage at `verify.py:3645-3735` and `verify.py:3880-3911`.

The plan defines the elementary mesh as the frozen uniform grid **union exact crossings** and requires every coarse increment to be a sum of those same leaves. `coarse_kicks` only fetches unsplit uniform root kicks and reshapes them; it cannot accept crossing geometry or `TreeLeaf` values. The verifier separately proves root-to-coarse summation and root-to-descendant conservation, but never proves a coarse increment is formed from the actual irregular leaves consumed by the fine path.

Directly, two uniform roots gave `0.0096509863441379`, while summing their four actual split descendants gave `0.009650986344137902` (difference `1.734723475976807e-18`). The small residual is not the main issue: the production API has no irregular-leaf coarse aggregation path, so later refinement code can silently use root sums while fine dynamics consumes crossing leaves.

**Bounded fix:** add a bounded/streamed coarse-tree API that accepts the frozen per-step crossings (or already materialized leaf iterator), constructs the exact elementary leaves in chronological order, and sums those leaves for every coarse rung. Add a test with crossings in multiple finest steps that compares the coarse result to the exact same `TreeLeaf.kick` sequence used by the fine consumer, including arbitrary windows.

## Medium — the public split primitive accepts inconsistent crossing geometry and identity

**Where:** `stochastic.py:719-778`; geometry validation exists only in `split_leaf` at `stochastic.py:780-848`; verifier refusal at `verify.py:4042-4053` exercises only `split_leaf`.

`split_kick` validates the fraction and that the crossing names the same clock, but it never binds `crossing.time` to `index`, `duration`, `fraction`, or the node interval. Both of these calls succeed:

```python
# step 4 is [0.04, 0.05]
s.split_kick(parent, 0.01, 0.5, 0, 5, 4, "",
             Crossing(5, "falling", digest, 99.0))
s.split_kick(parent, 0.01, 0.75, 0, 5, 4, "",
             Crossing(5, "falling", digest, 0.0425))
```

The first crossing is outside the parent; the second identity says one-quarter while the supplied fraction says three-quarters. Both consume a split key based on the inconsistent identity. That contradicts the requirement that invalid geometry and inconsistently identified crossings fail loudly.

**Bounded fix:** make the arithmetic primitive private and expose only the geometry-validating tree operation, or pass the node's exact start/end into the public method and derive the fraction from `crossing.time` rather than accepting it independently. Add both probes above to the public-boundary matrix.

## Medium — extreme finite inputs produce non-finite scales and a vacuous ULP bound

**Where:** `stochastic.py:375-390`, `stochastic.py:545-552`, `stochastic.py:597-600`, and the split scale at `stochastic.py:773-778`.

The boundary accepts any finite nonnegative diffusion, but intermediate multiplication is not range-checked. With `D = sys.float_info.max` and `h = 1`, `leaf_scale` is `inf`, so ordinary finite standard normals become non-finite kicks despite the public finite-input contract. Separately, `conservation_tolerance(sys.float_info.max)` is `inf` because `np.spacing(max_float)` overflows; any conservation error then passes that bound. Tiny/subnormal, ordinary, `1e300`, and cancellation-scale probes behave, but the top finite regime does not.

**Bounded fix:** reject a stream or split whose declared `2*D*h` is not finite and representable (or compute the scale with an overflow-safe factorization and still reject a non-finite variance). Use `math.ulp(scale)` or an equivalent finite endpoint treatment for the ULP bound, and require the returned tolerance itself to be finite. Add max-float, near-max, subnormal, large-cancellation, and overflow-product cases.

## Medium — unsigned clock arrays above `int64` silently wrap into negative keys

**Where:** `stochastic.py:227-258`, used at `stochastic.py:646-657`.

The array validator checks negativity before converting to `int64`. An unsigned value `np.uint64(2**63)` is nonnegative, passes, then `astype(np.int64)` wraps it to `-9223372036854775808`. `leaf_kicks` accepts the call and generates the stream for that negative serialized clock. Scalar APIs do not accept a negative clock, so the vector and scalar boundaries disagree and the claimed nonnegative identifier grammar is broken.

Exact probe:

```python
s.leaf_kicks(1, np.array([2**63], dtype=np.uint64), 0, 1)
```

The returned value matches `_normals(..., clock=-2**63, ...)` after scaling.

**Bounded fix:** range-check unsigned arrays against `np.iinfo(np.int64).max` before conversion, or preserve Python integers and serialize them consistently across scalar and vector APIs. Add `2**63-1`, `2**63`, and `2**64-1` boundary probes.

# Independently confirmed contracts

- **Distribution and independence:** 131,072 independently addressed kicks passed an independently derived 38-test family (mean, chi-square variance, lags 1–8, and 28 cross-clock correlations) at familywise `alpha=0.01` with Bonferroni threshold `2.63e-4`; minimum p-value was `0.00375`, with zero rejections.
- **Conditional split law:** 12,000 independent trials at each of `alpha = 0.2, 0.5, 0.8` passed 15 Bonferroni-controlled child-mean, duration-scaled variance, and sibling-covariance tests; minimum p-value `0.1149`. Residual construction conserved every parent within at most `0.25` of the declared four-ULP bound in the tested representable range.
- **Chronology and pairing:** sorted multi-crossing trees produce chronological `L, RL, ...` leaves with distinct split keys. Clock, edge, node path, pulse digest, crossing time, trial, dataset, and mesh separate split keys. No model label enters the API, so repeated full/control consumption is bit-identical.
- **Arbitrary request shape:** a randomized nine-window partition spanning block boundaries, requested forward and backward, reproduced a 6,200-step reference bit-for-bit. Single-clock/subpopulation and trial-order probes also agree. `D` exclusion is consistent with the declared common-normal pairing: it scales a realization rather than selecting one.
- **Exact branches:** zero diffusion produced byte-identical zero arrays and zero descendants; zero duration and fractions 0/1 produced exact zeros on the zero-duration side. Monkeypatch counting showed zero leaf/split key-to-number calls on these paths.
- **Mutation probes:** proportional splitting measured `0.255` of the required left variance at `alpha=0.25` versus `1.016` for the real split; an independent right child missed conservation by `1.59e15` tolerance units; model-specific keys separated paired children by `2.16e-3`; shared-clock noise had correlation `1.0` versus real maximum `0.0525`; request-window-dependent blocks changed values; a nonzero zero-D descendant is rejected by exact comparison.
- **Memory/no files:** the canonical measured path streamed 64 clocks by 200,000 steps in windows of 4,096 at 6.29 MB peak versus a 102.4 MB materialized array and changed no package file. Independent source inspection found no file-writing primitive in `stochastic.py`.
- **Raw isolation:** a fresh process loaded only package, `raw_config`, `raw_runner`, `stochastic`, and `validation`; no analytic/oracle/comparison module loaded. An independent AST traversal from `__init__.py`, `raw_runner.py`, and `raw_ledger.py` reached exactly `raw_config.py`, `raw_ledger.py`, `raw_runner.py`, `stochastic.py`, and `validation.py`; `stochastic.py` has no coupling, mismatch, amplitude, intensity, analytic, predictor, hazard, or model name. `raw_noise_stream` revalidates the exact config and passes only namespace, origin/timestep, and diffusion.
- **Reproducibility qualification:** the documentation correctly scopes exact normal values to the recorded Python/NumPy environment. Using Philox does not by itself freeze NumPy's future `standard_normal` transform; no stronger cross-version claim is made. A fully version-independent transform would be a product change, not a current defect.

# Commands and environment

Environment: macOS 26.5.2 arm64, Python 3.12.6, NumPy 2.3.5, SciPy 1.15.3.

Commands run from `~/Projects/Physics/DiracKuramotoFramework`:

```text
python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --verbose
python3 adler_born_two_channel/verify.py
PYTHONWARNINGS=error python3 -m adler_born_two_channel.verify
python3 -m adler_born_two_channel.verify --prove-failure-exit
python3 - <<'PY'  # independent S0/Split Bonferroni tests; window/order/key/zero/coarse/ULP probes
python3 - <<'PY'  # independent mutation and direct-geometry probes
python3 - <<'PY'  # fresh-import and independent AST graph/isolation probe
shasum -a 256 adler_born_two_channel/*.py adler_born_two_channel/README.md
```

Canonical module, direct-script, verbose, and warning-as-error runs pass **38/38**. The deliberate failure probe exits **1**. Verbose evidence reports 524,288 S0 kicks, 20,000 splits at each principal fraction, all six mutations rejected, 89 public callables / 323 invalid calls / 196 parameters, and 6.29 MB streaming peak.

All recorded Ticket 01 residuals remain unchanged, including wrapping `8.452e-15`, stable arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, outside-tongue slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, and exponent `8.604e-07`.

Pre/post source hashes were identical. Reviewed Ticket 02 source scope: `stochastic.py`, its raw boundary in `raw_runner.py`, transitive validators/imports in `raw_config.py`, `raw_ledger.py`, `validation.py`, and `__init__.py`, verification in `verify.py`, and the package `README.md`. No implementation file was edited, staged, reverted, or created; only this review artifact was added.

# Non-claims

This review confirms a minimal effective white-noise implementation in its ordinary representable range; it does not derive a microscopic bath, establish stochastic dynamics or commitment behavior, validate a killed-diffusion or moving-band audit, produce an event ledger, or support any Born-selection conclusion. Ticket 01's isolation limitation remains a scientific software boundary, not a hostile-code sandbox.

# Closure re-review — five-finding fix-up — 2026-08-27

## Verdict

**OPEN — the five original reproductions are substantially repaired, but five actionable defects remain.** The representable-range and identifier fixes are closed. Per-step v2 addresses, the irregular aggregation implementation, and the geometry-validating split all pass their direct happy-path probes, but their public contracts still have gaps a future caller can enter. A new half-open routing probe also found that accepted non-dyadic meshes can assign one boundary crossing to two adjacent steps.

## High — floating grid endpoints can double-route one boundary crossing

**Where:** `stochastic.py:529-532`, step endpoint construction at `stochastic.py:1087-1088`, and half-open routing at `stochastic.py:1281-1293`.

The half-open rule assumes `mesh.time_at(i) + mesh.step == mesh.time_at(i + 1)`. That identity does not hold generally in binary floating point because the two expressions round in different orders. With an accepted mesh `origin=1.0, step=0.1`:

```python
m = FinestMesh(1.0, 0.1)
s = PhaseNoiseStream("boundary", m, 0.07)
t = m.time_at(2)                       # 1.2
c = Crossing(0, "rising", digest, t)
leaves = s.elementary_leaves(0, 0, 1, 2, [c])
```

Step 1 ends at `m.time_at(1) + step == 1.2000000000000002`, while step 2 starts at `m.time_at(2) == 1.2`. `_crossings_in_step` therefore puts the same crossing in both steps. The two-step window produces four leaves with step indices `[1, 1, 2, 2]`, durations `[0.09999999999999987, 2.220446049250313e-16, 0.0, 0.10000000000000009]`, and paths `L, R, L, R`, rather than three leaves with one crossing. The first routing consumes a split normal and creates a tiny stochastic right child; the second repeats the endpoint handoff. The opposite rounding direction also occurs: `origin=0, step=0.1, index=100` gives an end at `10.1` and the next start at `10.100000000000001`, leaving a gap.

This breaks the elementary-mesh identity, chronological adjacency, exact-crossing uniqueness, window invariance at the mesh boundary, and the conditional law: the root kick is scaled for nominal duration `step`, while the geometry can span a differently rounded duration.

**Bounded fix:** define one canonical step-boundary representation and use it for routing, node endpoints, duration, and root variance. Do not mix `origin + i*step` with `start + step`. Add both overlap and gap cases above, assert each exact boundary crossing belongs to exactly one step, adjacent leaves abut, exactly one handoff occurs, and no split normal is consumed for a true endpoint.

## High — the unsafe uniform coarse path remains public and cannot reject crossing windows

**Where:** `stochastic.py:834-866` and `stochastic.py:1203-1252`; warning-only documentation at `README.md:529-546`.

`coarse_kicks_over_crossings` correctly sums the exact `TreeLeaf` sequence and is bounded to one coarse group. Independent probes with five crossings across eight steps found 13 chronological leaves, five split-normal draws, bit-exact agreement with an independently accumulated leaf sequence at stride 2, and invariance under windows 1, 3, 5, and 8. That closes the implementation half of the original finding.

The integration contract is not structurally closed, however. `coarse_kicks` remains a public method that accepts the same trial/clock/window/stride while having no crossing manifest and no way to know it is being used over a crossing-bearing interval. In the same direct probe it returned normally, drew zero split normals, and differed from the required irregular aggregation by `1.3877787807814457e-17`. No stepper exists yet that forces future refinement callers onto the irregular path. The README explicitly warns that a later study could choose roots while fine dynamics consumes leaves; documenting the failure mode does not satisfy the ticket's guarantee that coarse consumers receive sums of the same elementary leaves.

**Bounded fix:** make the general crossing-aware API the sole public coarse-refinement path, accepting an empty frozen crossing set for uniform windows. Privatize the root-only helper for controls, or bind a crossing manifest to the tree so a uniform fast path can prove the requested interval has none. Add a call-site/AST acceptance check once the stepper exists so production refinement cannot reach the root-only helper.

## Medium — `split_node` still lets one split key name incompatible node geometries

**Where:** `stochastic.py:902-968`; key construction at `stochastic.py:751-770`.

The old `split_kick` bypass is gone. `split_node` derives its fraction, refuses a crossing outside the step/node and a backwards/out-of-step node before any key-to-number call, and nested `split_leaf` uses it correctly. Those original reproductions are closed.

But `node_path` and `(node_start, node_end)` are still independent public claims. Nothing verifies that path `R` was actually produced by ancestry whose crossing fixes the supplied start. These two calls both succeed:

```python
s.split_node(0, clock, 10, "R", step_start + .2*h, step_end, parent, crossing)
s.split_node(0, clock, 10, "R", step_start + .4*h, step_end, parent, crossing)
```

They use the **same** split key—same trial, clock, step, node path, and crossing identity—but return different children because their derived durations/fractions differ. Thus one canonical Brownian-tree key still does not determine one node split when the public boundary is used directly. This is the nested-geometry version of the original inconsistent-fraction bug.

**Bounded fix:** make `split_node` private as well and expose only `split_leaf`/the validated tree walk, or require an immutable node object produced by that walk whose path, endpoints, parent kick, and ancestry cannot be supplied independently. Add the two-call same-key/different-geometry probe and require at least one call to reject before key consumption.

## Medium — `leaf_from_key` accepts noncanonical aliases for one leaf

**Where:** `stochastic.py:715-749`.

`leaf_key` itself is now injective across full blocks and boundaries, and `leaf_from_key(leaf_key(...))` reconstructs the exact root `TreeLeaf`. The deliberate bump to `dk-phase-noise/v2/physical` is the correct compatibility decision: the grammar and every keyed value visibly reset, no v1 run existed, private 1,024-value block seeding remains window/order invariant, and the changed statistical residuals are expected rather than a regression.

The parser is not canonical, though. Python's `int` accepts alternate spellings, so each of these resolves to the same leaf as the emitted address:

```text
trial=03/clock=5/step=7
trial=3/clock=+5/step=7
trial=3/clock=5/step=007
```

That gives multiple accepted address strings for one leaf despite the API and error text calling the grammar canonical. A manifest reader can therefore accept a spelling the canonical producer never emits.

**Bounded fix:** after parsing and range validation, require `key == self.leaf_key(trial, clock, index)` before reconstruction. Add leading-zero, explicit-plus, whitespace, and canonical round-trip controls.

## Low — README public-boundary counts are stale

**Where:** `README.md:706-709`.

The README still claims **70 public callables / 245 invalid calls / 141 parameters**. The current verbose verifier reports **93 / 347 / 215** after adding the new public methods and probes. The results section correctly says 42 checks, so this is a bounded documentation inconsistency rather than a code defect.

**Bounded fix:** update the three counts from the canonical verbose output and add a verifier assertion if these numbers are intended to remain exact documentation.

## Original finding dispositions

1. **Per-leaf key collisions:** **CLOSED for emitted v2 addresses and reconstruction; OPEN only for noncanonical parser aliases above.** Across 2,050 consecutive steps, all 2,050 public addresses were distinct, while private seeds formed three expected block groups. Exact reconstruction and arbitrary block-boundary windowing passed. The v2 reset and environment-scoped NumPy qualification are honest.
2. **Irregular coarse aggregation:** **CLOSED as an implementation, OPEN as a public integration boundary.** The chronological tree, split-normal evidence, strides/windows, and bounded stream work; the root-only public alternative remains callable over the same crossing window.
3. **Direct split geometry:** **CLOSED for out-of-parent/fraction disagreement, OPEN for path/endpoint ancestry binding.** Rejections consume no RNG/key; there is no public `split_kick`. The remaining same-key/different-node reproduction is above.
4. **Representable range and ULP bound:** **CLOSED.** Accepted maximum, near-maximum, subnormal, ordinary, zero, and cancellation regimes produce finite scales/kicks/children; `conservation_tolerance` stays finite through `DBL_MAX`; mathematical overflow declarations reject. The implementation conservatively rejects some extreme `(D,h)` pairs whose product could be rearranged to remain finite (for example `D=1e308, h=0.1`), but the public contract promises finite output for accepted values, not maximal acceptance, so this is not actionable for the experiment's domain.
5. **Unsigned identifier wrap:** **CLOSED.** Scalar/vector values agree at `2**63-1`, `2**63`, and `2**64-1`; negative, `2**64`, and `2**70` identifiers reject without conversion or wrap; mixed uint64 arrays preserve each row's stream.

## Re-run and independent evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error` runs: **42/42 pass**. `python3 -m compileall -q adler_born_two_channel` exits 0. The deliberate failure probe exits 1.
- Current v2 canonical statistics: S0 worst residual `3.316 sigma` and split worst residual `1.980 sigma`, versus v1 `3.184` and `1.215`. The schema prefix is part of every block and split seed, so this deterministic residual change is the expected consequence of the deliberate value reset. All thresholds remain frozen at 5 sigma.
- Independent familywise tests: 131,072 kicks passed 38 Bonferroni-controlled mean/variance/lag/cross-clock checks at family alpha 0.01 (minimum p `0.00160`, threshold `0.000263`, zero rejections). Twelve thousand splits at each of `alpha=0.2, 0.5, 0.8` passed 15 Bonferroni-controlled mean/variance/covariance tests (minimum p `0.103`, threshold `0.000667`); maximum conservation ratio `0.25` of the bound.
- Independent mutations: proportional splitting measured `0.250` of required left variance versus `1.023` real; an independent right child broke conservation by `2.63e15` tolerance units; shared-clock correlation was 1.0 versus real maximum `0.0724`; request-dependent blocks changed values while the real stream did not; model-specific keys separated paired children while the real split repeated bit-exactly; zero diffusion produced byte-exact zeros and zero key-to-number calls.
- Canonical memory/no-file evidence remains: uniform streaming 64 clocks by 200,000 steps peaks at 6.29 MB versus 102.4 MB materialization; irregular streaming of 20,000 steps peaks at 0.04 MB. Independent AST inspection found no write primitive, and pre/post implementation hashes were identical.
- Fresh raw import loaded only package, `raw_config`, `raw_runner`, `stochastic`, and `validation`. Independent AST traversal from the three raw roots reached exactly `raw_config`, `raw_ledger`, `raw_runner`, `stochastic`, and `validation`; no analytic/oracle/comparison module or coupling/mismatch/amplitude/intensity/predictor/hazard name entered `stochastic.py`.
- `elementary_leaves` intentionally materializes a single requested clock/window, while `stream_elementary_leaves` and the general coarse aggregator are bounded. Because the streamed form exists and the documentation does not claim the convenience method is bounded for an arbitrarily large caller request, this coexistence is not independently actionable. The unsafe issue is specifically the root-only coarse method, which can return the wrong tree for a crossing window without detecting misuse.

Environment: macOS 26.5.2 arm64, Python 3.12.6, NumPy 2.3.5, SciPy 1.15.3. Commands additionally included the three independent Python-stdin probe suites (five findings/API seams; Bonferroni distributions and mutations; fresh-import/AST isolation), `shasum -a 256 adler_born_two_channel/*.py adler_born_two_channel/README.md`, and verbose evidence filtering. No implementation code was edited; only this review artifact was appended.

# Closure re-review — canonical routing and safe API fix-up — 2026-08-27

## Verdict

**OPEN — the five requested API/routing corrections are substantially closed, but three numerical/mesh defects and one documentation defect remain; two are direct Brownian-law violations.** The canonical suite passes **46/46**, including all 32 pre-Ticket-02 checks with their prior residuals unchanged and all ten current Ticket-02 checks. The canonical `origin=1, step=.1, t=1.2` routing case, single public coarse path, private tree primitives, exact v2 parser, and mechanically pinned counts all pass cold probes. The new canonical geometry nevertheless exposes a mismatch between the duration used to draw a root and the duration used to split it; independent extreme-range probes also falsify the verifier's representable-range closure.

## High — canonical float geometry and the root noise law use different durations

**Where:** `stochastic.py:557-594`, `stochastic.py:761-772`, `stochastic.py:895-955`, `stochastic.py:1034-1179`, and the resulting leaf duration at `stochastic.py:1260-1263`.

`step_bounds` deliberately defines geometry as `time_at(i + 1) - time_at(i)`, while `leaf_scale` always uses the declared `mesh.step`. The claim at lines 575-579 that this difference “cannot do any harm” is false for a conditional Brownian split. If the realized width is `w` but the parent was drawn with variance `2 D h`, then at fraction `alpha` the implementation gives

```text
Var(L) = alpha^2 (2 D h) + 2 D w alpha (1-alpha)
Cov(L,R) = alpha (1-alpha) (2 D h - 2 D w)
```

rather than the required `Var(L) = 2 D alpha w` and `Cov(L,R) = 0` unless `h == w` exactly.

Exact public reproduction:

```python
m = FinestMesh(1e15, 0.2)
s = PhaseNoiseStream("duration-contract", m, 1.0)
start, end = m.step_bounds(0)       # realized end-start == 0.25
c = Crossing(0, "rising", digest, math.nextafter(start, end))
leaves = s.elementary_leaves(trial, 0, 0, 1, [c])
```

The two returned leaves each report duration `0.125`. The parent is drawn with variance `0.4`, although the reported interval requires `0.5`. At the midpoint the required child variance is `0.25`, while the construction's independently derived variance is `0.225` and its sibling covariance is `-0.025`. Over 12,000 keyed trials I measured parent variance `0.40401`, left/right variances `0.22850/0.22545`, and covariance `-0.02497` (`-11.98` standard errors from zero). This is not merely a last-bit conservation issue; accepted large origins make the law wrong by ten percent.

**Bounded fix:** choose one duration representation for the parent draw, split bridge, returned `TreeLeaf.duration`, and dynamics consumer. Either scale each root by its canonical realized width, or retain the declared duration through an exact/canonical mesh representation whose geometry agrees with it; reject a requested window when that agreement cannot be represented. Any change to the key-to-kick mapping needs the schema/version treatment the v2 documentation already requires. Add the exact reproduction above and assert root variance, both child variances, and sibling covariance from independently derived expectations.

## High — accepted subnormal products silently erase root and split randomness

**Where:** construction at `stochastic.py:761-772`, root scale at `stochastic.py:895-955`, and split variance/bridge at `stochastic.py:1168-1178`.

The finite-range check rejects overflow but does not detect underflow, and the multiplication is performed before the square root.

Two exact reproductions:

```python
# Resolvable positive-duration step; positive diffusion.
h = math.ulp(0.0)                    # 5e-324
s = PhaseNoiseStream("u", FinestMesh(0.0, h), 0.2)
s.leaf_kicks(0, [0], 0, 8)
```

`2*D*h` and `leaf_scale` both become `0.0`. The call is accepted, derives one keyed 1,024-value block, and returns eight signed zeros (`-0.0` and `+0.0`) even though both duration and diffusion are positive.

```python
# Parent variance remains representable, but its Brownian bridge is erased.
D = math.ulp(0.0)
s = PhaseNoiseStream("u-split", FinestMesh(0.0, 1.0), D)
c = Crossing(0, "rising", digest, 0.5)
s.elementary_leaves(trial, 0, 0, 1, [c])
```

Here the parent variance is the representable `1e-323`, but `2*D*1*.5*.5` underflows to zero before `sqrt`. A stable rearrangement gives a nonzero bridge scale `sqrt(2*D*1)*0.5 = 1.5717277847026288e-162`. In all eight direct trials the implementation instead returned `L == R == 0.5*parent` exactly: the proportional-split mutation that the ordinary-range verifier rejects. Thus the accepted children have half the required marginal variance and positive, not zero, sibling covariance.

**Bounded fix:** calculate Brownian standard deviations with an overflow/underflow-safe product (for example exponent-scaled factors) rather than materializing the variance before `sqrt`, or reject every mathematically positive combination whose required scale is outside the supported representable domain before deriving a key. Apply the same helper to roots and split bridges. Add the two probes above, including a key-call counter and a discriminator requiring a nonzero bridge for the second case.

## Medium — root-noise APIs accept an unresolvable mesh and consume randomness

**Where:** mesh construction at `stochastic.py:535-541`, local geometry rejection at `stochastic.py:581-594`, and geometry-free root paths at `stochastic.py:901-955` and `stochastic.py:1002-1032`.

`FinestMesh` accepts any finite positive step, and only `step_bounds` notices a collapsed interval. The physical root APIs never ask `step_bounds`, so an object that cannot represent its first timestep still emits physical noise:

```python
m = FinestMesh(1e16, 0.1)
s = PhaseNoiseStream("unresolved", m, 0.2)
s.leaf_kicks(0, [0], 0, 1)  # returns -0.5943897079445971 and derives a key
m.step_bounds(0)             # ValueError: interval [1e16, 1e16] has no width
```

The same occurs for `(origin=1e308, step=1.0)`. This leaves a public split personality: the root/no-crossing consumer accepts a step that the irregular tree and router call a configuration error. A 300,000-case log-scale routing search found no wrong answer after a resolvable interval was reached; larger initial-estimate displacements occurred only with collapsed boundaries. The problem is therefore validation/consumption, not the ordinary four-correction route itself.

**Bounded fix:** validate every requested physical-noise window's canonical step geometry before any key derivation, and make the root, streamed, elementary, and coarse paths share that validation. Reject collapsed steps consistently and before RNG consumption. Add constructor/start-window/inside-window/end-window collapse cases, including the two reproductions above.

## Low — coarse API docstrings still name the removed public method

**Where:** `stochastic.py:980`, `stochastic.py:987`, `stochastic.py:1288`, and `stochastic.py:1361-1369`.

The actual public surface is fixed, and the README is current, but source API documentation still links to the removed `coarse_kicks_over_crossings`. The surviving `coarse_kicks` docstring also calls itself the uniform method that cannot receive crossings, which is the opposite of its current required-schedule signature.

**Bounded fix:** replace the removed-name/self-contradictory references with `coarse_kicks` for the crossing-aware public path and `_coarse_kicks_uniform` for the private verifier control. Pin those names in the existing public-surface/documentation check if source docstrings are intended as API documentation.

## Requested closure dispositions

1. **Canonical routing:** **CLOSED in ordinary and large-index resolvable cases; OPEN for the duration-law and unresolvable-window defects above.** `FinestMesh(1, .1).step_containing(1.2) == 2`; exact starts route to their own step and exact ends to the next across positive/negative origins, opposite rounding, indices through 10,000, adjacent partitions, and reordered windows. The boundary produces one exact zero-duration child and no split draw, as the governing plan explicitly requires. No overlap, gap, duplicate ownership, or ordering change reproduced. The four-correction search found no resolvable counterexample; cases requiring more movement had already collapsed one or more boundaries and should be rejected consistently.
2. **One public coarse API:** **CLOSED.** Reflection finds one callable `coarse_kicks(self, trial, clock, start_index, count, stride, crossings)` and no public split/node/key primitive. It requires the frozen schedule, its private root control is underscore-only, and independent chronology/stride/window checks plus the built-in split-key counter show the public path uses actual tree leaves.
3. **Safe split ownership:** **CLOSED.** `_split_key`, `_split_node`, `_split_at_fraction`, and `_split_step` are private; the only public traversal owns ancestry and geometry. The former forged-`R` operations are not public, and invalid geometry rejects before key derivation. Private key collisions remain accurately scoped as an implementation invariant, not a promise to arbitrary callers.
4. **Canonical v2 parser:** **CLOSED.** Exact emitted addresses round-trip to the identical `TreeLeaf`; leading zeros, plus signs, whitespace, underscore digits, truncated/extended paths, and trailing separators reject. The v2 value reset remains deliberate and documented.
5. **README/API counts:** **CLOSED for the requested mechanical counts.** The verbose verifier and README agree exactly once on 46 checks, 91 public callables, 326 invalid calls, and 195 parameters. Only the stale method-name docstrings above remain.
6. **Finite range / uint64:** **OPEN for underflow, CLOSED for overflow/ULP and identifiers.** Max/near-max/cancellation cases retain finite scales and ULP bounds; overflow products reject. Scalar/vector clock values agree at `2**63-1`, `2**63`, and `2**64-1`; negatives and `2**64` reject without wrap.

## Re-run evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **46/46 pass**. `compileall` exits 0. The deliberate failure path prints **46/47** and exits 1.
- All pre-ticket deterministic residuals are unchanged: wrapping `8.452e-15`, arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`. Current v2 statistical residuals remain `3.316 sigma` and `1.980 sigma`, the expected deterministic reset from v1's `3.184/1.215` because the schema is in every seed.
- Independent ordinary-range distribution family: 131,072 kicks passed 38 Bonferroni-controlled mean, variance, lag-1–8, and 28 cross-clock tests at family alpha `0.01`; threshold `0.000263`, minimum p `0.0190`, zero rejections. Twelve thousand ordinary splits across `alpha=.2,.5,.8` passed 15 independently derived mean/variance/covariance tests; threshold `0.000667`, minimum p `0.0572`, zero rejections.
- Mutations/direct discriminators rerun: proportional split variance ratio `0.2523` at `alpha=.25`; independent-right maximum parent error `0.4575`; shared-clock correlation `1.0` versus real maximum `0.00603`; request-dependent blocks changed a value while canonical blocks did not; model-specific split keys differed; zero diffusion and endpoint branches produced exact zeros with zero key-to-number calls. The new subnormal reproduction shows the real implementation itself degenerates to the proportional mutation outside the ordinary range.
- Canonical no-cube evidence remains 6.29 MB for 64 clocks by 200,000 steps versus 102.4 MB materialization; irregular streaming remains 0.04 MB for 20,000 steps. Independent AST inspection found no file-write primitive in `stochastic.py`; pre/post hashes of all implementation files were unchanged.
- Fresh raw reachability remains exactly `__init__.py`, `raw_config.py`, `raw_ledger.py`, `raw_runner.py`, `stochastic.py`, and `validation.py`; no analytic, simulation, oracle, or comparison module is reachable. Raw isolation and absence of model/physics inputs remain closed.

Commands were run from `~/Projects/Physics/DiracKuramotoFramework` under macOS 26.5.2 arm64, Python 3.12.6, NumPy 2.3.5, and SciPy 1.15.3. They included all five canonical variants, `compileall`, four independent Python-stdin suites (routing/API/uint64/zero/duration/unresolvable; subnormal root/split; Bonferroni distributions/mutations; AST/raw/no-file), source searches, and SHA-256 snapshots. Reviewed scope was `stochastic.py`, `verify.py`, `README.md`, `raw_runner.py`, `raw_config.py`, `raw_ledger.py`, `validation.py`, `__init__.py`, the governing Brownian-tree plan/pressure test, Ticket 01 isolation contract, Ticket 02, and its two fix-up tickets. No implementation code, test, README, source file, or Git state was edited; only this review artifact was appended.

## Non-claims

This review does not derive the effective bath, validate stochastic phase evolution or commitment, establish a moving-band/killed-diffusion oracle, produce events, or support a Born-selection conclusion. It does not claim hostile-code sandboxing, NumPy-major-version bitwise reproducibility, or that a finite random search proves the four-correction bound for all IEEE-754 inputs. The OPEN verdict rests on the exact analytical and public reproductions above, not on that search.

# Closure re-review — realized-duration/stable-scale v3 fix-up — 2026-08-27

## Verdict

**OPEN — realized-duration consistency, eager window validation, and the v3/API corrections close, but two stable-scale defects and one stale semantic documentation claim remain.** The canonical suite passes **50/50** and the ordinary and realized-width Brownian statistics pass independent families. The remaining high finding is outside the suite's ordinary scale range: an accepted subnormal output scale quantizes the supposed Gaussian kicks so severely that their variance is only 54% of the required law. A separate exact large-value reproduction shows the constructor still rejects a mathematically representable variance because it evaluates the old overflow-prone product before the new stable scale can be used.

## High — an accepted subnormal output scale does not preserve the Gaussian variance law

**Where:** `_brownian_scale` at `stochastic.py:484-516`, construction/acceptance at `stochastic.py:833-847`, scale materialization at `stochastic.py:968-990` and `stochastic.py:1102-1124`, kick multiplication at `stochastic.py:1096-1100`, and the purported independent reference at `verify.py:5739-5815`.

The factorization correctly prevents an intermediate `2*D*h` underflow, but it rounds the *scale itself* to binary64 before multiplying the normal. When the true scale is subnormal, that early rounding can be a large fraction of the value. The suite's “both subnormal” case is the minimum example:

```python
u = math.ulp(0.0)                    # 4.9406564584124654e-324
s = PhaseNoiseStream("both-subnormal", FinestMesh(0.0, u), u)
x = s.leaf_kicks(0, [0], 0, 262144)[0]
```

The high-precision scale is `sqrt(2)*u = 6.987143370513132...e-324`; `_brownian_scale` returns `u`, the nearest double, with **29.289% relative error**. Multiplying standard normals by that already-rounded `u` quantizes all 262,144 kicks to only eleven lattice values `{-5u,...,5u}`, including **38.20% exact zeros**. After normalizing against the high-precision target scale, the measured variance is **0.54226**, not 1. The one-subnormal-operand controls remain sound: `(D=.2,h=u)` gives normalized variance `1.00055` with no zeros, and `(D=u,h=1)` gives `1.00896`; `D=h=1e-200` gives `1.00000`.

The verifier misses the failure because its “independent logarithmic reference” is `math.exp(0.5*(math.log(...)))`, another binary64 computation. In the both-subnormal case it rounds to the same `u` before the relative comparison, reporting `<=5e-14` where a 120-digit reference gives `0.292893...`. The returned scale is correctly rounded as a scalar, but “correctly rounded scale” is not equivalent to “kicks with the required variance” when that scale has one quantum of precision.

**Bounded fix:** either reject output-subnormal Brownian scales before key derivation (while continuing to accept subnormal *operands* whose final scale is normal), or retain an exponent/factor representation and multiply the keyed normal before the final subnormal rounding so `sqrt(2)` is not lost in a pre-rounded scalar. Apply the same policy to split bridges. Replace the binary64 log oracle with a high-precision reference and add a distributional discriminator for the accepted minimum scale, including zero mass and normalized variance. If quantized subnormal outputs are intentionally supported instead, narrow the white-Gaussian/moment contract and document the large, unavoidable error explicitly.

## Medium — the constructor still rejects a representable variance through the old product spelling

**Where:** `PhaseNoiseStream.__post_init__` at `stochastic.py:833-844`, contrasted with `_brownian_scale` at `stochastic.py:484-516` and the v3 accepted-domain prose at `README.md:572-590`.

Construction still evaluates `variance = 2.0 * phase_diffusion * mesh.step` left to right and rejects if that intermediate overflows. This defeats the factorization for a case where not only the scale, but the exact mathematical variance itself, is representable:

```python
D = sys.float_info.max
h = 0.25
_brownian_scale(D, h)                # 9.480751908109176e153, finite
PhaseNoiseStream("large", FinestMesh(0.0, h), D)
# ValueError because float evaluation of 2*D*h is inf
```

Mathematically `2*D*h = D/2 = 8.988465674311579e307`, a finite double, and a 120-digit reference agrees with the factored scale to `3.31e-17` relative. The same false rejection occurs at `D=1e308, h=.1`. By contrast `D=h=DBL_MAX` gives a genuinely unrepresentable scale and should reject. The current check therefore distinguishes evaluation order, not the stated accepted domain. It also makes the README claim that product overflow is survived true of a private helper but false of public root construction.

**Bounded fix:** validate the intended domain with overflow-safe arithmetic. If the contract remains “mathematical variance representable,” compare/rearrange without forming `2*D` first or use the factored scale plus an explicit `scale <= sqrt(DBL_MAX)` bound. If the contract is instead “scale representable,” use `_require_representable_scale(_brownian_scale(...))` and separately preserve the finite-kick guarantee. Add the exact `DBL_MAX,.25` acceptance and `DBL_MAX,DBL_MAX` refusal before-key controls.

## Low — two v2-era duration statements remain semantically stale

**Where:** `FinestMesh.step_bounds` at `stochastic.py:647-651` and the `PhaseNoiseStream` class contract at `stochastic.py:816-826`.

The removed method names and cross-references are fixed, and the new name check is non-vacuous. It does not inspect meaning, however. `step_bounds` still says the declared step is what the noise variance uses and that the realized-width difference “cannot do any harm,” exactly the policy v3 replaced. The stream class still says the old product is checked once at construction and therefore bounds every accepted leaf scale. These statements contradict `step_scale(index)`, the README, and the v3 schema rationale.

**Bounded fix:** rewrite both paragraphs around the realized per-step duration and the settled accepted-scale policy, then add a focused source assertion for the obsolete nominal-duration claim if prose is part of the verified API contract.

## Requested closure dispositions

1. **One realized duration throughout:** **CLOSED.** On `FinestMesh(1e15,.2)`, an independent 60,000-step run realized 24,000 widths of `.125` and 36,000 of `.25`, mean `.2`. Conditioned variances were `.12361` versus `.125` (`-1.21 sigma`) and `.25166` versus `.25` (`+0.89 sigma`). The pooled variance `.20045` also matches the mean/nominal `.2`, confirming the README correctly explains why pooling is non-discriminating. A public midpoint split over a `.25` step measured parent variance `.25034`, child variances `.12716/.12603` against `.125`, and correlation `-.0113`; child durations were `.125/.125`. A crossing-bearing two-group coarse call matched an independent chronological `TreeLeaf` sum bit-for-bit, with group durations `.75/.875` exactly equal to the corresponding boundary differences.
2. **Stable factorization:** **OPEN only for the subnormal-output law and constructor domain above.** Roots with `h=ulp(0),D=.2`, `D=ulp(0),h=1`, and `D=h=1e-200` retain nonzero ordinary-scale randomness. Public conditional splits for the latter two and the private arithmetic split for the one-ulp interval are non-proportional and have normalized child variances near one. Normal-output high-precision comparisons over 30,000 random exponent/mantissa pairs found at most three ulp (`2.95e-16`) error. The minimum subnormal output does not satisfy the law.
3. **Eager complete-window validation:** **CLOSED.** On the later-collapse mesh used by the fix-up, all six public generation routes—`standard_normals`, `leaf_kicks`, both streaming APIs, `elementary_leaves`, and `coarse_kicks`—reject a 500-step request at the call when step 100 collapses, with zero key calls; the 100-step resolvable prefix succeeds. Zero diffusion still rejects the invalid physical window before returning its exact, keyless limit. `step_scale` rejects a collapsed single step. The bounded `O(count)` chunk scan is intentional under the full eager-validation requirement; the streaming paths do repeat validation per emitted window, an efficiency cost but not a correctness defect at current production sizes.
4. **v3 visibility and compatibility:** **CLOSED.** `KEY_SCHEMA`, public leaf addresses, private block seeds, and split keys all contain `dk-phase-noise/v3/physical`. Exact v2 leaf/block spellings reject at `leaf_from_key`; v2 and v3 block seeds generate different values. The v3 duration/factor reset and absence of recorded v1/v2 runs are documented.
5. **Routing, public API, parser, uint64, ULP:** **CLOSED.** The prior canonical boundary, adjacent-window, single-coarse-API, private-node, exact-parser, scalar/vector `2**63-1`/`2**63`/`2**64-1`, overflow-bound, and scale-aware conservation controls all pass. Exact zero diffusion and endpoint children remain byte-zero and derive no keys.

## Re-run evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **50/50 pass**. `compileall` exits 0. The deliberate failure path prints **50/51** and exits 1.
- All pre-ticket deterministic residuals remain unchanged: wrapping `8.452e-15`, arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`. The v3 keyed reset changes the expected statistical residuals from v2 `3.316/1.980` to v3 `3.460/1.171`, both within the unchanged five-sigma bounds.
- Independent ordinary S0 family: 131,072 kicks passed 38 Bonferroni-controlled mean, variance, lag-1–8, and 28 cross-clock checks at family alpha `.01`; threshold `.000263`, minimum p `.0251`, zero rejections. Twelve thousand splits across `alpha=.2,.5,.8` passed 15 independent mean/variance/covariance checks; threshold `.000667`, minimum p `.0193`, zero rejections.
- Mutation rerun: proportional variance ratio `.2493` at `alpha=.25`; independent-right maximum parent error `.5375`; shared-clock correlation `1.0` versus real maximum `.00581`; request-dependent blocks changed the selected value while the real stream did not. Model-key, zero-descendant, geometry, and public-surface mutations pass in the canonical battery.
- Canonical memory evidence: 64 clocks by 200,000 steps stream at 6.39 MB versus a 102.4 MB cube; irregular 20,000-step streaming peaks at .48 MB. Independent AST inspection found no write call in `stochastic.py`. Pre/post source hashes were identical.
- Fresh/raw structural reachability remains exactly `__init__.py`, `raw_config.py`, `raw_ledger.py`, `raw_runner.py`, `stochastic.py`, and `validation.py`; no analytic, simulation, oracle, or comparison module is reachable.
- The README and verifier mechanically agree once on **50 checks, 91 public callables, 329 invalid calls, and 196 parameters**.

Commands were run from `~/Projects/Physics/DiracKuramotoFramework` under macOS 26.5.2 arm64, Python 3.12.6, NumPy 2.3.5, SciPy 1.15.3, and mpmath with 120-digit precision. They included all five canonical variants, `compileall`, independent realized-width/root/split/coarse probes, a 30,000-case high-precision factor-rounding scan, minimum-subnormal distribution probes, all public eager-window routes with key counters, v2/v3 address probes, independent Bonferroni families/mutations, uint64/ULP/zero controls, raw AST/no-file inspection, and SHA-256 snapshots. Reviewed code scope was `stochastic.py`, `verify.py`, `README.md`, the raw boundary/transitive modules, and the governing Ticket 02/fix-up artifacts. No implementation, test, README, source, or Git state was edited; only this review artifact was appended.

## Non-claims

This review does not require maximal acceptance of every finite pair; it does require the stated accepted-domain rule to reject mathematical unrepresentability rather than one evaluation order. It does not claim a continuous Gaussian can be represented exactly at the binary64 floor—the finding is that the current accepted input and documentation still promise the ordinary variance law there. No stochastic dynamics, commitment, event ledger, moving-band oracle, microscopic bath, cross-NumPy bitwise guarantee, or Born-selection conclusion is reviewed or implied.

# Closure re-review — normal-scale domain patch — 2026-08-27

## Verdict

**OPEN — the normal-floor policy closes the former quantized-root and proportional-split law failures, and the requested overflow-safe constructor cases close, but the declared upper domain still admits non-finite physical kicks; invalid public split schedules also consume a parent key before their scale refusal.** The canonical suite passes **51/51**, including the unchanged 32-check baseline and all current Ticket-02 checks, but its largest accepted generated scale is only about `9.48e153`; a cold public probe reaches `1.271e308` and falsifies both the finite-output contract and the source's explanation of why it is safe.

## High — the upper scale bound admits ordinary Gaussian draws that overflow the kick

**Where:** `_MAX_SCALE` and the domain test at `stochastic.py:491-492,529-566`, root multiplication at `stochastic.py:1142-1198`, and the contradictory class contract at `stochastic.py:890-895`.

The patch bounds the **scale** by `DBL_MAX`, but the public result is `scale * standard_normal`. A normal scale can therefore be accepted even though a routine, finite keyed normal overflows the returned kick. Exact reproduction:

```python
M = sys.float_info.max
D = h = M / 2
s = PhaseNoiseStream("upper-domain-probe", FinestMesh(0.0, h), D)
s.step_scale(0)                       # 1.2711610061536462e+308
s.standard_normals(1, 0, 0, 1)[0]    # 1.4196553287245008
s.leaf_kicks(1, [0], 0, 1)[0, 0]     # inf + RuntimeWarning: overflow
```

The overflow threshold is only `DBL_MAX / scale = sqrt(2)`. `stream_leaf_blocks` yields the `inf`; `elementary_leaves` and `coarse_kicks` raise `ValueError` only after the root key has been derived and the multiplication has overflowed. This is a current physical-output defect, not merely maximal-domain preference. It also directly contradicts the docstring: `DBL_MAX` does not prevent a normal larger than one, the largest accepted scale is not `1.34e154`, and the current domain does not ensure the scale is the square root of a representable variance.

The high-precision boundary has the same hole one ulp earlier. With

```python
x = nextafter(DBL_MAX / sqrt(2), +inf)
D = h = x
```

the exact Decimal reference is `1.00000000000000002237 * DBL_MAX`, hence genuinely unrepresentable, while `_brownian_scale` rounds down to exactly `DBL_MAX` and the policy accepts it. The verifier's much coarser `DBL_MAX * DBL_MAX` case does not exercise this classification boundary.

**Bounded fix:** restore a safe, product-representable upper scale bound such as `sqrt(DBL_MAX)` (which still accepts the required `DBL_MAX * .25` and `1e308 * .1` cases), or establish another conservative bound that proves every possible keyed-normal product finite. Classify against the mathematical/exponent-factored target before rounding at the boundary. Add the exact finite-scale overflow reproduction above under `PYTHONWARNINGS=error`, require constructor/root/stream/tree/coarse to share the refusal before RNG, and pin the corrected domain prose.

## Medium — a subnormal bridge in a public schedule is refused only after its parent key is consumed

**Where:** parent draw before recursion at `stochastic.py:1494-1496`, bridge validation at `stochastic.py:1408-1419`, and public/eager entry points at `stochastic.py:1521-1588,1591-1645`.

The arithmetic primitive correctly validates the node and bridge scales before deriving the **split** key, and its direct counter check passes. The public tree has already drawn the root, however:

```python
u = math.ulp(0.0)
s = PhaseNoiseStream("bridge-consumption-probe", FinestMesh(0.0, 1.0), u)
c = Crossing(0, "rising", digest, u)
s.elementary_leaves(0, 0, 0, 1, [c])
```

The root scale is normal, but the conditional bridge is `5e-324` and must be refused. A patched `_normals_from_key` counter records one v3 root block key before the `ValueError`. `stream_elementary_leaves(...)` returns a generator successfully, then consumes the same root key and refuses at the first `next()`; `coarse_kicks` behaves likewise. Thus the current statements that an out-of-domain tree/split is refused before **any** key, and that the streaming path is eagerly validated, are false for scale-invalid crossing schedules. The canonical check only calls `_split_at_fraction` directly, so it measures zero split-key consumption while missing the already-consumed public parent key.

**Bounded fix:** prewalk each routed crossing geometry and validate every node and bridge scale before drawing the root. Run that preflight over the complete requested schedule at the call boundary for both materialized and generator-returning APIs, and reuse it in `coarse_kicks`. Add public elementary/stream/coarse key counters, not only a private split-helper counter.

## Low — the Decimal domain check is independent but does not probe adjacent classification

**Where:** `_SCALE_CASES` and `check_stable_scale` at `verify.py:5744-5959`.

The 60-digit Decimal reference is genuinely independent and non-vacuous: it exposes the former both-subnormal scale's `-29.289%` error and several product underflow/overflow controls. Its declared cases are decade-scale rather than boundary-adjacent, so the implementation verdict can still disagree with the reference at the cutoff. For `D = ulp(0)` and

```python
h0 = 2**-971
h = nextafter(h0, 0)
```

the exact target is `0.99999999999999994449 * MIN_NORMAL`, hence subnormal under the documented mathematical policy. `_brownian_scale` rounds it up to exactly `MIN_NORMAL`, and `_require_representable_scale` accepts. The numerical error is tiny rather than the former quantized-law failure, but it disproves the check's claim that policy/reference classification agrees at the actual threshold.

**Bounded fix:** add immediate predecessor/exact/successor cases at both bounds, derive the expected class only from Decimal/exponent arithmetic, and make the production classification use the same mathematical boundary or explicitly narrow the contract to classification of the already-rounded scalar.

## Requested closure dispositions

1. **Normal-scale floor and former failure:** **CLOSED for the intended regimes.** Both-subnormal and `1e-308 * 1e-308` declarations reject; a direct invalid bridge rejects before its split key; `D=ulp(0),h=1`, `D=.2,h=ulp(0)`, and `D=h=1e-200` retain normal, nonzero outputs; exact zero diffusion/duration remain bit-zero and keyless. Independently reconstructing the old both-subnormal result gave a scale `-29.289%` from its exact target, 39.24% zero kicks in 10,000 draws, and an exactly zero quarter-split bridge, reproducing the old proportional mutation. Public preflight remains open as above.
2. **Overflow-safe constructor/domain:** **CLOSED for `DBL_MAX*.25`, `1e308*.1`, and `DBL_MAX*DBL_MAX`; OPEN for the broader accepted upper domain.** The first two work through constructor, root, tree, stream and coarse; the last rejects. The exact accepted `D=h=DBL_MAX/2` reproduction returns `inf`, and an adjacent truly overflowing target rounds into acceptance.
3. **High-precision reference:** **CLOSED as an independent arithmetic reference; OPEN as boundary coverage/classification.** `Decimal(float)` is exact and the 60-digit product/square root does not share the implementation oracle. The accepted comparisons are within `2.696e-16` relative, but neither adjacent cutoff is present.
4. **v3 compatibility:** **CLOSED.** `KEY_SCHEMA` is still exactly `dk-phase-noise/v3/physical`; the leaf grammar, block keys, split keys, Philox/SeedSequence transform, and ordinary scale mapping are unchanged. Canonical v3 statistical residuals remain exactly `3.460` and `1.171`; five independently reconstructed ordinary leaves at steps 0, 1, 1023, 1024 and 70001 round-trip through their exact emitted keys. No v2 address is admitted.
5. **Documentation/API guards:** **CLOSED for the two prior contradictions and mechanical counts; OPEN for the new upper-domain contradiction.** The five required/four forbidden semantic phrases are active and non-vacuous, and README/verifier agree once on **51 checks, 91 public callables, 329 invalid calls, and 196 parameters**. The guard does not cover the false `DBL_MAX`/`1.34e154`/normal-maximum paragraph or public bridge preflight claim.

## Re-run and independent evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **51/51 pass**. `compileall` exits 0. The deliberate failure path prints **51/52** and exits 1. The 32 pre-ticket deterministic/numerical checks and all prior v3 residuals are unchanged.
- Independent ordinary S0 family: 16 clocks by 4,096 kicks produced **216** mean, variance, lag-1–4 and cross-clock tests; Bonferroni family alpha `.01`, threshold `4.63e-5`, minimum p `.00174`, zero rejections. Independent splits at `alpha=.2,.5,.8`, 5,000 each, produced **15** mean/variance/covariance tests; threshold `.000667`, minimum p `.0189`, zero rejections. Child variance ratios ranged `.99999–1.02947`, largest absolute sibling correlation `.0332`, and parent conservation stayed within `3.47e-18` absolute.
- Mutation/direct controls rerun: proportional subdivision had only `.2074` of the required left variance at `alpha=.2`; an independently sampled right child missed the parent by up to `.0681`, versus `3.47e-18` for the real residual; shared-clock correlation was 1.0 versus `.0489` maximum real cross-clock correlation. The extreme accepted upper-domain case is a new real-implementation failure under `PYTHONWARNINGS=always`.
- Raw isolation, no-file, no-cube and public-surface closures remain unchanged. Fresh canonical reachability is the six raw/package modules only; independent AST inspection found no file-write call in them. Canonical streaming remains 6.39 MB for 64 clocks by 200,000 steps versus a 102.4 MB cube, with irregular streaming at .48 MB. The routing, single public coarse API, exact parser, uint64, realized-duration, zero-key, ULP conservation, chronological tree and block/window invariance checks all pass.
- Source hashes before and after the review are unchanged: `stochastic.py 4a1de91f...`, `verify.py 3768a825...`, `README.md c627510c...`, with raw/isolation files unchanged as recorded above.

Environment: macOS 26.5.2 arm64, Python 3.13.11, NumPy 2.4.3, SciPy 1.16.3. Commands included all five canonical variants, `compileall`, SHA-256 snapshots, source/API searches, independent Python-stdin suites for Decimal boundary classification, the former quantized law, public key consumption, extreme accepted overflow, Bonferroni moment/covariance families, mutations, v3 reconstruction, and raw/no-file AST inspection. Reviewed source scope was `stochastic.py`, `verify.py`, `README.md`, the raw transitive boundary, governing Brownian-tree plan/pressure test, Ticket 01 isolation contract, Ticket 02 and its fix-up history. No implementation, test, README, source file, or Git state was edited; only this review artifact was appended.

## Non-claims

This review does not require maximal acceptance of all finite `(D,h)` pairs; the high finding is that a pair already accepted by the published domain returns a non-finite physical kick. It does not audit downstream stochastic phase evolution, commitment, event ledgers, a moving-band oracle, microscopic bath physics, cross-NumPy bitwise identity, or Born selection. Statistical passes do not repair the exact boundary reproductions on which the OPEN verdict rests.

# Closure re-review — exact scale boundary and preflight fix-up — 2026-08-27

## Verdict

**OPEN — the exact scale classifier, conservative upper cap, finite-kick paths, and scale-invalid schedule preflight close, but the preflight still omits an existing complete-schedule validity rule and therefore can consume earlier keys before rejecting a later over-deep step. Three source/README statements also contradict the new half-open domain.** The canonical battery passes **54/54**, and independent exact-rational, Decimal, warning, distribution and mutation probes support the new numerical mechanism. The remaining correctness reproduction uses only the current public schedule API and its already-documented 32-crossing limit.

## Medium — schedule preflight omits the 32-crossing depth rule, so a later-invalid schedule still consumes keys

**Where:** scale-only preflight at `stochastic.py:1346-1391`, the depth check deferred to `_split_step` at `stochastic.py:1635-1662`, public materialized/stream/coarse entry points at `stochastic.py:1719-1830`, and the incomplete canonical preflight check at `verify.py:6616-6750`.

The new preflight correctly walks every node and bridge scale before a root draw, including a scale-invalid later step. It does not settle every property of the complete schedule: `_MAX_NODE_DEPTH` is enforced only when `_split_step` is reached during generation. A valid first step is therefore emitted/drawn before a later step with 40 otherwise-valid crossings is rejected.

Exact public reproduction:

```python
s = PhaseNoiseStream("depth-preflight-probe", FinestMesh(0.0, 1.0), 0.1)
schedule = [
    Crossing(0, "rising", f"{j:064x}", 1.0 + (j + 1) / 41.0)
    for j in range(40)
]
s.elementary_leaves(0, 0, 0, 2, schedule)
```

With `_normals_from_key` counted, this raises the documented `40 crossings ... exceeds the 32-level tree depth` error **after one root block key for step 0**. `coarse_kicks` does the same. `stream_elementary_leaves` returns a generator successfully; draining it consumes the step-0 key and only then raises. Even when the 40 crossings are in the first step, the generator-returning call succeeds instead of eagerly refusing, although draining then rejects before a key. Thus “every complete invalid crossing schedule is settled at the call with zero keys” remains false; the canonical fix-up check only supplies invalid **scales**, so it does not cover the older schedule-depth contract.

The same structure makes `_preflight_schedule` `O(count * len(routed))`: it loops every step and `_crossings_in_step` rescans the complete routed schedule. That is effectively `O(steps)` for the intended two tongue crossings, so it is not a separate production defect in the current experiment, but the public API accepts larger schedules and a one-crossing-per-step caller gets quadratic preflight before streaming begins.

**Bounded fix:** bucket routed crossings by step once at the public call boundary, reject any requested-step bucket longer than `_MAX_NODE_DEPTH` before preflighting scales, and pass those buckets through preflight/generation. That closes zero-key/eager validity and makes validation `O(count + crossings)` rather than repeatedly scanning. Add first-step and later-step 40-crossing controls to materialized, generator-at-call, generator-drained and coarse key counters; keep the valid 32-crossing boundary beside them.

## Low — three current domain descriptions still state a closed or obsolete upper bound

**Where:** `_require_representable_scale` at `stochastic.py:616-622`, `_admit_scale` at `stochastic.py:675-680`, README at `README.md:684-688`, and semantic guards at `verify.py:6135-6170`.

The code and the detailed boundary prose settle a lower-closed, upper-half-open **mathematical target** domain. Three current statements disagree:

- `_require_representable_scale` says the domain is “closed at both ends” and still prints the obsolete upper literal `1.7976931348623157e+308` (`DBL_MAX`), although its implementation now compares with `sqrt(DBL_MAX)`.
- `_admit_scale` says “The interval itself is closed, so a target exactly on a bound is admitted,” but `_scale_verdict` deliberately refuses the exact upper target.
- README displays `[2.225...e-308, 1.340...e154]` with a closed right bracket before later saying the upper end is half-open.

The semantic guard passes because it requires one correct `sqrt(DBL_MAX)` phrase and forbids only the earlier `DBL_MAX` overflow explanation; it does not forbid these surviving contradictions.

**Bounded fix:** state the exact-target domain uniformly as `[MIN_NORMAL, sqrt(DBL_MAX))`, separately explain that the rounded computed scalar must also be finite/in range, correct the helper literal/bracket, and add the three obsolete phrases to the semantic guards.

## Requested closure dispositions

1. **Exact scale domain:** **CLOSED in code.** Independent exact `Fraction` comparisons over 100,000 random root/bridge factor sets found zero disagreements with `_scale_verdict`. Decimal and exact-rational probes agree on lower predecessor/exact/successor (`subnormal/normal/normal`) and upper predecessor/exact/successor (`normal/overflow/overflow`). The lower predecessor's rounded factor is normal but refuses; the conservative upper case has an exact target inside yet a computed scale one ulp above the cap and refuses. All refusals are constructor-keyless. Documentation remains open as above.
2. **Finite accepted public outputs and cap:** **CLOSED.** The largest directly reachable accepted probe used scale `0x1.ffffffffffffep+511`; 262,144 kicks were finite, warning-free, and reached magnitude `6.526e154`. `DBL_MAX*.25` and `1e308*.1` remain finite/warning-free through root, tree, leaf streaming and coarse aggregation. `(DBL_MAX/2)^2`, `1e200^2` and `DBL_MAX^2` refuse at construction with zero key calls. The `sqrt(DBL_MAX)` cap gives an enormous margin over the current finite-discrete normal generator; the exact no-overflow guarantee is tied to that recorded generator/environment, not to an abstract unbounded continuous Gaussian.
3. **Complete invalid schedule preflight:** **OPEN only for the depth-limit reproduction above.** First/later subnormal bridges now refuse at each public call with zero parent/split keys, including generator creation; valid and zero-diffusion controls remain unchanged.
4. **v3 compatibility:** **CLOSED.** `KEY_SCHEMA`, grammar, leaf/block/split key formation and number transform remain v3. The five prior ordinary leaf values at steps 0, 1, 1023, 1024 and 70001 are byte-for-byte unchanged, and canonical keyed residuals remain `3.460` and `1.171`. Boundary changes only remove formerly accepted out-of-domain configurations.
5. **Prior closures:** **CLOSED except the semantic prose above.** Realized duration, routing, one public coarse API/private ancestry, canonical parser, uint64 identifiers, ULP conservation, zero-key endpoints/diffusion, raw transitive isolation, no-file and no-cube checks all pass unchanged.

## Re-run and independent evidence

- Canonical module, verbose module, direct script, and `PYTHONWARNINGS=error`: **54/54 pass**. `compileall` exits 0. The deliberate failure path prints **54/55** and exits 1. README/verifier agree once on 54 checks, 91 public callables, 329 invalid calls and 196 parameters. All pre-ticket deterministic residuals and v3 residuals are unchanged.
- Exact boundary oracle: 100,000 random positive binary64 root/bridge factor sets compared `_scale_verdict` with exact `Fraction` products against exact squared bounds; zero mismatches. The six named boundary cases and conservative rounded-out case independently agree with 100-digit Decimal values.
- Gradual underflow at the accepted lower boundary is not the former quantized-scale failure. At `D=ulp(0), h=2**-971`, 262,144 accepted kicks had zero exact zeros, 262,144 distinct values, normalized variance `.999883`, and at most `1.11e-16` normalized multiplication-rounding error. The scale itself is normal (`0x1.0000000000001p-1022`); subnormal kick values near zero retain gradual-underflow rounding rather than collapsing the Brownian scale.
- Independent S0 family: 216 Bonferroni-controlled mean/variance/lag/cross-clock tests, family alpha `.01`, threshold `4.63e-5`, minimum p `.00174`, zero rejections. Independent split family: 15 mean/variance/covariance tests across `alpha=.2,.5,.8`, threshold `.000667`, minimum p `.0189`, zero rejections; child variance ratios `.99999–1.02947`, maximum sibling correlation `.0332`.
- Mutation controls remain discriminating: proportional left variance ratio `.2074` at `alpha=.2`; independent-right parent error `.0681` versus real `3.47e-18`; shared-clock correlation 1 versus maximum real cross-clock `.0489`. Canonical request-dependent blocks, model-specific keys, zero descendants and forged geometry mutations also remain caught.
- Canonical memory/no-file evidence remains 6.39 MB for 64 clocks by 200,000 steps versus a 102.4 MB cube and .48 MB for irregular 20,000-step streaming. Raw reachability remains exactly the package root plus `raw_config`, `raw_ledger`, `raw_runner`, `stochastic`, and `validation`; no analytic/oracle/comparison module or file-write primitive is reachable.

Environment: macOS 26.5.2 arm64, Python 3.13.11, NumPy 2.4.3, SciPy 1.16.3. Commands included all five canonical variants, `compileall`, source hashes/searches, exact-Fraction and Decimal boundary suites, upper/lower public warning probes, complete-schedule key counters, independent Bonferroni families and mutations, v3 reconstruction, and canonical raw/no-file/no-cube checks. Source scope remained `stochastic.py`, `verify.py`, `README.md`, the raw transitive boundary, governing Brownian-tree plan/pressure test, Ticket 01 isolation contract, Ticket 02 and all fix-up history. No implementation, test, README, source file or Git state was edited; only this review artifact was appended.

## Non-claims

This review does not treat the quadratic schedule scan as material for the settled two-crossing production use, nor does it require maximal acceptance at either floating-point boundary. It does require every invalid schedule the public API already recognizes to fail at its call boundary without changing the keyed run. It does not audit downstream stochastic phase evolution, commitment, ledgers, a moving-band oracle, microscopic bath physics, cross-NumPy bitwise identity, or Born selection.

# Final closure re-review — eager depth and documentation patch — 2026-08-27

## Verdict

**CLOSED — no actionable current Ticket-02 defect remains.** The former later-depth key consumption and generator-deferral reproduction now refuses at every public call with zero root or split keys; exactly 32 crossings remains valid. One canonical routing pass builds buckets that the preflight and generation walk share without rescanning or re-deciding ownership. The mathematical-target and computed-scale domains are now distinguished consistently in source and README, and the semantic guards reject every prior stale phrase. The canonical suite passes **56/56**, with every pre-Ticket-02 residual and every v3 keyed residual unchanged.

## Closure determinations

### Complete schedule routing and eager depth

**CLOSED.** `elementary_leaves`, `stream_elementary_leaves`, and `coarse_kicks` each validate the window, validate and sort the frozen schedule, route it once into `{step: crossings}`, and preflight requested buckets before generation. Direct key counters presented **33 crossings** in step 0 and in later step 2 to materialized, generator-at-call, generator-drained, and coarse paths: all eight calls raised the named 32-level depth `ValueError` with **zero** `_normals_from_key` calls. The generator API therefore refuses before it returns an iterator, not at its first `next()`.

At the inclusive boundary, exactly **32 crossings** produced **33 chronological leaves**, one root-block derivation and 32 distinct split-key derivations. The first/last paths were `L` and `R` repeated 32 times; `math.fsum` of the leaf kicks differed from the parent by `1.11e-16`, within the declared scale-aware accumulation bound. The 33rd crossing is the first refused one, so the limit has no off-by-one.

An over-deep bucket wholly outside the requested window is intentionally irrelevant: a two-step request accompanied by 33 valid crossings in step 10 returned the same two unsplit leaves as an empty schedule. This is the correct streaming contract: a caller may retain the whole clock schedule without pre-partitioning it, while only requested steps are physically generated and preflighted. The whole schedule's type/clock/unique-time/unique-identity grammar is still checked globally before routing.

Reversing a six-crossing schedule did not change the leaf sequence, and two adjacent eight-step requests concatenated exactly to the 16-step request, including two crossings outside that window. Canonical boundary ownership, arbitrary input order, adjacent partitions and out-of-window irrelevance therefore agree.

### One routing and one set of validated buckets

**CLOSED.** Instrumented public calls found exactly one `_route` invocation for each of materialized, streamed and coarse generation. `_preflight_schedule` and every `_crossings_in_step` lookup received the same dictionary object by identity; generation made one dictionary lookup per requested step. `_split_step` copies/validates only its own bucket and never scans or reroutes the full schedule. The former `O(steps * crossings)` lookup has become `O(crossings)` routing plus `O(steps)` bucket lookups; no preflight/generation divergence reproduced.

The canonical 28-crossing/40-step control likewise produces one 68-leaf sequence under stream windows 1, 7 and 13, two adjacent half-windows, and a narrow four-step request that sees exactly its own four crossings. This is structural evidence, not only equal output: the shared bucket object and one route call were counted independently.

### Exact-target versus computed-scale documentation

**CLOSED.** Source now states two separate policies:

- the exact mathematical target lies in `[MIN_NORMAL, sqrt(DBL_MAX))`, lower closed and upper open;
- the computed binary64 scale lies in `[MIN_NORMAL, MAX_SCALE]`, closed, because it is the actual multiplier.

README states the same distinction and explains the conservative conjunction: rounded-in mathematical outsiders and rounded-out computed values both refuse. The obsolete `DBL_MAX` upper literal, closed-exact-target language and prior nominal/product claims are absent. The source guard has nine required semantic statements and nine forbidden statements. An independent in-memory mutation appended each forbidden statement as a valid source string in turn; **9/9** made `check_source_api_accuracy` fail. Required phrases and all 19 cross-references are present, so the check is non-vacuous.

### Numerical, keyed and isolation regressions

**CLOSED.** A fresh independent exact-rational comparison of 50,000 random binary64 root/bridge factor families found zero disagreements with `_scale_verdict`. Canonical Decimal predecessor/exact/successor cases, conservative rounded-out refusal, normal-scale floor, finite upper-cap generation, `DBL_MAX*.25` / `1e308*.1` acceptance, above-cap keyless refusal, realized-duration moments, uint64 identifiers and ULP conservation all pass unchanged.

The v3 grammar and values remain unchanged. `KEY_SCHEMA` is exactly `dk-phase-noise/v3/physical`; ordinary leaves at steps 0, 1, 1023, 1024 and 70001 remain respectively `-0.0068629490570279545`, `0.0037573012753621344`, `0.008976246627404125`, `-0.020823156099989724`, and `-0.013842192529922552` for the recorded independent namespace. Canonical statistical residuals remain exactly `3.460` and `1.171`.

Raw transitive reachability remains the package root, `raw_config`, `raw_ledger`, `raw_runner`, `stochastic`, and `validation`, with no analytic/oracle/comparison module. Independent AST inspection found no file-write primitive in those modules. Canonical memory evidence remains 6.39 MB for 64 clocks by 200,000 steps versus a 102.4 MB cube and .48 MB for irregular 20,000-step streaming.

## Re-run and independent evidence

- Canonical module, verbose module, direct script and `PYTHONWARNINGS=error`: **56/56 pass**. `compileall` exits 0. The deliberate failure path prints **56/57** and exits 1. README/verifier agree once on **56 checks, 91 public callables, 329 invalid calls, and 196 parameters**.
- All pre-ticket deterministic residuals are unchanged: wrapping `8.452e-15`, stationary arrival `4.441e-14`, relaxation `4.142e-06`, critical slowing `1.048e-05`, slip `3.829e-06`, envelope `4.441e-16`, normalization `1.370e-05`, flux `2.104e-05`, exponent `8.604e-07`. v3 S0/split residuals remain `3.460/1.171`.
- Independent S0 family: 216 Bonferroni-controlled mean, variance, lag-1–4 and cross-clock tests at family alpha `.01`; threshold `4.63e-5`, minimum p `.00174`, zero rejections. Independent split family: 15 mean/variance/covariance tests across `alpha=.2,.5,.8`; threshold `.000667`, minimum p `.0189`, zero rejections. Child variance ratios ranged `.99999–1.02947`; maximum absolute sibling correlation `.0332`.
- Mutation controls remain discriminating: proportional subdivision produced `.2074` of required left variance at `alpha=.2`; independent right sampling missed the parent by `.0681` versus `3.47e-18` for the real residual; shared-clock correlation was 1 versus maximum real cross-clock `.0489`. Canonical request-dependent blocks, model-specific keys, nonzero zero-diffusion descendants and forged geometry mutations also remain caught.
- Direct schedule instrumentation covered first/later invalid depth, generator creation/drain, exact depth 32, out-of-window depth 33, route-call count, shared bucket identity, reverse order and adjacent partitions. Source hashes remained unchanged across review: `stochastic.py e6a3f649...`, `verify.py 28868d69...`, `README.md 7808d0af...`, with raw/isolation modules unchanged.

Environment: macOS 26.5.2 arm64, Python 3.13.11, NumPy 2.4.3, SciPy 1.16.3. Commands included all five canonical variants, `compileall`, SHA-256 snapshots, exact-Fraction scale probes, public key counters, routing/bucket instrumentation, partition/order/out-of-window probes, independent Bonferroni families and mutations, v3 reconstruction, semantic-guard mutations, and raw/no-file AST inspection. Reviewed source scope remained `stochastic.py`, `verify.py`, `README.md`, the raw transitive boundary, governing Brownian-tree plan/pressure test, Ticket 01 isolation contract, Ticket 02 and the complete fix-up history. No implementation, test, README, source file or Git state was edited; only this review artifact was appended.

## Non-claims

Closure is for Ticket 02's keyed Brownian source and its documented API/domain. It does not establish stochastic phase evolution, commitment, event-ledger correctness, a killed-diffusion or moving-band oracle, a microscopic origin for the bath, cross-NumPy-major bitwise identity, or Born selection. The finite-kick claim remains tied to the recorded finite-discrete NumPy normal generator; no bounded binary64 implementation represents an abstract continuous Gaussian tail exactly.
