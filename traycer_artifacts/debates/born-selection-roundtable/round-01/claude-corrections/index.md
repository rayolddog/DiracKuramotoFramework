---
title: "Claude Fable 5 — correction architecture"
kind: spec
---

# Claude Fable 5 — correction architecture (Round 1, independent)

Verified manuscript SHA-256 `453acdad…497f1a227`. Written in the collaborative spirit John asked for: these are repairs offered as shared problem-solving, not verdicts. Each finding has a stable ID and concept tags for later focused lessons.

## CC-1 — The analyzed noise model does not conserve the quantum it is selecting

**Tags:** Itô calculus, stochastic processes, energy conservation.
**Location:** Theorem 1 (§5.1), P4(i) (§2), Appendix A/D.

**Issue.** Theorem 1 analyzes independent site noise $de_i=\sigma\sqrt{e_i},dW_i$. Under it the total $E=\sum_j e_j$ is itself a driftless square-root diffusion (a squared-Bessel-0 process): it fluctuates and almost surely hits zero. So in the model actually proved, the "last survivor" generically holds an energy different from $\hbar\omega$ at the moment it wins — while P4(i) defines class-(i) registration as *assembling the full quantum*. The physical picture (§4: exchange "redistributes the quantum among sites") and the proved model (bath injecting/withdrawing energy site-by-site) are different processes.

**Repair.** Split Theorem 1 into two theorems. (1a) *Conserving-exchange class:* pairwise transfers $de_i=\sum_j g(e_i,e_j),dW_{ij}$ with $dW_{ji}=-dW_{ij}$ conserve $E\equiv\hbar\omega$ exactly, make every share a martingale for **any** symmetric $g$, and terminate with the winner holding the full quantum, provided the zero boundary is absorbing (sticky), not reflecting — the clipped-parcel failure in §4(b) is precisely a reflecting boundary. Fairness here is a robustness result: the load-bearing condition is the boundary behavior, not the $\sqrt e$ law. (1b) *Bath-coupled class:* the current uniqueness proof, governing non-conserving environmental noise, where $\sqrt e$ is the unique drift-free scaling. State plainly that the interference-cross-term sketch (§4) supplies class (1b), and that the conserving derivation of §9.4 is a prerequisite for, not an ornament to, the headline claim.

**Label:** `narrows` (U5). The mechanism survives and in the conserving class becomes *more* robust; what narrows is the "one postulate, both jobs — the $\sqrt e$ knife-edge" rhetoric, whose uniqueness holds only within the bath-noise class.
**Plain English:** the theorem proves fairness for a casino where the bank's total money randomly fluctuates, but the story describes a fixed pot being passed around. In a fixed-pot game fairness is easier to get (good news), but the advertised "unique knife-edge" argument then applies only to the environment's contribution.
**Evidence needed:** the §9.4 conserving open-system calculation, with the boundary behavior of depleted sites derived, not assumed.

## CC-2 — The commit-rate law is derived with Born-rule machinery

**Tags:** Fermi golden rule, circularity, photodetection theory.
**Location:** Theorem 5 (§5.4), Appendix C, §6.2–6.3.

**Issue.** Appendix C computes commit rates from T-matrix elements and "the golden rule gives rate $\propto|M|^2$." Squaring a transition amplitude to get a rate *is* the Born rule — the very structure under derivation. §3 explicitly forbids this move at capture ("reducing the sum to a single diagram presupposes the Born rule"); Appendix C makes the analogous move at registration.

**Repair.** For the single-quantum sector, re-derive the class-(ii) rate from classical energetics, matching P1's own discipline: linear dissipation of an oscillator of energy $e$ transfers energy at rate $\Gamma e$ — linear in occupation, no squared amplitude invoked. That is all Theorem 4 needs, so the single-detector Born result stands on the repaired footing. For $k$-quantum channels ($G^{(k)}$ linearity, hence Glauber statistics and $\rho$-affinity), no Born-free derivation currently exists: downgrade Theorem 5's multi-quantum half to a *consistency condition* (any rate law reproducing QM must be $G^{(k)}$-linear) pending a derivation.

**Label:** `preserves` (U5, U6) for the single-detector claim via the classical-energetics route; `narrows` (U6) for §6.2–6.3, which become conditional results.
**Plain English:** you may not use the rule you are deriving as a tool inside the derivation. The one-photon case can be rescued with the same "oscillator mechanics" move that justified P1; the multi-photon case currently cannot, and should say so.
**Evidence needed:** a commit-rate derivation for $k\ge2$ channels using only P1-style energetics plus energy conservation.

## CC-3 — The tabletop discriminator's signature is degenerate with efficiency mismatch

**Tags:** detector physics, experiment design, POVM.
**Location:** §8.4, Fig. 7, §8.5.

**Issue.** §8.4 claims that for any local POVM the conditional port statistic $P'(S)$ is "exactly affine in $S$." It is not. With port efficiencies $\eta_A\neq\eta_B$, standard QM gives $P'(S)=\eta_AS/[\eta_AS+\eta_B(1-S)]$, and for small mismatch $\delta=(\eta_A-\eta_B)/\bar\eta$ this expands to $S+\delta,S(1-S)$ — *exactly* the predicted $\kappa S(1-S)$ bow (Appendix CC-A). The confound is not merely a calibration nuisance; it has the identical functional form, so bounding $\kappa$ at $10^{-3}$ requires port efficiencies matched or independently known at the $10^{-3}$ level, which the section does not currently demand.

**Repair.** Three-part redesign, any of which rescues the test: (i) use *unconditional* rates against a calibrated source flux, which are genuinely affine under local POVMs; (ii) symmetrize by swapping port roles with an upstream operation (efficiency curvature follows the hardware, $\kappa$ follows the collective structure, so the swap-antisymmetric part isolates $\kappa$); (iii) modulate the correlated port's structure in situ (lattice spacing, $\Delta c_{\rm eff}$) at fixed hardware — $\kappa$ is predicted to track the modulation, $\delta$ is not.

**Label:** `preserves` (U5, U7). The mechanism and its falsifiability survive; the flagship protocol as written would produce an uninterpretable positive and must be repaired before §8.5's fork can lean on it.
**Plain English:** the experiment's fingerprint — a bow in a curve — is also produced by one detector being slightly better than the other. The fix is to design the measurement so a hardware imbalance and the new physics bend the curve in distinguishable ways.
**Evidence needed:** a systematics budget for the redesigned protocol showing $\kappa$ and $\delta$ separate at target sensitivity.

## CC-4 — The entangled sector postulates the update it appears to derive

**Tags:** Born rule, nonlocality, Bell tests.
**Location:** Abstract, §6.2, §7.1, §7.4, §8.7.

**Issue.** P5's faithful registry renormalization ($\eta=1$) *is* the projection postulate, relocated into the medium — it also quietly powers the §6.2 Glauber composition. §7.5 is admirably honest about this, but the abstract still says the construction "yield[s] the full quantum correlations" and that "no-signaling follows," which reads as output rather than input. Separately, the above-Tsirelson prediction (§8.7 Knob 2) rests on modeling a coherent tone as a single-quantum share drift — a model §8.7's own caveats concede is not yet derived; an "$S>2\sqrt2$" claim should not rest on it.

**Repair.** Re-scope §7 (and the abstract) as a *consistency embedding*: the single-detector mechanism composes correctly inside a collapse-carrying nonlocal ontology, with $\eta$ a parametrized failure hypothesis and $S=2\sqrt2,\eta$ its signature. Keep Knob 1 (broadband, $\delta S=4(1-\eta)L$) as the near-term proposal; gate Knob 2 on the multi-quantum treatment already listed in §9.4(vii).

**Label:** `narrows` (U7 affected; U5 untouched). This does not abandon the entangled program — it prices it honestly, which U7 itself demands.
**Plain English:** for entangled pairs the mechanism doesn't explain the spooky update; it assumes a perfect one and shows the rest is then consistent. Valuable, but a different kind of claim, and the paper's front matter should match its own §7.5.
**Evidence needed:** the multi-quantum tone calculation; any dynamical account of $\eta=1$ beyond the rotation picture.

## CC-5 — Theorem 2 can stand on a weaker, safer premise than the $\kappa_{\rm ret}$ ansatz

**Tags:** linear response, synchronization, open quantum systems.
**Location:** Theorem 2 (§5.2), Appendix B, §9.4(viii).

**Issue.** The no-rich-get-richer conclusion currently routes through the unproved ansatz $\kappa_{\rm ret}=\Delta E/\hbar$ (flagged in v0.5.3). But Appendix B.3 shows the fairness argument only needs *concave uptake*: superlinear energy uptake requires gain, and a sub-threshold absorber with no population inversion is a passive linear system — a statement of linear-response theory, independent of $\kappa_{\rm ret}$'s value.

**Repair.** Restate Theorem 2 as: "a gainless (passive) sub-threshold site has linear response, hence uptake $\propto\sqrt e$ (concave, equalizing toward the Born pattern) and share-neutral return; amplification requires autonomy, confined to the layer." The $\kappa_{\rm ret}$ ansatz then sets only timescales and the layer width, not fairness. The quantized-field sub-threshold channel remains the honest residual risk, exactly as §5.2 states.

**Label:** `preserves` (U4). Same mechanism, weaker premise, stronger theorem.
**Plain English:** you don't need to know exactly how fast a failed lock returns energy; you only need that a sub-threshold site can't amplify — passivity, a standard property of gainless systems — to keep leaders from cheating.
**Evidence needed:** the §9.4(viii) microscopic calculation, now needed only for timescales and the layer width, not for fairness itself.

## Synthesis for the round table

**Strongest surviving contribution:** the single-detector selection game — capture energetics (P1), fair exchange, martingale stopping — survives all five findings, and CC-1/CC-5 arguably leave it *more* robust than the manuscript claims. **Strongest objection I could not repair away:** the multi-quantum sector (CC-2's $G^{(k)}$ half plus CC-4's registry) currently reproduces Glauber and Bell statistics partly by construction. **Open question, with a learning path:** whether a conserving microscopic model yields both the fair exchange (CC-1) and a Born-free multi-quantum commit law (CC-2) — the single calculation that would settle the two deepest findings at once; a minimal three-site, two-quantum conserving toy model would be a concrete first step any participant could build and check.

**Questions for the table:** (1) Does anyone see a Born-free derivation of $G^{(k)}$-linearity I've missed? (2) In the conserving-exchange class, what physical principle picks the absorbing over the reflecting zero boundary? (3) Can the port-swap redesign (CC-3 ii) be made loophole-free against polarization-dependent efficiency?

## Appendix CC-A — the efficiency mimic (CC-3)

$P'(S)=\dfrac{\eta_AS}{\eta_AS+\eta_B(1-S)}$; with $\eta_{A,B}=\bar\eta(1\pm\delta/2)$: numerator $\bar\eta S(1+\delta/2)$, denominator $\bar\eta[1+\delta(S-\tfrac12)]$, so $P'(S)\approx S,(1+\delta/2),(1-\delta(S-\tfrac12))=S+\delta S(1-S)+O(\delta^2)$ — the same bow as the predicted $\kappa S(1-S)$.

## Appendix CC-B — non-conservation of the total (CC-1)

Under $de_i=\sigma\sqrt{e_i},dW_i$ (independent), $dE=\sigma\sum_i\sqrt{e_i},dW_i$ has variance rate $\sigma^2E$: each $e_i$, and $E$ itself, is a squared Bessel process of dimension 0 — a martingale absorbed at 0 in finite time a.s. Sites die one by one, so a last survivor with $s=1$ exists (Appendix D's observation), but its absolute energy at that moment is a random variable, not $\hbar\omega$, conflicting with P4(i)'s registration condition. The pairwise-antisymmetric exchange form removes the conflict identically.
