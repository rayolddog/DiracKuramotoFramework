---
title: "Evaluator critique — Sprint 01 contract proposal r3"
kind: review
---

# Evaluator critique — Sprint 01 contract proposal r3

**Verdict:** acceptable after one narrow final revision. Revision 3 closes every earlier substantive gap; the remaining issue is a caller-controlled authority-shaped string inside the new same-space contract.

## Final required revision

`SameSpaceFlowContract` carries an “invariance predicate identifier” (FLW-02) without constraining its vocabulary. A caller could therefore serialize an authority-inflating identifier even if the emitted `PermittedClaim` remains safe. Make the predicate a fixed constant or a one-member closed enum with the literal value `same_space_measure_invariance_on_frozen_domain`; reject arbitrary strings and authority-shaped alternatives.

Rescope the two equivariance claims so their type and domain boundary is literal rather than explanatory prose:

- `equivariance_tested_nonphysical_fixture_same_space_flow_invariant_for_frozen_domain`
- `equivariance_tested_nonphysical_fixture_same_space_flow_not_invariant_for_frozen_domain`

The existing #6 lacks frozen-domain scope, and both omit `same_space`, which is the exact distinction the separate contract was added to preserve.

## Editorial consistency required in the agreed contract

- Update stale group headings (`MEA 30`, `PRV 20`, `CMP 17`, `RES 15`) and the §6 rubric mapping to include FLW, DEC, SEM, and the appended checks.
- Mark revision 4 as agreed rather than proposed; preserve all prior checks and record that this is negotiation exchange 4 of 4.

No further scope expansion is requested. With these edits, the contract is accepted for implementation.
