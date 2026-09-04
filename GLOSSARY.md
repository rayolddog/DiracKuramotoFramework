# Glossary — the program's vocabulary in plain terms

*Written 2026-09-04 for the sponsor, who is a physician and a self-taught programmer, and
for any later session that starts cold. Three dialects are mixed in this repository: the
physics of the three papers, the stochastic-simulation vocabulary of the race package and
its validation campaigns, and the survival-statistics vocabulary underneath both. Each
entry gives the plain meaning first, then the nearest relative in medicine or statistics
where one exists. Nothing here changes any definition in the papers; where a paper's
definition is the authority it is cited.*

---

## 1. The physics of the papers

**Wave packet / incident quantum.** The photon (or particle) arriving at the detector,
spread over every candidate absorbing site it can reach. Paper 1 treats it as a real wave
(premise P0), not as a probability amplitude.

**Site.** One candidate absorber — an atom, a grain, a carrier packet in silicon — that
could end up registering the quantum. A detector face has many; the papers' simulations
use 2 to 100, a real silicon face about $10^{10}$ in the diffraction volume.

**Share, $s_i$.** A site's fraction of the one quantum during the selection stage. Paper 1
premise P1 sets the initial shares proportional to the local intensity, $|A_i|^2$. Whether
a share is a physical energy that could be dissipated (reading A) or a bookkeeping
amplitude that becomes energy only when a site takes the whole quantum (reading B) is the
fork of Paper 1 §9.4(xi); v0.9 adopted B as the working choice.

**Exchange game / fair game.** Paper 1's selection dynamics: sites trade share in
zero-mean random steps until one holds the whole quantum. "Fair" means no site is favoured
by the noise (Theorems 1–3). *Statistical relative:* a martingale — a gambler's-ruin
process in which the expected fortune never changes.

**First passage.** The moment a site's share first reaches the whole quantum, ending the
game (Theorem 0). *Relative:* time-to-event, the quantity a Kaplan–Meier curve tracks.

**Commitment / first irreversibility.** The moment a site's excitation can no longer be
coherently returned to the field — fixed on 2026-09-02, before application, as the
paper's operational meaning of commitment (ledger E-16). Not the avalanche, not the
electrical pulse: in silicon it is the interband vertex plus thermalisation, 10 fs to 1 ps.

**Registration.** Writing the record: the avalanche, the hotspot, the developed grain.
Paper 3's Stage 3. Contributes no statistics of its own.

**$\theta = E_{\rm gap}/E_{\rm photon}$.** The share below which a site in a gapped absorber
has no real final state. Under reading A a site can commit only above $\theta$ (0.45 for
silicon at 500 nm); under reading B there is no gate. At $E_{\rm photon} > 2E_{\rm gap}$
(silicon below 553 nm) the quantum could pay for two real pairs and only premise P4(a)
forbids it.

**Born rule / Born weight / the square.** Outcome probability equals the squared amplitude,
$|A_i|^2$. In the race's language it is the statement that the hazard ratio between two
channels equals the ratio of their squared couplings. The papers do not derive it; they ask
what dynamics realizes it.

**Golden rule (Fermi's, derived by Dirac in 1927).** $\Gamma = (2\pi/\hbar)\,|\langle f|H'|i\rangle|^2\,\rho(E)$:
a transition into a continuum of final states proceeds at a constant rate, linear in the
coupling squared. Its two structural properties — a rate that is constant in time
(memoryless) and linear in the intensity — are exactly what the energy race needed and
what Paper 1's Theorem 5 and reading B import.

**Exclusivity / one-quantum constraint (premise P5).** Exactly one site registers the
quantum, however far apart the candidate sites are. Paper 1 v0.7 concedes this is a
nonlocal premise; the exclusivity discriminator measured that it must act within about a
thousandth of the commitment time, orders of magnitude faster than light crosses a
beamsplitter.

**Ensemble reading vs one-world reading.** Whether the golden rule's rate describes only
an average over many trials (ensemble) or each trial has one definite outcome (one-world).
Coincidence data at a balanced split ($g^{(2)}(0) \approx 0.002$) exclude independent
per-site rates by a factor of 400: the selection is one-world.

**Adler equation.** $\dot\theta = \Delta - K\sin\theta$: the phase error $\theta$ of a
clock driven at coupling $K$ with natural detuning $\Delta$. Named for Robert Adler's 1946
injection-locking equation (not Stephen Adler's collapse work).

**Arnold tongue.** The region $|\Delta| < K$ in which a clock can lock at all. Its width,
$2K$, is proportional to the field amplitude; it is a property of the physics, not of any
criterion.

**Locking rate / contraction rate.** $\sqrt{K^2 - \Delta^2}$: how fast a clock inside the
tongue relaxes to its stable phase. Fastest at the tongue's centre, zero at its edge.

**Rate sum / semicircle.** The sum of locking rates over the eligible clocks of a flat
detuning grid, $\approx (\pi/2)K^2/h$: tongue width ($\propto K$) times mean rate
($\propto K$). The plan's candidate mechanism for the square.

**Eligible count / width-only.** The number of clocks inside the tongue, $\propto K$: the
linear comparator.

**Lock tolerance (band).** A phase-angle window (0.35 rad) inside which a clock counts as
locked. A criterion, not physics; a band in phase space, not in the tongue's space.

**Dwell.** How long a clock must stay inside the band before it counts as committed (0.5
time units, fixed for every site and amplitude in the primary model). A criterion.
*Tuned dwell:* a dwell that depends on the coupling — an amplitude-dependent criterion
the plan allows only as a labelled control.

**Phase diffusion, $D$.** The strength of the independent, amplitude-neutral random kicks
to each clock's phase (0.08 frozen). The race's "bath."

**Hazard.** A site's probability per unit time of committing, given that it has not yet.
*Relative:* exactly the hazard function of survival analysis; the outcome of a two-channel
race is set by the hazard ratio at each instant.

**Memoryless (Poisson) commitment.** A hazard that is constant in time: exponential
waiting times, hazards that add across sites. The property deterministic locking lacks
and the golden rule has.

**Entry-time order statistics.** The distribution of the fastest of $N$ near-deterministic
slides from random starting phases; it gains only logarithmically in $N$ where a Poisson
race gains a full power. The computed source of the fixed-dwell race's exponent of 1.5.

**Exponent, $p$.** The fitted slope in $P_A/(P_A+P_B) = K_A^p/(K_A^p + K_B^p)$: 1 is
amplitude-linear, 2 is Born. *Relative:* the slope of a dose–response curve in a probit or
logit analysis; the 45° cell is the LD50.

**Comparator.** A predeclared alternative curve the data are scored against (linear,
Born, strongest-wins, rate-sum race, width-only race). *Relative:* a control arm.

**Diagnostic (label).** A result produced at a numerical budget the package's own gate
has not passed. Every race result in this repository carries it.

## 2. The race package and its validation campaigns

**Raw process / raw-process boundary.** The part of the package that generates events. It
is structurally forbidden from importing the prediction it will be compared with, so no
squared amplitude or prescribed hazard can reach the event generator. *Relative:*
blinding.

**Keyed noise.** Every random kick is derived from a key naming the trial, clock and time
step, never from a sequential generator, so a clock's realization does not depend on
batch size or loop order. *Relative:* a pre-generated randomization list.

**Master trial / replicate.** One realization of the physical noise (master trial) and
the auxiliary re-walks used by the audit (replicates).

**Ladder / refinement.** The same computation repeated at a timestep, then half of it,
then a quarter, to see whether the answer stops changing. "Converging" means the changes
shrink; a "reversal" is a step that moves the wrong way.

**Oracle (killed diffusion).** An independent partial-differential-equation solution of
the stationary problem, used as the continuum truth against which the endpoint scheme is
checked. *Relative:* a reference assay.

**Endpoint scheme.** The package's own way of deciding, from sampled phases, whether a
clock stayed in the band for the dwell. The thing being validated.

**Moving-band audit.** A Brownian-bridge diagnostic that can only add hidden band exits
between samples; measures what the endpoint scheme misses during a pulse. A diagnostic
beside the primary ledger, never a correction to it.

**Added-resets mean, and its cap.** How many hidden exits the audit adds per history; a
count that grows with the number of steps and has no continuum limit. Its cap of 3.0 was
frozen for the reference cell's granularity and fires at every finer step.

**Budget / allowance.** The numerical error a stage may carry: one quarter of the planned
statistical half-width for probabilities (0.005), and for times 0.02 plus one timestep.
*Relative:* assay precision requirements set from the trial's power calculation.

**Bound.** $|{\rm measured}| + 2\,{\rm SE}$, the number compared with the allowance.

**Gate.** A pass/fail rule applied before any interpretation is allowed. *Relative:*
quality control on an assay; a failed gate means no clinical read, not a negative result.

**`numerical_no_result`.** A gate failed: interpretation is blocked, nothing physical is
falsified, and the budget is not widened. *Relative:* an assay that failed QC.

**`unresolved` / `satisfied`.** Dispositions short of, and at, a passed budget.

**Blocker.** The named reason a disposition is not satisfied (e.g. `endpoint_envelope_
exceeds_allowance`, `probability_window_empty`).

**Evidence row.** One measured discrepancy, with its standard error, at one observable and
position, tagged by whether it was measured at the intended configuration.

**Intended configuration.** The physics the production sweep would use: 64 clocks on the
±3 grid, timestep $2^{-9}$, pulse 4.0, diffusion 0.08, tolerance 0.35, dwell 0.5.

**Reference cell.** The smaller configuration the package's own checks were run at;
evidence from it is tagged `non_intended`.

**Stage (S1–S4, M5–M7).** One validation computation in the frozen outline: stationary
probability at three refinements, a stationary time quantile, and moving-band probability
and time at two refinements and two trial multipliers.

**Stop rule / dependency rule.** A later stage never runs on a predecessor that returned a
no-result. **Override:** the sponsor's decision to run it anyway, quoted in the record.

**Pilot / production.** Software words for a clinical-trial structure: a pilot may choose
only the coupling range and its trials never enter the estimate (phase I); production is
the definitive, fully validated sweep whose numbers would be published, frozen before it
is opened. Nothing commercial.

**Manifest / frozen / digest.** A frozen manifest lists every input and rule of a run and
carries a hash (digest) of itself; a later reader can check nothing changed after the
results were opened. *Relative:* a pre-registered protocol with a timestamped record.

**Re-freeze.** A sponsor's change to a frozen design, recorded in a new hashed manifest
with its reasons. The 2026-09-04 re-freeze kept survival and the time rows and dropped
the exit-count fields and the commit-time quantile.

**Preflight / ceiling.** An estimate of a stage's time and memory from measured rates
before it launches, and the wall-clock and memory limits (one hour, then three; 2 GiB)
that stop it.

**Pricing.** Conservative cost estimates — machine time and memory, not money and not AI
usage — for each stage, from the slowest measured kernel rate times 1.5. A price is not
an approval.

**Power / half-width.** How many trials per cell buy a stated confidence half-width on
the exponent (target 0.25). *Relative:* sample-size calculation.

**Admissible trials.** The largest trial count at which every evidence row's bound still
fits the allowance the design implies; the design needs 2 406.

## 3. Statistical terms, with their medical relatives

| term here | plain meaning | relative |
|---|---|---|
| hazard | probability per unit time of the event, given survival so far | hazard function; Cox model |
| hazard ratio | ratio of two channels' hazards | the same term |
| memoryless | constant hazard | exponential survival |
| first passage | time at which a threshold is first reached | time to event |
| survival curve | fraction not yet committed at each time | Kaplan–Meier |
| censoring | a trial that ended (pulse closed) before the event | administrative censoring |
| unresolved trial | no commitment before the pulse closed | censored at end of follow-up |
| exponent $p$ | slope of the outcome sigmoid in log coupling ratio | probit/logit slope; dose–response |
| 45° symmetric cell | the point where the two channels are equal | LD50 |
| deviance | goodness of fit of a fixed curve to binomial counts | GLM deviance |
| Wilson interval | confidence interval for a proportion | binomial CI |
| profile likelihood interval | interval on a fitted parameter | fiducial limits |
| comparator | a predeclared alternative curve | control arm |
| pre-registration | fixing definitions and predictions before opening results | the same |
| `numerical_no_result` | the assay failed its own QC | no clinical read |
| pilot / production | range-finding run / definitive run | phase I / definitive trial |
| bootstrap SE | uncertainty from resampling master trials | the same |

## 4. Where to look

- Paper 1 (`drafts/PAPER1_DRAFT_born_selection.md`, v0.9) for the premises and theorems.
- The reconciliation ledger (`drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md`) for
  every finding of 2026-09-01 to 09-04, with its uncertainty stated first.
- `adler_two_channel_exploratory/RESULTS.md` for the race results and their non-claims.
- `adler_two_channel_exploratory/validation/` for the campaign records and reports.
