# Microstate contract — G1 (ontology) and G2 (preparation measure)

*Proposed closure of gates G1 and G2 of the [quantum-equilibrium selection revision](../traycer_artifacts/debates/born-selection-roundtable/quantum-equilibrium-selection-revision/index.md). Status: **drafted, not independently reviewed**. Readiness condition 9 of the revision plan requires independent agreement before either gate is recorded as closed; until then the terminal statuses `microstate_ontology_undefined` and `microstate_measure_undefined` remain the record.*

---

## 0. Scope and result

This document closes G1 and G2 **for the single-quantum, single-detector sector only** — one incident quantum, one detector containing `N` candidate absorber sites, no entangled partner, no joint registry. Multi-quantum (P5) and multi-partite (P6) sectors are explicitly out of scope and their gates stay open.

The result in one line: **the system factor of the microstate measure is a Dirac delta, not a distribution.** Under wave realism there is no probability law over hidden system variables, so there is nothing on the propagation side for a Born weight to hide in. All microstate randomness is detector-side, and it is the Gibbs/ground-state measure of the detector's own material Hamiltonian — an object with independent provenance that is the same for every incident state.

Two consequences worth stating up front, because they change the paper:

1. **"Quantum equilibrium" is the wrong name for this sector.** The Dürr–Goldstein–Zanghì object is a probability measure over hidden configurations of the *propagating* system. This contract has no such measure. What it has is a *detector ready-state equilibrium*. The phrase should be retired from Paper 1's system-side language and used only where it belongs, in the comparison with Bohmian mechanics.
2. **P3(a) and P3(b) stop being premises.** Both follow from the ready-state measure (§3). Paper 1's premise count drops from six to four in the single-detector sector.

---

## 1. G1 — the ontology

### 1.1 The choice, and why the other candidates are not it

The revision plan lists four candidate ingredients and forbids treating them as interchangeable. The choice here is **ingredient 4 (a joint preparation measure) built on ingredients 2 and 3, with ingredient 1 explicitly rejected.**

Ingredient 1 — Bohm-like configuration equilibrium — is rejected on grounds that are decisive rather than aesthetic. Setting `mu_sys(dx | Psi) = |Psi(x)|^2 dx` installs the Born measure as the preparation law. A selector that then registers at or near the beable position reproduces Born by construction, and the paper's central claim becomes vacuous. This is exactly finding 1 of the independent pressure test — "`mu_eq` can still contain the answer" — in its sharpest form. It is also inconsistent with P0, which is already Paper 1's stated ontological commitment: the incident quantum is *a real distributed field configuration, not a probability amplitude over mutually exclusive absorbers*. A framework cannot assert P0 and then place a probability measure over particle positions in the same sector.

**Name of the ontology: the single-quantum wave-realist field–matter ontology, written `Lambda_1`.** Neutral label per the review's finding 6: this is a *field–matter selector* ontology. It does not presuppose an autonomous oscillator, an Arnold tongue, or a Kuramoto reduction; whether Dirac spinor structure is load-bearing is a G3/G4 question, not settled here.

### 1.2 The probability space

`Lambda_1 = Lambda_field x Lambda_mat x Lambda_bath`, with `Sigma_Lambda` the product Borel sigma-algebra (each factor is a separable Banach or finite-dimensional real space, so the product is standard Borel and conditional measures are well defined).

| Factor | Contents | Space |
| --- | --- | --- |
| `Lambda_field` | the incident real field/spinor configuration: mode function `f`, carrier frequency, polarization, propagation vector, total energy `hbar omega` | real-valued classical field configurations on the detector region, `L^2` with the material's bandwidth cutoff |
| `Lambda_mat` | per site `i = 1..N`: sensitizer/absorber coordinates `q_i` and conjugate momenta `p_i`; site position `x_i`; dipole orientation `n_i`; static detuning `delta_i` | `R^{2n_q N} x (R^3 x S^2 x R)^N` |
| `Lambda_bath` | bath coordinates and the complete noise history `xi(t)` over the event window `[0, T_evt]` | Wiener space `C_0([0,T_evt], R^{N_b})` |

The event window `T_evt` is a declared model constant, frozen with the manifest.

### 1.3 Ontic status of every component

G1 requires this table; it is the substance of the gate.

| Component | Ontic status | Note |
| --- | --- | --- |
| Field configuration `f` | **Ontic, deterministic given `Psi`** | This is P0. The beable is the mode function itself, carrying total energy `hbar omega`. Contested premise, declared not derived. |
| Site coordinates `q_i, p_i` | **Ontic, random** | Real material degrees of freedom of the passive polarization model. |
| Site positions `x_i`, orientations `n_i` | **Ontic, random, frozen per detector** | Drawn once from material structure, then fixed for the device. |
| Static detunings `delta_i` | **Ontic, random, frozen per detector** | Inhomogeneous broadening. |
| Bath coordinates, noise history `xi(t)` | **Ontic, random** | Included in `lambda` in full — see §1.5 on selector semantics. |
| Capture energies `e_i(0)` | **Derived, not a component** | `e_i(0) = kappa |f(x_i)|^2` is a *function on* `Lambda_1`, computed from `f` and `x_i`. It is not sampled and carries no independent measure. |
| Registry / winner label | **Not a component. Absent by construction.** | See §1.4. |

### 1.4 What is deliberately absent

The review's finding 3 identified a fork: a registry beable that is already single-valued does the actuality work, and Kuramoto locking is then decorative. This ontology takes the other branch and pays its cost openly.

- **No hidden particle position.** There is no configuration beable in the propagating sector.
- **No separate registry beable.** The material record *is* the record — a trapped charge, a reduced cluster, an avalanche. "Registration" is a change in `Lambda_mat`, not an update to an extra variable.
- **No pre-actual winner label.** Nothing in `Lambda_1` names an outcome. This is machine-checkable: no field of `Lambda_1` has the outcome index as its type.
- **No autonomous oscillator is assumed.** Consistent with the silver-halide material audit, which found no powered or self-sustained oscillatory degree of freedom. The ready state below is that of a *passive* driven system.

The cost of this branch: **exclusivity is now a debt owed by the dynamics, not by the ontology.** Nothing above forbids two sites registering. Only energy conservation plus a physical quench can do that, and demonstrating it pathwise is G3. G1 closing does not discharge that debt; it makes it explicit.

### 1.5 Selector semantics

The revision plan requires each version to freeze exactly one `selector_semantics` value. This contract freezes:

```text
selector_semantics = deterministic_with_complete_noise_history
```

The noise history `xi(t)` is a component of `lambda`, so the selector `F` is deterministic conditional on `lambda`. The stochastic-kernel description `K` is not available in this version and no conversion between the two is permitted after freeze.

---

## 2. G2 — the preparation measure

### 2.1 The factorization

```text
mu_micro(dlambda | Psi, M, H)
  = delta_{f[Psi]}(dlambda_field)  ⊗  nu_ready(dlambda_mat, dlambda_bath | M, H)
```

with **`C ≡ 1`** — no cross-correlation term.

The independence is a physical claim, not a convenience, and it is the one place a reviewer should push hardest. Justification: the source and the detector are prepared by separate procedures that share no common cause within the event's past light cone after the detector's last thermalization. The detector's ready state is set by its own bath on the material relaxation timescale (`~ 1/Gamma_loc ~ 10^-13`–`10^-14 s`); the incident field is prepared upstream and independently. Any `C != 1` would require a physical mechanism coupling them before arrival, and none is proposed. **This is falsifiable:** a pre-illumination correlation between site phase and incident field phase is exactly the "engineered coherence" that P3(a) denies and that §8 of Paper 1 already proposes to test.

### 2.2 The system factor is degenerate

```text
mu_sys(dlambda_field | Psi) = delta_{f[Psi]}
```

`f[Psi]` is the one-quantum mode function named by `Psi`. The map `Psi -> f` is the identity in content, not a modelling choice with free parameters: there is no distribution, no width, no fitted correlation, nothing to tune per state.

This is the anti-circularity result. Finding 1 of the pressure test was that "a different conditional `mu_eq(. | Psi)` can be chosen for every `Psi`, or its correlations can be chosen after `F_DK` is known, so that the desired outcome partitions receive the desired masses." A Dirac measure has no such freedom. There is no per-`Psi` tuning surface because there are no parameters.

### 2.3 The ready factor, in two sectors

`nu_ready` is the invariant measure of the detector's own material Hamiltonian, per Gate E of the silver-halide authority packet ("each continuous and discrete subsystem declares its invariant measure"). It splits by the ratio `hbar Omega / k_B T`, and the split is not a modelling choice — it is where the physics changes.

**Optical-electronic sector (`hbar omega >> k_B T`).** For the passive polarization model `H_pol(q,p;0) = ½ p^T M^-1 p + ½ q^T K q`, the thermal occupation at optical frequency is numerically zero:

| `T` | `lambda` | `hbar omega` | `k_B T` | `hbar omega / k_B T` | `n_thermal` |
| --- | --- | --- | --- | --- | --- |
| 300 K | 500 nm | 2.480 eV | 25.85 meV | 95.9 | 2.2e-42 |
| 300 K | 600 nm | 2.066 eV | 25.85 meV | 79.9 | 1.9e-35 |
| 300 K | 1550 nm | 0.800 eV | 25.85 meV | 30.9 | 3.7e-14 |
| 77 K | 600 nm | 2.066 eV | 6.64 meV | 311.4 | 5.6e-136 |

The ready state is therefore the **ground state**, not a thermal state. Its microstate law is the ground-state Wigner distribution, which for this quadratic Hamiltonian is a zero-mean Gaussian on `(q, p)` — and, critically, **non-negative**, so it is a legitimate probability measure over beables rather than a quasi-distribution requiring interpretation. In normal-mode coordinates `a = 1..n_q N` with frequencies `Omega_a`:

```text
nu_ready^opt(dq, dp) = prod_a  (1 / pi hbar) exp[ -(Omega_a q_a^2 + p_a^2 / Omega_a) / hbar ]  dq_a dp_a
```

The non-negativity is a property of Gaussian states only. **Declared support limit:** this contract does not cover squeezed, number-state, or otherwise non-Gaussian detector preparations, where the Wigner function goes negative and no microstate law of this form exists. A detector deliberately prepared in such a state falls outside the frozen domain.

**Low-frequency material sector (`hbar Omega << k_B T`).** Phonon, ion-motion, and trap coordinates are genuinely thermal, and Gate E's underdamped Langevin form

```text
dq = M^-1 p dt,   dp = -grad U dt - Gamma M^-1 p dt + sqrt(2 k_B T Gamma) dW
```

has the Gibbs measure as its unique invariant law:

```text
nu_ready^therm(dq, dp)  ∝  exp[ -beta ( ½ p^T M^-1 p + ½ q^T K q ) ] dq dp
                        =  N(0, k_B T · M) in p   ⊗   N(0, k_B T · K^-1) in q
```

**Structural sector.** Site positions, orientations, and static detunings are drawn once per device from the measured material structure — site density and the measured inhomogeneous lineshape respectively — and then frozen. They are part of the device, not resampled per event.

Note that this two-sector split reproduces Paper 1's own fairness window `hbar omega >> k_B T` (§4) from the preparation side. That is a consistency check, not an independent confirmation.

### 2.4 Normalization and support

Each factor is a normalized probability measure on its own space: Dirac measure (mass 1 by definition); a product of normalized Gaussians; a Gibbs measure with `Z < infinity` because `M` and `K` are positive definite; Wiener measure on the event window. The product of normalized measures on a countable product of standard Borel spaces is normalized. Support: `Lambda_field` support is the single point `f[Psi]`; the Gaussian factors have full support on their respective `R^k`; structural factors have support on the measured material ranges declared in the manifest.

### 2.5 Provenance

Every factor traces to an observable measured **without reference to outcome frequencies** — the review's finding 5, requirement 1.

| Factor | Parameters | Independent source | Outcome-free? |
| --- | --- | --- | --- |
| `delta_{f[Psi]}` | none | the prepared state itself; beam calibration converts measured irradiance to real field amplitude | yes — no free parameters exist |
| `nu_ready^opt` | `M`, `K` (hence `Omega_a`) | absorption/emission spectra, oscillator strengths, refractive index — Gate A material functional | yes |
| `nu_ready^therm` | `M`, `K`, `Gamma`, `T` | measured linewidths, phonon spectra, mobilities; thermometry | yes |
| noise covariance | fixed by `Gamma` via FDT | **not free** — see §3.2 | yes |
| structural | site density, `rho_inhom(delta)` | crystallography, measured inhomogeneous lineshape | yes |

No entry depends on `F`, on `Pi_M`, on outcome data, or on comparator residuals.

### 2.6 State-dependence audit

The revision plan requires that any `Psi`-dependence be justified without using `F`, `Pi_M`, outcome data, or comparator residuals, and that the detector ready-state distribution be shared across all permitted states.

**Audit result: `nu_ready` is independent of `Psi` by construction.** It is the invariant measure of the detector Hamiltonian with the field absent. `Psi` enters `mu_micro` only through `delta_{f[Psi]}`, and there only as the identity.

This yields a **machine-checkable test** that should go in the dependency manifest and be run for every state in the blinded holdout suite:

```text
assert hash(nu_ready_params(Psi_k)) == hash(nu_ready_params(Psi_0))   for all k
```

One hash, all states. Any per-state drift in a ready-state parameter is a hard failure, not a tolerance. This converts the pressure test's prose prohibition into an enforceable check — the gap the review flagged as finding 4 ("the forbidden-input list is good but prose-only").

---

## 3. Two of Paper 1's premises become theorems

### 3.1 P3(a) — mutual incoherence

P3(a) currently asserts that site phases are initially mutually incoherent. Under `nu_ready` this is derived. Writing each normal mode in amplitude–phase variables `(x, y) = (p_a, Omega_a q_a)`, both the ground-state Wigner measure and the Gibbs measure are **isotropic** zero-mean Gaussians in `(x, y)`. An isotropic 2-D Gaussian is invariant under rotation of `(x, y)`, so the phase `phi_a = atan2(y, x)` is **uniform on `[0, 2pi)` and independent of the amplitude**, which is Rayleigh. Independence across modes follows from the product form.

So mutual incoherence is not an extra assumption about detectors; it is the `U(1)` invariance of a passive system's ready state. Engineering coherence *into* the detector means preparing it away from its invariant measure — which is precisely Phase III's nonequilibrium challenge, now with a sharp definition of what "away from equilibrium" means.

### 3.2 P3(b) — noise locality

P3(b) currently assumes the site-noise correlation matrix satisfies `C ≈ 1`, with the correlated fraction `f = Gamma_rad / Gamma_tot << 1`. Under the fluctuation–dissipation theorem the noise covariance is not an independent object: Gate E's `sqrt(2 k_B T Gamma) dW` ties it to the damping matrix `Gamma` (and at optical frequency to the quantum FDT, noise spectral density `∝ Gamma(omega) coth(beta hbar omega / 2) -> Gamma(omega)` as the vacuum limit). Therefore

```text
C ∝ Gamma,   and   C = 1 + O( max( f, exp(-d / ell) ) )
```

with `f = Gamma_rad / Gamma_tot`, `d` the site spacing and `ell` the local scattering correlation length. Paper 1's current statement `C = 1 + O(f)` is the `f`-dominated branch and is not always the binding one: when `f` is very small the residual off-diagonal correlation is set by the *local* correlation tail `exp(-d/ell)`, not by the radiative fraction. Numerically, for `d = 20 nm`, `ell = 2 nm`: at `f = 1e-3` and `1e-1` the residual tracks `f` exactly (ratio 1.00), but at `f = 1e-6` the residual is `4.6e-5` — some 46x larger than `f`, because the nearest-neighbour term `exp(-d/ell) = 4.5e-5` dominates. Paper 1 quotes `f ~ 1e-6`, so this detector sits in the branch where the local tail, not the radiative fraction, sets the correlation floor. **This should be corrected in §2/P3(b) of the manuscript**; it does not weaken the premise (both terms are tiny) but the stated scaling is wrong in the regime the paper actually claims.

`Gamma` is measured from linewidths. **The noise correlation is not a free parameter and cannot be tuned.** This closes one of the specific re-entry routes the review listed under finding 4 ("initial relative-phase, detuning, or bath correlations").

**A condition this exposes.** Because the binding term is `exp(-d/ell)` rather than `f`, P3(b) carries a geometric requirement that was not previously stated: `d >> ell`. Paper 1 quotes local correlation lengths "of nanometres". If the absorber array is dense enough that site spacing `d` is comparable to `ell`, the nearest-neighbour noise correlation is `O(1)` and clause (b) fails outright — Theorem 3's correlation penalty would then be doing real work rather than being negligible. This is a per-detector check that has not been performed for any of the detector families the manuscript discusses, and it is now flagged in the manuscript as an open item.

Both derivations are conditional on the passive-model Hamiltonian being the right material functional — Gate A of the silver-halide packet, still open. They are exact given that functional.

**Verification.** Both results in this section were checked numerically in `code/check_g1g2_ready_state.py` on a 6-site system with non-diagonal `M` and `K`: the modal covariances come out at `kT` to 0.4%, modal phase is uniform (worst max-bin deviation 0.024 against a Monte-Carlo scale of 0.008 over 144 bins, i.e. ~3 sigma as expected for a maximum statistic), phase–amplitude correlation is consistent with zero (|corr| < 0.004), and the `C` scaling is as stated above.

---

## 4. Residual circularity: where Born can still enter

Honest accounting. Having removed the system-side measure, the risk does not vanish; it concentrates.

**It concentrates entirely in P0 + P1.** The claim that `e_i(0) = kappa |f(x_i)|^2` are *simultaneously physically possessed* event-level energies is the whole ontological cost of the program. The review states the objection precisely: "Standard quantum theory's local quadratic quantities may be expectations or transition weights rather than simultaneously possessed event-level energy shares."

This contract does not answer that objection and should not pretend to. What it does is **isolate** it. After G1/G2 as written, there is exactly one place a Born weight can enter the raw path, it is a declared premise rather than a fitted measure, it is stated in the abstract, and it is the target of a specific experimental family. That is a materially better position than a `Psi`-conditioned microstate law, where the same weight could enter through any of five tunable surfaces and be invisible in the code.

Remaining lesser routes, all now manifest-checkable rather than prose-prohibited: the event window `T_evt`; the bandwidth cutoff defining `Lambda_field`; the invalid-event and no-click classification. Each is a frozen model constant with a manifest entry and must be fixed before comparator access.

---

## 5. What this does not close

- **G3 (physical selector).** Untouched. Exclusivity, quench, commitment current, and energy routing are all still owed, and §1.4 makes the debt larger by refusing a registry beable.
- **G4 (material authority).** Gate A (exact material functional) and Gate B (electronic-transfer authority) of the silver-halide packet remain open. §3's derivations are conditional on Gate A.
- **Multi-quantum and entangled sectors.** P5 and P6 need a joint registry with its own ontic status. Out of scope here; `microstate_ontology_undefined` still stands for those sectors.
- **Non-Gaussian detector ready states.** Outside the declared support (§2.3).
- **Whether Dirac structure is load-bearing.** `Lambda_1` is stated for a general field–matter system. Nothing here identifies a spinor bilinear whose removal changes the prediction — the review's finding 6 test. Neutral labels stay.
- **Independent review.** Readiness condition 9. Until an independent pass agrees, both gates are formally open.

---

## 6. Manifest entries

For the dependency contract, in canonical order: `selector_semantics`; `T_evt`; `bandwidth_cutoff`; `N_sites`; `site_density`; `rho_inhom`; `M`; `K`; `Gamma`; `T`; `f_rad_fraction`; `nu_ready_sector_boundary`; `kappa`; `invalid_event_policy`; `noclick_policy`.

Every entry carries: canonical name, units, allowed range, uncertainty, source artifact, allowed `Psi`-dependence (**`none` for all entries above except `f[Psi]`**), fix date, model version, pre-comparator confirmation, and downstream raw fields influenced.

---

## 7. Proposed gate status

| Gate | Proposed | Basis | Blocker to formal closure |
| --- | --- | --- | --- |
| **G1 — ontology** | **closes** | `(Lambda_1, Sigma_Lambda)` declared; ontic status given for every component; absences explicit and type-checkable; sector scope bounded | independent review only |
| **G2 — preparation measure** | **closes structurally; provenance populated by named source, not yet by measured value** | normalized factorization with `C ≡ 1` justified; support declared; state-dependence audit passes with an enforceable hash test | independent review; and numeric provenance for one named material, which depends on Gate A |

Recommended record until review: **G1 proposed-closed; G2 proposed-closed-pending-material-provenance.** The revision plan's overall status is otherwise unchanged — physical selector not demonstrated, conditional compatibility not testable, no equivariance result, no Born derivation.
