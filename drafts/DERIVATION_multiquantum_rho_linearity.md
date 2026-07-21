# DERIVATION — The N-Quantum Game and ρ-Linearity

*2026-07-20 (JB + Claude), completing the outcome-selection thread. Task (main open consistency item from `DERIVATION_inverted_gisin.md`): formulate the multi-quantum game and verify it reproduces the ρ-linearity of nonlinear-intensity detectors — two-photon absorption as a linear POVM. This was a genuine falsification risk: two-photon detectors exist and do not signal; if the framework made them ρ-nonlinear, the no-signaling resolution would collapse.*

---

## 1. The N-quantum registry

For an N-quantum state the substrate carries the **joint amplitude** — for two quanta, the symmetric pair registry $\psi(i,j)$ (the same correlated-phase-registry structure the Bell game used across two wings, here for two quanta of one field). Detector stakes are drawn from the registry **sector by sector**:

- **One-photon absorber** at site $i$: stakes = single-quantum marginal $m_i = \sum_j |\psi(i,j)|^2$. After the first commit at $i^*$, the registry renormalizes (resync) and the second game runs on the conditional row $|\psi(i^*,j)|^2 / m_{i^*}$.
- **Two-photon absorber** at site $i$: commits by consuming both quanta — exactly two absorption vertices — so its amplitude carries exactly one factor of the **pair** amplitude $\psi(i,i)$; rate $\propto |\psi(i,i)|^2 = G^{(2)}(i,i)$.

## 2. Sector-linearity theorem (inverted-Gisin Theorem 1, generalized)

In the N-quantum sector, a commit channel consuming $k$ quanta requires exactly $k$ absorption vertices: fewer cannot conserve energy into the $k\hbar\omega$ final state; extra absorb–emit pairs return quanta to the pool (exchange, not commitment); higher pure-absorption orders are kinematically blocked. Hence its rate is **exactly linear in the $k$-quantum coincidence weight $|\psi^{(k)}|^2$** — never a higher power of anything. Every $G^{(k)}$ is a linear functional of $\rho$; per-configuration outcome statistics are Born (the martingale theorems); mixtures average affinely over substrate configurations. Therefore:

$$\textbf{All outcome statistics are affine in } \rho, \textbf{ for arbitrary detectors, in every quantum sector.}$$

A "nonlinear" (two-photon) detector is nonlinear in classical *intensity* only; in the game this just means its stakes are drawn from the pair registry instead of the intensity landscape — drawn *linearly from $\rho$* either way. No-signaling therefore extends to all detector types, closing the last gap in the inverted-Gisin resolution. Decomposition-independence of mixed states follows for free: since per-configuration statistics are exactly Born (linear in $|\psi_k\rangle\langle\psi_k|$), any convex decomposition of the same $\rho$ yields the same predictions.

Corollary (bookkeeping): the "nonlinear-commit deviation channel" dies in the multi-quantum sector too, by the same kinematics that killed it for single quanta. **The framework's surviving Born-deviation predictions are now exclusively Stage-2 (fairness) effects** — correlated-noise atom arrays and pre-cohered ensembles.

## 3. Sequential commits reproduce Glauber counting

First commit: fair game + rate-linear commitment on the marginals ⇒ $P(i) = m_i$ (Born marginal). Resync ⇒ conditional game ⇒ $P(j|i) = |\psi(i,j)|^2/m_i$. Joint:

$$P(i,j) = m_i \cdot \frac{|\psi(i,j)|^2}{m_i} = |\psi(i,j)|^2$$

— **Glauber's joint photodetection distribution**, from the same marginal-times-conditional structure that produced the Bell correlations. The framework's photodetection theory is standard quantum optics at the statistics level, with the selection mechanism underneath.

## 4. Numerical checks (`multiquantum_rho_linearity.py`, 2026-07-20)

Two site-localized modes, **identical mean intensities (50/50), opposite pair correlations**:

| state | game: same-site / split | QM (Glauber) | naive mean-intensity model |
|---|---|---|---|
| $\|1,1\rangle$ (anti-correlated) | 0.000 / 1.000 | 0 / 1 | 0.5 / 0.5 ✗ |
| $(\|2,0\rangle{+}\|0,2\rangle)/\sqrt2$ (bunched) | 1.000 / 0.000 | 1 / 0 | 0.5 / 0.5 ✗ |

The game reproduces perfect anti-bunching and perfect bunching; any intensity-only model fails both. **Two-photon absorbers:** registry stakes give *zero* clicks on $|1,1\rangle$ (QM-correct — $\psi(i,i) = 0$) and 50/50 on the bunched state (game: 0.496/0.504); a naive intensity² model would falsely click on $|1,1\rangle$ — exactly the ρ-nonlinear error the registry formulation avoids. **Generic 3-site pair state:** game joint matches $|\psi_{ij}|^2$ to 0.0023 (statistical floor, 60k trials). **Mixture affinity:** $P(\tfrac12\rho_a + \tfrac12\rho_b)$ matches the average of the pure-state predictions to 0.0006.

## 5. Status and open items

The multi-quantum consistency check **passes**: the framework's game, with stakes drawn sector-by-sector from the joint registry, is ρ-linear by construction and reproduces Glauber counting statistics including bunching/anti-bunching. Both potential falsifiers (false two-photon clicks on anti-correlated states; correlation-blind joint statistics) are avoided — not by tuning, but because the registry formulation is the only one consistent with the framework's own Bell-game structure.

Remaining items (all checks/formalizations, no known theory gaps):
1. Full POVM completeness: arbitrary detector arrays mixing one- and two-photon absorbers competing on one state (plausible via total-rate bookkeeping; not yet formalized).
2. Induction to general N and to continuous-mode Glauber theory.
3. Signaling analysis of the two surviving Stage-2 deviation channels (atom arrays, pre-cohered) — now the only deviation predictions left.
4. Improper mixtures: marginals of entangled states already handled by the Bell game; a unified statement would be tidy.

---

*Glossary:* **Glauber counting distribution** — standard quantum optics' joint photodetection probability, $\propto$ normally-ordered field correlations $G^{(k)}$. **Bunching/anti-bunching** — photons arriving together/apart beyond classical expectation; the canonical signature that detection statistics read correlations, not just intensity. **POVM** — the most general quantum measurement, always linear in ρ. **Pair registry** — the substrate's stored joint amplitude $\psi(i,j)$; the two-quantum analogue of the Bell pair's shared phase thread.
