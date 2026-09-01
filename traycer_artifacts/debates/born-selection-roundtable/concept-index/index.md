---
title: "Born Selection learning concept index"
kind: spec
---

# Born Selection learning concept index

This was the first user-facing deliverable from the four independent reports. It groups overlapping findings without reproducing the detailed arguments. The cross-review is now complete; the updates below supersede the provisional impacts where they differ.

| ID | Concept tags | One-sentence lesson | Effect on foundational ideas | Independent convergence |
| --- | --- | --- | --- | --- |
| **LC-1** | martingales; Itô calculus; energy conservation | The martingale lemma is useful, but the paper's independent-noise process does not conserve the quantum, so “last surviving share” is not yet the physical event “one site receives exactly ℏω.” | `changes mechanism` for U5; U1 survives if a conserving exchange model can be derived | All four agents |
| **LC-2** | wave realism; local energy; quantum states | A physically spread-out one-quantum wave does not by itself establish that every site possesses a definite classical fraction of its energy; the proposed stakes need an operational definition or microscopic model. | `narrows` U1/U5; does not require collapse or many worlds | Both GPT agents; adjacent concern in Claude's formalism critique |
| **LC-3** | open systems; reversibility; synchronization | A globally contracting equation describes dissipation, while the manuscript calls the return reversible; the κ_ret rate and absence of phase feedback therefore need an explicit absorber–field calculation. | `narrows` U4; U2/U3 remain open | All four agents; Claude correction proposes passivity/no-gain as a possible repair |
| **LC-4** | Golden rule; photodetection; multi-quantum physics | Converting transition amplitudes into rates may reuse Born-rule machinery inside the proposed derivation; the one-quantum rate may have a classical-dissipation repair, while the multi-quantum claim remains conditional. | `preserves` a narrower single-detector U5; `narrows` U6 | All four agents |
| **LC-5** | Bell correlations; conditional probability; measurement update | The entangled extension assumes an exact conditional registry update, so it currently demonstrates consistency with quantum statistics rather than deriving the update mechanism. | `narrows` U7 and tests the no-collapse commitment; does not refute the single-detector game | All four agents |
| **LC-6** | detector efficiency; CHSH; falsifiability | Several proposed experimental signatures require stronger controls because ordinary efficiency or visibility effects can mimic them; the tests remain valuable after redesign and error budgeting. | `preserves` U7 while narrowing evidential claims | Both Claude agents, with related GPT concerns |
| **LC-7** | Dirac equation; spinors; ontology | Paper 1's present stochastic game does not yet derive its capture, exchange, or registry law from Dirac-spinor evolution, so the author's central spinor mechanism is currently unexercised—not disproved. | U2/U3 remain a research foundation requiring an explicit bridge to U4/U5 | Explicit in both critical reviews; compatible with both correction reports |

## Short orientation

- **Strongest mathematical survivor:** if bounded shares really form a terminating martingale, the probability of each winner equals its initial share.
- **Strongest physical gap:** the paper has not yet derived a conserving microscopic detector process realizing those shares and the exactly-one-quantum endpoint.
- **Most promising common repair:** build a conserving sites+field exchange model, derive its boundary behavior and registration law, then determine where Dirac-spinor dynamics enters.
- **Important distinction:** the independent reports challenge whether the proposed mechanism has been derived; they do not establish that wave realism, one-world evolution, or a spinor-centered mechanism is impossible.

## Detailed sources—held behind the index

- [Claude critical review](../round-01/claude-critical)
- [Claude correction architecture](../round-01/claude-corrections)
- [GPT critical review](../round-01/gpt-critical)
- [GPT correction architecture](../round-01/gpt-corrections)

## Cross-review updates

| ID | Final update |
| --- | --- |
| **LC-1** | A conserving Wright–Fisher repair exists, but fairness is not unique to the manuscript's square-root process and discrete fixation needs a new dropout premise. |
| **LC-3** | Narrowed rather than abandoned: κ_ret may govern timescale, while unbiasedness still requires a microscopic drift calculation. |
| **LC-4** | Becomes a conditional single-quantum first-registration theorem; full exclusivity and all multi-quantum extensions remain underived. |
| **LC-6** | The preferred test is in-situ modulation plus simultaneous ordinary-POVM tomography; port swapping alone is not decisive. |
| **LC-7** | Ordinary electromagnetic pointer selection may properly be generic charge/which-path physics. The spinor register remains ontological but should be tested in mass-sensitive channels or a controlled massless comparison. |

See [what changed in Round 2](../round-02/synthesis) and the [final synthesis](../final-synthesis).
