# Does the frame-bearing vacuum dominate the local material in the first step of Stage 2?

*Addresses DERIVATION_stage2_selectivity.md, item 3 — the undischarged postulate. Result:
"dominance" is the wrong requirement. The Adler equation you already use sources the
capture (locking) term from coherent references ONLY; the thermal material is
structurally a noise term and cannot be the reference. So the lab-material worry
dissolves — and the residue is exactly the "background-field selection" problem the paper
already names.*

---

## 1. Reframe: dominance is the wrong test

The worry was: the local material couples far more strongly than any vacuum sector, so the
first-step phase is lab-frame and there is no sidereal signal. Two reasons this is the
wrong framing:

**(a) Only the cosmic part modulates — so you need separability, not dominance.** A large
lab-frame material Lamb shift is a *constant* (DC) phase offset; it does not modulate
sidereally because the material co-rotates with the lab. The sidereal fit isolates the
beta^2 component locked to the CMB apex regardless of how large the static material offset
is. The material contribution is background to be fit out, not a competitor for the
modulated signal. (Material/thermal drifts ride the 24 h *solar* day; the signal rides the
23 h 56 m *sidereal* day — they separate over months.)

**(b) Capture is locking, and you cannot lock to noise.** This is the decisive point, and
it is native to your dynamics — next section.

## 2. The Adler equation already separates the reference from the bath

Your capture dynamics is the Adler equation (Adler 1946 was literally the theory of
injection locking):

    d(theta)/dt = Delta_omega  -  K sin(theta - theta_ref)  +  xi(t)

The two source terms have **different physical origins and cannot be interchanged**:

- **K sin(theta - theta_ref)** — the locking term. It requires a reference with a
  **definite phase** theta_ref. K is sourced *only* by a phase-coherent drive. This is the
  capture / first step / your **Re W**.
- **xi(t)** — the noise term. A thermal bath has random phase; it contributes here. It
  causes phase **diffusion / decoherence**, your **Im W**. It is the dissipative tail.

A phase-incoherent bath **cannot contribute to K**, because there is no stable theta_ref to
lock to — incoherent power produces diffusion (xi), never entrainment (K). This is the
ordinary fact of injection locking: a weak *coherent* tone entrains an oscillator even when
buried under stronger *incoherent* noise, because locking range depends on coherent
amplitude and detuning, not on total power.

**Consequence:** the first step of Stage 2 (establishing K — the lock) is, by the structure
of your own equation, sourced by a coherent reference. The dense, strongly-coupled local
material is *structurally relegated to xi* — it decoheres, it does not provide the locking
reference. The lab-material "dominance" worry is therefore moot: the material is the wrong
*kind* of bath to be the reference, no matter how strong its coupling.

The only universal, always-available, frame-bearing candidate for the coherent reference is
the postulated cosmic-frame vacuum field. Material loses not on magnitude but on coherence.

## 3. Supporting argument: the coherent phase is a Lamb shift, which is broadband

Independently, the coherent first-step phase is a Lamb-shift-type quantity: a
**principal-value** integral over *all* bath modes, weighted toward high, off-resonant
frequencies (Bethe). The dissipator, by contrast, is set by the **on-resonance** spectral
density J(omega_0) — the resonant local modes. So even in the master-equation picture:

- coherent shift (Re W)  <-  broadband, off-resonant, universal field (vacuum-accessible)
- decoherence (Im W)     <-  on-resonance, structured, local material

This is the same split as Section 2, reached a second way. (Cross-link: the high-frequency
cutoff that renders this Lamb shift finite is exactly your UV-catastrophe avenue's
"cutoff = synchronization bandwidth" — the same scale would set the magnitude here.)

## 4. Where all three arguments bottom out — and it is a problem you already named

Sections 1-3 dissolve the dominance worry but converge on one undischarged thing: **the
existence of a phase-coherent reference field at rest in the cosmic frame.** Note this is
strong — neither a thermal bath *nor the ordinary zero-point vacuum* qualifies, because both
are phase-random (the vacuum has <E> = 0). The reference must be a genuine "cosmic clock":
a field carrying a definite phase in the CMB frame.

That is precisely the open problem your abstract already lists: *"an explicit dynamical law
for the background-field selection — which is also the locus of the framework's
nonlocality."* So item 3 is **not a new gap.** Reaching it from the experimental side, from
the Stage-2 selectivity side, and from the nonlocality side, you land in the same place. The
whole framework's frontier is this one object. That convergence is itself informative: it
says the cosmic reference field is the single thing to either derive or postulate cleanly,
and everything else is downstream.

## 5. The honest residue

Two real risks survive, and neither is the material:

**(a) Magnitude.** Coherence-selectivity tells you *which* reference wins, not *how strong*
the imprint is. In injection locking the imprinted phase scales as (reference
amplitude / system amplitude) x geometric beta^2. If the coherent cosmic field is feeble,
K is small and kappa << 1 — possibly alpha-suppressed or worse. The kappa ~ 1 used in
Suggested_experiment.md is optimistic; the signal could sit well below beta^2 ~ 1e-6.
Computing K from the reference-field amplitude is the make-or-break number.

**(b) The real backgrounds are cosmic, not material.** Because the static material is fit
out, the dangerous backgrounds are other effects locked to the *same* sky directions:
- the **CMB dipole** itself (a real ~beta photon-flux anisotropy, locked to the apex),
- the **sidereal anisotropy of cosmic rays** (~1e-3 to 1e-4, galactic/heliospheric-locked).
These are genuine sidereal signals near the signal direction and must be in the systematics
budget — they, not the material Lamb shift, are the things that can fake a detection.

## 6. Verdict

- The "vacuum must dominate the material" requirement is **dissolved**: your Adler dynamics
  sources the locking term K from coherent references only, and the thermal material is
  structurally a noise (decoherence) term. Material cannot be the first-step reference
  regardless of coupling strength. This is a genuine, framework-native resolution of item 3.
- What remains undischarged is the **existence and amplitude of a phase-coherent cosmic-
  frame reference field** — which is the same "background-field selection" open problem the
  paper already flags, now shown to be the common root of the experiment, the Stage-2
  selectivity, and the nonlocality.

## 7. What to compute next (priority)

1. **K from the reference-field amplitude.** Model the coherent cosmic field's coupling in
   the Adler K term; extract kappa and the beta^2 coefficient. This decides whether the
   signal is at 1e-6 (testable) or alpha x 1e-6 or smaller (not).
2. **Specify the reference field.** State what carries the cosmic-frame coherent phase
   (this is the background-field law). Connect to the relational-clock references [29, 36].
   Until this exists as a definite field, the prediction's amplitude is unanchored.
3. **Cosmic-background systematics budget.** Quantify the CMB-dipole and cosmic-ray
   sidereal anisotropies at the apparatus and show the predicted signal is separable from
   them (different harmonic content, different exact direction, polarization, or energy
   dependence).

---

*Bottom line: capture locks to coherence, not to energy, and your Adler equation enforces
that — so the strongly-coupled lab material is disqualified as the reference and the worry
evaporates. The price is that the reference must be a phase-coherent cosmic-frame field,
which is exactly the background-field-selection problem the paper already owes. Item 3 and
the framework's central open problem are one and the same — solve it once.*
