# Synchronization, the Arnold Tongue, and the Born Rule

*A conceptual walkthrough — understanding-oriented, not paper text.*
*Date: 2026-06-23*

This note traces a single line of reasoning from "what kind of nonlinear
Schrödinger equation does the framework use?" down to "why is the outcome
weighting $|c_k|^2$, and is it the *area* or the *depth* of a sync basin that
decides?" Each section builds on the last. It records understanding reached in
discussion; it is not a derivation claimed to be rigorous end-to-end. The single
load-bearing assumption is flagged in §6 and recapped at the end.

---

## 0. Three things not to conflate

Before anything else, keep three notions separate — sloppiness here is the root
of most confusion:

1. **Interaction / coupling.** Couple system to apparatus and let them entangle.
   On the *joint* Hilbert space this is plain unitary evolution,
   $i\hbar\,\partial_t\Psi = H_{\text{tot}}\Psi$, $U=e^{-iH_{\text{tot}}t/\hbar}$.
   Entanglement grows but the map is **linear and reversible**. (This is Stage 1
   — bulk-mediated detector entanglement.)

2. **Openness / dissipation = decoherence.** Trace out a large environment and
   the reduced state obeys a Lindblad master equation,
   $$\dot\rho = -\tfrac{i}{\hbar}[H,\rho] + \sum_k \gamma_k\!\left(L_k\rho L_k^\dagger - \tfrac12\{L_k^\dagger L_k,\rho\}\right).$$
   This is non-unitary and irreversible, but **still linear in $\rho$**. It
   suppresses off-diagonal terms — makes the state *look* mixed — but by itself
   selects no outcome. **Dissipation $\ne$ nonlinearity.**

3. **The nonlinear lock.** The genuinely nonlinear dynamics — the synchronizing
   coupling that breaks symmetry onto one basin. This is the "nonlinear
   evolution," and it is a *separate* property from both interaction and
   dissipation.

The rest of this note is about (3): what form it takes, when it engages, and
what statistics it produces.

---

## 1. Which nonlinear Schrödinger variant?

"Nonlinear Schrödinger equation" is overloaded. In optics it means the cubic
NLS; in foundations it means a *modified* Schrödinger dynamics with an added
nonlinear term. We mean the foundations sense.

**The dissipation intuition is correct — at the pure-state level.** At the
density-matrix level dissipation stays linear (Lindblad). But the moment you
insist on a *wavefunction*-level description of an open/dissipative system —
which the phase-field/sync picture does — modeling friction *forces* a nonlinear
term. Canonical example: the **Schrödinger–Langevin (Kostin) equation**,

$$
i\hbar\,\partial_t\psi=\Big[-\tfrac{\hbar^2}{2m}\nabla^2+V+\underbrace{\tfrac{\hbar\gamma}{2i}\Big(\ln\tfrac{\psi}{\psi^*}-\big\langle\ln\tfrac{\psi}{\psi^*}\big\rangle\Big)}_{\text{nonlinear friction},\ \propto\ \gamma}\Big]\psi .
$$

Here $\gamma$ *is* the dissipation rate, the bracket is genuinely nonlinear, and
$\gamma\to0$ recovers linear Schrödinger. So "nonlinearity switches on with
dissipation" is literally true in this formulation — a level-of-description
fact, not a contradiction with point (2) above.

### Taxonomy of variants

Two axes: **conservative vs dissipative**, and **deterministic vs stochastic**.

| Family | Added term | Dissipative? | Selects outcome? | Signaling? |
|---|---|---|---|---|
| Cubic NLS / Gross–Pitaevskii | $g\lvert\psi\rvert^2\psi$ | No | No | safe |
| Logarithmic (Bialynicki-Birula) | $b\ln\lvert\psi\rvert^2\,\psi$ | No | No | safe |
| **Gisin–Weinberg** (deterministic) | arbitrary $\mathcal N[\psi]\psi$ | optional | yes-ish | **superluminal** ⚠ |
| **Kostin / Schrödinger–Langevin** | friction $\propto\gamma$ | **Yes** | partially | needs care |
| **CSL / GRW / Diósi–Penrose** (stochastic) | $\sqrt\lambda(A-\langle A\rangle)dW-\tfrac\lambda2(A-\langle A\rangle)^2dt$ | Yes | **Yes**, Born | **safe** |

### The constraint that decides it: no-signaling

This is a theorem, not a preference. **Gisin (1990), Polchinski (1991):** a
*deterministic* nonlinear Schrödinger equation generically permits superluminal
signaling — nonlinearity makes local evolution sensitive to the basis a distant
entangled partner is measured in. The only known escape: make the nonlinearity
**stochastic** and arrange that the **ensemble average is linear** (Lindblad).
That is exactly how CSL works:

$$
\overline{d\rho}=-\tfrac{i}{\hbar}[H,\rho]\,dt-\tfrac{\lambda}{2}[A,[A,\rho]]\,dt\quad(\text{linear}\Rightarrow\text{no signaling}),
$$

even though each individual trajectory $d|\psi\rangle$ is nonlinear and selects
an outcome.

**Choice for this framework: the stochastic / average-linear (CSL-like) box**,
possibly with a Kostin-style friction piece. Reasons: (i) it is the only
no-signaling-safe outcome-selecting option; (ii) the Born derivation already
runs on bulk noise, so the framework naturally lives there.

---

## 2. Why the MRI analogy is exact

The stochastic/average-linear picture is not merely *like* MRI — MRI is its
cleanest physical instance.

- You never track one proton's phase. Each spin random-walks in phase from local
  field fluctuations — that is the noise, the $dW$. A single spin's history is
  stochastic and irreversible-looking.
- What you *measure* is the **ensemble** — net transverse magnetization $M_{xy}$
  summed over $\sim10^{18}$ spins — and the ensemble obeys the **linear** Bloch
  equations:
  $$\dot M_{xy}=-\frac{M_{xy}}{T_2},\qquad \dot M_z=-\frac{M_z-M_0}{T_1}.$$

So MRI realizes the CSL split: **stochastic at the single-trajectory level,
linear at the ensemble level.** The Bloch equation *is* the textbook Lindblad
equation. $T_2$ = noise washing out coherence (dephasing); $T_1$ = dissipative
return to equilibrium *with the bulk*. That last clause is the framework's whole
reading of relaxation.

---

## 3. The Arnold tongue (single oscillator)

The tongue answers one question: **when do two oscillators lock?** Two things
matter — the frequency mismatch (*detuning* $\Delta\omega$) and the coupling
strength $K$.

Reduce to one variable $\phi$ = the phase *difference* between oscillator and
drive. The minimal equation (Adler's equation):

$$\dot\phi=\Delta\omega-K\sin\phi.$$

- **Locked** ⇔ a fixed point exists, $\sin\phi^\*=\Delta\omega/K$, which needs
  $$|\Delta\omega|\le K.$$
- **Unlocked** ($|\Delta\omega|>K$) ⇒ $\phi$ keeps winding; phases drift and slip
  past each other forever.

In the $(\Delta\omega, K)$ plane the locked region is a **wedge** with its tip at
the origin — the Arnold tongue:

```
 K  \  L O C K E D  /
 ^   \             /
 |    \           /
 |     \         /
 | drift\       /drift
 |       \     /
 |        \   /
 +---------\ /----------> Δω
            0
```

At $K=0$ the tongue is a single point — only *exactly* matched frequencies lock.
As $K$ grows, the band of lockable detunings widens linearly.

**MRI version:** a spin precesses at Larmor frequency $\omega_0=\gamma B_0$; an RF
field at $\omega_{\text{RF}}$ with strength $\propto\gamma B_1$ is the drive
($K$), $\Delta\omega=\omega_{\text{RF}}-\omega_0$ the off-resonance. Spins within
$|\Delta\omega|\lesssim\gamma B_1$ get flipped/locked — which is why excitation
bandwidth grows with $B_1$, and is exactly what spin-locking ($T_{1\rho}$) does
on purpose. The tongue is the slice-selection wedge.

---

## 4. Kuramoto: the tongue width becomes self-consistent

The single-oscillator tongue used a *fixed external* drive. Kuramoto's change:
the drive is *generated by the population*, and that turns the tongue width into
a threshold quantity.

Start from $N$ oscillators:
$$\dot\theta_i=\omega_i+\frac{K}{N}\sum_{j=1}^N\sin(\theta_j-\theta_i).$$

Define the **order parameter** (centroid of phases on the unit circle):
$$r\,e^{i\psi}=\frac1N\sum_j e^{i\theta_j},\qquad r\in[0,1].$$
$r=0$: phases scattered. $r=1$: all aligned. Multiply by $e^{-i\theta_i}$ and
take the imaginary part:
$$r\sin(\psi-\theta_i)=\frac1N\sum_j\sin(\theta_j-\theta_i).$$
The $N$-body sum collapses to $N$ **independent** Adler equations, with effective
coupling $Kr$ instead of bare $K$:

$$\boxed{\;\dot\theta_i=\omega_i+Kr\,\sin(\psi-\theta_i)\;}$$

In the frame rotating with $\psi$ ($\phi_i=\theta_i-\psi$):
$$\dot\phi_i=\omega_i-Kr\sin\phi_i\quad\Longrightarrow\quad\text{locks iff }|\omega_i|\le Kr.$$

So the **tongue width is $2Kr$**, not $2K$. Bare coupling sets the *capacity* to
lock; coherence $r$ sets how much is actually delivered.

### Self-consistency → threshold

$r$ is not given — the locked oscillators ($|\omega_i|<Kr$) *build* the mean
field; the drifters average to zero. So $r$ feeds the tongue that determines $r$:
$$r=Kr\int_{-\pi/2}^{\pi/2}\cos^2\!\phi\;g(Kr\sin\phi)\,d\phi,$$
with $g(\omega)$ the spread of natural frequencies. Positive feedback ⇒ sync is a
**bifurcation**, not a gradual onset. Taking $r\to0^+$:
$$K_c=\frac{2}{\pi\,g(0)}.$$

- $K<K_c$: only $r=0$ — every tongue has **zero width**, all drift.
- $K>K_c$: a synchronized branch appears, $r\propto\sqrt{(K-K_c)/K_c}$, tongue
  widening continuously from zero.

### Contrast in one line

| | Single oscillator | Kuramoto (collective) |
|---|---|---|
| Tongue width | $2K$ | $2Kr$ |
| Drive amplitude | imposed | self-generated ($r$) |
| Threshold? | none | **yes**, $K_c=2/\pi g(0)$ |

Two hooks:

- **Noise raises $K_c$.** Add stochastic dephasing of strength $D$ (the $T_2$,
  the $dW$): for identical oscillators $K_c=2D$. Frequency spread and noise both
  fight the lock; $Kr$ fights back. "Inside the tongue?" really means
  $Kr$ vs *(detuning spread + noise)* — the same competition as resonance
  bandwidth vs dephasing in MRI.
- **Micro/macro measurement boundary, for free.** A real detector is internally
  coherent (large $r$, supercritical) ⇒ wide tongue ⇒ entrains easily. A
  microscopic "would-be detector" sits below $K_c$, tongue width zero, doesn't
  measure — the interaction stays reversible. **Measurement = being inside a
  tongue whose width $2Kr$ is set by the apparatus's own coherence.**

---

## 5. Virtual vs real particles: the threshold as "on-shell"

The same lock threshold draws the **virtual / real** line — equivalently
**off-shell / on-shell**. The intuition: a virtual particle's lifetime is
governed by the energy-time uncertainty principle, while a real particle has
"escaped past a threshold" so its lifetime is no longer UP-governed. The tongue
makes this precise.

### The standard distinction

- **Virtual = off-shell**: does not satisfy $E^2=p^2c^2+m^2c^4$. The energy
  imbalance $\Delta E$ is "borrowed," so the excitation persists only for
  $\Delta t\sim\hbar/\Delta E$. Further off-shell ⇒ shorter-lived. (This *is*
  "lifetime governed by the UP.")
- **Real = on-shell**: energy conserved, propagates freely. Stable ⇒ lives
  forever; unstable ⇒ decays at a **golden-rule width** $\Gamma$,
  $\tau=\hbar/\Gamma$ — a physical decay clock, not the off-shell borrowing clock.
- **Escape past threshold = pair production.** Below $2m_ec^2$ a fluctuation must
  repay its debt and stays virtual; supply enough energy — or reach the
  **Schwinger critical field** $E_c=m^2c^3/e\hbar$, where the field does
  $\sim2m_ec^2$ of work over a Compton wavelength — and the pair goes on-shell and
  walks away as real particles.

### In the lock language

Dictionary:
$$\text{off-shell imbalance }\Delta E\ \longleftrightarrow\ \text{detuning }\hbar\,\Delta\omega\qquad(\Delta E=\hbar\,\Delta\omega).$$

- **Virtual** = an unlocked, off-resonance substrate oscillator: inside no
  tongue, it slips and dies as a transient.
- **Real** = a locked, on-resonance, self-sustaining mode — matter as a
  *persisting* wave (virtual = a *transient* wave).

Take the Adler equation $\dot\phi=\Delta\omega-K\sin\phi$. Off-resonance enough to
fail to lock ($|\Delta\omega|>K$), it slips with a finite transient time:

$$\tau_{\text{slip}}=\frac{2\pi}{\sqrt{\Delta\omega^{2}-K^{2}}}\ \xrightarrow[\ \Delta\omega\gg K\ ]{}\ \frac{2\pi}{\Delta\omega}=\frac{2\pi\hbar}{\Delta E}.$$

- **Far off-shell** ($\Delta E\gg\hbar K$): $\tau\sim\hbar/\Delta E$ — pure
  energy-time uncertainty. The UP *is* the off-resonance beat time of a failed
  lock; you don't postulate it, it falls out.
- **At the threshold** ($\Delta E\to\hbar K$, the tongue boundary):
  $\tau_{\text{slip}}\to\infty$ — **critical slowing down**. The excitation stops
  slipping, locks, and goes real. That divergence *is* the "escape past a
  threshold."

One curve spans both regimes: the off-shell tail reproduces the UP lifetime; the
lock threshold is where the lifetime diverges and the mode goes on-shell.

### Refinement: the clock changes, the UP doesn't "switch off"

| | governing clock | mechanism |
|---|---|---|
| Virtual (unlocked, off-shell) | $\hbar/\Delta E$ | off-resonance slip / energy-time UP |
| Real, stable (locked) | ∞ | self-sustaining attractor |
| Real, unstable (locked, open channels) | $\hbar/\Gamma$ | golden-rule decay |

Two caveats:

1. For a real *unstable* particle, $\Gamma\tau\sim\hbar$ still *looks* like the
   UP — but it is now a *consequence* (the Fourier width of an exponentially
   decaying amplitude), not the off-shell borrowing *cause*. It is the **same
   golden rule** that sets the Born capture rate (§6), which is why real fermion
   lifetimes come out governed by phase space (Sargent's $Q^5$), a decay-rate
   clock — *not* the UP. The "real" side confirms itself.
2. "Virtual particle lifetime" is itself a heuristic gloss on the propagator (QFT
   integrates over *all* off-shell momenta rather than tracking a clocked
   particle). The mapping here is a physical *re-reading* of that heuristic, not a
   literal lift from the Feynman rules.

**Bottom line:** the real/virtual boundary is the **lock threshold**. Below it the
lifetime is the off-resonance slip time (which *is* the energy-time UP); crossing
it (on-shell / inside the tongue) swaps that clock for "forever" (stable) or a
golden-rule width (unstable).

---

## 6. Born weighting: eligibility vs weight

Key distinction, easy to get wrong: **the tongue decides *eligibility*; the Born
weight comes from the locking *rate* — and these are different powers of the
amplitude.** Reading probabilities off tongue widths gives the *wrong* rule.

Write $|\psi\rangle=\sum_k c_k|k\rangle$, each branch $k$ a candidate sync basin.
Two distinct amplitude dependences:

**(1) Coupling — linear in amplitude.** The detector couples to component $k$,
whose "size" is $|c_k|$:
$$K_k\propto|c_k|\quad\Longrightarrow\quad\text{tongue width}=2K_k r\propto|c_k|.$$
This is *gating*: every branch with nonzero $c_k$ is inside its tongue, hence a
viable outcome. Probability enters only because *several* basins are lockable at
once.

**(2) Capture rate — quadratic in amplitude.** Locking is not instantaneous;
noise must kick the system out of the incoherent state into a basin. The
irreversible capture rate is Fermi golden rule — rate $\propto$ |matrix element|²
$\propto$ coupling²:
$$\Gamma_k\propto K_k^2\propto|c_k|^2.$$

### The race gives Born

Treat each basin as an independent noise-driven (Poisson) capture process,
rate $\Gamma_k$, **winner-take-all** (first to lock wins). Probability $k$ fires
first:
$$P(k)=\int_0^\infty\Gamma_k e^{-\Gamma_k t}\prod_{j\ne k}e^{-\Gamma_j t}\,dt
=\frac{\Gamma_k}{\sum_j\Gamma_j}=\frac{|c_k|^2}{\sum_j|c_j|^2}=|c_k|^2.$$

Normalization $\sum_k|c_k|^2=1$ *is* "exactly one basin eventually wins."
Born weighting = first-past-the-post statistics of competing golden-rule lock
rates.

### Why it must be the rate, not the width

The tongue width is $\propto|c_k|$. If probability tracked *width* — the naive
"bigger basin, more likely" guess — you'd get $P(k)\propto|c_k|$, an
**amplitude-linear** rule, which is *not* Born and is experimentally dead. Born
is special because it is the **square**, and the square enters only through the
golden-rule rate. Hence the framework needs *two separate facts*:

$$\underbrace{K_k\propto|c_k|}_{\text{coupling/tongue: eligibility}}\qquad\text{and}\qquad\underbrace{\Gamma_k\propto K_k^2\propto|c_k|^2}_{\text{rate: weight}}.$$

### What each piece does

- **Noise ($dW$, $T_2$)** supplies the randomness — different winner each run
  because each run sees a different bulk-noise realization. Born indeterminism is
  *physical substrate noise*, not a postulate.
- **Nonlinear feedback (self-amplifying tongue)** enforces winner-take-all: the
  first basin to catch a large fluctuation grows $r$ its way, widening its tongue
  and pulling coherence off rivals (dropping them below threshold). One basin
  wins — the single-world sync outcome.
- **Ensemble-linear closure**: single runs are stochastic/nonlinear (one
  winner), but frequencies $|c_k|^2$ mean the *averaged* $\rho$ decoheres in the
  $\{|k\rangle\}$ basis at rates $\propto|c_k|^2$ — a linear Lindblad map, same
  CSL/Bloch structure, no signaling.

---

## 7. Area vs depth of the basin

"Which geometric feature of a basin governs the outcome — its *area* or its
*volume/depth*?" is the same fork as §6 (width vs rate), in geometric clothes.

A landscape of sync basins can select an outcome two ways:

**Area / measure → selection by initial condition.** Drop the system somewhere,
roll deterministically downhill into whichever basin it started in:
$$P(k)=\frac{\text{vol(basin}_k)}{\sum_j\text{vol(basin}_j)}.$$
*Kinematic* — set by where separatrices fall, an accident of geometry. Same
*character* as tongue width: an **extent**. No natural reason a basin's volume
equals $|c_k|^2$; area-selection is Born only by fine-tuning.

**Depth / strength → selection by noise-activated rate.** Don't start in a basin;
hold the system in the incoherent metastable state and let noise kick it until
one basin captures it — first past the post:
$$P(k)\propto\Gamma_k\propto K_k^2\propto|c_k|^2.$$
*Dynamical* — set by how strongly each basin *pulls* (capture rate). Gives Born
robustly from linear-coupling-plus-squared-rate.

| | Area / measure | Depth / strength |
|---|---|---|
| Selection mode | initial condition (roll downhill) | noise-activated race |
| Governing quantity | basin volume (extent) | capture rate (pull) |
| Maps to | tongue **width**, $\propto|c_k|$ | golden-rule **rate**, $\propto|c_k|^2$ |
| Gives Born? | only by fine-tuning | **yes, generically** |

So the framework must come down on the **depth/rate** side — same reason as §6:
area is an extent (wrong, linear character), rate is a pull (the quadratic one
that *is* Born).

### Precision about "depth"

"Depth" here means the **perturbative pull at onset** — the curvature/coupling
setting the golden-rule rate $\Gamma_k\propto K_k^2$ — **not** the literal
Kramers barrier depth. That matters: Kramers escape over a deep well goes as
$\exp(-\Delta U/D)$, exponential in depth, which would *not* give $|c_k|^2$. The
framework lives in the weak-coupling / noise-dominated regime where the lock is a
perturbative transition (rate $\propto$ coupling²), not the deep-well activated
regime.

Timing: the **odds are set at onset** by the rate, while the well is still
shallow; the nonlinear winner-take-all feedback only *deepens* the winning basin
*afterward*. Depth governs the outcome via *attractor pull setting the capture
rate*, not *final well-depth via Kramers*.

### The payoff: noise picks the regime

What decides area-regime vs depth-regime is **how much bulk noise there is**:

- **Too little noise** → system freezes into whatever basin its initial condition
  sat in → selection by **area** → statistics set by geometry → *not* Born.
- **Enough noise** ($dW$, $T_2$ dephasing) → system continually re-randomized,
  never just rolling down from where it started; kicked between metastable states
  until a rate wins → selection by **depth/rate** → $|c_k|^2$.

So bulk noise is load-bearing twice: it is the *source of the randomness* (§6)
*and* what **guarantees you read probabilities off rates rather than basin
geometry** — keeping the system on the Born-producing side of the fork. Kill the
noise and the framework predicts the wrong rule.

---

## Summary

1. Use the **stochastic / average-linear (CSL-like)** nonlinear Schrödinger
   variant — the only no-signaling-safe outcome-selecting option; MRI's
   Bloch-from-stochastic-spins is its clean instance.
2. Locking obeys an **Arnold tongue**: lock iff $|\Delta\omega|\le$ (effective
   coupling). For a single oscillator that's $K$; for Kuramoto it's $Kr$, which
   is **self-consistent** and yields a **threshold** $K_c=2/\pi g(0)$. Below
   $K_c$: no lock (no measurement). Above: lock (measurement). Detector coherence
   $r$ sets the tongue width → micro/macro boundary.
3. **Virtual vs real** = on-shell vs off-shell = the same lock threshold.
   Off-shell/unlocked: lifetime is the off-resonance slip time
   $\tau\sim\hbar/\Delta E$ — *is* the energy-time UP. At the threshold
   $\tau\to\infty$ (critical slowing down) → the mode goes on-shell/real, its
   clock becoming ∞ (stable) or $\hbar/\Gamma$ (golden-rule decay).
4. **Born weighting** = first-past-the-post race of golden-rule capture rates
   $\Gamma_k\propto|c_k|^2$, giving $P(k)=|c_k|^2$ with normalization built in.
5. **Eligibility (tongue width $\propto|c_k|$) ≠ weight (rate $\propto|c_k|^2$).**
   Reading probability off width/area gives the wrong, amplitude-linear rule.
6. **Area vs depth**: outcomes are governed by basin **depth-as-rate** (pull),
   *not* basin **area** (extent). Bulk noise is what forces the depth/rate regime
   rather than the area/initial-condition regime.

### Load-bearing assumption

Everything downstream rests on one step: **coupling linear in amplitude
($K_k\propto|c_k|$) plus a golden-rule (squared) capture rate
($\Gamma_k\propto K_k^2$).** Granting that, the tongue/threshold machinery
supplies eligibility and winner-take-all, bulk noise supplies the randomness and
the regime, and the race delivers $|c_k|^2$. The rest is supporting dynamics
around that one step.
