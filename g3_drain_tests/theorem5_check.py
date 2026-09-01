"""Theorem 5 check: is Born robust to the COMMIT-RATE LAW in continuum absorbers?

Paper 1, Theorem 4: if the conditional site pick is ∝ s_i, Born holds at ANY
commit speed. Theorem 5: the commit rate IS linear in occupation, because each
absorption vertex is amplitude-linear (P2) and a rate ∝ e_i^2 would need two
vertices depositing 2*hbar*omega into a state that does not exist.

Theorem 5's argument is about ABSORPTION VERTICES. Real continuum detectors put
a downstream ACTIVATION barrier after absorption (vortex crossing in an SNSPD,
triggering in a SPAD, latent-image nucleation in film), whose rate is Arrhenius,
exp(-dU/kT), with dU falling as deposited energy rises -> rate ~ exp(beta*e).

Test: separate commit SPEED (q, per-step firing probability) from commit LAW
(f(e), the pick weight). Theorem 4 says f(e)=e gives Born at every q.

Validation anchor: paper reports alpha=2, fast commit, 2 sites at 0.8/0.2
-> P1 = 0.941 predicted, 0.938 observed.
"""
import numpy as np


def run(weights, law, q, param=None, step=0.25, n_trials=40000,
        max_steps=400_000, seed=0):
    rng = np.random.default_rng(seed)
    w = np.asarray(weights, float)
    born = w / w.sum()
    N = len(w)
    e = np.tile(born, (n_trials, 1))
    winner = np.full(n_trials, -1, int)
    idx = np.arange(n_trials)

    def f(x):
        if law == "linear":  return x
        if law == "power":   return x**param
        if law == "arr":     return np.exp(param * x)     # Arrhenius in deposit
        raise ValueError(law)

    for k in range(max_steps):
        T = e.shape[0]
        if T == 0:
            break
        # fair stakes-scaled exchange
        i = rng.integers(0, N, size=T)
        j = (i + rng.integers(1, N, size=T)) % N
        r = np.arange(T)
        ei, ej = e[r, i], e[r, j]
        d = step * np.minimum(ei, ej) * np.where(rng.random(T) < 0.5, 1.0, -1.0)
        e[r, i] = ei + d
        e[r, j] = ej - d

        # commit: fires with prob q per step, site picked ∝ f(e_i)
        fire = rng.random(T) < q
        if fire.any():
            wts = f(e[fire])
            wts = wts / wts.sum(axis=1, keepdims=True)
            cum = np.cumsum(wts, axis=1)
            u = rng.random((wts.shape[0], 1))
            winner[idx[fire]] = (u > cum).sum(axis=1)

        # absorbing boundary, evaluated for the trials that did NOT fire
        done = (~fire) & (e.max(axis=1) >= 0.995)
        if done.any():
            winner[idx[done]] = e[done].argmax(axis=1)

        gone = fire | done
        if gone.any():
            keep = ~gone
            e, idx = e[keep], idx[keep]

    p = np.bincount(winner[winner >= 0], minlength=N) / max((winner >= 0).sum(), 1)
    return born, p


two = [0.8, 0.2]
print("VALIDATION: 2 sites, Born 0.800/0.200, fast commit (q=0.5), rate ~ s^2")
print("            paper reports P1 = 0.941 predicted, 0.938 observed")
b, p = run(two, "power", q=0.5, param=2.0, seed=7)
print(f"            this implementation: P1 = {p[0]:.3f}\n")

print("Theorem 4 test: does the LINEAR law give Born at every commit speed?")
for q in (0.5, 0.1, 0.01, 0.001):
    b, p = run(two, "linear", q=q, seed=11)
    print(f"   q={q:<7} P1 = {p[0]:.4f}   (Born 0.8000, dev {p[0]-0.8:+.4f})")

print("\nWhat a downstream ARRHENIUS barrier does (rate ~ exp(beta*e)), q=0.5:")
for beta in (0.5, 2.0, 5.0, 10.0, 20.0):
    b, p = run(two, "arr", q=0.5, param=beta, seed=13)
    print(f"   beta={beta:<6} P1 = {p[0]:.4f}   (dev {p[0]-0.8:+.4f})")

print("\nSame, slow commit q=0.001 (does first passage rescue it?):")
for beta in (2.0, 10.0, 20.0):
    b, p = run(two, "arr", q=0.001, param=beta, seed=17)
    print(f"   beta={beta:<6} P1 = {p[0]:.4f}   (dev {p[0]-0.8:+.4f})")

print("\n=== Paper 6.1 regime: tau_game/tau_commit ~ 1e-2..1e-5 ===")
print("2-site game takes ~112 exchange steps, so q ~ (1/112)*(1e-2..1e-5)")
print("Worst-case rate law (beta=20, near-argmax) at physical commit speeds:")
for q in (1e-3, 1e-4, 1e-5, 1e-6):
    b, p = run(two, "arr", q=q, param=20.0, n_trials=40000, seed=23)
    print(f"   q={q:<9.0e} P1 = {p[0]:.4f}   (dev {p[0]-0.8:+.4f})")
print("\nAnd the 10-site case (Born 0.500), beta=20:")
ten = [1.0]*9 + [9.0]
for q in (1e-3, 1e-5):
    b, p = run(ten, "arr", q=q, param=20.0, n_trials=8000, seed=29)
    print(f"   q={q:<9.0e} P(bright) = {p[-1]:.4f}   (dev {p[-1]-0.5:+.4f})")
