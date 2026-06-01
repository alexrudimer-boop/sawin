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
coordinate_unit_route_fields_consistent
```

The route status is one of:

```text
two_sided_unit_pair
mixed_unit_context
unrouted_coordinate_unit_row
```

A row is route-field consistent only when the listed
`coordinate_unit_sides` are nonempty, are drawn from `{left,right}`, have the
matching `coordinate_side_unit_not_triangular` explanation, and are actually
unit sides in the supplied section data.  A row whose listed side is not
unit, or whose explanation does not match the listed coordinate-unit side, is
treated as `unrouted_coordinate_unit_row`.
The whole coordinate-unit routing ledger is also non-vacuous: with no
coordinate-unit rows it does not prove `all_coordinate_unit_rows_routed` or
`proves_coordinate_unit_routing_ledger`.

The post-linear finite-system wrapper reports the K-relevant part as:

```text
missing_triangular_coordinate_unit_routes
missing_triangular_coordinate_unit_mixed_rows
missing_triangular_coordinate_unit_unrouted_rows
missing_triangular_coordinate_unit_unclosed_two_sided_rows
missing_triangular_locally_nondegenerate_closed_branch
missing_triangular_coordinate_unit_routing_proved
```

## Lemma: coordinate-unit missing sides are routed

[Proved] Let `(a,b)` be a colour pair in a local interval, and suppose one
coordinate side is missing triangular only because every section on that side
is bijective.  Then exactly one of the following row-level alternatives holds.

1. Both coordinate sides are unit.  The row is a two-sided unit pair.  This
   closes only when the supplied global two-sided-unit audit proves the whole
   coloured interval is in the locally nondegenerate/guitar branch.  A
   two-sided unit row inside an otherwise nonunit interval is not silently
   closed by this row-level audit.
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
side-opposite operation).  If a coordinate-unit row is two-sided unit but the
global locally-nondegenerate branch is not proved, the row stays in active
System K and is recorded in
`missing_triangular_coordinate_unit_unclosed_two_sided_rows`.

If a coordinate-unit missing side is paired with any nonunit opposite side,
then it belongs to the mixed-unit context-recovery channel.  The nonunit
information is carried by the opposite triangular, partial-constant,
proper-kernel, injective-nonsurjective, or hidden-rank profile; it is not a
new one-sided unit obstruction and it is not a closed K row.  The
post-linear wrapper records such rows in
`mixed_context_routed_k_missing_latin_row_defects` and reports
`system_m_mixed_unit_context_endpoint` when no live K row remains.
This route is certificate-gated: if the supplied coordinate-unit routing audit
does not have the coloured-YBE premise, if the row does not list the actual
unit side, or if the listed side's explanation is not
`coordinate_side_unit_not_triangular`, the post-linear wrapper does not
remove the no-triangular row from active System K and does not create a
System M endpoint obligation from that supplied data.

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

[Proved] The mixed-unit endpoint burden is now an explicit supplied-certificate
finite system.  The helper

```text
mixed_unit_context_endpoint_witness_audit(...)
```

turns every mixed context route into endpoint keys

```text
(left_color, right_color, side)
```

and checks that each key has a product endpoint-longitude expression
certificate.  The post-linear wrapper accepts a matching
`mixed_unit_context_endpoint_witness`; if it proves the coordinate-unit routing
ledger and covers exactly the mixed context keys, the wrapper reports
`closed_by_mixed_unit_context_endpoint_witness` and no remaining System M
obligations.

The symmetric-detector alternative is recorded in
`proofs/mixed_unit_context_symmetric_endpoint_fork.md`.  Its helper

```text
mixed_unit_context_symmetric_endpoint_fork_audit(...)
```

checks that a faithful endpoint-family symmetric cutoff covers exactly the
mixed context keys from the same coordinate-unit routing ledger.  When
supplied to the post-linear wrapper, it closes System M as
`closed_by_mixed_unit_symmetric_endpoint_fork`; in a product endpoint row it
removes only M from `unclosed_routed_endpoint_systems`.

[Open] This supplied-certificate checker does not yet prove the uniform
nonlinear endpoint theorem.  The remaining nonlinear work is to construct
those mixed-unit endpoint factors for every routed row, or to upgrade a
specific missing/failing endpoint witness into a normalized-law B sequence.
