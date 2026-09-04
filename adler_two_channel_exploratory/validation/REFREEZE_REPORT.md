# Re-frozen production design — derivation report

**A derivation over existing records; no run and no package change.  Nothing here is an approval or a sufficiency promise.**

Date 2026-09-04.  Instruction (John, sponsor's plan change): "Re-freeze the production design on survival and the time rows."

## Environment identity

| Field | Value |
| --- | --- |
| platform | `macOS-26.5.2-arm64-arm-64bit-Mach-O` |
| cpu_brand | `Apple M4 Pro` |
| python_version | `3.13.11` |
| numpy_version | `2.4.3` |
| package source fingerprint | `8bb1a4eddd8b93a3458393bd027536e3b6f7a5f51d49fa561f7161926b945992` |
| frozen budget digest | `8ff45c2c33c01192129320db814f367845c4cf29cf05cbb7372af8aa0886da61` |
| record `first` sha256 | `0e2b2b9769dfcb793b05180b132ab1fca7367a745babe40bc2e15f62f21770b0` |
| record `redesign` sha256 | `5c4c4aeddb0edd617ae4d139f29514ca5ecc9fbbd4c7c79227e3bde5c380bb8e` |
| record `s2` sha256 | `2588c5e22937380b2dc61304c4bfe0957dba23972893311991f423e637bd7d58` |
| record `s3` sha256 | `3c1b2cf8e2434d2eb6e60185fc1ef2e93653b9b58d286409be6346d368a4de3c` |
| record `pricing` sha256 | `d22d12368a9c5ca07e9ba441fc4f638fb3901b7c6b4070fe22cd1014bf3a38a7` |

## Manifest (`REFROZEN_DESIGN.json`)

- **Manifest digest:** `13f3bf1f16d5463dfbfe91c7d1c1d5a80c70da2dd4bf3f91b8f934dab5685ec4`
- Retained: {"moving_band_audit": ["commit_probability_shift", "survival_shift_at_0.45", "survival_shift_at_0.60", "survival_shift_at_0.80"], "stationary_oracle": ["survival", "exit_quantile_p35"]}
- Dropped: ['exit_count_upper', 'exit_count_lower', 'commit_time_quantile_p20_shift']
  - **exit_count_upper**: S3 (dt/256 at eightfold space, 96,000 walkers): ladder gate numerical_no_result on this observable at two starts; the error RISES under refinement with paired bootstrap SEs far below the steps.  Quoted: ('exit_count_upper', 'x=0.435512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging; ('exit_count_upper', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging
    errors by level (coarse → fine): {"x=0.260512": [0.0011, 0.00094, 0.00089], "x=0.435512": [0.00137, 0.00167, 0.00187], "x=0.610512": [0.00094, 0.00146, 0.00183]}
  - **exit_count_lower**: S3: the edge-attribution offset does not fall with dt; the three finest-level rows are the only stationary rows over the allowance.  Quoted: 3 of 9 probability rows exceed the allowance 0.00499471: exit_count_lower@x=0.260512 bound 0.005166 (1.03x); exit_count_lower@x=0.435512 bound 0.006373 (1.28x); exit_count_lower@x=0.610512 bound 0.005582 (1.12x)
    errors by level (coarse → fine): {"x=0.260512": [0.00389, 0.00303, 0.00247], "x=0.435512": [0.00377, 0.00339, 0.00319], "x=0.610512": [0.00299, 0.00298, 0.00288]}
  - **commit_time_quantile_p20_shift**: M6 (dt/16 replay, 40 master trials): gate clause 3 [not_converging] on this observable; M5 (2560 trials) and the reference audit also fail the time allowance on it (3.81x, 8.06x).  Quoted: ('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3; ('commit_time_quantile_p20_shift', 'pooled'): [not_converging] 0.00546875 at 0.000488281 against 0.0283203 at 0.00012207, past the single whole-ladder allowance 0.0221183

- **Not re-frozen:** The ladder gates (killed_diffusion.compare_refinement under the frozen verify.py caps, INCLUDING the moving-band added_resets_mean absolute cap 3.0) and the frozen ticket-07 budget allowances (probability 0.004995, time 0.021953) are NOT re-frozen by this decision.
- **FLAG: every moving-band ladder verdict on record (reference S3b, M5, M6) is numerical_no_result under the un-re-frozen gate (added-resets cap and/or p20 non-convergence), and experiments.numerical_disposition carries that verdict through as the blocker moving_band_numerical_no_result regardless of which observables are retained.  Likewise S3's stationary gate verdict is numerical_no_result on exit_count_upper (a dropped observable) and is carried as endpoint_envelope_exceeds_allowance.  Unless the sponsor separately re-freezes the gates, the disposition cannot leave numerical_no_result whatever the observable set.  The hypothetical recomputations below show what changes if the gates were re-decided; they are labelled hypothetical and authorize nothing.**

## Dispositions on the re-frozen observable set (gate verdicts carried, as frozen)

### `stationary_only` (6 rows; row verdicts ['stationary_oracle:numerical_no_result'])

- Verdict **numerical_no_result**; blockers ['endpoint_envelope_exceeds_allowance']; probability-admissible trials 5704 (target 2406); time admissible True; overall admissible 5704.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.260512", "probability", 0.0032436325812476375, 0.004994710172401896, true], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |

### `all_intended` (14 rows; row verdicts ['moving_band_audit:numerical_no_result', 'stationary_oracle:numerical_no_result'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty']; probability-admissible trials 439 (target 2406); time admissible True; overall admissible 439.
- Limiting rows: {"probability": ["moving_band_audit", "survival_shift_at_0.80", "pooled", "probability", 0.011686381511775135, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### `reference_plus_intended` (24 rows; row verdicts ['moving_band_audit:numerical_no_result', 'stationary_oracle:numerical_no_result', 'stationary_oracle:pass'])

- Verdict **numerical_no_result**; blockers ['moving_band_numerical_no_result', 'endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (target 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.184397", "time", 0.1528954619884105, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.584397 | probability | 0.04125 | 0.00499 | 8.26x | NO |
| stationary_oracle | survival | x=0.384397 | probability | 0.04047 | 0.00499 | 8.10x | NO |
| stationary_oracle | survival | x=0.184397 | probability | 0.03974 | 0.00499 | 7.96x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.184397 | time | 0.15290 | 0.02195 | 6.96x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.03286 | 0.00499 | 6.58x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.384397 | time | 0.13299 | 0.02195 | 6.06x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.584397 | time | 0.13255 | 0.02195 | 6.04x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01905 | 0.00499 | 3.81x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
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

## HYPOTHETICAL — moving-band gate verdict not carried (audit gate re-frozen by the sponsor)

### `stationary_only` (6 rows; row verdicts ['stationary_oracle:numerical_no_result'])

- Verdict **numerical_no_result**; blockers ['endpoint_envelope_exceeds_allowance']; probability-admissible trials 5704 (target 2406); time admissible True; overall admissible 5704.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.260512", "probability", 0.0032436325812476375, 0.004994710172401896, true], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |

### `all_intended` (14 rows; row verdicts ['moving_band_audit:pass', 'stationary_oracle:numerical_no_result'])

- Verdict **numerical_no_result**; blockers ['endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'probability_window_empty']; probability-admissible trials 439 (target 2406); time admissible True; overall admissible 439.
- Limiting rows: {"probability": ["moving_band_audit", "survival_shift_at_0.80", "pooled", "probability", 0.011686381511775135, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### `reference_plus_intended` (24 rows; row verdicts ['moving_band_audit:pass', 'stationary_oracle:numerical_no_result', 'stationary_oracle:pass'])

- Verdict **numerical_no_result**; blockers ['endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (target 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.184397", "time", 0.1528954619884105, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.584397 | probability | 0.04125 | 0.00499 | 8.26x | NO |
| stationary_oracle | survival | x=0.384397 | probability | 0.04047 | 0.00499 | 8.10x | NO |
| stationary_oracle | survival | x=0.184397 | probability | 0.03974 | 0.00499 | 7.96x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.184397 | time | 0.15290 | 0.02195 | 6.96x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.03286 | 0.00499 | 6.58x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.384397 | time | 0.13299 | 0.02195 | 6.06x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.584397 | time | 0.13255 | 0.02195 | 6.04x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01905 | 0.00499 | 3.81x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
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

## HYPOTHETICAL — moving-band AND stationary gate verdicts not carried (both gates re-decided on the retained identities)

### `stationary_only` (6 rows; row verdicts ['stationary_oracle:pass'])

- Verdict **satisfied**; blockers []; probability-admissible trials 5704 (target 2406); time admissible True; overall admissible 5704.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.260512", "probability", 0.0032436325812476375, 0.004994710172401896, true], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |

### `all_intended` (14 rows; row verdicts ['moving_band_audit:pass', 'stationary_oracle:pass'])

- Verdict **unresolved**; blockers ['audit_envelope_exceeds_allowance', 'probability_window_empty']; probability-admissible trials 439 (target 2406); time admissible True; overall admissible 439.
- Limiting rows: {"probability": ["moving_band_audit", "survival_shift_at_0.80", "pooled", "probability", 0.011686381511775135, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.260512", "time", 0.007608777091452655, 0.021953125, true]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
| stationary_oracle | survival | x=0.610512 | probability | 0.00263 | 0.00499 | 0.53x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.260512 | time | 0.00761 | 0.02195 | 0.35x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.435512 | time | 0.00748 | 0.02195 | 0.34x | yes |
| stationary_oracle | exit_quantile_p35 | x=0.610512 | time | 0.00655 | 0.02195 | 0.30x | yes |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.00000 | 0.00499 | 0.00x | yes |

### `reference_plus_intended` (24 rows; row verdicts ['moving_band_audit:pass', 'stationary_oracle:pass'])

- Verdict **unresolved**; blockers ['endpoint_envelope_exceeds_allowance', 'audit_envelope_exceeds_allowance', 'no_evidence_at_intended_configuration', 'probability_window_empty', 'time_bounds_fail_at_every_trial_count']; probability-admissible trials 35 (target 2406); time admissible False; overall admissible 0.
- Limiting rows: {"probability": ["stationary_oracle", "survival", "x=0.584397", "probability", 0.0412453829967519, 0.004994710172401896, false], "time": ["stationary_oracle", "exit_quantile_p35", "x=0.184397", "time", 0.1528954619884105, 0.021953125, false]}

| Source | Observable | Position | Unit | Bound | Allowance | Ratio | Fits |
| --- | --- | --- | --- | --- | --- | --- | --- |
| stationary_oracle | survival | x=0.584397 | probability | 0.04125 | 0.00499 | 8.26x | NO |
| stationary_oracle | survival | x=0.384397 | probability | 0.04047 | 0.00499 | 8.10x | NO |
| stationary_oracle | survival | x=0.184397 | probability | 0.03974 | 0.00499 | 7.96x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.184397 | time | 0.15290 | 0.02195 | 6.96x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.03286 | 0.00499 | 6.58x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.384397 | time | 0.13299 | 0.02195 | 6.06x | NO |
| stationary_oracle | exit_quantile_p35 | x=0.584397 | time | 0.13255 | 0.02195 | 6.04x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01905 | 0.00499 | 3.81x | NO |
| moving_band_audit | survival_shift_at_0.80 | pooled | probability | 0.01169 | 0.00499 | 2.34x | NO |
| moving_band_audit | commit_probability_shift | pooled | probability | 0.01156 | 0.00499 | 2.31x | NO |
| moving_band_audit | survival_shift_at_0.60 | pooled | probability | 0.00853 | 0.00499 | 1.71x | NO |
| moving_band_audit | survival_shift_at_0.45 | pooled | probability | 0.00444 | 0.00499 | 0.89x | yes |
| stationary_oracle | survival | x=0.260512 | probability | 0.00324 | 0.00499 | 0.65x | yes |
| stationary_oracle | survival | x=0.435512 | probability | 0.00306 | 0.00499 | 0.61x | yes |
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

## Power translation (experiments.power_estimate, read-only)

The smallest exponent half-width whose power estimate needs no more than the admissible trial count (bisection on SamplingTarget.exponent_half_width), beside the 1/sqrt(n) scaling 0.25 x sqrt(2406/n); frozen target 0.25.

| Evidence set | Gates | Admissible trials | Half-width (power model) | Half-width (scaling) | Meets 0.25 |
| --- | --- | --- | --- | --- | --- |
| stationary_only | as frozen | 5704 | 0.162 | 0.162 | True |
| all_intended | as frozen | 439 | 0.585 | 0.585 | False |
| reference_plus_intended | as frozen | 0 | — | — | — |
| stationary_only | hypothetical, both gates re-decided | 5704 | 0.162 | 0.162 | True |
| all_intended | hypothetical, both gates re-decided | 439 | 0.585 | 0.585 | False |
| reference_plus_intended | hypothetical, both gates re-decided | 0 | — | — | — |

## What still blocks, and the cheapest priced run (proposal only)

- the moving-band audit's retained probability shifts at the intended step dt = 2^-9 (M5, 2560 master trials): bias-dominated, 1.7x-2.3x the allowance.
- Under the re-frozen set nothing stationary blocks except S3's carried gate verdict, which came from exit_count_upper (dropped).  Re-deciding that gate on the retained identities is a decision, not a run; a fresh verdict object would need S3 re-run under a re-frozen FrozenBudgets: 4040 s measured (7249 s priced), oracle child 1536 MiB, construction child 332 MiB.
- Projection rule: bias projected with the package's sqrt(dt) rule, SE unchanged at 2560 trials (about 0.001).

| Ladder | Projected finest bounds (retained moving rows) | All fit 0.004995 | Physical intervals | Priced (x1.5) |
| --- | --- | --- | --- | --- |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/2: mesh step 0.000977, 4096 steps, strides (4,2,1) | commit_probability_shift 0.0088, ss0.45 0.0035, ss0.60 0.0065, ss0.80 0.0089 | False | 55,096,320 | 11238 s (187.3 min) (3.1 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/4: mesh step 0.000488, 8192 steps, strides (4,2,1) | commit_probability_shift 0.0068, ss0.45 0.0028, ss0.60 0.0051, ss0.80 0.0069 | False | 110,146,560 | 22466 s (374.4 min) (6.2 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/8: mesh step 0.000244, 16384 steps, strides (4,2,1) | commit_probability_shift 0.0054, ss0.45 0.0023, ss0.60 0.0041, ss0.80 0.0054 | False | 220,247,040 | 44924 s (748.7 min) (12.5 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/16: mesh step 0.000122, 32768 steps, strides (4,2,1) | commit_probability_shift 0.0044, ss0.45 0.0020, ss0.60 0.0034, ss0.80 0.0044 | True | 440,448,000 | 89838 s (1497.3 min) (25.0 h) |

- **Cheapest that projects to fit:** M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/16: mesh step 0.000122, 32768 steps, strides (4,2,1).  Memory: M5 measured 76 MiB, M6 79 MiB with the streaming validation runner (records digested, not stored); the pricing session's linear memory model (54.7 B per physical interval) applied only to the pricing children, which kept every AuditedRun record.
- Pricing derivation used: `7c8c0f81d1f69f12f5043a352d2571f2b5f97a922b05634a4729d0f3f0062018`.

## Ambiguities and choices

1. **Gates carried.** The instruction re-freezes the observable set only; the gate verdicts on record are carried into the disposition exactly as experiments.numerical_disposition does.  Because S3's gate failed on a dropped observable and every moving-band gate failed on the added-resets cap and/or the dropped p20 row, two hypotheticals are shown, both labelled, neither authorizing anything.
2. **Stationary gate hypothetical.** compare_refinement judges each (observable, position) identity on its own; S3's recorded reasons name only exit_count_upper, so on the retained identities the recorded ladder would carry no reason.  The hypothetical relabels S3's rows as pass on that basis without re-running anything; a fresh verdict object would require re-running S3 under a re-frozen FrozenBudgets.
3. **Reference rows.** The reference set is restricted to the same retained observables, so the reference-plus-intended set is 24 rows rather than 39.
4. **Power translation.** power_estimate is inverted by bisection on the target half-width with every other SamplingTarget field frozen (maximum_trials_per_cell raised to 200,000 only so that half-widths below 0.25 can be resolved); the scaling column is the closed form.
5. **Proposal.** Bias projected with the package's sqrt(dt) rule, which on this cell was conservative for the retained (survival-type) rows and non-conservative only for the dropped edge-split rows; the M5 ladder's own levels show the retained shifts falling like sqrt(dt).  Prices use the pricing session's slowest replay rate with the 1.5x contingency; memory from the streaming validation runner's measured peaks.

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/refreeze_design.py --run     # writes REFROZEN_DESIGN.json and this report
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/refreeze_design.py --check   # recomputes and compares the manifest digest
```
