"""
honeycomb_emergence.py — Emergent chiral fermions, mass, and a topological
gauge response from a single phase-oscillator substrate
==========================================================================

CENTRAL CLAIM (the "field multiplicity from substrate dynamics" sketch):
─────────────────────────────────────────────────────────────────────────
Put ONE phase oscillator on every site of a honeycomb lattice (two
sublattices A, B) with inertial Kuramoto / Josephson-array dynamics

    m θ̈_i + γ θ̇_i = ω_i − K Σ_j sin(θ_i − θ_j + α_ij) − κ_i sin(θ_i).

Linearize the fluctuations about the synchronized background. The envelope
of the phase-fluctuation field obeys, near the two Brillouin-zone corners
K and K', the (2+1)D Weyl equation

    i ∂_t χ = c σ·p̂ χ,     c = (v/2)√(K/3m),

with NO chirality put in by hand. The two BZ corners wind oppositely → they
ARE the two chiralities (L, R). This script DERIVES and VISUALIZES that, plus
the two ways to give the emergent fermion a mass and the topological gauge
response that one of them generates.

SUBSTRATE  ⟷  EMERGENT (graphene/Haldane) DICTIONARY:
─────────────────────────────────────────────────────────────────────────
    Kuramoto coupling          K        ⟷   nearest-neighbour hopping   t
    sublattice pinning split   κ_A−κ_B  ⟷   Semenoff mass               2Δ
    Sakaguchi phase-lag        α        ⟷   Haldane flux phase          φ
    next-nearest sync          —        ⟷   NNN hopping                 t₂
    inertia / coupling         m, K     ⟷   emergent light-speed        c

CORRECTION / SCOPE NOTE (2026-07-05): this script studies the target Bloch
Hamiltonian (Haldane model with φ = α) written from the dictionary — it does
NOT linearize the oscillator equations. The honest linearization is done in
stuartlandau_haldane_check.py, with three qualifications derived there:
(1) NO phase-only model (first-order or inertial) carries the flux at linear
order — the coupling linearizes to a real symmetric cos α-weighted Laplacian;
the flux lives in the limit-cycle (amplitude+phase, Stuart–Landau)
linearization, whose particle-conserving block is exactly the H(k) below;
(2) the lag pattern must be ANTISYMMETRIC (α_ij = −α_ji, Haldane orientation
= a DMI in magnet language); (3) the coupling needs a REACTIVE component —
purely dissipative coupling obeys an exact no-go (particle-hole shadow band
restores the K-point degeneracy). See
drafts/DERIVATION_lag_flux_linearization.md.

WHAT EACH MASS MEANS:
─────────────────────────────────────────────────────────────────────────
  • Semenoff  (Δ ≠ 0, φ = 0): sublattice A/B pinning asymmetry. Opens the
    SAME-sign gap at both valleys → a TRIVIAL insulator (Chern C = 0). This
    is the parity-type Dirac mass m ψ̄ψ of the 2+1D toy.
  • Haldane   (φ ≠ 0): the Sakaguchi phase-lag IS a magnetic flux (a complex
    Peierls hopping te^{iα}). Arranged with zero net flux per cell but broken
    time-reversal, it opens OPPOSITE-sign gaps at K and K' → a Chern insulator
    (C = ±1) with a quantized Hall response = emergent U(1) gauge response.

The Berry curvature / Chern number are properties of the Bloch eigenVECTORS,
so they are identical whether the carrier dynamics is first- or second-order
in time — the topology does not care about the ω-vs-ω² dispersion mapping.

HONEST SCOPE (stated in PAPER terms, not hidden):
─────────────────────────────────────────────────────────────────────────
  (1) This produces the Dirac EQUATION, spinor, chirality, mass and gauge
      coupling as a CLASSICAL/bosonic field theory. Fermionic STATISTICS
      (Pauli) needs one more ingredient — flux attachment using exactly the
      Berry curvature generated here, or a soliton+Wess–Zumino construction.
  (2) Strict 2+1D has no γ⁵ chirality; the clean L↔R Dirac mass of 3+1D maps
      here onto an inter-valley (K↔K') coupling. The honeycomb is the 2D
      pedagogical shadow of a 3D Weyl-semimetal lattice, which is the real
      target. See the chat derivation / REVISION_OUTLINE.

Run:  MPLBACKEND=Agg python code/honeycomb_emergence.py
Deps: numpy, matplotlib
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Lattice geometry (nearest-neighbour distance a = 1)
# ----------------------------------------------------------------------------
SQ3 = np.sqrt(3.0)

# A→B nearest-neighbour vectors
DELTA = np.array([[1.0, 0.0],
                  [-0.5, SQ3 / 2],
                  [-0.5, -SQ3 / 2]])

# same-sublattice next-nearest-neighbour vectors (Σ b_i = 0)
BVEC = np.array([[0.0, SQ3],
                 [-1.5, -SQ3 / 2],
                 [1.5, -SQ3 / 2]])

# reciprocal primitive vectors (a_i · g_j = 2π δ_ij)
G1 = 2 * np.pi * np.array([1.0 / 3.0, -1.0 / SQ3])
G2 = 2 * np.pi * np.array([1.0 / 3.0, 1.0 / SQ3])

# Dirac points in reduced (k1,k2) coords -> Cartesian
K_PT = (1 / 3) * G1 + (2 / 3) * G2       # valley K   = (2π/3,  2π/3√3)
KP_PT = (2 / 3) * G1 + (1 / 3) * G2      # valley K'  = (2π/3, -2π/3√3)

T = 1.0          # nearest-neighbour Kuramoto coupling K  (sets the cone)
T2 = 0.10        # next-nearest sync strength  t₂
VF = 1.5 * T     # Dirac slope  v_F = 3 t a / 2  (emergent "speed of light")


# ----------------------------------------------------------------------------
# Bloch Hamiltonian  H(k) = ε(k) 1 + d(k)·σ   (sublattice pseudospin)
# ----------------------------------------------------------------------------
def d_vector(kx, ky, delta=0.0, phi=0.0):
    """Return (d_x, d_y, d_z) and the identity part ε for the Haldane model.

    delta = Semenoff mass Δ  (sublattice pinning asymmetry, κ_A−κ_B)/…
    phi   = Sakaguchi/Haldane flux α
    Works on scalars or broadcast arrays of kx, ky.
    """
    kx = np.asarray(kx)
    ky = np.asarray(ky)
    kdotd = kx[..., None] * DELTA[:, 0] + ky[..., None] * DELTA[:, 1]
    kdotb = kx[..., None] * BVEC[:, 0] + ky[..., None] * BVEC[:, 1]

    dx = -T * np.cos(kdotd).sum(-1)
    dy = T * np.sin(kdotd).sum(-1)
    dz = delta - 2 * T2 * np.sin(phi) * np.sin(kdotb).sum(-1)
    eps = -2 * T2 * np.cos(phi) * np.cos(kdotb).sum(-1)
    return dx, dy, dz, eps


def bands(kx, ky, delta=0.0, phi=0.0):
    dx, dy, dz, eps = d_vector(kx, ky, delta, phi)
    dnorm = np.sqrt(dx**2 + dy**2 + dz**2)
    return eps - dnorm, eps + dnorm     # lower, upper


def min_gap(delta=0.0, phi=0.0):
    """Smallest direct band gap (0 ⇒ gapless ⇒ Chern number undefined).

    In this model the gap only ever closes at the two Dirac points K, K'
    (the masses gap exactly there), so evaluate it there exactly rather than
    on an offset BZ grid that never lands on the corner.
    """
    gaps = []
    for P in (K_PT, KP_PT):
        dx, dy, dz, _ = d_vector(P[0], P[1], delta, phi)
        gaps.append(2 * np.sqrt(dx**2 + dy**2 + dz**2))
    return float(min(gaps))


# ----------------------------------------------------------------------------
# Chern number via Fukui–Hatsugai–Suzuki (gauge-invariant lattice method)
# ----------------------------------------------------------------------------
def chern_number(delta, phi, n=24):
    """Integer Chern number of the lower band over one BZ (reduced grid)."""
    s = (np.arange(n) + 0.5) / n
    k1, k2 = np.meshgrid(s, s, indexing="ij")
    kx = k1 * G1[0] + k2 * G2[0]
    ky = k1 * G1[1] + k2 * G2[1]

    dx, dy, dz, _ = d_vector(kx, ky, delta, phi)
    H = np.empty((n, n, 2, 2), dtype=complex)
    H[..., 0, 0] = dz
    H[..., 1, 1] = -dz
    H[..., 0, 1] = dx - 1j * dy
    H[..., 1, 0] = dx + 1j * dy
    _, vecs = np.linalg.eigh(H)
    u = vecs[..., :, 0]                 # lower-band eigenvector field

    def link(arr, axis):
        ov = np.sum(np.conj(arr) * np.roll(arr, -1, axis=axis), axis=-1)
        return ov / np.abs(ov)

    U1 = link(u, 0)
    U2 = link(u, 1)
    F = np.angle(U1 * np.roll(U2, -1, axis=0) /
                 (np.roll(U1, -1, axis=1) * U2))
    return int(np.rint(F.sum() / (2 * np.pi)))


def berry_curvature_field(delta, phi, n=80):
    """Berry-curvature density of the lower band over the BZ (for plotting)."""
    s = (np.arange(n) + 0.5) / n
    k1, k2 = np.meshgrid(s, s, indexing="ij")
    kx = k1 * G1[0] + k2 * G2[0]
    ky = k1 * G1[1] + k2 * G2[1]
    dx, dy, dz, _ = d_vector(kx, ky, delta, phi)
    H = np.empty((n, n, 2, 2), dtype=complex)
    H[..., 0, 0] = dz
    H[..., 1, 1] = -dz
    H[..., 0, 1] = dx - 1j * dy
    H[..., 1, 0] = dx + 1j * dy
    _, vecs = np.linalg.eigh(H)
    u = vecs[..., :, 0]

    def link(arr, axis):
        ov = np.sum(np.conj(arr) * np.roll(arr, -1, axis=axis), axis=-1)
        return ov / np.abs(ov)

    U1, U2 = link(u, 0), link(u, 1)
    F = np.angle(U1 * np.roll(U2, -1, axis=0) /
                 (np.roll(U1, -1, axis=1) * U2))
    return kx, ky, F * n * n / (2 * np.pi)     # density normalised per BZ area-ish


# ============================================================================
# FIGURE
# ============================================================================
def main():
    fig, ax = plt.subplots(2, 3, figsize=(16.5, 9.6))
    fig.suptitle("Emergent chiral fermions, mass, and a topological gauge "
                 "response from one honeycomb phase-oscillator substrate",
                 fontsize=14, fontweight="bold")

    # ---- Panel A: massless band gap over the BZ -> two Dirac cones ---------
    ng = 300
    kxr = np.linspace(-2 * np.pi / 3 * 1.6, 2 * np.pi / 3 * 1.6, ng)
    kyr = np.linspace(-np.pi / SQ3 * 1.7, np.pi / SQ3 * 1.7, ng)
    KX, KY = np.meshgrid(kxr, kyr)
    lo, hi = bands(KX, KY, delta=0.0, phi=0.0)
    gap = hi - lo
    a = ax[0, 0]
    pc = a.pcolormesh(KX, KY, gap, cmap="viridis", shading="auto")
    for P, lab in [(K_PT, "K"), (KP_PT, "K'")]:
        a.plot(*P, "o", ms=8, mfc="none", mec="w", mew=1.8)
        a.annotate(lab, P, color="w", fontsize=12, fontweight="bold",
                   xytext=(6, 6), textcoords="offset points")
    a.set_title("(A) Massless substrate: band gap 2|d(k)|\n"
                "→ degeneracies (cones) at the 2 inequivalent corners")
    a.set_xlabel("$k_x$"); a.set_ylabel("$k_y$")
    a.set_aspect("equal")
    fig.colorbar(pc, ax=a, fraction=0.046, label="gap")

    # ---- Panel B: cone zoom -> emergent linear dispersion / light-speed ----
    a = ax[0, 1]
    q = np.linspace(-0.6, 0.6, 400)
    ky_line = K_PT[1] + q
    kx_line = np.full_like(q, K_PT[0])
    lo, hi = bands(kx_line, ky_line, delta=0.0, phi=0.0)
    a.plot(q, lo, lw=2, color="#1f77b4")
    a.plot(q, hi, lw=2, color="#d62728")
    a.plot(q, VF * np.abs(q), "k--", lw=1, label=fr"slope $v_F=\frac{{3}}{{2}}ta={VF:.2f}$")
    a.plot(q, -VF * np.abs(q), "k--", lw=1)
    a.axvline(0, color="gray", lw=0.6)
    a.set_title("(B) Zoom on valley K: linear cone\n"
                "→ emergent Lorentz cone, $c=\\frac{v}{2}\\sqrt{K/3m}$")
    a.set_xlabel("$q_y$  (from K)"); a.set_ylabel("envelope energy $\\mathcal{E}$")
    a.legend(loc="upper center", fontsize=9)

    # ---- Panel C: Semenoff mass — sublattice pinning asymmetry opens gap ---
    a = ax[0, 2]
    ky_cut = np.linspace(-np.pi / SQ3 * 1.4, np.pi / SQ3 * 1.4, 600)
    kx_cut = np.full_like(ky_cut, 2 * np.pi / 3)   # vertical cut through K' and K
    for dval, col in [(0.0, "#999999"), (0.20, "#ff7f0e"), (0.45, "#8e44ad")]:
        lo, hi = bands(kx_cut, ky_cut, delta=dval, phi=0.0)
        a.plot(ky_cut, lo, color=col, lw=1.8)
        a.plot(ky_cut, hi, color=col, lw=1.8,
               label=fr"$\Delta={dval:.2f}$  (gap $=2\Delta$, $C=0$)")
    for yv, lab in [(K_PT[1], "K"), (KP_PT[1], "K'")]:
        a.axvline(yv, color="k", lw=0.5, ls=":")
        a.annotate(lab, (yv, 3.0), ha="center", fontsize=10)
    a.set_title("(C) Semenoff mass $\\Delta$ (κ$_A$≠κ$_B$):\n"
                "same-sign gap at both valleys → TRIVIAL")
    a.set_xlabel("$k_y$  (cut at $k_x=2\\pi/3$)"); a.set_ylabel("energy")
    a.legend(fontsize=8, loc="lower right")

    # ---- Panel D: Berry curvature in the topological phase ----------------
    a = ax[1, 0]
    kx_b, ky_b, Om = berry_curvature_field(delta=0.0, phi=np.pi / 2, n=90)
    vmax = np.percentile(np.abs(Om), 99.5)
    pc = a.pcolormesh(kx_b, ky_b, Om, cmap="RdBu_r",
                      vmin=-vmax, vmax=vmax, shading="auto")
    for P, lab in [(K_PT, "K"), (KP_PT, "K'")]:
        a.plot(*P, "o", ms=8, mfc="none", mec="k", mew=1.5)
        a.annotate(lab, P, fontsize=11, fontweight="bold",
                   xytext=(6, 6), textcoords="offset points")
    a.set_title("(D) Sakaguchi lag $\\alpha=\\pi/2$: Berry curvature\n"
                "OPPOSITE sign at K vs K' → quantized $U(1)$ response")
    a.set_xlabel("$k_x$"); a.set_ylabel("$k_y$")
    a.set_aspect("equal")
    fig.colorbar(pc, ax=a, fraction=0.046, label="$\\Omega(k)$")

    # ---- Panel E: Haldane phase diagram (numerical Chern number) ----------
    a = ax[1, 1]
    nphi, ndel = 49, 49
    phis = np.linspace(-np.pi, np.pi, nphi)
    dels = np.linspace(-6 * T2, 6 * T2, ndel)
    Cmap = np.zeros((ndel, nphi))
    for i, dv in enumerate(dels):
        for j, pv in enumerate(phis):
            Cmap[i, j] = chern_number(dv, pv, n=18)
    pc = a.pcolormesh(phis, dels / T2, Cmap, cmap="coolwarm",
                      vmin=-1, vmax=1, shading="auto")
    # analytic phase boundaries Δ = ± 3√3 t₂ sinφ
    a.plot(phis, 3 * SQ3 * np.sin(phis), "k-", lw=1.2)
    a.plot(phis, -3 * SQ3 * np.sin(phis), "k-", lw=1.2)
    a.set_title("(E) Haldane phase diagram (numerical $C$)\n"
                "topological lobes $|\\Delta|<3\\sqrt{3}\\,t_2|\\sin\\alpha|$")
    a.set_xlabel("Sakaguchi lag $\\alpha$"); a.set_ylabel("$\\Delta / t_2$")
    a.set_xticks([-np.pi, 0, np.pi]); a.set_xticklabels(["$-\\pi$", "0", "$\\pi$"])
    fig.colorbar(pc, ax=a, fraction=0.046, ticks=[-1, 0, 1], label="Chern $C$")

    # ---- Panel F: Chern number & valley masses vs the sync phase-lag ------
    a = ax[1, 2]
    phis2 = np.linspace(-np.pi, np.pi, 241)
    mK = np.array([d_vector(K_PT[0], K_PT[1], 0.0, p)[2] for p in phis2])
    mKp = np.array([d_vector(KP_PT[0], KP_PT[1], 0.0, p)[2] for p in phis2])
    Cs = np.array([chern_number(0.0, p, n=18) for p in phis2])
    a.plot(phis2, mK, color="#d62728", lw=2, label="mass at K")
    a.plot(phis2, mKp, color="#1f77b4", lw=2, label="mass at K'")
    a.axhline(0, color="gray", lw=0.6)
    a.fill_between(phis2, -2, 2, where=Cs > 0, color="#d62728", alpha=0.08)
    a.fill_between(phis2, -2, 2, where=Cs < 0, color="#1f77b4", alpha=0.08)
    a2 = a.twinx()
    a2.step(phis2, Cs, where="mid", color="k", lw=1.4, label="Chern $C$")
    a2.set_ylabel("Chern number $C$"); a2.set_ylim(-1.6, 1.6)
    a2.set_yticks([-1, 0, 1])
    a.set_ylim(-1.6, 1.6)
    a.set_title("(F) Δ=0: valley masses flip sign as α ramps\n"
                "→ $C$ jumps $0\\!\\to\\!\\pm1$ at each gap closing")
    a.set_xlabel("Sakaguchi lag $\\alpha$"); a.set_ylabel("valley Dirac mass")
    a.set_xticks([-np.pi, 0, np.pi]); a.set_xticklabels(["$-\\pi$", "0", "$\\pi$"])
    a.legend(loc="upper left", fontsize=8)

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    out = "code/honeycomb_emergence.png"
    fig.savefig(out, dpi=140)
    print(f"[saved] {out}")

    # ------------------------------------------------------------------ stdout
    print("\n" + "=" * 70)
    print("EMERGENT FIELD CONTENT FROM ONE HONEYCOMB PHASE SUBSTRATE")
    print("=" * 70)
    f_at_K = np.abs(np.exp(1j * (K_PT @ DELTA.T)).sum())
    print(f"  |f(K)| at the Dirac point          : {f_at_K:.2e}  (≈0 → cone)")
    print(f"  emergent Dirac slope  v_F = 3ta/2   : {VF:.3f}")
    print(f"  → these set the emergent light-speed c = v_F-rescaled by inertia")
    print("-" * 70)
    print("  Mass mechanism            (Δ, α)        Chern C    phase")
    print("-" * 70)
    cases = [
        ("massless",            0.00, 0.00),
        ("Semenoff (sublatt.)", 0.30, 0.00),
        ("Haldane (sync-lag)",  0.00, np.pi / 2),
        ("Haldane −α",          0.00, -np.pi / 2),
        ("Δ dominates Haldane",  0.60, np.pi / 2),
    ]
    for name, dv, pv in cases:
        g = min_gap(dv, pv)
        if g < 1e-3:                       # gapless → Chern number undefined
            print(f"  {name:22s} ({dv:+.2f}, {pv:+.2f})    C = (n/a)  "
                  f"Dirac semimetal (gapless)")
            continue
        C = chern_number(dv, pv, n=24)
        phase = "Chern insulator" if C != 0 else "trivial insulator"
        print(f"  {name:22s} ({dv:+.2f}, {pv:+.2f})    C = {C:+d}    {phase}")
    print("-" * 70)
    print("  Semenoff Δ  → trivial gap (C=0) : parity-type Dirac mass mψ̄ψ")
    print("  Sakaguchi α → C=±1, sign(α)     : topological mass = emergent")
    print("                                    U(1) gauge response")
    print("  Crossover at |Δ| = 3√3 t₂|sinα| = "
          f"{3*SQ3*T2:.3f} at α=π/2")
    print("=" * 70)
    print("CAVEATS (honest): (1) statistics still bosonic — needs flux")
    print("attachment / WZ to become fermionic. (2) true L↔R chirality wants")
    print("the 3D Weyl-semimetal upgrade; valley here is the γ⁵ proxy.")


if __name__ == "__main__":
    main()
