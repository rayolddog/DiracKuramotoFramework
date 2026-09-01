---
title: "Continuous generator for the 576-state two-absorber model"
kind: spec
---

# Continuous generator for the 576-state model

## Implementation status

The first calibration slice is implemented in `~/Projects/Physics/DiracKuramotoFramework/first_mark_two_absorber/`. It constructs the full 576-dimensional operators, coherent no-bath capture and return, field recombination, and the exact reverse-ordered global inverse. The final verification suite passes 18 of 18 checks under NumPy 2.3.5.

The [implementation ticket](implementation-no-bath), [independent review](implementation-no-bath/independent-review), two fixups, and [final closure review](implementation-no-bath/fixup-enforce-no-bath-contract/closure-review) record the full generator–reviewer exchange. All review findings are closed. Operational reversal, echo, and random-reference cases remain future work.

## Result

The baseline is one closed, time-dependent Hamiltonian acting on:

<user_quoted_section>photon field × absorber A × absorber B × phase qubit A × record qubit A × phase qubit B × record qubit B.</user_quoted_section>

It evolves continuously according to the ordinary Schrödinger equation. In plain English: at every instant, the Hamiltonian specifies how amplitude flows among the photon paths, reversible absorber excitations, phase records, and candidate material marks.

No collapse term, Lindblad jump, outcome sampler, registry variable, or Born-weighted random choice appears in this generator. It is the unconditional unitary baseline against which any later selection law must be compared.

## Evolution rule

In mathematical shorthand:

```text
d|Psi(t)>/dt = -(i / hbar) H(t) |Psi(t)>
```

The equivalent density-matrix form is:

```text
d rho(t)/dt = -(i / hbar) [H(t), rho(t)]
```

Here `[H,rho]` means “apply H before rho minus apply rho before H.” Because there is no extra dissipative term, the complete state remains pure and normalized. A reduced absorber state may nevertheless look mixed after the bath qubits are ignored.

The total generator is the sum of seven named pieces:

```text
H(t) = H_field
     + H_absorbers(t)
     + H_bath
     + H_capture(t)
     + H_phase(t)
     + H_mark
     + H_route(t)
```

Each piece is defined below and has one physical job.

## Subsystem order and dimensions

Use this tensor ordering everywhere in code and saved data:

```text
field, absorber_A, absorber_B, phase_A, record_A, phase_B, record_B
```

| Subsystem | Dimension | Basis order |
| --- | --- | --- |
| Field | 4 | vacuum, photon-A, photon-B, collected/outgoing photon |
| Absorber A | 3 | ground, reversible excitation, candidate mark |
| Absorber B | 3 | ground, reversible excitation, candidate mark |
| Phase A | 2 | phase-qubit zero, phase-qubit one |
| Record A | 2 | blank record, excited record |
| Phase B | 2 | phase-qubit zero, phase-qubit one |
| Record B | 2 | blank record, excited record |

The raw dimension is:

```text
4 × 3 × 3 × 2 × 2 × 2 × 2 = 576
```

## Basic transition operators

These are names for simple state changes. Identity operators on all unmentioned subsystems are implied.

### Field operators

```text
a_A   = |vacuum><photon-A|
a_B   = |vacuum><photon-B|
c_A   = |out><photon-A|
c_B   = |out><photon-B|
```

- `a_A` removes the photon from path A when absorber A is excited.
- `a_B` does the same in path B.
- The conjugates `a_A dagger` and `a_B dagger` return a photon to the corresponding path.
- `c_A` and `c_B` route returned arm amplitudes into the collected output mode.

These are truncated single-photon transitions, not unrestricted bosonic annihilation operators.

### Absorber operators

For absorber `i`, where `i` is A or B:

```text
S_i_plus  = |e_i><g_i|
S_i_minus = |g_i><e_i|
T_i       = |m_i><e_i|
P_e_i     = |e_i><e_i|
P_m_i     = |m_i><m_i|
```

- `S_i_plus` converts the ready absorber into its reversible optical excitation.
- `S_i_minus` reverses that capture.
- `T_i` converts the reversible excitation toward the candidate mark state.
- `P_e_i` and `P_m_i` measure whether the absorber occupies those states.

### Bath-qubit operators

For each phase qubit use the usual `Z` operator. For each record qubit use:

```text
r_i_plus  = |record-1><record-0|
r_i_minus = |record-0><record-1|
n_r_i     = |record-1><record-1|
```

- `Z_phase_i` stores a branch-dependent phase history.
- `r_i_plus` writes one local record excitation.
- `r_i_minus` erases it under exact reverse evolution.
- `n_r_i` measures its stored energy.

## 1. Free photon field

```text
H_field = hbar × omega × (
            |photon-A><photon-A|
          + |photon-B><photon-B|
          + |out><out|
          )
```

Plain English: a photon carries the same energy whether it is in arm A, arm B, or the collected output mode. The vacuum carries zero photon energy.

Keeping all three one-photon field states degenerate lets routing and interference move the photon without creating or destroying energy.

## 2. Free absorbers and record qubits

For each absorber:

```text
H_absorber_i(t) =
      [E_e + hbar × Delta_i(t)] P_e_i
    + E_m P_m_i

H_record_i = hbar × Omega_r × n_r_i
```

Use the baseline resonance conditions:

```text
E_e = hbar × omega
E_e = E_m + hbar × Omega_r
```

Plain English:

- The photon energy matches the reversible excitation energy.
- The reversible excitation can convert into the mark state while the record qubit receives exactly the energy difference.
- `Delta_i(t)` is an externally controlled detuning used for phase accumulation and echo tests.

Changing `Delta_i(t)` does work on the absorber. That control work must be recorded separately; energy conservation should not be tested as though a time-dependent control were free.

## 3. Free phase qubits

Choose the minimum baseline:

```text
H_phase_free = 0
```

The phase qubits are degenerate tags in Rung 1. They store relative phase information without carrying a meaningful share of the optical energy.

An optional known precession term may be added later:

```text
H_phase_free_i = (hbar × Omega_p_i / 2) Z_phase_i
```

That extension is unnecessary for the first model because the prepared reference history is already carried by the time-dependent functions `u_A(t)` and `u_B(t)` below.

For later shorthand, define the bath's free term as:

```text
H_bath = sum_i [H_phase_free_i + H_record_i]
```

## 4. Reversible photon capture

```text
H_capture(t) = hbar × sum over i=A,B of
    K_i(t) [a_i S_i_plus + a_i_dagger S_i_minus]
```

Plain English:

- In path A, photon amplitude can become absorber-A excitation amplitude.
- In path B, it can become absorber-B excitation amplitude.
- The same term permits the excitation to emit the photon back into its original arm.
- `K_i(t)` controls when the interaction is on and whether its sign is reversed during the direct-reversal protocol.

This term is Hermitian because every forward transition is paired with its reverse. With both absorbers identical and the input split equally, it cannot prefer A or B.

## 5. Pure-dephasing phase-history coupling

The selected minimum uses:

```text
H_phase(t) = hbar × sum over i=A,B of
    [chi_i × u_i(t) / 2] P_e_i Z_phase_i
```

Plain English:

- The phase qubit affects the phase accumulated by the reversible absorber excitation.
- It does not move population between the ground, excitation, and mark states.
- Because it commutes with the bare energy projectors, it carries phase history without consuming the optical photon energy.
- When the field is in a superposition of “absorber not excited” and “absorber excited,” this term correlates the phase qubit with those alternatives. Ignoring the phase qubit then reduces visible coherence.

`chi_i` is the strength of this phase-tag interaction. `u_i(t)` is a real, prepared reference projection bounded between minus one and plus one. It stands for the instantaneous projection of the local background phase onto the absorber's sensitive quadrature.

### Reference schedules

| Case | `u_A(t)` and `u_B(t)` |
| --- | --- |
| Common recorded reference | Same known constant or same known function |
| Known distinct references | Different known functions, both recorded |
| Random unrecorded | Independently generated piecewise functions; realized values hidden from operational controller |
| Random recorded twin | Exactly the same random functions, with values retained for time-reversed control |

This is a phenomenological representation of phase history. It does not derive the background distribution or vacuum noise from QED. Every random schedule still generates a unitary run; randomness enters only through the ensemble of prepared Hamiltonians.

## 6. Candidate mark and local energy record

```text
H_mark = hbar × sum over i=A,B of
    G_i [T_i r_i_plus + T_i_dagger r_i_minus]
```

Plain English:

- `T_i r_i_plus` converts reversible excitation `e_i` into candidate mark `m_i` while writing one excitation into record qubit `i`.
- The reverse term permits that record to return coherently into the absorber.
- The resonance condition above makes the exchange energy-conserving.
- `G_i` determines how quickly the candidate record forms and recurs.

This is not an irreversible collapse. With one record qubit, amplitude will generally oscillate back. The term provides the smallest energy-bearing record channel whose recurrence can be measured.

Operational reversal is not allowed to flip `G_i` or manipulate the record qubit. Exact global inversion must reverse both.

## 7. Field recombination and collection

```text
H_route(t) = hbar × sum over i=A,B of
    J_i(t) [exp(i theta_i) c_i + exp(-i theta_i) c_i_dagger]
```

Plain English:

- This is a controllable beamsplitter/recombiner inside the truncated field space.
- It sends a photon returned to arm A or B into the common output mode.
- `theta_A` and `theta_B` set the recombination phases.
- Successful reversal requires the original A/B relative phase so that both amplitudes enter the designated output constructively.

This term turns phase recovery into an observable output probability and interference visibility rather than merely an abstract state overlap.

## Complete forward generator

Using the definitions above:

```text
H_forward(t) =
      H_field
    + sum_i H_absorber_i(t)
    + H_bath
    + H_capture(t)
    + H_phase(t)
    + H_mark
    + H_route(t)
```

`i` runs over A and B. Every term acts as the identity on all subsystems it does not name.

## Initial state

For the equal-path baseline:

```text
|Psi(0)> =
    (|photon-A> + exp(i theta_in)|photon-B>) / sqrt(2)
    tensor |g_A>
    tensor |g_B>
    tensor |plus-x>_phase-A
    tensor |record-0>_A
    tensor |plus-x>_phase-B
    tensor |record-0>_B
```

Plain English:

- One photon is coherently divided across the two paths.
- Both absorbers are ready.
- Both phase qubits can acquire branch-dependent phase records.
- Both energy-record qubits are blank.

`theta_in` controls the initial path phase. Unequal path weights replace the equal coefficients only after the symmetric model passes all reversal controls.

## Exact global inversion

Suppose the forward evolution runs from time zero to interruption time `tau`. Introduce reverse time `s`, also running from zero to `tau`.

The exact inverse generator is:

```text
H_global_reverse(s) = -H_forward(tau - s)
```

Plain English:

- Replay the entire Hamiltonian schedule backward.
- Reverse its sign.
- Include capture, phase history, record writing, routing, free evolution, and every time-dependent control.

This is the mathematical Loschmidt reversal. It should return the complete state exactly, up to numerical error. It is not claimed to be experimentally available.

## Operational reversal generator

Operational reversal acts in an interaction/control frame where known free phases are compensated. It reverses only permitted controls:

| Forward term | Operational treatment |
| --- | --- |
| Capture `K_i(t)` | Replay with reversed sign and time order |
| Controlled detuning `Delta_i(t)` | Replay with opposite sign |
| Phase-history coupling | Reverse the known/recorded schedule through the absorber control frame |
| Field routing | Replay as the time-reversed recombiner |
| Mark coupling `G_i` | **Not reversed**; continues under the forward physical coupling |
| Record-qubit energy | **Not reversed** |
| Hidden random schedule | Cannot be replayed in the unrecorded branch; use only the preregistered ensemble-wide echo |

One compact bookkeeping expression is:

```text
H_operational(s) =
      compensated free evolution
    - time-reversed H_capture
    - time-reversed controlled detuning
    - time-reversed recorded H_phase
    - time-reversed H_route
    + forward H_mark
    + forward record free energy
```

This expression is deliberately not `-H_forward`. Its failure after record formation is therefore meaningful only relative to the declared operational control boundary.

## Echo/rephasing control

For a static or recorded phase history, choose a midpoint and make the phase-tag coefficient accumulate equal and opposite areas before and after the echo:

```text
first interval:   chi_i × u_i(t)
echo interval:   -chi_i × u_i(time-reversed)
```

Plain English: whatever phase the reversible excitation gained from the known reference before the echo is unwound afterward.

- In the common-reference case, A and B use the same echo.
- In the known-distinct case, each uses its own recorded schedule.
- In the random-recorded twin, the exact random schedule is replayed backward with opposite sign.
- In the random-unrecorded case, the controller does not know the realized schedule and can apply only a fixed ensemble-wide echo.

Because the phase term uses one commuting `Z` tag per absorber, the smallest model records the integrated reference history. Adding more phase qubits later tests noncommuting and multi-collision histories.

## Energy ledger

### During uncontrolled forward intervals

With fixed controls:

- capture exchanges energy between field and reversible excitation;
- the phase tag changes correlations but not bare optical energy;
- mark formation transfers the `e-to-m` energy difference into the record qubit;
- routing moves the photon between equal-energy field modes; and
- the total expectation of the fixed Hamiltonian remains constant.

### During control pulses

Time-dependent detuning, coupling sign changes, and field shaping can perform work. Record that work as a separate control-energy channel. Do not interpret a control-induced energy change as detector gain, bath loss, or violation of conservation.

### Required checks

1. Verify `H(t)` is Hermitian at every time.
2. Verify norm conservation in every forward run.
3. Verify fixed-Hamiltonian energy conservation.
4. Verify the record resonance relation.
5. Verify global inversion restores the initial subsystem energies.
6. Report control work during operational pulses.

## What the generator can establish

- Coherent capture and return in a two-path single-photon state.
- Phase-history entanglement and loss/recovery of accessible interference.
- Direct reversal, echo, and recorded/unrecorded reference comparisons.
- A finite energy-bearing local record and its recurrence.
- Whether one effective return rate adequately describes the microscopic motion.
- Whether recovery observables change near the proposed Paper 2 ratio.
- The exact point at which the standard unitary description stops short of one actual mark.

## What it cannot establish by itself

- Permanent irreversibility from a four-qubit bath.
- A true thermodynamic continuum.
- A microscopic QED derivation of `u_i(t)` or its random distribution.
- Ontic energy shares or the martingale premises.
- One actual registry value rather than A- and B-correlated alternatives.
- Nonlocal loser depletion.
- Born selection without an additional noncircular law.

The state space also forbids more than one optical excitation by construction. A zero simultaneous double-excitation amplitude therefore demonstrates single-excitation bookkeeping, not one-world exclusivity.

## Parameter discipline

Do not select numerical parameters to force a visible cut. Use this order:

1. Set the photon energy as the unit.
2. Enforce the two resonance relations exactly.
3. Calibrate `K` from no-bath coherent exchange.
4. Calibrate `chi` from a target, explicitly declared phase-tag timescale.
5. Calibrate `G` from record-formation and recurrence curves.
6. Sweep detuning and `K` independently when testing the proposed return-to-coupling ratio.
7. Report the full parameter range, including regimes where no single return rate or locking boundary exists.

## Implementation checks before physics plots

| Test | Required result |
| --- | --- |
| Operator shapes and tensor order | Every operator is 576 by 576 and acts on the intended subsystem |
| Hermiticity | Numerical residual consistent with machine precision |
| Forward norm | Constant to integration tolerance |
| No-bath Rabi check | Analytic two-state exchange reproduced |
| Mark-pair check | `e,record-0` and `m,record-1` exchange at the expected frequency |
| Global inverse | Forward followed by exact inverse returns the initial state |
| A/B swap symmetry | Equal inputs and parameters give identical A and B observables |
| Recorded-twin identity | Recorded and unrecorded twins have identical forward evolution before different reversal controls |
| Seed reproducibility | Random schedules and their recorded twins regenerate exactly |

## Recommended implementation files

When implementation is authorized, keep the model isolated from the manuscript simulations:

```text
first_mark_two_absorber/
    model.py          operator construction and H(t)
    controls.py       forward, global-reverse, direct, echo, recorded-twin schedules
    simulate.py       state evolution and interruption-time branching
    observables.py    energy, coherence, recovery, bath-record, recurrence metrics
    verify.py         Hermiticity, norm, analytic limits, inversion, symmetry tests
    README.md         plain-English model and reproduction commands
```

No manuscript claim should cite results from this model until `verify.py` passes and the finite-bath recurrence limitations are reported.

This generator implements the [minimal finite-bath decision](..) and the [reversal protocol](../..).
