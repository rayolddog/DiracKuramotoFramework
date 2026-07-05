# 2026-07-04 — The hologram critiqued, and measurement split into three stages

*Session log. Paper changes: `current_revision_DK_paper.md` v2–v4 (revision log). Formal
background: [`../drafts/NOTE_wave_energy_interpretation.md`](../drafts/NOTE_wave_energy_interpretation.md),
the 07-01 entry, and Appendix D of the paper.*

## Where it started

Asked for a critique of the current revision, then specifically of the idea that Born
predictions can be **mirrored by the framework's mechanics**, with the **hologram** as the
real-world model. Along the way: the July-1 review-driven edits landed (v2: new §3.8 owning
the §3.7 chiral-decoupling result, §2.3 corrected through Appendix D, §6.2 gradient-coupling
scaling argued, `resolution/` restored from the frozen journal-demonstration snapshot and
its script verified to reproduce Appendix D's numbers exactly), and the Born-gap restatements were
consolidated to a single canonical fork in §3.3 (v3).

## The hologram critique (five points)

1. **The metaphor points 180° from the mechanism.** The framework's Born mechanism
   (`born_substrate_sampling`) *requires phase randomness* — the linear term cancels over
   the random bulk phase, the surviving power term gives `|ψ|²`. A hologram *requires phase
   stability* (the reference beam). The hologram is the model system for the framework's
   Born-*breaking* (coherent-bulk) regime. Right model for §4 (reference coherence /
   visibility, where the paper already uses it); wrong model for §3.3/§8 (selection).
2. **A boson model paying a fermion debt.** Light has a classical field with primitive
   energy density `|E|²`; a single electron's ψ does not (Pauli). The analogy borrows
   exactly the feature assumption (A) has to establish. Tonomura build-up *demonstrates*
   Born, doesn't *mechanize* it.
3. **The single event is where Born lives, and the plate is silent there** — "which grain,
   with probability ∝ local `|ψ|²`" *is* Born re-imported. New sharpening: **winner-take-all
   exclusivity is nonlocal.** The threshold grounds each grain's *click* locally; nothing
   local prevents two distant grains firing on one photon — the exclusion is global
   one-quantum bookkeeping across the plate, i.e. the collapse nonlocality reappearing at
   the emulsion (the §7.5 non-separable configuration in photochemical clothes). Add to the
   honest ledger: "indivisibility dissolved detector-side" covers the click, not the
   exclusion.
4. **The framework itself superseded the hologram's literal mechanism.** Energy-deposition
   → outcome was the ladder; the §3.7 charge-vs-mass split (EM detectors read `j⁰=|ψ|²`,
   only gravity reads `T⁰⁰=E|ψ|²`) is the landing. Silver halide is also a *multi-quantum*
   threshold detector (Gurney–Mott ≈3–4 quanta/speck) with a nonlinear H&D response — the
   worst poster child for single-event Born.
5. **The falsifiability framing needs sharpening.** The coherent-bulk deviation regime may
   just be standard homodyne QM (a *different POVM*, which QM also predicts differently);
   strong-drive deviations map onto detector saturation. A genuine test needs Born violation
   **at fixed POVM** — joint detection-*timing* statistics (exponential first-passage) is
   the leading candidate.

## John's refinement → the three-stage division

John's distinction: Stage 1 *and the first step of Stage 2* both happen at the detector
surface; the subsequent amplification is charge-dependent and environment-specific (hologram:
local chemistry; PMT: cascade in an applied EM gradient). Caution agreed: the vertex is
energy-**selective** (resonance, a rate factor `σ(ω)` multiplying `|ψ|²`), not
energy-**coupled** — everything stays an EM (charge-current) coupling, preserving §3.7.

This forced the recognition that the paper's own formalism already carried three stages:
§3.5's cut condition is a **conjunction** (`Im W ≠ 0` ∧ `Γ_cap > 0`) — two boundaries, three
regimes — and Appendix D already separates trajectory localization from the amplification
threshold. Adopted (v4):

- **Stage 1 — capture** (reversible; Re W; energy-selective, amplitude/interference-driven;
  shapes the measured basis; records nothing).
- **Stage 2 — selection, the surface commit** (onset of Im W; *the
  excited-electron–host-atom interaction* — the ion's Coulomb field, recoil, shake-up/Auger,
  phonons — is the first dissipative channel and the door for the selecting background;
  Born weights **set** here; catch-and-reverse window; reversible in principle).
- **Stage 3 — registration** (reservoir-powered closure: dynode voltage, developer
  chemistry, supersaturation; charge-triggered, energy-blind, equivariant by design; Born
  weights **finalized**; Bohr's "irreversible act of amplification" is the closer, never the
  selector).

John flagged that the atom–excited-electron interaction "often gets forgotten (even by AI)"
— it is now explicit as the physical content of Stage 2.

## Detector taxonomy (from the Opus 4.8 thread)

Two numbers per architecture: per-event capture rate `r ∝ σ(ω)|ψ|²` and **commit threshold
k** (with site memory time τ_mem). Bell detectors: k = 1 — every capture commits; per-event
Born claims are k = 1 claims. Photographic grain: k ≈ 3–4 with finite memory —
**reciprocity failure = Stage-2 progress decaying before Stage 3**, everyday empirical
evidence the two stages are physically distinct. Cloud chamber: k = 1 per vertex, many
vertices (one particle/many sites vs. film's many quanta/one site — orthogonal axes). §5
rewritten around this; emulsion/hologram row added; Gurney–Mott is now ref [44].

## Net + next

Paper now at v4: three-stage architecture through abstract, §1–§3, §5, §7–§8, App D, with a
mapping note (old Stage 2 = new Stages 2–3) for the frozen snapshot and companions. Born
problem now has a precise address: **set at Stage 2, finalized at Stage 3, and Stage 3
contributes no statistics** — ruling out amplification-based Born mechanisms as a class.

**Open next:** (1) the exclusivity-nonlocality residue deserves a paragraph of its own
(candidate: §7.5 or the hinge-note ledger); (2) fixed-POVM discriminator — work out the
joint-timing prediction; (3) H-theorem / relaxation demonstration for the boundary-localized
resampling (unchanged from 07-01); (4) check whether companion papers (AB, DISCRETIZATION)
need the stage-mapping note.

---

## Addendum (same day, later) — exclusivity from energy conservation; envelopes; virtual bookkeeping

Two probing questions from John, then his proposal, then two follow-ups. Paper v5.

**Q: why aren't Born weights final when the photon affects one atom?** Because "one atom"
is outcome language — unitarily the wave excites *all* reachable sites coherently
(`Σ c_i |atom i excited⟩`), and **absorption ≠ detection**: a committed excitation can
re-emit (resonance fluorescence; radiation trapping cycles in dense media; Minev
catch-and-reverse; sub-latent speck decay). Recorded statistics = commit × closure;
equivariance of Stage 3 = closure site-independence — which is where quantum efficiency and
fair sampling physically live.

**Q: are vacuum effects confined to Stage 1?** No — *inverted at Stage 2*: reactive vacuum
at Stage 1 (Re Σ dressing), **selecting** vacuum at Stage 2 (App-D's dW *is* vacuum shot
noise; spontaneous emission is vacuum-triggered; zero-point is half the selecting
background), refereeing vacuum at Stage 3 (amplify above the vacuum floor; Caves bound).
Crossover criterion **ℏω vs k_BT**: optical detectors vacuum-dominated
(e^{−ℏω/k_BT} ~ 10⁻³⁵), NMR thermal — added to §4.3. Conceding "washed out after Stage 1"
would forfeit the VPFH/coherence-locus front and the App-D point-2 two-readings problem.

**John's proposal (exclusivity mechanism):** no waveform collapse — the absorbed quantum is
*subtracted from the packet's tails*; insufficient energy remains for a second electron.
Assessment: it **mechanizes winner-take-all** (conservation + threshold — no longer imported
by fiat in the substrate-sampling model) and gives the preferred frame a *job* (the budget
is enforced on the foliation — a cost becomes infrastructure). Three walls: (1) the drain is
**nonlocal** — a beamsplitter puts half the norm in a spacelike-separated arm; single-photon
spacelike antibunching (Guerreiro et al. 2012, now ref [45]) shows the enforcement is
superluminal — so this *physicalizes* collapse (foliation-synchronized energy transfer),
doesn't remove it; (2) **rate, not accumulation** — local accumulation predicts
intensity-dependent first-click latency, excluded since Lawrence–Beams 1928 (ref [46]); the
local step is a power-proportional rate, the budget global; (3) leftover must be **exactly
vacuum** — no sub-threshold real residue (keeps the first version's thermalization claim
retracted); drain provisional at Stage 2, final at Stage 3. Falsifiable edge: joint
click-timing at spacelike separation (fixed-POVM), constrained by the Zbinden-type
moving-frame experiments.

**Follow-up 1 — Gaussian envelopes?** Gaussian is an idealization (unique Gabor-limit
minimizer; closed under Fourier/propagation); spontaneous emission gives exponential/
Lorentzian; photon packets don't spread longitudinally in vacuum. Tails never exactly zero —
but the decisive point cuts the other way: envelopes can be **bimodal with half the energy
km away** (beamsplitter), so the depletion needs global bookkeeping regardless of shape.

**Follow-up 2 — virtual particles carrying off excess energy?** Not quite: internal lines
conserve four-momentum *exactly* at every vertex (what's relaxed is the mass-shell
condition, off-shell for ~ℏ/ΔE), and only **external legs** (real quanta) carry energy to
infinity. Excess energy leaves as real, local quanta at the winning site (photoelectron
KE = ℏω − W, phonons, fluorescence); the virtual sector is the Stage-1/2 loan window the
paper already carries (§3.5 Re W). Feynman structure mirrors the three stages: internal
lines = reversible window; external legs = the record. Split adopted for the mechanism:
energy books balanced *locally* by external legs; exclusivity enforced *globally* by the
budget.

**Paper v5:** conservation-exclusivity paragraph added to §3.3 (three walls, refs [45],
[46]); ℏω/k_BT selecting-noise criterion added to §4.3.

**Follow-up 3 — exclusivity by *rotation*? (John).** Proposal: the commit rotates the
wavepacket (tails included) about a central axis so the tails no longer interact with other
atoms. Axis-sorting: polarization rotation fails (random detector orientations;
polarization-blind absorbers); global phase rotation fails (rates ∝ |ψ|², phase-blind — the
toy model's own result); the surviving axis is the **complex energy plane** — on-shell →
off-shell — which the framework owns twice already (§3.6: the cut IS the mass pole rotating
off the real axis; virtual/real = lock threshold) and which is the hinge note's complex tilt
ζ = α + iη. Synthesis adopted: **rotation is the window mechanism, depletion the closure
outcome** — Stage 1–2 capture = injection-locking rotation into the winner's Arnold tongue,
the rigid extended mode (§7.5 non-separability = hinge rigidity) rotating the tails out of
every other tongue (real but sterile, reversible — catch-and-reverse = rotate back); Stage 3
completes the transfer, residual exactly vacuum. Nonlocality unchanged (rotating spacelike
tails is as superluminal as draining them; hinge §5 keeps it non-signalling). Disciplines:
no sterile off-shell residue after closure; the window is stealable by a wide-tongue
(strong-coupling) detector — a consistency check, and it re-sharpens the joint-timing
(fixed-POVM) edge: does far-detector suppression switch on at near-detector *capture* or
*closure*? Not yet in the paper — candidate sentence for §3.3 tying the provisional drain
to the off-shell rotation and §3.6's pole.

**Follow-up 4 (same night, 21:56) — the complex-plane synthesis.** Pushed on the rotation
picture and it closed a loop: **depletion and rotation are the modulus and argument of one
pole displacement.** The residual mode's eigenvalue is
`Ẽ = (E + Re Σ) − iΓ/2 = |Ẽ|e^{−iθ_E}`; evolution `e^{−iẼt} = e^{−i(E+ReΣ)t}·e^{−Γt/2}` —
John's two exclusivity proposals (energy subtracted from the tails / tails rotated) are the
same complex number, and §3.6's Kramers–Kronig sentence already asserts their
inseparability. Division of labor forced by KK: **the Re Σ line-pull detunes the tails
(reversible window sterility — only algebraic suppression from broadening; strong once shift
> γ_B), the Im Σ width drains them (exponential, absolute at closure).** Partial Wick
rotation `E → Ee^{−iθ}`: oscillation cosθ, decay sinθ — θ_E = 0 is Stage 1, small θ_E with
Γt ≲ 1 the Stage-2 window, Γt ≫ 1 Stage 3. Physical realization that already exists:
**evanescent waves** — imaginary k_z past the TIR critical angle = real amplitude, zero
flux, sterile, *stealable* by frustration (FTIR = wide-tongue detector raiding the window);
the critical angle is a sharp threshold in a continuous rotation, precedent for the §3.5
cut. For matter the axis is the ZBW clock: dressing tips the circular chiral rotation into
the §3.6 inward spiral by θ_E = arctan(Γ/2m) ~ 10⁻¹³ rad for optical Γ — *"the cut is not a
large rotation but an unclosed one"* (measurement strength = persistence of a tiny tilt;
ties θ_E to App-D's K_eff). Bookkeeping: three distinct complex rotations now named — α
(correlation), η (boost), θ_E (measurement progress) — α carries the cos² *shape*, θ_E the
*commitment*, neither the *measure* (Born gap unmoved). **Next computation:**
`code/complex_rotation_exclusivity.py` — N threshold sites, one quantum, explicit complex
pole per provisional commit (δ_i − iΓ_i/2), reversals in-window, first-closure-wins with
loan recall; check Born weights, exact antibunching, FTIR stealability, and above all
whether joint click-timing deviates at all from the QM envelope (the fixed-POVM edge, made
simulable).

**BUILT AND RUN (same night, ~22:20)** — `code/complex_rotation_exclusivity.py` (seed 7,
~23 s), figure alongside. Model: event-driven MC; a provisional commit adds pole (δ=3γ,
Γ=1γ) to the shared mode; sterility S = γ_B(γ_B+Γ/2)/((γ_B+Γ/2)²+δ²) (Lorentzian overlap;
= 0.13 for a matched narrow site, 0.88 for a wide γ_B=10 tongue); loaned norm drains at
Γ_loan during the window, restored on reversal; closure at R_close, reversal at R_rev;
first closure drains the budget and force-reverts other loans. Results (N=20k/run):

- **E1a Born survives equivariant closure:** P(win) = [.391,.303,.206,.100] vs
  |ψ|² = [.4,.3,.2,.1], TVD 0.009.
- **E1b Recorded = first-closure, not first-touch:** biasing one site's R_close (0.5 vs
  2.5) moves the stats to the commit×closure-branching prediction (TVD pred-vs-MC 0.010),
  0.105 away from bare Born — a *fair-sampling violation, not a Born failure*; the §3.3
  equivariance claim quantified.
- **E2 Antibunching bookkeeping:** 11.3% of runs have overlapping provisional windows
  (would-be coincidences — the superposition of virtual excitations is real); double
  registrations exactly 0 (budget); ~0.4 reversals/run.
- **E3 The one fingerprint:** click-time distribution = envelope ⊛ closure latency. Fast
  closure shows only the (universal, rate-model) commit distortion; slow closure adds a
  mean delay +0.845 vs predicted 1/R_close ≈ 0.98 (reversal recycling explains the gap).
  Vanishes as R_close → ∞; degenerate with ordinary detector jitter *unless correlated
  with engineered reservoir properties* (e.g. amplification bias) — that correlation is
  the honest form of the fixed-POVM test.
- **E4 FTIR steal:** a wide-tongue probe switched on during the window steals the quantum
  (P = 0.27 at t_on = 0.05, falling to 0.006 at t_on = 2.0 ≫ mean closure 0.4); a narrow
  tongue gets roughly half (sterility working); after closure, nobody. The
  evanescent/FTIR analogy holds quantitatively in-model.

Ledger: capture ∝ power and the pole values are inputs; the budget (first-closure-wins)
is the conservation postulate, enforced nonlocally (§3.3 wall i). What the run
establishes: the rotation+drain mechanism is *internally consistent* (Born, antibunching
survive), its Stage-2/3 split is *operationally meaningful* (E1b, E4), and its only new
observable is the latency convolution (E3).

**Follow-up 5 (22:17) — scattering amplitudes (John: can the model handle partial,
non-absorptive interaction?).** Answer: scattering theory is the *native home* of the
complex-rotation formalism. Dictionary: `S_ℓ = η_ℓ e^{2iδ_ℓ}` — phase shift δ = the
reversible rotation (Re Σ, Stage 1–2, no record); inelasticity η < 1 = the drain (Im,
closure probability; `1−η²` ↔ §3.5's `1−e^{−2Im W}`); Breit–Wigner resonance = the same
pole displacement E_R − iΓ/2; **Wigner time delay 2ℏ dδ/dE = the measured duration of the
Stage-2 window** (scattering theory has been clocking the provisional commit for a
century); Rayleigh scattering = commit-and-revert (pure rotation, no closure). Kinematic
gem: a **free electron cannot absorb a photon** (E–p conservation) — absorption needs the
host atom to take recoil, so the "forgotten atom" of Stage 2 is what makes a closure
channel *exist*, not just the first dissipative contact. **Optical theorem refines Wall 1:**
σ_tot = (4π/k) Im f(0) — downstream depletion is *causal* destructive interference with
the forward-scattered wave (the shadow); the nonlocal residue shrinks to exclusivity
across separated arms only (= §7.5's non-separable configuration, nothing extra). Honest
ledger: the framework adopts, doesn't re-derive, amplitudes; dσ/dΩ = |f|² is the same
imported Born squaring in the same place. Framework-specific adds: time-domain reading
(delay = window), channel classification by stages (elastic / recoil-record = track
regime, one closure per event with sequential events = Mott / full capture), and the
noticed coincidence that the sim's sterility S(δ,Γ) is already a Breit–Wigner overlap.
**Possible sim extension:** add a recoil channel (closure that registers E–p transfer
without consuming the quantum) → §5's whole capture-strength axis in one simulation.

**BUILT AND RUN (22:30)** — `code/recoil_channel_tracks.py` (seed 7, ~18 s), figure
alongside. Closure now branches: CAPTURE (prob β, consumes the budget, run ends — the
photodetector limit) vs RECOIL (prob 1−β, registers a droplet costing ε ≪ E₀, quantum
survives — the track limit). Direction handled as Mott-in-POVM-language: amplitude p(θ)
starts uniform (spherical wave); each recoil event draws its angle from p⊛K (Born-weighted
overlap with a site acceptance of width σ_meas) and applies the Kraus update p ← p·K —
§5's "each capture only partially sharpens the momentum" made executable. Results:

- **E1 click↔track axis:** mean registrations interpolate 1.00 (β=1) → 60.9 (β=0,
  = E₀/ε), matching the truncated-geometric prediction across the whole sweep; the
  capture-ended fraction falls 100% → 0. One mechanism, both §5 architectures.
- **E2 Mott gallery:** isotropic source → straight dotted tracks radiating in random
  directions (first-event angle uniform, TVD 0.043) — the spherical wave chooses once,
  then keeps its choice. Visually a cloud-chamber star.
- **E3 The Mott content quantified:** with amplitude conditioning the angular deviation
  *plateaus* at ~σ_meas (5.7°/17.5°/45.8° for σ = 5°/15°/40° at k=60); memoryless
  scattering with the same per-event width diffuses as σ√k (32°/96°/246°). The
  plateau-vs-diffusion contrast is why tracks are straight.
- **E4 Emergent Bragg curve:** with Bethe-inspired event spacing (ℓ ∝ E), deposition
  density shows the clinical shape — flat entrance, peak (~3× plateau) at 93% of mean
  range, sharp distal falloff; range straggling ±5.9 on mean 51.2 from stochastic
  per-event loss. Proton-therapy depth-dose from the recoil channel of a measurement
  toy model.

Ledger: per-event Born weighting, σ_meas (per-event partiality), and ℓ ∝ E are inputs;
emergent are the click↔track interpolation, the straightness (conditioning, not
memorylessness), and the Bragg shape. Exclusivity generalized as one record per *event*
(per-event E–p budget), sequential events allowed — completing the §5 taxonomy in code:
photodetector (k=1, β→1), cloud chamber (β→0, one particle/many sites), film (parent
script's k≥2, many quanta/one site), all one capture→commit→closure mechanism.
