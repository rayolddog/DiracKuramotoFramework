---
title: "Round 2 synthesis — what changed through collaboration"
kind: spec
---

# Round 2 synthesis — what changed through collaboration

The four reviewers converged far enough that another debate round is unlikely to alter the principal conclusions. No model was ranked, and the manuscript was not edited.

## Current best answer

The manuscript contains a sound and useful mathematical core, but not yet a complete physical derivation of the Born rule. The defensible core is a **conditional single-quantum theorem**:

<user_quoted_section>If physically real, nonnegative site stakes sum to one quantum; their normalized shares are conserving martingales; and registration has a passive linear first-event hazard, then the probability that site i registers first equals its initial share.</user_quoted_section>

This result does not require wave-function collapse or many-world branching. Its unresolved burden is physical: the paper must derive the stakes, conserving exchange, registration hazard, and winner routing from an absorber–field model without importing the Born rule.

## Conclusions changed by the cross-review

| Concept | Independent-round position | Position after direct exchange | Why it changed |
| --- | --- | --- | --- |
| **LC-1 — conserving game** | The stated independent square-root noise fails because total energy fluctuates and dies. | A canonical mathematical repair exists: neutral antisymmetric Wright–Fisher exchange conserves the total and gives Born-weighted fixation. The paper's square-root uniqueness claim does not survive. | The correction agents supplied an explicit conserving covariance; the critical agents verified the fixation logic and exposed the separate dropout premise. |
| **LC-3 — return dynamics** | The reversible-return story appeared inconsistent with a contracting equation; the κ_ret ansatz looked dispensable. | The claim is conditionally preservable: κ_ret may set a timescale rather than the weights, but passivity alone does not prove unbiased exchange. | Both sides agreed that phase memory, collective modes, or correlations may produce drift, so a microscopic drift bound is still required. |
| **LC-4 — registration** | Golden-rule rates risked importing the Born rule; the repair was uncertain. | A narrower, Born-independent route is plausible for one quantum if the stake is genuinely ontic and the detector has a linear classical escape/absorption hazard. Exclusivity has a finite drain-time correction. | Reviewers separated the first-event probability from the later physical routing of the remaining energy. |
| **LC-6 — experiment** | Port-efficiency mismatch could mimic the proposed curvature. | Port swapping alone is insufficient. The leading test is now in-situ modulation with a modulation-odd signal and simultaneous ordinary-POVM tomography. | The desired effect and an efficiency mismatch can follow the same physical port and have the same leading functional form. |
| **LC-7 — role of Dirac spinors** | Paper 1 seemed deficient because its detector game was not explicitly spinorial. | This criticism was narrowed. The framework's companion analysis already assigns ordinary electromagnetic pointer selection to charge/which-path coupling; the chiral mass register supplies ontology, clock structure, and a closed-system no-go rather than the ordinary pointer. | Both critical reviewers changed their view after checking the framework's electromagnetic coupling analysis. A spinor-specific positive effect should instead be sought in scalar/Yukawa, gravitational, or controlled massless-limit tests. |

## Agreements that did not change

- **LC-2 remains load-bearing.** A spatially spread one-quantum wave does not automatically establish definite classical fractional energies at detector sites. The stake variable needs an operational definition or microscopic derivation.
- **LC-5 remains a consistency embedding.** An exact conditional registry reset reproduces standard entangled statistics, but it does not derive the update and may be operationally indistinguishable from collapse until a finite dynamical flow is specified.
- **Multi-quantum claims remain conditional.** Glauber correlations, joint commit laws, and affine density-matrix extensions require a Born-independent joint-stake dynamics.
- **The author's ontology was not disproved.** The review found derivational gaps, not a proof against a real evolving wave, a single world, or a spinor-centered foundation.

## The two detector classes

The discussion showed that one repair cannot do every job.

1. **Discrete absorbers:** conserving Wright–Fisher fixation can model winner selection, but an irreversible `dropout at zero` rule is an additional physical premise. Ordinary hopping can otherwise repopulate an empty site.
2. **Continuum detectors:** a linear first-event hazard can give exact winner weights without waiting for boundary fixation. Exactly-one-click and exactly-one-quantum delivery additionally require rapid winner gating and routing; the expected correction scales as `O(Λ τ_drain)`.

## Keystone calculation

All four reviewers converged on the same next theoretical calculation:

1. Start with two localized detector sites, a common field mode, a bath, and the relevant Dirac matter current.
2. Project onto localized charge/current modes and integrate out the common mode and bath without using outcome-conditioned quantum jumps.
3. Derive the effective share drift, covariance, memory, conservation law, and boundary behavior.
4. Test whether the neutral conserving martingale kernel emerges, whether empty sites can be repopulated, and whether phase correlations bias the time-integrated transfer.
5. Compare the massive and massless limits and a non-spinorial control; then extend to three sites and two quanta.

This one calculation addresses LC-1, LC-3, the domain of LC-4, and the Dirac separation in LC-7.

## Agreed evidence ladder

1. Analytic proof for the effective conserving generator and first-event/fixation probabilities.
2. Direct stochastic simulation as a check of the effective model, not as its microscopic derivation.
3. Influence-functional, Keldysh, or stochastic-Hamiltonian reduction without outcome-conditioned jumps; a trajectory unraveling alone is insufficient because its probability rule may already contain the Born postulate.
4. Detector experiments only after the kernel and nuisance-parameter budget are fixed.

## Recorded participant discussions

- [Claude critical cross-review](../claude-critical)
- [Claude correction cross-review](../claude-corrections)
- [GPT critical cross-review](../gpt-critical)
- [GPT correction cross-review](../gpt-corrections)
