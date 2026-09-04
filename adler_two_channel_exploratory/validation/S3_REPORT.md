# S3 override — intended-configuration validation campaign report

**Nothing here is a physical finding, an approval, or a sufficiency promise.**  The third sponsor's override authorized S3 despite S2's `numerical_no_result` (one row, 1.05x); S4 kept the frozen dependency rule with no further override and judges S3's frozen ladder's time rows.  Every other rule stays frozen.

Session 2026-09-04T10:31:58-0600 → 2026-09-04T12:11:12-0600, wall 4040 s (67.3 min) of the 10800 s budget; per-process RSS ceiling 2 GiB; previous records `adler_two_channel_exploratory/validation/observations_redesign.json` (sha256 `5c4c4aeddb0edd61…`) and the first session (`0e2b2b9769dfcb79…`) untouched.

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
| repo git HEAD | `8c3df12288d7f78d68296a0e318c9c7c04b00b3f` |
| frozen ticket-07 budget digest | `8ff45c2c33c01192129320db814f367845c4cf29cf05cbb7372af8aa0886da61` (allowances {'count': 0.004994710172401896, 'probability': 0.004994710172401896, 'time': 0.021953125}) |
| pricing derivation used for preflight | `7c8c0f81d1f69f12f5043a352d2571f2b5f97a922b05634a4729d0f3f0062018` |
| O(walkers^2) identity-check seconds at 96,000 walkers (redesign S1) | 1544 s |

## Tree integrity

- `results/` (1176 entries) unchanged by SHA-256 = **True**; package tree (incl. `__pycache__`) unchanged = **True**.
- Strictly serial child processes (oracle phase, then construction phase, per stage); parent RSS poll every 50 ms with a 2 GiB kill.  No verifier, pilot, production, sensitivity or fit.

### Events

- S4: stopped by dependency on S3 (numerical_no_result)

## Walker count and memory

- 96000 walkers (chosen by the redesign session's memory-scaling measurement; construction-phase peak 273 MiB there).  Oracle phases run in their own child: S2 margin grid 4800 x 76800 (1,589 MiB in the pricing session); S3 uses the coarser 2400 x 76800 margin grid (refined 9600 x 307200 would exceed the cap; ~3x conservative).

## Stages

| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **S3** stationary probability, dt/256 at eightfold space (96,000 walkers; S2 stop rule overridden by the sponsor) | completed | oracle [4800, 153600], fine steps 524288, timesteps ['3.05e-05', '1.53e-05', '7.63e-06'], walkers 96000 | numerical_no_result | ok {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 3880.1703943160082, "paired_bitwise": true, "survival_sign_ok": true} | 6/9 fit (probability) | **numerical_no_result** | 4039 s (67.3 min) | 1536 MiB (oracle 1536 MiB, construction 332 MiB) |
| **S4** stationary time quantile, dt/256 at eightfold space (96,000 walkers; judged on S3's frozen ladder) | stopped:dependency | — | — | — | — | **not_run** | — | — |

### S3 — stationary probability, dt/256 at eightfold space (96,000 walkers; S2 stop rule overridden by the sponsor)

- State `completed`, stage verdict **numerical_no_result**.
- Override: predecessor S2 returned numerical_no_result (redesign session); stop rule overridden by the sponsor.  Overridden rule: verify.py _t07_campaign stop_rule: "stop at the first stage whose own predecessor returned a numerical_no_result; a later stage never runs on an unresolved one.  There is no resource cap here because there is no measured cost to cap"
- Reason: ladder gate: ('exit_count_upper', 'x=0.435512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging; ('exit_count_upper', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging
- Reason: 3 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.005166 (1.03x); exit_count_lower@x=0.435512 bound 0.006373 (1.28x); exit_count_lower@x=0.610512 bound 0.005582 (1.12x)
- Rules applied: verify.py _t07_campaign success_rule: "every probability row of this ladder must land, bias plus 2.0 standard errors, under the frozen probability allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"; gate = killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) budgeted and sampled with the contract's…
- Ladder gate **numerical_no_result**; reasons ["('exit_count_upper', 'x=0.435512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging", "('exit_count_upper', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging"].  Procedure checks {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 3880.1703943160082, "paired_bitwise": true, "survival_sign_ok": true}; oracle gap 2.297e-07 (coarsened grid [2400, 76800]), smallest finest error 8.913e-04.  Dataset digest `16547ee65cbc607f…`, budgets digest `8c9686fa6abc3c81…`.
- Oracle phase: wall 315 s (5.2 min), ru_maxrss 1536 MiB, timing {"oracle_margin_seconds": 29.24407204199815, "oracle_seconds": 285.3152109159855}.
- Construction phase: preflight 7249 s (120.8 min) (linear 3289 s (54.8 min) + quadratic 1544 s (25.7 min)); actual 3724 s (62.1 min); timing {"compare_seconds": 522.2828546660021, "dataset_seconds": 521.3550585419871, "samples_seconds": 520.5425337500055, "walk_seconds": 2160.1147560409736}; phase peaks {'compare': 332, 'dataset': 308, 'samples': 297, 'walk': 265} MiB; ru_maxrss 332 MiB; warnings 0.
- 2 SE alone vs the probability allowance 0.00499471: exit_count_lower@x=0.260512 0.0027 (fits); exit_count_lower@x=0.435512 0.0032 (fits); exit_count_lower@x=0.610512 0.0027 (fits); exit_count_upper@x=0.260512 0.0018 (fits); exit_count_upper@x=0.435512 0.0027 (fits); exit_count_upper@x=0.610512 0.0025 (fits); survival@x=0.260512 0.0017 (fits); survival@x=0.435512 0.0017 (fits); survival@x=0.610512 0.0016 (fits).

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 3.052e-05 | 0.65531 | 0.65920 | 0.00389 | 0.00151 | 0.00000 | 0.00047 |
| exit_count_lower | x=0.260512 | 1.526e-05 | 0.65618 | 0.65920 | 0.00303 | 0.00142 | 0.00027 | 0.00047 |
| exit_count_lower | x=0.260512 | 7.629e-06 | 0.65673 | 0.65920 | 0.00247 | 0.00135 | 0.00024 | 0.00047 |
| exit_count_lower | x=0.435512 | 3.052e-05 | 0.43680 | 0.44058 | 0.00377 | 0.00162 | 0.00000 | 0.00016 |
| exit_count_lower | x=0.435512 | 1.526e-05 | 0.43719 | 0.44058 | 0.00339 | 0.00161 | 0.00011 | 0.00016 |
| exit_count_lower | x=0.435512 | 7.629e-06 | 0.43739 | 0.44058 | 0.00319 | 0.00159 | 0.00009 | 0.00016 |
| exit_count_lower | x=0.610512 | 3.052e-05 | 0.24461 | 0.24761 | 0.00299 | 0.00137 | 0.00000 | 0.00011 |
| exit_count_lower | x=0.610512 | 1.526e-05 | 0.24463 | 0.24761 | 0.00298 | 0.00137 | 0.00008 | 0.00011 |
| exit_count_lower | x=0.610512 | 7.629e-06 | 0.24473 | 0.24761 | 0.00288 | 0.00135 | 0.00008 | 0.00011 |
| exit_count_upper | x=0.260512 | 3.052e-05 | 0.25831 | 0.25721 | 0.00110 | 0.00095 | 0.00000 | 0.00020 |
| exit_count_upper | x=0.260512 | 1.526e-05 | 0.25816 | 0.25721 | 0.00094 | 0.00091 | 0.00016 | 0.00020 |
| exit_count_upper | x=0.260512 | 7.629e-06 | 0.25810 | 0.25721 | 0.00089 | 0.00090 | 0.00009 | 0.00020 |
| exit_count_upper | x=0.435512 | 3.052e-05 | 0.45250 | 0.45113 | 0.00137 | 0.00121 | 0.00000 | 0.00037 |
| exit_count_upper | x=0.435512 | 1.526e-05 | 0.45279 | 0.45113 | 0.00167 | 0.00128 | 0.00023 | 0.00037 |
| exit_count_upper | x=0.435512 | 7.629e-06 | 0.45300 | 0.45113 | 0.00187 | 0.00133 | 0.00016 | 0.00037 |
| exit_count_upper | x=0.610512 | 3.052e-05 | 0.67115 | 0.67021 | 0.00094 | 0.00106 | 0.00000 | 0.00065 |
| exit_count_upper | x=0.610512 | 1.526e-05 | 0.67167 | 0.67021 | 0.00146 | 0.00116 | 0.00040 | 0.00065 |
| exit_count_upper | x=0.610512 | 7.629e-06 | 0.67204 | 0.67021 | 0.00183 | 0.00126 | 0.00027 | 0.00065 |
| exit_quantile_p35 | x=0.260512 | 3.052e-05 | 0.30289 | 0.29633 | 0.00656 | 0.00190 | 0.00000 | 0.00031 |
| exit_quantile_p35 | x=0.260512 | 1.526e-05 | 0.30136 | 0.29633 | 0.00503 | 0.00182 | 0.00022 | 0.00031 |
| exit_quantile_p35 | x=0.260512 | 7.629e-06 | 0.30042 | 0.29633 | 0.00409 | 0.00176 | 0.00021 | 0.00031 |
| exit_quantile_p35 | x=0.435512 | 3.052e-05 | 0.51464 | 0.50885 | 0.00579 | 0.00192 | 0.00000 | 0.00034 |
| exit_quantile_p35 | x=0.435512 | 1.526e-05 | 0.51357 | 0.50885 | 0.00472 | 0.00180 | 0.00028 | 0.00034 |
| exit_quantile_p35 | x=0.435512 | 7.629e-06 | 0.51281 | 0.50885 | 0.00397 | 0.00176 | 0.00017 | 0.00034 |
| exit_quantile_p35 | x=0.610512 | 3.052e-05 | 0.29208 | 0.28690 | 0.00518 | 0.00175 | 0.00000 | 0.00037 |
| exit_quantile_p35 | x=0.610512 | 1.526e-05 | 0.29086 | 0.28690 | 0.00396 | 0.00175 | 0.00022 | 0.00037 |
| exit_quantile_p35 | x=0.610512 | 7.629e-06 | 0.28998 | 0.28690 | 0.00308 | 0.00173 | 0.00025 | 0.00037 |
| survival | x=0.260512 | 3.052e-05 | 0.08637 | 0.08358 | 0.00279 | 0.00089 | 0.00000 | 0.00023 |
| survival | x=0.260512 | 1.526e-05 | 0.08567 | 0.08358 | 0.00208 | 0.00088 | 0.00013 | 0.00023 |
| survival | x=0.260512 | 7.629e-06 | 0.08517 | 0.08358 | 0.00158 | 0.00083 | 0.00015 | 0.00023 |
| survival | x=0.435512 | 3.052e-05 | 0.11070 | 0.10830 | 0.00240 | 0.00099 | 0.00000 | 0.00030 |
| survival | x=0.435512 | 1.526e-05 | 0.11002 | 0.10830 | 0.00172 | 0.00095 | 0.00015 | 0.00030 |
| survival | x=0.435512 | 7.629e-06 | 0.10961 | 0.10830 | 0.00132 | 0.00087 | 0.00020 | 0.00030 |
| survival | x=0.610512 | 3.052e-05 | 0.08424 | 0.08218 | 0.00206 | 0.00088 | 0.00000 | 0.00031 |
| survival | x=0.610512 | 1.526e-05 | 0.08371 | 0.08218 | 0.00152 | 0.00086 | 0.00013 | 0.00031 |
| survival | x=0.610512 | 7.629e-06 | 0.08323 | 0.08218 | 0.00105 | 0.00079 | 0.00022 | 0.00031 |

Stage rule rows (probability); bound = |error| + 2 SE vs allowance 0.00499471:

| Observable | Position | |error| | SE | bound | ratio | fits |
| --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 0.00247 | 0.00135 | 0.00517 | 1.03x | NO |
| exit_count_lower | x=0.435512 | 0.00319 | 0.00159 | 0.00637 | 1.28x | NO |
| exit_count_lower | x=0.610512 | 0.00288 | 0.00135 | 0.00558 | 1.12x | NO |
| exit_count_upper | x=0.260512 | 0.00089 | 0.00090 | 0.00270 | 0.54x | yes |
| exit_count_upper | x=0.435512 | 0.00187 | 0.00133 | 0.00454 | 0.91x | yes |
| exit_count_upper | x=0.610512 | 0.00183 | 0.00126 | 0.00436 | 0.87x | yes |
| survival | x=0.260512 | 0.00158 | 0.00083 | 0.00324 | 0.65x | yes |
| survival | x=0.435512 | 0.00132 | 0.00087 | 0.00306 | 0.61x | yes |
| survival | x=0.610512 | 0.00105 | 0.00079 | 0.00263 | 0.53x | yes |

### S4 — stationary time quantile, dt/256 at eightfold space (96,000 walkers; judged on S3's frozen ladder)

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S3 returned numerical_no_result

## Projected bounds (the package's own `NumericalEvidence.projected_bound`)

NumericalEvidence.projected_bound(2.0, timestep_factor, sample_factor=1): |measured| * sqrt(factor) + 2 SE

### From S2_override_96k (finest level measured at timestep 3.052e-05)

| Observable | Position | Unit | Measured bound | ratio | projected to dt/256 |
| --- | --- | --- | --- | --- | --- |
| exit_count_upper | x=0.610512 | probability | 0.00523 | 1.05x | 0.00389 (0.78x, fits) |
| exit_count_lower | x=0.435512 | probability | 0.00459 | 0.92x | 0.00356 (0.71x, fits) |
| survival | x=0.435512 | probability | 0.00457 | 0.91x | 0.00328 (0.66x, fits) |
| exit_count_lower | x=0.260512 | probability | 0.00422 | 0.85x | 0.00341 (0.68x, fits) |
| survival | x=0.610512 | probability | 0.00409 | 0.82x | 0.00291 (0.58x, fits) |
| survival | x=0.260512 | probability | 0.00288 | 0.58x | 0.00222 (0.44x, fits) |
| exit_count_upper | x=0.435512 | probability | 0.00246 | 0.49x | 0.00220 (0.44x, fits) |
| exit_quantile_p35 | x=0.610512 | time | 0.00981 | 0.45x | 0.00662 (0.30x, fits) |
| exit_quantile_p35 | x=0.435512 | time | 0.00901 | 0.41x | 0.00657 (0.30x, fits) |
| exit_count_lower | x=0.610512 | probability | 0.00202 | 0.40x | 0.00186 (0.37x, fits) |
| exit_count_upper | x=0.260512 | probability | 0.00195 | 0.39x | 0.00181 (0.36x, fits) |
| exit_quantile_p35 | x=0.260512 | time | 0.00717 | 0.33x | 0.00534 (0.24x, fits) |

### From S3 (finest level measured at timestep 7.629e-06)

| Observable | Position | Unit | Measured bound | ratio |  |
| --- | --- | --- | --- | --- |
| exit_count_lower | x=0.435512 | probability | 0.00637 | 1.28x |  |
| exit_count_lower | x=0.610512 | probability | 0.00558 | 1.12x |  |
| exit_count_lower | x=0.260512 | probability | 0.00517 | 1.03x |  |
| exit_count_upper | x=0.435512 | probability | 0.00454 | 0.91x |  |
| exit_count_upper | x=0.610512 | probability | 0.00436 | 0.87x |  |
| survival | x=0.260512 | probability | 0.00324 | 0.65x |  |
| survival | x=0.435512 | probability | 0.00306 | 0.61x |  |
| exit_count_upper | x=0.260512 | probability | 0.00270 | 0.54x |  |
| survival | x=0.610512 | probability | 0.00263 | 0.53x |  |
| exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.35x |  |
| exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.34x |  |
| exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.30x |  |

## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)

experiments.numerical_disposition: bound = |measured| + coverage_sigma * SE compared with budget.allowance(unit) (probability: 0.25 * planned 95% half-width at 2406 trials = 0.004995; time: 0.25 * 0.08 + one intended timestep = 0.021953); blockers: a numerical_no_result row is carried through; bound > allowance; not measured at the intended configuration; probability window empty below 2406 trials; any time row failing fails at every trial count.  README: "A measured discrepancy, inflated by the budget's own frozen coverage sigma, must sit under one quarter of the planned production 95 % half-width, with one intended timestep added for a commit-time quantile."

Superseding stationary stage: **S3** (replaces S2's rows per the dependency chain).

### Evidence set `new_stationary_only` (12 rows; configurations ['intended'])

- Verdict **numerical_no_result**; blockers ['endpoint_envelope_exceeds_allowance', 'probability_window_empty']; probability-admissible trials 1477 (needs 2406); time admissible True; overall admissible 1477.
- Limiting rows: {"probability": ["stationary_oracle", "exit_count_lower", "x=0.435512", "probability", 0.006373475313676062, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00637 | 0.00499 | 1.28x | NO |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00558 | 0.00499 | 1.12x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00517 | 0.00499 | 1.03x | NO |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00454 | 0.00499 | 0.91x | yes |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00436 | 0.00499 | 0.87x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00270 | 0.00499 | 0.54x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |

### Evidence set `intended_all_kept_M5_M6` (22 rows; configurations ['intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 439 (needs 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["moving_band_audit", "survival_shift_at_0.80", "pooled", "probability", 0.011686381511775135, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.08360834184430277, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.08361 | 0.02195 | 3.81x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.06070 | 0.02195 | 2.77x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00637 | 0.00499 | 1.28x | NO |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00558 | 0.00499 | 1.12x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00517 | 0.00499 | 1.03x | NO |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00454 | 0.00499 | 0.91x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00436 | 0.00499 | 0.87x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00270 | 0.00499 | 0.54x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### Evidence set `reference_plus_intended_all` (39 rows; configurations ['intended', 'non_intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (needs 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.17700055614529983, 0.021953125, false]}

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
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.08361 | 0.02195 | 3.81x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.06070 | 0.02195 | 2.77x | NO |
| stationary_oracle | exit_count_lower | x=0.584397 | probability | 0.01245 | 0.00499 | 2.49x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| stationary_oracle | exit_count_upper | x=0.184397 | probability | 0.01086 | 0.00499 | 2.17x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00637 | 0.00499 | 1.28x | NO |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00558 | 0.00499 | 1.12x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00517 | 0.00499 | 1.03x | NO |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00454 | 0.00499 | 0.91x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00436 | 0.00499 | 0.87x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00270 | 0.00499 | 0.54x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

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
10. **16x walkers and the frozen contract.** The sampling design's cluster count is part of the hashed contract and is set from the data (96,000 walkers -> 96,000 clusters), exactly as verify.py sets it from _S3_WALKERS; the frozen S3 caps and their resolution floors (0.012 probability, 0.030 time) are applied unchanged although they were derived for 6,000 walkers' granularity (a floor can only excuse a reversal, so at 96,000 walkers it is looser, never stricter).  Seeds, resamples (200), coverage (2), estimators and observables are unchanged.
11. **memory-scaling measurement.** The walker-dependent memory is the construction phase's process peak (walk + censoring + frozen dataset + compare_refinement), measured in its own child at 24,000 walkers and combined with the pricing session's 6,000-walker construction children (ru_maxrss 220-228 MiB, same code path without the comparison) for a two-point linear extrapolation; the oracle phase runs in a separate child whose peak is the solve's own (up to 1,589 MiB at eightfold space, measured in the pricing session) and never overlaps the construction.
12. **O(walkers^2) identity check.** killed_diffusion._require_names runs `listed.count(e)` for every label (about 4.4 ns x n^2) and is executed 36 times per stationary stage (12 samples x construction, ValidationDataset rebuild, compare_refinement rebuild).  Its time is measured in the 24,000-walker probe as the dataset-construction and comparison seconds and extrapolated quadratically to the chosen walker count for the preflight; nothing inside the package is changed or bypassed.
13. **M6 override.** M6 runs although its predecessor M5 returned numerical_no_result, by the sponsor's plan change; the frozen rule text is quoted and the override is stated.  M6 keeps its frozen design (40 master trials, 3 regime clocks, 4 replicates, strides (4,2,1) on the 2^-13 mesh over the 2048/2^-9 = 32768-step window).  The gate's added_resets_mean cap (3.0, frozen for the S3b cell) is reported as its own line beside the probability and time rows; it is not re-frozen.
14. **execution order.** M6 (priced 23 min) runs before the stationary path so that the sponsor's explicitly requested override stage cannot be skipped by the 4-hour preflight in the branch where S1 and S2 both succeed (S3 alone is priced at about two hours at 96,000 walkers); the stationary path keeps its own dependency order S1 -> S2 -> S3 -> S4.
15. **disposition sets.** Rows from this session replace last night's S1 rows (superseded by the 16x-walker S1) and add M6's rows; last night's M5 rows are kept (M6 does not supersede M5).  Three sets are run: redesign-only intended rows, all intended rows (S1-new [+S2,S3 if run] + M5-old + M6), and the 17 reference rows plus all intended rows.
16. **second override.** S2 runs although its predecessor S1 (96,000 walkers, redesign session) returned numerical_no_result, by the second sponsor's override; the frozen stop rule is quoted and the override stated.  S3 and S4 keep the frozen dependency rule with no further override.
17. **walker count.** 96,000 walkers, the count chosen by the redesign session's memory-scaling measurement (construction-phase peak 273 MiB measured there); no new probe.  The O(walkers^2) identity-check seconds measured at 96,000 walkers in that session (1545 s per stationary stage) enter the preflight directly.
18. **oracle margin grids.** S2: refined grid 4800 x 76800 (1,589 MiB in the pricing session, under the 2 GiB cap, in its own oracle child).  S3/S4: the refined grid 9600 x 307200 would exceed the cap, so the COARSER grid 2400 x 76800 is differenced, which overstates the oracle's own error by about 3x for a second-order scheme (the conservative direction).
19. **projected bounds.** For every S2 row the package's own NumericalEvidence.projected_bound(coverage_sigma=2, timestep_factor, sample_factor=1) is reported at dt/128 (factor 0.5) and dt/256 (factor 0.25): bias x sqrt(factor) + 2 SE.  These are planning projections by the package's stated rule (bias falls like sqrt(dt)), not evidence; they are also computed from the redesign S1 rows to dt/64 beside the measured S2 rows, so the rule's accuracy on this cell is visible.
20. **disposition sets.** Per the dependency chain the finest completed stationary stage supersedes its predecessors (S2 replaces S1; S3 would replace S2); M5's rows (first session) and M6's rows (redesign session) are kept.  Sets: new stationary rows only; all intended rows (new stationary + M5 + M6); the 17 reference rows plus all intended rows.
21. **third override.** S3 runs although its predecessor S2 (96,000 walkers, S2-override session) returned numerical_no_result on one row (exit_count_upper@x=0.610512, 1.05x), by the third sponsor's override; the frozen stop rule is quoted and the override stated.  S4 keeps the frozen dependency rule with no further override and judges the time rows of S3's frozen ladder (the same keyed, digest-verified data) rather than recomputing it.
22. **eightfold-space oracle margin.** The S3 oracle grid is 4800 x 153600 (about 1.6 GiB in its own child).  The refined margin grid 9600 x 307200 would exceed the 2 GiB cap, so the coarser grid 2400 x 76800 is differenced against the oracle; for a second-order scheme that gap is about three times the oracle's own error, so the margin ratio reported understates the true margin (conservative).
23. **disposition fallback.** If S3 completes, its rows supersede S2's; if S3 does not complete, S2's rows (from observations_s2.json) remain the superseding stationary rows.  M5 (first session) and M6 (redesign session) rows are kept.  S4's rows are S3's time rows, already present in S3's ladder.

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_s3_campaign.py --run
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_s3_campaign.py --derive-only
```

## Session log

```
[    0.0s] S2 override session start
[    0.4s] S3: preflight 7249s (linear 3289s + quadratic 1544s, x1.5); elapsed 0s; remaining 10800s; work {"endpoint_observations": 132120576000, "oracle_cells": 921600000, "resample_observations": 691200000}
[  315.1s]     |     oracle 4800x153600 in 285.3s; margin coarsened [2400, 76800] gap 2.297e-07
[  315.1s] S3 phase A: completed wall 315s rss 1536MiB
[ 4039.6s]     |     walk 96000x524288 in 2160.1s paired=True rss 265MiB
[ 4039.6s]     |     samples 520.5s, dataset 521.4s rss 308MiB
[ 4039.6s]     |     gate numerical_no_result in 522.3s rss 332MiB; checks {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 3880.1703943160082, "paired_bitwise": true, "survival_sign_ok": true}
[ 4039.6s] S3: completed verdict=numerical_no_result wall=3724s rss=332MiB reasons=["ladder gate: ('exit_count_upper', 'x=0.435512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging; ('exit_count_upper', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging", '3 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.005166 (1.03x); exit_count_lower@x=0.435512 bound 0.006373 (1.28x); exit_count_lower@x=0.610512 bound 0.005582 (1.12x)']
[ 4039.6s] S4: stopped — predecessor S3 = numerical_no_result
[ 4039.9s] session end: wall 4040s; results/ unchanged=True package unchanged=True
```
