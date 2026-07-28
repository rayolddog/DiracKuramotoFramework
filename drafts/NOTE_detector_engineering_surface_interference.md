# NOTE — Detector engineering as fairness engineering (for the DK Framework paper)

*JB's observation, 2026-07-28 session; formalized by Claude Fable 5. Companion to Paper 1 v0.5's §4 addition (interference-cross-term origin of the fair noise). This material is deliberately NOT in Paper 1 — it belongs to the eventual DK Framework paper's discussion of measurement.*

## The observation

The deposition of energy on the detector surface depends on the complex wave packets of *both* parties: the incident quantum and the quantum particles bound to the detector (plus whatever the vacuum contributes at the surface). The interaction must therefore be computed in the complex representation — interference between these wave packets participates in the eventual selection. We may not know the vacuum contribution or the detector-electron wave packets in detail, but the complex calculation is what carries the physics from capture to selection.

## What Paper 1 v0.5 now says (the physics core)

With site amplitude $a_i$ ($e_i = |a_i|^2$) and a surface fluctuation increment $\delta b_i$ of uncontrolled phase,

$$|a_i + \delta b_i|^2 = |a_i|^2 + 2\,\mathrm{Re}(a_i^*\,\delta b_i) + O(|\delta b_i|^2).$$

Direct term = capture law (P1). Cross term = the noise: zero-mean by phase randomness (P3a), variance $\propto e_i$ by linearity (P2) — the unique fair scaling of Theorem 1. Fairness = *nothing at the surface holds a phase reference against the players*. Homodyne detection is the engineered-violation limit (a local oscillator IS a phase reference; the cross term becomes a linear field readout).

## The framework-paper extension: why detectors are built the way they are

If selection is a fair game driven by the cross term, then the standard necessities of quantum-event recording are exactly the engineering of the statistics of $\delta b_i$ — keeping the game fair and the threshold honest:

- **Cooling the detector.** Thermal motion feeds the magnitude of $\delta b_i$ and, at high enough amplitude, lets noise alone assemble a threshold crossing with no incident quantum — a *dark count* is the selection game won by the bath. Cooling shrinks $|\delta b_i|$ so that only games seeded by real capture terminate. (Note the division of labor: noise *magnitude* never biases the odds — Theorem 0/1 — it only sets the rate of spurious games. Cooling is about false starts, not fairness.)
- **Shielding from incident (stray) radiation.** External fields arriving coherently across the face violate P3(b) locality (spatially correlated $C_{ij}$ → the rich-get-richer penalty of Theorem 3) and can carry a *defined phase* — an accidental partial local oscillator that biases the cross term (violates P3a). Shielding restores both premises. RF shielding of an MRI suite is the same discipline in JB's daily world.
- **Steady power supplies.** Supply ripple imposes a common, phase-coherent modulation on every site's bound charges — a global oscillating reference. That is a correlated, phase-defined contribution to every $\delta b_i$ simultaneously: it attacks P3(a) and P3(b) at once. A quiet supply is the removal of an unintended homodyne reference.

One sentence for the framework paper: **detector engineering is fairness engineering** — cryogenics bounds the stakes the bath can play with, shielding and supply regulation remove phase references and cross-site correlations, and the premises P2/P3 of Paper 1 are exactly the specification a detector engineer is (unknowingly) building to.

## How noise enters the *record*

JB's second point: the framework shows noise entering the recording through its effect on the wave functions of the interacting particles — not as an additive voltage on a wire but as a perturbation of $\delta b_i$'s statistics *upstream of selection*. Consequences worth developing in the framework paper:

1. Noise that stays zero-mean/local only adds dark counts and timing jitter (rate effects, never odds effects — Theorems 0, 4).
2. Noise that acquires phase coherence or spatial correlation shifts the *odds* (Theorem 3's computable penalty) — a qualitatively different failure signature: biased statistics, not just excess counts.
3. This dichotomy is testable in principle: deliberately injecting correlated vs uncorrelated perturbations into a detector should move statistics vs rates respectively — a lab-bench echo of Paper 1's §8 program, and possibly a diagnostic taxonomy for real instrument noise.

## Links

- Paper 1 v0.5 §4 ("The physical origin of the noise"), §9.4(iv) (open problem: promote sketch to conserving open-system calculation).
- Memory: project_born_gamblers_ruin, project_born_measure_status (the sketch grounds P2's *form*; it does not close the Born-measure question).
