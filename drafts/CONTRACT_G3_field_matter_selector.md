# Selector contract — G3 (physical selector)

*Companion to the [G1/G2 microstate contract](CONTRACT_G1_G2_microstate_ontology_and_preparation.md). Status: **G3 does not close.** Terminal status remains `individual_selection_not_demonstrated`. This document exists to make the failure specific: two of the seven selection-contract questions are answered, three are partially answered, and two are blocked — one of them by the measurement problem itself.*

---

## 0. Verdict first

G3 requires "deterministic equations or a normalized stochastic kernel; physical noise, commitment current, unique record, quench, and closed ledger." Scoring against that list:

| Requirement | State |
| --- | --- |
| Deterministic equations conditional on noise history | **supplied** (semantics frozen in G1/G2 §1.5) |
| Physical noise | **supplied** (G2 §3.2: FDT-tied to `Gamma`, not free) |
| Exchange current between sites | **derivation sketch + numerical validation** (§1.2) |
| Unique record (exclusivity) | **structural argument** (§3), with one gap at P4(ii) |
| **Commitment current** | **absent** (§5) — this is the blocker |
| **Quench and energy routing** | **absent** (§4), and entangled with a foliation cost |
| Closed ledger | partial — energy yes, charge and information no |

Nothing here promotes the existing Adler implementation. It remains `machinery_only` and `numerical_no_result`.

---

## 1. The selector, as far as the equations actually go

### 1.1 Semantics

Frozen in the G1/G2 contract: `selector_semantics = deterministic_with_complete_noise_history`. The noise history `xi(t)` is a component of `lambda`, so the selector `F` is deterministic conditional on `lambda`. The stochastic-kernel form `K` is not available in this version and no conversion is permitted after freeze.

### 1.2 The exchange current, derived rather than posited

This is the one place where a "chosen as a function of target weight" objection can be answered, so it is worth being explicit.

Paper 1 Appendix D uses the exchange rule `delta = step * min(e_i, e_j) * (+/-1)`. That rule was chosen for a numerical convenience — it can never drive a site negative — and nothing physical selects a minimum. So the question is whether Born survives when the kernel comes from the field theory instead.

Start from the field–matter coupling `H_int = -sum_i d_i . E(x_i)`. Eliminating the shared field in the standard way leaves resonant dipole–dipole exchange with coefficients `J_ij`. Writing site amplitudes `a_i` with `e_i = |a_i|^2`:

```text
de_i = 2 Re(a_i^* da_i) ~ 2 Re( -i a_i^* sum_j J_ij a_j ) dt
```

Under P3(a) — which the G1/G2 contract now derives from the `U(1)` invariance of the ready-state measure rather than assuming — the relative phases are uniform and independent, so each cross term carries a random sign and the increment scales as the **geometric mean**:

```text
de_i ~ sqrt(e_i e_j) * xi
```

Not a minimum. The geometric-mean kernel *can* drive a site negative at finite step, so whether it reproduces Born is a step-convergence question, not a matter of assertion. Ten-site configuration, bright-site Born weight 0.500, 8000 trials (Monte-Carlo `sigma = 0.0056`):

| kernel | step | P(bright) | deviation | clamp rate |
| --- | --- | --- | --- | --- |
| `min` | 0.25 → 0.02 | 0.500 → 0.497 | ≤ 2.2σ | 0 by construction |
| `geom` | 0.25 | 0.4769 | **4.1σ** | 6.9e-3 |
| `geom` | 0.10 | 0.4945 | 1.0σ | 1.1e-3 |
| `geom` | 0.05 | 0.5025 | 0.4σ | 2.7e-4 |
| `geom` | 0.02 | 0.5045 | 0.8σ | 4.4e-5 |

The derived kernel converges to Born, and the finite-step bias tracks the clamp rate, which falls as `step^2`. The sign is informative: the bias is *negative*, toward equalization, which is Paper 1's own variant-(b) clipping failure reappearing as a controlled discretization artifact and vanishing in the continuum limit.

**What this establishes:** Born statistics do not depend on the ad hoc `min` rule. The kernel obtained by eliminating the field gives the same answer. **What it does not establish:** that `J_ij` has the right magnitude, range, or material provenance for any real detector — that is Gate A/G4, still open — and, more importantly, that this exchange has anything to do with *commitment* (§5). Code: `g3_drain_tests/exchange_kernel.py`.

### 1.3 What the exchange current is not

The exchange current moves energy between sites. It does not remove energy from the game, does not make anything irreversible, and does not produce a record. Every result in §1.2 concerns the *competition*, and the competition is the part of the problem that was never hard.

---

## 2. The drain: a sink that opens, not an attractor that pulls

JB's drain analogy (recorded 2026-07-04, `discussions/2026-07-04-three-stage-measurement.md:121`) was assessed then as a candidate exclusivity mechanism — "the absorbed quantum is *subtracted from the packet's tails*; insufficient energy remains for a second electron" — and logged with the timing note "drain provisional at Stage 2, final at Stage 3." That timing note turns out to carry the whole weight, and it is now settled numerically.

Two readings of "the packet goes down the drain":

- **Attractor.** The aperture grows with the energy already held, `g_i = gamma * e_i^alpha` with `alpha > 1`, active *during* competition. A drift term.
- **Commit-sink.** The aperture is zero until a site reaches the full-quantum boundary; it then opens and takes `hbar omega`. A boundary condition.

Ten-site configuration, bright-site Born weight 0.500:

| variant | P(bright wins) | mean steps to commit |
| --- | --- | --- |
| fair exchange | 0.506 | 7003 |
| commit-sink | 0.497 | 7049 |
| attractor, `gamma = 0.001` | **0.634** | 3827 |
| attractor, `gamma = 0.01` | **0.981** | 668 |
| attractor, `gamma = 0.05` | **1.000** | 133 |
| control: linear aperture `alpha = 1`, `gamma = 0.05` | 0.507 | 7037 |

The `alpha = 1` control confirms Paper 1's Theorem 2(i) — a linear return is exactly share-neutral; only super-linear gain is share-amplifying.

**The timing is decisive and the margin is not subtle.** A sink that opens on commitment leaves Born intact. A sink that pulls during competition destroys it: at `gamma = 0.01` the bright site wins 98% of the time against a Born weight of 50%.

**A second, independent signature.** The attractor commits roughly 50× faster. That is a latency handle, and it is the same wall the July assessment raised as "rate, not accumulation" — local accumulation predicts intensity-dependent first-click latency, excluded since Lawrence–Beams 1928. So an attractor drain is falsifiable twice over: once in the statistics, once in the timing, with no shared assumption between the two tests.

**Why this keeps happening.** The rogue wave, the attractor drain, and a lightning-style leader channel are one failure mode wearing three costumes: selection by instability. Instabilities are exponentially sensitive to the largest fluctuation, giving exceedance odds `~ exp(-a^2 / 2 sigma_i^2)`, exponential in `1/|A_i|^2`. Born needs odds *proportional* to `|A_i|^2`. Symmetry breaking by runaway is how physics normally makes one thing happen at one place, and it generically gives the wrong law. That is the content of "fairness is a knife-edge," and it is worth stating in the manuscript as a general theorem-shaped claim rather than a series of individual refutations.

Code: `g3_drain_tests/drain_variants.py`.

---

## 3. Exclusivity without sampling a categorical outcome

The review's finding 3 objects that "a first-threshold stop is an imposed event rule unless the competing physical channels are actually quenched." The closed-pot structure answers the first half of that.

Under a closed pot `sum_i e_i = hbar omega` and a registration threshold at the full quantum, **at most one site can ever be above threshold**, because two sites above threshold would require more than `hbar omega`. Exclusivity is therefore not an imposed rule and not a categorical draw; it is a consequence of energy conservation plus the threshold. Nothing samples an outcome index.

Two qualifications, both real:

**P4(ii) is not covered by that argument.** For continuum absorbers registration is a rate process operating throughout selection, so a site could in principle commit holding less than the full quantum, and conservation alone would no longer forbid a second commitment. The paper's position — that registration consumes the full quantum in both classes, so the threshold sits at `hbar omega` regardless — is asserted through Theorem 5's energy accounting but is nowhere stated as a premise. **It should be stated explicitly**, because the entire exclusivity argument rests on it.

**The no-record category must stay in the outcome space.** In the idealized closed-pot model the bounded martingale reaches a vertex almost surely, so `P(no click) -> 0`. Real detectors have a finite exposure window, and the truncated process has genuine no-record and (in principle) double-record probabilities. These map onto detection efficiency and are not to be conditioned away — the plan's requirement that no-click, multiple-record, invalid-trajectory, and ledger-failure outcomes remain in the primary outcome law.

---

## 4. The quench and the energy routing — open, and entangled with a foliation cost

When one site commits, the excitation at the other `N-1` sites has to go somewhere. Paper 1's position (§8.6(vi)) is that it returns reversibly to the field, leaving no calorimetric residue at the losing sites — which is consistent with the reversible-capture evidence (spin echo, photon echo, AFC quantum memory) and with the July wall that "leftover must be exactly vacuum."

**No equation routes it.** There is no term in any model in this repository that removes energy from the losing sites and returns it to the field, conditioned on a commitment elsewhere. This is one of the two hard blockers.

It is also the point where the nonlocality bites. Split a single quantum at a beamsplitter into two spacelike-separated arms. The pot must be closed *across* that separation, since the exclusivity argument of §3 is exactly a statement about one conserved total. Enforcing it at spacelike separation requires the ordering foliation.

### A finding for Paper 1: P6 is not quarantined

§2 of the manuscript claims: *"P5 and P6 are where the premises exceed standard physics, and they are quarantined: no single-detector result (§§3–5, §6.1) uses either."*

§3 of the same manuscript assigns Stage 2 this job: *"a classical pulse carrying one quantum of energy, split between two separated detectors, excites both and forbids neither from registering — whereas experimentally a single photon never produces a coincidence (anticorrelation at a beamsplitter). Supplying exclusivity — one full quantum at one site, the rest relaxed — without importing the Born rule to do it is precisely the job assigned to Stage 2."*

These are inconsistent. Beam-splitter anticorrelation is a single-quantum, single-detector-sector result, and supplying it through a closed pot requires foliation-synchronized enforcement. **P6 is consumed in the single-detector sector.** The quarantine claim is too strong and should be corrected.

This is not cosmetic. The quarantine is what allows the paper to present the single-detector theory as cheap — P0–P4 only, with the exotic premises confined to the entangled sector. If spacelike anticorrelation needs the foliation, the single-detector theory carries a preferred frame as well, and the honest cost of the mechanism is higher than §2 currently advertises. It is also precisely the July wall 1: the drain is nonlocal, so it *physicalizes* collapse rather than removing it.

---

## 5. The commitment current — the blocker

Everything above concerns how energy moves *between* sites and how the game *ends*. None of it touches the step that makes an outcome an outcome.

What is missing is an equation for the transition from **"site `i` holds `hbar omega`"** to **"site `i` has irreversibly registered."** Paper 1 supplies a taxonomy for this (P4), a proof that the outcome statistics do not depend on the rate's magnitude (Theorem 4), and a derivation that the rate is kinematically linear in occupation (Theorem 5). Those are statements *about* a commitment process. They are not the process.

This is the measurement problem, and it should be labelled as such rather than deferred to a later gate as though it were a modelling detail. Three specific things are absent:

1. **A current.** No `j_commit` with a source, a sink, and a conservation law.
2. **An irreversibility mechanism.** Something must make the transition not run backwards. Coupling to a bath supplies decoherence, which is not selection — the review's finding 3 states this correctly: field–matter evolution under strict unitarity yields entangled record branches, and phase locking does not select one as actual.
3. **A quench.** §4.

Until these exist, `F` remains a contract placeholder. The G1/G2 contract made this debt *larger*, not smaller, by refusing a registry beable: with no pre-actual winner label in `Lambda_1`, nothing in the ontology forbids two sites registering, and only the physics of §3 plus a quench can.

---

## 6. The seven questions, scored

| # | Question | State |
| --- | --- | --- |
| 1 | Which degrees of freedom possess phases capable of synchronization? | **Partial.** Ready-state modes identified (G1/G2 §2.3). But Theorem 2 says no *autonomous* phase exists below threshold, and the material audit found none in passive absorbers. See §7. |
| 2 | Which coupling is derived rather than chosen against the target weight? | **Answered.** Dipole–dipole exchange from `H_int`; geometric-mean kernel; converges to Born (§1.2). Magnitude/provenance still Gate A. |
| 3 | What establishes the detuning distribution and bath noise? | **Answered.** G2 §2.3 and §3.2 — measured lineshape; noise FDT-tied to `Gamma`, not free. |
| 4 | What constitutes locking, commitment, and irreversible registration? | **Partial.** Commitment *timing* settled (§2). Commitment *mechanism* absent (§5). |
| 5 | How is exactly one winner enforced without sampling a categorical outcome? | **Answered for P4(i)**, conditional on the full-quantum threshold being stated as a premise (§3). Open for P4(ii). |
| 6 | Where do the energy and charge of losing alternatives go? | **Open.** Energy: proposed return to field, no equation (§4). Charge: not addressed anywhere. |
| 7 | Which variables are ontic per event, ensemble descriptors only? | **Answered.** G1 §1.3. |

---

## 7. The superconducting lead, and the reason to be careful about it

The material audit's verdict was that sensitized silver halide contains no powered or self-sustained oscillatory degree of freedom capable of Adler locking, which is what reduced the Adler branch to a phenomenological fixture. A superconducting detector is the obvious place where that objection lifts.

A Josephson junction obeys an Adler-type phase equation in the RSJ model, driven by a real pump — the bias current — and its Shapiro steps are Arnold tongues. Check that against the audit's own "evidence that would change the verdict" list: free-running frequency, linewidth and phase diffusion; locking range versus detuning and injected amplitude; phase pulling and slips outside the range, stable offset inside. A Josephson junction satisfies every item, and each is measured extensively in the literature. In an SNSPD the superconducting order parameter carries a genuine phase field `phi(x)` with supercurrent `~ grad phi`, maintained by the bias current, and phase slips are localized discrete events with a well-defined rate — suggestive as a commitment mechanism in a way nothing in the passive-material picture is.

**Three cautions, and they are not small.**

1. **Phase-slip rates are exponential.** Thermal and quantum phase-slip rates go as `exp(-Delta F / k_B T)` and `exp(-S/hbar)`. If the *relative* commitment rate between sites is exponential in the local occupation, that is the exceedance disease of §2 all over again and Born fails. Theorem 4 tolerates an arbitrary *overall* rate; what it requires is that the conditional pick be `∝ s_i`, i.e. relative rates linear in occupation. **This is the sharp, checkable question for any superconducting realization**, and it should be settled before any modelling effort is committed.
2. **The avalanche is Stage 3.** SNSPD hotspot growth (Joule heating) and SPAD avalanche (impact ionization) are both runaway amplification — lightning. They are registration, not selection. Which point along the nanowire absorbed the photon is settled upstream, and Theorem 4 exists to prove the avalanche's properties do not leak back into the odds.
3. **What are the sites?** A single junction is not `N` competing absorbers. The competition would have to live in positions along a nanowire or in a junction array, and the `J_ij` of §1.2 would need to be the coupling in *that* geometry. This is a different material contract, not a transfer of the existing one.

### Literature answer (2026-08-31): the rate is exponential

The question above was put to the literature rather than to a simulation. The answer is **exponential**, and it arrives from three directions.

1. **The Adler correspondence is confirmed, not merely plausible.** The overdamped RSJ model is a standard dynamical system on the torus whose phase-lock areas are Arnold tongues, and injection locking in Josephson devices is treated with an explicitly Adler-form equation ([Phys. Rev. B **104**, 054517](https://link.aps.org/doi/10.1103/PhysRevB.104.054517)). So the machinery does transfer — that part of §7 stands.
2. **SNSPD commitment is barrier-limited.** The leading predictive model is a probabilistic single-vortex-crossing criterion, in which photon absorption redistributes the bias current and raises the crossing probability "even if the vortex potential barrier has not vanished completely." The model's stated success includes explaining "the experimental observation of **exponential decrease in the quantum efficiency** of SNSPDs at lower energies" ([arXiv:1901.09291](https://arxiv.org/abs/1901.09291)). That is Arrhenius form in absorbed energy, not linear.
3. **Measured nonlinearity runs the wrong way.** A direct single-source absolute-nonlinearity measurement found **supralinear** response in both SPADs and SNSPDs, and states the SPAD result "cannot be explained using known theoretical models" ([arXiv:2109.08347](https://arxiv.org/abs/2109.08347)). Supralinearity is the rich-get-richer signature, which is the §2 failure direction.

**What this settles and what it does not.** It settles that commitment in superconducting detectors is barrier-limited rather than occupation-linear, so the naive superconducting route inherits the §2 failure mode. It does *not* settle Theorem 5 directly: efficiency-versus-photon-energy is a single-site question (does a detection occur at all at this quantum energy), while Theorem 5 concerns the *relative* commit rate between sites competing within one event. The two are related but not identical, and no measurement of the latter was found.

**A caution that now runs toward the manuscript.** Theorem 5 derives a commit rate linear in site occupation from P2 plus energy conservation, and Paper 1 presents that as covering P4(ii) continuum absorbers. The best-characterized continuum single-quantum absorbers we have are exponential near threshold and saturating well above it — neither of which is linear. **Resolved 2026-08-31; see §7a.**

## 7a. The Theorem 5 / continuum-absorber check — resolved

Run as `g3_drain_tests/theorem5_check.py`. Commit **speed** (`q`, per-step firing probability) is separated from commit **law** (`f(e)`, the pick weight), so Theorem 4's claim can be tested independently of Theorem 5's.

*Validation anchor.* Paper 1 reports, for two sites at Born 0.800/0.200 with rate `∝ s^2` at fast commit, `P1 = 0.941` predicted and `0.938` observed. This implementation gives **0.928** — about 1% low, consistent with a different exchange discretization, close enough to trust the qualitative behaviour but not an exact reproduction.

**Theorem 4 confirmed.** With the linear law, Born holds at every commit speed tested (`q` = 0.5 → 0.001), deviations ≤ 0.002.

**A wrong rate law is catastrophic — but only at fast commit.** With an Arrhenius pick weight `f(e) = exp(beta*e)`, modelling a downstream activation barrier whose height falls as the deposit rises, at `q = 0.5`:

| `beta` | 0.5 | 2 | 5 | 10 | 20 |
| --- | --- | --- | --- | --- | --- |
| `P1` (Born 0.800) | 0.575 | 0.760 | 0.938 | 0.989 | 0.995 |

Note that the family crosses Born somewhere between `beta = 2` and `beta = 5`. A threshold model can therefore be *tuned* onto Born — which is exactly the "tuned into a linear-response window by hand" failure §4 of the manuscript warns about, now exhibited in the commit law rather than the selection law.

**But the paper's own timescale ladder puts it in the regime where none of this matters.** §6.1 gives `1.7 fs << 10–70 fs << 12–81 ps << ns–µs`, with irreversibility supplied by "the *slow* dissipative commit at the bottom of the ladder." That is `tau_game / tau_commit ~ 1e-2` to `1e-5`. Testing the worst-case law (`beta = 20`, effectively argmax) at those speeds:

| | `q=1e-3` | `q=1e-4` | `q=1e-5` | `q=1e-6` |
| --- | --- | --- | --- | --- |
| 2-site, Born 0.800 | 0.806 | 0.801 | 0.803 | 0.804 |
| 10-site, Born 0.500 | 0.719 | — | **0.504** | — |

The controlling quantity is the expected number of commit opportunities during the game, `q x (steps per game)`: the 2-site game runs ~112 steps, the 10-site game ~7003. At `q = 1e-3` the 10-site case gets ~7 opportunities and the rate law bites hard (0.719); at `q = 1e-5` it gets ~0.07 and first passage decides (0.504).

### Conclusion: Theorem 5 is not load-bearing

In the timescale regime Paper 1 itself establishes, Born is delivered by **first passage** (Theorem 0), and the commit-rate law — linear, Arrhenius, or otherwise — drops out. The empirical worry raised by the SNSPD literature therefore does **not** threaten the manuscript's predictions.

It does expose an internal inconsistency that should be fixed:

- **P4(ii)** says continuum absorbers register by "a rate process operating **throughout** selection," and §5.4 concludes "continuum absorbers by stopped rate-linear commitment (Theorems 4–5)." That is the *fast*-commit reading, in which Theorem 5's linearity is load-bearing and the measured Arrhenius behaviour of real continuum detectors would break Born.
- **§6.1** says commitment is slow, ns–µs against a ps game. That is the *slow*-commit reading, in which the rate law is irrelevant.

Both cannot describe the same detector. **Recommended fix:** adopt §6.1's ladder consistently. State that continuum absorbers also deliver Born by first passage, and demote Theorems 4–5 from "the mechanism by which P4(ii) absorbers deliver Born" to a *robustness* result — Born survives even in the counterfactual regime where commitment is fast, provided the rate is linear there. This is a strengthening: the paper then does not depend on Theorem 5's empirically doubtful linearity claim at all, and P4's two-class taxonomy collapses to one mechanism (Theorem 0) with a robustness rider.

**The one live thread.** In the phase-diffusion regime, switching rates fall *below* Kramers because of **retrapping** — the phase is recaptured after a slip, with the retrapping process governed by the environment's frequency-dependent impedance ([arXiv:1405.1876](https://arxiv.org/abs/1405.1876); [arXiv:1111.5088](https://arxiv.org/abs/1111.5088)). A reversible slip that can be retrapped is structurally much closer to what this framework needs than an irreversible barrier crossing: it is a *provisional* commitment that only becomes final when retrapping fails. That is the "drain provisional at Stage 2, final at Stage 3" structure of §2, appearing in real device physics with measured parameters. Whether the retrapping-limited rate is linear in local suppression is not answered in the sources found, and is the successor question.

**Revised recommendation:** the superconducting route is not a home for the mechanism as it stands, because its commitment step is Arrhenius. The retrapping sub-regime is worth one focused look, and the Theorem 5 / continuum-absorber tension above is now the more urgent item, because it is a problem for the manuscript regardless of whether the superconducting thread is pursued.

### Successor question: the multiple-retrapping regime has the right structure

Pursued 2026-08-31. In moderately damped and overdamped junctions the literature documents a **multiple-retrapping process**: the energy of an escaped phase particle is dissipated during its motion, so the particle is retrapped in another local minimum of the washboard, and the thermally activated escape-and-retrap cycle repeats ([Phys. Rev. B **79**, 104509](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.79.104509); [arXiv:0807.4502](https://arxiv.org/pdf/0807.4502)). Switching occurs only when the phase finally runs away rather than being recaptured, and the observed switching-current distribution departs from Kramers accordingly — its second moment rises with temperature in the Kramers regime, then turns over and *narrows* past a crossover ([Phys. Rev. B **71**, 220509](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.71.220509)).

**Why this matters structurally.** A single Arrhenius escape is exceedance-governed and gives the wrong law (§2). But multiple retrapping is not a single escape — it is a **random walk among washboard minima with an absorbing running state**, and the switch is a *first-passage* event. That is the same structure as Theorem 0. The Arrhenius factor sets the step rate, i.e. the overall timescale, which Theorem 4 says the outcome statistics do not depend on; the outcome is decided by first-passage odds, which in a gambler's-ruin problem are linear in the starting position.

This is the first mechanism encountered anywhere in this program in which a real, measured device physics has the *architecture* the framework requires: provisional commitment, reversible recapture, finality only when recapture fails — JB's "drain provisional at Stage 2, final at Stage 3," with instrumented parameters.

**What is not established.** That the first-passage odds map linearly onto the site occupation `e_i`. The retrapping rate depends on the low-frequency damping and the environment's frequency-dependent impedance, not obviously on a per-site energy, and no source found addresses competing sites within one absorption event. The structural match is suggestive; it is not a result. Recorded as the live thread, not as progress on G3.

---

## 8. Proposed status

| Gate | Proposed | Basis |
| --- | --- | --- |
| **G3 — physical selector** | **does not close**; `individual_selection_not_demonstrated` | Exchange current derived and numerically validated; commitment timing settled; exclusivity structural for P4(i). Commitment current absent; quench absent; charge ledger absent. |

What would close it, in order:

1. A commitment current with a source, sink, conservation law, and an irreversibility mechanism that is not merely decoherence (§5).
2. A quench law routing the losing sites' energy back to the field, with its foliation cost stated (§4).
3. The full-quantum threshold stated as an explicit premise, closing the P4(ii) gap (§3).
4. Material authority for `J_ij` in a named detector (Gate A / G4).
5. A charge and information ledger to accompany the energy ledger.

Items 1 and 2 are not modelling gaps. Item 1 is the measurement problem, and no amount of further simulation of the competition stage will produce it.

### Corrections owed to Paper 1 from this pass

- The P5/P6 quarantine claim in §2 is false as stated; beam-splitter anticorrelation consumes P6 in the single-detector sector (§4).
- The full-quantum registration threshold should be promoted to an explicit premise (§3).
- The `min` exchange rule in Appendix D should be identified as a discretization of the geometric-mean kernel, not as the physical law (§1.2).
- "Fairness is a knife-edge" should be stated once as a general claim about instability-driven selection, rather than as three separate refutations (§2).
