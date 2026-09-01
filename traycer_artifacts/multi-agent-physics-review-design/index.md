---
title: "Multi-agent physics review design"
kind: spec
---

# Multi-agent physics review design

## Purpose

Run an adversarial but educational review of the physics program. The review must sharpen or falsify claims without silently rewriting the author's conceptual framework. Every substantive exchange is recorded in English, and every proposed correction declares which underlying idea it preserves, narrows, changes, or threatens.

The approved pilot is:

- **Paper 1:** `DiracKuramotoFramework/drafts/PAPER1_DRAFT_born_selection.md`
- **Pilot objective:** validate the review method before applying it to the remaining corpus.
- **Source rule:** review a frozen, hashed copy; do not edit the working manuscript during review.

The corpus inventory and author requirements are recorded in [Physics Markdown corpus inventory](../physics-markdown-inventory).

## Approved standing perspectives

| Perspective | Primary responsibility | What it protects |
| --- | --- | --- |
| Framework steward and teacher | Faithfully reconstruct the proposal, expose its premises, maintain conceptual continuity, and explain disputes plainly | The author's learning goal and the original intellectual thread |
| Mathematical consistency auditor | Check derivations, definitions, dimensions, limiting cases, normalization, theorem premises, and logical entailment | Mathematical validity |
| Quantum foundations/QFT/relativity critic | Test Dirac/Weyl, measurement, Born-rule, Bell, covariance, locality, and preferred-frame claims against established theory | Correct boundaries with accepted physics |
| Synchronization and open-systems specialist | Test the Adler/Kuramoto mapping, attractors, dissipation, noise, detector dynamics, and classical-to-quantum transfers | Physical legitimacy of the central mechanism |
| Experimental and computational auditor | Reproduce calculations where possible; inspect scales, code, controls, falsifiability, and discriminating predictions | Empirical meaning and reproducibility |

The mediator coordinates the panel but does not erase minority views or average incompatible verdicts. A specialist may be substituted for later side projects—for example, cosmology, nuclear astrophysics, or retinal neuroscience—only with author approval.

## Approved underlying-idea ledger

John M. Bramble approved U1–U7 on 2026-08-24. These are the conceptual commitments that the review must track faithfully:

| Idea ID | Approved statement |
| --- | --- |
| U1 | A real wave or field participates physically in capture and measurement rather than serving only as a probability-calculation device. |
| U2 | Phase may be understood as a physical clock variable, especially in the Dirac/Weyl representation. |
| U3 | Mass coupling between chiral sectors motivates a coupled-clock interpretation. |
| U4 | Closed dynamics yields coherent precession without an attractor; an open, dissipative environment can introduce synchronization or locking associated with measurement. |
| U5 | Detector-site energy shares and a fair stochastic competition may explain Born-weighted outcome selection. |
| U6 | The program seeks a physical interpretation or mechanism while reproducing established quantum predictions wherever it claims equivalence. |
| U7 | Any preferred-frame, nonlocal-registry, or beyond-standard-physics commitment must be explicit, narrowly scoped, and tied to a possible test. |

Reviewers may reject a claim associated with an idea. They may not quietly substitute a different idea under the same label. If a finding threatens a core idea, the final choice is presented to the author with consequences and alternatives.

## Proposed execution profiles — revised for model diversity, pending approval

John has requested model-family diversity because contrasting assessments are themselves part of the learning record. The roster therefore deliberately departs from the current all-Codex review preference. Approval of this table records the desired model assignment only; no agent launch is authorized.

| Perspective | Harness and concrete model | Reasoning | Provider profile | Rationale and independence status |
| --- | --- | --- | --- | --- |
| Framework steward and teacher | `claude` / `claude-fable-5[1m]` | high | ambient authenticated Claude terminal account | Best fit for faithful reconstruction and teaching because the manuscript credits this model family as coauthor. It is an **internal/conflicted** perspective and carries no verdict weight. |
| Mathematical consistency auditor | `codex` / `gpt-5.6-sol` | high | ambient authenticated Codex terminal account | Strong formal and adversarial derivation checking; external to the manuscript's named author-model family. |
| Quantum foundations/QFT/relativity critic | `kilocode` / `kilo/google/gemini-3.1-pro-preview` | thinking | ambient KiloCode account, connection unverified | Adds a Google model family for an independent reading of the foundational claims. This is a concrete current Pro-class catalog entry rather than the older Gemini 1.5 model used previously. |
| Synchronization and open-systems specialist | `claude` / `opus[1m]` | high | ambient authenticated Claude terminal account | Provides a second strong Anthropic model for the central physical analogy; external in model identity but not fully independent of the manuscript's Anthropic authorship ecosystem. |
| Experimental and computational auditor | `grok` / `grok-4.6` | high | ambient Grok terminal account, **currently unauthenticated** | Adds an xAI model family with an adversarial style suited to reproduction and falsifiability. Authentication is required before launch. |

All five would use GUI Traycer agents, `full_access` permission as required by the selection guide, fast mode off, and the `/Users/john-bramble/Projects/Physics` workspace. Review prompts prohibit source edits; `full_access` is an execution setting, not permission to revise manuscripts.

### Availability and diversity limits

- Codex and Claude ambient profiles are authenticated and currently healthy.
- Grok 4.6 is available as a concrete harness model, but the Grok profile is unauthenticated.
- KiloCode exposes `kilo/google/gemini-3.1-pro-preview`; its ambient profile status is unknown and must be tested before launch.
- Qwen is signed out and is not part of this roster.
- The target roster contains five distinct model identities across four model families/labs: Anthropic Fable, OpenAI GPT, Google Gemini, Anthropic Opus, and xAI Grok. Fable and Opus share an Anthropic ecosystem, which is disclosed rather than treated as full independence.
- If Gemini or Grok access cannot be established, launch pauses for an explicit substitution decision; neither role silently falls back to GPT or Claude.

### Access verification — 2026-08-25

- This coordinating agent is confirmed as `codex` / `gpt-5.6-sol`, high reasoning.
- The Claude Traycer provider is authenticated and healthy. An independently opened Claude Code Terminal window is not visible as a Traycer terminal, but it is not needed to create a Claude review agent.
- The Grok Traycer provider remains unauthenticated. An open SuperGrok webpage does not authenticate the Grok harness, and no browser-control connection is currently available to automate that page.
- The Gemini desktop app is not exposed to this session as a controllable agent or browser. KiloCode remains the proposed route to Gemini 3.1 Pro, with connection status still unverified.
- Manual copy-and-paste can include SuperGrok or Gemini as external reviewers, but they cannot participate in automatic agent-to-agent cross-examination unless a Traycer-addressable harness or browser connection is established.

## Input package and independence controls

The pilot package contains:

1. A frozen Markdown manuscript and SHA-256 hash.
2. A manifest identifying the exact version, Git state, date, and included computational files.
3. The author-approved underlying-idea ledger.
4. A terminology and symbol sheet containing definitions only, not defenses of claims.
5. Any code or data directly invoked by the manuscript, with seeds and run instructions.
6. A common reviewer instrument and finding schema.

Round 1 reviewers do **not** see prior AI reviews, author responses, other reviewers' reports, or anticipated-finding ledgers. This preserves independent discovery. Web or repository access must be equalized as far as the selected tools allow and recorded per reviewer. Sources used for technical verification should be primary literature or authoritative references.

The 2026 Born-selection reviews are revealed only after independent findings are frozen. They then become a calibration set: agents identify convergent findings, missed problems, resolved issues, and possible anchoring effects.

## Required finding format

Every finding uses the same record:

| Field | Required content |
| --- | --- |
| Finding ID and location | Stable ID plus section/equation/figure/code location |
| Original claim | Concise statement of what the manuscript actually claims |
| Charitable reconstruction | Strongest defensible interpretation, with premises made explicit |
| Classification | Mathematical error; conflict with established theory/evidence; unsupported inference; missing derivation; speculative extension; terminology/citation issue; numerical/reproducibility issue |
| Severity and confidence | Critical/high/medium/low plus explicit confidence and uncertainty |
| Technical analysis | Equations, counterexample, limiting case, source, or reproduction result sufficient to check the objection |
| Plain-English lesson | What the author should learn and why the issue matters |
| Proposed correction | One or more options, including the option to retain the claim and accept the stated burden |
| Idea impact | `preserves`, `narrows`, `changes mechanism`, `abandons subclaim`, or `threatens core idea`, with affected U-ID |
| Disconfirmation condition | What evidence or argument would make the reviewer withdraw the finding |
| Status | Open, answered, accepted, rejected with rationale, or deferred |

Verdicts do not substitute for this analysis. Numerical scores, if used, remain secondary and are never averaged into a false consensus.

## English discussion and transcript protocol

All participant messages, reports, challenges, replies, and syntheses are written in English. Equations may use standard notation, but each equation-level criticism must have an English explanation.

Substantive cross-agent discussion is recorded as a chronological exchange artifact:

```text
reviews/paper-1-pilot/
  index.md
  inputs/manifest.md
  underlying-idea-ledger.md
  claim-register.md
  round-01/<perspective>/index.md
  round-01/conflict-map.md
  round-02/exchanges/<finding-or-topic>/index.md
  round-02/<perspective>/response.md
  calibration/prior-review-comparison.md
  synthesis/finding-ledger.md
  synthesis/idea-impact-ledger.md
  synthesis/learning-guide.md
  final-synthesis/index.md
```

Each exchange artifact records, in order:

- speaker and perspective;
- question, challenge, or answer;
- evidence cited or calculation performed;
- whether the speaker changed its view;
- which finding and underlying idea are affected;
- unresolved point and who owes the next response.

Raw private reasoning is neither requested nor represented as a transcript. The durable record contains the agents' stated arguments, evidence, objections, replies, and conclusions—the material needed for human review and learning.

## Review sequence

### Phase 0 — Freeze and map

- Freeze Paper 1 and its invoked evidence without editing the working source.
- Confirm the underlying-idea ledger with the author.
- Build a claim register separating established inputs, derived results, interpretive readings, speculative extensions, and predictions.
- Record reviewer tools, source access, model/lab affiliation, and conflicts of interest.

### Phase 1 — Independent reviews

Each perspective reviews the same frozen package without seeing other reviews. It must identify both the strongest contribution and the strongest objection, produce structured findings, and state what would change its mind.

### Phase 2 — Conflict-directed cross-examination

The mediator constructs a conflict map rather than asking every agent to debate everything. Agents address one another directly where they disagree about a load-bearing premise, derivation, physical analogy, or correction. Every substantive exchange is copied into the chronological English record.

The framework steward challenges critics who misstate the proposal. Critics challenge the steward where charitable interpretation masks an unsupported claim. The mathematical and experimental auditors test proposed repairs, not merely the original wording.

### Phase 3 — Prior-review calibration

Reveal the frozen 2026 review record. For each prior finding, the panel records whether it independently rediscovered it, whether the current manuscript resolved it, and whether new evidence changes its importance. Prior verdicts are evidence about review history, not authority.

### Phase 4 — Synthesis and teaching

Produce four distinct outputs:

1. **Finding ledger:** deduplicated technical findings with evidence and dissent.
2. **Idea-impact ledger:** each proposed correction mapped to `preserves / narrows / changes / abandons / threatens`, with U-IDs.
3. **Learning guide:** plain-English explanation of the relevant established physics, the manuscript's move, the objection, and possible repair.
4. **Final synthesis:** strongest surviving claims, failed claims, open questions, discriminating tests, and decisions reserved for the author.

No source correction is applied automatically. If the author later approves revisions, they occur in a separate version with a claim → critique → response → change trail.

## Quality and stopping criteria

The pilot may close when:

- every load-bearing claim in the claim register has been examined by at least two relevant perspectives;
- every critical or high-severity finding has an evidence-backed response and an idea-impact classification;
- mathematical objections have either a checked derivation, counterexample, or clearly stated unresolved burden;
- empirical claims identify controls, parameter scales, and what outcome would distinguish the proposal from standard explanations;
- remaining disagreements and minority views are preserved;
- the learning guide explains the major issues without requiring the reader to infer the debate from scores;
- another cross-examination round is unlikely to change the central conclusions.

The panel may close without consensus. It may not close by hiding disagreement.

## Failure handling

- **Agent stalls or fails:** retain its partial artifact; replace it only if the missing perspective is material.
- **Unequal source/tool access:** disclose the difference and do not treat scores as directly comparable.
- **Citation cannot be verified:** mark the claim unverified; do not convert uncertainty into either acceptance or rejection.
- **Simulation cannot be reproduced:** preserve logs and environment details, classify the failure, and distinguish code failure from physics failure.
- **Conversation becomes repetitive:** mediator narrows the next prompt to the unresolved claim and evidence needed to settle it.
- **Proposed repair changes a core idea:** stop that branch at an explicit author decision gate.

## Remaining approval gates

Before execution:

1. John approves or changes the proposed execution profiles.
2. Grok is authenticated and KiloCode/Gemini access is verified without launching a reviewer.
3. The exact Paper 1 snapshot and evidence package are frozen and their hashes recorded without altering the working manuscript.
4. The mediator presents the frozen manifest and verified profile roster, then requests separate, explicit authorization to launch.
5. Only after that authorization are the five reviewer agents created and the pilot launched through synthesis and the stated stopping criteria.

This document designs the review. It does not authorize launching agents, editing manuscripts, or accepting corrections.

## Pilot launch authorization — 2026-08-25

John authorized a reduced four-agent round table for Paper 1: two Claude Fable 5 agents and two GPT-5.6 Sol agents, split into critical-review and correction-architecture perspectives. The dialogue must remain concise, educational, in English, and durably recorded. The active debate record is [Born Selection four-agent round table](../debates/born-selection-roundtable).

John subsequently clarified that this is not a model competition and that he should not be placed in the role of technical arbiter. The four agents must collaborate toward better concepts, resolve disputes through physics and evidence where possible, and turn unresolved disputes into concise learning and verification paths. The desired measure of success is faster, clearer evolution of the ideas and increased human understanding—not a winning model or aggregate score.
