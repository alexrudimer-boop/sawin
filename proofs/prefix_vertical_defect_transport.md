# Prefix vertical defect transport

Date: 2026-06-03

The vertical-defect transform audit extracts diagonal deletion defects as
finite permutations of post-deletion target tuple spaces.  This note records
the first transport check for those coefficient candidates.

Fix source point-pushing arity `5`, so the source braid index is `6`.  Let
`F` be a stationary deletion face and let `i in F`, so that the generator
`alpha_{i,6}` is already vertical after deleting `F`.  For an additional
stationary index `r notin F`, compare the two maps on the target tuple space
after deleting `F`:

```text
delete_r after defect_F
defect_{F union {r}} after delete_r.
```

The generated audit is:

```text
proofs/prefix_vertical_defect_transport_audit.md
```

It checks all `80` first transport rows:

```text
level 1 -> level 2:  20 rows,
level 2 -> level 3:  60 rows.
```

For the nondegenerate two-point prefix witness, every row commutes.  The
order-pair spectrum is `((2, 2),)`, so all already-vertical order-two defects
remain compatible after one additional stationary deletion.  For the
degenerate identity row, every row also commutes, with order-pair spectrum
`((1, 1),)`.

Thus the toy prefix coefficient candidates are not just finite permutations:
they are face-compatible under this first additional-deletion transport.  This
is still weaker than the required secondary obstruction.  The next layer must
compare distinct vertical defects around a deletion square, compute the
Peiffer boundary, and quotient by section changes and pullbacks from a fixed
finite operator-label Hurwitz base.
