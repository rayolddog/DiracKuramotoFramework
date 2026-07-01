#!/usr/bin/env python3
r"""
silver_twoslit_noise.py
=======================

Combined-design proposal + simulation:
    a SILVER (Ag, S=1/2 Stern-Gerlach atom) near-field Talbot-Lau matter-wave
    interferometer with a DOWNSTREAM Stern-Gerlach spin analyzer, used to
    compare the NOISE-INDUCED FRINGE BLUR predicted by

        (A) standard quantum mechanics  (Gaussian dephasing / decoherence theory)
        (B) the two-basin "strength-of-attractor" postulate
            (DISCRETIZATION_AS_SYNC_PAPER.md Sec 3.2 ; phi_dissipative_check.py)

Why silver:  ground state ^2S_{1/2}, pure electron-spin-1/2 moment, zero orbital
angular momentum -> the cleanest physical realization of the sigma_x binary
(the 0/pi basins).  The Talbot-Lau geometry is forced because lambda_dB ~ pm.

------------------------------------------------------------------------------
THE PHASE VARIABLE
------------------------------------------------------------------------------
phi = relative phase between the two interfering paths (= the equatorial azimuth
of the chiral/interference qubit in phi_dissipative_check.py).  The measured
fringe contrast after averaging over phase noise is the standard result

        V_obs = V_0 * |<exp(i phi)>|       (ensemble average over the noise).

Environmental noise (thermal photon scattering, stray EM fields, vibration)
enters as a stochastic kick on phi:

        d phi = ( -gamma sin 2phi  -  eps sin phi ) dt  +  sqrt(2 D) dW.

  gamma : STRENGTH OF THE ATTRACTOR (2nd-harmonic measurement coupling that makes
          the 0/pi binary).  In MCI gamma is a STAGE-2 (detector) quantity; the
          central experimental question is whether ANY of it reaches the
          STAGE-1 propagating fringe phase.
  eps   : faint polar bias (1st harmonic, the Sec 2.3 term).
  D     : noise strength.  We use the experimentally meaningful knob
          sigma^2 = 2 D T_transit  = the phase variance pure dephasing WOULD
          accumulate in transit.  Thermal/EM noise dials sigma^2 up.

MODELS
  (A) STANDARD QM  = gamma = eps = 0  -> pure Gaussian dephasing:
          V_QM = exp(-sigma^2 / 2)      (immediate, smooth exponential).
  (B) TWO-BASIN    = gamma > 0.  The attractor is a restoring force toward the
          fringe phase (well at 0).  It CAPS the in-well variance at D/(2gamma)
          instead of letting it grow ~2 D T, so for weak noise it PROTECTS the
          fringe:
          V_2b(plateau) ~ exp(-sigma^2 / (8 gamma))   (T-independent plateau),
          until Kramers escape over the pi/2 barrier (rate ~ exp(-gamma/D)
          = exp(-2 gamma / sigma^2)) lets trajectories hop to the antipodal pi
          well; once the two wells equalize, the antipodal fringes cancel and
          V -> 0 (a CLIFF near sigma^2 ~ 2 gamma).

  => DISTINGUISHING PREDICTION (if gamma touches the propagating phase):
     plateau-then-cliff, with the cliff position set by the ATTRACTOR STRENGTH
     gamma -- qualitatively unlike QM's immediate exp decay.
     If gamma = 0 in flight (strict MCI), B == A and the fringe channel CANNOT
     tell them apart -- the discriminator then lives only in the correlated
     Stern-Gerlach spin channel (Part 4).
"""

import numpy as np

# =============================================================================
# PART 0  --  silver parameters and the forced Talbot-Lau geometry
# =============================================================================
h = 6.62607015e-34          # J s
hbar = h / (2 * np.pi)
kB = 1.380649e-23           # J/K
amu = 1.66053907e-27        # kg
m_Ag = 107.8682 * amu       # silver atomic mass


def silver_geometry(T_oven=1300.0, grating_period_nm=257.0, n_talbot=1):
    """Print the de Broglie wavelength, Talbot length, transit time for an Ag beam."""
    v = np.sqrt(3 * kB * T_oven / m_Ag)          # rms thermal speed from the oven
    lam = h / (m_Ag * v)                         # de Broglie wavelength
    g = grating_period_nm * 1e-9
    L_T = g**2 / lam                             # Talbot length
    L_int = 2 * n_talbot * L_T                   # ~ two Talbot lengths grating-grating
    t_transit = L_int / v
    print("=" * 74)
    print("PART 0  --  SILVER Talbot-Lau interferometer parameters")
    print("=" * 74)
    print(f"  oven temperature                T   = {T_oven:.0f} K")
    print(f"  rms speed                       v   = {v:.0f} m/s")
    print(f"  de Broglie wavelength        lambda  = {lam*1e12:.2f} pm")
    print(f"  grating period                  g   = {grating_period_nm:.0f} nm")
    print(f"  Talbot length              L_T=g^2/l = {L_T*1e3:.2f} mm")
    print(f"  interferometer length        L_int   = {L_int*1e3:.2f} mm  (2 Talbot lengths)")
    print(f"  transit time              t_transit  = {t_transit*1e6:.1f} us")
    print(f"  (cf. C60 ~2.8 pm worked; cold He ~50-100 pm.  Ag ~{lam*1e12:.0f} pm is")
    print(f"   in the proven heavy-particle near-field regime.)")
    return dict(v=v, lam=lam, L_T=L_T, t_transit=t_transit)


# =============================================================================
# PART 1  --  Langevin integrator for the relative phase  phi
# =============================================================================
def langevin_visibility(sigma2_grid, gamma, eps=0.0, n=8000, T=1.0, dt=2e-3,
                         phi0=0.0, seed=0):
    """
    For each injected-noise value sigma^2 = 2 D T, integrate
        d phi = (-gamma sin2phi - eps sin phi) dt + sqrt(2D) dW
    over transit time T from phi0, return:
      V      : fringe visibility |<exp(i phi)>|
      Sbin   : "binary sharpness" = fraction of trajectories within pi/4 of a well (0 or pi)
      frac_pi: fraction that ended in the pi well (basin-flip population)
    gamma = 0 reproduces standard-QM Gaussian dephasing  V = exp(-sigma^2/2).
    """
    rng = np.random.default_rng(seed)
    nsteps = int(round(T / dt))
    V = np.empty_like(sigma2_grid)
    Sbin = np.empty_like(sigma2_grid)
    frac_pi = np.empty_like(sigma2_grid)
    for i, s2 in enumerate(sigma2_grid):
        D = s2 / (2.0 * T)                       # sigma^2 = 2 D T
        sq = np.sqrt(2.0 * D * dt)
        phi = np.full(n, phi0, dtype=float)
        for _ in range(nsteps):
            drift = -gamma * np.sin(2 * phi) - eps * np.sin(phi)
            phi = phi + drift * dt + sq * rng.standard_normal(n)
        V[i] = np.abs(np.mean(np.exp(1j * phi)))
        d0 = np.minimum(np.abs((phi) % (2*np.pi)), np.abs((phi) % (2*np.pi) - 2*np.pi))
        dpi = np.abs(((phi - np.pi) % (2*np.pi)) - np.pi)
        Sbin[i] = np.mean((d0 < np.pi/4) | (np.abs(dpi) < np.pi/4))
        frac_pi[i] = np.mean(np.abs(dpi) < np.pi/4)
    return V, Sbin, frac_pi


def phase_samples(sigma2, gamma, eps=0.0, n=40000, T=1.0, dt=2e-3, phi0=0.0, seed=1):
    """Return the final-phi ensemble at a single sigma^2 (for the P(phi) histogram)."""
    rng = np.random.default_rng(seed)
    nsteps = int(round(T / dt))
    D = sigma2 / (2.0 * T)
    sq = np.sqrt(2.0 * D * dt)
    phi = np.full(n, phi0, dtype=float)
    for _ in range(nsteps):
        drift = -gamma * np.sin(2 * phi) - eps * np.sin(phi)
        phi = phi + drift * dt + sq * rng.standard_normal(n)
    return (phi + np.pi) % (2 * np.pi) - np.pi      # wrap to (-pi, pi]


# =============================================================================
# PART 2/3  --  compare the noise-blur laws
# =============================================================================
def main():
    geo = silver_geometry()

    sigma2 = np.linspace(0.0, 8.0, 33)            # injected phase variance (the noise knob)

    print("\n" + "=" * 74)
    print("PART 2  --  STANDARD QM noise blur (Gaussian dephasing)")
    print("=" * 74)
    V_qm_analytic = np.exp(-sigma2 / 2.0)
    V_qm_sim, _, _ = langevin_visibility(sigma2, gamma=0.0, seed=10)
    err = np.max(np.abs(V_qm_sim - V_qm_analytic))
    print(f"  V_QM = exp(-sigma^2/2);  Langevin(gamma=0) reproduces it, max|err|={err:.3f}")
    print(f"  half-visibility at sigma^2 = {2*np.log(2):.2f}  (V=0.5)")

    print("\n" + "=" * 74)
    print("PART 3  --  TWO-BASIN noise blur (attractor strength gamma; eps=0)")
    print("=" * 74)
    gammas = [0.5, 2.0, 8.0]
    V_2b = {}
    Sbin_2b = {}
    for g in gammas:
        V, S, fpi = langevin_visibility(sigma2, gamma=g, eps=0.0, seed=20 + int(10*g))
        V_2b[g] = V
        Sbin_2b[g] = S
        plateau = np.exp(-sigma2 / (8 * g))       # analytic in-well prediction
        # cliff = where V has fallen below 0.5 of its low-noise plateau
        cliff_idx = np.argmax(V < 0.5 * V[1]) if np.any(V < 0.5 * V[1]) else -1
        cliff = sigma2[cliff_idx] if cliff_idx > 0 else np.nan
        print(f"  gamma={g:4.1f}:  in-well plateau V~exp(-s2/{8*g:.0f});  "
              f"predicted cliff s2~2*gamma={2*g:.1f};  measured half-drop at s2~{cliff:.1f}")
    print("  => attractor PROTECTS the fringe for weak noise (variance capped at D/2gamma),")
    print("     then a Kramers CLIFF near s2~2*gamma flips trajectories to the pi well.")
    print("     QM has NO plateau: it decays from s2=0.  This is the falsifiable difference")
    print("     -- *if* gamma reaches the propagating phase.  Strict MCI (gamma=0 in flight)")
    print("     gives V_2b == V_QM exactly: the fringe channel alone cannot distinguish them.")

    # biased case (eps>0): one well favored -> partial fringe survives, Boltzmann tilt
    Vb_bias, _, _ = langevin_visibility(sigma2, gamma=2.0, eps=0.8, seed=99)

    print("\n" + "=" * 74)
    print("PART 4  --  the COMBINED-DESIGN discriminator (Stern-Gerlach spin channel)")
    print("=" * 74)
    print("  As noise blurs the SPATIAL fringe, what happens in the correlated spin channel?")
    print("  'binary sharpness' S = fraction of atoms within pi/4 of a pointer (0 or pi):")
    s2_probe = [1.0, 2.0, 4.0]
    for s2p in s2_probe:
        j = np.argmin(np.abs(sigma2 - s2p))
        # QM sharpness: phase is a spread wrapped-Gaussian; fraction near 0 or pi
        ph_qm = phase_samples(sigma2[j], gamma=0.0, seed=3)
        d0 = np.abs(ph_qm); dpi = np.abs(np.abs(ph_qm) - np.pi)
        S_qm = np.mean((d0 < np.pi/4) | (dpi < np.pi/4))
        print(f"  sigma^2={sigma2[j]:.2f}:  V_QM={V_qm_analytic[j]:.2f}  S_QM={S_qm:.2f}   |   "
              f"V_2b(g=8)={V_2b[8.0][j]:.2f}  S_2b={Sbin_2b[8.0][j]:.2f}")
    print("  QM: as V falls, S falls too (phase just spreads out -- no structure).")
    print("  TWO-BASIN: as V falls, S stays HIGH -- every atom is still in SOME pointer;")
    print("  the lost spatial fringe re-appears as a SHARP BINARY in the SG readout.")
    print("  => the silver+SG correlation (fringe loss WITH spin-binary sharpening) is the")
    print("     signature a bare interferometer cannot see; it survives even if gamma=0 in")
    print("     flight, because the Stage-2 lock acts at the detector.")

    # ---- figure --------------------------------------------------------------
    make_figure(sigma2, V_qm_analytic, V_2b, Vb_bias, Sbin_2b, gammas)


def make_figure(sigma2, V_qm, V_2b, Vb_bias, Sbin_2b, gammas):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as e:
        print(f"\n[figure skipped: {e}]")
        return

    fig, ax = plt.subplots(2, 2, figsize=(12, 9))

    # (0,0) the headline: visibility vs noise
    a = ax[0, 0]
    a.plot(sigma2, V_qm, "k-", lw=2.5, label="standard QM  $e^{-\\sigma^2/2}$")
    colors = ["C0", "C1", "C2"]
    for g, c in zip(gammas, colors):
        a.plot(sigma2, V_2b[g], c, lw=2, marker="o", ms=3,
               label=f"two-basin $\\gamma={g}$")
        a.plot(sigma2, np.exp(-sigma2 / (8 * g)), c, lw=1, ls=":")  # analytic plateau
    a.plot(sigma2, Vb_bias, "C3--", lw=1.6, label="two-basin $\\gamma=2,\\ \\epsilon=0.8$ (biased)")
    a.set_xlabel(r"injected phase-noise variance  $\sigma^2 = 2DT$")
    a.set_ylabel(r"fringe visibility  $V=|\langle e^{i\phi}\rangle|$")
    a.set_title("Noise blur: QM (immediate exp) vs two-basin (plateau-then-cliff)")
    a.set_ylim(-0.02, 1.02)
    a.legend(fontsize=8)
    a.grid(alpha=0.25)

    # (0,1) phase distributions at a matched noise PAST the cliff (so the binary shows)
    a = ax[0, 1]
    s2p = 6.0                       # past the gamma=2 cliff (2*gamma=4): both wells populated
    bins = np.linspace(-np.pi, np.pi, 80)
    ph_qm = phase_samples(s2p, gamma=0.0, seed=5)
    ph_2b = phase_samples(s2p, gamma=2.0, seed=6)
    a.hist(ph_qm, bins=bins, density=True, alpha=0.55, color="k",
           label="QM (unimodal $\\to$ near-uniform)")
    a.hist(ph_2b, bins=bins, density=True, alpha=0.6, color="C2",
           label="two-basin $\\gamma=2$ (bimodal 0/$\\pi$ pointers)")
    a.axvline(0, color="g", lw=0.8); a.axvline(np.pi, color="g", lw=0.8); a.axvline(-np.pi, color="g", lw=0.8)
    a.set_xlabel(r"relative phase $\phi$ (rad)")
    a.set_ylabel("probability density")
    a.set_title(f"Phase distribution at matched $\\sigma^2={s2p:.0f}$ (the smoking gun)")
    a.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    a.set_xticklabels([r"$-\pi$", r"$-\pi/2$", "0", r"$\pi/2$", r"$\pi$"])
    a.legend(fontsize=8)

    # (1,0) the combined-design discriminator: spin-channel sharpness vs noise
    a = ax[1, 0]
    # QM sharpness curve
    S_qm = []
    for s2 in sigma2:
        ph = phase_samples(s2, gamma=0.0, n=8000, seed=7)
        d0 = np.abs(ph); dpi = np.abs(np.abs(ph) - np.pi)
        S_qm.append(np.mean((d0 < np.pi/4) | (dpi < np.pi/4)))
    a.plot(sigma2, V_qm, "k-", lw=1.5, alpha=0.5, label="QM visibility (falls)")
    a.plot(sigma2, S_qm, "k--", lw=2, label="QM spin-binary sharpness (falls too)")
    a.plot(sigma2, V_2b[8.0], "C2-", lw=1.5, alpha=0.5, label="two-basin visibility (falls)")
    a.plot(sigma2, Sbin_2b[8.0], "C2--", lw=2, label="two-basin spin sharpness (STAYS HIGH)")
    a.set_xlabel(r"injected phase-noise variance $\sigma^2$")
    a.set_ylabel("visibility  /  spin-binary sharpness")
    a.set_title("SG discriminator: does lost fringe re-appear as a sharp binary?")
    a.set_ylim(-0.02, 1.02)
    a.legend(fontsize=8)
    a.grid(alpha=0.25)

    # (1,1) strength-of-attractor map: cliff position scales with gamma
    a = ax[1, 1]
    g_grid = np.linspace(0.25, 10, 28)
    s2_grid = np.linspace(0.05, 8, 30)
    Z = np.empty((len(g_grid), len(s2_grid)))
    for ig, g in enumerate(g_grid):
        Vg, _, _ = langevin_visibility(s2_grid, gamma=g, eps=0.0, n=3000, seed=200 + ig)
        Z[ig] = Vg
    im = a.pcolormesh(s2_grid, g_grid, Z, shading="auto", cmap="viridis", vmin=0, vmax=1)
    a.plot(2 * g_grid, g_grid, "w--", lw=2, label=r"Kramers cliff $\sigma^2\approx2\gamma$")
    a.set_xlabel(r"injected phase-noise variance $\sigma^2$")
    a.set_ylabel(r"attractor strength $\gamma$")
    a.set_title("Strength-of-attractor: fringe survives until $\\sigma^2\\sim2\\gamma$")
    a.set_xlim(0, 8)
    a.legend(fontsize=8, loc="lower right")
    fig.colorbar(im, ax=a, label="visibility V")

    fig.tight_layout()
    out = __file__.rsplit("/", 1)[0] + "/silver_twoslit_noise.png"
    fig.savefig(out, dpi=130)
    print(f"\n[figure written: {out}]")


if __name__ == "__main__":
    main()
