# Triangular K-left structural independence

Date: 2026-05-31

This note refines the K-left ledgers by separating independent finite
defects from defects forced by the bijectivity of one triangular row.  It
does not prove `[Resolution: A]` or construct `[Resolution: B]`.

## Setup

Let one left triangular row be

```text
T_{a,b}(x,y) = (alpha(x), beta_x(y))
```

as a bijection

```text
A_a x A_b -> A_c x A_d.
```

The side-dual right triangular case is identical with left and right
interchanged.

## Forced row structure

[Proved] The constant map `alpha:A_a -> A_c` is surjective.

Proof.  For any `u in A_c` and any `v in A_d`, surjectivity of `T` gives
`x,y` with `T(x,y)=(u,v)`.  Then `alpha(x)=u`.  QED.

[Proved] Every companion section `beta_x:A_b -> A_d` is injective.

Proof.  If `beta_x(y0)=beta_x(y1)`, then

```text
T(x,y0)=T(x,y1).
```

Injectivity of `T` forces `y0=y1`.  QED.

[Proved] If `alpha` is bijective, then every companion section is bijective.

Proof.  Since `alpha` is bijective, the source slice `{x} x A_b` maps into
the target slice `{alpha(x)} x A_d`, and no other source slice maps there.
Bijectivity of `T` therefore makes

```text
beta_x:A_b -> A_d
```

a bijection.  QED.

Consequently, companion-section nonsurjectivity is not an independent
no-kernel K-left defect.  It can occur only when `alpha` has a nontrivial
kernel fibre.  Those constant-map kernel edges are precisely the edges
audited in `proofs/triangular_k_left_kernel_closure.md`.

## Hidden opposite columns

[Proved] If `alpha` and all companion sections are bijective, and one
opposite column

```text
C_y(x)=beta_x(y)
```

is a hidden nonunit column, then the row is product triangular.

Proof.  A hidden nonunit column has no proper kernel and is not
injective-nonsurjective.  Since it is nonbijective, it is noninjective; with no
proper kernel, its kernel is universal, so it is constant.  Say
`C_y0(x)=q` for all `x`.

For fixed `x`, `beta_x` is bijective.  Hence for every `y != y0`,
`beta_x(y) != q`.  Thus every other column `C_y` misses `q`, so it is not
surjective.  Under the hidden-nonunit hypothesis it cannot be
injective-nonsurjective and cannot have a proper kernel, hence every `C_y` is
constant.  Therefore

```text
T(x,y) = (alpha(x), gamma(y))
```

for a bijection `gamma`, so the row is product triangular.  QED.

## Executable rows

The triangular column audit now exposes:

```text
constant_map_non_surjective_rows
companion_kernel_rows
companion_nonbijective_without_constant_kernel_rows
hidden_nonunit_opposite_without_product_rows
```

For genuine bijective local intervals, the structural lemmas force these rows
to be empty.  If one appears in supplied finite data, it is an inconsistent
row certificate rather than a live K-left obstruction.  The nonlinear
refinement now records this closed state as:

```text
triangular_structural_inconsistency.
```

## Updated K-left residue

After this structural split, a live K-left row can no longer be justified by
any of:

```text
left_constant_map_not_surjective
left_companion_sections_proper_kernel
left_companion_sections_constant
left_companion_sections_injective_non_surjective without a constant-map kernel
left_opposite_hidden_nonunit_unclassified without product collapse.
```

The companion-constant label is kernel-local in the executable ledger: a
one-point companion section is treated as an injective-nonsurjective
block-image profile, not as a constant-kernel profile.
The active K ledger is now status-faithful, so these structural labels remain
available as raw diagnostics but are erased from
`active_missing_left_latin_row_defects` once
`triangular_structural_inconsistency` fires.
The remaining companion injective-nonsurjective active label is supported:
`active_companion_block_image_support_rows` records the same-side
constant-map kernel reason carrying it.  If no such support exists, this note
classifies the row as structural instead.

Thus the independent K-left finite work is reduced to:

```text
1. no left triangular row exists for a required colour pair;
2. a constant-map kernel edge forces universal closure and must be routed by
   fixed detector data;
3. no side-dual right Latin replacement is available, or the replacement is
   triangular but non-Latin and must be subjected to the same structural and
   kernel-closure ledger.
```

The downstream System U endpoint problem is unchanged.
