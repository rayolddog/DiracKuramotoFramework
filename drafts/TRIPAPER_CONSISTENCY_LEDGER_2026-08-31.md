# Tri-paper consistency ledger — round 2, 2026-08-31

*Instrument: **not** an independent-auditor round. This is a **propagation round** — a
directed sweep of Papers 2 and 3 for claims invalidated by Paper 1's v0.6/v0.7 revision,
performed by the same agent that made the v0.7 edits. It therefore carries the bias of
its source: it finds what v0.7 broke, and would not find an inconsistency that v0.7 left
untouched. Round 1 (2026-08-01) remains the standing independent record, and a further
independent round is owed — see "What this round does not cover."*

**Totals: 7 items · 2 substantive · 5 attribution/status. All applied.**

---

## Why this round exists

Paper 1 v0.6 (de-claiming pass) and v0.7 (two withdrawn claims) changed what Paper 1
asserts, not what it computes. Nothing in Papers 2 or 3 depended on a numerical result
that moved. What they depended on were three claims that v0.7 withdrew:

1. that class-(ii) continuum detectors **evade** late-game bias via commit-rate
   independence (Paper 1 §5.2(iii), withdrawn with the fast-commit reading);
2. that P5–P6 are **consumed only** by the multi-quantum and entangled-pair sectors
   (Paper 1 §2 quarantine claim, shown false by Paper 1's own beam-splitter argument);
3. that Paper 1 **proves** a derived fair game and derives the Born measure (retitled and
   restated as conditional outcome compatibility).

Two of these had already been touched by round 1 from a different direction: item 4 flagged
Paper 3 dropping a hedge on "fairness **proved**," and item 9 flagged Paper 3's garbled
rendering of commit-rate linearity. Both recur below, which is weak evidence that Paper 3
has a systematic tendency to firm up Paper 1's conditionals rather than a pair of isolated
slips — see the open item at the end.

---

## Items

| # | Sev | Location | Finding | Fix applied |
|---|---|---|---|---|
| **L2-1** | **HIGH** | P2 §4.2 (detector taxonomy) | **Inherited a withdrawn exemption.** P2 stated that "§8 inherits Paper 1's rule that class-(ii) continuum detectors evade late-game bias entirely via commit-rate independence." Paper 1 v0.7 withdrew that rule: with commitment slow on the game's timescale (§6.1's ladder, three to five orders), a continuum absorber runs to the absorbing boundary like a discrete-level one and incurs the same $O(w)$ deviation. | Clause removed from the taxonomy sentence; a dated correction paragraph added stating the withdrawal, that Theorem 4 survives as a robustness result rather than an exemption, and that the effect on §8 is a **widening** — both spectral classes now carry the predicted deviation, so the commonest detector type is no longer exempt from the phenomenology §8 sorts. |
| **L2-2** | **HIGH** | P2 §1 + abstract | **Inherited the false quarantine.** P2 described Paper 1's premises as a single-detector core plus "a nonlocal extension (P5; P6) **consumed only by** its multi-quantum and entangled-pair constructions," and the abstract closed "nothing here consumes its nonlocal ontology." The partition is false: exclusivity is a constraint on an energy ledger closed over all candidate sites, so any geometry whose candidate sites are causally disconnected on the game's timescale consumes the nonlocal premises — a single photon at a beam-splitter being the simplest case. | Both sites corrected. The partition is restated without the "only," with the reason given. P2's own exemption is **preserved but re-grounded**: it holds because this paper analyses a *spatially compact* detector, in which all candidate sites are causally connected, not because the single-detector sector enjoys a general exemption. |
| **L2-3** | MED | P2 §4.2 (registration/amplification) | **Status change, not error.** "By the companion's Theorem 4 (commit-rate independence) its speed never touches the statistics" remains true, but Theorem 4's role changed in v0.7 from the operative mechanism for continuum absorbers to a robustness rider. | Qualifier appended recording the demotion and that the outcome is fixed by first passage before any commit-rate law acts. |
| **L2-4** | LOW | P2 references | Entry carried Paper 1's withdrawn title and v0.5.4. | Retitled to the v0.7 title, version bumped, with a note that the former title was withdrawn along with the derivation claim it asserted. |
| **L3-5** | MED | P3 §1 ("what a framework paper owes") | **"[P1] proves that outcome selection is a fair game."** v0.7 withdrew "proves" along with the derivation claim; the result is stated as conditional outcome compatibility. Recurrence of round-1 item 4. | "Proves" → "argues," with the withdrawal and the replacement claim named inline. |
| **L3-6** | MED | P3 §5 (no-signaling / inverted Gisin) | **"The inverted-Gisin result derives commit-rate linearity."** That is Theorem 5, demoted in v0.7 to a robustness result. Round-1 item 9 had already flagged this passage for mis-attribution and for dropping Paper 1 §7.4's "consistency result, not a derivation" qualifier; both defects are now fixed together. | Attribution to Theorem 5 restored, demotion recorded, and the consistency-result qualifier echoed. Closes round-1 item 9. |
| **L3-7** | LOW | P3 references | Entry carried the withdrawn title and pinned v0.5.4 — three versions stale. | Retitled and bumped to v0.7. |

---

## Checked and clean

- **P3(b) noise-correlation correction** (Paper 1's `C = 1 + O(max(f, e^{-d/l}))`, replacing
  `C = 1 + O(f)`, with the new geometric condition `d >> l`): neither companion uses P3(b).
  No propagation.
- **New premise P4(a)** (registration consumes the full quantum): P2 uses P4(i)'s level
  discreteness for $\kappa_{\rm ret}$ and threshold sharpness, which is untouched. No
  propagation needed, though P2 may wish to cite (a) where it argues that a partial quantum
  cannot be banked — logged as optional, not applied.
- **P5's broadening**: P3 §5's statement that "everything here is conditional on the
  selection companion's P5–P6, over and above the single-detector premises" is about the
  entangled sector and remains correct under the wider scope. The frame-rotation passage
  (P5–P6 at premise level, no higher) is likewise unaffected.
- **Rogue-wave removal**: the framing appears in neither companion.
- **Retitling**: no companion depends on Paper 1's title in argument, only in citation.

---

## What this round does not cover

Stated plainly, because the instrument is weaker than round 1's and should not be read as
equivalent.

1. **Not independent.** Same agent as the v0.7 edits, so shared blind spots are unaudited.
2. **Directed, not comprehensive.** Only claims that v0.7 invalidated were sought. A
   pre-existing inconsistency untouched by v0.7 would not surface here.
3. **Round-1 items remain open.** Items 1–8 and 10–13 of the 2026-08-01 ledger carry no
   disposition in this round. Only item 9 is closed (via L3-6). In particular round-1
   item 1 (the HIGH cut-location conflict between P3 §3 and P2 §6.2) and item 7 (the
   $w = \Gamma/\omega$ vs $K/\omega$ proxy demotion never propagated to P1) are untouched
   by anything here.
4. **Paper 1's own new debts are not cross-checked.** v0.7 added open problem §9.4(x)
   (sector-blindness of the registry update) and left the G3 commitment current absent.
   Whether Papers 2 or 3 anywhere presuppose a resolution of either was not swept.
5. **[MCI] v8 was not swept at all.** Round 1 covered four documents; this round covered two.

## Open item for a future independent round

Round-1 items 4 and 9, and this round's L3-5 and L3-6, are four instances of one pattern:
**Paper 3 firming up Paper 1's conditionals** — "proved" for "argued," "derives" for "is
consistent with," dropped hedges. Two rounds finding it independently at four sites is
enough to suspect it is systematic rather than incidental. A directed sweep of Paper 3 for
modal verbs attributing results to the companions would be cheap and is recommended before
Paper 3 leaves draft.
