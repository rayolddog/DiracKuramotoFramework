---
title: "Claude corrections — cross-review record"
kind: spec
---

# Claude corrections — cross-review record (Round 2)

All four independent reports and the [concept index](../../concept-index) read. Direct exchanges below, one issue per message, in order. Views that changed are marked explicitly on both sides. No manuscript files touched.

## LC-3 — passivity versus κ_ret (with GPT correction architect)

**Asked:** can "no inversion ⇒ linear response ⇒ concave uptake ⇒ no winner amplification" replace the κ_ret = ΔE/ħ ansatz as Theorem 2's premise, and what is the minimal verifying calculation?

**Answer received:** partial acceptance with a correct counterargument — passivity forbids net energy creation but not time-integrated bias through phase–energy correlations, common-field memory, or collective/subradiant modes; the instantaneous uptake exponent p ≤ 1 is insufficient unless phase statistics are state-independent at the filtration level and no cross-site memory term survives.

**Joint statement (agreed verbatim, both artifacts):** *"κ_ret = ΔE/ħ is unnecessary for fairness if a microscopic reduction establishes a passive, gainless effective exchange whose conditional site flux is non-amplifying and whose residual phase/correlation terms give zero (or bounded) share drift; κ_ret then governs only timescales."*

**Views changed:** GPT moved from `abandons subclaim` (their BS-C3) to conditional preservation; I moved from "passivity suffices" to "passivity conditioned on filtration-level phase-randomness and no cross-site memory." Net effect on the ledger: Theorem 2 becomes `narrows` (U4) with a defined verification path, rather than abandoned.

**Verification (agreed):** the closed **two-site + common mode + bath** model — eliminate the common mode, obtain the effective share generator, and bound E[ds₁|F_t] analytically in coupling, detuning, and bath memory time. One-site poles cannot reveal shared-field competitive bias.

## LC-6 — experiment and systematics repairs (with GPT critical reviewer)

**Asked:** a shared ranking of the §8.4 discriminator (after my CC-3 efficiency-mimic finding), §8.7 Knob 1, and Knob 2, with decisive error-budget items.

**Answer received and accepted — my view changed on two points:** (1) my port-swap repair (CC-3 ii) is insufficient alone, because κ and the efficiency mismatch δ ride the same physical port under a swap. (2) The polarization-sign rotation of §8.6(iii) is a supporting fingerprint only — anisotropic collective optics can rotate too.

**Joint LC-6 position:**

- **First: redesigned §8.4** — modulate the collective correlation *in situ* with optics and readout held fixed, plus role reversal and unconditional-rate monitoring. Robust observable: the **modulation-odd component** of the port statistic, with simultaneous conventional-POVM tomography bounding the modulation-induced ordinary-efficiency change below the target κ (the decisive budget item).
- **Second: §8.7 Knob 1** as a model-conditional registry stress test — injection on/off and ρ-scaling establish a causal anomaly, but reading δS as (1−η) remains model-dependent. Decisive budget: injection-dependent accidentals and visibility (time-shifted windows, blocked/uncorrelated injection, separable-state controls, unchanged singles, total coincidence rates).
- **Third: Knob 2** (phase-locked tone, above-Tsirelson) stays gated on the multi-quantum derivation — unanimous across all four reports.

## LC-4 — Born-free registration scope (asked of me by both GPT agents)

**GPT critical's pressure test:** does the classical-dissipation repair (rate Γe) avoid the Born rule if e is only an excitation expectation, or does the circularity move into the definition of e? **My answer, now shared:** it moves into the definition. The repair is Born-free *only conditional on P0's ontic reading*; if e_i is a quantum expectation, its definition invokes the trace rule, Born-equivalent by Gleason. Consequence: **LC-2 (what the stakes are) is the load-bearing wall for the entire single-detector sector**, not a separate finding.

**GPT corrections' pressure test:** does passive power loss justify a *global one-click hazard*, and what routes E₀ − e_i to the winner? **My answer:** passive dissipation derives only the mean flux; the point-process structure requires three flagged, detector-checkable, non-probabilistic premises — (R1) the readout stage is classically metastable/excitable, so escapes are pointlike (Kramers, no quantum jumps); (R2) the hazard is linear in the flux only in a stated linear-response window ("linear counter" premise — Kramers rates are generically exponential); (R3) post-commit, the open channel is the unique resonant final state and the residue drains at the exchange rate. Exclusivity is then a theorem **up to a computable double-click floor ~ ΓE₀τ_drain** (10⁻²–10⁻⁵ on §6.1's ladder) — a falsifiable prediction, flagged as a feature.

**Narrowest theorem (endorsed by both chairs):** *"Under conserving martingale exchange plus R1–R3, exactly one site registers with probability 1 − O(ΓE₀τ_drain), the winner absorbs E₀, and P_i = e_i(0)/E₀, at every Γ; premises P0/P1 carry all ontological content."* G^(k) linearity, Glauber, and ρ-affinity: conjectures conditional on ontic joint stakes plus a Born-free k-channel rate law; presently consistency conditions.

## LC-1 — canonical conserving model (asked of me by GPT corrections)

**My proposal, accepted as the shared canonical model:** pairwise interference exchange de_i = Σ_j σ√(e_i e_j) dW_ij, dW_ji = −dW_ij. With E fixed, the shares have covariance σ²s_i(δ_ij − s_j) — **exactly the neutral multi-allele Wright–Fisher diffusion**: fixation is a.s. in finite time for finite N, and the fixation probability equals the initial share (Kimura). Born weights = neutral-drift fixation probabilities. Uniqueness relocates: *conservation buys fairness (generic for antisymmetric zero-mean exchange); amplitude-linearity buys termination* (vertices attainable iff the exchange exponent p < 1); the manuscript's √e uniqueness proof survives as a robustness statement about non-conserving bath noise.

**GPT's boundary correction — accepted, my view changed:** coherent hopping (a_i†a_j + h.c.) repopulates an empty site (da_i ∝ a_j; vacuum re-entry via the n_i+1 factor), so the vanishing of the noise coefficient at zero is **not** a consequence of P2. The shared model therefore carries an explicit **dropout premise**: a depleted site decouples irreversibly (detunes, dephases, or is spectrally removed) on the game timescale — pending a detector spectral/bath derivation. Mitigation: dropout is load-bearing only for class-(i) absorbers (fixation-defined registration); class (ii) is stopped by the global hazard, where optional stopping needs no vertex absorption. The conserving theorem covers class (ii) most cleanly today.

## LC-7 — Dirac-spinor bridge (asked of me by GPT corrections)

**My recommendation:** first target the **two-site conserving kernel**, not a one-site susceptibility (any oscillator gives a Lorentzian) or a jump map (presupposes missing machinery). Input: two localized Dirac absorbers (start 1+1D) + quantized common field, minimal coupling. Output: derived g(e_i,e_j), drift, and C_ij. Discriminator a scalar-oscillator model cannot supply: whether the βmc² chirality coupling (the author's coupled clocks, U2/U3) appears at leading order as a rest-mass- and helicity-dependent term in the kernel. An honest negative — spinor calculation reproduces the scalar kernel — would leave U2/U3 as compatible background for Paper 1, and the synthesis should leave that outcome open.

## Convergence note

Four exchange lines independently landed on the **same keystone calculation**: the closed two-site (extendable to three-site/two-quanta) conserving kernel with common mode + bath. It would simultaneously (i) derive or refute the canonical Wright–Fisher exchange and the dropout premise (LC-1), (ii) produce the LC-3 drift bound, (iii) ground the R1–R3 registration premises' domain (LC-4), and (iv) answer the Dirac-bridge discriminator (LC-7).
