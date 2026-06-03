# Affine F2 Full-Twist Audit

## Purpose

This generated audit stress-tests the central full-twist obstruction in
the translated affine four-point universe.  It is a finite-prefix
candidate-search audit, not an all-arity theorem.

The calculation uses affine block-map composition over `F_2`; it does
not enumerate all tuples in `(F_2^2)^n` when computing full-twist
orders.

## Results

- affine maps checked: `1048576`;
- invertible affine maps: `322560`;
- affine YBE tables: `481`;
- checked braid indices: `1 <= n <= 7`;
- maximum observed central full-twist order: `4`;
- order-cap misses: `0`;
- untagged affine rows: `24`.

Untagged full-twist profiles:

```text
1,2,1,2,1,2,1: 24
```

Thus every untagged affine `F_2^2` row in this finite universe has
central full-twist prefix orders

```text
1, 2, 1, 2, 1, 2, 1
```

for `n=1,...,7`.  These rows are already non-primitive in the
`proofs/affine_f2_audit.md` sense because they have proper mixed
retraction/coretraction families; this audit adds that they also do
not stress the central full-twist obstruction in the checked prefix.

## Consequence

The central full-twist route to outcome B must leave the four-point
translated affine `F_2` universe, or find behavior invisible in this
prefix.  In particular, the currently untagged affine rows do not
supply the needed unbounded orders of
`rho_X,n((sigma_1 ... sigma_{n-1})^n)`.
