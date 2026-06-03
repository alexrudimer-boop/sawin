# Prefix point-pushing tiny corpus

Date: 2026-06-03

The point-pushing route now uses the first marked surface

```text
Q_X(3) <= G_X(4),       Q_X(4) <= G_X(5)
```

rather than a naive bounded-exponent invariant.  A negative example must be
left-degenerate enough to create nonunit prefix memory, but it also has to
make that memory visible in the point-pushing image.  The size-2 and size-3
whole-table corpus is small enough to check exhaustively.

## Audit Question

For every bijective YBE table `X` on `d` points, with `d=2` or `d=3`, compute

```text
prefix_point_pushing_surface_audit(X)
```

and record whether all three conditions hold:

- `X` is left-degenerate;
- the left-prefix transformation monoid has a nonunit element;
- one of `Q_X(3)` or `Q_X(4)` is nontrivial.

Such a row would be the first plausible whole-table candidate for a
group-Hurwitz compression obstruction.

## Result

The generated report

```text
proofs/prefix_point_pushing_tiny_corpus_audit.md
```

finds no such row.

For size `2`, there are `5` bijective YBE tables.  Exactly one is
left-degenerate with nonunit prefix memory: the identity table.  Its
`Q_X(3)` and `Q_X(4)` images are both trivial.

For size `3`, there are `73` bijective YBE tables.  Exactly seven are
left-degenerate with nonunit prefix memory.  All seven have trivial
`Q_X(3)` and `Q_X(4)` images.

## Consequence

The first whole-table obstruction, if it exists, is not present on two or
three points.  A negative point-pushing route must now search either:

- larger whole tables, starting at size `4`; or
- quotient-fibre local intervals whose induced finite YBE data is not one of
  the tiny whole-table rows.

This is still finite evidence, not a theorem.  It only removes the smallest
whole-table candidates from the route.  The remaining theorem-level question
is unchanged: decide whether every finite bijective YBE point-pushing tower
admits a fixed finite group-Hurwitz base with uniformly bounded-exponent
vertical kernel, or exhibit compatible tower data that no such base can
explain.
