---
title: "Plain-English walkthrough: deterministic Adler controls"
kind: spec
---

# Plain-English walkthrough: deterministic Adler controls

## The result in one paragraph

The completed model correctly reproduces the deterministic Adler synchronization picture. A clock whose frequency mismatch is small enough can settle into a stable phase. A clock whose mismatch is too large keeps slipping. As the photon pulse rises and falls, it opens and closes the synchronization region. Clocks near its boundary enter late and synchronize slowly, so many run out of interaction time. Giving those same clocks a longer pulse recovers them. Separately, summing the ideal relaxation speeds across a flat population of clock mismatches produces a quantity proportional to the square of coupling strength. That last result is an analytic target, not a simulated detection probability.

The implementation and independent review are closed with 26 checks passing. Nothing here yet produces a detector outcome.

## A simple mental picture

Imagine a row of small clocks. Each naturally runs a little faster or slower than a reference clock.

- **Frequency mismatch** says how far a clock's natural rate differs from the reference.
- **Coupling** says how strongly the reference pulls on it.
- **Inside the Arnold tongue** means the pull is strong enough for a stable phase relationship to exist.
- **Locking** means the clock has actually moved sufficiently close to that stable phase.
- **Commitment** would mean it stayed there long enough to create a detector event. Commitment is not implemented yet.

The photon pulse is represented as a smooth rise and fall in coupling strength. The tongue starts closed, opens as the pulse grows, reaches its widest point at the pulse peak, and closes as the pulse passes.

This creates three distinct questions:

1. Was the clock ever admitted into the tongue?
2. Did it reach the lock region before the tongue closed?
3. Would it remain locked long enough to commit?

The present code answers the first two deterministic questions. It does not answer the third.

## What the coupling-squared calculation means

Two features of the stationary tongue both grow with coupling strength:

1. Stronger coupling admits a wider range of clock mismatches.
2. Stronger coupling also makes clocks inside that range relax faster.

For a perfectly flat population of frequency mismatches, combining width with relaxation speed gives a total proportional to coupling strength squared. Geometrically, the relaxation speeds form a semicircular profile across the tongue, and the relevant total is the area under that semicircle.

This is mathematically interesting because coupling can later be made proportional to photon amplitude. But it is not yet the Born rule. The missing question is whether real noisy first-commitment events sample that analytic total. The current dynamics never receive amplitude squared and never receive the analytic predicted rate.

## How to read the test results

Each check reports a **residual** and a **tolerance**.

- The residual is the measured disagreement between code and the independent expectation.
- The tolerance is the largest disagreement allowed for that check.
- Passing means the residual was below the tolerance.

A tiny residual is evidence that the numerical implementation matches the stated mathematical control. It is not evidence that the physical assumptions behind the model are true.

## Checks 1–6: the stationary one-clock control

### 1. Phase wrapping and circular distance

**Question:** Does the code remember that an angle just below one end of the circle is extremely close to an angle just above the other end?

**Test:** Thousands of angles were wrapped into one standard interval. Distances across the positive/negative boundary were compared with an independent circular calculation.

**Result:** The worst disagreement was about eight million-billionths of a radian.

**Why it matters:** A naive subtraction would sometimes report nearly a full turn of separation when two phases are actually adjacent. That would falsely reset future lock timers.

### 2. Convergence to the stable phase

**Question:** When a stationary clock is inside the tongue, does it actually approach the correct locked phase?

**Test:** Thirty-two starting phases distributed around the full circle were evolved at several frequency mismatches.

**Result:** All approached the predicted stable phase to roughly fourteen decimal places. The second fixed point was also shown to repel rather than attract.

**Why it matters:** Merely finding a point where phase motion stops is insufficient; the code must distinguish the stable point from the unstable one.

### 3. Near-lock relaxation speed

**Question:** Does the simulated clock approach the stable phase at the speed predicted by Adler theory?

**Test:** The late-time decay of phase error was measured at two coupling strengths and several positions from the tongue center toward its boundary.

**Result:** The worst relative disagreement was about four parts in a million.

**Why it matters:** The rate-weighted tongue idea relies on synchronization speed, not just tongue width.

### 4. Critical slowing at the edge

**Question:** Does synchronization become progressively slower near the Arnold-tongue boundary?

**Test:** Clocks were placed increasingly close to the edge, including one at 99.99 percent of the boundary mismatch.

**Result:** The rate dropped by a factor of about 31 and continued to match the independent prediction.

**Why it matters:** This slowing is the reason finite pulse duration can exclude clocks that were technically admitted.

### 5. Phase slipping outside the tongue

**Question:** Does a clock outside the tongue keep rotating rather than falsely settling?

**Test:** Positive and negative mismatches beyond the boundary were evolved and their average slip speeds measured. A just-inside clock was run as a contrasting control.

**Result:** Outside clocks slipped at the predicted speed to within about four parts in a million. The inside control locked.

**Why it matters:** The model must clearly separate no-lock dynamics from slow-lock dynamics.

### 6. Zero coupling

**Question:** Does zero coupling mean no synchronization influence?

**Test:** Zero coupling was tested across zero, tiny, and ordinary mismatches and in a zero-height pulse.

**Result:** No clock was admitted, no stable target was assigned, and a zero-mismatch phase simply remained where it began.

**Why it matters:** The code must not call an inert clock synchronized merely because nothing moves it.

## Checks 7–15: the deterministic photon-pulse control

### 7. Pulse endpoints, peak, symmetry, and area

**Question:** Is the photon envelope the intended smooth raised-cosine pulse?

**Test:** The pulse was checked at both ends, its center, off its support, and at mirrored times. Its total area was also measured. Two hypothetical channels were given the same envelope to confirm that only their peak strengths differed.

**Result:** It was exactly zero at both ends, exactly one at the normalized peak, and symmetric to numerical precision.

**Why it matters:** A shared pulse shape prevents channel preference from entering through different time profiles.

### 8. Independent interior pulse-shape test

**Question:** Could a different smooth pulse pass the coarse endpoint and symmetry checks?

**Test:** Twenty-one off-grid interior points were compared with a raised-cosine formula written independently in the verifier. A specially constructed non-cosine pulse with the same endpoints, peak, symmetry, bounds, and area was used as a counterexample.

**Result:** The real pulse matched exactly. The counterexample failed.

**Why it matters:** An earlier test version was circular and could approve the wrong pulse if its crossing formula was changed consistently. Independent review found and closed that weakness.

### 9. Independent tongue-crossing calculation

**Question:** Are the predicted tongue-entry and exit times independently correct?

**Test:** The implementation's crossing times were compared with both a separately derived inverse calculation and a numerical bisection of the independently written pulse.

**Result:** Agreement was about nine parts in one hundred trillion.

**Why it matters:** The pulse generator and its own inverse must not serve as each other's only evidence.

### 10. Simulated eligibility entry and exit

**Question:** Does the time-stepped simulation switch eligibility where the continuous pulse says it should?

**Test:** Six mismatches were followed while the timestep was repeatedly halved.

**Result:** Every transition lay within half a timestep of the predicted crossing, and the timing error decreased with refinement. Each clock had one continuous eligibility window rather than flickering in and out.
|

**Why it matters:** This connects the continuous tongue geometry to the discrete simulation.

### 11. Near-boundary lag and running out of time

**Question:** Do admitted clocks near the edge actually fail to reach the lock region during a finite pulse?

**Test:** Sixteen evenly spaced starting phases were run at five mismatch values from the tongue center to very near its edge.

**Result:** Central clocks received many relaxation times and nearly all reached the lock region. At the closest edge case, only about 19 percent ever reached it during the pulse, even though every clock was admitted at the peak.

**Why it matters:** Admission is not locking. This is the first direct demonstration of your finite-synchronization-time observation.

### 12. Classification at the exact entry instant

**Question:** Was a clock already inside the lock region when the tongue opened, or did it enter later?

**Test:** Instead of using the first stored time sample, each trajectory was propagated directly to the continuous analytic entry time. The result was compared with a calculation using a timestep 64 times smaller.

**Result:** Phase disagreement was about one tenth of a billionth of a radian, millions of times smaller than the nearest classification boundary. A clock previously misclassified by sampled timing was corrected.

**Why it matters:** It prevents numerical sampling from being mistaken for physical synchronization.

### 13. Recovery with longer pulses

**Question:** Are near-edge failures genuinely caused by insufficient time?

**Test:** The identical sixteen starting phases were reused while pulse duration was increased by factors of four and sixteen.

**Result:** At one near-edge mismatch, the fraction reaching the lock region rose from about 31 percent to 75 percent and then 100 percent. Closer to the boundary it rose from about 19 percent to 44 percent and then 88 percent. These totals were stable under timestep refinement.

**Why it matters:** This is the causal control. A longer interaction recovers the same clocks rather than merely changing the sample population.

### 14. Longer fixed-peak pulses provide longer eligibility

**Question:** Does increasing duration at a fixed peak always give a clock at least as much eligible time?

**Test:** Pulse duration was varied over a wide range at six mismatches.

**Result:** Eligibility time increased monotonically. A separately labeled fixed-area sweep did not behave monotonically, because stretching a fixed-energy pulse lowers its peak and can prevent admission entirely.

**Why it matters:** “Longer pulse” is ambiguous unless one states whether peak strength or total area is held fixed.

### 15. Slow-pulse agreement with the stationary model

**Question:** Does a very slow pulse approach the stationary result near its peak?

**Test:** Pulse duration was increased from 100 to 400 to 1,600 model-time units.

**Result:** The phase at the peak approached the stationary stable phase rapidly, reaching agreement within a few millionths of a radian.

**Why it matters:** It shows that the stationary and pulsed models are two limits of the same dynamics rather than unrelated constructions.

## Checks 16–18: the isolated analytic flat-spectrum control

### 16. Independent half-pi normalization

**Question:** Is the size of the semicircle total correct, not merely its coupling-squared shape?

**Test:** The verifier used its own independent half-pi constant and compared it with the numerical flat-grid sum. A deliberately doubled total was used as a negative control.

**Result:** The real normalization converged correctly; the doubled version failed by roughly 100 percent.

**Why it matters:** Earlier, the implementation and verifier shared the same constant, so a common factor-of-two mistake could pass. Independent review found and closed that circularity.

### 17. Flat-grid sum convergence

**Question:** Does refining a flat frequency-mismatch grid make the total approach coupling squared times the semicircle constant?

**Test:** Twenty-five coupling strengths spanning a factor of ten were evaluated while grid size increased from 2,000 to 64,000 points.

**Result:** The worst normalized error fell from under one percent to about two parts in one hundred thousand. Enlarging already sufficient outer support changed nothing.

**Why it matters:** The coupling-squared arithmetic is a continuum result; this shows the finite grid approaches it honestly.

### 18. Unconstrained fitted exponent

**Question:** If the code is not told the expected exponent, what power of coupling does it measure?

**Test:** A free log-log fit was performed at every grid refinement. The same fitter was tested on tongue width and eligible-clock count, which should be linear rather than quadratic.

**Result:** The fitted exponent converged to two within less than one part per million. The two negative controls returned approximately one.

**Why it matters:** The fitting procedure is not manufacturing a quadratic answer for every dataset.

## Checks 19–26: independence, numerical trust, and honest scope

### 19. Dynamics cannot access the analytic prediction

**Question:** Could the simulation accidentally or deliberately read the coupling-squared answer?

**Test:** The verifier parsed the source code. Dynamics imports are restricted, analytic names are forbidden, and the deterministic dynamics contain no exponentiation operation that could form coupling squared.

**Result:** No forbidden path was found. The analytic module also does not import the dynamics.

**Why it matters:** A later apparent confirmation must emerge from phase evolution and event rules, not from feeding the desired result into the simulator.

### 20. Independent eligibility implementations agree

**Question:** Do the model and analytic sides define the tongue boundary consistently despite being isolated?

**Test:** Their independently written predicates were compared on 200,000 random cases plus exact and one-machine-step-inside boundary cases.

**Result:** There were no disagreements.

**Why it matters:** Isolation should prevent circularity without allowing the two halves to silently study different systems.

### 21. Numerical integrator order

**Question:** Do the time integrators improve at their expected rates when the timestep is refined?

**Test:** Both the high-accuracy deterministic integrator and the simpler Euler integrator were compared with a known trajectory under repeated timestep halving.

**Result:** The high-accuracy error improved by about sixteenfold per halving; Euler improved by about twofold, as expected.

**Why it matters:** This tests the numerical machinery independently of the physics claims. Euler is retained because its stochastic counterpart will be used later.

### 22. Invalid basic inputs are rejected

**Question:** Do undefined or impossible controls fail loudly rather than look like physical no-lock results?

**Test:** Undefined numbers, infinities, negative or zero timesteps, invalid pulse parameters, wrong storage cadence, strings, and booleans were sent into public boundaries.

**Result:** Every invalid case raised the intended error type. Valid cases continued to run.

**Why it matters:** Invalid input once produced plausible “never admitted” results, which would be especially dangerous in this experiment.

### 23. The exported public interface enforces its declared contract

**Question:** Are validation checks applied across the package rather than only to a handpicked few functions?

**Test:** A table covers 56 public functions, constructors, methods, and properties; 112 parameters; and 159 declared invalid calls. It includes negative coupling histories, invalid callbacks, bad trajectory queries, non-Boolean flags, and silent data filtering.

**Result:** All declared invalid calls were rejected, while positive controls—including exactly zero coupling—remained valid.

**Important limitation:** This proves every public parameter has at least one declared probe. It does not automatically derive every possible way a parameter could be invalid. Independent review found a negative-coupling gap even after an earlier table was “complete,” and the documentation now uses that example to prevent overclaiming.

### 24. The verification program prints and fails correctly

**Question:** Can the harness itself hide a failed check or return success after failure?

**Test:** Synthetic pass and failure lists were sent through its summary function. A deliberate command-line failure was also exercised.

**Result:** All registered checks appear in output, and any failure produces a nonzero process exit.

**Why it matters:** Automated checks are useful only if external tools can trust their status.

### 25. Every acceptance criterion is represented

**Question:** Did implementation quietly omit part of the agreed ticket?

**Test:** Each registered check declares which acceptance criteria it covers, and the verifier compares their union with all twenty criteria accumulated through implementation and review.

**Result:** All twenty criteria are covered by the 26 checks.

**Why it matters:** This is a traceability check. It does not substitute for checking whether each test is scientifically strong—which is why the independent reviewer also used mutations and separate calculations.

### 26. Documentation preserves the non-claims

**Question:** Does the package clearly say what has not been demonstrated?

**Test:** The verifier checks the README for explicit statements about missing noise, commitment, competition, Born probabilities, exclusivity, and energy routing.

**Result:** All required non-claims are present.

**Why it matters:** The analytic coupling-squared result is easy to overinterpret. Documentation honesty is part of correctness here.

## What we have learned

The strongest completed finding is not yet the coupling-squared curve. It is the verified finite-time mechanism:

<user_quoted_section>A clock can enter the Arnold tongue without having enough time to synchronize. Near the boundary, critical slowing makes failure increasingly likely; extending the same pulse recovers the same clock phases.</user_quoted_section>

This supports your observation that time available for synchronization must be included. It also creates a serious test for the Born candidate: pulse duration may change only the overall efficiency, or it may change the normalized channel ratio. Only the later stochastic two-channel experiment can tell us which.

The analytic result is a clean target:

<user_quoted_section>With a flat mismatch population, tongue width and interior relaxation speed combine into a coupling-squared total.</user_quoted_section>

But the bridge from that total to detection frequencies remains unproved.

## What remains before a Born-rule claim

The next stages must add, in this order:

1. amplitude-neutral phase noise;
2. a fixed physical lock-band dwell requirement;
3. a single-channel first-commitment-time distribution;
4. two amplitude-linear channels competing under identical rules;
5. a complete ledger of wins, ties, and unresolved pulses;
6. pulse-duration, noise, population, timestep, and spectrum sensitivity;
7. comparison with linear, quadratic, and strongest-channel alternatives using a freely fitted exponent.

Even a robust coupling-squared winner frequency would still not derive energy routing, physical exclusivity, or a microscopic detector theory.

## Suggested review order

1. Read the non-claims at the start of the [package README](/Users/john-bramble/Projects/Physics/DiracKuramotoFramework/adler_born_two_channel/README.md).
2. Review checks 11–14 above; they carry your finite-synchronization-time idea.
3. Review checks 16–19; they separate the analytic prediction from the dynamics.
4. Read the [independent review record](/Users/john-bramble/.traycer/epics/c443d91e-b0d5-43ff-a31b-805574ab7771/artifacts/debates/born-selection-roundtable/adler-tongue-born-candidate/two-channel-stochastic-model/implementation-deterministic-analytic/independent-review/index.md), especially the final closure section. It shows how apparently complete tests were strengthened after adversarial counterexamples.
5. Run `python3 -m adler_born_two_channel.verify --verbose` from `/Users/john-bramble/Projects/Physics/DiracKuramotoFramework` when you want the exact numerical record.

No manuscript files were changed, and the package remains unstaged and uncommitted.
