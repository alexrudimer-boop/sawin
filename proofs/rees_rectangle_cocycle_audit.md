# Rees rectangle cocycle audit

Date: 2026-06-03

This generated audit records the finite sandwich-matrix convention
used by `proofs/rees_rectangle_cocycle_flatness_target.md`.
For a Rees matrix component `M[G; I, Lambda; P]`, rows are
`Lambda`, columns are `I`, and the rectangle cocycle is

```text
omega(lambda, mu; i, j)
  = p[lambda,i] p[mu,i]^{-1} p[mu,j] p[lambda,j]^{-1}.
```

The base-gauge flatness check is the row-column factorization

```text
p[lambda,i]
  = p[lambda,i0] p[lambda0,i0]^{-1} p[lambda0,i].
```

The audit is not a YBE realization claim.  It only fixes the exact
finite obstruction that a YBE-specific flatness lemma must kill, or
that an obstruction construction must realize inside actual local
bijective YBE rows.

## Rows

### row_column_flat_C3_2x3

- group order: `3`;
- rows: `2`; columns: `3`;
- rectangle count: `36`;
- rectangle failure count: `0`;
- coboundary failure count: `0`;
- rectangle cocycles are trivial: `True`;
- sandwich is row-column coboundary: `True`;
- flatness matches coboundary: `True`;
- is flat: `True`;

### nonflat_C2_2x2

- group order: `2`;
- rows: `2`; columns: `2`;
- rectangle count: `16`;
- rectangle failure count: `4`;
- coboundary failure count: `1`;
- rectangle cocycles are trivial: `False`;
- sandwich is row-column coboundary: `False`;
- flatness matches coboundary: `True`;
- is flat: `False`;
- distinguished `omega`: `1`;
- first rectangle failure:
  `(lambda0, lambda1; i0, i1) -> 1`;
- first coboundary failure:
  `(lambda1, i1): actual 1, expected 0`;

## Consequence

The `C2` square is the smallest algebraic rectangle obstruction:
three sandwich entries are the identity and the fourth is the
nonidentity element.  A positive semigroup-corridor proof must
show that actual Artin/YBE corridors never traverse such a
nonflat Rees rectangle except as a coboundary.  A negative route
must realize this exact square, or a larger analogue, in a finite
bijective YBE local quotient-fibre interval.
