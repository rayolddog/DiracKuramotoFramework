# Tri-paper consistency ledger — 2026-08-01

*Instrument: three independent auditors over the four manuscripts (Papers 1 v0.5.4,
2 v0.3, 3 v0.1, and the frozen [MCI] v8) — one on terminology/symbols, one on
claim-level consistency, one on cross-references (~135 citation checks). Findings
merged and deduplicated below; **CONVERGENT** marks items found independently by two
auditors (the strongest class, per round-protocol experience). Grouped by fix type in
application order. Disposition column is JB's: accept / reject / defer. Group III
items are mechanical (no physics judgment) and can be applied on standing word.*

**Totals after dedup: 3 HIGH · 11 MED · 16 LOW (30 items).**
**Clean categories, for the record:** no unflagged old-two-stage usage anywhere; P2's
premise labels match P1 §2 exactly; P3 never claims P1 "derived the Born rule"
outright; frame-rotation attribution correct (picture is in P1 §7.3; Toner–Bacon
framing properly P3's own); superposition/collapse language consistent across all
four documents including the closing line; every argument-bearing citation resolves
(75 cross-paper tags, 12 P2→P1 references).

---

## Group I — Conceptual / claim-level (JB adjudication required)

| # | Sev | Location | Finding | Suggested fix | Disposition |
|---|---|---|---|---|---|
| 1 | **HIGH** | P3 abstract + §3 vs. P2 §6.2 (and P3 §4.1/§6.1) | **Cut-location conflict.** P3 §3/abstract assign the cut to the *collective* sync transition ("the Kuramoto threshold… which is the cut"); P2 §6.2 insists the cut is a **crossover at the single-mode layer** κ_ret/K = 1 — and P3 §4.1/§6.1 use the single-mode assignment, contradicting P3's own §3. | Recommended: scope §3 — the collective lock is the *record's* classicality (registration, irreversibility, the ratchet); the cut proper remains P2's single-mode layer. Alternative: declare a deliberate revision of P2 and defend it. | |
| 2 | **HIGH** | P3 §3 ("inherits that scoping and adds none") | **Scoping claim contradicted by own content.** §3 adds three arguments beyond P2 §5's panel-forced correspondence scoping (the shadow-identity summary; the evanescent/propagating grounding; the in-tongue-off-bare-shell pole reading) and rests the ladder's first rung on a correspondence P2 explicitly rests nothing on. | Delete "and adds none"; add a status sentence labeling the three additions as *this paper's own*, at correspondence altitude; or demote the virtual rung. | |
| 3 | MED | P3 §7.1 "nonlocality (in the Bell sense, never signaling — §5)" | Unconditional "never signaling" vs. P1 §8.5's open fork (radical reading = in-principle signaling) and §8.7's ordering-window channel — both carried open by P3 itself (§6.2, ledger items 4/7). | "…never signaling under the stated premises; the §6.2 fork is where that could fail." | |
| 4 | MED | P3 §7.2 (Bohm comparison) | "Fairness **proved** from detector physics" drops the hedge: the measure-identification (premise P1) is open per [P1 §1/§9] — the direct analogue of Bohm's postulated equilibrium. [MCI §7.3] carried "if its premises hold"; P3 dropped it. | Restore the conditional; cross-reference P3 §7.3 item 2. | |
| 5 | MED | P3 §4.1 (capture reversibility) | Reversible capture stated for all detectors; P2 §4.1 (panel N5) scoped it: demonstrated for discrete-level ensembles, in-principle-but-foreclosed for broadband continuum absorbers. | Import the detector-class scoping sentence. | |
| 6 | MED | P3 §4.3 (diffused hologram) | Lost its **sponsor-originated interpretive label** (carried in P1 §4 and P2 §4.1); "makes its structure exact" over-claims — §4's own preamble promises flags kept. | Restore the label; "makes exact" → "organizes." | |
| 7 | MED | P1 §5.2, Fig. 4, Table 1, App. B.2 | P1 still treats w = Γ/ω as interchangeable with w = K/ω ("the same physics"); P2 v0.3 §3.2 demoted K ∼ Γ to a *passive-absorber proxy* (cavity-QED counterexample). Demotion never propagated to P1. | Add proxy scoping to P1 (→ v0.5.5) or cite P2 §3.2 for it. | |
| 8 | LOW | P3 §4.1/§6.1 + abstract | Quantitative cut claims (κ_ret ∼ K, w = K/ω, table widths) missing P2's local conditionals (κ_ret ansatz; passive-absorber proxy); abstract "companion papers **established**" exceeds P2's "we argue." | One parenthetical at first quantitative use; "argued" for "established." | |
| 9 | LOW | P3 §5.2 (inverted Gisin) | Rendering garbled: commit-rate linearity is P1 Theorem 5; "inverted Gisin" is the reversed arrow; P1 §7.4's "consistency result, not a derivation" qualifier omitted. | Attribute linearity to Theorem 5; echo the consistency-result qualifier. | |
| 10 | LOW | P3 §4.7 (energy audit) | "Until the **second stage** completes" vs. P1 §8.6(vi) "deposition completes only at **registration**"; residue clause stated declaratively where P1 has it as pending interpretive clause. | "Until registration completes"; restore "should… pending the κ_ret microphysics." | |
| 11 | LOW | P3 §6.2 (discriminator null) | Dropped P1 §8.5's closing qualifier. | Append "in every configuration tested." | |
| 12 | LOW | P3 §6.1 ("central experimental claim") | P2 §8.2 demoted the one-parameter collapse to "research direction"; the surviving discriminators are §8.3–8.4. | "Central experimental direction," cite §8.3–8.4. | |
| 13 | LOW | P3 §4.1 (stage boundaries) | Two clauses presented simultaneously as "the cut condition" and "the stage boundaries" — under P2's operational criterion only the conjunction is the cut. | Split the sentence: boundaries are the clauses; the cut is their conjunction. | |

## Group II — Terminology / symbols

| # | Sev | Location | Finding | Suggested fix | Disposition |
|---|---|---|---|---|---|
| 14 | **HIGH · CONVERGENT ×2** | P3 §6.1 | "this framework puts it on **γ/K**" — the exact pre-N2 usage the κ_ret rename exists to eliminate (γ reserved for genuine dissipative rates in the shared dictionary). | γ/K → κ_ret/K. | |
| 15 | MED | P2 §8.4 | "maintained below threshold (κ_ret ≪ K… kept coherent)" — inverted per P2's own §3.1 convention (coherent = far from shell = **large** κ_ret). Propagates into P3 §6.1's imported dial. | κ_ret ≫ K, or "kept outside the layer" (P2 touch). | |
| 16 | MED | P2 §2/§4.1 | Numbering collision: P2's trichotomy "(1) interaction / (2) decoherence / (3) lock" vs. Stage 1/2/3 (capture/selection/registration) in P1/P3/MCI — non-monotonic mapping ("stage (2)" = decoherence in P2, selection elsewhere). | Letter P2's trichotomy (A)/(B)/(C) or name the processes (P2 touch). | |
| 17 | MED | P3 §7.3 item 2 (and throughout) | Token collision: "P1" = premise P1 *and* citation tag [P1] in the same sentence. | Write "premise P1" explicitly wherever the premise is meant (or retag the papers). | |
| 18 | MED | P3 §§2, 3, 4.1, 4.6 | K polysemy: site–field coupling K (w = K/ω), chiral coupling K = m, Kuramoto K_c — all bare K in one paper; MCI's K_pair subscript silently dropped in §4.1. | Add a symbol table; keep "K = m" always paired or use K_χ; restore K_pair in §4.1. | |
| 19 | LOW | P3 §1, §5 intro | "P5–P6" jointly labeled "the shared-registry premise" — only P5 is the registry; P6 is the ordering foliation. | "The shared-registry and ordering-foliation premises (P5–P6)." | |
| 20 | LOW | P3 §2 table, §3; P2 §5 | Dictionary escapes: "locking transition" for the collective boundary (should be "sync transition") and, in P2 §5, for the single-mode boundary (should be "locking boundary/threshold"). | Apply P3 §3's own dictionary at each site. | |
| 21 | LOW | P3 §6.4 T-ledger | T3 row's bare "γ" undefined 50 lines after item 14's misuse. | Gloss ("dissipative rate γ") or restate. | |
| 22 | LOW | P3 §7 / §1 stub; P2 line ~233 | MCI name used (§7.1) before the §1 inheritance paragraph (still a stub) introduces it; P2's forward reference calls Paper 3 a "revision" where the decision is *supersession*. | Draft the §1 paragraph (already planned); update P2's [Paper 3] descriptor at next touch. | |

## Group III — Cross-references / mechanical (applicable on standing word)

| # | Sev | Location | Finding | Suggested fix | Disposition |
|---|---|---|---|---|---|
| 23 | MED · CONVERGENT ×2 | P2 reference list | "[Paper 1] … Manuscript v0.5.2" — stale by two point-versions; contradicts P2's own header ("propagated… as its v0.5.3"). | Bump to v0.5.4 at next P2 touch. | |
| 24 | MED | P3 references (Oppenheimer) | Annotation "(Majorana–Oppenheimer form, §2)" — the term never appears in P3's body; §2 names only Riemann–Silberstein. | Add "(the Majorana–Oppenheimer formulation)" to §2's sentence — one-phrase fix. | |
| 25 | LOW | P3 §4.1 | "[P1 §3]" for the three-stage decomposition — it's stated in P1 §2 (§3 is capture only). | → [P1 §2]. | |
| 26 | LOW | P3 §2 (registers) | Beamsplitter attributed to [MCI §2.5]'s examples — concept present there, example absent. | "A coherent boundary in the sense of [MCI §2.5]." | |
| 27 | LOW | P3 §6.1 | Recoverability cited to [P2 §8.3]; it is *defined* in §4.1 (P3 cites §4 correctly elsewhere). | → [P2 §4.1] (or "applied in §8.3"). | |
| 28 | LOW | P3 §4.5 | "The *what-escapes* of §3's threshold now identified" — §3 carries no escape framing. | Either add the escape sentence to §3 (it exists in the sync-tongue note §5) or rephrase §4.5. | |
| 29 | LOW | P3 references (Grangier) | Orphan entry — never used in the body (the anticorrelation material was dropped in drafting §2). | Restore the §2 parenthetical "(Grangier–Roger–Aspect: anticorrelation + interference in one apparatus)" or drop the entry. | |
| 30 | LOW | P1 header | Title line still reads "DRAFT v0.5"; v0.5.4 exists only inside the revision note. | Bump the header label before freeze (P1 touch). | |

---

*Application order once dispositioned: Group III (mechanical) → Group II → Group I,
with items 1–2 (the two conceptual HIGHs) resolved first inside Group I since several
lower items inherit their outcome. Files touched: P3 (most items), P2 (15, 16, 22b,
23), P1 (7, 30). P1/P2 edits are post-review version bumps and will be logged in
their revision notes per house convention.*
