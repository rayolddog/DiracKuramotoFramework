# Born selection: a negative result, recorded on purpose

*Written 2026-09-04 at the sponsor's instruction, on the view that unpublished failures are
a defect of the scientific record. This file states plainly what the Born-selection
program attempted, what failed, what was learned, and what remains. The papers and the
ledger carry the detail; this is the summary a reader should meet first.*

## What was attempted

The Dirac–Kuramoto program set out to derive the Born rule's statistics from a
microscopic mechanism in a real-wave substrate: a detector in which every candidate site
captures part of an incident quantum, and a selection dynamics among the sites produces
one registration with frequencies proportional to the squared amplitude, without the
square being put in by hand. Paper 1 (*A Field–Matter Selector for Outcome Production*)
developed the mechanism as a fair stochastic game over deposited energy; Paper 3 supplied
the substrate, phase locking of Dirac clocks, and its candidate for the selection law, a
race among noisy Adler clocks; Paper 2 (*The Heisenberg Cut as a Physical Threshold*)
located the irreversible step. Between 2026-09-01 and 2026-09-04 the mechanism was tested
by simulation at every joint the ledger could name.

## What failed

**The microscopic model did not produce the Born square from dynamics.** Specifically:

- The exchange game of Paper 1 carries no statistical weight once the share is read as
  amplitude bookkeeping (reading B, adopted in v0.9): the Born weight enters through the
  linearity of the commitment hazard in the share, which is the golden rule imported as a
  premise. Read the other way (reading A, shares as energies), the game over-predicts for
  asymmetric two-port splits in the paper's own engine.
- The Adler race with the plan's own amplitude-neutral commitment rule, a fixed dwell,
  gives a coupling exponent of 1.56 [1.44, 1.69], neither linear nor Born, and the reason
  was computed: each clock's commitment is a near-deterministic slide from its random
  starting phase, and the fastest of N such slides gains only logarithmically in N where
  the Born mechanism needs a full power. The exponent is criterion-dependent (1.4 to 1.8
  across dwell, tolerance, noise, pulse), tracks the detuning spectrum, and reaches 2 only
  with an amplitude-dependent dwell tuned to the answer.
- The race does give the Born curve (exponent 2.16, within 0.02 of Born at every angle)
  when commitment is made memoryless with a hazard linear in absorbed energy, under the
  Adler clock's own power law and no inserted square. But those two properties,
  memorylessness and hazard linearity, are the golden rule's structure, put in by hand.
  What the substrate supplied on its own was the amplitude dependence: tongue width times
  locked absorption rate. That is a real result about where a square can come from; it is
  not a derivation of the rule.
- Exclusivity, that exactly one site registers, is not derived and cannot be local: to
  match single-photon coincidence data the one-quantum stop must act within about a
  thousandth of the commitment time, orders of magnitude faster than light crosses a
  beamsplitter. It is Paper 1's premise P5, and it remains a premise.
- The race package's production-quality measurement was never reached. Three validation
  campaigns and three sponsor overrides brought its stationary numerics to a passing state
  on a re-frozen observable set, but the moving-band audit remains unresolved on one
  observable, and every physics result stays labelled diagnostic.

**Net:** a substrate of phase-locked clocks can realize the Born measure only by
containing a commitment process with the golden rule's structure and a nonlocal
one-quantum constraint, neither of which it produces. The program's honest position is
Paper 1 v0.9's: the papers supply at most the selector half of a theory, conditional on
the outcome weights entering as a premise, and the dynamics does not replace the premise.

## What was learned, and is worth keeping

- **A precise specification of the actualization law.** Any substrate that would derive
  the rule must supply per-site commitment that is stochastic, linear in the site's
  absorbed energy, with a site-independent time profile (memory in the timing is harmless;
  memory in the form is not), plus a one-quantum constraint acting faster than light
  across the detector. Simulations established each clause with numbers.
- **The square from geometry.** With that commitment structure, tongue width (∝ K) times
  a locked clock's absorbed power (∝ K) gives the square without a squared quantity
  anywhere in the dynamics, and the result is robust to hazard scale, noise, and a decade
  of hazard memory. This is the plan's mechanism working, once its commitment rule is
  right.
- **Commitment is the vertex, not the record.** The first irreversibility in a detector is
  the absorption vertex and thermalisation, femtoseconds to a picosecond in silicon, not
  the avalanche or the readout; everything downstream is photon-agnostic and carries no
  which-site weight; the SPAD/SNSPD asymmetry a gap-gated reading predicted does not
  arise. Paper 3's stage taxonomy was corrected accordingly.
- **Method.** Every definition was fixed before application and every prediction written
  down before the result was opened; four of the day's predictions were wrong and are
  recorded as wrong. That discipline, and the sponsor's questions from outside the field,
  caught more errors than the simulations did.

## What remains

- Paper 1's open-system derivation (§9.4 (iv), (viii)): a field–absorber–bath Hamiltonian
  that would make the hazard's form and the return rate results rather than premises. Not
  attempted. The 576-state two-absorber model exists as its unitary baseline.
- Paper 1's experiments (§8.4, §8.6(vii)): the tabletop discriminator and the
  asymmetric-split test below 553 nm, which separate the two readings on real detectors.
- The race package's moving-band ladder at dt/16 (priced at 25 hours) and, after it, the
  production sweep under the re-frozen design.

## Where the record is

- `drafts/PAPER1_DRAFT_born_selection.md` (v0.9) — the claim boundary as it now stands.
- `drafts/EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md` — every finding, uncertainty
  first, including the wrong predictions.
- `adler_two_channel_exploratory/RESULTS.md` — the race, its sensitivities, its positive
  variant and its non-claims.
- `adler_two_channel_exploratory/validation/` — the campaigns, overrides, re-freeze and
  re-decision, each a hashed record.
- `GLOSSARY.md` — the vocabulary in plain terms.
