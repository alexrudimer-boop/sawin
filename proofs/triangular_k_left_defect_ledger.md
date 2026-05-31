# Triangular K-left defect ledger

Date: 2026-05-31

This note refines the System K residue in
`proofs/post_linear_remaining_finite_system.md`.  It does not prove
`[Resolution: A]` or construct `[Resolution: B]`.  It replaces the phrase
"missing left Latin completion" by an explicit finite row ledger.

## Executable object

For a local interval `I`, the refinement audit now exposes:

```text
left_triangular_row_pairs
right_triangular_row_pairs
missing_left_latin_row_defects
missing_right_latin_row_defects
active_missing_left_latin_row_defects
active_missing_right_latin_row_defects
```

The defect rows have the form:

```text
((a,b), reason)
```

where `(a,b)` is a quotient-colour pair.  The left-handed reasons are:

```text
no_left_triangular_row
left_row_product_collapse
left_constant_map_not_bijective
left_constant_map_not_surjective
left_constant_map_proper_kernel
left_constant_map_universal_kernel
left_companion_sections_not_bijective
left_companion_sections_proper_kernel
left_companion_sections_constant
left_companion_sections_injective_non_surjective
left_opposite_sections_not_bijective
left_opposite_proper_kernel_visible
left_opposite_injective_non_surjective
left_opposite_hidden_nonunit_unclassified
side_dual_right_latin_available
side_dual_right_triangular_nonlatin
no_side_dual_right_latin_replacement
```

There is a symmetric right-handed list with `left` and `right` interchanged.

## Meaning of the row reasons

For a left triangular row

```text
T_{a,b}(x,y) = (alpha_{a,b}(x), beta_{a,b,x}(y)),
```

the row is left Latin-unit triangular exactly when:

```text
alpha_{a,b}: A_a -> A_{a*b} is bijective;
each beta_{a,b,x}: A_b -> A_a is bijective;
each opposite column x -> beta_{a,b,x}(y) is bijective.
```

The ledger records the first finite place where this can fail:

```text
no_left_triangular_row
```

means that the first output is not independent of `y`, so the triangular
row does not exist.

```text
left_constant_map_not_bijective
```

means that `alpha_{a,b}` is not a bijection.

The subreasons

```text
left_constant_map_not_surjective
left_constant_map_proper_kernel
left_constant_map_universal_kernel
```

separate a size/codomain failure from a proper or universal kernel of
`alpha_{a,b}`.  The universal-kernel label is kernel-local: it is used only
when the fibre of `alpha_{a,b}` is nontrivial and all inputs collapse to one
output.  A one-point domain that merely misses part of the codomain is only a
codomain failure, not a universal kernel edge.

```text
left_companion_sections_not_bijective
```

means that some `beta_{a,b,x}` is not a bijection.

The subreasons

```text
left_companion_sections_proper_kernel
left_companion_sections_constant
left_companion_sections_injective_non_surjective
```

record whether the companion failure loses information by a proper kernel, is
rank-one with a nontrivial collapsed fibre, or is injective but misses part of
the companion codomain.  Thus a one-point companion image is a block-image
case, not a companion constant-kernel case.

```text
left_opposite_sections_not_bijective
```

means that some opposite column `x -> beta_{a,b,x}(y)` is not a bijection.

The visible subreasons:

```text
left_opposite_proper_kernel_visible
left_opposite_injective_non_surjective
```

are already routed to the existing proper-kernel or injective-nonsurjective
readout splits.  The reason

```text
left_row_product_collapse
```

marks a row already caught by product triangular collapse.  The only
non-product, non-readout row type that the ledger cannot close by itself is:

```text
left_opposite_hidden_nonunit_unclassified.
```

This is the finite row where the constant map and companion sections are
bijective, the opposite columns are not bijective, and the nonunit defect is
not yet a proper kernel, an injective-nonsurjective column, or product
collapse.

The side-dual reasons identify whether the same colour pair has a right
triangular substitute:

```text
side_dual_right_latin_available
side_dual_right_triangular_nonlatin
no_side_dual_right_latin_replacement.
```

The first side-dual state is closed for genuine coloured-YBE data by the
side-opposite Latin YBE consistency and right-rack diagonal cancellation
notes.  The second and third states are not independent left defects; they
point to the right-side finite row ledgers recorded in
`proofs/triangular_k_left_side_dual_replacement_ledger.md`.

The `active_*` ledgers are the same finite rows after deleting pairs already
routed by product collapse, proper-kernel visibility,
injective-nonsurjective visibility, side-dual Latin availability, and
side-dual pointer labels.  A side-dual triangular-but-non-Latin row is live
through its opposite-side active defect rows; a missing side-dual triangular
replacement is live through the opposite-side missing-row profile.  The active
ledgers are only populated in the actual kink-completion status:

```text
triangular_recovery_kink_completion_deficit.
```

The companion note `proofs/triangular_k_left_kernel_closure.md` further
audits every actual kernel edge inside these non-Latin triangular rows.  A
proper generated closure contradicts local minimality; a universal generated
closure is the exact seed edge that still needs fixed detector routing.

The companion note `proofs/triangular_k_left_structural_independence.md`
separates independent defects from defects forced by bijectivity of a
triangular row.  In particular, constant-map nonsurjectivity, companion
kernel defects, companion nonsurjectivity without a constant-map kernel, and
hidden opposite nonunits without product collapse are inconsistent row
certificates rather than live K-left branches.

The companion note `proofs/triangular_k_left_missing_row_profile.md` splits
the raw `no_left_triangular_row` reason into coordinate-side unit,
proper-kernel visible, injective-nonsurjective, partial-constant hidden, and
nonconstant-hidden profile rows.  Its partial-constant rows are exactly
mixed-unit context-recovery rows on the missing coordinate side.

The companion note
`proofs/triangular_k_left_side_dual_replacement_ledger.md` splits the
side-dual replacement phrases into right-side defect ledgers:
right Latin available, right triangular but non-Latin, or no right triangular
replacement with a missing-row profile.

## Exact K-left residue

[Proved relative to the recorded row reductions] A live K-left survivor must
have at least one row in `missing_left_latin_row_defects` and cannot have its
survival explained solely by any of:

```text
left_row_product_collapse
left_opposite_proper_kernel_visible
left_opposite_injective_non_surjective
side_dual_right_latin_available.
```

Therefore the remaining K-left finite system is exactly:

```text
Find or rule out a local-minimal bi_free_universal_corridor_bottleneck
interval with a colour pair (a,b) such that:

1. triangular recovery is verified;
2. no earlier status closes the pair as product collapse, structural
   inconsistency, kink/YBE inconsistency, or side-dual Latin completion;
3. the pair appears in `active_missing_left_latin_row_defects` with one of:

   no_left_triangular_row;
   left_constant_map_proper_kernel;
   left_constant_map_universal_kernel;
   left_companion_sections_injective_non_surjective tied to such a
   constant-map kernel.
```

This is now an explicit finite algebraic system on the tables of
`R_C` and `T`.  Closing it on the A side means proving that every listed live
row reason either yields a fixed readout/detector or routes onward to the
fixed triangular recovery unit endpoint.  The structural labels
`left_constant_map_not_surjective`, `left_companion_sections_proper_kernel`,
`left_companion_sections_constant`, and
`left_opposite_hidden_nonunit_unclassified` remain in the raw
`missing_left_latin_row_defects` ledger, but they are not active K rows: they
are closed earlier by `triangular_structural_inconsistency`.  Side-dual
non-Latin or missing-replacement rows are still recorded, but only as
pointers to the right-side finite systems.  Turning the residue into B means
constructing one actual live left/right row defect and upgrading its finite
miss to a normalized-law sequence invisible to every finite group.

The kernel labels in the raw and active lists are now literal kernel labels.
Singleton domain maps do not contribute `*_universal_kernel` or
`*_companion_sections_constant`; their only possible non-bijective profile is
the codomain/block-image label already routed by the appropriate structural
or recovery-table ledger.

The companion block-image case is therefore not an independent fourth active
mechanism.  The audit records
`active_companion_block_image_support_rows`, and each row must name a
same-side constant-map proper or universal kernel reason.  Without that
support, the companion injective-nonsurjective profile is closed earlier by
the structural inconsistency ledger.
When the recovery table separates the supported kernel edge, the row is
listed in `recovery_routed_k_missing_latin_row_defects`.  If that exhausts
the active K ledger, the remaining finite system is System U, not a closed
K branch.

## Relation to System U

If every K-left defect is externally routed to fixed detector data, the
remaining problem is System U: prove that the triangular recovery endpoint
word lies in the fixed longitude subgroup `V_beta(U_tri)`, or extract a
stable perfect-residual miss in `P_tri`.

Without such a routing certificate, K-left is not System U.  It is the finite
row-completion problem displayed above.
