"""
stuartlandau_haldane_check.py — WHERE the Haldane flux honestly enters the
oscillator linearization (referee-proofing for EMERGENT_FIELDS_PAPER.md)
==========================================================================

THE TRAP (why this script exists): linearizing the PHASE-ONLY Kuramoto-
Sakaguchi model about the uniform synchronized state,

    force on i from j = -K sin(eps_i - eps_j + a_ij)
                      ~ -K sin(a_ij) - K cos(a_ij) (eps_i - eps_j),

gives a coupling matrix ~ cos(a) x (graph Laplacian): REAL SYMMETRIC — cos is
even, so even an antisymmetric lag a_ij = -a_ji contributes identically in
both directions. No mass term, no flux, Dirac points unbroken. Inertia
changes nothing. The Sakaguchi lag CANNOT produce a Haldane phase in a
phase-only model at linear order.

THE HONEST MODEL: limit-cycle (Stuart-Landau) oscillators,

  dz_i/dt = (mu + i w) z_i - |z_i|^2 z_i + e^{i beta} Sum_j g_ij e^{i a_ij} z_j

whose phase reduction IS Kuramoto-Sakaguchi. Two coupling angles matter:
  a_ij : ANTISYMMETRIC link lag (a_ij = -a_ji, Haldane/DMI orientation
         pattern on next-nearest-neighbour bonds) -> the would-be flux;
  beta : the coupling's global dissipative/reactive mixing angle
         (beta = 0: dissipative, real coupling; beta = pi/2: reactive,
         Hamiltonian-like coupling — the magnon limit).

FINDINGS VERIFIED HERE (no Hamiltonian written down by hand):
  (1) The 4x4 Bloch generator M(k) of the linearized dynamics — particle-
      conserving block P(k) = (Haldane Hamiltonian with flux a) plus a local
      anomalous (a, a*) block of strength r0^2 from the amplitude
      nonlinearity — is validated against a brute-force numerical Jacobian
      of the real 2N-dim ODE system on a torus (machine agreement).
  (2) PURELY DISSIPATIVE coupling (beta = 0): the anomalous block pairs each
      Haldane copy with its conjugate (opposite-mass) partner, and the two
      least-damped bands are EXACTLY degenerate at K, K' for every amplitude
      stiffness r0^2: the flux enters the eigenvectors but the spectrum
      stays gapless — no topological phase. (Checked to machine precision.)
      This is the BdG shadow of the phase-only cos-even obstruction.
  (3) REACTIVE coupling component (beta -> pi/2): the conjugate pairing is
      lifted; the positive-frequency band pair acquires the Haldane gap and
      the upper band carries Chern number C = sign(a) (FHS over the
      eigenvector bundle), robust across amplitude stiffness. K-point gap
      grows ~ sin(beta): the flux needs a REACTIVE coupling channel.
  (4) Phase-only control at beta = 0: the 2x2 phase stiffness has d_z == 0
      identically (gap at K exactly zero for all a) — trivial, as claimed.

PLATFORM MORAL: a Haldane phase in oscillator arrays needs (i) amplitude
dynamics (limit-cycle, not phase-only), (ii) an antisymmetric (DMI-like) lag
pattern, and (iii) a reactive component in the coupling. Laser/photonic,
optomechanical, NEMS and JJ couplings are generically complex (reactive +
dissipative), so (iii) is a parameter requirement, not an exclusion.

Run:  python stuartlandau_haldane_check.py     -> prints checks, saves .png
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SQ3 = np.sqrt(3.0)
DELTA = np.array([[1.0, 0.0], [-0.5, SQ3 / 2], [-0.5, -SQ3 / 2]])   # A -> B
BVEC = np.array([[0.0, SQ3], [-1.5, -SQ3 / 2], [1.5, -SQ3 / 2]])    # NNN
G1 = 2 * np.pi * np.array([1 / 3, 1 / SQ3])
G2 = 2 * np.pi * np.array([1 / 3, -1 / SQ3])
K_PT = (2 * G1 + G2) / 3

G1C, G2C = 1.0, 0.3          # NN / NNN coupling magnitudes
ALPHA = np.pi / 2            # antisymmetric NNN lag (Haldane/DMI pattern)
MU = 0.5


def structure(kx, ky, alpha, g1=G1C, g2=G2C):
    """Bare Bloch structure matrix S(k): Haldane form with flux = alpha."""
    kb = kx * BVEC[:, 0] + ky * BVEC[:, 1]
    kd = kx * DELTA[:, 0] + ky * DELTA[:, 1]
    gA = 2 * g2 * np.cos(kb + alpha).sum()
    gB = 2 * g2 * np.cos(kb - alpha).sum()
    f = g1 * np.exp(1j * kd).sum()
    return np.array([[gA, f], [np.conj(f), gB]], dtype=complex)


def bloch_generator(kx, ky, mu, alpha, beta, g1=G1C, g2=G2C):
    """4x4 generator of d/dt [aA(k), aB(k), aA*(-k), aB*(-k)] linearized about
    the uniform synchronized state, coupling prefactor e^{i beta}."""
    chi = (3 * g1 + 6 * g2 * np.cos(alpha)) * np.exp(1j * beta)  # uniform sum
    r2 = mu + chi.real                       # fixed-point amplitude^2
    if r2 <= 0:
        raise ValueError("no synchronized limit cycle at these parameters")
    cdiag = mu - 2 * r2 - 1j * chi.imag      # local part in rotating frame
    S = np.exp(1j * beta) * structure(kx, ky, alpha, g1, g2)
    Sm = np.exp(1j * beta) * structure(-kx, -ky, alpha, g1, g2)
    P = cdiag * np.eye(2) + S
    Pc = np.conj(cdiag) * np.eye(2) + np.conj(Sm)
    Q = -r2 * np.eye(2)
    return np.block([[P, Q], [Q, Pc]])


# ----------------------------------------------------------------------------
# (1) validation: brute-force Jacobian on an LxL torus
# ----------------------------------------------------------------------------
def torus_jacobian_eigs(L, mu, alpha, beta, g1=G1C, g2=G2C):
    n = 2 * L * L

    def idx(x, y, s):
        return ((x % L) * L + (y % L)) * 2 + s

    T = np.zeros((n, n), dtype=complex)
    for x in range(L):
        for y in range(L):
            iA, iB = idx(x, y, 0), idx(x, y, 1)
            for jB in (iB, idx(x - 1, y, 1), idx(x, y - 1, 1)):
                T[iA, jB] += g1; T[jB, iA] += g1
            for (dx, dy) in ((1, -1), (0, 1), (-1, 0)):     # +b_m in cell coords
                jA = idx(x + dx, y + dy, 0)
                T[iA, jA] += g2 * np.exp(1j * alpha)
                T[jA, iA] += g2 * np.exp(-1j * alpha)
                jB = idx(x + dx, y + dy, 1)
                T[iB, jB] += g2 * np.exp(-1j * alpha)
                T[jB, iB] += g2 * np.exp(1j * alpha)
    T *= np.exp(1j * beta)
    chi = (3 * g1 + 6 * g2 * np.cos(alpha)) * np.exp(1j * beta)
    r2 = mu + chi.real
    dw = -chi.imag                       # rotating-frame detuning

    def rhs(u):
        z = u[:n] + 1j * u[n:]
        dz = (mu + 1j * dw) * z - np.abs(z) ** 2 * z + T @ z
        return np.concatenate([dz.real, dz.imag])

    u0 = np.concatenate([np.full(n, np.sqrt(r2)), np.zeros(n)])
    assert np.max(np.abs(rhs(u0))) < 1e-12, "uniform state not a fixed point"
    eps = 1e-6
    J = np.empty((2 * n, 2 * n))
    for m in range(2 * n):
        d = np.zeros(2 * n); d[m] = eps
        J[:, m] = (rhs(u0 + d) - rhs(u0 - d)) / (2 * eps)
    return np.linalg.eigvals(J)


def bloch_eigs_all(L, mu, alpha, beta):
    ev = []
    for p in range(L):
        for q in range(L):
            k = (p / L) * G1 + (q / L) * G2
            ev.append(np.linalg.eigvals(
                bloch_generator(k[0], k[1], mu, alpha, beta)))
    return np.concatenate(ev)


# ----------------------------------------------------------------------------
# spectral gap of the least-damped pair at a given k
# ----------------------------------------------------------------------------
def pair_gap(kx, ky, mu, alpha, beta):
    lam = np.linalg.eigvals(bloch_generator(kx, ky, mu, alpha, beta))
    lam = lam[np.argsort(-lam.real)]
    return abs(lam[0] - lam[1])          # complex-plane distance, bands 0-1


# ----------------------------------------------------------------------------
# Chern number of the positive-frequency bands (reactive regime)
# ----------------------------------------------------------------------------
def chern_posfreq(mu, alpha, beta, n=36, band="upper"):
    """FHS Chern number over the eigenvector field of the positive-frequency
    (Im lambda > 0) pair of M(k); band = 'upper'/'lower' by Im lambda."""
    s = (np.arange(n) + 0.5) / n
    u = np.empty((n, n, 4), dtype=complex)
    mingap = np.inf
    sel = 1 if band == "upper" else 0
    for i in range(n):
        for j in range(n):
            k = s[i] * G1 + s[j] * G2
            lam, vec = np.linalg.eig(
                bloch_generator(k[0], k[1], mu, alpha, beta))
            pos = np.argsort(lam.imag)[-2:]          # two largest Im
            pos = pos[np.argsort(lam.imag[pos])]     # [lower, upper]
            u[i, j] = vec[:, pos[sel]]
            mingap = min(mingap, abs(lam[pos[1]] - lam[pos[0]]))

    def link(arr, axis):
        ov = np.sum(np.conj(arr) * np.roll(arr, -1, axis=axis), axis=-1)
        return ov / np.abs(ov)

    U1, U2 = link(u, 0), link(u, 1)
    F = np.angle(U1 * np.roll(U2, -1, axis=0) / (np.roll(U1, -1, axis=1) * U2))
    return int(np.rint(F.sum() / (2 * np.pi))), mingap


def main():
    print("=" * 72)
    print("(1) Bloch generator vs brute-force Jacobian (L=6 torus, 144 dims)")
    for beta in (0.0, np.pi / 2, 0.3):
        ej = torus_jacobian_eigs(6, MU, ALPHA, beta)
        eb = bloch_eigs_all(6, MU, ALPHA, beta)
        # multiset comparison robust to degenerate-eigenvalue sort order
        d = np.abs(ej[:, None] - eb[None, :])
        err = max(d.min(axis=0).max(), d.min(axis=1).max())
        print(f"    beta = {beta:5.3f}:  multiset eig distance = {err:.3e}")
        assert err < 1e-5

    print("(2) DISSIPATIVE coupling (beta=0): least-damped pair at K")
    print("    (particle-hole pairing carries the conjugate, opposite-mass")
    print("     Haldane copy -> exact degeneracy, NO topological gap):")
    for mu in (0.5, 4.0, 32.0):
        g = pair_gap(K_PT[0], K_PT[1], mu, ALPHA, 0.0)
        r2 = mu + 3 * G1C + 6 * G2C * np.cos(ALPHA)
        print(f"    r0^2 = {r2:6.2f}:  |lambda_0 - lambda_1|(K) = {g:.2e}")

    print("(3) REACTIVE coupling (beta=pi/2): positive-frequency bands")
    for a in (ALPHA, -ALPHA):
        C, gap = chern_posfreq(MU, a, np.pi / 2)
        print(f"    alpha = {a:+.3f}:  C(upper) = {C:+d}   "
              f"(min pair gap {gap:.4f})")
    print("    robustness across amplitude stiffness (alpha=+pi/2):")
    for mu in (0.2, 1.0, 4.0, 16.0):
        C, gap = chern_posfreq(mu, ALPHA, np.pi / 2, n=30)
        r2 = mu + 3 * G1C
        print(f"    r0^2 = {r2:6.2f}:  C = {C:+d}   (min pair gap {gap:.4f})")

    print("(3b) K-point gap vs dissipative/reactive mixing angle beta:")
    betas = np.linspace(0, np.pi / 2, 10)
    gk = [pair_gap(K_PT[0], K_PT[1], MU, ALPHA, b) for b in betas]
    for b, g in zip(betas, gk):
        print(f"    beta = {b:5.3f}:  gap(K) = {g:.4f}")

    print("(4) phase-only control: d_z(K) with lag, any pattern")
    #    linear phase coefficient is cos(a_ij) = cos(a) both directions ->
    #    the mass channel d_z = (gA - gB)/2 with cos-weights is identically 0:
    kb = K_PT[0] * BVEC[:, 0] + K_PT[1] * BVEC[:, 1]
    dz = (2 * G2C * np.cos(ALPHA) * np.cos(kb).sum()
          - 2 * G2C * np.cos(-ALPHA) * np.cos(kb).sum()) / 2
    print(f"    d_z(K)|phase-only = {dz:.2e}  (gapless for every alpha)")

    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(betas, gk, "o-")
    ax[0].set(xlabel=r"coupling mixing angle $\beta$ (0 = dissipative, "
                     r"$\pi/2$ = reactive)",
              ylabel=r"least-damped pair gap at $K$",
              title="the Haldane gap needs a reactive channel")
    nodes = [np.zeros(2), K_PT, (G1 + G2) / 2, np.zeros(2)]
    path = []
    for a_, b_ in zip(nodes[:-1], nodes[1:]):
        for t in np.linspace(0, 1, 60, endpoint=False):
            path.append(a_ + t * (b_ - a_))
    lam = np.array([np.sort(np.linalg.eigvals(
        bloch_generator(k[0], k[1], MU, ALPHA, np.pi / 2)).imag)
        for k in path])
    for b in range(4):
        ax[1].plot(lam[:, b], lw=1)
    ax[1].set(xlabel=r"$\Gamma \to K \to M \to \Gamma$",
              ylabel=r"Im $\lambda$ (frequency bands)",
              title=r"reactive limit $\beta=\pi/2$: gapped Haldane pair")
    fig.tight_layout()
    out = __file__.replace(".py", ".png")
    fig.savefig(out, dpi=130)
    print(f"figure -> {out}")


if __name__ == "__main__":
    main()
