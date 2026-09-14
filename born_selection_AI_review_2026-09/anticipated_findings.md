# Anticipated-findings ledger — Paper 1 v0.10 round

*Written and committed 2026-09-14 BEFORE any PDF was frozen and BEFORE any review was requested;
the freeze commit is to follow this one in git history, and that ordering is what makes the ledger
audit-proof. Each incoming finding will be classified against this list as ANTICIPATED,
ANTICIPATED-SHARPENED, or GENUINELY NEW. Written by the first author, who also wrote the MathX
studies that Addendum A reports and who is the model behind any internal-stage reviewer: a reason
to expect the reviews to find these, and a reason to hope they find more. One finding was caught
while writing this ledger and fixed in the manuscript before the freeze; it is item 9 below, kept
so the round can see it.*

## What the July panel found, and what v0.10 has done about it

The July round reviewed v0.3 (*The Born Rule as a Derived Fair Game*) and returned 0/2/2 external
scores. Its findings were: the derivation claim outran the premises (withdrawn at v0.6, title
changed); the noise was engineered rather than physical (§4 now gives the interference-cross-term
origin, as a sketch); simulation defects (corrected, `../corrected_python_programs_after_reviews/`);
mislabelled thresholds and a formula quoted outside its regime (v0.8's ladder correction);
misread sources (partly corrected); AI authorship. A reviewer of v0.10 will re-check every one of
these. The ledger below assumes they do, and adds what v0.10's own content invites.

## Anticipated major findings

1. **The paper is a negative result carrying a mechanism's title, and its revision history is the
   paper.** v0.6 to v0.10 withdraw claim after claim until §9.1 says the paper "supplies, at most,
   the selector half of a larger theory" and Addendum A.8 says it "changes no claim". A reviewer
   will ask what a reader is meant to take from a manuscript whose header is longer than some of
   its sections and whose result is that its own mechanism inherits what it set out to derive.
   *Status: the README says the papers are a record, not for submission; `NEGATIVE_RESULT.md`
   exists for this reason. Expect the reviewer to say the honest form of this document is
   `NEGATIVE_RESULT.md` with the theorems as an appendix, and that the paper should be retired
   rather than revised.*

2. **The paper now carries two selection mechanisms.** §§3–5 are a martingale exchange game
   terminating by first passage at the full share; Addendum A.7 is a first-passage race among
   exponential clocks whose hazard is linear in the deposit, offered as the "candidate replacement"
   for §§3–5. They give the same statistics for different reasons (Theorem 0 by optional stopping;
   Theorem 4 by the rate law), and A.1 says the two constructions "use the cross term differently".
   A reviewer will say the paper cannot hold both, that A.7 makes the fairness theorems of §5
   idle (if the hazard is linear, Theorem 4 alone gives Born and Theorems 1–3 govern a game that
   no longer decides anything), and that "not installed here" defers the inconsistency rather
   than resolving it. *Status: anticipated and real. The v0.9 header already admits that under
   reading B "the Born frequencies enter through the linearity of the commitment hazard"; A.7
   makes that the whole mechanism. The honest fix is the structural revision the header calls
   gate-blocked: one mechanism, and §5's theorems restated as what the substrate must not do to
   the shares before commitment.*

3. **The fresh-vacuum race inherits the staggered-arrival failure the September round found for
   the postulate.** *One World, One Cut* v1.0's selection postulate failed for time-separated
   detectors (that round's N1, confirmed by Run B): a hazard on the whole quantum's survival gives
   the click to the nearer detector whenever the arms are unequal. The MathX vacuum race was run
   with simultaneous arrival at both ports, and A.7's rule — every clock runs at a rate set by its
   deposit, the first to fire wins — is exactly the hazard that failed. A reviewer who has read
   the record will say A.7 reintroduces a defect the program already corrected (the v1.1
   restatement: the hazard acts on the *conditional* state, in the quantum-jump unravelling, so a
   site's rate is zero until the wave reaches it and the losing clocks are cancelled by the null
   record, not by a global stop). *Status: anticipated; not addressed in A.7, which should be
   amended to state that the race's rates are those of the conditional state and that the
   simultaneous-arrival runs do not test staggered arrival. A run with staggered arrival is owed
   and is a one-line change to `vacuum_race.py`.* **Removed before the freeze (2026-09-14, night;
   runs on record in MathX `vacuum_race/` addenda 2 and 2b, ledger L28).** The race as first
   written does inherit the failure (0.997 at a tenth of a packet length of stagger). A local
   repair, ports coupled only by the stop, gives 0.952 and was a registered prediction that
   missed. The rates on the normalized conditional state give Born at every stagger and coupling.
   A.7 is amended to state that premise. The item stays here so the round can see that the
   removal cost the second face of P5, renormalization on a null across the separation, which a
   reviewer may press as item 8 now doubled.*

4. **A.2's clause is either trivial or unfalsifiable in a real detector.** Any physical
   fluctuation in silicon decorrelates in femtoseconds, so the decorrelation requirement bounds
   nothing a detector could violate; and where frozen per-site structure does enter a hazard
   (inhomogeneous detuning), a real pixel holds $10^8$ sites, so the run's own Table 7 says the
   Fano factor is 1 regardless. Real SPAD counting statistics are moreover *not* binomial:
   afterpulsing, dead time, crosstalk and dark counts give super- and sub-Poissonian departures
   (the September round's N10), so "$F = 1$ in experiment" is a statement about corrected counts,
   not raw ones. *Status: anticipated. The reply is that the clause bites on models, not devices —
   it excludes the frozen-vacuum reading of the sponsor's model and any hidden per-site variable
   that a maximum can single out — and that the observable needs the confounds separated, which
   §8.6(v) already says of the warm-detector bias. The addendum calls it "a candidate for §8.6,
   not a ledger entry", which a reviewer may find is the right status and then ask why it is in
   the paper at all.*

5. **A.1 is a textbook identity presented as a result.** The Gumbel-max identity is McFadden 1974
   and the exponential-clock race is Gillespie 1977; the addendum says so, and a reviewer will say
   that §4(a)'s existing sentence ("tuned into a linear-response window by hand") already
   contained it and that "completed" overstates a citation. *Status: anticipated. The claim is
   only that the extreme-value and first-passage rules are the same object under one noise family,
   which §4(a) did not say; the reviewer may reasonably call that a footnote.*

6. **"Independent construction" overstates the independence.** The MathX studies were built by the
   same model family that wrote this paper, at the same sponsor's instruction, days after the
   negative result was written. That they "reached this paper's conclusions by another route" is
   evidence of consistency, not of independent confirmation, and a reviewer will say A.4's "that
   is the reason this addendum exists" rests on it. *Status: anticipated; the addendum's status
   paragraph says the runs were built without reference to the premises, which is true and is
   weaker than independence. The wording should say "a second construction by the same authors".*

7. **A.3 excludes a reading the paper had already dropped, on a toy model, under a named
   assumption.** Reading A was retired at v0.9; A.3 retires it again with a two-pixel lattice
   model and the assumption that sub-gap re-emission leaves the device. A reviewer will ask what
   the paper gains, whether the no-reabsorption assumption holds in a real SPAD (surface emission
   yes; bulk re-emission at the indirect gap is microsecond-scale and largely reabsorbed or
   non-radiative), and whether "excluded outright" is the right word for a conditional. *Status:
   anticipated; the assumption is named as load-bearing in the addendum. Expect the reviewer to
   downgrade "excluded" to "disfavoured, conditional on the release model".*

8. **P5 is still collapse without dynamics, and A.4 says so twice.** The one-quantum stop acting
   within a thousandth of the commitment time across a beam splitter is the September round's
   item 3 (GRW/CSL's cost without their equations, a foliation chosen not forced). A.4 corroborates
   the premise from the sponsor's model and adds nothing toward supplying it. *Status: known; no
   reply beyond the one the record gives. A reviewer may add that A.7's "cancelled at that instant"
   is the projection postulate written as a race, which the addendum concedes.*

9. **Citation precision in A.3, caught while writing this ledger and fixed before the freeze.**
   The first draft of A.3 cited Grangier et al. 1986 for the no-count side of reading A's failure
   (above 470 nm it predicts silence), but that experiment's beam-splitter photon was the 422.7 nm
   cascade line, below the line, where reading A instead predicts a record at both ports and fails
   through the anticorrelation. The sentence now states both sides with their respective data.
   *Status: fixed 2026-09-14 (ledger M-8). Kept here because a scholarship reviewer would have
   found it, and because the eleven references added at v0.10 are all marked [verify]; if the
   verification is not done before the freeze, expect a scholarship finding on every one of them,
   and it will be deserved.*

10. **The bound-state result of A.5 is the Pauli reduction.** That the lower component of a bound
    Dirac spinor is slaved to the upper, $\chi \approx \boldsymbol\sigma\cdot\mathbf p\,\varphi/2m$,
    in quadrature and small, is the nonrelativistic limit in every textbook; "negative-energy
    content" is representation-dependent and the addendum's numbers ($10^{-6}$, $10^{-16}$) are
    what the reduction gives. A reviewer will say A.5 supports Theorem 2 with a standard fact
    dressed in the sponsor's vocabulary. *Status: anticipated; the addendum offers it as support,
    not novelty. The sponsor's "second spinor" language should be mapped to the standard
    representation explicitly, as the MathX record does (its README: all the Dirac code uses the
    standard representation, not the Weyl one).*

11. **A.6 restates Bell's theorem with a simulation.** A local hidden-variable model gives Bell's
    bound; a detection gate gives the loophole; the projection update gives quantum mechanics.
    None of this needed running, and "Theorem 5's linearity is needed at the second wing" is
    Malus's law. *Status: anticipated; reported as corroboration for the sponsor's model, which
    had proposed the shared-bulk-phase option in earnest. A reviewer may say it belongs in the
    MathX record and not in this paper.*

12. **The conditional-compatibility claim is circular once reading B is adopted.** With the hazard
    linear in the share and the share proportional to $|A_i|^2$ by P1, $P_i \propto |A_i|^2$ is
    the premise restated; §9.1 concedes "P0 and P1 together carry the outcome weights into the
    argument as a premise". A reviewer will ask what the "tested domain" tests. *Status: known
    since v0.6; the answer (the theorems say what would spoil the compatibility, and §8 targets
    those failures) will be judged thin.*

13. **§6.1's timescale ladder is now decorative.** Under reading B there is no gate at $\theta$
    and Theorems 4–5 carry class (ii) at any commit speed, so the ladder's top rung protects
    nothing; yet §6.1 still carries the marginal-silicon, inverted-NbN computation and E-16's
    two flagged uncertainties. *Status: known (v0.9 header, "nothing left for the ladder's top rung
    to protect"); the section should be cut to the two lower rungs or moved to the ledger.*

14. **§8's experiments have no computed magnitude, and the paper's own judgment favours their
    null.** The tabletop discriminator's curvature $\kappa$ has never been computed since v0.6's
    fork; §8.5 says the authors favour the protective reading, under which the experiment returns
    quantum mechanics. A reviewer will say a prediction the authors expect to be null is not a
    prediction. *Status: known; the fork is open problem (i).*

15. **P3(b)'s geometric condition is unverified for the detectors named.** $d \gg \ell$ was flagged
    at v0.6 and is still open for silicon and NbN. *Status: known-open.*

16. **The record was declared closed and reopened ten days later.** The README of 2026-09-05
    closes the program; v0.10 reopens Paper 1 at the sponsor's instruction. A reviewer may say
    "closed" then means nothing, or may say the reopening is the right response to new runs and
    that the closure statement should be amended rather than contradicted. *Status: disclosed in
    the v0.10 header and the addendum ledger; the README's closing paragraph has not been
    amended and should be, with the date.*

17. **AI authorship and self-containment.** The byline lists an AI as first author; the numbers
    live in two GitHub repositories, not in the manuscript. *Status: known; the sponsor's decision;
    the repository's protocol asks the reviewer for the honest byline.*

## Anticipated minor findings

- Addendum A mixes the paper's notation ($e_i$, $A_i$, $s_i$) with MathX's ($d_i$, $\psi(x_i)$,
  $r$, $N$ per port, $\Delta\varphi_i$); one dictionary line is owed.
- Voice shifts in Addendum A between "we", "this paper" and "the sponsor"; the July panel flagged
  authorial voice once already.
- The Fano factor in A.2 is defined for the *share* over $M$ events; the Mandel-$Q$ parenthesis
  applies to the count at one port at fixed $M$. Both are right; a reviewer may want the
  relation written out.
- The v0.10 header note is a page of changelog before the abstract; move the version history to
  an appendix or the ledger and leave a two-line note.
- `[MathX repository]` lists "Claude (Anthropic)" as author; reconcile with `CITATION.cff` and
  the byline convention.
- MathX file paths are cited as references; non-archival, like the framework-repository citation
  the July panel noted.
- A.7 says the Bohm–Dirac transport gives arrivals "by equivariance" without saying that
  equivariance presupposes the $|\psi|^2$ initial distribution, which is quantum equilibrium — the
  same premise the G1/G2 contract holds explicitly.
- "470 nm" and "553 nm" are stated without the gap and photon energies that give them; one line.

## What would count as genuinely new

Anything not reducible to the items above — in particular: an error in the Gumbel-max
identification of A.1 at finite $N$ with the phase weight (the MathX verification passed at
every $N$, but a reviewer may find a case it did not cover); a demonstration that the race with
rates on the conditional state, run with staggered arrival, does *not* recover Born or
exclusivity (item 3 anticipates the defect, not that its fix fails); a published measurement of
super-binomial two-port splitting, or of a hidden per-site variable bounded by counting
statistics, that anticipates or contradicts A.2 (the stochastic-optics literature, Marshall and
Santos, is the place to look); evidence that bulk sub-gap re-emission in silicon is reabsorbed
at a rate that rescues reading A; a named prior work stating that an extreme-value selection rule
with Gumbel noise is the golden rule (the random-utility literature may contain it in another
vocabulary); an internal contradiction between Addendum A and §§3–8 that this ledger did not
name; or an error in the MathX numbers themselves, which are the addendum's only evidence.
