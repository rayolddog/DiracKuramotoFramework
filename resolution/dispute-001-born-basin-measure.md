# Dispute 001 — Do the synchronization dynamics reproduce Born weights?

- **Disputed claim:** That the framework's measurement dynamics are *consistent with* the Born rule in a non-trivial way. Taken seriously as an Adler/Kuramoto basin-of-attraction story, outcome weights are fixed by the geometry of the locking basins and the invariant measure on background configurations — which has no evident reason to equal |α|².
- **Raised by:** Fable 5 (Reviewer A), Major Concern #2 — pressed as the highest-leverage objection. Independently corroborated by Gemini 3.1 Pro (Reviewer B, §3.7 chirality route) and GPT-5.5 Thinking (Reviewer C, Q3 + Major Concern #2). **Three decorrelated labs, one objection.**
- **Defended by:** the manuscript, which treats the Born measure as an acknowledged open problem (§3.3, §7.3, §8) — reframed for equal-energy channels, not derived.
- **Status:** ✅ **RESOLVED — critique accepted (with a commissioned calculation)**, plus a **standing dissent on significance** (see Outcome). Run 2026-06-25.

---

## ⚠️ Honesty note on this loop's status (read first)

A *fully autonomous* cross-lab loop is not something this environment can run: it would require live calls to OpenAI and Google models, which are not available here. This loop is therefore run in the **highest-integrity form available**, and its provenance is stated plainly:

- **The parties' positions are real, not ventriloquized.** Each is quoted or faithfully paraphrased from that reviewer's *on-record report* in [`../review/`](../01-original-submission-and-review/review/). No model's view is invented.
- **The deciding move is a reproducible, lab-independent calculation** — [`dispute-001-basin-measure.py`](dispute-001-basin-measure.py) (numpy only; ~4 s). Arithmetic does not depend on which model runs it, so the facilitator's family does not bias the result.
- **Facilitation/synthesis is by Claude Opus 4.8** (Anthropic), disclosed. Claude does not get a vote that overrides the other labs; it commissions the calculation and reports where the numbers land.
- **Open continuation:** a genuine cross-lab *re-challenge* of the calculation (does any OpenAI/Google agent dispute the model or its reading?) is the remaining step, runnable by pasting this file + the script through other-lab subscriptions — exactly how Reviewers B and C were obtained.

So: positions = genuine 3-lab; decision = computation; facilitation = Claude, disclosed. Not a dress-up of same-family agents as "the OpenAI agent" — that would betray the decorrelation principle this journal is built on.

---

## The fork (why this is decidable, not merely "open")

Reviewer A sharpened "Born is unsolved" into a concrete fork:

1. **Measure derived from the dynamics** → then compute the basin measure for the simplest two-outcome Adler model. If it yields basin-area / equal weights rather than |α|², the framework is *internally falsified at the level of statistics* (**Horn 1**).
2. **Measure an independent postulate tuned to |α|²** → then the synchronization machinery does no work for the statistics, and the honest statement is that the dynamics explains registration/irreversibility while Born weights are imported by hand (**Horn 2**).

The manuscript currently sits between these; the loop forces it onto one horn.

---

## Round-by-round (≤5)

### Round 1 — claim stated, three-lab convergence confirmed
The objection is not one reviewer's idiosyncrasy. Verbatim from the record:
- **Fable 5 (A):** "In an Adler/Kuramoto system the locking basins are *concrete objects with computable measures* … there is no evident reason for that to equal |α|²." Predicts Horn 1 ("my expectation: it gives basin-area or equal weights").
- **GPT-5.5 (C), Q3:** "Why should basin measure equal |α|² rather than geometric basin volume?"
- **Gemini (B):** reaches the same gap from §3.7 — the lock is non-demolition for position, not for the chiral scalar, so the prepared weight is *erased*, not carried.
- **Manuscript (defense):** §7.3 already concedes an unbiased background "would … weight basins by their measure (tending to equal odds) rather than by |α|²"; §8 names the Born measure an open problem. The defense is *not* "the dynamics derives Born" — it is "equivariance carries a |α|² measure granted at preparation."

➡ *Narrowed to:* what is the basin measure of the minimal two-outcome Adler model, and can any non-tuned choice yield |α|²?

### Round 2 — commission the calculation
Per the routing note, the loop commissions the computation rather than terminating in talk. Model (the manuscript's own `RESULTS_PHASE_DISSIPATIVE`): the measured-channel dissipator `D[σx]` reduces to the **second-harmonic** Adler equation `dφ/dt = Ω − γ sin 2φ`, bistable at the pointer phases 0 and π. The prepared amplitude **α does not appear in this equation** — that absence is the whole question.

### Round 3 — the result (lab-independent)
From [`dispute-001-basin-measure.py`](dispute-001-basin-measure.py), figure [`dispute-001-basin-measure.png`](dispute-001-basin-measure.png):

| Test | Result |
|---|---|
| **(A)** Ω = 0, uniform background | **P(basin 0) = 0.500** (analytic basin areas π : π) |
| **(B)** sweep prepared weight \|α\|² ∈ {.05,.25,.5,.75,.95} | dynamical fraction **flat at 0.500**; matches Born only at \|α\|²=0.5; **max disagreement 0.45** |
| **(C)** vary apparatus detuning Ω/γ ∈ [−0.8, 0.8] | **still 0.500 for every Ω** — wells and barriers shift together, basins stay equal-width |
| **(D)** add first-harmonic bias ε·sin(φ−Φ_bulk) | split moves off 0.5 (0.50 → 0.53 → 0.57 → 0.60) — but tracks **ε and Φ_bulk** (the bulk reference), **never α** |

➡ The geometry gives **50/50**. It is *flat* in |α|² and *robust* even to apparatus detuning. The only knob that breaks 50/50 is the first-harmonic bias toward the bulk reference — an apparatus property, with no dependence on the prepared α.

### Round 4 — which horn? (a precision the reviewers' framing left open)
The result lands on **Horn 2, not Horn 1** — and the distinction is load-bearing:
- It is **not** true that the dynamics *predicts an observable 50/50 contradiction* (the strong "internally falsified" reading). The outcome weight is whatever measure you place on the initial phase / background; the dynamics is **silent** on that measure.
- It **is** true that the dynamics *does not derive Born*. To get P = |α|², the initial-condition measure must already encode |α|² — i.e. Born is imported by hand, the **quantum-equilibrium move, identical to Bohm's hypothesis** (exactly Reviewer C's "decoherence plus hidden variable, unspecified").

So GPT-5.5's strong phrasing ("predicts the wrong statistics") is itself *reduced* by the calculation: the framework is not falsified, it is **non-predictive about weights** without an added measure postulate. Fable 5's Horn 2 is confirmed.

➡ *Narrowed to the one irreducible question:* is "imports Born as a quantum-equilibrium measure, like Bohm" an honest open problem (→ major revision) or a disqualifying non-result (→ reject)?

### Round 5 — the irreducible disagreement
This last question is **not factual** — the calculation cannot settle it. It is a judgment about *significance and venue*:
- **Fable 5 + Gemini (major revision):** importing Born as a measure is the standard status of every ψ-ontic single-world theory (Bohm included); the framework's registration/irreversibility account still has value as a foundations contribution, *provided* it states Horn 2 explicitly and drops any suggestion the synchronization does work for the statistics.
- **GPT-5.5 (reject):** "the proposal has not advanced beyond decoherence plus hidden variable, unspecified"; without a selection law and a Born-measure proof it is not a worked theory.

There is one *factual* sub-question that could still move this: **can a sub-quantum dynamics relax an arbitrary background measure to |α|² (a Valentini-style H-theorem)?** The bare deterministic Adler flow does **not** (uniform measure → a fixed 50/50, no relaxation toward |α|²), corroborating Reviewers B/C Concern #4. Whether a *stochastic, mixing* extension exists with |α|² as its unique stationary measure is unproven and is genuine future work.

---

## Outcome

**Primary outcome: CRITIQUE ACCEPTED (with a commissioned calculation).**
The synchronization dynamics do **not derive the Born weights**. The minimal two-outcome Adler model gives basin areas 50/50, flat in |α|² and robust even to apparatus detuning; the only knob that breaks the symmetry tracks the bulk reference, not the prepared amplitude. The framework's consistency with Born survives **only on Horn 2** — by importing |α|² as a quantum-equilibrium measure on background configurations, exactly as Bohmian mechanics does, with the synchronization machinery doing the work of *registration/irreversibility* but **not of the statistics**.

**Required manuscript change:** state Horn 2 explicitly. Remove any phrasing that suggests the attractor/synchronization accounts for the *weights*; confine the dynamical claim to definite-outcome registration and the reversible→irreversible boundary. (This is consistent with — and sharpens — the manuscript's own §3.3/§8 concessions.)

**Secondary outcome: STANDING DISSENT on significance.** Whether an imported-Born, Bohm-status interpretation is a publishable foundations contribution (Fable 5, Gemini) or a non-result (GPT-5.5) is a value/venue judgment the calculation cannot adjudicate. Recorded as unresolved, with the full reasoning above. *(Spun off as **[dispute-002](dispute-002-significance.md)** — narrowed there to a single publish-bar criterion and routed to the invited assessor.)*

**Routing.** The one remaining *factual* lever — a Valentini-style H-theorem for the dissipative, boundary-localized dynamics — is **not settleable by the present model** and is logged as an open calculation (not apparatus; it does not route to [`../experiment.md`](../experiment.md)).

---

*Loop facilitated by Claude Opus 4.8 (Anthropic), 2026-06-25. Parties' positions quoted from the on-record reviews in [`../review/`](../01-original-submission-and-review/review/). Deciding calculation: [`dispute-001-basin-measure.py`](dispute-001-basin-measure.py) (reproducible, numpy-only). Genuine cross-lab re-challenge of the calculation remains open.*
