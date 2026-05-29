# Detector Product Groups

Date: 2026-05-28

The sharp obstruction theorem asks for one finite group `G`, but the
reduction program naturally produces several finite detector factors:
cyclic pairwise-linking groups, affine or semidirect factors, product-label
groups, symmetric Green kernel-block groups, Schutzenberger groups, and
known-branch factors.  This note records the harmless but necessary
combination step.

## Construction

For finite groups

```text
G_1, ..., G_r,
```

set

```text
G = G_1 x ... x G_r.
```

The implementation is

```text
direct_product_group((G_1,...,G_r))
```

in `src/ybe_domination/finite_group.py`.  The empty product is the trivial
one-element group.  Since every factor is finite and built from the interval
data, the product is finite and still independent of braid degree `n`.

## Longitude Equivalence

For every braid degree `n`, every braid `beta in B_n`, and every recursive
Artin longitude `L_i(beta)`, evaluation in the direct product is coordinate
evaluation:

```text
phi(L_i(beta)) = (phi_1(L_i(beta)), ..., phi_r(L_i(beta)))
```

where `phi_j:F_n -> G_j` is the projection of the assignment
`phi:F_n -> G`.

Therefore

```text
Lambda_{G,n}(beta)=Lambda_{G,n}(1)
```

if and only if

```text
Lambda_{G_j,n}(beta)=Lambda_{G_j,n}(1)
```

for every factor `G_j`.

Indeed, an assignment into `G` is the same thing as a tuple of assignments
into the factors, and an element of `G` is identity exactly when all of its
coordinates are identity.  The braid permutation part of `Lambda` is shared
by all factors.

The subgroup version is functorial as well, as recorded in
`proofs/longitude_subgroup_functoriality.md`: projection
`G -> G_j` sends `V_beta(G)` onto `V_beta(G_j)`.  Thus labels proved to lie
in a longitude-value subgroup before projecting to a detector factor remain
controlled after projection.

The direct-product subgroup is actually exact, as recorded in
`proofs/longitude_subgroup_products.md`:

```text
V_beta(G_1 x ... x G_r)
  =
V_beta(G_1) x ... x V_beta(G_r).
```

Thus factorwise longitude-subgroup membership combines into membership in
the single product detector group.

The detector rack action itself also projects factorwise, as recorded in
`proofs/detector_action_products.md`.  The active coordinates of
`A_{G_1 x ... x G_r}` are tuples of the active coordinates for the individual
`A_{G_j}` actions.  Therefore readouts through factor detector actions can be
combined into one readout through the product detector action.

## Use in the Congruence Chain

If an interval proof supplies finitely many branch tests of the form

```text
Lambda_{G_j,n}(beta)=Lambda_{G_j,n}(1)  =>  residual branch j is trivial,
```

then the single group

```text
G = product_j G_j
```

simultaneously enforces all of them.  The detector rack used in the sharp
obstruction theorem is then the single finite rack `A_G`, not a family of
racks and not an `n`-dependent object.

This also applies inside the congruence-chain induction.  At one local
interval, all local detector factors can first be multiplied into one
`G_i`; then the rack step remains

```text
Q_i = Q_{i+1} x A_{G_i}.
```

## Verification

Unit tests check the construction against cyclic factors `C_2` and `C_3`.
For the standard two-strand pure braid generator, the sixth power is invisible
to both factors and to `C_2 x C_3`, while the square is invisible to `C_2`
but not to `C_3` nor the product.  This is a finite sanity check of the
implemented convention; the proof above is the all-`n` reason the construction
is valid.
The helper `direct_product_longitude_subgroup_audit()` additionally checks the
subgroup equality above on the same cyclic factors and on the empty product.
The helper `direct_product_detector_action_audit()` checks the corresponding
action-level projection for explicit detector states.
The helper `exact_detector_product_readout_audit()` checks the fixed-index
readout analogue: a list of factor readout tables agrees with the table for
the single direct-product detector whenever the product group is small enough
to enumerate.
