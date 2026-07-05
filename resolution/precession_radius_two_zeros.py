#!/usr/bin/env python3
"""
precession_radius_two_zeros.py
==============================
Exploratory figure for the Appendix-D discussion (John Bramble + Claude, 2026-06-29).

Question on the table:  when the *precession radius* r_perp = |r| sin(theta) goes to
zero, has the chiral clock STOPPED, or is it still spinning while the radius collapses?

Key idea: r_perp -> 0 has THREE physically distinct causes, and the projected
(transverse) signal alone cannot tell them apart:

  (P) PERPENDICULAR pointer (Appendix D as written): dephasing axis (sigma_x) is
      PERPENDICULAR to the clock axis (sigma_z). Measurement and clock fight; the
      unconditional Bloch vector spirals to the ORIGIN -> maximally mixed. |r|->0.
      ("length collapse" -- the bad zero.)

  (A) ALIGNED pointer, UNCONDITIONAL: dephasing along the clock axis (sigma_z).
      Transverse coherence dies but the populations (z) survive -> the vector lands
      on the axis at an INTERIOR point (0,0,cos theta0): a classical MIXTURE of the
      two pointer states with the prepared (Born-like) weights. |r|->cos theta0.

  (A') ALIGNED pointer, CONDITIONAL (monitored single run): each trajectory PURIFIES
      to a pole (0,0,+/-1) -- a definite, full-length pointer; the clock phase keeps
      advancing until it localizes. Fraction to +pole = cos^2(theta0/2) = Born.
      ("tilt onto axis at preserved purity" -- the good zero, your picture.)

Born is IMPORTED here (it is built into the standard measurement unraveling), not
derived -- consistent with the framework's Horn-2 / quantum-equilibrium concession
(dispute-001).  This figure is about GEOMETRY/MECHANISM, not a Born derivation.

Plus two physical anchors the persistence-of-spin intuition rests on:
  - circular polarization of light: radius (ellipticity) and spin-rate (optical
    frequency) are independent knobs -- a line and a circle spin at the same omega.
  - sequential Stern-Gerlach: |+z> through an analyzer at angle theta gives
    P(+) = cos^2(theta/2); at pi/2 it is 1/2 -- the transverse spin PERSISTS.

numpy + matplotlib only.  Deterministic seed so the run is reproducible.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

rng = np.random.default_rng(7)

# ----------------------------------------------------------------------
# parameters
# ----------------------------------------------------------------------
Omega   = 2.0 * np.pi        # clock (precession) rate: 1 turn per unit time
gamma   = 0.6                # dephasing / measurement rate
theta0  = np.pi / 3.0        # initial tilt from the clock axis (z); cos^2(15deg..)
T       = 4.0
dt      = 2.0e-4
nsteps  = int(T / dt)
t       = np.linspace(0.0, T, nsteps + 1)

p_plus_born = np.cos(theta0 / 2.0) ** 2   # = 0.75 for theta0 = pi/3
r0 = np.array([np.sin(theta0), 0.0, np.cos(theta0)])   # pure, tilted in x-z plane

# ----------------------------------------------------------------------
# (P) perpendicular pointer, unconditional Bloch ODE
#     xdot=-Om y ;  ydot= Om x -2g y ;  zdot=-2g z   (L = sqrt(g) sigma_x)
# (A) aligned pointer, unconditional Bloch ODE
#     xdot=-Om y -2g x ; ydot= Om x -2g y ; zdot=0   (L = sqrt(g) sigma_z)
# ----------------------------------------------------------------------
def integrate_bloch(r0, mode):
    r = np.empty((nsteps + 1, 3)); r[0] = r0
    x, y, z = r0
    for k in range(nsteps):
        if mode == "perp":
            dx = -Omega * y
            dy =  Omega * x - 2 * gamma * y
            dz = -2 * gamma * z
        else:  # aligned
            dx = -Omega * y - 2 * gamma * x
            dy =  Omega * x - 2 * gamma * y
            dz =  0.0
        x += dx * dt; y += dy * dt; z += dz * dt
        r[k + 1] = (x, y, z)
    return r

r_perp_uncond = integrate_bloch(r0, "perp")
r_align_uncond = integrate_bloch(r0, "aligned")

# ----------------------------------------------------------------------
# (A') aligned pointer, CONDITIONAL: diffusive homodyne measurement of sigma_z,
#      c = sqrt(g) sigma_z, H = (Om/2) sigma_z, efficiency 1.  The Ito SME reduces
#      EXACTLY to the pure-state Bloch SDE below (derived from H[c]rho in Bloch
#      coords); these coefficients preserve |r|=1 analytically for eta=1:
#          dx = (-Om y - 2g x) dt   - 2 sqrt(g) z x dW
#          dy = ( Om x - 2g y) dt   - 2 sqrt(g) z y dW
#          dz = ( 0 )          dt   + 2 sqrt(g) (1 - z^2) dW
#      Ensemble-averaging (E[dW]=0) returns the aligned-unconditional ODE, and the
#      split fraction to the +pole is cos^2(theta0/2) = Born.  Vectorized over the
#      whole ensemble at once.
# ----------------------------------------------------------------------
n_ens  = 400
n_show = 6
s2g = 2.0 * np.sqrt(gamma)

X = np.full(n_ens, r0[0]); Y = np.full(n_ens, r0[1]); Z = np.full(n_ens, r0[2])
Xh = np.empty((nsteps + 1, n_show)); Yh = np.empty((nsteps + 1, n_show)); Zh = np.empty((nsteps + 1, n_show))
Xh[0] = X[:n_show]; Yh[0] = Y[:n_show]; Zh[0] = Z[:n_show]
for k in range(nsteps):
    dW = rng.normal(0.0, np.sqrt(dt), n_ens)
    ax_ = (-Omega * Y - 2 * gamma * X); bx_ = -s2g * Z * X
    ay_ = ( Omega * X - 2 * gamma * Y); by_ = -s2g * Z * Y
    az_ = 0.0;                          bz_ =  s2g * (1.0 - Z * Z)
    X = X + ax_ * dt + bx_ * dW
    Y = Y + ay_ * dt + by_ * dW
    Z = Z + az_ * dt + bz_ * dW
    Xh[k + 1] = X[:n_show]; Yh[k + 1] = Y[:n_show]; Zh[k + 1] = Z[:n_show]
traj = np.stack([Xh, Yh, Zh], axis=-1).transpose(1, 0, 2)   # (n_show, nsteps+1, 3)
final_z = Z
frac_plus = float(np.mean(final_z > 0.0))

# helpers
def Rlen(r): return np.linalg.norm(r, axis=-1)
def Rperp(r): return np.hypot(r[..., 0], r[..., 1])

# ----------------------------------------------------------------------
# FIGURE
# ----------------------------------------------------------------------
plt.rcParams.update({"font.size": 10, "axes.titlesize": 10.5,
                     "axes.labelsize": 9.5, "figure.dpi": 130})
fig = plt.figure(figsize=(14.5, 8.6))
gs = GridSpec(2, 3, figure=fig, hspace=0.34, wspace=0.28,
              left=0.06, right=0.985, top=0.92, bottom=0.07)

C_PERP, C_AUNC, C_ACON = "#c1121f", "#1d4e89", "#2a9d8f"

# (a) Bloch x-z projection: the two unconditional fates
ax = fig.add_subplot(gs[0, 0])
th = np.linspace(0, 2 * np.pi, 200)
ax.plot(np.cos(th), np.sin(th), color="0.8", lw=1)
ax.plot(r_perp_uncond[:, 0], r_perp_uncond[:, 2], color=C_PERP, lw=1.6,
        label="perpendicular pointer\n(uncond.) -> origin (mixed)")
ax.plot(r_align_uncond[:, 0], r_align_uncond[:, 2], color=C_AUNC, lw=1.6,
        label="aligned pointer (uncond.)\n-> axis interior (mixture)")
for j in range(n_show):
    ax.plot(traj[j, :, 0], traj[j, :, 2], color=C_ACON, lw=0.7, alpha=0.55)
ax.plot([], [], color=C_ACON, lw=1.2, label="aligned pointer (cond.)\n-> poles (pure)")
ax.scatter([0], [r0[2]], s=0); ax.scatter([r0[0]], [r0[2]], color="k", s=22, zorder=5)
ax.annotate("start (pure,\ntilted)", (r0[0], r0[2]), (0.42, 0.55),
            fontsize=8, ha="left")
ax.set_aspect("equal"); ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
ax.set_xlabel(r"$r_x$  (transverse / precession)"); ax.set_ylabel(r"$r_z$  (clock axis)")
ax.set_title("(a) Bloch fate: where the vector lands")
ax.legend(fontsize=6.6, loc="lower left", framealpha=0.9)

# (b) the two zeros: |r| (purity) and r_perp vs time
ax = fig.add_subplot(gs[0, 1])
ax.plot(t, Rlen(r_perp_uncond), color=C_PERP, lw=1.8, label=r"$|r|$ perp. (uncond.)")
ax.plot(t, Rperp(r_perp_uncond), color=C_PERP, lw=1.0, ls=":", label=r"$r_\perp$ perp.")
ax.plot(t, Rlen(r_align_uncond), color=C_AUNC, lw=1.8, label=r"$|r|$ aligned (uncond.)")
ax.plot(t, Rperp(r_align_uncond), color=C_AUNC, lw=1.0, ls=":", label=r"$r_\perp$ aligned")
ax.plot(t, Rlen(traj[0]), color=C_ACON, lw=1.4, label=r"$|r|$ aligned (cond., 1 run)")
ax.plot(t, Rperp(traj[0]), color=C_ACON, lw=1.0, ls=":", label=r"$r_\perp$ aligned (cond.)")
ax.axhline(np.cos(theta0), color=C_AUNC, lw=0.8, ls="--", alpha=0.6)
ax.text(T * 0.62, np.cos(theta0) + 0.02, r"$|r|\to\cos\theta_0$ (populations kept)",
        color=C_AUNC, fontsize=7.2)
ax.set_xlabel("time"); ax.set_ylabel("Bloch length")
ax.set_ylim(-0.03, 1.05)
ax.set_title("(b) two zeros of $r_\\perp$: length-collapse vs purity-kept")
ax.legend(fontsize=6.6, ncol=1, loc="upper right", framealpha=0.9)

# (c) conditional z(t): single outcomes + Born split
ax = fig.add_subplot(gs[0, 2])
for j in range(n_show):
    ax.plot(t, traj[j, :, 2], color=C_ACON, lw=0.8, alpha=0.7)
ax.plot(t, r_align_uncond[:, 2], color=C_AUNC, lw=2.0,
        label=r"uncond. $\langle\sigma_z\rangle$ (const.)")
ax.axhline(1, color="0.6", lw=0.8, ls="--"); ax.axhline(-1, color="0.6", lw=0.8, ls="--")
ax.set_xlabel("time"); ax.set_ylabel(r"$z = \langle\sigma_z\rangle$  (single runs)")
ax.set_ylim(-1.12, 1.12)
ax.set_title("(c) monitored runs purify to definite poles")
ax.text(0.04 * T, -0.55,
        f"Born check:\nprepared $\\cos^2(\\theta_0/2)={p_plus_born:.2f}$\n"
        f"sim. fraction to +pole $={frac_plus:.2f}$\n(N={n_ens})",
        fontsize=7.6, va="center",
        bbox=dict(boxstyle="round", fc="white", ec="0.7"))
ax.legend(fontsize=7, loc="upper right")

# (d) circular polarization: radius and spin-rate are independent
ax = fig.add_subplot(gs[1, 0])
tt = np.linspace(0, 2 * np.pi, 300)
for delta, lab, col in [(np.pi / 2, "circular (full spin)", C_ACON),
                        (np.pi / 4, "elliptical", C_AUNC),
                        (0.02, "linear (no net spin)", C_PERP)]:
    Ex = np.cos(tt); Ey = np.cos(tt - delta)
    ax.plot(Ex, Ey, color=col, lw=1.7, label=lab)
ax.set_aspect("equal"); ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
ax.set_xlabel(r"$E_x$"); ax.set_ylabel(r"$E_y$")
ax.set_title("(d) photon polarization:\nradius $\\neq$ optical frequency $\\omega$")
ax.legend(fontsize=7, loc="lower right", framealpha=0.9)
ax.text(-1.13, 1.0, "same $\\omega$ for all three;\nonly the radius (ellipticity) differs",
        fontsize=7, va="top")

# (e) sequential Stern-Gerlach: P(+) = cos^2(theta/2)
ax = fig.add_subplot(gs[1, 1])
ang = np.linspace(0, np.pi, 200)
ax.plot(np.degrees(ang), np.cos(ang / 2) ** 2, color="#5b2a86", lw=2)
ax.axvline(90, color="0.6", lw=0.9, ls="--")
ax.scatter([90], [0.5], color="#5b2a86", zorder=5)
ax.annotate(r"gradient rotated $\pi/2$: $P=\frac{1}{2}$"
            "\n(transverse spin persists)",
            (90, 0.5), (15, 0.62), fontsize=7.6,
            arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_xlabel(r"second-analyzer angle $\theta$ from $z$ (deg)")
ax.set_ylabel(r"$P(+)$ for input $|{+}z\rangle$")
ax.set_xlim(0, 180); ax.set_ylim(-0.03, 1.03)
ax.set_title("(e) sequential Stern-Gerlach")

# (f) discriminator: the (r_perp, r_z) plane with purity contours
ax = fig.add_subplot(gs[1, 2])
for rr in (0.25, 0.5, 0.75, 1.0):
    a = np.linspace(0, np.pi / 2, 80)
    ax.plot(rr * np.sin(a), rr * np.cos(a), color="0.85", lw=0.9)
ax.text(0.72, 0.74, r"$|r|=1$ (pure)", color="0.55", fontsize=7, rotation=-45)
ax.plot(Rperp(r_perp_uncond), r_perp_uncond[:, 2], color=C_PERP, lw=1.8,
        label="perp. (uncond.)")
ax.plot(Rperp(r_align_uncond), r_align_uncond[:, 2], color=C_AUNC, lw=1.8,
        label="aligned (uncond.)")
for j in range(n_show):
    ax.plot(Rperp(traj[j]), traj[j, :, 2], color=C_ACON, lw=0.7, alpha=0.6)
ax.plot([], [], color=C_ACON, lw=1.2, label="aligned (cond.)")
ax.scatter([0], [0], color=C_PERP, s=40, zorder=6)
ax.scatter([0], [np.cos(theta0)], color=C_AUNC, s=40, zorder=6)
ax.scatter([0, 0], [1, -1], color=C_ACON, s=40, zorder=6)
ax.scatter([Rperp(r0)], [r0[2]], color="k", s=22, zorder=6)
ax.set_xlabel(r"$r_\perp$  (precession radius)"); ax.set_ylabel(r"$r_z$  (populations)")
ax.set_xlim(-0.04, 1.05); ax.set_ylim(-1.12, 1.12)
ax.set_title("(f) where $r_\\perp\\to0$ ends up")
ax.legend(fontsize=7, loc="lower right", framealpha=0.9)

fig.suptitle("Precession radius $r_\\perp=|r|\\sin\\theta\\to0$: does the chiral clock stop, "
             "or keep spinning while the radius collapses?", fontsize=12.5, y=0.975)

out = "precession_radius_two_zeros.png"
fig.savefig(out, bbox_inches="tight")
print("wrote", out)
print(f"Born check: prepared cos^2(theta0/2) = {p_plus_born:.4f}; "
      f"sim fraction to +pole = {frac_plus:.4f} (N={n_ens})")
print(f"perp uncond final |r|   = {Rlen(r_perp_uncond)[-1]:.4f}  (-> 0, mixed)")
print(f"aligned uncond final |r| = {Rlen(r_align_uncond)[-1]:.4f}  (= cos theta0 = {np.cos(theta0):.4f})")
print(f"aligned cond  mean final |r| = {np.mean([Rlen(traj[j])[-1] for j in range(n_show)]):.4f}  (-> 1, pure)")
