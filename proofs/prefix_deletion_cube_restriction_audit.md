# Prefix deletion-cube restriction audit

Date: 2026-06-03

This generated audit compares the marked `Q_X(5)` point-pushing
generators with their expected `Q_X(2)` images after deleting three
stationary strands.  It is the first three-face ledger behind the
deletion-cube/Peiffer pressure test.

With source generator `alpha_{i,6}` and deleted stationary strands
`j<k<l`, the marked target is:

```text
identity,                           if i in {j,k,l},
alpha_{i-c,3}, where c=#({j,k,l}<i), otherwise.
```

For each row the audit compares all six coordinate-deletion orders
on the source tuple action.  Thus any mismatch recorded here is not a
literal failure of the semi-simplicial face maps; it is residual
vertical monodromy left when a pushed-around strand is forgotten.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source and target arities: `Q_X(5) -> Q_X(2)`;
- row count: `50`;
- total mismatch count: `1920`;
- deleted-generator mismatch count: `1920`;
- surviving generators all match: `True`;
- deletion orders all commute: `True`;
- all rows match: `False`;
- verifies first deletion-cube surface: `True`.

Restriction rows:

- forget `(1, 2, 3)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 3)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 3)`, source `alpha_{4,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 3)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 4)`, source `alpha_{3,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 2, 5)`, source `alpha_{3,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 4)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 5)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 3, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 4, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 4, 5)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{3,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(1, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 4)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 3, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 4, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 4, 5)`, source `alpha_{3,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(2, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(3, 4, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{2,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(3, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.
- forget `(3, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, deletion orders `6`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after triple deletion to `(0, 0, 1)`, expected `(0, 0, 0)`.

### degenerate_identity_deletion_cube

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source and target arities: `Q_X(5) -> Q_X(2)`;
- row count: `50`;
- total mismatch count: `0`;
- deleted-generator mismatch count: `0`;
- surviving generators all match: `True`;
- deletion orders all commute: `True`;
- all rows match: `True`;
- verifies first deletion-cube surface: `True`.

Restriction rows:

- forget `(1, 2, 3)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 3)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 3)`, source `alpha_{4,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 3)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{3,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{3,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 2, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{2,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{3,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(1, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 4)`, source `alpha_{5,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{4,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{3,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(2, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{1,6}`, target `alpha_{1,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{2,6}`, target `alpha_{2,3}`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.
- forget `(3, 4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, deletion orders `6`, orders commute `True`, witness `none`.

## Meaning

For the nondegenerate prefix witness, all `20` surviving-generator
rows match exactly.  The `30` rows where the source generator is one
of the three deleted strands each have `64` mismatches, for `1920`
total mismatches.  All six deletion orders commute on every row.

For the degenerate identity row, all `50` rows match.  This keeps
the pressure test focused on actual point-forgetting monodromy.

This audit is a cube ledger, not a full nonabelian secondary-class
calculation.  It shows that the direct cube faces remain ordinary
face-compatible while the vertical monodromy persists exactly on
deleted-generator rows.  A genuine obstruction would have to turn
the square-defect ledgers into a gauge-invariant Peiffer or
Postnikov class and show that class is not pulled back from one
fixed finite operator-label base.
