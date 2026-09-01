---
title: "Ticket 07 fix-up — close R1 documentation and criteria findings"
kind: ticket
status: 2
---

# Ticket 07 fix-up — close R1 documentation and criteria findings

## Objective

Close the three findings from the reconstruction-baseline R1 independent
review without adding, authorizing, or presenting Ticket 08 work.

## Required changes

### Remove the residual Ticket 08 presentation

- Remove or correct README statements that present seven Ticket 08 checks or
an implemented `production.py` gate. The live package has 127 Ticket 01–07
checks, criteria 1–121, no `production.py`, and Ticket 08 remains status 0.
- Remove the stale verifier source comment that describes an absent Ticket 08
import/seal route.
- Add a live-current-fact regression that fails if user-facing package text
again presents an implemented Ticket 08 gate, its seven checks, or
`production.py` while those surfaces are absent.

### Align criteria 110 and 118 with the accepted contract

- Criterion 118 must describe one unpriced intended-configuration outline and
one priced machinery-only diagnostic, not “both costed alternatives.”
- Criterion 110 must describe the closed vocabularies the Ticket 07
experiments layer actually owns and can enforce; it must not claim an
absent Ticket 08 production gate.
- Strengthen the covering checks so changing or extending any closed
Ticket-07 vocabulary named by criterion 110 is detected, and so the
Option-A/Option-B framing required by criterion 118 is mechanically pinned.
Criterion-number presence alone is not sufficient evidence.

### Correct and enforce budget ownership

- Correct `raw_runner.py` so Ticket 07 alone is identified as freezing the
production numerical budget; Ticket 08 neither co-owns it nor exists as an
implemented stage in this reconstruction.
- Route the actual co-ownership wording and reasonable whitespace/paraphrase
variants through the same discovered live-source validator so the stale
claim cannot pass by rewording.
- Preserve the truthful, separate statement that production-status schema v4
does not yet exist.

## Non-regression boundary

Preserve the closed fixture-plan work, all 127 checks and criteria 1–121, the
527/1,383/1,278 public-surface census unless a justified source-visible change
requires an explicit update, the scientific `numerical_no_result` boundary,
schema-v3 fail-closed behavior, Option A unpriced, Option B at exactly 18 runs
and 29,268 rows, no pilot/campaign/production activity, and Ticket 08 status 0.

## Acceptance

A fresh independent reviewer must return strict `CLOSED` on all three R1
findings, with the full quiet serial verifier/compile matrix and cleanup green.
The separate round-10 dynamic/line-wrapped prose limitation is not silently
reclassified unless this change explicitly and demonstrably closes it.

## Implementation record — awaiting independent review

Implemented in `verify.py`, `README.md` and `raw_runner.py`. Full evidence is in
the [Ticket 07 execution notes](../execution-notes), section *R1 documentation*
*and criteria closure — three findings, three mechanisms*. **Status stays 1**:
this records what was built, not a closure verdict.

All three findings were reproduced on the prior bytes first — every prose guard
clean over the README residue, a rogue `FEASIBILITY_VERDICTS` member leaving
`check_experiments_isolation` passing, and the `raw_runner.py` co-ownership
sentence passing both prose guards.

- **Ticket-08 residue.** README now states there is no ticket-08 production
gate, `production.py` does not exist, no check covers one and the criteria
stop at 121; the stage-table row says `**not implemented**`; the stale
`verify.py` import comment is gone. Enforced by three new current facts with
both spellings through the mutation loop, four new meaning-based stale
patterns, and asserted absences (no `production.py`, no module importing
`production`, criteria max 121).
- **Criteria 110 and 118.** Both texts corrected to what is actually enforced.
`check_experiments_isolation` now pins sixteen closed vocabularies member for
member, each exercised by an added, removed and reordered member against
copies. `check_checkpoint_handoff` pins the one-unpriced / one-priced
`ALTERNATIVE_CONTRACT` and proves it with four alterations.
- **Budget ownership.** `raw_runner.py` now credits ticket 07 alone; a new
current fact plus three ownership patterns and eleven two-directional control
sentences — including four line-wrapped variants — enforce it. The distinct
truthful schema-v4 absence statement is preserved.

**Round-10 P2 is half closed and stated as such**: both validators now fold
whitespace, so the line-wrap half is closed and independently demonstrated; the
runtime f-string construction half is untouched and that finding stays open.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]` (the deliberate probe), both compile passes clean,
`results/` absent throughout. Census unchanged at 127 checks, criteria 1–121,
527 / 1 383 / 1 278.

New hashes: `verify.py`
`cd706adf77799242083dcc183367c348d70b754eb8083e42184ee612e4d51275`,
`README.md` `aebefcbc4f901c894f0765f9e8c5f3baba846f8a91d09f8861e08fc602a43fc9`,
`raw_runner.py`
`ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b`;
`experiments.py`, `compare.py`, `__init__.py` and `raw_config.py` byte-identical
to the R1 baseline.

## Implementation record, round 2 — the re-review's two P1 escapes

Implemented in `experiments.py`, `verify.py` and `README.md`. Full evidence is
in the [Ticket 07 execution notes](../execution-notes), section *R1 re-review*
*closure — checkpoint authority, and ownership by meaning*. **Status stays 1**
pending the fresh independent re-review.

Both escapes were reproduced on the frozen reviewed bytes first: the directly
constructed `Checkpoint1Handoff` presenting Option B's 11.3 h / 28 836 rows as
the approved pilot's 32.1 h / 81 840 (with `dataclasses.replace` and a subclass
equally accepted), and the singular reversed plant `ticket 08 jointly owns the production numerical budget` in `__init__.py` passing both prose guards.

- **Checkpoint authority.** `Checkpoint1Handoff` is now factory-only under
`_CHECKPOINT_SEAL`, checked last so every existing field rule stays
separately reachable. `_require_authoritative_checkpoint` rebuilds a handoff
from its own components through `checkpoint_one_handoff` and compares field
for field and digest for digest, refusing a subclass by exact type;
`_require_unchanged_checkpoint` is the post-freeze door. Both are private, so
the exported surface stays at 527. The factory remains the sole authority and
still derives the pilot line from `pilot_cost_from_plan` and both
alternatives from `checkpoint_alternatives`; it takes no `pilot_line`,
`alternatives`, `requested_decision`, `seal` or ticket-08 state parameter.
Regressions cover every other cost line in the evidence at both the
construction and the rebuild door, plus replace, subclass, reordered
alternatives, a friendlier feasibility, and the unchanged-digest door.
- **Ownership by meaning.** `_budget_ownership_claims` folds whitespace and
searches three orders over declared subject and ownership-verb sets,
discarding negated windows so true denials still pass.
`_ownership_prose_problems` runs it over the discovered live set and **both**
prose checks call it. Twenty-four control sentences run both directions,
including the review's exact plant, eleven paraphrases, three line wraps,
three negated forms and two schema-v4 controls; the plant is also made in
three real discovered modules.

**Census moved by design:** the `seal` field is one probed parameter, so the
pinned numbers are now **527 / 1 384 / 1 279** and the README was updated to
match. Checks stay 127 and criteria 1–121.

**Round-10 P2 remains OPEN** for runtime f-string construction; this round does
not close or reclassify it.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]` (the deliberate probe), both compile passes clean,
`results/` absent throughout. Option A unpriced, Option B 18 runs / 29 268
rows, proposal `checkpoint_blocked`.

New hashes: `verify.py`
`e62f69e952301e86e14f75cda077c77fd99dfdd3a6acc01ee0d0c44fcf973c56`,
`experiments.py`
`35de6a27599986a3d2032a3e76a3334c4f127240a9b20e996516ba70c67d01ba`,
`README.md` `ad710e8031fee05096fdfa445c97ff1e2b4604727380e9cc7c4c26c2fb8c989f`;
`raw_runner.py`, `compare.py`, `__init__.py` and `raw_config.py` unchanged this
round.

## Implementation record, round 3 — the alignment review's seal finding

The round-2 checkpoint repair was insufficient and the alignment review was
right: `_CHECKPOINT_SEAL` is ordinary module state, so a caller reaches it,
builds the forgery, and calls the public `summary()` without presenting the
record to the private rebuild door. Both findings are now closed structurally.
**Status stays 1.** Full evidence in the [execution notes](../execution-notes),
section *Alignment re-review closure — the seal was not the answer*.

- **Nothing left to substitute.** `feasibility`, `alternatives` and
`pilot_line` are no longer fields; they are derived properties computed from
the components on every read. The record carries `plan` and `campaign` so
those derivations have their inputs, and binds every derivation input to the
canonical proposal at construction — eight component digests plus the
numerical verdict and ordered blockers, with `require_plan_firewall` beside
them. The alignment review's exact route now yields
`TypeError: got an unexpected keyword argument 'pilot_line'`, and a record
built through the reachable token, shown to no door, presents the frozen
plan's own 32 h / 81 840 rows. The seal and
`_require_authoritative_checkpoint` remain as defence in depth, explicitly
not as the defence.
- **Negation scoped to the relation.** `_budget_ownership_claims` cuts at the
last clause boundary before the ownership verb and searches only that clause.
`ticket 08 is not implemented but jointly owns the production numerical budget` is now caught; `ticket 08 does not own the production numerical budget` still passes. Ten new controls, six affirmative-after-negation
(one line-wrapped) and four true denials; the schema-v4 controls are
unchanged.

**Census moved again by design:** three derived properties are three new public
surface entries and the constructor lost three parameters and gained two, so
the pinned numbers are now **530 / 1 383 / 1 278**. README updated; checks 127,
criteria 1–121.

**Round-10 P2 remains OPEN** for runtime f-string construction.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]` (the deliberate probe), both compile passes clean,
`results/` absent throughout. Option A unpriced, Option B 18 runs / 29 268
rows, proposal `checkpoint_blocked`.

New hashes: `verify.py`
`5c4bf7f9d5b28121a3c7e19b3d9eca4f954afeaa82992fa80bc8ec7762455e77`,
`experiments.py`
`f90abbe955793a2711cb68cf7283df168cb1353343adf345ccab9238aac198d1`,
`README.md` `50f07413cf1a0f56c6f6789db0e632cf9eeafd480923428004c67eef8df5bb31`;
`raw_runner.py`, `compare.py`, `__init__.py`, `raw_config.py` unchanged.

## Implementation record, round 4 — the derivation inputs

The outputs were derived; two inputs they read were still caller-controlled and
the class docstring claimed otherwise. Both closed. **Status stays 1.** Full
evidence in the [execution notes](../execution-notes), section *Second*
*alignment closure — the derivation inputs*.

- **The benchmark is bound.** The slowest supplied benchmark must equal
`proposal.value("benchmark_digest")`, checked at construction — the binding
loop had listed eight components and omitted the one that prices the pilot
line, Option B and the presented rate. A slower foreign benchmark is refused
alone and beside the frozen set. For the rest of the tuple the proposal
freezes nothing, so nothing is claimed: what is asserted and tested is that
the only two values an extra measurement can move are maxima, so a supplied
benchmark can make the evidence more conservative and never more favourable.
`summary()` now carries `authoritative_benchmark_digest` and
`supplied_benchmark_digests`.
- **The campaign is gone.** Option A derived from a caller-supplied
`ValidationCampaign` that the 86-field proposal does not freeze. Rather than
invent a self-consistent caller digest, `campaign` was removed from
`Checkpoint1Handoff`, `checkpoint_one_handoff`, `checkpoint_alternatives` and
`intended_configuration_option`, which now takes nothing. The stage count was
the only caller-dependent element of Option A's text. The frozen proposal
contract is untouched and `_t07_campaign()` keeps its own checks.

**Census:** 530 callables unchanged; invalid calls 1 383 → **1 380**;
parameters 1 278 → **1 274**. README updated; checks 127, criteria 1–121.

**Round-10 P2 remains OPEN** for runtime f-string construction.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]`, both compile passes clean, `results/` absent throughout.
Fixture-plan attacks and the relation-scoped ownership fix preserved and green.
Option A unpriced, Option B 18 runs / 29 268 rows, proposal
`checkpoint_blocked`.

New hashes: `verify.py`
`95bfe576230ca72af9b970ddce73f64e70ac0461575773c0c04d17c9876e9056`,
`experiments.py`
`460c9a850743282297904990e63451e97f5e167a22a4504350110f0a6c96d77f`,
`README.md` `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9`;
`raw_runner.py`, `compare.py`, `__init__.py`, `raw_config.py` unchanged.

## Implementation record, round 5 — live-documentation cleanup

Removing the campaign route left four stale claims in `experiments.py` — live
API help describing a parameter and a field that no longer exist. All four
corrected and guarded. **Status stays 1.** Full evidence in the
[execution notes](../execution-notes), section *Live-documentation cleanup —*
*four stale campaign claims*.

- `intended_configuration_option`, `Checkpoint1Handoff.alternatives`,
`checkpoint_one_handoff` and the `_require_authoritative_checkpoint` refusal
message now say Option A is the fixed no-input unpriced record and Option B
derives from the bound matrix, the authoritative benchmark, the numerical
disposition and the safety factor. The `alternatives` docstring states why
there is no campaign clause to bind rather than leaving it inferred.
- `_campaign_claim_problems` reports any live sentence naming a checkpoint
subject, a campaign and a declared relation between them without a negator.
It runs in `check_stale_stage_strings` over the discovered source set beside
a structural assertion that the field and all three public signatures are
campaign-free. Each of the four corrected claims was restored and required
to be caught; twelve controls run both directions, including the exact
`derived by …` shape of the refusal message, one line-wrapped claim, and two
sentences from the separate planning machinery that must pass.
- `ValidationCampaign` and its own documentation are untouched and truthful.

**Census unchanged** at 530 / 1 380 / 1 274; 127 checks; criteria 1–121. This
round changed prose and added a guard, not surface.

**Round-10 P2 remains OPEN** for runtime f-string construction.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]`, both compile passes clean, `results/` absent throughout.
All earlier closures preserved and green.

Final seven: `verify.py`
`0732ca7643f26c047f45848472f92ba8cb1da06d640c06a9c7f9551dffd8b20f`,
`experiments.py`
`6f8e79a869c9b49ea29c6193a170900c555294b33bb42a8156f50464a4481b25`,
`README.md` `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9`,
`compare.py` `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817`,
`__init__.py` `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a`,
`raw_runner.py`
`ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b`,
`raw_config.py`
`eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430`.

## Implementation record, round 6 — the record itself is slotted

The derived properties closed what a caller could *supply*; nothing closed what
a caller could *attach*. `Checkpoint1Handoff` was frozen but not slotted, so
`object.__setattr__(h, "summary", ...)` shadowed the method and the authority
door returned the poisoned object. **Status stays 1.** Full evidence in the
[execution notes](../execution-notes), section *Slotted checkpoint — the record*
*itself could be poisoned*.

- **`@dataclass(frozen=True, slots=True)`** — no instance dictionary, so no
undeclared attribute can exist and no method or property can be shadowed.
The review's exact assignment now raises `AttributeError: … 'summary' is read-only`.
- **`_require_authoritative_checkpoint` returns its own rebuild**, never the
supplied object, so the boundary cannot forward caller behaviour even if a
future class change reintroduced state.
- **`_require_no_undeclared_state`** asserts exact type and the absence of an
instance dictionary; both doors call it.
`_require_unchanged_checkpoint` still returns what it was given — a digest
is not a set of components — and that rule is what makes it safe.
- Regressions: `__slots__` equals the declared field set exactly; nine
individual shadow attempts each required to raise; the review's exact
poisoned-summary case; a subclass with a dictionary whose shadow is shown to
take effect, refused at all three doors; `dataclasses.replace`; the reachable
seal; and the authority door asserted to return a different, exact-typed,
identically hashing, dictionary-free record.

**Census unchanged** at 530 / 1 380 / 1 274; 127 checks; criteria 1–121. Slots
add no public surface and the new door is private.

**Round-10 P2 remains OPEN** for runtime f-string construction.

Quiet strictly serial matrix under exclusive ownership from an absent
`results/`: 127/127 exit 0 on the four real invocations, 127/128 exit 1 with
exactly one `[FAIL]`, both compile passes clean, `results/` absent throughout.
The `-W error` invocation took 3 833 s against ~283 s for the others under a
load average of 14.9; the result was identical and the anomaly is recorded as a
machine observation, not a cost claim. All earlier closures preserved and
re-confirmed.

Final seven: `verify.py`
`259f2f864070989cc524c0499e1a7b8ef03f6a7973a8b579d775244774fa11c5`,
`experiments.py`
`b2672e0ff226ef48f073cb31176b656d301ec37f24fa13d28f027586bb68afeb`,
`README.md` `76fd5cc1c1570de81c622c98c2cf10629166f4b0908ef3d009912f38b0ca20f9`,
`compare.py` `abc89474b14d04f68bc21a4e61b9322c85847cd50152254a8ed6823062620817`,
`__init__.py` `9f05ee02d0c2e0c2fd0669b9d555b11408d88e7aae95dc2fc7a8301d59fe240a`,
`raw_runner.py`
`ee13e099c22bc7b492fb7439653a69cf5d4637aaa181571bf947706ba6442a2b`,
`raw_config.py`
`eb59d1971f74f772a2b8ccb21d20b363573e51bf2dd57b5a260645cf815d5430`.

## Independent closure

**Strict verdict: CLOSED.** The final independent review replayed the exact
poisoned-`summary` attack, reachable-seal construction, slot mutation,
subclass-with-dictionary, direct cost injection, `dataclasses.replace`,
foreign component and benchmark substitutions, and all earlier R1 prose and
criteria attacks. No actionable finding survived.

`Checkpoint1Handoff` is now an exact-type frozen slotted record with no
instance dictionary; every attempted method/property shadow is refused. The
authoritative checkpoint door returns a fresh factory rebuild rather than the
supplied object. The review also reconfirmed the Ticket-08 documentation,
criteria 110 and 118, benchmark provenance, campaign removal and live-doc
guard, budget ownership and relation-scoped negation, fixture-plan authority,
schema-v3 fail-closed behavior, and the unchanged scientific no-result
boundary.

The independent serial matrix passed canonical, verbose, direct-file and
`-W error` invocations; the deliberate-failure path exited 1 with exactly its
one expected failure; `py_compile` and `compileall` passed; and `results/` was
absent afterward. The verified census is 127 checks, criteria 1–121, 530
public callables, 1 380 invalid calls and 1 274 parameters.

Review evidence: [Ticket 07 independent review](../independent-review), final
artifact SHA-256
`3df53d73263327a42d82788f86f1a5c2e8ce6370eca4e938b6c9ab9dac82220e`.

The separate round-10 dynamic-f-string prose limitation remains explicitly
OPEN and outside this R1 closure; it was not reclassified.
