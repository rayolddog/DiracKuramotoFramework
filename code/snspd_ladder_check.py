"""
snspd_ladder_check.py — does Paper 1 section 6.1's timescale ladder survive in an SNSPD?

Ledger item E-16. Section 6.1 computes the ladder for ONE detector: a room-temperature
silicon SPAD at 500 nm. Section 8 discusses SNSPDs, which run at 1-4 K. Nobody has checked
whether the ladder holds there, and E-16 argues it may not, because the rungs scale
differently with the electronic relaxation rate Gamma:

    tau_c      = 1/Gamma                  <- noise correlation time, scales as 1/Gamma
    tau_game   = 2 ln^2(N) / Gamma        <- selection duration,     scales as 1/Gamma
    tau_commit = set by device physics    <- does NOT scale with Gamma

So the MIDDLE separation tau_game/tau_c = 2 ln^2(N) is Gamma-invariant (a robustness
result the paper does not currently claim), while the TOP separation
tau_game << tau_commit is not protected at all. Cooling lowers Gamma, stretches tau_game,
and pushes it toward tau_commit.

That matters because v0.7's restructuring rests on the top rung: commitment being slow is
why first passage settles the outcome before any commit-rate law acts, and why Theorems
4-5 were demoted from operative mechanism to robustness rider (section 5.4). Invert the
rung and the fast-commit reading v0.7 withdrew comes back — where v0.7's own check
(g3_drain_tests/theorem5_check.py) reports a deliberately wrong Arrhenius commit law
giving 0.719 against Born's 0.500, versus 0.504 at section 6.1's separation.

ALL SNSPD INPUTS BELOW ARE LITERATURE-TYPICAL ESTIMATES, NOT MEASUREMENTS FROM THIS
PROGRAM, and the two genuinely uncertain ones are flagged. This script exists to make the
assumptions inspectable, not to settle the question.
"""

import numpy as np


def ladder(name, gamma_lo, gamma_hi, N, commit_lo, commit_hi, note=""):
    sep = 2.0 * np.log(N) ** 2                      # tau_game / tau_c, Gamma-invariant
    tc = (1.0 / gamma_hi, 1.0 / gamma_lo)           # noise correlation time
    tg = (sep / gamma_hi, sep / gamma_lo)           # selection duration
    print(f"\n{'=' * 78}\n{name}\n{'=' * 78}")
    if note:
        print(f"  {note}")
    print(f"  Gamma          {gamma_lo:.2e} - {gamma_hi:.2e} s^-1")
    print(f"  N (sites)      {N:.1e}      ->  2 ln^2 N = {sep:.0f}")
    print(f"  tau_c          {tc[0] * 1e15:8.1f} - {tc[1] * 1e15:8.1f} fs")
    print(f"  tau_game       {tg[0] * 1e12:8.2f} - {tg[1] * 1e12:8.2f} ps")
    print(f"  tau_commit     {commit_lo * 1e12:8.2f} - {commit_hi * 1e12:8.2f} ps")

    # middle rung (should be 2 ln^2 N by construction, printed as a check)
    print(f"\n  MIDDLE rung  tau_game / tau_c      = {sep:8.0f}   "
          f"(Gamma-invariant; needs >> 1)  {'OK' if sep > 100 else 'THIN'}")

    # top rung — the unprotected one. Worst case = longest game vs fastest commit.
    worst = tg[1] / commit_lo
    best = tg[0] / commit_hi
    verdict = ("OK — game finishes first" if worst < 0.1 else
               "MARGINAL" if worst < 1.0 else
               "INVERTED — commitment competes with or precedes the game")
    print(f"  TOP rung     tau_game / tau_commit = {best:8.4f} - {worst:<8.1f} "
          f"(needs << 1)  {verdict}")
    return sep, tg, worst


print(__doc__)

# ---------------------------------------------------------------------------
# 1. Section 6.1's own detector, reproduced as a validation of this script.
#    Inputs taken directly from the paper: 10-100 meV final-state widths,
#    N ~ 5e10 sites in the diffraction volume, commitment ns-us.
# ---------------------------------------------------------------------------
ladder("SILICON SPAD @ 500 nm, 300 K  (Paper 1 section 6.1 — reproduction check)",
       gamma_lo=1.5e13, gamma_hi=1.0e14, N=5e10,
       commit_lo=1e-9, commit_hi=1e-6,
       note="paper quotes tau_c 10-70 fs, tau_game 12-81 ps — reproduce those to validate")

# ---------------------------------------------------------------------------
# 2. NbN SNSPD @ 1550 nm, ~2 K.  LITERATURE-TYPICAL, NOT MEASURED HERE.
#
#    Gamma: the electron-phonon relaxation rate. NbN thin films at a few K have
#    tau_ep ~ 10-20 ps, so Gamma ~ 5e10-1e11 s^-1 — two to three orders BELOW
#    silicon's phonon/carrier scattering. [UNCERTAIN #1: whether tau_ep is the
#    right analogue of section 6.1's "final-state width" for a superconductor is a
#    judgement, not a derivation.]
#
#    N: the photon deposits into a small nanowire volume, not a diffraction volume.
#    ~100 nm wide x 5 nm thick x ~50 nm along the wire at ~5e28 atoms/m^3 gives
#    ~1e6, far below silicon's 5e10. Only ln^2 N enters, so this is forgiving.
#
#    tau_commit: hotspot growth to a resistive barrier spanning the wire — the
#    irreversible step. Intrinsic detection latency and jitter are measured in the
#    few-ps to tens-of-ps range. [UNCERTAIN #2: if "commitment" instead means the
#    electrical pulse (L_k/R, 5-50 ns), the verdict changes — see the sweep below.]
# ---------------------------------------------------------------------------
ladder("NbN SNSPD @ 1550 nm, ~2 K  (literature-typical estimates)",
       gamma_lo=5e10, gamma_hi=1.0e11, N=1e6,
       commit_lo=10e-12, commit_hi=50e-12,
       note="commitment = hotspot -> resistive transition (intrinsic, ps-scale)")

ladder("NbN SNSPD, same but commitment = electrical reset (L_k/R)",
       gamma_lo=5e10, gamma_hi=1.0e11, N=1e6,
       commit_lo=5e-9, commit_hi=50e-9,
       note="the alternative reading of 'commitment' — much more forgiving")

# ---------------------------------------------------------------------------
# 3. How much does N matter?  Only through ln^2, so: very little.
# ---------------------------------------------------------------------------
print(f"\n{'=' * 78}\nSensitivity of the SNSPD verdict to N (Gamma = 1e11, "
      f"commit = 30 ps)\n{'=' * 78}")
print(f"  {'N':>10}  {'2 ln^2 N':>10}  {'tau_game':>12}  {'/tau_commit':>12}")
for N in (1e3, 1e4, 1e6, 1e8, 5e10):
    sep = 2 * np.log(N) ** 2
    tg = sep / 1e11
    print(f"  {N:10.0e}  {sep:10.0f}  {tg * 1e12:10.2f} ps  {tg / 30e-12:12.1f}")
print("\n  The inversion is robust to N: even at N = 1e3 the game outlasts a 30 ps\n"
      "  commitment by more than an order of magnitude.")
