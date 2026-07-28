#!/usr/bin/env python3
"""
make_figures.py — generate the paper's figures from the (corrected) simulations.

Design discipline (per the dataviz method): Okabe-Ito colorblind-safe palette,
every series carries a marker/linestyle + direct label so identity is never
colour-alone, thin marks, recessive grid/axes, single y-axis. Figures use the
TRUE absorbing boundary (last survivor) where the v0.4 correction matters.

Outputs: ../figures/fig2_knife_edge.png ... fig7_port.png  (300 dpi).
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUT, exist_ok=True)

# Okabe-Ito (colorblind-safe)
OK = dict(black="#000000", orange="#E69F00", sky="#56B4E9", green="#009E73",
          yellow="#F0E442", blue="#0072B2", verm="#D55E00", purple="#CC79A7")
BORN = "#555555"

plt.rcParams.update({
    "figure.dpi": 300, "savefig.dpi": 300, "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#dddddd", "grid.linewidth": 0.6,
    "axes.axisbelow": True, "figure.autolayout": True,
})


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, bbox_inches="tight")
    plt.close(fig)
    print("wrote", os.path.relpath(p))


# ---- shared corrected engines ---------------------------------------------
def absorb_game(e0, law="sqrt", sigma=0.3, dt=0.02, eps=1e-9, ntrials=4000,
                maxit=600000, seed=0):
    """Independent-noise shares martingale, TRUE absorbing boundary (last survivor)."""
    rng = np.random.default_rng(seed)
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool)
    win = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        ei = e[idx]
        amp = np.sqrt(ei) if law == "sqrt" else (0.3 * np.ones_like(ei) if law == "add" else ei)
        ei = ei + sigma * amp * rng.normal(0, np.sqrt(dt), ei.shape)
        ei = np.where(ei < eps, 0.0, ei)
        e[idx] = ei
        alive = (ei > 0).sum(1)
        done = alive <= 1
        dead = alive == 0
        if done.any():
            f = idx[done]; win[f] = e[f].argmax(1); active[f] = False
        if dead.any():
            active[idx[dead]] = False
    w = win[win >= 0]
    return np.bincount(w, minlength=n) / max(len(w), 1)


def gambler_threshold(e0, thresh, ntrials=8000, step=0.1, maxit=3000000, seed=11):
    """Conserving pairwise exchange, stop at share>=thresh (argmax winner)."""
    rng = np.random.default_rng(seed)
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool); win = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        i = rng.integers(0, n, idx.size); j = (i + rng.integers(1, n, idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        e[idx, i] -= d; e[idx, j] += d
        done = e[idx].max(1) >= thresh
        if done.any():
            f = idx[done]; win[f] = e[f].argmax(1); active[f] = False
    w = win[win >= 0]
    return np.bincount(w, minlength=n).max() / max(len(w), 1)


def gambler_absorb(e0, ntrials=8000, step=0.1, eps=1e-9, maxit=3000000, seed=11):
    rng = np.random.default_rng(seed)
    n = len(e0)
    e = np.tile(np.asarray(e0, float), (ntrials, 1))
    active = np.ones(ntrials, bool); win = np.full(ntrials, -1)
    for _ in range(maxit):
        if not active.any():
            break
        idx = np.where(active)[0]
        i = rng.integers(0, n, idx.size); j = (i + rng.integers(1, n, idx.size)) % n
        stake = step * np.minimum(e[idx, i], e[idx, j])
        d = stake * np.where(rng.random(idx.size) < 0.5, 1.0, -1.0)
        e[idx, i] -= d; e[idx, j] += d
        e[idx] = np.where(e[idx] < eps, 0.0, e[idx])
        done = (e[idx] > 0).sum(1) <= 1
        if done.any():
            f = idx[done]; win[f] = e[f].argmax(1); active[f] = False
    w = win[win >= 0]
    return np.bincount(w, minlength=n).max() / max(len(w), 1)


# ---- Fig 2 — the knife-edge (noise scaling) --------------------------------
def fig2():
    b = np.array([1.] * 9 + [9.]); b /= b.sum()          # 10-site, bright Born 0.5
    laws = [("√e  (amplitude-linear)", "sqrt", OK["blue"]),
            ("additive", "add", OK["verm"]),
            ("multiplicative", "lin", OK["green"])]
    bright = [absorb_game(b, law=k)[-1] for _, k, _ in laws]
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    xs = np.arange(len(laws))
    for x, (lab, _, c), v in zip(xs, laws, bright):
        ax.bar(x, v, width=0.6, color=c, zorder=3)
        ax.text(x, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    ax.axhline(0.5, color=BORN, lw=1.5, ls="--", zorder=2)
    ax.text(len(laws) - 0.4, 0.52, "Born = 0.50", color=BORN, fontsize=9, va="bottom", ha="right")
    ax.set_xticks(xs); ax.set_xticklabels([l for l, _, _ in laws], fontsize=9)
    ax.set_ylabel("bright-site registration probability")
    ax.set_ylim(0, 1.08)
    ax.set_title("Only √e noise is fair — the knife-edge (10-site test, Born 0.50)", fontsize=10)
    save(fig, "fig2_knife_edge.png")


# ---- Fig 3 — the threshold artifact and its fix ----------------------------
def fig3():
    e0 = np.array([0.8, 0.2])                              # Born bright 0.8
    ths = np.array([0.90, 0.95, 0.99, 0.995, 0.999])
    ps = [gambler_threshold(e0, t, ntrials=20000) for t in ths]
    p_abs = gambler_absorb(e0, ntrials=20000)
    tt = np.linspace(0.90, 0.999, 120)                    # closed-form threshold bias
    P_an = (0.8 - (1 - tt)) / (2 * tt - 1)
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.axhline(0.8, color=BORN, lw=1.5, ls="--", zorder=2)
    ax.text(0.90, 0.802, "Born = 0.800", color=BORN, fontsize=9, va="bottom")
    ax.plot(tt, P_an, color="#aaaaaa", lw=1.3, zorder=2,
            label="closed-form bias $\\,(s_0{-}(1{-}t))/(2t{-}1)$")
    ax.plot(ths, ps, marker="o", ms=6, lw=0, color=OK["verm"], zorder=3,
            label="finite-threshold stop (simulated)")
    ax.plot([1.0], [p_abs], marker="D", ms=9, lw=0, color=OK["blue"], zorder=4,
            label="true absorbing boundary")
    ax.annotate(f"{ps[1]:.3f} at $t=0.95$", xy=(0.95, ps[1]), xytext=(0.898, 0.816),
                fontsize=8.5, color=OK["verm"], ha="left",
                arrowprops=dict(arrowstyle="->", color=OK["verm"], lw=1))
    ax.annotate(f"{p_abs:.3f}", xy=(1.0, p_abs), xytext=(0.972, 0.818),
                fontsize=9, color=OK["blue"], ha="center",
                arrowprops=dict(arrowstyle="->", color=OK["blue"], lw=1))
    ax.set_xlabel("stopping threshold  $t$  (share)")
    ax.set_ylabel("bright-site win probability")
    ax.set_xlim(0.89, 1.01); ax.set_ylim(0.785, 0.875)
    ax.legend(frameon=False, fontsize=8.5, loc="upper right")
    ax.set_title("The martingale is exact only at the absorbing boundary", fontsize=10)
    save(fig, "fig3_threshold.png")


# ---- Fig 4 — Born deviation vs soft-layer width ----------------------------
def fig4():
    def biased(e0, w, ntrials=2500, step=0.1, thresh=0.995, maxit=600000, seed=23):
        rng = np.random.default_rng(seed)
        n = len(e0); e = np.tile(e0, (ntrials, 1))
        active = np.ones(ntrials, bool); win = np.full(ntrials, -1)
        for _ in range(maxit):
            if not active.any():
                break
            idx = np.where(active)[0]
            i = rng.integers(0, n, idx.size); j = (i + rng.integers(1, n, idx.size)) % n
            ei, ej = e[idx, i], e[idx, j]
            stake = step * np.minimum(ei, ej)
            if w > 0:
                bi = np.minimum(1.0, w / np.maximum(1 - ei, 1e-12))
                bj = np.minimum(1.0, w / np.maximum(1 - ej, 1e-12))
                p = 0.5 + (bi - bj) / 4.0
            else:
                p = 0.5
            d = stake * np.where(rng.random(idx.size) < p, -1.0, 1.0)
            e[idx, i] -= d; e[idx, j] += d
            done = e[idx].max(1) >= thresh
            if done.any():
                f = idx[done]; win[f] = e[f].argmax(1); active[f] = False
        w2 = win[win >= 0]
        freq = np.bincount(w2, minlength=n) / max(len(w2), 1)
        return np.max(np.abs(freq - e0))
    A = np.array([1.] * 9 + [3.]); born = A ** 2 / np.sum(A ** 2)
    ws = np.array([0.003, 0.01, 0.03, 0.1, 0.3])
    devs = [biased(born.copy(), w) for w in ws]
    fig, ax = plt.subplots(figsize=(5.2, 3.5))
    ax.loglog(ws, devs, marker="o", ms=6, lw=2, color=OK["purple"], zorder=3,
              label="worst-case (Adler-tail) bias")
    for xv in (1e-6, 1e-2):
        ax.axvline(xv, color="#bbbbbb", lw=1, ls=":")
    ax.text(1e-6, 3e-4, "atomic\nlines", fontsize=8, color="#777777", ha="center")
    ax.text(1e-2, 3e-4, "broadband\nsolids", fontsize=8, color="#777777", ha="center")
    ax.set_xlabel("soft lock-layer width  $w = \\Gamma/\\omega$")
    ax.set_ylabel("max Born deviation")
    ax.set_xlim(5e-7, 0.5)
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    ax.set_title("Sharpness is required: deviation shrinks with layer width", fontsize=10)
    save(fig, "fig4_layer_width.png")


# ---- Fig 5 — Glauber bunching / anti-bunching ------------------------------
def fig5():
    # same-site registration fraction: game vs naive mean-intensity model
    states = ["|1,1⟩\n(anti-correlated)", "(|2,0⟩+|0,2⟩)/√2\n(bunched)"]
    game = [0.0, 1.0]           # from multiquantum sim (perfect anti-/bunching)
    naive = [0.5, 0.5]          # intensity-only model: identical for both
    fig, ax = plt.subplots(figsize=(5.4, 3.5))
    x = np.arange(2); w = 0.36
    b1 = ax.bar(x - w / 2, game, w, color=OK["blue"], zorder=3, label="selection game (= Glauber)")
    b2 = ax.bar(x + w / 2, naive, w, color=OK["orange"], zorder=3, hatch="///",
                edgecolor="white", label="naive mean-intensity model")
    for xi, v in zip(x - w / 2, game):
        ax.text(xi, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    for xi, v in zip(x + w / 2, naive):
        ax.text(xi, v + 0.02, f"{v:.2f}", ha="center", va="bottom", fontsize=9)
    ax.set_xticks(x); ax.set_xticklabels(states, fontsize=9)
    ax.set_ylabel("same-site (two-photon) fraction")
    ax.set_ylim(0, 1.15)
    ax.legend(frameon=False, fontsize=9, loc="upper center")
    ax.set_title("Same marginals, opposite correlations — the game gets both", fontsize=10)
    save(fig, "fig5_glauber.png")


# ---- Fig 6 — the fidelity law S = 2√2 η ------------------------------------
def fig6():
    eta = np.linspace(0, 1, 100)
    S = 2 * np.sqrt(2) * eta
    pts_eta = [0.5, 0.707, 0.9, 1.0]
    pts_S = [1.421, 2.000, 2.533, 2.820]      # simulated (paper §7.2)
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    ax.plot(eta, S, lw=2, color=OK["blue"], zorder=3, label="$S = 2\\sqrt{2}\\,\\eta$")
    ax.plot(pts_eta, pts_S, "o", ms=7, color=OK["verm"], zorder=4, label="simulated joint game")
    ax.axhline(2.0, color=BORN, lw=1.4, ls="--", zorder=2)
    ax.text(0.02, 2.03, "local-realism bound  $S=2$", color=BORN, fontsize=9, va="bottom")
    ax.axhline(2 * np.sqrt(2), color="#999999", lw=1, ls=":", zorder=2)
    ax.text(0.02, 2 * np.sqrt(2) + 0.02, "Tsirelson  $2\\sqrt{2}$", color="#777777", fontsize=8.5, va="bottom")
    ax.axvline(1 / np.sqrt(2), color="#cccccc", lw=1, ls=":")
    ax.annotate("$S=2$ crossed\nat $\\eta=1/\\sqrt{2}$", xy=(1 / np.sqrt(2), 2.0),
                xytext=(0.40, 2.20), fontsize=8.5, color="#777777",
                arrowprops=dict(arrowstyle="->", color="#999999", lw=1))
    ax.set_xlabel("resync fidelity  $\\eta$")
    ax.set_ylabel("CHSH  $S$")
    ax.set_xlim(0, 1.02); ax.set_ylim(0, 3.0)
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    ax.set_title("Resync fidelity as a physical parameter", fontsize=10)
    save(fig, "fig6_fidelity.png")


# ---- Fig 7 — the port discriminator ----------------------------------------
def fig7():
    def port(Splus, c, m=4, ntrials=8000, sigma=0.3, dt=0.02, win=0.7, floor=1e-3,
             maxit=60000, seed=53):
        rng = np.random.default_rng(seed)
        n = 2 * m
        e0 = np.concatenate([np.full(m, Splus / m), np.full(m, (1 - Splus) / m)])
        C = np.eye(n); C[:m, :m] = c + (1 - c) * np.eye(m)
        C = (1 - floor) * C + floor * np.eye(n)
        lam, U = np.linalg.eigh(C); L = U * np.sqrt(np.clip(lam, 0, None))
        e = np.tile(e0, (ntrials, 1)); active = np.ones(ntrials, bool); win_ = np.full(ntrials, -1)
        for _ in range(maxit):
            if not active.any():
                break
            idx = np.where(active)[0]
            dW = (rng.normal(0, 1, (idx.size, n)) @ L.T) * np.sqrt(dt)
            ei = np.maximum(e[idx] + sigma * np.sqrt(e[idx]) * dW, 0.0); e[idx] = ei
            tot = ei.sum(1); s = ei / np.maximum(tot[:, None], 1e-12)
            done = (s.max(1) >= win) & (tot > 1e-6)
            if done.any():
                f = idx[done]; win_[f] = e[f].argmax(1); active[f] = False
            dead = tot <= 1e-6
            if dead.any():
                active[idx[dead]] = False
        w = win_[win_ >= 0]
        return (w < m).mean() if len(w) else np.nan
    S = np.array([0.2, 0.35, 0.5, 0.65, 0.8])
    p0 = [port(s, 0.0) for s in S]
    p5 = [port(s, 0.5) for s in S]
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    ax.plot([0, 1], [0, 1], color=BORN, lw=1.4, ls="--", zorder=2, label="Born / matched ports")
    ax.plot(S, p0, marker="o", ms=6, lw=2, color=OK["blue"], zorder=3, label="matched (c=0)")
    ax.plot(S, p5, marker="s", ms=6, lw=2, color=OK["verm"], zorder=3, label="mismatched (c=0.5)")
    ax.set_xlabel("input splitting share  $S$")
    ax.set_ylabel("P(correlated port wins | click)")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.legend(frameon=False, fontsize=9, loc="upper left")
    ax.set_title("The discriminator: a $\\kappa\\,S(1{-}S)$ bow under port mismatch", fontsize=10)
    save(fig, "fig7_port.png")


if __name__ == "__main__":
    print("generating figures ->", os.path.relpath(OUT))
    fig2(); fig3(); fig4(); fig5(); fig6(); fig7()
    print("done.")
