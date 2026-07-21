# DERIVATION — The Bell-Pair Game on the Joint Substrate

*2026-07-20 (JB + Claude), final installment of the outcome-selection thread (after `NOTE_born_gamblers_ruin.md`, `DERIVATION_slaved_phase_subthreshold.md`, `DERIVATION_vacuum_noise_correlation.md`). Task: run the (now fully grounded) fair-game selection machinery on an entangled pair across two wings, and show it reproduces quantum correlations — with the framework's nonlocality explicit and quantified.*

---

## 1. What the local games can and cannot do

$|\Phi^+\rangle = (|HH\rangle + |VV\rangle)/\sqrt2$, stations A and B, analyzers at $a, b$, two ports each. Structural facts that dictate the design:

- Each wing's **local** wave is unpolarized — 50/50 in every basis, no angle information present locally. The local fair game (2-port, shares ½/½) can therefore produce only the correct *marginals*.
- The joint weights $P(\pm\pm) = \frac12\cos^2(a-b)$ etc. live in the **substrate's correlated phase registry** — the pair was created as one substrate excitation, and the joint amplitude is the *unhidden variable* (detector–substrate entanglement; never "hidden": it is real, physical, and merely ignored by local bookkeeping).
- Bell's theorem is respected, not evaded: the mechanism below is **nonlocal in the preferred foliation** (the framework's khronon/CMB-frame ordering). The nonlocality is relocated into the substrate and made explicit — the framework's standing position (two-stage measurement, bulk-mediated detector entanglement, not LHV, not superdeterminism).

## 2. The two-stage mechanism in game terms

1. Both local fair games run **simultaneously** on their ½/½ shares (amplitude-linear noise ⇒ martingale shares; rate-linear commitment).
2. Whichever wing **commits first** — ordered by the preferred foliation — locks. By the fairness + rate-linearity theorems, its outcome is drawn with exactly the marginal Born probability (½).
3. The lock is a substrate-wide resync event on the pair's shared phase thread: the surviving joint amplitude **renormalizes** (evolution-not-collapse), which physically resets the other wing's shares to the *conditional* Born weights, e.g. $P(B{=}+|A{=}+) = \cos^2(a-b)$.
4. The second wing's fair game runs on the updated shares — its commit is conditional-Born-exact by the same theorems.

$$P(i,j) = \underbrace{m(i)}_{\text{marginal, exact}}\times\underbrace{P(j|i)}_{\text{conditional, exact}} = |c_{ij}|^2 \quad\text{— joint Born, }\textbf{independent of commit order},$$

and order-independence *is* the no-signaling property at the statistical level. The martingale machinery composes: the conditional reset is just a new initial condition for a fair game, and fair games honor any initial condition — the same property that made the single-detector derivation work does the two-wing bookkeeping for free.

## 3. Simulation (`bell_pair_game.py`, 2026-07-20)

Two simultaneous 2-port SDE games ($\sqrt e$ noise, $\sigma = 0.3$), constant-rate commitment (total rate is share-independent since shares sum to 1), stochastic commit order, conditional resync with **fidelity** $\eta$ (new shares $= \eta\cdot\text{conditional} + (1-\eta)\cdot\text{current}$). CHSH at standard angles ($a \in \{0, 45°\}$, $b \in \{22.5°, 67.5°\}$), 40k trials per angle pair:

| $\eta$ | $S$ (sim) | $S = 2\sqrt2\,\eta$ (pred) |
|---|---|---|
| 1.0 | **2.820** | 2.828 |
| 0.9 | 2.533 | 2.546 |
| $1/\sqrt2$ | 2.000 | 2.000 |
| 0.5 | 1.421 | 1.414 |

Checks: $E(a_1,b_1) = 0.706$ vs QM $0.707$; **no-signaling** — A's marginal $+0.007$ / $-0.007$ under B's two settings (consistent with 0); **order independence** — $E = 0.717$ (A first) vs $0.706$ (B first), both $= \cos2(a-b)$ within error; commit order 50/50 as it must be for symmetric stations.

## 4. What is derived vs. what is postulated

**Derived** (from the thread's theorems): that local fair games + rate-linear commitment turn the substrate's joint amplitudes into exactly Born-weighted joint outcomes, order-independently and without signaling. The delicate part — that pre-commit fluctuations at each wing don't corrupt the statistics — is handled by the martingale property (optional stopping applies at each wing's commit time separately).

**Postulated** (the framework's physical content, not derived here): that the substrate carries the joint two-photon amplitude between the wings, and that a lock renormalizes it faithfully ($\eta = 1$) across the pair's phase thread. This document is a **consistency proof** — the selection machinery composes correctly with the framework's entanglement ontology — not a derivation of entanglement itself.

## 5. The new quantitative handle: resync fidelity and speed

$S = 2\sqrt2\,\eta$ makes the substrate resync *measurable*:

- **Fidelity floor from existing experiments:** photonic CHSH results near $2.8$ imply $\eta \gtrsim 0.99$ over 100-km-class separations (fiber and free-space); loophole-free experiments ($S \approx 2.4$–2.7 with inefficiencies) are consistent. The substrate resync, whatever its mechanism, is near-perfect over terrestrial scales.
- **Speed:** if wing B commits before A's resync *arrives* (finite resync propagation in the preferred frame), those trials decorrelate — an effective $\eta < 1$ that grows with tighter coincidence timing and larger separation. This is exactly what "speed of spooky action" experiments bound: $v_{\rm resync} \gtrsim 5\times10^4\,c$ in any candidate preferred frame (Salart et al. 2008, 18-km Geneva test; satellite tests push further). The framework accommodates this naturally if resync is a *global* re-equilibration of the foliation-wide substrate coherence (effectively instantaneous in the cosmic frame) rather than a propagating signal — but the bound is a real constraint on any propagating-resync variant, and connects directly to the framework's standing quantum-eraser prediction (bulk-resync timescale observable in delayed-choice timing).
- **Degradation channel:** any physical process that decoheres the substrate phase thread between the wings should reduce $\eta$ below 1 at fixed local visibilities — standard QM predicts no such dependence on anything but the photons' own decoherence. A null result (which is what all data to date show) keeps $\eta = 1$ and pushes the framework toward the global-resync (non-propagating) variant.

## 6b. Candidate resync mechanism: shared-frame rotation at the source point (added from JB's earlier exploration, recorded 2026-07-20)

JB's picture (from a prior exploration, restated here since it predates the session records): the entangled pair is **one substrate object** whose correlation is a single shared internal orientation — a plane/phase frame anchored at the creation event (the "central point"). Both photons are defined relative to that frame. The first lock **rotates the shared plane**; nothing traverses the intervening space — the changed degree of freedom is an angle, not a field configuration spread over kilometers. "How fast did the update travel?" is a category error: speed presupposes propagation.

Analogy refinement: this is **phase-velocity-like**, not group-velocity-like — the family of pattern motions (scissors intersection, lighthouse spot) that can be arbitrarily fast because nothing physical travels the path; signal-front velocity stays $c$.

Consequences:
1. **Decides the §5 fork** in favor of global (non-propagating) resync, with a discriminating prediction: spooky-action-speed experiments will only ever produce growing lower bounds (Salart $5.4\times10^4c$; Yin $1.38\times10^4c$) — **no finite floor will ever be found**. A propagating variant predicts an eventual floor.
2. **Explains $\eta = 1$:** a rotation is exact; no transmission loss with distance. Fidelity degrades only if the shared frame itself decoheres — consistent with undiminished violation at 100-km and satellite scales.
3. **Dissolves before-before configurations** (Zbinden 2001; Stefanov 2002): the rotation happens at the shared object, ordered by the preferred foliation, not at either detector.

Does **not** resolve the Gisin tension (nonlinear-commit deviations would still bias the rotation statistics Bob receives ⇒ marginal shifts). Candidate resolution to develop: **inverted Gisin** — within the framework, observed no-signaling *derives* commit-rate linearity; the golden rule becomes a consistency requirement on the substrate rather than an input. Needs its own session before Paper 1.

## 6. Open items after this installment

1. Derive the resync dynamics itself — mechanism and why $\eta = 1$ (global foliation-wide re-equilibration vs. propagation), tying into the quantum-eraser timescale prediction and the T1–T5 preferred-frame test program.
2. Three-station / GHZ extension (the T2 sidereal GHZ test lives there).
3. The remaining thread items: detector commit-nonlinearity survey; $e \propto A^2$ within the ZBW model proper; cluster residual in the correlated-noise game.

---

*Glossary:* **khronon/foliation** — the framework's preferred time-slicing (constant sync-phase surfaces, identified with the CMB frame); "first commit" is defined in this slicing. **Resync fidelity $\eta$** — fraction of the conditional update actually delivered to the far wing; $S = 2\sqrt2\,\eta$, Bell violation requires $\eta > 1/\sqrt2$. **No-signaling** — marginal statistics at one wing independent of the other wing's setting; here automatic from martingale + conditional structure.
