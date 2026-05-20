# Tests for the DiracKuramotoFramework

This directory contains numerical verification scripts for the claims in
`PAPER_UNIFIED.md` and `EQUATIONS.md`. Each script verifies a specific
claim, prints a pass/fail summary, and exits with status code 0 on
success.

The tests are organized by which section of the paper they verify, so a
reviewer can locate the corresponding numerical evidence for any
particular claim in the manuscript.

## Quick start

```bash
# Run a specific test
python tests/simplicial_alignment.py

# Run all tests in sequence
for f in tests/*.py; do
    echo "===== $f ====="
    python "$f"
done
```

Each script runs in a few seconds on a modern laptop. No GPU is required.
The framework's main applications (e.g., `ich-maxvit`) require heavier
infrastructure, but verification of the theoretical claims does not.

## Dependencies

- Python 3.10 or newer
- numpy
- scipy
- matplotlib (for the figure-producing scripts)
- qiskit (only for `bell_energy_test.py`, `bulk_sync_asymmetry.py`, `bulk_sync_hardware.py`)

The simplicial-Kuramoto tests in this directory do not depend on the
`simplicial-kuramoto` package of Arnaudon et al. — the relevant incidence
matrices and operators are constructed from first principles for
transparency. Reviewers can independently verify the constructions against
Nurisso et al. (2024) without installing additional packages.

## Test catalog

The classification below follows `PAPER_UNIFIED.md` §8.4 ("Categorization
of Supporting Numerical Code"). Categories are: **Evidential** (could have
falsified a central claim), **Quantitative prediction** (operationalizes a
testable claim), **Consistency check**, **Illustrative**, **Clarifying**
(disarms a misreading), **Pedagogical**, **Negative result**,
**Speculative**, **Mixed**.

### Evidential

| Script | What it does |
|---|---|
| `spin_statistics.py` | Six tests; fermion antisymmetry sign across 6 decades of v/c. Could have falsified the chiral-pair commitment (Appendix D); did not. |

### Quantitative prediction

| Script | What it does |
|---|---|
| `gravitational_bell.py` | Implements §5.4 CHSH(Δν) = 2√2·exp(−δφ²/2). The framework's sharpest distinguishable prediction. |
| `predictions.py` | Catalog of P1–P6 testable predictions, with retractions explicitly marked (P1, P3 falsified by km-scale Bell tests). |
| `bell_energy_test.py` | Qiskit CHSH simulation testing K(E) scalings vs photon energy; discriminates K∝1/E from K∝ω from null QM. |
| `sg_angular.py` | Stern-Gerlach angular dependence on local gravity (~4% effect). Tests gravitational Kuramoto coupling beyond Bell tests. |
| `bulk_sync_asymmetry.py` | Single-particle vs bulk phase-rotation scaling (√N vs N). Tests the measurement asymmetry of §3. |
| `predict_visibility_vs_mass.py` | Threshold-mass curve for a proposed matter-wave interferometer test of DK; companion figure `predict_visibility_vs_mass.png`. |

### Consistency check

| Script | What it does |
|---|---|
| `bulk_sync_hardware.py` | IBM Quantum hardware execution of the bulk-sync circuits with readout mitigation, dynamical decoupling, and ZNE. GHZ slope ≈ 1 confirmed; product slope below noise floor at K=0.06. Not framework-distinctive, but demonstrates digital-hardware reproduction of the simulation. |
| `overstreet_constraint.py` | Drops the Overstreet/Kasevich 2022 atom-interferometer result (Science 375, 226) onto the DK predicted phase + visibility curves. Verdict: Overstreet's sensitivity is ~10⁻¹⁴× too coarse to constrain DK's natural Γ_bulk/K_pair. |

### Illustrative

| Script | What it does |
|---|---|
| `dirac_extension.py` | Three-term Bell decomposition E_LL + E_SS + E_LS = −cos(a−b) to machine precision; visualizes the weight redistribution of Appendix A. |
| `gravity_twistor.py` | Poisson ↔ Kuramoto field-equation correspondence; twistor connection. Visualizes §3.5 and `EQUATIONS.md` §8. |
| `entangled_pair_two_stage.py` | Schematic figure for the two-stage measurement of a polarization-entangled photon pair (§3.4 / §4.4). |

### Clarifying

| Script | What it does |
|---|---|
| `bell_phase.py` | Establishes that the Malus-law toy is sub-classical (CHSH ≤ √2), distinct from the Dirac large block. Disarms the §A.5 conflation. |
| `local_causality.py` | Identifies where Bell's factorization actually breaks in MCI. Disarms the superdeterminism misreading (§7.6). |

### Pedagogical

| Script | What it does |
|---|---|
| `kuramoto_sync.py` | Two-oscillator synchronization dynamics under K > 0. Shows what K = m sync looks like in time. |
| `higgs_clock.py` | K = m identification and antiparticle reverse-clock dynamics. Illustrates `EQUATIONS.md` §6. |

### Negative result

| Script | What it does |
|---|---|
| `resynchronization_calc.py` | Tests whether re-synchronization alone reproduces −cos(a−b). Confirms the Dirac spinor structure is necessary; closes a misreading. |

### Speculative

| Script | What it does |
|---|---|
| `everett_thermal.py` | Single-world energy accounting (paper marks this speculative). Illustrates §3.8. |

### Mixed

| Script | What it does |
|---|---|
| `vacuum_temperature.py` | ZPF / temperature / orbitals (claims 1–3); Brownian retracted (claim 4). Three illustrative claims with one disclosed retraction (see `EQUATIONS.md` §10). |

### Appendix B: Cochain Ontology (simplicial Kuramoto alignment)

These three scripts support Appendix B and the alignment with the
simplicial Kuramoto framework of Nurisso et al. (Chaos 2024,
arXiv:2305.17977).

#### `simplicial_alignment.py`

**Verifies §B.4** (K = m at the cochain level).

Demonstrates that the chiral L-R Kuramoto reduction (`EQUATIONS.md` §6)
embeds as the manifold-like simple simplicial Kuramoto model on a
1-simplex, per Theorem 1 of Nurisso et al. Three sub-tests:

1. **Trajectory equivalence.** The framework's chiral form and Nurisso's
   incidence-matrix form integrate to bit-identical trajectories at
   δ_CP = 0. (Result: ~0 residual at machine precision.)
2. **Harmonic gauge mode.** U(1) phase shifts of the framework (`PAPER`
   §1.5 item 6) are equivalent to the harmonic phase-shift symmetry of
   Nurisso §III.E. (Result: ~1e-12 invariance.)
3. **Synchronization timescale.** τ_sync = 1/(2K) for the two-clock case
   across four decades of K. (Result: 0.4% accuracy in the linear
   regime, exactly matching the analytical correction at d₀ = 0.1.)

Runtime: ~1 second.

#### `hodge_decomposition.py`

**Verifies §B.5** (Hodge decomposition as coherence structure).

Demonstrates the orthogonal decomposition of edge cochains into
curl-free, harmonic, and divergence-free components, and the
independent evolution of each component under simplicial Kuramoto
dynamics. On a 4-node, 5-edge, 1-face simplicial complex (the smallest
with all three components nontrivial). Five sub-tests:

1. **Projector orthogonality.** P_cf, P_h, P_df are mutually orthogonal
   and sum to the identity. (Result: ~1e-16.)
2. **Component-norm evolution.** Visual confirmation that the curl-free
   and divergence-free components synchronize while the harmonic
   component is frozen.
3. **Harmonic inertness.** With ω = 0, the harmonic component drifts by
   less than 1e-15 over the full integration window.
4. **Orthogonality preservation.** The three Hodge subspaces stay
   orthogonal throughout evolution.
5. **Structural confinement.** The Kuramoto vector field never produces
   a harmonic component.

Runtime: ~1 second.

#### `hodge_dirac.py`

**Verifies §B.3** (the Hodge-Dirac operator) and **§B.4** (chiral
decomposition at the cochain level).

Demonstrates the central algebraic property that justifies the name
"Dirac" for the operator 𝒟 = d + δ: it is the first-order square root
of the Laplacian. Six sub-tests:

1. **𝒟² = Δ exactly.** The defining algebraic identity. (Result: 0.)
2. **{𝒟, Γ} = 0 exactly.** Anticommutation with the chirality grading
   Γ: ψ⁽ᵏ⁾ ↦ (−1)ᵏ ψ⁽ᵏ⁾, the discrete analog of γ₅. (Result: 0.)
3. **𝒟 = 𝒟ᵀ.** Symmetry (Hermiticity for real complexes). (Result: 0.)
4. **Spectrum symmetric about zero.** 4 positive, 4 negative, 2 zero
   eigenvalues — with the zero eigenvalues corresponding to harmonic
   modes (dim ker 𝒟 = β₀ + β₁ + β₂ = 1 + 1 + 0 = 2).
5. **Grade-pure harmonic basis.** Harmonic modes are computed
   separately for ker Δ⁰ (the constant function on nodes) and ker Δ¹
   (the open loop on edges), confirming the Hodge theorem.
6. **Γ maps ±λ eigenspaces.** For each positive eigenvalue λ, Γψ is
   verified to be an eigenvector with eigenvalue −λ. (Result: ~1e-15.)

Runtime: ~1 second.

## Continuous integration

*[Optional: add a GitHub Actions workflow that runs all tests on push.
Sample `.github/workflows/tests.yml`:]*

```yaml
name: Verification tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install numpy scipy matplotlib qiskit
      - run: |
          for f in tests/*.py; do
              echo "===== $f ====="
              python "$f"
          done
```

## Citing the test suite

When citing these tests in a publication, please cite the framework
itself via the Zenodo DOI in `CITATION.cff` at the repository root.

## License

Same as the parent repository.
