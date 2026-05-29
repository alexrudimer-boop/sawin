# Detector action products

Date: 2026-05-29

This note records the action-level version of the detector-product
construction.  It complements `proofs/detector_product_groups.md` and
`proofs/longitude_subgroup_products.md`.

## Statement

Let

```text
G = G_1 x ... x G_r
```

be a finite direct product.  The active coordinates of the sharp detector
rack

```text
A_G = T_2 x (G x G)
```

project to the active coordinates of each factor detector `A_{G_j}`.  More
concretely, for an assignment

```text
g_i = (g_{i,1},...,g_{i,r}) in G,
```

the detector state

```text
rho_{A_G,n}(beta)((g_i,1_G)_i)
```

has first active coordinate equal to the tuple of the factor Artin image
values, and second active coordinate equal to the tuple of the factor
recursive-longitude values:

```text
image_G(i)      = (image_{G_1}(i),...,image_{G_r}(i)),
longitude_G(i)  = (longitude_{G_1}(i),...,longitude_{G_r}(i)).
```

The `T_2` factor is shared and still records the Artin strand permutation.

## Proof

The rack operation in `A_G` is

```text
(a,u) triangleright (b,v) = (a b a^{-1}, a v).
```

In a direct product group, multiplication, inverse, and conjugation are all
coordinatewise:

```text
(a_j)_j (b_j)_j (a_j)_j^{-1}
  =
(a_j b_j a_j^{-1})_j,

(a_j)_j (v_j)_j
  =
(a_j v_j)_j.
```

Therefore one positive or negative braid generator acts on `A_G^n` as the
coordinatewise product of its actions on the `A_{G_j}^n` active coordinates,
with the same `T_2` strand swap.  Induction on the braid word gives the
displayed statement for every braid.

## Readout Consequence

Suppose a local interval has several residual readouts, each factoring
through a fixed detector action `A_{G_j}`.  Then their combined readout
factors through the single fixed product detector action `A_G` by projecting
the active `G`-coordinates to the factors and applying the old readouts.

Thus the action-factor criterion in
`proofs/fixed_detector_action_factorization.md` is stable under multiplying
detector factors.  A proof may construct product-label, normalized holonomy,
unit-holonomy, Green kernel-block, Schutzenberger, quotient, and known-branch
readouts separately, then combine them into one finite group `G_i` for the
local interval.  The detector rack remains `A_{G_i}` and is independent of
the braid index.

## Executable Certificate

The helper

```text
direct_product_detector_action_audit(groups,factor_assignments,beta)
```

forms the product assignment, applies `detector_rack_state()` to the product
group, applies `detector_rack_state()` to each factor, and checks that the
active product image and longitude coordinates project to the factor states.
Regression tests cover `C_2 x C_3` on a nontrivial three-strand braid word
and basic argument validation.

The fixed-index readout-level helper

```text
exact_detector_product_readout_audit(qmap,Q,groups,n)
```

compares the residual-fibre readout table obtained from the displayed factor
list with the readout table obtained from the single product detector group
`prod_i G_i`, when that product is small enough to enumerate.  This is still
a fixed-degree audit, but it locks the convention needed by the sharp
obstruction theorem: separate branch readouts are evidence for one product
detector, not for an illicit family of detectors.
