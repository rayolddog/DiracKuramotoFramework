"""
Does noisy synchronization-capture reproduce the Born rule?

Question: a qubit state c0|0> + c1|1>, p1 = |c1|^2.
Can a dynamical capture process, started from a Born-AGNOSTIC initial
distribution, end in basin-1 with frequency p1 = |c1|^2 -- without putting
|c|^2 in by hand?

We test three things:
  Sim 1  Honest Langevin double-well capture (an Adler/Kuramoto-type SDE).
         Regimes: fast quench (low noise) and thermal (Kramers), with the
         well-tilt set either by an UNTUNED physical rule or TUNED to the
         Born answer.
  Sim 2  Competing-clock "race" model: two capture channels with rates
         r_i ~ |c_i|^gamma. Sweep gamma. Which exponent reproduces Born?

Seeded RNG -> reproducible.
"""
import numpy as np

rng = np.random.default_rng(20260614)

# ----------------------------------------------------------------------
# Sim 1: Langevin capture in a tilted double well
#   U(theta) = -A cos(2 theta) - h cos(theta)
#   minima at theta=0 (outcome 0) and theta=pi (outcome 1)
#   force = -dU/dtheta = -2A sin(2 theta) - h sin(theta)
#   outcome 1  <=>  cos(theta) < 0   (basin around pi)
# ----------------------------------------------------------------------
def run_langevin(p1, D, A, tilt_mode, n_trials=40000, n_steps=6000, dt=0.01, kappa=1.0):
    p0 = 1.0 - p1
    c0, c1 = np.sqrt(p0), np.sqrt(p1)
    if tilt_mode == "intensity":      # untuned, linear in intensity: h ~ |c0|^2-|c1|^2
        h = kappa * (p0 - p1)
    elif tilt_mode == "amplitude":    # untuned, linear in field amplitude
        h = kappa * (c0 - c1)
    elif tilt_mode == "tuned":        # h = (D/2) ln(p0/p1) -> Born by construction
        h = 0.5 * D * np.log(p0 / p1)
    else:
        raise ValueError(tilt_mode)

    theta = rng.uniform(-np.pi, np.pi, n_trials)   # Born-agnostic init
    s = np.sqrt(2.0 * D * dt)
    for _ in range(n_steps):
        force = -(2.0 * A * np.sin(2.0 * theta) + h * np.sin(theta))
        theta += force * dt + s * rng.standard_normal(n_trials)
    return np.mean(np.cos(theta) < 0.0)


# ----------------------------------------------------------------------
# Sim 2: competing exponential clocks, rate_i ~ |c_i|^gamma
#   P(channel 1 wins) = r1 / (r0 + r1)   (exact for exponentials)
# ----------------------------------------------------------------------
def run_race(p1, gamma, n_trials=200000):
    c0, c1 = np.sqrt(1 - p1), np.sqrt(p1)
    r0, r1 = c0**gamma, c1**gamma
    t0 = rng.exponential(1.0 / r0, n_trials)
    t1 = rng.exponential(1.0 / r1, n_trials)
    return np.mean(t1 < t0)


def table(title, ps, cols):
    print("\n" + title)
    print("  |c1|^2 (Born) | " + " | ".join(f"{name:>12}" for name, _ in cols))
    for p in ps:
        vals = " | ".join(f"{fn(p):>12.3f}" for _, fn in cols)
        print(f"  {p:>12.3f} | {vals}")


ps = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print("=" * 70)
print("SIM 1  Langevin double-well capture (uniform / Born-agnostic init)")
print("=" * 70)
table(
    "Regime: FAST QUENCH (low noise D=0.02, short time) -- frozen in initial basin",
    ps,
    [("quench", lambda p: run_langevin(p, D=0.02, A=1.0, tilt_mode="intensity",
                                       n_steps=600))],
)
table(
    "Regime: THERMAL (D=0.5, A=0.5, long time) -- Kramers occupation",
    ps,
    [
        ("untuned(I)", lambda p: run_langevin(p, D=0.5, A=0.5, tilt_mode="intensity")),
        ("untuned(amp)", lambda p: run_langevin(p, D=0.5, A=0.5, tilt_mode="amplitude")),
        ("TUNED->Born", lambda p: run_langevin(p, D=0.5, A=0.5, tilt_mode="tuned")),
    ],
)

print("\n" + "=" * 70)
print("SIM 2  Competing-clock race, rate ~ |c|^gamma  (which exponent = Born?)")
print("=" * 70)
table(
    "P(outcome 1) vs gamma   [gamma=2 means rate ~ intensity ~ amplitude^2]",
    ps,
    [
        ("g=1 (amp)", lambda p: run_race(p, 1.0)),
        ("g=2 (INT)", lambda p: run_race(p, 2.0)),
        ("g=4", lambda p: run_race(p, 4.0)),
    ],
)
print("\nBorn line is P = |c1|^2 (first column). Match it.")
