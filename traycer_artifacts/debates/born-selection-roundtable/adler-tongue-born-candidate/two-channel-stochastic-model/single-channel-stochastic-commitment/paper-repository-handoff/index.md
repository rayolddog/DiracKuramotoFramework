---
title: "Born Selection repository test-suite handoff"
kind: spec
---

# Settled intent

After the remaining implementation tickets are closed, include the cumulative test suite and its reproducible results in the repository that contains the Born Selection paper.

Do not split or relocate the active suite while later tickets are still extending it. The final handoff should preserve one authoritative executable suite and add enough durable context to reproduce and audit the results.

## Final handoff contents

- The cumulative source and verifier currently developed under `adler_born_two_channel/`.
- A ticket-to-check manifest covering every closed ticket, including the Ticket 01–03 checks already retained in the cumulative verifier.
- Exact commands, supported Python/dependency versions, and an environment manifest.
- Machine-readable final results plus human-readable summaries, with checksums and clear dates.
- The independent closure disposition for every ticket and an explicit list of scientific non-claims.
- A clean repository state: no dependence on temporary files, command logs, or Traycer-only paths for reproduction.

## Timing

Perform this packaging after the remaining tickets close, so the archived suite and results describe the final scientific contract rather than an intermediate checkpoint.
