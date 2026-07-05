# Dispute-002 Retirement Path — The Locking-Threshold Test

**Status:** 🟢 **Part I executed** (2026-06-25) — K_eff is now *derived* from the transmon+readout model, with all three SNIC signatures validated numerically ([`dispute-002-partI-Keff.py`](dispute-002-partI-Keff.py), [figure](dispute-002-partI-Keff.png)). Part II (the experiment) remains an open call (T6). This discharges the "Adler asserted, not derived" half; the prediction is now grounded. **(Reconciled 2026-06-30 with the second-revision Appendix D — see the note below: K_eff and the cut location stand and now sit *in* the manuscript; outcome-registration moves to the conditional σ_z trajectory; the SNIC exponents are T6's *prediction*, no longer banked as a manuscript claim.)**

---

## ⓘ Reconciliation with the second-revision Appendix D (2026-06-30)

Appendix D was rewritten on 2026-06-30 (route (a); [`../manuscript-second-revision-06-30-2026.md`](../03-current-revision/manuscript-second-revision-06-30-2026.md)). This spec is **rescoped, not retracted**:

- **Stands, and is now *in* the manuscript:** the derived **K_eff = 4χ²n̄/κ** and the cut location **n̄_crit = κ\|Ω\|/(4χ²)** (i.e. \|Ω\| = K_eff). Part I's central result is consistent with the rewrite; the Adler phase reduction φ̇ = Ω − K_eff sin2φ remains valid where the transverse radius r ≠ 0. The discharge of dispute-001's "Adler asserted, not derived" holds.
- **Rescoped — "locking = record formation":** the second-revision Appendix D withdraws the reading that the *unconditional* Adler lock is the measurement outcome (an unconditional master equation gives decoherence, not an outcome). Outcome-registration now runs through the **conditional (monitored) σ_z trajectory + amplification above the vacuum noise**. So \|Ω\| ≤ K_eff is the **phase-locking / cut-location** condition; a definite *record* additionally requires the conditional monitoring. T6 still tests whether the reversibility boundary sits at that locking edge — the narrow new empirical content this spec already isolated (§Honest limitations).
- **Pointer basis:** the faithful, outcome-registering measurement is **QND on σ_z** (the einselected pointer), not the σ_x interference channel Part I fits. K_eff's *magnitude is basis-independent* (Part I's own caveat), so the derivation carries over — and the Part II protocol already specifies **continuous σ_z readout**, so it is already aligned with the second-revision Appendix D.
- **The SNIC exponents (½, √-law slips):** the second-revision Appendix D **no longer banks** these as established (it reframes the cut as an amplification/SNR threshold and explicitly declines to re-assert specific exponents — consistent with GPT-5.5's round-2 note that the critical behavior was not independently reproduced). They remain the **falsifiable prediction T6 tests**. This *strengthens* the honesty: the exponents move from "confirmed" to "predicted, to-be-tested" — exactly the *new testable prediction* the dispute-002 lever needs.

**Net:** Part I's K_eff derivation and T6 as a falsifiable core-mechanism test both stand; outcome-registration is now the conditional-trajectory story (Appendix D, 2nd rev), and the SNIC exponents are T6's prediction rather than a manuscript claim. The conditional-trajectory companion to `dispute-002-partI-Keff.py` is the new [`precession_radius_two_zeros.py`](precession_radius_two_zeros.py).

---

## Why this retires the dissent

[Dispute-002](dispute-002-significance.md) narrowed the major-revision-vs-reject split to **one** irreducible criterion: GPT-5.5 (Reviewer C) requires a contribution to supply *a new mechanism or a new testable prediction*; Fable 5 and Gemini already judge the honest synthesis publishable for a foundations venue. Dispute-002 logged a single lever that could cross **even GPT-5.5's stricter bar**:

> develop the manuscript's one in-principle-falsifiable idea — **the Heisenberg cut as a measurable locking threshold** — into a concrete, falsifiable prediction.

This document is that development. It is deliberately structured to discharge **two** open items at once:

1. **dispute-002** (significance): supply the *new testable prediction* GPT-5.5's standard demands.
2. **dispute-001 / GPT-5.5 Major Concern #1** (the Adler equation is *asserted, not derived*): the prediction is *derived from* a concrete system–bath model, so the same work that produces the prediction closes the "phenomenological insertion" gap.

If both parts succeed, GPT-5.5's stated reason for **reject** is removed and the standing dissent converges to **major revision**. If the experiment returns the **null**, the framework's central dynamical claim is **falsified** — also a resolution, and the strongest outcome an honest journal can produce.

---

## The claim being made falsifiable

The framework's distinctive dynamical assertion (§3.5–3.6) is that the **record/no-record boundary — the Heisenberg cut — is not a smooth decoherence crossover but an Adler/Kuramoto *locking bifurcation*.** Standard open-system theory and the synchronization reading make **different, measurable** predictions about *how* the cut is approached. That difference is the test.

The minimal dynamics is the first-harmonic Adler equation for the system–pointer relative phase φ:

$$\dot\phi = \Delta\omega - K_{\text{eff}}\sin\phi,$$

where Δω is the system–reference detuning and K_eff the bath-mediated locking strength (§3.6's Im Σ = −½ K_eff cos Δ\*). This equation undergoes a **saddle-node-on-invariant-circle (SNIC) bifurcation** at |Δω| = K_eff, with three quantitative signatures.

---

## Part I — Derivation (discharges "Adler asserted, not derived")

Specify a concrete, standard circuit-QED model and *derive* the Adler reduction with controlled approximations — exactly what GPT-5.5 (Concern #1) and Fable 5 (Concern #4) asked for:

- **System:** a driven transmon qubit (Rabi rate Ω_R, detuning Δ) — the "internal clock."
- **Bath/pointer:** a dispersively coupled readout cavity (coupling χ, decay κ) traced out — the "bulk reference."
- **Reduction:** adiabatically eliminate the cavity to obtain a Lindblad master equation for the qubit; in the measurement-dominated regime extract the reduced equation of motion for the Bloch-vector azimuth φ in the measured plane. The claim to be shown: it takes Adler form with
  $$K_{\text{eff}} = K_{\text{eff}}(\Omega_R,\chi,\kappa,\bar n),\qquad \Gamma_{\text{lock}} = K_{\text{eff}}\cos\phi^\* = \sqrt{K_{\text{eff}}^2 - \Delta\omega^2}.$$
- **Deliverable:** closed-form (or numerically validated) K_eff in terms of lab knobs, *and* — discharging §3.6 — an independent computation of Im Σ in the *same* model showing Im Σ = −½ K_eff cos Δ\*. One model, both objects, shown to agree (Fable 5's Concern #4 exactly).

This converts "writing an Adler equation after tracing out a bath" into a derivation with a domain of validity.

### ✅ Part I — RESULT (executed 2026-06-25)

Run: [`dispute-002-partI-Keff.py`](dispute-002-partI-Keff.py) (numpy + scipy only, ~10 s), figure [`dispute-002-partI-Keff.png`](dispute-002-partI-Keff.png). Every link in the chain is checked numerically:

| Step | Check | Result |
|---|---|---|
| **(1a)** cavity → dephasing | Γ_φ from the full qubit+cavity Liouvillian vs the textbook 8χ²n̄/κ | **agreement 0.990** (χ=0.05, κ=1, n̄=3.21) |
| **(1b)** master eq → Adler | fit φ̇ to Ω − K_eff sin2φ on the Bloch equator | **K_eff/γ = 1.0000**, spurious 1st-harmonic **1.4×10⁻¹¹** (pure 2nd-harmonic, exact) |
| **(1c)** critical slowing | Γ_lock vs 2√(K_eff²−Ω²); log-log exponent | **exponent 0.495** (SNIC predicts ½); ratios 0.99–1.00 |
| **(1c)** sub-threshold slips | ⟨φ̇⟩ vs √(Ω²−K_eff²) | **ratio 1.000** across Ω/K_eff = 1.02–1.6 |

**Derived result:**

$$\boxed{\,K_{\text{eff}} = \frac{\Gamma_\phi}{2} = \frac{4\chi^2 \bar n}{\kappa}\,}$$

a closed-form locking strength in terms of lab knobs — the dispersive shift χ, readout photon number n̄, and cavity linewidth κ. The Adler equation is no longer inserted; it *emerges* from the standard dispersive-readout master equation, and its coupling constant is computed.

**Physical headline — the cut is a readout-power threshold.** Locking (record formation) requires |Ω| ≤ K_eff, i.e.

$$\bar n \;\ge\; \bar n_{\text{crit}} = \frac{\kappa\,|\Omega|}{4\chi^2}.$$

The Heisenberg cut "snaps" when the readout photon number crosses n̄_crit — a directly tunable, measurable knob (for χ=0.05κ, n̄_crit ≈ 100 |Ω|/κ). That is a concrete, quantitative, falsifiable statement of *where* the cut sits — which is exactly what Part II (T6) then tests for the SNIC signatures.

*Caveat kept honest:* (1a) uses the standard fast-cavity dispersive result (verified here to 1%); the σ_x-pointer identification is a basis choice (the rate formula is basis-independent in magnitude). The derivation establishes the *form and coupling* of the Adler reduction and its SNIC universality — it does not, by itself, prove the framework's *interpretation* (see Part II's limitations).

---

## Part II — The three falsifiable signatures (SNIC universality)

> 📋 **A full, hand-to-a-lab protocol is now drafted:** [`dispute-002-partII-protocol.md`](dispute-002-partII-protocol.md) — device parameters, the four measurements (Arnold tongue, critical-slowing exponent ½, √-law slips, catch-and-reverse edge), pulse sequences, the discrimination table, systematics, and a ~1-device-week resource estimate. The summary below states the predictions; the protocol states how to measure them.

From the Adler form, the approach to the cut has a **specific universality class** with a **parameter-free critical exponent**. Tune the ratio Δω/K_eff across the threshold (vary readout power → K_eff, and qubit/drive detuning → Δω):

| # | Signature | Prediction (SNIC) | Standard-decoherence null |
|---|---|---|---|
| **(1)** | **Sharp threshold** | record locks **iff** \|Δω\| ≤ K_eff — an Arnold-tongue edge | smooth monotonic crossover; **no** sharp boundary |
| **(2)** | **Critical slowing** approaching the edge from the locked side | $\tau_{\text{record}} = \Gamma_{\text{lock}}^{-1} \propto (K_{\text{eff}}-\|\Delta\omega\|)^{-1/2}$ — **exponent ½** | exponential decoherence; **no** diverging timescale, no ½ law |
| **(3)** | **Sub-threshold phase slips** just outside the edge | discrete slips at $\omega_{\text{slip}} = \sqrt{\Delta\omega^2 - K_{\text{eff}}^2}$, vanishing as √ at the edge | no slip frequency; phase diffuses, not winds |

**The coincidence claim (the decisive one):** the boundary of the **catch-and-reverse window** — the regime where a Minev-type mid-flight reversal [14] still succeeds — must fall **exactly at the SNIC edge |Δω| = K_eff**, not at an unrelated coupling scale, and reversal fidelity must collapse with the **same ½-exponent critical slowing**. The framework says the reversible→irreversible boundary *is* the locking bifurcation; standard theory has no reason for those two scales to coincide or to share an exponent.

---

## Platform and regime

Existing hardware suffices — no new apparatus:

- **Circuit QED**, transmon + tunable continuous dispersive readout (the Minev [14] / Murch–Siddiqi continuous-measurement regime). Readout power sets K_eff; qubit/drive detuning sets Δω; weak-measurement tomography reconstructs φ(t) and the reversal fidelity.
- **Knobs swept:** Δω/K_eff ∈ [0.5, 1.5] through the threshold; for each, measure (1) lock/no-lock, (2) τ_record vs (K_eff − |Δω|) on a log–log plot (slope = −½?), (3) the sub-threshold slip spectrum, and (4) the catch-and-reverse fidelity boundary.
- Optional second platform for universality: a driven trapped-ion or optomechanical pointer.

---

## Falsification table

| Observation | Verdict |
|---|---|
| Smooth crossover; no tongue edge; reversal fidelity ∝ measurement rate with **no** ½-law | **Framework's core dynamical claim FALSIFIED.** dispute-002 resolves to *reject* on the merits; dispute-001's mechanism is wrong, not merely under-derived. |
| Sharp tongue at \|Δω\| = K_eff; τ_record ∝ (K_eff−\|Δω\|)^(−1/2); slips at √(Δω²−K²); catch-and-reverse boundary on the tongue edge | **Consistent with the framework.** GPT-5.5's "no testable content" reason removed → dispute-002 converges toward *major revision*. |
| Partial (tongue but wrong exponent, or coincidence fails) | Diagnostic; refines the model and re-enters the loop. |

---

## Honest limitations (so the panel can't ambush them)

- **A positive result is necessary, not sufficient, for the *interpretation*.** SNIC phenomenology at a measured qubit is, on its own, *standard driven-dissipative physics* — quantum synchronization is established ([10–13]). The genuinely new empirical content is narrow and specific: **that the cut (the reversibility boundary) sits at the locking edge and inherits its ½ exponent.** That is a falsifiable claim about *where* the cut is and *how* it scales — not a claim only MCI could satisfy. Part I (derivation) is what would let a positive result be *attributed* to the framework's mechanism rather than coincidence.
- **A null result is decisive against the framework**, not just against the postulate. This is the first test that probes the **core mechanism** rather than the added preferred-frame postulate of T1–T5 — so it carries more weight in both directions.
- **This is a spec, not a result.** Nothing here is claimed as done. Part I (the derivation) is the prerequisite and is itself the highest-leverage technical task flagged in the rewrite plan.

---

## How it plugs into the journal

- Added to [`../experiment.md`](../experiment.md) as **T6 — Locking-Threshold / Adler-cut test** (the first test of the *core mechanism*, distinct from the postulate-probing T1–T5).
- Retires [dispute-002](dispute-002-significance.md) on success (or resolves it to *reject-on-merits* on the null); discharges [dispute-001](dispute-001-born-basin-measure.md)'s "Adler asserted not derived" via Part I.
- Routed to the **invited experimentalist** (Pillar III): a circuit-QED continuous-measurement group is the natural lab.

---

*Drafted by Claude Opus 4.8 (Anthropic), 2026-06-25, as the retirement-path spec for dispute-002. SNIC scaling laws are standard Adler/saddle-node results (Adler 1946; Pikovsky–Rosenblum–Kurths); the novel content is their identification with the measurement reversibility boundary. Independent cross-lab and human-expert scrutiny of this spec is invited — it is a proposal, not a verdict.*
