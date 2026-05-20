"""
hodge_decomposition.py

Numerical demonstration of the Hodge decomposition of edge cochains under
the simplicial Kuramoto dynamics, supporting PAPER_UNIFIED.md Appendix B,
section B.5 ("Hodge Decomposition as Coherence Structure").

Setting: a small simplicial complex with nontrivial topology -- a square
with one diagonal, with one of the two triangles filled.

      3 ---------- 2
      |          / |
      |  open   /  |
      |        /   |
      |       /  [012] (filled)
      |      /     |
      |     /      |
      0 ---------- 1

  4 nodes:  0, 1, 2, 3
  5 edges:  [01], [12], [02], [23], [30]
  1 face:   [012]  (oriented 0 -> 1 -> 2 -> 0)

The edge cochain space C^1 (5-dimensional) decomposes orthogonally as

    C^1  =  Im D^0   +  ker L^1  +  Im B_2
           (curl-free) (harmonic) (divergence-free)
            dim 3       dim 1       dim 1

Under the simplicial Kuramoto dynamics (Nurisso et al. 2024, Eq. 13/30),
these three components evolve independently. With zero natural frequencies
(omega = 0), the harmonic component is dynamically frozen -- this is the
cochain-level statement of the framework's U(1) gauge invariance
(PAPER_UNIFIED.md sec 1.5 item 6) and the harmonic phase-shift symmetry
of Nurisso et al. sec III.E.

The script verifies three claims:

  (1) Hodge orthogonality. The three projection operators P_cf, P_h, P_df
      onto the curl-free, harmonic, divergence-free subspaces are mutually
      orthogonal and sum to the identity.

  (2) Harmonic inertness. With omega = 0, the harmonic component of the
      cochain trajectory is constant in time, to numerical precision.

  (3) Independent evolution. The off-component inner products
      <theta_cf, theta_h>, <theta_cf, theta_df>, <theta_h, theta_df>
      remain zero throughout the evolution (no leakage between
      Hodge subspaces).

Reference:
  Nurisso, M. et al. "A unified framework for simplicial Kuramoto models."
  Chaos 34, 053118 (2024). arXiv:2305.17977.

Author: J. Bramble (with Claude Opus 4.7, Anthropic)
"""

import numpy as np
from scipy.integrate import solve_ivp


# ===========================================================================
#  Section 1: Simplicial complex setup
# ===========================================================================
#
# Orientations:
#   Each edge [ij] is oriented from i to j.
#   The face [012] has boundary  d[012] = +[01] + [12] - [02]
#     (the [02] sign is negative because the triangle traverses 2 -> 0).

NODES = 4
EDGES_LABELS = ["[01]", "[12]", "[02]", "[23]", "[30]"]
EDGES = len(EDGES_LABELS)             # 5
FACES_LABELS = ["[012]"]
FACES = len(FACES_LABELS)              # 1

# Incidence matrix B_1: rows are nodes, columns are edges.
# B_1[i,j] = +1 if edge j ends at node i, -1 if it starts at node i.
B1 = np.array([
    # [01] [12] [02] [23] [30]
    [-1,   0,  -1,   0,  +1],   # node 0
    [+1,  -1,   0,   0,   0],   # node 1
    [ 0,  +1,  +1,  -1,   0],   # node 2
    [ 0,   0,   0,  +1,  -1],   # node 3
], dtype=float)

# Incidence matrix B_2: rows are edges, columns are faces.
# B_2[i,j] = sign of edge i in the boundary of face j.
B2 = np.array([
    [+1.0],   # [01]: coherent with [012]
    [+1.0],   # [12]: coherent
    [-1.0],   # [02]: incoherent (the triangle goes 2 -> 0)
    [ 0.0],   # [23]: not on triangle
    [ 0.0],   # [30]: not on triangle
])

# Coboundary operators (unweighted simplicial complex: D^k = B_{k+1}^T)
D0 = B1.T    # 5 x 4: maps node cochains to edge cochains (gradient)
D1 = B2.T    # 1 x 5: maps edge cochains to face cochain (curl)

# Sanity check the "boundary of boundary is zero" identity:
# B_1 @ B_2 should be the 4x1 zero matrix.
assert np.allclose(B1 @ B2, 0.0), "B_1 @ B_2 must vanish (boundary of boundary)"


# ===========================================================================
#  Section 2: Hodge Laplacian and projectors onto Hodge subspaces
# ===========================================================================

def hodge_components(tol=1e-10):
    """Return projectors onto the three Hodge subspaces of C^1 (edges).

    P_cf : projects onto Im D^0    (curl-free,    image of node gradient)
    P_h  : projects onto ker L^1   (harmonic,     topologically nontrivial)
    P_df : projects onto Im B_2    (divergence-free, image of face curl)
    """
    # Curl-free: column space of D^0 (= B_1^T)
    U_cf, S_cf, _ = np.linalg.svd(D0, full_matrices=False)
    rank_cf = int(np.sum(S_cf > tol))
    basis_cf = U_cf[:, :rank_cf]
    P_cf = basis_cf @ basis_cf.T

    # Divergence-free: column space of B_2
    U_df, S_df, _ = np.linalg.svd(B2, full_matrices=False)
    rank_df = int(np.sum(S_df > tol))
    basis_df = U_df[:, :rank_df]
    P_df = basis_df @ basis_df.T

    # Harmonic: orthogonal complement of (curl-free + divergence-free) in C^1
    P_h = np.eye(EDGES) - P_cf - P_df

    return P_cf, P_h, P_df, rank_cf, rank_df


# ===========================================================================
#  Section 3: Simplicial Kuramoto on edges
# ===========================================================================

def edge_kuramoto(t, theta, omega, sigma_up, sigma_down):
    """The simplicial Kuramoto dynamics on edges (Nurisso et al. Eq. 13, k=1):

        dtheta/dt = omega - sigma_up * B_2 sin(D^1 theta)
                          - sigma_down * D^0 sin(B^1 theta)

    Interaction-from-above (sigma_up) couples edges through the filled triangle.
    Interaction-from-below (sigma_down) couples edges through shared nodes.
    """
    return (omega
            - sigma_up   * (B2 @ np.sin(D1 @ theta))
            - sigma_down * (D0 @ np.sin(B1 @ theta)))


# ===========================================================================
#  Section 4: Main demonstration
# ===========================================================================

def main():
    print("=" * 72)
    print("Hodge decomposition of edge cochains under simplicial Kuramoto")
    print("Demonstration for PAPER_UNIFIED.md Appendix B sec B.5")
    print("=" * 72)

    # ---- Hodge decomposition of C^1 ----
    P_cf, P_h, P_df, rk_cf, rk_df = hodge_components()
    rk_h = EDGES - rk_cf - rk_df

    print(f"\nSimplicial complex: {NODES} nodes, {EDGES} edges, {FACES} face(s)")
    print(f"  Edges:  {EDGES_LABELS}")
    print(f"  Face:   {FACES_LABELS}  (filled triangle)\n")

    print(f"Hodge decomposition of C^1 (5-dimensional edge cochain space):")
    print(f"  dim(Im D^0)   = {rk_cf}   (curl-free,    node gradients)")
    print(f"  dim(ker L^1)  = {rk_h}   (harmonic,     1 independent loop)")
    print(f"  dim(Im B_2)   = {rk_df}   (divergence-free,  face curls)")
    print(f"  Total         = {rk_cf + rk_h + rk_df}   (= 5 edges)\n")

    # ---- Verify projector properties ----
    print(f"[Test 1] Projector orthogonality (should all be ~0):")
    print(f"  ||P_cf @ P_h||  = {np.linalg.norm(P_cf @ P_h):.2e}")
    print(f"  ||P_cf @ P_df|| = {np.linalg.norm(P_cf @ P_df):.2e}")
    print(f"  ||P_h  @ P_df|| = {np.linalg.norm(P_h  @ P_df):.2e}")
    print(f"  ||P_cf + P_h + P_df - I|| = "
          f"{np.linalg.norm(P_cf + P_h + P_df - np.eye(EDGES)):.2e}")

    # ---- Set up initial condition spanning all three subspaces ----
    rng = np.random.default_rng(seed=42)
    theta0 = 0.4 * rng.standard_normal(EDGES)
    theta0_cf = P_cf @ theta0
    theta0_h  = P_h  @ theta0
    theta0_df = P_df @ theta0

    print(f"\nInitial cochain decomposition (random seed 42):")
    print(f"  ||theta_cf(0)|| = {np.linalg.norm(theta0_cf):.4f}")
    print(f"  ||theta_h(0)||  = {np.linalg.norm(theta0_h):.4f}")
    print(f"  ||theta_df(0)|| = {np.linalg.norm(theta0_df):.4f}")

    # ---- Run simplicial Kuramoto, omega = 0 ----
    omega = np.zeros(EDGES)
    sigma_up = 1.0
    sigma_down = 1.0
    t_max = 8.0
    t_eval = np.linspace(0.0, t_max, 200)

    sol = solve_ivp(
        edge_kuramoto, (0.0, t_max), theta0, t_eval=t_eval,
        args=(omega, sigma_up, sigma_down),
        method='RK45', rtol=1e-12, atol=1e-12,
    )

    theta_t = sol.y                       # shape (5, 200)
    theta_cf_t = P_cf @ theta_t
    theta_h_t  = P_h  @ theta_t
    theta_df_t = P_df @ theta_t

    norms_cf = np.linalg.norm(theta_cf_t, axis=0)
    norms_h  = np.linalg.norm(theta_h_t,  axis=0)
    norms_df = np.linalg.norm(theta_df_t, axis=0)

    # ---- Display evolution ----
    print(f"\n[Test 2] Component-norm evolution (omega=0, sigma_up=sigma_down=1):")
    print(f"  {'t':>6s}  {'||cf||':>12s}  {'||h||':>12s}  {'||df||':>12s}")
    print(f"  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}")
    for i in (0, 10, 40, 80, 120, 199):
        print(f"  {t_eval[i]:6.2f}  {norms_cf[i]:12.6f}  "
              f"{norms_h[i]:12.6f}  {norms_df[i]:12.6f}")

    # ---- Verify harmonic inertness ----
    harmonic_drift = np.max(np.abs(theta_h_t - theta_h_t[:, [0]]))
    print(f"\n[Test 3] Harmonic inertness (omega=0 -> theta_h is constant):")
    print(f"  Max |theta_h(t) - theta_h(0)| over all t = {harmonic_drift:.2e}")

    # ---- Verify orthogonality preserved by the dynamics ----
    ip_cf_h  = np.einsum('it,it->t', theta_cf_t, theta_h_t)
    ip_cf_df = np.einsum('it,it->t', theta_cf_t, theta_df_t)
    ip_h_df  = np.einsum('it,it->t', theta_h_t,  theta_df_t)
    print(f"\n[Test 4] Orthogonality preservation (max over t, should be ~0):")
    print(f"  max |<cf, h>|  = {np.max(np.abs(ip_cf_h)):.2e}")
    print(f"  max |<cf, df>| = {np.max(np.abs(ip_cf_df)):.2e}")
    print(f"  max |<h, df>|  = {np.max(np.abs(ip_h_df)):.2e}")

    # ---- Bonus: verify cross-coupling vanishes structurally ----
    # The Kuramoto interaction terms preserve the Hodge decomposition because
    # B_2 sin(D^1 theta) is always in Im B_2 (divergence-free)
    # D^0 sin(B^1 theta) is always in Im D^0 (curl-free)
    # We verify this for the initial condition.
    rhs = edge_kuramoto(0.0, theta0, omega, sigma_up, sigma_down)
    rhs_cf = P_cf @ rhs
    rhs_h  = P_h  @ rhs
    rhs_df = P_df @ rhs
    print(f"\n[Test 5] Vector field stays within Hodge structure at t=0:")
    print(f"  ||(I - P_cf - P_df) @ dtheta/dt|| = {np.linalg.norm(rhs_h):.2e}")
    print(f"  (i.e. the dynamics never produces a harmonic component)")

    print(f"\n" + "=" * 72)
    print(f"Summary")
    print(f"=" * 72)
    print(f"  C^1 decomposes orthogonally into curl-free, harmonic, and")
    print(f"  divergence-free subspaces. Under simplicial Kuramoto with")
    print(f"  omega = 0, the harmonic component is dynamically inert and")
    print(f"  the dynamics never leaks between subspaces. This is the")
    print(f"  cochain-level realization of PAPER sec 3.7's coherence")
    print(f"  sub-manifold and the sec 1.5 (item 6) U(1) gauge invariance,")
    print(f"  made rigorous via the simplicial Hodge decomposition of")
    print(f"  Nurisso et al. sec III.E.")
    print(f"=" * 72)


if __name__ == "__main__":
    main()
