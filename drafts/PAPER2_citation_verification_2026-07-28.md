# Paper 2 — Reference verification log, 2026-07-28

All 20 non-[P1-verified] entries of `PAPER2_DRAFT_heisenberg_cut.md` checked against publisher/indexer records by two independent web-search agents (10 entries each), each verdict requiring a confirming source URL. Result: **19 confirmed, 1 corrected.**

| Entry | Verdict | Source |
|---|---|---|
| Adler, R. (1946), Proc. IRE 34, 351–357 | confirmed | doi.org/10.1109/JRPROC.1946.229930 |
| Adler, S. L. (2003), SHPMP 34, 135–142 | confirmed | sciencedirect.com/science/article/abs/pii/S1355219802000862 |
| Arndt et al. (1999), Nature 401, 680–682 | confirmed | nature.com/articles/44348 |
| Bassi et al. (2013), RMP 85, 471–527 | confirmed | link.aps.org/doi/10.1103/RevModPhys.85.471 |
| Bell (1990), Physics World 3(8), 33–40 | confirmed | iopscience.iop.org/article/10.1088/2058-7058/3/8/26 |
| Emary, Lambert & Nori (2014), RPP 77, 016001 | confirmed (corrigendum exists: RPP 77, 039501) | iopscience.iop.org/article/10.1088/0034-4885/77/1/016001 |
| Fein et al. (2019), Nat. Phys. 15, 1242–1245 | confirmed | nature.com/articles/s41567-019-0663-9 |
| Ghirardi, Rimini & Weber (1986), PRD 34, 470–491 | confirmed | link.aps.org/doi/10.1103/PhysRevD.34.470 |
| Hornberger et al. (2012), RMP 84, 157–173 | confirmed | link.aps.org/doi/10.1103/RevModPhys.84.157 |
| Joos & Zeh (1985), Z. Phys. B 59, 223–243 | confirmed | link.springer.com/article/10.1007/BF01725541 |
| Leggett & Garg (1985), PRL 54, 857–860 | confirmed | link.aps.org/doi/10.1103/PhysRevLett.54.857 |
| Mott (1929), Proc. R. Soc. A 126, 79–84 | confirmed | royalsocietypublishing.org/doi/10.1098/rspa.1929.0205 |
| Penrose (1996), GRG 28, 581–600 | confirmed | link.springer.com/article/10.1007/BF02105068 |
| **Schlosshauer, RMP 76, 1267–1305** | **CORRECTED: year 2005 → 2004** (vol. 76 = 2004 volume; the Feb-2005 online posting drives the common miscitation; author's own list says 2004) | inspirehep.net; faculty.up.edu/schlosshauer (ADS bibcode 2004RvMP...76.1267S) |
| von Neumann (1932/1955) | confirmed | en.wikipedia.org/wiki/Mathematical_Foundations_of_Quantum_Mechanics |
| Zeh (1970), Found. Phys. 1, 69–76 | confirmed | link.springer.com/article/10.1007/BF00708656 |
| Zurek (1981), PRD 24, 1516–1525 | confirmed | link.aps.org/doi/10.1103/PhysRevD.24.1516 |
| Zurek (1982), PRD 26, 1862–1880 | confirmed | link.aps.org/doi/10.1103/PhysRevD.26.1862 |
| Zurek (2003), RMP 75, 715–775 | confirmed | link.aps.org/doi/10.1103/RevModPhys.75.715 |
| Pikovsky, Rosenblum & Kurths (2001), CUP | confirmed | Cambridge Nonlinear Science Series 12 |

Corrections applied to the draft: Schlosshauer year in both in-text citations (§1) and the reference entry; "Zurek 2003a" suffix dropped (only one Zurek 2003 in this paper's list). NOT covered by this pass: the order-of-magnitude values in the §3.3 layer-width table, which still carry their own [values to verify] flag and require physics sourcing (linewidth/frequency data per platform), not bibliographic checking.

## Addendum — §3.3 layer-width table sourcing (same day)

Every row of the table anchored to a citable source, all rates converted to a stated angular convention (Γ = 1/τ; Hz linewidths × 2π). Two corrections against the first-draft estimates, one sharpening:

| Row | Sourced result | Anchor | URL |
|---|---|---|---|
| Alkali D-line (natural) | **CORRECTED**: w = 1.4–1.9×10⁻⁸ (first-draft upper decade 10⁻⁶ unsupported for natural width — that is the Doppler-broadened vapor value, noted as caveat (i)) | Steck, Rubidium 87 D Line Data rev. 2.3.4 (2025): Γ = 38.117(11)×10⁶ s⁻¹, ω₀ = 2π·384.230 THz | steck.us/alkalidata/rubidium87numbers.pdf |
| Optical clock (⁸⁷Sr, Al⁺) | **SHARPENED**: w = 2–7×10⁻¹⁸ natural (was "≲10⁻¹⁴"); laser-limited practical coherence ≲10⁻¹⁵ | Dolde et al., PRA 112, 023121 (2025): measured ³P₀ lifetime τ = 167 s; Ludlow et al., RMP 87, 637 (2015) | arxiv.org/abs/2505.06440 |
| Transmon (1/T₂) | **CORRECTED**: w = 3×10⁻⁷–4×10⁻⁶ (first draft said 10⁻⁶–10⁻⁵; arithmetic error). Circa-2020 typical; modern T₂ > 300 μs → w → 10⁻⁸ (caveat iii) | Kjaergaard et al., ARCMP 11, 369–395 (2020): T₁,T₂ 50–100 μs, ω_q/2π ≈ 5 GHz | arxiv.org/abs/1905.13641 |
| Quantum dot 4 K | confirmed at order of magnitude, refined: w = 6×10⁻⁷–5×10⁻⁵ (radiative 800 ps → spectral-diffusion-broadened; upper bound inhomogeneous-in-time, caveat iv) | Kuhlmann et al., Nat. Commun. 6, 8204 (2015) | nature.com/articles/ncomms9204 |
| Si photodiode 300 K | confirmed: w = 10⁻³–3×10⁻², anchored 1×10⁻² (32±5 fs momentum relaxation at 5×10¹⁸ cm⁻³; density-dependent, caveat iv) | Sabbah & Riffe, PRB 66, 165217 (2002) | journals.aps.org/prb/abstract/10.1103/PhysRevB.66.165217 |

Consequence for the text: the table's dynamic range grew from eight to SIXTEEN orders of magnitude (§8.2 updated). Six new reference entries added (Dolde, Kjaergaard, Kuhlmann, Ludlow, Sabbah & Riffe, Steck), each confirmed by the URL above at sourcing time.
