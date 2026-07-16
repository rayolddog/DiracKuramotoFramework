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

## Next steps (in order, all cheap)

1. Order-of-magnitude a-priori estimate, T5 §3 style: what dissipation-sector
   coupling would a Q ~ 10¹⁰, months-long BAW record bound? Compare T5's
   reach.
2. Literature/data check: are BAW noise time series public (Tobar group,
   UWA; any LIGO-adjacent acoustic-mode archives)? Email-able ask if not.
3. If (1) and (2) survive: promote to `LIGO_SIDEREAL_TEST_T5.md`-style design
   doc (T6), with the mass–frequency plane figure updated to show T2/T4/T5/T6
   coverage.

*Provenance: idea surfaced in conversation between JB and Claude (Anthropic
Fable 5), 2026-07-15, while arm2 of an unrelated CT-sinogram experiment
trained in the background. Drafted by Claude; framing and the
phonon-realism connection are JB's.*
