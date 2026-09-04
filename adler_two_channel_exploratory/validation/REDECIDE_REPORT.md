# Re-decided gate verdicts — derivation report

**A derivation over recorded ladders; no run and no package change.  Nothing here is an approval or a sufficiency promise.**

Date 2026-09-04.  Instruction (John, sponsor's decision): "Re-decide the two gate verdicts on the retained identities."  Chained to REFROZEN_DESIGN.json digest `13f3bf1f16d5463dfbfe91c7d1c1d5a80c70da2dd4bf3f91b8f934dab5685ec4`.

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

## Manifest (`REDECIDED_GATES.json`)

- **Manifest digest:** `3f924ffcde067ab353a5fe45f46b1b372e743ed6d611566eb752fd398d6f4ec8`
- Method: RefinementLevel records rebuilt from each recorded ladder's per-level measured, reference, standard_error, paired_error, span_error and clusters; ValidationBudget per identity from the frozen caps; judged by killed_diffusion._ladder_codes (the package's single source of the gate decision) with coverage 2.0.  Mirror validated: judging every identity reproduces the recorded reasons verbatim (see per ladder).  Re-decided verdict = numerical_no_result if any RETAINED identity earns a code, else pass; no clause softened.
- added_resets_mean: Set aside for the re-decision by the sponsor's decision: it judges a diagnostic count with no continuum limit that is not a retained observable.  Its status under the frozen cap is reported separately per moving ladder and is NOT re-frozen.

## Re-decided ladders

| Ladder | Record | Original verdict | Retained identities judged | Retained codes | **Re-decided** | added_resets_mean status (set aside) | Mirror reproduces recorded reasons |
| --- | --- | --- | --- | --- | --- | --- | --- |
| REF_S3 | observations.json | pass | 6: exit_quantile_p35@x=0.184397, exit_quantile_p35@x=0.384397, exit_quantile_p35@x=0.584397, survival@x=0.184397, survival@x=0.384397, survival@x=0.584397 | none | **pass** | n/a | True |
| REF_S3B | observations.json | numerical_no_result | 4: commit_probability_shift@pooled, survival_shift_at_0.45@pooled, survival_shift_at_0.60@pooled, survival_shift_at_0.80@pooled | none | **pass** | no code | True |
| S3 | observations_s3.json | numerical_no_result | 6: exit_quantile_p35@x=0.260512, exit_quantile_p35@x=0.435512, exit_quantile_p35@x=0.610512, survival@x=0.260512, survival@x=0.435512, survival@x=0.610512 | none | **pass** | n/a | True |
| M5 | observations.json | numerical_no_result | 4: commit_probability_shift@pooled, survival_shift_at_0.45@pooled, survival_shift_at_0.60@pooled, survival_shift_at_0.80@pooled | none | **pass** | would block: [['absolute_cap', '3.6123 count with standard error 0.0769676 gives a 2-sigma bound 3.76624 past the cap 3']] | True |
| M6 | observations_redesign.json | numerical_no_result | 4: commit_probability_shift@pooled, survival_shift_at_0.45@pooled, survival_shift_at_0.60@pooled, survival_shift_at_0.80@pooled | none | **pass** | would block: [['absolute_cap', '14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3']] | True |

### REF_S3

- Original: **pass**; recorded reasons: []
- Re-decided on the retained identities: **pass**.

| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |
| --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower@x=0.184397 | no | 0.035993 / 0.08 ok | 0.0497 / 0.45 ok | 0.023861 ≤ 0.040027 + 0.015148 ok | 0 ok | — |
| exit_count_lower@x=0.384397 | no | 0.025987 / 0.08 ok | 0.0539 / 0.45 ok | 0.014192 ≤ 0.025025 + 0.014895 ok | 0 ok | — |
| exit_count_lower@x=0.584397 | no | 0.012452 / 0.08 ok | 0.0349 / 0.45 ok | 0.0047338 ≤ 0.011234 + 0.016232 ok | 0 ok | — |
| exit_count_upper@x=0.184397 | no | 0.010861 / 0.07 ok | 0.0296 / 0.45 ok | 0.0042971 ≤ 0.010797 + 0.016651 ok | 0 ok | — |
| exit_count_upper@x=0.384397 | no | 0.024425 / 0.07 ok | 0.0516 / 0.45 ok | 0.014236 ≤ 0.025402 + 0.014815 ok | 0 ok | — |
| exit_count_upper@x=0.584397 | no | 0.036692 / 0.07 ok | 0.0477 / 0.45 ok | 0.023795 ≤ 0.041295 + 0.01551 ok | 0 ok | — |
| exit_quantile_p35@x=0.184397 | yes | 0.1529 / 0.3 ok | 0.139 / 0.45 ok | 0.11128 ≤ 0.1855 + 0.053056 ok | 0 ok | — |
| exit_quantile_p35@x=0.384397 | yes | 0.13299 / 0.3 ok | 0.0731 / 0.45 ok | 0.091514 ≤ 0.16251 + 0.055208 ok | 0 ok | — |
| exit_quantile_p35@x=0.584397 | yes | 0.13255 / 0.3 ok | 0.116 / 0.45 ok | 0.087378 ≤ 0.15769 + 0.048998 ok | 0 ok | — |
| survival@x=0.184397 | yes | 0.039738 / 0.09 ok | 0.0752 / 0.3 ok | 0.028158 ≤ 0.050824 + 0.015624 ok | 0 ok | — |
| survival@x=0.384397 | yes | 0.040469 / 0.09 ok | 0.0617 / 0.3 ok | 0.028427 ≤ 0.050427 + 0.015672 ok | 0 ok | — |
| survival@x=0.584397 | yes | 0.041245 / 0.09 ok | 0.0781 / 0.3 ok | 0.028529 ≤ 0.052529 + 0.016426 ok | 0 ok | — |

### REF_S3B

- Original: **numerical_no_result**; recorded reasons: ["('commit_time_quantile_p20_shift', 'pooled'): [absolute_cap] 0.0112 time with standard error 0.0829003 gives a 2-sigma bound 0.177001 past the cap 0.1"]
- Re-decided on the retained identities: **pass**.

| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |
| --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean@pooled | no | 1.4454 / 3 ok | 0.981 / 30 ok | waived (require_decrease=false) | waived | — |
| commit_probability_shift@pooled | yes | 0.019046 / 0.1 ok | 0.00833 / 4 ok | 0.0083333 ≤ 0.00625 + 0.023883 ok | 1 ok | — |
| commit_time_quantile_p20_shift@pooled | no | 0.177 / 0.1 FAIL | 0.0112 / 4 ok | 0.0112 ≤ 0.1344 + 0.3333 ok | 0 ok | ['absolute_cap'] |
| survival_shift_at_0.45@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0.010417 + 0.026086 ok | 0 ok | — |
| survival_shift_at_0.60@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0.010417 + 0.025361 ok | 0 ok | — |
| survival_shift_at_0.80@pooled | yes | 0.032857 / 0.1 ok | 0.0146 / 4 ok | 0.014583 ≤ 0.022917 + 0.02088 ok | 1 ok | — |

### S3

- Original: **numerical_no_result**; recorded reasons: ["('exit_count_upper', 'x=0.435512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging", "('exit_count_upper', 'x=0.610512'): [repeated_reversal] 2 adjacent reversals; one upward step can be statistically unresolved, a ladder that turns around more than once is not converging"]
- Re-decided on the retained identities: **pass**.

| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |
| --- | --- | --- | --- | --- | --- | --- |
| exit_count_lower@x=0.260512 | no | 0.0051664 / 0.08 ok | 0.00375 / 0.45 ok | 0.0024744 ≤ 0.003891 + 0.012947 ok | 0 ok | — |
| exit_count_lower@x=0.435512 | no | 0.0063735 / 0.08 ok | 0.00724 / 0.45 ok | 0.0031899 ≤ 0.0037733 + 0.012319 ok | 0 ok | — |
| exit_count_lower@x=0.610512 | no | 0.0055823 / 0.08 ok | 0.0116 / 0.45 ok | 0.0028792 ≤ 0.0029937 + 0.012218 ok | 0 ok | — |
| exit_count_upper@x=0.260512 | no | 0.0026992 / 0.07 ok | 0.00347 / 0.45 ok | 0.00089127 ≤ 0.0010996 + 0.012405 ok | 0 ok | — |
| exit_count_upper@x=0.435512 | no | 0.004541 / 0.07 ok | 0.00415 / 0.45 ok | 0.0018733 ≤ 0.0013733 + 0.012737 ok | 2 FAIL | ['repeated_reversal'] |
| exit_count_upper@x=0.610512 | no | 0.0043552 / 0.07 ok | 0.00274 / 0.45 ok | 0.0018334 ≤ 0.00093755 + 0.013303 ok | 2 FAIL | ['repeated_reversal'] |
| exit_quantile_p35@x=0.260512 | yes | 0.0076088 / 0.3 ok | 0.0138 / 0.45 ok | 0.0040941 ≤ 0.0065561 + 0.03062 ok | 0 ok | — |
| exit_quantile_p35@x=0.435512 | yes | 0.0074797 / 0.3 ok | 0.0078 / 0.45 ok | 0.0039666 ≤ 0.00579 + 0.03068 ok | 0 ok | — |
| exit_quantile_p35@x=0.610512 | yes | 0.006549 / 0.3 ok | 0.0107 / 0.45 ok | 0.0030818 ≤ 0.0051826 + 0.030747 ok | 0 ok | — |
| survival@x=0.260512 | yes | 0.0032436 / 0.09 ok | 0.0189 / 0.3 ok | 0.0015831 ≤ 0.0027914 + 0.012461 ok | 0 ok | — |
| survival@x=0.435512 | yes | 0.0030635 / 0.09 ok | 0.0122 / 0.3 ok | 0.0013166 ≤ 0.0023999 + 0.012607 ok | 0 ok | — |
| survival@x=0.610512 | yes | 0.0026269 / 0.09 ok | 0.0127 / 0.3 ok | 0.0010458 ≤ 0.0020562 + 0.012618 ok | 0 ok | — |

### M5

- Original: **numerical_no_result**; recorded reasons: ["('added_resets_mean', 'pooled'): [absolute_cap] 3.6123 count with standard error 0.0769676 gives a 2-sigma bound 3.76624 past the cap 3"]
- Re-decided on the retained identities: **pass**.

| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |
| --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean@pooled | no | 3.7662 / 3 FAIL | 3.61 / 30 ok | waived (require_decrease=false) | waived | ['absolute_cap'] |
| commit_probability_shift@pooled | yes | 0.011559 / 0.1 ok | 0.00954 / 4 ok | 0.0095378 ≤ 0.018652 + 0.012526 ok | 0 ok | — |
| commit_time_quantile_p20_shift@pooled | no | 0.083608 / 0.1 ok | 0.059 / 4 ok | 0.058984 ≤ 0.125 + 0.035263 ok | 0 ok | — |
| survival_shift_at_0.45@pooled | yes | 0.0044355 / 0.1 ok | 0.00326 / 4 ok | 0.0032552 ≤ 0.0065104 + 0.011421 ok | 0 ok | — |
| survival_shift_at_0.60@pooled | yes | 0.0085336 / 0.1 ok | 0.00684 / 4 ok | 0.0068359 ≤ 0.011458 + 0.012156 ok | 0 ok | — |
| survival_shift_at_0.80@pooled | yes | 0.011686 / 0.1 ok | 0.00967 / 4 ok | 0.009668 ≤ 0.019108 + 0.012523 ok | 0 ok | — |

### M6

- Original: **numerical_no_result**; recorded reasons: ["('added_resets_mean', 'pooled'): [absolute_cap] 14.0938 count with standard error 2.54299 gives a 2-sigma bound 19.1797 past the cap 3", "('commit_time_quantile_p20_shift', 'pooled'): [not_converging] 0.00546875 at 0.000488281 against 0.0283203 at 0.00012207, past the single whole-ladder allowance 0.0221183"]
- Re-decided on the retained identities: **pass**.

| Identity | Retained | Clause 2 abs (bound / cap) | Clause 2 rel | Clause 3 finest ≤ coarsest + allowance | Clause 4 reversals | Codes |
| --- | --- | --- | --- | --- | --- | --- |
| added_resets_mean@pooled | no | 19.18 / 3 FAIL | 14.1 / 30 ok | waived (require_decrease=false) | waived | ['absolute_cap'] |
| commit_probability_shift@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0 + 0.01 ok | 1 ok | — |
| commit_time_quantile_p20_shift@pooled | no | 0.060704 / 0.1 ok | 0.0283 / 4 ok | 0.02832 ≤ 0.0054688 + 0.022118 FAIL | 1 ok | ['not_converging'] |
| survival_shift_at_0.45@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0 + 0.01 ok | 0 ok | — |
| survival_shift_at_0.60@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0 + 0.01 ok | 1 ok | — |
| survival_shift_at_0.80@pooled | yes | 0 / 0.1 ok | 0 / 4 ok | 0 ≤ 0 + 0.01 ok | 1 ok | — |

## Dispositions on the re-frozen observable set with the re-decided gate verdicts carried

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

## Power translation (experiments.power_estimate, read-only; frozen target 0.25)

| Evidence set | Admissible trials | Half-width (power model) | Half-width (scaling) | Meets 0.25 |
| --- | --- | --- | --- | --- |
| stationary_only | 5704 | 0.162 | 0.162 | True |
| all_intended | 439 | 0.585 | 0.585 | False |
| reference_plus_intended | 0 | — | — | — |

## What still blocks, and the cheapest priced run (proposal only)

- What still blocks is the moving-band audit's retained probability shifts at the intended step (M5 rows 1.7x-2.3x); the re-decided gates remove every carried gate verdict, so the all-intended set is 'unresolved' rather than 'numerical_no_result'.  The records suggest no cheaper route than the M5-size dt/16 ladder: at dt/8 the projected worst bound is 0.0054 (fails); fewer trials at dt/16 fail on SE (1280 trials: 0.0024 + 0.0028 = 0.0052); more trials at a coarser step cost more (dt/8 x 4 trials = 2x the dt/16 cost).
- Under the re-frozen set nothing stationary blocks except S3's carried gate verdict, which came from exit_count_upper (dropped).  Re-deciding that gate on the retained identities is a decision, not a run; a fresh verdict object would need S3 re-run under a re-frozen FrozenBudgets: 4040 s measured (7249 s priced), oracle child 1536 MiB, construction child 332 MiB.

| Ladder | Projected finest bounds (retained moving rows) | All fit 0.004995 | Physical intervals | Priced (x1.5) |
| --- | --- | --- | --- | --- |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/2: mesh step 0.000977, 4096 steps, strides (4,2,1) | commit_probability_shift 0.0088, ss0.45 0.0035, ss0.60 0.0065, ss0.80 0.0089 | False | 55,096,320 | 11238 s (187.3 min) (3.1 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/4: mesh step 0.000488, 8192 steps, strides (4,2,1) | commit_probability_shift 0.0068, ss0.45 0.0028, ss0.60 0.0051, ss0.80 0.0069 | False | 110,146,560 | 22466 s (374.4 min) (6.2 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/8: mesh step 0.000244, 16384 steps, strides (4,2,1) | commit_probability_shift 0.0054, ss0.45 0.0023, ss0.60 0.0041, ss0.80 0.0054 | False | 220,247,040 | 44924 s (748.7 min) (12.5 h) |
| M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/16: mesh step 0.000122, 32768 steps, strides (4,2,1) | commit_probability_shift 0.0044, ss0.45 0.0020, ss0.60 0.0034, ss0.80 0.0044 | True | 440,448,000 | 89838 s (1497.3 min) (25.0 h) |

- **Cheapest that projects to fit:** M5-size (2560 master trials x 3 clocks x 4 replicates) at dt/16: mesh step 0.000122, 32768 steps, strides (4,2,1).  Memory: M5 measured 76 MiB, M6 79 MiB with the streaming validation runner (records digested, not stored); the pricing session's linear memory model (54.7 B per physical interval) applied only to the pricing children, which kept every AuditedRun record.

## Ambiguities and choices

1. **The gate's own function.** Verdicts are re-decided by calling killed_diffusion._ladder_codes on rebuilt RefinementLevel records, not by a re-implementation; the mirror is validated per ladder by reproducing the recorded reasons verbatim over all identities (dropped ones included).
2. **Retained identities only.** A ladder's re-decided verdict considers only retained identities; a retained identity failing any frozen clause keeps the ladder at numerical_no_result.  No cap, floor or coverage is changed.
3. **added_resets_mean.** Set aside by the sponsor's decision as a diagnostic count outside the retained set; its frozen-cap status is reported separately and it is not re-frozen.
4. **Reference ladders.** The reference S3b ladder is re-decided on the same rule so that the reference-plus-intended set is consistent; the reference S3 ladder passed originally and passes on the retained identities.
5. **Evidence rows.** Rows carry the re-decided verdicts; observables, positions, measured errors and SEs are exactly the recorded ones.

## Reproduce

```
cd /Users/john-bramble/Projects/Physics/DiracKuramotoFramework
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/redecide_gates.py --run     # writes REDECIDED_GATES.json and this report
PYTHONDONTWRITEBYTECODE=1 python3 adler_two_channel_exploratory/validation/redecide_gates.py --check   # recomputes and compares the manifest digest
```
