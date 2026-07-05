# The Many Clocks Interpretation of Quantum Mechanics

**Every particle carries an internal phase clock. Measurement is dissipative re-synchronization to a macroscopic bulk. No observer is needed; no branching occurs. The Dirac mass term is the off-diagonal chiral coupling: K = m.**

---

## Overview

This repository presents the **Many Clocks Interpretation of Quantum Mechanics (MCI)**: an interpretive framework in which the Dirac equation, written in the chiral (Weyl) basis, exposes the fermion mass as the off-diagonal coupling between two chiral phase clocks --- a temporal clock and a spatial clock --- with coupling strength **K = m**. In the closed system this coupling is unitary: diagonalizing it reproduces E = √(p²+m²), with the de Broglie carrier and the Zitterbewegung beat as its normal modes. Phase-locking proper is a dissipative, open-system phenomenon, and in this framework it is what measurement is.

The name is a deliberate echo of, and contrast to, Many-Worlds: where MWI preserves unitarity by branching the universe at each measurement, MCI preserves a single world by treating each particle as carrying its own physical phase clock, with measurement as local synchronization between clocks. No observer and no branching are required, and the framework offers a positive dynamical mechanism for decoherence: phase overwriting at each interaction event. The current manuscript is candid that the framework carries a *physical preferred frame* --- the rest frame of the bulk/vacuum reference --- entering only through measurement (Stage 2), while the unitary dynamics stays exactly Lorentz covariant.

**The current paper is _"Two Regimes of the Chiral Mass Coupling"_ ([current_revision_DK_paper.md](current_revision_DK_paper.md)) --- the more conservative and more rigorous statement of the framework, and the one to read first.** Beyond the closed/open (two-regimes) core, it now makes explicit *when* the dissipative regime engages: a new **§2.5** establishes that the vacuum coupling acts only where an external structure deforms the wave's amplitude --- a material boundary, a field gradient, or spacetime curvature --- while a freely propagating particle stays coherent under the Madelung (pilot-wave) guidance law the framework adopts in that limit. For the Born measure, the revised paper identifies a candidate route --- *relaxation to quantum equilibrium* in the sense of Valentini's subquantum H-theorem --- while remaining explicit that it is not yet derived. ([PAPER_UNIFIED.md](PAPER_UNIFIED.md) is the earlier, longer, now-superseded version, retained for reference.)

From this single identification, the framework derives or reinterprets the items
below. *(Note: some entries record first-version results retained for the
historical record; the current revision is more conservative, and where the two
differ the bullet says so. The paper itself is the authority on what is currently
asserted.)*

- **Bell correlations** via the standard Dirac spinor structure (block decomposition E = E_LL + E_SS + E_LS = -cos(a-b) is a consistency check, not a derivation)
- **Quantum measurement** as Kuramoto re-synchronization to a macroscopic detector bulk
- **The Born rule** (P = |psi|^2) reframed, for outcome channels of equal energy per quantum, as quantum-number partition: |psi|^2 is the energy density of the real psi field, with stochasticity from unbiased background fluctuations at the synchronization event (the unequal-energy restriction is itself explained in the current revision, §3.7: electromagnetic detectors couple to the charge density j⁰ = |ψ|², so Born weights are energy-independent, and only gravity reads E|ψ|²)
- **The Heisenberg uncertainty principle** reframed as the Fourier/Gabor bandwidth theorem for a real wave (the first version's clock-geometry/twistor derivation is superseded and not asserted by the current paper)
- **Zitterbewegung** as the beat frequency between temporal and spatial clocks
- **The Higgs mechanism** as the process that sets K: K = y_f * v/sqrt(2) = m
- **Antiparticles** as time-reversed phase clocks, with CP violation as a chiral phase asymmetry
- **Gravity** confined to two honest roles in the current paper (§4.4): the ordinary redshift of the detectors' reference clocks (basis of the §6 candidate test) and the electromagnetically-quiet Penrose–Diósi regime — the first-version "gravity as bulk synchronization, recovering Newton" reading is superseded, and the naive pair-counted rate Γ_grav = GM²/(ℏΔz) is **retracted as a dimensional artifact** (§4.4)
- **Penrose objective reduction** as gravitational clock decoherence (tau = pi*hbar/E_G)
- **Photons** treated via Riemann–Silberstein form (F = E + iB), with K_γ ~ ω = E/ℏ for photon-detector sync; gravitational classicalization channel silent for photons (perpetually quantum until measured) — *first-version material; not carried in the current revision*
- **Temperature** as clock phase distribution width
- **The quantum-classical transition** via Nelson's stochastic mechanics with a physical zero-point field (the molecular Brownian extension is an open question; see EQUATIONS.md §10)

The framework does not modify the Dirac equation or challenge Bell's theorem. It reads mass as the off-diagonal chiral coupling and supplies a physical mechanism --- dissipative phase synchronization to a bulk --- for the measurement and decoherence processes that standard quantum mechanics describes but does not mechanistically explain.

---

## Documents

| File | Description |
|---|---|
| [current_revision_DK_paper.md](current_revision_DK_paper.md) | **"Two Regimes of the Chiral Mass Coupling" — the current, canonical manuscript** (the living working copy; start here) |
| [Two_Regimes_of_Chiral_Mass_Coupling.tex](Two_Regimes_of_Chiral_Mass_Coupling.tex) | LaTeX build source for the "Two Regimes" paper |
| [EQUATIONS.md](EQUATIONS.md) | Compact equation reference (all key results in one document) |
| [equations.tex](equations.tex) | LaTeX source of the equation reference |
| `resolution/` | Referee-dispute resolution artifacts and the Appendix D reproduction script (`precession_radius_two_zeros.py`) |
| [PAPER_UNIFIED.md](PAPER_UNIFIED.md) | Earlier, longer first version (the original "Many Clocks" long form) — *superseded by the current revision; retained as the first-version record* |
| [paper.pdf](paper.pdf) / [paper.tex](paper.tex) | First-version "Many Clocks" paper — compiled PDF (submission-of-record) / LaTeX |
| [build_pdfs.sh](build_pdfs.sh) | Pandoc + xelatex build script |

*Equation rendering: to read the LaTeX in a browser without building a PDF, open any `.md` with the local MathJax viewer at `~/Desktop/Tools/equation-preview.html`.*

### Companion papers (in development)

The following companion papers extend the framework into specific
experimental and astrophysical regimes. They are **work-in-progress drafts
not yet ready for journal submission**, posted here for transparency and
to invite discussion.

| File | Description | Status |
|---|---|---|
| [AB_VISIBILITY_PAPER.md](AB_VISIBILITY_PAPER.md) | AB visibility envelope as a test of Dirac–Kuramoto vacuum locking | **Development phase — not for citation** |
| [EMERGENT_FIELDS_PAPER.md](EMERGENT_FIELDS_PAPER.md) | Synchronization arrays as an analog-simulation platform for chiral fermions, topological mass, and fermionization | **Development phase — not for citation** |
| [DISCRETIZATION_AS_SYNC_PAPER.md](DISCRETIZATION_AS_SYNC_PAPER.md) | Discretization as synchronization — quantum spectra without quantizing spacetime | **Development phase — not for citation** |
| [COSMIC_EXPANSION_PAPER.md](COSMIC_EXPANSION_PAPER.md) | Cosmic-expansion companion (bulk-sync cosmology) | **Development phase — not for citation** |
| [LIGO_SIDEREAL_TEST_T5.md](LIGO_SIDEREAL_TEST_T5.md) | Proposed LIGO sidereal-anisotropy test of the Vacuum Preferred-Frame Hypothesis | **Working note** |
| [RESULTS_EMERGENT_FIELDS.md](results/RESULTS_EMERGENT_FIELDS.md) | Numerical results — field multiplicity from one phase-oscillator substrate | **Working note** |

## Numerical Verification Scripts

Each Python script verifies specific claims made in the paper. They can be run independently.

| Script | Verifies |
|---|---|
| `tests/kuramoto_sync.py` | Core Kuramoto phase dynamics --- particles synchronizing to detector bulk |
| `tests/bell_phase.py` | Bell inequality comparison: LHV vs phase-clock vs QM correlations |
| `tests/dirac_extension.py` | Three-term Bell decomposition (E_LL + E_SS + E_LS = -cos(a-b)) to machine precision |
| `tests/higgs_clock.py` | Higgs as the chiral coupling (K = m); antiparticles as reversed clocks; CP violation |
| `tests/gravity_twistor.py` | Gravity as bulk synchronization; Penrose collapse; twistor connection |
| `tests/local_causality.py` | Full causal timeline showing no FTL required for Bell correlations |
| `tests/predictions.py` | Five testable predictions where the framework differs from standard QM |
| `tests/vacuum_temperature.py` | Temperature as clock phase width; quantum-classical transition. (Note: contains a Brownian-motion section that uses a phenomenological K decoupled from the framework's K = m; see disclaimer in file and EQUATIONS.md §10.) |
| `tests/everett_thermal.py` | Single-world thermalization of residual wavefunction amplitude |
| `tests/bell_energy_test.py` | CHSH Bell test at different photon energies under Kuramoto model |
| `tests/gravitational_bell.py` | Bell correlation degradation from gravitational decoherence |
| `tests/bulk_sync_asymmetry.py` | Bulk vs single-particle synchronization asymmetry (statevector simulation) |
| `tests/bulk_sync_hardware.py` | IBM Quantum hardware execution of the bulk-sync circuits with readout mitigation, dynamical decoupling, and zero-noise extrapolation |
| `tests/resynchronization_calc.py` | Measurement as re-synchronization producing -cos(a-b) |
| `tests/sg_angular.py` | Stern-Gerlach splitting modulation with gravitational angle |
| `tests/spin_statistics.py` | Spin-statistics consistency check via the chiral pair structure |
| `tests/entangled_pair_two_stage.py` | Schematic figure for the two-stage measurement of a polarization-entangled photon pair (Paper §3.4 / §4.4) |

### Requirements

```
numpy
scipy
matplotlib
qiskit          # required by tests/bell_energy_test.py and tests/bulk_sync_asymmetry.py
```

### Running

```bash
python tests/dirac_extension.py    # verify three-term decomposition
python tests/higgs_clock.py         # Higgs-Kuramoto identification
python tests/gravity_twistor.py     # gravity and Penrose collapse
python tests/vacuum_temperature.py  # temperature and Brownian motion
```

---

## The Central Result

In the Weyl basis, the Dirac equation separates into two coupled equations:

```
i * sigma-bar^mu * d_mu * psi_L = m * psi_R
i * sigma^mu * d_mu * psi_R = m * psi_L
```

The mass is the single off-diagonal entry of the Dirac Hamiltonian in this basis --- the coupling K = m between the two chiral clocks. Writing psi_L and psi_R as amplitude-phase oscillators (Madelung-type polar decomposition) in the rest frame, the reduction is:

```
d(phi_L)/dt = -K * sqrt(rho_R/rho_L) * cos(phi_R - phi_L)
d(rho_L)/dt = +2K * sqrt(rho_L * rho_R) * sin(phi_R - phi_L)
```

where **K = m** (the fermion mass). The coupling appears as a *cosine in the phase equation* --- the reverse of the Kuramoto model --- and the phase difference has no attractor: on the symmetric manifold rho_L = rho_R it is stationary for every phase difference, as must hold for closed unitary evolution. The motion is coherent normal-mode precession, not phase-locking. Diagonalizing the coupling gives eigenfrequencies ±√(k²+m²) = ±E (the relativistic dispersion); the normal modes are the de Broglie carrier and the Zitterbewegung beat (rest-frame beat 2m = 2mc²/ℏ). Genuine Kuramoto/Adler phase-locking enters only when the system is opened to a dissipative bulk --- that is the measurement step (Paper §2.2, §2.3, §3, Appendix D).

- **K = 0 (massless spin-½):** Chiral sectors decouple --- idealized massless neutrinos.
- **K > 0 (massive):** The chiral clocks couple; the symmetric normal mode is a particle with definite rest mass.
- **K = y_f * v/sqrt(2):** The Higgs vacuum expectation value sets K for each fermion species.
- **Photons (spin-1):** Not Dirac particles. Treated separately via Riemann–Silberstein form, with K_γ ~ ω = E/ℏ for photon-detector sync (Paper §5).

---

## Key Predictions and Consequences

### Born Rule (reframed as quantum-number partition, equal-energy channels)

|psi|^2 is the energy density of the real psi field --- not a probability postulate. The synchronization event transfers wave energy from the particle to one detector channel. Which channel wins in any individual event depends on the unbiased zero-point + thermal background fluctuations at the moment of contact. For outcome channels carrying equal energy per quantum (spin, polarization, fixed-frequency detector clicks), long-run frequencies of channel selection converge to P(channel) = |amplitude|^2, read as a frequentist statement about quantum-number partition rather than as an independent probability axiom. The reading does not extend to channels of unequal energy, and does not by itself fix the squared functional form (Paper §4).

### Heisenberg Uncertainty (reframed as wave bandwidth)

For a real wave, Delta(x) * Delta(p) >= hbar/2 is the Fourier/Gabor bandwidth theorem — a property of any wave ontology rather than a separate quantum postulate. The first version's stronger claim (a derivation from the geometric orthogonality of temporal and spatial clocks via the twistor incidence relation, with a sigma_phi(0) = 1/sqrt(2) rad floor) is superseded and not asserted by the current paper.

### Measurement

A particle initially synchronized with its entangled partner re-synchronizes to the macroscopic detector bulk. The detector's overwhelming Kuramoto inertia (M_detector >> m_particle) forces conformity. Decoherence is not merely loss of phase coherence --- it is the positive process of gaining coherence with the bulk.

### Single-World Accounting

Residual coherence that does not couple to the detector is scrambled into the bulk's uncontrolled modes — globally unitary, locally irreversible (current paper §3.1). No branches are created; one world suffices. The first version's more specific claim (residual amplitude thermalizing into the electromagnetic vacuum as low-frequency radiation) is superseded.

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
