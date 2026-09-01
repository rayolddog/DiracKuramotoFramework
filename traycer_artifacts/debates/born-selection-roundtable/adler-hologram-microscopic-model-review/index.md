---
title: "Adversarial review: Adler hologram microscopic model"
kind: review
---

# Verdicts

| Question | Strict verdict | Basis |
| --- | --- | --- |
| **Born-free Adler derivation demonstrated?** | **No — blocked.** | The code assumes an event-rate law proportional to the classical intensity before it applies Poisson counting. No Adler differential equation or grain dynamics derives that rate. The one-event, weak-exposure regime then preserves the assumed square law by construction. |
| **Mere interference consistency demonstrated?** | **Yes, narrowly.** | The classical complex fields are coherently summed, `abs(E_total)**2` contains the expected cross term, relative phase translates the fringe, and the incoherent control is phase-independent. This validates classical-wave bookkeeping, not quantum event probabilities. |

Reviewed frozen inputs:

| File | SHA-256 |
| --- | --- |
| `hologram_phase_test/phase_sweep.py` | `8af23225bfba29ae60ba2cf9d040cb77399bcec8e81bee0a419de56bec0f318d` |
| `hologram_phase_test/test_phase_sweep.py` | `a82a7cc61a1336a03f37e79c005c78c724bd0b9f83449667e5d342de2afcfb90` |
| `hologram_phase_test/README.md` | `95adcc6383f9d500a0f89bfbb47efc05bdb1b18ad53b0d44b6e74e9d179dfdf9` |

# Findings, in priority order

## 1. Blocking — the target square law is inserted in the event-rate law

The implemented authority chain is algebraically:

```text
E_total = E_object + E_reference
I = |E_total|^2
K = g sqrt(I) = g |E_total|
locked_fraction = min(K / Delta, 1)
response = r K locked_fraction
mu = t response
P(activated) = P(Poisson(mu) >= n)
```

In the deliberately unsaturated regime, `locked_fraction = K / Delta`, so `response = (r/Delta) K^2 = (r g^2/Delta) I`. That conclusion is fixed at `phase_sweep.py:170-175`, before stochastic counting or a grain threshold enters. The alternative `square_drive` branch at `phase_sweep.py:172-174` inserts `K^2` even more directly.

The static Adler locking criterion can support a locked fraction proportional to `K` **if** one first assumes an independent uniform detuning population. It does not supply the additional factor of `K` interpreted here as flux per locked element. That factor is an unvalidated constitutive law and is exactly what changes the response from field amplitude (`sqrt(I)`) to intensity (`I`).

A targeted counterfactual using the frozen code's fields, coupling, Poisson layer, threshold 1, and exposure `0.01` gave:

| Rate supplied to counting | Fitted intensity exponent | Normalized RMSE vs intensity |
| --- | --- | --- |
| Implemented `K * locked_fraction` | 0.999854 | 0.000122 |
| `locked_fraction` alone | 0.499649 | 0.162106 |
| `K` alone | 0.499649 | 0.162106 |
| Constant rate for every nominally locked grain | approximately 0 | 0.612372 |

Thus Adler locking does not select the target law. The extra `K` does.

## 2. Blocking — the probability-generating authority is assumed, not derived

`thresholded_grain_response` declares `mean_count = exposure_time * adler_response` at `phase_sweep.py:248` and then assumes a Poisson point process at `phase_sweep.py:249-251`. Neither step follows from an Adler locking condition:

- identifying the algebraic response with a microscopic event intensity is an independent assumption;
- Poisson independence and stationarity are independent assumptions;
- the map from event count to developed silver-halide grain is an integer threshold chosen by the configuration, not a modeled latent-image mechanism.

Poisson statistics alone do not assume the Born rule. The circularity is that their mean inherits the already-assumed `mu proportional to I`. With the favorable default `n = 1` and weak exposure, `P(activated) = 1 - exp(-mu) approximately mu`, so the output necessarily preserves `I`. For weak exposure and threshold `n`, the same construction gives `P approximately mu^n/n!`, hence `I^n`; the frozen tests explicitly confirm exponents 1, 2, 3, and 4 (`test_phase_sweep.py:79-128`). This is sensitivity to an unconstrained threshold, not a derivation of universal event selection.

## 3. Blocking — no Adler evolution or microscopic grain dynamics is simulated

Despite the labels, the code never evolves an Adler equation such as `phase_dot = detuning - K sin(phase)`. There are no oscillator phases, trajectories, finite-time capture, phase slips, noise, initial conditions, relaxation rates, energy-transfer dynamics, or coupled absorber states. `locked_fraction` is the closed-form clipping expression at `phase_sweep.py:171`.

There is likewise no silver-halide model: no absorption cross-section, spectral sensitizer, electron/hole production, trapping, latent-image speck nucleation, multi-site survival, reciprocity failure, development, bleaching, or grain-density readout. The README correctly concedes this at `README.md:82-89`, and metadata calls the event rate assumed at `phase_sweep.py:760-765`. Consequently, “Adler” currently names a static algebraic ansatz rather than a microscopic mechanism.

## 4. High — the tests and exposure selection are consistency checks against a built-in target

The suite passes, but it is not an independent test of the decisive physics:

- `test_coherent_cross_term` reconstructs the same classical identity used by the implementation (`test_phase_sweep.py:12-25`).
- `test_unsaturated_tongue_flux_is_proportional_to_intensity` asserts the direct algebraic consequence of the chosen `K * locked_fraction` law (`test_phase_sweep.py:49-69`).
- the “Born” comparisons pass `result.coherent_intensity` itself as the variable named `psi_squared` (`test_phase_sweep.py:79-105`); no independently predicted or observed probability distribution is supplied;
- `run_self_checks` fixes the configuration below saturation, selects the one-event response, and fails if the result no longer resembles the same input intensity (`phase_sweep.py:560-623`);
- exposure criteria are explicitly defined by proximity to exponent 1 and small error against intensity (`phase_sweep.py:397-412,448-459`), then a favorable interval is selected (`phase_sweep.py:464-554`).

The exposure scan is useful for documenting when the assumed mapping preserves its input, but it cannot elevate that mapping into a derivation. A strict review must treat both the favorable threshold and target-based window as selection on the desired answer.

## 5. High — the parameters are physically non-identifiable in the demonstrated regime

Below saturation the observables depend only on the composite scale

```text
t * r * g^2 / Delta
```

where `t` is normalized exposure, `r` is `rate_scale`, `g` is `coupling_per_field`, and `Delta` is `detuning_half_width`. These quantities cannot be separately inferred from the generated activation pattern. The assumed uniform detuning distribution is not measured, and many non-Adler response laws can reproduce the same classical intensity fringe.

Normalization removes absolute units and the shape comparison removes the overall film-density scale (`phase_sweep.py:346-367`). That is appropriate for a dimensionless consistency illustration but prevents identification of a microscopic coupling, event rate, detuning distribution, threshold, or physical exposure time. Calibrating only the final rate would still be circular; the upstream ingredients must be constrained independently of the square-law outcome.

## 6. Medium — `|E|^2` is legitimate classical input, but calling it `|psi|^2` conflates two claims

The individual operations have different epistemic status:

| Operation | Does it already assume the conclusion? | Assessment |
| --- | --- | --- |
| `np.abs(E_total)**2` | **No, if `E_total` is a classical electromagnetic field.** | It is the standard classical interference/energy-density or flux pattern (up to units and medium factors). It does not derive a quantum detection probability. |
| `sqrt(intensity)` | **No by itself.** | It simply recovers field magnitude. Choosing `K = g\|E\|` is a coupling ansatz that still needs physical justification. |
| `locked_fraction = K/Delta` below saturation | **No square law by itself.** | It follows from a static Adler locking interval only after assuming a uniform detuning population; it scales as `sqrt(I)`, not `I`. |
| `K * locked_fraction` | **Yes, decisively in this setup.** | The extra `K` forces the unsaturated response to `K^2 proportional to I` without microscopic support. |
| Poisson mean `mu = t * response` | **It imports the assumed result.** | Poisson algebra is not Born's rule, but declaring the target-shaped response to be the event intensity makes the count mean target-shaped. |
| Analytic threshold tail | **No by itself.** | It correctly computes an assumed Poisson tail. Threshold 1 plus weak exposure is then a favorable regime that linearly preserves the assumed mean. |
| Exposure-window calculation | **Yes as evidence of derivation.** | Its pass/fail criteria explicitly optimize agreement with exponent 1 and the input intensity, so it can only characterize target preservation. |

The name `coherent_intensity` is accurate; the later renaming of that same array to `psi_squared` in comparisons and plots (`phase_sweep.py:325-367,745-797`) is not a derivation from a quantum state. The code demonstrates Maxwell interference consistency and then compares its assumed detector response back to the Maxwell input.

# What a PFG-01-class red plate test would still require

The manufacturer's current PFG-01 page reports a sensitivity peak around `100 microJoule/cm^2` near `640 nm`, provides an optical-density characteristic curve, and specifies processing chemistry and times ([GEOLA PFG-01 product data](https://www.geola.com/product/pfg-01-plates/)). At 640 nm that nominal incident fluence is about `3.2e14` photons per square centimetre, so it does not by itself establish a weak, one-event-per-grain regime.

A physically discriminating experiment/model would need, at minimum:

1. absolute irradiance and exposure calibration at the actual wavelength, with polarization, coherence length, phase stability, visibility, fringe pitch, vibration, and spatial nonuniformity controlled;
2. independently measured plate properties for the exact batch: grain-size and density distributions, emulsion thickness, absorption/sensitization efficiency, fog/dark response, reciprocity, saturation, and the post-development characteristic curve;
3. a microscopic latent-image model or measurements connecting absorbed quanta to electron/hole trapping, silver-speck nucleation, survival, development, and the operational definition of one “activated grain”;
4. an explicit Adler dynamical variable in the material, its detuning distribution, damping/noise, coupling units, finite-time locking/capture behavior, and an independently justified energy- or event-transfer law for locked and unlocked states;
5. independent calibration of `g`, `Delta`, the transfer rate, counting statistics, and grain threshold, without fitting them to square-law fringe density;
6. raw grain-level count distributions across randomized phase and exposure, including tests of Poisson variance/independence versus overdispersion, clustering, multi-hit thresholds, developer noise, and batch effects;
7. preregistered predictions that distinguish `K`, locked fraction, `K * locked_fraction`, ordinary photochemistry, and other response laws outside the hand-selected weak/unsaturated window.

Until those links are supplied, the code is a clean numerical illustration of how an assumed intensity-proportional rate survives a chosen counting/threshold regime. It is not a Born-free microscopic derivation.

# Verification record

- Frozen SHA-256 hashes: all matched.
- Command: `python3 -m unittest -v test_phase_sweep.py` from `hologram_phase_test`.
- Result: **13/13 passed** in 0.314 s.
- Focused counterfactuals were run in memory only; no reviewed code, Git state, or unrelated artifact was modified.
