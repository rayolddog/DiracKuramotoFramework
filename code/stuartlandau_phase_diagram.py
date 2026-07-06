"""
stuartlandau_phase_diagram.py — the three computations the referee demanded
==========================================================================
Companion to stuartlandau_haldane_check.py (imports its validated Bloch
builder). Produces, all within the HONEST Stuart-Landau linearization:

 (1) SEMENOFF-vs-HALDANE within SL: sublattice asymmetry enters the SL model
     naturally as a sublattice FREQUENCY DETUNING +/- delta (the oscillator
     realization of "pinning asymmetry"); sweep delta at fixed alpha, beta =
     pi/2 and find the C = +1 -> 0 boundary. Bare-dictionary prediction:
     |delta_c| = 3*sqrt(3)*g2*sin(alpha); report the SL-corrected value.
 (2) C(beta, r0^2) GRID: where in the dissipative/reactive x amplitude-
     stiffness plane the topological phase actually lives. C reported only
     where the band pair is cleanly separated (gap > GAP_MIN); 'und'
     otherwise. This is the paper's headline phase diagram.
 (3) RIBBON SPECTRUM: strip geometry (open along a2, Bloch along a1),
     linearized SL generator; look for a chiral in-gap branch localized on
     the edges — the honest (non-Hermitian-aware) check behind the paper's
     chiral-edge-mode signature. Also reports the edge-localization weight
     and checks for skin-effect pileup (bulk-state localization).

Run:  python stuartlandau_phase_diagram.py   -> prints results, saves .png
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from stuartlandau_haldane_check import (G1C, G2C, SQ3, G1, G2, K_PT,
                                        structure)

GAP_MIN = 0.05   # minimum band-pair separation for a trusted Chern number


def bloch_generator_d(kx, ky, mu, alpha, beta, delta=0.0, g1=G1C, g2=G2C):
    """4x4 SL Bloch generator with sublattice frequency detuning +/- delta.
    Detuning enters as +i*delta*sigma_z in the particle block and its
    conjugate in the hole block (rotating frame unchanged: the +/- detuning
    is traceless so the uniform sync solution is unaffected at this order
    for small delta; fixed point still checked in the parent script)."""
    chi = (3 * g1 + 6 * g2 * np.cos(alpha)) * np.exp(1j * beta)
    r2 = mu + chi.real
    if r2 <= 0:
        raise ValueError("no limit cycle")
    cdiag = mu - 2 * r2 - 1j * chi.imag
    S = np.exp(1j * beta) * structure(kx, ky, alpha, g1, g2)
    Sm = np.exp(1j * beta) * structure(-kx, -ky, alpha, g1, g2)
    sz = np.diag([1.0, -1.0])
    P = cdiag * np.eye(2) + S + 1j * delta * sz
    Pc = np.conj(cdiag) * np.eye(2) + np.conj(Sm) - 1j * delta * sz
    Q = -r2 * np.eye(2)
    return np.block([[P, Q], [Q, Pc]])


def chern_and_gap(mu, alpha, beta, delta=0.0, n=30):
    """FHS Chern of the upper positive-frequency band + min pair gap.
    Selection: two eigenvalues with largest Im (positive-frequency pair),
    upper = larger Im. Returns (C, mingap); C is None if gap < GAP_MIN."""
    s = (np.arange(n) + 0.5) / n
    u = np.empty((n, n, 4), dtype=complex)
    mingap = np.inf
    for i in range(n):
        for j in range(n):
            k = s[i] * G1 + s[j] * G2
            lam, vec = np.linalg.eig(
                bloch_generator_d(k[0], k[1], mu, alpha, beta, delta))
            pos = np.argsort(lam.imag)[-2:]
            pos = pos[np.argsort(lam.imag[pos])]
            u[i, j] = vec[:, pos[1]]
            mingap = min(mingap, abs(lam[pos[1]] - lam[pos[0]]))
    if mingap < GAP_MIN:
        return None, mingap

    def link(arr, axis):
        ov = np.sum(np.conj(arr) * np.roll(arr, -1, axis=axis), axis=-1)
        return ov / np.abs(ov)

    U1, U2 = link(u, 0), link(u, 1)
    F = np.angle(U1 * np.roll(U2, -1, axis=0) / (np.roll(U1, -1, axis=1) * U2))
    return int(np.rint(F.sum() / (2 * np.pi))), mingap


# ----------------------------------------------------------------------------
# (3) ribbon: open along a2 (W cells), Bloch along a1
# ----------------------------------------------------------------------------
def ribbon_generator(k1, W, mu, alpha, beta, g1=G1C, g2=G2C):
    """Linearized SL generator for a ribbon: W unit cells across, open
    boundary in the a2 direction, Bloch phase e^{i k1} per a1 step.
    Basis: for each row m: (a_A, a_B), then all conjugates."""
    chi = (3 * g1 + 6 * g2 * np.cos(alpha)) * np.exp(1j * beta)
    r2 = mu + chi.real
    cdiag = mu - 2 * r2 - 1j * chi.imag
    e = np.exp(1j * k1)
    n = 2 * W
    T = np.zeros((n, n), dtype=complex)      # particle-block hopping

    def A(m):
        return 2 * m

    def B(m):
        return 2 * m + 1

    for m in range(W):
        # NN: A(x,y) couples B(x,y), B(x-1,y), B(x,y-1)
        T[A(m), B(m)] += g1 * (1 + np.conj(e))     # same row: cells (0,0),(-1,0)
        T[B(m), A(m)] += g1 * (1 + e)
        if m > 0:
            T[A(m), B(m - 1)] += g1                # cell (0,-1)
            T[B(m - 1), A(m)] += g1
        # NNN Haldane pattern, +b_m in cell coords: (1,-1), (0,1), (-1,0)
        pa, ma = g2 * np.exp(1j * alpha), g2 * np.exp(-1j * alpha)
        for (dx, dy) in ((1, -1), (0, 1), (-1, 0)):
            ph = e ** dx
            m2 = m + dy
            if 0 <= m2 < W:
                T[A(m), A(m2)] += pa * ph
                T[A(m2), A(m)] += ma * np.conj(ph)
                T[B(m), B(m2)] += ma * ph
                T[B(m2), B(m)] += pa * np.conj(ph)
    T *= np.exp(1j * beta)
    # bulk-value diagonal (edge sites keep bulk r2: pinned-amplitude
    # approximation; adequate for band-structure demonstration)
    P = cdiag * np.eye(n) + T
    # conjugate block: conj of generator at -k1
    e2 = np.exp(-1j * k1)
    Tm = np.zeros((n, n), dtype=complex)
    for m in range(W):
        Tm[A(m), B(m)] += g1 * (1 + np.conj(e2))
        Tm[B(m), A(m)] += g1 * (1 + e2)
        if m > 0:
            Tm[A(m), B(m - 1)] += g1
            Tm[B(m - 1), A(m)] += g1
        pa, ma = g2 * np.exp(1j * alpha), g2 * np.exp(-1j * alpha)
        for (dx, dy) in ((1, -1), (0, 1), (-1, 0)):
            ph = e2 ** dx
            m2 = m + dy
            if 0 <= m2 < W:
                Tm[A(m), A(m2)] += pa * ph
                Tm[A(m2), A(m)] += ma * np.conj(ph)
                Tm[B(m), B(m2)] += ma * ph
                Tm[B(m2), B(m)] += pa * np.conj(ph)
    Tm *= np.exp(1j * beta)
    Pc = np.conj(cdiag) * np.eye(n) + np.conj(Tm)
    Q = -r2 * np.eye(n)
    return np.block([[P, Q], [Q, Pc]])


def main():
    MU, ALPHA = 0.5, np.pi / 2
    print("=" * 72)
    print("(1) Semenoff (sublattice detuning) vs Haldane within SL, beta=pi/2")
    bare = 3 * SQ3 * G2C * np.sin(ALPHA)
    print(f"    bare-dictionary boundary: delta_c = 3sqrt3*g2*sin(a) = {bare:.3f}")
    last = None
    for d in np.arange(0.0, 3.01, 0.25):
        C, gap = chern_and_gap(MU, ALPHA, np.pi / 2, delta=d)
        tag = "und" if C is None else f"{C:+d}"
        print(f"    delta = {d:4.2f}:  C = {tag:>3s}  (min gap {gap:.3f})")
        if C == 0 and last == 1:
            print(f"    -> SL boundary between {d-0.25:.2f} and {d:.2f} "
                  f"(bare {bare:.2f})")
        last = C

    print("(2) C(beta, r0^2) phase diagram (und = gap below "
          f"{GAP_MIN}, C untrusted)")
    betas = [0.4, 0.7, 1.0, 1.3, np.pi / 2]
    mus = [0.2, 0.5, 2.0, 8.0, 16.0]
    print("    r0^2 rows x beta cols; r0^2 = mu + Re[e^{ib}chi]")
    hdr = "    r0^2\\beta " + "".join(f"{b:8.2f}" for b in betas)
    print(hdr)
    grid = []
    for mu in mus:
        row = []
        r2s = []
        for b in betas:
            chi = (3 * G1C + 6 * G2C * np.cos(ALPHA)) * np.exp(1j * b)
            r2s.append(mu + chi.real)
            try:
                C, gap = chern_and_gap(mu, ALPHA, b, n=24)
                row.append("und" if C is None else f"{C:+d}")
            except ValueError:
                row.append("--")
        grid.append(row)
        print(f"    mu={mu:5.1f}    " + "".join(f"{c:>8s}" for c in row)
              + f"   (r0^2 = {r2s[-1]:.1f} at beta=pi/2)")

    print("(3) ribbon spectrum, W=24, beta=pi/2 (chiral edge check)")
    W = 24
    k1s = np.linspace(0, 2 * np.pi, 121)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    edge_found = 0
    skin_flag = 0.0
    for k1 in k1s:
        M = ribbon_generator(k1, W, MU, ALPHA, np.pi / 2)
        lam, vec = np.linalg.eig(M)
        sel = lam.imag > 0
        lam, vec = lam[sel], vec[:, sel]
        # edge weight: probability on outer 3 rows (both blocks)
        idx = np.arange(4 * W) % (2 * W) // 2      # row index of each basis el
        w_edge = (np.abs(vec[(idx < 3) | (idx >= W - 3), :]) ** 2).sum(0) / \
                 (np.abs(vec) ** 2).sum(0)
        ax[0].scatter(np.full(lam.shape, k1), lam.imag, c=w_edge, s=3,
                      cmap="coolwarm", vmin=0, vmax=1)
        # in-gap edge states near the bulk gap center at K-projection
        gapmask = (np.abs(lam.imag - lam.imag.mean()) <
                   0.45 * lam.imag.std()) & (w_edge > 0.6)
        edge_found += int(gapmask.sum() > 0)
        skin_flag = max(skin_flag, np.median(w_edge))
    ax[0].set(xlabel=r"$k_1$", ylabel=r"Im $\lambda$ (frequency)",
              title=f"SL ribbon bands, W={W}, colored by edge weight")
    print(f"    k-points with in-gap edge-localized states: {edge_found}"
          f" / {len(k1s)}")
    print(f"    median edge weight across ALL states (skin-effect flag; "
          f"~6/{W} = {6/W:.2f} expected if none): {skin_flag:.2f}")

    ax[1].axis("off")
    txt = "C(beta, r0^2) at alpha=pi/2\nrows mu = " + \
          ", ".join(str(m) for m in mus) + "\ncols beta = " + \
          ", ".join(f"{b:.2f}" for b in betas) + "\n\n" + \
          "\n".join("  ".join(f"{c:>4s}" for c in row) for row in grid)
    ax[1].text(0.05, 0.5, txt, family="monospace", fontsize=10, va="center")
    fig.tight_layout()
    out = __file__.replace(".py", ".png")
    fig.savefig(out, dpi=130)
    print(f"figure -> {out}")


if __name__ == "__main__":
    main()
