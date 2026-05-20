"""
predict_visibility_vs_mass.py — DK falsifiability roadmap
==========================================================

For a candidate matter-wave interferometer (geometry + sensitivity), compute
the test-particle mass at which the DK Penrose-Diosi visibility prediction
becomes detectable. Treat that mass as the framework's falsification threshold
for that experiment.

DK visibility envelope (Penrose-Diosi self-gravity branch, EQUATIONS.md §7,
mirroring gravitational_bell.chsh_penrose_diosi):

    V(m) / V0 = exp( -(Gamma_PD * t)^2 / 2 ),   Gamma_PD = G * m^2 / (hbar * dz)

Solving V0 - V = sigma_V for m gives:

    m_falsify = ( sqrt(-2 ln(1 - sigma_V)) * hbar * dz / (G * t) )^(1/2)

Below this mass, an experiment cannot distinguish DK from standard QM.
Above it, the framework predicts a contrast loss the experiment can resolve.

Companion mode: gravitational-source-driven (Gamma_KPS, mass-linear). Set
    delta_Phi_J_per_kg > 0 to override Gamma_PD with Gamma_KPS = m * dPhi / hbar.

Usage
-----
    python3 predict_visibility_vs_mass.py
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent

G = 6.674e-11
hbar = 1.055e-34
amu = 1.66054e-27   # kg per dalton

# ---------------------------------------------------------------------------
# Core predictions
# ---------------------------------------------------------------------------

def gamma_pd(m_kg, dz_m):
    """Penrose-Diosi self-gravity rate Gamma = G m^2 / (hbar dz).  rad/s."""
    return G * m_kg**2 / (hbar * dz_m)

def gamma_kps(m_kg, dPhi_Jkg):
    """KPS source-mass-driven rate Gamma = m * dPhi / hbar.  rad/s."""
    return m_kg * dPhi_Jkg / hbar

def visibility(m_kg, dz_m, t_s, dPhi=None):
    """DK fringe-contrast prediction. If dPhi is given, uses Gamma_KPS;
    otherwise uses Gamma_PD. Returns V/V0 in [0, 1]."""
    Gamma = gamma_kps(m_kg, dPhi) if dPhi else gamma_pd(m_kg, dz_m)
    dphi = Gamma * t_s
    return np.exp(-dphi**2 / 2.0)

def m_falsify(dz_m, t_s, sigma_V, dPhi=None):
    """Smallest test-particle mass at which DK predicts a visibility loss
    of magnitude sigma_V (i.e., 1-sigma detection threshold).

    sigma_V should be the experiment's *resolution* on visibility:
    e.g., 0.01 if it can confirm V/V0 = 0.99 against V/V0 = 1.00.
    """
    dphi_thresh = np.sqrt(-2.0 * np.log(1.0 - sigma_V))
    if dPhi:
        # Gamma_KPS branch: m = dphi_thresh * hbar / (dPhi * t)
        return dphi_thresh * hbar / (dPhi * t_s)
    # Gamma_PD branch: m = sqrt(dphi_thresh * hbar * dz / (G * t))
    return np.sqrt(dphi_thresh * hbar * dz_m / (G * t_s))

# ---------------------------------------------------------------------------
# Experimental landscape
# ---------------------------------------------------------------------------
# Each entry: (label, test_mass_kg, dz_m, t_s, sigma_V, mode, notes)
#   mode = "PD" for self-gravity branch (no external source), "KPS:<dPhi>"
#   for source-driven (give dPhi in J/kg).
#
# Numbers below are order-of-magnitude representative — adjust to your
# preferred reference values; the framework prediction is robust to ~factor-2
# variations in any single column.

EXPERIMENTS = [
    # label,                    m_kg,        dz_m,    t_s,     sigma_V, mode,        notes
    ("Overstreet 2022 (Stanford)",
                                1.443e-25,   0.25,    1.64,    2.3e-5,  "PD",
                                "Rb-87, 52hbar k, source-mass-driven AB phase"),
    ("KDTL Vienna (Arndt 2019)",
                                25000*amu,   2.66e-7, 8e-3,    0.01,    "PD",
                                "Oligoporphyrin near-field Talbot-Lau"),
    ("OTIMA Vienna (proposed)",
                                1e6 * amu,   1e-6,    0.1,     0.01,    "PD",
                                "Optical TL, decoherence-free regime target"),
    ("Levitated optomechanics (current)",
                                1e9 * amu,   1e-8,    1e-3,    0.05,    "PD",
                                "Silica nanosphere, ground-state cooled"),
    ("MAQRO (space proposal)",
                                1e10 * amu,  1e-7,    100.0,   0.01,    "PD",
                                "Microgravity, long coherence time"),
    ("BMV-style (mug entanglement)",
                                1e-9,        1e-6,    1.0,     0.01,    "PD",
                                "Bose-Marletto-Vedral target geometry"),
]

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def kg_to_dalton(m_kg):
    return m_kg / amu

def fmt_mass(m_kg):
    """Human-friendly mass."""
    da = kg_to_dalton(m_kg)
    if da < 1e3:
        return f"{da:.1f} Da"
    if da < 1e6:
        return f"{da/1e3:.2f} kDa"
    if da < 1e9:
        return f"{da/1e6:.2f} MDa"
    if da < 1e12:
        return f"{da/1e9:.2f} GDa"
    if da < 1e18:
        return f"{da/1e12:.2f} TDa"
    return f"{m_kg:.2e} kg"

def report():
    print("="*86)
    print("DK Falsifiability Roadmap — Penrose-Diósi visibility branch")
    print("="*86)
    print(f"{'Experiment':<32} {'m_test':<14} {'m_falsify':<14} {'V/V0':<10} {'Status':<14}")
    print("-"*86)

    for label, m_kg, dz, t, sV, mode, _ in EXPERIMENTS:
        if mode.startswith("KPS"):
            dPhi = float(mode.split(":")[1])
            mF = m_falsify(dz, t, sV, dPhi=dPhi)
            V  = visibility(m_kg, dz, t, dPhi=dPhi)
        else:
            mF = m_falsify(dz, t, sV)
            V  = visibility(m_kg, dz, t)

        ratio = m_kg / mF
        if ratio < 0.1:
            status = f"safe x{1/ratio:.1e}"
        elif ratio < 1.0:
            status = f"closing x{1/ratio:.2f}"
        else:
            status = f"FALSIFIED x{ratio:.1f}"

        print(f"{label:<32} {fmt_mass(m_kg):<14} {fmt_mass(mF):<14} "
              f"{V:<10.6f} {status:<14}")

    print()
    print("Reading the 'Status' column:")
    print("  safe x<N>     : test mass is N x below DK threshold; experiment cannot")
    print("                  distinguish DK from standard QM.")
    print("  closing x<r>  : within an order of magnitude — next-gen variant could bite.")
    print("  FALSIFIED x<f>: DK predicts a visibility loss the experiment should already")
    print("                  resolve. If the experiment instead saw full standard-QM")
    print("                  contrast, the framework is in tension.")
    print()
    print("How to read m_falsify:")
    print("  This is the smallest test-particle mass at which the experiment's")
    print("  visibility resolution sigma_V equals DK's predicted loss exp(-(Gm^2 t/hbar dz)^2 / 2).")
    print("  It scales as (sigma_V * dz / t)^(1/4), so longer coherence time and ")
    print("  smaller superposition separation tighten the bound (smaller m_falsify).")
    print("  Note dz appears in the numerator: a larger superposition makes self-gravity")
    print("  weaker per unit mass (Gm^2/dz), so larger dz raises m_falsify.")
    print()
    print("Caveats:")
    print("  - Uses Penrose-Diosi self-gravity branch (no external source mass).")
    print("    Source-mass-driven experiments (Overstreet) feed Gamma_KPS, which")
    print("    is mass-linear, not mass-quadratic.")
    print("  - sigma_V is the *visibility* resolution, not the phase resolution.")
    print("    For an interferometer where you only get a phase readout, convert")
    print("    via sigma_V ~ sigma_phi^2 / 2 (small-loss limit).")
    print("  - dz here is the framework's 'self-gravitational separation', taken to")
    print("    be the spatial-superposition extent. For a particle in a ground-state-")
    print("    cooled trap, the relevant dz is the wavepacket separation, not the")
    print("    trap size.")

# ---------------------------------------------------------------------------
# Falsification-mass curves (dz, t) -> m_falsify, for plotting
# ---------------------------------------------------------------------------

def m_falsify_grid(dz_array, t_array, sigma_V=0.01):
    """Return 2D grid of m_falsify (kg) over (dz, t)."""
    DZ, T = np.meshgrid(dz_array, t_array, indexing='ij')
    return np.sqrt(np.sqrt(-2.0 * np.log(1.0 - sigma_V)) * hbar * DZ / (G * T))


if __name__ == "__main__":
    report()

    # Optional: produce a 2D contour plot of m_falsify across the (dz, t) plane
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        dz = np.logspace(-9, -1, 80)   # 1 nm to 10 cm
        t  = np.logspace(-3, 3, 80)    # 1 ms to 1000 s
        M = m_falsify_grid(dz, t, sigma_V=0.01) / amu  # in Da

        fig, ax = plt.subplots(figsize=(8, 6))
        cs = ax.contourf(np.log10(dz), np.log10(t),
                         np.log10(M.T),
                         levels=np.arange(0, 22, 1),
                         cmap='viridis')
        plt.colorbar(cs, ax=ax, label=r'$\log_{10}\,m_\mathrm{falsify}$ (Da)')

        # Overlay current/proposed experiments
        for label, m_kg, dz_e, t_e, _, _, _ in EXPERIMENTS:
            ax.plot(np.log10(dz_e), np.log10(t_e), 'wo', markeredgecolor='k')
            ax.annotate(label.split('(')[0].strip(),
                        xy=(np.log10(dz_e), np.log10(t_e)),
                        xytext=(5, 5), textcoords='offset points',
                        fontsize=8, color='white',
                        path_effects=None)

        ax.set_xlabel(r'$\log_{10}\,\Delta z$ (m)')
        ax.set_ylabel(r'$\log_{10}\,t$ (s)')
        ax.set_title(r'DK falsification mass vs (Δz, t) at $\sigma_V = 0.01$')
        plt.tight_layout()
        plt.savefig(_HERE / 'predict_visibility_vs_mass.png', dpi=140, bbox_inches='tight')
        print("\nSaved predict_visibility_vs_mass.png")
    except ImportError:
        print("\n(matplotlib not available; skipping contour plot.)")
