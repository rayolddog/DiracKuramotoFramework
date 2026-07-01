# Can field multiplicity emerge from one phase-oscillator substrate? — RESULT

**Date:** 2026-06-17
**Code:** `code/honeycomb_emergence.py`, `code/weyl3d_emergence.py`,
`code/statistics_emergence.py` (each → a `.png`)
**Question:** the "one shared substrate" side of the field↔vacuum question (free
QFT factorizes into per-field vacua; the interacting vacuum is a single entangled
ground state) commits the framework to deriving the *multiplicity of fields* —
distinct chiral fermion species, their masses, gauge couplings, and Fermi
statistics — from the dynamics of **one** medium. Can a phase-oscillator (Kuramoto/
Josephson) substrate actually produce that content, and where does it stop?

This note ties three verified simulations into one arc. None of the individual
mechanisms is new physics; each is a textbook condensed-matter result. **The claim
under test is the *identification*** — that the DK sync parameters (coupling,
phase-lag, inertia, on-site asymmetry) map onto exactly the knobs that generate
emergent Dirac structure, and that a single substrate carries all of it at once.

---

**Terminology (consistent with PAPER_REVISED).** "Synchronization"/"locking" below
refers to the closed-system *ordered ground state* of a lattice of phase oscillators —
the standard condensed-matter construction whose linearized fluctuations give emergent
Dirac fields — **not** the open-system, dissipative Adler/Kuramoto *measurement* lock of
the companion framework (PAPER_REVISED §2.3). The mass coupling K = m is the off-diagonal
L↔R term these two regimes act on; the preferred frame, and the Vacuum Preferred-Frame
Hypothesis, enter only through the dissipative sector (PAPER_REVISED §8).

## 1. 2D — emergent chiral fermions, mass, and a topological gauge response

**`honeycomb_emergence.py`** — inertial phase oscillators on a honeycomb lattice;
linearize the fluctuation about the ordered ground state. The envelope obeys the
(2+1)D Weyl equation `i∂_t χ = c σ·p̂ χ`, with chirality *derived*, not assumed.

| Quantity | Substrate origin | Result |
|---|---|---|
| Dirac cones at K, K′ | nearest-neighbour coupling `K` | `\|f(K)\| ≈ 1e-15` |
| emergent light-speed | `c = (v/2)√(K/3m)` (slope `v_F=3ta/2`) | `v_F = 1.50` |
| Semenoff mass `Δ` | sublattice pinning asymmetry `κ_A≠κ_B` | same-sign gap, **`C = 0`** (trivial) |
| Haldane mass | **Sakaguchi phase-lag `α` = magnetic flux** | **`C = ±1 = sign(α)`** |
| topological boundary | `\|Δ\| = 3√3 t₂\|sin α\|` | numerically `= 0.520` at α=π/2 |

**Takeaway:** one scalar-ish phase field yields a 4-component chiral object (2
sublattice × 2 valley), two distinct mass mechanisms, and a quantized `U(1)`
response. The Sakaguchi lag literally *is* a Berry flux. **Caveat (2D-specific):**
2+1D has no real γ⁵, so "valley" is only a chirality proxy and the L↔R Dirac mass
is faked as inter-valley scattering — fixed in §2.

## 2. 3D — genuine L/R chirality and the Dirac mass as an L↔R sync coupling

**`weyl3d_emergence.py`** — 4-band Wilson–Dirac model on a cubic lattice in the
**chiral basis**, `H = (σ·sin k) τ_z + M_W(k) τ_x + b σ_z` (τ = L/R chirality).

| Claim | Result |
|---|---|
| two Weyl nodes, separated in `k_z` (genuine L, R) | nodes at `k_z = ±0.609` (Wilson-shifted) |
| opposite Berry-monopole charge | slice Chern `C(k_z)`: **−1 between nodes, 0 outside** |
| **Dirac mass `M τ_x` is the OFF-DIAGONAL L↔R coupling** | gaps only for `\|M\| > \|b\|`; M=0.8,b=0.6 → gap **0.40** |
| a lone Weyl node is uncuttable (chiral protection) | nodes merge & annihilate at `M = b` (exact) |
| Nielsen–Ninomiya doubling + Wilson fix | `r=0`: 8 nodes; `r=1`: corner gaps **4/8/12**, Γ stays **0** |

**Takeaway:** in 3D the chirality is real. The Dirac mass is genuinely
`m(ψ̄_L ψ_R + ψ̄_R ψ_L)` — off-diagonal in chirality — so the simulation makes the
framework's headline structural claim literal: **you cannot mass a single
chirality; mass *is* the off-diagonal L↔R coupling**, and only when the axial field
hasn't separated them past `|M|`. Bonus: the Wilson doubler-removal term is itself
a (momentum-dependent) L↔R coupling — the fermion-doubling obstacle becomes a
zone-boundary sync feature.

## 3. Statistics — Fermi statistics from a bosonic substrate

**`statistics_emergence.py`** — the last gate. Phase oscillators commute on
different sites (bosonic); can their excitations be true fermions?

| Test | Result |
|---|---|
| (A) hard-core XX chain spectrum **==** free-fermion spectrum (Jordan–Wigner) | match to **`1.3e-14`** |
| (B) bare `[S⁻_i,S⁻_j]` off-site (boson) | **`0`** (commute) |
| (B) dressed `{c_i,c_j}` and `{c_i,c_j†}−δ` (fermion / canonical CAR) | **`0`** (anticommute) |
| (C) Pauli exchange hole in the filled sea | `g_c(x,y) = −0.18 < 0` |
| (D) flux attachment: bind Berry flux Φ → exchange phase `θ=Φ`; fermion at `θ=π` | Wilson-loop AB = flux to **`8.9e-16`** |

**Takeaway:** in **1+1D the gate is passed rigorously, with no tunable input** — a
phase-oscillator chain *is* a free-fermion system, and the statistics is carried by
the **nonlocal Jordan–Wigner string** (a sync-dressing the bare oscillators lack).
This matches the framework's posture elsewhere: statistics, like Bell nonlocality,
is a **nonlocal property of the substrate's sync configuration**, not a local
attribute of a particle.

---

## What the arc establishes

One substrate ⟷ emergent Standard-Model-like content, all verified numerically:

| Substrate ingredient | Emergent object |
|---|---|
| inertial phase coupling `K`, `m` | relativistic dispersion, emergent `c`, chiral fermions |
| Sakaguchi phase-lag `α` | Berry flux / emergent `U(1)` gauge field, topological mass |
| sublattice/on-site asymmetry | Semenoff Dirac mass |
| off-diagonal chiral coupling `M τ_x` | **L↔R Dirac mass `m ψ̄ψ`** (the off-diagonal mass coupling the two regimes act on) |
| Wilson / zone-boundary coupling | Nielsen–Ninomiya doubler removal |
| Jordan–Wigner string / attached flux | **Fermi statistics** |

So "field multiplicity from substrate dynamics" has a worked, machine-checked
backbone: **a phase-oscillator substrate supports multiple chiral fermion species,
a Dirac mass that is an L↔R sync coupling, emergent gauge fields, and — at least in
1D rigorously — fermionic statistics.**

## Caveats (what it does NOT buy)

1. **No new physics — this is identification, not derivation.** Every mechanism is
   established condensed-matter / lattice theory: graphene Dirac cones, the Haldane
   Chern insulator, Volovik Fermi points, the Wilson–Dirac regularization and its
   fermion doubling, Jordan–Wigner, Chern–Simons flux attachment. The DK
   contribution is the *mapping* of these onto sync variables and the claim that one
   medium carries them jointly. Same honest status as the rest of the program.

2. **Statistics is rigorous only in 1+1D.** In 2+1D+ the transmutation needs a
   flux-attachment (Chern–Simons) term. The substrate *supplies* the flux (the
   Haldane Berry curvature of §1), but a **dynamical reason the attached flux locks
   to level-1 (`θ=π`) rather than an anyonic value is NOT derived.** This is the
   single sharpest open problem of the thread. The 3+1D analogue (Witten's
   Wess–Zumino mechanism making a sync-defect a fermion) is not attempted.

3. **The collective modes are bosonic until dressed.** §1–§2 give the Dirac
   equation / spinor / mass / chirality / gauge coupling as a *classical field
   theory*; Pauli exclusion is the separate §3 layer. The two are not yet welded
   into a single dynamical model that is fermionic *ab initio*.

4. **Emergent Lorentz invariance is only approximate.** Linear-in-`q` near the
   nodes; broken by lattice/warping terms at the cutoff. For DK this is a *feature*
   — the lattice rest frame is the preferred frame, and the violations are the form
   the experimental-test postulate would take — but it is not a fundamental-Lorentz
   construction.

5. **Toy models, not the Standard Model.** These reproduce SM-like *structure*
   (chiral fermions, a `U(1)`, two mass types), not the actual `SU(3)×SU(2)×U(1)`
   gauge group or three generations. Richer content needs decoration (more orbitals
   / larger cells / higher-winding defects). This is a proof of principle of the
   *mechanism*, not a derivation of the specific field content.

## Relation to the papers

This is a **separate thread** from the revised main paper (`PAPER_REVISED.md`,
measurement-as-sync) and from the cosmology/QCD spinoffs. It addresses the
"one substrate vs. many" fork raised by the field↔vacuum analysis: free QFT looks
like many per-field vacua, interacting QFT is provably one shared entangled vacuum,
and this thread is the constructive attempt to make the apparent multiplicity of
fields **emergent** from a single medium. Not yet drafted into any manuscript.
