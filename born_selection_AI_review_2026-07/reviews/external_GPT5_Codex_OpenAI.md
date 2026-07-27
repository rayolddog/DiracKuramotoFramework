# Referee report: *The Born Rule as a Derived Fair Game: Outcome Selection from Detector Dynamics*

## Standing and limitations

I am GPT-5 Codex (OpenAI, GPT-5), a language model. I can assess internal logic, the mathematical consequences of the stated stochastic model, consistency against standard quantum mechanics and detector theory at a high level, reproducibility, and where claims outrun their stated support. I cannot certify a specialist's complete microscopic QFT calculation or novelty against the entire literature. I weight the report accordingly.

I found no text in the submission directed at a reviewer or language model; the front-page editorial residue is not a prompt-injection finding.

## 1. Recommendation

**Recommendation: reject.**

**Venue note:** The subject is in scope for a foundations/interpretation venue only after radical reworking as a clearly labelled conditional phenomenological proposal. It is not ready as a research article claiming a detector-physics derivation of the Born rule.

**Authorship recommendation: revise the byline and disclosure.** The supplied manuscript names Claude Fable 5 as first author, but the cited public provenance identifies Claude Opus 4.6 and 4.7 as having contributed formalization, derivations, code, literature work, and prose in addition to the human author's physical framing and editorial decisions ([AUTHORSHIP.md](https://github.com/rayolddog/DiracKuramotoFramework/blob/main/AUTHORSHIP.md)). That is material AI contribution, at least co-first-author scale under this journal's policy, rather than a mere acknowledgement. Reconcile the exact materially contributing model/version(s), their roles, and the byline; identify John M. Bramble as the accountable human sponsor. The cited repository's current [CITATION.cff](https://github.com/rayolddog/DiracKuramotoFramework/blob/main/CITATION.cff) lists only Bramble and retains archival/DOI TODOs, so it also needs reconciliation.

## 2. Summary (to fix terms)

The manuscript proposes that an incident quantum deposits real fractional energies at all candidate detector sites in proportion to squared local amplitudes. Independent \(\sqrt{e}\)-scaled detector noise is then claimed to make the energy shares a martingale, so that a registration event has Born weights. The paper extends this construction to multi-quantum and entangled states using a shared registry and preferred foliation, and proposes mismatched collective detector ports as a test for departures from standard quantum mechanics.

## 3. Strengths

- The capture-selection-registration decomposition, P1-P6, and Theorems 0-5 make the intended logical scaffold unusually easy to inspect.
- The Itô calculation is algebraically correct for the narrow, stipulated case of drift-free independent square-root noise.
- The manuscript is commendably explicit that P5 and P6 are nonstandard ontological commitments, and that the entanglement construction does not derive entanglement.
- Table 1 openly records retracted deviation channels rather than concealing them.
- The supplied NumPy scripts are small, readable, and use pinned random seeds. They are useful as illustrative toy calculations even though they do not establish the physical premises.

## 4. Major concerns

1. **The central stochastic process violates the energy conservation that the mechanism requires.**

   **Claim.** Sections 3-5 describe a fixed one-quantum energy redistributed among sites until one site holds it, while Theorem 1 uses \(de_i=\sigma\sqrt{e_i}\,dW_i\) with independent site noises (p. 6).

   **Why it fails or is unsupported.** P2 itself includes unspecified "drift terms" (p. 3), which Theorem 1 drops. For \(de_i=b_i\,dt+\sigma\sqrt{e_i}\,dW_i\), the share drift contains \((b_i-s_i\sum_j b_j)/E\); it is zero only if the omitted drift is specially share-neutral. More decisively,

   \[
   dE=\sigma\sum_i\sqrt{e_i}\,dW_i,\qquad d[E]_t=\sigma^2E\,dt ,
   \]

   so \(E=\sum_i e_i\) fluctuates rather than being pathwise conserved. An energy-conserving exchange requires zero-sum, correlated increments and therefore changes the covariance structure on which the independent-noise proof relies. The claimed "unique fair point" is unique only within the restricted ansatz of diagonal, independent, drift-free Itô diffusion with a one-site coefficient.

   The programs reflect this mismatch. [noise_scaling_born.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/noise_scaling_born.py:19) independently changes every site energy and then divides by the random total to form shares; it is not a conserving exchange. The separate conserving gambler rule is simply stipulated in [gambler_ruin_born3.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/gambler_ruin_born3.py:17).

   **What would fix it.** Start with a specified detector-plus-bath Hamiltonian, derive a conserving constrained stochastic or quantum-stochastic process including damping, noise, and covariance, and re-prove the martingale and termination results for that process. Without this, the central physical mechanism is absent.

2. **P1 reintroduces the squared weight as an ontic stake rather than deriving it.**

   **Claim.** P1 and Section 3 (pp. 3-4) treat \(e_i(0)\propto A_i^2\) as real energy simultaneously held at every candidate site in a single one-photon event.

   **Why it fails or is unsupported.** Driven-oscillator energetics and semiclassical detection support response rates or expectation values; they do not by themselves establish a pathwise c-number allocation of one photon's energy over mutually exclusive absorbers. For a single-photon Fock-state detection event, the detector-field state is a superposition/entangled state, not shown here to be a collection of independently possessed fractional site energies. Interpreting the squared local weight as the initial physical stake installs the quantity whose outcome role is at issue. The notation is also materially wrong for a general complex amplitude: the needed quantity is \(\lvert A_i\rvert^2\), not \(A_i^2\).

   **What would fix it.** Provide an explicit microscopic ontology and Hamiltonian demonstrating how a one-quantum state yields positive, simultaneously real \(e_i\) values without invoking Born-weighted expectation values or a measurement update. Otherwise lower the claim to a conditional re-description.

3. **Theorem 2 and Theorem 5 are not consequences of the stated detector physics.**

   **Claim.** Theorem 2 identifies an off-shell energy deficit with a damping rate, \(\gamma=\Delta E/\hbar\) (p. 7; Appendix B, p. 17), and Theorem 5 claims energy conservation kinematically enforces a rate linear in occupation with corrections of order \((\Gamma/\omega)^2\) (pp. 7-8; Appendix C, p. 17).

   **Why it fails or is unsupported.** Detuning/energy mismatch is not generically a dissipative decay rate; damping is determined by coupling to a bath and its spectral density. A sub-threshold partial energy is not established as a detector eigenstate with the proposed uncertainty-time lifetime. Likewise, vertex counting and energy bookkeeping do not rule out saturation, resonant intermediates, collective modes, non-Markovian response, or nonlinear detector hazards. The very properties that would make the fair point physical are assumed rather than derived.

   **What would fix it.** Derive the detector instrument and the phase/noise dynamics for one concrete atom, semiconductor, or SPAD model, including higher-order and collective channels. Reclassify the present arguments as conjectures until such a derivation exists.

4. **The multi-quantum and Bell sections explicitly insert the Born conditionals and state update.**

   **Claim.** Sections 6.2-6.3 and 7 claim Glauber counting, rho-linearity, Bell correlations, and no-signaling as consequences of the detector mechanism.

   **Why it fails or is unsupported.** Section 6.2 begins from \(m_i=\sum_j\lvert\psi(i,j)\rvert^2\) and then uses \(\lvert\psi(i,j)\rvert^2/m_i\) as the conditional distribution (p. 9). Section 7 supplies the \(\cos^2(a-b)\) conditionals and P5 assumes a registry that renormalizes faithfully with \(\eta=1\) (pp. 10-11). That is the conditional Born/update structure in renamed form.

   The supplied programs make this especially clear: [multiquantum_rho_linearity.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/multiquantum_rho_linearity.py:26) sets P2 equal to the squared modulus of psi before sampling its marginal and rows, while [bell_pair_game.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/bell_pair_game.py:10) hard-codes the quantum \(\cos^2\) conditionals and applies them remotely at [lines 45-55](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/bell_pair_game.py:45). Matching CHSH is therefore a check of a sampler against an inserted quantum distribution, not evidence that the mechanism derives it.

   **What would fix it.** Either derive P5, its exact update, and rho-affinity from dynamics without using conditional Born weights, or label these sections a consistency construction conditional on the projection/update rule. The present no-signaling theorem must likewise be limited to the stipulated subclass, especially because Section 8.5 predicts signaling in another part of the claimed theory.

5. **The proposed tabletop discriminator confuses raw and conditional probabilities.**

   **Claim.** Section 8.4 states that conditional port statistics are exactly affine in the splitter share \(S\) for any local POVM, and treats curvature as a discriminator (p. 13).

   **Why it fails or is unsupported.** With unequal port efficiencies, standard quantum mechanics gives affine raw probabilities but generally nonlinear postselected port fractions:

   \[
   P(A\mid\mathrm{click})=
   \frac{S\eta_A}{S\eta_A+(1-S)\eta_B}.
   \]

   Thus ordinary loss, conditioning, efficiency drift, source-mode changes, or cross-talk can generate the advertised curvature. The supplied port code discards no-result trials before reporting its statistic ([stage2_port_signaling.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/stage2_port_signaling.py:29)). Its advertised fully correlated matched-port control fails: at \(c=1\), equal sites cannot cross the individual 0.7 threshold, and the program returns NaN for the purported fair matched control rather than a fair result ([lines 40-43](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/stage2_port_signaling.py:40)).

   **What would fix it.** Specify a complete instrument/POVM comparison and a pre-registered analysis of unconditioned port, no-click, and coincidence probabilities. Demonstrate with calibrated unequal-efficiency controls that the proposed statistic cannot be an ordinary postselection effect.

6. **The numerical evidence does not establish exact Born statistics and sometimes contradicts the stated controls.**

   **Claim.** Appendix D and the README describe simulations that reproduce Born statistics, verify theorem converses, and support the port prediction.

   **Why it fails or is unsupported.** The optional-stopping theorem requires terminal shares at 0 or 1. Several scripts instead stop when a share reaches 0.7-0.995 and declare the current argmax the winner, for example [gambler_ruin_born3.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/gambler_ruin_born3.py:21), [noise_scaling_born.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/noise_scaling_born.py:24), and [vacuum_correlation_born.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/vacuum_correlation_born.py:70). A martingale fixes \(\mathbb E[s_i(T)]\), not the probability that a site is the argmax at a finite threshold.

   This is observable in the supplied deterministic-seed run: the nominally fair [2,1] case in gambler_ruin_born3.py returns 0.8263 instead of the Born value 0.8000 at the 0.95 threshold. The scripts also clip Euler proposals at zero, condition away no-click trials, provide no convergence study in timestep/threshold/seed, and use an invalid Bernoulli probability for some nonlinear-rate cases: [rate_commit_born.py](/Users/john-bramble/Desktop/ReviewChatGPT/born_selection_sims/rate_commit_born.py:22) permits \(\lambda\,dt\sum_i s_i^\alpha>1\).

   **What would fix it.** Use a mathematically valid implementation of the proposed process, true absorption or an explicitly controlled limiting procedure, unconditional outcome accounting, confidence intervals, and convergence studies. Treat the current code as illustrative diagnostics rather than confirmatory evidence.

7. **The physical input and timescale claims are not adequately supported.**

   **Claim.** Section 6.1 says the game lasts 10-20 ps in a silicon SPAD while relevant losses are negligible; P3 and Sections 7-8 make similarly specific noise fractions, fidelity inferences, and claims about the existing experimental record.

   **Why it fails or is unsupported.** The displayed formula itself gives a wider interval: with \(N=5\times10^{10}\) and \(\Gamma=1.5\times10^{13}-10^{14}\,\mathrm{s}^{-1}\), \(2(\ln N)^2/\Gamma\) is about 12-81 ps, not 10-20 ps across the stated range. The assertion that multiphonon dissipation of a 2.5-eV silicon excitation is blocked is not derived or directly sourced. As a caution, measured single-crystal silicon electron-phonon relaxation in a different ultrafast regime is 0.4-1.2 ps in [Swain et al. (2025)](https://link.aps.org/doi/10.1103/PhysRevResearch.7.023114); this does not alone settle the SPAD case, but it shows why a detector-specific calculation is essential. The manuscript similarly needs direct primary support for \(f\sim10^{-6}\), the eta inference, and "all experiments on record" claims.

   **What would fix it.** Choose a specified device and geometry; provide measured parameters, uncertainty propagation, a detector-specific open-system calculation, and direct citations beside every empirical numerical input and exclusion claim.

8. **The submitted evidence package is incomplete.**

   **Claim.** The front matter calls the manuscript complete and Appendix D says the outputs match every quoted number.

   **Why it fails or is unsupported.** The 20-page PDF has no Figures 2-7 even though the text relies on them, contains two literal Fig. - placeholders, retains Section 8 [to draft], and gives only [repository ref] instead of an immutable source/code archive. The folder provides thirteen scripts, but no raw outputs, source manuscript, script-to-figure generation path, environment lockfile, commit hash, or archival DOI. The README itself refers to missing derivation-session and draft paths.

   **What would fix it.** Supply all figures and captions; release the source, code, environment, inputs, raw outputs, and one-command figure/table pipeline as a tagged, archived DOI-bearing package; and remove every draft placeholder before resubmission.

## 5. Minor / presentational

- Replace \(A_i^2\) by \(\lvert A_i\rvert^2\) consistently and define the amplitudes, site weights, and detector efficiencies precisely.
- Remove the front-page DRAFT/byline-confirmation/editorial notes, Section 8 [to draft], Fig. -, [repository ref], and the final citation's author-order reminder.
- Add the original Glauber photodetection/coherence citation rather than referring to "Glauber counting" without it; see [Glauber (1963)](https://journals.aps.org/pr/abstract/10.1103/PhysRev.130.2529).
- Table 2 (p. 15) is visually cramped, difficult to audit row by row, and gives the paper's own row emphatic styling. Simplify it and cite each comparison.
- Number displayed equations, add a notation table, and add a claim-status table distinguishing premise, mathematical conditional, simulation, empirical input, and open conjecture.
- The PDF typography is otherwise clean, but it is untagged and should be accompanied by accessible source and figure descriptions for a public release.

## 6. Specific questions for the author

1. What exact detector-plus-bath Hamiltonian produces a pathwise energy-conserving selection process with the required drift and covariance?
2. What physical observable is \(e_i\) in a single Fock-state detection event, and how is it distinguished from a Born-weighted expectation value?
3. Can P5's faithful remote registry update be derived without setting the conditional \(\lvert\psi\rvert^2\) weights by hand?
4. Why is \(\gamma=\Delta E/\hbar\) the relevant damping law for the proposed detector, and what measured parameters support it?
5. Can the port test be restated entirely in raw, unconditioned outcome probabilities, including no-clicks and unequal efficiencies?
6. Where are the missing figures, raw outputs, frozen code release, source manuscript, and exact commands that regenerate every quoted result?
7. Which precise AI model versions contributed to this paper, and how should their roles and authorship order be reconciled with the cited project provenance?

## 7. Rubric scores (1-5)

- **Novelty - 2/5.** The detector-side martingale framing and proposed test configuration are potentially distinctive, but the claimed mechanism is not established and the comparative literature analysis does not yet isolate a defensible new result.
- **Internal consistency - 1/5.** The conservation/drift conflict, P1 ontology, and P5/Born-update import undermine the central derivation.
- **Evidential grounding - 1/5.** No microscopic detector model or empirical evidence currently supports the load-bearing premises and numerical hierarchy.
- **Reproducibility - 1/5.** Readable, seeded scripts are a start, but they encode key inputs, use flawed stopping/postselection rules, and are not supplied as a complete archival reproduction package.
- **Citation integrity - 2/5.** A spot check confirms that central cited works such as [Adler et al. (2001)](https://arxiv.org/abs/quant-ph/0107153) and the [Kent (2025)](https://quantum-journal.org/papers/q-2025-05-20-1749/) / [Masanes, Galley, and Müller (2025)](https://quantum-journal.org/papers/q-2025-01-14-1592/) exchange are real. However, the central applications overreach their sources, key empirical inputs lack direct citations, and the cited project provenance is mutable and incomplete.

## 8. Overall assessment (0-5)

**0/5.** The manuscript does not clear the bar for a foundations journal because its central conclusion is assumed through the stochastic law, initial squared-energy allocation, and multipartite update rather than derived from detector dynamics.

## 9. Sign-off

Reviewer: GPT-5 Codex (OpenAI, GPT-5), 2026-07-26
