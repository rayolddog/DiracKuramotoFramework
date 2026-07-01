# Can the basin-selection weights be derived = |α|²? — RESULT

**Date:** 2026-06-13 · **Code:** `code/born_weights_check.py`
**Question:** does the dissipative chiral-pair dynamics produce long-run frequencies
`P(φ=0)=|⟨+x|ψ⟩|²`, `P(φ=π)=|⟨−x|ψ⟩|²` (Born weights) **without assuming them**?

## Test

Qubit, measured observable = σx (interference/mass channel), pointers |±x⟩ = φ=0,π.
Tilted initial state |ψ₀⟩ = 0.926|L⟩ + 0.378|R⟩ → |α|²=0.857, |β|²=0.143, ⟨σx⟩₀=0.70.
**Born target: P(0)=0.85, P(π)=0.15.** Computed three ways:

| method | P(φ=0) | P(φ=π) | gives Born? |
|---|---|---|---|
| Born (target) | 0.850 | 0.150 | — |
| (1) mean-field steady-state populations `(1±⟨σx⟩₀)/2` | 0.850 | 0.150 | yes |
| (2) quantum trajectories (4000 runs) | 0.852 | 0.148 | yes |
| **(3) deterministic basin volume (azimuth)** | **0.500** | **0.500** | **NO** |

Martingale check: ensemble-mean ⟨σx⟩ stays 0.700→0.704 across the run — the |·|²
measure is **conserved**, not generated.

## What the result means

**Born weights ARE recovered** by (1) and (2) — but the value |α|² enters as an
**input**, in three guises that are one and the same assumption:

- **(a)** reading the steady-state density-matrix populations as outcome frequencies
  — that *is* the Born postulate;
- **(b)** the |·|² **martingale / dW-weighting** of the stochastic unraveling
  (`√γ(σx−⟨σx⟩)dW`) — Born built into the noise;
- **(c)** equivalently, the **golden-rule rate ∝ |matrix element|²**.

**Method (3) is the decisive negative.** The *geometric* basin measure — the fraction
of initial relative-phases that flow to each well — is **50/50, independent of |α|²**.
So Born does **not** come from basin volume; it comes from the **measure placed on the
selecting ensemble** (the noise), which is the inserted |·|². This confirms the MCI
program's own "sharpest open critique": the naive basin-of-attraction measure does not
reproduce Born.

## The one genuine positive: equivariance, not derivation

The dynamics *does* contribute something real but modest: **⟨σx⟩ is conserved**
(`d⟨σx⟩/dt = 0` under D[σx], H=0). So the |·|² measure, **granted at preparation,
propagates undistorted to the outcome**. This is **equivariance** — exactly the status
of Bohm's quantum-equilibrium / Valentini's equivariant measure. It is Born-*compatible*,
not Born-*derivative*.

## The unsolved core (precisely located)

What is **not** supplied is a **typicality / relaxation** argument: a derivation that
the selecting ensemble *carries* the |·|² measure in the first place, without inserting
it. Decompose the Born problem into three pieces:

1. **Form** `P=|⟨k|ψ⟩|²` — settled (Gleason: unique non-contextual measure).
2. **Discreteness** (the binary) — supplied (the D[σx] pointer structure; this thread).
3. **Measure→frequency link** — **OPEN**. Conservation/equivariance is had; relaxation
   (why an arbitrary ensemble *becomes* |·|²-distributed) is not, and inserting it is
   what every route (Bohm, Zurek-envariance, Everett decision theory, and this one)
   ultimately does.

## Verdict

**NOT derived.** The frontier is reached, not crossed — the same place the
2026-06-12 Born analysis landed, now confirmed concretely in the MCI dissipative
machinery. The honest one-line status for the papers: *MCI is Born-compatible
(equivariant), not Born-derivative; the basin measure does not generate |α|² and the
geometric basin volume is provably 50/50.*

## Paper note (flagged, not yet applied)

The discretization companion's §6.1 currently frames the open problem as recovering
Born "**as the fraction of initial conditions that lock to the n-th mode**." Result
(3) shows that fraction is 50/50 — so that wording is over-optimistic and should be
corrected: the fraction of initial conditions does **not** give Born; the |·|² measure
on the ensemble does, and it is the inserted assumption. Recommend sharpening §6.1
(and PAPER_REVISED §8) accordingly.
