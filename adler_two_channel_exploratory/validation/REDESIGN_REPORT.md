# Redesigned intended-configuration validation campaign — report

**Nothing here is a physical finding, an approval, or a sufficiency promise.**  The sponsor's plan change authorized 16x walkers on the stationary path and running M6 despite M5's `numerical_no_result`; every other rule stays frozen.  The frozen added-resets cap is reported as found and is not re-frozen.  M5 was not re-run; M7 was not launched.

Session 2026-09-03T07:12:13-0600 → 2026-09-03T08:09:19-0600, wall 2684 s (44.7 min) of the 14400 s budget; per-process RSS ceiling 2 GiB; previous record `adler_two_channel_exploratory/validation/observations.json` (sha256 `0e2b2b9769dfcb79…`) untouched.

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
| repo git HEAD | `f8208e0fd9a572a591f0a45d3108bfc73373c9a6` |
| frozen ticket-07 budget digest | `8ff45c2c33c01192129320db814f367845c4cf29cf05cbb7372af8aa0886da61` (allowances {'count': 0.004994710172401896, 'probability': 0.004994710172401896, 'time': 0.021953125}) |
| pricing derivation used for preflight | `7c8c0f81d1f69f12f5043a352d2571f2b5f97a922b05634a4729d0f3f0062018` |

## Tree integrity

- `results/` (1176 entries) unchanged by SHA-256 = **True**; package tree (incl. `__pycache__`) unchanged = **True**.
- Strictly serial child processes (oracle phase and construction phase separately for each stationary stage); the parent polled RSS every 50 ms with a 2 GiB kill.  No verifier, pilot, production, sensitivity or fit.

### Events

- S2: stopped by dependency on S1 (numerical_no_result)
- S3: stopped by dependency on S2 (None)
- S4: stopped by dependency on S3 (None)

## Memory-scaling measurement and walker decision

- S1 construction phase at **24000 walkers** (32768 fine steps): child ru_maxrss **205 MiB** (parent-observed 205 MiB); phase peaks {'compare': 205, 'dataset': 203, 'samples': 203, 'walk': 202} MiB; timing {"compare_seconds": 31.766147417016327, "dataset_seconds": 30.908981125016, "samples_seconds": 30.877248792006867, "walk_seconds": 28.217432541016024}; quadratic (identity-check-dominated) seconds 93.6; gate numerical_no_result; wall 122 s (2.0 min).
- Probe rule rows (probability, |error| + 2 SE vs allowance): exit_count_lower@x=0.260512 0.0154 (3.1x); exit_count_lower@x=0.435512 0.0135 (2.7x); exit_count_lower@x=0.610512 0.0067 (1.3x); exit_count_upper@x=0.260512 0.0103 (2.1x); exit_count_upper@x=0.435512 0.0037 (0.7x); exit_count_upper@x=0.610512 0.0082 (1.6x); survival@x=0.260512 0.0078 (1.6x); survival@x=0.435512 0.0113 (2.3x); survival@x=0.610512 0.0092 (1.8x).
- Linear model: 6,000-walker construction peak 228 MiB (pricing session), 24000-walker peak 205 MiB → slope 0.0 B/walker.

| Candidate walkers | Extrapolated peak RSS | Under 2 GiB | Preflight (linear + quadratic, x1.5) | Fits budget |
| --- | --- | --- | --- | --- |
| 96000 | 205 MiB | True | 2605 s (43.4 min) (linear 239 s (4.0 min), quadratic 1497 s (24.9 min)) | True |
| 72000 | 205 MiB | True | 1543 s (25.7 min) (linear 187 s (3.1 min), quadratic 842 s (14.0 min)) | True |
| 48000 | 205 MiB | True | 762 s (12.7 min) (linear 134 s (2.2 min), quadratic 374 s (6.2 min)) | True |
| 24000 | 205 MiB | True | 261 s (4.4 min) (linear 80.7 s, quadratic 93.6 s) | True |

**Chosen walker count: 96000**.

## Stages

| Stage | State | Configuration | Ladder gate | Procedure checks | Rule rows (unit) | Stage verdict | Wall | Peak RSS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **M6** moving-band probability, dt/16 replay (stop rule after M5 overridden by the sponsor) | completed | 40 trials x 3 clocks x 4 replicates, mesh step 0.000122, 32768 steps, timesteps ['0.000488', '0.000244', '0.000122'] | numerical_no_result | ok {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true} | 4/4 fit (probability) | **numerical_no_result** | 895 s (14.9 min) | 79 MiB (construction 79 MiB) |
| **S1** stationary probability, dt/16 at doubled space (16x walkers) | completed | oracle [1200, 9600], fine steps 32768, timesteps ['0.000488', '0.000244', '0.000122'], walkers 96000 | pass | ok {"gate_pass": true, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 335.4821694829457, "paired_bitwise": true, "survival_sign_ok": true} | 3/9 fit (probability) | **numerical_no_result** | 1666 s (27.8 min) | 509 MiB (construction 273 MiB) |
| **S2** stationary probability, dt/64 at quadrupled space (16x walkers) | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **S3** stationary probability, dt/256 at eightfold space (16x walkers) | stopped:dependency | — | — | — | — | **not_run** | — | — |
| **S4** stationary time quantile, dt/256 at eightfold space (16x walkers) | stopped:dependency | — | — | — | — | **not_run** | — | — |

### M6 — moving-band probability, dt/16 replay (stop rule after M5 overridden by the sponsor)

- State `completed`, stage verdict **numerical_no_result**.
- Reason: ladder gate: ('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3; ('commit_time_quantile_p20_shift', 'pooled'): [not_converging] 0.00546875 at 0.000488281 against 0.0283203 at 0.00012207, past the single whole-ladder allowance 0.0221183
- Frozen stop rule overridden by the sponsor: verify.py _t07_campaign stop_rule: "stop at the first stage whose own predecessor returned a numerical_no_result; a later stage never runs on an unresolved one.  There is no resource cap here because there is no measured cost to cap"
- Rules applied: verify.py _t07_campaign success_rule: "every probability row of this ladder must land, bias plus 2.0 standard errors, under the frozen probability allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"; gate = killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) budgeted and sampled with the contract's…
- Ladder gate **numerical_no_result**; reasons ["('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3", "('commit_time_quantile_p20_shift', 'pooled'): [not_converging] 0.00546875 at 0.000488281 against 0.0283203 at 0.00012207, past the single whole-ladder allowance 0.0221183"].  Procedure checks {"both_edges_every_clock": true, "gate_pass": false, "subset_holds": true}.  Dataset digest `7b9cd275bc996808…`, budgets digest `55a0cad7051d10f5…`.
- Work {"audited_evaluations": 14915840, "physical_intervals": 6882000, "resample_observations": 144000}; preflight 1404 s (23.4 min); actual 895 s (14.9 min); timing {"compare_seconds": 0.037794250005390495, "dataset_seconds": 0.0011182090092916042, "ladder_seconds": 894.7651132080064}; ru_maxrss 79 MiB; warnings 0.
- **Frozen added-resets cap (reported separately, not re-frozen):** cap [3.0, 30.0, 0.0]; finest level 14.0938 ± 2.5430 (2-sigma bound 19.1797); gate verdict with the cap **numerical_no_result**; the gate's other clauses also fail; gate reasons naming it: ["('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3"].

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean | pooled | 0.0004883 | 7.06250 | 0.00000 | 7.06250 | 1.35259 | 0.00000 | 1.24021 |
| added_resets_mean | pooled | 0.0002441 | 9.84167 | 0.00000 | 9.84167 | 1.88333 | 0.57803 | 1.24021 |
| added_resets_mean | pooled | 0.0001221 | 14.09375 | 0.00000 | 14.09375 | 2.54299 | 0.70965 | 1.24021 |
| commit_probability_shift | pooled | 0.0004883 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| commit_probability_shift | pooled | 0.0002441 | -0.00208 | 0.00000 | 0.00208 | 0.00209 | 0.00209 | 0.00000 |
| commit_probability_shift | pooled | 0.0001221 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00209 | 0.00000 |
| commit_time_quantile_p20_shift | pooled | 0.0004883 | 0.00547 | 0.00000 | 0.00547 | 0.01232 | 0.00000 | 0.01081 |
| commit_time_quantile_p20_shift | pooled | 0.0002441 | 0.04453 | 0.00000 | 0.04453 | 0.02836 | 0.02718 | 0.01081 |
| commit_time_quantile_p20_shift | pooled | 0.0001221 | 0.02832 | 0.00000 | 0.02832 | 0.01619 | 0.02667 | 0.01081 |
| survival_shift_at_0.45 | pooled | 0.0004883 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| survival_shift_at_0.45 | pooled | 0.0002441 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| survival_shift_at_0.45 | pooled | 0.0001221 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| survival_shift_at_0.60 | pooled | 0.0004883 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| survival_shift_at_0.60 | pooled | 0.0002441 | 0.00208 | 0.00000 | 0.00208 | 0.00209 | 0.00209 | 0.00000 |
| survival_shift_at_0.60 | pooled | 0.0001221 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00209 | 0.00000 |
| survival_shift_at_0.80 | pooled | 0.0004883 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00000 |
| survival_shift_at_0.80 | pooled | 0.0002441 | 0.00208 | 0.00000 | 0.00208 | 0.00209 | 0.00209 | 0.00000 |
| survival_shift_at_0.80 | pooled | 0.0001221 | 0.00000 | 0.00000 | 0.00000 | 0.00000 | 0.00209 | 0.00000 |

Stage rule rows (probability); bound = |error| + 2 SE vs allowance 0.00499471:

| Observable | Position | |error| | SE | bound | ratio | fits |
| --- | --- | --- | --- | --- | --- | --- |
| commit_probability_shift | pooled | 0.00000 | 0.00000 | 0.00000 | 0.00x | yes |
| survival_shift_at_0.45 | pooled | 0.00000 | 0.00000 | 0.00000 | 0.00x | yes |
| survival_shift_at_0.60 | pooled | 0.00000 | 0.00000 | 0.00000 | 0.00x | yes |
| survival_shift_at_0.80 | pooled | 0.00000 | 0.00000 | 0.00000 | 0.00x | yes |

Time rows (informational for M6); bound = |error| + 2 SE vs allowance 0.0219531:

| Observable | Position | |error| | SE | bound | ratio | fits |
| --- | --- | --- | --- | --- | --- | --- |
| commit_time_quantile_p20_shift | pooled | 0.02832 | 0.01619 | 0.06070 | 2.77x | NO |

### S1 — stationary probability, dt/16 at doubled space (16x walkers)

- State `completed`, stage verdict **numerical_no_result**.
- Reason: 6 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.008532 (1.7x); exit_count_lower@x=0.435512 bound 0.007393 (1.5x); exit_count_upper@x=0.610512 bound 0.006986 (1.4x); survival@x=0.260512 bound 0.005246 (1.1x); survival@x=0.435512 bound 0.007188 (1.4x); survival@x=0.610512 bound 0.006946 (1.4x)
- Rules applied: verify.py _t07_campaign success_rule: "every probability row of this ladder must land, bias plus 2.0 standard errors, under the frozen probability allowance 0.00499471 at the trial count the matrix proposes"; verify.py _t07_campaign no_result_rule: "a stage that misses its target is a numerical_no_result: the budget is not widened, the allowance is not re-derived, and the moving-band verdict is not re-decided"; gate = killed_diffusion.compare_refinement: every (observable, position) identity is judged on its own, and all must pass: (1) budgeted and sampled with the contract's…
- Ladder gate **pass**.  Procedure checks {"gate_pass": true, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 335.4821694829457, "paired_bitwise": true, "survival_sign_ok": true}; oracle gap 2.955e-06 (refined grid [2400, 19200]), smallest finest error 9.913e-04.  Dataset digest `bef7f3f261553cc8…`, budgets digest `55b1da3eb2a98522…`.
- Oracle phase: wall 9.3 s, ru_maxrss 509 MiB, timing {"oracle_margin_seconds": 8.486344584001927, "oracle_seconds": 0.6465884589997586}.
- Construction phase: preflight 2605 s (43.4 min) (linear 239 s (4.0 min) + quadratic 1497 s (24.9 min)); actual 1657 s (27.6 min); timing {"compare_seconds": 516.5328752910136, "dataset_seconds": 513.7614200829994, "samples_seconds": 514.1357627499965, "walk_seconds": 112.08784866699716}; phase peaks {'compare': 273, 'dataset': 268, 'samples': 246, 'walk': 205} MiB; ru_maxrss 273 MiB; warnings 0.
- 2 SE alone at the chosen walker count vs the probability allowance 0.00499471: exit_count_lower@x=0.260512 0.0031 (fits); exit_count_lower@x=0.435512 0.0032 (fits); exit_count_lower@x=0.610512 0.0022 (fits); exit_count_upper@x=0.260512 0.0025 (fits); exit_count_upper@x=0.435512 0.0022 (fits); exit_count_upper@x=0.610512 0.0031 (fits); survival@x=0.260512 0.0017 (fits); survival@x=0.435512 0.0020 (fits); survival@x=0.610512 0.0019 (fits).

| Observable | Position | Timestep | Measured | Reference | |error| | SE | paired SE | span SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 0.0004883 | 0.64870 | 0.65920 | 0.01051 | 0.00151 | 0.00000 | 0.00030 |
| exit_count_lower | x=0.260512 | 0.0002441 | 0.65167 | 0.65920 | 0.00754 | 0.00152 | 0.00024 | 0.00030 |
| exit_count_lower | x=0.260512 | 0.0001221 | 0.65373 | 0.65920 | 0.00547 | 0.00153 | 0.00018 | 0.00030 |
| exit_count_lower | x=0.435512 | 0.0004883 | 0.43362 | 0.44058 | 0.00695 | 0.00158 | 0.00000 | 0.00024 |
| exit_count_lower | x=0.435512 | 0.0002441 | 0.43517 | 0.44058 | 0.00541 | 0.00158 | 0.00018 | 0.00024 |
| exit_count_lower | x=0.435512 | 0.0001221 | 0.43635 | 0.44058 | 0.00422 | 0.00159 | 0.00015 | 0.00024 |
| exit_count_lower | x=0.610512 | 0.0004883 | 0.24657 | 0.24761 | 0.00104 | 0.00110 | 0.00000 | 0.00020 |
| exit_count_lower | x=0.610512 | 0.0002441 | 0.24650 | 0.24761 | 0.00111 | 0.00111 | 0.00015 | 0.00020 |
| exit_count_lower | x=0.610512 | 0.0001221 | 0.24650 | 0.24761 | 0.00111 | 0.00110 | 0.00015 | 0.00020 |
| exit_count_upper | x=0.260512 | 0.0004883 | 0.25919 | 0.25721 | 0.00197 | 0.00125 | 0.00000 | 0.00024 |
| exit_count_upper | x=0.260512 | 0.0002441 | 0.25922 | 0.25721 | 0.00201 | 0.00125 | 0.00018 | 0.00024 |
| exit_count_upper | x=0.260512 | 0.0001221 | 0.25918 | 0.25721 | 0.00196 | 0.00125 | 0.00016 | 0.00024 |
| exit_count_upper | x=0.435512 | 0.0004883 | 0.44788 | 0.45113 | 0.00325 | 0.00160 | 0.00000 | 0.00135 |
| exit_count_upper | x=0.435512 | 0.0002441 | 0.44916 | 0.45113 | 0.00197 | 0.00132 | 0.00068 | 0.00135 |
| exit_count_upper | x=0.435512 | 0.0001221 | 0.45014 | 0.45113 | 0.00099 | 0.00108 | 0.00080 | 0.00135 |
| exit_count_upper | x=0.610512 | 0.0004883 | 0.66210 | 0.67021 | 0.00810 | 0.00155 | 0.00000 | 0.00025 |
| exit_count_upper | x=0.610512 | 0.0002441 | 0.66464 | 0.67021 | 0.00557 | 0.00154 | 0.00018 | 0.00025 |
| exit_count_upper | x=0.610512 | 0.0001221 | 0.66631 | 0.67021 | 0.00390 | 0.00155 | 0.00017 | 0.00025 |
| exit_quantile_p35 | x=0.260512 | 0.0004883 | 0.31982 | 0.29633 | 0.02349 | 0.00204 | 0.00000 | 0.00060 |
| exit_quantile_p35 | x=0.260512 | 0.0002441 | 0.31445 | 0.29633 | 0.01812 | 0.00202 | 0.00047 | 0.00060 |
| exit_quantile_p35 | x=0.260512 | 0.0001221 | 0.30994 | 0.29633 | 0.01361 | 0.00204 | 0.00039 | 0.00060 |
| exit_quantile_p35 | x=0.435512 | 0.0004883 | 0.53010 | 0.50885 | 0.02126 | 0.00214 | 0.00000 | 0.00054 |
| exit_quantile_p35 | x=0.435512 | 0.0002441 | 0.52441 | 0.50885 | 0.01557 | 0.00207 | 0.00042 | 0.00054 |
| exit_quantile_p35 | x=0.435512 | 0.0001221 | 0.52100 | 0.50885 | 0.01215 | 0.00197 | 0.00033 | 0.00054 |
| exit_quantile_p35 | x=0.610512 | 0.0004883 | 0.30322 | 0.28690 | 0.01632 | 0.00170 | 0.00000 | 0.00045 |
| exit_quantile_p35 | x=0.610512 | 0.0002441 | 0.29810 | 0.28690 | 0.01119 | 0.00167 | 0.00037 | 0.00045 |
| exit_quantile_p35 | x=0.610512 | 0.0001221 | 0.29468 | 0.28690 | 0.00778 | 0.00169 | 0.00031 | 0.00045 |
| survival | x=0.260512 | 0.0004883 | 0.09211 | 0.08358 | 0.00853 | 0.00090 | 0.00000 | 0.00024 |
| survival | x=0.260512 | 0.0002441 | 0.08911 | 0.08358 | 0.00553 | 0.00089 | 0.00019 | 0.00024 |
| survival | x=0.260512 | 0.0001221 | 0.08709 | 0.08358 | 0.00351 | 0.00087 | 0.00015 | 0.00024 |
| survival | x=0.435512 | 0.0004883 | 0.11850 | 0.10830 | 0.01020 | 0.00098 | 0.00000 | 0.00021 |
| survival | x=0.435512 | 0.0002441 | 0.11568 | 0.10830 | 0.00738 | 0.00099 | 0.00017 | 0.00021 |
| survival | x=0.435512 | 0.0001221 | 0.11351 | 0.10830 | 0.00521 | 0.00099 | 0.00015 | 0.00021 |
| survival | x=0.610512 | 0.0004883 | 0.09132 | 0.08218 | 0.00914 | 0.00099 | 0.00000 | 0.00023 |
| survival | x=0.610512 | 0.0002441 | 0.08886 | 0.08218 | 0.00668 | 0.00098 | 0.00017 | 0.00023 |
| survival | x=0.610512 | 0.0001221 | 0.08719 | 0.08218 | 0.00500 | 0.00097 | 0.00013 | 0.00023 |

Stage rule rows (probability); bound = |error| + 2 SE vs allowance 0.00499471:

| Observable | Position | |error| | SE | bound | ratio | fits |
| --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower | x=0.260512 | 0.00547 | 0.00153 | 0.00853 | 1.71x | NO |
| exit_count_lower | x=0.435512 | 0.00422 | 0.00159 | 0.00739 | 1.48x | NO |
| exit_count_lower | x=0.610512 | 0.00111 | 0.00110 | 0.00330 | 0.66x | yes |
| exit_count_upper | x=0.260512 | 0.00196 | 0.00125 | 0.00446 | 0.89x | yes |
| exit_count_upper | x=0.435512 | 0.00099 | 0.00108 | 0.00315 | 0.63x | yes |
| exit_count_upper | x=0.610512 | 0.00390 | 0.00155 | 0.00699 | 1.40x | NO |
| survival | x=0.260512 | 0.00351 | 0.00087 | 0.00525 | 1.05x | NO |
| survival | x=0.435512 | 0.00521 | 0.00099 | 0.00719 | 1.44x | NO |
| survival | x=0.610512 | 0.00500 | 0.00097 | 0.00695 | 1.39x | NO |

### S2 — stationary probability, dt/64 at quadrupled space (16x walkers)

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S1 returned numerical_no_result

### S3 — stationary probability, dt/256 at eightfold space (16x walkers)

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S2 returned nothing

### S4 — stationary time quantile, dt/256 at eightfold space (16x walkers)

- State `stopped:dependency`, stage verdict **not_run**.
- Reason: stop rule: predecessor S3 returned nothing

## Ticket-07 numerical disposition (experiments.numerical_disposition, frozen budget)

experiments.numerical_disposition: bound = |measured| + coverage_sigma * SE compared with budget.allowance(unit) (probability: 0.25 * planned 95% half-width at 2406 trials = 0.004995; time: 0.25 * 0.08 + one intended timestep = 0.021953); blockers: a numerical_no_result row is carried through; bound > allowance; not measured at the intended configuration; probability window empty below 2406 trials; any time row failing fails at every trial count.  README: "A measured discrepancy, inflated by the budget's own frozen coverage sigma, must sit under one quarter of the planned production 95 % half-width, with one intended timestep added for a commit-time quantile."

### Evidence set `redesign_intended_only` (17 rows; configurations ['intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 824 (needs 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["stationary_oracle", "exit_count_lower", "x=0.260512", "probability", 0.008531803011296456, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.06070388887758073, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.06070 | 0.02195 | 2.77x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00739 | 0.00499 | 1.48x | NO |
| stationary_oracle | survival | x=0.435512 | probability | 0.00719 | 0.00499 | 1.44x | NO |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00699 | 0.00499 | 1.40x | NO |
| stationary_oracle | survival | x=0.610512 | probability | 0.00695 | 0.00499 | 1.39x | NO |
| stationary_oracle | survival | x=0.260512 | probability | 0.00525 | 0.00499 | 1.05x | NO |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00446 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.01768 | 0.02195 | 0.81x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.01609 | 0.02195 | 0.73x | yes |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00330 | 0.00499 | 0.66x | yes |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00315 | 0.00499 | 0.63x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.01115 | 0.02195 | 0.51x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### Evidence set `intended_all_kept_M5` (22 rows; configurations ['intended'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 439 (needs 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["moving_band_audit", "survival_shift_at_0.80", "pooled", "probability", 0.011686381511775135, 0.004994710172401896, false], "time": ["moving_band_audit", "commit_time_quantile_p20_shift", "pooled", "time", 0.08360834184430277, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.08361 | 0.02195 | 3.81x | NO |
| moving_band_audit | commit_time_quantile_p20_shift | pooled | time | 0.06070 | 0.02195 | 2.77x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00739 | 0.00499 | 1.48x | NO |
| stationary_oracle | survival | x=0.435512 | probability | 0.00719 | 0.00499 | 1.44x | NO |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00699 | 0.00499 | 1.40x | NO |
| stationary_oracle | survival | x=0.610512 | probability | 0.00695 | 0.00499 | 1.39x | NO |
| stationary_oracle | survival | x=0.260512 | probability | 0.00525 | 0.00499 | 1.05x | NO |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00446 | 0.00499 | 0.89x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.01768 | 0.02195 | 0.81x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.01609 | 0.02195 | 0.73x | yes |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00330 | 0.00499 | 0.66x | yes |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00315 | 0.00499 | 0.63x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.01115 | 0.02195 | 0.51x | yes |
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
| stationary_oracle | exit_count_lower | x=0.260512 | probability | 0.00853 | 0.00499 | 1.71x | NO |
| stationary_oracle | exit_count_lower | x=0.435512 | probability | 0.00739 | 0.00499 | 1.48x | NO |
| stationary_oracle | survival | x=0.435512 | probability | 0.00719 | 0.00499 | 1.44x | NO |
| stationary_oracle | exit_count_upper | x=0.610512 | probability | 0.00699 | 0.00499 | 1.40x | NO |
| stationary_oracle | survival | x=0.610512 | probability | 0.00695 | 0.00499 | 1.39x | NO |
| stationary_oracle | survival | x=0.260512 | probability | 0.00525 | 0.00499 | 1.05x | NO |
| stationary_oracle | exit_count_upper | x=0.260512 | probability | 0.00446 | 0.00499 | 0.89x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.01768 | 0.02195 | 0.81x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.01609 | 0.02195 | 0.73x | yes |
| stationary_oracle | exit_count_lower | x=0.610512 | probability | 0.00330 | 0.00499 | 0.66x | yes |
| stationary_oracle | exit_count_upper | x=0.435512 | probability | 0.00315 | 0.00499 | 0.63x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.01115 | 0.02195 | 0.51x | yes |
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

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_redesign_campaign.py --run
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/run_redesign_campaign.py --derive-only
```

## Session log

```
[    0.0s] redesigned validation campaign session start
[    0.6s] M6: preflight 1404s; elapsed 0s; remaining 14400s; work {"audited_evaluations": 14915840, "physical_intervals": 6882000, "resample_observations": 144000}
[  895.9s]     |     ladder 40 trials x 3 clocks x 3 strides in 895s; subset=True
[  895.9s]     |     gate numerical_no_result; checks {'subset_holds': True, 'both_edges_every_clock': True, 'gate_pass': False}
[  895.9s] M6: completed verdict=numerical_no_result wall=895s rss=79MiB reasons=["ladder gate: ('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3; ('commit_time_quantile_p20_shift', 'pooled'): [not_converging] 0.00546875 at 0.000488281 against 0.0283203 at 0.00012207, past the single whole-ladder allowance 0.0221183"]
[  895.9s] S1 phase A (oracle): preflight 42s; elapsed 896s
[  905.2s]     |     oracle 1200x9600 in 0.6s; margin refined [2400, 19200] gap 2.955e-06
[  905.2s] S1 phase A: completed wall 9s rss 509MiB
[  905.2s] memory probe: S1 construction at 24000 walkers; preflight (linear terms only) 121s; elapsed 905s
[ 1027.1s]     |     walk 24000x32768 in 28.2s paired=True rss 202MiB
[ 1027.1s]     |     samples 30.9s, dataset 30.9s rss 203MiB
[ 1027.1s]     |     gate numerical_no_result in 31.8s rss 205MiB; checks {"gate_pass": false, "nonzero_se_ok": true, "oracle_margin_ok": false, "oracle_margin_ratio": 0.5682312603758349, "paired_bitwise": true, "survival_sign_ok": true}
[ 1027.1s] memory probe: ru_maxrss 205MiB, phase peaks {'compare': 205, 'dataset': 203, 'samples': 203, 'walk': 202} MiB, quadratic seconds 93.6, wall 122s
[ 1027.1s]     candidate 96000: extrapolated peak 205MiB (ok), preflight 2605s (ok)
[ 1027.1s]     candidate 72000: extrapolated peak 205MiB (ok), preflight 1543s (ok)
[ 1027.1s]     candidate 48000: extrapolated peak 205MiB (ok), preflight 762s (ok)
[ 1027.1s]     candidate 24000: extrapolated peak 205MiB (ok), preflight 261s (ok)
[ 1027.1s] walker decision: 96000
[ 1027.1s] S1 phase B: 96000 walkers; preflight 2605s (linear 239s + quadratic 1497s, x1.5); elapsed 1027s; remaining 13373s
[ 2683.8s]     |     walk 96000x32768 in 112.1s paired=True rss 205MiB
[ 2683.8s]     |     samples 514.1s, dataset 513.8s rss 268MiB
[ 2683.8s]     |     gate pass in 516.5s rss 273MiB; checks {"gate_pass": true, "nonzero_se_ok": true, "oracle_margin_ok": true, "oracle_margin_ratio": 335.4821694829457, "paired_bitwise": true, "survival_sign_ok": true}
[ 2683.8s] S1: completed verdict=numerical_no_result wall=1657s rss=273MiB reasons=['6 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.008532 (1.7x); exit_count_lower@x=0.435512 bound 0.007393 (1.5x); exit_count_upper@x=0.610512 bound 0.006986 (1.4x); survival@x=0.260512 bound 0.005246 (1.1x); survival@x=0.435512 bound 0.007188 (1.4x); survival@x=0.610512 bound 0.006946 (1.4x)']
[ 2683.8s] S2: stopped — predecessor S1 = numerical_no_result
[ 2683.8s] S3: stopped — predecessor S2 = None
[ 2683.8s] S4: stopped — predecessor S3 = None
[ 2684.1s] session end: wall 2684s; results/ unchanged=True package unchanged=True
```
