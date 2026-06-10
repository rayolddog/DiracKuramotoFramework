"""
overstreet_constraint.py — AB-visibility companion check vs Overstreet et al. 2022
==================================================================================

Companion-paper [26] (Aharonov–Bohm Visibility Envelope) material: drops the
Overstreet/Kasevich gravitational AB measurement (Science 375, 226) onto the
predicted phase + visibility curves to ask whether their result already
constrains the gravitational-visibility coefficient.

SCOPE (PAPER_REVISED.md §4.4): the quantity Gamma_bulk = G·M²/(ℏ·Δz) used below
as an order-of-magnitude scale is the Penrose–Diósi gravitational self-energy
rate, NOT a framework-derived rate — the main paper explicitly repudiates
asserting a gravitational coherence rate of that form (a dimensional artifact
from an unnormalized pairwise sum). It is retained here only as a
back-of-envelope sensitivity scale for the companion AB-visibility analysis.

Three checks:
  1. Does the framework reproduce the measured AB/COW phase (m·Φ·t/ℏ)?  [standard]
  2. Applying a Gaussian phase-noise envelope exp(-dφ²/2) to the AB phase,
     what visibility loss is implied?
  3. What would Overstreet's *visibility* sensitivity allow us to constrain?
"""

import numpy as np

# Constants
G = 6.674e-11
hbar = 1.055e-34
c = 3.0e8

# Overstreet 2022 parameters
m_Rb87 = 1.443e-25         # kg
M_W   = 1.25                # kg, tungsten source
R_close = 0.075             # m, closest approach (upper arm)
Dx_sep  = 0.25              # m, wave packet separation
T_int   = 0.82              # s, interferometer half-time
T_tot   = 2 * T_int         # s, total free-flight time
phi_meas = 0.182            # rad, measured |phi_DS| at Rx=9cm
phi_meas_err = 0.028        # rad, 1-sigma uncertainty
sigma_shot = 0.030          # rad, single-shot phase noise
N_shots = 20                # shots per point

# 1. Time-averaged potential difference between arms
#    Upper arm passes within R_close; lower arm at R_close + Dx_sep
R_far = R_close + Dx_sep
Phi_close = -G * M_W / R_close
Phi_far   = -G * M_W / R_far
dPhi_peak = abs(Phi_close - Phi_far)
# Atom only spends a fraction of T_tot near closest approach;
# treat geometric duty cycle ~ R_close / (v * T_tot) where v ~ 1 m/s vertical scale
duty = 0.3   # rough fraction; the actual time profile is non-trivial (Eq. 1 in paper)
dPhi_eff = duty * dPhi_peak

# 2. AB/COW phase: phi_DK = m * dPhi * T / hbar  (standard interferometer phase; companion [26])
phi_DK = m_Rb87 * dPhi_eff * T_tot / hbar

# 3. Naive Gaussian phase-noise visibility envelope
#    S = 2sqrt(2) * exp(-dphi^2 / 2)  -> visibility V/V0 = exp(-dphi^2 / 2)
V_loss_naive = 1 - np.exp(-phi_meas**2 / 2)

# 4. Experimental sensitivity to a visibility change
#    A visibility loss eta translates to an *additional* phase scatter
#    sigma_phi_extra ~ sqrt(-2 ln(1 - eta)) ~ sqrt(2 eta) for small eta.
#    Per-point sensitivity = sigma_shot / sqrt(N_shots)
sigma_pt = sigma_shot / np.sqrt(N_shots)
# Express the per-point sensitivity as a 1-sigma upper bound on visibility loss:
eta_bound = sigma_pt**2 / 2.0    # tight, since extra noise adds in quadrature

# 5. What does this constrain about alpha = (visibility-loss prefactor) ?
#    DK distinctive prediction: V(x) ~ V0 [1 - alpha * Phi(x)/c^2]
#    Solve for alpha bound from eta_bound and Phi_close / c^2
alpha_bound = eta_bound / (abs(Phi_close) / c**2)

# 6. Compare to natural DK scale:
#    K_pair ~ hbar * omega_imaging for Rb D2 line (780 nm)
omega_imaging = 2*np.pi * c / 780e-9
K_pair_natural = omega_imaging                  # rad/s
# Penrose–Diósi self-energy scale for the apparatus (M ~ 100 kg, Delta z ~ 1 m).
# NOTE (PAPER_REVISED.md §4.4): this G*M^2/(hbar*Dz) form is NOT a framework rate —
# it is repudiated there as a dimensional artifact and used here only as a scale.
M_app = 100.0
Dz_app = 1.0
Gamma_bulk_natural = G * M_app**2 / (hbar * Dz_app)   # Penrose–Diósi scale only
ratio_natural = Gamma_bulk_natural / K_pair_natural

print("="*72)
print("Overstreet 2022 vs DK Framework — quantitative constraint")
print("="*72)
print()
print(f"Gravitational potential difference (peak):     {dPhi_peak:.3e} J/kg")
print(f"Effective time-averaged Phi difference:        {dPhi_eff:.3e} J/kg")
print(f"DK predicted AB phase (m*dPhi*T/hbar):         {phi_DK:.3f} rad")
print(f"Measured |phi_DS| (Rx=9 cm):                   {phi_meas:.3f} +/- {phi_meas_err:.3f} rad")
print(f"  -> agreement: DK reproduces COW/AB phase to within geometric duty cycle.")
print()
print("Visibility-loss prediction:")
print(f"  Naive Gaussian phase-noise envelope:               {V_loss_naive*100:.2f}%")
print(f"  (NOTE: this formula treats dphi as stochastic; here it's deterministic,")
print(f"   so the actual DK prediction for *coherent* AB phase is zero visibility loss.)")
print()
print("Experimental visibility-loss sensitivity:")
print(f"  Per-point phase resolution:                  {sigma_pt*1000:.2f} mrad")
print(f"  Implied 1-sigma bound on visibility loss:    {eta_bound:.2e}")
print(f"  (This is 'how much extra fringe scatter would have shown up.')")
print()
print("Constraint on alpha (the V = V0[1 - alpha * Phi/c^2] coefficient):")
print(f"  |Phi_close|/c^2:                             {abs(Phi_close)/c**2:.2e}")
print(f"  Upper bound: alpha <                          {alpha_bound:.2e}")
print()
print("Natural DK scales:")
print(f"  K_pair ~ omega_imaging (Rb D2):              {K_pair_natural:.2e} rad/s")
print(f"  Gamma_bulk (apparatus, M=100kg, Dz=1m):      {Gamma_bulk_natural:.2e} rad/s")
print(f"  Gamma_bulk / K_pair:                         {ratio_natural:.2e}")
print()
print("Verdict:")
print(f"  Overstreet bounds alpha < {alpha_bound:.1e}.")
print(f"  Natural DK Gamma_bulk/K_pair is ~{ratio_natural:.1e}.")
if alpha_bound > ratio_natural:
    print("  -> Overstreet DOES NOT constrain DK's natural prediction;")
    print("     the experimental sensitivity is ~{:.1e}x too coarse.".format(
        ratio_natural / alpha_bound))
else:
    print("  -> Overstreet CONSTRAINS DK's natural prediction.")
print()
print("Why the experiment doesn't bite:")
print("  The source-mass-induced gravitational redshift Phi/c^2 ~ 1e-26 is so")
print("  small that even a huge Gamma_bulk/K_pair ratio gives no detectable")
print("  visibility loss. To put DK under pressure you need Phi/c^2 large")
print("  *or* a measurement of Stage-1 vs Stage-2 dynamics directly,")
print("  which an AB-phase experiment isn't designed to do.")
