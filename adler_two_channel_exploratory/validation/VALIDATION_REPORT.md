# Intended-configuration validation campaign — report

**Nothing here is a physical finding, an approval, or a sufficiency promise.**  Every stage keeps its predeclared success, `numerical_no_result`, dependency and stop rules; a stage that misses its target is a numerical no-result, never a reason to widen a budget.  M7 was not launched (`pricing_unresolved`).

Session 2026-09-02T23:33:17-0600 → 2026-09-03T00:33:44-0600, wall 3627 s (60.5 min) of the 7200 s budget; per-process RSS ceiling 2 GiB.

## Environment identity

| Field | Value |
| --- | --- |
| platform | `macOS-26.5.2-arm64-arm-64bit-Mach-O` |
| cpu_brand | `Apple M4 Pro` |
| physical_cpus | `12` |
| memory_bytes | `25769803776` |
| os_version | `26.5.2` |
| python_version | `3.13.11` |
| numpy_version | `2.4.3` |
| numpy_blas | `accelerate` |
| environment digest | `9dfcbc23f4c8b0902b797b311bf4250546eb42d400a6f3dac719aae0e30d3c56` |
| package source fingerprint | `8bb1a4eddd8b93a3458393bd027536e3b6f7a5f51d49fa561f7161926b945992` |
| repo git HEAD | `edaee80791e85c80b1c425cca9da2d7c40726fcb` |
| frozen ticket-07 budget digest | `8ff45c2c33c01192129320db814f367845c4cf29cf05cbb7372af8aa0886da61` (trials/cell 2406, allowances {'count': 0.004994710172401896, 'probability': 0.004994710172401896, 'time': 0.021953125}) |
| pricing derivation used for preflight | `7c8c0f81d1f69f12f5043a352d2571f2b5f97a922b05634a4729d0f3f0062018` |

## Tree integrity

- `results/` (1176 entries) unchanged by SHA-256 snapshot = **True**; package tree (incl. `__pycache__`) unchanged = **True**.
- One child process at a time; the parent polled its RSS every 50 ms.  No verifier run, no pilot, production, sensitivity or exponent fit, no exponent output opened.

### Events

- S2: stopped by dependency on S1 (numerical_no_result)
- S3: stopped by dependency on S2 (None)
- S4: stopped by dependency on S3 (None)
- M6: stopped by dependency on M5 (numerical_no_result)
- M7: not launched (pricing_unresolved)

## Intended configuration and cells

- Production physics (verify.py `_t07_config`/`_t07_matrix`): {"clocks": 64, "dwell_time": 0.5, "grid_half_width": 3.0, "lock_tolerance": 0.35, "peak_coupling": 1.0, "phase_diffusion": 0.08, "pulse_centre": 0.0, "pulse_duration": 4.0, "timestep": 0.001953125}
- Stationary cell: {"base_fine_steps": 2048, "base_space": 600, "base_time": 600, "chunk": 1500, "coupling": 1.0, "detuning": 0.421875, "diffusion": 0.08, "fractions": [0.25, 0.5, 0.75], "horizon": 2.0, "namespace": "t07-campaign-stationary", "quantile": 0.35, "resamples": 200, "seed": 20260828, "strides": [8, 4, 2], "tolerance": 0.35, "walkers": 6000, "window": 1024}
- Moving cell: {"audit_namespace": "t07-campaign-auxiliary", "base_step": 0.001953125, "base_steps": 2048, "base_trials": 40, "centre": 0.0, "clocks": [[32, 0.046875, "central"], [36, 0.421875, "interior+"], [22, -0.890625, "near_edge-"]], "diffusion": 0.08, "duration": 4.0, "dwell": 0.5, "label_prefix": "T07/campaign", "origin": -2.0, "peak": 1.0, "physical_namespace": "t07-campaign-physical", "quantile": 0.2, "replicates": 4, "resamples": 200, "seed": 20260901, "strides": [4, 2, 1], "survival_fractions": [0.45, 0.6, 0.8], "tolerance": 0.35}
- Moving clocks (grid index, detuning, regime): [[32, 0.046875, 'central'], [36, 0.421875, 'interior+'], [22, -0.890625, 'near_edge-']]

## Stages

| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **REF_S3** ticket-04 S3 stationary reference ladder (reproduction, non_intended) | completed | oracle [600, 600], fine steps 2048, timesteps ['0.00781', '0.00391', '0.00195'], walkers 6000 | pass | ok {"gate_pass": true, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 36.56536152065438, "paired_bitwise": true, "survival_sign_ok": true} | — | **reference** | 6.9 s | 231 MiB |
| **REF_S3B** ticket-04 S3b pooled moving-band ladder (reproduction, non_intended) | completed | 40 trials x 3 clocks x 4 replicates, mesh step 0.008, 500 steps, timesteps ['0.032', '0.016', '0.008'] | numerical_no_result | ok {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true} | — | **reference** | 13.6 s | 55 MiB |
| **S1** stationary probability, dt/16 at doubled space | completed | oracle [1200, 9600], fine steps 32768, timesteps ['0.000488', '0.000244', '0.000122'], walkers 6000 | numerical_no_result | ok {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 888.9715200191995, "paired_bitwise": true, "survival_sign_ok": true} | 0/9 fit (probability) | **numerical_no_result** | 21.4 s | 635 MiB |
| **S2** stationary probability, dt/64 at quadrupled space | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **S3** stationary probability, dt/256 at eightfold space | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **S4** stationary time quantile, dt/256 at eightfold space | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **M5** moving-band probability, 64x master trials | completed | 2560 trials x 3 clocks x 4 replicates, mesh step 0.00195, 2048 steps, timesteps ['0.00781', '0.00391', '0.00195'] | numerical_no_result | ok {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true} | 1/4 fit (probability) | **numerical_no_result** | 3585 s (59.8 min) | 76 MiB |
| **M6** moving-band probability, dt/16 replay | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **M7** moving-band time quantile, 1024x master trials | not_launched | — | — | — | — | **not_launched** | — | — |

### REF_S3 — ticket-04 S3 stationary reference ladder (reproduction, non_intended)

- State `completed`, stage verdict **reference**.
- Rules applied: killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) …; stage rule: verify.py _t07_campaign success_rule: "every - row of this ladder must land, bias plus 2.0 standard errors, under the frozen - allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"
- Ladder gate verdict **pass**.  Procedure checks: {"gate_pass": true, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 36.56536152065438, "paired_bitwise": true, "survival_sign_ok": true}; oracle gap 1.175e-04 (refined grid [1200, 1200]), smallest finest error 4.297e-03.  Dataset digest `1018571a766f119d…`, budgets digest `cb248c2b9f45071d…`.
- Work {"endpoint_observations": 32256000, "resample_observations": 43200000, "space_time_cells": 1800000}; preflight 5.7 s; actual 6.9 s; timing {"compare_seconds": 2.2484597500006203, "dataset_seconds": 4.013284792017657, "oracle_margin_seconds": 0.12843091698596254, "oracle_seconds": 0.02463908400386572, "walk_seconds": 0.3939902499841992}; peak RSS 231 MiB (parent-observed 230 MiB); warnings 0.

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.184397 | 0.007812 | 0.44033 | 0.48036 | 0.04003 | 0.00627 | 0.00000 | 0.00157 |
| exit_count_lower | x=0.184397 | 0.003906 | 0.45083 | 0.48036 | 0.02953 | 0.00614 | 0.00125 | 0.00157 |
| exit_count_lower | x=0.184397 | 0.001953 | 0.45650 | 0.48036 | 0.02386 | 0.00607 | 0.00103 | 0.00157 |
| exit_count_lower | x=0.384397 | 0.007812 | 0.23817 | 0.26319 | 0.02503 | 0.00592 | 0.00000 | 0.00145 |
| exit_count_lower | x=0.384397 | 0.003906 | 0.24467 | 0.26319 | 0.01853 | 0.00592 | 0.00103 | 0.00145 |
| exit_count_lower | x=0.384397 | 0.001953 | 0.24900 | 0.26319 | 0.01419 | 0.00590 | 0.00094 | 0.00145 |
| exit_count_lower | x=0.584397 | 0.007812 | 0.12450 | 0.13573 | 0.01123 | 0.00426 | 0.00000 | 0.00212 |
| exit_count_lower | x=0.584397 | 0.003906 | 0.12783 | 0.13573 | 0.00790 | 0.00419 | 0.00122 | 0.00212 |
| exit_count_lower | x=0.584397 | 0.001953 | 0.13100 | 0.13573 | 0.00473 | 0.00386 | 0.00151 | 0.00212 |
| exit_count_upper | x=0.184397 | 0.007812 | 0.13450 | 0.14530 | 0.01080 | 0.00409 | 0.00000 | 0.00233 |
| exit_count_upper | x=0.184397 | 0.003906 | 0.13700 | 0.14530 | 0.00830 | 0.00405 | 0.00110 | 0.00233 |
| exit_count_upper | x=0.184397 | 0.001953 | 0.14100 | 0.14530 | 0.00430 | 0.00328 | 0.00202 | 0.00233 |
| exit_count_upper | x=0.384397 | 0.007812 | 0.25067 | 0.27607 | 0.02540 | 0.00515 | 0.00000 | 0.00141 |
| exit_count_upper | x=0.384397 | 0.003906 | 0.25700 | 0.27607 | 0.01907 | 0.00508 | 0.00113 | 0.00141 |
| exit_count_upper | x=0.384397 | 0.001953 | 0.26183 | 0.27607 | 0.01424 | 0.00509 | 0.00095 | 0.00141 |
| exit_count_upper | x=0.584397 | 0.007812 | 0.45767 | 0.49896 | 0.04130 | 0.00643 | 0.00000 | 0.00175 |
| exit_count_upper | x=0.584397 | 0.003906 | 0.46900 | 0.49896 | 0.02996 | 0.00640 | 0.00140 | 0.00175 |
| exit_count_upper | x=0.584397 | 0.001953 | 0.47517 | 0.49896 | 0.02380 | 0.00645 | 0.00097 | 0.00175 |
| exit_quantile_p35 | x=0.184397 | 0.007812 | 0.98438 | 0.79888 | 0.18550 | 0.02751 | 0.00000 | 0.01153 |
| exit_quantile_p35 | x=0.184397 | 0.003906 | 0.93750 | 0.79888 | 0.13862 | 0.02138 | 0.01023 | 0.01153 |
| exit_quantile_p35 | x=0.184397 | 0.001953 | 0.91016 | 0.79888 | 0.11128 | 0.02081 | 0.00545 | 0.01153 |
| exit_quantile_p35 | x=0.384397 | 0.007812 | 1.41406 | 1.25155 | 0.16251 | 0.02786 | 0.00000 | 0.01260 |
| exit_quantile_p35 | x=0.384397 | 0.003906 | 1.37754 | 1.25155 | 0.12599 | 0.02185 | 0.01019 | 0.01260 |
| exit_quantile_p35 | x=0.384397 | 0.001953 | 1.34307 | 1.25155 | 0.09151 | 0.02074 | 0.00717 | 0.01260 |
| exit_quantile_p35 | x=0.584397 | 0.007812 | 0.91406 | 0.75637 | 0.15769 | 0.02164 | 0.00000 | 0.00950 |
| exit_quantile_p35 | x=0.584397 | 0.003906 | 0.87109 | 0.75637 | 0.11472 | 0.02089 | 0.00724 | 0.00950 |
| exit_quantile_p35 | x=0.584397 | 0.001953 | 0.84375 | 0.75637 | 0.08738 | 0.02259 | 0.00692 | 0.00950 |
| survival | x=0.184397 | 0.007812 | 0.42517 | 0.37434 | 0.05082 | 0.00600 | 0.00000 | 0.00181 |
| survival | x=0.184397 | 0.003906 | 0.41217 | 0.37434 | 0.03782 | 0.00582 | 0.00135 | 0.00181 |
| survival | x=0.184397 | 0.001953 | 0.40250 | 0.37434 | 0.02816 | 0.00579 | 0.00130 | 0.00181 |
| survival | x=0.384397 | 0.007812 | 0.51117 | 0.46074 | 0.05043 | 0.00636 | 0.00000 | 0.00184 |
| survival | x=0.384397 | 0.003906 | 0.49833 | 0.46074 | 0.03759 | 0.00615 | 0.00153 | 0.00184 |
| survival | x=0.384397 | 0.001953 | 0.48917 | 0.46074 | 0.02843 | 0.00602 | 0.00125 | 0.00184 |
| survival | x=0.584397 | 0.007812 | 0.41783 | 0.36530 | 0.05253 | 0.00652 | 0.00000 | 0.00221 |
| survival | x=0.584397 | 0.003906 | 0.40317 | 0.36530 | 0.03786 | 0.00637 | 0.00174 | 0.00221 |
| survival | x=0.584397 | 0.001953 | 0.39383 | 0.36530 | 0.02853 | 0.00636 | 0.00118 | 0.00221 |

### REF_S3B — ticket-04 S3b pooled moving-band ladder (reproduction, non_intended)

- State `completed`, stage verdict **reference**.
- Rules applied: killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) …; stage rule: verify.py _t07_campaign success_rule: "every - row of this ladder must land, bias plus 2.0 standard errors, under the frozen - allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"
- Ladder gate verdict **numerical_no_result**; reasons: ["('commit_time_quantile_p20_shift', 'pooled'): [absolute_cap] 0.0112 time with standard error 0.0829003 gives a 2-sigma bound 0.177001 past the cap 0.1"].  Procedure checks: {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true}.  Dataset digest `a1b71abec7557997…`, budgets digest `aeb97e3c0c7e5f75…`.
- Work {"audited_evaluations": 246880, "physical_intervals": 105480, "resample_observations": 144000}; preflight 21.5 s; actual 13.6 s; timing {"compare_seconds": 0.03714050000417046, "dataset_seconds": 0.0009963330230675638, "ladder_seconds": 13.396854749997146}; peak RSS 55 MiB (parent-observed 55 MiB); warnings 0.

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean | pooled | 0.032 | 0.47708 | 0.00000 | 0.47708 | 0.11019 | 0.00000 | 0.15739 |
| added_resets_mean | pooled | 0.016 | 0.61042 | 0.00000 | 0.61042 | 0.13768 | 0.07396 | 0.15739 |
| added_resets_mean | pooled | 0.008 | 0.98125 | 0.00000 | 0.98125 | 0.23208 | 0.11244 | 0.15739 |
| commit_probability_shift | pooled | 0.032 | -0.00625 | 0.00000 | 0.00625 | 0.00496 | 0.00000 | 0.00694 |
| commit_probability_shift | pooled | 0.016 | -0.00417 | 0.00000 | 0.00417 | 0.00303 | 0.00457 | 0.00694 |
| commit_probability_shift | pooled | 0.008 | -0.00833 | 0.00000 | 0.00833 | 0.00536 | 0.00481 | 0.00694 |
| commit_time_quantile_p20_shift | pooled | 0.032 | 0.13440 | 0.00000 | 0.13440 | 0.13909 | 0.00000 | 0.15065 |
| commit_time_quantile_p20_shift | pooled | 0.016 | 0.11520 | 0.00000 | 0.11520 | 0.12679 | 0.13771 | 0.15065 |
| commit_time_quantile_p20_shift | pooled | 0.008 | 0.01120 | 0.00000 | 0.01120 | 0.08290 | 0.12494 | 0.15065 |
| survival_shift_at_0.45 | pooled | 0.032 | 0.01042 | 0.00000 | 0.01042 | 0.00804 | 0.00000 | 0.00804 |
| survival_shift_at_0.45 | pooled | 0.016 | 0.00833 | 0.00000 | 0.00833 | 0.00745 | 0.00203 | 0.00804 |
| survival_shift_at_0.45 | pooled | 0.008 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00745 | 0.00804 |
| survival_shift_at_0.60 | pooled | 0.032 | 0.01042 | 0.00000 | 0.01042 | 0.00768 | 0.00000 | 0.00768 |
| survival_shift_at_0.60 | pooled | 0.016 | 0.01042 | 0.00000 | 0.01042 | 0.00768 | 0.00000 | 0.00768 |
| survival_shift_at_0.60 | pooled | 0.008 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00768 | 0.00768 |
| survival_shift_at_0.80 | pooled | 0.032 | 0.02292 | 0.00000 | 0.02292 | 0.01123 | 0.00000 | 0.00544 |
| survival_shift_at_0.80 | pooled | 0.016 | 0.01250 | 0.00000 | 0.01250 | 0.00788 | 0.00726 | 0.00544 |
| survival_shift_at_0.80 | pooled | 0.008 | 0.01458 | 0.00000 | 0.01458 | 0.00914 | 0.00426 | 0.00544 |

### S1 — stationary probability, dt/16 at doubled space

- State `completed`, stage verdict **numerical_no_result**.
- Reason: ladder gate: ('exit_count_lower', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging
- Reason: 9 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.02768 (5.5x); exit_count_lower@x=0.435512 bound 0.02063 (4.1x); exit_count_lower@x=0.610512 bound 0.0131 (2.6x); exit_count_upper@x=0.260512 bound 0.01902 (3.8x); exit_count_upper@x=0.435512 bound 0.0102 (2.0x); exit_count_upper@x=0.610512 bound 0.01258 (2.5x); survival@x=0.260512 bound 0.01408 (2.8x); survival@x=0.435512 bound 0.02132 (4.3x); survival@x=0.610512 bound 0.01682 (3.4x)
- Rules applied: killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) …; stage rule: verify.py _t07_campaign success_rule: "every probability row of this ladder must land, bias plus 2.0 standard errors, under the frozen probability allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"
- Ladder gate verdict **numerical_no_result**; reasons: ["('exit_count_lower', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging"].  Procedure checks: {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 888.9715200191995, "paired_bitwise": true, "survival_sign_ok": true}; oracle gap 2.955e-06 (refined grid [2400, 19200]), smallest finest error 2.627e-03.  Dataset digest `110ea3c3c9d6a1a3…`, budgets digest `7c5eff8d642b5171…`.
- Work {"endpoint_observations": 516096000, "resample_observations": 43200000, "space_time_cells": 57600000}; preflight 61.4 s; actual 21.4 s; timing {"compare_seconds": 2.3271800839866046, "dataset_seconds": 4.150871833990095, "oracle_margin_seconds": 7.078448167012539, "oracle_seconds": 0.6574422080011573, "walk_seconds": 7.049871167022502}; peak RSS 635 MiB (parent-observed 635 MiB); warnings 0.

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 0.0004883 | 0.63800 | 0.65920 | 0.02120 | 0.00589 | 0.00000 | 0.00123 |
| exit_count_lower | x=0.260512 | 0.0002441 | 0.64100 | 0.65920 | 0.01820 | 0.00593 | 0.00091 | 0.00123 |
| exit_count_lower | x=0.260512 | 0.0001221 | 0.64333 | 0.65920 | 0.01587 | 0.00591 | 0.00080 | 0.00123 |
| exit_count_lower | x=0.435512 | 0.0004883 | 0.42717 | 0.44058 | 0.01341 | 0.00533 | 0.00000 | 0.00104 |
| exit_count_lower | x=0.435512 | 0.0002441 | 0.42883 | 0.44058 | 0.01174 | 0.00526 | 0.00067 | 0.00104 |
| exit_count_lower | x=0.435512 | 0.0001221 | 0.43033 | 0.44058 | 0.01024 | 0.00519 | 0.00066 | 0.00104 |
| exit_count_lower | x=0.610512 | 0.0004883 | 0.24400 | 0.24761 | 0.00361 | 0.00350 | 0.00000 | 0.00150 |
| exit_count_lower | x=0.610512 | 0.0002441 | 0.24333 | 0.24761 | 0.00428 | 0.00369 | 0.00094 | 0.00150 |
| exit_count_lower | x=0.610512 | 0.0001221 | 0.24250 | 0.24761 | 0.00511 | 0.00400 | 0.00087 | 0.00150 |
| exit_count_upper | x=0.260512 | 0.0004883 | 0.26633 | 0.25721 | 0.00912 | 0.00521 | 0.00000 | 0.00109 |
| exit_count_upper | x=0.260512 | 0.0002441 | 0.26683 | 0.25721 | 0.00962 | 0.00525 | 0.00085 | 0.00109 |
| exit_count_upper | x=0.260512 | 0.0001221 | 0.26600 | 0.25721 | 0.00879 | 0.00512 | 0.00081 | 0.00109 |
| exit_count_upper | x=0.435512 | 0.0004883 | 0.44617 | 0.45113 | 0.00496 | 0.00441 | 0.00000 | 0.00209 |
| exit_count_upper | x=0.435512 | 0.0002441 | 0.44783 | 0.45113 | 0.00329 | 0.00395 | 0.00153 | 0.00209 |
| exit_count_upper | x=0.435512 | 0.0001221 | 0.44850 | 0.45113 | 0.00263 | 0.00379 | 0.00076 | 0.00209 |
| exit_count_upper | x=0.610512 | 0.0004883 | 0.65900 | 0.67021 | 0.01121 | 0.00543 | 0.00000 | 0.00338 |
| exit_count_upper | x=0.610512 | 0.0002441 | 0.66333 | 0.67021 | 0.00687 | 0.00466 | 0.00202 | 0.00338 |
| exit_count_upper | x=0.610512 | 0.0001221 | 0.66567 | 0.67021 | 0.00454 | 0.00402 | 0.00177 | 0.00338 |
| exit_quantile_p35 | x=0.260512 | 0.0004883 | 0.32600 | 0.29633 | 0.02967 | 0.00838 | 0.00000 | 0.00296 |
| exit_quantile_p35 | x=0.260512 | 0.0002441 | 0.31876 | 0.29633 | 0.02243 | 0.00823 | 0.00166 | 0.00296 |
| exit_quantile_p35 | x=0.260512 | 0.0001221 | 0.31160 | 0.29633 | 0.01527 | 0.00817 | 0.00240 | 0.00296 |
| exit_quantile_p35 | x=0.435512 | 0.0004883 | 0.52686 | 0.50885 | 0.01801 | 0.00812 | 0.00000 | 0.00284 |
| exit_quantile_p35 | x=0.435512 | 0.0002441 | 0.52197 | 0.50885 | 0.01313 | 0.00746 | 0.00204 | 0.00284 |
| exit_quantile_p35 | x=0.435512 | 0.0001221 | 0.51880 | 0.50885 | 0.00995 | 0.00727 | 0.00209 | 0.00284 |
| exit_quantile_p35 | x=0.610512 | 0.0004883 | 0.30127 | 0.28690 | 0.01437 | 0.00838 | 0.00000 | 0.00483 |
| exit_quantile_p35 | x=0.610512 | 0.0002441 | 0.29346 | 0.28690 | 0.00656 | 0.00655 | 0.00344 | 0.00483 |
| exit_quantile_p35 | x=0.610512 | 0.0001221 | 0.29114 | 0.28690 | 0.00424 | 0.00577 | 0.00194 | 0.00483 |
| survival | x=0.260512 | 0.0004883 | 0.09567 | 0.08358 | 0.01208 | 0.00360 | 0.00000 | 0.00096 |
| survival | x=0.260512 | 0.0002441 | 0.09217 | 0.08358 | 0.00858 | 0.00359 | 0.00076 | 0.00096 |
| survival | x=0.260512 | 0.0001221 | 0.09067 | 0.08358 | 0.00708 | 0.00350 | 0.00056 | 0.00096 |
| survival | x=0.435512 | 0.0004883 | 0.12667 | 0.10830 | 0.01837 | 0.00429 | 0.00000 | 0.00100 |
| survival | x=0.435512 | 0.0002441 | 0.12333 | 0.10830 | 0.01504 | 0.00424 | 0.00080 | 0.00100 |
| survival | x=0.435512 | 0.0001221 | 0.12117 | 0.10830 | 0.01287 | 0.00423 | 0.00055 | 0.00100 |
| survival | x=0.610512 | 0.0004883 | 0.09700 | 0.08218 | 0.01482 | 0.00395 | 0.00000 | 0.00122 |
| survival | x=0.610512 | 0.0002441 | 0.09333 | 0.08218 | 0.01115 | 0.00368 | 0.00090 | 0.00122 |
| survival | x=0.610512 | 0.0001221 | 0.09183 | 0.08218 | 0.00965 | 0.00359 | 0.00061 | 0.00122 |

Stage rule rows (probability, finest level; bound = |error| + 2 SE vs allowance 0.00499471):

| Observable | Position | |error| | SE | bound | ratio to allowance | fits |
| --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 0.01587 | 0.00591 | 0.02768 | 5.54x | NO |
| exit_count_lower | x=0.435512 | 0.01024 | 0.00519 | 0.02063 | 4.13x | NO |
| exit_count_lower | x=0.610512 | 0.00511 | 0.00400 | 0.01310 | 2.62x | NO |
| exit_count_upper | x=0.260512 | 0.00879 | 0.00512 | 0.01902 | 3.81x | NO |
| exit_count_upper | x=0.435512 | 0.00263 | 0.00379 | 0.01020 | 2.04x | NO |
| exit_count_upper | x=0.610512 | 0.00454 | 0.00402 | 0.01258 | 2.52x | NO |
| survival | x=0.260512 | 0.00708 | 0.00350 | 0.01408 | 2.82x | NO |
| survival | x=0.435512 | 0.01287 | 0.00423 | 0.02132 | 4.27x | NO |
| survival | x=0.610512 | 0.00965 | 0.00359 | 0.01682 | 3.37x | NO |

### S2 — stationary probability, dt/64 at quadrupled space

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S1 returned numerical_no_result; a later stage never runs on an unresolved one

### S3 — stationary probability, dt/256 at eightfold space

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S2 returned nothing; a later stage never runs on an unresolved one

### S4 — stationary time quantile, dt/256 at eightfold space

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S3 returned nothing; a later stage never runs on an unresolved one

### M5 — moving-band probability, 64x master trials

- State `completed`, stage verdict **numerical_no_result**.
- Reason: ladder gate: ('added_resets_mean', 'pooled'): [absolute_cap] 3.6123 count with standard error 0.0769676 gives a 2-sigma bound 3.76624 past the cap 3
- Reason: 3 of 4 probability rows exceed the allowance 0.00499471: commit_probability_shift@pooled bound 0.01156 (2.3x); survival_shift_at_0.60@pooled bound 0.008534 (1.7x); survival_shift_at_0.80@pooled bound 0.01169 (2.3x)
- Rules applied: killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) …; stage rule: verify.py _t07_campaign success_rule: "every probability row of this ladder must land, bias plus 2.0 standard errors, under the frozen probability allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"
- Ladder gate verdict **numerical_no_result**; reasons: ["('added_resets_mean', 'pooled'): [absolute_cap] 3.6123 count with standard error 0.0769676 gives a 2-sigma bound 3.76624 past the cap 3"].  Procedure checks: {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true}.  Dataset digest `64ff29574b0ad19b…`, budgets digest `5f405885c890dbb6…`.
- Work {"audited_evaluations": 59719680, "physical_intervals": 27571200, "resample_observations": 9216000}; preflight 5624 s (93.7 min); actual 3585 s (59.8 min); timing {"compare_seconds": 0.38352874998236075, "dataset_seconds": 0.36874616699060425, "ladder_seconds": 3584.165349125018}; peak RSS 76 MiB (parent-observed 76 MiB); warnings 0.

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean | pooled | 0.007812 | 1.76003 | 0.00000 | 1.76003 | 0.03787 | 0.00000 | 0.04411 |
| added_resets_mean | pooled | 0.003906 | 2.52474 | 0.00000 | 2.52474 | 0.05480 | 0.02170 | 0.04411 |
| added_resets_mean | pooled | 0.001953 | 3.61230 | 0.00000 | 3.61230 | 0.07697 | 0.02852 | 0.04411 |
| commit_probability_shift | pooled | 0.007812 | -0.01865 | 0.00000 | 0.01865 | 0.00147 | 0.00000 | 0.00126 |
| commit_probability_shift | pooled | 0.003906 | -0.01286 | 0.00000 | 0.01286 | 0.00114 | 0.00102 | 0.00126 |
| commit_probability_shift | pooled | 0.001953 | -0.00954 | 0.00000 | 0.00954 | 0.00101 | 0.00076 | 0.00126 |
| commit_time_quantile_p20_shift | pooled | 0.007812 | 0.12500 | 0.00000 | 0.12500 | 0.01523 | 0.00000 | 0.01373 |
| commit_time_quantile_p20_shift | pooled | 0.003906 | 0.08984 | 0.00000 | 0.08984 | 0.01297 | 0.01163 | 0.01373 |
| commit_time_quantile_p20_shift | pooled | 0.001953 | 0.05898 | 0.00000 | 0.05898 | 0.01231 | 0.00887 | 0.01373 |
| survival_shift_at_0.45 | pooled | 0.007812 | 0.00651 | 0.00000 | 0.00651 | 0.00083 | 0.00000 | 0.00071 |
| survival_shift_at_0.45 | pooled | 0.003906 | 0.00381 | 0.00000 | 0.00381 | 0.00059 | 0.00057 | 0.00071 |
| survival_shift_at_0.45 | pooled | 0.001953 | 0.00326 | 0.00000 | 0.00326 | 0.00059 | 0.00043 | 0.00071 |
| survival_shift_at_0.60 | pooled | 0.007812 | 0.01146 | 0.00000 | 0.01146 | 0.00100 | 0.00000 | 0.00108 |
| survival_shift_at_0.60 | pooled | 0.003906 | 0.00872 | 0.00000 | 0.00872 | 0.00088 | 0.00089 | 0.00108 |
| survival_shift_at_0.60 | pooled | 0.001953 | 0.00684 | 0.00000 | 0.00684 | 0.00085 | 0.00067 | 0.00108 |
| survival_shift_at_0.80 | pooled | 0.007812 | 0.01911 | 0.00000 | 0.01911 | 0.00150 | 0.00000 | 0.00126 |
| survival_shift_at_0.80 | pooled | 0.003906 | 0.01263 | 0.00000 | 0.01263 | 0.00115 | 0.00107 | 0.00126 |
| survival_shift_at_0.80 | pooled | 0.001953 | 0.00967 | 0.00000 | 0.00967 | 0.00101 | 0.00075 | 0.00126 |

Stage rule rows (probability, finest level; bound = |error| + 2 SE vs allowance 0.00499471):

| Observable | Position | |error| | SE | bound | ratio to allowance | fits |
| --- | --- | --- | --- | --- | --- | --- |
| commit_probability_shift | pooled | 0.00954 | 0.00101 | 0.01156 | 2.31x | NO |
| survival_shift_at_0.45 | pooled | 0.00326 | 0.00059 | 0.00444 | 0.89x | yes |
| survival_shift_at_0.60 | pooled | 0.00684 | 0.00085 | 0.00853 | 1.71x | NO |
| survival_shift_at_0.80 | pooled | 0.00967 | 0.00101 | 0.01169 | 2.34x | NO |

### M6 — moving-band probability, dt/16 replay

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor M5 returned numerical_no_result; a later stage never runs on an unresolved one

### M7 — moving-band time quantile, 1024x master trials

- State `not_launched`, stage verdict **not_launched**.
- Reason: pricing_unresolved in the pricing session: replay work 128x and comparison work 17.1x beyond the largest measured points (16x limit)

## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)

experiments.numerical_disposition: bound = |measured| + coverage_sigma * SE compared with budget.allowance(unit) (probability: 0.25 * planned 95% half-width at 2406 trials = 0.004995; time: 0.25 * 0.08 + one intended timestep = 0.021953); blockers: a numerical_no_result row is carried through; bound > allowance; not measured at the intended configuration; probability window empty below 2406 trials; any time row failing fails at every trial count.  README: "A measured discrepancy, inflated by the budget's own frozen coverage sigma, must sit under one quarter of the planned production 95 % half-width, with one intended timestep added for a commit-time quantile."

### Evidence set `reference_only` (17 rows; configurations ['non_intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (needs 2406); time admissible False; overall admissible trials 0.
- Limiting rows: {"count": null, "probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.17700055614529983, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.584397 | probability | 0.04125 | 0.00499 | 8.26x | NO |
| stationary_oracle | survival | x=0.384397 | probability | 0.04047 | 0.00499 | 8.10x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.17700 | 0.02195 | 8.06x | NO |
| stationary_oracle | survival | x=0.184397 | probability | 0.03974 | 0.00499 | 7.96x | NO |
| stationary_oracle | exit_count_upper | x=0.584397 | probability | 0.03669 | 0.00499 | 7.35x | NO |
| stationary_oracle | exit_count_lower | x=0.184397 | probability | 0.03599 | 0.00499 | 7.21x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.184397 | time | 0.15290 | 0.02195 | 6.96x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.03286 | 0.00499 | 6.58x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.384397 | time | 0.13299 | 0.02195 | 6.06x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.584397 | time | 0.13255 | 0.02195 | 6.04x | NO |
| stationary_oracle | exit_count_lower | x=0.384397 | probability | 0.02599 | 0.00499 | 5.20x | NO |
| stationary_oracle | exit_count_upper | x=0.384397 | probability | 0.02443 | 0.00499 | 4.89x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01905 | 0.00499 | 3.81x | NO |
| stationary_oracle | exit_count_lower | x=0.584397 | probability | 0.01245 | 0.00499 | 2.49x | NO |
| stationary_oracle | exit_count_upper | x=0.184397 | probability | 0.01086 | 0.00499 | 2.17x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### Evidence set `reference_plus_intended` (34 rows; configurations ['intended', 'non_intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (needs 2406); time admissible False; overall admissible trials 0.
- Limiting rows: {"count": null, "probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.17700055614529983, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.584397 | probability | 0.04125 | 0.00499 | 8.26x | NO |
| stationary_oracle | survival | x=0.384397 | probability | 0.04047 | 0.00499 | 8.10x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.17700 | 0.02195 | 8.06x | NO |
| stationary_oracle | survival | x=0.184397 | probability | 0.03974 | 0.00499 | 7.96x | NO |
| stationary_oracle | exit_count_upper | x=0.584397 | probability | 0.03669 | 0.00499 | 7.35x | NO |
| stationary_oracle | exit_count_lower | x=0.184397 | probability | 0.03599 | 0.00499 | 7.21x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.184397 | time | 0.15290 | 0.02195 | 6.96x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.03286 | 0.00499 | 6.58x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.384397 | time | 0.13299 | 0.02195 | 6.06x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.584397 | time | 0.13255 | 0.02195 | 6.04x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.02768 | 0.00499 | 5.54x | NO |
| stationary_oracle | exit_count_lower | x=0.384397 | probability | 0.02599 | 0.00499 | 5.20x | NO |
| stationary_oracle | exit_count_upper | x=0.384397 | probability | 0.02443 | 0.00499 | 4.89x | NO |
| stationary_oracle | survival | x=0.435512 | probability | 0.02132 | 0.00499 | 4.27x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.02063 | 0.00499 | 4.13x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01905 | 0.00499 | 3.81x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.08361 | 0.02195 | 3.81x | NO |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.01902 | 0.00499 | 3.81x | NO |
| stationary_oracle | survival | x=0.610512 | probability | 0.01682 | 0.00499 | 3.37x | NO |
| stationary_oracle | survival | x=0.260512 | probability | 0.01408 | 0.00499 | 2.82x | NO |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.01310 | 0.00499 | 2.62x | NO |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.01258 | 0.00499 | 2.52x | NO |
| stationary_oracle | exit_count_lower | x=0.584397 | probability | 0.01245 | 0.00499 | 2.49x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| stationary_oracle | exit_count_upper | x=0.184397 | probability | 0.01086 | 0.00499 | 2.17x | NO |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.01020 | 0.00499 | 2.04x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.03161 | 0.02195 | 1.44x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.02449 | 0.02195 | 1.12x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.01578 | 0.02195 | 0.72x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### Evidence set `intended_only` (17 rows; configurations ['intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 78 (needs 2406); time admissible False; overall admissible trials 0.
- Limiting rows: {"count": null, "probability": ["stationary_oracle", "exit_count_lower", "x=0.260512", "probability", 0.02768332351862115, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.08360834184430277, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.02768 | 0.00499 | 5.54x | NO |
| stationary_oracle | survival | x=0.435512 | probability | 0.02132 | 0.00499 | 4.27x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.02063 | 0.00499 | 4.13x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.08361 | 0.02195 | 3.81x | NO |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.01902 | 0.00499 | 3.81x | NO |
| stationary_oracle | survival | x=0.610512 | probability | 0.01682 | 0.00499 | 3.37x | NO |
| stationary_oracle | survival | x=0.260512 | probability | 0.01408 | 0.00499 | 2.82x | NO |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.01310 | 0.00499 | 2.62x | NO |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.01258 | 0.00499 | 2.52x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.01020 | 0.00499 | 2.04x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.03161 | 0.02195 | 1.44x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.02449 | 0.02195 | 1.12x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.01578 | 0.02195 | 0.72x | yes |

## Rules quoted

- **stage_success**: verify.py _t07_campaign success_rule: "every {unit} row of this ladder must land, bias plus 2.0 standard errors, under the frozen {unit} allowance {allowance:.6g} at the trial count the matrix proposes"
- **stage_no_result**: verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"
- **stage_stop**: verify.py _t07_campaign stop_rule: "stop at the first stage whose own predecessor returned a numerical_no_result; a later stage never runs on an unresolved one.  There is no resource cap here because there is no measured cost to cap"
- **matrix_failure**: verify.py _t07_matrix failure_rule: "a refinement ladder that misses the frozen numerical budget, or a moving-band audit that returns numerical_no_result, blocks scientific interpretation of the whole sweep; no fit window is reselected and no budget is widened after results are opened"
- **gate**: killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) budgeted and sampled with the contract's cluster and level count; (2) at the finest timestep the uncertainty-aware absolute error |error| + coverage*SE is within the absolute cap and the relative point estimate within the relative cap; (3) the finest error is no larger than the coarsest within ONE allowance (resolution floor + coverage * paired bootstrap SE of the end-to-end change); (4) at most one adjacent pair may go the wrong way, inside the floor + coverage * paired SE of that step.  Failure of any clause yields numerical_no_result.
- **frozen_contract**: README 'The frozen contract': "FrozenBudgets hashes its own contents, and compare_refinement refuses to produce a verdict at all unless the caller hands back the digest it recorded earlier."  The reference caps of verify.py _s3_budgets and _audit_caps are used unchanged; no tolerance is invented.
- **s3_oracle_margin**: verify.py (S3 check): "the oracle moved by {gap} under its own refinement, which is not a factor 20 below the smallest endpoint error it is the reference for" -> problem; i.e. oracle_gap * 20 <= smallest finest-level absolute error.
- **s3_sign**: verify.py (S3 check): "endpoint survival fell below the oracle by {x}; missing a between-step exit can only overcount uninterrupted dwell" -> problem when measured - reference < -0.02.
- **s3_zero_se**: verify.py (S3 check): "a level reports a zero bootstrap standard error; every S3 observable is a Monte Carlo estimate and none of them is deterministic".
- **s3_paired**: verify.py _s3_measured: each coarse increment must be the bit-for-bit left-to-right sum of the same fine leaves (control against PhaseNoiseStream._coarse_kicks_uniform).
- **s3b_subset**: moving_band_audit reset-only contract (README 'The audit'): "Every audited commitment is a delayed copy of an endpoint one at every level and in every cell" -> AuditedRun.subset_holds for every record.
- **s3b_edges**: README 'The reduced matrix': "Both pulse edges are covered by construction ... measured, by requiring every cell to report eligible intervals on both the rising and the falling side of its window".
- **evidence_rows**: verify.py _t07_evidence: every observable at every position at each ladder's finest level, added_resets_mean excluded (frozen with require_decrease=false, no continuum limit), measured = absolute_error, standard_error = bootstrap SE, sample_clusters = walkers / master trials, verdict = the ladder's verdict.
- **disposition**: experiments.numerical_disposition: bound = |measured| + coverage_sigma * SE compared with budget.allowance(unit) (probability: 0.25 * planned 95% half-width at 2406 trials = 0.004995; time: 0.25 * 0.08 + one intended timestep = 0.021953); blockers: a numerical_no_result row is carried through; bound > allowance; not measured at the intended configuration; probability window empty below 2406 trials; any time row failing fails at every trial count.  README: "A measured discrepancy, inflated by the budget's own frozen coverage sigma, must sit under one quarter of the planned production 95 % half-width, with one intended timestep added for a commit-time quantile."

## Ambiguities and choices

1. **'intended configuration' versus 'relative to the ticket-04 ladder'.** The frozen stage candidates say 'timestep x{f}, sample x{s}, spatial x{sp} relative to the ticket-04 ladder', while the ticket-07 blocker no_evidence_at_intended_configuration and NumericalBudget.intended_timestep (2^-9) define 'intended' by the production physics.  As instructed, the stages are run on the intended physics (pulse 4.0 at peak coupling 1.0, phase diffusion 0.08, tolerance 0.35, dwell 0.5, dt = 2^-9 on the 64-clock +-3 grid) with the outline's refinement factors and trial counts: stationary dt/f means finest endpoint step 2^-9/f (fine steps 2048*f over horizon 2.0) with the oracle grid (600*space_factor) x (600*f); moving 'x1 timestep' means the ladder (4dt, 2dt, dt) with dt = 2^-9 over the 2048-step pulse window, and dt/16 means (4,2,1) x 2^-13 over 32768 steps.
2. **the stationary cell at the intended configuration.** The S3 procedure is one fixed coupling, one fixed band, three starts.  At the intended configuration: coupling = the intended peak coupling 1.0, detuning = the intended-grid clock nearest the S3b interior regime (+0.45 -> index 36, 0.421875; the S3 reference ratio 0.3/0.8 = 0.375 maps to the same clock under an upward tie-break), tolerance 0.35, diffusion 0.08, horizon 2.0 and quantile p35 exactly as S3, starts at 0.25/0.5/0.75 of the admissible band, 6000 walkers (sample factor 1), chunk 1500 / window 1024 / strides (8,4,2) as S3.
3. **the moving cell and '64 clocks'.** The S3b pooled ladder is 3 regime clocks x master trials x 3 strides x 4 auxiliary replicates.  The outline scales its master trials (64x -> 2560) and its timestep; it does not change the clock set.  Running all 22 eligible clocks of the 64-clock grid at 2560 trials would cost ~7x more than M5's price (about 8 hours) and cannot fit the 2-hour budget, so the three regime clocks are mapped onto the intended grid (central -> index 32, 0.046875; interior+ -> 36, 0.421875; near_edge- -> 22, -0.890625; the even-parity grid has no clock at exactly 0) and keyed by their grid index.  Peak coupling 1.0 is the benchmark fixture's (_t07_config) and S3b's; the production matrix sweeps six nodes and its own dt-halving refinement at 0.6598/1.1487 is a different, unpriced design.
4. **the oracle-margin check at eightfold space.** verify.py refines the oracle (2M, 2N) and requires the change to be 20x below the smallest endpoint error.  At M = 4800 the refined grid (9600 x 307200) needs ~740 MB per dense matrix and cannot stay under 2 GiB, so for S3/S4 the check differences against the COARSER grid (2400 x 76800); for a second-order scheme that overstates the oracle's own error by about 3x, the conservative direction.  S1 and S2 use the refined grid as verify.py does.
5. **S4.** S4 is 'the same three with time observable' on the dt/256 eightfold ladder S3 already computed; the keyed streams are deterministic and digest-verified, so S4 judges the time rows of S3's frozen ladder instead of recomputing it (13 minutes), and its own stage rule is applied to the time-unit rows.
6. **frozen caps at the intended cell.** The S3 reference caps (survival 0.09/0.30/floor 0.012; p35 0.30/0.45/0.030; exit counts 0.07 and 0.08/0.45/0.012) and the S3b caps (0.10/4.0/floor 0.010; quantile floor = coarsest timestep; added_resets 3.0/30.0) are applied unchanged, as the frozen contract requires; their floors were derived for 6000 walkers / 40 trials x 4 replicates and are kept as frozen even where the sample is larger.
7. **stage verdict.** A stage 'succeeds' only if (i) compare_refinement under the frozen reference caps returns pass, (ii) the procedure's own checks pass (S3: bitwise pairing, oracle margin, bias sign, nonzero SE; S3b: reset-only subset on every record, both pulse edges on every clock), and (iii) every row of the stage's unit at the finest level satisfies |error| + 2 SE <= the frozen allowance.  Anything else is numerical_no_result and the stop rule applies to its dependents.
8. **reference reproduction.** REF_S3 and REF_S3B re-run the ticket-04 reference ladders through the same kernels (not the verifier) to validate this mirror against the README's published bounds (stationary survival 0.04125, p35 0.15290, moving p20 0.17700) and to supply the 17 non_intended rows; they are not stages.
9. **preflight.** predicted seconds = 1.5 x sum(component slowest rate from ../pricing/observations.json x the stage's work at the intended configuration, oracle-margin solve included); a stage is launched only if elapsed + predicted <= 7200 s.

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_validation_campaign.py --run
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_validation_campaign.py --derive-only
```

## Session log

```
[    0.0s] validation campaign session start
[    0.2s] source 8bb1a4eddd8b93a3 env 9dfcbc23f4c8b090 budget 8ff45c2c33c01192 allowances {'probability': 0.004994710172401896, 'time': 0.021953125, 'count': 0.004994710172401896}; pricing derivation 7c8c0f81d1f69f12
[    0.2s] REF_S3: preflight 6s predicted; elapsed 0s; budget remaining 7200s; work {'space_time_cells': 1800000, 'endpoint_observations': 32256000, 'resample_observations': 43200000}
[    7.1s]     |     oracle 600x600 solved in 0.0s
[    7.1s]     |     oracle margin (refined [1200, 1200]): gap 1.175e-04
[    7.1s]     |     endpoint walk 6000x2048 in 0.4s; paired=True
[    7.1s]     |     gate pass; checks {'paired_bitwise': True, 'oracle_margin_ok': True, 'oracle_margin_ratio': 36.56536152065438, 'survival_sign_ok': True, 'nonzero_se_ok': True, 'gate_pass': True}
[    7.1s] REF_S3: completed verdict=reference wall=7s rss=231MiB reasons=[]
[    7.1s] REF_S3B: preflight 22s predicted; elapsed 7s; budget remaining 7193s; work {'physical_intervals': 105480, 'audited_evaluations': 246880, 'resample_observations': 144000}
[   20.8s]     |     ladder 40 trials x 3 clocks x 3 strides in 13s; subset=True
[   20.8s]     |     gate numerical_no_result; checks {'subset_holds': True, 'both_edges_every_clock': True, 'gate_pass': False}
[   20.8s] REF_S3B: completed verdict=reference wall=14s rss=55MiB reasons=[]
[   20.8s] S1: preflight 61s predicted; elapsed 21s; budget remaining 7179s; work {'space_time_cells': 57600000, 'endpoint_observations': 516096000, 'resample_observations': 43200000}
[   42.2s]     |     oracle 1200x9600 solved in 0.7s
[   42.2s]     |     oracle margin (refined [2400, 19200]): gap 2.955e-06
[   42.2s]     |     endpoint walk 6000x32768 in 7.0s; paired=True
[   42.2s]     |     gate numerical_no_result; checks {'paired_bitwise': True, 'oracle_margin_ok': True, 'oracle_margin_ratio': 888.9715200191995, 'survival_sign_ok': True, 'nonzero_se_ok': True, 'gate_pass': False}
[   42.2s] S1: completed verdict=numerical_no_result wall=21s rss=635MiB reasons=["ladder gate: ('exit_count_lower', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging", '9 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.02768 (5.5x); exit_count_lower@x=0.435512 bound 0.02063 (4.1x); exit_count_lower@x=0.610512 bound 0.0131 (2.6x); exit_count_upper@x=0.260512 bound 0.01902 (3.8x); exit_count_upper@x=0.435512 bound 0.0102 (2.0x); exit_count_upper@x=0.610512 bound 0.01258 (2.5x); survival@x=0.260512 bound 0.01408 (2.8x); survival@x=0.435512 bound 0.02132 (4.3x); survival@x=0.610512 bound 0.01682 (3.4x)']
[   42.2s] S2: stopped — predecessor S1 = numerical_no_result
[   42.2s] S3: stopped — predecessor S2 = None
[   42.2s] S4: stopped — predecessor S3 = None
[   42.2s] M5: preflight 5624s predicted; elapsed 42s; budget remaining 7158s; work {'physical_intervals': 27571200, 'audited_evaluations': 59719680, 'resample_observations': 9216000}
[ 3627.3s]     |     stride 4 clock 32 (central) done at 317s
[ 3627.3s]     |     stride 4 clock 36 (interior+) done at 603s
[ 3627.3s]     |     stride 4 clock 22 (near_edge-) done at 857s
[ 3627.3s]     |     stride 2 clock 32 (central) done at 1294s
[ 3627.3s]     |     stride 2 clock 36 (interior+) done at 1672s
[ 3627.3s]     |     stride 2 clock 22 (near_edge-) done at 1985s
[ 3627.3s]     |     stride 1 clock 32 (central) done at 2639s
[ 3627.3s]     |     stride 1 clock 36 (interior+) done at 3176s
[ 3627.3s]     |     stride 1 clock 22 (near_edge-) done at 3584s
[ 3627.3s]     |     ladder 2560 trials x 3 clocks x 3 strides in 3584s; subset=True
[ 3627.3s]     |     gate numerical_no_result; checks {'subset_holds': True, 'both_edges_every_clock': True, 'gate_pass': False}
[ 3627.3s] M5: completed verdict=numerical_no_result wall=3585s rss=76MiB reasons=["ladder gate: ('added_resets_mean', 'pooled'): [absolute_cap] 3.6123 count with standard error 0.0769676 gives a 2-sigma bound 3.76624 past the cap 3", '3 of 4 probability rows exceed the allowance 0.00499471: commit_probability_shift@pooled bound 0.01156 (2.3x); survival_shift_at_0.60@pooled bound 0.008534 (1.7x); survival_shift_at_0.80@pooled bound 0.01169 (2.3x)']
[ 3627.3s] M6: stopped — predecessor M5 = numerical_no_result
[ 3627.4s] session end: wall 3627s; results/ unchanged=True package unchanged=True
```
