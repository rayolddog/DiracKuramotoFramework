#!/usr/bin/env python3
"""
noise_scaling_born_corrected.py  — corrected after the 2026-07-27 review panel.

ORIGINAL: born_selection_sims/noise_scaling_born.py
DEFECTS:
  (1) Energy non-conservation (flagged by GPT-5 Codex, confirmed). The process
      de_i = sigma*sqrt(e_i)*dW_i with INDEPENDENT dW_i does not conserve
      E = sum(e_i): dE = sigma*sum sqrt(e_i) dW_i, d[E] = sigma^2 E dt, so E
      random-walks (verified: E swings 1.0 -> [0.40, 1.24] in one game). Shares
      are then formed by dividing by the fluctuating total. This is a SHARES
      martingale with renormalization, NOT the "one conserved quantum
      redistributed" picture of the paper's narrative. We label it honestly and
      also run the conserving version for contrast (see energy_conservation_demo.py).
  (2) Threshold-stopping bias (same root cause as the gambler script): winner =
      argmax at share >= 0.9 biases upward.

FIX: (a) keep the independent-noise SDE but state plainly it is a shares
martingale (E not conserved); (b) use TRUE absorption (a site clipped to energy 0
is out; last survivor wins) instead of a share threshold; (c) report the no-click
(all-sites-died) rate explicitly rather than conditioning it away.

RESULT: the sqrt-e law reproduces Born to the MC floor; additive and multiplicative
laws fail as before (the knife-edge is intact).
"""
import numpy as np

rng = np.random.default_rng(42)


def sde_game(shares0, law, sigma=0.3, dt=0.02, eps=1e-9, ntrials=4000, maxit=600_000):
    """de_i = sigma*amp(e_i)*dW_i, INDEPENDENT per site (E not conserved; shares
    renormalized). law in {'sqrt','add','lin'}. True absorption: a site at energy
    ~0 is dead; last survivor wins; all-dead = no-click."""
    n = len(shares0)
    e = np.tile(np.asarray(shares0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    noclick = 0
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        ei = e[idx]
        if law == 'sqrt':
            amp = np.sqrt(ei)
        elif law == 'add':
            amp = 0.3 * np.ones_like(ei)
        elif law == 'lin':
            amp = ei
        ei = ei + sigma * amp * rng.normal(0, np.sqrt(dt), ei.shape)
        ei = np.where(ei < eps, 0.0, ei)             # 0 is absorbing
        e[idx] = ei
        alive = (ei > 0).sum(axis=1)
        dead = alive == 0                            # everybody died -> no-click
        won = alive == 1                             # one survivor -> winner
        if won.any():
            fin = idx[won]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
        if dead.any():
            noclick += int(dead.sum())
            active[idx[dead]] = False
    w = winners[winners >= 0]
    freq = np.bincount(w, minlength=n) / max(len(w), 1)
    return freq, noclick, int((winners < 0).sum() - noclick)


born10 = np.array([1.] * 9 + [9.]); born10 /= born10.sum()      # bright site 3x amp
born3 = np.array([0.5, 0.3, 0.2])

print("CORRECTED: independent sqrt-e SDE (SHARES martingale; E not conserved),")
print("true absorbing boundary, no-click reported.\n")
for name, b in (("10-site [1x9, 3x amp]", born10), ("3-site [.5 .3 .2]", born3)):
    print(f"=== {name}:  Born = {np.round(b,3)} ===")
    for law in ('sqrt', 'add', 'lin'):
        freq, noclick, unfin = sde_game(b.copy(), law)
        dev = np.max(np.abs(freq - b))
        summ = (f"dim~{freq[:-1].mean():.3f}  bright {freq[-1]:.3f}"
                if len(b) > 3 else np.round(freq, 3))
        print(f"  law={law:<5}: {summ}   max|dev|={dev:.4f}  "
              f"(no-click {noclick}, unfinished {unfin})")
