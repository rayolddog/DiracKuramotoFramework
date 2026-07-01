# Reconciling §2.3 (first-harmonic Adler) with the bistable 0/π binary — DRAFT

**Date:** 2026-06-13 · **Status:** draft for review — `PAPER_REVISED.md` is **not** edited yet.
**Backing:** `code/phi_dissipative_check.py` (reconciliation block), `RESULTS_PHASE_DISSIPATIVE.md`.

## The tension

§2.3 writes the open-system reduction as a **first-harmonic** Adler equation
$$\dot\phi = \omega + K_{\text{eff}}\sin(\Phi_{\text{bulk}} - \phi),$$
which is **monostable**: one stable locked phase, hence one outcome. But measurement
must yield ≥2 outcomes, and the discretization companion's §3.2 now shows the binary
needs a **second-harmonic**, $\dot\phi=-\gamma\sin2\phi$ (stable at *both* 0 and π),
which comes from a *measurement* dissipator $D[\sigma_x]$. Taken at face value these
look like rival reductions of "couple to a bath."

## The resolution: one equation, two limits

They are not rivals. The general dissipative coupling to the bulk carries **both**
harmonics, because a bath does two distinct things to the chiral interference channel:

- it **measures** it — a *symmetric* (Hermitian, $\langle\text{bias}\rangle$-free)
  coupling, even under $\phi\to\phi+\pi$ → second harmonic, rate $\gamma$;
- it **biases** it — a *polar* reference with a definite axis $\Phi_{\text{bulk}}$
  (the faint thermal/ppm bias) → first harmonic, strength $\epsilon$ — exactly the
  §2.3 term $K_{\text{eff}}\sin(\Phi_{\text{bulk}}-\phi)$.

The reduced phase therefore obeys the **unified equation**
$$\boxed{\;\dot\phi = \omega - \gamma\,\sin 2\phi - \epsilon\,\sin(\phi-\Phi_{\text{bulk}})\;}$$

Fixed points (take $\omega,\Phi_{\text{bulk}}\to0$): $\sin\phi\,(2\gamma\cos\phi+\epsilon)=0$.
- $\phi=0$ stable for all $\gamma,\epsilon>0$;
- $\phi=\pi$ stable **iff** $\epsilon<2\gamma$ — otherwise it turns into a repeller.

| regime | stable phases | character |
|---|---|---|
| $\epsilon \ll \gamma$ (measurement-dominated) | 0 **and** π | **bistable binary**; bias only deepens the φ=0 well by $2\epsilon$ |
| $\epsilon = 2\gamma$ (threshold) | π marginal | binary melts |
| $\epsilon > 2\gamma$ (bias-dominated) | 0 only | **monostable = the §2.3 Adler limit** |

(All confirmed numerically — see the reconciliation block of the code; threshold
$\epsilon=2\gamma$ is exact.)

**So §2.3 is correct, but it is the *bias-dominated* limit of the full reduction.**
The first-harmonic term is real (it is the polar bias); it simply is not what creates
the basins. The two-outcome structure is carried by the *symmetric measurement* part,
which §2.3 omitted.

## The consequence the framework already commits to

The companion models the bulk reference as a **faint, overwhelmingly thermal bias
(ppm, as in MRI)** [PAPER_REVISED §4.1], *not* a coherent macrostate. A faint bias is
exactly $\epsilon\ll\gamma$ — the **measurement-dominated** regime. So the framework's
own ppm-bias commitment *predicts the bistable binary* and makes the monostable
first-harmonic writing of §2.3 the wrong limit for a measurement. This is consistent
with NMR/MRI, where strong $T_2$ dephasing (measurement) sets the up/down **binary**
and the ppm polarization only biases the populations.

---

## Ready-to-paste paragraph for §2.3 (paper voice)

> *(insert after the Adler equation, before "This — not the closed mass term —…")*

The form above is the lock's **first-harmonic limit**, with the bulk entering as a
single biased reference phase $\Phi_{\text{bulk}}$; it is monostable — one locked
phase, one outcome. The general dissipative coupling carries a second term. A bulk
that *measures* the chiral interference channel — a symmetric, $\langle\cdot\rangle$-free
coupling even under $\phi\to\phi+\pi$ — contributes a second harmonic, so
$$\dot\phi = \omega - \gamma\,\sin 2\phi - \epsilon\,\sin(\phi-\Phi_{\text{bulk}}),$$
with $\gamma$ the symmetric measurement rate and $\epsilon$ the polar bias of the line
above. The anti-phase fixed point $\phi=\pi$ is stable iff $\epsilon<2\gamma$: for a
*faint* bias ($\epsilon\ll\gamma$ — the ppm thermal bias of §4.1) the lock is
**bistable**, stabilizing phases near $0$ and $\pi$ (a binary), the bias merely
deepening one well; for a *dominant* bias ($\epsilon>2\gamma$) it collapses to the
monostable first-harmonic lock. Both are limits of one equation. The two-outcome
structure of a measurement is thus the symmetric (measurement) part of the bulk
coupling; the bias selects among the basins but does not create them. This
*stabilizes* a binary but fixes neither its cardinality (set by the measured
observable's spectrum) nor the Born weights (§8), both of which remain open.

---

## Caveats (do not let the draft overclaim)

1. **Bias ≠ Born weights.** The $\epsilon$ term breaks the 0/π degeneracy
   deterministically (deeper φ=0 well, $\Delta V=2\epsilon$); under noise that is a
   Boltzmann/Kramers tilt, **not** $|\alpha|^2$. Born weights stay the open §8 problem.
2. **Cardinality unchanged.** "Two" is the two eigenvalues of $\sigma_x$ (the chiral
   2-level structure) — representation theory, not generated here.
3. **Standard physics.** This is pointer-state (einselection) measurement theory plus
   a biased reference; the contribution is internal consistency + the identification
   (measured observable = chiral interference σ_x).
4. **Modeling commitment.** This presumes Stage-2 dissipation genuinely *measures* the
   interference channel. That is the natural reading of "registration," but it is a
   commitment, now made explicit rather than hidden in the first-harmonic notation.

## Integration options (your call)

- **(A) Additive** — paste the paragraph above into §2.3; least invasive, preserves
  the existing equation and revision history.
- **(B) Replace** — rewrite the §2.3 equation as the unified two-harmonic form from
  the start. Cleaner, but rewrites a core line of the main manuscript.

I recommend **(A)**. Say the word and I'll splice it in and rebuild
`Two_Regimes_of_Chiral_Mass_Coupling.pdf` (that one PDF only).
