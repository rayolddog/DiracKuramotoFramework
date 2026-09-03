#!/usr/bin/env python3
"""vertex_exclusivity_discriminator.py — ensemble versus one-world selection at the vertex.

The energy race gives the Born curve when each site commits as a stochastic event with
hazard linear in its absorbed energy. Two readings of that stochastic selection remain:
  ENSEMBLE   the golden rule gives independent rates at every site; in a single trial
             nothing forbids two separated sites from both committing;
  ONE-WORLD  exactly one site commits per quantum; the race enforces this by the
             first-commit stop, which the plan calls imposed bookkeeping, not derived.
The observable that separates them is the coincidence rate between the two channels of a
balanced split fed with single photons: item 2b's heralded 505 nm source gives
g2(0) = 0.0023 with silicon SPADs. This script computes, in the race's own units,
  (a) what independent hazards predict for the double-commit fraction (ensemble);
  (b) what the first-commit stop predicts (one-world: zero, up to same-step ties);
  (c) a one-world rule with FINITE-SPEED exclusivity — after the first commit anywhere,
      the other channel keeps its hazard for a delay tau_x before it is switched off — as a
      curve of double-commit fraction against tau_x, and the tau_x at which it meets the
      observed bound; then converts that tau_x to physical time through the E-16
      first-irreversibility clocks and compares it with the light-crossing time of a
      laboratory beamsplitter separation.
Same race as energy_hazard_race.py (gated, Adler power, hazard c*E with c = 1, noise
0.08); per-trial commit times of the two channels are generated independently, which is
exactly the ensemble model; the rules differ only in how the pair is read.
"""

import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from energy_hazard_race import channel_commit, D_FROZEN, DURATION, CENTRE, K_TOTAL  # noqa: E402
from analysis import wilson  # noqa: E402

G2_BOUND = 0.0023          # heralded 505 nm, silicon SPADs (item 2b)
DT = 2.0 ** -8             # finer than the race's 2^-6: the tie floor scales with the step
TAUS = [DT, 2 * DT, 4 * DT, 8 * DT, 3e-2, 1e-1, 3e-1, 1.0]
trials = 20000

print(__doc__)
t0 = time.time()
for deg in (45, 20):
    KA, KB = K_TOTAL * math.cos(math.radians(deg)), K_TOTAL * math.sin(math.radians(deg))
    cA, _ = channel_commit(KA, 1, 1.0, D_FROZEN, trials, mode="gated", dt=DT)
    cB, _ = channel_commit(KB, 1, 1.0, D_FROZEN, trials, mode="gated", dt=DT)
    a_ok, b_ok = ~np.isnan(cA), ~np.isnan(cB)
    pA, pB = a_ok.mean(), b_ok.mean()
    both = (a_ok & b_ok).mean()
    start = CENTRE - DURATION / 2
    latA = np.nanmean(cA) - start
    latB = np.nanmean(cB) - start
    print(f"\n===== phi = {deg} deg: K_A = {KA:.3f}, K_B = {KB:.3f}, {trials} trials")
    print(f"  single-channel commit probabilities  P(A) = {pA:.3f}   P(B) = {pB:.3f}")
    print(f"  mean commit latency from pulse start  A {latA:.3f}   B {latB:.3f}  (pulse duration {DURATION})")
    print(f"  (a) ENSEMBLE, independent hazards, no exclusivity: P(both commit) = {both:.3f}; "
          f"g2-like ratio P(both)/(P(A)P(B)) = {both / (pA * pB):.3f}   [observed 0.0023]")
    # (b) first-commit stop
    tie = (a_ok & b_ok & (cA == cB)).mean()
    print(f"  (b) ONE-WORLD, first-commit stop: doubles = 0 by rule; same-step ties {tie:.4f} at dt = {DT:.4g} "
          f"(a discretisation floor — exact simultaneity has zero probability in continuous time; excluded below)")
    # (c) finite-speed exclusivity: doubles = strictly separated commits within tau_x of each other
    diff = np.abs(cA - cB)
    sep = a_ok & b_ok & (diff > 0)
    print(f"  (c) ONE-WORLD with finite-speed exclusivity: fraction of trials with both channels committing "
          f"within tau_x of each other (ties excluded)")
    print(f"      {'tau_x':>8} {'tau_x/latency':>14} {'P(double)':>10} {'[Wilson 95%]':>18}")
    fr = []
    for tau in TAUS:
        m = sep & (diff <= tau + 1e-12)
        d, k = m.mean(), int(m.sum())
        lo, hi = wilson(k, trials)
        fr.append(d)
        print(f"      {tau:8.4f} {tau / latA:14.5f} {d:10.4f} [{lo:.4f}, {hi:.4f}]")
    # density of |cA - cB| at zero from the first resolvable bins, and the critical delay
    rho = fr[1] / (2 * DT)              # P(0 < diff <= 2 dt) / (2 dt)
    tau_lin = G2_BOUND / rho
    fr = np.array(fr)
    T = np.array(TAUS)
    if fr[0] < G2_BOUND < fr[-1]:
        j = int(np.searchsorted(fr, G2_BOUND))
        tau_star = math.exp(np.interp(math.log(G2_BOUND), np.log(fr[j - 1:j + 1]), np.log(T[j - 1:j + 1])))
    else:
        tau_star = tau_lin
    print(f"\n  density of commit-time differences at zero: rho = {rho:.3f} per race unit; "
          f"linear estimate tau_x* = {G2_BOUND}/rho = {tau_lin:.2e}; interpolated tau_x* = {tau_star:.2e}")
    print(f"  tau_x at which P(double) = {G2_BOUND}:  {tau_star:.2e} race units = {tau_star / latA:.2e} of the mean "
          f"commit latency = {tau_star / DURATION:.2e} of the pulse")
    # physical conversion through the E-16 first-irreversibility clocks (latency <-> commit clock)
    print("  Converting with the E-16 first-irreversibility clock as the race's commit latency:")
    for name, (lo_s, hi_s) in (("Si SPAD (10 fs - 1 ps)", (10e-15, 1e-12)),
                               ("NbN SNSPD hotspot (10 - 50 ps)", (10e-12, 50e-12))):
        tx_lo, tx_hi = tau_star / latA * lo_s, tau_star / latA * hi_s
        print(f"    {name:<32} tau_x = {tx_lo * 1e15:8.3f} - {tx_hi * 1e15:8.1f} fs;  light travels "
              f"{tx_lo * 3e8 * 1e6:8.3f} - {tx_hi * 3e8 * 1e6:8.1f} um in that time")
    print("    A laboratory beamsplitter separates its output ports by 1 mm to 1 m: light-crossing 3 ps to 3 ns.")
print(f"\nrun time {time.time() - t0:.0f} s")
