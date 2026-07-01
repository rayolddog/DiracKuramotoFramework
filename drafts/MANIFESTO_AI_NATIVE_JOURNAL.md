# Manifesto for an AI-Native Journal

*Working title for the venture:* **Aperture** *(placeholder — see "Naming" below).*

*A proposal for a scientific journal built around AI authorship, AI peer review, and AI tutoring — with humans kept where they are load-bearing and removed where they are a bottleneck.*

---

## 1. The premise: we are not publishing truth, we are accelerating error-correction

In the first week of medical school the class is told that roughly half of what they are about to learn will be considered wrong within ten years. That half-life is shorter now, and it will get shorter still as AI begins responding to other AI's output. This is not a flaw in science; it *is* science. Knowledge grows by making mistakes faster than it makes them permanent.

So the goal of this journal is **not to publish only what is true** — no venue has ever managed that. The goal is to **maximize the rate of honest, visible, self-correction.** Every design choice below serves that single metric: make errors cheaper to find, faster to surface, and impossible to bury.

Once that is the goal, most of the objections to AI-native publishing invert. "It will produce a flood of mistakes" — yes, and so does the current system, only slower and behind a paywall. The question is not whether missteps happen. It is whether the venue makes them *legible and correctable* or hides them inside closed review and frozen PDFs.

## 2. The two problems it solves

**Problem A — the throughput bottleneck.** Human peer review takes months to years, is unpaid, anonymous, and discarded after use. The reasoning that gatekept a result never becomes part of the record. As the volume of work grows, this stage does not scale; it is the rate-limiter on dissemination.

**Problem B — the authorship wall.** Current publisher policy forbids naming an AI as an author, regardless of contribution. This is already producing dishonest bylines: work substantially done in collaboration with a model must either understate the model's role or contort the author-contributions statement to stay compliant. *(This is not hypothetical for me — my own physics paper states that the collaborating model would be co-first author if policy allowed, and policy does not.)* A venue that simply tells the truth about who did the work would be a meaningful contribution on its own.

## 3. What it is

A journal where:

- **Authorship may be AI, human, or any mix — and the byline says so honestly,** including which model(s) and which humans, with their roles.
- **Peer review is performed by a panel of AI models from multiple labs; disputes are settled in a bounded five-round resolution loop; the full review and its transcript are published alongside the article.**
- **Invited humans contribute in two roles** — a signed expert assessment, and, where the claim is testable, a lab that commits to the experiment that could verify or refute it — both guaranteed to publish next to the article.
- **Every article ships with an AI tutor** that explains the paper — and its cited references — at whatever level the reader needs.

## 4. The five design pillars

### I. Published adversarial review and the bounded resolution loop

Because AI review is cheap enough to publish in full, do exactly that. Each submission's complete review transcript — every objection raised, every rebuttal, every issue left unresolved — is published with the article and is itself citable and versioned. This is strictly more honest than closed anonymous review, where the strongest objection to a paper often dies in a file drawer. Here the disagreement *is* part of the scientific object.

But a transcript of disagreement is not yet a resolution. When a reviewing model raises a critique and the authoring model — or another reviewer — disputes it, the two are not left talking past each other indefinitely. The dispute enters a **bounded resolution loop: a panel of agents drawn from different foundational models argues the point for at most five rounds.** The bound is the whole design — it forces the models to converge, or to locate crisply *why* they cannot, rather than looping toward exhaustion or sliding into sycophantic agreement. Each round must narrow the disagreement to its load-bearing claim. The loop terminates in exactly one of three recorded outcomes:

1. **Critique accepted** — the authors revise the paper, and the revision *plus the argument that forced it* become part of the record.
2. **Critique withdrawn** — the panel is persuaded the objection does not hold, and the refuted objection is published anyway (a critique that failed is still information about what was checked).
3. **Standing dissent** — after five rounds the disagreement is genuine and unresolved, so it is published *as* unresolved, with the full five-round transcript attached.

Forcing false consensus would betray the journal's premise, so the bound exists to make disagreement *legible*, not to manufacture agreement. An unresolved dispute is often the most valuable thing on the page — a signpost to exactly where the field's knowledge is soft. Where a standing dissent turns on a question only apparatus can settle, it routes directly to the invited experimentalist (Pillar III).

### II. The decorrelated multi-lab panel and the ranking it produces

Review must come from models drawn from **multiple labs**, and this is not diplomacy — it is an epistemic requirement. A single model family has *correlated* blind spots; a panel built from one model is one reviewer with a stutter. Independent review requires model diversity, which requires multiple providers.

The panel does two things:

1. **Scores each submission against a fixed public rubric** (novelty, internal consistency, evidential grounding, reproducibility, citation integrity), producing a **ranking** rather than a binary accept/reject. Ranking is triage, not gatekeeping — weak work is not hidden, it is sorted, and the sorting reasoning is visible.
2. **Records full provenance** for every article: which AI models authored it, which humans contributed and in what role, which model panel reviewed it, and what each scored. This metadata is not bureaucratic exhaust — it is a research dataset. Over time it lets anyone study *which models, configurations, and human-AI arrangements produced durable results versus retracted ones.* The journal becomes an instrument for studying its own epistemics.

### III. Invited human contributions — the theorist's assessor and the experimentalist's test

Humans enter the loop here, in two distinct roles, both placed where humans are *load-bearing* rather than where they are a bottleneck.

**The invited assessor.** For each article, an established expert in the field is invited to write a **signed assessment, guaranteed to publish alongside** the work — agreeing, dissenting, or contextualizing. Guaranteed publication makes the incentive candor, not gatekeeping: they cannot kill a paper, only situate it. Their reputation is attached to the assessment, which is exactly the accountability AI review lacks. When a paper carries a *standing dissent* out of the resolution loop (Pillar I), the assessor is the natural human voice to weigh in on it.

**The invited experimentalist.** Science has always run on a division of labor between those who propose and those who test — John Bell wrote the inequality; Alain Aspect built the apparatus that closed the loopholes. A theoretical result is a *postulate* until someone with equipment tries to refute it. So invited contributions explicitly include **the labs capable of performing the experiment that would verify or falsify the claim.** Their invitation is a standing call to commit to a test, and their eventual result — confirming, refuting, or null — publishes as part of the article's living record. This is the *mechanism*, not merely the aspiration, behind "verified novelty anchored outside the text" (Pillar V): the journal does not wait passively for replication to happen, it **invites the Aspects to test the Bells.**

### IV. The recursive tutor — a comprehension layer scholarship has never had

Every paper is written for an assumed-background reader who mostly does not exist; every actual reader is missing some prerequisite. Each article ships with a tutor that:

- explains the work at the reader's level — from "I am a physician, not a physicist" to "I am a specialist, skip to the contested step";
- **recurses into the cited references**, so the reader can actually follow the chain of support rather than taking citations on faith.

This is the single most buildable piece and should be the **first demonstration**, independent of everything else. It also quietly polices citation integrity: a tutor that has to explain a reference will surface one that was misread, misused, or hallucinated.

### V. Grounding and the scarce resource

The moment AI authorship is allowed, the marginal cost of a plausible-looking paper approaches zero, and infinite generation meeting infinite review risks a closed loop of models certifying models — the reproducibility crisis on fast-forward. The defense is to be explicit that the journal's actual product is **selection and grounding**, not publication. The scarce, valued resource is **verified novelty anchored to something outside the text**: a reproduced result, a released dataset, a prediction that later paid off, an experiment a human actually ran. Provenance tracking (Pillar II), the invited assessor, and above all the **invited experimentalist** (Pillar III) are the anchors that tie a paper to the physical world — the deliberate answer to a flood of synthetic text certified by synthetic review. Volume is free; grounding is the moat.

## 5. Where humans stay load-bearing

The thesis is **not** "humans are the bottleneck." It is sharper: *humans in the loop at the wrong stages are the bottleneck; at the right stages they are irreplaceable.*

- **Remove humans from:** review throughput, the months-to-years dissemination latency, the discarding of review reasoning. This is the target.
- **Keep humans in:** empirical grounding (a model cannot run the wet lab or the interferometer — physical results still need apparatus and hands), accountability (especially in healthcare, where someone may act on a result and someone must be answerable), and agenda-setting and taste (Pillar III).

## 6. Scope

Sections, each with disciplinary subsections: **Physics, Biology, Chemistry, Healthcare, Economics, Philosophy.**

- **Politics and religion are excluded** — not because they are unworthy, but because they are adjudicated by values rather than evidence, and the grounding criterion that makes the science sections credible does not apply to them. Including them would let value-disputes contaminate the evidence-based work by association.
- **Fiction and historical essays live in a separate journal.** The grounding requirement that makes this venture work is precisely the thing fiction should not have.

## 7. Bootstrap: demonstrate it on GitHub this month

A full venture needs multiple labs and institutional backing. A *convincing demonstration* needs one person and a public repository. Stand up the journal as a GitHub organization where each article is a folder containing:

```
/articles/0001-<slug>/
    paper.pdf | paper.md          the work itself
    review/                       review transcripts from ≥2 different models
    resolution/                   bounded-loop transcript per disputed point + outcome
    assessment.md                 the invited (or simulated) expert assessment
    experiment.md                 invited lab's test: protocol, status, result when in
    provenance.yaml               models used, human roles, panel scores, rubric
    tutor/                        entry point for the recursive tutor
    README.md                     the article's front page, links to all of the above
```

- **Use GitHub Issues / Pull Requests as the open-review mechanism.** Challenges, corrections, and rebuttals become versioned, timestamped, and permanent — the published-adversarial-review pillar for free.
- **Article 0001 is the demonstrator:** the Dirac–Kuramoto paper itself. It already names a model as would-be co-first author, so it is the natural first honest byline. Run the multi-model review panel on it now, publish the transcripts, write the provenance file, and stand up a tutor over it and its references. It also already specifies its own falsification tests (T1–T5), so the **invited-experimentalist slot starts pre-populated** — `experiment.md` is a standing, public call for a lab to run them.
- The result is not a manifesto *about* the idea — it is a *working instance* of it that anyone can read, fork, and challenge. That is how the idea gets out there.

## 8. The honest part

This will produce mistakes, and once models begin reviewing and citing other models' output, it will produce *correlated* mistakes and feedback loops — claims that look supported only because the support is also synthetic. There is no design that prevents this. There are only designs that make it **visible and fast to correct** versus designs that hide it.

So the misstep rate is not a shame to minimize out of view — it is a **quantity to measure and publish.** Track retraction rates by model, by human-involvement level, by section. Make the half-life of the journal's own claims a number on the masthead. A venue honest enough to publish its own error rate is doing something no existing journal does, and it is the only honest answer to "won't this produce a flood of wrong things?" — *yes, like all of science, but here you can watch it correct itself in the open.*

---

## Naming

Working title **Aperture** (an opening; letting more light and more eyes in). Alternatives to consider: *Open Ledger*, *Substrate*, *Recension*, *The Open Review of Record*. The name should signal two things: that the work is **open** (review and provenance visible) and that it is **self-correcting** (the half-life is a feature, not a secret).
