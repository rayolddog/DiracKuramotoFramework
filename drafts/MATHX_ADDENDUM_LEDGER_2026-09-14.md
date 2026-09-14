# MathX addendum ledger — 2026-09-14

*Instrument: the six MathX explorations (`rayolddog/MathX`, 2026-09-06 to 2026-09-14) read
against Paper 1 v0.9, `NEGATIVE_RESULT.md`, the G1/G2 contract and *One World, One Cut* v1.5,
at the sponsor's instruction to draft an addendum. Not an independent audit: the same agent ran
the MathX studies and wrote this. The 2026-09-01 reconciliation ledger closed itself at item 15
and is not reopened; this file is the record of what v0.10 applied and why. This reopens a record
the sponsor closed on 2026-09-05; every edit is marked v0.10 in the text, and §§1–9 of Paper 1
are unchanged.*

| # | Kind | MathX source | Paper 1 location | Disposition |
|---|---|---|---|---|
| M-1 | sharpening | `vacuum_race/` Tables 1–4, L24, L25 | §4(a); Addendum A.1 | Applied. The argmax rule gives Born for exactly one noise family (Gumbel on log-deposit, unit scale), under which it is Theorem 4's first-passage race; Gaussian and bounded factors give the bright port every time; a factor on the amplitude gives √Born. Pointer at §4(a). |
| M-2 | **new clause + observable** | `vacuum_race/frozen_fresh.py`, Tables 6–7, L26 | Addendum A.2; `NEGATIVE_RESULT.md` "What was learned" (pointer) | Applied as a candidate for §8.6, not a ledger entry: site-specific hazard factors must decorrelate between arrivals; Fano factor of one detector's split reads their correlation time; F = 1 in experiment bounds it under one arrival interval. Condition on the G1/G2 frozen sector stated (harmless only through a sum over many sites). |
| M-3 | conditional exclusion | `spad_surface_contact/` Part G, L21–L23 | §8.6(vii), §9.4(xi); Addendum A.3 | Applied with its assumption named: with sub-gap re-emission leaving the device, reading A registers nothing at a balanced split above 470 nm; existing balanced-split data exclude it. §8.6(vii) remains the discriminator if reabsorption is retained. Pointers at §8.6(vii) and §9.4(xi). |
| M-4 | corroboration | MathX L27 (its own correction) | P5, §2 third remark; Addendum A.4 | Applied as one paragraph: the sponsor's construction arrived at both premises and derived neither. |
| M-5 | corroboration + qualification | `spad_surface_contact/` Parts E, F, L13–L16 | Theorem 2, Appendix B; OWOC v1.5 §5.1; Addendum A.5 | Applied: the bound Dirac electron's lower spinor is slaved (computed, 10⁻⁸ degrees). Qualification: "phase plays no role" holds for passive detectors; a coherently driven absorber has a phase-dependent response in quantum mechanics (coherent control). OWOC itself not edited. |
| M-6 | corroboration | `pair_case/` Tables 1–4, L17–L20 | §7; Addendum A.6 | Applied: local rules give Bell's foil (S = 2.00, 1.41); the detection gate rides Garg–Mermin to 2.83 at η_c = 0.828 (closed loophole); the conditional update gives 2.83 with a rate-linear reading at B and 4.00 with a deterministic one, so Theorem 5's linearity is needed at the second wing too. |
| M-7 | **refined model** | MathX `MODEL_SECTION.md` §§1–5, 10–12 | §§3–5; [P3 §4.1]; Addendum A.7 | Applied as a statement and mapping, not an installation: the selection stage as a first-passage race with the vacuum term as the per-site clock, hazard linear in \|ψ\|² and renewal per arrival as premises, P5 as the cancellation of the losing clocks; capture and registration as computed in MathX agree with [P3 §4.1]'s placement. Candidate replacement for the exchange game in a later structural revision; Paper 3 is frozen and not edited. Sponsor's reading, 2026-09-14. |
| M-8 | correction, pre-freeze | MathX L10, L23 | Addendum A.3 | Applied 2026-09-14 while writing the review round's anticipated-findings ledger: Grangier 1986's beam-splitter photon (422.7 nm) lies below reading A's 470 nm line, where the exclusion runs through the predicted coincidences (L10), not the predicted silence (L23); the sentence now states both sides. |
| — | not applied | MathX Part C (packet beat at twice the mean energy) | EQUATIONS.md §15 | Consistent with the rest-frame splitting 2mc²/ℏ already corrected there; no edit. |
| — | not applied | `Born_Selection.pdf` | build | Not rebuilt (no pandoc/xelatex in the drafting environment). Rebuild and freeze with a tag before any review round. |

**Open before a review round.** (1) Sponsor review of Addendum A's wording, in particular A.3's
assumption. (2) References marked [verify] in Paper 1's list are from memory. (3) PDF rebuild and
freeze. (4) An anticipated-findings ledger written before any panel report is read, as the
program's instrument requires.
