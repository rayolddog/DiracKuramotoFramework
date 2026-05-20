import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent

"""
sg_angular.py -- Stern-Gerlach Angular Dependence Prediction
=============================================================

Implements the KPS (Kuramoto Phase Synchronization) model prediction for
angular dependence of Stern-Gerlach splitting relative to gravity.

PHYSICAL PICTURE
----------------
In the KPS framework, the gravitational Kuramoto coupling synchronizes
spin states to the local gravitational bulk. When the SG magnetic field
axis is rotated by angle theta relative to the gravitational field
direction, only the projection of gravity onto the SG axis contributes
to the synchronization rate:

    Gamma_eff(theta) = Gamma_0 * |cos(theta)|

where:
    theta   : angle between SG magnetic field axis and local gravity
    Gamma_0 : synchronization rate when SG axis is aligned with gravity

This predicts that the SG beam splitting acquires a small angular
modulation on top of the standard magnetic splitting. The fractional
change in splitting is:

    delta_splitting / splitting_0 = Gamma_eff(theta) * t / (mu_B * dB/dz * t)

TWO COUPLING ESTIMATES
----------------------
1. KPS coupling (stronger): Gamma_0 = m * delta_phi_local / hbar
   For silver atoms in a typical SG apparatus (delta_z ~ 1 mm):
     delta_phi_local = g * delta_z ~ 9.8 * 1e-3 = 9.8e-3 J/kg
     Gamma_0 ~ 1.791e-25 * 9.8e-3 / 1.055e-34 ~ 1.66e7 rad/s
   This gives a ~4% effect (as estimated in the KPS framework discussions).

2. Penrose-Diosi coupling (weaker): Gamma_0 = G * m^2 / (hbar * delta_z)
   For silver atoms:
     Gamma_0 ~ 6.674e-11 * (1.791e-25)^2 / (1.055e-34 * 1e-3) ~ 2.03e-8 rad/s
   This gives an essentially undetectable effect (~10^-15 fractional change).

CONFOUNDING EFFECTS
-------------------
Any experiment measuring this angular dependence must subtract:
1. Earth's magnetic field (~50 microT): produces cos(theta) splitting ~1-10%
   depending on SG gradient strength. Must be shielded or subtracted.
2. Gravitational sag: beam deflects under gravity during flight, producing
   a geometric cos(theta) effect proportional to t^2 * g * cos(theta).
   Well-understood and calculable.
3. Coriolis effects: negligible for typical SG dimensions.
4. Magnetic field inhomogeneity: gradient variations with orientation.

The KPS prediction is DISTINCT from these because:
- It affects the SPLITTING (difference between spin-up and spin-down),
  not just the overall beam deflection
- It has a specific mass dependence (heavier particles show larger effect)
- The confounding effects are well-characterized and can be subtracted

REFERENCES
----------
- KPS Framework Papers 1-3 (SchrodingerBell repository)
- CRITIQUE3.md Section D1: "Genuinely new if the coupling strength is correct"
- Penrose, R. "On Gravity's Role in Quantum State Reduction" (1996)
- Gerlach, W. and Stern, O. (1922) original SG experiment
"""

# ─── Physical constants ───────────────────────────────────────────────
G = 6.674e-11         # gravitational constant (m^3 kg^-1 s^-2)
hbar = 1.055e-34      # reduced Planck constant (J s)
g_earth = 9.81        # gravitational acceleration at Earth surface (m/s^2)
mu_B = 9.274e-24      # Bohr magneton (J/T)
k_B = 1.381e-23       # Boltzmann constant (J/K)

# Particle parameters
m_silver = 1.791e-25  # Ag-107 mass (kg)
m_C60 = 1.197e-24     # C60 buckyball mass (kg)
m_electron = 9.109e-31

# Typical SG experimental parameters
dBdz_typical = 100    # typical SG gradient (T/m)
L_sg = 0.1            # magnet length (m)
v_beam = 600          # silver atom beam velocity (m/s) at ~1000 K
t_flight = L_sg / v_beam  # time in SG magnet region

# Superposition separation in SG
delta_z_sg = 1e-3     # ~1 mm splitting (m)

# ─── Model functions ──────────────────────────────────────────────────

def gamma_kps(m, delta_phi):
    """KPS gravitational synchronization rate: Gamma = m * delta_phi / hbar."""
    return m * np.abs(delta_phi) / hbar


def gamma_penrose_diosi(m, delta_z):
    """Penrose-Diosi rate: Gamma = G * m^2 / (hbar * delta_z)."""
    return G * m**2 / (hbar * np.abs(delta_z))


def gamma_effective(gamma_0, theta):
    """
    Angular modulation of the gravitational coupling.

    Gamma_eff(theta) = Gamma_0 * |cos(theta)|

    When theta=0 (SG aligned with gravity): full coupling.
    When theta=pi/2 (SG perpendicular to gravity): zero coupling.
    """
    return gamma_0 * np.abs(np.cos(theta))


def fractional_splitting_change(gamma_0, theta, t, m, dBdz):
    """
    Fractional change in SG splitting due to gravitational coupling.

    The standard SG splitting is:
        Delta_x = mu_B * dB/dz * t^2 / (2 * m)  [for spin-1/2]

    The gravitational coupling adds:
        delta(Delta_x) = hbar * Gamma_eff * t / (2 * m * v)

    Fractional change:
        delta(Delta_x) / Delta_x = hbar * Gamma_eff / (mu_B * dB/dz * t)

    Parameters
    ----------
    gamma_0 : float
        Base synchronization rate (rad/s) when aligned with gravity
    theta : float or array
        Angle between SG axis and gravity (radians)
    t : float
        Time in magnetic field region (s)
    m : float
        Particle mass (kg)
    dBdz : float
        Magnetic field gradient (T/m)

    Returns
    -------
    fractional : float or array
        Relative change in splitting
    """
    gamma_eff = gamma_effective(gamma_0, theta)
    # Standard splitting force: F_mag = mu_B * dB/dz
    # Gravitational sync contribution: F_grav ~ hbar * Gamma_eff / delta_z
    # Fractional = Gamma_eff * hbar / (mu_B * dBdz * t)
    return gamma_eff * hbar / (mu_B * dBdz * t)


def splitting_ratio(gamma_0, theta, t, m, dBdz):
    """
    Ratio of splitting at angle theta to splitting at theta=0.

    splitting(theta) / splitting(0) = 1 + fractional_change(theta) - fractional_change(0)

    Since the gravitational effect adds to the splitting:
        ratio = 1 + [Gamma_eff(theta) - Gamma_eff(0)] * hbar / (mu_B * dBdz * t)
              = 1 + Gamma_0 * (|cos(theta)| - 1) * hbar / (mu_B * dBdz * t)
    """
    delta_frac = gamma_0 * (np.abs(np.cos(theta)) - 1.0) * hbar / (mu_B * dBdz * t)
    return 1.0 + delta_frac


# ─── Plotting ─────────────────────────────────────────────────────────

def make_plots():
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle(
        'Stern-Gerlach Angular Dependence -- KPS Framework Predictions',
        fontsize=14, fontweight='bold', y=0.98
    )

    theta = np.linspace(0, np.pi, 500)
    theta_deg = np.degrees(theta)

    # ── Panel 1: Splitting ratio vs angle for different coupling strengths ──
    ax = axes[0, 0]

    # Define a range of coupling strengths to illustrate the effect
    delta_phi_local = g_earth * delta_z_sg  # ~ 9.8e-3 J/kg for 1mm
    gamma_kps_ag = gamma_kps(m_silver, delta_phi_local)
    gamma_pd_ag = gamma_penrose_diosi(m_silver, delta_z_sg)

    coupling_strengths = [
        (gamma_kps_ag * 10, r'$10 \times$ KPS', 'C2', '-'),
        (gamma_kps_ag, r'KPS: $m\Delta\Phi_{local}/\hbar$', 'C0', '-'),
        (gamma_kps_ag * 0.1, r'$0.1 \times$ KPS', 'C1', '--'),
        (gamma_pd_ag, r'Penrose-Di\'{o}si', 'C3', ':'),
    ]

    for gamma_0, label, color, ls in coupling_strengths:
        ratio = splitting_ratio(gamma_0, theta, t_flight, m_silver, dBdz_typical)
        ax.plot(theta_deg, ratio, label=label, color=color, linestyle=ls, linewidth=2)

    ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.4)
    ax.set_xlabel(r'Angle $\theta$ (degrees)', fontsize=12)
    ax.set_ylabel('Splitting ratio vs $\\theta = 0$', fontsize=12)
    ax.set_title('Splitting ratio vs angle (Ag atoms)', fontsize=11)
    ax.legend(fontsize=8, loc='lower left')
    ax.set_xlim(0, 180)
    ax.grid(True, alpha=0.3)

    # ── Panel 2: The 4% KPS effect in detail ──────────────────────────
    ax = axes[0, 1]

    # KPS prediction for different particles
    particles = [
        (m_electron, 'Electron', 'C4'),
        (m_silver,   'Silver (Ag-107)', 'C0'),
        (m_C60,      'C$_{60}$ buckyball', 'C2'),
    ]

    for m, label, color in particles:
        gamma_0 = gamma_kps(m, delta_phi_local)
        frac = fractional_splitting_change(gamma_0, theta, t_flight, m, dBdz_typical)
        ax.plot(theta_deg, frac * 100, label=label, color=color, linewidth=2)

    ax.set_xlabel(r'Angle $\theta$ (degrees)', fontsize=12)
    ax.set_ylabel('Fractional splitting change (%)', fontsize=12)
    ax.set_title(r'KPS coupling: $\Gamma = m\Delta\Phi_{local}/\hbar$', fontsize=11)
    ax.legend(fontsize=9)
    ax.set_xlim(0, 180)
    ax.grid(True, alpha=0.3)

    # Annotate the predicted effect size at theta=0
    gamma_ag = gamma_kps(m_silver, delta_phi_local)
    frac_0_ag = fractional_splitting_change(gamma_ag, 0, t_flight, m_silver, dBdz_typical)
    ax.annotate(
        f'Ag at $\\theta=0$: {frac_0_ag*100:.2f}%',
        xy=(5, frac_0_ag * 100), fontsize=9,
        xytext=(40, frac_0_ag * 100 * 1.3),
        arrowprops=dict(arrowstyle='->', color='C0'),
        color='C0'
    )

    # ── Panel 3: Penrose-Diosi prediction (essentially zero) ─────────
    ax = axes[1, 0]

    for m, label, color in particles:
        gamma_0 = gamma_penrose_diosi(m, delta_z_sg)
        frac = fractional_splitting_change(gamma_0, theta, t_flight, m, dBdz_typical)
        ax.plot(theta_deg, frac, label=label, color=color, linewidth=2)

    ax.set_xlabel(r'Angle $\theta$ (degrees)', fontsize=12)
    ax.set_ylabel('Fractional splitting change (absolute)', fontsize=12)
    ax.set_title(r"Penrose-Di\'{o}si: $\Gamma = Gm^2/(\hbar\Delta z)$", fontsize=11)
    ax.legend(fontsize=9)
    ax.set_xlim(0, 180)
    ax.grid(True, alpha=0.3)

    # Add annotation about the scale
    ax.text(0.5, 0.5,
            'Effect is $\\sim 10^{-15}$ or smaller\n'
            'for all particles.\n\n'
            'Completely undetectable with\n'
            'current technology.',
            transform=ax.transAxes, fontsize=12, ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow',
                      edgecolor='orange', alpha=0.8))

    # ── Panel 4: Confounding effects ──────────────────────────────────
    ax = axes[1, 1]
    ax.axis('off')

    # Build a table of confounding effects
    confound_data = [
        [
            "Earth's B field\n(~50 $\\mu$T)",
            r"$\mu_B B_{Earth} \cos\theta$"
            "\n/ ($\\mu_B$ dB/dz $\\cdot$ $\\Delta z$)",
            "1-10%\n(depends on\nSG gradient)",
            "Mu-metal\nshielding +\nsubtraction"
        ],
        [
            "Gravitational\nsag",
            r"$\frac{1}{2}g t^2 \cos\theta$"
            "\n/ $\\Delta z_{SG}$",
            f"{0.5 * g_earth * t_flight**2 / delta_z_sg * 100:.4f}%",
            "Well-known,\ncalculable"
        ],
        [
            "Coriolis\neffect",
            r"$2 v \Omega \sin\lambda$"
            "\n$\\cdot t^2 / \\Delta z$",
            "~$10^{-8}$%",
            "Negligible"
        ],
        [
            "Gradient\ninhomogeneity",
            r"$\delta(dB/dz)$"
            "\n/ dB/dz",
            "0.1-1%\n(setup\ndependent)",
            "Careful magnet\ndesign"
        ],
        [
            "KPS gravity\nprediction",
            r"$m\Delta\Phi_{local}$"
            "\n/ ($\\hbar \\mu_B$ dB/dz $t$)",
            f"{frac_0_ag*100:.2f}%\n(Ag atoms)",
            "NOVEL:\nmass-dependent\n$|\\cos\\theta|$"
        ],
    ]

    col_labels = ['Effect', 'Formula', 'Magnitude', 'Mitigation /\nSignature']

    table = ax.table(
        cellText=confound_data,
        colLabels=col_labels,
        loc='center',
        cellLoc='center',
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1.0, 2.8)

    # Style header
    for j in range(len(col_labels)):
        table[0, j].set_facecolor('#d4e6f1')
        table[0, j].set_text_props(fontweight='bold')

    # Highlight the KPS prediction row
    n_rows = len(confound_data)
    for j in range(len(col_labels)):
        table[n_rows, j].set_facecolor('#d5f5e3')

    ax.set_title(
        'Confounding effects vs KPS prediction\n'
        '(must be subtracted to isolate gravitational signal)',
        fontsize=11, pad=20
    )

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(_HERE / 'sg_angular.png', dpi=150,
                bbox_inches='tight')
    print("Saved sg_angular.png")

    # ── Print numerical summary ───────────────────────────────────────
    print("\n" + "="*70)
    print("NUMERICAL SUMMARY: SG Angular Dependence")
    print("="*70)
    print(f"SG parameters: dB/dz = {dBdz_typical} T/m, L = {L_sg} m, "
          f"v = {v_beam} m/s, t = {t_flight:.4e} s")
    print(f"Superposition separation: delta_z = {delta_z_sg} m")
    print(f"Local delta_phi = g * delta_z = {g_earth * delta_z_sg:.4e} J/kg")
    print()
    print(f"{'Particle':<15} {'KPS Gamma (rad/s)':<22} {'PD Gamma (rad/s)':<22} "
          f"{'KPS effect (%)':<18} {'PD effect':<18}")
    print("-"*70)

    for m, name in [(m_electron, 'Electron'), (m_silver, 'Silver (Ag)'),
                     (m_C60, 'C60')]:
        g_kps = gamma_kps(m, g_earth * delta_z_sg)
        g_pd = gamma_penrose_diosi(m, delta_z_sg)
        frac_kps = fractional_splitting_change(g_kps, 0, t_flight, m, dBdz_typical)
        frac_pd = fractional_splitting_change(g_pd, 0, t_flight, m, dBdz_typical)
        print(f"{name:<15} {g_kps:<22.4e} {g_pd:<22.4e} "
              f"{frac_kps*100:<18.6f} {frac_pd:<18.4e}")

    print()
    print("Key discriminant: The KPS effect is mass-dependent and scales as")
    print("|cos(theta)|, while Earth's B field effect has a fixed magnitude")
    print("independent of particle mass. Running the experiment with particles")
    print("of different mass (e.g., Ag vs C60) at the same angle would")
    print("separate the gravitational signal from the magnetic background.")


if __name__ == '__main__':
    make_plots()
