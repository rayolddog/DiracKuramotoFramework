# The single-photon avalanche: an honest phase-reduction attempt

*Working derivation note (for §7 of `DIRAC_HEISENBERG_CUT_PAPER.md`). Goal: carry
H(sys+det+bath) → reduced dynamics → the two-basin registration → the record, with the rate
derived from the actual electromagnetic coupling, for a single-photon avalanche detector.
**Result up front:** the derivation succeeds and gives a rate from real EM parameters — but it
lands on a **bistable-amplitude (branching-escape)** reduction, NOT an Adler **phase** reduction.
That is a genuine finding, not a failure: it tells us the photon counter is a different
dissipative class from the meter-oscillator case, and it sharpens what "synchronization" may
and may not mean. Details and the recommendation below.*

---

## 1. The device and the three ingredients

A Geiger-mode single-photon avalanche detector (SPAD) or photomultiplier, biased above
breakdown $V>V_{\rm br}$. Three parts:

- **Absorber** — a bound electron modeled as a two-level/threshold system, $|g\rangle$ (bound)
  → $|e\rangle$ (liberated carrier), coupled to the incident single-photon mode $a$.
- **Multiplier** — a high-field region of width $w$, field $E=V/w$, carrier number $n$, in which
  carriers impact-ionize. The **bias voltage is the free-energy reservoir** (Stage 3).
- **Bath** — phonons and thermal carriers, supplying dissipation and the noise $\xi(t)$.

## 2. Stage 1 — capture (the absorption POVM), and a first honest signal

Absorption is the Jaynes–Cummings vertex

$$ H_{\rm c} = \hbar g\,(a\,\sigma_+ + a^\dagger \sigma_-), $$

taking $|1\rangle_\gamma|g\rangle \to |0\rangle_\gamma|e\rangle$. For a photon in $\alpha|0\rangle+\beta|1\rangle$
the capture is a POVM element $\propto|1\rangle\langle1|$ with intrinsic efficiency $\eta_{\rm abs}$;
it liberates one seed carrier, $n:0\to1$.

The clock here is the **photon frequency $\omega$**, imprinted on the electron during the vertex;
it is *not* a chiral clock (a photon is not a Dirac spinor). And note the first honest signal:
a **single** photon is annihilated at capture, so it provides **no persistent phase reference to
lock to**. Whatever happens next is not "phase-locking to the incident field" — the field is
gone. Stage 1 leaves a seed carrier, not an ongoing drive.

## 3. Stages 2–3 — the multiplication, and the rate from electromagnetism

The carrier number in the high-field region obeys a mean-field-plus-noise rate equation,

$$ \dot n = \underbrace{[\,\alpha(E)-\beta_{\rm loss}\,]\,v_d}_{\displaystyle \equiv\,\gamma(V)}\;n \;-\; c\,n^2 \;+\; \sqrt{2D\,n}\,\xi(t), $$

with

- $\alpha(E)$ — the **impact-ionization coefficient** (ionizing collisions per unit length), a
  steep function of the field, $\alpha(E)\sim A\,e^{-b/E}$ (Chynoweth);
- $v_d$ — carrier drift velocity; $\beta_{\rm loss}$ — extraction/recombination loss;
- $c\,n^2$ — space-charge saturation (self-limits at $n_{\rm sat}$);
- $\sqrt{2Dn}\,\xi$ — multiplicative shot noise, $D$ set by the ionization branching statistics.

**The rate $\gamma(V)=[\alpha(E)-\beta_{\rm loss}]\,v_d$ is derived from real electromagnetism** —
the ionization coefficient, the drift velocity, and the bias field $E=V/w$. This is the concrete
deliverable: a "locking-rate" analog computed from the detector's actual EM parameters, not
asserted. $\gamma$ changes sign at breakdown: $\gamma(V_{\rm br})=0$.

## 4. The two basins — a branching process with extinction vs. self-sustaining avalanche

For $V>V_{\rm br}$ ($\gamma>0$) the seed carrier initiates a **branching (Galton–Watson) process**:
each carrier ionizes and produces further carriers before being extracted. Two fates:

- **Extinction** ($n\to 0$): the seed and its progeny leave the high-field region before a
  self-sustaining chain forms → **no click**.
- **Survival** ($n\to n_{\rm sat}$): the chain runs away to space-charge saturation → **click**.

The survival (avalanche-triggering) probability $P_{\rm trig}$ is the branching-process
non-extinction probability. With generating function $F(s)$ for the per-carrier offspring, the
extinction probability $q$ is the smallest root of $q=F(q)$, and $P_{\rm trig}=1-q$; $P_{\rm trig}$
turns on continuously above breakdown (McIntyre). It is fixed by the ionization ratios and the
geometry — again, **EM-derived**.

**The cut and reversibility.** Below the self-sustaining size (a few carriers) the incipient
avalanche can still go extinct or be quenched — this is the **reversible Stage 2** (a passive- or
active-quench circuit exploits exactly this window). Once the chain exceeds the self-sustaining
threshold, extinction probability $\to 0$ and the space-charge-limited avalanche is an
**irreversible Stage-3 record**. **The Heisenberg cut for this detector is the avalanche-triggering
threshold** — a concrete, bias-tunable size, not a universal location.

## 5. Where is the phase $\delta$? There isn't one — and that is the point

The reduced variable is the **carrier number $n$** — real, non-negative, an amplitude — and the
dynamics is a **branching/escape** process. There is no phase $\delta$ on a circle, no
$\sin(N\delta)$, no Adler equation. The two-outcome structure (extinction / survival) is genuine,
but it lives in an **amplitude**, not a phase.

So the honest verdict on the single-photon counter:

> It yields a legitimate two-outcome dissipative reduction with the rate $\gamma(V)$ and the
> outcome-triggering probability $P_{\rm trig}$ **derived from electromagnetism** — but it is a
> **bistable / branching *amplitude*** reduction (extinction vs. self-sustaining avalanche),
> **not an Adler *phase* reduction.** The word "synchronization" (phase-locking) does not
> literally apply to a photon counter. What applies is the more general "dissipative attraction
> into one of the apparatus's pointer basins," of which phase-locking is only one realization.

Two supporting reasons this was to be expected, visible in the derivation: (i) a single photon
leaves no persistent phase to lock to (§2); (ii) a photon counter measures **number**, and number
is conjugate to phase — so a *relative-phase* hidden variable is not the natural order parameter
for a *number* outcome.

## 6. The structural payoff — assign each detector its reduction class

Taking the derivation seriously reveals that measurement reductions come in (at least) two
classes, and forcing one form on all detectors is the overreach a careful reviewer would catch:

| Class | Order parameter | Reduction | Detectors |
|---|---|---|---|
| **Phase-Adler** (meter oscillator) | meter-field phase $\delta$ | $\dot\delta=\Delta\omega-\gamma\sin\delta+\eta$ | dispersive / QND readout (circuit-QED, homodyne — Appendix D of the framework paper) |
| **Amplitude-bistable** (branching escape) | carrier number $n$ | $\dot n=\gamma n - c n^2 + \text{noise}$; extinction vs. survival | direct single-photon counters (SPAD, PMT) |

Stern–Gerlach sits nearer the phase class (the spin azimuth is projected, though the recorded
variable is packet position); the hologram and cloud chamber are continuous pointer manifolds
built from many local amplitude-bistable commits. The common umbrella — the honest generalization
— is **"dissipative attraction into the apparatus's stable pointer basins"**, with phase-Adler and
amplitude-bistable as two sub-mechanisms.

## 7. Recommendation for the paper

- **Do not present the single-photon avalanche as a phase-Adler synchronizer.** The derivation
  shows it is the amplitude-bistable class. Presenting it otherwise is exactly the "synchronization
  = metaphor" charge, and it would not survive a careful read.
- **For the one worked *phase*-Adler derivation** (the burden §7 names), use the **dispersive/QND
  meter** — the circuit-QED model already in the framework paper's Appendix D — where a genuine
  meter-oscillator phase is injection-locked. That case earns "synchronization" literally.
- **Reframe §7 around two reduction classes**, not one law. This is stronger and more honest than
  forcing Adler everywhere: it turns "is synchronization real or a metaphor?" into "here are the
  two dissipative reduction classes, each with a worked example (QND → phase-Adler; SPAD →
  amplitude-branching), unified as entrainment into pointer basins." That is a taxonomy *with
  derivations*, which is what the reviewer asked for.

## 8. What is still owed (unchanged by tonight)

- **Born is still not derived.** For a photon in $\alpha|0\rangle+\beta|1\rangle$ the click probability is
  $\eta_{\rm abs}\,P_{\rm trig}\,|\beta|^2$: the detector factor $\eta_{\rm abs}P_{\rm trig}$ is
  EM-derived here, but the $|\beta|^2$ is the **imported** Born weight. The derivation gives the
  *detector response*, not the *quantum weight*. Consistent with the paper's parked scope.
- **The full device master equation** (a real SPAD has dead space, afterpulsing, and a quench
  circuit) is sketched at mean-field level here; a complete treatment is a separate task.
- **The QND phase-Adler derivation** (the other class) still needs to be written out cleanly from
  Appendix D — that is the natural next session.

---

*Bottom line for the morning: I did carry the single-photon counter from Hamiltonian to a
two-outcome record with the rate from real electromagnetism. The honest surprise is that the
counter is bistable-amplitude, not phase-Adler — so the cleanest move is to let the four-detector
zoo span **two** reduction classes, put the phase-Adler derivation on the QND meter where it
genuinely belongs, and keep the photon counter as the amplitude-branching exemplar. That is a
better answer to the reviewer than a single forced law would have been.*
