# G3 drain tests

Numerical probes behind `drafts/CONTRACT_G3_field_matter_selector.md`.
Pure stdlib + numpy. No comparator is imported into any raw path; the winner is
whoever reaches the absorbing boundary, and no outcome is drawn from |A_i|^2.

| script | question | result |
| --- | --- | --- |
| `drain_variants.py` | Does the drain's *timing* decide whether Born survives? | Yes, decisively. Sink-on-commitment 0.497 vs Born 0.500; attractor-during-competition 0.634 / 0.981 / 1.000 as gain rises. Linear aperture (alpha=1) is share-neutral, confirming Theorem 2(i). |
| `exchange_kernel.py` | Does the *derived* exchange kernel give Born, or only the ad hoc `min` rule? | Derived geometric-mean kernel converges to Born; finite-step bias tracks the clamp rate, which falls as step^2. |

Raw output: `results_drain_variants.txt`, `results_exchange_kernel.txt`.
Reproduce: `python3 drain_variants.py` (~4 min), `python3 exchange_kernel.py` (~20 min).
