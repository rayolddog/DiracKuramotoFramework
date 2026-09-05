#!/usr/bin/env python3
"""Stage 2, Part B: sharpness of the crossover in Paper 2's own continuous model, the injected
Stuart-Landau oscillator, with a record channel and an optional counter-rotating drive.
See PREDICTIONS_STAGE2.md. Vectorised over the gain grid; Heun integration."""
import json, math, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DELTA, F = 1.0, 0.35
GS = np.linspace(-1.0, 1.5, 61)
T_TRANS, T_AVG = 200.0, 600.0


def run(D, grec, omega_d, dt, seed=1):
    rng = np.random.default_rng(seed)
    g = GS.astype(complex); a = np.full_like(g, 0.1 + 0.0j)
    def rhs(a, t):
        drive = F * (1.0 + (np.exp(2j * omega_d * t) if omega_d else 0.0))
        return (g - np.abs(a) ** 2) * a - 1j * DELTA * a - 0.5 * grec * a + drive
    t = 0.0; nsteps_tr = int(T_TRANS / dt); nsteps = int(T_AVG / dt)
    sig = math.sqrt(2 * D * dt) if D > 0 else 0.0
    def step(a, t):
        k1 = rhs(a, t); ap = a + dt * k1
        k2 = rhs(ap, t + dt)
        a = a + 0.5 * dt * (k1 + k2)
        if sig: a = a + sig * (rng.standard_normal(len(a)) + 1j * rng.standard_normal(len(a))) / math.sqrt(2)
        return a
    for _ in range(nsteps_tr):
        a = step(a, t); t += dt
    phase_acc = np.zeros(len(g)); u_acc = np.zeros(len(g)); p_acc = np.zeros(len(g)); prev = np.angle(a)
    for _ in range(nsteps):
        a = step(a, t); t += dt
        ph = np.angle(a); d = ph - prev; d = (d + math.pi) % (2 * math.pi) - math.pi
        phase_acc += d; prev = ph
        u_acc += np.abs(a) ** 2; p_acc += 2 * np.real(F * np.conj(a))
    return phase_acc / T_AVG, u_acc / nsteps, p_acc / nsteps


def onset(wind, thresh=1e-3):
    idx = np.where(np.abs(wind) > thresh)[0]
    return float(GS[idx[0]]) if len(idx) else float("nan")


if __name__ == "__main__":
    t0 = time.time(); out = {"g": GS.tolist(), "runs": []}
    configs = [  # (D, Gamma_rec, omega_d or 0 for RWA, dt)
        (0.0, 0.0, 0, 0.01), (1e-4, 0.0, 0, 0.01), (0.0, 0.1, 0, 0.01), (1e-4, 0.1, 0, 0.01),
        (0.0, 0.0, 40.0, 0.002), (0.0, 0.0, 10.0, 0.002), (0.0, 0.1, 40.0, 0.002),
    ]
    print(f"Hopf of the forced fixed point (analytic, RWA, D=0, Grec=0): solve (g/2)(g^2/4+1) = F^2 -> g_H = "
          f"{[g for g in np.linspace(0,1,100001) if abs((g/2)*(g*g/4+1)-F*F)<2e-5][0]:.3f}; Adler estimate (F/Delta)^2 = {F*F:.4f}")
    print(f"{'D':>7} {'Grec':>5} {'om_d':>5} {'onset g':>8}  |a|^2 at g = -0.5, 0, 0.1, 0.2, 0.3, 0.4, 0.6, 1.0   (winding rate in brackets)")
    for D, grec, om, dt in configs:
        wind, u, p = run(D, grec, om, dt)
        out["runs"].append(dict(D=D, grec=grec, omega_d=om, dt=dt, wind=wind.tolist(), u=u.tolist(), p=p.tolist(), onset=onset(wind)))
        samp = [(-0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.6, 1.0)]
        vals = "  ".join(f"{np.interp(gv, GS, u):.3f}({np.interp(gv, GS, np.abs(wind)):.3f})" for gv in samp[0])
        print(f"{D:7.0e} {grec:5.2f} {str(om if om else 'RWA'):>5} {onset(wind):8.3f}  {vals}"); sys.stdout.flush()
    # B2: max relative change of |a|^2 over any 0.1 window in g, RWA D=0 Grec=0
    u0 = np.array(out["runs"][0]["u"]); w0 = np.array(out["runs"][0]["wind"])
    k = int(round(0.1 / (GS[1] - GS[0])))
    rel = np.max(np.abs(u0[k:] - u0[:-k]) / np.minimum(u0[k:], u0[:-k]))
    print(f"\nB2: max relative change of |a|^2 over any 0.1-wide window in g (RWA, D=0, Grec=0): {rel:.3f}")
    lin = F * F / (GS ** 2 + DELTA ** 2)
    m = GS < 0
    print(f"B2: |a|^2 vs linear response F^2/(g^2+Delta^2) for g<0: max abs deviation {np.max(np.abs(u0[m]-lin[m])):.4f}")
    print("B1: winding rate near onset (RWA, D=0):", "  ".join(f"g={gv:.3f}:{np.interp(gv, GS, np.abs(w0)):.4f}" for gv in (0.20, 0.25, 0.30, 0.35, 0.40, 0.45)))
    json.dump(out, open(os.path.join(HERE, "stage2_stuart_landau_results.json"), "w"))
    print(f"\nrun time {time.time()-t0:.0f} s")
