#!/usr/bin/env python3
"""
stage2_port_signaling_corrected.py  — corrected after the 2026-07-27 review panel.

ORIGINAL: born_selection_sims/stage2_port_signaling.py
DEFECTS (flagged by GPT-5 Codex, confirmed):
  (1) The fully-correlated matched control port_game(S, 1.0, 1.0) returns NaN:
      at c=1 the m equal sites in a port share identical noise and never separate,
      so no single site crosses the win threshold -> empty winners -> NaN, printed
      under the false label "matched ports -> fair".
  (2) The reported statistic conditions away no-click trials (up to ~47% of them
      at c=1) and compares the mechanism's conditional P'(S) implicitly against a
      straight line. But under UNEQUAL detection efficiency, standard QM's
      *conditional* (post-click) port fraction is already curved,
      P_QM(A|click) = S*eta_A / (S*eta_A + (1-S)*eta_B); "curvature" per se does
      not discriminate. The affine statement holds for UNCONDITIONAL probabilities.

FIX: (a) lift the c=1 degeneracy with a small independent noise floor so the
matched control is non-degenerate and actually fair; (b) report the no-click rate
alongside the conditional fraction; (c) print the QM conditional-fraction curve so
the mechanism's kappa*S(1-S) bow is compared against the correct QM baseline, not
against a straight line.
"""
import numpy as np

rng = np.random.default_rng(53)


def port_game(Splus, c_plus, c_minus=0.0, m=4, ntrials=20000, sigma=0.3, dt=0.02,
              win=0.7, floor=1e-3, maxit=60000):
    """Two ports x m sites; within-port noise correlation c_plus / c_minus.
    A small independent `floor` is added to the covariance diagonal so the fully
    correlated (c=1) case is non-degenerate. Returns (P(port+|click), no_click_frac)."""
    n = 2 * m
    e0 = np.concatenate([np.full(m, Splus / m), np.full(m, (1 - Splus) / m)])
    C = np.eye(n)
    C[:m, :m] = c_plus + (1 - c_plus) * np.eye(m)
    C[m:, m:] = c_minus + (1 - c_minus) * np.eye(m)
    C = (1 - floor) * C + floor * np.eye(n)              # lift degeneracy
    lam, U = np.linalg.eigh(C)
    L = U * np.sqrt(np.clip(lam, 0, None))
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    noclick = 0
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        dW = (rng.normal(0, 1, (idx.size, n)) @ L.T) * np.sqrt(dt)
        ei = np.maximum(e[idx] + sigma * np.sqrt(e[idx]) * dW, 0.0)
        e[idx] = ei
        tot = ei.sum(axis=1)
        s = ei / np.maximum(tot[:, None], 1e-12)
        done = (s.max(axis=1) >= win) & (tot > 1e-6)
        dead = tot <= 1e-6
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
        if dead.any():
            noclick += int(dead.sum())
            active[idx[dead]] = False
    w = winners[winners >= 0]
    p_cond = (w < m).mean() if len(w) else float('nan')
    # trials that never resolved within maxit count as no-result, reported separately
    unresolved = int((winners < 0).sum() - noclick)
    return p_cond, noclick / ntrials, unresolved


print("Mismatched ports: port+ internally correlated at c, port- independent (m=4).")
print("Compared against the QM CONDITIONAL baseline (equal efficiency -> P_QM = S).")
print(f"{'S+':>5} | {'c=0':>7} | {'c=0.3':>7} | {'c=0.5':>7} | no-click(c=.5) | QM(=S)")
for S in (0.2, 0.35, 0.5, 0.65, 0.8):
    r0, nc0, _ = port_game(S, 0.0)
    r3, nc3, _ = port_game(S, 0.3)
    r5, nc5, _ = port_game(S, 0.5)
    print(f"{S:>5} | {r0:>7.4f} | {r3:>7.4f} | {r5:>7.4f} | {nc5:>13.3f} | {S:>5}")

print("\nMatched-ports control (c_plus = c_minus), now non-degenerate via floor:")
for c in (0.5, 1.0):
    print(f"  c={c}:")
    for S in (0.2, 0.5, 0.8):
        r, nc, _ = port_game(S, c, c)
        print(f"    S+={S}: P(port+|click)={r:.4f}  dev={r-S:+.4f}  no-click={nc:.3f}")

print("\nWeak-mismatch kappa scaling (port+ c, port- 0), S+=0.5:")
for c in (0.1, 0.25, 0.5):
    r, nc, _ = port_game(0.5, c)
    print(f"  c={c}: P(port+|click)={r:.4f}  dev={r-0.5:+.4f}  no-click={nc:.3f}")

print("\nWhy 'curvature' alone does not discriminate (GPT-5 concern):")
print("QM post-click fraction under unequal efficiency eta_A:eta_B is ALREADY curved:")
print(f"  {'S':>5} | {'eta=1:1 (=S)':>12} | {'eta=1:2':>9} | {'eta=2:1':>9}")
for S in (0.2, 0.35, 0.5, 0.65, 0.8):
    f11 = S
    f12 = S * 1 / (S * 1 + (1 - S) * 2)
    f21 = S * 2 / (S * 2 + (1 - S) * 1)
    print(f"  {S:>5} | {f11:>12.4f} | {f12:>9.4f} | {f21:>9.4f}")
print("=> the discriminator must compare P'(S) against this QM conditional curve")
print("   (or use UNCONDITIONAL probabilities), not against a straight line.")
