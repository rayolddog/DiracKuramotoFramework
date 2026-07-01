# Sync Cosmology: Foliation, H, and Dark Energy from Criticality

*A conceptual walkthrough — speculative toy cosmology, understanding-oriented, not paper text.*
*Date: 2026-06-23. Sibling to `NOTE_sync_tongue_born_walkthrough.md`.*

This note develops cosmic expansion in the foliation picture: time = the advance of
the synchronization phase, expansion = the slow drift of the sync order parameter.
It works out what sets the Hubble rate $H$, derives a dark-energy equation of state
$w(z)$ from the relaxing order parameter (thread a), and asks what drives the
coupling toward criticality (thread b). It is **more conjectural than the Born note**
— several steps are parametrized ansätze, flagged throughout. Confidence is labeled
"solid / sketch / open" as we go.

---

## 0. Why foliation, not a moving boundary

Two pictures of "expansion" were on the table:

1. **Foliation (chosen).** Expansion is a *clock* ticking, not a *substance* flowing.
   Slice the 4D substrate by constant sync-phase $\theta$; advancing $\theta$ is time;
   the locked pattern dilates uniformly across every slice. Expansion is everywhere,
   no center, no surface.
2. **Substrate transport (rejected).** Spacetime created at a sphere's surface and
   diffusing inward. Rejected because transport implies a gradient, a gradient
   implies a center + radial anisotropy we don't observe, and diffusion can't
   reproduce a uniform Hubble law. It also fails the standard redshift tests
   (supernova time-dilation $\propto(1+z)$, Tolman $(1+z)^{-4}$ surface brightness,
   CMB blackbody, image sharpness) unless its redshift is genuine metric stretching —
   in which case the transport machinery was unnecessary.

So everything below is the foliation/clock mechanism. "$\Lambda$ tracks the sync
fraction" and "preferred frame = constant-$\theta$ foliation" are the load-bearing
prior commitments.

---

## 1. The mechanism: two clocks

The structure is **two clocks**, and $H$ is the bridge between them.

- **Fast clock — defines time.** The synchronized condensate oscillates at the
  collective (Kuramoto mean-field) frequency $\Omega$. Cosmic proper time is the
  accumulated collective phase, $dt = d\theta/\Omega$. Foliating by constant $\theta$
  gives the spatial "now"; matter (locked standing waves) lives on those slices.
  This constant-$\theta$ foliation *is* the comoving / CMB frame.
- **Slow drift — defines expansion.** The global synchronization is still settling:
  the order parameter $r(t)$ relaxes toward its attractor. The effective metric the
  excitations ride (analog-gravity style) has a scale factor $a$ set by the sync
  parameters, so $a$ drifts as the condensate settles.

Expansion and time are the *same act*: each tick of $\theta$ carries a tiny change
in $a$. The ratio "fractional expansion per tick" is $H/\Omega$.

---

## 2. What sets H

**Solid (scaling).** $H$ is **not** the fast clock $\Omega$ — it is the slow
**logarithmic relaxation rate of the cosmic sync order parameter**:

$$H = \frac{\dot a}{a} = \frac{d}{dt}\ln a(r) \ \sim\ \frac{\dot r}{r}.$$

This explains the otherwise mysterious smallness of $H$. With $H\approx10^{-18}\,
\mathrm{s^{-1}}$ and any microscopic $\Omega\gtrsim10^{20}\,\mathrm{s^{-1}}$, the
hierarchy $H/\Omega\lesssim10^{-38}$ is enormous. The mechanism that makes a
relaxation rate near-zero is the same **critical slowing down** used for the
virtual/real threshold:

$$\tau_{\text{relax}}\sim|K-K_c|^{-z\nu}\to\infty,\qquad \Gamma=1/\tau\to0\ \ \text{as}\ \ K\to K_c.$$

If the **global/cosmic** condensate sits near its critical point, $H\sim\Gamma$ is
tiny. (Scale separation matters: the cosmic order parameter is near-critical and
slow; **local detectors are deeply supercritical and fast** — different order
parameters, different scales. $H$ is governed only by the cosmic one.)

**Subtlety (which identification of $H$?).** Two readings compete:

| | identification | asymptotics | gives acceleration? |
|---|---|---|---|
| (i) kinematic | $H\sim\dot r/r$ (expansion = order-parameter drift) | $H\to0$ as $r\to r_\infty$ | no — linearized settling gives $\ddot a<0$ |
| (ii) Friedmann | $H^2\sim\tfrac{8\pi G}{3}\rho_\Lambda(r)$, with a $\rho_\Lambda$ floor | $H\to H_\infty=$ const (de Sitter) | yes |

Reading (i) is the cleaner conceptual origin but, taken literally in the linearized
settling regime, gives $H\sim\delta\Gamma e^{-\Gamma t}\ll\Gamma$, hence
$\ddot a/a = H(H-\Gamma)<0$ — **deceleration**, contradicting observation. So the
quantitative cosmology uses **(ii)**: Friedmann with $\rho_\Lambda$ sourced by the
sync fraction. The permanent floor gives the observed acceleration; the slow
relaxation on top gives $w\neq-1$ (thread a). Reading (i) with *no* floor would
instead predict a coasting halt ($H\to0$) — a genuine fork, decided by whether a
permanent unsynced tail exists (§3 says it does).

---

## 3. Thread (a): w(z) from the relaxing order parameter

**Step 1 — order-parameter dynamics (solid).** Near the transition, the Kuramoto
amplitude obeys the time-dependent Ginzburg–Landau normal form of the supercritical
pitchfork:

$$\dot r = \varepsilon\,r - g\,r^3,\qquad \varepsilon\equiv\frac{K-K_c}{K_c}.$$

Fixed point $r_\infty=\sqrt{\varepsilon/g}$. Linearizing $r=r_\infty+\delta r$ gives
$\dot{\delta r}=-2\varepsilon\,\delta r$, so the **relaxation rate is $\Gamma=2\varepsilon$**
(→ 0 at criticality). In $u=r^2$ it is exactly logistic,
$\dot u=2\varepsilon\,u(1-u/u_\infty)$.

**Step 2 — dark energy from the Landau free energy (derived).** The potential whose
gradient gives the TDGL flow ($\dot r=-\partial_r f$) is the Landau free energy

$$f(r)=-\frac{\varepsilon}{2}r^2+\frac{g}{4}r^4,\qquad r_\infty=\sqrt{\varepsilon/g},\quad f(r_\infty)=-\frac{\varepsilon^2}{4g},\quad f''(r_\infty)=2\varepsilon=\Gamma.$$

(The curvature *is* the relaxation rate — consistent with Step 1.) The dynamics is
**overdamped** (first order, no kinetic term), so the gravitating vacuum energy is
purely the potential, split into a permanent **floor** (the always-drifting tongue
tail $|\omega|>Kr$, which never locks) plus the condensate's free energy above its
minimum:

$$\rho_\Lambda(r)=\underbrace{\rho_\infty}_{\text{floor: drift tail}}+\underbrace{\big[f(r)-f(r_\infty)\big]}_{\text{relaxing}}.$$

Landau fixes *differences*, so it pins the relaxing piece but **not** the floor
$\rho_\infty$ (the actual value of $\Lambda$ today — the CC problem is relocated, not
solved). Expanding about the minimum, $r=r_\infty+\eta$:

$$f(r)-f(r_\infty)=\tfrac12 f''(r_\infty)\,\eta^2=\varepsilon\,(r-r_\infty)^2\ \ge 0.$$

No linear term (it's a minimum), so the relaxing energy is **quadratic and
non-negative whichever side $r$ approaches from** — $\rho_\Lambda$ always settles to
its floor *from above* ($\dot\rho_\Lambda<0$). The **sign of $1+w$ is forced by
convexity ($f''>0$), not chosen.**

**Step 3 — read off $w$ via continuity (solid given Step 2).** For any component
$\dot\rho+3H(1+w)\rho=0$, so $1+w=-\tfrac{1}{3H}\,d\ln\rho_\Lambda/dt$. With
$\eta\sim e^{-\Gamma t}$ the relaxing energy goes as $\eta^2\sim e^{-2\Gamma t}$ —
settling at **twice** the order-parameter rate (energy $\sim$ amplitude²) — so
$\rho_\Lambda=\rho_\infty[\,1+\delta\,e^{-2\Gamma t}\,]$ with
$\delta=\varepsilon\eta_0^2/\rho_\infty>0$, and:

$$\boxed{\,1+w(a)\;\simeq\;\frac{2\Gamma\,\delta}{3H}\;a^{-2\Gamma/H}\,}\qquad\xrightarrow[a\to\infty]{}\;0\ \ (w\to-1).$$

Dark energy relaxes to $-1$ in the future and sat **further** from $-1$ in the past.
Around today ($a=1$), matching the CPL fit $w(a)=w_0+w_a(1-a)$:

$$1+w_0=\frac{2\Gamma\,\delta}{3H_0}>0,\qquad \frac{w_a}{1+w_0}\simeq-\frac{2\Gamma}{H_0}.$$

**Solid vs parametrized.**

- *Solid (structure):* $w\to-1$ asymptotically; deviation controlled by the single
  ratio $\Gamma/H$; $w_0$ and $w_a$ **linked**, not independent.
- *Derived (was a free choice):* the **sign** $1+w>0$ ($w>-1$, quintessence-side) —
  forced by convexity of the Landau minimum ($f''>0$); and the exponent $2\Gamma/H$
  (energy $\sim\eta^2$), not $\Gamma/H$.
- *Robust prediction:* overdamped relaxation is monotone, so $r$ never overshoots
  $r_\infty$ — the mechanism **cannot** give $w<-1$ or a $-1$ crossing. Firm
  phantom/quintom evidence would falsify the minimal single-order-parameter version.
- *Still free:* $\varepsilon$ (hence $\Gamma$), the displacement $\delta$, and the
  floor $\rho_\infty$ (absolute $\Lambda$).

---

## 4. Thread (b): why poised near $K_c$

**The natural feedback (sketch).** Mean-field coupling scales with oscillator
density, $K\propto a^{-3}$, and expansion is sync-driven, so expansion **dilutes**
the coupling:

$$\dot K=-3H K.$$

Negative feedback: sync → expansion → dilution → $K$ down toward $K_c$. But by
itself it **overshoots** — $K\propto a^{-3}$ sails through $K_c$ into the subcritical
(desync) regime. Pure dilution predicts the universe *passes through* criticality
rather than sitting at it. Three readings, increasing ambition:

- **(b1) Slow transit + selection (weakest).** Critical slowing down ($\Gamma=2\varepsilon
  \to0$) throttles the approach, so the transit lasts $\sim$ a Hubble time and
  "near-critical now" spans much of cosmic history. Structure/observers (persisting
  locked modes needing slow ordered relaxation) plausibly require this regime.
- **(b2) Genuine SOC attractor.** Add a compensating *up*-drive — gravitational
  clustering raises local density → local $K$ — balancing dilution at $K_c$
  (sandpile structure: accumulation ↑ vs dissipation ↓). Self-tunes to $K_c$, but
  the balance-at-$K_c$ is not yet shown.
- **(b3) RG fixed point (cleanest).** Expansion *is* an RG flow: the Hubble horizon
  is a moving cutoff, modes are integrated out as they exit it, and the dilution law
  $dK/d\ln a=-3K$ is the beta-function. $K_c$ as an **IR-attractive fixed point**
  would drive the universe to it. Elegant, but "is $K_c$ IR-attractive?" is an
  unproven conjecture about fixed-point stability.

**Open:** closing (b) — proving $K_c$ is a genuine attractor, not a point of passage.

---

## 5. Synthesis: one knob

The same $\varepsilon=(K-K_c)/K_c$ runs both threads:

- in **(a)** it sets $\Gamma=2\varepsilon$, hence the size of $1+w$;
- in **(b)** it is exactly what the cosmic feedback drives toward zero.

$$1+w_0=\frac{4\varepsilon_0\,\delta}{3H_0}\quad\Longrightarrow\quad (1+w_0)\ \propto\ \varepsilon_0=\text{today's distance from the synchronization critical point.}$$

So **measuring DESI's $w_0$ is measuring how near the universe is to its
synchronization transition right now.** As (b) drives $\varepsilon\to0$, (a) gives
$w\to-1$: the model **flows into ΛCDM**, the present deviation a clock on how far
through the transition we are.

Falsifiable structure (not numbers): $w_0$ and $w_a$ tied by $2\Gamma/H$ rather than
free; dark energy genuinely dynamical and quintessence-side (sign derived from
convexity, no $-1$ crossing); $w\to-1$ in the future.

Internal consistency: $\rho_\Lambda$ from the residual unsynced fraction *is*
"$\Lambda$ tracks sync fraction"; $H$ is read in the constant-$\theta$ (comoving/CMB)
frame; the smallness of $H$, $\Lambda$, and $|1+w|$ all trace to the **same critical
slowing down** as the virtual/real threshold.

---

## 6. Open gaps (for next time)

1. **The map $\rho_\Lambda(r)$ — RESOLVED for the sign; floor still open.** Derived
   from the Landau free energy in §3: $\rho_\Lambda=\rho_\infty+[f(r)-f(r_\infty)]$,
   relaxing piece $=\varepsilon(r-r_\infty)^2\ge0$, fixing $1+w>0$ by convexity and
   the exponent at $2\Gamma/H$. Still open: the **floor** $\rho_\infty$ (absolute
   $\Lambda$) — Landau fixes only differences, so the CC-problem magnitude is
   relocated, not derived.
2. **The attractor question (b).** Until $K_c$ is shown to be a genuine dynamical /
   RG attractor, "poised near criticality" is a restatement, not an explanation.
3. **Acceleration vs identification of $H$.** Confirm the Friedmann/floor reading
   (ii) is the right one and characterize when (if ever) the no-floor coasting-halt
   reading (i) applies.

---

## Summary

1. **Foliation mechanism:** time = advance of sync-phase $\theta$ (fast clock $\Omega$);
   expansion = slow drift of the order parameter $r$; $H$ bridges them. Expansion is
   everywhere, no center/surface.
2. **What sets $H$:** the cosmic order parameter's relaxation rate. Smallness =
   **critical slowing down** near $K_c$. Quantitatively via Friedmann with
   $\rho_\Lambda$ = residual unsynced fraction (floor → acceleration).
3. **Thread (a):** TDGL relaxation ($\Gamma=2\varepsilon$) + Landau free energy for
   $\rho_\Lambda$ + continuity ⇒ $1+w(a)\simeq(2\Gamma\delta/3H)\,a^{-2\Gamma/H}\to0$;
   CPL $w_0,w_a$ linked by $2\Gamma/H$; **sign $w>-1$ derived from convexity** (no
   $-1$ crossing).
4. **Thread (b):** expansion dilutes coupling ($\dot K=-3HK$) → drives $K\to K_c$;
   overshoots unless an up-drive (SOC) or IR fixed point (RG) holds it there. Open.
5. **Synthesis:** one knob $\varepsilon_0$. $(1+w_0)\propto\varepsilon_0$ = today's
   distance from criticality; model flows into ΛCDM as $\varepsilon\to0$.

### Load-bearing assumptions

(i) $\rho_\Lambda$ = permanent floor (always-drifting tail) + relaxing piece from the
Landau free energy $f(r)$ — the latter *derives* the sign $w>-1$; (ii) $H$ set by
Friedmann from that $\rho_\Lambda$; (iii) the order parameter obeys overdamped TDGL
relaxation near a critical point the cosmos sits close to. Grant those and threads
(a)+(b) follow. The values of $\varepsilon_0$ (how near criticality) and the floor
$\rho_\infty$ (absolute $\Lambda$) remain free inputs, exactly as $\Lambda$'s value is
in ΛCDM.
