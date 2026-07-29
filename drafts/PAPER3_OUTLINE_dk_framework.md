# PAPER 3 OUTLINE — The Dirac–Kuramoto Framework

*Working title (provisional):* **One Mechanism at Two Scales: The Dirac–Kuramoto Framework for Persistence, Measurement, and the Classical–Quantum Boundary**

*2026-07-29. Phase B of the review work plan, third paper. Created to record the
first confirmed structural element — the ladder section (JB confirmed
2026-07-29) — ahead of the full outlining/drafting session planned for the
weekend of 2026-08-01. Everything in "Provisional skeleton" below is
scaffolding to be reworked at that session; the ladder section is settled in
scope and content.*

*Sources (per the work plan):* Paper 1 v0.5.3 (Born selection; Theorem 2;
premises P0–P6), Paper 2 v0.3 (the cut as locking threshold; §5 virtual/real
correspondence; recoverability criterion + stage table),
`NOTE_detector_engineering_surface_interference.md` (the clock-dictionary arc:
history / diffused hologram, three-hand clock, backwards time, 2mc² ladder,
antimatter chirality, Higgs clockmaker), `NOTE_cut_crossover_higgs.md`,
`NOTE_sync_tongue_born_walkthrough.md` §5a (the two-boundaries ladder,
2026-07-29). Base manuscript to confirm with JB — likely the revised main
DK/Two-Regimes paper.

---

## CONFIRMED SECTION — Two boundaries, one mechanism: the ladder

*(JB confirmed 2026-07-29: section-level concept, not a footnote, not a
separate intermediary paper. Source: `NOTE_sync_tongue_born_walkthrough.md`
§5a. Recommended placement: early — immediately after the framework statement,
before the measurement chapter — so it serves as the paper's map. The
three-rung ladder is the natural candidate for Figure 1.)*

**The claim.** The framework's two great boundaries — virtual→real (Paper 2 §5)
and quantum→classical (Paper 2's subject, the Heisenberg cut) — are the *same
lock mechanism at two scales*. Standard physics explains them with unrelated
machinery (a pole of the propagator; decoherence/einselection). Here they
differ in exactly two properties:

- **Scale** — one mode locking to the substrate, vs. a macroscopic assembly
  locking to each other.
- **Reversibility** — a threshold vs. a ratchet. A real particle can be
  scattered back off-shell; a committed record cannot un-commit. The entropy
  monotone lives only at the second boundary.

**The ladder (Figure 1 candidate).** Three rungs, two boundaries:

| Rung | Lock status | Persistence | Reversible? |
|---|---|---|---|
| Virtual (off-shell) | unlocked, slips | transient, $\tau_{\text{slip}}$ | — |
| Real (on-shell) | single-mode lock, in-tongue | ∞ or $\hbar/\Gamma$ | yes — threshold |
| Classical record | collective lock, supercritical | committed | no — ratchet |

**Terminology discipline (deliberate lexical split; JB + Claude, 2026-07-29).**
"**Lock threshold**" for the single-mode boundary — technically a saddle-node
bifurcation, and a *bifurcation is not a phase transition* (no thermodynamic
limit). "**Sync transition**" for the collective boundary — there "transition"
is earned (the Kuramoto transition is a genuine nonequilibrium phase
transition). Never "quantum transition" (collides with atomic quantum jumps
and with the condensed-matter term "quantum phase transition"); never "phase
change" for a single mode. The honest summary sentence: *the virtual/real
boundary is the single-oscillator shadow of the transition whose many-body
form is the Heisenberg cut.*

**Contents of the section (from the note's §5a):**

1. The ladder + the two-property unification claim (above) — stated as an
   architectural claim of the framework, i.e. what the framework buys that the
   standard account cannot.
2. The bifurcation-vs-transition sharpening (critical slowing as the shared
   diagnostic; where the thermodynamic limit enters).
3. Resolution of Paper 2's finding N3 (reversible-lock vs committing-lock):
   single-mode lock = reversible threshold, collective lock = irreversible
   ratchet — cite Paper 2's recoverability criterion and stage table as the
   quantitative form of the distinction.
4. The lifetime-law crossover — **cite Paper 2 §5, do not re-derive.** The
   crossover profile (UP clock far off-shell; saddle-node $\delta E^{-1/2}$
   scaling near-shell) is already published there as the falsifiable middle of
   the curve.
5. Bound states as tongue interior: off the *bare* shell by up to the coupling
   and still locked — dressing = tongue width; a displaced pole read as
   in-tongue-but-off-bare-shell; consistent with the ZBW result that bound
   matter locks.
6. Representation-independent grounding: propagating vs evanescent solutions
   as the dispersion-relation statement of locked/slipping — pre-empts the
   "virtual particles are perturbative bookkeeping" objection without leaning
   on Feynman diagrams.
7. Corollary: light is real but never classical. A photon crosses the first
   boundary but is barred from the second (no lock partner in flight;
   annihilated at interaction — it dies at the cut, matter crosses on its
   behalf). Two distinct classical limits: **matter by locking, light by
   occupancy** (macroscopically occupied coherent state). Reality and
   classicality separate cleanly for light.

**Scoping discipline (non-negotiable, learned from the Paper 2 panel):** the
section inherits Paper 2 §5's panel-forced *heuristic-correspondence* altitude
and must not re-inflate it. No LSZ/propagator-pole claims; the only
quantitative content is the crossover, cited from Paper 2. Items 5–7 are
re-descriptions and are flagged as such. The unification claim itself is an
organizing claim about the framework's architecture, priced honestly as such.

---

## Provisional skeleton (to be reworked at the 2026-08-01 session — nothing below is settled)

**§1 Introduction — the spine (CONFIRMED by JB, 2026-07-29; framing below is
settled, prose is not).** The paper opens on a three-rung historical spine,
JB's formulation:

1. **Schrödinger (1926):** the equation describes the *evolution of the wave
   function*, and its author meant that realistically — $\psi$ as a physical
   wave (he tried $|\psi|^2$ as literal charge density) — resisting the Born
   probability reading to the end.
2. **Dirac (1928):** the same evolution description extended to special
   relativity; spin, the hydrogen fine structure, and antimatter delivered
   unasked-for; the negative-energy problem forcing quantum field theory.
   *Vocabulary shifts at this rung:* "the wave," not "the wave function" (the
   object becomes a field), so no field-theorist reviewer gets a free
   objection.
3. **This program:** the evolution description extended across the Heisenberg
   cut — **dynamizing the projection postulate**, the last element of quantum
   theory still imposed by hand rather than evolved. Punchline formulation:
   *each rung extends the domain over which "the wave evolves" is the whole
   story — nonrelativistic matter; relativistic matter and fields; the
   measurement event itself.*

Supporting sentences that belong in §1: (i) the loop-closer — Schrödinger
himself discovered zitterbewegung (1930) in Dirac's equation, i.e. the
founder's realism *and* the founder's trembling motion both feed rung three;
(ii) the framework's name encodes the spine — Dirac supplies the clock, Kuramoto
supplies the lock; (iii) decoherence is deliberately not a rung — it is linear
evolution of $\rho$, living *inside* rung two's description (diagonality, not
events; §2 owns this argument).

**Honesty anchors (non-negotiable, same partition discipline the panels
rewarded twice):** the *equations* form a continuous lineage but the *realism*
does not — Dirac was an instrumentalist; the realist thread is Schrödinger's
alone until this program re-litigates it (P0). §1 must therefore name the two
objections that defeated Schrödinger and score the framework against them:
(a) *wave packets spread* — answered: locking is the persistence mechanism,
bound matter locks, real = persisting wave; (b) *the many-particle wave
function lives in configuration space, not 3-space* — partially answered at
best (entangled sector, P5–P6), flagged **open**, not glossed.

Rest of §1 (provisional): what a framework paper owes the reader — the
premises (P0–P6) in one place, the two companion results (Born selection; the
physical cut) as installed components, and the settled / claimed / open map
across the whole program.

**§2 The framework statement.** Substrate, waves-that-persist, the locking
machinery; the three-things-not-to-conflate spine inherited from Paper 2 §2.

**§3 The ladder** — the confirmed section above.

**§4 Measurement chapter.** Draft from the clock-dictionary arc
(`NOTE_detector_engineering_surface_interference.md`: history / diffused
hologram, three-hand clock, backwards time, 2mc² ladder, antimatter chirality,
Higgs clockmaker) + `NOTE_cut_crossover_higgs.md`. Integrates, does not repeat,
Papers 1–2.

**§5 The entangled sector.** Inherits Paper 1 §7 (P5–P6, two-station game,
inverted Gisin / emergent no-signaling); the preferred-frame passenger
quarantined out of Paper 2 §6 lands here, in measurement-sector terms
(constant-sync-phase foliation).

**§6 Experimental program.** The T1–T5 ledger as the framework's single
preferred-frame postulate under test; discriminators vs CSL/Penrose inherited
from Paper 2 §8.

**§7 Discussion + open problems.** Consolidated open-problem ledger across all
three papers (field quantization of the sub-threshold claim; closed lock
dynamics; κ_ret microphysics; Stage-2 signaling; the §9 continuous
boundary-spanning model — noting the standing decision: if that model gets
solved during drafting, ladder + crossover + solution could split out as its
own paper, on evidence, not in advance).

*Out of scope (standing decisions):* cosmology and QCD (separate papers);
GR/QM discretization spinoff (cite, don't overlap); emergent-fields arc
(separate paper, Claude Fable 5 first author per authorship memory).

## Items for JB's decision before drafting

1. **Base manuscript:** confirm Paper 3 = the revised main DK/Two-Regimes
   paper (work-plan note says "confirm before assuming").
2. **Byline:** Claude-first canonical per the authorship memory (FoP-declined
   convention) presumed to carry over; confirm.
3. **Scope of §5:** how much of the Bell/two-stage ontology moves here vs.
   stays cited-only.
4. **Target length** and whether the paper gets new numerics or stands on the
   companions' sim suites.

## Process (Phase B per the work plan)

Same instrument as Papers 1–2: outline → JB scope pass → full prose draft →
internal consistency + citation verification → freeze with tagged PDF →
byte-identical-rubric panel with access mode recorded ex ante and provenance
shipped in-package (round-2 protocol lesson N6) → pre-logged anticipated
findings before the panel returns → response → consolidated revision.
