# DERIVATION — Signaling Analysis of the Stage-2 Deviation Channels

*2026-07-20 (JB + Claude), final pre-paper check of the outcome-selection thread. Task: determine whether the two surviving Born-deviation predictions (correlated-noise atom arrays; pre-cohered ensembles — both Stage-2 fairness effects) enable signaling, what protects existing experiments, and what the falsifiable configuration is.*

---

## 1. The port decomposition: which deviations can signal at all

Stage-2 deviations bias *which site within a detector patch* wins. But the outcome carrying entanglement information is the **port** (which analyzer output fired). Summing the correlated-noise drift formula over ports (with cross-port noise uncorrelated — ports are macroscopically separated):

$$\dot S_A \;\propto\; q_B\,S_A - q_A\,S_B, \qquad q_P \equiv \textstyle\sum_{i,j\in P} C_{ij}\sqrt{e_ie_j},$$

giving two structural results:

**Result 1 (within-port protection).** If the two ports have matched collective-noise structure ($q_A/S_A = q_B/S_B$ — same geometry, same internal correlation), the port-level share is drift-free: **port statistics remain exactly Born even while which-atom statistics inside each port deviate arbitrarily.** Within-port deviations never signal. Every existing experiment uses structurally symmetric ports — hence no deviation and no signaling anywhere in the record. ✓

**Result 2 (mismatched ports — and no symmetry protection).** If the ports differ in collective structure (dense sub-λ array vs sparse; one port phase-locked), the port game acquires drift and $P'(\text{port}) \ne$ Born. Crucially, unlike the commit-channel analysis, **maximal entanglement does not protect**: the asymmetry lives in the *detector*, not the state. With $P'(+) = \tfrac12 + \delta$ on a maximally entangled pair, the far wing's marginal becomes

$$M(\alpha) = \tfrac12 + \delta\cos 2\alpha \cdot P_{\rm first}$$

— dependent on the deviant wing's *setting*. Direct signaling at amplitude $\sim\delta/2$, no partial entanglement needed.

## 2. Numerics (`stage2_port_signaling.py`): the port-level bias, quantified

Two ports × 4 sites, port + internally noise-correlated at level $c$, port − independent, fair $\sqrt e$ exchange otherwise:

- **Mismatch scaling is linear and clean:** at $S_+ = \tfrac12$, deviation $= -0.025, -0.068, -0.140$ for $c = 0.1, 0.25, 0.5$ ⇒ $\boxed{\kappa \approx -c}$ (bias parameter = within-port correlated-fraction mismatch), with $P'(S) \approx S + \kappa S(1-S)$. Sign: the internally-correlated port is **suppressed** (Jensen/concavity: correlated noise inflates the port's energy variance, and shares are concave in energy).
- **Matched-ports control** ($c = 0.5$ both): dev $= +0.0003$ at $S = \tfrac12$; small equalizing residual $\pm0.027$ at $S = 0.2/0.8$ — an evolved-configuration effect in the family of the known cluster residual (open item), negligible at physical correlation levels.
- **Degenerate limit** ($c = 1$): perfectly common noise preserves within-port ratios exactly — the port can never concentrate onto one site and either collectively dies or loses (P(port+) → 0, with a **strongly state-dependent no-click rate**: 5% at $S_+ = 0.2$ vs 47% at $S_+ = 0.8$). Physically an artifact softened by any independent noise component, but it flags a second observable: **state-dependent detection inefficiency**, which standard QM's constant-efficiency model cannot produce and which violates fair-sampling in a specific, testable way.

## 3. Magnitudes: why all existing physics is safe

The port bias is $\kappa \approx -\,\Delta c_{\rm eff}$, where $\Delta c_{\rm eff}$ = difference between ports of (correlated noise fraction × internal correlation). For every real detector, the correlated (radiative) noise fraction is $f \sim 10^{-6}$ (locality protection, `DERIVATION_vacuum_noise_correlation.md`) ⇒ $\kappa \lesssim 10^{-6}$ ⇒ far-wing marginal shifts $\lesssim 10^{-7}$. Invisible everywhere, consistent with all Bell data and all detector calibrations. The channel becomes live only for **engineered radiative-dominated absorbers with deliberately mismatched ports** — a device nobody has built.

## 4. The fork (must be stated in Paper 1)

For an asymmetric-collective detector in a Bell setup, the framework as currently formulated predicts a real far-wing marginal shift — in-principle superluminal signaling. Two readings:

- **Radical reading:** the prediction is genuine; an asymmetric-array Bell experiment would show marginal shifts $\sim\kappa/2\cdot\cos2\alpha$ (and CHSH distortion), overturning no-signaling at the engineered-detector level. Extraordinary claim; nothing in existing data supports or excludes it (the configuration is unexplored).
- **Protective reading (more likely, in our judgment):** a deeper fairness principle protects port-level statistics even for asymmetric collectives — e.g., the same substrate dynamics that generates the correlated noise also renormalizes uptake and decay in a compensating way (our drift analysis treats noise correlation in isolation; a full dynamical model of the asymmetric detector could close the channel the way rate-linearity closed the commit channel). If so, the Stage-2 deviation predictions close entirely and the framework becomes empirically equivalent to QM for all detector configurations — with the equivalence *derived*, which would itself be the strongest form of the program.

The honest position: the framework currently *cannot decide* between these; the analysis above defines exactly what a resolution must do.

## 5. The tabletop discriminator (no Bell test needed)

The two readings — and framework vs standard QM — separate in a **single-photon experiment**: feed one photon at a variable beam-splitting ratio $S$ into a two-port detector whose ports have mismatched collective structure, and measure the port statistics $P'(S)$:

- **Standard QM:** $P'(S) = \eta_+ S / (\eta_+ S + \eta_-(1-S))$ — a *constant-efficiency* rescaling, no curvature beyond it, no state-dependent no-click anomaly.
- **Framework (current form):** $P'(S) = S + \kappa S(1-S)$ — genuine curvature with $\kappa \approx -\Delta c_{\rm eff}$, plus state-dependent no-click rate.

Curvature beyond the efficiency model = the signature. This is a table-top pre-test of the framework's most radical corner, properly ordered *before* any Bell-configuration drama.

## 6. Pre-cohered channel

Same port structure: **symmetric** pre-coherence (both ports phase-locked identically) leaves port statistics fair — protected; **differential** pre-coherence (one port locked to an external reference, the other not) is a $\Delta c$ mismatch and inherits everything above. Caveat: maintaining pre-coherence requires continuous driving (a local-oscillator field), which adds quanta and takes the detector out of the single-quantum sector — the kinematic protections must be re-examined in that setting (noted, not done).

## 7. Status

Pre-Paper-1 checklist complete. Bookkeeping for the paper: (i) all existing experiments protected by port symmetry + noise locality, with margins of $10^6$; (ii) the surviving falsifiable content of the framework is concentrated in ONE experimental family — asymmetric-collective two-port detectors — with a cheap tabletop discriminator (§5) preceding any Bell version; (iii) the framework owes a resolution of the §4 fork, and "deeper fairness principle" is the designated open problem inherited by future sessions (alongside GHZ, e ∝ A² in ZBW proper, and the cluster residual, which reappeared here in the matched-port control).
