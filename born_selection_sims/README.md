# born_selection_sims — Simulations for the Outcome-Selection (Born Rule) Paper

Archived 2026-07-20 from the derivation session (session log: `sessions/2026-07-20-born-gamblers-ruin-outcome-selection.md`; paper outline: `drafts/PAPER1_OUTLINE_born_selection.md`). All scripts are self-contained (numpy only), run in seconds-to-minutes via `python3 <script>.py`, and have **pinned seeds** (`np.random.default_rng(N)`) — outputs are reproducible and match the numbers quoted in the derivation notes.

Run order below follows the derivation chain. "Note" column = the drafts/ document that quotes each script's results.

| # | Script | Demonstrates | Note |
|---|--------|--------------|------|
| 1 | `tango_selection.py` | **Failure (diagnostic):** one-shot winner = max instantaneous overlap \|A·cosθ\| is far too winner-favoring (bright-among-nine wins 79% vs Born 50%). Motivates the prolonged fair game. | NOTE_born_gamblers_ruin §2 |
| 2 | `gambler_ruin_born2.py` | **Failure (diagnostic):** fixed-step exchange clipped at zero = reflecting boundary = drift; Born badly broken. Shows the martingale property is knife-edge. | NOTE_born_gamblers_ruin §2 |
| 3 | `gambler_ruin_born3.py` | **Pass:** stakes-scaled fair exchange (δ = ±step·min(eᵢ,eⱼ)) reproduces Born to ~2% at absorb 0.95 (exact in continuum limit by optional stopping). | NOTE_born_gamblers_ruin §2 |
| 4 | `soft_threshold_born.py` | Born deviation vs soft lock-layer width w with the worst-case (Adler-tail) bias profile: dev ~ w^0.4 — sharpness is required, not optional. | NOTE_born_gamblers_ruin §3b |
| 5 | `gapped_threshold_born.py` | Tail-free (slaved-phase-licensed) bias profile cuts deviations 5–15× at fixed w — the slaving proof's numerical payoff. | DERIVATION_slaved_phase §4b |
| 6 | `noise_scaling_born.py` | **The knife-edge:** √e (amplitude-linear) noise reproduces Born; additive noise → rich-get-richer; multiplicative → equalizing. Verifies the Itô fairness theorem. | DERIVATION_slaved_phase §3–4a |
| 7 | `window_tests.py` | (A) Commit-at-layer-entry boundary error is at the MC noise floor for realistic w; (B) fully common-mode noise is catastrophic (bright wins 100%) — motivates the correlation analysis. | DERIVATION_slaved_phase §7 |
| 8 | `vacuum_correlation_born.py` | Correlated-noise drift on fringe patterns (3 vacuum kernels incl. polarization-dependent); full game: +20% violation at λ/2 fringes at f=1; deviation ∝ correlated fraction f (locality protection). | DERIVATION_vacuum_noise §3 |
| 9 | `rate_commit_born.py` | **Rate-linearity theorem:** commit rate ∝ share^α — α=1 gives Born at every commit speed; α=2 / α=0.5 deviate exactly as theory predicts and relax toward Born at slow commit. | DERIVATION_slaved_phase §9 |
| 10 | `bell_pair_game.py` | Two-wing joint game: CHSH S = 2.82 ≈ 2√2; fidelity law S = 2√2·η; no-signaling and commit-order independence verified. | DERIVATION_bell_pair §3 |
| 11 | `inverted_gisin.py` | Signaling amplitude of a hypothetical commit nonlinearity ε on partially entangled states: closed form vs full game; exact zero at ε=0 and at p=½ (symmetry protection). | DERIVATION_inverted_gisin §3 |
| 12 | `multiquantum_rho_linearity.py` | N-quantum registry game reproduces Glauber counting: perfect anti-bunching (\|1,1⟩) and bunching ((\|2,0⟩+\|0,2⟩)/√2) with identical marginals; two-photon absorber correctly silent on \|1,1⟩; mixture affinity. | DERIVATION_multiquantum §4 |
| 13 | `stage2_port_signaling.py` | Port-level bias from mismatched within-port noise correlation: κ ≈ −c, P′(S) ≈ S + κS(1−S); matched-ports control fair; degenerate c=1 limit (collective death, state-dependent no-click). | DERIVATION_stage2_signaling §2 |

Notes for paper figures: Fig. 2 ← #6; Fig. 3 ← #1–3; Fig. 4 ← #4–5; Fig. 5 ← #12; Fig. 6 ← #10; Fig. 7 ← #13 (plus the constant-efficiency QM comparison line, to be added).

Superseded/not archived: `gambler_ruin_born.py` (v1, unvectorized, timed out; superseded by #3).
