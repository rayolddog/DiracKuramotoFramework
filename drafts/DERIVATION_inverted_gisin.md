# DERIVATION — The Inverted Gisin Argument: No-Signaling as an Emergent Theorem

*2026-07-20 (JB + Claude), closing installment of the outcome-selection thread. Task: resolve the Gisin tension flagged in due diligence (`PRIOR_WORK_born_selection.md`, referee trap #3) — a nonlinear commit rate would break Born and open a superluminal signaling channel. Resolution: linearity is* derived *(kinematics), and the residual is* quantified *(a computable signaling amplitude bounded by experiment). No-signaling comes out of the framework as an emergent, falsifiable theorem rather than an axiom.*

---

## 0. The tension

Gisin (1984, 1989, 1990): deviations from Born-faithful (linear/martingale) dynamics generically permit superluminal signaling via entangled pairs. Our framework predicted Born deviations for detectors with nonlinear commit rates — so either such detectors signal (radical), or something forbids them (derive it). Both branches are resolved below: the single-quantum sector *forbids* commit nonlinearity kinematically (§1), and the residual signaling amplitude for hypothetical violations is computed exactly and bounded (§3).

## 1. Theorem 1 (forward): commit linearity is kinematically forced in the single-quantum sector

The commit rate at site $i$ arises from a matrix element $M_i$ connecting the distributed one-quantum excitation to a registered final state of energy $\hbar\omega$. Count powers of the local amplitude $\sqrt{e_i}$ vertex by vertex (each vertex is amplitude-linear — the framework's coupling postulate):

- **One vertex:** $M_i \propto \sqrt{e_i}$ ⇒ rate $\propto e_i$. This is the golden rule; it is the *only* leading-order channel.
- **Two absorption vertices** ($M_i \propto e_i$ ⇒ rate $\propto e_i^2$): delivers $2\hbar\omega$ — **no final state exists in the one-quantum sector.** Kinematically blocked, exactly.
- **Absorb–emit combinations:** return the quantum to the pool — that is the exchange game itself (Stage 2), not commitment. Already counted; contributes no rate nonlinearity.
- **Three-vertex paths** (absorb–absorb–emit, net $\hbar\omega$): allowed, amplitude $\propto e_i^{3/2}$, suppressed by two extra powers of the coupling: relative size $\sim (\Gamma/\omega)^2 = w^2 \lesssim 10^{-4}$ even for broadband silicon ($w\sim10^{-2}$), $\lesssim10^{-14}$ for atomic lines.
- **Saturation/Pauli corrections** (sublinear rates): require occupied final states — vanish for a ground-state detector.

Hence the effective commit rate in the single-photon sector is

$$f(e_i) = \Gamma\,e_i\,\big[1 + O(w^2)\big],$$

with the deviation parameter $\varepsilon \equiv$ (deviation from linearity) bounded by $\varepsilon \lesssim w^2$. **The same amplitude-linearity postulate that makes the game fair (Itô theorem) makes commitment linear. One postulate now does four jobs**: Born form (FGR), fairness (martingale), commit linearity (this theorem), and — via the Bell-game construction — statistical no-signaling. Gisin's condition is satisfied automatically, not imposed.

## 2. No-signaling from the linear game (restatement)

With $f(e)=e$ and martingale shares, the two-wing game gives joint Born order-independently (Bell installment, verified): marginals at each wing are independent of the far wing's setting, and of whether the far wing measures at all. So **no-signaling holds exactly at the statistical level despite explicit ontic nonlocality** (the shared-frame rotation, §6b of the Bell note). This is the framework's version of the peaceful-coexistence structure: nonlocal beables, local statistics — with the local statistics now *derived* from §1 rather than postulated.

## 3. Theorem 3 (inverse): the signaling amplitude of a hypothetical violation, exactly

Suppose (counterfactually, or in an exotic system) Alice's detector commits with $f(s) = s^{1+\varepsilon}$. For the partially entangled state $\sqrt p\,|00\rangle + \sqrt{1-p}\,|11\rangle$, Alice at analyzer angle $\alpha$, Bob at $\beta = 0$, the fast-commit limit gives Bob's marginal in closed form:

$$M(B{=}0;\alpha) \;=\; p\;\frac{\cos^2\!\alpha\, s_+^{\varepsilon} + \sin^2\!\alpha\, s_-^{\varepsilon}}{s_+^{1+\varepsilon} + s_-^{1+\varepsilon}}, \qquad s_+ = p\cos^2\!\alpha + (1{-}p)\sin^2\!\alpha,\; s_- = 1-s_+ .$$

Properties (all verified in `inverted_gisin.py`, closed form *and* full stochastic game):

| | closed form | full game |
|---|---|---|
| $\varepsilon=0$: $\Delta M$ between $\alpha=0°,45°$ | $0$ exactly | $-0.0002$ (noise floor) |
| $\varepsilon=0.2$, $p=0.8$ | $+0.041$ | $+0.021$ |
| $\varepsilon=0.5$, $p=0.8$ | $+0.089$ | $+0.044$ |
| $p=0.5$ (any $\varepsilon$) | $0$ exactly | $-0.002$ (noise floor) |

The full-game values are one-half the fast-commit ceiling — exactly the $P(\text{Alice commits first}) = \tfrac12$ dilution (signaling requires the nonlinear wing to commit first in the foliation). Three structural facts:

1. **Signaling $\propto \varepsilon$** with coefficient $K(p,\alpha) \approx 0.18$ at $p=0.8$ (ceiling): $\Delta M \approx K\varepsilon$ small-$\varepsilon$.
2. **Symmetry protection at maximal entanglement:** $\Delta M \equiv 0$ at $p = \tfrac12$ for *any* $\varepsilon$. Standard Bell tests (maximally entangled) are the *least sensitive* place to look for this physics.
3. **The sensitive configuration is partial entanglement + asymmetric bases** — a concrete experimental pointer: a dedicated no-signaling analysis on partially-entangled-state data bounds $\varepsilon$ directly as $\varepsilon \le \Delta M_{\rm exp}/(K\cdot P_{\rm first})$.

Combining: experiment (no-signaling checks in Bell datasets, typically $10^{-2}$–$10^{-4}$ depending on counts — *precision claims to be verified against specific datasets before citing*) bounds $\varepsilon \lesssim 10^{-2}$–$10^{-3}$ empirically; §1 predicts $\varepsilon \lesssim w^2 \lesssim 10^{-4}$ theoretically. Consistent, with orders of margin.

## 4. Consequences for the framework's claims (bookkeeping)

1. **Gisin tension: resolved.** No-signaling is an emergent theorem (kinematic linearity + martingale fairness), not an axiom. The framework's stance for Paper 1: *all* of its novel deviation channels are signaling-capable in principle — and the framework's own protections (kinematic linearity §1, noise locality, symmetry) suppress every one of them in all tested regimes. That is a coherent, falsifiable structure: no-signaling holds because ordinary matter satisfies the protections, not because the theory forbids the question.
2. **Rescoping the nonlinear-commit deviation prediction** (second retraction-grade correction of the thread): in the single-quantum sector, commit nonlinearity is kinematically suppressed to $\varepsilon \lesssim w^2$ — ordinary single-photon detectors (including "cooperative registration" designs) cannot show the $\alpha \ne 1$ deviations at any interesting level. The channel survives only in: (a) **multi-quantum states** (two-photon absorbers etc.) — where standard QM keeps such detectors $\rho$-linear (nonlinear in *intensity*, linear in the *state*) and hence non-signaling; whether the framework's multi-quantum game reproduces that $\rho$-linearity is an open consistency check; (b) the **Stage-2 channels** (correlated-noise atom arrays, pre-cohered ensembles), which are fairness violations, not commit violations — their signaling implications inherit the same analysis: deviations there are also in-principle signaling-capable, also symmetry-protected at maximal entanglement.
3. **The remaining live deviation predictions**, post-rescoping: atom arrays (must beat dressed-state Born, per referee trap #2) and pre-cohered ensembles. Both are Stage-2 (fairness) effects; both should be analyzed for their signaling signature before Paper 1 claims them.

## 5. Open items

1. Multi-quantum sector: formulate the N-quantum game and verify it reproduces the $\rho$-linearity of nonlinear-intensity detectors (two-photon absorption as a linear POVM). This is the main consistency check left.
2. Verify actual no-signaling precision in published Bell datasets (partial-entanglement data especially) before quoting bounds.
3. Signaling analysis of the two surviving Stage-2 deviation channels.

---

*Glossary:* **ρ-linearity** — outcome probabilities affine in the density matrix; the standard-QM property equivalent to no-signaling for local measurements. A detector can be nonlinear in intensity yet ρ-linear (two-photon absorber). **Kinematic suppression** — a process forbidden by energy conservation in a given sector, not by small couplings; exact, not approximate. **$P_{\rm first}$ dilution** — signaling requires the deviant wing to commit first in the preferred foliation; symmetric stations give ½.
