# Page–Wootters, the Chiral Clock, and Thermal Time

*A conceptual walkthrough — understanding-oriented, increasingly speculative toward the
end. Not paper text.*
*Date: 2026-06-26. Sibling to `NOTE_sync_cosmology_walkthrough.md` and
`NOTE_sync_tongue_born_walkthrough.md`. Glossary terms extended at the bottom.*

This note works out how the Page–Wootters (PW) mechanism — quantum mechanics'
standard answer to "why does anything happen if the universe's wavefunction is
frozen?" — maps onto the DK framework's emergent-time / foliation picture. The
through-line: PW gives a **reversible** relational time from a clock; the DK
framework needs *two* extra ingredients PW lacks on its own — an **irreversible**
arrow (the locking events) and a way to **share** time across the cosmos (the CMB as
a thermal reference). Both have names in the literature. Confidence is labeled
**solid / sketch / open** throughout. §5–6 are first runs at the two hardest gaps
(thermal-time = sync-time, and the modular-rate ↔ Hubble bridge); the last section
(§7, signature emergence) is the most conjectural — flagged heavily.

---

## 0. The problem PW solves

Canonical quantum gravity gives the **Wheeler–DeWitt equation** $\hat H_{\text{tot}}
|\Psi\rangle = 0$: the wavefunction of the whole universe is annihilated by the total
Hamiltonian, i.e. it is a *stationary, frozen* state. ("Constraint" = an equation the
state must satisfy, not an equation of motion.) But the Schrödinger equation needs an
external time $t$, and for the universe *as a whole* there is no outside clock. So the
universe looks timeless. How does anything evolve?

---

## 1. The mechanism proper (solid — this is textbook)

Split the total Hilbert space into a **clock** and **the rest**:

$$\mathcal H=\mathcal H_C\otimes\mathcal H_S,\qquad
\hat H_{\text{tot}}=\hat H_C\otimes\mathbb 1+\mathbb 1\otimes\hat H_S.$$

The global state $|\Psi\rangle\rangle$ is a single static, **entangled** state with
$\hat H_{\text{tot}}|\Psi\rangle\rangle=0$. Nothing in it moves. Define the
**conditional state** of the rest, *given that the clock reads $t$*:

$$|\phi_S(t)\rangle\equiv\langle t|_C\,|\Psi\rangle\rangle.$$

Apply $\langle t|_C$ to the constraint $(\hat H_C+\hat H_S)|\Psi\rangle\rangle=0$:

$$\underbrace{\langle t|\hat H_C|\Psi\rangle\rangle}_{=\,i\hbar\,\partial_t|\phi_S(t)\rangle}
+\;\hat H_S|\phi_S(t)\rangle=0
\quad\Longrightarrow\quad
\boxed{\,i\hbar\,\frac{d}{dt}|\phi_S(t)\rangle=\hat H_S|\phi_S(t)\rangle\,}$$

The first term becomes a time-derivative because a **good clock** is *conjugate* to
its energy, $[\hat T_C,\hat H_C]=i\hbar$, so $\hat H_C$ generates translations in $t$
(exactly as momentum generates translations in position). **Schrödinger evolution
falls out of a globally frozen state.** Time = a correlation between a clock and
everything else; the "flow" is just stepping through correlations already baked into
$|\Psi\rangle\rangle$. (Page & Wootters 1983; firmed up by Giovannetti–Lloyd–Maccone
2015; the "trinity" equivalence to relational-Heisenberg and gauge-fixed pictures,
Höhn–Smith–Lock 2021.)

**The catch (solid, and it is the hinge of everything below):** a good PW clock needs
$\hat H_C$ with spectrum running over all of $\mathbb R$ (unbounded). A clock with a
*bounded or cyclic* energy spectrum can only tell time **modulo a period** — it
aliases. Hold that thought.

---

## 2. The chiral clock is the "second hand" (solid physics, DK reading)

The chiral phase — the L↔R Weyl oscillation set by the mass term — rotates at the
zitterbewegung frequency

$$\omega_\chi=\frac{2mc^2}{\hbar}\qquad(\text{Compton frequency }\omega_C=mc^2/\hbar).$$

This is a *real, built-in clock*: a massive Dirac particle ticks at its Compton
frequency, and one has been built (Lan, Müller et al., *Science* 2013, "A clock
directly linking time to a particle's mass"). So **the chiral clock is the Compton
clock** — your "second hand."

And it is a second hand *with no minute or hand* precisely because of §1's catch. Its
spectrum is effectively cyclic, so it only resolves time modulo

$$T_\chi=\frac{2\pi\hbar}{2mc^2}\sim10^{-21}\,\text{s (electron).}$$

Interaction can **phase-lock** two chiral second hands (sync), but the cyclic phase
can never *accumulate* long duration — it just wraps. This is the bounded-clock defect
made physical: the chiral phase is a perfect PW clock for ultrashort, reversible
intervals and useless for the hours. The real question is then: **what is the
unbounded, monotone variable that counts the hours?**

---

## 3. The irreversible interaction is the "long hands" (NOVEL claim — sketch, defensible)

Here is the load-bearing insight, and it is the one worth defending as ours.

**Bare PW is time-symmetric.** The conditional evolution $i\hbar\,\partial_t|\phi_S\rangle
=\hat H_S|\phi_S\rangle$ runs equally forwards and backwards. PW gives a *parameter*
of evolution but **no arrow and no accumulation**. So the long hands cannot come from
any reversible phase — chiral or otherwise. They must come from a monotone quantity,
and the only monotone available is **irreversibility**: records, decoherence, entropy.

This is not hand-waving — it is forced by a theorem. Erker et al. (*Autonomous
Quantum Clocks*, PRX 2017) proved a clock's **accuracy is bounded by the entropy it
dissipates per tick**: no irreversibility, no accurate long-duration clock. So your
statement — *"total time evolution has to be the irreversible phase of particle
interaction"* — is exactly what that bound demands. And it resolves §1's catch in a
physical way:

> **The unbounded monotone that bare PW needed (and a cyclic chiral phase cannot
> supply) is the entropy of the irreversible record — not a fundamental unbounded
> energy.** Entropy only goes up, so it is the genuinely unbounded "hour hand."

In DK terms each irreversible tick is a **locking event** — an off-shell→on-shell
threshold crossing (`NOTE_sync_tongue_born_walkthrough.md`), a Stage-2 detector sync
(Bell two-stage), a measurement record. The **count of locks** is the minute-and-hour
hand; the **chiral phase** is the second hand. Two timescales, two jobs the word
"time" usually conflates:

| | mechanism | character | role |
|---|---|---|---|
| second hand | chiral / Compton phase | unitary, cyclic, reversible | the PW parameter $t$ (local, aliased) |
| minute + hour | count of irreversible syncs | dissipative, monotone | the arrow & long duration |

---

## 4. How time is *shared* across the universe: CMB = cosmic thermal clock (sketch, strong fit)

A local clock is not yet a *cosmic* time. For everyone to agree, all the local chiral
second-hands must be phase-referenced to one shared standard. Two well-established
pieces converge on your CMB answer.

**(a) The CMB is the standard cosmological PW clock (solid).** The textbook internal
clock of quantum cosmology is the **scale factor** $a$ — the size of the universe *is*
time in the Wheeler–DeWitt picture. The CMB temperature reads it off directly:

$$T_{\text{CMB}}(z)=2.725\,(1+z)\;\text{K}\;\propto\;\frac1a.$$

A monotone, universal dial every patch of the cosmos is bathed in. "CMB as cosmic
clock" $\equiv$ "scale factor as PW clock," with $T_{\text{CMB}}$ as the hand. (This
is the *same* fast/slow split as `NOTE_sync_cosmology`: $\Omega$ the fast tick, the
order-parameter drift the slow hand.)

**(b) "Interacting with the vacuum" = the thermal time hypothesis (sketch — this is
the deep part).** A thermal bath at temperature $T$ is a **KMS state** (Kubo–Martin–
Schwinger — the rigorous definition of equilibrium). Connes & Rovelli (1994) proved
that *any* such state defines its own flow of time — its **modular flow**:

$$\rho=\frac{e^{-\beta\hat H}}{Z},\qquad
K\equiv-\ln\rho,\qquad
\sigma_s(A)=e^{iKs}\,A\,e^{-iKs},$$

i.e. **the statistical state itself is the time-generator** (physical time $t=\hbar\beta
s$). Time is not a stage the state sits on; the mixed, thermal state *is* the clock.
The CMB — a literal thermal photon bath coupled to everything — is the natural cosmic
KMS state. So *"the CMB interacting with the quantum vacuum provides the shared time"*
is, almost verbatim, the thermal time hypothesis with the CMB as the global
equilibrium state.

This unifies §3 and §4: **the arrow and the sharing are one fact.** The irreversible
locking events *are* the universe exchanging quanta with the cosmic thermal state, and
the modular flow of that state is the common time all local clocks reference.

**Beyond bare PW (sketch — note where we've left the textbook).** Vanilla PW uses a
*non-interacting* split; the clock correlates with the system only through the
*initial* entanglement. Your "CMB *interacting with* the vacuum" needs an ongoing
clock–system coupling — the **interacting-clock** extensions (Smith–Ahmadi 2019;
Castro-Ruiz et al. 2020). Tellingly, those are exactly where **gravitational /
cosmological time dilation** comes from — so the interacting version should *predict*
differential clock rates, not merely recover a global $t$. (Consistent with the
preferred-frame postulate: sharing time via the CMB rest frame picks out the
comoving/CMB frame, softly breaking Lorentz invariance in the measurement sector only
— the same load-bearing assumption as the rest of DK.)

---

## 5. Gap 4, first run: the two hands are a *factorization* of U(t) (mostly resolved)

*Which sector?* The left (winding) factor below needs the **closed/unitary** structure
— a phase $\theta$ with a conserved conjugate charge $[\hat\theta,\hat N]=i$ (the
quantum-Kuramoto / Bose-condensate substrate). The right (modular) factor needs an
**open/dissipative** coupling to a bath (where the KMS state and its modular flow live).
These are *not* competing choices to pick between: `PAPER_UNIFIED` already runs on
**both** — the closed mass term *and* the open bulk coupling, "the same off-diagonal
coupling under two boundary conditions" (App F). So the factorization is native to the
framework, not an extra assumption. (Detailed correspondence at the end of this section.)

Gap 4 asked: is thermal (modular) time the same as sync time? **Answer: no as an
identity, yes as a factorization** — and the factorization *derives* the two-hand
clock of §2–§3 instead of assuming it.

Three generators, not one: lab time ↔ $\hat H$; sync-phase $\theta$ ↔ $\hat N$;
modular/thermal time ↔ $\hat K=-\ln\rho$. The condensate winds at
$\dot\theta=\partial H/\partial N=\mu/\hbar=\Omega$ (Josephson relation), so **a
ticking clock necessarily has chemical potential $\mu=\hbar\Omega\neq0$.** A conserved
charge at $\mu\neq0$ *forces* the **grand-canonical** KMS state — and (the decisive
subtlety) such a state is KMS with respect to $\hat H-\mu\hat N$, not $\hat H$:

$$\rho=\frac{e^{-\beta(\hat H-\mu\hat N)}}{Z}\qquad\Rightarrow\qquad
\hat K=-\ln\rho=\beta(\hat H-\mu\hat N)+\ln Z.$$

The modular generator is $\hat H-\mu\hat N$ — **neither** lab time ($\hat H$) **nor**
sync phase ($\hat N$), but their difference. Since the charge is conserved
$[\hat N,\hat H]=0$, evolution splits **exactly** (no Trotter error):

$$e^{-i\hat Ht/\hbar}=\underbrace{e^{-i\mu\hat Nt/\hbar}}_{\text{sync winding (gen }N)}
\cdot\underbrace{e^{-i(\hat H-\mu\hat N)t/\hbar}}_{\text{modular flow (gen }K)}.$$

- **Left = the second hand.** A $U(1)$ rotation at $\Omega=\mu/\hbar$, generated by a
  *conserved charge* → a symmetry direction → reversible, cyclic, no arrow. The
  chiral/Compton hand of §2.
- **Right = the long hand.** The modular flow of a *mixed* KMS state → carries the
  arrow. The irreversible hand of §3.

So the two-hand clock is **the decomposition of $U(t)$ into its symmetry factor (gen
$N$) and its modular factor (gen $K$)** — exact whenever the sync charge is conserved.
Not an analogy; a factorization.

**Entropy bonus (closes the loop with §3).** Since $\hat K=-\ln\rho$,

$$\langle\hat K\rangle_\rho=-\mathrm{Tr}(\rho\ln\rho)=S_{\mathrm{vN}}$$

(check: $\langle K\rangle=\beta(U-\mu N)+\ln Z=S$, the grand-canonical entropy). **The
generator of the irreversible long hand, averaged, is the thermodynamic entropy
operator.** §3's "entropy is the unbounded monotone PW was missing" stops being a
slogan: the long-hand generator literally *is* the surprisal operator $-\ln\rho$.

**Status:** solid given both sectors. Caveats: (a) the winding factor needs the
closed-quantum charge $\hat N$ and the modular factor needs the open bath — *both of
which the framework already supplies* (App F), so this is not the load-bearing worry I
first flagged; (b) the rigorous infinite-system algebra is type III, so $\hat K=-\ln\rho$
and $\langle K\rangle=S$ need the finite/regularized form — but the modular *flow* and
the factorization survive (that is the whole Connes–Rovelli point).

**Cross-reference — this factorization *is* `PAPER_UNIFIED`'s closed/open division
(App F).** The paper's Appendix F proves the **closed** chiral mass term has *no
attractor* — a marginal line of fixed points, "as must be the case for closed unitary
evolution" — and treats that as a feature: it is why an isolated superposition neither
decoheres nor selects an outcome. Tracing out the bulk then yields the **open** Adler
equation $\dot\phi=\omega+K_{\rm eff}\sin(\Phi_{\rm bulk}-\phi)$, "which *does* possess a
genuine attractor, because the dissipation is now physical" (App F.5; measurement, §3.4).
That split maps onto the two factors here:

| §5 factor | App F regime | role |
|---|---|---|
| winding (gen $N$, unitary) | closed mass term (Rabi/Zitterbewegung) | **no** attractor — protects superposition |
| modular flow (gen $K$) + dissipative gap (§6) | open Adler/Lindblad bulk coupling | **the** attractor; strength $=\Gamma=2\varepsilon$ |

So measurement's attractor *is* supplied (by the bulk), and the closed mass term's is
correctly absent. The only attractor question still open is **neither** of these — it is
the **bulk's own coherence** (what orders the bath every local clock locks onto), which
is exactly the cosmology note's thread (b) (is $K_c$ a genuine SOC/RG fixed point?). The
thermal-time story therefore inherits **no new** attractor liability beyond the one the
cosmology paper already carries.

---

## 6. Caveat 3 + Gap 5: the modular rate is the de Sitter temperature (mostly resolved)

The modular flow's rate is $ds/dt=1/\hbar\beta=k_BT/\hbar$ — set by **temperature**.
At $T=T_{\text{CMB}}=2.725$ K, $k_BT/\hbar\approx3.6\times10^{11}\,\mathrm{s^{-1}}$
(≈ the CMB peak frequency), versus $H_0\approx2.2\times10^{-18}\,\mathrm{s^{-1}}$ — a
factor $\sim10^{29}$. So **the modular/thermal clock is a *fast* clock (~CMB
frequency), not Hubble.** $H$ enters one level up, two complementary ways:

1. **$H$ = drift of the modular generator.** $\hat K=\beta(\hat H-\mu\hat N)$ with
   $\beta=\hbar/k_BT_{\text{CMB}}\propto a$ (CMB cools as $T\propto1/a$). Hence
   $$\frac{\dot K}{K}=\frac{\dot\beta}{\beta}=-\frac{\dot T}{T}=\frac{\dot a}{a}=H.$$
   **Cosmic expansion = the thermal clock's generator slowly cooling.** Matches the
   cosmology note's $H=\frac{d}{dt}\ln a$. Honest: leans on adiabatic $T\propto1/a$, so
   this is *reinterpretation*, not from-scratch derivation.
2. **$H$ = dissipative gap (sketch).** Split the open-system generator into a
   modular/Hamiltonian part (reversible, KMS-preserving, rate $k_BT/\hbar$) + a
   dissipator (return to equilibrium, rate = spectral gap). The gap $\to0$ at
   criticality — the cosmology note's $\Gamma=2\varepsilon\to0$. So $H\sim$ gap = the
   rate the universe is still settling *onto* the KMS state the modular flow lives on.

**Gap 5 resolution (second run — the bath was wrong).** The two faces above looked
irreconcilable because Face 1 used the **CMB** bath. But for the *expansion / dark-energy
sector* the cosmologically fundamental KMS state is not the CMB photon gas (that clocks
the radiation *content*) — it is the **de Sitter horizon** at the Gibbons–Hawking
temperature:

$$T_{\rm dS}=\frac{\hbar H}{2\pi k_B}\qquad\Longrightarrow\qquad
\text{modular rate}=\frac{k_BT_{\rm dS}}{\hbar}=\frac{H}{2\pi}.$$

With the *right* bath the modular rate **is** the Hubble rate (up to $2\pi$). The
factor-$10^{29}$ above was just $T_{\rm CMB}/T_{\rm dS}$ (2.7 K vs $\sim10^{-30}$ K) —
radiation content vs. the expansion vacuum. (Rigorous: the modular flow of the de
Sitter vacuum on a static patch *is* the static-time translation at $T=H/2\pi$ — the
de Sitter Bisognano–Wichmann/Unruh theorem.)

The two faces then reconcile as **value vs. rate-of-change of one quantity**,
$T_{\rm dS}\propto H$:

- **Face 1 = the value.** Modular rate $=H/2\pi$: the thermal clock ticks at Hubble.
- **Face 2 = its relaxation.** $T_{\rm dS}\propto H$ is itself relaxing because the order
  parameter is still settling onto the floor: with $\rho_\Lambda\propto H^2$ and
  $\rho_\Lambda=\rho_\infty[1+\delta e^{-2\Gamma t}]$ (cosmology note thread a),
  $\dot H/H\simeq-\delta\Gamma e^{-2\Gamma t}$ — the modular temperature relaxes at the
  dissipative gap $\Gamma=2\varepsilon$.

They were never the same number and shouldn't be: **one is the modular rate's value
($H$), the other its log-relaxation ($\Gamma$).** The dark-energy observable falls out
directly — since $T_{\rm dS}\propto H$ and $\rho_\Lambda\propto H^2$,

$$1+w=-\frac{1}{3H}\frac{d\ln\rho_\Lambda}{dt}
=-\frac{2}{3H}\frac{d\ln T_{\rm dS}}{dt}\;\simeq\;\frac{2\Gamma\delta}{3H}>0,$$

matching `NOTE_sync_cosmology` exactly. **One knob, two roles:** $\varepsilon$ sets the
relaxation $\Gamma=2\varepsilon$ (Face 2); the floor $\rho_\infty$ sets the asymptotic
value $H_\infty$ (Face 1); their ratio is $1+w$. As $\varepsilon\to0$: $\Gamma\to0$,
$T_{\rm dS}\to$ const, $w\to-1$ — eternal de Sitter at a fixed Gibbons–Hawking
temperature.

> **One-liner:** dark energy's equation of state is (up to $-2/3H$) the logarithmic
> relaxation rate of the de Sitter modular temperature.

**Still open:** (a) *which bath clocks which sector* — CMB (radiation), de Sitter
(vacuum/expansion), and the condensate's own effective $T$ are three distinct KMS
states; the clean $T=H/2\pi$ result is **DE-era only**; (b) extend the modular-temperature
story back through the matter/radiation eras, where the de Sitter identification fails;
(c) this still inherits the cosmology note's thread-(a) machinery for Face 2.

---

## 7. Speculative extension: a randomized 4D vacuum → 3+1 spacetime (OPEN — most conjectural)

Your follow-on question: could this be pushed to *emergent signature* — a featureless,
"randomized" 4D vacuum becoming 3 space + 1 time? There is a real route, and three of
its pieces are the *same* machinery used above. Status: speculative, but not idle.

**The setup.** Take the "randomized 4D vacuum" as a phase substrate with **no
long-range order** and maximal symmetry — effectively Euclidean, SO(4)-symmetric, all
four directions equivalent, disordered phases. No direction is yet "time."

**Step 1 — synchronization is the symmetry breaking (sketch).** As coupling crosses
$K_c$, the substrate synchronizes: the condensate $r\,e^{i\theta}$ turns on. Its phase
*gradient* is a 4-vector, the **khronon** $\partial_\mu\theta$ (the constant-sync-phase
foliation field of `preferred_frame_coherence`). When the condensate acquires a uniform
**timelike "ticking"** — a persistent phase advance in one direction, exactly a
superfluid's $\dot\theta=-\mu/\hbar$ set by the vacuum chemical potential —

$$\langle\partial_\mu\theta\rangle=\mu\,\delta_\mu^{\,0},$$

it spontaneously breaks $SO(4)\to SO(3)$. The broken direction is **time**; the
unbroken $SO(3)$ is **isotropic space**. Note the clean accounting:
- the condensate **amplitude** $r$ is the same in all spatial directions → spatial
  isotropy;
- the condensate **phase winding** picks out one axis → exactly one time.

**Why exactly 1 time, not 2 (sketch — actually a feature).** The order parameter is a
*vector* (the gradient of a scalar phase), and a single vector VEV singles out exactly
one direction. A scalar phase field can only ever give **1+3**. (A 2-form condensate
would give multiple times — so the scalar-phase substrate is what forces a single time
axis. Nice consistency.)

**Step 2 — where the minus sign comes from (open — the hard part).** Breaking
$SO(4)\to SO(3)$ only picks an *axis*; it does **not** by itself flip the metric
signature ($+\!+\!+\!+ \to -\!+\!+\!+$). The Lorentzian light-cone must come from the
**dispersion relation of low-energy excitations** around the synced vacuum. Near a
Weyl / Fermi point the linearized spectrum is

$$E^2=c^2|\mathbf p|^2\quad(\text{a light cone}),$$

which *is* Lorentzian — Volovik's emergent relativity (*The Universe in a Helium
Droplet*): metric, Lorentz invariance, chiral fermions, and gauge fields all emerge
near a Fermi point. This is the **same Weyl-point structure already in the DK
emergence code** (`code/honeycomb_emergence`, `code/weyl3d_emergence`;
`emergent_fields_substrate`). So: **SSB picks the time axis; the excitation spectrum
near the Weyl point supplies the Lorentzian signature.** Deriving the genuine sign
*flip* dynamically (not merely anisotropy) is the open problem.

**Step 3 — the thermal bridge ties it to §4 (sketch, and the satisfying part).** A KMS
(thermal) state is periodic in *imaginary* time with period $\beta=\hbar/k_BT$ (the
Matsubara circle): a 4D Euclidean theory with one compact direction of circumference
$\beta$ *is* a 3D thermal theory. So the **emergent time direction is simultaneously**:
1. the SSB-selected axis (Step 1),
2. the modular-flow / thermal-time direction (§4b, Connes–Rovelli),
3. the Matsubara imaginary-time circle, analytically continued to real time.

These three coincide. The very mechanism that *shares* time (the cosmic KMS state /
CMB) is the one that *distinguishes* one direction as time. **Wick rotation isn't a
formal trick here — it's the statement that the thermal vacuum's special direction
becomes the time axis.**

**Honest status.** Heavily speculative. The genuine open holes: (i) deriving the
signature *flip* (Step 2), not just a preferred axis; (ii) showing the disordered 4D
phase is truly metric-less / Euclidean and not smuggling in a time; (iii) why the
ticking is timelike rather than spacelike (what makes $\mu$ the time component — likely
the sign of the vacuum's compressibility / the excitation spectrum, again Step 2). But
the skeleton — *disorder → sync/SSB → timelike khronon VEV → Weyl-point Lorentz cone →
thermal/Matsubara identification of that axis* — reuses machinery DK already has.

---

## 8. Open gaps (for next time)

1. **Clock-quality bound for the chiral phase.** Quantify the aliasing/error of a
   bounded cyclic Compton clock as a PW clock; show the irreversible-lock count
   genuinely supplies the unbounded monotone (entropy) per the Erker bound. A *number*
   here would turn §3 from a story into a claim.
2. **Interacting-clock prediction.** Make the CMB-coupled (interacting) PW model
   predict a concrete differential clock rate (time dilation) — tie to the existing
   preferred-frame tests T1–T5.
3. **Signature flip (§7, Step 2).** Derive the Lorentzian minus sign dynamically from
   the synced-vacuum excitation spectrum, not by assumption.
4. **~~Does modular time = sync time?~~ RESOLVED (§5).** Not an identity but an exact
   *factorization*: $U(t)=$ (sync winding, gen $N$) $\times$ (modular flow, gen $K$),
   with $\langle K\rangle=S$. The new live gap it spawns:
5. **~~Reconcile the two faces of $H$~~ RESOLVED (§6).** Not one number: with the
   *de Sitter* bath ($T_{\rm dS}=\hbar H/2\pi k_B$, modular rate $=H/2\pi$), Face 1 is
   the rate's *value* ($H$) and Face 2 its *log-relaxation* ($\Gamma=2\varepsilon$);
   ratio $=1+w=-\frac{2}{3H}d\ln T_{\rm dS}/dt$. New live gaps it spawns:
6. **Which bath clocks which sector?** CMB (radiation), de Sitter (vacuum/expansion),
   and the condensate's own effective $T$ are distinct KMS states; the $T=H/2\pi$ result
   is DE-era only. Extend the modular-temperature story through matter/radiation eras.

---

## Summary

1. **PW proper:** a frozen global state $\hat H_{\text{tot}}|\Psi\rangle\rangle=0$
   yields Schrödinger evolution for a subsystem *conditioned on a clock* — time = a
   correlation. Catch: a good clock needs an *unbounded* spectrum.
2. **Chiral = second hand:** the Compton/zitterbewegung phase is a real but **cyclic**
   PW clock — it can sync but only resolves time modulo $T_\chi\sim10^{-21}$ s.
3. **Irreversible interactions = long hands (our claim):** bare PW is reversible and
   has no arrow; by the Erker bound an accurate long clock *requires* dissipation, so
   the **entropy of the lock-count is the unbounded monotone PW was missing.**
4. **CMB = shared cosmic time:** scale factor / $T_{\text{CMB}}\propto1/a$ is the
   standard cosmological PW clock; "CMB interacting with the vacuum" = the **thermal
   time hypothesis** (Connes–Rovelli modular flow of the cosmic KMS state). Arrow and
   sharing are one fact. Going "interacting" (beyond bare PW) should predict time
   dilation.
5. **Gap 4 (§5) — mostly resolved:** thermal time ≠ sync time as an *identity* but
   they are the two factors of $U(t)=e^{-i\mu Nt/\hbar}\,e^{-i(H-\mu N)t/\hbar}$ — the
   sync winding (gen $N$, reversible second hand) times the modular flow (gen
   $K=\beta(H-\mu N)$, irreversible long hand). Bonus: $\langle K\rangle=S$, so the
   long-hand generator *is* the entropy operator. Quantum sector only.
6. **Caveat 3 / Gap 5 (§6) — resolved:** the CMB bath gives a fast clock, but the right
   bath for expansion is the **de Sitter horizon**, $T_{\rm dS}=\hbar H/2\pi k_B$, so the
   modular rate $=H/2\pi$ — Hubble itself. The "two faces of $H$" are then the *value*
   ($H$) and the *relaxation* ($\Gamma=2\varepsilon$) of $T_{\rm dS}\propto H$; ratio
   $1+w=-\frac{2}{3H}\,d\ln T_{\rm dS}/dt$, matching the cosmology note.
7. **Speculative §7:** disorder → sync/SSB → timelike khronon VEV ($SO(4)\to SO(3)$,
   one time because the order parameter is a vector) → Lorentzian cone from the
   Weyl-point spectrum (Volovik) → that axis identified with the thermal/Matsubara time.
   The same KMS state that *shares* time *selects* it. Signature flip still open.

### Load-bearing assumptions

(0) **Both sectors, as the framework already has them** — the winding factor needs the
closed-quantum charge $[\hat\theta,\hat N]=i$; the modular/attractor factor needs the
open dissipative bulk. `PAPER_UNIFIED` App F supplies both (closed mass term = no
attractor, protects superposition; open Adler coupling = the measurement attractor), so
§5–6 are native to the framework rather than an extra postulate. The *only* residual
attractor question is the bulk's own coherence (cosmology thread b), not a new one here. (i) The chiral/Compton phase is the PW clock, but cyclic —
so it cannot be the source of long-duration time; (ii) irreversible locking events
supply the arrow, with **entropy as the unbounded monotone** (Erker), now sharpened:
the long-hand generator $\hat K=-\ln\rho$ satisfies $\langle K\rangle=S$ (§5);
(iii) the CMB is the cosmic KMS state whose **modular flow is the shared time**
(Connes–Rovelli), with $H=\dot\beta/\beta$ the slow cooling of that clock's generator
(§6); (iv) §7 only: the synced vacuum's Weyl-point spectrum supplies the Lorentzian
signature, and the thermal/SSB/Matsubara directions coincide. Grant (0)–(iii) and the
two-hand cosmic clock follows as a factorization of $U(t)$; (iv) remains a research
conjecture.

---

## Glossary additions (companion to `GLOSSARY.md`)

- **Page–Wootters mechanism** — "evolution without evolution": a globally frozen
  universe yields ordinary time evolution for a subsystem when you *condition on a
  clock* subsystem. Time = correlation, not background.
- **Problem of time** — in quantum gravity the universe's wavefunction satisfies
  $\hat H|\Psi\rangle=0$ (frozen); PW explains how internal observers still see change.
- **Compton clock** — a massive particle's intrinsic tick at $\omega_C=mc^2/\hbar$;
  the chiral L↔R oscillation runs at twice this. A real, demonstrated clock.
- **KMS state** — the rigorous definition of a thermal-equilibrium quantum state
  (named for Kubo–Martin–Schwinger); characterized by periodicity $\beta=\hbar/k_BT$
  in *imaginary* time.
- **Modular flow / thermal time hypothesis** — Connes–Rovelli: a mixed (thermal) state
  $\rho$ generates its own time via $\sigma_s(A)=\rho^{-is}A\,\rho^{is}$. The state
  *is* the clock; "time is what a thermal state does."
- **Modular Hamiltonian $\hat K=-\ln\rho$** — the generator of modular flow; also the
  "surprisal/entanglement operator." Its expectation in its own state is the entropy,
  $\langle\hat K\rangle=S$ — which is why it can be the long hand's monotone generator.
- **Chemical potential $\mu$ / grand-canonical ensemble** — $\mu=\partial E/\partial N$
  is the energy cost of adding one quantum; the grand-canonical state
  $\rho\propto e^{-\beta(H-\mu N)}$ is equilibrium for a system that can exchange a
  conserved charge $N$. A *winding* condensate has $\mu\neq0$ (its phase advances at
  $\dot\theta=\mu/\hbar$), so its KMS state is grand-canonical.
- **Josephson / phase-winding relation** — $\hbar\dot\theta=\mu$: a condensate's
  collective phase advances at a rate set by its chemical potential. The "second hand"
  ticking rate $\Omega=\mu/\hbar$ comes from here.
- **Matsubara / imaginary-time circle** — a thermal QFT equals a Euclidean theory with
  one direction compactified to circumference $\beta$. The bridge between "thermal" and
  "a fourth dimension."
- **de Sitter / Gibbons–Hawking temperature** — an observer in an exponentially
  expanding (de Sitter) universe sees a thermal bath at $T_{\rm dS}=\hbar H/2\pi k_B$,
  radiated by the cosmological horizon (the expansion analog of Hawking/Unruh
  radiation). Tiny today ($\sim10^{-30}$ K), but it makes the modular/thermal clock of
  the *expansion sector* tick at exactly $H/2\pi$.
- **Emergent / dynamical signature** — the idea that the metric's minus sign (what
  makes one direction *time*) is not fundamental but arises by symmetry breaking +
  the excitation spectrum, e.g. near a Weyl point (Volovik).
