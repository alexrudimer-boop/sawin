# Linear F2 audit

## Purpose

This audit enumerates all linear bijective set-theoretic YBE maps on
`F_2^2 x F_2^2`.  Each table has the form

```text
R(x,y) = (A x + B y, C x + D y),
```

where the `4 x 4` block matrix over `F_2` is invertible.  This is the complete
four-point affine-linear universe over `F_2` without translations.  It is a
candidate search only, not global proof evidence.

## Results

```text
matrices checked: 65536
invertible matrices: 20160
linear YBE tables: 97
unknown primitive examples: 0
two-strand Sym period: 24
two-strand Sym-gate bad rows: 0
crossing-order histogram: {1:1, 2:42, 3:12, 4:36, 6:6}
gate explanation counts:
  involutive_order_two: 42
  nondegenerate_derived_rack_branch: 34
  permutation_form_twist_order_2: 3
  permutation_form_twist_order_3: 4
  rack_inner_group_branch: 13
  trivial_crossing_action: 1
```

Two-sided retraction branches among the `97` linear YBE tables:

```text
equality/two-sided-retraction-free:
  1  involutive identity-table
  6  involutive nondegenerate
  12 involutive
  10 nondegenerate
  2  rack-type nondegenerate

proper mixed:
  6  involutive nondegenerate
  12 involutive
  24 nondegenerate
  6  rack-type nondegenerate

universal:
  18 product-permutation witnesses
```

Thus the smallest affine-linear `F_2` universe contains no
two-sided-retraction-free degenerate local obstruction outside the known
measurable branches.  Mixed two-sided-retraction cases are not local-minimal
candidates; universal cases have the product-permutation witness.

## Consequence

The audit reinforces the branch split already observed in whole-solution and
two-colour/fibre-2 scans.  A counterexample, if it exists, must escape this
linear `F_2^2` family as well as the product-permutation and known
nondegenerate/involutive branches.
