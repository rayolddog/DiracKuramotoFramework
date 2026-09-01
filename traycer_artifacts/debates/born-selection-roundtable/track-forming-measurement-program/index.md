---
title: "Track-forming measurement program"
kind: spec
---

# Track-forming measurement program

## Purpose

This program pursues two connected deliverables without editing any manuscript:

1. [Candidate revisions for Papers 1–3](paper-update-candidates), concentrating on **Born Selection** and **Heisenberg Cut**; and
2. [A three-mark, two-rail microscopic model](three-mark-two-rail-model) that tests what unconditional unitary dynamics can explain about a particle track before any unique first mark is assumed.

It builds on the [cloud-chamber–SPAD first-mark audit](../cloud-chamber-spad-first-mark-comparison) and the [two-absorber first-mark plan](../two-absorber-first-mark-model).

## Settled design decisions

| Question | Decision | Reason |
| --- | --- | --- |
| Track geometry | Two rails through three detector layers | Smallest geometry that distinguishes straight continuation from a turn and contains three ordered marks |
| Baseline dynamics | Unconditional unitary evolution first | Prevents a Born-weighted trajectory sampler or outcome-conditioned jump from silently choosing the track |
| Editorial mode | Candidate revision artifact | Preserves the active drafts until John reviews the wording |
| Paper scope | Papers 1, 2, and 3; emphasis on Papers 1 and 2 | Paper 1 owns the first-mark selection problem; Paper 2 owns recoverability and the cut at each partial mark; Paper 3 owns the combined taxonomy |

## Central distinction

An **absorptive event detector** and a **track-forming detector** do not perform the same microscopic operation.

| Absorptive event | Track-forming vertex |
| --- | --- |
| The incident excitation is captured and destroyed as a travelling excitation | The traveller scatters or ionizes the medium and continues |
| The event can transfer the entire incident quantum to one detector channel | The event normally transfers only part of the traveller's energy and momentum |
| One capture can seed one macroscopic click | Several partial marks form one track |
| The event ledger ends the incident traveller | The ledger must retain a lower-energy, phase-shifted, deflected travelling wave |

A small energy transfer can nevertheless create a strong which-path record. Measurement strength therefore cannot be identified solely with the fraction of the traveller's energy deposited.

## Scientific boundary

Mott-type multi-atom dynamics can explain why later marks are correlated with an earlier mark. It does not derive:

- which candidate becomes the first actual mark;
- why first-mark frequencies follow the Born weights; or
- why one unitary record history is actual while the alternatives are not.

The three-mark model is designed to make that boundary visible rather than to hide it.

## Status

- Manuscript changes: **none**
- Model implementation: **not started**
- Paper 1 candidate wording: **author-reviewed; not inserted**
- Papers 2–3 candidate wording: **awaiting author review**
- Technical architecture: **ready for ticket breakdown**
