"""
colored_noise_knife_edge.py — the knife-edge under finite noise correlation time.

TARGET. This is a colored-noise variant of #6 `noise_scaling_born.py`, the script the
suite README calls "**The knife-edge:** sqrt(e) (amplitude-linear) noise reproduces Born;
additive -> rich-get-richer; multiplicative -> equalizing. Verifies the Ito fairness
theorem." Same configurations, same sigma, dt and threshold, same non-conserving
independent-site SDE. Only the driving noise changes.

WHY (ledger EQUATIONS_RECONCILIATION_LEDGER_2026-09-01.md, E-14 + open item 2).
Paper 1 section 6.1 separates the noise correlation time (10-70 fs) from the game duration
(12-81 ps). The ratio is 2 ln^2 N, independent of Gamma, since both scale as 1/Gamma:
~1210 at N ~ 5e10, but ~11 at N = 10 and ~1 at N = 2. Below the washout point the noise is
not white, and the martingale's premise is not obviously met.

WHAT THIS TURNED OUT TO BE ABOUT — the stochastic calculus, not the correlation time.

Theorem 1's proof applies **Ito's lemma** to s_i = e_i / sum_j e_j. Appendix D integrates
by **Euler-Maruyama**, which is Ito by construction. Neither states why Ito rather than
Stratonovich. For multiplicative noise the choice is physical, not cosmetic:

  Wong-Zakai: colored noise of any finite correlation time converges, as tau_c -> 0, to the
  STRATONOVICH equation — never to the Ito one. For a(e) = sqrt(e) the two differ by

      a a' / 2 = sqrt(e) * (1/(2 sqrt(e))) / 2 = 1/4,   i.e. a drift  sigma^2/4

  identical on every site. Equal ADDITIVE drift is share-equalising: a leader gains
  proportionally less, so shares are pushed toward 1/N and the initial-share information
  the martingale is supposed to preserve is destroyed.

Physical detector noise has tau_c ~ 10-70 fs — finite, hence colored, hence Stratonovich.
So the question this script asks is not "does correlation time perturb the answer" but the
sharper one: **is the paper's Ito baseline the small-tau_c limit of the physical process at
all?**

WHAT THE ANSWER DOES NOT SETTLE. The sigma^2/4 drift requires the total energy to grow,
which this SDE permits and a closed pot does not. Paper 1 v0.7's P4(a) makes the pot closed
(sum_i e_i = hbar omega). So conservation, if imposed, forbids the drift — which would
justify the Ito choice, but on grounds the paper does not currently give. That connection
is the useful output here, not a defect claim.

Run:  python3 born_selection_sims/colored_noise_knife_edge.py
"""

import numpy as np

rng = np.random.default_rng(20260901)

SIGMA, DT, THRESH = 0.3, 0.02, 0.9
NTRIALS, MAXIT = 4000, 300_000


def game(shares0, tau_c=None, law="sqrt", stratonovich=False, conserve=False,
         sigma=SIGMA, dt=DT, thresh=THRESH, ntrials=NTRIALS, maxit=MAXIT):
    """noise_scaling_born.py's engine, with three switches added.

    tau_c=None    -> white Wiener increments (Euler-Maruyama = Ito), the paper's engine.
    tau_c=float   -> Ornstein-Uhlenbeck noise, unit intensity, correlation time tau_c.
    stratonovich  -> white, plus the Wong-Zakai drift sigma^2 a a'/2 (the limit colored
                     noise should approach).
    conserve      -> project each step onto sum_i e_i = const, i.e. a closed pot.
    """
    n = len(shares0)
    e = np.tile(np.asarray(shares0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    winners = np.full(ntrials, -1)

    if tau_c is not None:
        a_ou = np.exp(-dt / tau_c)
        var_stat = 1.0 / (2.0 * tau_c)
        eta = rng.normal(0.0, np.sqrt(var_stat), (ntrials, n))
        step_sd = np.sqrt(var_stat * (1.0 - a_ou * a_ou))

    for it in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        ei = e[idx]

        amp = np.sqrt(ei) if law == "sqrt" else (0.3 * np.ones_like(ei) if law == "add" else ei)

        if tau_c is None:
            incr = sigma * amp * rng.normal(0.0, np.sqrt(dt), ei.shape)
            if stratonovich:
                # sigma^2 * a * a' / 2 ; a=sqrt(e) -> 1/4, a=e -> e/2, a=const -> 0
                corr = {"sqrt": 0.25, "lin": 0.5 * ei, "add": 0.0}[law]
                incr = incr + sigma ** 2 * corr * dt
        else:
            eta[idx] = eta[idx] * a_ou + rng.normal(0.0, step_sd, ei.shape)
            incr = sigma * amp * eta[idx] * dt

        ei = np.maximum(ei + incr, 0.0)
        if conserve:
            tot0 = e[idx].sum(axis=1)
            tot1 = np.maximum(ei.sum(axis=1), 1e-12)
            ei = ei * (tot0 / tot1)[:, None]
        e[idx] = ei

        tot = ei.sum(axis=1)
        dead = tot < 1e-6
        s = ei / np.maximum(tot[:, None], 1e-12)
        done = (s.max(axis=1) >= thresh) & ~dead
        if done.any():
            fin = idx[done]
            winners[fin] = e[fin].argmax(axis=1)
            active[fin] = False
        if dead.any():
            active[idx[dead]] = False

    won = winners[winners >= 0]
    freq = np.bincount(won, minlength=n) / max(len(won), 1)
    return freq, 1.0 - len(won) / ntrials


def line(label, freq, born, unfin, bright_idx):
    print(f"  {label:<34} bright={freq[bright_idx]:.4f}  "
          f"vs Born {freq[bright_idx] - born[bright_idx]:+.4f}  "
          f"max|dev|={np.max(np.abs(freq - born)):.4f}  unfin={unfin:.1%}")


def suite(born, name, bright_idx, conserve=False):
    tag = "CLOSED POT (conserving)" if conserve else "open pot (paper's engine)"
    print(f"\n{'=' * 84}\n{name}  —  {tag}\n  Born bright = {born[bright_idx]:.4f}\n{'=' * 84}")
    fi, ui = game(born.copy(), tau_c=None, conserve=conserve)
    line("white, Ito  (paper's baseline)", fi, born, ui, bright_idx)
    fs, us = game(born.copy(), tau_c=None, stratonovich=True, conserve=conserve)
    line("white, Stratonovich", fs, born, us, bright_idx)
    print(f"  {'-' * 80}")
    for frac in (0.001, 0.01, 0.1, 1.0):
        fc, uc = game(born.copy(), tau_c=frac * 10.0, conserve=conserve)
        line(f"colored, tau_c = {frac * 10.0:7.3f}", fc, born, uc, bright_idx)


if __name__ == "__main__":
    born10 = np.array([1.] * 9 + [9.]); born10 /= born10.sum()
    born3 = np.array([0.5, 0.3, 0.2])

    print("Knife-edge under colored noise — variant of noise_scaling_born.py (#6)")
    print(f"sigma={SIGMA}  dt={DT}  thresh={THRESH}  trials={NTRIALS}  law=sqrt")
    print(f"Wong-Zakai drift for the sqrt law: sigma^2/4 = {SIGMA ** 2 / 4:.4f} per unit time")

    suite(born10, "10-site [1x9, 3x amp]", 9)
    suite(born3, "3-site [.5 .3 .2]", 0)
    suite(born10, "10-site [1x9, 3x amp]", 9, conserve=True)
