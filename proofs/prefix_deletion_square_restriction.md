# Prefix deletion-square restriction surface

Date: 2026-06-03

The single point-forgetting surface

```text
Q_X(4) <= G_X(5)   --->   Q_X(3) <= G_X(4)
```

showed that deleting the stationary strand encircled by a point-pushing
generator can leave vertical monodromy on tuple labels.  The next
semi-simplicial pressure test is the first two-face surface

```text
Q_X(5) <= G_X(6)   --->   Q_X(3) <= G_X(4),
```

where two stationary strands are deleted.

Use the standard generators `alpha_{i,n+1}` of the point-pushing kernel.
For source generator `alpha_{i,6}` and deleted stationary strands `j<k`,
the abstract marked target is

```text
identity,                         if i in {j,k},
alpha_{i-c,4}, where c=#({j,k}<i), otherwise.
```

The generated report

```text
proofs/prefix_deletion_square_restriction_audit.md
```

checks all `50` rows: ten deleted pairs and five source generators.  It also
checks that the two coordinate-deletion orders commute on the source tuple
action.  This separates ordinary semi-simplicial face compatibility from the
vertical defect left by a forgotten point-pushing strand.

## Audit outcome

For the nondegenerate two-point prefix witness:

- all `30` surviving-generator rows match the marked target exactly;
- all `20` rows where the source generator is one of the two deleted strands
  have `64` mismatches;
- the total mismatch count is `1280`;
- the two deletion orders commute in every row.

For the degenerate identity row, all `50` rows match.

Thus the two-face surface does not give an obstruction by itself.  It records
that the first square layer is still ordinary face-compatible while carrying
vertical monodromy exactly on deleted-generator rows.  A positive
finite-rack-domination proof must absorb these rows into one finite
operator-label Artin-envelope tower with bounded vertical exponent.

## Next obstruction

The next theoretical pressure point is not another raw deletion-order check.
It is a deletion-cube/Peiffer coherence class: after three stationary
deletions, the two-face defects must themselves be compatible under the three
ways of taking square boundaries.  A strict crossed-module envelope would
force the resulting secondary class to vanish; a weak finite 2-group envelope
would have to make all such classes pull back from one fixed finite Postnikov
class.

That is the next finite arity to audit if this route is pursued further.
