# Stage 2 — sharpness of the cut for a self-sustaining absorber, and whether the carrier enters

*2026-09-04. Written before either stage-2 script was run. Redefined after the correction
logged in `RESULTS.md`: Paper 2's w = K/ω is a layer width in share, equivalent to a
crossover of relative width order one in κ_ret/K, which stage 1 measured. The open
question is therefore not whether ω sharpens the crossover but whether a self-sustaining
absorber does, and separately whether the carrier frequency enters the recoverability
crossover at all. Two parts, two scripts.*

## Part A — does the carrier frequency enter? (`stage2_rabi_carrier.py`)

Stage 1's absorber was a rotating-wave two-level system, in which ω cannot appear. Part A
removes the approximation: the quantum Rabi model, H = ω a†a + (ω+Δ)|e⟩⟨e| +
K(a + a†)(σ₊ + σ₋), photon Fock space truncated at n ≤ 3, the same dense record channel
(N = 128 modes, bandwidth 40, single excitation in the channel), the same echo
recoverability (system block reversed, channel untouched). K = 1; ω/K ∈ {8, 16, 32, 64}
and the rotating-wave reference; Δ/K on ±[0.05, 6] (21 log points per sign) and 0;
Γ = 0.2 and 0.5; t = 3. The rate curve is Γ_eff(Δ) = −ln R/(2t); its centre c is the
midpoint of the two half-maximum points and its half-width h is half their separation.

- **A1 (calibration).** No channel: echo returns 1 to 10⁻¹² at every Δ and ω. At
  ω/K = 64 the centre and half-width agree with the rotating-wave reference to 3 %.
- **A2 (Bloch–Siegert).** The centre shifts as c = −s·K²/ω with s between 0.5 and 2:
  the counter-rotating term displaces the resonance by the Bloch–Siegert amount, of
  relative size K/ω, and to negative Δ (the dressed atom sits above the bare one).
- **A3 (no sharpening).** The half-width h changes by less than 10 % between ω/K = 64
  and ω/K = 16, and by less than 25 % at ω/K = 8. The carrier enters as a shift, not a
  width. If h *narrows* by more than 25 % at ω/K = 8, this prediction is wrong and the
  carrier does sharpen the crossover.
- **A4 (truncation).** n ≤ 3 versus n ≤ 4 differ by less than 10⁻³ in R at ω/K = 8.

## Part B — is the crossover sharp for a self-sustaining absorber? (`stage2_stuart_landau_sharpness.py`)

Paper 2's own continuous model (Appendix A, Figure 1): the injected Stuart–Landau
oscillator ȧ = (g − |a|²)a − iΔa + F + ξ, with Δ = 1, F = 0.35, complex white noise of
strength D, gain g swept through the Hopf threshold (g = 0) and the locking boundary.
Part B adds (i) a record channel as a Markovian damping Γ_rec on a (stage 1 established
that a dense channel is memoryless) with its leak Γ_rec|a|² tracked, and (ii) an optional
counter-rotating drive term F·e^{2iω_d t} (the real drive F cos ω_d t in the lab frame),
ω_d ∈ {∞, 40, 10}. Observables per g: the winding rate ⟨φ̇⟩ (Paper 2's Figure 1(a)),
the stored energy ⟨|a|²⟩ (the leak-relevant quantity, stage 1's occupation), the drive
power ⟨2 Re(F a*)⟩, and the leak Γ_rec⟨|a|²⟩. D ∈ {0, 10⁻⁴}; Γ_rec ∈ {0, 0.1};
g on 61 points in [−1, 1.5]; Heun integration, dt = 0.002 (0.01 for the rotating-wave
runs), transient 200, average 600.

Analytic structure fixed before running, for the rotating-wave, noiseless, Γ_rec = 0
case. The forced fixed point satisfies F² = u[(g−u)² + Δ²] with u = |a|²; its Jacobian
has trace 2g − 4u and determinant (g−u)(g−3u) + Δ². A saddle-node needs
(g−u)(g−3u) = −Δ², which for Δ = 1 requires g ≥ √3; so on the whole swept range the
locked state is lost by a *Hopf bifurcation of the forced fixed point*, at u = g/2, i.e.
where (g/2)(g²/4 + Δ²) = F²: **g_H ≈ 0.243** for Paper 2's parameters. The Adler
estimate g = (F/Δ)² = 0.1225 assumes F ≪ √g, which is false here (F/√g = 1 at that
point). After the Hopf, the small newborn cycle around the fixed point does not encircle
the origin, so the winding rate stays zero until the cycle grows to enclose it.

- **B1 (the caption's attribution is wrong).** The noiseless winding onset lies between
  g = 0.243 and g = 0.35, not at 0.1225, and the noise D = 10⁻⁴ moves it by less than
  0.02. Appendix A's statement that the onset near g ≈ 0.35 is "noise-smeared upward"
  from 0.1225 misattributes a deterministic effect (the failure of the weak-injection
  Adler reduction at F ~ √g) to noise. Paper 2's Figure 1 caption and Appendix A need
  correcting if this holds.
- **B2 (smooth energy, sharp winding).** ⟨|a|²⟩ is continuous across g = 0 and across the
  winding onset, with at most a kink; its relative change over any interval of width
  0.1 in g is below 30 %. Below the Hopf of the free oscillator it follows the linear
  response F²/(g² + Δ²). The winding rate is exactly zero below onset (D = 0) and rises
  continuously above it. Hence the leak-relevant observable, and with it the recoverability
  crossover, is *smooth* for the self-sustaining absorber too; only the phase-winding
  observable is sharp. This is the stage-2 answer to the question left open by stage 1.
- **B3 (carrier does not enter).** The counter-rotating drive at ω_d = 40 changes ⟨|a|²⟩
  and the onset by less than 10⁻²; at ω_d = 10 by less than 5 × 10⁻². No sharpening.
- **B4 (record channel).** Γ_rec = 0.1 shifts the free Hopf from g = 0 to g = Γ_rec/2 =
  0.05 and the winding onset upward by about the same, and changes nothing about
  sharpness. The leak Γ_rec⟨|a|²⟩ is a smooth function of g.

## What would count as what

- A2 and A3 both confirmed: the carrier is a shift of relative size K/ω and nothing
  else; Paper 2's ω belongs in the share conversion only.
- B2 confirmed: the recoverability crossover is smooth on both sides of the threshold
  in Paper 2's own model; the paper's "crossover" language (§6.2) is right and the
  "razor-sharp" language attached to small w describes the layer's *extent*, not an
  abrupt switch. B2 refuted (a jump in ⟨|a|²⟩ at the onset): the self-sustaining absorber
  does sharpen the cut, and stage 1's smoothness was a linear-absorber artefact.
- B1 confirmed: a factual correction owed to Paper 2's Appendix A and Figure 1 caption.
