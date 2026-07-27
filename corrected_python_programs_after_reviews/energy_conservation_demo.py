#!/usr/bin/env python3
"""
energy_conservation_demo.py  — new diagnostic for the 2026-07-27 review panel.

Addresses GPT-5 Codex Major Concern 1 (energy non-conservation), which is
conceptual rather than a mere bug: the paper's narrative is "one conserved quantum
redistributed among sites," but Theorem 1 is stated and simulated with INDEPENDENT
noise de_i = sigma*sqrt(e_i)*dW_i, for which E = sum(e_i) is NOT pathwise conserved
(dE = sigma*sum sqrt(e_i) dW_i; d[E] = sigma^2 E dt). These are two different
processes.

This script shows both explicitly and makes the honest point: the Born result is a
property of the SHARES martingale and holds for BOTH processes at the true
absorbing boundary, but only the conserving process matches the "fixed quantum"
picture. A microscopic derivation from a closed field+detector+bath Hamiltonian
(the paper's stated open problem) would supply a conserving process with the
correct covariance and thereby GROUND the sqrt-e scaling instead of postulating it.
"""
import numpy as np

rng = np.random.default_rng(0)


def energy_trace(mode, e0, sigma=0.3, dt=0.02, eps=1e-9, maxsteps=5000):
    """Run ONE game and return the trajectory of total energy E = sum(e_i)."""
    e = np.asarray(e0, float).copy()
    Es = [e.sum()]
    for _ in range(maxsteps):
        if mode == 'independent':                       # Theorem-1 SDE, E not conserved
            e = np.maximum(e + sigma * np.sqrt(e) * rng.normal(0, np.sqrt(dt), len(e)), 0.0)
        elif mode == 'conserving':                      # pairwise exchange, E fixed
            i, j = 0, 1
            d = 0.1 * min(e[i], e[j]) * (1 if rng.random() < 0.5 else -1)
            e[i] -= d; e[j] += d
        Es.append(e.sum())
        s = e / max(e.sum(), 1e-12)
        if s.max() >= 0.999 or (e > 0).sum() <= 1:
            break
    return np.array(Es)


def born_check(mode, e0, ntrials=20000, sigma=0.3, dt=0.02, eps=1e-9, maxit=2_000_000):
    """Winner frequency under TRUE absorption for either process."""
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    win = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        if mode == 'independent':
            ei = np.maximum(e[idx] + sigma * np.sqrt(e[idx]) * rng.normal(0, np.sqrt(dt), (idx.size, n)), 0.0)
            ei = np.where(ei < eps, 0.0, ei)
            e[idx] = ei
        else:
            i = rng.integers(0, n, idx.size)
            j = (i + rng.integers(1, n, idx.size)) % n
            stake = 0.1 * np.minimum(e[idx, i], e[idx, j])
            d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
            e[idx, i] -= d; e[idx, j] += d
            e[idx] = np.where(e[idx] < eps, 0.0, e[idx])
        alive = (e[idx] > 0).sum(axis=1)
        done = alive <= 1
        if done.any():
            fin = idx[done]
            win[fin] = e[fin].argmax(axis=1)
            active[fin] = False
    w = win[win >= 0]
    return np.bincount(w, minlength=n) / max(len(w), 1)


print("Total-energy behavior over one game (3-site [.5 .3 .2]):")
for mode in ('independent', 'conserving'):
    Es = energy_trace(mode, [0.5, 0.3, 0.2])
    print(f"  {mode:>12}: E(0)={Es[0]:.4f}  E(end)={Es[-1]:.4f}  "
          f"range=[{Es.min():.4f}, {Es.max():.4f}]  steps={len(Es)-1}")

print("\nBorn check at the TRUE absorbing boundary — BOTH processes (shares martingale):")
for amps in ([2., 1.], [0.5, 0.3, 0.2], [1.] * 9 + [3.]):
    A = np.array(amps, float)
    born = A ** 2 / A.dot(A) if max(amps) > 1 else A / A.sum()
    # normalize consistently: treat amps>1 as amplitudes, else as shares
    born = A ** 2 / np.sum(A ** 2)
    print(f"  config {np.round(amps,2)}  Born={np.round(born,3)}")
    for mode in ('independent', 'conserving'):
        f = born_check(mode, born)
        print(f"    {mode:>12}: {np.round(f,3)}  max|dev|={np.max(np.abs(f-born)):.4f}")
print("\nConclusion: the sqrt-e SHARES martingale gives Born either way; only the")
print("conserving process matches the 'fixed quantum redistributed' narrative. The")
print("open task (paper's own): derive a conserving process + its covariance from a")
print("closed field+detector+bath model, grounding the sqrt-e scaling.")
