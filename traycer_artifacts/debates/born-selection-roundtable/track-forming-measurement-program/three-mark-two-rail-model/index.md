---
title: "Technical plan: three-mark, two-rail unitary track model"
kind: spec
---

# Three-mark, two-rail unitary track model

## Question the model must answer

What is the smallest closed microscopic model in which one travelling excitation can create three successive partial detector marks, conserve total energy, and display track persistence—without selecting an outcome in advance?

The model is a diagnostic. Its first job is to show exactly what unconditional unitary evolution supplies. It must not claim a one-world track unless the calculation actually produces one without a Born-weighted sampler or conditioned jump.

## Minimal architecture

The state space contains:

- one **nine-state traveller**; and
- six **two-state local mark systems**, one for each rail and detector layer.

The raw state count is therefore 576. This equals the earlier two-absorber model's dimension by coincidence; its factorization and physical purpose are different.

### Traveller positions

| State | Meaning |
| --- | --- |
| Source | Traveller before the first detector layer |
| A1, B1 | Traveller after interacting at layer 1 on rail A or B |
| A2, B2 | Traveller after layer 2 |
| A3, B3 | Traveller after layer 3 |
| Exit A, Exit B | Traveller leaving the model after three possible marks |

### Local marks

The six record systems are A1, B1, A2, B2, A3, and B3. Each begins unexcited and can store one fixed energy deposit. They represent microscopic ionization or excitation marks—not visible droplets, avalanche gain, or an irreversible macroscopic register.

## Generator in plain English

At each layer, a coupling moves amplitude from an incoming traveller state to an outgoing rail and simultaneously excites the corresponding local mark.

Examples:

- Source can move to A1 only while mark A1 is excited.
- A1 can move to A2 while mark A2 is excited, representing straight continuation.
- A1 can instead move to B2 while mark B2 is excited, representing a turn.
- The same pattern repeats at layer 3 and then routes the traveller to an exit.

Every forward interaction has its reverse. The reverse removes the local mark's excitation while returning the traveller to its earlier state. This makes the baseline generator Hermitian and permits an exact global inversion test.

## Track geometry controls

| Control | Role | Status |
| --- | --- | --- |
| Straight coupling | Strength for staying on the same rail at the next layer | Model input |
| Turn coupling | Strength for switching rails | Model input |
| Layer timing | Opens interactions in physical order | Experimental/control analogue |
| Rail phase | Tests coherent interference between alternative histories | Control |
| Local mark gap | Energy stored by each microscopic record | Physical parameter |

Track persistence appears when straight continuation is stronger than turning. That ratio is not yet a microscopic derivation of Mott collinearity; it is an explicit model input to be swept and reported.

## Exact energy ledger

Choose the traveller's energy ladder so each new local mark lowers the traveller energy by the same amount:

| Stage | Traveller energy | Stored mark energy | Total |
| --- | --- | --- | --- |
| Before any mark | Initial energy | Zero | Initial energy |
| After mark 1 | Initial energy minus one deposit | One deposit | Initial energy |
| After mark 2 | Initial energy minus two deposits | Two deposits | Initial energy |
| After mark 3 | Initial energy minus three deposits | Three deposits | Initial energy |

The deposit can be small relative to the initial traveller energy. The model can therefore create a strong history correlation while leaving most energy in the continuing traveller.

No energy is assigned to “the vacuum,” and no remainder is deleted. Any later bath extension must name its energy-bearing degrees of freedom.

## Baseline run sequence

1. Prepare the traveller at the source with all six marks unexcited.
2. Apply equal first-layer couplings so rails A and B are symmetric.
3. Apply layer-2 and layer-3 straight and turn couplings.
4. Propagate to the exit without reading or conditioning on any mark.
5. Report the complete final state by record history.
6. Reverse the segment order and the sign of the complete generator.
7. Verify recovery of the source state and erasure of all six microscopic marks.

The expected unitary result is a coherent state containing several alternative record histories. Conservation and collinearity may be demonstrated, but unique actuality will not have been demonstrated.

## First-mark audit

The output must answer these questions explicitly:

| Question | Acceptable answer in the baseline |
| --- | --- |
| Are A-first and B-first histories both present? | Measure and report their amplitudes; do not silently choose one |
| Does the model enforce one excitation budget? | Demonstrate it through a conserved operator and the energy ledger |
| Is there one actual first mark? | No, unless a new law produces it without conditioning |
| Does zero amplitude at a site remain zero? | Test; do not assume irreversible dropout in a reversible generator |
| Can two alternative record histories coexist in the global state? | Yes; distinguish branchwise exclusivity from one-world exclusivity |
| Are displayed conditioned tracks Born-weighted? | Label them as standard conditioned benchmarks, not model outputs |

## Reversal program

The same architecture must later support all three Paper 2 cases:

| Case | Operation | What it tests |
| --- | --- | --- |
| Exact global inversion | Reverse the full generator and segment order | Whether the closed baseline is truly unitary and energy conserving |
| Echo/rephasing | Reverse accessible phases and structured reference histories, but not every degree of freedom | Whether apparent loss can be recovered with finite control |
| Random reference | Leave local reference phases uncontrolled | Whether operational recovery fails while global unitarity remains intact |

Only exact global inversion belongs in the first implementation ticket. Echo and random-reference cases require the finite bath already designed for the broader reversal protocol.

## Verification contract

The initial implementation should pass at least these checks:

1. All operators have the declared 576-state shape and correct subsystem placement.
2. Every named interaction and the complete generator are Hermitian.
3. Time evolution preserves norm.
4. The fixed-generator energy expectation is constant.
5. The excitation/energy ledger closes at every layer.
6. Equal first-layer couplings preserve A/B symmetry.
7. A one-vertex special case matches the analytic exchange cycle.
8. Increasing the straight-to-turn ratio increases straight-history weight.
9. Both straight and turned histories exist when both couplings are nonzero.
10. The unconditioned final state retains alternative first-mark histories.
11. No check confuses one-excitation conservation with one actual outcome.
12. Exact global inversion restores the source and clears all marks.
13. Reversal works for arbitrary prepared rail phase, not one tuned phase.
14. Recurrence is visible in the finite closed system and labeled as such.
15. Any conditioned-track display is isolated as a Born-conditioned benchmark.

## Interpretation matrix

| Possible result | Meaning | What it would not show |
| --- | --- | --- |
| Several correlated record histories | Unitary dynamics can build track structure and conserve energy | One actual track |
| Strong straight-history dominance | The chosen scattering geometry supports persistence | A derived first-mark Born law |
| Exact recovery | Microscopic marks are reversible in the closed control | Operational recoverability in a macroscopic chamber |
| Failed energy ledger | The generator or level assignment is wrong | New physics |
| Unique history only after conditioning | Standard conditional quantum prediction | Born-free selection |

## Deferred extensions

- Finite phase bath and structured reference histories
- Operational echo and random-reference reversal
- More rails and realistic scattering angles
- Unequal first-layer amplitudes
- Mark amplification and durable visible records
- A candidate ontic share or registry law, considered only after the unitary baseline is understood

## Non-claims

This model will not, by construction alone, prove the Born rule, collapse, one-world exclusivity, Many-Worlds wrong, or the Dirac–Kuramoto selection law. Its value is to separate energy-conserving track formation from the still-unresolved first-mark selection step.
