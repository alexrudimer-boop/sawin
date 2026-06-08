# Linear F3 Separating Rows: Relative Quotient Closure

Date: 2026-06-08

This note records the all-arity closure for the `32` monolith
`J`-separating subdirect rows in the six-point linear skew-over-flip family

```text
X={0,1} x F_3.
```

The generated audit is

```text
proofs/linear_f3_separating_quotient_closure_audit.md
```

It verifies the finite hypotheses of the relative contextual extension
theorem for all `32` rows.

## Setup

Let `mu` be the monolith of a separating row.  The audit checks that:

```text
|X/mu| = 4,
```

and the quotient `Z=X/mu` is involutive.  By the known involutive theorem, `Z`
is dominated by a finite rack.

The audit also checks that the two-sided contextual quotient `P_X` has the
identity-extension rack completion preserving forced products:

```text
identity_extension_total_permutations = True,
identity_extension_conjugacy_covariance = True,
contextual_conflict_count = 0.
```

Thus the contextual readout

```text
J_n:X^n -> P_X^n
```

is braid-equivariant through the finite contextual rack.

Finally, the finite relative contextual separation graph verifies all-arity
injectivity of

```text
(pi_mu^n,J_n):X^n -> (X/mu)^n x P_X^n.
```

Equivalently, if two words have the same monolith quotient coordinates and
the same contextual readout, then they are equal.

## Relative Kernel Argument

Let `Y_Z` be a finite rack dominating the involutive quotient `Z=X/mu`, and
let `Y_ctx` be the contextual rack completion of `P_X`.

Take

```text
beta in ker rho^{Y_Z x Y_ctx x T_2}_n.
```

The `T_2` factor forces `beta` to be pure.  For any `x in X^n`, put

```text
x' = rho^X_n(beta)(x).
```

Since `Y_Z` dominates `Z`,

```text
pi_mu^n(x') = pi_mu^n(x).
```

Since `beta` is also in the contextual rack kernel and `J_n` is
braid-equivariant,

```text
J_n(x') = J_n(x).
```

By the audited all-arity injectivity of `(pi_mu^n,J_n)`, this implies

```text
x'=x.
```

Since `x` was arbitrary,

```text
ker rho^{Y_Z x Y_ctx x T_2}_n <= ker rho^X_n
```

for every `n`.  Therefore each of the `32` separating rows is finite-rack
dominated.

## Consequence

Together with

```text
proofs/linear_f3_gap_corrected_invariant_closure.md
```

which closes the `32` formal monolith-collision rows, this closes all `64`
subdirectly irreducible six-point linear `F_3` skew-over-flip degenerate
non-involutive rows.
