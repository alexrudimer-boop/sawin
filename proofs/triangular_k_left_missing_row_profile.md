# Triangular K-left missing-row profile

Date: 2026-05-31

This note refines the remaining no-left-triangular part of System K.  It does
not prove `[Resolution: A]` or construct `[Resolution: B]`.  It replaces the
single reason

```text
no_left_triangular_row
```

by a finite coordinate-section profile.

## Executable object

The helper

```text
missing_triangular_row_profile_audit(I)
```

records every colour pair and side for which no constant-section triangular
row exists.  For such a side it stores the coordinate-section rank profiles
and one explanation:

```text
proper_section_kernel_visible
injective_non_surjective_section
coordinate_side_unit_not_triangular
partial_constant_hidden_rank_loss
nonconstant_hidden_rank_loss
unclassified_missing_triangular_profile
```

The post-linear finite-system wrapper reports the profiles relevant to the
missing left/right Latin rows:

```text
missing_triangular_row_profiles
missing_triangular_duplicate_profile_keys
missing_triangular_duplicate_section_profile_inputs
missing_triangular_mismatched_section_profile_rows
missing_triangular_partial_constant_rows
missing_triangular_partial_constant_mixed_unit_rows
missing_triangular_nonconstant_hidden_rows
```

It also uses the supplied profile ledgers to refine the active K tuple.  A raw
`no_left_triangular_row` or `no_right_triangular_row` remains live if this
profile audit is absent.  The profile ledger is keyed by
`(side,left_color,right_color)` and must be duplicate-free.  If two profile
rows share that key, even with different section-profile payloads or
explanations, the wrapper treats the profile ledger as ambiguous and leaves
the raw K row live.  Each profile row's internal section-profile ledger must
also be exact: every section row must match the parent side and colour pair,
and fixed inputs may not be duplicated.  A duplicated fixed input or
mismatched section row makes the profile explanation
`unclassified_missing_triangular_profile`, so it cannot be used to close or
route the K row.  When the duplicate-free profile audit and the relevant
route audit are supplied, the row is removed from
`live_k_missing_latin_row_defects` if it falls into one of the routed or
closed cases listed below.

## Meaning

For a would-be left triangular row, inspect the maps

```text
L_x^{a,b}: y |-> pr_1 T_{a,b}(x,y).
```

The row is left triangular exactly when every `L_x^{a,b}` is constant.  If it
is not, the profile explains why.

If a proper section kernel appears, the row is already visible to the
proper-kernel readout.  If an injective-nonsurjective section appears, the row
has a size/codomain miss but no input collision in that section.  If every
section is bijective, the side is locally unit and the obstruction cannot be a
hidden rank-loss on that side.

After the rank-profile collapse, the only hidden nonunit sections allowed are
constant.  Therefore a genuine hidden no-left-triangular row has the finite
shape:

```text
some sections are constant,
some sections are not constant,
and no proper-kernel or injective-nonsurjective route applies.
```

This is the `partial_constant_hidden_rank_loss` row.

## Partial-constant means mixed unit

[Proved] In the post-linear rank-profile branch, a
`partial_constant_hidden_rank_loss` row is exactly a mixed-unit context row on
that coordinate side.

Proof.  Proper kernels and injective-nonsurjective sections have already been
removed from the hidden rank-loss branch.  Hence every nonunit section left in
the profile has universal kernel and is constant.  Since the row is not
triangular, not all sections are constant.  The remaining nonconstant
sections are therefore units, i.e. bijective coordinate sections.  Thus the
profile has both unit sections and nonunit constant sections.  This is exactly
the mixed-unit context-recovery shape recorded in
`proofs/two_sided_unit_collapse.md` and
`proofs/mixed_unit_companion_separation.md`.  QED.

## Consequence for K-left

The no-left-triangular residue is now split into:

```text
proper_section_kernel_visible:
  routed out by existing readouts;

injective_non_surjective_section:
  closed by `proofs/triangular_k_left_rack_cardinality_closure.md` in the
  genuine left-rack-base branch: the relevant finite section domains and
  codomains have equal cardinality, so injective implies surjective;

coordinate_side_unit_not_triangular:
  routed by `proofs/triangular_k_left_coordinate_unit_routing.md`: if all
  pairs are two-sided unit, the locally nondegenerate/guitar branch applies;
  a two-sided unit row without that global branch certificate remains live;
  otherwise the row is mixed-unit context when the opposite side carries
  nonunit data;

partial_constant_hidden_rank_loss:
  refined by `proofs/triangular_k_left_partial_constant_closure.md`: the
  constant nonunit sections give explicit kernel seed edges; proper generated
  closures contradict local minimality, while universal generated closures are
  routed by
  `proofs/triangular_k_left_partial_constant_continuation_route.md` into the
  continuation/descent seed channel;

nonconstant_hidden_rank_loss:
  inconsistent with the finite rank-profile classification; after removing
  proper kernels and injective-nonsurjective sections, every hidden nonunit
  section has universal kernel and is constant;

unclassified_missing_triangular_profile:
  empty by the same finite-map trichotomy recorded in
  `proofs/triangular_k_left_rack_cardinality_closure.md`.
```

Thus the remaining independent K-left work is narrower again:
partial-constant hidden profiles no longer create a separate endpoint system;
they feed into the same universal continuation seed closures that the
descent-endpoint repair theorem must handle.

In the executable wrapper this means that a no-triangular-row defect is live
only until its profile has been identified by a duplicate-free profile ledger
with exact section rows and routed.  Proper-kernel visible profiles are
removed immediately; coordinate-unit profiles are removed when
`missing_triangular_coordinate_unit_routing_audit` has either routed the pair
to mixed context or proved the global locally-nondegenerate branch for a
two-sided unit pair; partial-constant profiles are removed when their proper
closures or continuation routes have been verified; and the finite
cardinality/profile closure removes injective-nonsurjective,
nonconstant-hidden, and unclassified profile rows when its proof flag is true
and the profile ledger is duplicate-free with exact section rows.
When a partial-constant row is removed by a continuation route, the wrapper
keeps the downstream burden in
`continuation_routed_k_missing_latin_row_defects` and reports
`system_c_universal_continuation_endpoint` if no live K row remains.
When a coordinate-unit row is removed by a mixed-unit-context route, the
wrapper keeps that downstream burden in
`mixed_context_routed_k_missing_latin_row_defects` and reports
`system_m_mixed_unit_context_endpoint` if no live K row remains.
