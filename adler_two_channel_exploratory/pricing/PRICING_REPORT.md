# Validation-campaign pricing report (Ticket 07 pricing plan)

**A price is not an approval and not a sufficiency promise.**  Nothing here authorizes a validation stage, pilot, production run, sensitivity, fit or Ticket 08; every stage keeps its predeclared success, `numerical_no_result`, dependency and stop rules, and no stage is promised to resolve the numerical block.  The scientific disposition is unchanged: the moving-band result is `numerical_no_result`.

Plan: `traycer_artifacts/debates/born-selection-roundtable/adler-tongue-born-candidate/two-channel-stochastic-model/single-channel-stochastic-commitment/tickets/07-feasibility-pilot-and-freeze/validation-campaign-pricing-plan/index.md` (sha256 `86a21e0774aa70e9999d10940bdaef5e6ef04845595091a9941dea1966fefc54`).  Session started 2026-09-02T21:53:08-0600, finished 2026-09-02T22:34:41-0600, wall 2493 s (41.6 min) of the 3600 s ceiling.

## Machine and environment identity

| Field | Value |
| --- | --- |
| platform | `macOS-26.5.2-arm64-arm-64bit-Mach-O` |
| cpu_brand | `Apple M4 Pro` |
| physical_cpus | `12` |
| performance_cores | `8` |
| efficiency_cores | `4` |
| logical_cpus | `12` |
| memory_bytes | `25769803776` |
| os_version | `26.5.2` |
| python_version | `3.13.11` |
| python_executable | `/Users/john-bramble/miniconda3/bin/python3` |
| numpy_version | `2.4.3` |
| numpy_blas | `accelerate` |
| psutil_version | `7.2.0` |
| environment digest | `9dfcbc23f4c8b0902b797b311bf4250546eb42d400a6f3dac719aae0e30d3c56` |
| repo git HEAD | `26e86e30771dd943a769005eac7539273bf821f1` (the package itself is untracked) |
| package source fingerprint (`experiments.source_fingerprint`) | `8bb1a4eddd8b93a3458393bd027536e3b6f7a5f51d49fa561f7161926b945992` |

<details><summary>Per-file SHA-256 of the package sources fingerprinted</summary>

| File | SHA-256 |
| --- | --- |
| __init__.py | `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a` |
| analysis.py | `0b3b57ff75f07510b1d0d29d611d0841ed3dc54613ece513e0b56fb1e6e1015b` |
| analytic.py | `de572b82d5ef130acc1239723672efa9f25a12400eee6370851069741a83a6b1` |
| commitment.py | `7f12124540dc8dd576833d40793c05893eca04ab867a48f0c21a03f31de02a57` |
| compare.py | `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817` |
| dynamics.py | `9ecfefb4a5918f0f42bca7dee281f3b2a51d49325e6766be704bd6ac82eb3e11` |
| experiments.py | `b2672e0ff226ef48f073cb31176b656d301ec37f24fa13d28f027586bb68afeb` |
| killed_diffusion.py | `9a852a096d85583025b4c2f796766c61b9d2e884cd9463d2ff704f072674a457` |
| model.py | `c3f4e5ca70b2c8c11a203d1fea6799bb3347aafc6dea23fc7de87e67ea9f80df` |
| moving_band_audit.py | `135cbead60d03f44638b8ba77843984c825476f09f4625aa4bead2dfe7e344c9` |
| observables.py | `38223e39a726b747680d6f16610bb90dae60fa75fd5e1e29f3dbf57ed087fe92` |
| raw_config.py | `eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430` |
| raw_experiments.py | `b492e3a4556efbabb5cf7373dd4fd43009a10ea0baf7e784e0f9f4edc31217d9` |
| raw_ledger.py | `91af4540abea7eccd4ab52b25d3e1d3dc7b4f805e283a89f24630d1596c26504` |
| raw_race.py | `44e83995c12b6d08d766efcc39ed6a1ee2b64c3fdc7dbb43c665808bcd7f6432` |
| raw_runner.py | `ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b` |
| simulate.py | `1acb84aeddaf22e795738d1b2c7a20d4b5f092aa565e08eb5c6b71bd57c98d6c` |
| stochastic.py | `fdf5420ebe38b1c85f27a121efe626f690b30bd00bfd09f511feef01563cbac2` |
| validation.py | `ede647938253fefec4b366dbaa5117356638d070db3a794a6de1252a88bf693d` |

</details>

## Preconditions and tree integrity

- `results/` entries at start: 1176; SHA snapshot start `b467a6ed3a162752…`, end `b467a6ed3a162752…`; unchanged = **True**.  (The plan's literal 'empty results/' precondition is NOT met by this tree — see interpretation 1 — so 'unchanged' is the condition verified before and after every case.)
- Package tree (every entry except `results/`, including `__pycache__`) unchanged = **True**.
- No fixture touched disk: every fixture is in memory in a child process that exits with its case; the per-case JSON handoff in the scratchpad is removed in `finally`.
- The package verifier was not run; no validation stage, pilot, production, sensitivity or exponent fit was entered; no pilot/exponent output was opened.

## Components

### `refinement_comparison` — **priced**

| Case | work (resample-cluster-sample-level observation) | repeats (s) | slowest (s) | traced warmup (s) | ns per resample_observations | tracemalloc peak | ru_maxrss | sampled RSS | digest | warnings | exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C600 | 2,160,000 | 0.109, 0.108, 0.109 | 0.109 | 0.285 | 50.63 | 2 MiB | 56 MiB | 56 MiB | `ddaf772503ac` | 0 | completed |
| C1200 | 4,320,000 | 0.199, 0.200, 0.198 | 0.200 | 0.397 | 46.27 | 4 MiB | 61 MiB | 61 MiB | `ce9ef9998ed6` | 0 | completed |
| C2400 | 8,640,000 | 0.441, 0.444, 0.453 | 0.453 | 0.687 | 52.41 | 7 MiB | 73 MiB | 73 MiB | `7588aa7ce4c4` | 0 | completed |

- Normalized rate per resample-cluster-sample-level observation: 50.63 ns, 46.27 ns, 52.41 ns; ratio 1.133x (band 1.5x) → flat; slowest 52.41 ns; largest measured work 8,640,000.
- Memory (ru_maxrss over the three cases, ascending work): [56, 61, 73] MiB → model **linear** (slope 2.65 B/unit).
  - C600: verdict=numerical_no_result
  - C1200: verdict=numerical_no_result
  - C2400: verdict=numerical_no_result

### `stationary_construction` — **priced**

| Case | work (walker-position-level (endpoint) observation) | repeats (s) | slowest (s) | traced warmup (s) | ns per endpoint_observations | tracemalloc peak | ru_maxrss | sampled RSS | digest | warnings | exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W6000xF49152 | 774,144,000 | 16.038, 16.459, 16.420 | 16.459 | 37.095 | 21.26 | 43 MiB | 220 MiB | 220 MiB | `1f362dc4dbfb` | 0 | completed |
| W6000xF98304 | 1,548,288,000 | 26.951, 26.939, 27.933 | 27.933 | 68.153 | 18.04 | 43 MiB | 220 MiB | 220 MiB | `283307ebdd90` | 0 | completed |
| W6000xF196608 | 3,096,576,000 | 52.487, 52.340, 51.410 | 52.487 | 133.422 | 16.95 | 43 MiB | 228 MiB | 228 MiB | `3419c522febb` | 0 | completed |

- Normalized rate per walker-position-level (endpoint) observation: 21.26 ns, 18.04 ns, 16.95 ns; ratio 1.254x (band 1.5x) → flat; slowest 21.26 ns; largest measured work 3,096,576,000.
- Memory (ru_maxrss over the three cases, ascending work): [220, 220, 228] MiB → model **flat**.
  - W6000xF49152: paired_bitwise=True
  - W6000xF98304: paired_bitwise=True
  - W6000xF196608: paired_bitwise=True

### `moving_replay` — **priced**

| Case | work (physical interval) | work (audited interval evaluation) | repeats (s) | slowest (s) | traced warmup (s) | ns per physical_intervals | ns per audited_evaluations | tracemalloc peak | ru_maxrss | sampled RSS | digest | warnings | exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T20 | 52,740 | 123,440 | 7.156, 7.163, 7.154 | 7.163 | 35.411 | 135820.91 | 58029.77 | 1 MiB | 54 MiB | 54 MiB | `10c48110008b` | 0 | completed |
| T80 | 210,960 | 493,760 | 28.607, 28.651, 28.589 | 28.651 | 141.368 | 135812.73 | 58026.27 | 3 MiB | 66 MiB | 66 MiB | `93fe3fd58658` | 0 | completed |
| T320 | 843,840 | 1,975,040 | 114.577, 114.667, 114.745 | 114.745 | 562.144 | 135979.32 | 58097.45 | 7 MiB | 97 MiB | 97 MiB | `e2ba4e0c6445` | 0 | completed |

- Normalized rate per physical interval: 135820.91 ns, 135812.73 ns, 135979.32 ns; ratio 1.001x (band 1.5x) → flat; slowest 135979.32 ns; largest measured work 843,840.
- Normalized rate per audited interval evaluation: 58029.77 ns, 58026.27 ns, 58097.45 ns; ratio 1.001x (band 1.5x) → flat; slowest 58097.45 ns; largest measured work 1,975,040.
- Two-counter scalar collapse: counter ratio per case [2.3405, 2.3405, 2.3405]; allowed = True.
- Memory (ru_maxrss over the three cases, ascending work): [54, 66, 97] MiB → model **linear** (slope 54.7 B/unit).
  - T20: subset_holds=True, dataset_seconds_untimed=0.000694, eligible_intervals_from_records=30860, bridged_intervals_from_records=6586, uniform_draws=26344
  - T80: subset_holds=True, dataset_seconds_untimed=0.0015, eligible_intervals_from_records=123440, bridged_intervals_from_records=23168, uniform_draws=92672
  - T320: subset_holds=True, dataset_seconds_untimed=0.00876, eligible_intervals_from_records=493760, bridged_intervals_from_records=90538, uniform_draws=362152

### `stationary_solve` — **priced**

| Case | work (space-time cell) | repeats (s) | slowest (s) | traced warmup (s) | ns per space_time_cells | tracemalloc peak | ru_maxrss | sampled RSS | digest | warnings | exit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M4800xN4800 | 23,040,000 | 11.083, 11.057, 10.988 | 11.083 | 10.925 | 481.04 | 1055 MiB | 1588 MiB | 1588 MiB | `bdecbb2f2458` | 0 | completed |
| M4800xN19200 | 92,160,000 | 36.884, 37.208, 37.154 | 37.208 | 37.911 | 403.73 | 1055 MiB | 1575 MiB | 1575 MiB | `34aa7538a2b4` | 0 | completed |
| M4800xN76800 | 368,640,000 | 141.514, 142.011, 141.806 | 142.011 | 151.952 | 385.23 | 1055 MiB | 1589 MiB | 1589 MiB | `f3924699111b` | 0 | completed |

- Normalized rate per space-time cell: 481.04 ns, 403.73 ns, 385.23 ns; ratio 1.249x (band 1.5x) → flat; slowest 481.04 ns; largest measured work 368,640,000.
- Memory (ru_maxrss over the three cases, ascending work): [1588, 1575, 1589] MiB → model **flat**.
  - M4800xN4800: closure_residual=2.22e-16
  - M4800xN19200: closure_residual=2.22e-16
  - M4800xN76800: closure_residual=2.22e-16

## Stage work (declared) and per-stage prices

Baseline shapes (ticket-04 reference, verify.py constants): oracle grid 600x600; endpoint ladder 6000 walkers x 3 starts x 2048 fine steps at strides (8, 4, 2); stationary comparison 200 resamples x 6000 clusters x 12 samples x 3 levels; audit ladder 40 master trials x 3 clocks x strides (4, 2, 1) x 4 replicates on mesh (origin -2.0, step 0.008, 500 steps); moving comparison 200 resamples x clusters x 6 samples x 3 levels.

Exact replay counters per master trial: reference mesh physical=2637, eligible=1543 (x4 replicates = 6172 audited evaluations); dt/16 mesh physical=42012, eligible=24604.

| Stage | Shape | Component work | Price (time, x1.5 contingency) | Memory | Verdict |
| --- | --- | --- | --- | --- | --- |
| **S1** stationary probability, dt/16 at doubled space | fine_steps=32768, oracle_grid=[1200, 9600], space_factor=2, time_factor=16, walkers=6000 | stationary_solve: space_time_cells=11,520,000<br>stationary_construction: endpoint_observations=516,096,000<br>refinement_comparison: resample_observations=43,200,000 | 28.2 s | 1589 MiB | **priced** |
| **S2** stationary probability, dt/64 at quadrupled space | fine_steps=131072, oracle_grid=[2400, 38400], space_factor=4, time_factor=64, walkers=6000 | stationary_solve: space_time_cells=92,160,000<br>stationary_construction: endpoint_observations=2,064,384,000<br>refinement_comparison: resample_observations=43,200,000 | 136 s (2.3 min) | 1589 MiB | **priced** |
| **S3** stationary probability, dt/256 at eightfold space | fine_steps=524288, oracle_grid=[4800, 153600], space_factor=8, time_factor=256, walkers=6000 | stationary_solve: space_time_cells=737,280,000<br>stationary_construction: endpoint_observations=8,257,536,000<br>refinement_comparison: resample_observations=43,200,000 | 799 s (13.3 min) | 1589 MiB | **priced** |
| **S4** stationary time quantile, dt/256 at eightfold space | fine_steps=524288, oracle_grid=[4800, 153600], space_factor=8, time_factor=256, walkers=6000 | stationary_solve: space_time_cells=737,280,000<br>stationary_construction: endpoint_observations=8,257,536,000<br>refinement_comparison: resample_observations=43,200,000 | 799 s (13.3 min) | 1589 MiB | **priced** |
| **M5** moving-band probability, 64x master trials | clocks=3, fine_step=0.008, master_trials=2560, replicates=4, steps=500 | moving_replay: audited_evaluations=15,800,320, physical_intervals=6,750,720<br>refinement_comparison: resample_observations=9,216,000 | 1378 s (23.0 min) | 405 MiB | **priced** |
| **M6** moving-band probability, dt/16 replay | clocks=3, fine_step=0.0005, master_trials=40, replicates=4, steps=8000 | moving_replay: audited_evaluations=3,936,640, physical_intervals=1,680,480<br>refinement_comparison: resample_observations=144,000 | 343 s (5.7 min) | 141 MiB | **priced** |
| **M7** moving-band time quantile, 1024x master trials | clocks=3, fine_step=0.008, master_trials=40960, replicates=4, steps=500 | moving_replay: audited_evaluations=252,805,120, physical_intervals=108,011,520<br>refinement_comparison: resample_observations=147,456,000 | — | — | **pricing_unresolved** |

### Per-stage detail

- **S1** — priced; time 28.2 s (before contingency 18.8 s); memory 1589 MiB
  - stationary_solve: 5.5 s before contingency (slowest rate x work (space-time cell)); memory 1589 MiB; span factor(s) space_time_cells=0.03x
  - stationary_construction: 11.0 s before contingency (slowest rate x work (walker-position-level (endpoint) observation)); memory 228 MiB; span factor(s) endpoint_observations=0.17x
  - refinement_comparison: 2.3 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 160 MiB; span factor(s) resample_observations=5.00x
- **S2** — priced; time 136 s (2.3 min) (before contingency 90.5 s); memory 1589 MiB
  - stationary_solve: 44.3 s before contingency (slowest rate x work (space-time cell)); memory 1589 MiB; span factor(s) space_time_cells=0.25x
  - stationary_construction: 43.9 s before contingency (slowest rate x work (walker-position-level (endpoint) observation)); memory 228 MiB; span factor(s) endpoint_observations=0.67x
  - refinement_comparison: 2.3 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 160 MiB; span factor(s) resample_observations=5.00x
- **S3** — priced; time 799 s (13.3 min) (before contingency 532 s (8.9 min)); memory 1589 MiB
  - stationary_solve: 355 s (5.9 min) before contingency (slowest rate x work (space-time cell)); memory 1589 MiB; span factor(s) space_time_cells=2.00x
  - stationary_construction: 176 s (2.9 min) before contingency (slowest rate x work (walker-position-level (endpoint) observation)); memory 228 MiB; span factor(s) endpoint_observations=2.67x
  - refinement_comparison: 2.3 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 160 MiB; span factor(s) resample_observations=5.00x
- **S4** — priced; time 799 s (13.3 min) (before contingency 532 s (8.9 min)); memory 1589 MiB
  - stationary_solve: 355 s (5.9 min) before contingency (slowest rate x work (space-time cell)); memory 1589 MiB; span factor(s) space_time_cells=2.00x
  - stationary_construction: 176 s (2.9 min) before contingency (slowest rate x work (walker-position-level (endpoint) observation)); memory 228 MiB; span factor(s) endpoint_observations=2.67x
  - refinement_comparison: 2.3 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 160 MiB; span factor(s) resample_observations=5.00x
  - S4 is priced as a full independent stage; if S3's solve and walk are reused, its marginal cost is its comparison term alone.
- **M5** — priced; time 1378 s (23.0 min) (before contingency 918 s (15.3 min)); memory 405 MiB
  - moving_replay: 918 s (15.3 min) before contingency (scalar collapse allowed (both counters flat and proportional): max of the two single-counter terms); memory 405 MiB; span factor(s) audited_evaluations=8.00x, physical_intervals=8.00x
  - refinement_comparison: 0.5 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 74 MiB; span factor(s) resample_observations=1.07x
- **M6** — priced; time 343 s (5.7 min) (before contingency 229 s (3.8 min)); memory 141 MiB
  - moving_replay: 229 s (3.8 min) before contingency (scalar collapse allowed (both counters flat and proportional): max of the two single-counter terms); memory 141 MiB; span factor(s) audited_evaluations=1.99x, physical_intervals=1.99x
  - refinement_comparison: 0.0 s before contingency (slowest rate x work (resample-cluster-sample-level observation)); memory 73 MiB; span factor(s) resample_observations=0.02x
- **M7** — pricing_unresolved
  - moving_replay: unresolved — physical interval work is 128.0x the largest measured point (limit 16.0x); audited interval evaluation work is 128.0x the largest measured point (limit 16.0x)
  - refinement_comparison: unresolved — resample-cluster-sample-level observation work is 17.1x the largest measured point (limit 16.0x)
  - M7's comparison runs at 40960 clusters, in the quadratic regime of `compare_refinement` (see interpretation 'refinement comparison — quadratic term'); even where the 16x rule is formally met its comparison term would understate the cost.

## Dependency-path totals

| Path | Time (with contingency) | Memory | Verdict |
| --- | --- | --- | --- |
| S1 | 28.2 s | 1589 MiB | priced |
| S1 → S2 | 164 s (2.7 min) | 1589 MiB | priced |
| S1 → S2 → S3 | 963 s (16.0 min) | 1589 MiB | priced |
| S1 → S2 → S3 → S4 | 1761 s (29.4 min) | 1589 MiB | priced |
| M5 | 1378 s (23.0 min) | 405 MiB | priced |
| M5 → M6 | 1721 s (28.7 min) | 405 MiB | priced |
| M5 → M7 | — | — | pricing_unresolved (unresolved: M7) |

**Worst-case sum (every declared stage runs):** pricing_unresolved.  Sum over the resolved stages only (S1, S2, S3, S4, M5, M6): 3482 s (58.0 min); unresolved stages: M7.  This sum is not an approval estimate and not a sufficiency promise.

**Benchmark-only cost:** session wall 2493 s (41.6 min) (child processes 2492 s (41.5 min)); design probes before the session, not recorded here, took about two minutes.

Derivation digest (SHA-256 of the derived prices; `--derive-only` must reproduce it): `7c8c0f81d1f69f12f5043a352d2571f2b5f97a922b05634a4729d0f3f0062018`

## Interpretations of ambiguous plan definitions

1. **results/ precondition.** The plan requires an 'empty results/ state'.  The package's results/ holds 198 pre-existing run directories from unrelated exploratory work that this session must not touch.  None of the four kernels reads or writes results/.  The verifiable condition applied instead is 'results/ unchanged': a stat snapshot (path, size, mtime, mode) of every entry is taken before and after every case, and a SHA-256 snapshot of every file at session start and end; any difference is a failed precondition.
2. **stationary solve — unit and cases.** Unit is the plan's 'space-time cell' = space_steps x time_steps.  The propagator is dense (killed_diffusion._propagator: 'Dense rather than banded'), so cost per cell grows ~linearly with space_steps and a case series that varies space cannot pass the 1.5x band.  To keep the plan's unit AND stay conservative for every stationary stage, all three cases are run at the LARGEST stage space (M = 4800, 'eightfold' of the 600 reference grid) and vary only time_steps; a per-cell rate measured at M = 4800 bounds the per-cell rate at M = 1200 and 2400 from above.
3. **stationary solve — stage grids.** 'dt/f at s-fold space' is read as the oracle grid (600*s) x (600*f): the campaign refines the oracle's time grid with the endpoint timestep it is the reference for, and its space grid by the stated factor ('space refined separately from time').  Stage cells: S1 1200x9600, S2 2400x38400, S3/S4 4800x153600.
4. **stationary endpoint and sample construction — boundary.** 'From solved ladder outputs through exit-time/censoring arrays and ValidationDataset construction' is read as: the oracle SurvivalSolution is an untimed input; the timed region is the paired endpoint walk that GENERATES the exit-time/edge arrays (verify.py _s3_measured, mirrored call for call), the censoring, the PairedSample and ValidationDataset construction, and the dataset digest.  The alternative reading (walk excluded) would leave the 'stationary endpoint generation' the plan says was omitted from pricing still unpriced.
5. **stationary endpoint and sample construction — unit.** 'walker-position-level observation' is read as one endpoint observation of one walker at one start position at one refinement level, i.e. walkers x positions x sum_over_levels(fine_steps / stride).  This is the count of endpoint evaluations the scheme performs and it scales with the timestep lever (x16 at dt/16).  The alternative reading (walkers x positions x levels, a shape count) does not move with dt and would price dt/256 at the reference cost.
6. **stationary endpoint and sample construction — cases.** 6000 walkers (sample factor 1 in every stationary stage), chunk 1500, window 1024, strides (8,4,2), fine steps 49152 / 98304 / 196608 (dt/24, dt/48, dt/96 relative to the 2048-step reference).  A 4x span: the ValidationDataset construction carries a fixed ~3.8 s cost at 6000 walkers (an O(walkers^2) identity-uniqueness check in killed_diffusion._require_names, re-run on every PairedSample rebuild), so a wider span starting lower would fail the 1.5x band for a reason that is not the walk.
7. **moving-band replay — counters.** Counter 1 'physical interval' = elementary intervals of strictly positive duration walked by replay_pulse (the walk is shared by all replicates), summed over trials x clocks x strides.  Counter 2 'audited interval evaluation' = intervals whose schedule state is 'interior' (rising + falling in AuditedRun) times the replicate count: every such interval is classified and decided once per auxiliary replica.  Both are exact functions of (clock, stride, mesh) and the trial count.
8. **moving-band replay — cases and dataset.** 20 / 80 / 320 master trials at the reference pulse, mesh (origin -2.0, step 0.008, 500 steps), 3 clocks, strides (4,2,1), 4 replicates, initial phases the verifier's deterministic sweep of the circle over the case's own trial count.  The pooled ValidationDataset is assembled AFTER the timed region exactly as verify.py _audit_samples does, untimed; its seconds are recorded as a diagnostic and its digest is the output identity.
9. **moving-band replay — stage work.** M5 = 64 x 40 = 2560 master trials on the reference mesh; M6 = 40 trials on a 16x finer mesh (step 0.0005, 8000 steps, same strides, so the ladder timesteps are 0.002/0.001/0.0005); M7 = 40960 trials.  Counters for every stage are computed exactly from the schedule.
10. **refinement comparison — cases.** Synthetic datasets with the moving-band layout (6 samples: commit probability shift, three survival shifts, the p20 commit-time quantile shift with a baseline arm, added_resets_mean without one; 12 audited members = 3 clocks x 4 replicates; 3 primary members; 3 levels), generated by a seeded RNG, at 600 / 1200 / 2400 clusters (a 4x span, the plan's minimum), 200 resamples.  Values do not affect the bootstrap's cost; the layout does.  The moving layout carries 15 members per cluster-level against the stationary layout's one, so its per-observation rate bounds the stationary comparisons from above (a design probe of the true stationary-layout comparison at 6000 walkers gave 53.6 ns per observation).  A 16x span is impossible under the 1.5x band: the per-observation cost is U-shaped (see the next item), and the best 16x ladder probed, 300/1200/4800, varies 1.585x.
11. **refinement comparison — quadratic term.** compare_refinement rebuilds every PairedSample and pays _require_names' O(clusters^2) duplicate check per sample (killed_diffusion.py, `listed.count(e)` for every label).  Design probes of nanoseconds per resample-observation against cluster count: 200: 73.1, 300: 59.8, 400: 53.3, 600: 48.3, 800: 45.3, 1200: 44.1, 1600: 46.3, 2400: 50.5, 3200: 54.7, 4800: 69.9, 6400: 83.3, and from earlier probes 20480: 188.  Below ~800 clusters the fixed per-resample Python overhead dominates; above ~3000 the quadratic check does.  The plan's unit is therefore valid only in that window, and the cases are placed inside it.  Consequences: M6's comparison (40 clusters) is overhead-dominated and its priced term understates a cost that is tens of milliseconds in absolute terms; M7's comparison (40960 clusters, ~0.5 us per observation extrapolated) is 17x beyond the largest measured point and fails the 16x rule.
12. **tracemalloc.** The untimed warmup runs under tracemalloc and supplies the traced peak; the three timed repeats run untraced so that the price reflects the kernel and not the tracer (tracemalloc inflates the pure-Python replay 4.5x).  All four outputs (warmup + 3 repeats) must be digest-identical.
13. **process peak RSS.** Each case runs in a fresh child process; 'process peak RSS' is the child's ru_maxrss at exit (bytes on Darwin), which includes the untimed fixture construction — the conservative reading.  A sampled peak over the timed repeats is recorded beside it.  The parent polls the child's RSS every 20 ms and kills it above 2 GiB.
14. **'within 16x' and '1.5x'.** Both are read inclusively: stage_work <= 16 x largest measured work, and max_rate / min_rate <= 1.5, with a 1e-9 relative tolerance.
15. **stage S4.** Priced as a full independent stage (solve + walk + comparison at dt/256, eightfold space).  If S3's solve and walk are reused, S4's marginal cost is its comparison alone; the report shows both.
16. **preflight.** A case is launched only if elapsed + predicted <= 3600 s, where predicted = declared work x (slowest normalized rate so far in the component, or a declared prior for the first case) x (3 + traced-warmup factor) x 1.25.  A skipped case makes its component pricing_unresolved.

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/pricing/price_validation_campaign.py --run
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/pricing/price_validation_campaign.py --derive-only   # prices from observations.json
```

## Session log

```
[    0.0s] pricing session start
[    0.1s] source fingerprint 8bb1a4eddd8b93a3  env 9dfcbc23f4c8b090
[    0.2s] results/ snapshot: 1176 entries, sha b467a6ed3a162752; package stat 2cf5b3bf47bc1671
[    0.2s] replay counters per trial: reference phys=2637 elig=1543; dt/16 phys=42012 elig=24604
[    0.2s] refinement_comparison/C600: preflight predicted 1s (single 0.2s, trace x1.60); elapsed 0s; remaining 3600s
[    1.0s]     child rc=0 wall=0.8s rss_peak=56MiB state=completed
[    1.0s]     repeats [0.109, 0.108, 0.109] slowest 0.109s warmup(traced) 0.285s tm_peak 2.5MiB ru_maxrss 56MiB digest ddaf772503ac identical=True warnings=0
[    1.0s] refinement_comparison/C1200: preflight predicted 2s (single 0.2s, trace x2.65); elapsed 1s; remaining 3599s
[    2.3s]     child rc=0 wall=1.2s rss_peak=61MiB state=completed
[    2.3s]     repeats [0.199, 0.2, 0.198] slowest 0.200s warmup(traced) 0.397s tm_peak 4.0MiB ru_maxrss 61MiB digest ce9ef9998ed6 identical=True warnings=0
[    2.3s] refinement_comparison/C2400: preflight predicted 3s (single 0.4s, trace x2.65); elapsed 2s; remaining 3598s
[    4.8s]     child rc=0 wall=2.5s rss_peak=72MiB state=completed
[    4.8s]     repeats [0.441, 0.444, 0.453] slowest 0.453s warmup(traced) 0.687s tm_peak 7.0MiB ru_maxrss 73MiB digest 7588aa7ce4c4 identical=True warnings=0
[    4.8s] stationary_construction/W6000xF49152: preflight predicted 312s (single 54.2s, trace x1.60); elapsed 5s; remaining 3595s
[   91.0s]     child rc=0 wall=86.2s rss_peak=220MiB state=completed
[   91.0s]     repeats [16.038, 16.459, 16.42] slowest 16.459s warmup(traced) 37.095s tm_peak 42.7MiB ru_maxrss 220MiB digest 1f362dc4dbfb identical=True warnings=0
[   91.0s] stationary_construction/W6000xF98304: preflight predicted 219s (single 32.9s, trace x2.31); elapsed 91s; remaining 3509s
[  241.2s]     child rc=0 wall=150.1s rss_peak=220MiB state=completed
[  241.2s]     repeats [26.951, 26.939, 27.933] slowest 27.933s warmup(traced) 68.153s tm_peak 42.7MiB ru_maxrss 220MiB digest 283307ebdd90 identical=True warnings=0
[  241.2s] stationary_construction/W6000xF196608: preflight predicted 455s (single 65.8s, trace x2.53); elapsed 241s; remaining 3359s
[  531.1s]     child rc=0 wall=289.8s rss_peak=228MiB state=completed
[  531.1s]     repeats [52.487, 52.34, 51.41] slowest 52.487s warmup(traced) 133.422s tm_peak 42.7MiB ru_maxrss 228MiB digest 3419c522febb identical=True warnings=0
[  531.1s] moving_replay/T20: preflight predicted 74s (single 7.4s, trace x5.00); elapsed 531s; remaining 3069s
[  588.1s]     child rc=0 wall=57.0s rss_peak=54MiB state=completed
[  588.1s]     repeats [7.156, 7.163, 7.154] slowest 7.163s warmup(traced) 35.411s tm_peak 1.4MiB ru_maxrss 54MiB digest 10c48110008b identical=True warnings=0
[  588.1s] moving_replay/T80: preflight predicted 285s (single 28.7s, trace x4.95); elapsed 588s; remaining 3012s
[  815.5s]     child rc=0 wall=227.4s rss_peak=66MiB state=completed
[  815.6s]     repeats [28.607, 28.651, 28.589] slowest 28.651s warmup(traced) 141.368s tm_peak 2.6MiB ru_maxrss 66MiB digest 93fe3fd58658 identical=True warnings=0
[  815.6s] moving_replay/T320: preflight predicted 1139s (single 114.6s, trace x4.95); elapsed 816s; remaining 2784s
[ 1722.0s]     child rc=0 wall=906.4s rss_peak=92MiB state=completed
[ 1722.0s]     repeats [114.577, 114.667, 114.745] slowest 114.745s warmup(traced) 562.144s tm_peak 7.0MiB ru_maxrss 97MiB digest e2ba4e0c6445 identical=True warnings=0
[ 1722.0s] stationary_solve/M4800xN4800: preflight predicted 74s (single 13.8s, trace x1.30); elapsed 1722s; remaining 1878s
[ 1766.3s]     child rc=0 wall=44.2s rss_peak=1588MiB state=completed
[ 1766.3s]     repeats [11.083, 11.057, 10.988] slowest 11.083s warmup(traced) 10.925s tm_peak 1054.7MiB ru_maxrss 1588MiB digest bdecbb2f2458 identical=True warnings=0
[ 1766.3s] stationary_solve/M4800xN19200: preflight predicted 222s (single 44.3s, trace x1.00); elapsed 1766s; remaining 1834s
[ 1915.6s]     child rc=0 wall=149.3s rss_peak=1569MiB state=completed
[ 1915.6s]     repeats [36.884, 37.208, 37.154] slowest 37.208s warmup(traced) 37.911s tm_peak 1054.7MiB ru_maxrss 1575MiB digest 34aa7538a2b4 identical=True warnings=0
[ 1915.6s] stationary_solve/M4800xN76800: preflight predicted 893s (single 177.3s, trace x1.03); elapsed 1916s; remaining 1684s
[ 2493.1s]     child rc=0 wall=577.4s rss_peak=1585MiB state=completed
[ 2493.1s]     repeats [141.514, 142.011, 141.806] slowest 142.011s warmup(traced) 151.952s tm_peak 1054.7MiB ru_maxrss 1589MiB digest f3924699111b identical=True warnings=0
[ 2493.2s] session end: wall 2493.2s; results/ unchanged=True package unchanged=True
```
