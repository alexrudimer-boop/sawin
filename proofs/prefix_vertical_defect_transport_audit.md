# Prefix vertical defect transport audit

Date: 2026-06-03

This generated audit checks the first face-transport law for the
vertical coefficient candidates extracted from diagonal
point-forgetting defects.  It fixes source point-pushing arity `5`
and asks whether an already-vertical defect remains compatible after
one additional stationary strand is deleted.

For a deletion face `F`, an extra stationary index `r` not in `F`,
and a source generator `i` already in `F`, it checks the square

```text
delete_r after defect_F  =  defect_{F union {r}} after delete_r
```

on all post-deletion target tuples.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source point-pushing arity: `5`;
- row count: `80`;
- all additional faces surjective: `True`;
- all defects transportable: `True`;
- all transports commute: `True`;
- total mismatch count: `0`;
- order-pair spectrum: `((2, 2),)`;
- verifies transport audit: `True`.

Transition summaries:

- `1->2`: rows `20`, mismatches `0`, orders `((2, 2),)`, identity pairs `0`, commuting rows `20`.
- `2->3`: rows `60`, mismatches `0`, orders `((2, 2),)`, identity pairs `0`, commuting rows `60`.

Transport rows:

- `1` -> `2`, face `(1,)`, extra `2`, target `(1, 2)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `3`, target `(1, 3)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `4`, target `(1, 4)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `5`, target `(1, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `1`, target `(1, 2)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `3`, target `(2, 3)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `4`, target `(2, 4)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `5`, target `(2, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `1`, target `(1, 3)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `2`, target `(2, 3)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `4`, target `(3, 4)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `5`, target `(3, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `1`, target `(1, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `2`, target `(2, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `3`, target `(3, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `5`, target `(4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `1`, target `(1, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `2`, target `(2, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `3`, target `(3, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `4`, target `(4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `3`, target `(1, 2, 3)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `4`, target `(1, 2, 4)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `5`, target `(1, 2, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `3`, target `(1, 2, 3)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `4`, target `(1, 2, 4)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `5`, target `(1, 2, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `2`, target `(1, 2, 3)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `4`, target `(1, 3, 4)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `5`, target `(1, 3, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `2`, target `(1, 2, 3)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `4`, target `(1, 3, 4)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `5`, target `(1, 3, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `2`, target `(1, 2, 4)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `3`, target `(1, 3, 4)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `5`, target `(1, 4, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `2`, target `(1, 2, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `3`, target `(1, 3, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `5`, target `(1, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `2`, target `(1, 2, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `3`, target `(1, 3, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `4`, target `(1, 4, 5)`, source `alpha_{1,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `2`, target `(1, 2, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `3`, target `(1, 3, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `4`, target `(1, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `1`, target `(1, 2, 3)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `4`, target `(2, 3, 4)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `5`, target `(2, 3, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `1`, target `(1, 2, 3)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `4`, target `(2, 3, 4)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `5`, target `(2, 3, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `1`, target `(1, 2, 4)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `3`, target `(2, 3, 4)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `5`, target `(2, 4, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `1`, target `(1, 2, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `3`, target `(2, 3, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `5`, target `(2, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `1`, target `(1, 2, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `3`, target `(2, 3, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `4`, target `(2, 4, 5)`, source `alpha_{2,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `1`, target `(1, 2, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `3`, target `(2, 3, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `4`, target `(2, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `1`, target `(1, 3, 4)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `2`, target `(2, 3, 4)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `5`, target `(3, 4, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `1`, target `(1, 3, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `2`, target `(2, 3, 4)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `5`, target `(3, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `1`, target `(1, 3, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `2`, target `(2, 3, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `4`, target `(3, 4, 5)`, source `alpha_{3,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `1`, target `(1, 3, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `2`, target `(2, 3, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `4`, target `(3, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `1`, target `(1, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `2`, target `(2, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `3`, target `(3, 4, 5)`, source `alpha_{4,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `1`, target `(1, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `2`, target `(2, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `3`, target `(3, 4, 5)`, source `alpha_{5,6}`: orders `(2, 2)`, commutes `True`, mismatches `0`, witness `none`.

### degenerate_identity_vertical_transport

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source point-pushing arity: `5`;
- row count: `80`;
- all additional faces surjective: `True`;
- all defects transportable: `True`;
- all transports commute: `True`;
- total mismatch count: `0`;
- order-pair spectrum: `((1, 1),)`;
- verifies transport audit: `True`.

Transition summaries:

- `1->2`: rows `20`, mismatches `0`, orders `((1, 1),)`, identity pairs `20`, commuting rows `20`.
- `2->3`: rows `60`, mismatches `0`, orders `((1, 1),)`, identity pairs `60`, commuting rows `60`.

Transport rows:

- `1` -> `2`, face `(1,)`, extra `2`, target `(1, 2)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `3`, target `(1, 3)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `4`, target `(1, 4)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(1,)`, extra `5`, target `(1, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `1`, target `(1, 2)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `3`, target `(2, 3)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `4`, target `(2, 4)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(2,)`, extra `5`, target `(2, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `1`, target `(1, 3)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `2`, target `(2, 3)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `4`, target `(3, 4)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(3,)`, extra `5`, target `(3, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `1`, target `(1, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `2`, target `(2, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `3`, target `(3, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(4,)`, extra `5`, target `(4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `1`, target `(1, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `2`, target `(2, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `3`, target `(3, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `1` -> `2`, face `(5,)`, extra `4`, target `(4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `3`, target `(1, 2, 3)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `4`, target `(1, 2, 4)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `5`, target `(1, 2, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `3`, target `(1, 2, 3)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `4`, target `(1, 2, 4)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 2)`, extra `5`, target `(1, 2, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `2`, target `(1, 2, 3)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `4`, target `(1, 3, 4)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `5`, target `(1, 3, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `2`, target `(1, 2, 3)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `4`, target `(1, 3, 4)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 3)`, extra `5`, target `(1, 3, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `2`, target `(1, 2, 4)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `3`, target `(1, 3, 4)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `5`, target `(1, 4, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `2`, target `(1, 2, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `3`, target `(1, 3, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 4)`, extra `5`, target `(1, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `2`, target `(1, 2, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `3`, target `(1, 3, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `4`, target `(1, 4, 5)`, source `alpha_{1,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `2`, target `(1, 2, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `3`, target `(1, 3, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(1, 5)`, extra `4`, target `(1, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `1`, target `(1, 2, 3)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `4`, target `(2, 3, 4)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `5`, target `(2, 3, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `1`, target `(1, 2, 3)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `4`, target `(2, 3, 4)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 3)`, extra `5`, target `(2, 3, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `1`, target `(1, 2, 4)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `3`, target `(2, 3, 4)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `5`, target `(2, 4, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `1`, target `(1, 2, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `3`, target `(2, 3, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 4)`, extra `5`, target `(2, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `1`, target `(1, 2, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `3`, target `(2, 3, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `4`, target `(2, 4, 5)`, source `alpha_{2,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `1`, target `(1, 2, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `3`, target `(2, 3, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(2, 5)`, extra `4`, target `(2, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `1`, target `(1, 3, 4)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `2`, target `(2, 3, 4)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `5`, target `(3, 4, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `1`, target `(1, 3, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `2`, target `(2, 3, 4)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 4)`, extra `5`, target `(3, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `1`, target `(1, 3, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `2`, target `(2, 3, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `4`, target `(3, 4, 5)`, source `alpha_{3,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `1`, target `(1, 3, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `2`, target `(2, 3, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(3, 5)`, extra `4`, target `(3, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `1`, target `(1, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `2`, target `(2, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `3`, target `(3, 4, 5)`, source `alpha_{4,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `1`, target `(1, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `2`, target `(2, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.
- `2` -> `3`, face `(4, 5)`, extra `3`, target `(3, 4, 5)`, source `alpha_{5,6}`: orders `(1, 1)`, commutes `True`, mismatches `0`, witness `none`.

## Meaning

For the nondegenerate prefix witness, every already-vertical
order-two defect commutes with deleting one further stationary
strand.  The vertical coefficient candidates therefore form a
face-compatible system at this first transport layer.

For the degenerate identity row, all transported defects are
identity permutations, and all transport squares commute.

This is still not a Peiffer/Postnikov obstruction.  It verifies
only the functorial transport of already-existing vertical
defects.  The next layer must compare two different vertical
defects around a deletion square and quotient by the section
change law.
