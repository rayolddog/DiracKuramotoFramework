#!/usr/bin/env python3
"""e16_memoryless_hazard_check.py — does a detector's first irreversibility have the
memoryless-hazard structure the energy race needs, and how much memory does the Born
result tolerate?

The energy race (energy_hazard_race.py) gives the Born curve when commitment is a Poisson
event with hazard linear in the energy a clock has absorbed inside its tongue. Fermi's
golden rule gives exactly that structure — a constant rate, linear in the coupling squared
— but only in its regime of validity: the transition rate lambda must be small compared
with the bandwidth of the continuum it decays into, i.e. the bath correlation time
tau_c = 1/Gamma must be short compared with the commitment time 1/lambda. Otherwise the
early-time (quadratic, coherent) growth is not over before the transition completes, the
hazard carries memory, and the process is a cascade rather than a Poisson event.

PART 1 — the detectors, from the E-16 ledger inputs (all literature-typical, none measured
by this program): the Markov ratio lambda * tau_c for each first-irreversibility reading.

PART 2 — the race with a hazard that has memory: each clock's absorbed energy becomes
hazard-bearing only after a lag tau_mem (first-order relaxation H -> E over tau_mem;
tau_mem = 0 is the memoryless race, p = 2.16). Sweep lambda * tau_mem from 0 to ~10, where
lambda ~ c * E is the race's own commitment rate (c = 1, E ~ 10 at peak, so lambda ~ 10 per
time unit and lambda * tau_mem = 1 at tau_mem = 0.1).

PREDICTION, fixed before running: a lag common to both channels leaves the channel ratio
near 2.16 while lambda * tau_mem is small (the Poisson race is insensitive to a common
delay); as the lag grows, commitment is pushed toward the pulse end where the strong
channel's accumulated advantage is larger, so the exponent should rise, and unresolved
trials should appear once the lag approaches the pulse duration (4).

PART 3 — place the detectors on the sweep.
"""

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from energy_hazard_race import race, D_FROZEN  # noqa: E402

# --- Part 1: detectors (E-16 ledger inputs) --------------------------------------------
# Gamma: final-state width / bath relaxation rate (s^-1); tau_c = 1/Gamma.
# lambda: first-irreversibility rate = 1 / (first-irreversibility clock).
DETECTORS = [
    # name, Gamma range, commit-clock range (s), reading
    ("Si SPAD 500 nm, 300 K", (1.5e13, 1.0e14), (10e-15, 1e-12), "interband vertex + thermalisation (device review)"),
    ("InGaAs SPAD 1550 nm (Si inputs, flagged)", (1.5e13, 1.0e14), (10e-15, 1e-12), "as silicon; flagged"),
    ("NbN SNSPD 1550 nm, 2 K — hotspot", (5e10, 1e11), (10e-12, 50e-12), "hotspot -> resistive transition"),
    ("NbN SNSPD 1550 nm, 2 K — cascade", (5e10, 1e11), (100e-15, 1e-12), "quasiparticle cascade onset (uncertain)"),
]

print(__doc__)
print("PART 1 — Markov ratio lambda * tau_c = tau_c / tau_commit (memoryless hazard needs << 1)")
print(f"  {'detector':<44} {'tau_c':>16} {'tau_commit':>16} {'lambda*tau_c':>16}  verdict")
table = []
for name, (g_lo, g_hi), (t_lo, t_hi), reading in DETECTORS:
    tc = (1 / g_hi, 1 / g_lo)
    ratio = (tc[0] / t_hi, tc[1] / t_lo)            # best .. worst
    v = ("memoryless (golden-rule regime)" if ratio[1] < 0.1 else
         "NOT memoryless: commits inside the bath correlation time" if ratio[0] > 1 else
         "MARGINAL: range straddles unity")
    table.append((name, ratio))
    print(f"  {name:<44} {tc[0]*1e15:6.0f}-{tc[1]*1e15:<6.0f} fs {t_lo*1e15:7.0f}-{t_hi*1e15:<7.0f} fs "
          f"{ratio[0]:7.3f}-{ratio[1]:<7.1f}  {v}")
print("  (tau_c from the final-state width Gamma; tau_commit from the first-irreversibility clock; "
      "all literature-typical, E-16 uncertainties #1 and #2 apply.)\n")

# --- Part 2: the race with a hazard that has memory ------------------------------------
t0 = time.time()
trials = 10000
LAGS = [0.0, 0.01, 0.03, 0.1, 0.3, 1.0]
out = []
for tau in LAGS:
    label = f"[gated] Adler power, hazard c*H, c = 1, memory lag tau_mem = {tau} (lambda*tau_mem ~ {10 * tau:.1f})"
    out.append((tau, race(1, 1.0, D_FROZEN, trials, label, mode="gated", m_hazard=1.0, stationary=False,
                          tau_mem=tau)))

print("\nPART 2 — SUMMARY: exponent versus hazard memory (lambda ~ 10 per time unit at c = 1)")
print(f"  {'tau_mem':>8} {'lambda*tau_mem':>15} {'p [95%]':>18} {'dev Born':>9} {'unresolved':>11}")
for tau, (p, (lo, hi), dev_b, unres, slope) in out:
    print(f"  {tau:8.2f} {10 * tau:15.1f} {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {unres:11.3f}")

# --- Part 3: place the detectors ---------------------------------------------------------
print("\nPART 3 — detectors placed on the sweep (by lambda * tau_c against lambda * tau_mem):")
for name, (r_lo, r_hi) in table:
    # nearest sweep points bracketing the detector's range
    below = [tau for tau in LAGS if 10 * tau <= r_lo]
    above = [tau for tau in LAGS if 10 * tau >= r_hi]
    span = f"lambda*tau_c in [{r_lo:.3f}, {r_hi:.1f}]"
    print(f"  {name:<44} {span}")
print(f"\nrun time {time.time() - t0:.0f} s")
