# Third round — findings on v1.3, classified, with proposed v1.4 dispositions (not applied)

*Four reviewers, same personas, fresh contexts, no access to earlier rounds (`reviews_v1.3/`).
Written for the accountable author to read before anything is changed; the paper is
untouched. One measurement the round demanded was run and put in the record first
(`../heisenberg_cut_recoverability/REVIEW_RUNS_RESULTS.md`, Run A′).*

## Scores on v1.3

| reviewer | recommendation | overall | novelty | internal consist. | evidential | reproducibility | citation |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 decoherence theorist | major revision | **2** | 2 | 3 | 2 | 4 | 3 |
| R2 detector experimentalist | major revision | **2** | 2 | 3 | 3 | 4 | 3 |
| R3 foundations philosopher | major revision | **2** | 2 | 3 | 3 | 4 | 4 |
| R4 transactional & scholarship | major revision | **2** | 2 | 3 | 3 | 4 | 3 |

Three rounds, twelve reviews, twelve scores of 2. Novelty 2 in every one. The reviewers
did not pass v1.3.

## What the third round found

**A. Physics corrections to the v1.2 repair (R1 M1, R2 M2; confirmed by Run A′).** The
displayed formula √(Γ²/4 + 2K²) is an interpolation that fails by up to a factor of three
for Γ/K between 1.5 and 7, is non-monotone with a dip at the exceptional point Γ = 4K, and
drifts by a factor of 4 with observation time at Γ/K = 3; "to 15 % from 0.2 to 1000" is
false; "√2 K in the rate convention" is the fit's limit, not the convention's, which
drifts toward 2K/√3; the "factor √3" sentence is arithmetically wrong. *Proposed
disposition:* drop the formula from the abstract; state the two asymptotes only; call the
intermediate region non-monotone and convention-dependent; cite Run A′.

**B. The temperature attribution is backwards (R1 M3, R2 M1).** "Γ/2, set by the record
channel and hence by temperature" is a non sequitur for band absorbers: hot-carrier
relaxation is set by excess energy and is weakly temperature-dependent at 300 K and at
1 K alike, while rare-earth coherence in the Γ ≪ K regime is strongly temperature-
dependent. And "Γ/K of order 10⁵" borrows an atomic dipole's K for a band absorber, with
no derivation in the record. *Proposed disposition:* withdraw "and hence by temperature";
state that the record-set regime's Γ is the hot-carrier relaxation rate and is set by
excess energy; drop the 10⁵ or derive it for a band.

**C. §6's picture paragraph is not self-consistent (R3 M1).** "The nonlocality is the
sharing" conflates sharing with Bell nonlocality — Everett shares the state too; the pull
is the nonlocality; "first is frame-dependent" sits beside a preferred slicing that makes
it definite; a Lorentz-bound residue survives in open problem 2 and in the long form.
*Proposed disposition:* rewrite the paragraph: the sharing is the ontology, the pull is
the nonlocality; the slicing decides "first" unobservably; delete the Lorentz-bound
residue.

**D. The foliation is avoidable by the paper's own lights (R3 M2).** With commuting
site-local jump operators and no local beables, hypersurface-relative conditional states
are available at no cost (Myrvold 2002 is cited on the wrong side; Norsen 2010 is in the
list, uncited). *Proposed disposition:* either drop the preferred slicing from the price
list in favour of hypersurface-relative conditional states, or argue for it.

**E. §7's order-independence paragraph mischaracterizes the experiments and overclaims
(R2 M3, R3 M3).** The before-before and swapping experiments do not refute "a phase sent
to the partner" for any preferred-frame picture, the paper's own included; Stefanov 2002
moved beam splitters, not detectors; Salart 2008 is a speed bound, not a before-before
experiment; Minev 2019 evidences trajectory detector-dependence, not reversible capture;
the circuit-QED experiments cited are diffusive-record experiments the ontic-jump reading
never addresses. "Branch selected, not phase rotated" is basis-relative (steering).
*Proposed disposition:* rewrite the paragraph as consistency only; characterize each
experiment correctly; own the steering point.

**F. "The cut" names three objects, and the postulate's real cut is the FAPP-graded
site–record split (R1 M2, R3 M3).** Bell's shifty split, imported into the beable
dynamics; "commitment is the vertex, not the record" is contradicted by the jump
operator, which acts on the site → record transition for Γ ≪ K. *Proposed disposition:*
one definition of "the cut" — the site–record split on which the jump operators are
defined — stated as FAPP-graded, and the §4.3 sentence reworded.

**G. §5.2 still above its altitude (R1 M3, R2, R4 M3).** Gleason does not constrain the
race models (dynamical extra-variable models), so it is misapplied; the abstract's "no
synchronization substrate can move the outcome weights" contradicts §5.2's 1.08–2.21 —
the correct statement is that a substrate cannot make them Born without Born being put in;
the narrow-band falsification of the substrate is omitted; Run B's physics is already in
the semiclassical-versus-quantum photodetection literature (Clauser 1974; Kimble, Dagenais
& Mandel 1977; Grangier, Roger & Aspect 1986). *Proposed disposition:* restate as a
negative result for the family, citing that literature; delete the Gleason step or scope
it to the graded-weight identity.

**H. The transactional attribution, third attempt (R4 M1, M2).** Marchildon 2017 disputes
the coupling-amplitude-as-probability criterion and the absorber definition, not the
emission × absorption derivation; Boisvert & Marchildon 2013 is cited against a 2018
argument; TI's no-foliation claim is stated as fact without Maudlin's contingent-absorber
counter-price (Kastner 2013 uncited). *Proposed disposition:* one sentence per dispute,
each attributed to its actual paper.

**I. The header (R4 M6, R1).** The three overnight adjudications are not named; a blanket
instruction is presented as their ratification; "reversible with one edit" is false for
two of them. *Proposed disposition:* name them; say the accountable author has not yet
ratified them in his own words; drop "one edit".

**J. Divergence again (R2 M3, R4 M4).** NEGATIVE_RESULT.md and the long form still carry
"a thousandth of the commitment time" and the energy-linear hazard the candidate
withdrew; two §4.2 numbers came from a reviewer's re-run rather than the record (now
replaced by Run A′). *Proposed disposition:* propagate; cite Run A′.

## What three rounds establish

Every revision fixed the previous round's list and introduced errors of its own at a
comparable rate; the overall score never moved from 2, and novelty never moved from 2.
The reviewers' reading is stable across twelve reviews: a priced, honest restatement of
the projection postulate at the decoherence crossover, with a negative result for one
model family, in scope for a foundations venue and not a contribution beyond that. The
first author's assessment for the accountable author: the process has converged on the
paper's status rather than on a passing version, and a fourth internal round would find
a fourth list. The choices are the ones stated after the second round — accept the record
as the deliverable, or recast the paper as the priced restatement and nothing more — with
item A and item B applied in either case, since they are corrections of fact.
