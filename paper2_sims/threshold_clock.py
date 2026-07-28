#!/usr/bin/env python3
"""Paper 2, Figure 1 — the locking layer as physics (two panels).

Panel (a): WHEN DOES A MODE OWN A CLOCK? Injected Stuart-Landau oscillator
    da/dt = (g - |a|^2) a - i*Delta*a + F + noise,
net linear gain g swept through zero at fixed detuning Delta and injection F.
Below g = 0 the mode is a driven damped LINEAR system: unique globally
attracting fixed point, phase slaved to the drive, winding rate exactly zero
(Paper 1, Theorem 2 / Appendix B.1). Above g = 0 the mode owns a limit cycle
(radius ~ sqrt(g)) and a free phase; once the injection can no longer entrain
it (effective locking range K_eff = F/sqrt(g) < Delta), the free clock RUNS:
mean winding rate rises toward the autonomous Adler value
sqrt(Delta^2 - K_eff^2). The onset of a running clock at/above threshold --
and its structural absence below -- is the content of Theorem 2 rendered as
a single observable.

Panel (b): ONE CURVE SPANS VIRTUAL AND REAL. Adler phase equation
    dphi/dt = dw - K sin(phi),
slip period T_slip vs detuning dw/K. Far off-resonance (dw >> K):
T_slip -> 2*pi/dw, i.e. tau ~ hbar/Delta-E -- the energy-time-uncertainty
lifetime of a virtual (off-shell) excitation. At the tongue boundary
(dw -> K+): T_slip -> infinity -- critical slowing; the mode stops slipping,
locks, and goes real (on-shell). Numerical slip periods overlay the analytic
T = 2*pi/sqrt(dw^2 - K^2).

Seeded, pure numpy + matplotlib. Output: ../figures/p2_fig1_threshold.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(20260728)

# ---------------------------------------------------------------- panel (a)
DELTA, F, D = 1.0, 0.35, 1e-4
dt = 0.01
T_TR, T_AV = 200.0, 800.0
N_TR, N_AV = int(T_TR / dt), int(T_AV / dt)
g_vals = np.linspace(-1.0, 1.5, 26)


def winding_rate(g):
    a = 0.1 + 0.0j
    sq = np.sqrt(D * dt)
    for _ in range(N_TR):
        a += dt * ((g - abs(a) ** 2) * a - 1j * DELTA * a + F) \
            + sq * (rng.standard_normal() + 1j * rng.standard_normal())
    tot, prev = 0.0, np.angle(a)
    for _ in range(N_AV):
        a += dt * ((g - abs(a) ** 2) * a - 1j * DELTA * a + F) \
            + sq * (rng.standard_normal() + 1j * rng.standard_normal())
        cur = np.angle(a)
        d = (cur - prev + np.pi) % (2 * np.pi) - np.pi
        tot += d
        prev = cur
    return abs(tot) / T_AV


wind = np.array([winding_rate(g) for g in g_vals])

# analytic autonomous-Adler winding rate for g > 0 (amplitude ~ sqrt(g),
# effective locking range K_eff = F/sqrt(g); runs when K_eff < Delta)
g_pos = np.linspace(1e-3, 1.5, 300)
keff2 = F ** 2 / g_pos
adler = np.where(DELTA ** 2 > keff2, np.sqrt(np.maximum(DELTA ** 2 - keff2, 0.0)), 0.0)

# ---------------------------------------------------------------- panel (b)
K = 1.0
dws = np.concatenate([np.linspace(1.02, 1.5, 13), np.linspace(1.6, 5.0, 12)])


def slip_period(dw):
    phi, t, dt2 = 0.0, 0.0, 0.0005
    target = phi + 2 * np.pi
    while phi < target:
        phi += dt2 * (dw - K * np.sin(phi))
        t += dt2
        if t > 5e4:
            return np.nan
    return t


T_slip = np.array([slip_period(dw) for dw in dws])
dw_fine = np.linspace(1.001, 5.0, 500)
T_analytic = 2 * np.pi / np.sqrt(dw_fine ** 2 - K ** 2)
T_up = 2 * np.pi / dw_fine

# ------------------------------------------------------------------- figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.0))

ax1.plot(g_pos, adler, "-", color="0.55", lw=1.4,
         label=r"autonomous Adler rate $\sqrt{\Delta^2-K_{\rm eff}^2}$")
ax1.plot(g_vals, wind, "o", ms=5, color="#1f4e8c", label="simulated winding rate")
ax1.axvline(0.0, color="0.75", lw=0.8, ls="--")
ax1.annotate("slaved phase\n(no clock)", xy=(-0.62, 0.42), ha="center", fontsize=9,
             color="0.35")
ax1.annotate("free clock runs", xy=(0.95, 0.55), ha="center", fontsize=9,
             color="0.35")
ax1.set_xlabel(r"net gain $g$  (threshold at $g=0$)")
ax1.set_ylabel(r"mean phase winding rate $|\langle\dot\varphi\rangle|$")
ax1.set_title("(a)  The clock switches on at threshold", fontsize=10)
ax1.legend(fontsize=8, loc="upper left")

ax2.plot(dw_fine, T_analytic, "-", color="0.55", lw=1.4,
         label=r"$2\pi/\sqrt{\Delta\omega^2-K^2}$")
ax2.plot(dw_fine, T_up, ":", color="0.35", lw=1.2,
         label=r"UP tail $2\pi/\Delta\omega\ (=2\pi\hbar/\Delta E)$")
ax2.plot(dws, T_slip, "o", ms=5, color="#1f4e8c", label="simulated slip period")
ax2.axvline(1.0, color="0.75", lw=0.8, ls="--")
ax2.annotate("lock\n(goes real)", xy=(1.09, 45), ha="left", fontsize=9, color="0.35")
ax2.set_xlabel(r"detuning $\Delta\omega/K$  (off-shellness $\Delta E/\hbar K$)")
ax2.set_ylabel(r"slip period $T_{\rm slip}\cdot K$")
ax2.set_yscale("log")
ax2.set_title("(b)  One curve spans virtual and real", fontsize=10)
ax2.legend(fontsize=8, loc="upper right")

for ax in (ax1, ax2):
    ax.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig("../figures/p2_fig1_threshold.png", dpi=300)
print("wrote ../figures/p2_fig1_threshold.png")
print("panel a: winding at g=-1:", wind[0], " at g=+1.5:", wind[-1])
print("panel b: T_slip at dw=1.02:", T_slip[0], " at dw=5:", T_slip[-1],
      " analytic:", 2 * np.pi / np.sqrt(25 - 1))
