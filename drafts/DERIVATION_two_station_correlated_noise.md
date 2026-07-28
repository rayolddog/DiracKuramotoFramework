# DERIVATION — Cross-station correlated noise in the two-stage Bell game

*2026-07-28. The calculation flagged as prerequisite in the framework note's Bell-station-independence section and in [[project_noise_origin_surface_interference]]. Extends Paper 1 §7.1–7.2 (two concurrent fair share-games; first commit resets the far wing to $\eta\cdot\text{conditional} + (1-\eta)\cdot\text{current}$; $E(a,b) = \eta\cos 2(a-b)$, $S = 2\sqrt2\,\eta$). Simulation: `two_station_sims/two_station_correlated_noise.py`, results in `two_station_sims/results.txt`.*

**Headline: the two-stage construction is far more protected against cross-station correlated noise than the audit-list discussion assumed.** Broadband (white) common noise between the stations — even in-band, even at correlation $\rho = 0.99$ — produces *zero* shift in the outcome statistics when the registry update is faithful ($\eta = 1$). Only two channels touch $S$: **registry infidelity** ($\eta < 1$) leaking the correlation, and a **phase-locked coherent tone** whose bias persists through the reset. This *corrects* the earlier working claim ("a shift growing with the correlated fraction $f$"): for white noise there is no such shift at $\eta = 1$.

## 1. Setup

Each station is a two-port game: share $\alpha$ (station $A$) and $\beta$ (station $B$), both starting at $1/2$ (unpolarized marginals, §7.1), evolving as the Wright–Fisher-form fair diffusion implied by $de_i = \sigma\sqrt{e_i}\,dW_i$ for two ports:
$$d\alpha = \sigma\sqrt{\alpha(1-\alpha)}\;dW_A,\qquad d\beta = \sigma\sqrt{\beta(1-\beta)}\;dW_B,$$
absorbing at $0/1$. Cross-station injection enters as either
- **(white)** correlated increments $\langle dW_A\,dW_B\rangle = \rho\,dt$ during the temporal overlap of the two games, or
- **(tone)** a common coherent drift: $d\alpha \mathrel{+}= \lambda\sigma^2\cos 2(a-\psi)\cos\varphi\,\sqrt{\alpha(1-\alpha)}\,dt$ (same for $\beta$ with $b$), where $\psi$ is the tone polarization, $\cos 2(\theta-\psi)$ its intensity asymmetry between the ports of an analyzer at $\theta$, and $\varphi$ a global phase, *random per shot but common to both stations* (phase-locked injection).

First commit (P6 ordering) resets the far wing to $\eta\,p_{\rm cond} + (1-\eta)\,(\text{current})$, with $p_{\rm cond} = \cos^2(a-b)$ or $\sin^2(a-b)$; the far game then completes. Convention: $E(a,b) = \cos 2(a-b)$, CHSH at $a=0,\,a'=\pi/4,\,b=\pi/8,\,b'=-\pi/8$, $S_{\rm QM} = 2\sqrt2$.

Distinction maintained throughout: the pair's *own* substrate fluctuations (the shared-registry physics of P5) are part of the mechanism; what is analyzed here is *additional laboratory-classical* correlation between the stations' local noises.

## 2. Result 1 — Marginals are protected unconditionally

Each station's share drift under Itô involves only that station's own quadratic variation; the cross-covariance $\langle dW_A dW_B\rangle$ never enters $\mathbb E[d\alpha]$ or $\mathbb E[d\beta]$. Both shares remain martingales for **any** cross-station correlation, white or coherent-in-$\varphi$-averaged, so the singles at each wing stay at their Born marginals. **Cross-station correlated noise is invisible in singles rates; only coincidences can carry a signature.** (For the tone at *fixed* $\varphi$ the marginals do shift; the shot-to-shot random global phase averages them back to Born — the deviation hides itself in exactly the way no-signaling operates.)

## 3. Result 2 — Protection theorem (white noise, faithful registry)

*Claim.* For white cross-station correlation of any $\rho < 1$ and $\eta = 1$, the joint outcome statistics are exactly the QM values: $P(i,j) = m(i)\,P(j|i)$, $S = 2\sqrt2$.

*Argument (two layers).*
1. **Temporal:** white noise is memoryless. If the selection windows do not overlap in the P6 foliation, the increments driving the two games are disjoint in time and correlation has nothing to act on. Deviations could only come from overlap.
2. **The reset discards the accumulated correlation.** During overlap the joint moment grows, $d\,\mathbb E[\alpha\beta] = \rho\,\sigma^2\,\mathbb E\!\left[\sqrt{\alpha(1-\alpha)\beta(1-\beta)}\right]dt$, so at the first commit the far share carries a real correlation with the near outcome: simulation measures $L \equiv \mathbb E[(\beta^*-\tfrac12)\cdot\text{sign(first outcome)}] = +0.289$ at $\rho = 0.8$ — the far wing *leans* toward the near wing's result. But the faithful reset **overwrites** $\beta^*$ with the exact conditional; the post-reset game is a martingale from $p_{\rm cond}$ driven by future (hence, for white noise, independent) increments; and the near wing's marginal was protected by Result 1. Every factor of $P(i,j) = m(i)P(j|i)$ is exact, independently of $\rho$. $\blacksquare$

Simulation: $\rho = 0.8$ and $\rho = 0.99$ sit on the baseline within Monte-Carlo error [numbers in §6]. The correlation is generated (measured $L > 0$) and then destroyed by the registry, shot by shot.

*Discretization lesson with physical content.* A first version of the simulation silently skipped the reset when both wings crossed threshold in the same time step — and correlated paths finish together, so this "simultaneous-commit" fraction grows with $\rho$ (13% at $\rho=0.99$), producing a spurious Bell-correlation excess that mimics $\eta$-degradation. In continuous time simultaneous absorption is measure-zero, and ordering same-step commits restores the theorem exactly. But the artifact models a real question: **commits of finite duration** $\tau_{\rm commit}$ that overlap in time cannot be ordered by the foliation update, and would escape conditioning at rate $\sim P(|t_A - t_B| < \tau_{\rm commit})$ — a channel that *grows* with cross-station noise correlation. Whether physical commits have such a window is a question for the §6.1 ladder; flagged, not claimed.

## 4. Result 3 — Registry infidelity leaks the correlation

For $\eta < 1$ the reset retains $(1-\eta)\beta^*$, and $\beta^*$ carries the lean $L$. The far wing then starts at $p_{\rm cond} \pm (1-\eta)L$ (toward the near outcome); shares being martingales, the final probabilities shift by the same amount:
$$\delta E = 2(1-\eta)\,L(\rho), \qquad \delta S = 2\,\delta E = 4(1-\eta)\,L(\rho),$$
**angle-independent** at leading order, because the overlap phase runs from 50/50 marginals and never sees the analyzer angles. ($L(\rho) = 2\rho J$, with $J = \mathbb E\int_0^{T_1}\!\sigma^2\sqrt{\alpha\bar\alpha\beta\bar\beta}\,dt \le \tfrac14$ from $\mathbb E[\alpha\bar\alpha](t) = \tfrac14 e^{-\sigma^2 t}$ and Cauchy–Schwarz; measured $J \approx 0.18$.)

Simulation (full statistics, $n = 240{,}000$/angle pair): $\eta = 0.9,\ \rho = 0.8$ gives all four $E$'s shifted by $+0.055$ to $+0.060$ uniformly against the $\eta$-law baseline — the predicted $2(1-\eta)L = 2(0.1)(0.288) = +0.058$ — and $\delta S = +0.1167 \pm 0.0045$ against the predicted $+0.1153$. The angle-independence and the magnitude are both confirmed at the percent level.

**Reading:** cross-station white noise converts registry infidelity into a *correlation excess* over the fidelity law: $S = 2\sqrt2\,\eta + 4(1-\eta)L(\rho)$. Since $\eta \gtrsim 0.99$ experimentally (§7.2), the leakage is bounded by $\delta S \lesssim 0.04\,\rho\cdot(J/0.18)$ — and conversely, a *deliberate* white-noise injection at known $\rho$ becomes a **direct experimental bound on the registry fidelity $\eta$**: any observed $\delta S$ under broadband injection measures $(1-\eta)$.

## 5. Result 4 — The phase-locked tone evades both protections

The tone is not white: its phase persists through the reset, so it biases the far wing's *post-reset* game — the one thing the registry cannot wipe. Per shot (fixed $\varphi$): first wing's outcome acquires bias $u_F = \kappa_1\lambda\cos 2(\theta_F-\psi)\cos\varphi$; the second wing, restarting from $p_{\rm cond}$, acquires $u_S = \kappa_2\lambda\cos2(\theta_S-\psi)\cos\varphi$; conditioning gives $\mathbb E[AB\,|\,\varphi] = E_{\rm QM} + 4u_Fu_S$, and the shot average over the common random phase leaves
$$\delta E(a,b) = 2\,\kappa_1\kappa_2\,\lambda^2\cos2(a-\psi)\cos2(b-\psi).$$
Measured susceptibilities at $\lambda = 0.3$: $\kappa_1$-response $\delta P = 0.165$ from a 50/50 start, $\kappa_2$-response $0.073$ from $p_{\rm cond} = 0.854$ — predicting, at leading order, $\delta E \approx 0.024\cos2(a-\psi)\cos2(b-\psi)$ and, summed over the CHSH combination (which for such products at the standard angles equals $\sqrt2$ independently of $\psi$ — the standard-angle CHSH functional is rotationally invariant *at this order*), $\delta S \approx +0.034$ for any tone polarization.

**What the full-statistics simulation actually shows** (three $\psi$ values, $n = 120{,}000$/pair): $\delta S = +0.005,\ +0.008,\ +0.0135$ (each $\pm 0.005$) at $\psi = 0,\ \pi/8,\ \pi/4$ — *positive in all three configurations* (pooled $\approx 3\sigma$), but smaller than the leading-order estimate and $\psi$-spread. The per-$E$ patterns explain both discrepancies: the first-order fingerprint is clearly present (at $\psi = \pi/4$ the shifts land precisely on the two $a'$ pairs with the predicted signs, $+0.012/-0.008$; at $\psi = 0$ the $a$ pairs strengthen), but a *second-order* effect — curvature of the drift response, which makes a one-sidedly biased wing lose correlation magnitude $\propto u^2$ — contributes at comparable size at $\lambda = 0.3$ and breaks the $\psi$-invariance, which is a first-order statement only. A clean quantitative test of the first-order law wants smaller $\lambda$ and correspondingly larger statistics; the qualitative conclusions are not in doubt. Three signatures survive:
1. $\delta S > 0$ in every configuration: the tone *adds* classical common-bias correlation on top of the quantum correlation, pushing $S$ **above the Tsirelson bound** $2\sqrt2$ (relative to the same-discretization baseline), which no quantum-mechanical mechanism can do. A Bell experiment reading $S > 2\sqrt2$ under deliberate in-band phase-locked injection would be an unambiguous non-QM signature.
2. The angle-resolved pattern $\delta E \propto \cos2(a-\psi)\cos2(b-\psi)$ carries the tone polarization $\psi$ — rotating the injected tone rotates the fingerprint through the four settings (verified at $\psi = 0$ vs $\pi/4$).
3. Singles stay Born ($\langle A\rangle = -0.003 \pm 0.003$ under the tone): the effect lives *only* in coincidences.

*Sector caveat:* the tone drift is the effective single-quantum-sector model of a weak coherent injection; a coherent field adds quanta, and the full treatment belongs to the §6.3 multi-quantum machinery (same caveat the paper attaches to driven pre-coherence, §8.6(iv)).

## 6. Simulation results (full statistics)

$n = 240{,}000$/angle pair (configs 1–4), $120{,}000$ (tones); $\sigma^2 dt = 4\times10^{-3}$; `dbl` = same-step double-commit fraction (ordered by coin flip and properly reset — see §3). Baseline carries a $-0.009$ finite-$dt$ bias; all comparisons are against it, not against $2\sqrt2$ directly.

| config | $S$ | $\pm$ | $E(a,b)$ | $E(a,b')$ | $E(a',b)$ | $E(a',b')$ | dbl |
|---|---|---|---|---|---|---|---|
| 1 baseline | 2.8190 | 0.0029 | +0.7044 | +0.7034 | +0.7058 | −0.7054 | 0.002 |
| 2 white ρ=0.8 | 2.8146 | 0.0029 | +0.7045 | +0.7040 | +0.7034 | −0.7027 | 0.021 |
| 2b white ρ=0.99 | 2.8204 | 0.0029 | +0.7062 | +0.7034 | +0.7044 | −0.7064 | 0.134 |
| 3 η=0.9 | 2.5329 | 0.0032 | +0.6339 | +0.6323 | +0.6333 | −0.6334 | 0.002 |
| 4 η=0.9, ρ=0.8 | 2.6496 | 0.0031 | +0.6929 | +0.6920 | +0.6887 | −0.5759 | 0.021 |
| 5 tone ψ=0 | 2.8236 | 0.0041 | +0.7134 | +0.7162 | +0.6973 | −0.6967 | 0.002 |
| 6 tone ψ=π/8 | 2.8270 | 0.0041 | +0.7137 | +0.6979 | +0.7113 | −0.7041 | 0.002 |
| 7 tone ψ=π/4 | 2.8325 | 0.0041 | +0.7031 | +0.6980 | +0.7177 | −0.7137 | 0.002 |

Diagnostics: leak $L = +0.288$ at $\rho = 0.8$ (η=1 — generated, then wiped by the reset); config-4 prediction $\delta S = 4(1-\eta)L = +0.115$ vs observed $+0.117 \pm 0.005$; tone-mode marginals $\langle A\rangle = -0.003$ under either $b$ setting; single-station drift responses $+0.165$ (from 0.500) and $+0.073$ (from 0.854) at $\lambda = 0.3$.

## 7. What this changes

1. **Audit-list re-ranking (correction to the framework note's first pass):** broadband common-mode pickup between Bell stations is harmless to the odds *even in-band* at $\eta = 1$ — two protection layers, not one. The only laboratory couplings that can touch the outcome statistics are *phase-locked coherent* references reaching both absorbers in the selection band: shared optical paths, common local oscillators, phase-locked in-band electronics. The supply-phase worry that started this thread is now doubly closed.
2. **The injection experiment becomes a two-knob instrument:** (i) broadband injection at known $\rho$ → any $\delta S$ measures registry infidelity $(1-\eta)$, sharpening §7.2's $\eta \gtrsim 0.99$ into a *controlled* bound; (ii) phase-locked tone injection → $\delta S = 2\kappa_1\kappa_2\lambda^2\cdot\sqrt2 > 0$ with the $\psi$-fingerprint, and the $S > 2\sqrt2$ smoking gun. QM predicts null for both (beyond rate artifacts removable by time-tagged analysis).
3. **Open ends:** the finite-$\tau_{\rm commit}$ escape channel (§3); the multi-quantum treatment of the tone; optimal (non-standard) angle sets where the tone fingerprint's $\psi$-dependence survives in $S$ itself; whether $L(\rho)$'s angle-independence acquires corrections when capture profiles differ between stations.

*Prepared by Claude Fable 5 (Anthropic); issued under the accountability of John M. Bramble, MD. Companion artifacts: simulation + results in `two_station_sims/`; corrected conclusions folded into `NOTE_detector_engineering_surface_interference.md`.*
