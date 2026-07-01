#!/usr/bin/env python3
r"""
born_mass_penrose.py
====================

born_decisive.py showed Born needs the Stage-2 bath to couple to the SCALAR/MASS
density psi-bar psi = sigma_x (not the gauge current sigma_z).  A bath coupling to the
mass density is precisely the Diosi-Penrose (DP) gravitational operator.  So the
"mass as a dynamical synchronization field" escape hatch IS, structurally, gravitational
decoherence in the mass-density basis -- "back to Penrose."

This script tests the FATAL quantitative problem of that route: the rate.  The DP /
Penrose objective-reduction timescale for a mass M of size R held in a spatial
superposition is, to order of magnitude,
        E_G ~ G M^2 / R        (gravitational self-energy of the mass difference)
        tau_DP ~ hbar / E_G .
We compare tau_DP across scales to the timescale on which real measurement actually
happens (EM detection, ~ns or faster).

Result (preview): a single electron/atom has tau_DP ~ 10^16 - 10^24 s (>> age of the
universe) -- gravitational mass coupling is ~30 orders of magnitude too slow to drive
measurement.  It becomes fast (sub-microsecond) ONLY at the MACROSCOPIC DETECTOR-POINTER
scale (~10^-6 kg) -- which is exactly Penrose's own resolution (collapse happens at the
heavy pointer, not the particle).  So the right OPERATOR forces the locus to the detector
and localizes the POINTER's mass-configuration (position), not the chiral phase -- and DP
itself does NOT derive the Born weights (they are normalized in by hand, as in CSL).
"""

import numpy as np

G = 6.674e-11          # N m^2 / kg^2
hbar = 1.054571817e-34 # J s
amu = 1.66053907e-27   # kg
age_universe = 4.35e17 # s


def tau_DP(M, R):
    """Order-of-magnitude DP/Penrose reduction time tau ~ hbar / (G M^2 / R)."""
    E_G = G * M**2 / R
    return hbar / E_G, E_G


def main():
    print("=" * 86)
    print("ESCAPE-HATCH RATE TEST: 'mass as sync field' = DP gravitational mass-density coupling")
    print("  tau_DP ~ hbar / (G M^2 / R)   (schematic Penrose self-energy timescale)")
    print("=" * 86)
    systems = [
        ("electron",            9.109e-31,   3.86e-13),  # R ~ Compton wavelength
        ("silver atom",         107.87*amu,  1.4e-10),   # R ~ atomic size
        ("large molecule (10^5 amu)", 1e5*amu, 1e-9),
        ("DP-test nanosphere (~10^-14 kg)", 1e-14, 1e-7),
        ("detector micro-pointer (~10^-9 kg)", 1e-9, 1e-5),
        ("detector pointer grain (~10^-6 kg)", 1e-6, 1e-4),
    ]
    print(f"\n  {'system':36s} {'M (kg)':>10s} {'E_G (J)':>11s} {'tau_DP (s)':>12s}   vs measurement")
    print("  " + "-" * 84)
    for name, M, R in systems:
        tau, E_G = tau_DP(M, R)
        if tau > age_universe:
            verdict = f"{tau/age_universe:.0e}x age of universe -- DEAD"
        elif tau > 1e-6:
            verdict = "slower than a real detector"
        else:
            verdict = "FAST: sub-microsecond (Penrose's locus)"
        print(f"  {name:36s} {M:10.2e} {E_G:11.2e} {tau:12.2e}   {verdict}")

    print("\n  Reference timescales for ACTUAL measurement (EM-driven, the gauge sigma_z channel):")
    print("    spontaneous emission ~ 1e-9 s ;  ionization/detection ~ 1e-12-1e-15 s")
    print("\n  => The Born-compatible operator (mass density) has a NEGLIGIBLE single-particle")
    print("     rate; it only becomes fast at the MACROSCOPIC POINTER (>~1e-9 kg).  So 'mass as")
    print("     sync field' forces the measurement locus onto the heavy detector -- Penrose's")
    print("     own picture -- and localizes the POINTER's position, not the chiral sigma_x phase.")

    print("\n" + "=" * 86)
    print("CONCEPTUAL MAP:  is the escape hatch 'back to Penrose'?")
    print("=" * 86)
    rows = [
        ("coupling operator",     "D[sigma_x] = D[psi-bar psi] (mass/scalar density)", "DP: couples to mass density rho(x)  -> SAME"),
        ("regime",               "gravity-dominated, EM/thermal removed",             "DP: gravity-dominated              -> SAME"),
        ("locus (from rate)",    "macroscopic detector pointer (mass)",               "DP/Penrose: heavy pointer collapses -> SAME"),
        ("mechanism",            "no-collapse, dissipative (needs bath)",             "Penrose: objective collapse (intrinsic) -> DIFFERS"),
        ("",                     "(= Diosi's stochastic/Lindblad reading)",           "Diosi: decoherence master eq      -> CLOSE"),
        ("Born weights",         "still NOT derived (the open problem)",              "DP/CSL: normalized in by hand     -> NEITHER derives"),
    ]
    for a, b, c in rows:
        print(f"  {a:18s} | framework hatch: {b:48s}")
        print(f"  {'':18s} | {c}")
    print("\n  VERDICT: following the Born requirement (mass-density coupling) leads straight to")
    print("  Diosi-Penrose -- same operator, same regime, same detector locus.  It converts MCI")
    print("  from a DP *rival* into a no-collapse DP *cousin*.  And it does NOT solve Born: DP/CSL")
    print("  do not derive |alpha|^2 either (they post-impose it via noise normalization).  So the")
    print("  Born-measure problem is ROBUST across both programs -- the hatch relocates it, not closes it.")

    make_figure(systems)


def make_figure(systems):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print(f"\n[figure skipped: {e}]"); return
    Ms = np.logspace(-31, -4, 200)
    # use a smooth R(M) ~ (M/rho)^(1/3) with rho~3000 kg/m^3 for the curve
    rho = 3000.0
    R = (3 * Ms / (4 * np.pi * rho))**(1/3)
    R = np.maximum(R, 3.86e-13)
    taus = np.array([tau_DP(M, r)[0] for M, r in zip(Ms, R)])

    fig, ax = plt.subplots(figsize=(9.5, 6))
    ax.loglog(Ms, taus, "C0-", lw=2.5, label=r"$\tau_{DP}\sim\hbar/(GM^2/R)$ (gravitational mass coupling)")
    ax.axhspan(1e-15, 1e-9, color="C2", alpha=0.18, label="EM measurement (gauge $\\sigma_z$): ns and faster")
    ax.axhline(4.35e17, color="C3", ls="--", lw=1.5, label="age of the universe")
    ax.axhline(1e-6, color="0.5", ls=":", lw=1.2, label="real-detector speed (~$\\mu$s)")
    for name, M, Rr in systems:
        tau = tau_DP(M, Rr)[0]
        ax.plot(M, tau, "ko", ms=6)
        ax.annotate(name.split("(")[0].strip(), (M, tau), fontsize=7,
                    xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel("mass M (kg)"); ax.set_ylabel(r"reduction time $\tau_{DP}$ (s)")
    ax.set_title("'Mass as sync field' = DP gravitational coupling: right operator, hopeless rate\n"
                 "fast only at the macroscopic pointer (Penrose's locus), not the particle")
    ax.legend(fontsize=8, loc="upper right"); ax.grid(alpha=0.25, which="both")
    fig.tight_layout()
    out = __file__.rsplit("/", 1)[0] + "/born_mass_penrose.png"
    fig.savefig(out, dpi=130)
    print(f"\n[figure written: {out}]")


if __name__ == "__main__":
    main()
