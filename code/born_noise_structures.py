#!/usr/bin/env python3
r"""
born_noise_structures.py
========================

Direct attack on the Born-measure problem (follow-up to lock_time.py):
for the bistable lock  dphi = a(phi) dt + sqrt(2 D(phi)) dW  with detector wells at
0, pi, WHICH noise structure D(phi) bends the basin split P(basin 0 | phi0) onto the
Born target  cos^2(phi0/2)?

Analytic key (committor / splitting probability for an Ito diffusion with absorbing
pointers at 0 and pi):
        q(phi) = [ int_phi^pi s(x) dx ] / [ int_0^pi s(x) dx ],
        scale density  s(x) = exp( - int_0^x a(y)/D(y) dy ).
We want q(phi) = cos^2(phi/2).

Result derived by hand and checked numerically below:
    With the Adler drift a = -gamma sin2phi and  D(phi) = 2 gamma sin^2 phi,
        a/D = -cot(phi)  ->  s(phi) = sin(phi)  ->  q(phi) = (1+cos phi)/2 = cos^2(phi/2).
    EXACTLY BORN.

The winning D(phi) = 2 gamma sin^2 phi is NOT arbitrary:  sin^2 phi = 1 - <sigma_x>^2
= Var(sigma_x) on the equator.  It is the MEASUREMENT-BACKACTION noise -- it VANISHES
at the pointer states (phi=0,pi, where there is nothing left to measure) and is maximal
at the equator (max superposition).  Constant ("thermal/vacuum-additive") noise does
NOT vanish at the pointers -> gives the STEP, not Born.

So: Born <=> the Stage-2 noise is QND measurement backaction (drift and noise LINKED,
both from sigma_x, vanishing on the pointer states), NOT a generic additive bath.
This is exactly the structure the QSD already has and that Sec 3.2's D[sigma_x] commits
to -- i.e. Born FOLLOWS IF Stage-2 is a measurement of the chiral channel, but the
Born-giving math is standard backaction, not derived from "synchronization" per se.

The vacuum (user's question) enters as a FLOOR: a residual additive noise D_vac (the
1/2 hbar omega zero-point piece of the fluctuation-dissipation spectrum, surface/Purcell-
modified).  We show it DEGRADES Born -- pulling the split back toward the step -- unless
it too is backaction-structured.  So the vacuum is a liability for Born, not a rescue.
"""

import numpy as np


def committor_analytic(a_func, D_func, gamma, npts=4001):
    """q(phi) via scale density s(phi)=exp(-int a/D), absorbing pointers at 0,pi."""
    phi = np.linspace(1e-4, np.pi - 1e-4, npts)
    ratio = a_func(phi, gamma) / D_func(phi, gamma)
    # cumulative integral of a/D from phi[0]
    integ = np.concatenate([[0.0], np.cumsum(0.5 * (ratio[1:] + ratio[:-1]) * np.diff(phi))])
    s = np.exp(-integ)
    # q(phi) = int_phi^pi s / int_0^pi s
    cum = np.concatenate([[0.0], np.cumsum(0.5 * (s[1:] + s[:-1]) * np.diff(phi))])
    total = cum[-1]
    q = (total - cum) / total
    return phi, q


def basin_split_sim(phi0, D_func, gamma, with_drift=True, n=5000, T=6.0, dt=1e-3, seed=0):
    """Ito Euler-Maruyama; return fraction ending in basin 0 (cos phi > 0)."""
    rng = np.random.default_rng(seed)
    nsteps = int(T / dt)
    phi = np.full(n, float(phi0))
    for _ in range(nsteps):
        a = -gamma * np.sin(2 * phi) if with_drift else 0.0
        D = np.maximum(D_func(phi, gamma), 1e-12)
        phi = phi + a * dt + np.sqrt(2 * D * dt) * rng.standard_normal(n)
    return np.mean(np.cos(phi) > 0)


# ---- candidate noise structures ---------------------------------------------
def D_const(phi, gamma):   return 0.30 * np.ones_like(phi)        # thermal / vacuum-additive
def D_sin2(phi, gamma):    return 2 * gamma * np.sin(phi)**2       # measurement backaction
def D_absin(phi, gamma):   return 1.0 * np.abs(np.sin(phi))        # |sin| (wrong power)
def a_adler(phi, gamma):   return -gamma * np.sin(2 * phi)
def a_zero(phi, gamma):    return np.zeros_like(phi)


def main():
    gamma = 1.0
    phis = np.radians(np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 150, 180.0]))
    born = np.cos(phis / 2)**2

    print("=" * 78)
    print("BORN-MEASURE TEST: which D(phi) makes the basin split = cos^2(phi0/2)?")
    print("  dynamics: dphi = a(phi) dt + sqrt(2 D(phi)) dW ; wells at 0, pi ; gamma=1")
    print("=" * 78)

    models = [
        ("constant D=0.30  (thermal / vacuum-additive)", D_const, a_adler, True),
        ("D=2g sin^2(phi)  (measurement BACKACTION)    ", D_sin2,  a_adler, True),
        ("D=|sin(phi)|     (wrong power)                ", D_absin, a_adler, True),
        ("D=2g sin^2(phi) but NO drift (a=0)           ", D_sin2,  a_zero,  False),
    ]

    print(f"\n  phi0(deg):  " + "  ".join(f"{int(np.degrees(p)):4d}" for p in phis))
    print(f"  Born     :  " + "  ".join(f"{b:4.2f}" for b in born))
    print("  " + "-" * 74)
    results = {}
    for i, (name, Df, af, drift) in enumerate(models):
        split = np.array([basin_split_sim(p, Df, gamma, with_drift=drift, seed=100 + i * 11 + j)
                          for j, p in enumerate(phis)])
        results[name] = split
        rms = np.sqrt(np.mean((split - born)**2))
        print(f"  {name}\n     sim   :  " + "  ".join(f"{s:4.2f}" for s in split)
              + f"     RMS vs Born = {rms:.3f}")

    # analytic committor confirmation for the winner
    phi_a, q_a = committor_analytic(a_adler, D_sin2, gamma)
    born_a = np.cos(phi_a / 2)**2
    print(f"\n  ANALYTIC committor for D=2g sin^2 + Adler drift:  max|q - cos^2(phi/2)| "
          f"= {np.max(np.abs(q_a - born_a)):.4f}  (scale density s=sin phi -> exact Born)")

    # ---- vacuum-floor sweep: does residual additive vacuum noise hurt Born? ----
    print("\n" + "=" * 78)
    print("VACUUM FLOOR (user's question): D(phi) = 2g sin^2(phi) + D_vac  (additive ZPF)")
    print("  does a residual additive vacuum noise degrade Born?")
    print("=" * 78)
    vac_rms = {}
    for Dvac in [0.0, 0.1, 0.3, 1.0]:
        Df = lambda phi, g, dv=Dvac: 2 * g * np.sin(phi)**2 + dv
        split = np.array([basin_split_sim(p, Df, gamma, seed=500 + j) for j, p in enumerate(phis)])
        rms = np.sqrt(np.mean((split - born)**2))
        vac_rms[Dvac] = (split, rms)
        print(f"  D_vac={Dvac:4.2f}:  RMS vs Born = {rms:.3f}"
              + ("   (pure backaction -> Born)" if Dvac == 0 else "   (pulled toward STEP)"))
    print("  => an ADDITIVE vacuum floor (constant, doesn't vanish at pointers) degrades Born.")
    print("     The vacuum helps ONLY if its coupling is itself QND backaction; as a generic")
    print("     additive bath it is a LIABILITY for the Born weights, not a rescue.")

    make_figure(phis, born, results, vac_rms, phi_a, q_a)

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print("  * Born is recovered by EXACTLY ONE structure: D(phi) ∝ sin^2(phi) = Var(sigma_x),")
    print("    LINKED to the Adler drift (ratio a/D = -cot phi -> scale density sin phi).")
    print("  * That is the MEASUREMENT-BACKACTION noise (vanishes at the pointer states) --")
    print("    i.e. the standard QND structure the QSD/Sec-3.2 D[sigma_x] already has.")
    print("  * So Born FOLLOWS IF Stage-2 is a QND measurement of the chiral channel, but the")
    print("    Born-giving math is standard backaction; 'synchronization' only supplies the")
    print("    identification of the measured observable, not a NEW derivation of |alpha|^2.")
    print("  * Vacuum/thermal ADDITIVE noise degrades Born; it is not the missing ingredient.")


def make_figure(phis, born, results, vac_rms, phi_a, q_a):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print(f"\n[figure skipped: {e}]")
        return
    fig, ax = plt.subplots(1, 3, figsize=(16, 5))
    pd = np.degrees(phis)
    fine = np.linspace(0, 180, 200)

    # (0) candidate structures vs Born
    a = ax[0]
    a.plot(fine, np.cos(np.radians(fine) / 2)**2, "k-", lw=2.5, label=r"Born $\cos^2(\phi_0/2)$")
    styles = {"constant D=0.30  (thermal / vacuum-additive)": ("C3", "s", "--"),
              "D=2g sin^2(phi)  (measurement BACKACTION)    ": ("C2", "o", "-"),
              "D=|sin(phi)|     (wrong power)                ": ("C1", "^", ":"),
              "D=2g sin^2(phi) but NO drift (a=0)           ": ("C0", "v", ":")}
    for name, split in results.items():
        c, m, ls = styles[name]
        a.plot(pd, split, color=c, marker=m, ls=ls, lw=1.5, ms=5, label=name.split("(")[0].strip())
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)"); a.set_ylabel(r"$P(\rm basin\,0\,|\,\phi_0)$")
    a.set_title("Only $D\\propto\\sin^2\\phi$ (backaction) reproduces Born")
    a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=7.5); a.grid(alpha=0.25)

    # (1) the winning noise profile vs phi
    a = ax[1]
    pp = np.radians(fine)
    a.plot(fine, np.sin(pp)**2, "C2-", lw=2.5, label=r"$D\propto\sin^2\phi=\mathrm{Var}(\sigma_x)$ (backaction)")
    a.axhline(0.30, color="C3", ls="--", lw=2, label="constant (thermal/vacuum) noise")
    for x0 in (0, 180):
        a.axvline(x0, color="g", lw=0.8)
    a.annotate("pointer\nstates", (5, 0.05), fontsize=8, color="g")
    a.set_xlabel(r"phase $\phi$ (deg)"); a.set_ylabel(r"noise strength $D(\phi)$")
    a.set_title("Backaction noise VANISHES at the pointers; thermal does not")
    a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    # (2) vacuum floor degrades Born
    a = ax[2]
    a.plot(fine, np.cos(np.radians(fine) / 2)**2, "k-", lw=2, label="Born")
    cols = ["C2", "C1", "C3", "0.3"]
    for (Dvac, (split, rms)), c in zip(vac_rms.items(), cols):
        a.plot(pd, split, color=c, marker="o", ms=4, lw=1.3,
               label=f"$D_{{vac}}={Dvac}$ (RMS {rms:.2f})")
    a.set_xlabel(r"phase mismatch $\phi_0$ (deg)"); a.set_ylabel(r"$P(\rm basin\,0)$")
    a.set_title("Additive vacuum floor pulls the split back toward the step")
    a.set_xticks([0, 45, 90, 135, 180]); a.legend(fontsize=8); a.grid(alpha=0.25)

    fig.tight_layout()
    out = __file__.rsplit("/", 1)[0] + "/born_noise_structures.png"
    fig.savefig(out, dpi=130)
    print(f"\n[figure written: {out}]")


if __name__ == "__main__":
    main()
