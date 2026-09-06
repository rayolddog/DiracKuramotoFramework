#!/usr/bin/env python3
"""The entanglement cut: two two-level absorbers under three noises, exact Lindblad propagation;
concurrence vs the local (single-quantum), double-quantum and zero-quantum coherences.
Predictions in PREDICTIONS_entanglement_cut.md, fixed first."""
import math, numpy as np
from scipy.linalg import expm

I2 = np.eye(2); sz = np.diag([1.0, -1.0]); sm = np.array([[0, 0], [1, 0]], float)   # basis |e>=0, |g>=1
def kron(a, b): return np.kron(a, b)
SZA, SZB, SMA, SMB = kron(sz, I2), kron(I2, sz), kron(sm, I2), kron(I2, sm)

def liouvillian(Ls):
    d = 4; L = np.zeros((d*d, d*d), complex)
    for c in Ls:
        cd = c.conj().T; cdc = cd @ c
        L += np.kron(c, c.conj()) - 0.5*np.kron(cdc, np.eye(d)) - 0.5*np.kron(np.eye(d), cdc.T)
    return L
def evolve(rho0, L, t):
    return (expm(L*t) @ rho0.reshape(-1)).reshape(4, 4)
def concurrence(rho):
    sy = np.array([[0, -1j], [1j, 0]]); Y = np.kron(sy, sy)
    R = rho @ Y @ rho.conj() @ Y
    ev = np.sort(np.sqrt(np.abs(np.linalg.eigvals(R))))[::-1]
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])
def ket(*amps):  # amplitudes on |ee>,|eg>,|ge>,|gg>
    v = np.array(amps, complex); v /= np.linalg.norm(v); return np.outer(v, v.conj())
STATES = {"Psi+": ket(0, 1, 1, 0), "Phi+": ket(1, 0, 0, 1), "Phi_tilt(0.2,0.8)": ket(math.sqrt(0.8), 0, 0, math.sqrt(0.2)), "product |eg>": ket(0, 1, 0, 0)}
gamma = 1.0
NOISES = {"independent dephasing": liouvillian([math.sqrt(gamma/2)*SZA, math.sqrt(gamma/2)*SZB]),
          "correlated dephasing":  liouvillian([math.sqrt(gamma/2)*(SZA + SZB)]),
          "independent damping":   liouvillian([math.sqrt(gamma)*SMA, math.sqrt(gamma)*SMB])}
def local_coh(rho):  # single-quantum coherence of A: 2|rho_A,eg|
    rA = np.array([[rho[0,0]+rho[1,1], rho[0,2]+rho[1,3]], [rho[2,0]+rho[3,1], rho[2,2]+rho[3,3]]]); return 2*abs(rA[0,1])
TS = [0.0, 0.1, 0.25, 0.5, 0.693, 0.75, 1.0, 1.5, 2.0, 3.0]
for noise, L in NOISES.items():
    print(f"\n=== {noise} (rate 1) ===")
    print(f" {'state':<20} {'t':>6} {'C':>8} {'c_A':>7} {'c_A*c_B':>8} {'DQ':>7} {'ZQ':>7}   analytic")
    for name, rho0 in STATES.items():
        for t in TS:
            rho = evolve(rho0, L, t); C = concurrence(rho); cA = local_coh(rho)
            rB = np.array([[rho[0,0]+rho[2,2], rho[0,1]+rho[2,3]], [rho[1,0]+rho[3,2], rho[1,1]+rho[3,3]]]); cB = 2*abs(rB[0,1])
            DQ, ZQ = 2*abs(rho[0,3]), 2*abs(rho[1,2]); p = 1 - math.exp(-t)
            an = {"independent dephasing": math.exp(-2*t) if name in ("Psi+","Phi+") else float("nan"),
                  "correlated dephasing": (1.0 if name=="Psi+" else math.exp(-4*t) if name=="Phi+" else float("nan")),
                  "independent damping": (math.exp(-t) if name=="Psi+" else (1-p)**2 if name=="Phi+" else 2*(1-p)*max(0, 0.4-0.8*p) if name.startswith("Phi_tilt") else float("nan"))}[noise]
            print(f" {name:<20} {t:6.3f} {C:8.5f} {cA:7.4f} {cA*cB:8.5f} {DQ:7.4f} {ZQ:7.4f}   {an:8.5f}")
# finite-bath cross-check: |Psi+> with N modes per absorber, single-excitation sector
print("\n=== finite record channels, |Psi+> under independent damping (Gamma = 1, bandwidth 40) ===")
def finite_bath_C(N, t, B=40.0):
    g = math.sqrt(1.0*B/(2*math.pi)); gk = g/math.sqrt(N); eps = np.linspace(-B/2, B/2, N) if N > 1 else np.array([0.0])
    d = 2 + 2*N; H = np.zeros((d, d))
    for a in range(2):
        for k in range(N):
            i = 2 + a*N + k; H[i, i] = eps[k]; H[a, i] = H[i, a] = gk
    w, V = np.linalg.eigh(H); psi = np.zeros(d, complex); psi[0] = psi[1] = 1/math.sqrt(2)
    psi = V @ (np.exp(-1j*w*t) * (V.conj().T @ psi))
    # reduced two-absorber state in {|eg>,|ge>} + |gg> (bath traced)
    a, b = psi[0], psi[1]; pgg = 1 - abs(a)**2 - abs(b)**2
    rho = np.zeros((4, 4), complex); rho[1,1] = abs(a)**2; rho[2,2] = abs(b)**2; rho[1,2] = a*np.conj(b); rho[2,1] = np.conj(rho[1,2]); rho[3,3] = pgg
    return concurrence(rho)
print(f" {'N':>4} " + " ".join(f"{t:>7.2f}" for t in (0.5, 1.0, 2.0, 3.0, 5.0)) + "   (exp(-t): " + " ".join(f"{math.exp(-t):.3f}" for t in (0.5,1,2,3,5)) + ")")
for N in (1, 4, 16, 64):
    print(f" {N:4d} " + " ".join(f"{finite_bath_C(N, t):7.3f}" for t in (0.5, 1.0, 2.0, 3.0, 5.0)))
