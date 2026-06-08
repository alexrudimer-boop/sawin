# Theoretical Review: Linear F3 Skew-Over-Flip Orbit Audit

Date: 2026-06-07.

## Verdict

This is verified finite evidence for the orbit-separation part of the positive
route.  It is not an all-arity theorem and does not prove A.

The result was locally audited by:

```text
tools/run_linear_f3_skew_flip_orbit_audit.py
proofs/linear_f3_skew_flip_orbit_audit.json
proofs/linear_f3_skew_flip_orbit_audit.md
```

## Scope

The audit checks contextual readout orbit-injectivity for the 144 degenerate
non-involutive rows in the six-point linear skew-over-flip family

```text
X={0,1} x F_3.
```

It uses the two-sided contextual quotient `P_X` and the readout `J_n:X^n->P_X^n`.

## Result

The audit verifies:

```text
degenerate non-involutive rows: 144
all rows checked through arity: 5
representative contextual types checked through arity: 6
representative contextual type count: 16
orbit-injectivity failure count: 0
all claimed checks passed: true
```

Thus, in this finite range, no two distinct points in the same braid orbit have
the same contextual readout.

## Consequence

Together with the finite completion audit for the same family, this gives
positive evidence for both current obligations:

```text
active lift/completion exists;
contextual readout is orbit-injective.
```

The remaining proof obligation is the all-arity orbit-injectivity theorem, or a
finite `X` where orbit-injectivity fails and the failure yields actual
Brunnian detector-kernel witnesses.
