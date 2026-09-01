"""Checks for CONTRACT_G1_G2 section 3.
P3(a): does the Gibbs / ground-state ready measure give uniform modal phase?
P3(b): with a genuinely local damping matrix, is C = 1 + O(f)?"""
import numpy as np
rng = np.random.default_rng(20260831)

n = 6
A = rng.normal(size=(n, n)); M = A @ A.T + n*np.eye(n)   # pos def, off-diagonal
B = rng.normal(size=(n, n)); K = B @ B.T + n*np.eye(n)   # pos def, coupled
kT = 0.7

L = np.linalg.cholesky(M)                 # M = L L^T
Kt = np.linalg.solve(L, np.linalg.solve(L, K).T).T   # L^-1 K L^-T
w2, V = np.linalg.eigh(Kt); Omega = np.sqrt(w2)

Ns = 400_000
p = rng.multivariate_normal(np.zeros(n), kT*M, size=Ns)
q = rng.multivariate_normal(np.zeros(n), kT*np.linalg.inv(K), size=Ns)

# modal coords: Q = V^T L^T q,  P = V^T L^-1 p   (row-vector convention)
Q = (q @ L) @ V
P = np.linalg.solve(L, p.T).T @ V

print("mode frequencies:", np.round(Omega, 3))
print("Cov(P) diag / kT      :", np.round(P.var(axis=0)/kT, 3), " (want all 1)")
print("Cov(Omega*Q) diag / kT:", np.round((Omega*Q).var(axis=0)/kT, 3), " (want all 1)")

print("\n--- P3(a) uniform phase ---")
mc = 1/np.sqrt(Ns/24)
worst = 0.0
for a in range(n):
    x, y = P[:, a], Omega[a]*Q[:, a]
    phi = np.arctan2(y, x); R = np.hypot(x, y)
    hist, _ = np.histogram(phi, bins=24, range=(-np.pi, np.pi))
    dev = np.abs(hist/hist.mean() - 1).max()
    worst = max(worst, dev)
    print(f"  mode {a}: max bin dev = {dev:6.4f}   corr(cos phi, R) = {np.corrcoef(np.cos(phi), R)[0,1]:+.4f}")
print(f"  worst {worst:.4f} vs Monte-Carlo scale {mc:.4f}  -> {'UNIFORM' if worst < 5*mc else 'NOT UNIFORM'}")

print("\n--- P3(b) C = 1 + O(f) with a local damping matrix ---")
# sites on a line, spacing 20 nm; local scattering correlation length 2 nm
x = np.arange(n)*20.0
Gam_loc = np.exp(-np.abs(x[:,None]-x[None,:])/2.0)   # near-diagonal
Gam_rad = np.ones((n, n))                            # wavelength-correlated
for f in (1e-6, 1e-3, 1e-1):
    Gam = (1-f)*Gam_loc + f*Gam_rad
    C = Gam/np.sqrt(np.outer(np.diag(Gam), np.diag(Gam)))
    off = np.abs(C - np.diag(np.diag(C))).max()
    print(f"  f = {f:.0e} -> max off-diagonal |C_ij| = {off:.3e}   ratio to f = {off/f:.2f}")
