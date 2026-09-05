#!/usr/bin/env python3
"""Noise-off race at the longest commitment time: stationary, window 32, 64 clocks, D = 0, c = 2.5e-4. See PREDICTIONS_energy_race_adiabatic.md, third addendum."""
import time
from energy_race_adiabatic import race_on, flat
t0 = time.time()
p, lo, hi, dev_b, slope, unres, pa30 = race_on(flat(64), 32.0, True, 2.5e-4, 0.0, 5000)
print(f"NOISEOFF stationary T=32, 64 clk, c=0.00025, D=0   {p:6.2f} [{lo:.2f}, {hi:.2f}] {dev_b:9.1f} {slope:6.2f} {unres:6.3f} {pa30:8.3f}   {time.time()-t0:7.0f} s")
print(f"run time {time.time()-t0:.0f} s")
