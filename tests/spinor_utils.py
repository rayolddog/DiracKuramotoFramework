"""
spinor_utils.py — Shared Dirac/Pauli spinor utilities
=====================================================

Primitive spinor objects shared by more than one verification script
(currently dirac_extension.py and spin_statistics.py). Factored out of
dirac_extension.py so the two scripts import one source of truth rather
than one depending on the other.

Natural units throughout: m = c = ℏ = 1.

Contents:
  - Pauli matrices σ1, σ2, σ3 and helpers I2, O2
  - energy(p, m), mixing_angle(p, m)
  - dirac_spinor(p_z, spin_up, m): positive-energy 4-spinor
  - singlet_dirac(p, m), singlet_pauli(): two-particle singlets
  - spin_op_2 / spin_op_4 / spin_op_large_only / spin_op_small_only
"""

import numpy as np


# ─── Pauli matrices ───────────────────────────────────────────────────────────

σ1 = np.array([[0, 1], [1, 0]], dtype=complex)
σ2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
σ3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
O2 = np.zeros((2, 2), dtype=complex)


def spin_op_2(angle):
    """2×2 spin operator for measurement along (sin θ, 0, cos θ)."""
    return np.cos(angle) * σ3 + np.sin(angle) * σ1


# ─── Dirac spinors (natural units: m = c = ℏ = 1) ───────────────────────────

def energy(p, m=1.0):
    return np.sqrt(p**2 + m**2)


def dirac_spinor(p_z, spin_up: bool, m=1.0):
    """
    Positive-energy Dirac spinor for momentum p_z along z.
    u(p, ↑) = N · [1, 0,  r, 0]^T
    u(p, ↓) = N · [0, 1,  0,-r]^T
    where r = p/(E+m) = tan(θ_rel/2),  N = √((E+m)/(2E))
    """
    E = energy(p_z, m)
    r = p_z / (E + m)                         # small/large ratio
    N = np.sqrt((E + m) / (2 * E))            # normalisation
    if spin_up:
        return N * np.array([1, 0, r, 0], dtype=complex)
    else:
        return N * np.array([0, 1, 0, -r], dtype=complex)


def mixing_angle(p_z, m=1.0):
    """
    θ_rel: the rotation angle between time-phase and property vectors.
    tan(θ/2) = |p|/(E+m)  →  θ = 2·arctan(|p|/(E+m))
    """
    E = energy(p_z, m)
    return 2 * np.arctan(abs(p_z) / (E + m))


# ─── Singlet states ──────────────────────────────────────────────────────────

def singlet_dirac(p, m=1.0):
    """
    Singlet of two spin-1/2 Dirac particles:
      A with momentum +p along z
      B with momentum -p along z

    |Ψ⟩ = (u_A(+p,↑) ⊗ u_B(−p,↓) − u_A(+p,↓) ⊗ u_B(−p,↑)) / √2
    """
    uA_up = dirac_spinor(+p, True,  m)
    uA_dn = dirac_spinor(+p, False, m)
    uB_up = dirac_spinor(-p, True,  m)
    uB_dn = dirac_spinor(-p, False, m)
    return (np.kron(uA_up, uB_dn) - np.kron(uA_dn, uB_up)) / np.sqrt(2)


def singlet_pauli():
    """Standard NR 4-component singlet (2×2)."""
    up = np.array([1, 0], dtype=complex)
    dn = np.array([0, 1], dtype=complex)
    return (np.kron(up, dn) - np.kron(dn, up)) / np.sqrt(2)


# ─── Measurement operators ────────────────────────────────────────────────────

def spin_op_4(angle):
    """
    4×4 Dirac spin operator: Σ·n̂ = [[σ·n̂, 0], [0, σ·n̂]]
    Measures spin in BOTH large and small subspaces.
    """
    s = spin_op_2(angle)
    return np.block([[s, O2], [O2, s]])


def spin_op_large_only(angle):
    """4×4 operator that measures only the large (upper) component."""
    s = spin_op_2(angle)
    return np.block([[s, O2], [O2, O2]])


def spin_op_small_only(angle):
    """4×4 operator that measures only the small (lower) component."""
    s = spin_op_2(angle)
    return np.block([[O2, O2], [O2, s]])
