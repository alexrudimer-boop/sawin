# Prefix vertical Peiffer cube transport

Date: 2026-06-03

The vertical Peiffer square audit computes pair-face commutators of diagonal
vertical deletion defects.  This note records the first cubical transport
check for those square-boundary values.

Fix source point-pushing arity `5`.  For a deleted stationary triple `T` and a
pair face `F subset T`, compare the pair-face Peiffer boundary transported
through the remaining deletion with the direct triple-face Peiffer boundary:

```text
delete_{T-F} after Peiffer_F
=
Peiffer_T(F) after delete_{T-F}.
```

The generated audit is:

```text
proofs/prefix_vertical_peiffer_cube_transport_audit.md
```

It checks all `30` pair-in-triple rows: ten triples, each with three pair
faces.  For the nondegenerate two-point prefix witness, all `30` rows commute.
The pair Peiffer boundaries and direct triple-face Peiffer boundaries are all
identity, so the Peiffer order-pair spectrum is `((1, 1),)`, with mismatch
count `0`.

For the degenerate identity row, all `30` rows commute for the trivial
identity-defect reason.

The external theoretical pressure check frames the next invariant as a
normalized deletion `2`-cocycle with coefficients in vertical fibre-bisection
groups, modulo section-change gauge and pullback from a fixed finite
operator-label Hurwitz base.  This cube-transport audit verifies only the
first cubical coherence identity for the current prefix surface; it does not
yet compute the gauge quotient or the fixed-base pullback obstruction.
