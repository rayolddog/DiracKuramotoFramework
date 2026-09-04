# Recoverability test of the Heisenberg-cut threshold — predictions, fixed before running

*2026-09-04. Written before `fano_recoverability.py` was run, at the sponsor's instruction
("start the recoverability test with the predictions on record"). Nothing below was
changed after the results were opened; the results file scores each prediction.*

## What Paper 2 claims, in the form to be tested

Paper 2 (*The Heisenberg Cut as a Physical Threshold*, v0.3, §3–§4) makes three testable
statements about a captured quantum:

- **P2-L (location).** The cut is where in-principle recoverability ends, and it sits at
  $\kappa_{\rm ret}/K = 1$: the deficit-induced return rate of an off-shell site,
  $\kappa_{\rm ret} = \Delta E/\hbar$, equals the site–field coupling $K$. Below that ratio
  the site can hold the quantum (lock); above it the excitation returns to the field.
- **P2-W (width).** The crossover has relative width $w = K/\omega$, the coupling over the
  carrier frequency — $10^{-6}$ for atomic lines, $10^{-2}$ for broadband solids (Paper 2
  §3.3's table).
- **P2-C (completion).** Irreversibility enters at lock *completion*, when one site holds
  the whole quantum; before that the capture is reversible in principle (echoes, quantum
  memories; Paper 2 §4.1, Paper 1 §3), and the record is written afterwards.

## The model

The smallest exact system that contains capture, off-resonant return, and an
irreversible record channel: one photon mode $|p\rangle$, one absorber excitation
$|e\rangle$ detuned by $\Delta$ from the photon, and $N$ record modes $|k\rangle$ spread
over a bandwidth $B$ around the absorber's energy, all in the single-excitation sector
(dimension $N+2$, so $N$ can be hundreds):

$$H = \Delta\,|e\rangle\langle e| + \sum_k \epsilon_k |k\rangle\langle k|
    + K\,(|p\rangle\langle e| + {\rm h.c.}) + \sum_k g_k\,(|e\rangle\langle k| + {\rm h.c.}),$$

$g_k = g/\sqrt N$, so the golden-rule decay rate of $|e\rangle$ into the record modes is
$\Gamma = 2\pi g^2/B$, independent of $N$; $N$ controls only how long the bath behaves as a
continuum (recurrence time $\sim 2\pi N/B$). This is the Wigner–Weisskopf / Fano model
with the photon added as a second, coherent channel. It is the single-absorber,
many-record-mode version of the 576-state model's `H_capture` plus `H_mark`, whose one
record qubit is the $N = 1$ case; its recorded numbers (operational return 0.83 at
$G = 0.1$, 0.09 at $G = 0.3$, 0.25 at $G = 0.5$ for $K = 0.85$, dark time 1.9) are the
$N = 1$ check.

**Recoverability** is defined operationally, as Paper 2 does: capture for a time $t$ under
$K$, then apply the reversal an experimenter has, $K \to -K$ for the same time with the
detuning and the record couplings left running, and read off the fraction of the photon
returned to $|p\rangle$: $R = |\langle p|\psi_{\rm final}\rangle|^2$. (Paper 3 §4 and the
576-state README: the exact global inverse is a mathematical Loschmidt reversal, not an
operation; reversing $K$ alone is.)

## Predictions

1. **No bath ($\Gamma = 0$): $R = 1$ at every $K$, $\Delta$, $t$.** Capture is reversible
   in principle. (Paper 2 §4.1; already verified in the 576-state no-bath slice to
   $10^{-15}$; re-verified here as the calibration.)
2. **Single record mode ($N = 1$): $R$ oscillates in $g\,t$, is not monotone in $g$, and
   never settles.** One record qubit is a coherent partner, not a bath; the 576-state
   model's non-monotone return (0.83 → 0.09 → 0.25) is this. *Consequence on record:* the
   existing 576-state model cannot exhibit Paper 2's threshold as it stands; a
   many-mode record subsystem is required, which is why this test builds one.
3. **Dense bath ($N \gg 1$, $t \ll 2\pi N/B$): $R$ falls monotonically with captured time,
   as $\exp(-\Gamma_{\rm eff}\,t)$ with $\Gamma_{\rm eff} = \Gamma \times$ (the fraction
   of the time the excitation spends on the absorber).** The record channel is
   irreversible on any time short of the recurrence; what leaks does not come back.
4. **P2-L, the location: at fixed $\Gamma t$, $R$ as a function of $\Delta/K$ is a
   crossover centred at $\Delta/K \approx 1$.** Inside the tongue ($\Delta < K$) the
   excitation dwells on the absorber and leaks; outside ($\Delta > K$) it is off-shell,
   returns at rate $\sim\Delta$, spends a fraction $\sim K^2/\Delta^2$ of its time on the
   absorber, and leaks slowly. The crossover's midpoint in $\Delta/K$ is the quantity to
   compare with Paper 2's $\kappa_{\rm ret}/K = 1$. *Expected: near 1, within a factor of
   two; the model's own fixed point is at $\Delta/K = 1$ by the same balance argument.*
5. **P2-W, the width: in this model it is of order one in $\Delta/K$, not $K/\omega$.**
   The rotating-wave exchange coupling contains no carrier frequency, so nothing in the
   model can produce $K/\omega$; a linear two-level absorber's occupation off resonance is
   the Lorentzian $K^2/(K^2+\Delta^2)$, whose width in $\Delta/K$ is order one. *If the
   measured width is of order one, that is not a falsification of Paper 2: it says the
   sharp layer of Paper 2 is a property of a nonlinear, self-sustaining absorber (Adler
   locking with its counter-rotating terms), which a linear absorber cannot show, and the
   width claim needs a stage-2 model with a limit-cycle absorber and no rotating-wave
   approximation. If the width comes out much narrower than order one, prediction 5 is
   wrong and something in the linear model sharpens it.*
6. **P2-C, completion: recoverability does not switch off at any share threshold in this
   model; it degrades continuously with $\Gamma_{\rm eff} t$.** The model has no lock
   threshold (it is linear), so it can test whether continuous leakage alone reproduces
   the phenomenology; a threshold at $s = 1$ would need the nonlinear stage-2 absorber
   as well. *On record: this model is expected to show P2-C's ordering (capture
   reversible, record irreversible) but not its sharpness.*
7. **Dependence on the bath's bandwidth $B$ at fixed $\Gamma$: none in the golden-rule
   regime ($B \gg \Gamma, K, \Delta$).** If $R$ depends on $B$ at fixed $\Gamma$, the bath
   is not in the memoryless regime and the E-16 Markov ratio enters here too.

## What would count as what

- Predictions 1–3 are calibration; failing any of them means the model, not Paper 2.
- Prediction 4 confirmed: Paper 2's location survives in the smallest exact model that
  has capture, return and a record channel. Refuted (midpoint far from 1, or no
  crossover): Paper 2's location claim fails in the linear model and the paper must say
  why locking is required for it.
- Prediction 5: whichever way it goes, it fixes the *scope* of Paper 2's width claim, and
  is the finding this stage exists to make.

## Grid

$K = 1$ (units); $\Delta/K \in [0.05, 20]$ log-spaced (41 points); $\Gamma \in
\{0.05, 0.2, 1.0\}$; captured time $t \in \{1, 3, 10\}$ (so $\Gamma t$ from 0.05 to 10);
$N \in \{1, 4, 16, 64, 256\}$; $B = 40$ (golden-rule regime for $\Gamma \le 1$); record
modes uniformly spaced over $[-B/2, B/2]$ about the absorber energy. Exact propagation by
eigendecomposition; no integrator. Crossover midpoint: the $\Delta/K$ at which $R$ is
halfway between its inside-tongue plateau and its far-off-resonance value; width: the
$\Delta/K$ interval between the 25% and 75% points, divided by the midpoint.

## Addendum, 2026-09-04, written after the calibration and before the corrected run

**Prediction 1 failed, as a definition error.** With no bath, the operational reversal as
defined above ($K \to -K$, detuning left running) returned the photon only on resonance:
min $R$ over the $\Delta$ grid was 0.044, max 0.99999. The reason is elementary and the
576-state README states it: reversing $K$ alone inverts the capture term and nothing
else, so a detuning left running is never undone. Off resonance the $\{p, e\}$ dynamics is
a rotation about a tilted axis, and flipping $K$ tilts the axis the other way instead of
reversing the rotation. The $\Delta$-scan under that operation therefore mixes two
things, the detuning's non-reversal (present with no bath) and the record channel's
irreversibility (the thing under test), and predictions 4–7 cannot be scored on it.

**Corrected definition, fixed before the corrected run.** Recoverability is the *partial
Loschmidt echo*: forward under $H$ for $t$, then for $t$ under $H$ with the system block
reversed, $\Delta \to -\Delta$ and $K \to -K$, and the record modes' energies and couplings
left untouched. With no bath this is the exact inverse and gives $R = 1$ at every $\Delta$
by construction (to be re-verified); with a bath, whatever amplitude has entered the record
channel is not reversed, and the deficit from 1 is the record channel's doing alone. This
is the standard echo definition of in-principle recoverability with an untouched
environment, and it matches Paper 2's usage (§4.1: in-principle recoverability, not what a
particular reversal operation achieves). The operational $K$-flip result is kept on record
as $R_{\rm op}$, labelled as conflating the two effects.

**Predictions 2–7 stand unchanged, restated for the echo.** The sweep under the flawed
observable was printed before this addendum was written; it was not used to adjust the
predictions, whose content does not depend on the reversal protocol. One expectation is
sharpened by the calibration, not by the sweep: in the two-level system with off-diagonal
element $K$, the time-averaged occupation of the absorber is $2K^2/(\Delta^2 + 4K^2)$, so
the leak rate is $\Gamma_{\rm eff} \approx \Gamma \cdot 2K^2/(\Delta^2+4K^2)$, and the
crossover midpoint in occupation is at $\Delta = 2K$, the resonant Rabi frequency. If Paper
2's $K$ is the rate at which the coupling moves population (the Rabi frequency, as the
Adler $K$ is the rate of phase pull), that is $\kappa_{\rm ret}/K = 1$ exactly; if it is
the matrix element, it is 2. Both conventions are reported. The midpoint in $R$ is
expected to drift outward as $\Gamma t$ grows, because $R = \exp(-\Gamma_{\rm eff} t)$
reaches a given value at smaller occupation when $\Gamma t$ is larger; that drift is a
real feature (the location of the cut in this model is a statement about rates, not about
a fixed observation time), and its size is recorded.
