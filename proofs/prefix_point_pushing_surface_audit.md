# Prefix point-pushing surface audit

Date: 2026-06-03

This generated audit computes the first concrete point-pushing
surfaces `Q_X(3)` and `Q_X(4)` for the prefix-edge transducer
route.  It uses the standard pure generators
`alpha_{i,n+1}=A_{i,n+1}` and checks that the prefix-path encoding
sees the same marked action as the original tuple action.

The audit is still finite-prefix evidence.  It is not a proof that
every arity admits a fixed group-Hurwitz compression, and it is not
a normalized-law counterexample.  It records the first concrete
surface where such a compression has to be tested.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- checked arities: `(3, 4)`;
- all rows untruncated: `True`;
- verifies prefix point-pushing surface: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- prefix path count: `16`;
- prefix encoding injective: `True`;
- generator count: `3`;
- generator braid words: `((3, 2, 1, 1, -2, -3), (3, 2, 2, -3), (3, 3))`;
- generator orders: `(2, 2, 2)`;
- point-pushing group size: `8`;
- point-pushing group exponent: `2`;
- prefix action matches tuple action: `True`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- prefix path count: `32`;
- prefix encoding injective: `True`;
- generator count: `4`;
- generator braid words: `((4, 3, 2, 1, 1, -2, -3, -4), (4, 3, 2, 2, -3, -4), (4, 3, 3, -4), (4, 4))`;
- generator orders: `(2, 2, 2, 2)`;
- point-pushing group size: `16`;
- point-pushing group exponent: `2`;
- prefix action matches tuple action: `True`;
- truncated: `False`.

### degenerate_identity_prefix_surface

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- checked arities: `(3, 4)`;
- all rows untruncated: `True`;
- verifies prefix point-pushing surface: `True`.

#### Q_X(3) in B_4

- tuple count: `16`;
- prefix path count: `16`;
- prefix encoding injective: `True`;
- generator count: `3`;
- generator braid words: `((3, 2, 1, 1, -2, -3), (3, 2, 2, -3), (3, 3))`;
- generator orders: `(1, 1, 1)`;
- point-pushing group size: `1`;
- point-pushing group exponent: `1`;
- prefix action matches tuple action: `True`;
- truncated: `False`.

#### Q_X(4) in B_5

- tuple count: `32`;
- prefix path count: `32`;
- prefix encoding injective: `True`;
- generator count: `4`;
- generator braid words: `((4, 3, 2, 1, 1, -2, -3, -4), (4, 3, 2, 2, -3, -4), (4, 3, 3, -4), (4, 4))`;
- generator orders: `(1, 1, 1, 1)`;
- point-pushing group size: `1`;
- point-pushing group exponent: `1`;
- prefix action matches tuple action: `True`;
- truncated: `False`.

## Meaning

The rows make the `Q_X(3), Q_X(4)` pressure surface explicit.
For the nondegenerate two-point witness, the point-pushing
groups have sizes `8` and `16` with exponent `2`; for the
degenerate identity row, the point-pushing groups are trivial
even though the left-prefix monoid contains nonunit memory.
A genuine obstruction must therefore use a less trivial
degenerate table and show that every fixed group-Hurwitz
compression leaves incompatible or unbounded vertical data
on this surface and throughout the tower.
