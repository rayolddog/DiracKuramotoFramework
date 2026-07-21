# DERIVATION — Slaved Phase Below Threshold, and Fairness from Amplitude-Linear Coupling

*2026-07-20 (JB + Claude), continuation of `NOTE_born_gamblers_ruin.md` §3b. Goal: make the slaved-phase argument quantitative in the ZBW/Adler model — i.e., prove that a sub-threshold virtual polarization exerts no rich-get-richer drift on the exchange game. Outcome: proved, plus a stronger bonus — the martingale (fair-game) property itself is* derived *from the framework's amplitude-linear coupling postulate rather than assumed.*

---

## 1. The slaving proof: no autonomous clock below threshold

**Model.** A sub-threshold ZBW tip is a *driven, damped* mode (no self-sustenance — that is what "off-shell" means). Rotating frame at the substrate/photon frequency; complex amplitude $a = re^{i\varphi}$; detuning $\Delta$; drive $f$ at phase $\varphi_d$; decay $\gamma = \Delta E/\hbar$, the framework's off-shell slip rate (energy–time uncertainty: a state short of the shell by $\Delta E$ persists for $\tau\sim\hbar/\Delta E$).

$$\dot r = -\gamma r + f\cos(\varphi_d-\varphi), \qquad
\dot\varphi = \Delta + \frac{f}{r}\,\sin(\varphi_d-\varphi).$$

**The phase equation is Adler-shaped** ($K_{\rm eff}=f/r$) **but the system is not Adler.** Adler's equation describes a *limit-cycle* oscillator: $r$ frozen at a radius maintained by the oscillator's own gain, phase a *free variable on the circle* (a zero mode). Here there is no gain. In Cartesian coordinates the system is **linear**, with eigenvalues

$$\lambda = -\gamma \pm i\Delta,$$

hence a unique, globally attracting **fixed point**

$$r^* = \frac{f}{\sqrt{\gamma^2+\Delta^2}}, \qquad \varphi^* = \varphi_d - \arctan(\Delta/\gamma).$$

Phase deviations *decay* at rate $\gamma$; the phase never winds and never slips. The Adler entrainment average $\langle\sin\varphi\rangle \approx K/2\Delta\omega$ — the rich-get-richer bias channel — is derived from *running* (winding) phase solutions and **does not apply**: below threshold there are none. The phase is an enslaved coordinate, pinned to $\varphi_d - \arctan(\Delta/\gamma)$ — a value set by the *common* drive and the *common* susceptibility, identical for identical transitions, independent of the site's stored energy.

**Where the free clock emerges.** Autonomy requires the phase to become marginal: $\gamma \to 0$, i.e. $\Delta E \to 0$ — the shell. The phase becomes Adler-susceptible when its restoring rate falls below the coupling, $\gamma \lesssim K$, i.e.

$$\Delta E \lesssim \hbar K \quad\Longleftrightarrow\quad w \equiv \frac{\Delta E_{\rm layer}}{E} = \frac{K}{\omega},$$

recovering the boundary-layer width of NOTE §3b from the opposite direction. **Outside the layer the bias is not merely small — it is structurally absent** (no free phase to entrain). This is the quantitative content of "orbital discreteness enforces sharpness": with no resonant mode below the gap, $\gamma = \Delta E/\hbar$ stays large until the full quantum is nearly assembled.

## 2. The feedback hierarchy: who can get richer?

From $\dot e = 2r\dot r$ with $e = r^2$:

$$\dot e = -2\gamma e + 2f\sqrt{e}\,\cos(\varphi_d-\varphi).$$

| term | scaling in $e$ | effect on the *share* $s_i = e_i/\sum_j e_j$ |
|---|---|---|
| slaved uptake from common field | $\propto \sqrt e$ (drive does work on **amplitude**) | concave ⇒ **equalizing** (toward the drive pattern — which *is* the Born pattern, so harmless while the drive is on) |
| off-shell decay / re-radiation | $\propto e$ | linear ⇒ exactly **share-neutral** |
| vacuum noise (amplitude-linear coupling) | work $\propto\sqrt{e}\,\xi$ ⇒ energy variance $\propto e$ | **share-neutral** (theorem below) |
| autonomous / stimulated gain | $\gtrsim e$ | **share-amplifying** — exists only above threshold (real occupation), confined to the layer $w$ |

Rich-get-richer requires energy uptake at least linear in stored energy. A linear (slaved) response cannot supply it: its uptake is concave. The only amplifying term lives inside the layer.

## 3. Bonus theorem: fairness is forced by amplitude-linear coupling

The framework's standing postulate (Born-rule memory line) is that couplings are **amplitude-linear**. Vacuum noise therefore does work on tip $i$ at rate $\propto \sqrt{e_i}\,\xi_i(t)$ with independent, symmetric $\xi_i$:

$$de_i = \sigma\sqrt{e_i}\;dW_i .$$

Apply Itô's lemma (the stochastic chain rule, which adds a second-derivative term $\tfrac12\sum_j \mathrm{Var}_j\,\partial^2_j$ to the naive drift) to the share $s_i = e_i/E$, $E = \sum_j e_j$. With $\partial^2 s_i/\partial e_j^2 = -2\delta_{ij}/E^2 + 2e_i/E^3$:

$$\mathbb{E}[ds_i] \;=\; \frac{\sigma^2}{2}\sum_j e_j\!\left(-\frac{2\delta_{ij}}{E^2} + \frac{2e_i}{E^3}\right)
= \frac{\sigma^2}{2}\left(-\frac{2e_i}{E^2} + \frac{2e_i}{E^2}\right) \;=\; 0
\qquad \text{identically, any } N.$$

**The shares are a martingale — the fair game is derived, not assumed.** With absorbing barriers (lock at $s_i \to 1$; relaxed sites drop out), optional stopping gives $P(i\text{ wins}) = s_i(0) = A_i^2/\sum_j A_j^2$: Born.

The scaling is a knife-edge, and amplitude-linear coupling sits exactly on it:

- **additive noise** (variance independent of $e$): $\mathbb{E}[ds_i] = \frac{\sigma^2}{E^2}(N s_i - 1)$ — *rich-get-richer*;
- **multiplicative noise** (variance $\propto e^2$): $\mathbb{E}[ds_i] = \frac{\sigma^2 e_i}{E^2}\!\big(\tfrac{1}{E}\sum_j e_j^2 - e_i\big)$ — *equalizing*;
- **amplitude-linear** (variance $\propto e$): drift $\equiv 0$ — *fair*.

So the same coupling law that produced the Born *form* via the golden rule produces the Born *probability* via the martingale. One postulate, both jobs.

## 4. Numerical verification (scratchpad, 2026-07-20)

**(a) Noise-scaling test** (`noise_scaling_born.py`) — SDE $de_i = \sigma\,\mathrm{amp}(e_i)\,dW_i$, win at share $\ge 0.9$:

| law | 3-site $[.5,.3,.2]$ | 10-site (bright Born $0.500$) |
|---|---|---|
| $\sqrt e$ (amplitude-linear) | $[0.510, 0.298, 0.191]$ — dev $0.011$ | bright $0.534$ — dev $0.035$ |
| additive | dev $0.050$ (+ boundary pathology, mass no-clicks) | bright $\to 1.0$ — dev $0.50$ |
| multiplicative | dev $0.042$, equalized | bright $0.316$ — strongly equalized |

Only the amplitude-linear law is fair; residuals for it are finite-threshold/step artifacts. (Caveat recorded: the additive-law *simulation* mixes the Itô rich-get-richer drift with a reflecting-zero boundary artifact; the analytic drift signs are the clean statement. The multiplicative equalization matches theory cleanly.)

**(b) Gapped vs tailed bias** (`gapped_threshold_born.py`) — gambler's ruin with lock-layer bias, 10-site stress config. "Tail" = old worst-case Adler profile $\beta = \min(1, w/(1-e))$; "gapped" = $\beta = \mathbb{1}[1-e \le w]$, as licensed by the slaving proof:

| $w$ | tailed dev | gapped dev |
|---|---|---|
| $0.003$ | $0.021$ | $0.006$ |
| $0.01$ | $0.063$ | $0.012$ |
| $0.03$ | $0.151$ | $0.015$ |
| $0.1$ | $0.328$ | $0.023$ |

Confining bias to the layer cuts Born violation by ~5–15× at fixed $w$ (values at small $w$ are at the 3000-trial noise floor). At physical $w = \Gamma/\omega \sim 10^{-6}$–$10^{-8}$, deviations are far below any measurement.

## 5. Born-accuracy budget (current best statement)

$$\text{dev(Born)} \;\lesssim\; O(w) \;+\; O\!\big(\Gamma_{\rm hop}/\Gamma_{\rm noise}\big) \;+\; \text{(2nd-order }r\text{–}\varphi\text{ correlations)}$$

- $w = \Gamma/\omega$: lock-layer width (final-state linewidth over transition frequency) — $10^{-6}$–$10^{-8}$ for photodetectors; $\sim10^{-2}$ in engineered strong-coupling systems ⇒ the percent-level-deviation prediction stands.
- $\Gamma_{\rm hop}$: coherent site-to-site hopping ($J^2/\gamma_\phi$), which is *equalizing*; must be slow vs. the noise-driven exchange. Plausibly tiny for micron-separated absorbers (dipole–dipole falls fast); estimate not yet done.
- Neglected: correlations between amplitude and phase fluctuations of a slaved site (vanish at leading order by the odd-moment argument; second order unquantified).

## 7. Timescale window for a real photodetector (added same day)

Workhorse case: **silicon SPAD at $\lambda = 500$ nm** ($\omega = 3.8\times10^{15}$ rad/s, optical period 1.7 fs, $E = 2.5$ eV); contrast case: narrow-line atomic absorber.

| scale | value (Si) | source |
|---|---|---|
| exchange step $1/\Gamma_{\rm noise}$ | 10–70 fs | final-state width 10–100 meV (fluctuation–dissipation ties noise variance to damping) |
| competitors $N$ | $\sim5\times10^{10}$ | diffraction volume $\times$ valence density; only $\ln^2 N \approx 400$–600 enters |
| **game duration** $\tau_{\rm game}\sim \ln^2\!N/\Gamma_{\rm noise}$ | **10–20 ps** | log-share diffusion must cover $\ln N$ |
| loss during game | fraction $\lesssim10^{-5}$ | indirect gap: radiative lifetime µs; multiphonon dissipation of a 2.5 eV virtual quantum blocked (orbital-discreteness protection again) |
| pattern-equalizing transport | $\sim 8$ nm $\ll$ µm pattern | below threshold coherent transport is the *slaved polariton wave* — pattern-preserving; incoherent diffusion needs real population, exists only post-commit ($\sqrt{2D\tau_{\rm commit}}$, $D\sim10$ cm²/s, $\tau\sim30$ fs) |
| photon coherence time | fs–ns | both orderings benign: long pulse ⇒ drive re-pins shares *to the Born pattern* (re-preparation; predicts click-time density $\propto|{\rm envelope}|^2$ — time-resolved Born, as observed); short pulse ⇒ clean post-pulse free game |

**The window chain:** $\;1.7\,\text{fs} \ll 10\text{–}70\,\text{fs} \ll 10\text{–}20\,\text{ps} \ll \text{ns–µs}$. It closes with 2–4 orders of margin on each side. $\Gamma_{\rm hop}/\Gamma_{\rm noise}\approx 0$ below threshold by slaving. (Consistency note, not overclaimed: $\tau_{\rm game}$ lands in the ballpark of measured SPAD timing jitter, tens of ps.)

**The solid-state layer problem and its resolution.** For silicon, $w = \Gamma/\omega \sim 4\times10^{-3}$–$4\times10^{-2}$ — a *percent-level* lock layer, unlike atomic lines ($w\sim10^{-8}$). Biased play inside such a layer would give percent-scale Born violations (§4b). The physical resolution: reaching the layer means real occupation begins, and Stage-3 commitment (avalanche seeding, rate $\sim\Gamma$) is faster than continued exchange — the layer is an **absorbing boundary at $1-w$, not a biased arena**. Then the only error is boundary placement. Verified (`window_tests.py`, Test A): a *fair* game absorbed at $1-w$ shows deviations at the Monte-Carlo noise floor ($<1\%$) for $w\le0.03$, and $3.3\%$ only at an absurd $w=0.1$. Analytically the 2-site boundary error is exact: $P = (s_0-w)/(1-2w)$ — confirmed by simulation to $0.003$ ($0.872$ observed vs $0.875$ predicted at $w=0.1$).

**Prediction sharpened.** Narrow-line detectors ($w\sim10^{-8}$): Born exact. Broadband solid-state detectors ($w\sim10^{-2}$): possible deviations up to $\sim$1%, bright-favored, **at the edge of current single-photon calibration precision (0.1–1%)** — provided commitment at layer entry is not instantaneous. Discriminating test: read the *same* interference pattern with detectors of very different $\Gamma/\omega$ and compare click statistics at $10^{-3}$–$10^{-4}$.

**New wrinkle found: correlated vacuum noise.** The fairness theorem (§3) requires *independent* noise per site. For a **shared** Wiener increment ($de_i = \sigma\sqrt{e_i}\,dW$, same $dW$), Itô gives a genuine rich-get-richer drift, e.g. for $N=2$: $\mathbb{E}[ds_1] = \sigma^2\sqrt{e_1e_2}\,(e_1-e_2)/E^3 > 0$ for the leader. Simulation (Test B): under fully common noise the bright site wins **100%** — catastrophic. Physical protection: (i) vacuum-noise correlation falls as $\mathrm{sinc}(k\,\Delta r)$ — sites farther than $\sim\lambda/2$ have nearly independent noise; (ii) within one correlation cell the amplitude pattern is smooth, so competitors are near-equal and bias among equals does not distort Born; (iii) the worst case — standing-wave fringes at $\lambda/2$ spacing — puts adjacent antinodes at the *zero* of the sinc correlation, possibly protectively. A full spatial-correlation analysis is the new open item.

## 9. Commitment: the rate-linearity theorem (added same day; supersedes the §7 layer-boundary picture for continuum absorbers)

**The §7 open question ("does Stage-3 commit outpace biased exchange in the layer?") dissolves.** Two observations restructure it:

**(a) Γ_commit = Γ_width is an identity, not a coincidence.** The final-state width *is* the rate of irreversible scattering into registered products (dephasing into the incoherent bath) — fluctuation–dissipation. A wide layer commits fast by construction.

**(b) Continuum absorbers have no threshold commit at all.** In a broadband absorber (Si), final states exist at every energy above the gap, so commitment does not wait for full assembly of the quantum at one site. It is a **rate process running throughout the game**: golden-rule form, $\text{rate}_i = \Gamma\,e_i/E_0$ — linear in occupation.

**Theorem (commit-rate independence).** Let commitment fire at any total rate (even time-varying), with conditional site-selection probability equal to the share $s_i$ — which is exactly what rate $\propto e_i$ gives, since $\text{rate}_i/\sum_j\text{rate}_j = e_i/E = s_i$. The commit time $T$ is a stopping time; the shares are martingales (§3); optional stopping gives

$$P_i \;=\; \mathbb{E}[s_i(T)] \;=\; s_i(0) \;=\; \frac{A_i^2}{\sum_j A_j^2} \qquad \textbf{exactly, at any commit speed.}$$

**What actually needs justifying is not the rate but its** ***linearity*** **in occupation — and that is the Fermi golden rule itself.** Meanwhile the discrete-level absorber (atomic) takes the other route: no partial-energy final states, so commitment requires full assembly — first-passage to $s=1$, optional stopping again, Born again. **Both detector classes give exact Born as two corollaries of the same martingale property** (a pleasing echo of the framework's standing detector-class taxonomy: discrete event detectors vs. continuous-medium absorbers).

**Numerics** (`rate_commit_born.py`): fair game + rate commitment with rate $\propto s^\alpha$. $\alpha = 1$: Born at every speed (dev ≤ 0.007, 2-site; ≤ 0.015, 10-site slow — numerical floor). $\alpha = 2$: bright-favored, $P_1 = 0.938$ at fast commit vs theory $0.8^2/0.68 = 0.941$; $\alpha = 0.5$: dim-favored, $0.675$ vs theory $0.667$; both relax toward Born as commitment slows (concentration completes first). Failure modes behave exactly as the theorem's converse predicts.

**Retraction.** The §7 "decision at $1-w$" boundary picture — and with it the "$\lesssim1\%$ bright-favored deviation for broadband detectors" prediction — was an artifact of imposing a hard threshold on a continuum absorber. Real broadband absorbers commit by rate; linear rate ⇒ exact Born, no $O(w)$ boundary error. Born robustness is *stronger* than the §7 estimate — and more consistent with the absence of observed deviations. The surviving deviation predictions are: (i) **nonlinear-commit systems** — any absorber whose registration requires cooperative/two-carrier processes (effective $\alpha \approx 2$: bright-favored) or saturates (effective $\alpha < 1$: dim-favored), with the deviation largest for fast commitment; (ii) correlated-noise atom arrays (see `DERIVATION_vacuum_noise_correlation.md`); (iii) pre-cohered (phased) detector ensembles.

## 8→10. Remaining open items

1. ~~Timescale window~~ — done, §7 (closes with 2–4 orders of margin).
2. ~~Spatial vacuum-noise correlation~~ — done, `DERIVATION_vacuum_noise_correlation.md` (locality protection, $f\sim10^{-6}$; atom-array prediction).
3. ~~Commit rate at layer entry~~ — dissolved by the rate-linearity theorem, §9.
4. Second-order slaved-site $r$–$\varphi$ correlations (see §5).
5. Bell pairs: run the fair game on the joint substrate state across both wings.
6. Survey real detector types for effective commit-rate nonlinearity ($\alpha \ne 1$) — the live deviation channel.
7. Evolved-configuration cluster residual in the correlated-noise game (other file, §6.2).

**Status:** the rich-get-richer objection is closed at the level of this model: below threshold there is no free phase (slaving, §1), no superlinear uptake (§2), and the vacuum-noise exchange is provably drift-free given amplitude-linear coupling (§3), with numerics confirming both the knife-edge and the layer confinement (§4).

---

*Glossary:* **slaved/enslaved variable** — a coordinate with no dynamics of its own; it relaxes to a value dictated by other variables (here: phase pinned by the drive). **Limit cycle** — a self-sustained periodic orbit; its phase is a *zero mode* (neutrally stable direction), which is what lets a clock be entrained. **Zero mode** — a perturbation direction with zero restoring force. **Itô's lemma** — chain rule for stochastic processes; adds a curvature term $\tfrac12\sigma^2\partial^2$ to the drift. **Martingale** — zero-drift process ("fair game"). **Hopf bifurcation** — transition where a damped fixed point becomes a limit cycle; here it sits at the lock threshold ($\gamma\to0$). **CIR-type noise** — noise with variance proportional to the state, as in $\sqrt{e}\,dW$; zero is naturally sticky/absorbing.
