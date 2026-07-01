#!/usr/bin/env python3
r"""
finite_time_weights.py
======================

Question: the dissipative lock is NOT instantaneous. Given finite settling time,
shouldn't the ATTRACTOR STRENGTH (rate of pull / well depth) matter more than the
BASIN AREA (volume) for which pointer a run ends in -- and could that carry |alpha|^2?

Three things to separate, in the chiral-pair qubit measured along sigma_x
(pointers |+-x> = phi=0, pi).  x := <sigma_x>;  Born weight P(+x) = (1+x0)/2.

(I)  ATTRACTOR STRENGTH (symmetric case):  dphi/dt = -gamma sin 2phi.
     Linearize at phi=0 and phi=pi -> BOTH have rate 2*gamma. Equal strength.
     Strength is a property of the DYNAMICS (gamma), not of the initial state,
     so it cannot encode |alpha|^2.  (Biased case below: 2*gamma +- epsilon.)

(II) The real stochastic selection:  x performs a driftless bounded random walk
     (a MARTINGALE) with absorbing pointers at x=+-1.  Optional stopping ->
     P(absorb at +1) = (1+x0)/2 = Born, and E[x(t)] = x0 at EVERY finite time.
     So the asymptotic weight is time-independent; finite time does not shift it.

(III) FINITE-TIME / incomplete collapse:  before full absorption, the split AMONG
     already-locked runs is skewed toward the NEARER pointer (reached faster), then
     relaxes to Born as gamma*t -> infinity.  This is the user's instinct, made
     precise -- but it is a DEVIATION FROM Born, not a route TO it.

This script measures (II) and (III) by direct vectorized quantum-trajectory
simulation, and prints the attractor-strength symmetry (I).
"""

import numpy as np

gamma = 1.0
x0_target = 0.70                       # tilted state; Born P(+x) = 0.85
# |psi0> = cos(tt/2)|L> + sin(tt/2)|R>, <sx>=sin(tt)
tt = np.arcsin(x0_target)
psi0 = np.array([np.cos(tt / 2), np.sin(tt / 2)], dtype=complex)
born_plus = (1 + x0_target) / 2

print("=" * 78)
print("(I) ATTRACTOR STRENGTH vs BASIN AREA  (deterministic phase flow)")
print("=" * 78)
print("  symmetric lock dphi/dt = -gamma sin2phi:")
print("    rate at phi=0  : 2*gamma = %.2f" % (2 * gamma))
print("    rate at phi=pi : 2*gamma = %.2f   -> EQUAL strength (and area 50/50)" % (2 * gamma))
print("  biased lock dphi/dt = -gamma sin2phi - eps sinphi (eps=0.4):")
eps = 0.4
print("    rate at phi=0  : 2*gamma+eps = %.2f  (stronger, deeper)" % (2 * gamma + eps))
print("    rate at phi=pi : 2*gamma-eps = %.2f" % (2 * gamma - eps))
print("  => strength CAN differ -- but only via eps (a bath/bias property),")
print("     NEVER via the initial amplitude. Attractor strength is state-independent,")
print("     so it cannot carry |alpha|^2.")


# ---- vectorized quantum-state-diffusion for continuous sigma_x measurement ----
def apply_M(psi, ex):
    """(sigma_x - <sigma_x>) |psi> for a batch psi shape (N,2), ex shape (N,)."""
    out = np.empty_like(psi)
    out[:, 0] = psi[:, 1] - ex * psi[:, 0]
    out[:, 1] = psi[:, 0] - ex * psi[:, 1]
    return out


def run(N=40000, T=10.0, dt=2e-3, seed=1):
    rng = np.random.default_rng(seed)
    psi = np.tile(psi0, (N, 1)).astype(complex)
    nsteps = int(T / dt)
    checkpoints = {}
    targets = [0.5, 1.0, 2.0, 4.0, 8.0]
    tgt_steps = {int(t / dt): t for t in targets}
    for i in range(nsteps):
        ex = np.real(np.conj(psi[:, 0]) * psi[:, 1] + np.conj(psi[:, 1]) * psi[:, 0])
        dW = rng.normal(0.0, np.sqrt(dt), size=N)
        Mpsi = apply_M(psi, ex)
        drift = -0.5 * gamma * apply_M(Mpsi, ex)
        psi = psi + drift * dt + np.sqrt(gamma) * Mpsi * dW[:, None]
        psi /= np.linalg.norm(psi, axis=1, keepdims=True)
        if (i + 1) in tgt_steps:
            xq = np.real(np.conj(psi[:, 0]) * psi[:, 1] + np.conj(psi[:, 1]) * psi[:, 0])
            checkpoints[tgt_steps[i + 1]] = xq.copy()
    xf = np.real(np.conj(psi[:, 0]) * psi[:, 1] + np.conj(psi[:, 1]) * psi[:, 0])
    return checkpoints, xf


print("\n" + "=" * 78)
print("(II)+(III) FINITE-TIME WEIGHTS  (40000 trajectories, x0=0.70, Born P(+x)=0.850)")
print("=" * 78)
cps, xf = run()
print(f"  {'gamma*t':>8} | {'E[x](t)':>8} | {'%locked':>8} | {'P(+x|locked)':>13} | dev from Born")
print("  " + "-" * 66)
for t in sorted(cps):
    x = cps[t]
    Ex = np.mean(x)
    locked = np.abs(x) > 0.9
    frac_locked = np.mean(locked)
    if locked.sum() > 0:
        p_plus_locked = np.mean(x[locked] > 0)
    else:
        p_plus_locked = float("nan")
    print(f"  {gamma * t:8.1f} | {Ex:8.3f} | {100*frac_locked:7.1f}% | "
          f"{p_plus_locked:13.3f} | {p_plus_locked - born_plus:+.3f}")
# asymptotic
xfl = np.abs(xf) > 0.9
print(f"  {'asymp':>8} | {np.mean(xf):8.3f} | {100*np.mean(xfl):7.1f}% | "
      f"{np.mean(xf[xfl] > 0):13.3f} | {np.mean(xf[xfl] > 0) - born_plus:+.3f}")

print("\n" + "=" * 78)
print("VERDICT")
print("=" * 78)
print("""  - E[x](t) stays at x0=0.70 for ALL t (martingale): the *mean* weight, hence the
    asymptotic Born split, is TIME-INDEPENDENT. Finite time does not move it.
  - Among already-locked runs at SHORT times, P(+x|locked) is ABOVE the Born 0.850
    (the nearer pointer is reached faster), relaxing DOWN to 0.850 as gamma*t grows.
    So finite time produces a DEVIATION FROM Born (over-weighting the nearer state),
    not a derivation OF it.
  - Attractor strength is symmetric (2*gamma both wells) and state-independent, so it
    is 50/50 just like basin area and cannot encode |alpha|^2. The quantum weight
    lives ONLY in the initial projection x0, conserved by the martingale.
  CONCLUSION: the finite-time / attractor-strength idea is dynamically correct for
  capture from a distribution, but it does NOT rescue the Born derivation. It instead
  predicts small finite-time (weak/short-measurement) deviations from Born that must
  vanish as gamma*T -> infinity -- a falsifiable handle, not a route to |alpha|^2.""")
