# Prefix deletion-square restriction audit

Date: 2026-06-03

This generated audit compares the marked `Q_X(5)` point-pushing
generators with their expected `Q_X(3)` images after deleting two
stationary strands.  It is the first two-face surface behind the
Peiffer/secondary-class pressure test.

With source generator `alpha_{i,6}` and deleted stationary strands
`j<k`, the marked target is:

```text
identity,                         if i in {j,k},
alpha_{i-c,4}, where c=#({j,k}<i), otherwise.
```

The audit also checks that the two coordinate-deletion orders commute
on the source action.  Thus any mismatch is not a raw failure of the
semi-simplicial face identity; it is residual vertical monodromy left
when a pushed-around strand is forgotten.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source and target arities: `Q_X(5) -> Q_X(3)`;
- row count: `50`;
- total mismatch count: `1280`;
- deleted-generator mismatch count: `1280`;
- surviving generators all match: `True`;
- deletion orders all commute: `True`;
- all rows match: `False`;
- verifies first deletion-square surface: `True`.

Restriction rows:

- forget `(1, 2)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 2)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 2)`, source `alpha_{3,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 3)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 3)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 4)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(1, 5)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 3)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 3)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 4)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(2, 5)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(3, 4)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(3, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(3, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(4, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{3,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `(4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `64`, orders commute `True`, witness `(0, 0, 0, 0, 0, 0)` maps after double deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.

### degenerate_identity_deletion_square

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source and target arities: `Q_X(5) -> Q_X(3)`;
- row count: `50`;
- total mismatch count: `0`;
- deleted-generator mismatch count: `0`;
- surviving generators all match: `True`;
- deletion orders all commute: `True`;
- all rows match: `True`;
- verifies first deletion-square surface: `True`.

Restriction rows:

- forget `(1, 2)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{3,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 2)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 3)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{1,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{2,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(1, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{4,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 3)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{2,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{3,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(2, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 4)`, source `alpha_{5,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{3,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{4,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(3, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{1,6}`, target `alpha_{1,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{2,6}`, target `alpha_{2,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{3,6}`, target `alpha_{3,4}`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{4,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.
- forget `(4, 5)`, source `alpha_{5,6}`, target `identity`: mismatches `0`, orders commute `True`, witness `none`.

## Meaning

For the nondegenerate prefix witness, all `30` surviving-generator
rows match exactly.  The `20` rows where the source generator is one
of the two deleted strands each have `64` mismatches, for `1280`
total mismatches.  The two deletion orders still commute on every
row, so the visible defect is vertical rather than a failure of
coordinate face maps.

For the degenerate identity row, all `50` rows match.  This keeps
the pressure test pointed at actual point-forgetting monodromy, not
at nonunit prefix memory alone.

The result still is not a counterexample to finite rack domination.
It identifies the first two-face ledger that a positive proof must
explain by a finite operator-label Artin envelope.  The next
possible obstruction is a genuine deletion-cube/Peiffer coherence
class, where these two-face defects must be compatible under three
stationary deletions.
