# 2026-07-15 — T6 sketch: sidereal decoherence search in cryogenic phonon resonators (BAW quartz)

*Session log / idea sketch. Companion to [`../LIGO_SIDEREAL_TEST_T5.md`](../LIGO_SIDEREAL_TEST_T5.md)
(same dissipative-registration channel, different point on the mass–frequency
plane), `current_revision_DK_paper.md` §3 (three-stage measurement), and the
T4 literature-check loophole (Lindblad-sector Lorentz violation untabulated).
Status: SKETCH ONLY — no sensitivity estimate yet, no data located yet. Every
claim below that isn't cited is an assumption to check.*

## Where it started

JB (John Bramble) watched a talk on phonons as gravitational-wave recorders and connected it
to the framework's core commitment: wavefunction realism and persistence in
macroscopic solids, with heat, chemical interactions (TLS defects), and
radiation as the coherence-scrambling channels — i.e., decoherence is
environmental coupling, not size. The framework adds the sharper claim: a
coherent phonon mode is a **Kuramoto object** — ~10²³ ions sharing one phase,
a macroscopic synchronized-clock ensemble — and decoherence is
desynchronization into the thermal bath. If the framework's non-covariant
coupling lives in the measurement/dissipation sector (Stages 2–3), phonon
decoherence rates should carry a **sidereal anisotropy**.

## What T6 would test

Same postulate as T5, different oscillator: a frame-bearing dissipation
coupling, dormant in free evolution, active in registration. T5 reads it on
LIGO's ~10 kg differential arm mode at ~100 Hz; T6 reads it on a cryogenic
bulk-acoustic-wave (BAW) quartz mode at ~MHz–GHz, effective mass ~mg–g scale,
Q ~ 10⁹–10¹⁰ (Goryachev & Tobar lineage). That is a **different point on the
quantum–classical boundary map** the paper flags ("do cooled optomechanical
membranes count?") — and arguably a cleaner one than LIGO: smaller thermal
occupation at cryogenic temperatures for GHz modes, single-quantum readout
demonstrated in qubit-coupled acoustic resonators (quantum acoustics), and no
km-scale environmental coupling.

Observable: sidereal-phase modulation of (a) resonator noise floor, (b)
ring-down time / linewidth, (c) frequency stability residuals — after the T5
detrending discipline (rolling median) and with the **solar fold as
systematics control**. Lesson imported from the T5 pilot: tidal constituents
are real and detectable (lunar M2/O1 at 10–12σ in H1; K1 is the named
sidereal confound) — a quartz resonator in a cryostat should be far less
tidally coupled than a 4-km interferometer, but temperature-servo diurnal
cycles will play the same confounding role; K1-vs-sidereal separation needs a
long record (months+).

## Why it might be cheap (the T5 argument again)

- Tobar's group and others have run BAW resonators continuously for
  **years** as GW/dark-matter/Lorentz-invariance instruments (e.g., the
  "rare events" BAW antenna paper, Goryachev et al., PRL 2021 — logged
  multi-month records; VERIFY citation). If any of that
  data is public or shareable, T6 is a **zero-new-hardware analysis**, like
  T5. UNKNOWN: whether the noise/linewidth time series (not just event
  triggers) are archived and obtainable — first thing to check.
- The analysis pipeline is a transplant: `t5_pilot/reduce.py`'s
  chunk→band-PSD→checkpoint pattern and `fold.py`'s sidereal/solar dual fold
  apply nearly unchanged; only the band selection and data reader change.

## Honest caveats (carry T4/T5's discipline)

1. **No coherent amplifier** — same fatal caveat as T4/T5: this bounds the
   dissipation-sector coupling, it does not amplify it. Raw sensitivity is
   unquantified until an order-of-magnitude estimate is done (NEXT STEP #1).
2. **TLS defects dominate cryogenic acoustic loss** and have their own slow
   dynamics (aging, drift). Any sidereal claim must survive a TLS-aging null
   model, not just a solar-fold control.
3. Radiation events (muons, radioactivity) cause correlated loss bursts in
   cryogenic devices (measured in superconducting qubits); these are
   Poissonian, not sidereal, but they fatten σ₁ — the T5 per-chunk scatter
   lesson applies.
4. The phonon-GW-detection literature targets MHz–GHz GWs with no confirmed
   sources; T6 borrows the *instrument*, not that science case. Frame it as
   a decoherence-anisotropy bound, never as GW detection.

## A-priori estimate (added same evening — NEXT STEP #1 done)

T5 §2 methodology transplanted. Observable: fractional modulation of the
resonator's loss/linewidth (the dissipation channel; frequency stability is
deliberately NOT the signal channel — it is unitary-sector, already bounded
brutally by cryo-BAW Lorentz-invariance work, and serves as the built-in
null/control). Reach: 5σ floor = 5·σ₁·√(2/M), M = live time / τ_sample at
70% duty, τ_sample = 100 s (T5 convention; see mode caveat below).

| σ₁ (per-100-s loss scatter) | live | 5σ floor | vector β margin | tensor β² margin |
|---|---|---|---|---|
| 6.5e-2 (T5's raw floor)   | 2 yr | 6.9e-4 | 1.7× | 0.002× |
| 1e-2 (plausible: ~1% per-ring-down Q metrology) | 6 mo | 2.1e-4 | 5.6× | 0.007× |
| 1e-2                      | 2 yr | 1.1e-4 | 11×  | 0.014× |
| 2e-3 (post-regression, optimistic) | 2 yr | 2.1e-5 | 56× | 0.07× |
| 1e-4 (implausible today)  | 2 yr | 1.1e-6 | 1128× | 1.4× |

**Verdict — same shape as T5, shifted mass/frequency point:**
- **Vector channel (β = 1.2e-3): reachable**, margin ~5–50× at plausible σ₁.
  A months-long cryo-BAW loss record can bound κ·ξ_DK in the vector channel
  at the few-percent-of-natural level, at ~mg effective mass and MHz–GHz —
  a new point on the exclusion map, orthogonal systematics to LIGO.
- **Tensor channel (β² = 1.5e-6): out of reach** — needs σ₁ ≲ 1e-4 per
  100 s (two orders beyond current loss metrology). Same no-coherent-
  amplifier verdict as T4/T5. N-phonon Fock states from quantum acoustics
  (N ~ 10 demonstrated) amplify the *phase* channel T2-style, not the
  fractional *dissipation* modulation — noted, not a rescue.

Mode-choice caveat: τ_sample = 100 s requires ring-down time ≪ 100 s for
sample independence. Q/(πf): 5 MHz @ Q=1e10 → 637 s (samples NOT
independent at 100 s; M drops ~6×, floor worsens ~2.5×); 100 MHz @ Q=1e9 →
3.2 s (fine); GHz @ Q=1e8 → ms (fine). **Prefer ≳100 MHz overtones.**

Single-device weakness vs T5: one crystal = one sensitive axis = no
multi-detector sidereal-phase discriminant. Cheap fix worth noting in any
design doc: **two crystals, orthogonal axes, one cryostat** — common-mode
thermal/TLS systematics, opposite-sign geometric factor g(n̂,t).

ξ_DK ceiling remark (speculative, VERIFY): LIGO's loss budget is
characterized to a few percent, capping ξ_DK small; cryogenic quartz
acoustic loss at 4 K is *less* completely budgeted (Landau–Rumer vs TLS vs
anchoring attribution is partly model-based), so the excludable ξ_DK
fraction may actually be more generous here. Needs a literature number.

## Next steps (in order, all cheap)

1. ~~Order-of-magnitude a-priori estimate~~ **DONE above** — vector
   reachable (5–50× margin), tensor out of reach; prefer ≳100 MHz modes.
2. ~~Literature/data check~~ **DONE 2026-07-15 (web check):**
   - **The data exist and the format is right, but they are NOT public.**
     The GEN 1/2 runs (the "rare events" PRL 127, 071102 (2021),
     arXiv:2102.05859) logged **153 days over two runs**, acquiring
     lock-in amplitude at each quartz mode frequency **digitized at
     100 Hz** — mode-amplitude time series, exactly what a loss/noise
     sidereal fold consumes. MAGE (Scientific Reports 13 (2023),
     arXiv:2307.00715) has been "actively taking data intermittently as
     of early 2023" with multiple modes per crystal continuously
     monitored — likely years of records by now.
   - **Access:** "available from the corresponding author on reasonable
     request" (MAGE paper) — no GWOSC-style archive. So T6 is NOT a
     zero-ask analysis like T5; it requires a data-sharing request to
     the UWA QDM lab (Tobar/Goryachev). Downgrade "zero new hardware"
     to "zero new hardware, one email."
   - **Bonus:** MAGE already runs **two near-identical quartz BAW
     resonators** — the two-crystal discriminant configuration proposed
     above may physically exist; their relative orientation is not
     stated in the paper (ask in the same email).
3. If (1) and (2) survive: promote to `LIGO_SIDEREAL_TEST_T5.md`-style design
   doc (T6), with the mass–frequency plane figure updated to show T2/T4/T5/T6
   coverage.

*Provenance: idea surfaced in conversation between JB and Claude (Anthropic
Fable 5), 2026-07-15, while arm2 of an unrelated CT-sinogram experiment
trained in the background. Drafted by Claude; framing and the
phonon-realism connection are JB's.*
