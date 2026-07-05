# Part II — T6 Experimental Protocol (for an invited circuit-QED group)

**Status:** 📋 **protocol draft** (2026-06-25). This is the concrete, hand-to-a-lab specification of T6 — the test of whether the Heisenberg cut is an **Adler/SNIC locking bifurcation** (framework) or a **smooth decoherence crossover** (null). Part I ([`dispute-002-partI-Keff.py`](dispute-002-partI-Keff.py)) already *derived* the prediction from the dispersive-readout master equation; Part II measures it.

> **What this test does and does not decide (read first).** Part I derived the SNIC structure *from standard open-quantum-systems theory*, so a positive result vindicates the **dynamical reframing** — "the cut is a locking bifurcation with critical universality" — **not** the framework's ontology. The genuine, falsifiable target is the bifurcation-vs-crossover question: does the measurement cut carry **critical structure** (sharp threshold, exponent ½, √-law slips, reversibility edge on the tongue) at all? Standard rigorous theory says yes; an informal "decoherence is a smooth crossover" picture says no. A **null falsifies the framework's central dynamical claim**; a positive result supplies the *new testable prediction* GPT-5.5 (Reviewer C) demanded and removes the stated reason for **reject** — see [dispute-002](dispute-002-significance.md). It does not claim to distinguish MCI from standard QM (the manuscript asserts empirical equivalence in its core).

---

## 1. Platform and device (typical, existing hardware)

A single transmon dispersively coupled to a readout resonator with near-quantum-limited continuous homodyne detection (Minev / Murch–Siddiqi / Vijay–Korotkov class setup). No new fabrication.

| Parameter | Symbol | Value (target) | Role |
|---|---|---|---|
| Qubit frequency | ω_q/2π | ~5.0 GHz | — |
| Relaxation / coherence | T₁ / T₂ᴱ | ≥ 80 / 60 µs | must give intrinsic rate ≪ K_eff |
| Resonator linewidth | κ/2π | 4.0 MHz | sets readout rate; need χ ≲ κ |
| Dispersive shift | χ/2π | 0.20 MHz | enters K_eff ∝ χ² |
| Readout photons (swept) | n̄ | 1 – 10 | **sets K_eff = 4χ²n̄/κ** |
| Rabi drive (swept) | Ω_R/2π | 0 – 0.40 MHz | **the detuning Ω in the Adler eq** |
| Measurement efficiency | η | ≥ 0.6 (TWPA/JPA) | needed only for Measurement 4 |

**Derived working point:** K_eff/2π = 4χ²n̄/κ = **0.04 n̄ MHz**. At n̄ = 4, K_eff/2π = 0.16 MHz — a factor ~10 above the intrinsic decoherence 1/T₂ ≈ 0.017 MHz (clean separation), and well inside the dispersive limit (n̄ ≪ n_crit ≈ 100). The cut sits at the **readout-power threshold n̄_crit = κΩ_R/(4χ²) = 25·(Ω_R/2π[MHz])**.

**The mapping (exact reduction from Part I).** Continuously measure σ_z (standard dispersive readout) while driving Rabi Ω_R about x. The Bloch-vector azimuth φ in the y–z plane obeys

$$\dot\phi = \Omega_R - K_{\text{eff}}\sin 2\phi,\qquad K_{\text{eff}} = \frac{4\chi^2\bar n}{\kappa},$$

with the two pointer states at φ = 0, π being |0⟩ and |1⟩. **Lock (record forms) iff Ω_R ≤ K_eff** — physically, the measurement arrests the Rabi oscillation (quantum-Zeno locking); above threshold the Rabi oscillation persists (winding). This locking transition is itself established (Korotkov; Vijay et al. 2011; Murch et al. 2013) — T6's new content is its **critical structure** (Measurements 2–4).

---

## 2. The four measurements

### Measurement 1 — the Arnold tongue (threshold)
**Goal:** map lock vs wind in the (n̄, Ω_R) plane; confirm the boundary is the straight wedge Ω_R = 4χ²n̄/κ.
**Sequence:** for each (n̄, Ω_R): turn on readout tone (→ n̄) and Rabi drive simultaneously; record the homodyne current I(t) continuously for T_acq ≈ 200 µs; compute the power spectrum S_I(ω).
**Readout:** *locked* → single Lorentzian at ω = 0; *winding* → peak at the slip frequency. The lock/wind boundary traces the tongue.
**Expected:** a wedge opening linearly in n̄, edge slope set by 4χ²/κ. (Largely a re-demonstration of persistent-Rabi/Zeno — the calibration step.)

### Measurement 2 — critical slowing, exponent ½ (the first new signature)
**Goal:** show Γ_lock = 2√(K_eff²−Ω_R²) → 0 with **exponent ½** approaching the edge from inside.
**Sequence A (spectral):** in the locked phase, sweep Ω_R toward K_eff at fixed n̄; fit the **width** of the ω = 0 peak in S_I(ω). Width = Γ_lock.
**Sequence B (time-domain):** prepare a small phase excursion (a short Rabi pulse of area δφ ≈ 0.1 rad off the pointer), then resume continuous measurement; reconstruct φ(t) by the quantum filter; fit the exponential return rate to the pointer.
**Analysis:** plot log Γ_lock vs log(K_eff − Ω_R). **Predicted slope = ½** (Part I numerics: 0.495). A smooth-crossover null gives no diverging timescale and no ½ law.

### Measurement 3 — sub-threshold slip frequency, √-law (the second new signature)
**Goal:** show the winding peak position obeys ⟨φ̇⟩ = √(Ω_R²−K_eff²).
**Sequence:** just above threshold (Ω_R = 1.02–1.6 K_eff), record I(t); locate the spectral peak ω_slip.
**Analysis:** plot ω_slip vs √(Ω_R²−K_eff²) — predicted **slope 1, intercept 0** (Part I numerics: ratio 1.000), and ω_slip → 0 as √ at the edge. A null gives a peak that does not vanish, or vanishes with the wrong power.

### Measurement 4 — catch-and-reverse edge on the tongue (the decisive signature)
**Goal:** test the framework's central claim — that the **reversibility boundary coincides with the locking bifurcation** and inherits its ½ critical slowing.
**Sequence (Minev catch-and-reverse, swept through the tongue):**
1. Initialize |0⟩; start continuous monitoring at photon number n̄, with Rabi Ω_R fixed.
2. **Catch:** when the filtered record indicates a phase excursion of preset size (a partial "jump" toward the other pointer), trigger.
3. **Reverse:** apply the calibrated reversal pulse (the unitary that undoes the caught excursion).
4. **Verify:** strong projective readout; score reversal fidelity F.
5. Repeat ~10⁴ shots per setting; **sweep n̄** (→ K_eff) at fixed Ω_R across n̄_crit = κΩ_R/(4χ²).
**Predicted (framework):** F stays high for n̄ < n̄_crit (below the lock: excursions are recoverable), then **collapses at n̄ = n̄_crit**, with the collapse *width* set by the ½-critical-slowing of Measurement 2 — i.e. the reversibility edge sits **on the Arnold tongue**, not at an unrelated power.
**Predicted (null):** F degrades **smoothly and monotonically** with n̄ (more measurement → more irreversible backaction), with **no feature at n̄_crit** and no ½-law.
Requires high η (so individual trajectories are faithfully tracked).

---

## 3. Discrimination table

| Observation | Verdict |
|---|---|
| Sharp tongue **and** Γ_lock ∝ (K_eff−Ω_R)^½ **and** ω_slip = √(Ω_R²−K_eff²) **and** catch-and-reverse edge on the tongue | **Framework's dynamical claim confirmed.** Cut = SNIC bifurcation. GPT-5.5's "no testable content" reason removed → dispute-002 → *major revision*. |
| Smooth crossover; reversal fidelity ∝ n̄ with **no** tongue/½-law/coincidence | **Framework's core dynamical claim FALSIFIED.** dispute-002 → *reject on the merits*. |
| Tongue present but wrong exponent, or reversibility edge **off** the tongue | Diagnostic; revise the system–bath model (Part I domain of validity) and re-enter the loop. |

---

## 4. Systematics and controls

- **Calibrate χ, κ, n̄ independently** (qubit-spectroscopy AC-Stark shift → χn̄; ring-down → κ) so K_eff = 4χ²n̄/κ is a *predicted* number, not a fit. The tongue edge must land at the **independently predicted** n̄_crit — that is the non-trivial check.
- **Intrinsic decoherence floor.** Keep K_eff ≥ 10/T₂ so the locking dynamics dominates; subtract the T₁/T₂ contribution measured at n̄ = 0.
- **Dispersive validity.** Hold n̄ < n_crit and verify no measurement-induced state transitions (monitor leakage to |2⟩).
- **Distinguish from trivial Zeno.** The Zeno *freezing* (lock) alone is expected; the **critical exponents** (½ slowing, √ slips) and the **edge coincidence** are what discriminate bifurcation from crossover — report those, not just lock/no-lock.
- **Efficiency budget for M4.** Report η; low η blurs the catch-and-reverse edge symmetrically and must be deconvolved.

---

## 5. Resource estimate

All on one existing continuous-measurement setup: Measurements 1–3 are spectra over a 2-D (n̄, Ω_R) grid (~few hundred settings × 200 µs × averaging ≈ **1–2 device-days**). Measurement 4 (catch-and-reverse sweep, 10⁴ shots × ~30 settings) ≈ **1–2 device-days**. Total ~**1 device-week**, no new hardware.

---

## 6. How it closes the loop

- **Positive (SNIC confirmed):** retires the [dispute-002](dispute-002-significance.md) standing dissent — GPT-5.5's stated reject criterion ("no new testable prediction") is met; combined with Part I (derivation done), the locking-threshold idea is now a *derived, falsifiable, hardware-ready* prediction.
- **Null (crossover):** falsifies the framework's central claim that measurement *is* a dissipative locking transition — the strongest possible service the journal can render.
- Routed to the **invited experimentalist** (Pillar III). A continuous-measurement circuit-QED group ("invite the Aspects to test the Bells") is the natural lab; this file is the commit-ready protocol.

---

*Drafted by Claude Opus 4.8 (Anthropic), 2026-06-25, as the Part II protocol for T6. Builds on the Part I derivation ([`dispute-002-partI-Keff.py`](dispute-002-partI-Keff.py)) and standard continuous-measurement circuit-QED technique (Korotkov; Vijay et al. 2011; Murch et al. 2013; Minev et al. 2019 [14]). A proposal for an invited lab — independent scrutiny of the protocol is invited; nothing here is a result.*
