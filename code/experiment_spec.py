#!/usr/bin/env python3
r"""
experiment_spec.py
==================

Turns the silver/two-basin discussion into a concrete experimental requirement.

The framework reproduces standard QM EXCEPT for one free deviation: whether the
Stage-2 measurement attractor (rate gamma) leaks into Stage-1 free propagation
(gamma_flight > 0).  This is the only falsifiable handle in the fringe channel.

Two observables, with their measurement requirements:

  (1) PRIMARY -- the visibility-vs-noise SHAPE / initial slope.
      QM (pure dephasing):   V = exp(-sigma^2/2)         -> slope dV/dsigma^2|_0 = -1/2
      two-basin (attractor):  in-well plateau V~exp(-sigma^2/8gamma)
                                                          -> slope = -1/(8 gamma)  (shallower)
      So the LOW-NOISE INITIAL SLOPE is the discriminator.  gamma here is in units
      of 1/transit-time, i.e. the dimensionless lock-strength  a = gamma * tau_transit.
      A measured slope of -1/2 bounds a; a shallower slope detects a>0.

  (2) CONDITIONAL (only if a deviation is seen) -- the eraser-recovery test, where
      silver's clean spin-1/2 pointer earns its role:
      if gamma_flight>0 and noise has driven a fraction f into the antipodal pi-well,
      the UNSORTED fringe is V ~ |1-2f| (the two wells' fringes cancel), but SORTING
      atoms by their internal pointer (SG) RECOVERS each sub-fringe to ~exp(-sigma^2/8gamma).
      Standard decoherence: the which-path info is in the ENVIRONMENT, so sorting on
      the atom's own state recovers nothing (V_sorted ~ V_unsorted).
      V_sorted >> V_unsorted is the signature that the info is locked in the ATOM.

Counting statistics: a sinusoidal fringe estimated from N detected atoms has
visibility uncertainty  delta_V ~ sqrt(2/N).
"""

import numpy as np

h = 6.62607015e-34; kB = 1.380649e-23; amu = 1.66053907e-27
m_Ag = 107.8682 * amu


def slope_discriminator():
    print("=" * 74)
    print("(1) PRIMARY OBSERVABLE: initial slope of V vs injected noise sigma^2")
    print("=" * 74)
    print("    QM slope dV/dsigma^2|_0 = -0.500   (V = exp(-sigma^2/2))")
    print("    two-basin slope = -1/(8a),  a = gamma*tau_transit (dimensionless lock strength)\n")
    print("      a (lock strength)   slope -1/8a   deviation from QM   detectable?")
    for a in [0.1, 0.25, 0.5, 1.0, 2.0, 5.0]:
        slope = -1.0 / (8 * a)
        dev = abs(-0.5 - slope)
        # the plateau formula is the LARGE-a (confining) limit; for a<~0.25 the well
        # does not confine and V -> QM, so small-a "slopes" are not physical plateaus.
        regime = "plateau (confining)" if a >= 0.25 else "-> reverts to QM (no confinement)"
        print(f"      a={a:5.2f}            {slope:+.3f}        {dev:.3f}            {regime}")
    print("\n    => the attractor SHALLOWS the initial slope once a>~0.25 and adds a")
    print("       Kramers cliff at sigma^2~2a.  A clean -1/2 slope at low noise bounds a.")


def counting_requirements():
    print("\n" + "=" * 74)
    print("(2) HOW MANY ATOMS?  delta_V ~ sqrt(2/N) per visibility point")
    print("=" * 74)
    print("    To resolve a slope deviation Delta_s by measuring V at sigma^2=0 and =Delta")
    print("    (span Delta), need delta_s = 2/(Delta*sqrt(N)) < Delta_s  ->  N > (2/(Delta*Delta_s))^2.\n")
    print("    target slope-deviation Delta_s   (detects a up to)   N needed (span Delta=0.5)")
    Delta = 0.5
    for Ds in [0.375, 0.05, 0.01, 0.002]:
        # invert -0.5 - (-1/8a) = Ds  -> 1/8a = 0.5 - Ds -> a = 1/(8(0.5-Ds))
        a_det = 1.0 / (8 * (0.5 - Ds)) if Ds < 0.5 else np.inf
        N = (2.0 / (Delta * Ds))**2
        print(f"        Delta_s = {Ds:6.3f}              a >~ {a_det:5.2f}            N ~ {N:>10.0f}")
    print("\n    => STATISTICS ARE CHEAP (10^2-10^6 atoms).  The real limit is SYSTEMATICS:")
    print("       calibrating the injected noise sigma^2 and the baseline visibility V0.")
    print("       A ~1% visibility calibration bounds a down to ~0.25 (slope dev ~0.01).")


def gamma_flight_bound():
    print("\n" + "=" * 74)
    print("(3) WHAT LOCK RATE gamma_flight DOES THE BOUND CORRESPOND TO?")
    print("=" * 74)
    print("    a = gamma_flight * tau_transit.  Bounding a<~0.25 bounds gamma_flight<0.25/tau.\n")
    print("      platform / transit time tau        bound on gamma_flight (a<0.25)")
    cases = [
        ("Ag Talbot-Lau, ~20 mm @ 548 m/s", 35.7e-6),
        ("slow Ag / long baseline, ~0.5 m @ 100 m/s", 5.0e-3),
        ("fullerene Talbot-Lau, ~1 m @ 150 m/s", 6.7e-3),
        ("10 m atom fountain, ~1 s", 1.0),
    ]
    for name, tau in cases:
        bound = 0.25 / tau
        print(f"      {name:42s}  gamma_flight <~ {bound:8.1f} s^-1")
    print("\n    => existing SLOW matter-wave interferometers (fullerenes, fountains) already")
    print("       show clean exp(-sigma^2/2) blur, so an in-flight measurement-lock faster")
    print("       than ~kHz is ALREADY excluded.  Consistent with MCI's gamma_flight=0 claim.")
    print("       A dedicated low-noise SLOPE scan tightens this by orders of magnitude.")


def eraser_recovery():
    print("\n" + "=" * 74)
    print("(4) CONDITIONAL CONFIRMATION (if a deviation IS seen): eraser-recovery")
    print("    -- this is where silver's clean spin-1/2 pointer is REQUIRED.")
    print("=" * 74)
    print("    Suppose gamma_flight>0 and noise drove a fraction f into the pi-well.\n")
    print("      f (pi-well pop)   V_unsorted=|1-2f|   V_sorted(two-basin)   V_sorted(decoherence)")
    for f, s2, a in [(0.05, 0.5, 4.0), (0.20, 2.0, 4.0), (0.50, 4.0, 4.0)]:
        Vu = abs(1 - 2 * f)
        Vs_2b = np.exp(-s2 / (8 * a))     # each sorted sub-fringe ~ in-well plateau
        Vs_dec = Vu                       # decoherence: sorting recovers nothing
        print(f"        f={f:4.2f}              {Vu:.2f}                {Vs_2b:.2f}                  {Vs_dec:.2f}")
    print("\n    => TWO-BASIN: V_sorted >> V_unsorted (info locked in the atom's pointer,")
    print("       recoverable by SG -- eraser-like).  DECOHERENCE: V_sorted ~ V_unsorted")
    print("       (info gone to the environment).  This is the ONE place spin-1/2 silver")
    print("       does something a spinless interferometer cannot.")


def main():
    print("\nEXPERIMENT SPEC: bounding/detecting the in-flight measurement attractor")
    print("(the framework's sole falsifiable fringe-channel deviation from standard QM)\n")
    slope_discriminator()
    counting_requirements()
    gamma_flight_bound()
    eraser_recovery()
    print("\n" + "=" * 74)
    print("SUMMARY")
    print("=" * 74)
    print("  * Primary test needs NO spin and NO silver: a precision V-vs-noise SLOPE scan")
    print("    on ANY interferometer with a calibrated noise knob (fullerene thermal-photon")
    print("    rig is the ready-made platform).  Null = bound gamma_flight; deviation = new physics.")
    print("  * Silver's spin-1/2 earns a UNIQUE role ONLY in the conditional eraser-recovery")
    print("    follow-up, and ONLY if step (1) sees a deviation.")
    print("  * Neither test touches the BORN WEIGHTS (still the open problem) or the CHIRAL")
    print("    ORIGIN of the 2nd harmonic (that needs the mass-channel AB-visibility test).")


if __name__ == "__main__":
    main()
