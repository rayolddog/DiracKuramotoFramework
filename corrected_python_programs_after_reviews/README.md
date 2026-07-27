# Corrected Python programs — after the 2026-07-27 review panel

These are corrected reruns of the simulations in `../born_selection_sims/`, made in
response to the external review panel (GPT-5 Codex / OpenAI, Gemini 1.5 Pro / Google,
SuperGrok / xAI) on Born_Selection v0.3. **The originals are preserved unchanged in
`../born_selection_sims/`** for provenance; nothing there was edited. Each script
here documents, in its header, the specific defect, who flagged it, the fix, and the
result.

All GPT-5 Codex code claims were independently verified as **correct** before these
corrections were written (the panel's other reviewers did not audit the code at this
level). The corrections confirm that the defects were real **and** that fixing them
*recovers* the paper's core qualitative claim while retiring its overstated
quantitative language.

## Defect → fix → result

| Corrected script | Defect (flagged by GPT-5 Codex) | Fix | Before → After |
|---|---|---|---|
| `gambler_ruin_born_corrected.py` | Stops at share ≥ 0.95 + argmax; optional stopping needs barriers at 0/1, so the winner probability is biased upward. | **True absorbing boundary**: a site whose energy hits ~0 is out; last survivor wins (no threshold parameter). | `[2,1]` **0.8263 (+2.6%, 3.6σ) → 0.7976 (dev 0.0024)**; all configs at MC floor. |
| `noise_scaling_born_corrected.py` | Same threshold bias; **and** the independent-noise SDE does not conserve energy. | True absorption; explicit label that this is a **shares martingale** (E not conserved); no-click reported. | √e 10-site bright **0.534 → 0.509** (dev 0.009); add/lin still fail (knife-edge intact). |
| `rate_commit_born_corrected.py` | `λ·dt·Σsᵅ` reaches **1.342 > 1**, an invalid Bernoulli probability, at α=0.5, λ=50. | Correct Poisson hazard **p = 1 − exp(−λ·dt·Σsᵅ)** ∈ [0,1]. | α=1 → Born at every speed (0.796–0.806); α=2/0.5 deviate as the converse predicts, now with valid probabilities. |
| `stage2_port_signaling_corrected.py` | c=1 matched control returns **NaN** (degenerate); conditional fractions compared implicitly against a straight line. | Small independent noise floor lifts the degeneracy; **no-click rate reported**; **QM conditional curve** printed for comparison. | NaN → c=1 matched control **fair** (0.506, no-click 0.27 reported); κ-scaling preserved. |
| `energy_conservation_demo.py` *(new)* | Energy non-conservation is conceptual, not just a bug: Theorem 1's SDE ≠ the "fixed quantum redistributed" narrative. | Show E-trace for both processes; Born check for both at true absorption. | Independent E swings **[0.18, 1.62]**; conserving E **≡ 1.000**; **both give Born** (shares martingale). |

## What survives, what is retired

**Survives (the science is intact):**
- The √e (amplitude-linear) law is the knife-edge: at the true absorbing boundary it
  reproduces Born to the Monte-Carlo floor, while additive and multiplicative laws
  fail decisively.
- Rate-linear commitment (α=1) reproduces Born at every commit speed (Theorem 4–5);
  α≠1 deviates exactly as the converse predicts.
- The port mechanism's κ·S(1−S) suppression under mismatched within-port correlation
  is reproduced, and the matched-port control is now genuinely fair.

**Retired / corrected (overstated in v0.3):**
- "Reproduces Born within numerical resolution" (§5.1) was true only in the
  absorbing/continuum limit; the shipped finite-threshold scripts carried a
  computable O(1−threshold) bias (~+2.6% at threshold 0.95). Text should say Born is
  recovered at the absorbing boundary, with a finite-threshold bias that vanishes as
  threshold → 1 (sweep in `gambler_ruin_born_corrected.py`).
- The "one conserved quantum redistributed" narrative does not match the
  independent-noise SDE actually used for Theorem 1. The honest statement: Born is a
  property of the **shares** martingale, which holds with or without conservation;
  matching the physical narrative requires a **conserving** process. Deriving one —
  with its covariance — from a closed field+detector+bath Hamiltonian is the paper's
  own open problem, and would also *ground* the √e scaling that reviewers 3/4 note is
  currently postulated.
- The §8.4 discriminator's "any local POVM gives affine P′(S)" holds for
  **unconditional** probabilities. The **conditional** (post-click) port fraction
  under unequal efficiency, S·η_A/(S·η_A+(1−S)·η_B), is already curved — so curvature
  per se does not discriminate. The test must compare against that QM conditional
  curve (printed in the corrected script) or use unconditional probabilities.

## Honest caveats on the corrections

- For the **additive** noise law, energy 0 is *not* absorbing (constant noise kicks a
  zeroed site back up), so the true-absorption termination does not cleanly apply and
  the additive runs stall (reported as "unfinished") rather than concentrating. That
  0 is absorbing *specifically* for √e is itself part of why √e is the special law.
- Monte-Carlo floors are ~1/√(ntrials) per proportion; residual deviations quoted
  above are at or below that floor. Seeds are pinned as in the originals.

These corrected results feed the authors' response (disposition: **accept-and-revise**
for every item above) and the single consolidated v0.4 revision.
