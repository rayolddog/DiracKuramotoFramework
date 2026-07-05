#!/usr/bin/env python3
"""
dispute-001-basin-measure.py
============================
Commissioned calculation for the bounded resolution loop on Dispute 001:

    "Can the Adler/Kuramoto synchronization dynamics reproduce Born weights
     |alpha|^2, or does it predict the wrong (basin-area / equal) statistics?"

Both Fable 5 (Reviewer A, Major Concern #2) and GPT-5.5 (Reviewer C, Q3) state
the dispute is settleable by computing the basin measure of the simplest
two-outcome Adler model. This script does exactly that. The result is
lab-independent: it is arithmetic, not opinion.

Model (the minimal two-outcome pointer dynamics used in the manuscript's own
RESULTS_PHASE_DISSIPATIVE: the measured-channel dissipator D[sigma_x] reduces to
a SECOND-harmonic Adler equation that is bistable at the two pointer phases 0 and pi):

    dphi/dt = Omega - gamma * sin(2 phi)

  - gamma  : measurement/locking strength (sets the double well V = -1/2 cos 2phi)
  - Omega  : residual precession in the measured plane (an APPARATUS property)
  - stable fixed points at phi ~ 0 and phi ~ pi for |Omega| < gamma  -> two basins

The prepared amplitude alpha of the system state |psi> = alpha|+x> + beta|-x>
DOES NOT APPEAR in this equation. That absence is the whole question.

No third-party dependencies beyond numpy (+ optional matplotlib).
"""

import numpy as np

GAMMA = 1.0


def drift(phi, omega):
    return omega - GAMMA * np.sin(2.0 * phi)


def basin_fraction(omega, n_phi0=2000, T=40.0, dt=2e-3):
    """Fraction of UNIFORMLY-sampled initial phases landing in basin 0.

    Vectorized RK4: all n_phi0 trajectories are integrated simultaneously.
    basin 0 = locked near phi = 0 (pointer '+x'); basin 1 = near phi = pi.
    """
    # uniform initial-phase measure; nudge off the unstable separatrix
    phi = np.linspace(0.0, 2 * np.pi, n_phi0, endpoint=False) + 1e-6
    n = int(T / dt)
    for _ in range(n):
        k1 = drift(phi, omega)
        k2 = drift(phi + 0.5 * dt * k1, omega)
        k3 = drift(phi + 0.5 * dt * k2, omega)
        k4 = drift(phi + dt * k3, omega)
        phi = phi + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    # fold to (-pi, pi]; basin 0 if nearer 0 than pi
    phi = (phi + np.pi) % (2 * np.pi) - np.pi
    return float(np.mean(np.abs(phi) < np.pi / 2))


def basin_fraction_biased(eps, omega=0.0, phi_bulk=0.0, n_phi0=2000, T=40.0, dt=2e-3):
    """Same, but with a FIRST-harmonic injection-locking bias added (the manuscript's
    Sec 2.3 term):  dphi/dt = omega - gamma sin(2 phi) - eps sin(phi - phi_bulk).
    The first harmonic breaks the 0<->pi symmetry, so basins can become unequal."""
    phi = np.linspace(0.0, 2 * np.pi, n_phi0, endpoint=False) + 1e-6
    n = int(T / dt)

    def f(p):
        return omega - GAMMA * np.sin(2.0 * p) - eps * np.sin(p - phi_bulk)

    for _ in range(n):
        k1 = f(phi)
        k2 = f(phi + 0.5 * dt * k1)
        k3 = f(phi + 0.5 * dt * k2)
        k4 = f(phi + dt * k3)
        phi = phi + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    phi = (phi + np.pi) % (2 * np.pi) - np.pi
    return float(np.mean(np.abs(phi) < np.pi / 2))


def main():
    print("=" * 72)
    print("DISPUTE 001 — basin measure of the minimal two-outcome Adler model")
    print("    dphi/dt = Omega - gamma sin(2 phi),  gamma =", GAMMA)
    print("=" * 72)

    # ---- (A) Unbiased background, symmetric apparatus (Omega = 0) -----------
    f0 = basin_fraction(omega=0.0)
    print("\n(A) Omega = 0, uniform (unbiased) initial-phase measure:")
    print(f"    P(basin 0) = {f0:.4f}   [analytic basin areas: pi : pi = 0.5000]")
    print("    -> the locking geometry gives 50/50, by symmetry of the double well.")

    # ---- (B) Does it track the prepared weight |alpha|^2 ? ------------------
    print("\n(B) Sweep the prepared weight |alpha|^2 and compare:")
    print("    alpha^2 |  Born P=|alpha|^2 |  dynamical basin frac (Omega=0)")
    print("    --------+------------------+--------------------------------")
    alphas2 = [0.05, 0.25, 0.50, 0.75, 0.95]
    dyn = basin_fraction(omega=0.0)  # constant: alpha is NOT in the dynamics
    max_gap = 0.0
    for a2 in alphas2:
        gap = abs(dyn - a2)
        max_gap = max(max_gap, gap)
        print(f"     {a2:4.2f}   |      {a2:5.3f}       |        {dyn:5.3f}   (|gap|={gap:4.2f})")
    print(f"    -> dynamical fraction is FLAT at {dyn:.3f} regardless of alpha;")
    print(f"       it matches Born only at |alpha|^2 = 0.5. Max disagreement = {max_gap:.2f}.")

    # ---- (C) Residual precession Omega does NOT even move the split ---------
    print("\n(C) Vary residual precession Omega/gamma (second harmonic only):")
    print("    Omega/gamma |  P(basin 0)")
    print("    ------------+------------")
    for og in [-0.8, -0.4, 0.0, 0.4, 0.8]:
        print(f"      {og:+4.1f}     |   {basin_fraction(omega=og*GAMMA):5.3f}")
    print("    -> still 0.500 for every Omega: in the pure second-harmonic model both")
    print("       wells AND both barriers shift together, so basins stay equal-width")
    print("       (pi:pi). Apparatus detuning does not even break 50/50 here.")

    # ---- (D) Only a FIRST-harmonic bias breaks 50/50 — and it tracks eps ----
    print("\n(D) Add the Sec-2.3 first-harmonic bias eps*sin(phi - Phi_bulk):")
    print("    eps  |  P(basin 0)")
    print("    -----+------------")
    for eps in [0.0, 0.2, 0.4, 0.6]:
        print(f"    {eps:4.2f} |   {basin_fraction_biased(eps):5.3f}")
    print("    -> NOW the split moves off 0.5 — but it tracks eps and Phi_bulk (the")
    print("       BULK REFERENCE / apparatus bias), still with no dependence on alpha.")

    # ---- (E) Verdict logic --------------------------------------------------
    print("\n" + "=" * 72)
    print("VERDICT (lab-independent):")
    print("  * The synchronization dynamics do NOT DERIVE Born: |alpha|^2 never")
    print("    enters dphi/dt. The bare (second-harmonic) geometry gives 50/50,")
    print("    robustly — even apparatus detuning Omega does not move it.")
    print("  * The only knob that breaks 50/50 (the first-harmonic bias eps toward")
    print("    Phi_bulk) is an APPARATUS/REFERENCE property, not the prepared alpha.")
    print("  * They also do not PREDICT a fixed wrong number observably: the outcome")
    print("    weight is whatever measure you place on the initial phase / background.")
    print("    Set that measure = Born and you recover |alpha|^2 — by hand (Horn 2).")
    print("  * No deterministic relaxation to |alpha|^2 exists here (uniform measure")
    print("    -> a fixed number), so the sub-quantum H-theorem route is unsupported")
    print("    in this model (corroborates Reviewer B/C concern #4).")
    print("=" * 72)

    # ---- optional figure ----------------------------------------------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        xs = np.linspace(0, 1, 200)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(xs, xs, "k--", lw=2, label="Born  P = |α|²")
        ax.axhline(0.5, color="C3", lw=2.5, label="Adler dynamics (Ω=0): flat 0.5")
        ax.scatter(alphas2, [dyn] * len(alphas2), color="C3", zorder=5)
        ax.scatter([0.5], [0.5], s=120, facecolors="none", edgecolors="k",
                   zorder=6, label="only point they agree")
        ax.set_xlabel("prepared weight  |α|²")
        ax.set_ylabel("P(outcome '+x')")
        ax.set_title("Dispute 001: basin measure vs Born\nminimal two-outcome Adler model")
        ax.legend(loc="upper left", fontsize=9)
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        fig.tight_layout()
        out = "dispute-001-basin-measure.png"
        fig.savefig(out, dpi=130)
        print(f"\n[figure written: {out}]")
    except Exception as e:  # noqa
        print(f"\n[figure skipped: {e}]")


if __name__ == "__main__":
    main()
