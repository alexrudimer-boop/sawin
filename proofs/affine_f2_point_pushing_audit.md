# Affine F2 Point-Pushing Audit

## Purpose

This generated audit stress-tests the point-pushing generator-order
route in the translated affine four-point universe.  It complements
`proofs/affine_f2_full_twist_audit.md`: the central full twist did not
grow in the untagged affine rows, so here we check the standard pure
point-pushing generators `A_{i,q}`.

This is finite-prefix evidence only, not an all-arity theorem.

## Results

- affine maps checked: `1048576`;
- invertible affine maps: `322560`;
- affine YBE tables: `481`;
- checked point-pushing braid indices: `2 <= q <= 5`;
- maximum observed point-pushing generator order: `4`;
- untagged affine rows: `24`.

Untagged point-pushing generator-order profiles:

```text
2,2,2,2: 24
```

Thus every untagged affine `F_2^2` row in this finite universe has
standard point-pushing generator orders

```text
2, 2, 2, 2
```

for `q=2,...,5`.  The recorded untagged examples also have
point-pushing subgroup sizes `2,4,8,16` and exponent `2` through
`q=5` under the audit cap.

## Consequence

The elementary pure-generator order route to a normalized-law
counterexample must leave the checked translated affine `F_2^2`
universe, or use more subtle relations inside the moving
point-pushing subgroup rather than unbounded orders of the standard
generators.
