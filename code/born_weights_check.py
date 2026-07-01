#!/usr/bin/env python3
r"""
born_weights_check.py
=====================

CAN the basin-selection weights be DERIVED?  i.e. does the dissipative chiral-pair
dynamics produce long-run frequencies  P(phi=0) = |<+x|psi>|^2 ,  P(phi=pi) =
|<-x|psi>|^2  (the Born weights) WITHOUT assuming them?

Setting: chiral pair = qubit, measured observable = sigma_x (the L<->R interference
/ mass channel).  Pointers |+-x> = (|L> +- |R>)/sqrt2  =  relative phase phi = 0, pi.
Initial state |psi0> = cos(tt/2)|L> + e^{i chi} sin(tt/2)|R>  (a TILTED, unequal
superposition so the two Born weights differ and the test is non-trivial).

We compute the weights three ways and compare, then locate exactly where (if
anywhere) the value |alpha|^2 enters.
"""

import numpy as np

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def bloch(psi):
    return np.array([np.real(np.vdot(psi, M @ psi)) for M in (sx, sy, sz)])


# ---- initial tilted state ----------------------------------------------------
tt = np.arcsin(0.7)          # so <sigma_x>_0 = sin(tt) = 0.7  (chi=0)
chi = 0.0
psi0 = np.array([np.cos(tt / 2), np.exp(1j * chi) * np.sin(tt / 2)], dtype=complex)
x0, y0, z0 = bloch(psi0)
aL2, aR2 = abs(psi0[0])**2, abs(psi0[1])**2

# Born weights (the target):  P(+-x) = |<+-x|psi>|^2 = (1 +- <sigma_x>)/2
P_plus_born = abs((psi0[0] + psi0[1]) / np.sqrt(2))**2
P_minus_born = abs((psi0[0] - psi0[1]) / np.sqrt(2))**2

print("=" * 74)
print("TARGET: Born weights for the two pointers (phi=0 -> +x, phi=pi -> -x)")
print("=" * 74)
print(f"  initial state: |L> coeff={psi0[0]:.3f}, |R> coeff={psi0[1]:.3f}")
print(f"  |alpha_L|^2={aL2:.3f}, |alpha_R|^2={aR2:.3f};  <sigma_x>_0={x0:.3f}")
print(f"  BORN:  P(phi=0)=|<+x|psi>|^2 = {P_plus_born:.3f}   "
      f"P(phi=pi)=|<-x|psi>|^2 = {P_minus_born:.3f}")


# ---- (1) Mean-field master equation: D[sigma_x], H=0 -------------------------
# d/dt: x_dot=0, y_dot=-2g y, z_dot=-2g z.  <sigma_x> is CONSERVED.
# Steady state rho_inf = 1/2(I + x0 sigma_x); its diagonal populations in the
# +-x basis are (1 +- x0)/2.
print("\n" + "=" * 74)
print("(1) MEAN-FIELD  (Lindblad D[sigma_x], H=0)")
print("=" * 74)
print("  <sigma_x> obeys  d<sigma_x>/dt = 0  -> EXACTLY conserved (equivariance).")
print(f"  steady-state populations (1 +- x0)/2 = {(1+x0)/2:.3f} , {(1-x0)/2:.3f}")
print("  These EQUAL the Born weights -- BUT only once we read the density-matrix")
print("  populations as outcome frequencies, which IS the Born postulate.")


# ---- (2) Quantum trajectories (stochastic, individual selections) ------------
def trajectories(psi0, gamma=6.0, T=3.0, dt=1e-3, n=4000, seed=2):
    rng = np.random.default_rng(seed)
    nsteps = int(T / dt)
    finals = np.empty(n)
    ens_mean_sx = np.zeros(nsteps + 1)   # for the martingale check
    for k in range(n):
        psi = psi0.astype(complex).copy()
        ens_mean_sx[0] += np.real(np.vdot(psi, sx @ psi))
        for i in range(nsteps):
            ex = np.real(np.vdot(psi, sx @ psi))
            dW = rng.normal(0.0, np.sqrt(dt))
            drift = -0.5 * gamma * (sx - ex * I2) @ ((sx - ex * I2) @ psi)
            diff = np.sqrt(gamma) * (sx - ex * I2) @ psi
            psi = psi + drift * dt + diff * dW
            psi = psi / np.linalg.norm(psi)
            ens_mean_sx[i + 1] += np.real(np.vdot(psi, sx @ psi))
        finals[k] = np.real(np.vdot(psi, sx @ psi))
    ens_mean_sx /= n
    return finals, ens_mean_sx


print("\n" + "=" * 74)
print("(2) QUANTUM TRAJECTORIES  (continuous sigma_x measurement, 4000 runs)")
print("=" * 74)
finals, ens = trajectories(psi0)
P_plus_traj = np.mean(finals > 0)
P_minus_traj = np.mean(finals < 0)
print(f"  empirical: P(phi=0)={P_plus_traj:.3f}   P(phi=pi)={P_minus_traj:.3f}")
print(f"  Born     : P(phi=0)={P_plus_born:.3f}   P(phi=pi)={P_minus_born:.3f}")
print(f"  MARTINGALE check: ensemble-mean <sigma_x>  t=0: {ens[0]:.3f}  "
      f"mid: {ens[len(ens)//2]:.3f}  end: {ens[-1]:.3f}  (should stay = x0)")
print("  => trajectories reproduce Born. WHY: <sigma_x> is a martingale of the")
print("     stochastic eq.; that martingale measure IS |.|^2, built into the dW")
print("     weighting sqrt(gamma)(sigma_x-<sigma_x>). Born inserted via the noise.")


# ---- (3) Deterministic basin geometry: azimuth volume = 50/50 ----------------
# Pure equatorial states, flow dphi/dt = -sin(2phi): basin boundary at +-pi/2.
print("\n" + "=" * 74)
print("(3) DETERMINISTIC BASIN GEOMETRY  (azimuth volume on the equator)")
print("=" * 74)
phi0 = np.linspace(0, 2 * np.pi, 100000, endpoint=False)
# integrate sign of attractor: basin of 0 is (-pi/2, pi/2), basin of pi is the rest
to_zero = ((phi0 < np.pi / 2) | (phi0 > 3 * np.pi / 2))
vol_zero = np.mean(to_zero)
print(f"  basin volume -> phi=0 : {vol_zero:.3f}   -> phi=pi : {1-vol_zero:.3f}")
print("  The GEOMETRIC basin measure is 50/50 and knows NOTHING about |alpha|^2.")
print("  So Born does NOT come from basin volume; it comes from the MEASURE placed")
print("  on the selecting ensemble (the noise), not from the attractor geometry.")
print("  [Confirms the MCI 'sharpest open critique': naive basin measure != Born.]")


# ---- Verdict -----------------------------------------------------------------
print("\n" + "=" * 74)
print("VERDICT")
print("=" * 74)
print(f"""  Born weights ({P_plus_born:.2f}/{P_minus_born:.2f}) are RECOVERED by the trajectory
  statistics and by the mean-field populations -- but in BOTH the value |alpha|^2
  enters as an INPUT, in three guises that are one assumption:
    (a) reading rho_inf diagonal populations as frequencies  (Born postulate);
    (b) the |.|^2 martingale / dW-weighting of the stochastic unraveling;
    (c) (equivalently) the golden-rule rate ~ |matrix element|^2.
  The purely DYNAMICAL content the framework adds is EQUIVARIANCE: <sigma_x> is
  conserved, so the |.|^2 measure granted at preparation propagates to the outcome
  (same status as Bohm's quantum-equilibrium / Valentini equivariance).
  What is NOT supplied: a TYPICALITY/relaxation argument deriving that the selecting
  ensemble carries the |.|^2 measure without inserting it. That -- not the form
  (Gleason) and not the discreteness (the binary) -- is the unsolved core.
  STATUS: NOT derived. Born-compatible, not Born-derivative. Frontier reached, not
  crossed.""")
