"""Does the PHYSICALLY DERIVED exchange kernel give Born, or only the ad hoc one?

Paper Appendix D uses  delta = step * min(e_i, e_j) * (+/-1)  -- chosen because it
is manifestly fair and cannot drive a site negative. But eliminating the shared
field from H_int = -sum_i d_i . E(x_i) gives resonant dipole-dipole exchange:
with amplitudes a_i and random relative phases (P3a),

    de_i = 2 Re(a_i^* da_i) ~ 2 Re(-i a_i^* sum_j J_ij a_j) dt  ~  sqrt(e_i e_j) * xi

i.e. a GEOMETRIC-MEAN kernel, not a min kernel. The geometric mean CAN drive a
site negative at finite step, so this is a step-convergence question: does the
derived kernel reproduce Born as step -> 0, and how often does clamping fire?
"""
import numpy as np


def run(weights, kernel, step, thresh=0.995, n_trials=20000,
        max_steps=4_000_000, seed=0):
    rng = np.random.default_rng(seed)
    w = np.asarray(weights, float)
    born = w / w.sum()
    N = len(w)
    e = np.tile(born, (n_trials, 1))
    winner = np.full(n_trials, -1, int)
    idx = np.arange(n_trials)
    clamps = 0
    moves = 0

    for k in range(max_steps):
        T = e.shape[0]
        if T == 0:
            break
        i = rng.integers(0, N, size=T)
        j = (i + rng.integers(1, N, size=T)) % N
        r = np.arange(T)
        ei, ej = e[r, i], e[r, j]

        if kernel == "min":
            mag = np.minimum(ei, ej)
        elif kernel == "geom":
            mag = np.sqrt(ei * ej)
        d = step * mag * np.where(rng.random(T) < 0.5, 1.0, -1.0)

        # clamp so no site goes negative; count how often this fires
        hi = np.where(d > 0, ej, ei)
        bad = np.abs(d) > hi
        clamps += int(bad.sum())
        moves += T
        d = np.where(bad, np.sign(d) * hi, d)

        e[r, i] = ei + d
        e[r, j] = ej - d

        done = e.max(axis=1) >= thresh
        if done.any():
            winner[idx[done]] = e[done].argmax(axis=1)
            keep = ~done
            e, idx = e[keep], idx[keep]

    p = np.bincount(winner[winner >= 0], minlength=N) / max((winner >= 0).sum(), 1)
    return born, p, clamps / max(moves, 1), (winner < 0).sum()


if __name__ == "__main__":
    ten = [1.0]*9 + [9.0]
    print("10-site, bright-site Born = 0.500;  step-convergence of each kernel\n")
    print(f"{'kernel':<8}{'step':>7}{'P(bright)':>12}{'dev':>9}{'clamp rate':>13}{'unfin':>8}")
    for kernel in ("min", "geom"):
        for step in (0.25, 0.10, 0.05, 0.02):
            born, p, cr, unfin = run(ten, kernel, step, n_trials=8000,
                                     seed=hash((kernel, step)) % 2**31)
            print(f"{kernel:<8}{step:>7.2f}{p[-1]:>12.4f}"
                  f"{p[-1]-born[-1]:>+9.4f}{cr:>13.2e}{unfin:>8d}")
