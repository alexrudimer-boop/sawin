# Triangular K-left coordinate-unit routing

Date: 2026-05-31

This note refines the `coordinate_side_unit_not_triangular` line in
`proofs/triangular_k_left_missing_row_profile.md`.

It does not prove `[Resolution: A]` or construct `[Resolution: B]`.  It
removes one apparent ambiguity from System K: a no-triangular row whose
sections on one coordinate side are all units is not an independent hidden
rank-loss obstruction.

## Executable object

The helper

```text
missing_triangular_coordinate_unit_routing_audit(I)
```

groups every missing triangular profile with explanation

```text
coordinate_side_unit_not_triangular
```

by colour pair `(a,b)`.  For that pair it records:

```text
coordinate_unit_sides
left_explanation
right_explanation
left_unit_inputs
left_nonunit_inputs
right_unit_inputs
right_nonunit_inputs
status
```

The route status is one of:

```text
two_sided_unit_pair
mixed_unit_context
unrouted_coordinate_unit_row
```

The post-linear finite-system wrapper reports the K-relevant part as:

```text
missing_triangular_coordinate_unit_routes
missing_triangular_coordinate_unit_mixed_rows
missing_triangular_coordinate_unit_unrouted_rows
missing_triangular_locally_nondegenerate_closed_branch
```

## Lemma: coordinate-unit missing sides are routed

[Proved] Let `(a,b)` be a colour pair in a local interval, and suppose one
coordinate side is missing triangular only because every section on that side
is bijective.  Then exactly one of the following row-level alternatives holds.

1. Both coordinate sides are unit.  The row is a two-sided unit pair.  If this
   holds for every colour pair in a coloured YBE interval, then the whole
   interval is in the locally nondegenerate/guitar branch.
2. The opposite coordinate side has a nonunit section.  Since the original
   side has unit sections, the row is a mixed-unit context row.

Proof.  The coordinate-unit hypothesis says that at least one of the two
coordinate-section families is entirely bijective.  Inspect the opposite
coordinate family.  If it is also entirely bijective, the row is two-sided
unit.  If not, then the same row has both a unit section and a nonunit section,
which is precisely the mixed-unit context recorded by
`SectionUnitRowAudit.row_is_mixed_unit`.  There is no third case.  QED.

## Consequence for no-triangular rows

[Proved] The `coordinate_side_unit_not_triangular` explanation does not create
a new finite algebraic obstruction in System K.

If all colour pairs are two-sided unit and the interval satisfies coloured
YBE, the interval routes to the already recorded locally nondegenerate/guitar
branch (`proofs/left_nondegenerate_guitar_branch.md`, also stable under the
side-opposite operation).

If a coordinate-unit missing side is paired with any nonunit opposite side,
then it belongs to the mixed-unit context-recovery channel.  The nonunit
information is carried by the opposite triangular, partial-constant,
proper-kernel, injective-nonsurjective, or hidden-rank profile; it is not a
new one-sided unit obstruction.

Thus the no-triangular K-left ledger is narrowed again:

```text
proper_section_kernel_visible:
  existing readout/closure route;

injective_non_surjective_section:
  finite size/codomain ledger;

coordinate_side_unit_not_triangular:
  two-sided-unit branch if global, otherwise mixed-unit context;

partial_constant_hidden_rank_loss:
  mixed-unit context with constant nonunit sections;

nonconstant_hidden_rank_loss:
  incompatible with the post-linear rank-profile collapse unless another
  finite endpoint channel has failed.
```

## Remaining burden

[Open] This routing does not yet prove the uniform nonlinear endpoint theorem.
After coordinate-unit rows are removed as independent obstructions, the
remaining nonlinear work is still to prove that every mixed-unit/triangular
recovery endpoint has a fixed finite `V_beta` witness, or to upgrade a
specific failure into a normalized-law B sequence.
