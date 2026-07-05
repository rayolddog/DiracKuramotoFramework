"""
complex_rotation_exclusivity.py — proof of mechanism, NOT proof of nature.

One quantum, N threshold detector sites, and an explicit COMPLEX POLE carried by
the shared field mode while any site holds a provisional commit.

Physics being modeled (paper refs: current_revision_DK_paper.md §3.1 three
stages, §3.3 conservation-enforced winner-take-all, §3.6 dressed pole;
discussions/2026-07-04-three-stage-measurement.md Follow-ups 3-4):

  * Stage 2 (provisional commit): while site j is provisionally committed, the
    mode eigenvalue is displaced by  delta_j - (i/2)*Gamma_j  (one complex
    number). Its two Kramers-Kronig faces act differently on OTHER sites:
      - Re (line pull, delta):   detunes the tails out of other sites'
        Lorentzian acceptance -> "rotation sterility" (reversible).
      - Im (width/drain, Gamma): the loaned norm decays exp(-Gamma_loan*age)
        -> "depletion sterility" (exponential; restored on reversal).
    Suppression of site i's capture while a pole (delta, Gamma) is active:
        S_i = gamma_i*(gamma_i + Gamma/2) / ((gamma_i + Gamma/2)^2 + delta^2)
    (overlap of the shifted/broadened mode with site i's acceptance of width
    gamma_i, normalized to 1 at delta=Gamma=0). Broadening alone is algebraic;
    shift beyond gamma_i is strong; the norm drain is what becomes absolute.

  * Stage 3 (closure): a provisional site registers irreversibly at rate
    R_close (reservoir-triggering), or reverts at rate R_rev (re-emission /
    sub-latent-speck decay). FIRST CLOSURE WINS; any other provisional commit
    is force-reverted (the loan recalled) — the one-quantum budget, enforced
    globally. Double registrations are therefore impossible BY CONSTRUCTION;
    what the model tests is what statistics survive that construction.

Emergent outputs checked below:
  E1  Born weights with equivariant closure (P(i) -> |psi_i|^2), and the
      first-closure-vs-first-touch split when closure is NOT equivariant
      (recorded = commit x closure branching).
  E2  Antibunching bookkeeping: overlapping provisional windows are real
      (would-be coincidences) but registrations never double.
  E3  Click-TIMING: registration-time distribution vs the wavepacket power
      envelope |f(t)|^2. The model's fingerprint is a closure-latency
      convolution (exponential tail ~1/R_close) that vanishes as
      R_close -> infinity. (The commit-stage r*exp(-int r) distortion is
      common to every rate-based detector model and is not the new piece.)
  E4  FTIR "steal": a wide-tongue probe (gamma_W >> gamma) switched on during
      the Stage-2 window can still capture the quantum (evanescent-frustration
      analog); a narrow-tongue probe mostly cannot; after closure, nobody can.

Honest ledger: capture-rate ∝ delivered power is an INPUT (the Born-form
question lives in born_substrate_sampling.py, not here); the sterility law S
is derived from Lorentzian overlap but the pole values are inputs; the budget
(first-closure-wins) is the conservation postulate whose enforcement is
nonlocal (paper §3.3 wall (i)). This script shows the mechanism is internally
consistent and locates its one observable fingerprint (E3 latency tail).

Usage:  python code/complex_rotation_exclusivity.py     (seed 7, ~<1 min)
Output: code/complex_rotation_exclusivity.png + printed summary.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

# ----------------------------------------------------------------------------
# model pieces
# ----------------------------------------------------------------------------

def sterility(delta, Gamma, gamma_i):
    """Suppression S in [0,1] of a site with acceptance width gamma_i while a
    pole (delta, Gamma) is active. S=1 with no pole; algebraic in Gamma alone;
    strong once delta > gamma_i."""
    g = gamma_i + 0.5 * Gamma
    return gamma_i * g / (g * g + delta * delta)


def run_trial(w, Rc, Rclose, Rrev, delta, Gpole, Gloan, gamma_sites,
              env=None, t_end=np.inf, probe=None, rng=rng):
    """One quantum, event-driven (Gillespie with thinning when env given).

    w           : per-site power weights (sum <= 1)
    Rc          : per-site capture-attempt scale (array)
    Rclose,Rrev : per-site closure / reversal rates (arrays)
    delta,Gpole : complex-pole displacement contributed by an active commit
    Gloan       : drain rate of the loaned norm during a window
    gamma_sites : per-site acceptance widths
    env         : optional power envelope function p(t) (else flat 1)
    probe       : optional dict(site=k, t_on=...) enabling site k only after
                  t_on (FTIR probe); t_on measured from FIRST commit if
                  key 'after_first_commit' is True.
    returns dict(winner, t_close, n_reversals, overlap_windows, t_first_commit)
    """
    N = len(w)
    state = np.zeros(N, dtype=int)          # 0 free, 1 provisional
    t_commit = np.zeros(N)
    t = 0.0
    n_rev = 0
    n_overlap = 0
    t_first = None
    probe_site = probe["site"] if probe else None
    probe_on = False

    # upper bound on total rate for thinning
    def total_and_rates(t):
        nonlocal probe_on
        prov = np.where(state == 1)[0]
        if probe and t_first is not None and not probe_on:
            if t - t_first >= probe["t_on"]:
                probe_on = True
        p_env = env(t) if env else 1.0
        if len(prov) > 0:
            age = t - t_commit[prov].min()
            f_avail = np.exp(-Gloan * age)
            S = np.array([sterility(delta, Gpole, g) for g in gamma_sites])
        else:
            f_avail = 1.0
            S = np.ones(N)
        r_cap = Rc * w * p_env * S * f_avail
        r_cap[state == 1] = 0.0
        if probe_site is not None and not probe_on:
            r_cap[probe_site] = 0.0
        r_close = np.where(state == 1, Rclose, 0.0)
        r_rev = np.where(state == 1, Rrev, 0.0)
        return r_cap, r_close, r_rev

    # crude global bound for thinning (flat env <= 1 assumed)
    R_bound = float(np.sum(Rc * w) + np.sum(Rclose) + np.sum(Rrev)) + 1e-9

    while t < t_end:
        t += rng.exponential(1.0 / R_bound)
        r_cap, r_close, r_rev = total_and_rates(t)
        R_tot = r_cap.sum() + r_close.sum() + r_rev.sum()
        if rng.random() > R_tot / R_bound:
            continue                          # thinned (no event)
        u = rng.random() * R_tot
        c1, c2 = r_cap.sum(), r_cap.sum() + r_close.sum()
        if u < c1:                            # capture -> provisional commit
            i = rng.choice(N, p=r_cap / c1)
            state[i] = 1
            t_commit[i] = t
            if t_first is None:
                t_first = t
            if state.sum() >= 2:
                n_overlap += 1
        elif u < c2:                          # CLOSURE: budget drained, run over
            prov = np.where(state == 1)[0]
            j = rng.choice(prov, p=r_close[prov] / r_close.sum())
            return dict(winner=int(j), t_close=t, n_reversals=n_rev,
                        overlap_windows=n_overlap, t_first_commit=t_first)
        else:                                 # reversal: loan returned
            prov = np.where(state == 1)[0]
            j = rng.choice(prov, p=r_rev[prov] / r_rev.sum())
            state[j] = 0
            n_rev += 1
    return dict(winner=None, t_close=None, n_reversals=n_rev,
                overlap_windows=n_overlap, t_first_commit=t_first)


def tvd(p, q):
    p = np.asarray(p, float); q = np.asarray(q, float)
    return 0.5 * np.abs(p / p.sum() - q / q.sum()).sum()

# ----------------------------------------------------------------------------
# defaults (units: gamma = 1 sets the acceptance-width scale)
# ----------------------------------------------------------------------------
GAMMA = 1.0
DELTA_POLE = 3.0     # Re-Sigma line pull, in units of gamma  -> S ~ 0.13
GAMMA_POLE = 1.0     # Im-Sigma broadening
GAMMA_LOAN = 1.0     # norm-drain rate during a window
R_CAP = 6.0
R_CLOSE = 2.5
R_REV = 1.0

print("=" * 72)
print("complex_rotation_exclusivity.py  (seed 7)")
print(f"pole: delta={DELTA_POLE}, Gamma={GAMMA_POLE}  ->  sterility of a")
print(f"matched narrow site S = {sterility(DELTA_POLE, GAMMA_POLE, GAMMA):.3f}"
      f"   (wide tongue gamma=10: S = {sterility(DELTA_POLE, GAMMA_POLE, 10*GAMMA):.3f})")
print("=" * 72)

fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("Complex-pole exclusivity: rotation (Re) + drain (Im) as one displacement "
             "— proof of mechanism", fontsize=13)

# ----------------------------------------------------------------------------
# E1a — Born weights, equivariant closure
# ----------------------------------------------------------------------------
W4 = np.array([0.4, 0.3, 0.2, 0.1])
N_TRIALS = 20000
ones4 = np.ones(4)
wins = np.zeros(4)
for _ in range(N_TRIALS):
    r = run_trial(W4, R_CAP * ones4, R_CLOSE * ones4, R_REV * ones4,
                  DELTA_POLE, GAMMA_POLE, GAMMA_LOAN, GAMMA * ones4)
    wins[r["winner"]] += 1
freq_eq = wins / wins.sum()
tvd_eq = tvd(freq_eq, W4)
print(f"\nE1a Born (equivariant closure), N={N_TRIALS}:")
print(f"    |psi|^2   = {W4}")
print(f"    P(win)    = {np.round(freq_eq, 4)}   TVD from Born = {tvd_eq:.4f}")

ax = axes[0, 0]
x = np.arange(4)
ax.bar(x - 0.18, W4, 0.36, label=r"$|\psi_i|^2$ (Born)", color="#4477aa")
ax.bar(x + 0.18, freq_eq, 0.36, label="MC winner freq", color="#ee6677")
ax.set_title(f"E1a  Born, equivariant closure (TVD={tvd_eq:.4f})")
ax.set_xlabel("site"); ax.set_ylabel("probability"); ax.legend()

# ----------------------------------------------------------------------------
# E1b — non-equivariant closure: recorded = commit x closure-branching
# ----------------------------------------------------------------------------
Rclose_bad = np.array([R_CLOSE, R_CLOSE, 0.5, R_CLOSE])   # site 2 closes poorly
p_branch = Rclose_bad / (Rclose_bad + R_REV)
pred = W4 * p_branch
pred = pred / pred.sum()
wins = np.zeros(4)
for _ in range(N_TRIALS):
    r = run_trial(W4, R_CAP * ones4, Rclose_bad, R_REV * ones4,
                  DELTA_POLE, GAMMA_POLE, GAMMA_LOAN, GAMMA * ones4)
    wins[r["winner"]] += 1
freq_ne = wins / wins.sum()
print(f"\nE1b Born broken by non-equivariant closure (site 2 R_close=0.5):")
print(f"    predicted commit x branching = {np.round(pred, 4)}")
print(f"    MC                            = {np.round(freq_ne, 4)}"
      f"   (TVD pred vs MC = {tvd(freq_ne, pred):.4f})")
print(f"    TVD from bare Born            = {tvd(freq_ne, W4):.4f}"
      f"   <-- fair-sampling violation, not a Born failure")

ax = axes[0, 1]
ax.bar(x - 0.27, W4, 0.27, label="Born", color="#4477aa")
ax.bar(x, pred, 0.27, label=r"commit$\times$closure pred.", color="#ccbb44")
ax.bar(x + 0.27, freq_ne, 0.27, label="MC", color="#ee6677")
ax.set_title("E1b  non-equivariant closure:\nrecorded = first-closure, not first-touch")
ax.set_xlabel("site"); ax.legend(fontsize=8)

# ----------------------------------------------------------------------------
# E2 — antibunching bookkeeping (two-site beamsplitter)
# ----------------------------------------------------------------------------
W2 = np.array([0.5, 0.5]); ones2 = np.ones(2)
overlaps = 0; revs = 0; doubles = 0
for _ in range(N_TRIALS):
    r = run_trial(W2, R_CAP * ones2, R_CLOSE * ones2, R_REV * ones2,
                  DELTA_POLE, GAMMA_POLE, GAMMA_LOAN, GAMMA * ones2)
    overlaps += (r["overlap_windows"] > 0)
    revs += r["n_reversals"]
    # doubles stays 0: closure ends the run and recalls the other loan
frac_overlap = overlaps / N_TRIALS
print(f"\nE2  antibunching (50/50 split), N={N_TRIALS}:")
print(f"    runs with overlapping provisional windows (would-be coincidences):"
      f" {frac_overlap:.3%}")
print(f"    double registrations: {doubles}   (0 by budget construction)")
print(f"    mean reversals/run: {revs/N_TRIALS:.3f}")

ax = axes[0, 2]
ax.bar(["overlapping\nwindows", "double\nregistrations"],
       [frac_overlap, 0.0], color=["#ccbb44", "#ee6677"])
ax.set_title("E2  windows overlap; records never double")
ax.set_ylabel("fraction of runs")
ax.text(1, 0.002, "0 (budget)", ha="center", fontsize=10)

# ----------------------------------------------------------------------------
# E3 — click timing vs packet envelope: the closure-latency fingerprint
# ----------------------------------------------------------------------------
T0, SIG = 3.0, 0.6
def env_gauss(t):
    return np.exp(-((t - T0) ** 2) / (2 * SIG ** 2))

N_T = 12000
t_grid = np.linspace(0, 8, 400)
p_env = env_gauss(t_grid); p_env /= np.trapezoid(p_env, t_grid)

def timing_run(Rclose_val):
    ts = []
    for _ in range(N_T):
        r = run_trial(np.array([1.0]), np.array([R_CAP]),
                      np.array([Rclose_val]), np.array([R_REV]),
                      DELTA_POLE, GAMMA_POLE, GAMMA_LOAN, np.array([GAMMA]),
                      env=env_gauss, t_end=12.0)
        if r["winner"] is not None:
            ts.append(r["t_close"])
    return np.array(ts)

ts_fast = timing_run(50.0)     # closure much faster than envelope
ts_slow = timing_run(1.0)      # closure latency ~ envelope width
mean_shift_fast = ts_fast.mean() - np.trapezoid(t_grid * p_env, t_grid)
mean_shift_slow = ts_slow.mean() - np.trapezoid(t_grid * p_env, t_grid)
latency_fingerprint = ts_slow.mean() - ts_fast.mean()
print(f"\nE3  click timing vs envelope (Gaussian t0={T0}, sigma={SIG}):")
print(f"    fast closure (R_close=50): mean shift = {mean_shift_fast:+.3f}"
      f"  (commit-stage distortion, common to all rate models)")
print(f"    slow closure (R_close=1):  mean shift = {mean_shift_slow:+.3f}")
print(f"    FINGERPRINT (slow - fast) = {latency_fingerprint:+.3f}"
      f"   vs closure-latency prediction ~ 1/R_close = {1/1.0 - 1/50.0:.3f}")
print(f"    -> the model's one observable: a closure-latency convolution that")
print(f"       vanishes as R_close -> inf (degenerate with detector jitter")
print(f"       unless correlated with engineered reservoir properties)")

ax = axes[1, 0]
ax.plot(t_grid, p_env, "k-", lw=2, label=r"envelope $|f(t)|^2$ (QM)")
ax.hist(ts_fast, bins=60, density=True, alpha=0.55, color="#4477aa",
        label=r"MC, $R_{close}=50$")
ax.hist(ts_slow, bins=60, density=True, alpha=0.55, color="#ee6677",
        label=r"MC, $R_{close}=1$")
ax.set_title("E3  registration timing:\nlatency tail = falsifiable fingerprint")
ax.set_xlabel("t"); ax.set_ylabel("click density"); ax.legend(fontsize=8)

# ----------------------------------------------------------------------------
# E4 — sterility law + FTIR steal (wide vs narrow tongue probe)
# ----------------------------------------------------------------------------
deltas = np.linspace(0, 8, 200)
ax = axes[1, 1]
for g, c in [(1.0, "#ee6677"), (3.0, "#ccbb44"), (10.0, "#4477aa")]:
    ax.plot(deltas, [sterility(d, GAMMA_POLE, g) for d in deltas],
            color=c, label=fr"$\gamma_B={g:g}$")
ax.plot(deltas, [sterility(0, 2 * d, GAMMA) for d in deltas], "k--", lw=1,
        label=r"broadening only ($\Gamma=2\delta$, $\delta=0$)")
ax.axvline(DELTA_POLE, color="gray", ls=":", lw=1)
ax.text(DELTA_POLE + 0.1, 0.9, "pole used", fontsize=8, color="gray")
ax.set_title("E4a  sterility $S$: shift detunes (strong),\nbroadening alone is algebraic (weak)")
ax.set_xlabel(r"line pull $\delta$ (units of $\gamma$)"); ax.set_ylabel("S")
ax.legend(fontsize=8)

# FTIR steal: probe enabled t_on after first commit
def steal_prob(gamma_W, t_on, n=4000):
    wW = np.array([0.45, 0.45, 0.10])       # probe carries little native weight
    Rc = np.array([R_CAP, R_CAP, 40.0])     # ... but couples strongly
    got = 0; tot = 0
    for _ in range(n):
        r = run_trial(wW, Rc, R_CLOSE * np.ones(3), R_REV * np.ones(3),
                      DELTA_POLE, GAMMA_POLE, GAMMA_LOAN,
                      np.array([GAMMA, GAMMA, gamma_W]),
                      probe=dict(site=2, t_on=t_on))
        if r["winner"] is not None:
            tot += 1
            got += (r["winner"] == 2)
    return got / max(tot, 1)

t_ons = [0.05, 0.2, 0.5, 1.0, 2.0]
steal_wide = [steal_prob(10.0, t) for t in t_ons]
steal_narrow = [steal_prob(1.0, t) for t in t_ons]
print(f"\nE4  FTIR steal probability (probe on at t_on after first commit;")
print(f"    mean closure time ~ 1/R_close = {1/R_CLOSE:.2f}):")
print(f"    t_on:        {t_ons}")
print(f"    wide tongue (gamma_W=10):  {np.round(steal_wide, 3)}")
print(f"    narrow tongue (gamma_W=1): {np.round(steal_narrow, 3)}")

ax = axes[1, 2]
ax.plot(t_ons, steal_wide, "o-", color="#4477aa", label=r"wide tongue $\gamma_W=10$")
ax.plot(t_ons, steal_narrow, "s-", color="#ee6677", label=r"narrow tongue $\gamma_W=1$")
ax.axvline(1 / R_CLOSE, color="gray", ls=":", lw=1)
ax.text(1 / R_CLOSE + 0.05, max(steal_wide) * 0.9, "mean closure", fontsize=8,
        color="gray")
ax.set_title("E4b  FTIR: the Stage-2 window is stealable\n(by a wide tongue, before closure)")
ax.set_xlabel(r"probe switch-on delay $t_{on}$"); ax.set_ylabel("P(probe wins)")
ax.legend(fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.95])
out = __file__.replace(".py", ".png")
plt.savefig(out, dpi=110)
print(f"\nwrote {out}")
print("\nSummary: Born survives equivariant closure (E1a); breaks exactly as")
print("commit x closure when closure is biased (E1b — fair sampling, not Born);")
print("windows overlap but records never double (E2 — budget); the one")
print("fingerprint is the closure-latency tail in click timing (E3), vanishing")
print("as R_close -> inf; the window is stealable by a wide tongue and closed")
print("to everyone afterward (E4). Mechanism internally consistent; the budget")
print("(first-closure-wins) remains the nonlocal postulate (paper 3.3 wall i).")
