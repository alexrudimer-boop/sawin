# Unit-continuation derived product detector

Date: 2026-05-30

This note follows the abelian quotient, derived-series, and perfect-residual
unit-continuation notes.  It does not prove the terminal unit theorem.  It
records the product assembly step for supplied derived-series endpoint
certificates.

## Setup

Let `M_1,...,M_r` be fixed finite endpoint or continuation transition monoids
attached to one local interval, and let

```text
U_i = U(M_i)
```

be their unit groups.  For a residual braid `beta`, suppose each terminal
unit endpoint

```text
S_i(beta) in U_i
```

has a derived-series lift certificate:

1. lifted abelian quotient witnesses through the derived series of `U_i`;
2. a final witness in the stable perfect residual of `U_i`;
3. a combined witness evaluating to `S_i(beta)` in `U_i`.

Then the endpoint tuple

```text
(S_1(beta),...,S_r(beta))
```

lies in

```text
V_beta(U_1 x ... x U_r).
```

## Proof

For each factor, the derived-series lift certificate supplies a literal
subgroup witness

```text
W_i(beta)
```

whose letters are recursive-longitude values in `U_i` and whose value is
`S_i(beta)`.

Embed the letters of `W_i(beta)` into the `i`-th coordinate of the direct
product, using identity assignments in all other coordinates.  Multiplying
these embedded witnesses over all `i` gives a literal word in generators of

```text
V_beta(U_1 x ... x U_r)
```

with value `(S_1(beta),...,S_r(beta))`.  This is the same
direct-product witness calculus as `proofs/longitude_subgroup_products.md`.
No enumeration of the product subgroup is required.  QED.

## Consequence

Identity finite-longitude data in the single fixed product group

```text
U_1 x ... x U_r
```

kills every supplied terminal unit endpoint at once.  Therefore a terminal
unit proof may split each endpoint into derived abelian quotients and perfect
residuals factorwise, but the sharp obstruction theorem still receives one
finite detector group independent of braid index.

## Executable audit

The helper

```text
unit_composite_product_derived_series_lift_audit(
    monoids,n,beta,factor_words,stage_lifted_witnesses,final_witnesses
)
```

constructs the factor audits with
`unit_composite_derived_series_lift_audit(...)`, assembles their combined
witnesses by `direct_product_longitude_subgroup_witness(...)`, and checks the
result in the direct product group.

Its flag

```text
proves_product_endpoint_detector_by_derived_lift
```

is true exactly when the supplied factor certificates prove the product
endpoint lies in the single product longitude-value subgroup.

This remains a supplied-certificate audit.  The all-`n` Green/corridor proof
must still construct the factor certificates uniformly for every residual
braid action, or a B route must upgrade the first genuine failure to a
normalized-law obstruction.
