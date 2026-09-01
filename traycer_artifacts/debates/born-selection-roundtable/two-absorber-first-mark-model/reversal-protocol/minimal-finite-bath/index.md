---
title: "Minimal finite bath and reversal controls"
kind: spec
---

# Minimal finite bath and reversal controls

## Decision

Use **two bath qubits per absorber**, for four bath qubits total:

- one **phase-history qubit** at A and one at B; and
- one **record/energy qubit** at A and one at B.

This is the smallest finite bath that can keep echo-recoverable phase history physically separate from an energy-bearing material record. One bath degree of freedom per absorber is rejected because the same variable would have to represent both reversible dephasing and durable commitment, building the desired boundary into the model.

The model is an exact, finite unitary control system. It is not yet a continuum bath and cannot establish permanent irreversibility; its recurrences are a feature to measure before enlarging it.

## Minimum state space

| Subsystem | States | Role |
| --- | --- | --- |
| Photon field | Vacuum, photon in path A, photon in path B, and a collected/outgoing mode | Carries the initial two-path wave and names the no-absorption or recovered output channel |
| Absorber A | Ground `g_A`, reversible excitation `e_A`, candidate mark `m_A` | Separates capture from mark formation |
| Absorber B | Ground `g_B`, reversible excitation `e_B`, candidate mark `m_B` | Identical competitor |
| Phase qubit A | Two coherent phase-tag states | Stores the local reference history that may be common, known-distinct, or random |
| Phase qubit B | Two coherent phase-tag states | Independent copy for B |
| Record qubit A | Ground and excited record states | Accepts the energy difference when `e_A` converts toward `m_A` and carries an A-specific record |
| Record qubit B | Ground and excited record states | Independent B-specific record |

The unreduced tensor space has 576 basis states: four field states, two three-state absorbers, and four two-state bath qubits. Symmetry and excitation-number blocks can make the working sector smaller, but the first implementation should keep the full bookkeeping visible enough to audit energy and inversion.

## Why two bath qubits are minimal

| Bath size per absorber | What it can do | Why it is accepted or rejected |
| --- | --- | --- |
| No bath | Coherent capture and direct reversal | Necessary calibration, but cannot represent reference history or a material mark |
| One qubit | Carry either phase history or a record | **Rejected as the complete bath:** it conflates dephasing and commitment if asked to do both |
| **Two qubits** | One phase-history channel plus one independent record/energy channel | **Chosen minimum:** implements all three reference cases and keeps their physical roles distinct |
| Three or more modes | Produce richer spectra, slower recurrences, and more continuum-like dispersal | Deferred to the convergence ladder after the exact minimum works |

## Bath-qubit roles

### Phase-history qubit

The phase qubit interacts dispersively with the reversible absorber excitation. In plain English, its state changes the phase accumulated by `e_A` or `e_B` without consuming the optical photon energy.

In the chosen generator, every phase qubit begins in the same `plus-x` state. The reference history is carried by the prepared real coupling schedule `u_i(t)`, which represents the projection of the background phase onto the absorber's sensitive quadrature:

- the same known schedule at A and B for the common-reference case;
- different but recorded schedules for the echo/rephasing case; or
- independently sampled schedules for the random-reference case.

The recorded twin uses exactly the same sampled schedule as the unrecorded branch; only the controller's access to that information changes. This is a phenomenological phase-history surrogate, not yet a QED derivation of the background field.

### Record/energy qubit

The record qubit begins in its ground state. It couples the reversible excitation and mark sectors so that:

<user_quoted_section>reversible absorber excitation + blank record ↔ candidate mark + excited local record.</user_quoted_section>

Its energy gap is chosen so the exchange closes the microscopic energy ledger. It is not a sink of unnamed “vacuum energy.” Because it is only one qubit, the exchange can recur; operational controls are not allowed to reverse it, while global inversion must reverse it exactly.

The record qubit therefore supplies a **candidate finite record**, not permanent macroscopic irreversibility.

## Minimum interaction terms in plain English

The complete mathematical form and term-by-term explanation are recorded in the [continuous 576-state generator](continuous-generator).

| Interaction | Symbol used in planning | Physical job |
| --- | --- | --- |
| Field–absorber capture | `K_A(t)`, `K_B(t)` | Exchanges the photon in path A or B with the matching reversible excitation |
| Absorber detuning | `Δ_A(t)`, `Δ_B(t)` | Sets the phase accumulated between ground and reversible excitation |
| Phase-history coupling | `χ_A`, `χ_B` | Correlates the reversible excitation with the local phase qubit without transferring the photon energy |
| Mark/record exchange | `G_A`, `G_B` | Converts reversible excitation toward a candidate mark while exciting the local record qubit |
| Free energies | field, absorber, and record gaps | Ensure every transfer has a named energy source and destination |

The two absorbers use identical parameters in the baseline. Asymmetry is introduced only as a later calibration test.

## Chosen absorber controls

### Operational controls

| Control | Allowed action | Used for |
| --- | --- | --- |
| Capture switch/sign | Set each `K_i(t)` to forward, off, or reversed sign | Directly reverse coherent photon capture and collection |
| Detuning inversion | Change `Δ_i` to its negative | Undo known phase accumulation and implement a simple echo |
| Absorber echo pulse | Apply a symmetric pulse that reverses the sign of the phase-history interaction in the toggling frame | Refocus the known phase-qubit coupling without directly manipulating the bath qubit |
| Recorded-phase correction | Apply a precomputed absorber phase shift using only reference information recorded independently of the outcome | Complete common-reference, known-distinct, and random-recorded recovery |
| Field time reversal | Prepare or collect the time-reversed two-path field envelope | Reconstruct the original photon rather than merely returning energy |

Every operational control is applied symmetrically to A and B unless the protocol is explicitly calibrating an imposed asymmetry. No control may ask which absorber appears to be winning.

### Controls reserved for global inversion

The global branch reverses the sign of the **complete** generator, including:

- the phase-qubit free evolution and coupling;
- the mark/record exchange `G_A`, `G_B`;
- the record-qubit free energies; and
- every field and absorber term.

Operational branches may not manipulate the record qubits or reverse `G_i`. This distinction creates a meaningful test of accessible recovery while preserving exact global reversibility.

## Three reference cases in the chosen bath

| Case | Phase-history schedule | Operational sequence | Expected diagnostic |
| --- | --- | --- | --- |
| **Common recorded reference** | A and B use the same known `u(t)` | Reverse capture, invert known detuning, apply one common phase correction, time-reverse the field | Establishes the best operational recovery envelope |
| **Known distinct references** | A and B use different recorded `u_A(t)`, `u_B(t)` | Apply the absorber echo/detuning inversion, then separate precomputed phase corrections, then time-reverse collection | Recovery beyond direct reversal identifies echo-recoverable dephasing |
| **Random unrecorded** | A and B schedules are sampled independently; realized functions hidden from controller | Apply the same ensemble-wide echo and no per-run correction | Tests loss caused by unavailable phase history |
| **Random recorded twin** | Identical random schedules, now logged | Replay the time-reversed schedules and corrections computed from the log; never use outcome information | Distinguishes missing phase knowledge from deeper bath entanglement or inadequate controls |

## Minimal experiment sequence

1. **No-bath control:** set both bath couplings to zero and verify exact capture reversal.
2. **Phase-only control:** turn on `χ_i`, keep `G_i` off, and verify common-reference and echo recovery.
3. **Random-reference twins:** use the phase qubits alone to verify that recorded and unrecorded cases separate as designed.
4. **Record-only control:** set `χ_i` to zero, turn on `G_i`, and map coherent record formation and its finite recurrence.
5. **Full minimum bath:** turn on both roles and repeat all three reference cases.
6. **Two-absorber symmetry:** verify identical A/B energies, recovery errors, and recurrence spectra for an equal input.
7. **Unequal-input control:** alter only the photon splitter after the symmetric reversal protocol passes.

This order prevents a record-coupling error from being mislabeled phase irreversibility and prevents an echo-control error from being mislabeled commitment.

## Measurements required at every interruption time

| Measurement | Purpose |
| --- | --- |
| Complete-state reconstruction after global inversion | Confirms exact unitary bookkeeping |
| Returned photon envelope and phase | Tests recovery of the complex wave, not energy alone |
| A–B interference visibility | Detects whether relative phase history was restored |
| Ground, reversible-excitation, and mark populations | Locates capture, return, and candidate mark formation |
| Phase-qubit correlations | Measures how much reference history left the accessible absorber variables |
| Record-qubit excitation and A/B distinguishability | Measures the local material record and its recurrence |
| Named subsystem energies | Closes the energy ledger at all times |
| Natural recurrence times | Prevents a finite bath from masquerading as permanent commitment |

## Expected finite-bath limitations

- Two qubits per absorber cannot generate a true continuum or irreversible exponential decay for arbitrarily long times.
- A fitted single return rate may fail; oscillatory or multi-rate return is an admissible and informative result.
- The record excitation can recur into the absorber. Any “durable mark” is therefore provisional until recurrence scaling is studied.
- One phase qubit driven by one sampled schedule per absorber tests missing reference information, but not a long noncommuting collision history.
- A successful echo in this small model establishes a control principle, not a claim that a room-temperature silicon detector can be rephased experimentally.

## Convergence ladder after the minimum

Do not enlarge the bath until the four-qubit version passes its unitary, energy, echo, and random-twin tests. Then use this ordered ladder:

| Level | Bath per absorber | Question |
| --- | --- | --- |
| 0 | One phase qubit + one record qubit | Do the three reversal cases work and remain conceptually distinct? |
| 1 | Two phase qubits + one record qubit | Does a longer known/random phase history change echo and recorded-twin recovery? |
| 2 | Two phase qubits + two nondegenerate record qubits | Does record recurrence move later and does return become multi-rate? |
| 3 | Four phase tags + four record modes or collision ancillas | Do recovery curves converge toward stable bath-size behavior? |
| 4 | Controlled spectral continuum | Only now test continuum claims, irreversible limits, and silicon-like spectral densities |

At every level, compare the same physical time window rather than merely waiting until a larger finite bath eventually recurs.

## Implementation fit

The current repository's simulations primarily use NumPy and Matplotlib rather than a specialized quantum package. The 576-state raw model is small enough for exact state-vector evolution and Hermitian eigendecomposition in that style; a specialized package is optional, not required. The implementation should:

- construct tensor-product operators explicitly;
- keep a single source of truth for subsystem ordering;
- test Hermiticity and global inversion before any physics claims;
- exploit conserved blocks only after the unreduced implementation passes; and
- store random phase seeds so the recorded and unrecorded twins are physically identical preparations.

## Acceptance criteria for the chosen minimum

The finite bath is adequate for Rung 1 when:

1. global inversion restores every subsystem to numerical tolerance;
2. common-reference operational reversal restores the original photon;
3. known-reference echo outperforms direct reversal when controlled dephasing is introduced;
4. random-unrecorded recovery differs from its recorded twin without changing forward physics;
5. record-qubit excitation closes the energy ledger and is distinguishable from phase history;
6. finite recurrence is measured rather than hidden; and
7. no outcome sampler or conditioned jump enters any of these results.

This choice implements the [two-absorber reversal protocol](..) and the reversibility variables in the [Papers 2–3 mapping](../../paper3-mapping).
