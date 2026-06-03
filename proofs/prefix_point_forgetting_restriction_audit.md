# Prefix point-forgetting restriction audit

Date: 2026-06-03

This generated audit compares the marked `Q_X(4)` point-pushing
generators with their expected `Q_X(3)` images after deleting one
stationary strand.  With the standard generators
`alpha_{i,5}`, deleting stationary strand `j` should send the
marked generator to:

```text
identity,             if i=j,
alpha_{i,4},          if i<j,
alpha_{i-1,4},        if i>j.
```

When the tuple action does not match that expected marked action,
the difference is exactly the first visible vertical cocycle data
that a finite Artin-envelope tower must absorb.

## Rows

### nondegenerate_prefix_witness

- element count: `2`;
- left-prefix monoid size: `2`;
- nonunit prefix count: `0`;
- source and target arities: `Q_X(4) -> Q_X(3)`;
- row count: `16`;
- total mismatch count: `128`;
- diagonal mismatch count: `128`;
- off-diagonal all match: `True`;
- all rows match: `False`;
- verifies first restriction surface: `True`.

Restriction rows:

- forget `1`, source `alpha_{1,5}`, target `identity`: mismatches `32`, witness `(0, 0, 0, 0, 0)` maps after deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `1`, source `alpha_{2,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `1`, source `alpha_{3,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `1`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{2,5}`, target `identity`: mismatches `32`, witness `(0, 0, 0, 0, 0)` maps after deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `2`, source `alpha_{3,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{2,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{3,5}`, target `identity`: mismatches `32`, witness `(0, 0, 0, 0, 0)` maps after deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.
- forget `3`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{2,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{3,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{4,5}`, target `identity`: mismatches `32`, witness `(0, 0, 0, 0, 0)` maps after deletion to `(0, 0, 0, 1)`, expected `(0, 0, 0, 0)`.

### degenerate_identity_restriction_surface

- element count: `2`;
- left-prefix monoid size: `3`;
- nonunit prefix count: `2`;
- source and target arities: `Q_X(4) -> Q_X(3)`;
- row count: `16`;
- total mismatch count: `0`;
- diagonal mismatch count: `0`;
- off-diagonal all match: `True`;
- all rows match: `True`;
- verifies first restriction surface: `True`.

Restriction rows:

- forget `1`, source `alpha_{1,5}`, target `identity`: mismatches `0`, witness `none`.
- forget `1`, source `alpha_{2,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `1`, source `alpha_{3,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `1`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{2,5}`, target `identity`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{3,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `2`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{2,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{3,5}`, target `identity`: mismatches `0`, witness `none`.
- forget `3`, source `alpha_{4,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{1,5}`, target `alpha_{1,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{2,5}`, target `alpha_{2,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{3,5}`, target `alpha_{3,4}`: mismatches `0`, witness `none`.
- forget `4`, source `alpha_{4,5}`, target `identity`: mismatches `0`, witness `none`.

## Meaning

The nondegenerate witness has perfect off-diagonal restriction
compatibility, but the four diagonal rows each have `32`
mismatches.  This is the first concrete vertical point-forgetting
cocycle: after deleting the stationary strand that was looped
around, the abstract point-pushing generator forgets to the
identity, but the tuple labels retain monodromy.

The degenerate identity row has no mismatch, even though its
left-prefix monoid has nonunit memory.  Thus the restriction
surface separates two issues: nonunit prefix memory and actual
vertical point-forgetting monodromy.

A positive finite-rack-domination proof must show that these
diagonal vertical rows are controlled by one fixed finite
operator-label base with bounded vertical exponent.  A negative
proof must find a local interval or larger table where the same
restriction cocycles cannot be made compatible through the tower.
