---
title: "Independent pressure-test — quantum-equilibrium selection revision"
kind: review
---

# Independent pressure-test — quantum-equilibrium selection revision

## Final verdict

The revision makes the necessary high-level concession: **quantum equilibrium is an input, not a Dirac–Kuramoto derivation**. That is a substantial correction. It does not yet make the program non-circular, physically specified, or ready for manuscript revision.

The central unresolved problem is now precise. `mu_eq(d lambda | Psi)` is not defined on a chosen ontology, and `F_DK` is a placeholder for the very one-event actuality law the paper needs to supply. Until both are independently fixed, the pushforward equation can be satisfied by construction: the Born rule can enter through the state-dependent microstate law, the coupling and phase preparation, the stopping/commit rule, postselection, or the analyst's choice of test family. Conversely, a program that explicitly assumes a standard quantum-equilibrium law may legitimately test **conditional outcome compatibility**, but it cannot call that result equilibrium preservation in the dynamical sense or a Born derivation.

The genuinely open explanatory opportunity is one-event actuality: how a distributed field–matter state produces one irreversible material record. Dirac–Kuramoto dynamics would fill that gap only if it supplies a physically derived, pathwise exclusivity and registration law. A simulation function that returns one label, a first-threshold stop, a stochastic draw, or a registry beable initialized as already actual merely relocates the selection postulate.

### Separate dispositions

| Object | Strict verdict | Maximum claim now |
| --- | --- | --- |
| **Claim architecture** | **Revision required before use.** The measure/selector split is sound, but Q0 conflates a quantum outcome measure with a microstate measure and Q2 misnames a cross-space pushforward as “preservation.” | “We propose a conditional microstate-to-record program and state its unresolved contracts.” |
| **Bounded diagnostic implementation** | **Go only as a nonphysical-fixture diagnostic after the gates below are written.** Existing Adler code may remain a synchronization/stopping-rule test; it is not an outcome model. | `individual_selection_demonstrated_nonphysical_fixture` or `individual_selection_not_demonstrated`. |
| **Equilibrium-preservation evidence** | **Not testable as presently specified.** No unique `mu_eq`, preparation kernel, or equivariant dynamics exists. | After repair: conditional outcome-law compatibility for a frozen ensemble and selector, not equilibrium explanation. |
| **Individual-selection mechanism** | **Not demonstrated.** `F_DK` names the missing mechanism; it does not supply it. | Candidate mechanism only after a microscopic reduction, unique record, and closed ledger are pathwise demonstrated. |
| **Full Born derivation** | **Refused.** The Born/equilibrium measure is explicitly assumed, and no Q4 theorem exists. | None. A later independent typicality, uniqueness, equivariance, or relaxation result would be required. |

## Findings in priority order

### 1. Critical — `mu_eq` can still contain the answer because no microstate probability space is defined

The plan declares `mu_eq(d lambda | Psi)` and then asks whether its pushforward equals the Born outcome law ([revision, central statement](..#central-mathematical-statement)). The later “equilibrium contract” offers configuration, phase, thermal/material, or joint equilibrium as alternatives rather than selecting one ([revision, equilibrium contract](..#equilibrium-contract)). These are not interchangeable:

- Gleason-type structural results constrain outcome measures on quantum effects; they do not provide a probability law over complete detector, bath, phase, noise-path, or registry beables.
- Bohm-like configuration equilibrium is meaningful only after the configuration ontology and guidance/current law are fixed.
- Haar-uniform phases provide an invariant phase measure, not a joint Born measure over detector and field microstates.
- A thermal ready-state law is a detector preparation law, not a state-dependent law for system beables.

As written, a different conditional `mu_eq(. | Psi)` can be chosen for every `Psi`, or its correlations can be chosen after `F_DK` is known, so that the desired outcome partitions receive the desired masses. The firewall forbids explicit fitting but does not make this construction impossible or auditable.

**Required bounded repair before either prose or code:** define one probability space `(Lambda, Sigma)`, the ontic status of every component of `lambda`, and one normalized joint law with provenance. At minimum write a preparation factorization or kernel such as

```text
mu_eq(dlambda | Psi, M)
  = mu_sys(dlambda_sys | Psi)
    nu_ready(dlambda_det, dlambda_bath, dnoise | M, preparation_history)
```

plus every justified correlation term. State which factor, if any, is `Psi`-dependent; prove or cite that dependence without using `F_DK`, `Pi_a`, or outcome data; and freeze the law before defining test-state partitions. If such a law cannot be supplied, use `equilibrium_contract_undefined` and stop before outcome simulation.

### 2. Critical — the plan calls a pushforward “equilibrium preservation,” but the two measures live on different spaces

`F_DK# mu_eq` is an outcome measure, while `mu_eq` is a microstate measure. Equality of the former to `<Psi|Pi_a|Psi>` is **outcome compatibility**, not preservation of `mu_eq`. Preservation/equivariance would require a microstate flow `T_t` and a statement such as `(T_t)# mu_eq,Psi = mu_eq,Psi_t`, with its domain, conditioning, and dynamics specified.

This terminology matters because a one-time outcome fit can pass even when the microstate distribution is not invariant, not physically preparable, or silently reset between events. The plan itself correctly warns that repeated observations do not cause relaxation, but Q2 and the thesis still overstate what the proposed test establishes.

**Required repair:** rename Q2 to **equilibrium-conditioned outcome compatibility** (or “equilibrium pushforward agreement”). Reserve **preservation/equivariance** for a same-space dynamical theorem and keep relaxation as a separate Q4-class claim.

### 3. Critical — `F_DK` may simply encode the missing actuality postulate

The map notation (`a = F_DK(Psi, lambda)`) guarantees a single returned label syntactically. It does not show that physical evolution produces one actual record. The plan lists “any actual configuration or registry beable” among the state variables, but this creates a fork that must be resolved:

- If the registry/configuration is already single-valued and actual, its ontology and guidance/update law—not Kuramoto locking alone—does the actuality work.
- If the global state remains strictly unitary, field–matter evolution yields entangled record branches; decoherence and phase locking do not by themselves select one branch as actual.
- If `F_DK` is stochastic, the primitive stochastic law does the selection unless its noise source and coupling to a physical commitment current are independently derived.
- If “first threshold crossed” or “first dwell completed” stops the simulation, exclusivity is an imposed event rule unless the competing physical channels are actually quenched and their energy/norm is routed by the equations.

This reproduces the historical synthesis: ontic stakes, winner gating, finite registry flow, and the specific Dirac role remain “derive before claiming” ([historical synthesis](../../final-synthesis#claim-disposition)). The current candidate ledger also says a local registry does not solve the first-mark problem ([candidate ledger](../../author-ai-update-candidates#comparison-with-the-multi-model-recommendations)).

**Required repair:** choose and name the ontology. Then provide either:

1. deterministic equations for field, matter, bath, and actual registry variables, including pathwise uniqueness and exclusivity; or
2. a stochastic transition kernel with an independently specified physical noise law and a commitment current, explicitly admitting stochasticity as primitive where it is primitive.

For a genuinely stochastic selector, replace the deterministic pushforward formula by

```text
P_DK(a | Psi) = integral K_DK(a | Psi, lambda) mu_eq(dlambda | Psi).
```

Alternatively include the entire noise history in `lambda` and state that `F_DK` is deterministic conditional on it. Do not switch between the two descriptions.

### 4. High — the anti-circularity firewall lacks an auditable dependency contract

The forbidden-input list is good but prose-only. The same Born dependence can re-enter under physically respectable names:

- `mu_eq(. | Psi)` or a `Psi`-conditioned detector ready state;
- initial relative-phase, detuning, or bath correlations;
- a channel coupling proportional to a target amplitude without a detector Hamiltonian deriving that dependence;
- a lock tolerance, dwell time, hazard, exposure window, no-click cutoff, or invalid-trajectory rule chosen because it yields exponent one or two;
- site density or active-volume selection that changes with the test state;
- conditioning winner frequencies on “valid clicks” when the invalid/no-click probability is state- or outcome-dependent;
- model selection, test-state selection, or error-budget widening after comparator access.

Calling `|Psi|^2` a bilinear current, energy density, or absorbed work does not by itself make its use non-circular. Standard quantum theory's local quadratic quantities may be expectations or transition weights rather than simultaneously possessed event-level energy shares; the active manuscript itself concedes this at [lines 21–23](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:21) while still installing `e_i(0) proportional to |A_i|^2` as P1 at [lines 41–49](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:41).

**Required repair:** add a machine-checkable dependency manifest for every raw-model input. Each entry must state source, units, calibration data, allowed state dependence, uncertainty, and whether it was fixed before comparator access. Hash the raw configuration and executable; keep the comparator in a separate read-only analysis package; include zero/no-click/double/invalid events in the primary multinomial outcome rather than silently conditioning them away; and make any post-freeze change start a new preregistered model version.

### 5. High — the proposed tests do not yet distinguish conditional compatibility from target-fitting

“Freeze, then choose holdout states” is insufficient ([revision, Phase II](..#phase-ii--equilibrium-pushforward)). The model family, parameterization, preparation law, and informal physical judgments can all have been selected with full knowledge of the Born target. A few weights, phases, and bases then test interpolation, not an independently risky prediction. “Structured nonequilibrium departures or justified robustness” is also too permissive: either result can be narrated as success after the fact.

**Required bounded test contract:**

1. Calibrate material parameters only on non-outcome observables: spectra, linewidths, response functions, bath correlations, carrier/trap kinetics, and amplifier thresholds.
2. Seal code, parameters, `mu_eq`, invalid-event handling, state generator, sample size, equivalence margin, and failure thresholds before outcome runs.
3. Generate a large blinded/adversarial holdout suite after the seal from a preregistered seed or independent generator, including arbitrary states, bases, dimensions, near-zero channels, detector permutations, and physically equivalent representations.
4. Require one shared detector-ready distribution and one parameter set across all permitted input states and bases.
5. Use an equivalence test against a predeclared physical/numerical tolerance, not failure to reject a difference.
6. Predeclare nonequilibrium perturbation families and quantitative predicted response surfaces. “Structured” is not a pass condition.
7. Include mechanistic negative controls that preserve the target curve while breaking the claimed DK layer, and controls that preserve DK synchronization while changing the commitment law. If both give the same result, the claimed mechanism is not identified.
8. Repeat across detector substitutions using only independently measured material parameters. Cross-material retuning is failure, not calibration.

Passing this contract would support conditional outcome compatibility of one frozen model. It would not establish the unique truth of the mechanism; observationally equivalent hidden-variable or stochastic maps may produce the same pushforward.

### 6. High — Dirac–Kuramoto is not yet shown to be load-bearing

The revised title and thesis foreground “Dirac–Kuramoto,” but the plan presently supplies no microscopic equation showing that specifically Dirac spinor structure and a synchronization reduction cause commitment.

- **Dirac:** Massive spin-1/2 detector electrons may ultimately be described relativistically, but ordinary optical detector microphysics is usually governed by QED reduced to material-specific band, exciton, carrier, and bath Hamiltonians. Merely beginning from Dirac/QED and then reducing to a generic phase model does not make Dirac structure explanatory. Identify a spinor bilinear, phase, current, or symmetry whose removal changes the selection prediction.
- **Photons:** The photon is spin 1. A Riemann–Silberstein/first-order Maxwell representation is a representation of Maxwell dynamics, not a spin-1/2 Dirac ontology or a new selection mechanism. The existing bridge states this correctly ([photon bridge](../../photon-dirac-and-absorption-bridge#citation-finding)). Photon representation should be secondary in Paper 1 unless it changes the material commitment law.
- **Kuramoto/Adler:** Adler phase reduction presupposes an autonomous, maintained oscillator with a free-running phase. The material audit found no such powered oscillator in sensitized silver halide; the supported chain is passive excitation, transfer, trapping, cluster growth, and development ([material audit](../../born-free-adler-silver-halide-plan/material-oscillator-evidence#verdict)). A passive driven resonance, transient coherence, Rabi exchange, or phase lag is not an Arnold-tongue oscillator.
- **Commitment:** The rate-weighted tongue calculation proves only an integral proportional to `K^2` under a flat detuning density. Its own record says the missing step is whether relaxation flux is a physical commitment hazard ([candidate calculation](../../adler-tongue-born-candidate#load-bearing-assumptions-and-failure-modes)). Synchronization does not by itself create irreversibility, global exclusivity, or energy routing.
- **Quaternions:** Quaternionic notation is an optional representation of `SU(2)`/spinor rotations. Representation invariance is a necessary check, but quaternions supply neither probability nor actuality.

**Required repair:** use neutral labels—“field–matter selector” and “phenomenological phase-reduction fixture”—until a material Hamiltonian yields the phase degree of freedom, the reduction, its validity range, and a commitment current. Keep the silver-halide Adler branch counterfactual unless new evidence supplies a pump, free-running phase, and injection-locking behavior. For passive materials, begin from the documented dissipative polarization/charge-transfer/trapping model.

### 7. High — several detector claims in the active manuscript are hypotheses, not established premises

The current draft conflicts directly with the revision and cannot be lightly patched:

- The title and abstract claim a “derived fair game” and that the mechanism operates within ordinary quantum dynamics ([manuscript lines 1–9](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:1)).
- It claims fairness is derived and the Born weight is nowhere inserted by hand ([lines 19–21](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:19)).
- It says the measurement postulate is redundant and definite outcomes, Born weights, Glauber statistics, and Bell correlations follow ([line 29](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:29)).
- P0 treats simultaneously present site energies as ontic; P1 sets them proportional to the quadratic wave amplitude; P2 installs the square-root noise; P3 calls phase incoherence and dominant local noise standard working-detector facts; P4 claims a comprehensive registration taxonomy ([premises, lines 35–61](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:35)). These are precisely the load-bearing model assumptions still awaiting the microscopic derivation.
- `kappa_ret = Delta E / hbar` is admitted to be an ansatz but is used as a contraction rate and to support threshold claims ([lines 131–141](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:131)). An energy deficit divided by `hbar` is a frequency scale, not by itself a decay/return rate or pole of an open-system generator.
- The manuscript's SPAD timescale, loss, “virtual stake,” full-quantum boundary, and kinematic-hazard claims ([lines 181–192](~/Projects/Physics/DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md:181)) require a detector-specific open-system derivation. SPAD amplification is powered mainly by the bias supply and must remain downstream of absorption/commit unless backaction is calculated ([photon bridge, energy ledger](../../photon-dirac-and-absorption-bridge#correct-spad-energy-ledger)).
- Multi-quantum conditional reset, Bell registry update, and above-Tsirelson predictions are consistency constructions with imported conditional weights, not evidence for the single-event selector; the historical synthesis already directs them out of the proof.

**Required repair before manuscript revision starts:** treat the existing file as a historical draft, not a text to patch section by section. Prepare a new scoped draft whose abstract leads with the imported equilibrium premise; restrict the main result to one quantum/one event; move multi-quantum, Bell, above-Tsirelson, and production experiments to clearly labeled future-work history; and label every material claim `standard`, `derived-here`, `phenomenological`, or `open`.

### 8. Medium — the existing Adler implementation is well quarantined but cannot be promoted

The current code's own contracts are appropriately strict:

- a first clock is not an outcome or unique actuality ([README lines 27–35](~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md:27));
- “commitment” is only a dwell rule ([README lines 41–52](~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md:41));
- the moving-band audit and production numerical budget are a `numerical_no_result` ([README lines 54–70](~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md:54));
- every scaling verdict is `machinery_only` ([README lines 72–87](~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md:72)); and
- the package lacks a photon field, absorber levels, amplification, bias supply, losing-amplitude routing, and derived exclusivity ([README lines 123–131](~/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md:123)).

That is the correct disposition. The revision should cite this package only as a numerical/phase-dynamics fixture. Do not rename its dwell event into microscopic commitment or use an exponent near two as equilibrium, selection, or detector evidence. Any new implementation should inherit these non-claim gates and add an immutable `physical_authority = fixture | reduced_model | material_derived` field.

### 9. Medium — the result vocabulary needs failure states for the newly exposed contracts

The current vocabulary omits the most likely outcomes: undefined equilibrium, conditional compatibility without preservation, selector-by-stipulation, and physically unjustified reduction. Without those states, pressure can accumulate to choose a more favorable existing label.

**Add exactly these dispositions:**

- `equilibrium_contract_undefined`
- `equilibrium_pushforward_compatible_conditionally`
- `equivariance_not_demonstrated`
- `individual_selection_reimplemented_by_event_rule`
- `physical_reduction_not_demonstrated`
- `material_authority_refused`

Retain the ban on `born_rule_derived` unless Q4 is independently closed.

## Exact go/no-go gates

### Before any manuscript revision

1. Select the ontology and one `mu_eq` contract; do not present a menu.
2. Rename Q2 and every “preservation” claim to conditional pushforward compatibility unless an equivariance theorem is actually supplied.
3. Decide whether the event law is deterministic conditional on a complete noise history or stochastic via a kernel.
4. State what is physically actual before, during, and after commitment and what equation prevents a second record.
5. Downgrade Dirac, Adler/Kuramoto, silver-halide, SPAD, and quaternion claims to the warranted levels above.
6. Freeze Paper 1 to the one-quantum/one-record question; keep broader statistics as historical consistency material.
7. Replace the active draft's title, abstract, and theorem-level claims wholesale; do not preserve “measurement postulate redundant,” “derived fairness,” or “nowhere inserted by hand.”

### Before any outcome-producing implementation

1. Write the dependency manifest and comparator-isolation boundary.
2. Supply the joint preparation sampler and demonstrate normalization, reproducibility, and state-dependence rules without outcome access.
3. Supply the physical or fixture status of every coupling, phase, detuning, noise, threshold, dwell, hazard, exposure, and invalid-event rule.
4. Implement the full outcome alphabet, including no record, multiple record, invalid trajectory, and ledger failure, with no postselection.
5. Seal the blinded holdout generator, equivalence margins, nonequilibrium response predictions, and detector-substitution rule.
6. Demonstrate numerical convergence before any physics comparison. The current moving-band `numerical_no_result` must remain a stop, not a tunable tolerance.
7. Permit a paper-level `equilibrium_pushforward_compatible_conditionally` result only if the model has material authority above `fixture` and passes all gates without retuning.

## What survives this review

- The measure/individual-event split is the right conceptual correction.
- The anti-circularity intent, raw/comparator separation, invalid-event ledger, representation checks, and nonequilibrium challenge are worth retaining.
- The one-event actuality/physical-registration question is a real explanatory target not discharged by a structural Born argument or decoherence alone.
- The martingale and Adler calculations remain useful controls and effective-model diagnostics.
- None of those surviving elements presently demonstrates a physical selector, equilibrium preservation, or a Born derivation.

**Overall status:** **promising but under-specified research program; claim architecture requires repair; bounded fixture work may continue; manuscript revision and physical interpretation remain blocked.**
