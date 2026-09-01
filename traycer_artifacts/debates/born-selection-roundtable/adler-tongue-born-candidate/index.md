---
title: "Candidate calculation: Adler locking flux and the Born square"
kind: spec
---

# Candidate calculation: Adler locking flux and the Born square

## Status and verdict

**Status:** promising candidate; not a Born-rule derivation and not approved manuscript text.

The published Adler, Lohe, and quantum-synchronization calculations do **not** derive Born outcome frequencies. A new inference is nevertheless worth testing:

<user_quoted_section>For a broad, approximately flat population of candidate absorber detunings, the number of clocks eligible to lock is proportional to the wave-amplitude coupling, and their characteristic locking speed is also proportional to that coupling. Summing the variable locking speed across the Arnold tongue therefore produces a total locking flux proportional to the coupling squared.</user_quoted_section>

If the coupling to outcome channel `k` is linear in the magnitude of that channel's wave amplitude, this total flux has the quadratic dependence required by the Born rule—without first invoking Fermi's golden rule.

The unresolved step is whether this rate-weighted tongue integral is physically the **commitment hazard** of a detector channel rather than merely a measure of its synchronization response.

## Which calculation John may have remembered

| Name | What it actually calculates | Born-selection relevance |
| --- | --- | --- |
| **Adler** | Phase locking of a driven self-sustained oscillator; tongue boundary, locked phase, slip time, and relaxation toward the locked phase | Supplies the variable locking time needed for the new candidate calculation |
| **Lohe / Schrödinger–Lohe** | Deterministic nonlinear synchronization of quantum-state nodes; sufficiently strong coupling aligns their states | Does not produce random outcomes or Born frequencies |
| **Mari et al.** | Measures of complete and phase synchronization based on quantum variances and correlations | Measures degree of synchronization, not probability of choosing an outcome |
| **Walter–Nunnenkamp–Bruder** | Driven quantum van der Pol oscillator; Wigner phase distribution, power spectrum, and weak-to-strong entrainment crossover | Shows synchronization is graded inside a quantum tongue, but uses a standard Lindblad master equation and derives no new outcome law |
| **Goychuk et al.** | Noise-assisted synchronization of a driven spin-boson tunnelling system | Studies residence/transition timing under standard open quantum dynamics, not a Born-free first outcome |

## The new calculation in plain English

Consider one possible detector outcome channel with effective coupling `K`.

1. Only absorber clocks whose natural frequencies lie within `K` of the drive can lock. The tongue therefore includes a detuning interval of total width `2K`.
2. The locking speed is not constant inside that interval. It is maximal at the tongue's center and decreases as a semicircle, reaching zero at both edges.
3. If candidate absorber detunings are nearly uniformly distributed across the narrow tongue, sum the locking speed of all eligible clocks.
4. The width of the eligible population supplies one factor of `K`.
5. The characteristic locking speed supplies a second factor of `K`.
6. The integrated locking flux is therefore proportional to `K` squared.

For the ideal Adler equation, the local relaxation rate at detuning `d` is the square root of `K` squared minus `d` squared. Its graph across the tongue is a semicircle. The exact area under that semicircle is `pi/2` times `K` squared.

Numerical integration verified the constant ratio for couplings from 0.1 through 5:

| Coupling `K` | Integrated locking flux | Flux divided by `K` squared |
| --- | --- | --- |
| 0.10 | 0.0157079634 | 1.57079634 |
| 0.50 | 0.392699086 | 1.57079634 |
| 1.00 | 1.57079634 | 1.57079634 |
| 2.00 | 6.28318537 | 1.57079634 |
| 5.00 | 39.2699086 | 1.57079634 |

The constant is irrelevant when competing channel rates are normalized; the quadratic scaling is the important result.

## Why the time-scaling is more general than one formula

Inside the simple Adler tongue, measure detuning as a fraction of the coupling. After that rescaling, a locking time has the form:

<user_quoted_section>one divided by K, multiplied by a dimensionless function of fractional detuning, initial phase, and the chosen lock tolerance.</user_quoted_section>

Consequently, any consistently defined inverse locking time contributes one factor of `K`, while the detuning interval contributes the other. The quadratic scaling is therefore not limited to using the small-error relaxation rate, provided:

- the lock criterion is dimensionless and common to all channels;
- the initial phase distribution is common to all channels;
- no additional channel-dependent timescale is introduced; and
- the detuning density is locally flat.

## Possible Born mapping

For outcome channel `k`:

1. classical field coupling is linear in the magnitude of the local complex amplitude;
2. the integrated Adler locking flux is quadratic in that coupling;
3. therefore the candidate commitment flux is quadratic in the amplitude;
4. if several channel fluxes form a genuine first-commitment race, the chance that channel `k` commits first is its flux divided by the total flux; and
5. normalized channel amplitudes then yield the Born weights.

This replaces the earlier note's load-bearing “golden-rule rate is coupling squared” step with a synchronization calculation. It does **not** yet derive steps 1, 3, or 4 microscopically.

## Where exactness fails

The quadratic result is exact only for an effectively flat detuning density across the tongue. A Gaussian test shows how spectral curvature changes the flux:

| Tongue half-width divided by spectral width | Change from the flat-spectrum quadratic result |
| --- | --- |
| 0.02 | −0.005% |
| 0.05 | −0.031% |
| 0.10 | −0.125% |
| 0.25 | −0.775% |
| 0.50 | −3.03% |
| 1.00 | −11.09% |
| 2.00 | −32.63% |

This creates both a problem and a possible prediction:

- **Problem:** Born frequencies are extremely robust across detector materials, so the relevant microscopic spectral density must be flat over the locking range or a deeper sum rule must remove the material dependence.
- **Possible prediction:** deliberately structured absorber spectra could produce a calibrated deviation if this synchronization flux really sets selection statistics.

## Load-bearing assumptions and failure modes

| Required step | Why it is not yet established | What would falsify or repair it |
| --- | --- | --- |
| Coupling is linear in outcome amplitude | Plausible for a field driving a dipole, but the detector-specific `K` must be derived | Microscopic field–absorber reduction |
| Candidate detunings are locally flat | Real solids have structured bands, disorder, and depth-dependent fields | Calculate the dressed spectral density for one detector |
| Locking speed is a commitment hazard | Relaxation toward phase lock is not automatically an irreversible detector event | Derive a current through a commitment surface from the open-system generator |
| Channel fluxes race independently | Common fields and baths can correlate them | Two-channel common-bath model |
| First lock excludes all rivals | Adler locking alone does not conserve and reroute one photon excitation globally | Explicit finite-time energy/norm routing or a passive-registry law |
| Noise measure is Born-free | Lindblad quantum jumps and standard trajectory unravelings already use Born weights | Derive the stochastic forcing without outcome conditioning |
| Flat-density result is basis covariant | A preferred absorber basis can make the rule context-dependent | Repeat for rotated polarization bases and general detector POVMs |

## Important negative results

- **Tongue width alone is wrong:** it is linear in amplitude, not quadratic.
- **Deterministic fastest-lock wins is wrong:** it would make the strongest channel win almost every run rather than with a Born frequency.
- **Literal basin depth is wrong:** noisy escape rates often depend exponentially on barrier depth, not quadratically on amplitude.
- **Lohe synchronization alone is insufficient:** it aligns quantum states deterministically and supplies no first actual outcome.
- **Published quantum synchronization alone is insufficient:** its phase distributions and trajectory probabilities already use standard quantum expectation or unraveling rules.

## Smallest decisive calculation

Detailed technical plan: [Two-channel stochastic Adler test](two-channel-stochastic-model).

Build a two-channel absorber model with couplings set by two input amplitudes and a shared, explicitly represented bath:

1. derive the two Adler reductions rather than postulating them;
2. derive the distribution of absorber detunings and initial phases;
3. define a microscopic commitment surface distinct from ordinary phase alignment;
4. compute the unconditional probability current into each commitment channel;
5. test whether the currents follow the rate-weighted tongue integral;
6. enforce a global one-excitation ledger and measure double commitment;
7. rotate the input polarization and test whether the ratio reproduces Malus' law;
8. repeat for flat, Gaussian, Lorentzian, and structured spectra; and
9. keep standard Born-conditioned quantum trajectories only as labeled controls.

The calculation succeeds as a Born candidate only if the quadratic channel-current ratio emerges from the unconditional generator and survives basis rotation without inserting squared amplitudes into a stochastic jump law.

## Relation to the existing framework note

The earlier [Synchronization, Arnold Tongue, and Born Rule note](/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/drafts/NOTE_sync_tongue_born_walkthrough.md:443) correctly separated tongue eligibility from outcome weight. It then supplied the square through a golden-rule capture rate. The Sol–Fable review identified that move as Born-adjacent and potentially circular.

The present candidate retains the note's separation but asks whether the **rate-weighted interior of the tongue itself** supplies the square. This is a sharper, independently testable proposal.

## Primary references checked

- R. Adler, “A Study of Locking Phenomena in Oscillators,” *Proceedings of the IRE* **34** (1946), 351–357. DOI: `10.1109/JRPROC.1946.229930`.
- M. A. Lohe, “Quantum synchronization over quantum networks,” *Journal of Physics A* **43** (2010), 465301. [Publisher record](https://doi.org/10.1088/1751-8113/43/46/465301).
- A. Mari et al., “Measures of Quantum Synchronization in Continuous Variable Systems,” *Physical Review Letters* **111** (2013), 103605. [APS full text](https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.111.103605/fulltext).
- S. Walter, A. Nunnenkamp, and C. Bruder, “Quantum Synchronization of a Driven Self-Sustained Oscillator,” *Physical Review Letters* **112** (2014), 094102. [APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.112.094102).
- I. Goychuk et al., “Quantum Stochastic Synchronization,” *Physical Review Letters* **97** (2006), 210601. [APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.97.210601).
- L. Zhang et al., “Quantum synchronization of a single trapped-ion qubit,” *Physical Review Research* **5** (2023), 033209. [Open-access article](https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.5.033209).
