---
title: "01 — Establish the raw-process isolation boundary"
kind: ticket
status: 2
---

# 01 — Establish the raw-process isolation boundary

## Objective

Make it structurally impossible for stochastic event-generation code to load the analytic tongue-rate prediction, comparison machinery, or continuum oracles. Preserve every deterministic result while creating the validated raw configuration boundary used by later tickets.

## Governing artifacts

- [Closed single-channel plan](../..)
- [Pressure-test and closure record](../../pressure-test)
- [Parent two-channel plan](../../..)
- [Ticket sequence](..)

Code boundary: `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/`.

## In scope

- Remove the eager `analytic` import from package initialization while retaining an explicit, documented way to import analytic tools.
- Add the raw-event import boundary and validated raw-configuration types needed by later tickets.
- Define allowed raw dependencies and forbidden modules/names, including analytic rates, amplitude squares, intensities, predictor callbacks, comparison objects, and prescribed hazards.
- Extend AST, import-graph, and runtime-namespace verification to every module transitively reachable from the raw entry point.
- Define the close-marker and hash interface that a future raw ledger must satisfy before any comparison process may open it; actual event and ledger generation remain later work.
- Update package documentation to state which stages remain unimplemented.

## Out of scope

- Random-noise generation, stochastic integration, dwell, commitments, populations, statistical fitting, production runs, or manuscript edits.
- Treating import checks as a security sandbox.
- Staging or committing the currently untracked package.

## Dependencies

None. This ticket starts from the verified 26-check deterministic baseline.

## Requirements

1. `import adler_born_two_channel` must not eagerly load `analytic`.
2. Explicit analytic imports remain possible for deterministic comparison work, without becoming reachable from the raw process.
3. The raw configuration accepts only physical/numerical inputs named in the plan and rejects arbitrary callables or opaque comparison objects.
4. The transitive scanner follows local imports rather than checking only a fixed pair of files.
5. Raw-process modules may use shared physics-free validation helpers but cannot reach analytic, killed-diffusion, bridge-audit, analysis, comparison, or reporting modules.
6. No existing deterministic tolerance is weakened.

## Acceptance criteria

- `python3 -m adler_born_two_channel.verify` passes all 26 existing checks plus the new isolation checks.
- A runtime probe confirms that importing the package and raw entry point does not place analytic/comparison/oracle modules in the raw namespace or module graph.
- Deliberate mutations that add direct, indirect, package-root, or lazy analytic access to the raw graph fail.
- Invalid raw configuration objects fail at the public boundary with named exception types.
- The README accurately distinguishes implemented isolation infrastructure from unimplemented noise and commitment physics.
- No file outside `adler_born_two_channel/` is modified.

## Handoff

Report the exact import boundary, files changed, new checks, canonical command output, unchanged deterministic residuals, and any compatibility compromise. Do not claim stochastic behavior or Born selection.
