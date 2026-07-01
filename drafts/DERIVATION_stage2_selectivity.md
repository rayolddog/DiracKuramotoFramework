# Derivation pass: why the frame coupling is Stage-2-only

*Addresses Suggested_experiment.md §7 item 1 — the linchpin. Goal: derive why a
preferred-frame coupling can be invisible in free (unitary) evolution yet active in
measurement capture. If this holds, it simultaneously (a) explains the null clock/LPI
Lorentz tests and (b) defines the sidereal observable.*

Verdict in one line: **Stage-2 selectivity is earned from symmetry; the *cosmic* (vs
lab) character of the frame is not — it is the single irreducible postulate.**

---

## Step 1 — The closed system is frame-blind by symmetry (exact, not small)

The free dynamics is the Dirac equation (chiral mass coupling, Zitterbewegung, the
closed-system Rabi precession of §2.2). It is **exactly Lorentz covariant**. A covariant
theory has no preferred frame: any "frame-dependent phase" you compute in the closed
system is pure gauge — it boosts away. So the free-evolution preferred-frame observable
is not merely small, it is **identically zero, protected by Poincare symmetry.**

This is stronger than "the effect is below 1e-18." It says the closed channel is *exactly*
empty, which is why decades of clock/LPI Lorentz tests — which probe free precession —
are null. They are testing a symmetry-protected zero.

## Step 2 — Measurement breaks the symmetry, and only there

Measurement = open the system to a bath and trace it out (Stage 1 capture -> Stage 2
equilibration). Write

    H_tot = H_S (Dirac, covariant) + H_B (bath) + H_int (surface coupling).

The bath has a rest frame, four-velocity u^mu, and a state (thermal/vacuum) defined in
that frame. Tracing it out (Born-Markov) gives a reduced master equation

    d rho/dt = -i [ H_S + H_LS , rho ]  +  D[rho],

where the Lamb shift H_LS and the dissipator D are built from bath correlation functions
evaluated **in the bath frame** — so both carry u^mu. Open-system reduced dynamics is
generically **not** Lorentz covariant precisely because the bath singles out a frame.

Both H_LS and D scale as |H_int|^2 (the spectral density at the system frequency). Hence:

    frame-dependent effect  ∝  (capture coupling)^2  ->  0 as the system closes.

**This is the derivation of Stage-2 selectivity.** The preferred frame enters only through
the bath, the bath enters only through H_int, and H_int is ~0 in free evolution and large
in capture. No fine-tuning: the closed-channel zero is a symmetry, the open-channel
nonzero is the broken symmetry, and the knob between them is the measurement coupling.

## Step 3 — Coherent vs incoherent maps onto your Re W / Im W

The reduced dynamics splits exactly as your §3.5 does:

- **H_LS (Lamb shift)** — Hermitian, generates a *coherent mean phase*. This is the
  reversible part, your **Re W**, the coherent first step of Stage 2. **This is the
  testable (Channel A) signal.**
- **D (dissipator)** — non-Hermitian, *decoherence / variance*. Your **Im W**, the
  irreversible tail. This is the N^4-suppressed Channel B — not feasible at ppm.

So the feasible observable is precisely the **frame-dependent Lamb shift**: a coherent,
bath-induced energy shift that carries the bath frame and lives on the reversible side of
the Heisenberg cut. The framework's own structure already separates the channel you can
measure from the one you can't.

(A static Lamb-shift phase would be absorbable by recalibration. What makes it observable
is that it (i) appears only during the capture window and (ii) modulates sidereally as the
apparatus orientation changes — neither of which a fixed recalibration removes.)

## Step 4 — Symmetry fixes the harmonic and the amplitude

The GHZ probe encodes the signal in a (pseudo)spin — an **axial** vector. Under parity P,
velocity beta is a polar vector (beta -> -beta) while spin is axial (s -> s). A
parity-conserving phase is therefore even in beta:

- **Generic prediction (parity-conserving capture): tensor, O(beta^2) ~ 1.5e-6, SECOND
  sidereal harmonic.** This is the headline target: N ~ 100 GHZ, multi-month run.
- A **first-harmonic, O(beta) ~ 1.2e-3** signal is *forbidden by parity* unless the
  capture coupling is **chirally asymmetric** (treats L and R differently) — i.e. parity-
  violating.

Framework hook: the one place chirality is built in is the **chiral mass coupling** (L-R
off-diagonal). A chirally-asymmetric surface coupling is exactly what would promote the
signal to first-harmonic / beta. Since fundamental EM and gravity conserve parity, the
*default* expectation is parity-even -> beta^2; a beta signal would be a discovery of
capture-channel parity violation. Either way the framework now **predicts the harmonic**,
which is a sharp, falsifiable structural claim (and it tightens Suggested_experiment.md:
lead with the second-harmonic, beta^2 target).

## The irreducible residue — the one thing not earned

Steps 1-4 are (mostly) earned from covariance, open-systems, and parity. They do NOT tell
you **which frame the bath is in.** And here is the trap:

- For an ordinary detector, the operative bath is its own **material** — rest frame = the
  **lab**. A lab-frame Lamb shift co-rotates with the apparatus and produces **no sidereal
  modulation.** Conservative reading => null signal.
- A **sidereal** signal exists only if the operative bath has a **cosmic** rest frame —
  i.e. the capture couples the system to a universal **vacuum sector whose rest frame is
  the CMB frame** (the "surface/vacuum interplay"). Standard QED vacuum is Lorentz-
  invariant and has no such frame: **this is the non-covariant postulate, in one sentence.**

So the derivation succeeds at localizing the entire non-covariant content into a single
statement:

    POSTULATE: capture couples the system to a frame-bearing vacuum whose
    rest frame is cosmic (CMB), distinct from the covariant QED vacuum and
    from the local thermal material.

Everything testable (Stage-2 selectivity, coherent-vs-incoherent, beta^2 / second
harmonic) follows. The postulate itself is not derived — it is isolated. That is what a
good reduction does, and it is also the honest limit of this pass.

## Decision tree (and an honest softening of "a null is fatal")

- Operative bath = lab material  -> no sidereal signal. Null result. Framework's
  measurement mechanism survives; only the cosmic-vacuum postulate is excluded.
- Operative bath = cosmic vacuum -> beta^2 second-harmonic signal at the CMB apex, size
  set by kappa.

So the experiment is really a **test of which bath frame governs capture**, lab vs cosmic.
This softens the earlier "a null is fatal" claim: a null kills the *cosmic-frame coupling
at that kappa*, not the two-stage mechanism. State it that way in the paper.

## What to compute next (in priority order)

1. **kappa from the surface coupling.** Model H_int at the detector surface, compute the
   anisotropic part of the bath spectral density seen at velocity beta, and extract H_LS's
   beta^2 coefficient. This turns "kappa ~ 1" into a real number, which is what makes a
   null meaningful.
2. **Confirm parity-even.** Verify the capture coupling conserves parity (=> beta^2,
   second harmonic) or identify the chiral-mass route to a beta first-harmonic term.
3. **Justify cosmic over lab.** The whole sidereal program rests here. Either argue the
   frame-bearing vacuum dominates the local material in the first capture step, or accept
   that the prediction is a lab-frame null and find a different observable.
4. **Check the Lamb-shift bound.** Ordinary (covariant) Lamb shifts are measured to high
   precision; confirm the frame-dependent piece rides only on the capture coupling and is
   not already bounded by precision spectroscopy / g-2.

---

*Bottom line: Stage-2 selectivity is genuinely earned — it is a symmetry-protected zero in
the closed channel, switched on by the measurement coupling, with the coherent (testable)
part identified as a frame-dependent Lamb shift = your Re W. Parity then predicts a beta^2
second-harmonic signal. The price is one sharp, undischarged postulate: that the capture
bath's rest frame is cosmic, not the lab. Item 3 above is now the real frontier.*
