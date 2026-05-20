"""
hodge_dirac.py

Numerical demonstration that the discrete Hodge-Dirac operator

    D = d + delta

on a simplicial complex satisfies the key algebraic identity

    D^2 = Delta  (the Hodge Laplacian on the full cochain complex),

and anticommutes with the chirality grading

    Gamma : psi^(k) -> (-1)^k psi^(k),    {D, Gamma} = 0.

This is the discrete realization of the property that justifies the name
"Dirac" for the operator D: it is the first-order square root of the
Laplacian, exactly as Dirac's  i gamma^mu d_mu  is the first-order square
root of the Klein-Gordon operator. The framework's chiral grading
(temporal vs. spatial clock; psi_L vs. psi_R) is the spectral consequence
of the Gamma-grading: eigenvalues of D come in +/- pairs, with zero
eigenvalues corresponding to harmonic (topologically protected) modes.

This script supports PAPER_UNIFIED.md Appendix B sec B.3
("The Hodge-Dirac Operator") and sec B.4 (chiral decomposition).

Verification claims:

  (1) D^2 = Delta on the full cochain complex.
  (2) {D, Gamma} = 0 (anticommutation with chirality grading).
  (3) D is symmetric (real-Hermitian) for the unweighted complex.
  (4) Spectrum: eigenvalues come in +/- pairs about zero, with
      multiplicity of the zero eigenvalue = sum of Betti numbers
      (i.e., dim ker D = beta_0 + beta_1 + beta_2 for our complex).
  (5) Each harmonic eigenvector lives in a single Gamma sector
      (grade-pure: a harmonic cochain belongs to exactly one C^k).
  (6) For each nonzero eigenvalue lambda, Gamma applied to the eigenvector
      produces an eigenvector with eigenvalue -lambda.

Reference:
  Nurisso, M. et al. "A unified framework for simplicial Kuramoto models."
  Chaos 34, 053118 (2024). arXiv:2305.17977.

Author: J. Bramble (with Claude Opus 4.7, Anthropic)
"""

import numpy as np
from scipy.linalg import block_diag


# ===========================================================================
#  Section 1: Simplicial complex (same complex as hodge_decomposition.py)
# ===========================================================================
#
#       3 ---------- 2
#       |          / |
#       |         /  |
#       |        /   |
#       |       /  [012] (filled)
#       |      /     |
#       |     /      |
#       0 ---------- 1
#
#   4 nodes: 0, 1, 2, 3                       dim C^0 = 4
#   5 edges: [01], [12], [02], [23], [30]     dim C^1 = 5
#   1 face:  [012]                            dim C^2 = 1
#
# Total cochain complex dimension: 4 + 5 + 1 = 10.

N0, N1, N2 = 4, 5, 1
TOTAL = N0 + N1 + N2  # 10

# Incidence matrices
B1 = np.array([
    [-1,   0,  -1,   0,  +1],
    [+1,  -1,   0,   0,   0],
    [ 0,  +1,  +1,  -1,   0],
    [ 0,   0,   0,  +1,  -1],
], dtype=float)                                # 4 x 5

B2 = np.array([
    [+1.0],
    [+1.0],
    [-1.0],
    [ 0.0],
    [ 0.0],
])                                              # 5 x 1

# Sanity check: boundary of boundary vanishes (Nurisso et al. Eq. 9).
assert np.allclose(B1 @ B2, 0.0), "B_1 @ B_2 must vanish"

# Exterior derivative (coboundary) and codifferential (boundary), unweighted:
#   d^k     = B_{k+1}^T   :  C^k -> C^{k+1}    (going "up")
#   delta^k = B_k         :  C^k -> C^{k-1}    (going "down")
d0     = B1.T                                   # 5 x 4
d1     = B2.T                                   # 1 x 5
delta1 = B1                                     # 4 x 5
delta2 = B2                                     # 5 x 1


# ===========================================================================
#  Section 2: Build the Hodge-Dirac operator and the Hodge Laplacian
# ===========================================================================
#
# Acting on the column vector (psi^0, psi^1, psi^2)^T,
#
#        [ 0     delta1   0      ]
#   D =  [ d0    0        delta2 ]
#        [ 0     d1       0      ]
#
# Block-diagonal Hodge Laplacian:
#
#        [ Delta^0   0          0       ]
#   Delta =  [ 0       Delta^1   0       ]
#        [ 0          0          Delta^2 ]
#
# with
#     Delta^0 = delta1 d0
#     Delta^1 = d0 delta1 + delta2 d1
#     Delta^2 = d1 delta2

def build_hodge_dirac():
    """Return the full Hodge-Dirac operator D as a 10x10 matrix."""
    D = np.zeros((TOTAL, TOTAL))
    s0 = slice(0,            N0)
    s1 = slice(N0,           N0 + N1)
    s2 = slice(N0 + N1,      TOTAL)
    D[s0, s1] = delta1
    D[s1, s0] = d0
    D[s1, s2] = delta2
    D[s2, s1] = d1
    return D


def build_hodge_laplacian():
    """Return the block-diagonal Hodge Laplacian on the full complex."""
    Delta0 = delta1 @ d0                        # 4 x 4
    Delta1 = d0 @ delta1 + delta2 @ d1          # 5 x 5
    Delta2 = d1 @ delta2                        # 1 x 1
    return block_diag(Delta0, Delta1, Delta2)


def build_chirality_grading():
    """Return Gamma = diag(+I, -I, +I) on the (C^0, C^1, C^2) blocks.

    Gamma is the discrete analog of gamma_5 in standard Dirac theory.
    """
    return block_diag(+np.eye(N0), -np.eye(N1), +np.eye(N2))


# ===========================================================================
#  Section 3: Verification tests
# ===========================================================================

def main():
    print("=" * 72)
    print("Hodge-Dirac operator on a simplicial complex:  D^2 = Delta")
    print("Demonstration for PAPER_UNIFIED.md Appendix B sec B.3 / B.4")
    print("=" * 72)

    D = build_hodge_dirac()
    Delta = build_hodge_laplacian()
    Gamma = build_chirality_grading()

    print(f"\nCochain complex dimensions:")
    print(f"  dim C^0 (nodes) = {N0}")
    print(f"  dim C^1 (edges) = {N1}")
    print(f"  dim C^2 (faces) = {N2}")
    print(f"  total           = {TOTAL}")

    # ---- Test 1: D^2 = Delta ----
    D_squared = D @ D
    err_DD = np.max(np.abs(D_squared - Delta))
    print(f"\n[Test 1] D^2 = Delta  (algebraic identity defining 'Dirac'):")
    print(f"  max |D^2 - Delta| = {err_DD:.2e}")

    # ---- Test 2: {D, Gamma} = 0 ----
    anticomm = D @ Gamma + Gamma @ D
    err_anticomm = np.max(np.abs(anticomm))
    print(f"\n[Test 2] Anticommutation  {{D, Gamma}} = 0  (chirality grading):")
    print(f"  max |D Gamma + Gamma D| = {err_anticomm:.2e}")

    # ---- Test 3: D = D^T (symmetric) ----
    err_sym = np.max(np.abs(D - D.T))
    print(f"\n[Test 3] Symmetry  D = D^T  (unweighted complex):")
    print(f"  max |D - D^T| = {err_sym:.2e}")

    # ---- Test 4: spectrum of D ----
    eigvals, eigvecs = np.linalg.eigh(D)
    eps = 1e-9
    n_zero = int(np.sum(np.abs(eigvals) < eps))
    n_pos  = int(np.sum(eigvals > eps))
    n_neg  = int(np.sum(eigvals < -eps))

    print(f"\n[Test 4] Spectrum of D (real, symmetric about zero):")
    print(f"  {'idx':>4s}  {'lambda':>12s}")
    print(f"  {'-'*4}  {'-'*12}")
    for i, lam in enumerate(eigvals):
        marker = "  <-- harmonic" if abs(lam) < eps else ""
        print(f"  {i:>4d}  {lam:+12.6f}{marker}")
    print(f"\n  Zero eigenvalues:     {n_zero}")
    print(f"  Positive eigenvalues: {n_pos}")
    print(f"  Negative eigenvalues: {n_neg}")
    print(f"  Symmetric about zero: |#pos - #neg| = {abs(n_pos - n_neg)}")
    print(f"  Predicted dim ker D = beta_0 + beta_1 + beta_2 = 1 + 1 + 0 = 2")
    print(f"  Measured  dim ker D = {n_zero}")

    # ---- Test 5: harmonic eigenvectors are grade-pure ----
    # The full kernel of D is invariant under Gamma (since {D, Gamma} = 0
    # gives [D^2, Gamma] = 0, so Gamma commutes with Delta = D^2). So we can
    # diagonalize each Delta^k separately and find grade-pure harmonic modes.
    print(f"\n[Test 5] Grade-pure harmonic basis (computed from each Delta^k):")
    Delta_per_grade = (delta1 @ d0,                 # Delta^0  (nodes)
                       d0 @ delta1 + delta2 @ d1,   # Delta^1  (edges)
                       d1 @ delta2)                 # Delta^2  (faces)
    grade_labels = ("C^0 (nodes)", "C^1 (edges)", "C^2 (faces)")
    expected_betti = (1, 1, 0)

    for k, (Dk, label, beta) in enumerate(
            zip(Delta_per_grade, grade_labels, expected_betti)):
        evals_k, evecs_k = np.linalg.eigh(Dk)
        zero_idx = np.where(np.abs(evals_k) < eps)[0]
        print(f"  ker Delta^{k}  ({label}):  "
              f"dim = {len(zero_idx)}  (expected beta_{k} = {beta})")
        for j, idx in enumerate(zero_idx):
            v = evecs_k[:, idx]
            if v[np.argmax(np.abs(v))] < 0:    # sign convention for display
                v = -v
            print(f"    harmonic mode: {v.round(4)}")

    # ---- Test 6: Gamma maps +lambda eigenspace to -lambda eigenspace ----
    print(f"\n[Test 6] Gamma maps eigenspaces +/- (D (Gamma psi) = -lambda Gamma psi):")
    print(f"  {'+lambda':>12s}  {'||D(Gamma psi) + lambda*Gamma psi||':>40s}")
    print(f"  {'-'*12}  {'-'*40}")
    pos_idx = np.where(eigvals > eps)[0]
    for idx in pos_idx:
        lam = eigvals[idx]
        psi = eigvecs[:, idx]
        Gpsi = Gamma @ psi
        residual = np.linalg.norm(D @ Gpsi + lam * Gpsi)
        print(f"  {lam:+12.6f}  {residual:>40.2e}")

    print(f"\n" + "=" * 72)
    print(f"Summary")
    print(f"=" * 72)
    print(f"  The Hodge-Dirac operator D = d + delta on the cochain complex")
    print(f"  satisfies D^2 = Delta (machine precision), anticommutes with")
    print(f"  the chirality grading Gamma, and has a spectrum symmetric")
    print(f"  about zero with harmonic modes (zero eigenvalues) of total")
    print(f"  multiplicity equal to the sum of Betti numbers of the complex.")
    print(f"  This is the discrete realization of the algebraic property")
    print(f"  that gives the Dirac operator its name and motivates the")
    print(f"  framework's chiral L/R decomposition (Appendix B sec B.3-B.4).")
    print(f"=" * 72)


if __name__ == "__main__":
    main()
