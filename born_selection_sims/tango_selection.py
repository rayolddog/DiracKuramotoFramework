import numpy as np
rng = np.random.default_rng(7)

def trial_born_compare(amps, ntrials=2_000_000, noise=0.0):
    """Winner = argmax |A_i cos(theta_i)| (+ optional small vacuum seed noise).
    Compare empirical win freq to Born A^2/sum A^2."""
    A = np.asarray(amps, float)
    n = len(A)
    th = rng.uniform(0, 2*np.pi, size=(ntrials, n))
    s = np.abs(A * np.cos(th))
    if noise > 0:
        s = s + rng.normal(0, noise, size=s.shape)
    w = np.argmax(s, axis=1)
    emp = np.bincount(w, minlength=n) / ntrials
    born = A**2 / np.sum(A**2)
    return emp, born

configs = [
    [1.0, 1.0],
    [2.0, 1.0],
    [3.0, 1.0],
    [10.0, 1.0],
    [1.0, 1.0, 1.0],
    [2.0, 1.0, 1.0],
    [3.0, 2.0, 1.0],
    [1.0]*9 + [3.0],          # one bright site among many dim
    list(np.linspace(0.2, 2.0, 10)),  # gradient across patch
]

for amps in configs:
    emp, born = trial_born_compare(amps)
    err = np.max(np.abs(emp - born))
    print(f"A={np.round(amps,2)}")
    print(f"  empirical: {np.round(emp,4)}")
    print(f"  Born:      {np.round(born,4)}   max|diff|={err:.4f}")
