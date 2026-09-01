---
title: "Photon Dirac-like evolution and the absorption-to-avalanche bridge"
kind: spec
---

# Photon Dirac-like evolution and the absorption-to-avalanche bridge

## Citation finding

Paper 3 already cites Białynicki-Birula (1996), *Photon wave function*, and already states the necessary caveats: the photon is spin 1; the Riemann–Silberstein helicity sectors obey decoupled Weyl-form equations; and these sectors are not literal spin-½ electron spinors.

Two strong additional primary references are:

1. S. M. Barnett, “Optical Dirac equation,” *New Journal of Physics* **16**, 093008 (2014), doi:10.1088/1367-2630/16/9/093008. It writes source-free Maxwell equations in a form analogous to the free-electron Dirac equation and explicitly relates the three-component spin-1 matrices to the two-component spin-½ Weyl construction.
2. P. J. Mohr, “Solutions of the Maxwell equations and photon wave functions,” *Annals of Physics* **325**, 607–663 (2010). It gives a six-component matrix Maxwell equation analogous to the four-component Dirac equation, two uncoupled circular-polarization equations analogous to Weyl equations, wave-packet evolution, source terms, and the associated Poynting energy balance.
3. Tamburini and D. Vicino, “Photon wave function: A covariant formulation and equivalence with QED,” *Physical Review A* **78**, 052116 (2008), is useful as a scope citation: the Dirac-like photon-wave-function formulation is an alternative representation consistent with standard electrodynamics/QED, not by itself a new theory of interacting photons and matter.

### Recommended wording

<user_quoted_section>Source-free Maxwell evolution admits a first-order spin-1 matrix form analogous to the massless Dirac/Weyl equations. Its two helicity sectors propagate independently in vacuum because no mass term couples them. This is a structural spin-1 analogy, not the assertion that a photon is an ordinary spin-½ Dirac particle.</user_quoted_section>

## Author's absorption picture

John's intended picture is:

- the photon wave packet and detector-electron states are physically real and delocalized;
- their interaction initially creates a distributed excitation pattern;
- a competitive focusing or “rogue-wave” process concentrates the one-quantum excitation into one electronic channel;
- the selected excitation then seeds a condensed-matter cascade; and
- an applied electric potential strongly biases the downstream carrier motion and amplification.

## A precise quantum-state bridge

A clean starting point is

`|Ψ(0)⟩ = |1_f⟩ |G⟩ |B_0⟩`,

where `|1_f⟩` is the incident one-photon wave packet, `|G⟩` is the detector ground state, and `|B_0⟩` is the initial environment. Electromagnetic coupling can produce

`|Ψ(t)⟩ = α(t)|1_f,G,B_0⟩ + Σ_i β_i(t)|0,E_i,B_i(t)⟩ + …`,

where `|E_i⟩` denotes a localized electronic excitation or, more realistically in a solid, a localized component of an excitonic/carrier mode. This expression captures distributed absorption amplitudes without assigning each site a separately possessed classical fraction of the photon energy.

Standard unitary evolution leaves a superposition of the `i` channels. The framework's unresolved selection problem is to derive why one channel becomes the single ontic commit while the others return their amplitude/energy to the remaining field and detector degrees of freedom.

## Status of the rogue-wave analogy

The analogy is useful only if labeled as an organizing picture. Classical rogue-wave concentration requires a focusing or nonlinear instability; linear interference alone creates high local intensity but does not establish irreversible transfer of the full quantum into one channel. To make the analogy a mechanism, the detector model must derive the corresponding nonlinear or stochastic focusing term and its conservation law.

“Competitive localization of a distributed excitation” is a safer provisional term than “rogue-wave absorption” in theorem statements.

## Correct SPAD energy ledger

For an avalanche detector, the photon energy seeds the process but does not power the macroscopic avalanche:

1. photon absorption creates an electron–hole excitation and any excess above the relevant transition/band energy may thermalize into the lattice;
2. the applied electric field accelerates carriers;
3. carriers obtain energy from the detector's bias supply and cause impact ionization;
4. the avalanche's macroscopic energy therefore comes predominantly from the external electrical reservoir;
5. quenching and reset dissipate that supplied energy into the circuit and bath.

The conserved ledger must consequently track

`E_total = E_incident field + E_detector matter + E_lattice/bath + E_bias supply`.

The framework repository already contains a directly relevant working note, `single_photon_derivation.md`, which identifies the SPAD cascade as an amplitude-branching process with the bias voltage as the free-energy reservoir. It also correctly records that this derivation supplies detector response and amplification probability but does not yet derive the Born weight.

## Revision implications

- Cite the optical-Dirac/Maxwell literature in Paper 3, where the photon-as-uncoupled-limit claim is made; cross-reference it briefly from Paper 1 rather than making photon representation a second theme there.
- In Paper 1, use the distributed excitation state to define the physical problem before introducing c-number site stakes.
- Make the “one localized electronic commit” the precise event the Born Selection mechanism must derive.
- Put the field-biased avalanche downstream of that commit unless a coupled calculation shows amplification backaction participates in selection.
- Separate the photon-energy ledger from the much larger bias-supply energy that powers registration.

No manuscript or reference list has been edited; these are citation and revision recommendations.
