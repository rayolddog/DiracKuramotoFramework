# Silver two-slit + Stern-Gerlach: QM vs two-basin noise blur

**Run:** `code/silver_twoslit_noise.py` → `code/silver_twoslit_noise.png` (2026-06-13)

**Question (from session).** A silver (Ag, `^2S_{1/2}`, pure electron-spin-½) Talbot–Lau
interferometer with a downstream Stern–Gerlach analyzer: does the two-basin
"strength-of-attractor" postulate (DISCRETIZATION §3.2; `phi_dissipative_check.py`)
predict the same noise-induced fringe blur as standard QM, or a different one?

---

## Literature check (the experimental backdrop)

- **Silver has *not* been used for matter-wave interference.** Atom double-slit /
  grating interferometry has used metastable He (Carnal–Mlynek), Na, Li, K, Rb, Cs,
  and metastable noble gases; the mass record (~25,000 amu) is Arndt's Talbot–Lau.
  Silver's matter-wave role is **Stern–Gerlach** (1922) and **atom lithography**
  (depositing Ag/Cr through optical standing waves), not interference. No fundamental
  obstacle — it is simply not the species people picked (no easy cooling/cycling
  transition; UV 328 nm resonance; detection by deposition or resonant ionization).
- **Architecture is forced to near-field Talbot–Lau**, not far-field Young, because
  `λ_dB ≈ 6.75 pm` for a 1300 K Ag beam (v ≈ 548 m/s) — same pm regime as the C₆₀
  fullerenes that interfered successfully. (Geometry from the sim: 257 nm gratings →
  Talbot length 9.8 mm, interferometer ~20 mm, transit ~36 µs.)
- **Standard-QM blur law is settled and measured.** Gaussian phase noise gives
  `V = V₀·exp(−⟨φ²⟩/2)`; the C₇₀ thermal-emission and collisional-decoherence
  experiments (Hackermüller/Hornberger/Arndt, *Nature* 427, 711 (2004)) confirmed the
  exponential visibility loss quantitatively. This is the benchmark the framework must
  reproduce.

---

## The model

Relative phase between the two paths, with environmental noise as a stochastic kick:

```
dφ = (−γ sin2φ − ε sinφ) dt + √(2D) dW ,     V_obs = |⟨exp(iφ)⟩|
```

- **Standard QM** = γ = ε = 0 (pure dephasing) → `V_QM = exp(−σ²/2)`, σ² = 2DT.
- **Two-basin** = γ > 0 (the attractor that makes the 0/π binary); ε = polar bias.
- Noise knob = σ² = the phase variance pure dephasing *would* accumulate in transit
  (what thermal/EM noise dials up).

---

## Results (all four panels validated against analytics)

1. **Fringe channel — the laws differ ONLY if γ touches the propagating phase.**
   - QM: immediate, smooth `exp(−σ²/2)`; half-visibility at σ² = 1.39. (Langevin with
     γ=0 reproduces it, max err 0.013.)
   - Two-basin: the attractor is a restoring force toward the fringe phase, so it
     **caps** the in-well variance at `D/2γ` instead of letting it grow ~2DT →
     **PLATEAU** `V ≈ exp(−σ²/8γ)` that *protects* the fringe against weak noise,
     then a **Kramers CLIFF** near `σ² ≈ 2γ` (escape rate ~exp(−γ/D)) where
     trajectories hop to the antipodal π well and the antipodal fringes cancel.
     Measured half-drops: γ=0.5→σ²≈2, γ=2→σ²≈3, γ=8→σ²≈6 (cliff scales with γ).
   - **Plateau-then-cliff is qualitatively unlike QM's immediate decay** — a clean
     falsifiable signature *if* the measurement attractor reaches Stage-1 propagation.

2. **The honest null.** In strict MCI the attractor is a **Stage-2 (detector)**
   object: γ = 0 during flight ⟹ `V_2b ≡ V_QM` **exactly**. **The noise-blur curve
   alone cannot distinguish the two models** in the regime the framework actually
   claims. (CORRECTION to an earlier overstatement: a nonzero in-flight attractor does
   NOT kill fringes — sitting at φ=0 it *protects* them — so the existence of fringes
   does not bound γ_flight; only the V-vs-noise SHAPE does. See `experiment_spec.py`.)

3. **The spin channel is NOT an independent discriminator (refined).** A projective
   SG gives a definite ±1 in *both* theories, so when γ=0 in flight the spin readout
   is identical. The "binary sharpness" difference the sim shows only appears when
   γ_flight>0 — the *same* regime as the fringe-shape test, not a separate one. Spin's
   genuine role is the **conditional eraser-recovery** test (§Experiment below): IF a
   deviation is seen, sorting atoms by their internal pointer recovers the fringe in
   the two-basin case (info locked in the atom) but not under decoherence (info in the
   environment). That recovery needs silver's clean spin-½; the primary test does not.

4. **Strength-of-attractor map.** V(σ², γ) heatmap: the fringe survives until
   `σ² ≈ 2γ` (white dashed Kramers line) — the cliff position is a direct readout of
   the attractor strength.

---

## Verdict

- **Noise blur per se: no distinguishing prediction.** In the framework's own regime
  (γ a detector quantity) the two-basin postulate reproduces standard QM's
  `exp(−σ²/2)` exactly — consistent, not novel. Same honest status as the rest of MCI.
- **Two genuinely falsifiable handles the combined design adds:**
  (a) *bound γ_flight* — search the fringe-visibility-vs-noise curve for any
  plateau-then-cliff departure from `exp(−σ²/2)`; a null tightens the bound that the
  measurement attractor does not leak into propagation.
  (b) *the SG correlation* — measure whether fringe-contrast loss is accompanied by
  spin-binary **sharpening** (two-basin) or structureless Born statistics (QM). This
  is the test silver is uniquely suited for, via its clean spin-½ moment.
- **Still NOT addressed:** the basin *weights*. Bias ε tilts 0 vs π by a Boltzmann
  factor, not |α|² — the open Born-measure problem (`born_weights_check.py`,
  [[project_born_rule_analysis]]) is untouched here.

---

## Experiment spec (`experiment_spec.py`)

The one falsifiable fringe-channel deviation is whether the Stage-2 attractor leaks
into Stage-1 propagation: **γ_flight > 0**, parametrized by the dimensionless lock
strength `a = γ_flight · τ_transit`.

- **Primary observable — the low-noise initial slope of V(σ²).** QM: `dV/dσ²|₀ = −1/2`.
  Two-basin (confining, a≳0.25): `−1/(8a)`, shallower, plus a Kramers cliff at σ²≈2a.
  Measuring a clean −1/2 slope bounds `a`; a shallower slope detects it.
- **Statistics are cheap.** `δV ≈ √(2/N)`; resolving a slope deviation needs N ~ 10²–10⁶
  atoms. The real limit is **systematics** — calibrating the injected noise σ² and the
  baseline visibility V₀. A ~1% visibility calibration reaches `a ~ 0.25`.
- **What that bounds.** `γ_flight < 0.25/τ_transit`: Ag Talbot–Lau (τ≈36 µs) → ~7000 s⁻¹;
  a 0.5 m slow-Ag or 1 m fullerene rig (τ≈5–7 ms) → ~40–50 s⁻¹; a 1 s fountain → ~0.2 s⁻¹.
  **Existing slow-molecule interferometers already show clean exp(−σ²/2), so an in-flight
  measurement-lock faster than ~kHz is already excluded** — consistent with γ_flight=0.
- **Primary test needs no spin and no silver** — any interferometer with a calibrated
  noise knob (the fullerene thermal-photon rig is ready-made). Reanalyzing/extending
  that data for the low-σ² slope is the cheapest real test of Pillar 2.
- **Silver's spin-½ earns a unique role only in the conditional eraser-recovery
  follow-up**, and only if the primary test sees a deviation: sort atoms by internal
  pointer (SG) and check whether the fringe is **recoverable** (two-basin: V_sorted ≫
  V_unsorted, info in the atom) or **not** (decoherence: V_sorted ≈ V_unsorted, info in
  the environment). At f=0.5: V_unsorted→0 but V_sorted→0.88 for two-basin vs ~0 for
  decoherence.

**Caveat on scope:** silver's SG binary is the *electron spin* (²S_{1/2}), distinct
from the *chiral L/R channel* that the two basins come from. So this experiment tests
**Pillar 2** (measurement = dissipative synchronization / Stage-2 lock) generically,
*not* **Pillar 1** (the chiral-spinor / Zitterbewegung origin of the 2nd harmonic) —
that requires the mass-channel test in `AB_VISIBILITY_PAPER.md`.
