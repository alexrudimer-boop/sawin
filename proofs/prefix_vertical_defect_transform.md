# Prefix vertical defect transform extraction

Date: 2026-06-03

The single, square, and cube point-forgetting ledgers record raw mismatch
counts on deleted-generator rows.  This note records the next finite datum:
whether those raw defects descend to transformations of the post-deletion
target tuple space.

For a deleted-generator row, fix the source arity, the stationary strands to
forget, and a point-pushing generator whose index is among the forgotten
strands.  Group all source tuples by the tuple left after deleting the
stationary strands.  If every group has a single post-deletion output after
the source generator acts, the defect descends to a map on the target tuple
space.  If that map is bijective, it is a finite vertical coefficient
candidate for the corresponding point-forgetting face.

The generated audit is:

```text
proofs/prefix_vertical_defect_transform_audit.md
```

It extracts all deleted-generator rows from the first three ledgers:

```text
Q_X(4) <= G_X(5)  --->  Q_X(3) <= G_X(4),
Q_X(5) <= G_X(6)  --->  Q_X(3) <= G_X(4),
Q_X(5) <= G_X(6)  --->  Q_X(2) <= G_X(3).
```

For the nondegenerate two-point prefix witness, all `54` defects are
well-defined on post-deletion target tuples, all are permutations, and the
order spectrum is `(2,)`.  At each deletion level there is one distinct
nontrivial defect permutation.

For the degenerate identity row, all `54` defects are identity permutations,
with order spectrum `(1,)`.

Thus the toy prefix surface does have concrete finite vertical coefficient
groups on the deleted-generator faces.  This is not yet a gauge-invariant
Peiffer/Postnikov class.  The next genuine obstruction must add face
transports, compute the square-boundary/Peiffer expression over these
coefficient groups, and separate section-change coboundaries from a real
obstruction to one fixed finite operator-label Artin envelope.

## Theoretical checkpoint

The latest external theoretical pressure check framed the invariant not as a
raw square defect but as a relative cubical Peiffer class.  In that language,
one first forms a primary square class with coefficients in the cokernel of
the crossed-module boundary measuring face defects, modulo section changes
and pullbacks from the proposed fixed finite operator-label base.  When that
primary class vanishes, the next obstruction is a secondary cube class with
coefficients in the kernel of the same boundary, again modulo pullback from
the fixed base.

This audit supplies only the coefficient-candidate part of that package: the
finite vertical transformations carried by the diagonal deletion rows.  The
next audit should therefore add the missing structural data explicitly:
face transports between these coefficient groups, the Peiffer boundary map,
the section-change law, and the smallest arity at which the resulting class
can be distinguished from a coboundary.
