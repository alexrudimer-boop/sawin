# Linear F3 Nonsubdirect Rows: Quotient-Factor Closure

Date: 2026-06-08

This note records the closure of the `80` non-subdirect rows in the six-point
linear skew-over-flip degenerate non-involutive family.

The generated audit is

```text
proofs/linear_f3_nonsubdirect_quotient_factor_closure_audit.md
```

## Certificate

For each non-subdirect row `X`, enumerate its nontrivial proper braided
congruences.  Keep only quotient factors already known to be finite-rack
dominated:

```text
rack-form quotients,
nondegenerate quotients,
involutive quotients.
```

The audit checks that these known dominated proper quotients are enough:

```text
1. their common refinement is the equality congruence on X;
2. the active-factor finite certificate holds.
```

Thus the product of these proper quotient actions already separates the
`X`-action in every arity.

## Kernel Argument

Let

```text
pi_j:X -> Z_j
```

be the selected known dominated quotient factors.  For each `j`, choose a
finite rack `Y_j` dominating `Z_j`.  The active-factor certificate gives

```text
ker rho^{prod_j Z_j}_n <= ker rho^X_n
```

for every `n`.  Since each `Y_j` dominates `Z_j`,

```text
ker rho^{prod_j Y_j}_n <= ker rho^{prod_j Z_j}_n.
```

Therefore

```text
ker rho^{prod_j Y_j}_n <= ker rho^X_n
```

for every `n`, and `X` is finite-rack dominated.

## Consequence

All `80` non-subdirect degenerate non-involutive rows in the six-point linear
`F_3` skew-over-flip family are finite-rack dominated by products of already
known dominated proper quotient factors.
