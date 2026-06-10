# Tests for the DiracKuramotoFramework

Numerical verification scripts for **`PAPER_REVISED.md`** — *"Two Regimes of
the Chiral Mass Coupling: Quantum Measurement as Bath-Induced Synchronization."*
Each script runs in a few seconds, prints its own summary, and exits 0 on
success.

> **Scope discipline (why this suite is small).** The revised paper concedes
> Stage 1 (resonant capture) to **standard QED** and the Bell correlations to
> **standard QM** (adopted, not derived; Appendix A shows a clock-as-local-
> variable model is sub-classical). A script therefore earns its place only if
> it probes something framework-*specific*: the closed→open boundary (§2.2–2.3),
> the sub-classical no-go (App A), the honest Born-rule negative (§3.3/§7.3),
> the spin-statistics consistency check (App B), or the one candidate signature
> (§6). Scripts that merely reproduced a standard QED/QM result, or supported
> sections cut from the revised paper, were removed (see *Removed in this
> revision* below).

## Quick start

```bash
export MPLBACKEND=Agg          # headless figure backend
python tests/bell_phase.py     # run one script
for f in tests/*.py; do        # run all (skips the hardware script below)
    [ "$(basename "$f")" = bulk_sync_hardware.py ] && continue
    [ "$(basename "$f")" = spinor_utils.py ] && continue
    echo "===== $f ====="; python "$f"
done
```

## Dependencies

- Python 3.10+
- numpy, scipy, matplotlib
- qiskit — only for `bulk_sync_asymmetry.py` and `bulk_sync_hardware.py`
- `bulk_sync_hardware.py` additionally needs live IBM Quantum credentials and
  is **not** part of the offline suite.

## Shared module

| File | Role |
|---|---|
| `spinor_utils.py` | Pauli/Dirac spinor primitives (σ-matrices, `dirac_spinor`, `mixing_angle`, the singlets, 4×4 spin operators). Imported by `dirac_extension.py` and `spin_statistics.py` so they share one source of truth. Not a test. |

## Test catalog

### Framework-distinctive core

| Script | Verifies |
|---|---|
| `bell_phase.py` | **Appendix A.** The clock-as-local-variable (Malus) model gives `E = −½cos(Δ)`, CHSH ≤ √2 — *sub-classical*. This is the load-bearing no-go: the correlations must come from standard QM, so synchronization is confined to the local measurement mechanism. |
| `resynchronization_calc.py` | **§3.3 / §7.3 (negative result).** The Dirac/Kuramoto dynamics do **not** reproduce the Born rule `cos²` — definiteness only, "why squared" left open. Confirms the paper's honest scoping. |
| `higgs_clock.py` | **§2.2–2.4.** `K = m`; the *closed* coupling is unitary normal-mode (Rabi/ZBW) precession with no attractor, vs the *open* dissipative Adler lock. (CP-violation / baryogenesis panels are marked **exploratory — not in the revised paper**.) |
| `kuramoto_sync.py` | **§2.3.** The dissipative Adler/Kuramoto lock itself — what `K = m` synchronization looks like in time once a bath is present. |
| `spin_statistics.py` | **Appendix B (consistency check).** Fermion exchange sign = −1 across six decades in momentum; the Kuramoto phase ODE alone is sign-free. Confirms the chiral-pair reframing does not break spin-statistics. |

### The one candidate signature

| Script | Verifies |
|---|---|
| `predictions.py` | **§6.** P1–P5 are framed as *consistency with standard QM*; P6/P6b are the linewidth-dependent gravitational Bell effect, `δφ = ω·ΔΦ/(c²·Δν)`, `CHSH = 2√2·exp(−δφ²/2)` — explicitly a test of the **non-covariant postulate H′ of §6.2**, not the framework's core. |

### Stage-2 measurement asymmetry (incl. hardware)

| Script | Verifies |
|---|---|
| `bulk_sync_asymmetry.py` | **§3.3.** Single-particle vs bulk phase-rotation scaling (√N vs N) — the M ≫ m inertia asymmetry that delivers one definite outcome. Discriminating variable is circuit structure (hardware-testable), not photon energy. |
| `bulk_sync_hardware.py` | IBM Quantum execution of the bulk-sync circuits (readout mitigation, dynamical decoupling, ZNE). Demonstrates digital-hardware reproduction of the simulation. Needs live hardware. |

### Illustrative

| Script | Verifies |
|---|---|
| `dirac_extension.py` | The three-term block decomposition `E_LL + E_SS + E_LS = −cos(a−b)` — *an identity, not a discovery*; visualizes how the block weights redistribute with v/c. ZBW described as the ±E normal-mode splitting (§2.4). |
| `entangled_pair_two_stage.py` | Schematic of the two-stage (capture → bulk relaxation) measurement of a polarization-entangled pair (§3.1, §5). Stage-2 relaxation labeled as EM-mediated (Γ_cap ~ K_eff, T1/T2). |

### Companion paper [26] (AB-Visibility Envelope)

These support the cited companion preprint, *not* the main paper's claims.

| Script | Verifies |
|---|---|
| `overstreet_constraint.py` | Whether Overstreet/Kasevich 2022 already constrains the gravitational-visibility coefficient. Uses the Penrose–Diósi self-energy scale as an order-of-magnitude reference only (the `Gm²/ℏΔz` form is **not** a framework rate; §4.4). |
| `predict_visibility_vs_mass.py` | Threshold-mass curve for a matter-wave interferometer test, via the Penrose–Diósi branch. |

### Mixed / with disclosed caveats

| Script | Verifies |
|---|---|
| `everett_thermal.py` | Single-world energy accounting (§3.1): residual amplitude thermalizes rather than branching. Local accounting only; the earlier cosmological-constant speculation is dropped. |
| `vacuum_temperature.py` | ZPF / temperature / orbitals (§4.3). The Brownian-motion section uses a phenomenological `K` decoupled from `K = m` and is flagged in-file (see `EQUATIONS.md` §10). |

## Removed in this revision

Eight scripts were deleted to keep the suite aligned with the revised paper:

- **Redundant with / repudiated by the revised paper:** `local_causality.py`
  (argued the abandoned *local* explanation of Bell correlations — the framework
  is single-world but **nonlocal**, §7.2/§7.5); `bell_energy_test.py`
  (CHSH-vs-photon-**energy**, but §6.4 makes linewidth, not energy, the
  discriminator); `gravitational_bell.py` (gravity-as-Kuramoto-sync, repudiated
  in §4.4; the correct effect lives in `predictions.py` P6b).
- **Repudiated gravitational rate `Γ ~ Gm²/(ℏΔz)`:** `gravity_twistor.py`,
  `sg_angular.py` (§4.4 calls this a dimensional artifact, not a rate).
- **Supported the cut cochain Appendix:** `hodge_decomposition.py`,
  `hodge_dirac.py`, `simplicial_alignment.py` (cochain ontology moved to a
  separate note).

These remain recoverable from git history.

## Citing the test suite

Cite the framework via the Zenodo DOI in `CITATION.cff` at the repository root.

## License

Same as the parent repository.
