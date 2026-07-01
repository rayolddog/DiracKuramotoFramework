"""
weyl3d_emergence.py — Genuine 3+1D chiral fermions and the L↔R Dirac mass
as a sync coupling, from a 3D phase-oscillator substrate
==========================================================================

THE UPGRADE (from code/honeycomb_emergence.py):
─────────────────────────────────────────────────────────────────────────
The 2D honeycomb gave Dirac cones, but in 2+1D there is no real γ⁵ — the two
"valleys" were only a chirality PROXY, and the L↔R Dirac mass had to be faked
as inter-valley scattering. In 3D the story becomes honest: the two
chiralities are GENUINE Weyl nodes separated in momentum, and the Dirac mass
is a real off-diagonal L↔R coupling. This is the lattice realisation of
"Two Regimes of the Chiral Mass Coupling."

MODEL — 4-band Wilson–Dirac on a cubic lattice, written in the CHIRAL basis
(τ = L/R chirality, σ = spin):

  H(k) = (σ·s(k)) τ_z  +  M_W(k) τ_x  +  b σ_z
         └────────────┘   └────────┘    └────┘
         two counter-chiral   L↔R Dirac    axial field that
         Weyl fermions        mass (sync   SEPARATES L,R in
         (τ_z=+ is L,         coupling)    momentum (k_z = ±b)
          τ_z=− is R)

  s_j(k) = sin k_j ,   M_W(k) = M + r Σ_j (1 − cos k_j)   (Wilson term)

SUBSTRATE  ⟷  EMERGENT DICTIONARY:
─────────────────────────────────────────────────────────────────────────
  kinetic  τ_z σ·s     ⟷  two Weyl oscillators of OPPOSITE chirality
  Dirac mass  M τ_x    ⟷  the L↔R sync coupling, m(ψ̄_L ψ_R + ψ̄_R ψ_L),
                          OFF-DIAGONAL in chirality (the headline claim)
  axial field b σ_z    ⟷  background that pulls L and R apart in k-space
  Wilson term  r       ⟷  momentum-dependent L↔R coupling that gaps the
                          zone-boundary DOUBLERS (Nielsen–Ninomiya fix)

THE THREE THINGS THIS DEMONSTRATES (numerically):
─────────────────────────────────────────────────────────────────────────
 (1) GENUINE CHIRALITY. With b≠0, M=0 the two Weyl nodes sit at k_z = ±k*,
     opposite Berry-monopole charge → real L and R (panels A, C).
 (2) MASS = L↔R COUPLING, AND IT NEEDS BOTH CHIRALITIES. The Dirac mass M
     gaps the fermion ONLY by coupling L to R, and ONLY when |M| > |b|
     (when the L↔R coupling beats the axial separation). A single isolated
     Weyl node can NEVER be gapped — chiral protection (panels B, E, F).
 (3) FERMION DOUBLING + ITS FIX. The naive (r=0) lattice fermion has 2³ = 8
     Weyl doublers at the BZ corners; the Wilson L↔R term r lifts 7 of them,
     leaving ONE physical Dirac fermion at Γ (panel D).

HONEST SCOPE (carried over):
─────────────────────────────────────────────────────────────────────────
  Statistics are still bosonic: this is the Dirac EQUATION/spinor/mass/
  chirality as a classical field theory. Fermionic Pauli exclusion needs the
  separate statistics-generating step (flux attachment / Wess–Zumino). What
  the 3D upgrade BUYS is point (2) above being literal, not analogy.
  See [[project_emergent_fields_substrate]].

Run:  MPLBACKEND=Agg python code/weyl3d_emergence.py
Deps: numpy, matplotlib
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Pauli matrices and the 4x4 chiral-basis building blocks
# ----------------------------------------------------------------------------
s0 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(a, b):
    return np.kron(a, b)


# Gamma-like 4x4 operators in the chiral basis (τ ⊗ σ)
G_KIN = [kron(sz, sx), kron(sz, sy), kron(sz, sz)]   # τ_z σ_j  (kinetic)
G_MASS = kron(sx, s0)                                # τ_x      (L↔R Dirac mass)
G_AXIAL = kron(s0, sz)                               # σ_z      (axial field)

R_WILSON = 1.0   # Wilson parameter r


def hamiltonian(kx, ky, kz, M=0.0, b=0.0, r=R_WILSON):
    """4x4 Wilson–Dirac Bloch Hamiltonian at a single k-point."""
    s = [np.sin(kx), np.sin(ky), np.sin(kz)]
    Mw = M + r * (3 - np.cos(kx) - np.cos(ky) - np.cos(kz))
    H = Mw * G_MASS + b * G_AXIAL
    for sj, Gj in zip(s, G_KIN):
        H = H + sj * Gj
    return H


def ham_grid(KX, KY, KZ, M=0.0, b=0.0, r=R_WILSON):
    """Vectorised 4x4 Hamiltonian over an array of k-points -> (...,4,4)."""
    shp = np.broadcast(KX, KY, KZ).shape
    s = [np.sin(KX) * np.ones(shp), np.sin(KY) * np.ones(shp),
         np.sin(KZ) * np.ones(shp)]
    Mw = M + r * (3 - np.cos(KX) - np.cos(KY) - np.cos(KZ))
    H = Mw[..., None, None] * G_MASS + b * G_AXIAL
    for sj, Gj in zip(s, G_KIN):
        H = H + sj[..., None, None] * Gj
    return H


def bands_line(kz, kx=0.0, ky=0.0, M=0.0, b=0.0, r=R_WILSON):
    """Sorted eigenvalues along a k_z line -> (len(kz), 4)."""
    KZ = np.asarray(kz)
    H = ham_grid(np.full_like(KZ, kx), np.full_like(KZ, ky), KZ, M, b, r)
    return np.linalg.eigvalsh(H)


# ----------------------------------------------------------------------------
# Multiband (non-abelian) Chern number of a 2D (kx,ky) slice at fixed kz
# ----------------------------------------------------------------------------
def chern_slice(kz, M=0.0, b=0.0, r=R_WILSON, n=22):
    """Chern number of the 2 occupied (lowest) bands over a (kx,ky) BZ slice."""
    k = (np.arange(n)) * 2 * np.pi / n - np.pi
    KX, KY = np.meshgrid(k, k, indexing="ij")
    H = ham_grid(KX, KY, np.full_like(KX, kz), M, b, r)
    _, vecs = np.linalg.eigh(H)
    occ = vecs[..., :, :2]                      # (n,n,4,2) occupied frame

    def link(arr, axis):
        ov = np.einsum("...ca,...cb->...ab", np.conj(arr),
                       np.roll(arr, -1, axis=axis))
        d = np.linalg.det(ov)
        return d / np.abs(d)

    Ux, Uy = link(occ, 0), link(occ, 1)
    F = np.angle(Ux * np.roll(Uy, -1, axis=0) /
                 (np.roll(Ux, -1, axis=1) * Uy))
    return int(np.rint(F.sum() / (2 * np.pi)))


# On the line kx=ky=0, σ_z is a good quantum number, so the four bands are
# exactly ±b ± √Q(k_z) with Q = sin²k_z + (M + r(1−cos k_z))².  The middle gap
# is 2|b − √Q|, which we can evaluate analytically (no grid-miss artifact at
# the node, unlike sampling the eigenvalues).
def _sqrtQ(kz, M, b, r):
    return np.sqrt(np.sin(kz) ** 2 + (M + r * (1 - np.cos(kz))) ** 2)


def min_gap_nodal_line(M, b, r=R_WILSON, n=4000):
    """Exact smallest gap along kx=ky=0 (0 ⇒ gapless Weyl semimetal)."""
    kz = np.linspace(-np.pi, np.pi, n)
    d = _sqrtQ(kz, M, b, r) - b
    if d.min() < 0.0 < d.max():                  # √Q crosses b ⇒ true node
        return 0.0
    return float(2 * np.min(np.abs(d)))


def find_nodes(M, b, r=R_WILSON, n=8000):
    """Positive-k_z Weyl-node positions on the line kx=ky=0 (empty if gapped)."""
    kz = np.linspace(0.0, np.pi, n)
    d = _sqrtQ(kz, M, b, r) - b
    sign = np.where(np.diff(np.sign(d)))[0]
    return [0.5 * (kz[i] + kz[i + 1]) for i in sign]


# ============================================================================
# FIGURE
# ============================================================================
def main():
    fig, ax = plt.subplots(2, 3, figsize=(16.5, 9.6))
    fig.suptitle("Genuine 3+1D chiral fermions and the L↔R Dirac mass as a "
                 "sync coupling, from a 3D phase-oscillator substrate",
                 fontsize=14, fontweight="bold")

    B0 = 0.6          # axial field for the Weyl-semimetal panels
    kz = np.linspace(-np.pi, np.pi, 600)

    # ---- Panel A: two separated Weyl nodes = genuine L and R --------------
    a = ax[0, 0]
    E = bands_line(kz, M=0.0, b=B0)
    for c in range(4):
        a.plot(kz, E[:, c], color="#1f77b4", lw=1.4)
    kstar = find_nodes(0.0, B0)[0]               # exact node position
    for ks, lab, col in [(+kstar, "L  (χ=+1)", "#d62728"),
                         (-kstar, "R  (χ=−1)", "#2ca02c")]:
        a.plot(ks, 0, "o", ms=9, mfc="none", mec=col, mew=2)
        a.annotate(lab, (ks, 0), color=col, fontsize=10, fontweight="bold",
                   xytext=(8, 10), textcoords="offset points")
    a.axhline(0, color="gray", lw=0.5)
    a.set_title("(A) Axial field b=0.6, mass M=0: TWO Weyl nodes\n"
                "separated in $k_z$ → genuine separated L and R")
    a.set_xlabel("$k_z$  (at $k_x=k_y=0$)"); a.set_ylabel("energy")
    a.set_xticks([-np.pi, 0, np.pi]); a.set_xticklabels(["$-\\pi$", "0", "$\\pi$"])

    # ---- Panel B: L↔R mass gaps them, but only when |M| > |b| ------------
    a = ax[0, 1]
    kzz = np.linspace(-1.6, 1.6, 500)
    for Mv, col in [(0.0, "#999999"), (0.4, "#ff7f0e"), (0.8, "#8e44ad")]:
        Eb = bands_line(kzz, M=Mv, b=B0)
        a.plot(kzz, Eb[:, 1], color=col, lw=1.6)
        tag = "Weyl semimetal" if Mv < B0 else "gapped Dirac"
        a.plot(kzz, Eb[:, 2], color=col, lw=1.6,
               label=fr"$M={Mv:.1f}$  ({tag})")
    a.axhline(0, color="gray", lw=0.5)
    a.set_title("(B) Ramp the L↔R Dirac mass $M$ (b=0.6):\n"
                "gap opens only once $|M|>|b|$ (coupling beats separation)")
    a.set_xlabel("$k_z$"); a.set_ylabel("energy")
    a.legend(fontsize=8, loc="upper center")

    # ---- Panel C: Chern of (kx,ky) slices jumps ±1 across each node -------
    a = ax[0, 2]
    kz_slices = np.linspace(-np.pi, np.pi, 61)
    Cs = np.array([chern_slice(kzv, M=0.0, b=B0, n=22) for kzv in kz_slices])
    a.step(kz_slices, Cs, where="mid", color="#1f77b4", lw=2)
    a.fill_between(kz_slices, 0, Cs, step="mid", alpha=0.15, color="#1f77b4")
    for ks, col in [(+kstar, "#d62728"), (-kstar, "#2ca02c")]:
        a.axvline(ks, color=col, ls=":", lw=1.4)
    a.set_title("(C) Chern number $C(k_z)$ of 2D slices\n"
                "jumps ±1 AT each node → opposite Berry monopoles")
    a.set_xlabel("$k_z$"); a.set_ylabel("slice Chern $C(k_z)$")
    a.set_xticks([-np.pi, 0, np.pi]); a.set_xticklabels(["$-\\pi$", "0", "$\\pi$"])
    a.set_yticks([-1, 0, 1]); a.set_ylim(-1.6, 1.6)

    # ---- Panel D: fermion doubling and the Wilson fix --------------------
    a = ax[0, 0]  # placeholder, reassigned below
    a = ax[1, 0]
    rs = np.linspace(0, 1.2, 80)
    trims = {
        "Γ (0,0,0)": (0, 0, 0),
        "(π,0,0)×3": (np.pi, 0, 0),
        "(π,π,0)×3": (np.pi, np.pi, 0),
        "(π,π,π)": (np.pi, np.pi, np.pi),
    }
    cols = ["#000000", "#d62728", "#1f77b4", "#2ca02c"]
    for (lab, (kx, ky, kz0)), col in zip(trims.items(), cols):
        gaps = []
        for rv in rs:
            H = hamiltonian(kx, ky, kz0, M=0.0, b=0.0, r=rv)
            ev = np.linalg.eigvalsh(H)
            gaps.append(ev[2] - ev[1])
        a.plot(rs, gaps, color=col, lw=1.8, label=lab)
    a.set_title("(D) Nielsen–Ninomiya: 8 doublers at $r=0$;\n"
                "Wilson L↔R term $r$ gaps all but Γ → one Dirac fermion")
    a.set_xlabel("Wilson parameter $r$"); a.set_ylabel("gap at BZ corner")
    a.legend(fontsize=8, loc="upper left")

    # ---- Panel E: phase diagram in (M, b): WSM vs gapped Dirac -----------
    a = ax[1, 1]
    Ms = np.linspace(-1.2, 1.2, 121)
    bs = np.linspace(0.0, 1.2, 121)
    MM, BB = np.meshgrid(Ms, bs, indexing="ij")
    GAP = np.zeros_like(MM)
    for i in range(MM.shape[0]):
        for j in range(MM.shape[1]):
            GAP[i, j] = min_gap_nodal_line(MM[i, j], BB[i, j])
    pc = a.pcolormesh(Ms, bs, GAP.T, cmap="magma", shading="auto")
    a.plot(Ms, np.abs(Ms), "w--", lw=1.5)           # boundary |M| = |b|
    a.text(0.0, 0.9, "Weyl\nsemimetal", color="w", ha="center",
           fontsize=10, fontweight="bold")
    a.text(0.85, 0.25, "gapped\nDirac", color="w", ha="center", fontsize=9)
    a.set_title("(E) Phase diagram: $|M|<|b|$ Weyl semimetal,\n"
                "$|M|>|b|$ gapped Dirac (L↔R coupling wins)")
    a.set_xlabel("L↔R Dirac mass $M$"); a.set_ylabel("axial field $b$")
    fig.colorbar(pc, ax=a, fraction=0.046, label="min gap")

    # ---- Panel F: node positions merge & annihilate at |M|=|b| -----------
    a = ax[1, 2]
    Mm = np.linspace(0, 1.0, 300)
    kpos = np.array([(find_nodes(m, B0)[0] if find_nodes(m, B0) else np.nan)
                     for m in Mm])
    a.plot(Mm, kpos, color="#d62728", lw=2, label="L node $k_z^+$")
    a.plot(Mm, -kpos, color="#2ca02c", lw=2, label="R node $k_z^-$")
    a.axvline(B0, color="gray", ls=":", lw=1.4)
    a.annotate("nodes meet &\nannihilate at $M=b$", (B0, 0.05),
               fontsize=9, ha="right", color="gray")
    a.fill_betweenx([0, 1.2], B0, 1.0, color="0.85", alpha=0.6)
    a.text(0.82, 1.0, "gapped", fontsize=9, color="0.4")
    a.set_title("(F) Δ=node separation vs mass (b=0.6):\n"
                "single isolated node is UNCUTTABLE — mass needs the pair")
    a.set_xlabel("L↔R Dirac mass $M$"); a.set_ylabel("node position $|k_z^*|$")
    a.set_ylim(-0.2, 1.2); a.legend(fontsize=8, loc="upper right")

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out = "code/weyl3d_emergence.png"
    fig.savefig(out, dpi=140)
    print(f"[saved] {out}")

    # ------------------------------------------------------------------ stdout
    print("\n" + "=" * 70)
    print("GENUINE 3+1D CHIRAL FERMIONS FROM A 3D PHASE SUBSTRATE")
    print("=" * 70)
    print(f"  Weyl nodes at b={B0}, M=0 : k_z = ±{kstar:.3f}  "
          f"(Wilson-shifted from ±arcsin b)")
    print("  Chern of slice between nodes (k_z=0)   : "
          f"C = {chern_slice(0.0, 0.0, B0):+d}   (2D QH layer)")
    print("  Chern of slice outside nodes (k_z=π)   : "
          f"C = {chern_slice(np.pi, 0.0, B0):+d}   (trivial)")
    print("  → the ±1 jump IS the opposite chirality of L and R")
    print("-" * 70)
    print("  L↔R Dirac mass vs axial field  (b = 0.6):")
    for Mv in [0.0, 0.4, 0.6, 0.8]:
        g = min_gap_nodal_line(Mv, B0)
        phase = "Weyl semimetal (gapless)" if g < 1e-3 else "gapped Dirac"
        print(f"    M = {Mv:.1f} :  min gap = {g:6.3f}   {phase}")
    print("  → mass gaps the fermion ONLY for |M| > |b|: the L↔R coupling")
    print("    must overcome the chiral separation. A lone Weyl node cannot")
    print("    be gapped at all (chiral protection).")
    print("-" * 70)
    print("  Fermion doubling (r = 0, M = 0): gaps at the 8 BZ corners")
    for lab, (kx, ky, kz0) in {
            "Γ": (0, 0, 0), "(π,0,0)": (np.pi, 0, 0),
            "(π,π,0)": (np.pi, np.pi, 0), "(π,π,π)": (np.pi, np.pi, np.pi)}.items():
        ev0 = np.linalg.eigvalsh(hamiltonian(kx, ky, kz0, 0, 0, r=0.0))
        ev1 = np.linalg.eigvalsh(hamiltonian(kx, ky, kz0, 0, 0, r=1.0))
        print(f"    {lab:9s}: r=0 gap {ev0[2]-ev0[1]:.2f}  →  "
              f"r=1 gap {ev1[2]-ev1[1]:.2f}")
    print("  → Wilson r leaves only Γ light: ONE physical Dirac fermion.")
    print("=" * 70)
    print("CAVEAT (honest): statistics still bosonic — Pauli needs the")
    print("separate flux-attachment / Wess–Zumino step. What 3D BUYS is that")
    print("L↔R chirality and the mass-as-coupling are now LITERAL, not proxy.")


if __name__ == "__main__":
    main()
