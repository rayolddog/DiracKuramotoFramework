# NOTE — Born as a Fair Gambler's Ruin over Deposited Energy

*Session walkthrough, 2026-07-20 (JB + Claude). Status: derivation skeleton with numerical support; open problems listed at the end. Refines the honest negative recorded in the Born-measure status: the squaring is no longer imported — it enters twice, both times physically.*

---

## 1. The construction, step by step (as it emerged in dialogue)

**Step 1 — Capture is plural.** A single photon incident on a detector interacts coherently with *all* bound electrons in the illuminated patch, not with one. The one-photon-one-electron Feynman vertex is one term in a sum over every candidate electron; reducing the sum to a single diagram *already uses* the Born rule. So the single-electron character of the event must be the *output* of selection, never an input assumption. Discipline: **keep the plural alive until the dynamics kills it.**

**Step 2 — Tipping (the MRI analogy, load-bearing).** Each electron in the patch is driven like a spin under an RF pulse: pulled out of phase equilibrium with its neighbors, with the drive's phase imprinted on it, by an amount proportional to the *local* field amplitude $A_i$. The energy stored in a displaced oscillator is quadratic in the displacement, so the deposited "tip energy" is

$$e_i \propto A_i^2 .$$

*This is the first appearance of the squaring, and it is physical:* elementary oscillator energetics, not an axiom. (Same fact the holography route found as energy density $=|\mathrm{amp}|^2$; same fact as NMR's small-tip excitation $\propto \sin^2(\theta/2)\approx(\theta/2)^2$.) For a resonant secular drive the tip *magnitude* is phase-independent — the relative phase's job comes later.

**Step 3 — The vacuum seed.** The quantum vacuum contributes a small, structureless random deviation to the interaction. It is a symmetry-breaking tie-breaker, **not** a hidden variable: it carries no outcome information, and its magnitude drops out of the statistics (a bifurcation seed only needs to be nonzero). Bell guardrail: in an entangled-pair experiment this randomness must be a fluctuation of the *shared* substrate, not two private coin flips — else it's an LHV and dead on arrival.

**Step 4 — "It takes two to tango" (JB's key ingredient).** The detector electrons' internal clocks are mutually incoherent — random phases, at most infinitesimal pre-existing coherence. Energy exchange between two coupled oscillators is directional only if they hold a definite phase relation (flow $\propto \sin\Delta\varphi$). With incoherent, drifting clocks, $\langle\sin\Delta\varphi\rangle = 0$:

> **Clock incoherence kills the drift.** No electron is *systematically* favored in the tug-of-war for the quantum.

*This is the second appearance of phase-randomness doing real work, and it is the missing symmetry:* the generic disease of winner-take-all competition (laser mode competition) is exponential favoritism toward the largest amplitude; uniform relative phase is precisely the condition that zeroes the favoritism. (Radiology echo: Rician noise in magnitude MRI — discard phase and signal can only enter through $A^2$.)

**Step 5 — Selection as gambler's ruin.** Stage 2 is not a one-shot comparison but a *prolonged stochastic energy exchange* among the tipped electrons, mediated by the substrate, seeded by vacuum noise:

- The exchanged quantum per step scales with the stakes, $\delta \propto \pm\,\mathrm{step}\cdot\min(e_i,e_j)$, fair sign. A site relaxed back to equilibrium ($e\to 0$) naturally drops out — zero is absorbing.
- An electron that accumulates the full quantum crosses the **sync lock threshold** (goes on-shell; critical slowing makes it irreversible) — that's the other absorbing barrier, and it *is* the discreteness.
- In between, by Step 4, each $e_i$ evolves with **zero drift** — a *martingale* ("fair game": fluctuations redistribute, nothing systematically favors the leader).

**Step 6 — The theorem.** A bounded martingale run to absorption obeys the *optional stopping theorem*: the expected final value equals the initial value. Since the final value of $e_i$ is either $E$ (electron $i$ locked) or $0$,

$$P(i \text{ wins})\cdot E = e_i(0) \quad\Longrightarrow\quad P(i \text{ wins}) = \frac{e_i(0)}{E} = \frac{A_i^2}{\sum_j A_j^2}.$$

**Exactly.** Any number of sites, all orders, no expansion. Normalization is automatic because exactly one quantum is conserved through the game. The Born rule is the fair-lottery theorem applied to deposited oscillator energy.

---

## 2. Numerical checks (Monte Carlo, this session)

**One-shot selection FAILS (diagnostic).** Winner $=\arg\max_i |A_i\cos\theta_i|$, $\theta_i$ uniform: close to Born for 2 sites ($0.791$ vs $0.800$ at $A=[2,1]$ — a near-coincidence of arcsine statistics) but badly winner-favoring for many sites: one bright site ($A=3$) among nine dim ($A=1$) wins **79%** vs Born's **50%**. Extreme-value selection reintroduces the drift. The tango overlap must *not* pick the winner directly.

**Biased exchange FAILS (also diagnostic).** Fixed-size steps clipped at zero make empty sites reflecting (they can only gain) — an upward drift for small stakes. The 3-site case then gives $[0.46, 0.27, 0.26]$ vs Born $[0.64, 0.29, 0.07]$. The martingale property is knife-edge, and the sims feel it.

**Fair exchange PASSES.** Stakes-scaled fair steps, absorption at $0.95E$, 3000 trials/config:

| Config $A$ | Empirical | Born | max diff |
|---|---|---|---|
| $[2,1]$ | $[0.826, 0.174]$ | $[0.800, 0.200]$ | $0.026$ |
| $[3,2,1]$ | $[0.658, 0.283, 0.059]$ | $[0.643, 0.286, 0.071]$ | $0.015$ |
| $[1{\times}9,\,3]$ | dim $\approx 0.052$ ea, bright $0.525$ | $0.056$ ea, $0.500$ | $0.025$ |

Residual $\sim$2% is finite step/threshold artifact; the theorem gives exactness in the continuum limit.

### Simulation code (preserved here; originals in session scratchpad)

```python
# gambler_ruin_born3.py — fair stakes-scaled exchange vs Born
import numpy as np
rng = np.random.default_rng(11)

def fair_exchange_batch(e0, ntrials=3000, step=0.1, thresh=0.95, maxit=400000):
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    for it in range(maxit):
        if not active.any(): break
        idx = np.where(active)[0]
        i = rng.integers(0, n, size=idx.size)
        j = (i + rng.integers(1, n, size=idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        e[idx, i] -= d;  e[idx, j] += d
        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    w = winners[winners >= 0]
    return np.bincount(w, minlength=n) / max(len(w), 1)

for amps in ([2.,1.], [3.,2.,1.], [1.]*9+[3.]):
    A = np.array(amps); e0 = A**2/np.sum(A**2)
    print(np.round(fair_exchange_batch(e0), 4), " Born:", np.round(e0, 4))
```

```python
# tango_selection.py — one-shot max-overlap selection (the FAILING rule, kept as control)
import numpy as np
rng = np.random.default_rng(7)
def oneshot(amps, ntrials=2_000_000):
    A = np.asarray(amps, float)
    th = rng.uniform(0, 2*np.pi, size=(ntrials, len(A)))
    w = np.argmax(np.abs(A*np.cos(th)), axis=1)
    return np.bincount(w, minlength=len(A))/ntrials
```

---

## 3. Credit and precedent

The martingale $\Rightarrow$ Born argument is **Philip Pearle's** (gambler's-ruin dynamical reduction, 1976; later CSL). CSL *engineers* the noise to have the zero-drift property and leaves its physical origin open. What the DK construction adds is a physical identification of every element:

| Gambler's-ruin element | DK realization |
|---|---|
| The stakes | tip energy $e_i \propto A_i^2$ (oscillator energetics) |
| The noise | unlocked vacuum modes (shared substrate, not private) |
| The fairness (zero drift) | detector clock incoherence: $\langle\sin\Delta\varphi\rangle=0$ |
| Absorbing barrier (win) | sync lock threshold (on-shell, critical slowing) |
| Absorbing barrier (lose) | relaxation back to bulk equilibrium |
| Normalization | one conserved quantum |

---

## 3b. Addendum (same session) — the rich-get-richer problem and its resolution

**Threat, made quantitative.** An electron holding $e<E=\hbar\omega$ is off-shell by $\Delta E$, slips on $\tau\sim\hbar/\Delta E$, and partially entrains per Adler: bias $\beta(e)\sim\min(1,\hbar K/(E-e))$; full lock engages in a boundary layer of fractional width $w=K/\omega$. Simulation (`soft_threshold_born.py`) of the game with this bias: Born deviation grows **sublinearly** ($\sim w^{0.4}$ in this bias model) — $w=0.003$ already gives 3.7% deviation; $w=0.1$ gives 18–32%. The fair control ($w=0$, absorb at $0.995$) matches Born to $0.07\%$. Sharpness is *required*, not optional.

**Resolution (JB): orbital discreteness.** A bound electron has **no resonant mode below the transition energy** — nowhere to bank partial winnings. Sub-threshold energy exists only as *virtual, slaved polarization*: a forced response phase-slaved to the common driving field, with no autonomous clock. A slaved oscillation confers no competitive advantage (it re-radiates coherently with the field, identically for all sites) and has no ratchet (virtual winnings decay on $\tau$). An autonomous clock — the thing that could bias exchanges — appears only when a *real* state is populated, which takes the full quantum. **Level discreteness enforces the sharp threshold.** Residual softness = final-state linewidth: $w=\Gamma/\omega\sim10^{-6}\!-\!10^{-8}$ for real photodetectors $\Rightarrow$ Born deviations $\lesssim10^{-3}$ by the worst-case sim scaling (the physical bias lacks the sub-threshold entrainment tail the sim assumed, so smaller still).

**Consistency check.** The absorber where rich-get-richer *would* operate — a gapless continuum (free electron, arbitrary energy banking) — is exactly the system where single-photon absorption is kinematically forbidden (free electrons scatter, never absorb). "No gap $\to$ no sharp lock $\to$ no discrete outcome" agrees with QED kinematics.

**Second testable hook.** Soft-threshold systems (strong coupling / broad lines: circuit QED with $g/\omega\sim10^{-2}$) should show *percent-level* Born deviations scaling with $w=\Gamma/\omega$.

## 4. Open problems (the honest list)

1. **Fairness during late-game locking — resolved in outline, quantify next.** Rich-get-richer is disarmed by orbital discreteness (no autonomous clock below the full quantum; see §3b). Remaining work: make the slaved-phase argument quantitative in the ZBW/Adler model, and recompute the deviation scaling with a gapped (tail-free) bias profile.
2. **Derive $e_i\propto A_i^2$ inside the ZBW model proper** (currently generic-oscillator energetics).
3. **Bell pairs:** for entangled photons the exchange game must run on the *joint* substrate state across both wings — connect to the two-stage/bulk-resync picture.
4. **Role split to keep straight:** the tango overlap (relative phase) sets the *fairness* of the game, not the initial shares; the amplitude sets the shares. Conflating these reproduces the failed one-shot rule.

## 5. Testable hook

Fairness rests on detector clock incoherence — a physical, molecular-chaos-like assumption, so it can *fail* in engineered conditions: **a detector whose electron ensemble is pre-cohered (phased) should show deviations from Born statistics.** Worth a feasibility think: what system has opticaly pumpable, phase-lockable absorbers? (Superradiant/Dicke-prepared ensembles are the obvious candidate.)

---

*Glossary (per standing convention):* **martingale** — a stochastic process whose expected next value equals its current value ("fair game," zero drift). **Optional stopping theorem** — for a bounded martingale, the expected value at a stopping time equals the initial value; the reason a fair gambler's win probability equals their share of the total capital. **Absorbing barrier** — a state the process cannot leave (here: locked, or fully relaxed). **Arcsine distribution** — the distribution of $\cos\theta$ for uniform $\theta$; piles up near $\pm 1$. **Rician noise** — magnitude-image noise in MRI; what you get when phase is discarded and signal enters only through intensity. **Extreme-value selection** — picking the maximum of many random draws; statistics dominated by tails, hence winner-favoring.
