"""
silicon_commit_recompute.py — discharge ledger open item #2 (E-16): recompute Paper 1
section 6.1's timescale ladder for SILICON under the first-irreversibility definition of
commitment, which was fixed on 2026-09-02 BEFORE this script was written.

THE DEFINITION (ledger E-16, uncertainty #2, resolved):
    tau_commit is the time from capture at which the deposited excitation ceases to be
    coherently returnable to the common field. First irreversibility. Not the avalanche,
    not the electrical pulse, not the readout.

WHAT PROTECTS A SHARE, per section 6.1 itself: the absence of final states below the
registration threshold. In a gapped absorber a site holding share s_i carries
e_i = s_i * E_photon, and there is NO real final state while e_i < E_gap, i.e. while

    s_i < theta = E_gap / E_photon.

Above theta a real electron-hole pair (plus phonons carrying e_i - E_gap) IS available, and
the interband vertex plus thermalisation runs on the device-physics clock. That is the first
irreversibility for a site above theta. So the fixed definition, applied honestly, gives
silicon TWO regimes on the share axis:

    s < theta : protected  (no channel; the only exit is return to the field)
    s > theta : exposed    (tau_commit = vertex dephasing + thermalisation, 10 fs - 1 ps)

and section 6.1's quoted ns-us is neither. It is the avalanche-and-quench cycle, downstream.

WHAT IS COMPUTED, for silicon at several wavelengths and, by the same rule, for the two
comparison detectors already in the ledger:

 (1) The whole-game top rung, tau_game / tau_commit, as E-16 computed it for the SNSPD.
 (2) The EXPOSED-WINDOW top rung. Only a site above theta can commit, and under a closed
     pot with theta >= 1/2 at most one site is ever above theta; the exposure is the
     leader's final climb from theta to 1. Under section 6.1's own diffusive log-share
     scaling that leg takes t_exp ~ 2 ln^2(1/theta) / Gamma. This is the physically
     relevant comparison. It is applied to the NbN case too, so both detectors are judged
     by one rule rather than the silicon by a kinder one.
 (3) The instant-commit bias: the outcome if commitment fired the moment a site crossed
     theta (the exposed reading at its worst). This is section 6.1's own remark that
     "stopping at any finite share introduces a computable O(1-threshold) bias", made
     explicit for a two-site split by the martingale hitting probabilities.
 (4) Whether the closed pot can pay for TWO real sub-gap excitations, E_photon > 2 E_gap.
     Where it can, the gap does not enforce exclusivity and P4(a) must do so as a premise.

ALL DEVICE TIMESCALES ARE LITERATURE-TYPICAL, NOT MEASUREMENTS FROM THIS PROGRAM. The
silicon figures follow the SPAD device-physics review in
traycer_artifacts/debates/spad-event-cascade/round-01/device-physics (three-event
structure: photon-annihilation irreversibility fs-100 fs; which-site distinguishability
10 fs-1 ps; field-driven seed unrecoverability ~1 ps). Uncertain inputs are flagged.
The exposed-window leg time inherits E-15's caveat: it uses the same continuum diffusive
scaling section 6.1 uses, at a leg length of about one exchange step, where that scaling is
least trustworthy.
"""

import numpy as np

HC_EV_NM = 1239.84


def leg_time(log_distance, gamma):
    """Section 6.1's diffusive log-share scaling, applied to one leg of the walk."""
    return 2.0 * log_distance ** 2 / gamma


def two_site_instant_commit(s0, theta):
    """P(site 1 registers) if commitment fires the instant a site's share crosses theta,
    two-site fair game started at (s0, 1-s0).

    For theta >= 1/2 at most one site can be above theta. Absorbing boundaries at
    s = theta (site 1 commits) and s = 1 - theta (site 2 commits) give, by the martingale
    property of the share, P1 = (s0 - (1 - theta)) / (2 theta - 1), clipped to [0, 1]:
    a site already above theta at t = 0 commits at once.

    For theta < 1/2 both sites can be exposed simultaneously and the pot can pay for two
    real pairs; the two-site hitting problem no longer describes it. Returns None."""
    if theta < 0.5:
        return None
    if theta == 1.0:
        return s0
    return float(np.clip((s0 - (1.0 - theta)) / (2.0 * theta - 1.0), 0.0, 1.0))


def fmt_t(t):
    if t < 1e-12:
        return f"{t * 1e15:7.1f} fs"
    if t < 1e-9:
        return f"{t * 1e12:7.2f} ps"
    if t < 1e-6:
        return f"{t * 1e9:7.2f} ns"
    return f"{t * 1e6:7.2f} us"


def verdict(best, worst):
    """Judge the whole input range, not one corner of it."""
    if worst < 0.1:
        return "OK - game finishes first"
    if best > 1.0:
        return "INVERTED - commitment precedes the game across the whole input range"
    return "MARGINAL - range straddles unity"


def ladder(name, lam_nm, E_gap, gamma, N, commit_exposed, note="", downstream=None):
    E_ph = HC_EV_NM / lam_nm
    ratio = E_ph / E_gap
    theta = min(1.0, 1.0 / ratio)
    n_pairs = int(np.floor(ratio))            # real sub-gap pairs the closed pot can pay for
    g_lo, g_hi = gamma
    sep = 2.0 * np.log(N) ** 2
    tc = (1.0 / g_hi, 1.0 / g_lo)
    tg = (sep / g_hi, sep / g_lo)
    d_exp = -np.log(theta)                    # log-distance of the exposed leg
    t_exp = (leg_time(d_exp, g_hi), leg_time(d_exp, g_lo))
    c_lo, c_hi = commit_exposed

    print(f"\n{'=' * 78}\n{name}\n{'=' * 78}")
    if note:
        print(f"  {note}")
    print(f"  E_photon       {E_ph:6.3f} eV   E_gap {E_gap:8.4f} eV   ratio {ratio:8.1f}")
    print(f"  theta          {theta:6.3f}   (share below which NO real final state exists)")
    print(f"  exposed axis   {100 * (1 - theta):5.1f} % of the share axis has a real final state")
    print(f"  pot pays for   {n_pairs} real sub-gap excitation(s)   "
          f"{'-> two-pair channel OPEN; gap does not enforce exclusivity' if n_pairs >= 2 else '-> gap enforces exclusivity'}")
    print(f"  Gamma          {g_lo:.1e} - {g_hi:.1e} s^-1     N = {N:.0e}   2 ln^2 N = {sep:.0f}")
    print(f"  tau_c          {fmt_t(tc[0])} - {fmt_t(tc[1])}")
    print(f"  tau_game       {fmt_t(tg[0])} - {fmt_t(tg[1])}")
    print(f"  t_exposed      {fmt_t(t_exp[0])} - {fmt_t(t_exp[1])}   "
          f"(leader's climb theta -> 1; {d_exp:.2f} log-units; ~{d_exp ** 2 * 2:.1f} exchange steps)")
    print(f"  tau_commit     {fmt_t(c_lo)} - {fmt_t(c_hi)}   (first irreversibility, exposed site)")
    if downstream:
        print(f"  [downstream    {fmt_t(downstream[0])} - {fmt_t(downstream[1])}   "
              f"section 6.1's quoted figure: avalanche/quench cycle, NOT commitment]")

    print(f"\n  MIDDLE rung  tau_game / tau_c         = {sep:8.0f}   (Gamma-invariant)  "
          f"{'OK' if sep > 100 else 'THIN'}")
    worst_whole = tg[1] / c_lo
    best_whole = tg[0] / c_hi
    print(f"  TOP rung (whole game)   tau_game / tau_commit = {best_whole:9.4f} - {worst_whole:<9.1f}  "
          f"{verdict(best_whole, worst_whole)}")
    worst_exp = t_exp[1] / c_lo
    best_exp = t_exp[0] / c_hi
    print(f"  TOP rung (exposed leg)  t_exposed / tau_commit = {best_exp:9.4f} - {worst_exp:<9.2f}  "
          f"{verdict(best_exp, worst_exp)}")

    print(f"\n  Instant-commit bias (commitment fires the moment a share crosses theta):")
    for s0 in (0.6, 0.8, 0.95):
        p = two_site_instant_commit(s0, theta)
        if p is None:
            print(f"     Born {s0:.2f}  ->  undefined: both sites can be exposed at once (theta < 1/2)")
        else:
            print(f"     Born {s0:.2f}  ->  P1 = {p:.3f}   (deviation {p - s0:+.3f})")
    return dict(name=name, ratio=ratio, theta=theta, n_pairs=n_pairs, sep=sep,
                whole=(best_whole, worst_whole), exp=(best_exp, worst_exp),
                bias80=two_site_instant_commit(0.8, theta))


print(__doc__)

SI_GAMMA = (1.5e13, 1.0e14)          # section 6.1: final-state widths 10-100 meV
SI_N = 5e10                          # section 6.1: sites in the diffraction volume
SI_COMMIT = (10e-15, 1e-12)          # device review: dephasing <~100 fs; thermalisation
                                     # 0.1-1 ps; seed unrecoverable ~1 ps  [literature-typical]
SI_DOWNSTREAM = (1e-9, 1e-6)         # section 6.1's quoted "ns-us": avalanche/quench cycle

# ---------------------------------------------------------------------------
# 0. Reproduce section 6.1's own numbers (validation), then apply the definition.
# ---------------------------------------------------------------------------
results = []
results.append(ladder(
    "SILICON SPAD @ 500 nm, 300 K  (section 6.1's own detector)",
    500, 1.12, SI_GAMMA, SI_N, SI_COMMIT,
    note="validation: paper quotes tau_c 10-70 fs, tau_game 12-81 ps; reproduced below",
    downstream=SI_DOWNSTREAM))

# ---------------------------------------------------------------------------
# 1. Silicon across the visible/NIR: same device family, same Gamma, only the
#    photon-to-gap ratio changes. The ratio-2 boundary sits at 553 nm.
# ---------------------------------------------------------------------------
for lam in (405, 650, 800, 1000):
    results.append(ladder(
        f"SILICON SPAD @ {lam} nm, 300 K", lam, 1.12, SI_GAMMA, SI_N, SI_COMMIT,
        note=("ratio > 2: the closed pot can pay for two real pairs" if HC_EV_NM / lam > 2.24
              else "ratio < 2: at most one site can hold a real final state at a time"),
        downstream=SI_DOWNSTREAM))

# ---------------------------------------------------------------------------
# 2. The comparison detectors already in the ledger, judged by the same rule.
# ---------------------------------------------------------------------------
results.append(ladder(
    "InGaAs SPAD @ 1550 nm  (Gamma and commit taken as silicon's - UNCERTAIN, flagged)",
    1550, 0.75, SI_GAMMA, SI_N, SI_COMMIT,
    note="near-gap operation: theta ~ 0.94, the exposed leg is a fraction of one exchange step",
    downstream=SI_DOWNSTREAM))

NBN_GAMMA = (5e10, 1e11)             # tau_ep 10-20 ps  [E-16 uncertainty #1, unchanged]
NBN_N = 1e6
results.append(ladder(
    "NbN SNSPD @ 1550 nm, ~2 K  -  commit = hotspot -> resistive (10-50 ps), as E-16 logged",
    1550, 1.5e-3, NBN_GAMMA, NBN_N, (10e-12, 50e-12),
    note="E_gap = 1.5 meV as in the E-16 table (single-particle gap Delta; 2Delta would halve the ratio)"))
results.append(ladder(
    "NbN SNSPD @ 1550 nm, ~2 K  -  commit = quasiparticle cascade onset (0.1-1 ps)  [UNCERTAIN]",
    1550, 1.5e-3, NBN_GAMMA, NBN_N, (100e-15, 1e-12),
    note="the strict first-irreversibility analogue of silicon's vertex+thermalisation clock"))

# ---------------------------------------------------------------------------
# 3. Summary
# ---------------------------------------------------------------------------
print(f"\n{'=' * 78}\nSUMMARY  (top rung: needs << 1; whole-game vs exposed-leg accounting)\n{'=' * 78}")
print(f"  {'detector':<58} {'ratio':>6} {'theta':>6} {'pairs':>5} {'whole-game':>16} {'exposed-leg':>16} {'bias@0.8':>8}")
for r in results:
    b = "n/a" if r['bias80'] is None else f"{r['bias80']:.3f}"
    print(f"  {r['name'][:58]:<58} {r['ratio']:6.1f} {r['theta']:6.3f} {r['n_pairs']:5d} "
          f"{r['whole'][0]:7.3f}-{r['whole'][1]:<8.1f} {r['exp'][0]:7.3f}-{r['exp'][1]:<8.2f} {b:>8}")

print("""
READING THE TABLE
  * 'whole-game' is the comparison E-16 used for the SNSPD. On that accounting silicon
    inverts too, by one to four orders. Section 6.1's "two to four orders to spare at every
    rung" does not survive its own detector under the fixed definition.
  * 'exposed-leg' is the physically relevant comparison: only a site above theta can commit,
    and for theta >= 1/2 that is one site, during its final climb. On that accounting
    silicon is MARGINAL at every visible wavelength (the range straddles unity by about an
    order each way), closing toward safe only near the band edge. The SNSPD stays INVERTED
    on either reading of its commitment, because theta ~ 0.002 makes its exposed leg
    ~79 exchange steps (0.8-1.6 ns) against a 10-50 ps commit. E-16's whole-game accounting
    overstated the exposure for both detectors; the asymmetry between them survives it,
    weakened from "safe by 2-4 orders vs inverted by 2-3" to "straddling unity vs inverted
    by 1-2 (hotspot) or 3-4 (cascade)".
  * 'bias@0.8' is the two-site outcome for an 80/20 split if commitment were instant above
    theta. It is large at every wavelength (even at InGaAs's theta = 0.94 it is +0.04),
    so the exposed reading is only compatible with routine SPAD splitting-ratio data if the
    exposed leg is short compared with tau_commit, i.e. if the marginal ratio sits at the
    low end of its range. That is a constraint, not a refutation.
  * 'pairs' >= 2 (silicon below 553 nm) means the gap does not block a second real
    excitation; exclusivity there rests on P4(a) as a premise, not on the level structure.
""")
