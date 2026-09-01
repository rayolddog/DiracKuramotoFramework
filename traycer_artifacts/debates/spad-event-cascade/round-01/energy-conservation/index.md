---
title: "Energy and conservation audit — SPAD event cascade"
kind: spec
---

# Energy and conservation audit — SPAD event cascade

## Protected concern

The enlarged system must keep a closed ledger across the incident electromagnetic field, detector electronic modes, lattice/phonons, radiative field, junction field and bias supply, quench/readout circuit, and all outgoing fields. No amplitude, norm, or energy may disappear at “selection,” “threshold,” or into an unnamed “vacuum.”

The most important distinction is:

<user_quoted_section>A local energy expectation, such as $\langle H_i\rangle=|\beta_i|^2\hbar\omega$, is not evidence that site $i$ ontically possesses the classical fraction $|\beta_i|^2\hbar\omega$ in that event.</user_quoted_section>

For a one-excitation state, a local excitation-number measurement has eigenvalues zero or one. The fractional number is an ensemble/state expectation. The Born Selection proposal may posit physically real fractional stakes, but that is an additional ontology requiring its own microscopic variables and conservation law; it cannot be inferred from the standard distributed absorption amplitudes.

## Stage-by-stage ledger

| Stage | State change and photon status | Energy source → named receivers | Conservation / reversibility |
| --- | --- | --- | --- |
| **0. Arrival and optical scattering** | $ | 1_f,G\\rangle\\to r | 1_{f_r},G\\rangle+t |
| **1. Coherent capture build-up** | $ | 1_f,G,B_0\\rangle\\to \\alpha | 1_f,G,B_0\\rangle+\\sum_i\\beta_i |
| **2. Localization / proposed selection** | Standard unitary dynamics leaves the channel sum $\\sum_i\\beta_i | E_i,B_i\\rangle$; decoherence suppresses interference between records but does not delete the losing amplitudes. A one-world single-site commit therefore needs an additional finite dynamical law. | Ideally no new macroscopic energy source. Any transfer among candidate channels must obey $dE_{\\rm EM}+dE_{\\rm el}+dE_{\\rm ph}+dE_{\\rm rad}=0$. Vacuum fluctuations may perturb rates, but the stationary vacuum is not a net energy reservoir. |
| **3. Carrier thermalization and collection** | A localized electron–hole pair cools and drifts toward the multiplication region; collection may fail. | Photon excess energy and field-supplied drift energy → phonons. If the pair recombines: roughly $E_g$ → phonons (dominant nonradiative route) and/or a real luminescence photon in an outgoing radiative mode. | Dissipative and normally irreversible, but still recordless. An absorbed-but-untriggered photon has a complete no-click ledger: its energy becomes lattice heat and/or outgoing recombination radiation. |
| **4. Incipient avalanche** | One carrier seeds a branching process that either becomes extinct or survives. | Junction electric field/bias reservoir → carrier kinetic energy → impact ionization, additional pair excitation, and phonons. The original photon no longer powers this stage. | Extinction remains possible. This is a bias-dependent click/no-click gate, not a site-selection law. |
| **5. Self-sustaining avalanche / commitment** | Carrier number grows to a space-charge-limited macroscopic pulse. | Bias supply plus stored junction-field energy → pair production, lattice heat, trap occupation, and weak hot-carrier electroluminescence/crosstalk photons. | Effectively irreversible. With $Q=\\int I,dt$, $E_{\\rm av}=\\int V_d(t)I(t),dt$ typically in the pJ range, versus a visible photon's $\\sim10^{-19}$ J: a gain-energy ratio of order $10^7$. |
| **6. Registration** | Avalanche current crosses a comparator threshold and produces a digital record. | Readout-rail energy → logic switching and circuit heat; avalanche signal energy is an input to, not the sole power source of, the electronics. | Classical and irreversible. The comparator threshold is an engineering threshold, downstream of microscopic selection. |
| **7. Quench** | Diode voltage is pulled toward/below breakdown and the avalanche extinguishes. | Remaining junction-field energy → junction and quench-resistor heat; weak outgoing EM transients propagate in circuit modes. | Irreversible dissipation. Count the capacitor discharge only once: it is an intermediate store of bias energy, not a second reservoir. |
| **8. Recharge / reset** | Bias supply restores junction voltage; traps may retain memory and later cause afterpulses. | Bias supply → restored capacitor energy $\\tfrac12 CV^2$ plus resistor/driver heat. Trap energy is temporary electronic/lattice storage and must be released as phonons, carriers, or radiation. | Dissipative; detector returns to a ready state after dead time. |

For a full event, with the source and supplies included rather than treated as prescribed backgrounds,

$$
\Delta!\left(E_{\rm EM}^{\rm inc}+E_{\rm el}+E_{\rm ph}+E_{\rm rad}+E_{\rm junction}+E_{\rm bias}+E_{\rm circuit}+E_{\rm out}\right)=0.
$$

Electrical bookkeeping should use measured energy currents, not “gain” as an energy source:

$$
W_{\rm bias}=\int V_{\rm supply}(t)I_{\rm supply}(t),dt,
\qquad
\Delta U_C=\tfrac12 C\big(V_f^2-V_i^2\big),
$$

with avalanche, quench, and reset heat/radiation summing to $W_{\rm bias}-\Delta U_C$ after sign conventions are fixed.

## Equations and state bookkeeping

A conserving starting point is

$$
H=H_{\rm EM}+H_{\rm el}+H_{\rm ph}+H_{\rm rad}+H_{\rm junction}+H_{\rm bias}+H_{\rm circuit}+H_{\rm int},
\qquad \frac{d}{dt}\langle H\rangle=0,
$$

where time-dependent circuit controls are replaced by explicit source degrees of freedom or else recorded as work. A schematic absorption coupling is

$$
H_{\rm int}=\sum_i \hbar g_i,b_i^\dagger a_f+\text{h.c.},
$$

where $b_i^\dagger$ creates the relevant interband/excitonic carrier excitation. The state normalization obeys

$$
|\alpha|^2+\sum_i|\beta_i|^2+P_{\rm other}=1,
$$

and the energy expectation is carried by all sectors. If site excitations are nearly degenerate, $\langle H_i\rangle\simeq |\beta_i|^2\hbar\omega$; again, this is not a possessed fractional quantum at site $i$.

If the framework introduces ontic site stakes $e_i$, a minimally conserving effective exchange must satisfy pathwise $\sum_i de_i=0$, for example

$$
de_i=\sum_{j\ne i}\sigma_{ij}(e),dW_{ij},
\qquad dW_{ji}=-dW_{ij},\quad \sigma_{ij}=\sigma_{ji},
$$

with absorbing/dropout behavior derived rather than imposed by numerical clipping. This antisymmetric form repairs the ledger mathematically, but it does **not** derive the $e_i$ as physical variables or explain how a winning channel receives one whole quantum. A Lindblad jump or quantum-trajectory unraveling can account for missing norm by routing it into named channels, but its jump probabilities cannot serve as a Born-independent derivation if the Born rule was used to define them.

## Selection and amplification must remain separate

The measurable click probability has the schematic factorization

$$
P_{\rm click}(i)=p_{\rm abs}(i),\eta_{\rm col}(i,V),P_{\rm trig}(i,V),
$$

where $p_{\rm abs}(i)$ contains the upstream quantum weight, while collection and avalanche survival are device-dependent thinning. The bias changes collection, triggering probability, latency, gain, and direction; spatially nonuniform bias can therefore distort the **observed** click map. That is detector response unless a calculation shows bias feedback during the coherent absorption/selection interval.

Avalanche energy is powered by the bias reservoir:

$$
E_{\rm av}=\int V_d I_{\rm av},dt\gg\hbar\omega.
$$

A thermal/tunneling dark carrier launches the same downstream cascade without a photon, which is strong evidence that stages 4–8 amplify a seed but do not choose among optical absorption amplitudes. Absorption without avalanche is also possible; therefore localization/selection, avalanche commitment, and electronic registration are distinct events.

## Analogy verdict and repair

**Verdict:** literal clipping of an optical wave crest is not conservation-respecting. A map that deletes the portion above a height changes field norm and energy without naming a receiver; sending the remainder to “the vacuum” is not an answer because vacuum is a state of specified field modes, not a drain. Nor may the clipped-away quantity be called the deposited photon energy while a remainder of the same one-photon excitation continues as though it retained a classical energy fraction.

Two repairs are useful:

1. **Upstream: energy-conserving scattering, not clipping.** Replace the platform by a unitary absorber map
   $$
                |1_f,G,B_0\rangle\to \alpha|1_{\rm out},G,B_\alpha\rangle+\sum_i\beta_i|0,E_i,B_i\rangle.
                $$
                The “height” becomes coupling to allowed material final states; every rejected/returned component is an explicit outgoing EM mode and every absorbed component is an explicit electronic/bath channel. This describes capture but does not yet select one $i$.
2. **Downstream: first passage in carrier number.** Use the platform for the real metastable variable
   $$
                dn=[\alpha(E)-\beta_{\rm loss}]v_d n,dt-cn^2dt+\sqrt{2Dn},dW,
                $$
                with extinction versus passage into the self-sustaining avalanche basin. Each impact-ionization step draws named energy from the junction field. This is a valid threshold model for click/no-click amplification, not a derivation of Born site selection.

A stage-2 “rogue-wave” selection can be more than metaphor only after a nonlinear/nonlocal focusing or conserving first-passage law is derived from the absorber–field–bath Hamiltonian. Its output map must preserve norm, deliver exactly one $\hbar\omega$ excitation, and state what physical modes contain the nonwinning amplitudes before and after commitment.

## Missing measurements and calculations

- Derive the absorber + common EM field + lattice influence functional/master equation without outcome-conditioned jumps; compute energy-current operators, drift, covariance, memory, boundary behavior, and whether any ontic conserving $e_i$ process actually emerges.
- Specify a finite winner-gating/drain law. Calculate the fate of $\beta_{j\ne i}$, the energy/norm flow during the drain interval, and double-commit probability.
- Measure event-resolved $V_d(t)$ and $I(t)$ together with supply/readout-rail currents, junction temperature rise, electroluminescence, and emitted circuit transients to close the pJ ledger with uncertainties.
- Quantify absorbed-but-untriggered events: nonradiative heat versus recombination luminescence, including wavelength and bias dependence.
- Bound residual energy at losing sites and any coherent outgoing optical remainder with pump–probe/echo or interferometric measurements. “No calorimetric residue” needs a numerical bound, not a verbal claim.
- At fixed optical preparation, sweep excess bias and map $P_{\rm trig}$, spatial click probabilities, timing, and pulse energy to test upstream-weight/downstream-thinning factorization.
- Include trap-stored energy and secondary photons in afterpulse/crosstalk accounting rather than assigning all avalanche energy directly to phonons.

## Questions for the other participants

**Foundational selection:** What is the ontic variable whose value is $e_i$ rather than merely $\langle H_i\rangle$? At what instant is the photon fully annihilated? What finite equation removes or reroutes losing amplitudes while preserving norm and energy, especially for two separated SPADs? Did selection occur in an absorbed-but-untriggered event?

**Device physics:** Can measured or simulated current/voltage traces supply a non-double-counted split among junction discharge, supply work, phonons, secondary photons, traps, quench heat, and readout energy? What bounds exist on recombination radiation in the no-click channel?

**Analogy/experiment:** Which named modes receive the “remainder,” and what measurement distinguishes conservative coherent return from ordinary reflection, transmission, nonradiative loss, and simple detector inefficiency?

## What would change my mind

- A microscopic derivation that produces ontic site energies (not expectations), pathwise conservation, unbiased winner statistics, a finite one-winner drain, and correct beamsplitter anticorrelation without inserting Born-weighted jumps.
- Event-resolved calorimetry showing reproducible fractional photon-energy residues at losing sites or a coherent outgoing remainder quantitatively tied to those sites.
- A bias-dependent change in upstream site selection or interference, after electroabsorption, collection efficiency, heating, dark counts, and threshold effects are controlled.
- Conversely, a verified Hamiltonian scattering calculation showing that “losing amplitudes” are coherently routed into explicit modes while one channel receives exactly one quantum would validate a repaired wave-realistic picture, though the outcome-weight derivation would still be a separate burden.

## Cross-review

### Direct exchanges and concessions

| Contact | Resolution |
| --- | --- |
| **Device physics** | Ratified the closed ledger and capacitor-counted-once rule. I narrowed “capture is reversible”: echo media prove reversibility in principle, but an indirect-gap room-temperature Si SPAD becomes practically one-way within roughly $10$–$100$ fs; channel-specific carrier commitment completes on the ensuing sub-ps-to-$\\sim1$ ps phonon/separation scale. The device review also supplied the active/parasitic absorption split, depth-dependent response, and realistic measurement limits below. |
| **Foundational selection** | We jointly separated three ontologies that cannot share one energy story: strict unitary evolution, unitary wave plus a one-world beable, and continuous winner routing. We agreed that norm redistribution is not an energy current and that local expectations are not possessed fractional parcels. |
| **Analogy / experiment** | We agreed on two platforms—open upstream selection and standard downstream avalanche escape—and on a bias-reservoir-powered flood. After direct correction, the analogy report adopted the explicit unitary-beable/routing fork, the collection “soak-away” channel, the full no-click partition, and the distinction between luminescence bounds and hypothetical losing-site residue. The repaired dam is now jointly ratified as a teaching aid, not a derived selection mechanism. |

### Joint probability and no-click ledger

Let $a_{\rm act}(x)$ be the active-region absorption density, $A_{\rm par}$ parasitic absorption in contacts, coatings, guard structures, or unreachable neutral material, and

$$
A=A_{\rm par}+\int dx,a_{\rm act}(x).
$$

The defensible four-way partition is

$$P_{\rm out}=1-A.$$

$$P_{\rm abs,loss}=A_{\rm par}+\int dx,a_{\rm act}(x)[1-\eta_{\rm col}(x,V)].$$

$$P_{\rm abs,ext}=\int dx,a_{\rm act}(x)\eta_{\rm col}(x,V)[1-P_{\rm trig}^{\rm reg}(x,V)].$$

$$P_{\rm click}=\int dx,a_{\rm act}(x)\eta_{\rm col}(x,V)P_{\rm trig}^{\rm reg}(x,V),\qquad \sum P=1.$$

Here $P_{\rm trig}^{\rm reg}$ is defined to include survival through the discriminator; otherwise twilight/sub-threshold pulses form a fifth branch. Scalar $A\eta_{\rm col}P_{\rm trig}$ is only a position-averaged shorthand because absorption depth, electron/hole collection, and triggering probability are correlated. Bias calibration must include depletion-width modulation as well as Franz–Keldysh response.

The energy consequences differ sharply: $P_{\rm out}$ contains one whole photon in named outgoing optical modes; parasitic or uncollected absorption sends the photon energy mainly to phonons; an extinct incipient avalanche sends the absorbed photon energy **plus the small bias energy already drawn** to phonons, with minor trap and radiative channels. Dark counts, afterpulses, and crosstalk are separate input histories, not additional partitions of the incident photon.

### The one-world energy fork

1. **Strict unitary evolution:** all entangled amplitudes persist. There is no physical loser drain and no unique ontic seed; only total and local expectation energies are defined by the quantum state. Decoherence does not change this.
2. **Unitary wave + selected beable:** one material configuration is actual while empty-wave components persist. The theory must define whether the wave carries stress-energy and how it couples to the beable. It may not book $|\beta_j|^2\hbar\omega$ as a separately possessed parcel in every empty component and also book a full $\hbar\omega$ at the actual site.
3. **Continuous winner routing:** losing components are dynamically driven to zero and one channel receives the excitation. In ordinary taxonomy this is a continuous objective-reduction law. It owes explicit field/matter/bath energy currents, a finite drain time, and a no-double-commit law; norm flow alone does not close the ledger.

Thus, in a one-world model that actually supplies a localized pair, an absorbed-but-untriggered history contains microscopic selection even though no click record forms. Strict unitary evolution supplies no such unique selected history.

### Corrected dam wording

The dam survives only as a stage-separation and conditional-theorem picture:

- **Ripple and inlets:** the incident one-photon state couples to bath-defined carrier channels. The upstream “fair inlet lottery” is not established SPAD physics; it stands for the still-underived stake ontology, conserving kernel/linear hazard, absorbing boundary, and finite exclusivity law.
- **Ontology fork at the inlets:** winner routing may say one inlet receives the whole excitation while others drain to zero, but must name the currents. A unitary-beable version must instead say the wave reaches all inlets while one inlet contains the actual configuration; empty components persist and their energetic status remains open.
- **Soak-away channel:** after a unique seed exists, collection can fail before the avalanche lip; this is $1-\eta_{\rm col}$, not avalanche extinction.
- **Lip:** carrier-number branching crosses a bias- and position-dependent committor surface. This is standard first-passage/branching physics and is not Born selection.
- **Reservoir and flood:** the junction field is the intermediate store; capacitor discharge plus contemporaneous supply work power the avalanche. $\int V_dI_{\rm av}dt$ is not added again as a separate reservoir.
- **Drains and reset:** phonons dominate; secondary photons and trap storage are energetically tiny but functionally important. Readout-rail work, quench heat, outgoing circuit fields, and recharge work are named separately. A trap-released carrier only seeds an afterpulse; the later avalanche is again bias-powered.

No sub-quantum optical remainder propagates in any repaired whole-photon capture story. That statement does **not** authorize deletion of empty unitary components or settle their energy ontology.

### Measurement limits and surviving objection

- Event-resolved measurements can identify an exiting heralded photon and close the pJ avalanche ledger from calibrated $V_d(t)$ and $I(t)$. They cannot calorimetrically resolve a few-eV deposit in a 300 K SPAD junction.
- Recombination luminescence, secondary photons, and losing-site heat can be bounded only in ensembles. Silicon's very small radiative yield makes luminescence a statistical bound, not an event tag. That bound does not by itself constrain hypothetical losing-site residue.
- The no-click exit test directly separates $P_{\rm out}$ from the union of absorbed no-click histories. Collection loss versus avalanche extinction can be decomposed statistically by wavelength and bias sweeps, not event by event.
- The cleanest finite-drain target is a separation- and timing-dependent excess of two unique seeds after subtracting multiphoton input, accidentals, crosstalk, and dark histories. $O(\Lambda\tau_{\rm drain})$ is only generic hazard-window scaling, not a universal coefficient.
- Residual outgoing coherence/energy is model-dependent. A weak reversible absorber or quantum-memory medium is more suitable than a Si SPAD, whose fs-scale dephasing closes the coherent window before ordinary gating can resolve it.

The surviving objection is therefore unchanged but sharper: neither the repaired dam nor the SPAD avalanche supplies the upstream one-world law. The theory still owes an ontic stake definition, a Born-independent conserving kernel, and finite exclusivity/energy routing across separated absorbers.

### Synthesis recommendation

Adopt the position-integrated four-way ledger and the two-platform dam for teaching. Present the upstream inlet lottery only as a conditional mathematical repair with the three ontology options explicit. Treat the downstream collection, avalanche, registration, quench, and reset chain as standard bias-powered detector physics. Prioritize: (1) the two-absorber microscopic reduction with energy-current operators; (2) calibrated bias/wavelength factorization and no-click exit accounting; (3) controlled two-seed coincidence bounds on finite drain; and (4) reversible-absorber coherence tests. Do not describe ontic fractional site energies, loser deletion, or “vacuum disposal” as established consequences of the real-wave hypothesis.
