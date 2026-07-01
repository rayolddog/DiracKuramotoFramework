# Glossary

*Plain-language definitions of the technical terms used in the sync / Born / cosmology
study notes. Companion to `NOTE_sync_tongue_born_walkthrough.md` and
`NOTE_sync_cosmology_walkthrough.md`. Each entry is one or two lines, with an everyday
analogy (a few medical/MRI ones). Date: 2026-06-23.*

---

## A. Phase transitions & synchronization — the core toolkit

*(Underpins both notes — the Arnold tongue, the Born race, and the cosmology all run
on this machinery.)*

- **Order parameter** — a single number measuring "how ordered" a system is, from 0
  (chaos) to 1 (perfect order). For a magnet it's the magnetization; for us it's $r$,
  the fraction of oscillators ticking together. The "one dial that summarizes the crowd."
- **Phase transition** — a qualitative change of state as you turn a knob: water → ice,
  or a metal becoming magnetic as it cools. Synchronization is one (incoherent → locked).
- **Landau free energy / Landau theory** — Lev Landau's recipe for phase transitions:
  write the system's "energy landscape" as a simple polynomial in the order parameter,
  e.g. $f(r)=-\frac{\varepsilon}{2}r^2+\frac{g}{4}r^4$. The system settles at the
  **minimum**, like a ball rolling to the bottom of a valley. Turn the knob and the
  valley reshapes from one minimum (disorder) into two (order) — that's the transition.
- **Free energy** — physicists' name for the "effective potential" a system rolls
  downhill in at equilibrium (it bundles energy + disorder). Just think "the landscape."
- **Critical point / criticality** — the exact tipping point of the transition (a
  magnet's Curie temperature; our sync threshold $K_c$). The system is most sensitive
  and most sluggish right there.
- **Critical slowing down** — near that tipping point the system takes forever to settle
  after a nudge (a ball in an almost-flat valley rolls back very slowly). This is why the
  Hubble rate $H$ is so tiny — the cosmic order parameter is near-critical.
- **Bifurcation / supercritical pitchfork** — a "bifurcation" is where behavior
  qualitatively splits as you turn a knob; the "pitchfork" is the shape where one stable
  state smoothly becomes two (the valley splitting in Landau's landscape).
- **Mean-field** — an approximation where each part feels the *average* of all the others
  instead of every neighbor individually. Each oscillator responds to the collective $r$,
  not to each partner.
- **Convexity** — a minimum is "cup-shaped" ($\cup$), curving upward on both sides. The
  fact we used: *any* stable minimum is convex, so the energy just above it is always
  positive — which forced the sign of the dark-energy answer.
- **Kuramoto model** — the standard model of synchronization: many oscillators with
  slightly different natural rhythms, each pulled toward the others; past a coupling
  threshold they spontaneously lock (fireflies flashing in unison).
- **Adler equation / Arnold tongue** — Adler's is the minimal equation for whether one
  oscillator locks to a drive; the Arnold tongue is the wedge-shaped "locking zone" (wide
  for strong coupling, pinching to a point for weak).
- **Self-organized criticality (SOC)** — when a system tunes *itself* to its critical
  point with no hand-tuning (a sandpile that keeps avalanching just enough to stay at the
  critical slope). We asked whether the cosmos parks itself at $K_c$ this way.

## B. Quantum-measurement terms

*(Used in the Born-rule note.)*

- **Fermi's golden rule** — a standard quantum formula: a transition's *rate* is
  proportional to the *square* of the coupling. This is what makes the Born rule come out
  amplitude-**squared**.
- **Lindblad / master equation** — the standard equation for an "open" quantum system
  leaking into its environment (decoherence). It's *linear* and averages out individual
  randomness — the MRI **Bloch equations** are exactly this kind.
- **CSL (continuous spontaneous localization)** — a family of modified quantum theories
  where the wavefunction is continuously, randomly nudged to definite outcomes (real
  collapse), engineered so the *average* still obeys ordinary linear QM (hence no
  faster-than-light signaling). Our sync mechanism lives in this family.
- **On-shell / off-shell** — "on-shell" = a particle obeying $E^2=p^2c^2+m^2c^4$ (real,
  propagating); "off-shell" = breaking it temporarily on borrowed energy (virtual). The
  "shell" is the surface where that equation holds.
- **Energy-time uncertainty** — the relation $\Delta E\,\Delta t\gtrsim\hbar$: a state
  with energy spread $\Delta E$ only stays coherent for a time $\sim\hbar/\Delta E$. In
  our reading it's the off-resonance "slip time" of an oscillator that fails to lock.

## C. Cosmology terms

*(Used in the cosmology note.)*

- **Friedmann equation** — cosmology's master equation: expansion rate squared is
  proportional to total energy density, $H^2\propto\rho$.
- **Hubble rate $H$** — the fractional rate the universe expands, $H=\dot a/a$ (where $a$
  is the scale factor). Roughly $1/(\text{age of universe})$.
- **Equation of state, $w$** — a substance's pressure-to-density ratio, $w=p/\rho$; it
  dictates how its density dilutes as the universe expands. $w=-1$ is a true constant
  (dark energy that never dilutes); $w\neq-1$ means *dynamical*, time-varying dark energy.
- **ΛCDM** — the standard cosmological model: a cosmological constant Λ (dark energy at
  exactly $w=-1$) + cold dark matter. The baseline everything is measured against.
- **de Sitter** — the geometry of a universe ruled by constant dark energy; expands
  exponentially forever (ΛCDM's far future).
- **Quintessence / phantom / quintom** — flavors of *dynamical* dark energy: quintessence
  $w>-1$ (our prediction), phantom $w<-1$, quintom crosses between. (DESI is testing which.)
- **CPL ($w_0$, $w_a$)** — the standard two-number summary of how $w$ drifts with time,
  $w(a)=w_0+w_a(1-a)$: today's value plus its rate of change. What surveys fit.
- **Foliation** — slicing a higher-dimensional space into a stack of sheets ("leaves"),
  like slicing a loaf. Slicing spacetime into "space at each instant" = choosing what
  "time" means; we slice by constant sync-phase.
- **Cosmological constant problem** — the notorious ~$10^{120}$ mismatch between the naive
  quantum guess for vacuum energy and what's observed. Our mechanism *relocates* it (into
  the unexplained "floor") but doesn't solve it.
- **Renormalization group (RG) / fixed point / IR** — a tool for how a system's effective
  behavior changes as you "zoom out" to larger scales (the "infrared / IR" end); a "fixed
  point" is behavior unchanged by zooming — an attractor. We floated cosmic expansion as a
  zoom-out flowing toward the critical fixed point.
- **Analog gravity** — the result that ripples on a flowing medium (a condensate, a fluid)
  experience an effective curved spacetime; we use it to say excitations on the synced
  substrate see a Lorentzian metric.

## D. A few named touchstones

- **Schwinger critical field** — the electric-field strength $E_c=m^2c^3/e\hbar$ at which
  the vacuum does enough work over a Compton wavelength to turn virtual pairs into real
  ones; the textbook "escape past a threshold."
- **Supernova time-dilation / Tolman test** — two observational checks any redshift
  mechanism must pass: distant supernova light-curves are stretched by $(1+z)$, and
  surface brightness dims as $(1+z)^{-4}$. Genuine metric expansion passes; "tired-light"
  alternatives fail.
- **TDGL (time-dependent Ginzburg–Landau)** — the equation $\dot r=-\partial_r f$ that
  rolls the order parameter downhill on the Landau landscape; the "overdamped" (no
  inertia) dynamics behind our relaxation rate $\Gamma=2\varepsilon$.
