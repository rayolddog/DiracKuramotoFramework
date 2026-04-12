# Dirac-Kuramoto Framework

**The Dirac equation is a Kuramoto synchronization system. Mass is the coupling constant.**

---

## Overview

This repository presents an interpretive framework in which the Dirac equation, written in the chiral (Weyl) basis, has the mathematical structure of the Kuramoto phase-synchronization model. The left- and right-handed chiral sectors act as coupled oscillators --- a temporal clock and a spatial clock --- with the fermion mass playing the role of the Kuramoto coupling constant: **K = m**.

From this single identification, the framework derives or reinterprets:

- **Bell correlations** via a three-term spinor decomposition (E = E_LL + E_SS + E_LS = -cos(a-b))
- **Quantum measurement** as Kuramoto re-synchronization to a macroscopic detector bulk
- **The Born rule** (P = |psi|^2) from synchronization statistics of complex oscillators
- **The Heisenberg uncertainty principle** from the geometric orthogonality of the two clocks
- **Zitterbewegung** as the beat frequency between temporal and spatial clocks
- **The Higgs mechanism** as the process that sets K: K = y_f * v/sqrt(2) = m
- **Antiparticles** as time-reversed phase clocks, with CP violation as synchronization asymmetry
- **Gravity** as bulk clock synchronization (recovers Newton exactly)
- **Penrose objective reduction** as gravitational clock decoherence (tau = pi*hbar/E_G)
- **Temperature** as clock phase distribution width
- **Brownian motion** from clock desynchronization at molecular collisions
- **The quantum-classical transition** via Nelson's stochastic mechanics with a physical zero-point field

The framework does not modify the Dirac equation or challenge Bell's theorem. It provides a physical mechanism --- phase synchronization --- for processes that standard quantum mechanics describes but does not mechanistically explain.

---

## Documents

| File | Description |
|---|---|
| [PAPER_UNIFIED.md](PAPER_UNIFIED.md) | The full paper with all derivations and discussion |
| [EQUATIONS.md](EQUATIONS.md) | Compact equation reference (all key results in one document) |
| [equations.tex](equations.tex) | LaTeX source for the equation reference |
| [equations.pdf](equations.pdf) | Compiled PDF of the equation reference |

---

## The Central Result

In the Weyl basis, the Dirac equation separates into two coupled equations:

```
i * sigma-bar^mu * d_mu * psi_L = m * psi_R
i * sigma^mu * d_mu * psi_R = m * psi_L
```

Writing psi_L and psi_R as amplitude-phase oscillators, the phase dynamics are:

```
d(phi_L)/dt = omega_L + K * sin(phi_R - phi_L)
d(phi_R)/dt = omega_R + K * sin(phi_L - phi_R)
```

where **K = m** (the fermion mass). This is the Kuramoto synchronization equation for two coupled oscillators.

- **K = 0 (massless):** Chiral clocks decouple. Photons, massless neutrinos.
- **K > 0 (massive):** Clocks synchronize. The synchronized state is a particle with definite rest mass.
- **K = y_f * v/sqrt(2):** The Higgs vacuum expectation value sets K for each fermion species.

---

## Key Predictions and Consequences

### Born Rule (derived, not postulated)

The probability P = |alpha|^2 follows from the synchronization statistics of complex oscillators coupling to a detector bulk. The squared modulus is the natural probability measure because quantum probability equals wave intensity --- the coupling efficiency of a physical oscillator to a resonant absorber.

### Heisenberg Uncertainty (derived from clock geometry)

The position-momentum uncertainty relation Delta(x) * Delta(p) >= hbar/2 follows from the geometric orthogonality of temporal and spatial clocks. Locking one clock's phase forces the other into a frequency superposition via the twistor incidence relation. The zero-point phase noise sigma_phi(0) = 1/sqrt(2) rad is the irreducible floor.

### Measurement

A particle initially synchronized with its entangled partner re-synchronizes to the macroscopic detector bulk. The detector's overwhelming Kuramoto inertia (M_detector >> m_particle) forces conformity. Decoherence is not merely loss of phase coherence --- it is the positive process of gaining coherence with the bulk.

### Single-World Energy Accounting

Residual wavefunction amplitude that does not couple to the detector thermalizes into the electromagnetic vacuum as low-frequency radiation. No branches are created. Energy is conserved within a single world.

---

## What This Framework Does Not Claim

- It does not modify the Dirac equation or any of its predictions
- It does not challenge Bell's theorem
- It does not propose new physics --- it proposes a new *mechanism* for known physics
- The connections are genuine mathematical correspondences, presented as a framework rather than a complete theory
- Quantitative predictions (decoherence rates, thermalization timescales) remain to be derived from first principles

---

## Development History

This framework evolved from an earlier project, [BellWithoutFasterThanLight](https://github.com/rayolddog/BellWithoutFasterThanLight), which explored Bell correlations via local clock synchronization. The original repository contains the developmental Python simulations and the progression of ideas. This repository presents the mature, unified framework.

---

## Inspirations

- **de Broglie** --- pilot wave; the wave is real
- **Bohm** --- hidden variables; holographic order in nature
- **Dirac** --- the equation that started it all
- **Penrose** --- twistor theory, objective reduction, conformal cyclic cosmology
- **Kuramoto** --- phase synchronization of coupled oscillators (1975)
- **Nelson** --- stochastic mechanics; Brownian motion satisfies the Schrodinger equation (1966)
- **Bell** --- rigorously identifying what any local theory must satisfy

---

## About

Developed in conversation between a radiologist and Claude (Anthropic). The radiologist provided the physical intuitions; the AI developed the mathematics.

> *"I couldn't help thinking along those lines after studying some work by de Broglie and Bohm."*

---

## License

[MIT](LICENSE)
