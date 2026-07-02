# Bounded revision plan — fold today's wave-energy / substrate-sampling results into `current_revision_DK_paper.md`

*Date: 2026-07-01. Status: PLAN for approval. Nothing in the manuscript is edited until approved.*
*Backing: `drafts/NOTE_wave_energy_interpretation.md` §7½; `code/born_substrate_sampling.py`, `code/detector_resonance_selection.py`.*

## Goal

Add **concrete computational support** and **one new test** for claims the manuscript already
makes — without changing its published stance. This is a *strengthening pass*, not a new result.

## Hard guardrails (non-negotiable)

- **Stance is preserved verbatim:** "MCI is Born-*compatible*, never Born-*derivative*" (§3.3, §8).
  Nothing here derives Born; nothing upgrades the claim.
- **No rewrite of Appendix D's math.** The 06-30 conditional-trajectory calculation stands as-is;
  we only add pointers in its "not established" list.
- **Do not touch the abstract, §1.3 honesty box, or §3.3** except (optionally) a single citation.
- **Frame everything as support for existing open items,** because the paper already states them.

## The key finding that bounds the scope

Most of today's "results" are **already in the manuscript** — so the revision must present them as
*illustration/support*, not discovery:

| Today's result | Where the paper already says it |
|---|---|
| EM couples to charge `j⁰=|ψ|²`, not to energy `E|ψ|²`; the Born-compatible coupling is gravitational | **§3.7** (vector current vs. `ψ̄ψ=T^μ_μ`), **§8**, Appendix D item 3 |
| Typicality (not basin geometry) is the gap; relaxation-to-equilibrium is the candidate route | **§8 item 1** (verbatim) |
| Born-weight is imported (quantum-equilibrium, Bohm status) | **§3.3** second horn, **§8**, Appendix D item 1 |

**Genuinely new (and hence worth adding):**
1. A **toy model** showing the relaxation-to-equilibrium route can generate the `|ψ|²` weight
   *non-circularly* (squaring from delivered power + random-phase average, not an assumed rate law),
   with **falsifiable non-equilibrium deviations** (`born_substrate_sampling.py`).
2. A **numerical demonstration** of §3.7's charge-vs-gravity claim, closing the equal-energy caveat
   as a consequence of EM (charge) + resonance (`detector_resonance_selection.py`).
3. A **second gravitational test** — the BMV / gravitational-entanglement discriminator —
   complementing §6's gravitational Bell, plus the structural observation that energy-realism is
   empirically identical to standard QM *except gravitationally* (which explains *why* §6 is gravitational).

## Proposed edits (section by section)

| # | Location | Change | Bounding language |
|---|---|---|---|
| E1 | **§8, item 1** (relaxation-to-equilibrium paragraph, ~line 1351) | Add 2–3 sentences: a toy substrate model (`born_substrate_sampling.py`) now shows *how* a random-phase (equilibrium) bulk yields `|ψ|²` frequencies by winner-take-all detection, with the squaring emerging from the delivered **power** (linear drive → `|ψ|²` after the phase average) rather than an assumed golden-rule rate — and that it **breaks** (Born-deviations) out of equilibrium. | "…a concrete illustration of the relaxation route, **not** a discharge of the Born debt; the equilibrium of the bulk is still assumed (the second horn of §3.3)." |
| E2 | **Appendix D, "Not established" list** (items 1–3, ~line 1654) | Append one sentence per item: item 1/2 → point to `born_substrate_sampling.py` as a *candidate* outcome-selection mechanism given equilibrium; item 3 (detector bridge) → point to `detector_resonance_selection.py` showing EM detectors read the charge/which-path basis (`|ψ|²`, `E`-independent), consistent with §3.7. | "…candidate, resting on the assumed bulk equilibrium; still open." Keep all three items marked open. |
| E3 | **§3.7** (after the `ψ̄ψ=T^μ_μ` / gravitational-coupling paragraph, ~line 704) | Add a numerical footnote: `detector_resonance_selection.py` verifies that a resonant EM (charge-coupled) detector reports `|ψ|²` (Born), `E`-independent, while the `E|ψ|²` weighting is recovered only by an energy-coupled (gravitational) readout — so the "does not extend to unequal-energy channels" caveat is a *consequence* of charge-coupling + resonance, not an unexplained limitation. | Neutral, factual; no stance change. |
| E4 | **§6.4** (parameter space / falsification, ~line 1020) *or* a new §6.5 | Add the **BMV / gravitational-entanglement** test as a *second, independent* gravitational discriminator of the wave-energy ontology (a delocalized mass sourcing a mean `E|ψ|²` field → no gravitationally-induced entanglement), and note the structural point that the ontology is empirically identical to QM except gravitationally — which is why every candidate signature is gravitational. | Heavy caveats: semiclassical gravity's known problems; Diósi–Penrose constraints (Donadi 2021); BMV is far-future; **not** load-bearing for the paper's core. |

*(Optional, low priority) E5 — one clause in §7.4 (Penrose–Diósi) noting the wave-energy reading
sits in the same gravitational-source family, so its deviation regime coincides with objective-collapse's.*

## Does this address GPT-5.5's Appendix D concern? (honest)

- The **core** round-2 objection (unconditional Lindblad → maximally mixed, no bistable attractor)
  was **already answered by the 06-30 rewrite** (conditional trajectory; mixture of the two pointers).
- Today's additions **strengthen the residual** (outcome-selection weights, detector bridge) with a
  concrete candidate mechanism and a numerical detector-bridge check — but the **fundamental import
  of the Born weight remains open and openly conceded.** We do **not** claim to have closed it.
- Net: a more complete, better-supported measurement account; **no change to the honest status.**
  A re-reviewer should see added rigor and candor, not new over-reach.

## What NOT to do

- Do not claim Born is derived, or soften "Born-compatible not derivative."
- Do not re-open Appendix D's Lindblad derivation.
- Do not present the BMV test as a framework prediction that *follows* — it is a discriminator of the
  *ontology*, carrying the same gravitational-postulate caveats §6.2/§8 already flag.
- Do not inflate the abstract; if anything changes there, it is at most one citation.

## Execution (once approved)

1. Apply E1–E4 as small, localized insertions (each ≤ a short paragraph).
2. Add a `code/` cross-reference and ensure both scripts are cited where used.
3. Append a revision-log timestamp to `current_revision_DK_paper.md` (date/time only, per preference).
4. Log the change in `discussions/` and, if you wish, note it in `drafts/NOTE_…` §8.
5. Commit (not push) on your say-so.

## Open questions for you

1. **Worth it at all?** Since the paper already states §3.7/§8, the additions are modest. Fine to
   proceed, or would you rather hold until the BMV discriminator is *quantified* (the "how big /
   reachable" calculation) so E4 lands with numbers?
2. **BMV scope (E4):** full new subsection, or a two-sentence pointer in §6.4? (I lean pointer — it
   keeps the paper's one-signature discipline and avoids leaning on contested semiclassical gravity.)
3. **Where should the toy-model figure live** — cited from §8/Appendix D as `code/…png`, or not
   figure-referenced at all (text pointer only)? (I lean text pointer, to avoid implying a result.)
