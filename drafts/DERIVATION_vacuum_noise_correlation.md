# DERIVATION — Spatial Correlation of Vacuum Noise and the Fairness of Outcome Selection

*2026-07-20 (JB + Claude), third installment of the outcome-selection thread (after `NOTE_born_gamblers_ruin.md` and `DERIVATION_slaved_phase_subthreshold.md`). Question: the fairness theorem requires site-independent noise; vacuum noise is spatially correlated on the λ/2 scale — how much Born violation does that cause in real geometries, and what protects real detectors?*

**TL;DR: the sinc zero does NOT protect fine fringes (early guess overturned by computation). What protects solid-state detectors is the *locality of the dominant noise*: the deviation scales linearly with the correlated fraction $f = \Gamma_{\rm rad}/\Gamma_{\rm total} \sim 10^{-6}$, giving $\sim10^{-7}$ violations. Radiatively-limited detectors (atom arrays) are NOT protected — large, polarization-dependent deviations predicted there, connecting to known collective sub/superradiance physics.**

---

## 1. General drift formula under correlated noise

With amplitude-linear vacuum coupling, $de_i = \sigma\sqrt{e_i}\,dW_i$, and correlations $\langle dW_i\,dW_j\rangle = C_{ij}\,dt$, Itô's lemma on the shares $s_i = e_i/E$ gives

$$\boxed{\;\mathbb{E}[\dot s_i] = \frac{\sigma^2}{E^2}\Big[\,s_i\big(\sqrt{e}\cdot C\cdot\sqrt{e}\big) - \sqrt{e_i}\,\big(C\sqrt{e}\big)_i\Big]\;}$$

Limits: $C = I$ ⇒ drift $\equiv 0$ (fairness theorem recovered); $C_{ij} = 1$ ⇒ the common-mode catastrophe. Two sites with correlation $c$: $\dot s_1 \propto c\,\sqrt{e_1e_2}\,(e_1 - e_2)$ — **linear in $c$**; rich-get-richer for $c>0$, equalizing for $c<0$. Linearity in $C$ is the load-bearing structural fact (see §4).

## 2. Physical kernels

Vacuum noise filtered near the transition frequency: scalar model $C(\Delta r) = \operatorname{sinc}(k\Delta r)$ (first zero at $\lambda/2$). The vector vacuum (dipole cross-damping, the collective-decay $\Gamma_{12}/\Gamma$ of Dicke physics) depends on the angle $\theta$ between polarization and separation: at $\Delta r = \lambda/2$,

$$c_{\perp} = -\tfrac{3}{2\pi^2} \approx -0.15 \qquad (\theta = 90^\circ), \qquad
c_{\parallel} = +\tfrac{3}{\pi^2} \approx +0.30 \qquad (\theta = 0^\circ).$$

The sign of the correlation — hence of the Born deviation — **flips with polarization** at fine separations.

## 3. Numerics (`vacuum_correlation_born.py`, 2026-07-20)

1D dense array (site spacing ≪ λ), fringe pattern $I(x) = 1 + 0.8\cos(2\pi x/d)$, two periods.

**Study 1 — initial drift of the bright-region share** (units $\sigma^2/E$; fully-common reference = 8.0):

| $d/\lambda$ | scalar | ⊥ pol | ∥ pol |
|---|---|---|---|
| 0.5 | **4.06** | 3.44 | 5.29 |
| 1.0 | 1.89 | 1.30 | 3.05 |
| 2.0 | 0.16 | −0.10 | 0.69 |
| 3.0 | 0.002 | −0.12 | 0.25 |
| 10 | 0.004 | −0.002 | 0.015 |

**The sinc zero does not save fine fringes**: a continuum of sites spans all separations, so the bright fringe behaves as one internally-correlated blob adjacent to the dim blob — at $d = \lambda/2$ the drift is *half the fully-common catastrophe*. Decay is steep for $d \gtrsim 2\lambda$; the ∥-pol kernel (with its $1/r^2$ near-field tail) decays slowest; ⊥-pol goes *negative* (equalizing) at intermediate $d$.

**Study 2 — full correlated game** ($f = 1$, scalar kernel; deviation of P(winner ∈ bright half) from Born, with independent-noise control):

| $d/\lambda$ | dev (correlated) | dev (control) |
|---|---|---|
| 0.5 | **+0.203** | +0.010 |
| 1.0 | +0.071 | −0.008 |
| 2.0 | −0.012 | +0.023 |
| 5.0 | −0.032 | +0.005 |

Fine fringes: ~20% bright-favored violation. At $d \gtrsim 2\lambda$ the game shows small *negative* residuals (few %, at $f=1$) beyond the $t=0$ drift — an evolved-configuration effect (a concentrating leader loses the correlated-cluster noise amplification $\propto\sqrt{m}$ that distributed clusters keep); noted, not fully analyzed. Common noise also produces collective no-click events (whole-patch death) — a toy-level curiosity possibly relevant to detector-efficiency modeling.

**Study 3 — mixed kernel** $C = (1-f)I + fC_{\rm scalar}$ at $d = \lambda/2$ (the worst case):

| $f$ | 1.0 | 0.3 | 0.1 | 0.03 | 0 |
|---|---|---|---|---|---|
| dev | +0.209 | +0.034 | +0.009 | +0.011 (floor) | +0.001 |

**Deviation ∝ $f$**, as linearity of the drift in $C$ demands (values ≤ 0.01 are at the 2000-trial Monte-Carlo floor).

## 4. The physical resolution: locality of the dominant noise

The noise that drives the exchange game has two components: a **local** part (phonon/carrier scattering in a solid — nm correlation length, width 10–100 meV, $\Gamma_{\rm loc}\sim10^{13\text{–}14}\,{\rm s^{-1}}$) and a **radiative** part correlated on the λ/2 scale ($\Gamma_{\rm rad}\sim10^{8}\,{\rm s^{-1}}$). Only the radiative fraction

$$f = \frac{\Gamma_{\rm rad}}{\Gamma_{\rm total}} \sim 10^{-6} \quad(\text{solid-state detector})$$

carries dangerous correlations. By Study 3's linear scaling, worst-case (λ/2 fringe) Born violations in a solid detector are $\sim 0.2\,f \sim 10^{-7}$. **Solid-state detectors are protected by the locality of their noise, not by the geometry of the vacuum.** This also retroactively justifies the independent-noise assumption of the fairness theorem for every realistic solid-state scenario, closing open item 2 of the slaved-phase derivation.

Consistency: sub-λ standing-wave detection in emulsions and atomic systems (Wiener 1890 onward) shows no gross fringe distortion — consistent with local-noise-dominated absorbers.

## 5. Where deviations survive: radiatively-limited detectors

For absorbers whose linewidth is *purely radiative* ($f \to 1$) — free-space **atom arrays** (optical-tweezer arrays, small Dicke samples) — the full correlated-noise deviation applies: tens of percent at sub-λ site spacing, polarization-dependent in sign (§2). This is not an embarrassment but a **connection**: collective modification of absorption in dense radiatively-coupled ensembles is established physics (sub/superradiance). The framework's claim is that outcome *statistics* on such arrays deviate from naive per-site Born weighting in a way controlled by the collective-decay matrix $\Gamma_{ij}$ — a quantitative, testable prediction with a distinctive **polarization signature**: rotate the drive polarization relative to the array axis and the sign of the deviation flips (⊥: dim-favored, ∥: bright-favored, at spacing where the kernels differ in sign).

## 6. Caveats and open items

1. 1D dense-array toy; 2D detector-face geometry and depth not yet modeled.
2. The evolved-configuration negative residual at $d\gtrsim2\lambda$, $f=1$ (§3, Study 2) deserves its own analysis (cluster-concentration effect).
3. Kernel refinements: in-medium (polariton) correlation length λ/n; half-space (one-sided illumination) mode restriction.
4. The atom-array prediction should be checked against existing collective-absorption experiments before being claimed as novel.
5. Remaining from the thread: Stage-3 commit rate at layer entry (broadband solid detectors); Bell pairs on the joint substrate; $e \propto A^2$ within the ZBW model proper.

---

*Glossary:* **collective/cross-damping $\Gamma_{ij}$** — the off-diagonal decay rate coupling two dipoles through the shared vacuum; the mathematical object behind Dicke sub/superradiance. **Sub/superradiance** — suppressed/enhanced collective emission (and absorption) when emitters share vacuum modes within ~λ. **Correlated fraction $f$** — share of the total noise power carried by the spatially-correlated (radiative) channel.
