"""
entangled_pair_two_stage.py
---------------------------

Schematic illustration of the two-stage measurement of an entangled photon
pair, in the Many Clocks / Dirac-Kuramoto framework (Paper §3.4).

Layout, left to right:
  * Detector A (bulk, polarizer angle a, bulk phase Φ_bulk^A)
  * Photon γ_A in flight (chiral clocks φ_L, φ_R, decoupled because K=0)
  * Creation event (synchronized chiral clocks: φ_A = φ_B)
  * Photon γ_B in flight (chiral clocks decoupled, K=0)
  * Detector B (bulk, polarizer angle b, bulk phase Φ_bulk^B)

At each detector, two stages are labelled:
  Stage 1 (pair-sync, K_pair = e|A_γ| ~ ℏω): γ ↔ bulk-bound electron e.
  Stage 2 (bulk relax, Γ_bulk = GM²/(ℏΔz)): e ↔ lattice; secondary radiation.

The cos²(θ/2) Bell visibility is built in Stage 1, because the bulk-bound
electron arrives carrying Φ_bulk (the polarizer's basis orientation) and the
photon (K=0) adopts that reference at the vertex.
"""

import numpy as np
from pathlib import Path
_HERE = Path(__file__).resolve().parent
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.lines import Line2D


def draw_clock(ax, x, y, phi, r=0.18, color="black", lw=1.4):
    """A small dial: circle + radial hand at angle phi."""
    ax.add_patch(Circle((x, y), r, fill=False, edgecolor=color, lw=lw))
    ax.plot([x, x + r * np.cos(phi)],
            [y, y + r * np.sin(phi)],
            color=color, lw=lw + 0.3)


def draw_spinor(ax, x, y, phi_L, phi_R, color, label=None, decoupled=False,
                K_label=None, scale=1.0):
    """Two chiral clocks side by side. If decoupled (m=0 photon), draw with a
    'broken' dotted link; otherwise draw a solid link to indicate L-R sync.

    A synchronized spinor has phi_L == phi_R (same hand direction). A
    decoupled photon has independent phi_L, phi_R."""
    r = 0.18 * scale
    dx = 0.28 * scale
    draw_clock(ax, x - dx, y, phi_L, r=r, color=color)
    draw_clock(ax, x + dx, y, phi_R, r=r, color=color)
    ax.text(x - dx, y - (r + 0.18) * scale, r"$\varphi_L$", ha="center",
            fontsize=8, color=color)
    ax.text(x + dx, y - (r + 0.18) * scale, r"$\varphi_R$", ha="center",
            fontsize=8, color=color)
    # link between L and R
    if decoupled:
        ax.plot([x - 0.10 * scale, x + 0.10 * scale], [y, y], color=color,
                lw=1.0, linestyle=":")
    else:
        ax.plot([x - 0.10 * scale, x + 0.10 * scale], [y, y],
                color=color, lw=1.8)
    # K label above
    if K_label is not None:
        ax.text(x, y + (r + 0.10) * scale, K_label, ha="center",
                fontsize=7, color=color, style="italic")
    if label is not None:
        ax.text(x, y - (r + 0.40) * scale, label, ha="center",
                fontsize=9, color=color, fontweight="bold")


def draw_detector(ax, cx, cy, color, polarizer_phi, name):
    """Bulk = many small atoms locked to a common Φ_bulk. A subset of
    the atoms is drawn as tiny synchronized clocks (with small angular
    jitter to convey realistic imperfect sync). The locked direction is
    shown with a thick central Φ_bulk arrow."""
    rng = np.random.default_rng(73 if cx < 0 else 91)

    # bulk atoms drawn as synchronized mini-clocks (no faceless discs).
    # Hands point ~along polarizer_phi with small Gaussian jitter
    # (sigma ~ 7 deg) to indicate realistic imperfect synchronization.
    n_clocks = 18
    placed = []
    attempts = 0
    while len(placed) < n_clocks and attempts < 800:
        attempts += 1
        dx, dy = rng.uniform(-0.82, 0.82), rng.uniform(-0.52, 0.52)
        # avoid the central Φ_bulk arrow region
        if dx * dx + dy * dy < 0.10:
            continue
        # avoid overlapping previously placed mini-clocks
        if any((dx - px) ** 2 + (dy - py) ** 2 < 0.062
               for (px, py) in placed):
            continue
        placed.append((dx, dy))

    for dx, dy in placed:
        phi = polarizer_phi + np.deg2rad(rng.normal(0.0, 7.0))
        rr = 0.072
        ax.add_patch(Circle((cx + dx, cy + dy), rr,
                            fill=False, edgecolor=color, lw=0.9))
        ax.plot([cx + dx, cx + dx + rr * np.cos(phi)],
                [cy + dy, cy + dy + rr * np.sin(phi)],
                color=color, lw=1.05)

    # bulk envelope
    ax.add_patch(FancyBboxPatch((cx - 0.95, cy - 0.65), 1.9, 1.3,
                                 boxstyle="round,pad=0.06",
                                 edgecolor=color, facecolor="none",
                                 lw=1.6, linestyle="--"))
    # bulk phase arrow (Φ_bulk)
    ax.annotate("", xy=(cx + 0.55 * np.cos(polarizer_phi),
                        cy + 0.55 * np.sin(polarizer_phi)),
                xytext=(cx, cy),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2.5))
    ax.text(cx + 0.86 * np.cos(polarizer_phi),
            cy + 0.86 * np.sin(polarizer_phi),
            r"$\Phi_{\rm bulk}$", color=color, fontsize=9,
            ha="center", va="center")
    # name + polarizer label
    ax.text(cx, cy - 1.05, name, ha="center", fontsize=10,
            fontweight="bold", color=color)


# --------------------------------------------------------------------- #
fig, ax = plt.subplots(figsize=(14, 7.2))
ax.set_xlim(-7.5, 7.5)
ax.set_ylim(-3.4, 3.6)
ax.set_aspect("equal")
ax.axis("off")

# title
ax.text(0, 3.25,
        "Two-Stage Measurement of a Polarization-Entangled Photon Pair",
        ha="center", fontsize=14, fontweight="bold")
ax.text(0, 2.85,
        "Many Clocks / Dirac–Kuramoto framework — §3.4",
        ha="center", fontsize=9, style="italic", color="gray")

# --------------- Source (creation point) ---------------
# small source bulk: synchronized mini-clocks (matching detector style)
src_rng = np.random.default_rng(5)
phi_src = np.deg2rad(70)
src_placed = []
src_attempts = 0
while len(src_placed) < 12 and src_attempts < 600:
    src_attempts += 1
    dx, dy = src_rng.uniform(-0.55, 0.55), src_rng.uniform(-0.42, 0.42)
    # avoid the central source spinor region
    if dx * dx + dy * dy < 0.13:
        continue
    if any((dx - px) ** 2 + (dy - py) ** 2 < 0.060
           for (px, py) in src_placed):
        continue
    src_placed.append((dx, dy))
for dx, dy in src_placed:
    phi_a = phi_src + np.deg2rad(src_rng.normal(0.0, 7.0))
    rr = 0.062
    ax.add_patch(Circle((dx, dy), rr, fill=False,
                        edgecolor="dimgray", lw=0.9))
    ax.plot([dx, dx + rr * np.cos(phi_a)],
            [dy, dy + rr * np.sin(phi_a)],
            color="dimgray", lw=1.0)
ax.add_patch(FancyBboxPatch((-0.7, -0.55), 1.4, 1.1,
                             boxstyle="round,pad=0.05",
                             edgecolor="dimgray", facecolor="none",
                             lw=1.4, linestyle="--"))
# synchronized chiral clocks INSIDE the source: phi_L = phi_R
draw_spinor(ax, 0, 0.05, phi_src, phi_src, color="dimgray",
            scale=0.85, K_label=r"$K=m$ (synced)")
# emission burst marker (gold star) just below the spinor
ax.scatter([0], [-0.78], s=320, marker="*",
           color="gold", edgecolors="black", lw=1.2, zorder=10)
ax.text(0, -1.18,
        "Source\n"
        r"$\varphi_A^{L,R}=\varphi_B^{L,R}$ at emission",
        ha="center", fontsize=8.5, va="top")

# worldlines (light cones in flat representation)
for sign, color in [(-1, "tab:blue"), (+1, "tab:red")]:
    ax.annotate("", xy=(sign * 4.5, 0.95), xytext=(sign * 0.7, 0.05),
                arrowprops=dict(arrowstyle="->", color=color, lw=2))

# --------------- In-flight photons (K=0, decoupled) ---------------
common_phi_L, common_phi_R = 0.45, 0.45 + np.pi / 2  # decoupled (K=0)
draw_spinor(ax, -2.7, 1.85, common_phi_L, common_phi_R,
            color="tab:blue", label=r"$\gamma_A$ in flight",
            decoupled=True, K_label=r"$K=0$")
draw_spinor(ax, 2.7, 1.85, common_phi_L, common_phi_R,
            color="tab:red", label=r"$\gamma_B$ in flight",
            decoupled=True, K_label=r"$K=0$")
ax.text(-2.7, 0.95, r"polarization preserved by free Maxwell",
        ha="center", fontsize=7.5, style="italic", color="tab:blue")
ax.text(2.7, 0.95, r"polarization preserved by free Maxwell",
        ha="center", fontsize=7.5, style="italic", color="tab:red")

# --------------- Detectors ---------------
# Bulk Φ_bulk is a TIME-phase, approximately universal across the source
# and both detectors (shared gravitational environment + environmental
# thermalization). Both detector bulks therefore lock to the same Φ as
# the source (~70°), with σ ≈ 7° jitter.
phi_bulk_universal = phi_src  # = 70°
draw_detector(ax, -5.7, 0.5, "tab:blue",
              polarizer_phi=phi_bulk_universal,
              name=r"Detector A bulk")
draw_detector(ax, 5.7, 0.5, "tab:red",
              polarizer_phi=phi_bulk_universal,
              name=r"Detector B bulk")

# bound-electron spinor at each detector: synchronized clocks oriented
# along the universal Phi_bulk direction (NOT the polarizer angle)
draw_spinor(ax, -5.7, 1.45, phi_bulk_universal, phi_bulk_universal,
            color="tab:blue", scale=0.85, label=r"bound $e^-$",
            K_label=r"$K=m$  locked to $\Phi_{\rm bulk}$")
draw_spinor(ax, 5.7, 1.45, phi_bulk_universal, phi_bulk_universal,
            color="tab:red", scale=0.85, label=r"bound $e^-$",
            K_label=r"$K=m$  locked to $\Phi_{\rm bulk}$")

# --------------- Polarizers (basis selectors) ---------------
# Polarizer = aperture circle with a double-headed transmission-axis
# arrow. The polarizer's mechanical orientation defines the measurement
# basis -- a direction in the photon's polarization Hilbert space, NOT
# in the chiral-clock phase. cos^2(theta/2) Bell visibility comes from
# the polarizer-axis difference (standard QED), not from Phi_bulk.
def draw_polarizer(ax, cx, cy, axis_phi, color, basis_label):
    r = 0.27
    ax.add_patch(Circle((cx, cy), r, fill=False,
                        edgecolor="black", lw=1.4))
    dxa, dya = r * 0.85 * np.cos(axis_phi), r * 0.85 * np.sin(axis_phi)
    ax.annotate("", xy=(cx + dxa, cy + dya),
                xytext=(cx - dxa, cy - dya),
                arrowprops=dict(arrowstyle="<|-|>", color=color,
                                lw=2.0, mutation_scale=12))
    ax.text(cx, cy + r + 0.18, basis_label, ha="center",
            fontsize=10, fontweight="bold", color=color)
    ax.text(cx, cy - r - 0.18, "polarizer", ha="center",
            fontsize=7, style="italic", color="black")


pol_a = np.deg2rad(35)
pol_b = np.deg2rad(110)
draw_polarizer(ax, -4.30, 0.85, pol_a, "tab:blue", r"basis $a$")
draw_polarizer(ax, 4.30, 0.85, pol_b, "tab:red", r"basis $b$")

# Stage 1 box (pair-sync) at each detector
def stage1_box(x_left, x_right, y, color):
    ax.add_patch(FancyBboxPatch((x_left, y - 0.30),
                                 x_right - x_left, 0.60,
                                 boxstyle="round,pad=0.04",
                                 edgecolor=color, facecolor="white",
                                 lw=1.0))
    ax.text((x_left + x_right) / 2, y,
            "Stage 1  $\\gamma\\leftrightarrow e$  pair-sync\n"
            r"$K_{\rm pair} = e\,|A_\gamma|\sim\hbar\omega$",
            ha="center", va="center", fontsize=8, color=color)


stage1_box(-5.45, -3.45, -1.45, "tab:blue")
stage1_box(3.45, 5.45, -1.45, "tab:red")

# Stage 2 box (bulk relax) below Stage 1
def stage2_box(x_left, x_right, y, color):
    ax.add_patch(FancyBboxPatch((x_left, y - 0.36),
                                 x_right - x_left, 0.72,
                                 boxstyle="round,pad=0.04",
                                 edgecolor=color, facecolor="white",
                                 lw=1.0, linestyle="--"))
    ax.text((x_left + x_right) / 2, y,
            "Stage 2  $e\\leftrightarrow$ bulk  relax\n"
            r"$\Gamma_{\rm bulk}=GM^2/(\hbar\Delta z)$"
            "\n(secondary radiation)",
            ha="center", va="center", fontsize=7.5, color=color)


stage2_box(-5.55, -3.35, -2.55, "tab:blue")
stage2_box(3.35, 5.55, -2.55, "tab:red")

# arrows from photon arrival → Stage 1, Stage 1 → Stage 2
for cx, color in [(-5.7, "tab:blue"), (5.7, "tab:red")]:
    ax.annotate("", xy=(cx + 0.45 * np.sign(cx), -1.15),
                xytext=(cx + 0.45 * np.sign(cx), -0.25),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.2))
    ax.annotate("", xy=(cx, -2.20), xytext=(cx, -1.75),
                arrowprops=dict(arrowstyle="->", color=color,
                                lw=1.2, linestyle="dashed"))

# Bell-correlation arc connecting the two detection events at the top
ax.annotate("", xy=(5.0, 2.45), xytext=(-5.0, 2.45),
            arrowprops=dict(arrowstyle="<->", color="purple",
                            lw=1.6, linestyle="--",
                            connectionstyle="arc3,rad=-0.15"))
ax.text(0, 2.55,
        r"Bell visibility  $\cos^2(\theta/2)$,  $\theta = a-b$  "
        r"(set by polarizer-axis difference; standard QED, "
        r"not by $\Phi_{\rm bulk}$)",
        ha="center", fontsize=9, color="purple")

# legend (at bottom)
legend_elems = [
    Line2D([0], [0], color="tab:blue", lw=2, label=r"$\gamma_A$ → Detector A"),
    Line2D([0], [0], color="tab:red", lw=2, label=r"$\gamma_B$ → Detector B"),
    Line2D([0], [0], color="black", lw=0,
           marker="*", markerfacecolor="gold", markersize=12,
           label="creation event"),
    Line2D([0], [0], color="purple", lw=1.6, linestyle="--",
           label="Bell correlation (polarizer-axis $\\theta=a-b$)"),
]
ax.legend(handles=legend_elems, loc="lower center",
          bbox_to_anchor=(0.5, -0.07), ncol=4,
          frameon=False, fontsize=9)

plt.tight_layout()
out = _HERE / "entangled_pair_two_stage.png"
plt.savefig(out, dpi=170, bbox_inches="tight")
print(f"saved {out}")
