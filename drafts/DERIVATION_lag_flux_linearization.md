# Where the Haldane Flux Honestly Enters the Oscillator Linearization

*Date: 2026-07-05. Referee-proofing derivation for `EMERGENT_FIELDS_PAPER.md`
(closes the gap flagged in `drafts/EMERGENT_FIELDS_NOVELTY_CHECK.md`). All
numerical claims are outputs of `code/stuartlandau_haldane_check.py`, which
validates its Bloch construction against a brute-force Jacobian of the real
nonlinear dynamics (multiset eigenvalue agreement ≤ 10⁻⁹ at three coupling
mixing angles). Status: **the result is sharper than the claim it was meant to
protect** — it adds one no-go theorem and two physical requirements.*

## 0. Summary for the paper

The chain "Sakaguchi lag ⇒ Haldane flux ⇒ $C=\pm1$" is TRUE but under three
conditions, all now derived and verified:

1. **Amplitude dynamics must be alive** (limit-cycle / Stuart–Landau
   oscillators). Phase-only models — first-order *or* inertial — cannot host
   the flux at linear order (Lemma 1). And even with amplitude dynamics, the
   topological gap dies when the amplitude stiffness $r_0^2$ is taken to
   infinity (the phase-reduction limit): verified, $C: +1 \to 0$ between
   $r_0^2 = 7$ and $19$ at our parameters.
2. **The lag pattern must be antisymmetric** ($\alpha_{ij}=-\alpha_{ji}$, the
   Haldane orientation on NNN bonds) — this is exactly a Dzyaloshinskii–Moriya
   structure in oscillator language. The symmetric (uniform-delay) Sakaguchi
   lag contributes only a global complex rotation.
3. **The coupling must have a reactive component** (Theorem 1, the no-go):
   purely dissipative coupling — the standard Kuramoto realization — gives an
   *exact* degeneracy of the two least-damped bands at $K, K'$ for every
   amplitude stiffness: flux in the eigenvectors, no gap in the spectrum, no
   topological phase. The gap turns on $\propto \sin\beta$ where $\beta$ is
   the dissipative→reactive mixing angle, and the magnon precedent (Kim et
   al. 2016) sits at exactly $\beta=\pi/2$.

## 1. Lemma 1 (the phase-only trap)

Linearize $-K\sin(\theta_i-\theta_j+\alpha_{ij})$ about the uniform sync state
($\theta_i = \bar\theta$): the fluctuation force is
$-K\cos\alpha_{ij}\,(\varepsilon_i-\varepsilon_j)$ plus a constant. Because
$\cos$ is even, $\cos\alpha_{ij}=\cos\alpha_{ji}$ **whatever the lag pattern**:
the coupling matrix is real symmetric (a $\cos\alpha$-weighted Laplacian). A
real symmetric stiffness supports no Berry curvature, and its NNN "mass
channel" $d_z\propto(\gamma_A-\gamma_B)$ vanishes identically (verified:
$d_z(K)=0$ exactly, for every $\alpha$). Adding inertia ($m\ddot\varepsilon$)
leaves the stiffness real symmetric. **No phase-only Kuramoto model has a
linear-order Haldane phase.** The $\sin\alpha_{ij}$ piece survives only in the
constants (frequency shift) and at quadratic order.

## 2. The honest model and its linearization

Limit-cycle oscillators (Stuart–Landau; phase reduction = Kuramoto–Sakaguchi):

$$
\dot z_i = (\mu + i\omega)z_i - |z_i|^2 z_i
 + e^{i\beta}\sum_j g_{ij}\,e^{i\alpha_{ij}} z_j ,
$$

with $g_{ij}$ real ($g_1$ on NN, $g_2$ on NNN), $\alpha_{ij}$ the antisymmetric
NNN lag with Haldane orientation, and $\beta$ the coupling's global
dissipative/reactive angle. Uniform sync state $z_i = r_0 e^{i\Omega t}$ with
$r_0^2 = \mu + \mathrm{Re}[e^{i\beta}\chi]$, $\chi = 3g_1 + 6g_2\cos\alpha$
(the antisymmetric pattern cancels the $\sin\alpha$ frequency shift).

Linearizing $z_i = (r_0 + a_i)e^{i\Omega t}$ in the complex envelope $a$ gives,
in Bloch form on the basis $(a_A(k), a_B(k), a_A^*(-k), a_B^*(-k))$:

$$
\frac{d}{dt}\,v = M(k)\,v,\qquad
M(k)=\begin{pmatrix} c\,\mathbb 1 + e^{i\beta}S(k) & -r_0^2\,\mathbb 1 \\
                     -r_0^2\,\mathbb 1 & \bar c\,\mathbb 1 + e^{-i\beta}\bar S(-k)
     \end{pmatrix},
$$

with $c = \mu - 2r_0^2 - i\,\mathrm{Im}[e^{i\beta}\chi]$ and

$$
S(k) = \begin{pmatrix} \gamma_A(k) & f(k) \\ \bar f(k) & \gamma_B(k)\end{pmatrix},
\quad
\gamma_{A/B}(k) = 2g_2\sum_m \cos(k\!\cdot\! b_m \pm \alpha),\quad
f(k) = g_1\sum_\delta e^{ik\cdot\delta}.
$$

**$S(k)$ is exactly the Haldane Bloch Hamiltonian** — $\tfrac12(\gamma_A-
\gamma_B) = -2g_2\sin\alpha\sum_m\sin(k\!\cdot\!b_m)$ is the topological mass
— so the complex hopping $g_2 e^{\pm i\alpha}$ *is* a Peierls phase, exactly
as the dictionary asserted. But the physical spectrum is that of $M(k)$, not
$S(k)$: the amplitude nonlinearity adds the local anomalous block $-r_0^2$
coupling each mode to its conjugate partner, **which carries the
opposite-mass Haldane copy** ($\bar S(-k)$ has $\gamma_A \leftrightarrow
\gamma_B$). Everything below is the fight between $S$ and its shadow.

## 3. Theorem 1 (dissipative no-go)

At $\beta=0$ (real coupling — the standard "sum of sines" Kuramoto case), $c$
is real. At $K$ (where $f=0$) the $4\times4$ blocks decouple into sublattice
sectors

$$
\mathcal A = \begin{pmatrix} c+\gamma_A & -r_0^2 \\ -r_0^2 & c+\gamma_B\end{pmatrix},
\qquad
\mathcal B = \begin{pmatrix} c+\gamma_B & -r_0^2 \\ -r_0^2 & c+\gamma_A\end{pmatrix},
$$

which have identical trace and determinant, hence **identical eigenvalue
pairs: the two least-damped bands are exactly degenerate at $K$ (and $K'$)
for every $r_0^2$ and every $\alpha$.** The Dirac touching survives; the
Haldane mass is neutralized by its particle-hole shadow. Verified numerically:
$|\lambda_0-\lambda_1|(K) \le 10^{-15}$ at $r_0^2 = 3.5,\,7,\,35$. This is the
BdG avatar of Lemma 1 — the same evenness obstruction, one level up.

For $\beta\neq0$ the sector traces differ by
$2i\sin\beta\,(\gamma_A-\gamma_B)$: **the K-point splitting switches on
proportionally to $\sin\beta$ times the Haldane mass.** Verified: gap$(K)$
rises from $0$ at $\beta=0$ to $2.80$ at $\beta=\pi/2$ (non-monotonic
crossover region near $\beta\approx0.6$–$0.9$ where the gap changes character
from dissipative to reactive).

## 4. The reactive regime (where the claim is true)

At $\beta = \pi/2$ (Hamiltonian-like coupling — lasers/photonic lattices,
reactive JJ networks; the magnon limit), with $g_1=1$, $g_2=0.3$,
$\alpha=\pm\pi/2$, $\mu=0.5$:

| check | result |
|---|---|
| Chern number of upper positive-frequency band | $C = \pm 1 = \mathrm{sign}(\alpha)$ |
| minimum band-pair gap | $2.04$ |
| robustness | $C=+1$ at $r_0^2 = 3.2,\,4,\,7$; $C\to0$ by $r_0^2=19$ |

The last line is the quantitative form of "phase reduction kills the flux":
increasing amplitude stiffness drives the system toward the phase-only limit
and the topological gap closes on the way. The topological phase lives in the
window where the amplitude quadrature is dynamically accessible.

## 5. Consequences

- **For the paper's §3:** `honeycomb_emergence.py` writes the Haldane Bloch
  Hamiltonian with $\phi=\alpha$ by dictionary. That is now *derived* — it is
  the particle-conserving block of the honest linearization — but its spectrum
  is physical only given amplitude dynamics + antisymmetric lag + reactive
  coupling. The paper's claims must carry those three conditions.
- **For §6 (platforms):** the requirement $\beta\neq0$ reorders the platform
  list. Laser arrays and photonic/polariton lattices (reactive-dominant
  coupling) move to the front; overdamped, dissipatively coupled arrays are
  excluded at linear order. Josephson and NEMS/optomechanical arrays qualify
  to the extent their coupling has a reactive (energy-conserving) component —
  which it generically does.
- **Relation to the magnon precedent:** Kim–Ochoa–Zarzuela–Tserkovnyak (PRL
  2016) is recovered as the $\beta=\pi/2$, $r_0^2$-rigid corner of this phase
  diagram (precessional dynamics, DMI = antisymmetric lag). What the
  oscillator version adds is the two new axes — dissipative/reactive mixing
  $\beta$ and amplitude stiffness $r_0^2$ — and the no-go/crossover structure
  along them. That is a *stronger* novelty position than the original
  dictionary claim, and it is falsifiable in hardware: tune a laser array's
  coupling phase through $\beta_c$ and watch the chiral edge mode die.
- **For the DK framework thread:** the "shadow copy" mechanism (conjugate
  sector carrying the opposite mass) is structurally the same L↔R pairing that
  the 3D story (`weyl3d_emergence.py`) treats as the chiral mass coupling —
  worth a closer look at whether the dissipative no-go has a 3+1D analogue.

## Glossary extensions

- **Reactive vs dissipative coupling** — the energy-conserving
  (frequency-pulling, $i g$) vs energy-exchanging (amplitude-pulling, real
  $g$) parts of an oscillator coupling; $\beta$ parametrizes the mix.
- **Bogoliubov / anomalous block** — the part of a linearization that couples
  a fluctuation mode to the complex conjugate of another; here generated by
  the $|z|^2 z$ nonlinearity, strength $r_0^2$.
- **Peierls phase** — the complex phase a hopping amplitude acquires along a
  link; its loop sum is a magnetic flux for the lattice problem.
