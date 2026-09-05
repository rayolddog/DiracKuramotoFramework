#!/usr/bin/env python3
"""Run A of the review round: the recoverability crossover for Gamma/K from 0.2 to 1000, Markov
(non-Hermitian) form of the record-untouched echo. Predictions in PREDICTIONS_review_runs.md."""
import math, numpy as np
from scipy.linalg import expm
K = 1.0
DPOS = np.logspace(-1.5, 3.5, 121)   # Delta/K from 0.03 to 3000

def R_echo(delta, gamma, t):
    Hf = np.array([[0.0, K], [K, delta - 0.5j * gamma]], complex)
    He = np.array([[0.0, -K], [-K, -delta - 0.5j * gamma]], complex)
    psi = expm(-1j * He * t) @ (expm(-1j * Hf * t) @ np.array([1.0, 0.0], complex))
    return abs(psi[0]) ** 2

def midpoint(gamma, t):
    rate = np.array([-math.log(max(R_echo(d, gamma, t), 1e-300)) / (2 * t) for d in DPOS])
    r0 = -math.log(max(R_echo(0.0, gamma, t), 1e-300)) / (2 * t)
    f = rate / r0
    for i in range(len(f) - 1):
        if (f[i] - 0.5) * (f[i + 1] - 0.5) <= 0:
            s = (f[i] - 0.5) / (f[i] - f[i + 1])
            return math.exp(math.log(DPOS[i]) + s * (math.log(DPOS[i + 1]) - math.log(DPOS[i]))), r0
    return float("nan"), r0

print(f"{'Gamma/K':>8} {'t':>8} {'rate(0)':>9} {'x50 (Delta/K)':>14} {'sqrt(G^2/4+2K^2)/K':>19} {'Gamma/2K':>9}")
for gamma, t in ((0.2, 3.0), (1.0, 3.0), (10.0, 3.0), (100.0, 25.0), (1000.0, 250.0)):
    x50, r0 = midpoint(gamma, t)
    print(f"{gamma:8.1f} {t:8.1f} {r0:9.4f} {x50:14.3f} {math.sqrt(gamma*gamma/4 + 2*K*K)/K:19.3f} {gamma/(2*K):9.3f}")
