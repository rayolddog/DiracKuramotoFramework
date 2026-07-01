#!/usr/bin/env python3
r"""
phi_dissipative_check.py
========================

Question (DISCRETIZATION_AS_SYNC_PAPER.md, new Sec 3.2 paragraph):
    Does a second-harmonic term  sin(2 phi)  survive the *dissipative* reduction
    of the chiral mass coupling, and does it stabilize BOTH phi=0 and phi=pi
    (a genuine binary), rather than only the single-basin sin(phi) Adler term?

Model
-----
The chiral pair (psi_L, psi_R) is one qubit.  Pauli basis: the {|L>,|R>}
(z) basis.  Density matrix rho = 1/2 (I + r . sigma), Bloch vector r=(x,y,z).

    x = <sigma_x> = 2 Re(psi_L^* psi_R)   (the L<->R interference / mass channel)
    y = <sigma_y> = 2 Im(psi_L^* psi_R)
    z = <sigma_z> = |psi_L|^2 - |psi_R|^2

The RELATIVE PHASE is the equatorial azimuth  phi = atan2(y, x):
    phi = 0   -> in-phase   |L>+|R>   (+x pointer)
    phi = pi  -> anti-phase |L>-|R>   (-x pointer)

phi -> phi+pi is rotation by pi about z, i.e. sigma_x -> -sigma_x, sigma_y -> -sigma_y.
A phase potential V(phi) is period-pi (bistable 0/pi candidate) iff the dynamics
is EVEN under that flip.

Closed Hamiltonian (BUILD 3 / mass_shell.py):  H = -p sigma_z + m sigma_x.
As an effective Bloch field  H = 1/2 omega . sigma  with omega = (2m, 0, -2p);
commutator gives precession  r_dot = omega x r  (NO attractor -- Sec 2.2).

Three dissipators are compared (rate gamma), each in Lindblad form
    D[L] rho = L rho L^dagger - 1/2 {L^dagger L, rho}:

  (A) measure_sx :  L = sqrt(gamma) sigma_x
        = continuous measurement of the MASS / interference channel.
        Quadratic in sigma_x  ->  EVEN under phi->phi+pi.
  (B) dipole_x   :  amplitude damping toward the single pointer |+x>
        = POLAR relaxation toward a fixed axis (the Sec 3.2 "T1 toward B0" case).
        Linear/odd  ->  monostable.
  (C) measure_sz :  L = sqrt(gamma) sigma_z
        = dephasing in the L/R basis (a control: kills phi, no locking).

Output: prints fixed points + harmonic content of dphi/dt for each model,
runs quantum trajectories for (A), maps the locking (Arnold) tongue of the
second-harmonic Adler equation, and writes phi_dissipative_check.png.
"""

import numpy as np

# ---- Pauli matrices ----------------------------------------------------------
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


# ---- Bloch right-hand sides for each model -----------------------------------
def rdot_hamiltonian(r, m=0.0, p=0.0):
    """Closed precession r_dot = omega x r, omega=(2m,0,-2p)."""
    omega = np.array([2 * m, 0.0, -2 * p])
    return np.cross(omega, r)


def rdot_measure_sx(r, g):
    """D[sqrt(g) sigma_x] on the Bloch vector:  (0, -2g y, -2g z)."""
    x, y, z = r
    return np.array([0.0, -2 * g * y, -2 * g * z])


def rdot_measure_sz(r, g):
    """D[sqrt(g) sigma_z]:  (-2g x, -2g y, 0)  (dephasing in L/R basis)."""
    x, y, z = r
    return np.array([-2 * g * x, -2 * g * y, 0.0])


def rdot_dipole_x(r, G):
    """Amplitude damping toward |+x> (polar T1 toward a fixed axis).
    Longitudinal axis = x: x -> +1; transverse y,z damp at G/2."""
    x, y, z = r
    return np.array([G * (1 - x), -0.5 * G * y, -0.5 * G * z])


# ---- Phase flow on the equator (|r|=1, z=0) ----------------------------------
def phase_flow(rdot_func, phi, **kw):
    """dphi/dt for a Bloch RHS evaluated on the unit equatorial circle."""
    x, y = np.cos(phi), np.sin(phi)
    r = np.array([x, y, 0.0])
    rd = rdot_func(r, **kw)
    xd, yd = rd[0], rd[1]
    return (x * yd - y * xd)  # (x ydot - y xdot)/(x^2+y^2), denom=1


def harmonic_content(flow_vals, phi):
    """Return |sin(phi)| (n=1) and |sin(2phi)| (n=2) Fourier amplitudes of dphi/dt."""
    N = len(phi)
    a1 = (2.0 / N) * np.sum(flow_vals * np.sin(phi))
    a2 = (2.0 / N) * np.sum(flow_vals * np.sin(2 * phi))
    c1 = (2.0 / N) * np.sum(flow_vals * np.cos(phi))
    c2 = (2.0 / N) * np.sum(flow_vals * np.cos(2 * phi))
    return dict(sin1=a1, sin2=a2, cos1=c1, cos2=c2)


def fixed_points(flow_vals, phi):
    """Find zeros of dphi/dt and classify stability by the sign of the slope."""
    f = flow_vals
    fps = []
    for i in range(len(phi)):
        j = (i + 1) % len(phi)
        if f[i] == 0 or (f[i] < 0) != (f[j] < 0):  # sign change i->j
            # linear interp location
            denom = (f[j] - f[i])
            frac = 0.0 if denom == 0 else -f[i] / denom
            phi_star = phi[i] + frac * (phi[j] - phi[i])
            slope = denom / (phi[j] - phi[i])
            stable = slope < 0  # dphi/dt decreasing through zero -> attractor
            fps.append((phi_star % (2 * np.pi), stable))
    # dedupe near-identical
    out = []
    for ph, st in sorted(fps):
        if not any(abs(((ph - q) + np.pi) % (2 * np.pi) - np.pi) < 1e-3 for q, _ in out):
            out.append((ph, st))
    return out


# ---- Part A/B/C: phase-flow analysis of the three dissipators -----------------
def analyze_models():
    phi = np.linspace(0, 2 * np.pi, 2001, endpoint=False)
    print("=" * 74)
    print("PHASE FLOW  dphi/dt  ON THE EQUATOR  (H = 0; pure dissipator, rate=1)")
    print("=" * 74)
    results = {}
    for name, func, kw in [
        ("measure_sx (mass channel, L=sigma_x)", rdot_measure_sx, dict(g=1.0)),
        ("dipole_x   (polar T1 toward +x)      ", rdot_dipole_x, dict(G=1.0)),
        ("measure_sz (dephasing in L/R basis)  ", rdot_measure_sz, dict(g=1.0)),
    ]:
        flow = np.array([phase_flow(func, ph, **kw) for ph in phi])
        h = harmonic_content(flow, phi)
        fps = fixed_points(flow, phi)
        stable = [f"{np.degrees(p):6.1f} deg" for p, s in fps if s]
        unstab = [f"{np.degrees(p):6.1f} deg" for p, s in fps if not s]
        results[name] = (flow, phi, h, fps)
        print(f"\n  {name}")
        print(f"    harmonics of dphi/dt:  sin(phi)={h['sin1']:+.3f}   "
              f"sin(2phi)={h['sin2']:+.3f}")
        print(f"    STABLE fixed pts  : {stable if stable else 'none (no phase lock)'}")
        print(f"    unstable fixed pts: {unstab if unstab else 'none'}")
        if abs(h['sin2']) > 5 * (abs(h['sin1']) + 1e-9):
            verdict = "-> pure 2nd harmonic: BISTABLE candidate (0 and pi)"
        elif abs(h['sin1']) > 5 * (abs(h['sin2']) + 1e-9):
            verdict = "-> 1st harmonic dominant: MONOSTABLE"
        elif not any(s for _, s in fps):
            verdict = "-> no stable phase: pure dephasing (phase destroyed)"
        else:
            verdict = "-> mixed"
        print(f"    VERDICT: {verdict}")
    return results


# ---- Part D: second-harmonic Adler equation & locking (Arnold) tongue --------
def second_harmonic_adler():
    r"""
    With a residual precession Omega in the measured plane competing with the
    sigma_x measurement, the equatorial phase obeys
            dphi/dt = Omega - gamma sin(2 phi).
    Lock (two stable phases ~0 and ~pi) requires gamma >= |Omega|.
    """
    print("\n" + "=" * 74)
    print("SECOND-HARMONIC ADLER:   dphi/dt = Omega - gamma sin(2 phi)")
    print("  (Omega = residual precession in measured plane; gamma = measurement rate)")
    print("=" * 74)
    gamma = 1.0
    phi = np.linspace(0, 2 * np.pi, 4001, endpoint=False)
    for Omega in [0.0, 0.5, 0.9, 1.0, 1.5]:
        flow = Omega - gamma * np.sin(2 * phi)
        fps = fixed_points(flow, phi)
        nstab = sum(1 for _, s in fps if s)
        locked = nstab >= 1 and abs(Omega) <= gamma + 1e-9
        tag = (f"LOCKED: {nstab} stable basin(s)" if locked
               else "UNLOCKED: phase winds (no discrete value)")
        stab = ", ".join(f"{np.degrees(p):.0f}" for p, s in fps if s) or "-"
        print(f"  Omega/gamma={Omega/gamma:4.2f}:  {tag:38s} stable phi(deg)=[{stab}]")
    print("  => bistable binary (TWO stable phases) whenever |Omega| < gamma;")
    print("     the two basins sit symmetrically about 0 and pi.")


# ---- Part E: reconciliation with the Sec 2.3 first-harmonic Adler form -------
def reconciliation_unified():
    r"""
    Unified equatorial phase equation: the SYMMETRIC measurement of the interference
    channel (gamma, 2nd harmonic) PLUS a faint POLAR bias of the bulk reference
    (epsilon, 1st harmonic) -- the latter is exactly the Sec 2.3 K sin(Phi_bulk-phi):

        dphi/dt = Omega - gamma sin(2 phi) - epsilon sin(phi)

    Fixed points (Omega=0): sin(phi) (2 gamma cos phi + epsilon) = 0
        phi = 0   : stable for all epsilon, gamma > 0
        phi = pi  : stable IFF epsilon < 2 gamma ; else it turns into a repeller.

    So the two pictures are LIMITS of one equation:
        epsilon << gamma   -> BISTABLE binary (0 and pi); phi=0 well deeper by 2*epsilon
        epsilon  > 2 gamma -> MONOSTABLE (only phi=0) = the Sec 2.3 Adler limit.
    The framework's "faint (ppm) thermal bias" commitment puts it at epsilon << gamma,
    i.e. in the bistable regime.
    """
    print("\n" + "=" * 74)
    print("RECONCILIATION:  dphi/dt = Omega - gamma sin(2phi) - epsilon sin(phi)")
    print("  gamma = symmetric MEASUREMENT (2nd harmonic, the binary)")
    print("  epsilon = faint POLAR bias of the reference (1st harmonic = Sec 2.3 term)")
    print("=" * 74)
    gamma = 1.0
    phi = np.linspace(0, 2 * np.pi, 4001, endpoint=False)
    print("  analytic threshold: phi=pi loses stability at epsilon = 2*gamma\n")
    for eps in [0.0, 0.2, 1.0, 2.0, 3.0]:
        flow = -gamma * np.sin(2 * phi) - eps * np.sin(phi)
        fps = fixed_points(flow, phi)
        stab = ", ".join(f"{np.degrees(p):.0f}" for p, s in fps if s) or "-"
        regime = ("BISTABLE (binary)" if sum(s for _, s in fps) >= 2
                  else "MONOSTABLE  = Sec 2.3 first-harmonic limit")
        depth_gap = 2 * eps  # V(pi) - V(0) = 2 epsilon : phi=0 deeper
        print(f"  eps/gamma={eps / gamma:4.2f}:  stable phi(deg)=[{stab:8s}]  "
              f"well bias V(pi)-V(0)={depth_gap:+.2f}  -> {regime}")
    print("\n  => Sec 2.3's monostable Adler is the BIAS-DOMINATED limit (eps>2gamma);")
    print("     the bistable binary is the MEASUREMENT-DOMINATED limit (eps<<gamma).")
    print("     The faint bias breaks the 0/pi degeneracy (deepens phi=0) but this is")
    print("     a deterministic/Boltzmann tilt, NOT the Born weight |alpha|^2 (open).")


# ---- Part C: quantum trajectories under sigma_x measurement ------------------
def quantum_trajectories(n_traj=600, gamma=4.0, m=0.0, p=0.0,
                         T=4.0, dt=2e-3, seed=12345, psi0=None):
    """
    Stochastic Schrodinger eq. (quantum-state-diffusion) for continuous
    measurement of sigma_x, with closed Hamiltonian H = -p sz + m sx.
    Returns array of final phi (azimuth) per trajectory and the final <sx>.
    NOTE: this unraveling is BUILT to respect the Born rule; it therefore
    tests only the BISTABILITY (do trajectories collapse to phi=0 OR pi?),
    NOT the weights -- those remain the open Born-measure problem.
    """
    rng = np.random.default_rng(seed)
    H = -p * sz + m * sx
    nsteps = int(T / dt)
    if psi0 is None:
        psi0 = np.array([1.0, 0.0], dtype=complex)  # |L> : <sx>=0 -> 50/50
    phis = np.empty(n_traj)
    sxs = np.empty(n_traj)
    for k in range(n_traj):
        psi = psi0.astype(complex).copy()
        for _ in range(nsteps):
            ex = np.real(np.vdot(psi, sx @ psi))      # <sigma_x>
            dW = rng.normal(0.0, np.sqrt(dt))
            # Ito QSD increment for Hermitian L=sqrt(gamma) sigma_x:
            drift = (-1j * H @ psi
                     - 0.5 * gamma * (sx - ex * I2) @ ((sx - ex * I2) @ psi))
            diff = np.sqrt(gamma) * (sx - ex * I2) @ psi
            psi = psi + drift * dt + diff * dW
            psi = psi / np.linalg.norm(psi)
        x = np.real(np.vdot(psi, sx @ psi))
        y = np.real(np.vdot(psi, sy @ psi))
        phis[k] = np.arctan2(y, x) % (2 * np.pi)
        sxs[k] = x
    return phis, sxs


def main():
    results = analyze_models()
    second_harmonic_adler()
    reconciliation_unified()

    print("\n" + "=" * 74)
    print("QUANTUM TRAJECTORIES: continuous measurement of sigma_x (mass channel)")
    print("  start |L> (equal overlap with both pointers); gamma=4, H=0")
    print("=" * 74)
    phis, sxs = quantum_trajectories(n_traj=600, gamma=4.0, m=0.0, p=0.0)
    near0 = np.mean(np.minimum(np.abs(phis), np.abs(phis - 2 * np.pi)) < np.pi / 4)
    nearpi = np.mean(np.abs(phis - np.pi) < np.pi / 4)
    middle = 1 - near0 - nearpi
    print(f"  fraction ending near phi=0   (+x, in-phase) : {near0:.3f}")
    print(f"  fraction ending near phi=pi  (-x, anti-phase): {nearpi:.3f}")
    print(f"  fraction left in between (unresolved)        : {middle:.3f}")
    print(f"  mean |<sigma_x>| at end (1.0 = fully locked) : {np.mean(np.abs(sxs)):.3f}")
    print("  => trajectories collapse onto the TWO pointer phases 0 and pi:")
    print("     a bistable binary. (Split ~50/50 here is the Born weight of |L>,")
    print("     assumed by the unraveling -- NOT independently derived.)")

    # Crossover with a residual precession: does bistability survive Omega?
    print("\n  Crossover check: add residual precession Omega about z (gamma=4)")
    for Om in [0.0, 2.0, 4.0, 6.0]:
        ph, sx_ = quantum_trajectories(n_traj=300, gamma=4.0, m=0.0, p=Om / 2.0,
                                       seed=7, T=4.0)
        lock = np.mean(np.abs(sx_) > 0.6)
        print(f"    Omega/gamma={Om/4.0:4.2f}:  fraction phase-locked (|<sx>|>0.6) "
              f"= {lock:.2f}")

    # ---- Figure --------------------------------------------------------------
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(2, 2, figsize=(11, 8))

        # (0,0) phase flows
        phi = np.linspace(0, 2 * np.pi, 2001, endpoint=False)
        deg = np.degrees(phi)
        ax[0, 0].axhline(0, color="0.7", lw=0.8)
        ax[0, 0].plot(deg, -np.sin(2 * phi), label=r"measure $\sigma_x$  $\propto-\sin2\phi$", lw=2)
        fdip = np.array([phase_flow(rdot_dipole_x, p_, G=1.0) for p_ in phi])
        ax[0, 0].plot(deg, fdip / np.max(np.abs(fdip)), label=r"polar T1 (dipole) $\propto-\sin\phi$", lw=2, ls="--")
        ax[0, 0].set_xlabel(r"relative phase $\phi$ (deg)")
        ax[0, 0].set_ylabel(r"$d\phi/dt$ (norm.)")
        ax[0, 0].set_title("Phase flow: bistable (solid) vs monostable (dashed)")
        ax[0, 0].set_xticks([0, 90, 180, 270, 360])
        for ph0 in (0, 180):
            ax[0, 0].axvline(ph0, color="g", lw=0.6, alpha=0.5)
        ax[0, 0].legend(fontsize=8)

        # (0,1) potentials V(phi) = -int dphi/dt
        V_meas = -0.5 * np.cos(2 * phi)        # -int(-sin2phi)=  -1/2 cos2phi
        V_dip = -np.cos(phi)
        ax[0, 1].plot(deg, V_meas - V_meas.min(), label=r"measure $\sigma_x$: $-\frac{1}{2}\cos2\phi$", lw=2)
        ax[0, 1].plot(deg, V_dip - V_dip.min(), label=r"polar T1: $-\cos\phi$", lw=2, ls="--")
        ax[0, 1].set_xlabel(r"$\phi$ (deg)")
        ax[0, 1].set_ylabel(r"effective potential $V(\phi)$")
        ax[0, 1].set_title("Double well (0 and $\\pi$) vs single well")
        ax[0, 1].set_xticks([0, 90, 180, 270, 360])
        ax[0, 1].legend(fontsize=8)

        # (1,0) trajectory histogram
        ax[1, 0].hist(np.degrees(phis), bins=60, color="C2", alpha=0.85)
        ax[1, 0].set_xlabel(r"final $\phi$ (deg)")
        ax[1, 0].set_ylabel("trajectories")
        ax[1, 0].set_title(r"600 measured-$\sigma_x$ trajectories $\to$ {0, $\pi$}")
        ax[1, 0].set_xticks([0, 90, 180, 270, 360])
        for ph0 in (0, 180):
            ax[1, 0].axvline(ph0, color="g", lw=1.0)

        # (1,1) Arnold tongue: stable-basin count vs Omega/gamma
        og = np.linspace(0, 2.0, 200)
        nst = []
        phi2 = np.linspace(0, 2 * np.pi, 4001, endpoint=False)
        for r_ in og:
            flow = r_ - np.sin(2 * phi2)  # gamma=1 units
            fps = fixed_points(flow, phi2)
            nst.append(sum(1 for _, s in fps if s))
        ax[1, 1].plot(og, nst, lw=2, color="C3")
        ax[1, 1].axvline(1.0, color="0.5", ls=":", label=r"lock threshold $|\Omega|=\gamma$")
        ax[1, 1].set_xlabel(r"$\Omega/\gamma$ (residual precession / measurement)")
        ax[1, 1].set_ylabel("number of stable phase basins")
        ax[1, 1].set_title("2nd-harmonic Adler: 2 basins while measurement wins")
        ax[1, 1].set_yticks([0, 1, 2])
        ax[1, 1].legend(fontsize=8)

        fig.tight_layout()
        out = __file__.rsplit("/", 1)[0] + "/phi_dissipative_check.png"
        fig.savefig(out, dpi=130)
        print(f"\n[figure written: {out}]")
    except Exception as e:
        print(f"\n[figure skipped: {e}]")


if __name__ == "__main__":
    main()
