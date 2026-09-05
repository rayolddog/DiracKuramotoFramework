#!/usr/bin/env python3
"""Small-hazard stationary races: commitment pushed past the locking transient. See PREDICTIONS_energy_race_adiabatic.md, second addendum."""
import time, sys
from energy_race_adiabatic import race_on, flat
from energy_hazard_race import D_FROZEN
t0 = time.time()
for c in (1e-3, 2.5e-4):
    p, lo, hi, dev_b, slope, unres, pa30 = race_on(flat(64), 32.0, True, c, D_FROZEN, 5000)
    print(f"SMALLC stationary T=32, 64 clk, c={c:g}   {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {slope:6.2f} {unres:6.3f} {pa30:8.3f}   {time.time()-t0:7.0f} s"); sys.stdout.flush()
print(f"run time {time.time()-t0:.0f} s")
