# Longitude subgroup products

Date: 2026-05-29

This note strengthens the detector-product bookkeeping.  It is not the
Master Local-Minimal Residual Theorem, but it proves that the
longitude-value subgroup criterion composes exactly under finite direct
products of detector groups.

## Statement

Let

```text
G = G_1 x ... x G_r
```

be a finite direct product.  For a braid `beta in B_n`, set

```text
V_beta(G) =
  < phi(L_i(beta)) : phi:F_n -> G, 1<=i<=n > <= G.
```

Then

```text
V_beta(G_1 x ... x G_r)
  =
V_beta(G_1) x ... x V_beta(G_r).
```

The empty product case gives the trivial one-element subgroup.

## Proof

The projection maps `G -> G_j` are surjective homomorphisms, so
`proofs/longitude_subgroup_functoriality.md` gives

```text
pr_j(V_beta(G)) = V_beta(G_j)
```

for every factor.  This proves that `V_beta(G)` projects onto every factor
subgroup, but the direct equality needs one more elementary observation.

Fix a factor `j` and a generator

```text
v = phi_j(L_i(beta)) in V_beta(G_j).
```

Choose the assignment `F_n -> G` whose `j`-th component is `phi_j` and whose
other components are the all-identity assignments.  The same longitude value
in `G` is

```text
(1,...,1,v,1,...,1).
```

Thus every embedded factor generator lies in `V_beta(G)`.  Since these
embedded generators for all factors generate the full Cartesian product
`prod_j V_beta(G_j)`, we get

```text
prod_j V_beta(G_j) <= V_beta(G).
```

The reverse containment is immediate from coordinatewise evaluation: every
longitude value in `G` has `j`-th coordinate in `V_beta(G_j)`, so every
generator of `V_beta(G)` lies in the Cartesian product of the factor
subgroups.  Hence equality holds.

## Consequence

If a local interval has several fixed finite detector factors

```text
G_1,...,G_r,
```

the single detector group

```text
G = product_j G_j
```

does not merely have the same identity-longitude kernel as the factors.  Its
longitude-value subgroup is exactly the product of the factor
longitude-value subgroups.  Therefore a residual label tuple

```text
(h_1(beta),...,h_r(beta))
```

lies in `V_beta(G)` whenever each coordinate label satisfies

```text
h_j(beta) in V_beta(G_j).
```

This is the algebraic step needed when product-label, normalized holonomy,
unit-holonomy, Green kernel-block, Schutzenberger, quotient, and known-branch
detectors are multiplied into one `G_i` for a local interval.  It keeps the
resulting rack `A_{G_i}` finite and independent of `n`.

## Executable Certificate

The helper

```text
direct_product_longitude_subgroup_audit(groups,n,beta)
direct_product_longitude_subgroup_witness(groups,n,factor_witnesses)
direct_product_longitude_subgroup_witness_audit(groups,n,beta,factor_witnesses)
```

computes `V_beta(product_i G_i)`, the factor subgroups `V_beta(G_i)`, and
checks exact equality with their Cartesian product.  Regression tests cover
`C_2 x C_3` for the two-strand pure generator and its sixth power, plus the
empty direct product.

The witness helpers give the non-enumerative certificate form of the product
lemma.  Given one explicit longitude subgroup witness in each factor, they
embed each factor witness into the product by identity assignments in all
other coordinates and concatenate the embedded words.  The audit verifies
that the product witness evaluates to the tuple of the factor witness values.
Thus product endpoint certificates can be assembled in the single detector
group required by the sharp obstruction theorem without first enumerating
`V_beta(product_i G_i)`.
