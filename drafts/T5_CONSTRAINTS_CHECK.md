# T5 vector-channel prior-constraints check — VERDICT: unprobed, paper cleared

*Date: 2026-07-05. Decisive literature check for `LIGO_SIDEREAL_TEST_T5.md` (the
"likely already constrained?" caveat in §2.5). Question: is a vector-type,
sidereally modulated, MEASUREMENT-SECTOR-ONLY anisotropy of decoherence rates at
fractional amplitude β ≈ 1.2×10⁻³ already excluded? Researched by web agent;
five fronts, all bounds verified against the cited sources.*

## Overall verdict — (c): channel genuinely unprobed

No experiment constrains a vector, sidereally modulated, measurement-sector-only
anisotropy of decoherence rates at ~1.2×10⁻³. Every existing bound falls into one
of two non-applicable classes:

1. **All sidereal Lorentz-violation bounds are Hamiltonian/propagation-sector** —
   comagnetometers, ion traps, optical clocks, the KMM LIGO analysis, KLOE Δa_μ.
   The SME data tables contain *no dissipative coefficients by construction*.
2. **All decoherence/Lindblad bounds are additive, isotropic, free-propagation** —
   CPLEAR/KLOE α, β, γ (γ < 3.7×10⁻²¹ GeV), KLOE ζ₀₀ ~ 10⁻⁷, IceCube
   Γ₀ ≤ 1.17×10⁻¹⁵ eV, CSL λ bounds from GW detectors — and none were sidereally
   analyzed. They cannot see a *multiplicative* modulation of environment-induced
   dissipation.

## Front-by-front

| # | Front | Strongest relevant bound | Applies to T5 channel? |
|---|---|---|---|
| 1 | SME data tables (Kostelecký & Russell, RMP 83, 11; arXiv:0801.0287, 2026 ed.) | all ~52 tables | **No** — Lagrangian (unitary) sector only; no Lindblad sector exists in the SME |
| 2 | Open-system LV/CPT: kaons (CPLEAR PLB 364, 239 (1995); KLOE-2 JHEP 04 (2022) 059), IceCube (arXiv:2308.00105, Nat. Phys. 2024) | γ < 3.7×10⁻²¹ GeV; ζ₀₀ = (1.4±9.5±3.8)×10⁻⁷; Γ₀ ≤ 1.17×10⁻¹⁵ eV | **No** — additive free-propagation decoherence, isotropic models, never sidereally binned |
| 3 | Sidereal entanglement/Bell/coherence analyses (Pruttivarasin Nature 517, 592; Megidish arXiv:1809.09807; Yb⁺ arXiv:2206.00570; Allmendinger PRL 112, 110801) | c_μν ~10⁻¹⁸–10⁻²¹; b_⊥ⁿ < 6.7×10⁻³⁴ GeV | **No** — observable is always frequency/phase; **no published bound on sidereal variation of any decoherence rate (T₂, visibility, fidelity)** |
| 4 | Sidereal LIGO analyses | KMM: Kostelecký–Melissinos–Mewes, PLB 761, 1 (2016), arXiv:1608.02592 — δn/n ≲ 10⁻¹⁹–2×10⁻²² sidereal | **No** — photon-sector refractive index (propagation). **No sidereal analysis of squeezing/quantum-noise floor exists; nobody has proposed T5** |
| 5 | Anisotropic collapse models | Carlesso et al. PRD 94, 124036; LISA Pathfinder λ_CSL < 2.96×10⁻⁸ s⁻¹ (PRD 95, 084054) | **No** — isotropic λ only; anisotropic collapse-rate never proposed or bounded |

## Referee-critical cautions (fold into the paper)

1. **KMM 2016 is genuine prior art** for "sidereal-bin LIGO instrument data for
   Lorentz violation." The paper must foreground the propagation-vs-dissipation
   distinction in the introduction or referees will call the test already done.
   (It is also a methodological asset: it proves LIGO channels sidereal-bin to
   extreme fractional precision.)
2. **The KLOE ω-effect bound (|ω| ≲ 10⁻⁴) is numerically below β = 1.2×10⁻³.**
   The paper must argue explicitly why a measurement-sector modulation does not
   feed the ω parameter: ω is an anomaly *in the initial entangled state*, while
   the T5 coupling acts *at detection*. One paragraph, but mandatory.
3. **Nearest competing dataset:** the ³He/¹²⁹Xe comagnetometer free-precession
   amplitude-decay records (Allmendinger 2014) *could* be reanalyzed for sidereal
   T₂ modulation; no such bound is published. Acknowledge it, and offer it as the
   cheap tabletop companion test (it is precisely T4's channel).

## Citations that establish the gap (for the paper's intro)

1. Kostelecký & Russell, Rev. Mod. Phys. 83, 11 (2011); arXiv:0801.0287 (2026 ed.)
2. Kostelecký, Melissinos & Mewes, Phys. Lett. B 761, 1 (2016); arXiv:1608.02592
3. Ellis et al. + CPLEAR, Phys. Lett. B 364, 239 (1995); KLOE-2, JHEP 04 (2022) 059
4. IceCube Collaboration, Nature Physics (2024); arXiv:2308.00105 (10.7-yr update arXiv:2507.12316)
5. Carlesso, Bassi et al., PRD 94, 124036 (2016); LISA Pathfinder, PRD 95, 084054 (2017)
