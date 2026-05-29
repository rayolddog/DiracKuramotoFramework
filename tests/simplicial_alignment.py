"""
simplicial_alignment.py

Verification that the chiral-pair Kuramoto *model* (K = m) embeds as the
manifold-like simple simplicial Kuramoto model on a 1-simplex.

SCOPE: this test compares two *Kuramoto formulations* and shows they are
equivalent on the 2-node, 1-edge complex. It does NOT show that the closed
Dirac equation reduces to a Kuramoto attractor -- it does not. The Madelung
reduction of the closed chiral Dirac equation gives cosine-in-phase /
sine-in-amplitude with no attractor on rho_L = rho_R (see PAPER_UNIFIED.md
sec 2.2 and Appendix F). The sine-coupled Kuramoto/Adler form with K = m as a
coupling is the framework's *measurement* (open-system) dynamics
(EQUATIONS.md sec 2); the intra-spinor K = m is otherwise the unitary
off-diagonal coupling that sets the normal modes and the dispersion relation.

Tests the alignment between:
  (A) The chiral-pair Kuramoto model used in the framework's measurement
      dynamics (EQUATIONS.md sec 2; PAPER_UNIFIED.md sec 3.4), with K = m.
  (B) Theorem 1 of Nurisso et al. (2024, arXiv:2305.17977), which states
      that the simple simplicial Kuramoto model on a manifold-like
      simplicial complex reduces to the standard node Kuramoto on the
      dual 1-skeleton.

The test: build a 2-node simplicial complex (nodes = chiral sectors L, R;
single edge = mass coupling). Integrate two systems from the same initial
condition:
  (A) The chiral-pair Kuramoto model (sine/Adler form, EQUATIONS.md sec 2).
  (B) The simplicial Kuramoto in Nurisso et al.'s incidence-matrix form
      (their Eq. 13/15, for k=0, i.e. node Kuramoto in matrix form).
Verify they produce identical trajectories within numerical tolerance.

Also tests:
  - Harmonic gauge invariance (Nurisso sec III.E = U(1) of PAPER sec 1.5)
  - Synchronization timescale tau_sync = 1/K (EQUATIONS sec 2)

Reference:
  Nurisso, M., Arnaudon, A., Lucas, M., Peach, R.L., Expert, P.,
  Vaccarino, F., Petri, G. "A unified framework for Simplicial Kuramoto
  models." Chaos 34, 053118 (2024). arXiv:2305.17977.

Author: J. Bramble (with Claude Opus 4.7, Anthropic)
"""

import numpy as np
from scipy.integrate import solve_ivp


# ===========================================================================
#  Section 1: The chiral L-R Kuramoto (the framework's form)
# ===========================================================================

def chiral_lr_kuramoto(t, phi, omega, K, delta_CP=0.0):
    """
    The chiral-pair Kuramoto model (the open-system / measurement-level
    Adler form, EQUATIONS.md sec 2):

        dphi_L/dt = omega + K sin(phi_R - phi_L + delta_CP)
        dphi_R/dt = omega + K sin(phi_L - phi_R - delta_CP)

    with coupling K = m. NOTE: this is the dissipative Kuramoto/Adler form,
    not the closed-system Madelung reduction of the Dirac equation -- the
    latter gives cosine-in-phase with no attractor (PAPER_UNIFIED.md sec 2.2,
    Appendix F). This function exists to check equivalence with the simplicial
    Kuramoto form below, not to assert a closed-Dirac reduction.
    """
    phi_L, phi_R = phi
    dphi_L = omega + K * np.sin(phi_R - phi_L + delta_CP)
    dphi_R = omega + K * np.sin(phi_L - phi_R - delta_CP)
    return np.array([dphi_L, dphi_R])


# ===========================================================================
#  Section 2: The simplicial Kuramoto on a 2-node, 1-edge complex
# ===========================================================================
#
# Following Nurisso et al. (2024), section III.A:
#
# A simplicial complex Delta with N_0 nodes and N_1 edges has incidence
# matrix B_1 of shape (N_0, N_1) defined by:
#     B_1[i, j] = +1   if edge j is coherently oriented with node i
#                      (i.e. node i is the head of edge j)
#     B_1[i, j] = -1   if edge j is incoherently oriented with node i
#                      (i.e. node i is the tail of edge j)
#     B_1[i, j] =  0   otherwise
#
# The node Kuramoto in matrix form is (their Eq. 15, sigma -> K):
#
#     dtheta/dt = omega - K * B_1 @ sin(D_0 @ theta)
#
# where D_0 = B_1.T is the coboundary operator (the discrete gradient).
#
# For our 2-node, 1-edge case:
#   nodes = {[L], [R]}, edge = [L->R] oriented from L to R
#   B_1 = [[-1], [+1]]    (L is tail, R is head)
#   D_0 = B_1.T = [[-1, +1]]

B1 = np.array([[-1.0], [+1.0]])   # 2 nodes x 1 edge
D0 = B1.T                          # 1 edge x 2 nodes


def simplicial_node_kuramoto(t, theta, omega_vec, K, B1, D0):
    """
    Node Kuramoto in Nurisso et al.'s incidence-matrix form (their Eq. 15):

        dtheta/dt = omega - K * B_1 @ sin(D_0 @ theta)

    For a manifold-like complex, their Theorem 1 guarantees this equals the
    standard pairwise node Kuramoto. For our 2-node case it should be
    exactly the chiral L-R dynamics with delta_CP = 0.
    """
    return omega_vec - K * (B1 @ np.sin(D0 @ theta))


# ===========================================================================
#  Section 3: Trajectory equivalence test
# ===========================================================================

def run_alignment_test(omega=1.0, K=0.5, delta_CP=0.0,
                       phi0=(0.3, -0.7), t_max=20.0, n_points=2000,
                       tol=1e-9):
    t_eval = np.linspace(0.0, t_max, n_points)
    omega_vec = np.array([omega, omega])
    phi0 = np.array(phi0)

    sol_fw = solve_ivp(chiral_lr_kuramoto, (0.0, t_max), phi0, t_eval=t_eval,
                       args=(omega, K, delta_CP), method='RK45',
                       rtol=1e-12, atol=1e-12)
    sol_sp = solve_ivp(simplicial_node_kuramoto, (0.0, t_max), phi0,
                       t_eval=t_eval, args=(omega_vec, K, B1, D0),
                       method='RK45', rtol=1e-12, atol=1e-12)

    residual = np.abs(sol_fw.y - sol_sp.y)
    return {
        't': sol_fw.t,
        'phi_framework': sol_fw.y,
        'theta_simplicial': sol_sp.y,
        'max_residual': residual.max(),
        'passes': residual.max() < tol,
    }


# ===========================================================================
#  Section 4: Hodge gauge mode test
# ===========================================================================
#
# Nurisso et al. sec III.E: "the harmonic space is the gauge of the
# simplicial Kuramoto. ... the addition of a harmonic cochain x in ker L^k
# to the phases has no effect on the dynamics."
#
# For a connected 2-node graph, ker L^0 = span{[1, 1]^T} -- the constant-
# phase mode. This is exactly the framework's U(1) gauge invariance
# (PAPER_UNIFIED.md sec 1.5, item 6): only the difference phi_L - phi_R
# enters the sine coupling.

def hodge_gauge_test(omega=1.0, K=0.5, phi0=(0.3, -0.7),
                     alpha_list=(0.0, 0.5, 1.7, np.pi, 5.21), t_max=10.0):
    t_eval = np.linspace(0.0, t_max, 500)
    omega_vec = np.array([omega, omega])

    diff_trajectories = []
    for alpha in alpha_list:
        phi0_shifted = np.array(phi0) + alpha
        sol = solve_ivp(simplicial_node_kuramoto, (0.0, t_max), phi0_shifted,
                        t_eval=t_eval, args=(omega_vec, K, B1, D0),
                        method='RK45', rtol=1e-12, atol=1e-12)
        diff_trajectories.append(sol.y[0] - sol.y[1])

    diff_arr = np.array(diff_trajectories)
    max_deviation = np.max(np.abs(diff_arr - diff_arr[0]))
    return {
        'alpha_list': alpha_list,
        'max_deviation': max_deviation,
        'gauge_invariant': max_deviation < 1e-10,
    }


# ===========================================================================
#  Section 5: Synchronization timescale tau_sync = 1/(2K) for two clocks
# ===========================================================================
#
# EQUATIONS.md sec 2 gives the single-clock-to-bulk rate: tau_sync = 1/K
# (one oscillator driven toward a fixed bulk phase decays at rate K).
#
# For the two-clock case relevant here, both clocks move toward each other,
# so the relative phase d = phi_L - phi_R linearizes near zero as:
#     dd/dt = -2K sin(d) ~ -2K d
# giving tau_sync_rel = 1/(2K). With K = m in natural units this is
# hbar/(2 m c^2) -- half the inverse Compton frequency.
#
# Initial condition is chosen well away from the unstable fixed point at
# d = pi (where sin(d) = 0 traps the dynamics).

def sync_timescale_test(omega=1.0, K_values=(0.1, 0.5, 1.0, 2.0),
                        phi0=(0.05, -0.05)):
    """Two-clock relative-phase decay: predicted tau = 1/(2K).

    Initial condition kept small (|phi_L - phi_R| = 0.1 rad) so sin(d) ~ d
    holds and the linearized prediction is accurate. Larger initial offsets
    incur a 2*log[tan(d0/2)/tan(d0/(2e))] / (2K) correction from the
    nonlinear sine; check the analytical solution
    d(t) = 2 arctan[tan(d0/2) exp(-2Kt)] if you change phi0.
    """
    omega_vec = np.array([omega, omega])
    results = []
    for K in K_values:
        # Scale integration window with 1/K so we always span ~10 timescales.
        t_max = 20.0 / K
        t_eval = np.linspace(0.0, t_max, 10000)
        sol = solve_ivp(simplicial_node_kuramoto, (0.0, t_max), np.array(phi0),
                        t_eval=t_eval, args=(omega_vec, K, B1, D0),
                        method='RK45', rtol=1e-12, atol=1e-12)
        diff = sol.y[0] - sol.y[1]
        initial_diff = abs(diff[0])
        target = initial_diff / np.e
        mask = np.abs(diff) <= target
        tau_measured = t_eval[np.argmax(mask)] if np.any(mask) else np.nan
        tau_predicted = 1.0 / (2.0 * K)
        results.append({
            'K': K,
            'tau_measured': tau_measured,
            'tau_predicted': tau_predicted,
            'ratio': (tau_measured / tau_predicted
                      if tau_predicted > 0 else np.nan),
        })
    return results


# ===========================================================================
#  Main
# ===========================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("Simplicial Alignment Test: K = m on a 1-simplex (manifold-like)")
    print("DiracKuramotoFramework <-> Nurisso et al. (Chaos 2024)")
    print("=" * 72)

    print("\n[Test 1] Trajectory equivalence (delta_CP = 0)")
    print("-" * 72)
    r = run_alignment_test()
    print(f"  Max |phi_framework - theta_simplicial| = {r['max_residual']:.2e}")
    print(f"  Equivalence verified (tol = 1e-9):     {r['passes']}")

    print("\n[Test 2] Harmonic gauge mode (Nurisso III.E = U(1) of PAPER 1.5)")
    print("-" * 72)
    g = hodge_gauge_test()
    print(f"  Max deviation of (phi_L - phi_R) across gauge shifts: "
          f"{g['max_deviation']:.2e}")
    print(f"  Gauge invariance verified: {g['gauge_invariant']}")

    print("\n[Test 3] Sync timescale tau_sync = 1/K (EQUATIONS sec 2)")
    print("-" * 72)
    print(f"  {'K':>8s}  {'tau_predicted':>16s}  "
          f"{'tau_measured':>16s}  {'ratio':>10s}")
    for s in sync_timescale_test():
        print(f"  {s['K']:>8.2f}  {s['tau_predicted']:>16.4f}  "
              f"{s['tau_measured']:>16.4f}  {s['ratio']:>10.4f}")

    print("\n" + "=" * 72)
    print("Summary")
    print("=" * 72)
    print("  The chiral-pair Kuramoto model (K = m) embeds as the")
    print("  manifold-like simple simplicial Kuramoto model on a 1-simplex;")
    print("  K = m is the edge coupling of this 1-simplex, and the U(1) gauge")
    print("  invariance is the harmonic phase-shift symmetry of Nurisso et al.")
    print("  Theorem 1. (Equivalence of two Kuramoto forms -- NOT a reduction")
    print("  of the closed Dirac equation; see PAPER sec 2.2 / Appendix F.)")
    print("=" * 72)
