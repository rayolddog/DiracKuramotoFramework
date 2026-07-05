"""
recoil_channel_tracks.py — recoil-channel extension of
complex_rotation_exclusivity.py: puts the WHOLE of paper §5's capture-strength
axis (single click <-> Mott track) inside one simulation.

Extension (paper refs: §3.1 three stages, §3.3 conservation exclusivity, §5
detector taxonomy; discussions/2026-07-04 Follow-up 5):

Each interaction event is a full capture -> commit -> closure cycle (the parent
script's window physics — pole sterility, reversals — is inherited per event and
suppressed here to isolate the CHANNEL structure). Closure now has two modes:

  * CAPTURE channel (branching beta): consumes the remaining quantum; the run
    ends with one full registration. beta -> 1 is the photodetector /
    projective limit ("one quantum, one capture, one commit, one registration,
    one click").
  * RECOIL channel (branching 1-beta): registers a PARTIAL record — a droplet /
    ionization — that takes only eps << E0 from the energy budget and only
    partially measures the direction; the quantum survives and continues.
    beta -> 0 is the cloud-chamber / track limit. Exclusivity generalizes to
    one record PER EVENT (E-p budget bookkeeping per event), with sequential
    events allowed — Mott's track.

Directional mechanics (Mott 1929, in POVM language): the particle's direction
amplitude p(theta) starts UNIFORM (spherical wave). Each recoil closure is a
weak direction measurement with angular acceptance sigma_meas: the event angle
is drawn from q = p (*) K (overlap of amplitude power with site acceptance —
Born-weighted, imported as in the parent), and the post-event amplitude is
p <- p * K(theta_evt) (Kraus update). This is §5's sentence — "each capture
only partially sharpens the momentum, so the next fires preferentially along
the line of flight" — made executable.

Emergent outputs:
  E1  Click<->track axis: mean registrations per run vs beta interpolates from
      1 to E0/eps, matching the truncated-geometric prediction.
  E2  Mott gallery: isotropic source -> straight tracks in random directions;
      first-event angle uniform (the spherical wave chooses ONCE).
  E3  Collinearity: with amplitude conditioning the angular deviation
      PLATEAUS (~sigma_meas); memoryless scattering (no amplitude update)
      diffuses as sigma*sqrt(k). The plateau-vs-diffusion contrast IS Mott's
      result.
  E4  Bragg curve: with Bethe-inspired event spacing (ell ∝ E), deposition
      density rises toward the range end — an emergent Bragg peak, with range
      straggling from stochastic per-event loss.

Honest ledger: firing probability ∝ overlap power is the imported Born
weighting (same status as the parent script); the kernel width sigma_meas (the
per-event partiality) and the Bethe-like spacing ell ∝ E are physical INPUTS;
what is emergent is the click<->track interpolation, the straightness, and the
Bragg shape.

Usage:  python code/recoil_channel_tracks.py     (seed 7, ~<1 min)
Output: code/recoil_channel_tracks.png + printed summary.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

# ----------------------------------------------------------------------------
# directional machinery (theta grid, wrapped Gaussian kernel, Kraus update)
# ----------------------------------------------------------------------------
N_TH = 720
THETA = np.linspace(-np.pi, np.pi, N_TH, endpoint=False)
DTH = THETA[1] - THETA[0]

def wrapped_kernel(sigma):
    """Wrapped Gaussian acceptance kernel on the theta grid, centered at 0."""
    k = np.zeros(N_TH)
    for m in (-1, 0, 1):
        k += np.exp(-0.5 * ((THETA + 2 * np.pi * m) / sigma) ** 2)
    return k / k.sum()

def sample_event_angle(p, K_fft, rng):
    """Draw event angle from q = p (*) K (circular convolution)."""
    q = np.real(np.fft.ifft(np.fft.fft(p) * K_fft))
    q = np.clip(q, 0, None); q /= q.sum()
    return rng.choice(N_TH, p=q)

def kraus_update(p, K, idx):
    """p <- p * K centered at THETA[idx], renormalized."""
    p = p * np.roll(K, idx - N_TH // 2)
    return p / p.sum()

def run_track(E0, eps_mean, beta, sigma_meas, rng, bethe=False,
              max_events=10_000):
    """One quantum with budget E0. Returns event angles, depths, losses,
    and how the run ended ('capture' or 'range')."""
    K = wrapped_kernel(sigma_meas)
    K_fft = np.fft.fft(np.roll(K, N_TH // 2))   # kernel centered for conv
    p = np.ones(N_TH) / N_TH                    # spherical wave: uniform
    E = E0
    angles, depths, losses = [], [], []
    depth = 0.0
    for _ in range(max_events):
        idx = sample_event_angle(p, K_fft, rng)
        step = (E / E0) if bethe else 1.0       # Bethe-like: spacing ∝ E
        depth += max(step, 0.02)
        if rng.random() < beta:                 # CAPTURE closure: budget gone
            angles.append(THETA[idx]); depths.append(depth); losses.append(E)
            return angles, depths, losses, "capture"
        eps = rng.exponential(eps_mean)         # RECOIL closure: partial record
        eps = min(eps, E)
        angles.append(THETA[idx]); depths.append(depth); losses.append(eps)
        E -= eps
        p = kraus_update(p, K, idx)
        if E <= 0:
            return angles, depths, losses, "range"
    return angles, depths, losses, "maxed"

def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi

# ----------------------------------------------------------------------------
print("=" * 72)
print("recoil_channel_tracks.py  (seed 7) — click <-> track from one mechanism")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(13.5, 11))
fig.suptitle("Recoil channel: §5's capture-strength axis in one simulation "
             "(click ↔ Mott track ↔ Bragg)", fontsize=13)

# ----------------------------------------------------------------------------
# E1 — click <-> track axis: mean registrations vs capture branching beta
# ----------------------------------------------------------------------------
E0, EPS = 60.0, 1.0
SIGMA = np.deg2rad(15)
betas = np.array([1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.0])
N1 = 800
mean_regs, ends_cap = [], []
for b in betas:
    n = []
    caps = 0
    for _ in range(N1):
        a, d, l, end = run_track(E0, EPS, b, SIGMA, rng)
        n.append(len(a)); caps += (end == "capture")
    mean_regs.append(np.mean(n)); ends_cap.append(caps / N1)
mean_regs = np.array(mean_regs)

# truncated-geometric prediction: M(beta) = (1 - (1-beta)^nmax)/beta
nmax = E0 / EPS
b_grid = np.linspace(1e-4, 1, 400)
M_pred = (1 - (1 - b_grid) ** nmax) / b_grid
print(f"\nE1  click<->track axis (E0/eps = {nmax:.0f}):")
for b, m, c in zip(betas, mean_regs, ends_cap):
    print(f"    beta={b:6.3f}   mean registrations = {m:8.2f}"
          f"   (ended by capture: {c:.0%})")

ax = axes[0, 0]
ax.plot(b_grid, M_pred, "k-", lw=1.5,
        label=r"truncated geometric $\frac{1-(1-\beta)^{n_{max}}}{\beta}$")
ax.plot(betas[betas > 0], mean_regs[betas > 0], "o", color="#ee6677", ms=7,
        label="MC")
ax.axhline(nmax, color="#4477aa", ls=":", lw=1)
ax.text(0.02, nmax * 0.88, r"track limit $E_0/\epsilon$", fontsize=9,
        color="#4477aa")
ax.axhline(1, color="gray", ls=":", lw=1)
ax.text(0.3, 1.25, "click limit", fontsize=9, color="gray")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel(r"capture branching $\beta$")
ax.set_ylabel("mean registrations per quantum")
ax.set_title("E1  one mechanism: photodetector ($\\beta\\to1$)\n"
             "to cloud chamber ($\\beta\\to0$)")
ax.legend(fontsize=8)

# ----------------------------------------------------------------------------
# E2 — Mott gallery: spherical wave -> straight tracks
# ----------------------------------------------------------------------------
N_GAL = 24
first_angles = []
ax = axes[0, 1]
cmap = plt.cm.viridis(np.linspace(0, 1, N_GAL))
for i in range(N_GAL):
    a, d, l, end = run_track(E0, EPS, 0.0, SIGMA, rng, bethe=True)
    xs = np.cumsum(np.diff([0] + list(d)) * np.cos(a))
    ys = np.cumsum(np.diff([0] + list(d)) * np.sin(a))
    ax.plot(np.concatenate([[0], xs]), np.concatenate([[0], ys]),
            ".", ms=2.0, color=cmap[i])
    first_angles.append(a[0])
# uniformity of first-event angle over many trials
fa = [run_track(E0, EPS, 0.0, SIGMA, rng)[0][0] for _ in range(1500)]
hist, _ = np.histogram(fa, bins=12, range=(-np.pi, np.pi))
tvd_uniform = 0.5 * np.abs(hist / hist.sum() - 1 / 12).sum()
print(f"\nE2  Mott gallery: first-event angle TVD from uniform = "
      f"{tvd_uniform:.3f}  (spherical wave chooses once, isotropically)")
ax.set_aspect("equal")
ax.set_title("E2  Mott 1929: isotropic wave $\\to$ straight tracks\n"
             "(dots = recoil registrations; spacing $\\propto E$)")
ax.set_xlabel("x"); ax.set_ylabel("y")

# ----------------------------------------------------------------------------
# E3 — collinearity: amplitude conditioning vs memoryless scattering
# ----------------------------------------------------------------------------
N3, K_EV = 400, 60
sigmas = [np.deg2rad(5), np.deg2rad(15), np.deg2rad(40)]
ax = axes[1, 0]
colors = ["#4477aa", "#ccbb44", "#ee6677"]
print("\nE3  collinearity (mean |theta_k - theta_1|, deg):")
for s, c in zip(sigmas, colors):
    devs = np.zeros(K_EV)
    for _ in range(N3):
        a, _, _, _ = run_track(1e9, EPS, 0.0, s, rng, max_events=K_EV)
        a = np.array(a)
        devs += np.abs(wrap(a - a[0]))
    devs /= N3
    ax.plot(np.arange(1, K_EV + 1), np.rad2deg(devs), "-", color=c,
            label=fr"conditioned, $\sigma={np.rad2deg(s):.0f}^\circ$")
    # memoryless comparison: random walk theta_k = theta_{k-1} + N(0, s)
    steps = rng.normal(0, s, size=(N3, K_EV))
    walk = np.cumsum(steps, axis=1)
    ax.plot(np.arange(1, K_EV + 1),
            np.rad2deg(np.abs(walk).mean(axis=0)), "--", color=c, alpha=0.5)
    print(f"    sigma={np.rad2deg(s):4.0f}deg: conditioned plateau ~ "
          f"{np.rad2deg(devs[-20:].mean()):5.1f}  vs memoryless(k={K_EV}) ~ "
          f"{np.rad2deg(np.abs(walk[:, -1]).mean()):5.1f}")
ax.plot([], [], "k--", alpha=0.5, label="memoryless (diffuses $\\sqrt{k}$)")
ax.set_xlabel("event number $k$")
ax.set_ylabel(r"mean $|\theta_k-\theta_1|$  (deg)")
ax.set_title("E3  amplitude conditioning makes tracks straight;\n"
             "memoryless scattering would diffuse")
ax.legend(fontsize=8)

# ----------------------------------------------------------------------------
# E4 — emergent Bragg curve (Bethe-like spacing ell ∝ E) + range straggling
# ----------------------------------------------------------------------------
N4 = 3000
E0_b = 100.0
all_depths, all_losses, ranges = [], [], []
for _ in range(N4):
    a, d, l, end = run_track(E0_b, EPS, 0.0, SIGMA, rng, bethe=True)
    all_depths.extend(d); all_losses.extend(l); ranges.append(d[-1])
all_depths = np.array(all_depths); all_losses = np.array(all_losses)
ranges = np.array(ranges)
bins = np.linspace(0, all_depths.max() * 1.02, 80)
dep, _ = np.histogram(all_depths, bins=bins, weights=all_losses)
dep = dep / N4 / np.diff(bins)          # mean deposition per unit depth
centers = 0.5 * (bins[1:] + bins[:-1])
peak_depth = centers[np.argmax(dep)]
print(f"\nE4  Bragg: mean range = {ranges.mean():.1f} +/- {ranges.std():.1f}"
      f" (straggling), peak deposition at depth {peak_depth:.1f}"
      f" = {peak_depth/ranges.mean():.0%} of mean range")

ax = axes[1, 1]
ax.plot(centers, dep, "-", color="#ee6677", lw=2)
ax.axvline(ranges.mean(), color="gray", ls=":", lw=1)
ax.text(ranges.mean() * 1.01, dep.max() * 0.9, "mean range", fontsize=8,
        color="gray", rotation=90)
ax.set_xlabel("depth along track")
ax.set_ylabel(r"mean energy deposition $dE/dx$")
ax.set_title("E4  emergent Bragg curve\n(event spacing $\\propto E$; "
             "stochastic per-event loss $\\to$ straggling)")

plt.tight_layout(rect=[0, 0, 1, 0.94])
out = __file__.replace(".py", ".png")
plt.savefig(out, dpi=110)
print(f"\nwrote {out}")
print("\nSummary: one closure mechanism with two channels spans the full")
print("capture-strength axis (E1); an isotropic wave yields straight tracks in")
print("once-chosen random directions because each partial closure conditions")
print("the amplitude (E2, E3 — Mott, and the plateau-vs-diffusion contrast is")
print("the content); Bethe-like spacing gives an emergent Bragg peak with")
print("range straggling (E4). Born weighting per event remains imported.")
