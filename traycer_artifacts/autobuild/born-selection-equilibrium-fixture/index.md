---
title: "Autobuild — Born Selection conditional-compatibility diagnostic harness"
kind: story
status: 1
---

# Autobuild — Born Selection conditional-compatibility diagnostic harness

## Purpose

Build and adversarially verify a strictly nonphysical diagnostic harness that exposes circular or unjustified routes from a microstate preparation law and selector to a Born-shaped outcome curve. It must not implement, imply, or serialize a physical Born selector.

## Approval state

Approved by John Bramble on 2026-08-30. Generator/evaluator loop launched for Sprint 1.

## Evaluation path

The evaluator will receive the isolated package and run, at minimum:

```text
python3 -m pytest -q born_selection_equilibrium_fixture/tests
python3 -m born_selection_equilibrium_fixture.verify
python3 -W error -m born_selection_equilibrium_fixture.verify
python3 born_selection_equilibrium_fixture/verify.py
python3 -m born_selection_equilibrium_fixture.verify --prove-failure-exit
python3 -m py_compile born_selection_equilibrium_fixture/*.py
python3 -m compileall -q born_selection_equilibrium_fixture
```

Python 3.12.6 and pytest 9.0.2 are available. The evaluator will also perform independent source inspection, public-API mutation attacks, raw-import isolation checks, manifest replay/staleness attacks, and cleanup verification. No server, account, credential, network service, or external data is required.

## Sprints

| Sprint | Scope | Status | Contract | Verdict |
| --- | --- | --- | --- | --- |
| [01](sprint-01) | Measure-space, dependency, provenance, and fail-closed schemas | In progress | Negotiating | — |
| [02](sprint-02) | Nonphysical selector/control fixtures and raw/comparator firewall | Pending | Not negotiated | — |
| [03](sprint-03) | Blinded compatibility, nonequilibrium, negative-control, and adversarial test suite | Pending | Not negotiated | — |

## Hard boundary

No sprint may claim physical material authority, individual actuality, equilibrium preservation, a Born derivation, or validation of Dirac–Kuramoto dynamics. The maximum result is that the diagnostic harness correctly distinguishes classes of circular and non-identifying fixtures.
