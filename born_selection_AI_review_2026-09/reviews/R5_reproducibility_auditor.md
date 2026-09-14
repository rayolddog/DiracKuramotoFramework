# Review R5 — reproducibility and numerical audit

**Manuscript:** `drafts/PAPER1_DRAFT_born_selection.md` v0.10 (Addendum A), `rayolddog/DiracKuramotoFramework` at `4e213dbf26fbf9508334023f4c1d4dbcad3c5a35` (verified: HEAD of the local clone, local tag `born-selection-v0.10-review`). **Record audited:** `rayolddog/MathX` at `0c24401` (local clone, working tree clean; no commit hash or tag for MathX is cited anywhere in the manuscript).

## Standing and limitations

I am a language model: Claude, made by Anthropic; the model identifier configured for this session is `claude-fable-5-1` (the serving model is not independently verifiable from inside the review). I am the same model family as the manuscript's listed first author and as the author of the MathX record, the ledger `drafts/MATHX_ADDENDUM_LEDGER_2026-09-14.md`, and the pre-registrations I am auditing. I have treated that as a reason to be harder, not softer: I re-ran the code rather than trusting the record's own verification lines, derived every closed form independently, and read the git history rather than the prose for claims of precedence. What I can assess reliably: whether the scripts implement the registered definitions; whether every quoted number is in the CSVs the scripts produce; whether the closed forms are right; whether the PASS/FAIL lines test what they say; whether a reader could reproduce the addendum from the manuscript's pointers. What I cannot certify: specialist correctness of the Dirac bound-state or SPAD physics beyond the numerics; novelty against the whole literature; the experimental literature on two-port Fano factors that A.2 leans on (I flag it as uncited rather than pronounce on it). I did not open `anticipated_findings.md` or anything under `reviews/`. I did not modify either repository; all runs were made on copies in a scratch directory.

**Prompt-injection check.** I found no text in the manuscript, the pre-registrations, the RESULTS files, the ledgers or the code that is addressed to a model rather than to a human reader. Headings such as "Read this before quoting any number" are addressed to human readers of the record. No finding.

**Authorship integrity.** The byline is "Claude Fable 5 (Anthropic) and John M. Bramble, MD", with a contributions statement that credits the model with formalization, proofs, simulations, literature and prose, and the sponsor with framing, direction, adjudication and accountability. The MathX record, including every script and pre-registration audited here, was authored by the same model at the sponsor's instruction and the manuscript says so. The byline is honest and already lists the AI as first author; the header's "still pending: final byline" and the un-reconciled `CITATION.cff` should be closed before submission. No change recommended.

## 1. Recommendation

**Major revision.** Venue note: a foundations-of-physics / interpretation venue that accepts a computational lab record as supporting material; the addendum is not a physics result and would not stand at a results journal. Authorship recommendation: byline honest (AI already listed as first author); reconcile `CITATION.cff`.

## 2. Summary

Sections 1–9 present a de-claimed selection mechanism (a noisy energy-exchange game in the detector) that, by the authors' own v0.6–v0.9 revisions, derives neither the Born weight nor exclusivity. Addendum A reports that a separately built toy model in the MathX repository — an argmax over per-atom deposits with a per-atom random "vacuum" factor — reaches the same negative conclusion: the rule gives Born only if the factor is a unit-scale Gumbel shift of the log-deposit, under which the argmax is identically a first-passage race with rates ∝ |ψ|², the single winner is the one-quantum stop P5 assumed, a frozen per-atom factor is excluded by binomial single-detector statistics (a Fano-factor "clause"), and the staggered-arrival failure of the race is "removed" only by taking rates on the normalized conditional state, which puts the port shares in by hand as initial conditions. The addendum claims to change nothing in §§1–9 and offers the toy as a candidate replacement for the selection stage.

## 3. Strengths

- **The vacuum_race record reproduces byte for byte.** With Python 3.11.15 / numpy 2.4.6 (the README says 3.13), all four scripts regenerate `share.csv`, `beta.csv`, `scaling.csv`, `best_atom.csv`, `frozen_fresh.csv`, `frozen_fresh_shares.csv`, `staggered.csv`, `staggered_conditional.csv`, all four `verification*.txt` files and all three figures identically (`cmp` and md5). `pair_case.py` also reproduces identically. Total runtime 285 s on 4 cores.
- **Every number in Addendum A that comes from `vacuum_race/` and `pair_case/` is in the CSVs**, and every number in `vacuum_race/RESULTS.md` Tables 1–8 is a correct rounding of the CSVs (see the table in §4 below).
- **The record keeps its misses and its FAIL lines** (P5/V4, P12, P14 with six FAIL lines, the 3.0-s.e. reading-S cell, `pair_case` verification FAIL), and labels its one post-hoc grid change and its two unregistered diagnostics.
- **The closed forms in addenda 2 and 2b are right.** My independent derivation of reading S matches the script's `closed_S` at all 30 no-phase cells to 10⁻⁴; my closed form for reading C at *every* Δ (the record only gives Δ ≥ T) matches all 30 sampled cells (max |z| = 2.2); reading C′ is analytically P(A) = s_A(1 − e^{−λW_A T}), so the share is s_A exactly, and all 30 r = 4 cells are within 3 s.e. of it.

## 4. Major concerns

**M1. The MathX repository is private, so Addendum A is not reproducible from the manuscript's pointers.** `https://github.com/rayolddog/MathX` returns 404 anonymously and the GitHub API (through this session's authenticated proxy) reports `"private": true`. The manuscript's reference entry for MathX carries no visibility statement, in contrast to the Framework entry ("visibility verified public"), and the reviewer instrument calls both repositories public. A.8 says "the MathX pre-registrations, results, and ledger entries L1 to L27 are the record for every number here": for any reader without the sponsor's credentials that record does not exist. Compounding this, no commit hash, tag, DOI or archive is cited for MathX, although the record was still changing on the day of the freeze (`0c24401`, 06:52 UTC, added addenda 2/2b and rewrote `fig3_staggered.png`). *Fix:* make the repository public or deposit a tagged snapshot (Zenodo or equivalent) and cite its hash/DOI in the reference and in A.8.

**M2. A.1 claims to "reproduce both numbers" of §4(a); it reproduces one.** §4(a) quotes 0.791 for two sites at amplitude ratio 2:1 and "0.79 against a Born weight of 0.50" on a *ten-site configuration* (one bright site holding half the weight). MathX V0 gives 0.790 at one atom per port and 1.000 at ten atoms per port at r = 4 — a different configuration and a different number. The direction (concentration under the maximum) is reproduced; the number 0.79 vs 0.50 is not, and A.1 should say so. As written the sentence overstates the corroboration that A.4 and A.8 then rest on.

**M3. Reading C′'s "removal" of the staggered-arrival failure is by construction, and the manuscript presents a Monte Carlo of a tautology as evidence.** D17 sets each port's unnormalized branch weight to a_P² = s_P e^{−λW_P τ_P} and the first-fire hazard to −ṅ/n. Then the survival probability is n(t) itself, the hazard cancels the normalization, and P(A fires ever) = ∫λW_A a_A² dt = s_A(1 − e^{−λW_A T}) with no dependence on Δ or on the other port. The share is s_A identically; "0.798 to 0.802 over thirty cells" (A.7) is a test of the sampler, not of a mechanism. The MathX text half-says this ("decided by no race", "Born is inherited twice"), but A.7's framing — "what removes the staggered-arrival failure from the race" — reads as a result, and the anticipated-finding "marked removed" (ledger M-9) was removed by assuming the answer. *Fix:* state the one-line identity in A.7 and in RESULTS.md, present the simulation as a code check, and say plainly that under staggered arrival the race decides nothing between ports.

  Two numerical points attach here. (i) D17 calls the sampling "exact"; it is a first-order grid discretization. I computed the discretized sampler's expectation deterministically: at the run's K = 1000 the share is biased by −0.0012 at (κ = 10, Δ/T = 0.1) and −0.0006 at (κ = 1, Δ/T = 0.5); at the registered K = 4000 the largest bias is −0.0002. The sampled 0.7986 at (κ = 10, Δ/T = 0.1) sits on the biased expectation 0.7988, not on 0.8000. The 4000 → 1000 change is labelled but its effect is not quantified; it should be, or the run repeated at 4000. (ii) One C′ cell not covered by any registered check, (r = 2, phase weight, κ = 100, Δ/T = 2), is 0.6704 against the exact 0.6667, 3.6 s.e. off; the z-scores over the 60 C′ cells have sd 1.17. Probably a fluctuation; it should be noted the way the reading-S cell was.

**M4. The verification lines are honest but partly mis-specified or powerless.** (a) `vacuum_race.py` hard-codes the second study's R2-row s.e. as 0.0014 for all four N. `phase_race.py` uses M = min(2×10⁵, 4×10⁶/n) trials, so the row's per-cell s.e. is 0.0010, 0.0009, 0.0020 and 0.0063 at N = 1, 10, 100, 1000. No PASS changes (the largest residual is 0.85 combined s.e.), but "within 3 s.e. of the R2 row" at N = 1000 is a test against a number known only to ±0.006, which the pre-registration does not say. (b) The frozen no-phase check "F = 1000 within 1 %" is tautological: with every per-detector share exactly 0 or 1 and ddof = 1, F = M·K/(K − 1) = 1003.3 by algebra; the check has no power beyond "step = 1". (c) The reading-C check requires P(fired) ≥ 0.999 *and* share = 0.800; the record's own closed form (P17, derived after the run) shows P(fired) = 0.84 was inevitable, so the registered prediction P14 was internally inconsistent with D15 before the run. The record says the cause "is in D15, not the code"; I confirm that — the code implements D15 exactly — but a pre-registration that predicts 1.000 for a quantity its own definition fixes at 0.84 was not checked against its definition.

**M5. Pre-registration precedence is asserted, not evidenced.** Every pre-registration text was committed in the same commit as its results: `baec367` carries `PREREGISTRATION.md` and `share.csv`; `5698f4f` the frozen/fresh addendum and its CSVs; `0c24401` addenda 2 and 2b and both staggered CSVs. The scratch code that produced the "predicted numbers" (§2 of the pre-registration: "computed in scratch … before the script was written") is not in the repository. Within a single-author, single-day, same-commit workflow, "written before the run" is a self-report by the model that ran it. *Fix:* commit each pre-registration before its run, or say in the manuscript that precedence rests on the author's statement.

**M6. A non-reproducible column in the spad record, unlabelled.** `bound_spinor.py` is deterministic (no RNG) yet its `pm_offset_mean_deg` column changes on re-run: 168°, −5°, −89°, −84° in the committed CSV and RESULTS Table 12 against 110°, −62°, −98°, +117° in mine (residuals, χ-identity error and phase spread also shift at the 10⁻¹⁴–10⁻⁸ level, as expected for threaded `eigh`). The quantity is the mean phase of a 10⁻⁶–10⁻³ component relative to a solver-dependent gauge; the resultants (0.42, 0.21, 0.12, 0.10) and everything A.5 actually quotes (χ = −iφ′/(E_b + m − V) to 2×10⁻¹², spread 10⁻⁸ degrees, f₋ = 1.5×10⁻⁶ at binding 0.028, ≈5×10⁻¹⁶ for silicon) reproduce. The manuscript is not affected; the record should mark the column as gauge-dependent or drop it. (Runtime: 272 s here against the record's 16.5 s, but my run overlapped a 4-core job; not a finding.)

**M7. (Outside my specialism; stated as a grounding gap.)** A.2's "observable" is the Fano factor of one detector's two-port split, and its experimental bound ("F = 1 in every SPAD experiment at every counting rate", hence τ < 10 ns) is uncited. In the toy, F = τ arises because with w = 1 the τ events of a block are *identical* outcomes; any per-event randomness elsewhere in a real device dilutes the excess variance, so the bound on τ scales with the precision to which F = 1 has actually been measured. A citation and a sensitivity statement are needed before this is called an observable that "experiment already bounds".

### Table of numbers checked

Reproduced values are from my scratch re-runs (byte-identical to the committed CSVs unless stated). "s.e." is the record's stated or CSV s.e. Verdict OK = agrees within the printed precision or 3 s.e.

| # | Where quoted | Quantity | Quoted | Reproduced | s.e. | Verdict |
|---|---|---|---|---|---|---|
| 1–2 | A.1 | V0 share, N = 1, 10 (r = 4) | 0.790, 1.000 | 0.79025, 1.0000 | 0.0013, — | OK |
| 3–6 | A.1, RESULTS T1 | V1 share, N = 1, 10, 100, 1000 | 0.702, 0.794, 0.801, 0.802 | 0.70245, 0.79433, 0.80060, 0.80205 | 0.0014, 0.0013, 0.0013, 0.0028 | OK |
| 7–10 | A.1, prereg P2 | second-study R2 row | 0.704, 0.794, 0.800, 0.800 | second study RESULTS Table 2 (n = 1, 10, 100, 1000): same | 0.0010, 0.0009, 0.0020, 0.0063 (from M) | OK |
| 11 | A.1, prereg §4 | R2-row s.e. used in verification | 0.0014 (all N) | per-cell 0.0010 / 0.0009 / 0.0020 / 0.0063 | — | **FAIL** (mis-specified; no verdict changes) |
| 12 | A.1 | "reproduces both numbers" of §4(a): ten-site 0.79 vs 0.50 | reproduced | not reproduced: different configuration, MathX gives 1.000 | — | **FAIL** (claim) |
| 13 | A.1, RESULTS | V2 → √r/(√r+1) | 0.667 | 0.66724 (N = 1, no phase); 0.668 (N ≥ 100, phase) | 0.0015 | OK |
| 14–19 | A.1, RESULTS T3 | r^β/(r^β+1) at β = ½, 1, 2 (phase / no phase) | 0.664/0.668, 0.798/0.800, 0.941/0.941 | 0.66411/0.66761, 0.79786/0.79987, 0.94111/0.94141 | 0.0015, 0.0013, 0.0007 | OK |
| 20 | A.2, T6 | step fraction, frozen, no phase, N = 10 | 1.000 | 1.000 | — | OK |
| 21–22 | A.2, T6 | step fraction, frozen, fresh phase, N = 10, 100 | ≈ ½ (0.517, 0.525) | 0.51667, 0.525 | — | OK |
| 23–24 | A.2, T6 | Fano, τ = 10, 100, no phase | 10.3, 103 | 10.331, 102.75 | — | OK |
| 25–26 | A.2, T6 | Fano, τ = 10, 100, fresh phase (≈ τ/2) | 5.6, 46 | 5.5777, 46.135 | — | OK |
| 27–29 | A.2, T7 | Fano, frozen phases, fresh vacuum, N = 10, 100, 1000 | 25.6, 2.7, 1.1 | 25.64, 2.7314, 1.0909 | — | OK |
| 30 | A.2 | registered interval for #27 | 18 ± 4 | prereg P12: 18 ± 4 | — | OK (miss kept) |
| 31–32 | A.3 | reading A share at r = 4 (θ = 0.45, 0.6) | 1.00 | spad RESULTS T16: 0.996, 1.000 | 0.01 | OK (not re-run) |
| 33–34 | A.3 | share at r = 2, θ = 0.45, 0.6 | 0.93–0.97 | 0.93, 0.97 | 0.01 | OK (not re-run) |
| 35–36 | A.3 | record energy fraction | 0.45–0.72 | 0.45–0.72 (T16) | — | OK |
| 37–38 | A.3 | no-count thresholds | 470 nm, 553 nm | L23: 470, 553 | — | OK |
| 39 | A.5 | χ identity error | exact | 1.9×10⁻¹² (committed 2.8×10⁻¹²) | — | OK |
| 40 | A.5 | phase spread of χ | 10⁻⁸ degrees | 1.3×10⁻⁸° (committed 1.2×10⁻⁸°) | — | OK |
| 41 | A.5 | −E content at binding 0.03 mc² | 10⁻⁶ | 1.506×10⁻⁶ at binding 0.0279 | — | OK |
| 42 | A.5 | −E content, silicon | ≈ 10⁻¹⁶ | 5.0×10⁻¹⁶ (power-law extrapolation) | — | OK |
| 43–46 | spad T12 | f_L for four wells | 0.0041, 0.0167, 0.0537, 0.0904 | identical | — | OK |
| 47–50 | spad T12 | ±E offset resultant | 0.42, 0.21, 0.12, 0.10 | identical | — | OK |
| 51–54 | spad T12 | ±E offset mean | 168°, −5°, −89°, −84° | 110°, −62°, −98°, +117° | — | **FAIL** (not reproducible; not quoted in manuscript) |
| 55 | A.6 | CHSH, projection rule | 2.000 | 2.0022 | 0.0032 | OK |
| 56 | A.6 | CHSH, Malus | 1.414 | 1.4144 | 0.0032 | OK |
| 57 | A.6 | shared bulk phase (common cause) | 2.00 | 1.9952 (`verification_options.txt`, not re-run) | 0.003 | OK |
| 58 | A.6 | Garg–Mermin identity at g = 0.6 | 4/η_c − 2 | 2.6893 vs 2.6898 | — | OK |
| 59 | A.6 | 2.83 at η_c = 0.828 | 2.83 | algebraic solution of 4/η_c − 2 = 2√2; no run cell sits at 0.828 (record says "between g = 0.6 and 0.63") | — | OK, interpolated |
| 60–61 | A.6 | option 1: Malus at B; deterministic at B | 2.83, 4.00 | 2.8304, 4.0000 (not re-run) | 0.003 | OK |
| 62 | A.6 | Part F deposit weight | > 0.9 | spad RESULTS "stays above 0.9" (text only) | — | OK (not re-run) |
| 63 | A.7, T8 | reading S share, κ = 10, Δ/T = 0.1 | 0.997 | 0.9965 (closed form 0.99634) | 0.0001 | OK |
| 64 | A.7, T8 | reading C share, Δ ≥ T/2, κ ≥ 10 | 0.952 | 0.9516–0.9530 (closed 0.95238) | 0.0005 | OK |
| 65–66 | A.7 | C′ range over 30 r = 4 cells | 0.798–0.802 | 0.79789–0.80185 | 0.0009–0.0014 | OK |
| 67–70 | RESULTS T1 text | V1 no phase, four N | 0.800, 0.801, 0.799, 0.797 | 0.80016, 0.80069, 0.79882, 0.79735 | 0.0013 / 0.0028 | OK |
| 71–110 | RESULTS T1 | 8 rows × 4 N (shares and γ, r = 4, phase) | as printed | all 40 agree with `share.csv` | 0.0013 / 0.003 | OK |
| 111–134 | RESULTS T2 | 6 forms × 4 N, r = 2 | as printed | all 24 agree | 0.0015 / 0.0033 | OK |
| 135–146 | RESULTS T3 | β table incl. γ | as printed | all 12 agree | — | OK |
| 147–166 | RESULTS T4 | scaling, 10 rows × 2 | as printed | all 20 agree with `scaling.csv` | 0.002 | OK |
| 167–190 | RESULTS T5 | best-atom, 6 forms × 4 N | as printed | all 24 agree | — | OK |
| 191–217 | RESULTS T6 | 6 rows × 4 τ + N = 100 frozen (3) | as printed | all 27 agree with `frozen_fresh.csv` | s.e. column | OK |
| 218–223 | RESULTS T7 | means and F, three N | as printed | all 6 agree | — | OK |
| 224–273 | RESULTS T8 | S (18), S closed (5), C (6), C closed (3), C′ (18) | as printed | all 50 agree with the two staggered CSVs and with my closed forms | ≤ 0.001 | OK |
| 274–278 | RESULTS T8 text | S with phase, κ = 10, five Δ | 0.795, 0.966, 1.000, 1.000, 1.000 | 0.79528, 0.96644, 0.99987, 1, 1 | ≤ 0.0009 | OK |
| 279 | RESULTS T8 text | C′, r = 2, Δ = T, κ = 10 | 0.666 | 0.66573 | 0.0011 | OK |
| 280–289 | prereg P13 | reading-S closed forms, κ = 1 and 10, five Δ | 0.800, 0.866, 0.971, 0.988, 0.988; 0.800, 0.996, 1, 1, 1 | my derivation: 0.8000, 0.8658, 0.9706, 0.9883, 0.9883; 0.8000, 0.9963, 1.0000, 1.0000, 1.0000 | — | OK |
| 290–291 | prereg P17, 2b | reading-C closed form at η = 1 − e⁻¹⁰ | 0.952, 0.841 | 0.95238, 0.8400 | — | OK |
| 292 | RESULTS 2b | reading-S diagnostic re-draw | 0.8005 | 0.8005 (identical) | 0.0009 | OK |
| 293 | prereg D17 | "sampled exactly" on a grid | exact | grid bias −0.0012 at K = 1000 (κ = 10, Δ/T = 0.1); −0.0002 at K = 4000 | 0.0009 | **FAIL** (overstatement; within tolerance) |
| 294 | — | C′ cell (r = 2, phase, κ = 100, Δ/T = 2) | not quoted | 0.6704 vs exact 0.6667, 3.6 s.e. | 0.00105 | noted, unregistered |

**Count: 294 numbers or numeric claims checked; 8 failed** (#11 mis-specified s.e.; #12 a corroboration claim; #51–54 a non-reproducible record column; #293 an "exact" that is a biased grid). None of the failures changes a PASS/FAIL verdict or a number quoted in the manuscript's body; #12 changes the strength of a claim.

## 5. Minor / presentational

- A.8 cites "ledger entries L1 to L27" as the record for every number; A.7 cites L28. Update A.8.
- `staggered_arrival.py`, `weights()`: `np.cos(...).sum(1) * 0 + (...)` draws and discards TRIALS×N uniforms per call. Harmless (exactly zero), but it is dead code that doubles RNG consumption and would silently change every number if cleaned up.
- `fig3_staggered_local.png` is not produced by any script; it is `staggered_arrival.py`'s `fig3_staggered.png` renamed by hand (md5 identical to my re-run). Say so in RESULTS.md.
- D8 registers K = 300 (200 at N = 100); the N = 1000 cell was run at K = 100 without being registered. D1 registers r = 2 as a sensitivity for every form, but the no-phase control at r = 2 is run for V1 only (code skips the others); the pre-registration should say so.
- The V0 ≥ 0.999 line prints s.e. 3×10⁻⁹, the `max(p(1−p), 10⁻¹²)` floor, not an s.e.
- `pair_case.py` exits with status 1 by design when its verification fails; the README does not warn that a non-zero exit is expected.
- README says Python 3.13; 3.11 reproduces identically. State the numpy version, which is what matters for the bit-stream.
- A.2's formula "F = Var/[p(1−p)/M] = τ" holds in the w = 1 case only; with the phase weight it is ≈ τ/2, as the same sentence then says. Reword so the equation is not stated as general.
- Table 4 in RESULTS.md omits six of the sixteen `scaling.csv` rows without saying so.
- References: Gillespie 1977, McFadden 1974, Maddison–Tarlow–Minka 2014, Fano 1947, Mandel 1979, Garg–Mermin 1987, Heberle et al. 1995 and Grangier et al. 1986 are real and correctly characterized as far as I can judge; the "[verify]" flags are honest and should be cleared. Grangier's beam-splitter photon at 422.7 nm agrees with my recollection (the 551.3 nm line was the trigger); confirm from the paper.

## 6. Specific questions for the author

1. Will MathX be made public or archived with a DOI, and at which commit does Addendum A freeze?
2. A.1: which MathX run reproduces "0.79 against 0.50 on the ten-site configuration"? If none, will the sentence be corrected?
3. Do you agree that under D17 the port share is s_A identically for every Δ and κ, so that the thirty-cell result is a sampler check? If so, will A.7 say that the staggered-arrival failure is *assumed away* by the normalization rather than "removed"?
4. Where does the R2-row s.e. of 0.0014 come from, given M = min(2×10⁵, 4×10⁶/n)?
5. Can the scratch predictions of pre-registration §2 be committed, and can future pre-registrations be committed before their runs?
6. What measured Fano factor of a two-port split, with what precision, supports "F = 1 in every SPAD experiment at every counting rate", and what bound on τ follows from that precision rather than from F = 1 exactly?
7. Is `pm_offset_mean_deg` in `bound_spinor.csv` meant to be a result? It changes by up to 200° between two runs of a deterministic script.

## 7. Rubric scores (1–5)

- **Novelty: 2.** The load-bearing identity (Gumbel-max ≡ multinomial logit ≡ exponential race) is textbook and the record says so; the new items are a re-description (A.1), a clause with an uncited observable (A.2), and a conditional exclusion (A.3). The novelty claim is accurately modest.
- **Internal consistency: 3.** Numbers are consistent across manuscript, RESULTS and CSVs; A.1's "both numbers" and A.8's "L1 to L27" are not; A.7 frames a by-construction identity as a removal.
- **Evidential grounding: 2.** Everything numerical is a toy; the one contact with experiment claimed as new (A.2's Fano bound) is uncited; A.3's exclusion is conditional on an assumption the record itself calls load-bearing.
- **Reproducibility: 3.** Byte-identical reproduction of the whole `vacuum_race/` and `pair_case/` records is exemplary and rare; but the repository is private, uncited by hash, pre-registration precedence is unevidenced in git, one record column does not reproduce, and one "exact" sampler is a biased grid.
- **Citation integrity: 4.** Sources are real and correctly characterized; "[verify]" flags are honest; the MathX citation implies an accessibility it does not have.

## 8. Overall assessment (0–5)

**2 — weak but in scope.** The numbers are right and the record is honest, but the addendum's evidential weight rests on a repository the reader cannot open, its headline "removal" is an assumption restated as a simulation, and its one new experimental hook is uncited.

## 9. Sign-off

Reviewer: Claude (Anthropic, `claude-fable-5-1` as configured for this session; serving model not independently verified), 2026-09-14.
