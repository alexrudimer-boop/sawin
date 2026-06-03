# Prefix point-pushing tiny corpus audit

Date: 2026-06-03

This generated audit exhaustively scans all bijective YBE whole
tables on two and three points.  It asks whether the first
point-pushing pressure surface

```text
Q_X(3) <= G_X(4),       Q_X(4) <= G_X(5)
```

already contains a left-degenerate solution with nonunit prefix
memory and nontrivial point-pushing image.

The scan is deliberately finite.  It does not search four-point
tables, quotient-fibre local intervals, or all possible finite
group-Hurwitz compressions.

## Corpus Rows

### Size 2

- bijective YBE solution count: `5`;
- left-degenerate count: `1`;
- left-degenerate with nonunit prefix count: `1`;
- left-degenerate nonunit rows with nontrivial surface: `0`;
- any-row nontrivial surface count: `2`;
- truncated surface count: `0`;
- no bad left-degenerate nonunit surface candidates: `True`.

Recorded left-degenerate nonunit rows:

- index `0`; tags `involutive, identity_table, affine_cyclic`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`

Tag profile counts:

- `involutive+identity_table+affine_cyclic`: `1`
- `involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`
- `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`
- `rack_type+involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`
- `rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`

### Size 3

- bijective YBE solution count: `73`;
- left-degenerate count: `7`;
- left-degenerate with nonunit prefix count: `7`;
- left-degenerate nonunit rows with nontrivial surface: `0`;
- any-row nontrivial surface count: `54`;
- truncated surface count: `12`;
- no bad left-degenerate nonunit surface candidates: `True`.

Recorded left-degenerate nonunit rows:

- index `0`; tags `involutive, identity_table, affine_cyclic`; nonunit prefixes `3`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `1`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `2`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `3`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `4`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `18`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`
- index `26`; tags `involutive`; nonunit prefixes `2`; `|Q_X(3)|=1`; `|Q_X(4)|=1`; truncated `False`

Tag profile counts:

- `involutive`: `6`
- `involutive+identity_table+affine_cyclic`: `1`
- `involutive+left_nondegenerate+right_nondegenerate+nondegenerate`: `6`
- `involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `5`
- `left_nondegenerate+right_nondegenerate+nondegenerate`: `24`
- `left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `11`
- `permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `7`
- `rack_type+involutive+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`
- `rack_type+left_nondegenerate+right_nondegenerate+nondegenerate`: `6`
- `rack_type+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `1`
- `rack_type+permutation_form+left_nondegenerate+right_nondegenerate+nondegenerate+affine_cyclic`: `5`

## Meaning

The first bad surface is absent from the exhaustive whole-table
corpus on two and three points.  In size `2`, the only
left-degenerate nonunit-prefix table is the identity table, and
its `Q_X(3)` and `Q_X(4)` images are trivial.  In size `3`, all
seven left-degenerate nonunit-prefix rows again have trivial
`Q_X(3)` and `Q_X(4)` images.

Thus a negative point-pushing route cannot start with a whole
size-2 or size-3 table.  A genuine obstruction must move to
larger whole tables or to quotient-fibre local intervals, and
must still show incompatibility with every fixed finite
group-Hurwitz base plus bounded-exponent vertical kernel.
