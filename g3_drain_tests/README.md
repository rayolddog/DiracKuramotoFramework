# G3 drain tests

Numerical probes behind `drafts/CONTRACT_G3_field_matter_selector.md`.
Pure stdlib + numpy. No comparator is imported into any raw path; the winner is
whoever reaches the absorbing boundary, and no outcome is drawn from |A_i|^2.

| script | question | result |
| --- | --- | --- |
| `drain_variants.py` | Does the drain's *timing* decide whether Born survives? | Yes, decisively. Sink-on-commitment 0.497 vs Born 0.500; attractor-during-competition 0.634 / 0.981 / 1.000 as gain rises. Linear aperture (alpha=1) is share-neutral, confirming Theorem 2(i). |
| `exchange_kernel.py` | Does the *derived* exchange kernel give Born, or only the ad hoc `min` rule? | Derived geometric-mean kernel converges to Born; finite-step bias tracks the clamp rate, which falls as step^2. |
| `theorem5_check.py` | Is Born robust to the commit-rate *law* at fast commit? | Linear law: Born at every speed (Theorem 4). Arrhenius law: 0.719 vs 0.500 at fast commit, 0.504 when slowed to Paper 1 §6.1's separation. |
| `threshold_gated_commit.py` | If only sites above θ = E_gap/E_photon can commit (Paper 1 v0.8 §6.1, reading A), how long is the winner actually exposed, and what does the gate do to the outcome? | Exposure is 40–90% of the game in this engine, not one exchange step. Ungated (θ = 0) linear law gives Born at every speed; *any* gate biases toward the bright site even for a linear law — +0.04 at one expected commit per exposed leg, +0.12 to +0.19 at ten (80/20 and ten-site). Grounds for Paper 1 v0.9's adoption of reading B. |

Raw output: `results_drain_variants.txt`, `results_exchange_kernel.txt`, `results_theorem5_check.txt`, `results_threshold_gated_commit.txt` (all gitignored by the `*.txt` rule; regenerate).
Reproduce: `python3 drain_variants.py` (~4 min), `python3 exchange_kernel.py` (~20 min), `python3 theorem5_check.py` (~2 min), `python3 threshold_gated_commit.py` (2-site and 10-site grids in ~8 min; the 100-site grid dominates the run).
