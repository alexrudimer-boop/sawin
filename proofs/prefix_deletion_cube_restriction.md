# Prefix deletion-cube restriction surface

Date: 2026-06-03

The deletion-square surface

```text
Q_X(5) <= G_X(6)   --->   Q_X(3) <= G_X(4)
```

records the first two-face point-forgetting ledger.  The next direct cube
ledger uses the same source arity and deletes three stationary strands:

```text
Q_X(5) <= G_X(6)   --->   Q_X(2) <= G_X(3).
```

Use the standard generators `alpha_{i,n+1}` of the point-pushing kernel.
For source generator `alpha_{i,6}` and deleted stationary strands `j<k<l`,
the abstract marked target is

```text
identity,                           if i in {j,k,l},
alpha_{i-c,3}, where c=#({j,k,l}<i), otherwise.
```

The generated report

```text
proofs/prefix_deletion_cube_restriction_audit.md
```

checks all `50` rows: ten deleted triples and five source generators.  For
each row it checks all six orders of deleting the three stationary
coordinates, so a mismatch cannot be blamed on ordinary coordinate face maps.

## Audit outcome

For the nondegenerate two-point prefix witness:

- all `20` surviving-generator rows match the marked target exactly;
- all `30` rows where the source generator is one of the three deleted
  strands have `64` mismatches;
- the total mismatch count is `1920`;
- all six deletion orders commute in every row.

For the degenerate identity row, all `50` rows match.

Thus the direct cube ledger still has strict coordinate-face compatibility
and the same vertical monodromy pattern: defects occur exactly when a
pushed-around stationary strand is forgotten.  This is not yet a
gauge-invariant Peiffer or Postnikov obstruction.

## Next obstruction

The next step is to stop comparing raw deleted tuple actions and instead
extract the secondary class built from the square-defect ledgers.  A strict
crossed-module envelope would force that Peiffer boundary to vanish; a weak
finite `2`-group envelope would have to realize every such secondary class as
a pullback of one fixed finite Postnikov class.

An actual finite-rack-domination obstruction would therefore require a local
interval whose base deletion cube is trivial but whose transported
square-defect boundary is nontrivial in a gauge-invariant vertical
coefficient group.
