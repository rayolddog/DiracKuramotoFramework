# DRAFT subsection — "What the measurement coupling can and cannot supply"

*Intended for PAPER_REVISED.md, in the measurement/Born section (after the §3.2 D[σₓ]
material). Technical draft — integrate/reword to taste. Backing computations:
`code/born_decisive.py`, `code/born_noise_structures.py`, `code/born_mass_penrose.py`.*

---

## X.Y  What the measurement coupling can and cannot supply

The two-stage account locates outcome selection at the onset of Stage 2, the
dissipative locking of the chiral interference phase. For that account to recover the
Born weights rather than merely *a* binary, the Stage-2 coupling must take a specific
form, and it is worth stating plainly what that form is and whether the framework's own
ingredients supply it.

**The requirement.** Write the equatorial state of the chiral qubit as
$|\psi\rangle = (|L\rangle + e^{i\phi_0}|R\rangle)/\sqrt{2}$, with pointer states at
$\phi=0,\pi$. The Born weight of the $\phi=0$ pointer is $\cos^2(\phi_0/2)$. Modelling
Stage 2 as a phase diffusion $d\phi = a(\phi)\,dt + \sqrt{2D(\phi)}\,dW$ with wells at
$0,\pi$, the basin-splitting probability (committor) is fixed by the scale density
$s(\phi)=\exp\!\big(-\!\int a/D\big)$. One finds that the split equals
$\cos^2(\phi_0/2)$ **for one structure only**: the diffusion must be
$D(\phi)=2\gamma\sin^2\phi$ *linked* to the drift $a=-\gamma\sin2\phi$, giving
$a/D=-\cot\phi$, $s(\phi)=\sin\phi$, and committor $(1+\cos\phi)/2$ exactly. The factor
$\sin^2\phi = 1-\langle\sigma_x\rangle^2 = \mathrm{Var}(\sigma_x)$ is not arbitrary: it
is the *measurement back-action* of $\sigma_x$, which vanishes at the pointer states
(where there is nothing left to measure) and is maximal on the equator. Equivalently,
Stage 2 must be a quantum-non-demolition (QND) measurement of the interference channel,
$\mathcal{D}[\sigma_x]$. Any additive (pointer-independent) noise — thermal or vacuum —
fails: it does not vanish at the pointers, leaks probability out of the wells, and bends
the split away from $\cos^2(\phi_0/2)$ toward a step or toward $1/2$.

**What the gauge coupling actually supplies.** In the chiral reduction
($\gamma^0=\sigma_x$, $\gamma^1=-i\sigma_y$, $\gamma^5=\sigma_z$) the scalar density is
$\bar\psi\psi=\sigma_x$, the charge density is $j^0=\psi^\dagger\psi=\mathbb{1}$, and the
spatial current is $j^1=\bar\psi\gamma^1\psi=\sigma_z$. The mass term $m\bar\psi\psi=
m\sigma_x$ enters the system Hamiltonian as a c-number; it is *not* a coupling to the
bath. The QED gauge vertex $e\,j^\mu A_\mu$ couples the system to the radiation field —
and hence to any photonic/vacuum bath, including the detector — through $\mathbb{1}$ and
$\sigma_z$, **not** through $\sigma_x$. Carrying the corresponding Born–Markov dissipator
through to the basin split, the $\sigma_z$ coupling reproduces the Born weights in no
regime: for $p=0$ it is transverse to $H_S=m\sigma_x$ and drives *relaxation* toward the
$\sigma_x$ ground state (monostable at $T=0$, a Boltzmann mixture at $T>0$); for
$p\gg m$ it is longitudinal and drives *dephasing* in the chirality basis. In every case
the outcome probability is independent of $\phi_0$ — the input amplitude is erased — so
the gauge coupling does not even constitute a measurement of $\sigma_x$, let alone a
Born-weighted one. The QND structure $\mathcal{D}[\sigma_x]$ that Stage 2 requires is
therefore *assumed* in identifying the measured observable; it is not delivered by the
electromagnetic interaction that physically couples particle to detector.

**The only coupling that would deliver it, and where that leads.** A dissipator
$\mathcal{D}[\sigma_x]=\mathcal{D}[\bar\psi\psi]$ requires the bath to couple to the
*scalar/mass density* — a Yukawa-type scalar field or, equivalently, a fluctuating mass
(a dynamical chiral condensate). This is precisely the operator of Diósi–Penrose
gravitational decoherence, which localizes in the mass-density basis. The escape route
"mass as a dynamical synchronization field" is thus, structurally, gravitational
decoherence read in the no-collapse, dissipative mode (the Diósi master-equation reading
rather than Penrose's objective reduction). Two facts make this a costly route rather
than a resolution. First, the rate: the Penrose self-energy timescale
$\tau\sim\hbar/E_G$ with $E_G\sim GM^2/R$ is $\sim10^{24}\,$s for an electron and
$\sim10^{16}\,$s for a single atom — many orders of magnitude beyond any measurement —
and becomes sub-microsecond only at macroscopic pointer masses ($\gtrsim10^{-9}\,$kg).
Mass-density coupling therefore forces the locus of selection onto the heavy detector
(Penrose's own conclusion) and localizes the *pointer's* configuration, reached only
indirectly through entanglement with the chiral channel. Second, and decisively for the
present purpose, Diósi–Penrose and the broader objective-collapse family do not
*derive* the Born weights either; they post-impose them through the normalization of the
collapse noise, exactly as CSL does. Routing Stage 2 through a mass-density bath thus
relocates the Born-measure question to the gravitational sector without answering it.

**The 3+1D statement (not a reduction artifact).** The conclusion does not rely on the
1+1D toy model; it follows from the chiral classification of Dirac bilinears, an exact
consequence of chiral symmetry. The sixteen bilinears split by their behavior under
$\psi\to e^{i\alpha\gamma^5}\psi$: the **vector and axial** currents
($\bar\psi\gamma^\mu\psi$, $\bar\psi\gamma^\mu\gamma^5\psi$) are chirality-**preserving**
($\bar\psi_L\Gamma\psi_L$, $\bar\psi_R\Gamma\psi_R$), while the **scalar, pseudoscalar,
and tensor** ($\bar\psi\psi$, $\bar\psi i\gamma^5\psi$, $\bar\psi\sigma^{\mu\nu}\psi$)
are chirality-**flipping** ($\bar\psi_L\Gamma\psi_R$). The QED gauge field couples to the
vector current $\bar\psi\gamma^\mu\psi$ — chirality-preserving — so in the chiral qubit it
supplies only the charge density ($j^0=\mathbb{1}$) and the chirality-diagonal spatial
current ($\sigma_z$ sector); it cannot generate the $L\leftrightarrow R$ mixing
$\bar\psi\psi=\sigma_x$. The magnetic-moment (Pauli, tensor) term *is* chirality-flipping,
but it acts on **spin**, coupling spin to $B$ (Stern–Gerlach) — a different qubit from the
chiral channel — not on the scalar $\bar\psi\psi$. Equivalently, at the self-energy level:
the QED self-energy $\Sigma = \Sigma_V(p^2)\,\not p + \Sigma_S(p^2)\,m$ has a scalar
(mass-dressing) part that is **proportional to $m$ and protected by chiral symmetry**
($\Sigma_S\to0$ as $m\to0$), so its absorptive piece $\mathrm{Im}\,\Sigma_S$ — the very
mass-channel Adler lock invoked for Stage 2 — is the *chirally suppressed* one, while the
unsuppressed dissipation lives in the chirality-preserving vector channel
$\mathrm{Im}\,\Sigma_V$. The operator that reaches $\bar\psi\psi$ without this suppression
is one that couples to the scalar/mass density directly: a Yukawa scalar, or gravity —
$\bar\psi\psi$ is (up to the equations of motion) the trace of the stress–energy tensor
$T^\mu{}_\mu = m\bar\psi\psi$. This is the rigorous reason the Born-compatible coupling is
gravitational, and it is exact, not a feature of the reduction.

**Status.** We therefore do not claim to derive the Born rule. The continuous,
no-collapse account is consistent with it — the QND $\mathcal{D}[\sigma_x]$ unraveling
reproduces $\cos^2(\phi_0/2)$ — but that dissipator is an input identifying the measured
channel, and the electromagnetic coupling that actually mediates detection supplies a
different one ($\sigma_z$: relaxation/dephasing, not $\mathcal{D}[\sigma_x]$). The single
coupling that would supply $\mathcal{D}[\sigma_x]$ is mass-density (gravitational), which
both fails on rate for microscopic systems and inherits the unsolved Born-measure
problem of the objective-collapse programs. We regard the origin of the Born weights as
open, and — on this analysis — *uniformly* open across the synchronization and
gravitational-reduction approaches alike.
