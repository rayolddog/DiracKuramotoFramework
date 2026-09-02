"""
colored_noise_exchange.py — the knife-edge under colored noise, EXCHANGE formulation.

The decisive companion to colored_noise_knife_edge.py (E-15).

That script re-ran #6 `noise_scaling_born.py`, whose engine is independent-per-site,
non-conserving noise integrated by Euler-Maruyama (Ito). Colored noise broke Born badly
there — ten-site bright weight 0.53 -> 0.29 against Born 0.50 — in the equalising direction
predicted by the Wong-Zakai drift sigma^2 a a'/2 = sigma^2/4 for a(e) = sqrt(e). Imposing
conservation as a projection did not help, because adding a constant to every site and
renormalising still sends s_i -> (s_i + c/E)/(1 + nc/E), a pull toward 1/n.

THIS script tests the formulation that objection does not reach: #3
`gambler_ruin_born3.py`'s stakes-scaled fair exchange,

    d = step * min(e_i, e_j) * sign,     e_i -= d,  e_j += d

which the suite README records as the PASS case ("reproduces Born to ~2% at absorb 0.95").
Two structural properties matter here:

  1. It is exactly conserving — energy is moved, never created.
  2. The increment is ANTISYMMETRIC in (i, j). Whatever leaves i enters j, identically.
     A common-mode drift — the same gain on every site — is therefore not merely forbidden
     by a constraint, it is unrepresentable. The sigma^2/4 term has nowhere to live.

So if the knife-edge is calculus-sensitive only through a common-mode drift, this
formulation should be immune, and E-15 reduces to a presentational gap: the paper should
say that its Ito choice is licensed by the exchange structure of the physical dynamics
rather than by the discretisation. If Born breaks here too, the problem is real and
sits in the mechanism rather than in the engine.

Colored noise enters where the fair coin was: each site carries an Ornstein-Uhlenbeck
phase proxy eta_i of correlation time tau_c, and the exchange direction is
sign(eta_i - eta_j). As tau_c -> 0 the eta decorrelate every step and the sign becomes a
fair coin, recovering gambler_ruin_born3.py exactly — so the white limit validates the
harness rather than being assumed.

tau_c is swept at the three separations in the ledger, since that is the decision-relevant
axis: tau_game/tau_c = 2 ln^2 N is ~1210 at the detector's N ~ 5e10, ~11 at N = 10, and
~1 at N = 2. Only the last two are regimes the simulations actually occupy.

Run:  python3 born_selection_sims/colored_noise_exchange.py
"""

import numpy as np

rng = np.random.default_rng(20260901)

STEP, THRESH = 0.1, 0.95          # gambler_ruin_born3.py's parameters
NTRIALS, MAXIT = 3000, 400_000


def exchange(amps, tau_c=None, step=STEP, thresh=THRESH,
             ntrials=NTRIALS, maxit=MAXIT):
    """Stakes-scaled conserving exchange. tau_c in exchange steps; None = white.

    No clipping is needed: d = step*min(e_i,e_j) with step < 1 can never drive either
    site negative, so the martingale is exact at the boundary as well as in the bulk.
    """
    A = np.asarray(amps, float)
    e0 = A ** 2 / np.sum(A ** 2)
    n = len(e0)
    e = np.tile(e0, (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)
    t_abs = np.full(ntrials, np.nan)

    if tau_c is not None:
        a_ou = np.exp(-1.0 / tau_c)
        eta = rng.normal(0.0, 1.0, (ntrials, n))
        sd = np.sqrt(1.0 - a_ou * a_ou)

    for it in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        m = idx.size
        i = rng.integers(0, n, size=m)
        j = (i + rng.integers(1, n, size=m)) % n

        if tau_c is None:
            sgn = np.where(rng.random(m) < 0.5, 1.0, -1.0)
        else:
            eta[idx] = eta[idx] * a_ou + rng.normal(0.0, sd, (m, n))
            sgn = np.sign(eta[idx, i] - eta[idx, j])
            sgn[sgn == 0.0] = 1.0

        d = step * np.minimum(e[idx, i], e[idx, j]) * sgn
        e[idx, i] -= d
        e[idx, j] += d

        done = e[idx].max(axis=1) >= thresh
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            t_abs[fin] = it + 1
            active[fin] = False

    won = winners[winners >= 0]
    freq = np.bincount(won, minlength=n) / max(len(won), 1)
    return freq, np.nanmean(t_abs) if len(won) else np.nan, 1.0 - len(won) / ntrials


def suite(amps, name, bright_idx):
    A = np.asarray(amps, float)
    born = A ** 2 / np.sum(A ** 2)
    n = len(A)
    sep_N = 2.0 * np.log(n) ** 2
    print(f"\n{'=' * 88}\n{name}\n  Born bright = {born[bright_idx]:.4f}   "
          f"2 ln^2 N at N={n} is {sep_N:.1f}\n{'=' * 88}")

    fw, tw, uw = exchange(A, tau_c=None)
    print(f"  {'white (= gambler_ruin_born3)':<40} bright={fw[bright_idx]:.4f}  "
          f"vs Born {fw[bright_idx] - born[bright_idx]:+.4f}  "
          f"max|dev|={np.max(np.abs(fw - born)):.4f}  tau_game={tw:.0f} steps  unfin={uw:.1%}")
    print(f"  {'-' * 84}")

    for sep, tag in ((1210.0, "detector, N~5e10"),
                     (11.0, "ten-site sim"),
                     (1.0, "two-site sim")):
        tau_c = max(tw / sep, 1e-6)
        fc, tc, uc = exchange(A, tau_c=tau_c)
        print(f"  tau_game/tau_c = {sep:7.1f}  ({tag:<16})  "
              f"bright={fc[bright_idx]:.4f}  vs Born {fc[bright_idx] - born[bright_idx]:+.4f}  "
              f"vs white {fc[bright_idx] - fw[bright_idx]:+.4f}  unfin={uc:.1%}")


if __name__ == "__main__":
    print("Knife-edge under colored noise — EXCHANGE formulation (gambler_ruin_born3 rule)")
    print(f"step={STEP}  absorbing threshold={THRESH}  trials={NTRIALS}")
    print("Increment is antisymmetric in (i,j): a common-mode drift is unrepresentable.")

    suite([1.0] * 9 + [3.0], "ten-site [1x9, 3x amp]", 9)
    suite([2.0, 1.0], "two-site [2:1]", 0)
    suite([3.0, 2.0, 1.0], "three-site [3:2:1]", 0)
