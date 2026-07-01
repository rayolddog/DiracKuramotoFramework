# 2026-07-01 — Born from wave-energy: substrate sampling, the two seams, and the gravitational discriminator

*Session log. Formal write-up: [`../drafts/NOTE_wave_energy_interpretation.md`](../drafts/NOTE_wave_energy_interpretation.md) §7½. Code: [`../code/born_substrate_sampling.py`](../code/born_substrate_sampling.py), [`../code/detector_resonance_selection.py`](../code/detector_resonance_selection.py).*

## Where it started

Reconstructed a discussion that began, some time back, with a **hologram** thought experiment — recording an interference pattern as a photon deposits energy in a silver-halide grain, squaring the wave to hit the developing threshold — and carried to a claim: the wave packet represents **real energy**, not a probability amplitude in Hilbert space, and on that reading both the Born rule and Heisenberg uncertainty stop being postulates. Electron microscopy came up as an attempt to extend the energy grounding from photons to electrons.

Honest correction reached first: the wave-energy route **derives the `|ψ|²` *form*** (positivity + bilinearity + Parseval force the square, no probability axiom), and **dissolves Heisenberg into the Fourier/Gabor bandwidth theorem** (textbook; only the substrate-sampling tie is framework-specific) — but it does **not** by itself derive Born as a *probability*, and electron microscopy actually *sharpens* the gap (a boson has a classical field whose energy is `|E|²`; a fermion does not, so `|ψ|²` is Born from the start unless the substrate makes the electron a real energy-carrying oscillation). See NOTE §2–§5.

## The run: Born from a random-phase substrate bath

Took a run at the open piece — show a substrate oscillation both carries energy `∝ |ψ|²` **and** produces `|ψ|²` landing frequencies. Physical inputs the user supplied were load-bearing: the **bulk is disordered, phases random, tiny coherent background**; the **quantum vacuum enters at the detector surface** as a reference (possibly cosmic-background-coherent); gravity negligible.

**Mechanism** ([`born_substrate_sampling.py`](../code/born_substrate_sampling.py)): each detector atom is a threshold-escape clock driven by a **linear** real oscillation `a|ψ|cos(ωt+φ)` in a random-phase bath. Averaging over the random phase kills the linear term (`⟨cos⟩=0`) and leaves the **power** — `Δr ∝ |ψ|²`. The squaring is *generated from a linear input*, so the golden-rule circularity ("assume rate ∝ |amplitude|²") is avoided. Winner-take-all among indivisible quanta → Born. Numerics: excess rate tracks `A²/4` to <2% for weak drive; TVD from Born **0.0008** (discrete), **0.0037** (interference fringes). It **breaks** where predicted — strong signal and coherent bulk → Born deviations — so it's falsifiable, not tautological.

Honest ledger: this is **proof of mechanism, not of nature**. Given (A) ψ is a real oscillation coupling linearly and (B) the bulk is a random-phase equilibrium bath, Born follows. (B) is the relocated Born postulate = Valentini quantum-equilibrium, now a physical bath condition with non-equilibrium deviation signatures.

## Closing the seams

**Open computation #1 (Lagrangian grounding of A).** From the Dirac Lagrangian: Noether U(1) gives `j⁰ = ψ†ψ = |ψ|²` (unique positive conserved density); time-translation gives `T⁰⁰ = E|ψ|²` for a stationary state. So "energy density ∝ |ψ|²" is **derived for equal-energy channels**. Left two seams.

**Seam 1 — equal-energy — CLOSED** ([`detector_resonance_selection.py`](../code/detector_resonance_selection.py)). Two reasons: (i) a resonant detector is a narrow filter at `ℏω_d`, so it sees one energy and `E|ψ|² ∝ |ψ|²`; (ii) deeper — ordinary detectors couple to the **charge** density `j⁰=|ψ|²` (→ `A_μ`, electromagnetic), *not* the **energy** density `T⁰⁰=E|ψ|²` (→ `g_μν`, gravitational). So all EM detection reports Born, `E`-independent (verified: charge readout of an unequal-energy state → Born, TVD 0.004; energy readout → `E_n|c_n|²`, TVD 0.13). The `E|ψ|²` weighting is **gravitational-only**.

**Seam 2 — real field vs. probability amplitude — LOCATED.** The sharp result: every Standard-Model force couples to a conserved current `∝ |ψ|²`, so the real-field and amplitude readings are **empirically identical everywhere except gravity** (the only thing coupling to `T⁰⁰=E|ψ|²`). This *retro-explains* why the framework's one candidate signature was always gravitational. The discriminator is the **Bose–Marletto–Vedral** class of tabletop tests: does a delocalized quantum source a spread `E|ψ|²` mean field (real-field → no gravitational entanglement) or a superposed/quantized field (amplitude → entanglement)? Caveats: semiclassical gravity has known problems (may force a Diósi–Penrose-type collapse, already constrained); BMV is a decade-plus away; the framework's gravitational postulate has its own baggage.

## Occam (user raised it)

Is energy-realism favored by parsimony? The strong form is the **Boltzmann move** (replace a primitive postulate with derived equilibrium statistics) and it *unifies* (one lever dissolves Born-form, normalization, and Heisenberg). But raw assumption-count is a wash (trades Born for substrate-realism + bath-equilibrium), and — decisively — the two readings are **not empirically equivalent** (energy predicts Born deviations). So prefer it for **falsifiability, not parsimony**: *Popper before Occam.*

## Net + next

Born's *squaring* is off the assumption list (earned twice: Noether form + power/phase-cancellation). Discreteness = indivisibility. Typicality = the random-phase bath (B). Equal-energy seam = closed. The **single remaining hinge is seam 2**, and it is empirically decidable — gravitationally.

**Decision on the paper:** keep the Aperture demonstration **frozen**; continue physics here in DiracKuramotoFramework. The living manuscript is `current_revision_DK_paper.md` (copied from the 06-30 Aperture snapshot). A short, honestly-bounded revision incorporating these results — the substrate outcome-selection mechanism as a *candidate* completion of Appendix D, plus the "difference is gravitational-only" structural result strengthening §6 — is planned, **not yet written** (stance stays "Born-compatible, not Born-derivative").

**Open next:** (1) draft that bounded revision plan; (2) quantify the gravitational `E`-weighting / BMV discriminator; (3) Heisenberg computation #2 (substrate phase-space cell = `h`); (4) which side investigations (AB, discretization, cosmic-expansion) need updating in light of the above.
