"""
detector_resonance_selection.py
================================

Closes "seam 1" of the wave-energy Born route (drafts/NOTE_wave_energy_interpretation.md
Sec 7 1/2 .b): the Dirac energy density is T00 = E|psi|^2, so an ENERGY-weighted readout
of an unequal-energy superposition would give P ~ E_n|c_n|^2, deviating from Born
(P ~ |c_n|^2).  Claim: a real (resonant, electromagnetic) detector does NOT do that.

Two independent reasons, both shown here:
  (a) RESONANCE = ENERGY SELECTION.  A two-level detector of transition freq w_d is a
      narrow filter L(w_n - w_d) = g^2/((w_n-w_d)^2 + g^2); as linewidth g->0 it -> delta,
      so each detector sees ONE energy.  With E pinned to hbar*w_d, E|psi|^2 ~ |psi|^2.
  (b) CHARGE vs ENERGY COUPLING.  The two Noether densities couple differently:
        j0  = psi^dag psi = |psi|^2   (CHARGE  -> A_mu, electromagnetic)
        T00 = E|psi|^2                (ENERGY  -> g_mu_nu, gravitational)
      An ordinary detector is EM: it reads j0 = |psi|^2 -> Born, E-independent.
      Only a GRAVITATIONAL detector would read T00 = E|psi|^2 -> the deviation.

Experiments
-----------
 (1) Resonance lineshape: one detector's excitation vs drive frequency (energy selection).
 (2) Spectrometer readout of an UNEQUAL-energy superposition:
        Born |c_n|^2  vs  charge-coupled bank (-> Born)  vs  energy-coupled bank (-> E_n|c_n|^2).
 (3) Finite-linewidth leakage: TVD(charge readout, Born) vs g  (exact only as g->0);
     and TVD(energy readout, Born) = the intrinsic E-weighting a gravitational probe would see.

numpy + matplotlib only.  Deterministic.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- an unequal-energy superposition (the regime where the seam bites) ----
w = np.array([1.0, 1.5, 2.0, 2.5])          # channel energies (hbar=1): 2.5x spread
p_born = np.array([0.40, 0.30, 0.20, 0.10]) # |c_n|^2  (Born target)
p_born = p_born / p_born.sum()
csq = p_born                                # |c_n|^2
p_energy = w * csq; p_energy = p_energy / p_energy.sum()   # E_n|c_n|^2  (the deviation)

def lorentz(dw, g):
    return g**2 / (dw**2 + g**2)            # peak 1 at resonance, width g

def readout(gamma, energy_coupled=False):
    """Detector bank tuned to w_d = w_n. Rate(d) = sum_n coeff_n |c_n|^2 L(w_n-w_d)."""
    coeff = w * csq if energy_coupled else csq          # energy- vs charge-coupling
    rate = np.array([np.sum(coeff * lorentz(w - wd, gamma)) for wd in w])
    return rate / rate.sum()

def tvd(a, b):
    return 0.5 * np.abs(np.asarray(a) - np.asarray(b)).sum()

# ---- (1) resonance lineshape for the w_d = 2.0 detector ----
wd0 = 2.0
scan = np.linspace(0.0, 3.5, 700)
lines = {g: lorentz(scan - wd0, g) for g in (0.05, 0.15, 0.4)}

# ---- (2) spectrometer readout, narrow detectors ----
g_meas = 0.05
meas_charge = readout(g_meas, energy_coupled=False)
meas_energy = readout(g_meas, energy_coupled=True)

# ---- (3) leakage vs linewidth ----
g_axis = np.linspace(0.01, 0.6, 40)
tvd_charge = np.array([tvd(readout(g, False), p_born) for g in g_axis])
tvd_energy_dev = tvd(p_energy, p_born)      # intrinsic E-weighting deviation (g-independent target)

# ================================================================ report
print("=" * 72)
print("SEAM 1: does a resonant EM detector report Born or the energy-weighting?")
print("=" * 72)
print(f"\nUnequal-energy superposition:  E_n = {w}")
print(f"  Born   |c_n|^2            = {np.round(p_born,3)}")
print(f"  Energy E_n|c_n|^2 (T00)   = {np.round(p_energy,3)}   <- the seam's deviation")
print(f"\n[2] narrow detectors (linewidth g={g_meas}):")
print(f"  charge-coupled readout (j0=|psi|^2)  = {np.round(meas_charge,3)}   TVD(Born)={tvd(meas_charge,p_born):.4f}")
print(f"  energy-coupled readout (T00=E|psi|^2)= {np.round(meas_energy,3)}   TVD(Born)={tvd(meas_energy,p_born):.4f}")
print(f"\n  => the EM (charge) detector reports BORN; only an ENERGY (gravitational)")
print(f"     coupling reproduces E_n|c_n|^2.  Seam 1 closes for all EM detection.")
print(f"\n[3] finite-linewidth leakage (charge readout):")
for g in (0.05, 0.15, 0.30, 0.50):
    print(f"     g={g:4.2f} : TVD(charge, Born) = {tvd(readout(g,False),p_born):.4f}")
print(f"     -> exact Born as g->0; small off-resonant leak ~ (g/Delta)^2 for finite g.")
print(f"     intrinsic E-weighting deviation (what a gravitational probe sees): TVD={tvd_energy_dev:.3f}")

# ================================================================ figure
fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.6))

a0 = ax[0]
for g, L in lines.items():
    a0.plot(scan, L, lw=2, label=fr"$\gamma$={g}")
for wn in w:
    a0.axvline(wn, color="gray", ls=":", alpha=0.5)
a0.axvline(wd0, color="k", ls="--", alpha=0.7)
a0.set_xlabel(r"drive energy $E=\hbar\omega$"); a0.set_ylabel("excitation (norm.)")
a0.set_title(r"(1) Resonance = energy selection" + "\n" + r"detector at $\omega_d$=2.0 filters one energy")
a0.legend(fontsize=9); a0.grid(alpha=0.3)

a1 = ax[1]
idx = np.arange(len(w)); bw = 0.2
a1.bar(idx - 1.5*bw, p_born, bw, color="k", label=r"Born $|c_n|^2$")
a1.bar(idx - 0.5*bw, meas_charge, bw, color="tab:green", label="charge readout (EM)")
a1.bar(idx + 0.5*bw, meas_energy, bw, color="tab:red", label="energy readout (grav.)")
a1.bar(idx + 1.5*bw, p_energy, bw, color="tab:orange", alpha=0.6, label=r"$E_n|c_n|^2$ target")
a1.set_xticks(idx); a1.set_xticklabels([f"E={e}" for e in w])
a1.set_ylabel("measured weight")
a1.set_title("(2) EM detector -> Born; only\nenergy(gravitational) coupling -> $E_n|c_n|^2$")
a1.legend(fontsize=8); a1.grid(alpha=0.3, axis="y")

a2 = ax[2]
a2.plot(g_axis, tvd_charge, "o-", ms=4, color="tab:green", label="TVD(charge readout, Born)")
a2.axhline(tvd_energy_dev, color="tab:red", ls="--", lw=2,
           label=f"TVD(energy readout, Born) = {tvd_energy_dev:.2f}")
a2.set_xlabel(r"detector linewidth $\gamma$"); a2.set_ylabel("TVD from Born")
a2.set_title("(3) Charge readout -> Born as $\\gamma\\to0$;\nleak ~ $(\\gamma/\\Delta)^2$. Energy dev. is gravitational.")
a2.legend(fontsize=8); a2.grid(alpha=0.3)

fig.suptitle("Seam 1 closed: resonant EM (charge-coupled) detection reports Born $|\\psi|^2$; "
             "the $E|\\psi|^2$ energy-weighting is gravitational only", fontsize=12.5, y=1.02)
fig.tight_layout()
out = "code/detector_resonance_selection.png"
fig.savefig(out, dpi=130, bbox_inches="tight")
print(f"\nfigure -> {out}")
