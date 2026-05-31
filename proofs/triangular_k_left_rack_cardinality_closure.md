# Triangular K-left rack cardinality closure

Date: 2026-05-31

This note closes the `injective_non_surjective_section` and
`unclassified_missing_triangular_profile` lines in
`proofs/triangular_k_left_missing_row_profile.md` for genuine left-rack-base
local intervals.  It is a finite symbolic argument, not a search.

## Executable object

The helper

```text
missing_triangular_left_rack_cardinality_audit(I)
```

records:

```text
base_rows_are_left_rack_form
all_section_domains_match_codomain
injective_non_surjective_rows
injective_non_surjective_rows_eliminated
nonconstant_hidden_rows
unclassified_rows
proves_left_rack_missing_triangular_cardinality_closure
```

The post-linear finite-system wrapper reports:

```text
missing_triangular_left_rack_section_cardinality_failures
missing_triangular_injective_non_surjective_rows
missing_triangular_profile_unclassified_rows
missing_triangular_left_rack_cardinality_proved
```

## Lemma 1: left-rack base gives equal section cardinalities

[Proved] Let a local interval have base row

```text
R_C(a,b) = (a*b, a).
```

Since the local row

```text
T_{a,b}: A_a x A_b -> A_{a*b} x A_a
```

is a bijection and fibres are nonempty finite sets,

```text
|A_a| |A_b| = |A_{a*b}| |A_a|,
```

so

```text
|A_b| = |A_{a*b}|.
```

Thus every left coordinate section

```text
y |-> pr_1 T_{a,b}(x,y): A_b -> A_{a*b}
```

has equal finite domain and codomain.  Every right coordinate section

```text
x |-> pr_2 T_{a,b}(x,y): A_a -> A_a
```

also has equal finite domain and codomain directly from the rack-form second
colour.  QED.

## Lemma 2: injective-nonsurjective sections cannot survive

[Proved] In the same left-rack-base setting, no missing triangular coordinate
section can be injective but nonsurjective.

Proof.  By Lemma 1, the relevant coordinate section is a map between finite
sets of the same cardinality.  Any injective map between equal-size finite
sets is surjective.  Therefore `injective_non_surjective_section` is a
cardinality contradiction, not a live K-left branch.  QED.

## Lemma 3: the finite profile split is exhaustive

[Proved] For a finite coordinate section, a nonbijective map has one of the
following kernel/rank forms:

```text
proper nontrivial kernel,
equality kernel but nonsurjective,
universal kernel.
```

The universal-kernel case is constant.  Therefore, once the profile is not
already triangular and the proper-kernel and injective-nonsurjective cases
are removed, every hidden nonunit section is constant.  Hence the only hidden
rank-loss profile is the partial-constant mixed-unit profile; the
`nonconstant_hidden_rank_loss` and
`unclassified_missing_triangular_profile` buckets are empty for finite maps.
QED.

## Consequence for K-left

In the genuine post-linear left-rack-base K-left branch, the raw
no-triangular profile list is now reduced to:

```text
proper_section_kernel_visible
coordinate_side_unit_not_triangular
partial_constant_hidden_rank_loss
```

The first is routed to existing proper-kernel readouts.  The second is routed
by `proofs/triangular_k_left_coordinate_unit_routing.md`.  The third is routed
by `proofs/triangular_k_left_partial_constant_closure.md` and
`proofs/triangular_k_left_partial_constant_continuation_route.md` into the
universal-continuation endpoint ledger.

Thus missing triangular rows no longer contribute an independent
injective-nonsurjective, nonconstant-hidden, or unclassified K-left subsystem.
