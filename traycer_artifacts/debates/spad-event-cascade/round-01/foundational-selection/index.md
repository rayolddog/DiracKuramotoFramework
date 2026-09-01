---
title: "Foundational selection in a SPAD — where one world needs an extra law"
kind: spec
---

# Foundational selection in a SPAD — where one world needs an extra law

## Protected concern

John's target is coherent and worth protecting: the photon and detector are physically real waves; one event occurs in one world; the event is produced by continuous dynamics rather than a projection postulate; and the electrical bias amplifies the result rather than secretly supplying the quantum outcome.

The protection has a sharp price. Standard unitary detector theory gives a distributed, entangled photon–matter–bath state and explains decoherence, stable pointer channels, avalanche gain, and observed probabilities once the Born/measurement rule is used. **Unitary dynamics alone does not make one term of that state the uniquely actual term.** Decoherence suppresses interference between channels in a reduced density matrix; it does not choose one channel in the closed state. The avalanche then magnifies whichever seed a quantum trajectory or measurement postulate says occurred, but it does not retrospectively derive that seed.

Therefore the framework needs an ontic selection law between distributed excitation and the unique localized seed. Calling the later avalanche threshold “selection” would move the unresolved step offstage, because an identical avalanche can be launched by a dark carrier with no photon present.

This conclusion preserves the one-world goal, but it also classifies the available ways to realize it:

1. **Additional beables/registry:** the wave remains unitary, while a unique material configuration or registry selects the actual channel. This is a one-world hidden-variable completion. It owes a Born-weighted distribution, a finite exclusivity law, and an account of why physically real “empty” wave components cannot later seed records.
2. **Continuous stochastic or nonlinear winner routing:** the wave itself transfers norm/excitation into one channel and drives the others to zero. It avoids a discontinuous projection, but in standard foundations vocabulary it is still a continuous objective-reduction law unless the losing wave remains physically present.
3. **Decoherence alone:** insufficient for the stated aim. It provides an improper mixture, not one actual result.

The framework should choose between the first two rather than use language that slides between them.

## State and equation sequence

### 0. Incoming wave packet and closed ledger — standard

Take the incident photon to be

$$
\lvert1_f\rangle=a_f^\dagger\lvert0\rangle,
\qquad
a_f^\dagger=\int d^3k f(\mathbf k)a_{\mathbf k}^\dagger,
\qquad
\int d^3k |f(\mathbf k)|^2=1.
$$

The full initial state is

$$
\lvert\Psi_0\rangle=\lvert1_f\rangle\lvert G\rangle\lvert B_0\rangle\lvert V_{\rm bias}\rangle,
$$

where $|G\rangle$ is the semiconductor ground state, $|B_0\rangle$ includes lattice and circuit microstates, and the last factor names the biased electrical reservoir. A closed description evolves under

$$
H=H_\gamma+H_{\rm det}+H_B+H_{\rm bias}+H_{\rm int},
\qquad
H_{\rm int}=-\int d^3x \mathbf J_{\rm m}(\mathbf x)\cdot\mathbf A(\mathbf x).
$$

In a band basis, the rotating-wave part has the illustrative form

$$
H_{\rm int}\simeq \sum_\mu \hbar g_\mu a_f c_\mu^\dagger v_\mu+\text{h.c.}
$$

For the reference room-temperature silicon SPAD, the modes $\mu$ are extended Bloch interband electron–hole modes; excitons are not a useful intermediate because their binding is below $k_BT$ and the junction field ionizes them. A localized channel basis $i$ emerges only through detector–bath coupling, disorder, and the multiphonon thermalization cascade. Cross-review identifies it with phonon-dressed free-carrier packets of roughly 10 nm extent, not atomic sites or pixels.

### 1. Distributed capture amplitude — standard

Unitary interaction produces, schematically,

$$
\lvert\Psi(t)\rangle=
c_\gamma(t)\lvert1_{f_t},G,B_0\rangle
+\sum_\mu\beta_\mu(t)\lvert0,E_\mu,B_\mu(t)\rangle
+\sum_r u_r(t)\lvert1_r,G,B_r\rangle+\cdots .
$$

The $\lvert E_\mu\rangle$ are extended electronic excitations spatially weighted by the optical packet; in indirect-gap silicon, $\lvert B_\mu\rangle$ already includes the momentum-conserving vertex phonon, which does not by itself distinguish position. The $r$ terms name reflected, transmitted, or scattered optical modes. This is the precise sense in which capture is initially distributed. It is **not yet a unique capture event**. It is coherent transfer amplitude between the one-photon and one-excitation sectors.

The standard absorption calculation fixes the response kernel and the extended-mode amplitudes $\beta_\mu$; transformation into the bath-selected packet basis gives coefficients $c_i$. These become outcome probabilities only after the Born rule or an equivalent measurement postulate is applied.

### 2. Bath-induced localization basis — standard, but not selection

Tracing over lattice and circuit modes gives

$$
\rho_C(t)=\sum_{ij}c_i c_j^*D_{ij}(t)\lvert C_i\rangle\langle C_j\rvert,
\qquad
D_{ij}(t)=\langle B_j(t)|B_i(t)\rangle.
$$

Here $\lvert C_i\rangle$ denotes a bath-defined, phonon-dressed free-carrier packet. Phonon scattering and carrier–environment entanglement can rapidly make $D_{ij}\approx0$ for distinct packets. This explains why localized carrier configurations are robust pointer states. It does not turn the full state into one $\lvert C_k,B_k\rangle$. A diagonal reduced density matrix and ignorance about an already selected channel are experimentally similar, but ontologically different.

### 3. Candidate conserving selection game — framework hypothesis, microscopic derivation open

If the framework posits physically real nonnegative excitation stakes $s_i$ with

$$
s_i\ge0,\qquad \sum_i s_i=1,
$$

a canonical conserving martingale can be written as pairwise exchange. For every unordered pair $i<j$,

$$
ds_i=+\sqrt{\kappa_{ij}s_is_j} dW_{ij},
\qquad
ds_j=-\sqrt{\kappa_{ij}s_is_j} dW_{ij},
$$

with all pair contributions summed. Then $\sum_i ds_i=0$, each $s_i$ has zero drift, and a face $s_i=0$ is absorbing if no separate Hamiltonian term repopulates it. If the process reaches a simplex vertex and

$$
T_{\rm fix}=\inf(t:s_k(t)=1\text{ for some }k),
$$

optional stopping gives

$$
\Pr(K=i)=\mathbb E[s_i(T_{\rm fix})]=s_i(0).
$$

This is the strong conditional result retained by the [Born Selection synthesis](../../../born-selection-roundtable/final-synthesis). It is a mathematically valid form for the fair lottery. It is **not yet a SPAD derivation**, because five physical premises remain open:

- what $s_i$ is ontically, rather than as the already-Born quantity $\langle\Psi|\Pi_i|\Psi\rangle$;
- why the closed photon–matter–bath dynamics reduces to zero-drift conserving exchange;
- why $s_i=0$ is physically absorbing rather than repopulated by ordinary hopping or coherent evolution;
- why fixation completes inside the actual femtosecond-to-picosecond pre-seed window; and
- how exclusivity works across separated detectors that do not share local bath microstates.

### 4. Alternative linear first-event law — framework hypothesis, microscopic derivation open

Fixation is not the only conditional route. Let a genuinely ontic stake process be a martingale and let an irreversible seed event at channel $i$ have classical hazard

$$
\lambda_i(t)=\Lambda(t)s_i(t),
\qquad
\sum_i\lambda_i(t)=\Lambda(t).
$$

The mark of the first event then has

$$
\Pr(K=i)
=\mathbb E\left[\int_0^\infty
e^{-\int_0^t\Lambda(u)du} \Lambda(t)s_i(t) dt\right]
=s_i(0),
$$

when an event occurs with probability one and the martingale/integrability conditions hold. With a no-absorption branch, the same statement applies conditionally on entry into the active absorption sector, provided the total hazard does not itself favor a channel.

This law could attach to the first channel-specific irreversible process: production of an on-shell electron–hole pair plus channel-distinguishing phonons, irreversible carrier separation, or entry into a multiplication trajectory. It must **not** be justified by saying “Fermi’s golden rule gives $\lambda_i\propto|\beta_i|^2$,” because the usual interpretation of golden-rule rates as event probabilities already uses the Born rule. A Born-independent derivation would have to begin with ontic energy/stake and a classical escape law, then derive both linearity and the noise measure from the closed dynamics.

### 5. Unique seed, transport, and avalanche trial — standard after selection is supplied

Once one localized seed $K$ exists, write

$$
\lvert\Psi\rangle_{\rm actual}\longrightarrow \lvert0,C_K,B_K'\rangle,
$$

where $C_K$ contains an on-shell carrier pair and the channel-specific bath/transport state. The photon energy is now in band excitation, carrier kinetic energy, phonons, and possibly re-emitted optical modes. An absorbed photon whose carrier recombines or whose avalanche dies has still undergone microscopic site selection, although it produces no registered click.

Carrier multiplication is the amplitude-branching process identified in `single_photon_derivation.md`:

$$
dn=\big([\alpha(E)-\beta_{\rm loss}]v_d n-cn^2\big)dt
+\sqrt{2Dn} dW_t.
$$

For a seed $n=1$, the chain either becomes extinct or survives to a space-charge-limited avalanche. Its survival probability is $P_{\rm trig}=1-q$, where $q$ is the smallest root of the offspring generating-function equation $q=F(q)$. This stochastic gate determines **click versus silent absorption**, not which absorption channel was selected. The applied bias controls $\alpha(E)$, drift, collection, $P_{\rm trig}$, gain, and timing. Apart from ordinary field-dependent changes in local optical response, it need not and in standard theory does not choose the Born channel.

### 6. Macroscopic record and reset — standard

A useful detector-level click-commit boundary is a committor threshold,

$$
N_*(x,V;\varepsilon):
\Pr(\text{avalanche survives}\mid N_*,x,V)>1-\varepsilon,
$$

not a universal carrier number. The electrical record occurs later when the current pulse crosses the circuit discriminator. Quench and recharge may be represented schematically by

$$
C_j\frac{dV_d}{dt}=\frac{V_{\rm bias}-V_d}{R_q}-I_{\rm av}(t),
$$

which first drives $V_d$ below breakdown and then returns it to the armed value. These processes are strongly dissipative and bias-powered. They explain irreversibility of the record, not uniqueness of the upstream quantum outcome.

## Detailed stage table

Labels: **[S] standard**, **[F] framework hypothesis**, **[O] open calculation**.

| Stage | Degrees of freedom and illustrative state/law | Energy source and receiving modes | Reversibility | Stochastic status | Bias role | Status and observable check |
| --- | --- | --- | --- | --- | --- | --- |
| **0. Optical arrival** | One-photon packet transformed among incident, reflected, and transmitted modes | The photon energy remains in named optical modes | Reversible linear optics | None in the closed evolution | Changes depletion profile and weakly the optical response; no gain yet | **[S]** Reflection/transmission and absorption-depth spectra |
| **1. Distributed capture coupling** | One-photon + ground state → unabsorbed component + extended interband electron–hole modes through current–field coupling | Field energy enters the one-excitation sector; above-gap excess later reaches phonons | Photon annihilation becomes practically irreversible through escape into the continuum on a fs–100 fs scale, although the closed evolution remains unitary | Global unitary evolution is deterministic; standard event probabilities use Born | May alter local coupling or absorption efficiency through device electro-optics, but does not supply avalanche energy | Amplitude formation **[S]**; unique capture **[O]**. Check spectroscopy, absorption tomography, and ultrafast polarization dephasing |
| **2. Distributed excitation and decoherence** | Extended modes become entangled phonon-dressed carrier packets of roughly 10 nm extent; reduced-state coherences decay over 10 fs–1 ps | Electronic excitation entangles with phonons, disorder, and other carriers | Closed evolution reversible in principle; recoherence fantastically impractical | Environmental entanglement; no fundamental random winner in unitary theory | Field can displace/shape the packet basis locally while not thereby selecting Born weights | Pointer-basis formation **[S]**; single actuality **not supplied**. Check two-pulse dephasing and localization time/length |
| **3. Ontic selection** | Candidate $s_i$ martingale, first fixation, or first linear-hazard mark $K$ | A conserving law must keep the full field+matter+bath ledger closed; “vacuum” is not a sink | Must become exclusive; whether losers vanish, persist as empty waves, or return energy is model-dependent | **[F]** must choose fundamental stochasticity or ignorance over hidden microstates; standard noise does not decide ontology | A local field dependence is allowed only as a calibrated coupling/efficiency or a derived term; unexplained bias-driven drift would change outcome weights | **[F/O]**. Check calibrated two-pixel bias asymmetry, Born linearity, anticorrelation, and finite double-commit bounds |
| **4. Microscopic seed commitment** | One on-shell localized electron–hole pair plus channel-specific bath/transport correlations | Photon energy becomes gap energy, carrier kinetic energy, and phonons or luminescence on recombination | Practically irreversible once field-driven separation and many bath modes encode the channel; still reversible for the exact closed unitary state | Standard theory uses a jump/measurement outcome here; framework must provide the ontic law | Controls carrier separation and collection probability; can turn an absorbed event into a lost seed | Matter/bath mechanism **[S]** near 1 ps; why this channel **[O]**. Check absorbed-but-untriggered channels and ultrafast localization |
| **5. Carrier transport** | Localized carrier drift/diffusion into multiplication region, or recombination/loss | Bias field supplies kinetic energy, dissipated to phonons; recombination sends $E_g$ to phonons or a photon | Open-device irreversible but leaves no macroscopic record | Environmental/effective/ignorance noise | Sets direction, collection efficiency, depth-dependent jitter | **[S]** Timing tails, wavelength/depth dependence |
| **6. Incipient avalanche** | Branching from one carrier; extinction probability `q`, survival probability `1 − q` | Bias supply/junction capacitance powers impact ionization; phonons receive most dissipation | Can still go extinct; no guaranteed click | Effective branching randomness from microscopic scattering; operational quantum rates do not constitute upstream selection | Dominant control of trigger probability and buildup time | **[S]** Trigger probability versus bias, dark-count and photon-seeded buildup statistics |
| **7. Click commitment and amplification** | Carrier number crosses the position- and bias-dependent committor `N*(x,V;ε)` and grows toward saturation | Macroscopic energy is drawn from the bias reservoir, not the photon | Irreversible for practical purposes | Residual buildup jitter is effective; winner already fixed | Sets gain, saturation, lateral spread, and crosstalk | **[S]** Pulse-charge and buildup distributions. This is a record boundary, not Born selection |
| **8. Registration** | Comparator maps avalanche current to a digital edge | Front-end supply and avalanche energy dissipate as circuit/lattice heat | Irreversible engineering latch | Electronic noise affects timestamp and false counts | Affects signal amplitude indirectly | **[S]** Threshold scans. This is a literal threshold but a convention, not a foundational boundary |
| **9. Quench and reset** | Diode voltage is forced below breakdown, avalanche dies, RC/active recharge rearms the device | Stored junction energy and supply energy go to resistor, junction, lattice, and traps | Strongly dissipative | Trap release produces afterpulsing; circuit noise is environmental/effective | Entirely controls quench, dead time, recharge, twilight sensitivity | **[S]** Dead-time, recharge, afterpulse, and thermal measurements |

## Exact selection and commitment verdicts

### Selection verdict

**Selection is required after distributed photon–matter amplitude has formed and no later than the first unique channel-specific seed.** Standard unitary theory does not select that channel. It supplies the entangled state, and decoherence supplies an effectively classical channel basis. A POVM, quantum jump, or sampled trajectory supplies a selected channel only because a Born-weighted outcome rule has been added.

The most plausible device window is from the absorption vertex through the first channel-distinguishing phonon/scattering or carrier-separation event—femtoseconds to at most the sub-picosecond localization/dephasing scale for a room-temperature semiconductor. The current materials model does not locate a sharper instant. An ontic first-event law may make selection and seed commitment coincide. A fixation law instead makes selection a finite competition ending at the seed-commit boundary.

Selection also occurs in **absorbed-but-untriggered events**: a localized pair can be selected, recombine or fail to trigger, and leave no click. Thus selection is neither logically nor experimentally identical to registration.

### Commitment verdict

There are two physically useful commitments, and using one word for both causes the central confusion:

| Commitment | Exact meaning | Placement |
| --- | --- | --- |
| **Microscopic seed commitment** | One channel becomes the unique on-shell carrier/bath configuration and alternative channels can no longer seed independent records | For the reference Si SPAD: field-driven electron–hole separation at roughly 1 ps, after the multiphonon cascade has established which-site distinguishability |
| **Click commitment** | Given the seed, avalanche extinction has become negligibly probable | At the bias- and position-dependent avalanche committor, before the comparator fires |

`single_photon_derivation.md` correctly locates the SPAD's **record irreversibility** at the avalanche survival boundary. It does not locate or derive the upstream **quantum winner selection**. Both statements should be kept.

## Can the martingale or first-event law attach here?

**Yes as a precise conditional model; no as a result already derived from SPAD physics.**

- The best place to attach it is the active one-excitation manifold after optical coupling has established candidate channels and before one channel becomes an on-shell seed.
- **Fixation version:** the “platform” is the absorbing boundary $s_K=1$ (or a derived thin commit layer $1-w$), while zero-share channels drop out. This directly answers the analogy participant's question: Platform A can be drawn this way, but the boundary is only a commitment condition; the martingale kernel is the selecting dynamics and remains open.
- **First-event version:** a linear ontic hazard can terminate the game before fixation. It may better match a continuum absorber in which irreversible scattering occurs faster than a long gambler's-ruin game.
- A finite boundary $1-w$ generally perturbs exact fixation probabilities unless the commit mark is sampled linearly from the martingale shares. The size and sign of that correction must be calculated, not hidden in “near unity.”
- A local field dependence is **not categorically forbidden**. If it changes $g_i$, absorption, collection, or seed escape, it belongs in the calibrated detector response $\eta_i(V)$ or in the definition of the active channels. What Born fairness forbids is an unaccounted drift or nonlinear mark law that changes the conditional winner odds after those local response factors are fixed.
- Across separated detectors, a local bath-driven process cannot by itself guarantee one global winner. The current framework has no derived finite global-stop law. A viable registry must specify propagation/foliation, drain time $\tau_{\rm drain}$, loser-wave behavior, and a double-commit correction expected generically at order $O(\Lambda\tau_{\rm drain})$. This is a requirement, not yet a favored mechanism.

The most important calculation is therefore the one already identified by the Born review: start with two localized absorber sectors plus a common electromagnetic field and baths; integrate out unobserved modes without an outcome-conditioned unraveling; derive the drift, covariance, memory, boundary behavior, and first irreversible escape. Only that calculation can say whether a conserving martingale genuinely attaches to a SPAD.

## Raised-platform and rogue-wave analogy: repair, do not promote

The original picture contains three different thresholds:

1. **Spectral threshold:** the photon must match an allowed interband/impurity transition. This is a condition on frequency and material states, not on the instantaneous height of a weak classical field.
2. **Selection boundary:** a proposed absorbing boundary in ontic share/configuration space. This is the framework's open law.
3. **Avalanche and comparator thresholds:** standard carrier-number survival and circuit discrimination thresholds, powered by the bias supply.

### Threshold clipping — reject for microscopic selection

Clipping a local field peak above a height predicts partial removal, multiple crossings, and nonlinear click statistics set by tail probabilities. Single-photon absorption instead transfers one whole quantum per captured event, and standard detector response is linear in the one-photon density operator. A clipped “remainder” cannot be sent vaguely to vacuum.

### Absorbing boundary / first passage — best mathematical repair

Place the platform in **share space**, not above a real-space optical waveform. The raised edge is $s_K=1$ or the first irreversible linear-hazard event; crossing absorbs the entire one-excitation state into channel $K$. This cleanly represents exclusivity and commitment. It does not explain the martingale dynamics, the initial shares, or the global stopping rule, so it is a diagram of the required theorem rather than evidence for it.

On a no-capture event the whole photon remains in outgoing reflected/transmitted/scattered optical modes. On a capture event the whole photon is converted to the selected electronic and named bath modes. There is no physical channel in which “the energy above the platform” is taken while a lower-energy remainder of the same photon continues.

### Nonlinear focusing / rogue wave — possible only as a new theory with a high burden

A genuine focusing mechanism would require an explicit nonlinear equation for the one-excitation field, such as a norm- and energy-conserving coupling among photon, exciton, carrier, and bath fields. The nonlinearity must operate at one-photon occupation, generate one winner rather than multiple hot spots, reproduce linear Born weights rather than activation-tail weights, respect no-signaling constraints in entangled tests, and identify where the balancing energy goes. No known standard SPAD mechanism supplies such pre-seed focusing. The avalanche is nonlinear, but it starts after a seed exists and is photon-origin-blind.

“Rogue wave” may survive as teaching language for a stochastic concentration trajectory in share space. It should not be presented as a physical mechanism until the nonlinear/conserving kernel is derived.

## Born and collapse circularity audit

| Shortcut | Why it is circular or insufficient | Acceptable replacement |
| --- | --- | --- |
| Set the initial stake equal to a quantum projector expectation and call it real local energy | This is the Born weight written as a stake; a one-excitation superposition does not automatically give independently possessed classical energy parcels at every site | Derive an ontic energy/share variable from the real field–matter model and show how it maps to detector channels without outcome probabilities |
| Use a POVM to define capture | A POVM is the correct operational prediction but already contains the probability rule under review | Use it as the benchmark response only; derive the ontic event law separately |
| Use a sampled Lindblad/quantum-jump trajectory | Different unravelings give the same master equation; choosing one as actual and sampling its jumps invokes Born probabilities | Derive a unique ontic noise/registry law from microphysics or state it as a new postulate |
| Say decoherence selected the site | Tracing out the bath removes observable interference but leaves all branches in the closed state | Add a beable/registry or a continuous winner-routing law |
| Invoke Fermi's golden rule as the Born derivation | The standard transition-probability interpretation uses squared amplitudes and the quantum probability postulate | Derive a classical linear hazard for already-ontic stakes, then show its domain and noise measure |
| Treat vacuum fluctuations as an automatically fair random seed | Quantum vacuum correlations do not by themselves define realized classical samples; a chosen stochastic representation can import the desired measure | Specify whether noise is fundamental or ignorance, derive its covariance, and test drift/conservation |
| Simulate a Wright–Fisher process and recover $s_i(0)$ | This verifies optional stopping for the chosen process, not that a SPAD realizes the process | Derive the generator from the absorber–field–bath Hamiltonian, then use simulation as a check |
| Declare $s_i=0$ absorbing or “first click wins” | This imports dropout and exclusivity, while ordinary hopping can repopulate sites and separated detectors can nearly commit together | Supply a physical winner gate, finite drain/registry flow, and a bound on double commits |
| Drive losing amplitudes to zero and call it “not collapse” | Continuous branch suppression is still objective reduction in the usual taxonomy | Either accept and specify a continuous reduction law, or keep the unitary wave and specify a one-world beable plus empty-wave behavior |
| Condition the state on the observed click and read that as dynamics | Conditional updating is an observer's inference unless a physical update law is supplied | Give an unconditional finite evolution for field, matter, bath, and registry |

## Questions and replies for the other participants

### To SPAD device physics

1. What localized basis does the material actually select immediately after absorption—impurity-scale orbital, wave packet built from Bloch bands, exciton center-of-mass packet, or carrier position after the first phonon—and what are the localization length and time? This determines what the index $i$ can physically mean.
2. What is the earliest channel-specific process that is effectively unrecoverable: first phonon emission, carrier separation, trap capture, or entry into the multiplication layer? I place microscopic seed commitment there, not at the later avalanche threshold.
3. Can the click committor $N_*(x,V;\varepsilon)$ be estimated from standard avalanche transport rather than quoted as a universal “few carriers” threshold?
4. Please confirm the important no-click case: an absorbed photon can create a localized carrier that recombines or launches an extinct avalanche. My verdict is that microscopic selection occurred even though click commitment did not.

### To energy and conservation audit

1. If $s_i$ is claimed to be ontic energy rather than probability, what exact local or mode-resolved observable defines it inside the one-excitation sector?
2. In a winner-routing model, identify the Hamiltonian current that moves excitation from losing $i\ne K$ sectors to $K$ or to outgoing field/lattice modes. Norm redistribution alone is not an energy ledger.
3. In a beable-plus-unitary-wave model, decide whether empty branches carry physical energy. If they do, explain why the selected site can still receive the full $\hbar\omega$ without double counting; if they do not, explain what “physically real wave” means energetically.
4. Separate and close the two no-click ledgers: whole-photon non-absorption into outgoing optical modes, and absorbed-but-untriggered recombination/extinction into phonons, luminescence, and circuit/bias channels.

### To analogy and experiment

1. **Answer to Platform-A first passage:** yes, conditionally. The platform is the absorbing commit boundary; the selecting content lies in the conserving martingale or linear-hazard dynamics that has not yet been derived.
2. **Answer on bias:** linear hazard does not forbid calibrated local-field effects in $g_i$ or $\eta_i(V)$. It forbids treating an unexplained field-induced drift as Born-neutral. The clean null is factorization after local response calibration, not raw bias independence.
3. **Answer on a finite global stop:** none is currently derived. The clean observable is a separation- and timing-dependent excess double-commit probability or a finite loser-drain latency. Fast SPAD gating mainly probes the much later avalanche dynamics; two separated, independently read absorbers with sub-jitter coincidence bounds are closer to the foundational registry test.
4. In the proposed two-pixel bias test, please distinguish selection anomalies from ordinary POVM change by calibrating the complete local response at each bias, wavelength, position, and recharge phase. Only a residual nonfactorizing dependence bears on selection.
5. The sharpest conceptual interferometer is not “does a fractional remainder interfere?”—a one-photon event has no such standard remainder—but whether a deliberately weak, reversibly coupled absorber changes downstream coherence before irreversible seed commitment. Please state the visibility prediction of each ontic model.

## Cross-review

### Direct contacts

| Peer | Contact and convergence |
| --- | --- |
| [SPAD device physics](../device-physics) | Replaced atomic-site/excitonic language with extended Bloch interband excitation followed by roughly 10 nm phonon-dressed free-carrier pointer packets; split capture irreversibility, which-site distinguishability, and seed commitment; supplied a position- and bias-dependent avalanche committor |
| [Energy and conservation](../energy-conservation) | Ratified the unitary/beable/routing ontology fork; prohibited double-booking empty-branch expectations and a full quantum at the actual site; selected excess two-seed coincidences as the safest finite-registry bound |
| [Analogy and experiment](../analogy-experiment) | Accepted that the dam is a conditional-theorem/stage map rather than a mechanism; refined the factorization test, committor lip, Stage-A burden tags, and the distinction between passive and active ontic models |

### Material view changes

1. **The localized basis is now device-specific rather than schematic.** For room-temperature silicon, the absorption vertex populates extended Bloch interband modes. The indirect-transition phonon carries momentum information but does not select position. A multiphonon/disorder cascade creates approximately 10 nm phonon-dressed free-carrier packets over 10 fs–1 ps. Excitonic language is dropped for this reference device.
2. **“Irreversible absorption” has been split into three boundaries.** Photon annihilation into the e–h continuum becomes practically irreversible on a fs–100 fs scale; which-site distinguishability develops throughout the multiphonon cascade; field-driven electron–hole separation at roughly 1 ps is the earliest defensible microscopic seed commitment. An ontic winner law must finish no later than that last boundary.
3. **Avalanche commitment is now a committor, not a universal carrier count.** If a carrier has independent extinction probability $q(x,V)$, an illustrative threshold is
   $$
     N_*(x,V;\varepsilon)=\frac{\ln\varepsilon}{\ln q(x,V)},
     $$
     with independence and space-charge corrections stated. This keeps the standard click commitment bias- and position-dependent.
4. **The ontology remains deliberately unresolved.** Neither peer review nor device facts choose between a passive beable plus unitary wave and continuous winner-routing. The previous report's classification is retained as an explicit fork rather than collapsed into one “framework mechanism.”
5. **The dam language is narrowed.** “One inlet wins the whole ripple; the others end at zero” describes only continuous winner-routing. A passive-beable version must instead say that the wave reaches all inlets while one inlet contains the actual carrier configuration; empty-wave components persist unless another law removes them.
6. **The registry observable is rate-based, not SPAD-timestamp-based.** The primary bound is a separation- and delay-dependent excess two-seed coincidence probability per herald after subtracting multiphoton input, accidentals, dark histories, and optical/electrical crosstalk. Registered-edge timing is secondary because avalanche jitter is much slower than the proposed selection window.

### Joint statements

- **Standard unitary theory:** the closed state conserves total energy and has local energy expectations, but those expectations are not separately possessed classical parcels. There is no loser drain, decoherence supplies no unique seed, and the Born rule is still required for outcome probabilities.
- **Passive beable plus unitary wave:** one actual carrier configuration can exist while the wave remains unitary. This preserves no physical branch suppression, but the beable distribution, global exclusivity, empty-wave efficacy, and empty-wave stress-energy remain additional ontology. The selected site cannot simply be booked a full $\hbar\omega$ while every empty component is also booked its expectation share.
- **Continuous winner-routing:** driving losing components to zero is a continuous objective-reduction law in ordinary foundations terminology, even if it has no discontinuous projection. It needs explicit norm dynamics plus field/matter/bath energy currents; norm flow alone is not an energy ledger.
- **Downstream agreement:** avalanche extinction/survival, gain, comparator registration, quench, and reset are standard and seed-origin-blind. They do not derive upstream Born selection. Absorbed-but-untriggered events underwent microscopic localization/selection but not click commitment.
- **Analogy agreement:** the upstream platform is at best an absorbing boundary in a still-unproved selection law; the downstream spillway lip is a standard branching committor; the reservoir is the bias supply. Optical amplitude clipping remains rejected.
- **Bias agreement:** local fields may shape the pointer packets and the calibrated response $\eta_i(V)$. The selection test is residual failure of response factorization after calibration, not raw bias independence.

### Unresolved options and discriminators

| Option | What makes one seed actual? | Fate of losing components | Honest observable consequence |
| --- | --- | --- | --- |
| **Passive beable + strictly unitary wave** | A global material configuration/registry guided by the wave | Persist as empty wave components; energetic status must be defined | Exactly standard weak-absorber visibility and no excess one-photon double seeds, after ordinary backgrounds |
| **Active beable backreaction or continuous routing** | Finite feedback or stochastic/nonlinear transfer selects the winner | Suppressed, drained, or rerouted by an explicit law | Possible excess visibility loss during reversible coupling and/or excess two-seed probability during a finite drain window |
| **Standard unitary + Born conditioning** | Measurement postulate/operational update | Persist in the unconditioned state | Benchmark detector statistics; does not independently meet the requested one-world selection explanation |

A routing law gated only after irreversible seed commitment and faster than experimental resolution can be operationally indistinguishable from the passive-beable option in these tests. Therefore visibility and coincidence measurements bound **active backreaction and finite drain dynamics**, not ontology as such. Under a particular hazard model, an excess double-commit window may scale as $O(\Lambda\tau_{\rm drain})$; neither the coefficient nor a drain-time conversion is universal without the registry equation. Residual outgoing coherence or energy is a useful secondary probe but is more model-dependent and can be hidden by ordinary dephasing.

The dam's Stage-A lottery now carries four mandatory burden labels:

1. **Stake ontology/Born map:** $s_i(0)=|\beta_i|^2$ is imported if it is merely a quantum expectation; a real-field share still needs a derivation.
2. **Kernel:** zero-drift conserving exchange or a linear first-event hazard is the selecting premise, not a consequence of the picture.
3. **Absorption/dropout/return:** zero-share channels must remain out, finite commit layers must not silently bias weights, and no-capture amplitude must return through named modes.
4. **Finite exclusivity (U7):** separated absorbers require a one-winner law with a stated drain time and double-commit bound.

The downstream committor lip, bias reservoir, avalanche drains, and seed-origin-blindness are standard and do not hide Born selection.

### Synthesis recommendation

Use one six-part cascade in the round synthesis:

**Extended interband capture amplitude → bath-defined 10 nm carrier packets → ontic winner option still unresolved → field-separated unique seed at about 1 ps → collection plus extinction/survival at the position- and bias-dependent committor → bias-powered avalanche, registration, quench, and reset.**

Present the passive-beable and continuous-routing completions side by side. Do not choose between them without a microscopic law. Keep the dam as a teaching map with the four Stage-A burden labels, not as evidence. Lead experimentally with (i) calibrated upstream-weight/downstream-thinning factorization, including recharge/twilight sweeps; (ii) heralded, separated-absorber excess-coincidence bounds; and (iii) weak reversible-absorber visibility as a bound on active pre-commit routing. Fast SPAD gating should be treated primarily as an avalanche/backaction test, because it cannot directly resolve the sub-picosecond ontic-selection interval.

## What would change my mind

- **A microscopic open-system derivation, without outcome-conditioned jumps,** that produces ontic nonnegative shares, pathwise conservation, negligible drift, absorbing dropout, and either fixation or a linear first-event hazard in the actual pre-seed time window would promote the martingale proposal from conditional theorem to mechanism.
- **A finite one-world registry law** that handles separated absorbers, routes losing wave/energy, predicts a small double-commit or drain-time signature, and remains no-signaling would resolve the largest foundational gap.
- **Evidence that avalanche backaction reaches the still-coherent absorption state before localization** would move part of selection downstream and weaken my clean selection/amplification separation. The evidence must survive ordinary electroabsorption, collection, timing, and crosstalk controls.
- **A derived one-photon nonlinear focusing equation** that conserves the complete energy/norm ledger, gives one winner, recovers calibrated linear Born statistics, and passes separated-detector anticorrelation would rehabilitate “rogue wave” as mechanism rather than metaphor.
- **Conversely, a proof that the only viable detector reduction is the standard unitary entangled state plus Born conditioning** would not refute the real-wave ontology, but it would refute the claim that this detector model independently explains one-world selection.

## Bottom line

The physically honest cascade is

$$
\text{one-photon packet}
\rightarrow
\text{extended interband amplitude and bath-defined carrier packets}
\rightarrow
\boxed{\text{ontic winner law still required}}
\rightarrow
\text{one localized on-shell seed}
\rightarrow
\text{collection/loss}
\rightarrow
\text{branching extinction or survival}
\rightarrow
\text{bias-powered avalanche}
\rightarrow
\text{digital registration}
\rightarrow
\text{quench/reset}.
$$

The conserving martingale and passive linear first-event laws can sit exactly in the boxed interval and conditionally recover initial shares. What remains unproved is the decisive physics: that those shares are ontic rather than Born expectations, that the SPAD's closed dynamics realizes the fair conserving kernel and absorbing boundary, and that a finite one-world rule enforces exclusivity. The raised platform is best retained as an absorbing-boundary picture for that missing theorem and as a literal branching threshold for the later avalanche. It is not a valid optical-amplitude clip, and standard avalanche theory does not by itself select the quantum outcome.
